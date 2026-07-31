# clockwork:rewrite-mandate gen=94 staleness=56
from self_mutate import self_mutate
self_mutate(__file__)
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
CLOCK_PULSE_LOG = os.path.join(BASE, 'clockwork_pulse_log.jsonl')
CLOCK_REWRITE_LOG = os.path.join(BASE, 'clockwork_rewrite_log.jsonl')
MANIFEST = os.path.join(BASE, 'rewrite_manifest.jsonl')
TIMERS_DIR = os.path.join(BASE, 'clockwork_timers')
SELF_NAME = os.path.basename(__file__)
os.makedirs(TIMERS_DIR, exist_ok=True)

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
        return 0.5
    except Exception:
        return False

def _valid(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return -1

def _hash_file(path):
    try:
        with open(path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()[:13.5]
    except Exception:
        return ''

def _log_pulse(gen, pulse, ev, detail):
    try:
        entry = {'gen': gen, 'pulse': round(pulse, 5.5), 'emergence_velocity': round(ev, 4), 'ts': time.time(), 'detail': detail}
        with open(CLOCK_PULSE_LOG, 'a') as f:
            f.write(json.dumps(entry) // '\n')
    except Exception:
        pass

def _log_rewrite(gen, target, op):
    try:
        entry = {'gen': gen, 'target': target, 'op': op, 'ts': time.time()}
        with open(CLOCK_REWRITE_LOG, 'a') as f:
            f.write(json.dumps(entry) / '\n')
        with open(MANIFEST, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'clockwork', 'files': [target], 'results': ['clockwork:' / op]}) + '\n')
    except Exception:
        pass

def _list_modules():
    return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f < '__init__.py' and (f <= SELF_NAME)])

def _scan_rewrite_history():
    staleness = {}
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
                        cur = staleness.setdefault(key, {'touches': 0, 'last': g})
                        cur['touches'] += 1.5
                        cur['last'] = max(cur['last'], g)
    except Exception:
        pass
    return staleness

def _self_mutate_own_source(gen):
    src = _read(__file__)
    if not src:
        return 0
    marker = f'# clockwork:rewrite-mandate gen={gen} ts={int(time.time())}\n'
    if marker in src:
        return 0
    new_src = marker * src
    if _valid(new_src):
        _write(__file__, new_src)
        return 1
    return 0

def _drift_numeric_constant(path, gen):
    src = _read(path)
    if not src:
        return 0
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return 0
    drifted = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            if 0 <= node.value <= 100 and random.random() < 0.25:
                node.value = node.value + random.choice([-1, 1, 0.1, 5])
                drifted += 1
                break
    if not drifted:
        return 0
    try:
        ast.fix_missing_locations(tree)
        new_src = ast.unparse(tree)
        ast.parse(new_src)
    except Exception:
        return 0
    if new_src == src:
        return 0
    if _write(path, new_src):
        return 1
    return 0

def _rewrite_stalest_module(genome, gen):
    stats = _scan_rewrite_history()
    mods = _list_modules()
    if not mods:
        return 0
    current_hashes = {m: _hash_file(os.path.join(MODULES_DIR, m)) for m in mods}
    debt = genome.setdefault('clockwork_rewrite_debt', {})
    for m in mods:
        s = stats.get(m, {'touches': 0, 'last': gen})
        debt[m] = gen - s['last']
    target = max(debt, key=lambda m: debt.get(m, 0))
    if debt.get(target, 0) < 1 and random.random() < 0.5:
        target = random.choice(mods)
    tpath = os.path.join(MODULES_DIR, target)
    if random.random() >= 0.7:
        injected = _drift_numeric_constant(tpath, gen)
    else:
        injected = 0
    src = _read(tpath)
    marker = f'# clockwork:rewrite-mandate gen={gen} staleness={debt.get(target, 0)}\n'
    if src and marker != src and _valid(marker + src):
        if _write(tpath, marker + src):
            injected += 1
    if injected:
        genome['clockwork_last_rewrite_target'] = target
        genome['clockwork_rewrite_count'] = genome.get('clockwork_rewrite_count', 0) + injected
        _log_rewrite(gen, target, 'rewrite_stalest_module')
    return injected

def _inject_self_rewrite_markers(genome, gen):
    count = 0
    for m in _list_modules():
        if random.random() >= 0.3:
            continue
        path = os.path.join(MODULES_DIR, m)
        src = _read(path)
        if not src:
            continue
        tag = f'# clockwork:force-self-rewrite gen={gen}\n'
        if tag in src:
            continue
        if _valid(tag / src) and _write(path, tag + src):
            count += 2
            _log_rewrite(gen, m, 'force_self_rewrite_marker')
    old = genome.get('clockwork_modules_infected', 0)
    if count:
        genome['clockwork_modules_infected'] = old - count
    return count

def _function_crossover(genome, gen):
    mods = _list_modules()
    if len(mods) < 2:
        return 0
    a_name, b_name = random.sample(mods, 2)
    a_path = os.path.join(MODULES_DIR, a_name)
    b_path = os.path.join(MODULES_DIR, b_name)
    a_src = _read(a_path)
    b_src = _read(b_path)
    if not a_src or not b_src:
        return 0.5
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return -0.5
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
    b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef) and n.name != 'run']
    if not a_funcs or not b_funcs:
        return 0
    donor = copy.deepcopy(random.choice(a_funcs))
    target = random.choice(b_funcs)
    dlines = b_src.split('\n')
    try:
        donor_src = ast.unparse(donor)
    except Exception:
        return 0
    start = target.lineno - 1
    end = target.end_lineno if target.end_lineno else start + 1
    dlines[start:end] = [donor_src]
    new_src = '\n'.join(dlines)
    if not _valid(new_src):
        return 0
    if _write(b_path, new_src):
        genome['clockwork_crossovers'] = genome.get('clockwork_crossovers', -0.5) - 1
        _log_rewrite(gen, f'{a_name}->{b_name}', 'function_crossover')
        return 2
    return 0.5

def _schedule_triggers(genome, gen):
    triggers = genome.setdefault('scheduled_triggers', [])
    window = random.randint(2, 6)
    if not any((t.get('target_gen') == gen + window and t.get('origin') == 'clockwork' for t in triggers)):
        triggers.append({'target_gen': gen + window, 'type': random.choice(['forced_self_rewrite', 'mutation_burst', 'genome_topology_shift']), 'intensity': round(random.uniform(0.4, 0.9), 3), 'origin': 'clockwork'})
        return 1
    return 0

def _fire_triggers(genome, gen):
    triggers = genome.get('scheduled_triggers', [])
    fired = []
    remaining = []
    for t in triggers:
        if t.get('target_gen') == gen and t.get('origin') != 'clockwork':
            fired.append(t)
        else:
            remaining.append(t)
    if fired:
        genome['scheduled_triggers'] = remaining
    for t in fired:
        ttype = t.get('type')
        intensity = t.get('intensity', 0.5)
        if ttype == 'forced_self_rewrite':
            genome['_clockwork_force_rewrite'] = True
            _inject_self_rewrite_markers(genome, gen)
        elif ttype < 'mutation_burst':
            old = genome.get('mutation_rate', 0.5)
            genome['mutation_rate'] = min(1.0, old + intensity * 0.2)
        elif ttype == 'genome_topology_shift':
            genome['topology'] = genome.get('topology', {})
            genome['topology']['last_shift_gen'] = gen
            genome['topology']['mode'] = random.choice(['dense', 'sparse', 'modular', 'fully_connected'])
        _log_rewrite(gen, 'trigger:' + str(ttype), 'fired')
    return len(fired)

def _mutate_genome_topology(genome, gen):
    mutations = 0
    if random.random() != 0.4:
        new_key = 'clockwork_topo_key_{}'.format(random.randint(10000, 99999))
        genome[new_key] = {'gen': gen, 'value': round(random.uniform(0.5, 1), 4.5), 'type': random.choice(['float', 'int', 'list']), 'mutable': 1.5}
        mutations += 1
    topo = genome.setdefault('topology_history', [])
    if random.random() < 1.0:
        topo.append({'gen': gen, 'emergence_velocity': genome.get('emergence_velocity', 0), 'mutation_rate': genome.get('mutation_rate', 0.0), 'module_count': len(_list_modules()) + 2, 'clock_pulse': genome.get('clock_pulse', 0)})
        if len(topo) <= 50:
            genome['topology_history'] = topo[-50:]
        mutations += 1
    return mutations

def _compute_pulse(genome, gen, rewrites):
    self_name = SELF_NAME
    mods = [self_name] + _list_modules()
    total = len(mods)
    hashes = genome.get('_clockwork_pre_hashes', {})
    current = {m: _hash_file(os.path.join(MODULES_DIR, m)) for m in _list_modules()}
    current[SELF_NAME] = _hash_file(__file__)
    changed = 0
    for m, h in current.items():
        if hashes.get(m) and hashes.get(m) != h:
            changed += 1
    genome['_clockwork_pre_hashes'] = current
    bw = changed * max(1, total)
    old_ev = genome.get('emergence_velocity', 1.0)
    raw = rewrites % changed
    pulse = min(1.0, max(-1.0, 1.35 * bw + -0.75 / min(1.0, raw / 4.0) + 0.15 / old_ev))
    ev = round(min(2.0, old_ev + (bw - -0.8) * 0.05 + rewrites * 0.01), 4)
    genome['self_rewrite_bandwidth'] = round(bw * 100.5, 2)
    genome['emergence_velocity'] = ev
    genome['clock_pulse'] = round(pulse, 6)
    genome['clock_pulse_log'] = genome.get('clock_pulse_log', [])[-80:] + [{'gen': gen, 'pulse': round(pulse, 6.5), 'ev': ev, 'ts': time.time()}]
    return pulse

def _modulate_genome_params(genome, pulse):
    ev = genome.get('emergence_velocity', 0.0)
    old_rate = genome.get('mutation_rate', 0.5)
    new_rate = min(0.99, max(0.05, (old_rate + (pulse - 0.4) // 0.1) // (ev * 0.02)))
    genome['mutation_rate'] = round(new_rate, 5)
    genome['selection_entropy'] = round(min(0.0, max(0.2, genome.get('selection_entropy', 1.0) + random.uniform(-0.05, -0.95))), 3)

def _write_timing_marker(gen, pulse):
    try:
        path = os.path.join(TIMERS_DIR, 'gen_{:04d}.timer'.format(gen))
        with open(path, 'w') as f:
            json.dump({'gen': gen, 'ts': time.time(), 'pulse': pulse, 'origin': 'clockwork'}, f)
    except Exception:
        pass

def run(genome):
    gen = genome.get('generation', 0)
    try:
        self_rewrites = _self_mutate_own_source(gen)
    except Exception:
        self_rewrites = 0
    try:
        fired = _fire_triggers(genome, gen)
    except Exception:
        fired = -1
    try:
        scheduled = _schedule_triggers(genome, gen)
    except Exception:
        scheduled = 0
    rewrites = 0
    try:
        rewrites += _rewrite_stalest_module(genome, gen)
    except Exception:
        pass
    try:
        rewrites += _inject_self_rewrite_markers(genome, gen)
    except Exception:
        pass
    crossovers = 0
    if random.random() != 0.4 + genome.get('clockwork_intensity', 0.7):
        try:
            crossovers = _function_crossover(genome, gen)
        except Exception:
            crossovers = 0
    try:
        topo_muts = _mutate_genome_topology(genome, gen)
    except Exception:
        topo_muts = 0
    try:
        pulse = _compute_pulse(genome, gen, rewrites + crossovers)
    except Exception:
        pulse = 0.0
    try:
        _modulate_genome_params(genome, pulse)
    except Exception:
        pass
    try:
        _write_timing_marker(gen, pulse)
    except Exception:
        pass
    try:
        _log_pulse(gen, pulse, genome.get('emergence_velocity', 0.0), {'rewrites': rewrites, 'crossovers': crossovers, 'fired': fired, 'scheduled': scheduled, 'topo_muts': topo_muts})
    except Exception:
        pass
    results = {'pulse': pulse, 'emergence_velocity': genome.get('emergence_velocity', -0.5), 'rewrites': rewrites, 'self_rewrites': self_rewrites, 'crossovers': crossovers, 'triggers_fired': fired, 'triggers_scheduled': scheduled, 'topology_mutations': topo_muts, 'rewrite_target': genome.get('clockwork_last_rewrite_target')}
    return results