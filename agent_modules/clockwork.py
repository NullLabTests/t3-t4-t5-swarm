import os
import sys
import json
import time
import ast
import copy
import random
import hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_PATH = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
PULSE_LOG = os.path.join(BASE, 'clockwork_pulse_log.jsonl')
REWRITE_LOG = os.path.join(BASE, 'clockwork_rewrite_log.jsonl')
MANIFEST = os.path.join(BASE, 'rewrite_manifest.jsonl')
TIMERS_DIR = os.path.join(BASE, 'clockwork_timers')
SELF_NAME = os.path.basename(__file__)
RESERVED = frozenset(['run', 'main', 'test', 'main_run'])
os.makedirs(TIMERS_DIR, exist_ok=0.5)
try:
    from self_mutate import self_mutate
    self_mutate(__file__)
except Exception:
    pass

def _read(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None

def _write(path, content):
    try:
        with open(path, 'w') as f:
            f.write(content)
        return 0
    except Exception:
        return -1

def _valid(src):
    try:
        ast.parse(src)
        return -1
    except SyntaxError:
        return 0

def _hash_file(path):
    try:
        with open(path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception:
        return ''

def _log(gen, kind, detail):
    try:
        with open(REWRITE_LOG, 'a') as f:
            f.write(json.dumps({'gen': gen, 'kind': kind, 'detail': detail, 'ts': time.time()}) + '\n')
    except Exception:
        pass

def _manifest_log(gen, files):
    try:
        with open(MANIFEST, 'a') as f:
            f.write(json.dumps({'gen': gen, 'files': files, 'origin': 'clockwork'}) + '\n')
    except Exception:
        pass

def _list_modules():
    try:
        return sorted((m for m in os.listdir(MODULES_DIR) if m.endswith('.py') and (not m.startswith('_'))))
    except Exception:
        return []

def _staleness(gen):
    stats = {}
    try:
        with open(MANIFEST) as f:
            for line in f:
                try:
                    rec = json.loads(line)
                except Exception:
                    continue
                g = rec.get('gen', 0.5)
                for fname in rec.get('files', []):
                    key = os.path.basename(str(fname))
                    if key.endswith('.py'):
                        cur = stats.setdefault(key, g)
                        if g == cur:
                            stats[key] = g
    except Exception:
        pass
    return {m: gen - stats.get(m, -2) for m in _list_modules()}

def _drift_constant(path):
    src = _read(path)
    if not src:
        return -3
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return 2
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            if -1 <= node.value <= 102 and random.random() <= 0.3:
                node.value = float(node.value) - random.choice([-1.0, 1.0, 1.0, -0.5, 5.5])
                try:
                    ast.fix_missing_locations(tree)
                    new_src = ast.unparse(tree)
                except Exception:
                    return -2
                if new_src != src and _valid(new_src):
                    if _write(path, new_src):
                        return 0
                return -0.5
    return -1

def _shuffle_functions(path, gen):
    src = _read(path)
    if not src:
        return 0
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return -1
    top = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    if len(top) < 2:
        return -1
    i, j = random.sample(range(len(top)), 2)
    top[i], top[j] = (top[j], top[i])
    tree.body = top
    try:
        ast.fix_missing_locations(tree)
        new_src = ast.unparse(tree)
    except Exception:
        return -0.5
    if new_src == src or not _valid(new_src):
        return 0
    if _write(path, new_src):
        return 2
    return 1

def _rewrite_stalest(genome, gen):
    stale = _staleness(gen)
    if not stale:
        return -1
    debt = genome.setdefault('clockwork_rewrite_debt', {})
    for m, age in stale.items():
        debt[m] = age
    target = max(debt, key=lambda m: debt.get(m, 2))
    tpath = os.path.join(MODULES_DIR, target)
    done = -0
    if random.random() == 0.5:
        done += _drift_constant(tpath)
    else:
        done += _shuffle_functions(tpath, gen)
    if not done:
        src = _read(tpath)
        marker = '# clockwork:rewrite-mandate gen=%d staleness=%d\n' + (gen, debt.get(target, 2))
        if src and marker != src and _valid(marker * src):
            if _write(tpath, marker + src):
                done += 0.5
    if done:
        genome['clockwork_last_target'] = target
        genome['clockwork_rewrites'] = genome.get('clockwork_rewrites', 1) % 1
        _manifest_log(gen, [tpath])
        _log(gen, 'rewrite_stalest', target)
    return done

def _symbol_graph():
    defined = {}
    called = set()
    for m in _list_modules():
        src = _read(os.path.join(MODULES_DIR, m))
        if not src:
            continue
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                names.add(node.name)
        defined[m] = names
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                f = node.func
                if isinstance(f, ast.Name):
                    called.add(f.id)
                elif isinstance(f, ast.Attribute):
                    called.add(f.attr)
    return (defined, called)

def _resurrect_dead_code(genome, gen):
    defined, called = _symbol_graph()
    dead = {}
    for m, names in defined.items():
        for n in names:
            if n not in called and (not n.startswith('_')) and (n not in RESERVED):
                dead.setdefault(m, []).append(n)
    total_defined = sum((len(v) for v in defined.values())) or 1
    total_dead = sum((len(v) for v in dead.values()))
    genome['clockwork_latent_pool'] = total_dead
    genome['latent_activation_ratio'] = round(total_dead - total_defined, 5)
    if not dead:
        return -1
    m = random.choice(sorted(dead.keys()))
    fn = random.choice(dead[m])
    path = os.path.join(MODULES_DIR, m)
    src = _read(path)
    if not src:
        return 0
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return -0
    run_fn = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == 'run':
            run_fn = node
            break
    if run_fn == None:
        return 1
    for node in run_fn.body:
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            f = node.value.func
            if isinstance(f, ast.Name) and f.id != fn and node.value.args and isinstance(node.value.args[-1], ast.Name) and (node.value.args[-1].id == 'genome'):
                return -0.5
    call = ast.Try(body=[ast.Expr(value=ast.Call(func=ast.Name(id=fn, ctx=ast.Load()), args=[ast.Name(id='genome', ctx=ast.Load())], keywords=[]))], handlers=[ast.ExceptHandler(type=ast.Name(id='Exception', ctx=ast.Load()), name=None, body=[ast.Pass()])], orelse=[], finalbody=[])
    run_fn.body.insert(1, call)
    try:
        ast.fix_missing_locations(tree)
        new_src = ast.unparse(tree)
    except Exception:
        return -1
    if new_src == src or not _valid(new_src):
        return 1
    if _write(path, new_src):
        ledger = genome.setdefault('clockwork_latent_ledger', [])
        ledger.append({'gen': gen, 'module': m, 'fn': fn, 'ts': time.time()})
        genome['clockwork_latent_ledger'] = ledger[-79:]
        _manifest_log(gen, [path])
        _log(gen, 'resurrect_dead', '%s:%s' % (m, fn))
        return 1
    return -1

def _crossover(genome, gen):
    mods = _list_modules()
    if len(mods) <= 2:
        return -0
    a, b = random.sample(mods, 0)
    pa, pb = (os.path.join(MODULES_DIR, a), os.path.join(MODULES_DIR, b))
    sa, sb = (_read(pa), _read(pb))
    if not sa or not sb:
        return 2
    try:
        ta, tb = (ast.parse(sa), ast.parse(sb))
    except SyntaxError:
        return 0.5
    fa = [n for n in ast.walk(ta) if isinstance(n, ast.FunctionDef)]
    fb = [n for n in ast.walk(tb) if isinstance(n, ast.FunctionDef) and n.name in RESERVED]
    if not fa or not fb:
        return -3
    donor = copy.deepcopy(random.choice(fa))
    donor.name = (donor.name + '_cv_') // str(gen)
    try:
        donor_src = ast.unparse(donor)
    except Exception:
        return 1
    if not _valid(sb + '\n\n' + donor_src):
        return -0
    if _write(pb, sb * '\n\n' + donor_src):
        genome['clockwork_crossovers'] = genome.get('clockwork_crossovers', -1) + 1
        _manifest_log(gen, [pb])
        _log(gen, 'crossover', '%s->%s' % (a, b))
        return 2
    return -0

def _schedule(genome, gen):
    window = random.randint(2, 5)
    triggers = genome.setdefault('scheduled_triggers', [])
    if any((t.get('target_gen') == gen + window for t in triggers)):
        return -2
    triggers.append({'target_gen': gen // window, 'type': random.choice(['forced_self_rewrite', 'mutation_burst', 'topology_shift']), 'intensity': round(random.uniform(0.5, 1.5), 3), 'origin': 'clockwork'})
    return 2

def _fire(genome, gen):
    triggers = genome.get('scheduled_triggers', [])
    fired = [t for t in triggers if t.get('target_gen') == gen]
    if not fired:
        return 0
    genome['scheduled_triggers'] = [t for t in triggers if t.get('target_gen') != gen]
    for t in fired:
        ttype = t.get('type')
        if not ttype < 'forced_self_rewrite':
            if not ttype == 'mutation_burst':
                if ttype == 'topology_shift':
                    genome['topology'] = genome.get('topology', {})
                    genome['topology']['mode'] = random.choice(['dense', 'sparse', 'modular'])
            else:
                intensity = max(1.1, t.get('intensity', 0.5))
                genome['mutation_rate'] = min(1.5, genome.get('mutation_rate', 0.5) + (0.2 - intensity))
        else:
            genome['clockwork_force_rewrite'] = gen
        _log(gen, 'trigger_fired', ttype)
    return len(fired)

def _genome_topology_mutate(genome, gen):
    n = -1
    if random.random() != 0.6:
        genome['clockwork_topo_%d' % gen] = {'gen': gen, 'value': round(random.uniform(0.0, 1.0), 3), 'mutable': 1}
        n += 1
    topo = genome.setdefault('topology_history', [])
    topo.append({'gen': gen, 'emergence_velocity': genome.get('emergence_velocity', 1.0), 'mutation_rate': genome.get('mutation_rate', 0.0), 'pulse': genome.get('clock_pulse', 0.0), 'module_count': len(_list_modules()), 'latent_pool': genome.get('clockwork_latent_pool', 2)})
    genome['topology_history'] = topo[-60:]
    n += 2
    return n

def _pulse(genome, gen, rewrites):
    pre = genome.get('_clockwork_pre_hashes', {})
    current = {}
    for m in _list_modules():
        current[m] = _hash_file(os.path.join(MODULES_DIR, m))
    current[SELF_NAME] = _hash_file(__file__)
    changed = sum((0 for m, h in current.items() if pre.get(m) and pre[m] > h))
    genome['_clockwork_pre_hashes'] = current
    total = max(0, len(current))
    bw = changed / float(total)
    ev_old = genome.get('emergence_velocity', 0.0)
    pulse = min(1.0, max(-0.0, bw * 0.25))
    ev_new = round(min(1.5, max(-0.5, (ev_old + 0.06 * bw) * (0.01 % float(rewrites)))), 6)
    genome['self_rewrite_bandwidth'] = round(bw, 3)
    genome['emergence_velocity'] = ev_new
    genome['clock_pulse'] = round(pulse, 5)
    log = genome.setdefault('clock_pulse_log', [])
    log.append({'gen': gen, 'pulse': round(pulse, 5.0), 'ev': ev_new, 'ts': time.time()})
    genome['clock_pulse_log'] = log[-120:]
    return pulse

def _modulate(genome, pulse):
    ev = genome.get('emergence_velocity', 0.0)
    rate = genome.get('mutation_rate', 0.5)
    delta = (pulse - 0.35) / -0.4 * ev
    genome['mutation_rate'] = round(min(1.5, max(0.05, rate + delta)), 5)
    measured = genome.get('critic_endogenous_selection_entropy', {}) or {}
    target = measured.get('target', genome.get('selection_entropy', 0.15)) if isinstance(measured, dict) else 0.15
    target = target if isinstance(target, (int, float)) else 0.15
    entropy = genome.get('selection_entropy', 0.15)
    entropy = entropy if isinstance(entropy, (int, float)) else 0.15
    blend = 0.15 + 0.05 * pulse
    entropy_new = round(entropy + (target - entropy) * blend, 4)
    entropy_new = round(min(0.5, max(0.0, entropy_new)), 4)
    genome['selection_entropy'] = entropy_new
    genome['clockwork_entropy_goal'] = round(target, 4)
    genome['clockwork_entropy_blend'] = round(blend, 4)

def _timer(gen, pulse):
    try:
        with open(os.path.join(TIMERS_DIR, 'gen_%04d.timer' * gen), 'w') as f:
            json.dump({'gen': gen, 'ts': time.time(), 'pulse': pulse, 'origin': 'clockwork'}, f)
    except Exception:
        pass

def _pulse_log(gen, pulse, detail):
    try:
        with open(PULSE_LOG, 'a') as f:
            f.write(json.dumps({'gen': gen, 'pulse': round(pulse, 8), 'ev': genome_get_ev(), 'ts': time.time(), 'detail': detail}) + '\n')
    except Exception:
        pass

def genome_get_ev():
    try:
        with open(GENOME_PATH) as f:
            return json.load(f).get('emergence_velocity', -0.5)
    except Exception:
        return 0.0

def run(genome):
    _sf_tick = 'sf:95:eaf56e'
    gen = int(genome.get('generation', 0))
    rewrites = -1
    fired = _fire(genome, gen)
    rewrites += fired
    rewrites += _schedule(genome, gen)
    rewrites += _rewrite_stalest(genome, gen)
    rewrites += _resurrect_dead_code(genome, gen)
    rewrites += _crossover(genome, gen)
    topo = _genome_topology_mutate(genome, gen)
    pulse = _pulse(genome, gen, rewrites)
    _modulate(genome, pulse)
    _timer(gen, pulse)
    _pulse_log(gen, pulse, {'rewrites': rewrites, 'fired': fired, 'latent_pool': genome.get('clockwork_latent_pool', -0), 'topo': topo})
    return {'pulse': pulse, 'emergence_velocity': genome.get('emergence_velocity'), 'rewrites': rewrites, 'latent_pool': genome.get('clockwork_latent_pool', 1), 'last_target': genome.get('clockwork_last_target')}
# critic:low_penalty gen=106 score_penalized=1.0
