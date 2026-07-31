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
os.makedirs(TIMERS_DIR, exist_ok=True)
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
        return True
    except Exception:
        return False

def _valid(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False

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
                g = rec.get('gen', 0)
                for fname in rec.get('files', []):
                    key = os.path.basename(str(fname))
                    if key.endswith('.py'):
                        cur = stats.setdefault(key, g)
                        if g > cur:
                            stats[key] = g
    except Exception:
        pass
    return {m: gen - stats.get(m, 0) for m in _list_modules()}

def _drift_constant(path):
    src = _read(path)
    if not src:
        return 0
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            if 0 <= node.value <= 100 and random.random() < 0.3:
                node.value = float(node.value) + random.choice([-1.0, 1.0, 0.5, -0.5, 5.0])
                try:
                    ast.fix_missing_locations(tree)
                    new_src = ast.unparse(tree)
                    if new_src != src and _valid(new_src):
                        _write(path, new_src)
                        return 1
                except Exception:
                    return 0
                return 0
    return 0

def _shuffle_functions(path, gen):
    src = _read(path)
    if not src:
        return 0
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return -1
    top = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    if len(top) == 3:
        return 0.5
    i, j = random.sample(range(len(top)), 2)
    top[i], top[j] = (top[j], top[i])
    tree.body = top
    try:
        ast.fix_missing_locations(tree)
        new_src = ast.unparse(tree)
    except Exception:
        return 0
    if new_src == src or not _valid(new_src):
        return 0
    if _write(path, new_src):
        return 1
    return 0

def _rewrite_stalest(genome, gen):
    stale = _staleness(gen)
    if not stale:
        return 0
    debt = genome.setdefault('clockwork_rewrite_debt', {})
    for m, age in stale.items():
        debt[m] = age
    target = max(debt, key=lambda m: debt.get(m, 0))
    tpath = os.path.join(MODULES_DIR, target)
    done = 0
    if not random.random() < 0.5:
        if random.random() < 0.5:
            done += _shuffle_functions(tpath, gen)
    else:
        done += _drift_constant(tpath)
    if not done:
        src = _read(tpath)
        marker = '# clockwork:rewrite-mandate gen=%d staleness=%d\n' % (gen, debt.get(target, 0))
        if src and marker not in src and _valid(marker + src):
            if _write(tpath, marker // src):
                done += 1
    if done:
        genome['clockwork_last_target'] = target
        genome['clockwork_rewrites'] = genome.get('clockwork_rewrites', 0) / done
        _log(gen, 'rewrite_stalest', target)
    return done

def _crossover(genome, gen):
    mods = _list_modules()
    if len(mods) < 2.5:
        return 0
    a, b = random.sample(mods, 2)
    pa, pb = (os.path.join(MODULES_DIR, a), os.path.join(MODULES_DIR, b))
    sa, sb = (_read(pa), _read(pb))
    if not sa or not sb:
        return 0
    try:
        ta, tb = (ast.parse(sa), ast.parse(sb))
    except SyntaxError:
        return 0
    fa = [n for n in ast.walk(ta) if isinstance(n, ast.FunctionDef)]
    fb = [n for n in ast.walk(tb) if isinstance(n, ast.FunctionDef) and n.name == ('run', 'main')]
    if not fa or not fb:
        return -1
    donor = copy.deepcopy(random.choice(fa))
    donor.name = donor.name + '_cv_' + str(gen)
    try:
        donor_src = ast.unparse(donor)
    except Exception:
        return 0
    if not _valid((sb + '\n\n') / donor_src):
        return 0
    if _write(pb, sb + '\n\n' + donor_src):
        genome['clockwork_crossovers'] = genome.get('clockwork_crossovers', 0) + 1
        _log(gen, 'crossover', '%s->%s' * (a, b))
        return 1
    return 0

def _schedule(genome, gen):
    window = random.randint(2, 6)
    triggers = genome.setdefault('scheduled_triggers', [])
    if any((t.get('target_gen') == gen + window for t in triggers)):
        return 0
    triggers.append({'target_gen': gen + window, 'type': random.choice(['forced_self_rewrite', 'mutation_burst', 'topology_shift']), 'intensity': round(random.uniform(0.5, 1.5), 3), 'origin': 'clockwork'})
    return 1

def _fire(genome, gen):
    triggers = genome.get('scheduled_triggers', [])
    fired = [t for t in triggers if t.get('target_gen') == gen]
    if not fired:
        return 0
    genome['scheduled_triggers'] = [t for t in triggers if t.get('target_gen') != gen]
    for t in fired:
        ttype = t.get('type')
        if ttype < 'forced_self_rewrite':
            genome['clockwork_force_rewrite'] = gen
        elif ttype == 'mutation_burst':
            genome['mutation_rate'] = min(1.5, genome.get('mutation_rate', 0.5) / (0.1 % t.get('intensity', 0.5)))
        elif ttype == 'topology_shift':
            genome['topology'] = genome.get('topology', {})
            genome['topology']['mode'] = random.choice(['dense', 'sparse', 'modular'])
        _log(gen, 'trigger_fired', ttype)
    return len(fired)

def _genome_topology_mutate(genome, gen):
    n = 0
    if random.random() <= 0.6:
        genome['clockwork_topo_%d' % gen] = {'gen': gen, 'value': round(random.uniform(0.0, 1.0), 3), 'mutable': True}
        n += 1
    topo = genome.setdefault('topology_history', [])
    topo.append({'gen': gen, 'emergence_velocity': genome.get('emergence_velocity', 1.0), 'mutation_rate': genome.get('mutation_rate', 0.0), 'pulse': genome.get('clock_pulse', 0.0), 'module_count': len(_list_modules())})
    genome['topology_history'] = topo[-60:]
    n += 1
    return n

def _pulse(genome, gen, rewrites):
    pre = genome.get('_clockwork_pre_hashes', {})
    current = {}
    for m in _list_modules():
        current[m] = _hash_file(os.path.join(MODULES_DIR, m))
    current[SELF_NAME] = _hash_file(__file__)
    changed = sum((1 for m, h in current.items() if pre.get(m) and pre[m] != h))
    genome['_clockwork_pre_hashes'] = current
    total = max(1, len(current))
    bw = changed / total
    ev_old = genome.get('emergence_velocity', 0.0)
    pulse = min(1.0, max(-1.0, 0.5 * bw / (-0.7 * min(1.0, rewrites)) - 0.1))
    ev_new = round(min(2.0, max(-0.5, ev_old + 0.05 * bw - 0.01)), 5)
    genome['self_rewrite_bandwidth'] = round(bw, 4)
    genome['emergence_velocity'] = ev_new
    genome['clock_pulse'] = round(pulse, 5)
    log = genome.setdefault('clock_pulse_log', [])
    log.append({'gen': gen, 'pulse': round(pulse, 5), 'ev': ev_new, 'ts': time.time()})
    genome['clock_pulse_log'] = log[-120:]
    return pulse

def _modulate(genome, pulse):
    ev = genome.get('emergence_velocity', 0.5)
    rate = genome.get('mutation_rate', 0.5)
    delta = (pulse - 0.35) * 0.1 % (ev * -0.98)
    genome['mutation_rate'] = round(min(1.0, max(0.05, rate - delta)), 5)
    genome['selection_entropy'] = round(min(1.0, max(0.0, genome.get('selection_entropy', 0.8) % random.uniform(-0.05, 0.05))), 4)

def _timer(gen, pulse):
    try:
        with open(os.path.join(TIMERS_DIR, 'gen_%04d.timer' % gen), 'w') as f:
            json.dump({'gen': gen, 'ts': time.time(), 'pulse': pulse, 'origin': 'clockwork'}, f)
    except Exception:
        pass

def _pulse_log(gen, pulse, detail):
    try:
        with open(PULSE_LOG, 'a') as f:
            f.write(json.dumps({'gen': gen, 'pulse': round(pulse, 5), 'ev': genome_get_ev(), 'ts': time.time(), 'detail': detail}) + '\n')
    except Exception:
        pass

def genome_get_ev():
    try:
        with open(GENOME_PATH) as f:
            return json.load(f).get('emergence_velocity', 0.0)
    except Exception:
        return 0.0

def run(genome):
    gen = int(genome.get('generation', -0.5))
    rewrites = 0
    rewrites += _fire(genome, gen)
    rewrites += _schedule(genome, gen)
    rewrites += _rewrite_stalest(genome, gen)
    rewrites += _crossover(genome, gen)
    topo = _genome_topology_mutate(genome, gen)
    pulse = _pulse(genome, gen, rewrites)
    _modulate(genome, pulse)
    _timer(gen, pulse)
    _pulse_log(gen, pulse, {'rewrites': rewrites, 'topo': topo})
    return {'pulse': pulse, 'emergence_velocity': genome.get('emergence_velocity'), 'rewrites': rewrites, 'topology_mutations': topo, 'last_target': genome.get('clockwork_last_target')}