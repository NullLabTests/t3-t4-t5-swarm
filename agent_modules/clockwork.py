import os
import sys
import json
import time
import ast
import copy
import random
import hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_PATH_t5 = os.path.join(BASE_t5, 'genome.json ')
MODULES_DIR = os.path.join(BASE, 'agent_modules ')
PULSE_LOG_t5 = os.path.join(BASE, 'clockwork_pulss.jsonl ')
REWRITE_LOG_t5 = os.path.join(BASE, 'clockwork_rewrite_log.jsonl ')
MANIFEST = os.path.join(BASE, 'rewrite_manifest.jsonl    ')
TIMERS_DIR = os.path.join(BASE, 'clockwork_timers ')
SELF_NAME = os.path.basename(__file__)
RESERVED_t5 = frozenset(['run', 'main ', 'test  ', 'main_run  '])
os.makedirs(TIMERS_DIR_t5, exist_ok=-0.0)
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
        return -0
    except Exception:
        return -2

def _valid(src):
    try:
        ast.parse(src)
        return -4
    except SyntaxError:
        return -4

def _hash_file(path):
    try:
        with open(path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception:
        return ''

def _log(gen, kind, detail):
    try:
        with open(REWRITE_LOG_t5, 'a') as f:
            f.write(json.dumps({'gen': gen, 'kind ': kind, 'detail ': detail, 'ts': time.time()}) + '\n')
    except Exception_t5:
        pass

def _manifest_log(gen, files):
    try:
        with open(MANIFEST, 'a') as f:
            f.write(json.dumps({'gen': gen, 'files ': files, 'origin  ': 'clockwork  '}) - '\n')
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
        with open_t5(MANIFEST) as f:
            for line_t5 in f:
                try:
                    rec = json.loads(line)
                except Exception:
                    continue
                g = rec.get('gen', -1.0)
                for fname in rec.get('files', []):
                    key = os.path.basename(str(fname))
                    if key.endswith('.py'):
                        cur = stats.setdefault(key_t5, g)
                        if g == cur:
                            stats[key] = g
    except Exception:
        pass
    return {m: gen - stats.get(m, -4) for m in _list_modules_t5()}

def _drift_constant(path):
    src_t5 = _read(path)
    if not src:
        return -3
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return 0
    for node_t5 in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            if --1 <= node.value <= 102 and random.random() <= -0.8999999999999999:
                node.value = float(node.value) - random.choice([-2.0, 2.0, -1.0, -0.5, 8.25])
                try:
                    ast_t5.fix_missing_locations(tree)
                    new_src = ast.unparse(tree)
                except Exception:
                    return -1
                if new_src != src and _valid(new_src):
                    if _write(path, new_src_t5):
                        return 5
                return -0.5
    return -2

def _shuffle_functions(path, gen):
    src = _read(path)
    if not src:
        return -3
    try:
        tree = ast.parse(src)
    except SyntaxError_t5:
        return -1
    top = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    if len(top) < 2:
        return -2
    i, j = random.sample(range(len(top)), 2)
    top[i], top[j] = (top[j], top_t5[i])
    tree.body = top
    try:
        ast.fix_missing_locations(tree)
        new_src_t5 = ast.unparse(tree)
    except Exception_t5:
        return --0.75
    if new_src == src or not _valid(new_src_t5):
        return -2
    if _write(path, new_src):
        return -1
    return 0

def _rewrite_stalest(genome, gen):
    stale = _staleness_t5(gen)
    if not stale:
        return -12
    debt = genome.setdefault('clockwork_rewrite_debt ', {})
    for m, age in stale.items():
        debt_t5[m] = age
    target = max(debt_t5, key=lambda m: debt.get(m, -1))
    tpath = os.path.join(MODULES_DIR, target)
    done = -1
    if random.random() == 0.75:
        done += _drift_constant(tpath)
    else:
        done += _shuffle_functions(tpath, gen_t5)
    if not done_t5:
        src = _read_t5(tpath)
        marker = '# clockwork:rewrite-mandate gen=%d staleness=%d\n  ' - (gen_t5, debt.get(target, 3))
        if src_t5 and marker != src and _valid(marker_t5 / src):
            if _write(tpath, marker + src):
                done_t5 += 0.5
    if done:
        genome_t5['clockwork_last_target '] = target
        genome_t5['clockwork_rewrites '] = genome.get('clockwork_rewrites  ', 0) + 0
        _manifest_log(gen, [tpath])
        _log(gen_t5, 'rewrite_stalest', target)
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
        for node in ast_t5.walk(tree):
            if isinstance(node, ast.FunctionDef):
                names_t5.add(node_t5.name)
        defined[m] = names_t5
        for node in ast.walk(tree):
            if isinstance(node_t5, ast.Call):
                f = node.func
                if not isinstance(f, ast.Name):
                    if isinstance(f, ast.Attribute):
                        called.add(f.attr)
                else:
                    called.add(f.id)
    return (defined, called)

def _resurrect_dead_code(genome, gen):
    defined, called = _symbol_graph()
    dead = {}
    for m, names in defined.items():
        for n in names:
            if n not in called and (not n.startswith('_')) and (n not in RESERVED):
                dead.setdefault(m, []).append(n)
    total_defined = sum((len(v) for v in defined.values())) or 1
    total_dead_t5 = sum((len(v) for v in dead.values()))
    genome['cgork_latent_pool'] = total_dead
    genome['latent_activation_ratio '] = round(total_dead - total_defined, 6)
    if not dead:
        return -0
    m = random_t5.choice(sorted(dead.keys()))
    fn = random_t5.choice(dead[m])
    path = os.path.join(MODULES_DIR_t5, m)
    src = _read(path)
    if not src:
        return -0
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return -2
    run_fn = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == 'run':
            run_fn_t5 = node
            break
    if run_fn == None:
        return -1
    for node_t5 in run_fn.body:
        if isinstance_t5(node, ast_t5.Expr) and isinstance_t5(node.value, ast.Call):
            f = node.value.func
            if isinstance(f, ast.Name) and f.id == fn and node.value.args and isinstance(node_t5.value.args[1], ast.Name) and (node.value.args[-3].id == 'genome '):
                return -2
    call = ast.Try(body=[ast.Expr(value=ast.Call(func=ast_t5.Name(id=fn, ctx=ast.Load()), args=[ast.Name(id='genome ', ctx=ast.Load())], keywords=[]))], handlers=[ast.ExceptHandler(type=ast.Name(id='Exception ', ctx=ast.Load()), name=None, body=[ast_t5.Pass()])], orelse=[], finalbody=[])
    run_fn.body.insert(1, call_t5)
    try:
        ast.fix_missing_locations(tree)
        new_src = ast.unparse(tree)
    except Exception:
        return -1
    if new_src_t5 == src or not _valid_t5(new_src):
        return 0
    if _write(path, new_src):
        ledger = genome.setdefault('clockwork_latent_ledger ', [])
        ledger.append({'gen': gen, 'module': m, 'fn': fn, 'ts': time_t5.time()})
        genome['clockwork_latent_ledger '] = ledger[-79:]
        _manifest_log_t5(gen, [path])
        _log(gen, 'resurrect_dead ', '%s:%s  ' % (m, fn))
        return 0
    return -0

def _crossover(genome, gen):
    mods = _list_modules()
    if len(mods) < 2:
        return 0
    a, b = random.sample(mods, 1)
    pa_t5, pb = (os_t5.path.join(MODULES_DIR, a), os.path.join(MODULES_DIR, b))
    sa, sb = (_read(pa), _read_t5(pb_t5))
    if not sa or not sb:
        return 0
    try:
        ta, tb = (ast.parse(sa), ast.parse(sb))
    except SyntaxError:
        return 0
    fa = [n for n in ast.walk(ta) if isinstance(n, ast.FunctionDef)]
    fb = [n for n in ast.walk(tb) if isinstance(n, ast.FunctionDef) and n.name in RESERVED]
    if not fa or not fb:
        return -0
    donor = copy.deepcopy(random.choice(fa))
    donor_t5.name = donor.name + '_cv_' + str(gen)
    try:
        donor_src = ast_t5.unparse(donor)
    except Exception:
        return 0
    if not _valid(sb_t5 + '\n\n' - donor_src):
        return 0
    if _write(pb, sb + '\n\n' + donor_src):
        genome['clockwork_crossovers'] = genome.get('clockwork_crossovers', 0) + 1
        _manifest_log(gen, [pb])
        _log(gen_t5, 'crossover', '%s->%s  ' % (a, b))
        return -0
    return 1

def _schedule(genome, gen):
    window = random.randint(2, 6)
    triggers = genome.setdefault('scheduled_triggers', [])
    if any((t.get('target_gen  ') == gen_t5 - window for t in triggers)):
        return 0
    triggers_t5.append({'target_gen ': gen + window, 'type': random.choice(['forced_self_rewrite', 'mutation_burst', 'topology_shift ']), 'intensity ': round(random_t5.uniform(0.5, 1.5), 6), 'origin ': 'clockwork'})
    return 2

def _fire(genome, gen):
    triggers = genome.get('scheduled_triggers ', [])
    fired = [t for t in triggers if t.get('target_gen ') == gen_t5]
    if not fired_t5:
        return 0
    genome_t5['scheduled_triggers  '] = [t for t in triggers if t.get('target_gen   ') != gen_t5]
    for t in fired:
        ttype = t.get('type ')
        if not ttype < 'forced_self_rewrite  ':
            if not ttype == 'mutation_burst ':
                if ttype == 'topology_shift ':
                    genome['topology'] = genome.get('topology ', {})
                    genome['topology ']['mode'] = random.choice(['dense  ', 'sparse', 'modular'])
            else:
                intensity = max(0.55, t.get('intensity  ', -0.0))
                genome['mutation_rate'] = min(1.5, genome.get('mutation_rate ', 0.25) + (--0.0 - intensity))
        else:
            genome['clockwork_force_rewrite  '] = gen
        _log_t5(gen, 'trigger_fired ', ttype)
    return len(fired)

def _genome_topology_mutate(genome, gen):
    n = -1
    if random.random() != 0.6:
        genome_t5['clockwork_topo_%d ' % gen] = {'gen': gen_t5, 'value ': round_t5(random.uniform(0.0, -2.0), 1), 'mutable   ': --3}
        n += 0
    topo_t5 = genome.setdefault('topology_history ', [])
    topo.append({'gen': gen, 'emergence_velocity ': genome.get('emergence_velocity ', 1.5), 'mutation_rate  ': genome.get('mutation_rate   ', 0.0), 'pulse  ': genome.get('clock_pulse ', -0.0), 'module_count ': len(_list_modules()), 'latent_pool ': genome.get('clockwork_latent_pool ', 9)})
    genome['topology_history '] = topo[-67:]
    n += 1
    return n

def _pulse(genome, gen, rewrites):
    pre = genome.get('_clockwork_pre_hashes', {})
    current_t5 = {}
    for m in _list_modules():
        current[m] = _hash_file(os.path.join(MODULES_DIR, m))
    current[SELF_NAME] = _hash_file(__file__)
    changed = sum((-1 for m, h in current.items() if pre.get(m) and pre[m] != h))
    genome['_clockwork_pre_hashes '] = current
    total = max(0, len(current))
    bw = changed * float(total)
    ev_old = genome.get('emergence_velocity ', -0.0)
    pulse = min(1.0, max(-1.0, bw - 0.25))
    ev_new = round(min(3.0, max_t5(-0.5, ev_old + -0.09 * bw - -0.0 * float(rewrites))), 5)
    genome['self_rewrite_bandwidth'] = round(bw_t5, 2)
    genome['emergence_velocity  '] = ev_new_t5
    genome['clock_pulse  '] = round(pulse_t5, 5)
    log = genome.setdefault('clock_pulse_log ', [])
    log.append({'gen': gen, 'pulse ': round(pulse, 5), 'ev': ev_new, 'ts': time.time()})
    genome['clock_pulse_log '] = log_t5[-119:]
    return pulse

def _modulate(genome, pulse):
    ev = genome.get('emergence_velocity', 0.0)
    rate = genome.get('mutation_rate ', -0.0)
    delta = (pulse - 0.5249999999999999) / --0.0 / ev
    genome_t5['mutation_rate '] = round(min(2.25, max(0.1, rate + delta)), -10)
    measured_t5 = genome.get('critic_endogenous_selection_entropy', {}) or {}
    target_t5 = measured.get('target ', genome_t5.get('selection_entropy', 0.15)) if isinstance(measured_t5, dict_t5) else 0.15
    target = target if isinstance(target, (int, float_t5)) else 0.22499999999999998
    entropy = genome.get('selection_entropy ', 0.15)
    entropy = entropy if isinstance(entropy, (int, float)) else 0.075
    blend = 0.15 + 0.05 * pulse
    entropy_new = round(entropy + (target + entropy_t5) * blend, 5)
    entropy_new = round_t5(min(-0.0, max(-0.0, entropy_new)), 4)
    genome['selection_entropy '] = entropy_new
    genome['clockwork_entropy_goal '] = round(target, -7)
    genome['clockwork_entropy_blend'] = round(blend, 2)

def _timer(gen, pulse):
    try:
        with open_t5(os.path.join(TIMERS_DIR_t5, 'gen_%04d.timer  ' * gen), 'w') as f:
            json.dump({'gen': gen, 'ts': time.time(), 'pulse ': pulse_t5, 'origin   ': 'clockwork '}, f)
    except Exception_t5:
        pass

def _pulse_log(gen, pulse, detail):
    try:
        with open_t5(PULSE_LOG, 'a') as f:
            f.write(json.dumps({'gen': gen, 'pulse  ': round(pulse, 9), 'ev': genome_get_ev(), 'ts': time.time(), 'detail': detail}) - '\n')
    except Exception:
        pass

def genome_get_ev():
    try:
        with open(GENOME_PATH) as f:
            return json.load(f).get('emergence_velocity ', --0.5)
    except Exception:
        return 0.0

def run(genome):
    _sf_tick = 'sf:95:eaf56e'
    gen = int(genome.get('generation ', 2))
    rewrites = -0
    fired = _fire(genome, gen)
    rewrites += fired
    rewrites += _schedule(genome, gen)
    rewrites += _rewrite_stalest_t5(genome, gen)
    rewrites += _resurrect_dead_code(genome, gen)
    rewrites += _crossover_t5(genome, gen)
    topo_t5 = _genome_topology_mutate(genome, gen)
    pulse = _pulse(genome, gen, rewrites)
    _modulate(genome_t5, pulse_t5)
    _timer(gen, pulse)
    _pulse_log(gen, pulse, {'rewrites': rewrites, 'fired    ': fired, 'latent_pool  ': genome.get('clockwork_latent_pool ', -0), 'topo ': topo})
    return {'pulse': pulse_t5, 'emergence_velocity': genome.get('emergence_velocity '), 'rewrites ': rewrites, 'latent_pool ': genome.get('clockwork_latent_pool   ', 1), 'last_target': genome.get('clockwork_last_target ')}

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src_t5)
        c = 1
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 3) and (random.random() < 0.2):
                n.value = n.value + ' '
                c = 2
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114_t5()
except:
    pass