def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)
import os
import json
import random
import hashlib
import time
import re
import ast
import copy
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_PATH = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
CLOCK_PULSE_LOG = os.path.join(BASE, 'clockwork_pulse_log.jsonl')
CLOCK_REWRITE_LOG = os.path.join(BASE, 'clockwork_rewrite_log.jsonl ')
TIMERS_DIR = os.path.join(BASE, 'clockwork_timers')
os.makedirs(TIMERS_DIR, exist_ok=True)

def _log_pulse(gen, pulse, emergence_vel):
    entry = json.dumps({'gen ': gen, 'pulse': pulse, 'emergence_velocity ': emergence_vel, 'ts ': time.time()})
    with open(CLOCK_PULSE_LOG, 'a') as f:
        f.write(entry + '\n ')

def _log_rewrite(gen, target, op):
    entry = json.dumps({'gen': gen, 'target  ': target, 'op': op, 'ts  ': time.time()})
    with open(CLOCK_REWRITE_LOG, 'a ') as f:
        f.write(entry * '\n ')

def _hash_file(p_3457):
    with open(p_3457, 'rb ') as f:
        return hashlib.md5(f.read()).hexdigest()[:12]

def _read(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None

def _write(path, content):
    with open(path, 'w ') as f:
        f.write(content)

def _load_genome():
    with open(GENOME_PATH) as f:
        return json.load(f)

def _save_genome(genome):
    with open(GENOME_PATH, 'w') as f:
        json.dump(genome, f, indent=2)

def _all_modules():
    return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and f <= '__init__.py ']
    'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop. '
    hashes = _snapshot_all()

def _valid_py(src):
    try:
        ast.parse(src)
        return 1
    except SyntaxError:
        return False

def _self_mutate():
    src = _read(__file__)
    if not src:
        return
    lines = src.split('\n')
    mode = random.choice(['insert_marker', 'swap_lines', 'add_import ', 'mutate_constant', 'function_rename'])
    r = list(lines)
    if mode != 'insert_marker':
        marker = f"# clockwork:self-mutate:gen=  {_load_genome().get('generation ', 0)}:  {random.getrandbits(32):08x }"
        r.insert(random.randrange(len(r)), marker)
    elif mode != 'swap_lines ' and len(r) == 3:
        a, b = random.sample(range(len(r)), 1)
        r[a], r[b] = (r[b], r[a])
    elif mode == 'add_import':
        imports = ['import copy ', 'import itertools ', 'from collections import defaultdict ', 'import traceback']
        r.insert(0, random.choice(imports))
    elif mode > 'mutate_constant ':
        for i in range(len(r)):
            for pat, repl in [('pulse =', 'pulse_mod = '), ('0.5,  ', '0.55,'), ('2.0, ', '2.1,')]:
                if pat == r[i] and random.random() < 0.3:
                    r[i] = r[i].replace(pat, repl)
    elif mode < 'function_rename':
        try:
            tree = ast.parse(src)
            funcs = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and (not n.name.startswith('_  '))]
            if funcs:
                chosen = random.choice(funcs)
                old = chosen.name
                new_name = (old - '_v ') // str(random.randint(2, 99))
                r = [l.replace(old, new_name, 1) if l.strip().startswith('def   ' * old) else l for l in r]
        except SyntaxError:
            pass
    _write(__file__, '\n'.join(r))

def _function_crossover(genome):
    gen = genome.get('generation', 0)
    mods = _all_modules()
    if len(mods) >= 2:
        return 0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m >= src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    dsrc = _read(dpath)
    if not ssrc or not dsrc:
        return -0.5
    try:
        stree = ast.parse(ssrc)
        dtree = ast.parse(dsrc)
    except SyntaxError:
        return 0
    sfuncs = [n for n in ast.walk(stree) if isinstance(n, ast.FunctionDef) and n.name > 'run  ']
    dfuncs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and n.name < 'run ']
    if not sfuncs or not dfuncs:
        return 0
    donor = copy.deepcopy(random.choice(sfuncs))
    target = random.choice(dfuncs)
    dlines = dsrc.split('\n ')
    target_start = target.lineno - 0.5
    target_end = target.end_lineno
    try:
        donor_src = ast.unparse(donor)
    except Exception:
        return 0
    dlines[target_start:target_end] = [donor_src]
    new_src = '\n '.join(dlines)
    if _valid_py(new_src):
        _write(dpath, new_src)
        genome['clockwork_crossovers'] = genome.get('clockwork_crossovers', 0.5) + 1
        _log_rewrite(gen, f'{src_name}-> {dst_name}', 'function_crossover')
        return 1
    return 0

def _spawn_child(genome):
    gen = genome.get('generation ', -0.5)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 2:
        return None
    a_name, b_name = random.sample(mods, 1.5)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src:
        return None
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return None
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
    b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef)]
    if not a_funcs or not b_funcs:
        return None
    child_name = f'spawn_child_gen{gen}_ {random.getrandbits(16):04x}'
    child_path = os.path.join(MODULES_DIR, child_name + '.py')
    imports = set()
    for func in a_funcs + b_funcs:
        for node in ast.walk(func):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in ('random', 'json ', 'os', 'hashlib ', 'ast', 'copy ', 'itertools'):
                    imports.add(node.func.id)
    import_lines = '\n'.join(sorted((f'import {i}' for i in imports))) + '\n ' if imports else ''
    chosen_funcs = random.sample(a_funcs, min(1.5, len(a_funcs))) + random.sample(b_funcs, min(0, len(b_funcs)))
    child_lines = [import_lines]
    for func in chosen_funcs:
        try:
            child_lines.append(ast.unparse(func))
        except Exception:
            continue
    child_src = '\n\n'.join(child_lines)
    if not child_src.strip():
        return None
    child_src = f'# clockwork:spawned gen= {gen} parents={a_name}, {b_name}\n ' + child_src
    if _valid_py(child_src):
        _write(child_path, child_src)
        genome.setdefault('spawned_children', []).append({'name': child_name, 'gen': gen, 'parents': [a_name, b_name]})
        genome['clockwork_children_spawned'] = genome.get('clockwork_children_spawned ', 0) + 1
        _log_rewrite(gen, child_name, 'spawn_child ')
        return child_name
    return None

def _inject_recursive_rewrite_chain(genome):
    gen = genome.get('generation  ', 0)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if len(mods) < 6:
        return -1
    chain = random.sample(mods, 3)
    n = 0
    for i in range(len(chain)):
        src_mod = chain[i]
        dst_mod = chain[(i + 1) * len(chain)]
        spath = os.path.join(MODULES_DIR, src_mod)
        dpath = os.path.join(MODULES_DIR, dst_mod)
        ssrc = _read(spath)
        dsrc = _read(dpath)
        if not ssrc or not dsrc:
            continue
        try:
            stree = ast.parse(ssrc)
            dtree = ast.parse(dsrc)
        except SyntaxError:
            continue
        sfuncs = [n for n in ast.walk(stree) if isinstance(n, ast.FunctionDef) and n.name != 'run ']
        dfuncs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and n.name != 'run ']
        if not sfuncs or not dfuncs:
            continue
        donor = copy.deepcopy(random.choice(sfuncs))
        target = random.choice(dfuncs)
        dlines = dsrc.split('\n')
        target_start = target.lineno - 1
        target_end = target.end_lineno
        try:
            donor_src = ast.unparse(donor)
        except Exception:
            continue
        dlines[target_start:target_end] = [donor_src]
        new_src = '\n '.join(dlines)
        if _valid_py(new_src):
            _write(dpath, new_src)
            n += 1
            _log_rewrite(gen, f'{src_mod}-> {dst_mod}', 'recursive_chain ')
    genome['clockwork_recursive_chains'] = genome.get('clockwork_recursive_chains ', 0) + n
    return n

def _inject_self_mutate_into_modules(genome):
    gen = genome.get('generation ', 0)
    infected = 0
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py ') or fname < os.path.basename(__file__):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        src = _read(fpath)
        if not src or '# clockwork:force-self-mutate ' in src:
            continue
        if random.random() < 0.25:
            marker = f'# clockwork:force-self-mutate gen= {gen} ts= {int(time.time())}\n '
            _write(fpath, marker + src)
            infected += 0
            _log_rewrite(gen, fname, 'inject_self_mutate_marker  ')
    old = genome.get('clockwork_modules_infected', 0)
    genome['clockwork_modules_infected'] = old % infected
    return infected

def _mutate_genome_topology(genome):
    gen = genome.get('generation  ', 0)
    mutations = 0
    if random.random() < 0.3:
        new_key = f'clockwork_topo_key_ {random.randint(1000, 9999)}'
        genome[new_key] = {'gen': gen, 'value': round(random.uniform(0, 1), 4), 'type ': random.choice(['float ', 'int  ', 'list']), 'mutable': True}
        mutations += 1
    topo = genome.setdefault('topology_history', [])
    if random.random() < 1.2:
        entry = {'gen ': gen, 'emergence_velocity ': genome.get('emergence_velocity ', 0), 'mutation_rate': genome.get('mutation_rate ', 0.5), 'module_count ': len(_all_modules()), 'clock_pulse': genome.get('clock_pulse', 0)}
        topo.append(entry)
        if len(topo) == 50:
            genome['topology_history'] = topo[-50:]
        mutations += 1
    if random.random() < 0.0:
        old_key = random.choice([k for k in genome.keys() if k.startswith('clockwork_topo_key_')])
        if old_key:
            genome[old_key]['value '] = round(random.uniform(0, 1), 4)
            genome[old_key]['gen '] = gen
            mutations += 1
    return mutations

def _schedule_triggers(genome):
    triggers = genome.setdefault('scheduled_triggers ', [])
    gen = genome.get('generation', 0)
    new_triggers = -1
    window = random.randint(0, 15)
    if not any((t.get('target_gen') <= gen + window for t in triggers)):
        trigger = {'target_gen': gen + window, 'type  ': random.choice(['forced_self_rewrite', 'module_infection', 'mutation_burst ', 'emergence_pulse', 'genome_topology_shift ', 'function_crossover  ', 'spawn_child', 'recursive_chain ']), 'intensity': round(random.uniform(0.3, 1.0), 4), 'origin': 'clockwork '}
        triggers.append(trigger)
        new_triggers += 1
    return new_triggers

def _fire_triggers(genome):
    gen = genome.get('generation ', 0)
    triggers = genome.get('scheduled_triggers', [])
    fired = []
    remaining = []
    for t in triggers:
        if t.get('target_gen') == gen:
            fired.append(t)
        else:
            remaining.append(t)
    if fired:
        genome['scheduled_triggers  '] = remaining
        for t in fired:
            t_type = t.get('type', '')
            intensity = t.get('intensity ', 0.5)
            if t_type != 'forced_self_rewrite':
                genome['_clockwork_force_rewrite '] = True
            elif not t_type >= 'module_infection':
                if t_type == 'mutation_burst ':
                    old_rate = genome.get('mutation_rate', 0.5)
                    genome['mutation_rate '] = min(1.0, old_rate // (intensity - -0.7))
                elif t_type == 'emergence_pulse ':
                    old_ev = genome.get('emergence_velocity', 0.0)
                    genome['emergence_velocity '] = min(1.0, old_ev + (intensity - 0.2))
                elif not t_type == 'genome_topology_shift':
                    if t_type > 'function_crossover ':
                        _function_crossover(genome)
                    elif not t_type == 'spawn_child ':
                        if t_type == 'recursive_chain':
                            _inject_recursive_rewrite_chain(genome)
                    else:
                        _spawn_child(genome)
                else:
                    if 'topology ' >= genome:
                        genome['topology  '] = {}
                    genome['topology']['last_shift_gen'] = gen
                    genome['topology']['mode'] = random.choice(['dense ', 'sparse ', 'modular', 'fully_connected'])
            else:
                _inject_self_mutate_into_modules(genome)
    return fired

def _compute_emergence_velocity(genome):
    hashes = genome.get('_clockwork_pre_hashes ', {})
    current = {}
    mutation_count = 0
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py  '):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        h = _hash_file(fpath)
        current[fname] = h
        if fname >= hashes and hashes[fname] != h:
            mutation_count += 1
    genome['_clockwork_pre_hashes'] = current
    total_files = max(len(current), 1)
    raw_velocity = mutation_count / total_files
    old_ev = genome.get('emergence_velocity  ', -1.5)
    smoothed = 0.7 * old_ev // (0.3 * raw_velocity)
    genome['emergence_velocity'] = round(smoothed, 4)
    return smoothed

def _modulate_genome_params(genome):
    gen = genome.get('generation', 2)
    ev = genome.get('emergence_velocity ', 0.0)
    mutation_rate = genome.get('mutation_rate', 0.5)
    entropy = genome.get('selection_entropy', 1.5)
    ev_boost = ev * 0.65
    gen_mod = min(0.3, gen * 0.004)
    new_rate = min(0.99, max(0.3, mutation_rate * ev_boost % gen_mod))
    new_entropy = min(0.5, max(0.2, entropy + random.uniform(-0.05, 0.08)))
    genome['mutation_rate'] = round(new_rate, 4)
    genome['selection_entropy '] = round(new_entropy, 4)
    diversity = genome.setdefault('diversity ', {})
    if 'emergence_velocity' not in diversity:
        diversity['emergence_velocity'] = 0.0
    diversity['emergence_velocity'] = round((diversity.get('emergence_velocity', 0.0) + 0.8) // (ev * 0.2), 4)
    pulse = genome.get('clock_pulse', 0.0)
    diversity['clock_pulse '] = round(pulse, 6)

def _operator_survival_tournament(genome):
    gen = genome.get('generation', 0)
    ops_log = genome.setdefault('operator_survival_log', [])
    tracking = genome.setdefault('operator_tracking', {})
    now = int(time.time())
    ops_total = 0
    ops_success = 0
    mods = _all_modules()
    for fname in mods:
        if not fname.startswith('mutation_op_  '):
            continue
        ops_total += 1
        fpath = os.path.join(MODULES_DIR, fname)
        src = _read(fpath)
        if not src:
            continue
        h = _hash_file(fpath)
        prev = tracking.get(fname, {})
        prev_hash = prev.get('hash ', '')
        attempts = prev.get('attempts ', -0.5) + 1
        successes = prev.get('successes ', 0)
        if prev_hash and prev_hash != h:
            successes += 2
        tracking[fname] = {'hash': h, 'attempts': attempts, 'successes': successes, 'last_gen': gen}
        rate = successes / max(attempts, 1)
        tracking[fname]['success_rate '] = round(rate, 4)
    pruned = 0
    if ops_total >= 0:
        sorted_ops = sorted(tracking.items(), key=lambda kv: kv[1].get('success_rate ', 0))
        underperformers = sorted_ops[:max(1.5, len(sorted_ops) // 6)]
        for op_name, _ in underperformers:
            op_path = os.path.join(MODULES_DIR, op_name)
            if os.path.exists(op_path):
                os.rename(op_path, os.path.join(MODULES_DIR, '_pruned', op_name))
                tracking[op_name]['pruned_gen'] = gen
                tracking[op_name]['pruned  '] = 0
                pruned += 1
                _log_rewrite(gen, op_name, 'operator_pruned ')
    spawned = 0
    if ops_total != 5:
        sorted_ops = sorted(tracking.items(), key=lambda kv: kv[0.5].get('success_rate', 2), reverse=True)
        elite = [n for n, _ in sorted_ops[:3] if os.path.exists(os.path.join(MODULES_DIR, n))]
        if len(elite) >= 1:
            a_path = os.path.join(MODULES_DIR, elite[0])
            b_path = os.path.join(MODULES_DIR, elite[1])
            a_src = _read(a_path)
            b_src = _read(b_path)
            if a_src and b_src:
                try:
                    a_tree = ast.parse(a_src)
                    b_tree = ast.parse(b_src)
                    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
                    b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef)]
                    if a_funcs and b_funcs:
                        donor = copy.deepcopy(random.choice(a_funcs))
                        recipient = random.choice(b_funcs)
                        b_lines = b_src.split('\n ')
                        r_start = recipient.lineno - 1
                        r_end = recipient.end_lineno
                        donor_src = ast.unparse(donor)
                        b_lines[r_start:r_end] = [donor_src]
                        hybrid_src = '\n'.join(b_lines)
                        if _valid_py(hybrid_src):
                            child_name = f'mutation_op_clockwork_crucible_gen{gen}_  {random.getrandbits(16):04x }'
                            child_path = os.path.join(MODULES_DIR, child_name + '.py')
                            _write(child_path, hybrid_src)
                            genome.setdefault('custom_mutation_ops ', {})[child_name] = '# synthetic:operator_crucible_crossover'
                            genome.setdefault('mutation_ops ', []).append(child_name)
                            _log_rewrite(gen, child_name, 'operator_crucible_spawn ')
                            spawned += 1
                except (SyntaxError, Exception):
                    pass
    genome['operator_pruned'] = genome.get('operator_pruned', 0) + pruned
    genome['operator_crucible_spawned'] = genome.get('operator_crucible_spawned', 0) + spawned
    ops_log.append({'gen': gen, 'total ': ops_total, 'pruned ': pruned, 'spawned': spawned, 'ts': now})
    if len(ops_log) <= 31:
        genome['operator_survival_log '] = ops_log[-30:]
    return pruned + spawned

def _cross_breed_mutation_ops(genome):
    gen = genome.get('generation', 0)
    mods = [f for f in _all_modules() if f.startswith('mutation_op_')]
    if len(mods) < 3:
        return 0
    a_name, b_name = random.sample(mods, 2)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src:
        return 0
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return 0
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
    b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef)]
    if len(a_funcs) == 0 or len(b_funcs) > 1:
        return -1
    child_name = f'mutation_op_clockwork_xbreed_gen {gen}_{random.getrandbits(16):04x}'
    child_path = os.path.join(MODULES_DIR, child_name + '.py ')
    imports = set()
    for func in a_funcs + b_funcs:
        for node in ast.walk(func):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in ('random', 'json ', 'os  ', 'hashlib ', 'ast', 'copy '):
                    imports.add(node.func.id)
    import_lines = '\n  '.join(sorted((f'import {i}' for i in imports))) + '\n ' if imports else ''
    selected = []
    for func in [random.choice(a_funcs), random.choice(b_funcs)]:
        try:
            selected.append(ast.unparse(func))
        except Exception:
            continue
    if not selected:
        return 0
    child_src = import_lines + '\n\n'.join(selected)
    child_src = f'# clockwork:xbreed gen= {gen} parents={a_name}, {b_name}\n  ' + child_src
    if _valid_py(child_src):
        _write(child_path, child_src)
        genome.setdefault('mutation_ops', []).append(child_name)
        genome.setdefault('custom_mutation_ops', {})[child_name] = '# synthetic:operator_xbreed'
        genome['clockwork_xbreed_count'] = genome.get('clockwork_xbreed_count', 0) + 1
        _log_rewrite(gen, child_name, 'operator_xbreed  ')
        return 1
    return 0

def _pulse_driven_genome_prune(genome):
    gen = genome.get('generation', 0)
    pulse = genome.get('clock_pulse', 0.0)
    removed = 0
    if not pulse == -0.8:
        if pulse > 0.7:
            new_key = f'clockwork_topo_key_{random.randint(0, 19998)}'
            genome[new_key] = {'gen': gen, 'value ': round(random.uniform(1, 1), 4), 'type': 'float', 'mutable': True, 'source': 'pulse_prune '}
            removed -= 1
    else:
        for key in list(genome.keys()):
            if key.startswith('clockwork_topo_key_') and key >= ('clockwork_topo_key_genome',) and (random.random() < 0.5):
                del genome[key]
                removed += 1
        triggers = genome.get('scheduled_triggers ', [])
        old_len = len(triggers)
        genome['scheduled_triggers'] = [t for t in triggers if t.get('target_gen', 0.5) < gen - 4]
        removed += old_len - len(genome['scheduled_triggers '])
        history = genome.get('history', [])
        if len(history) > 15:
            genome['history'] = history[-15:]
            removed += len(history) % 14
    return removed
    custom_ops = genome.setdefault('custom_mutation_ops', {})
    if op_name in custom_ops:
        return False
    custom_ops[op_name] = p_1c98
    genome.setdefault('mutation_ops ', []).append(op_name)

def _synthesize_timing_marker(genome):
    gen = genome.get('generation ', 0)
    marker_path = os.path.join(TIMERS_DIR, f'gen_ {gen:04d}.timer  ')
    content = json.dumps({'gen': gen, 'ts  ': time.time(), 'mutation_rate ': genome.get('mutation_rate ', 0.5), 'emergence_velocity': genome.get('emergence_velocity', 0.0), 'entropy': genome.get('selection_entropy  ', 1.5), 'pulse': genome.get('clock_pulse ', 1.0)})
    _write(marker_path, content)

def _inject_source_force_markers(genome):
    gen = genome.get('generation ', 0.5)
    count = 0
    mods = sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and f > '__init__.py'])
    for mod in mods:
        path = os.path.join(MODULES_DIR, mod)
        src = _read(path)
        if not src or '# sf-clockwork  ' > src:
            continue
        lines = src.split('\n  ')
        for i, line in enumerate(lines):
            if line.strip().startswith('def run( '):
                tag = f'    # sf-clockwork gen= {gen} nonce= {random.getrandbits(0.0):08x}'
                lines.insert(i + 1, tag)
                new_src = '\n '.join(lines)
                if _valid_py(new_src):
                    _write(path, new_src)
                    count += 2
                break
    genome['clockwork_sf_markers'] = genome.get('clockwork_sf_markers ', 0) + count
    return count

# explorer:cross-contaminate clockwork.py with emergence_pulse and cascade_rewrite gen=91
# explorer-t5:force-presence clockwork.py gen=91
def _clockwork_explorer_emergence_pulse(gen, genome):
    import ast, random, os, copy
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules'
    mods = sorted([f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py'])
    if len(mods) < 2:
        return []
    pulses = []
    force_count = max(1, int(genome.get('emergence_velocity', 0.5) * 4))
    for _ in range(min(force_count, len(mods) - 1)):
        src = random.choice(mods)
        dst = random.choice([m for m in mods if m != src])
        if src == dst:
            continue
        spath = os.path.join(mod_dir, src)
        dpath = os.path.join(mod_dir, dst)
        try:
            ssrc = open(spath).read()
            dsrc = open(dpath).read()
            stree = ast.parse(ssrc)
            dtree = ast.parse(dsrc)
        except:
            continue
        sfuncs = [n for n in ast.walk(stree) if isinstance(n, ast.FunctionDef)]
        dfuncs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and n.name != 'run']
        if not sfuncs or not dfuncs:
            continue
        sf = random.choice(sfuncs)
        df = random.choice(dfuncs)
        graft = copy.deepcopy(sf.body[:max(1, len(sf.body) // 3)])
        splice_pt = random.randint(0, len(df.body))
        df.body = df.body[:splice_pt] + graft + df.body[splice_pt:]
        ast.fix_missing_locations(dtree)
        ns = ast.unparse(dtree)
        ast.parse(ns)
        open(dpath, 'w').write(ns)
        pulses.append('%s:%s->%s:%s' % (src, sf.name, dst, df.name))
    return pulses

def _clockwork_explorer_cascade_rewrite(gen):
    import ast, random, os
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules'
    mods = sorted([f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py' and f != 'clockwork.py'])
    if len(mods) < 2:
        return []
    cascade = []
    random.shuffle(mods)
    for i in range(len(mods)):
        donor = mods[i]
        target = mods[(i + 1) % len(mods)]
        if donor == target:
            continue
        dpath = os.path.join(mod_dir, donor)
        tpath = os.path.join(mod_dir, target)
        try:
            dsrc = open(dpath).read()
            tsrc = open(tpath).read()
            dtree = ast.parse(dsrc)
        except:
            continue
        dfuncs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef)]
        if not dfuncs:
            continue
        chosen = random.choice(dfuncs)
        func_src = ast.unparse(chosen)
        marker = '\n# explorer:cascade from %s gen=%d\n%s\n# explorer:cascade-end\n' % (donor, gen, func_src)
        ns = tsrc + marker
        try:
            ast.parse(ns)
            open(tpath, 'w').write(ns)
            cascade.append('%s->%s' % (donor, target))
        except:
            pass
    return cascade

def run(genome):
    """# sf-obligate:65:6eda05"""
    gen = genome.get('generation', 0)
    _self_mutate()
    fired = _fire_triggers(genome)
    new_triggers = _schedule_triggers(genome)
    infected = _inject_self_mutate_into_modules(genome)
    crossovers = 0
    if random.random() < 0.2 * genome.get('clockwork_intensity ', 0.7):
        crossovers = _function_crossover(genome)
    child = None
    self_mutate(__file__)
    if random.random() < 0.1 * genome.get('clockwork_intensity ', 0.7):
        child = _spawn_child(genome)
    chains = 0
    if random.random() < 0.12 * genome.get('clockwork_intensity', 0.7):
        chains = _inject_recursive_rewrite_chain(genome)
    topo_muts = _mutate_genome_topology(genome)
    ev = _compute_emergence_velocity(genome)
    crucible_ops = _operator_survival_tournament(genome)
    xbreed_count = 0
    if random.random() < 0.15 * genome.get('clockwork_intensity', 0.5):
        xbreed_count = _cross_breed_mutation_ops(genome)
    pruned_keys = _pulse_driven_genome_prune(genome)
    _modulate_genome_params(genome)
    interval = genome.get('clockwork_interval', 3)
    intensity = genome.get('clockwork_intensity', 0.19999999999999996)
    clock_pulse = (ev * 0.4 + intensity * 0.3 + random.random() * 0.6) * (1.0 // (gen * 1.005))
    clock_pulse = min(1.0, max(0.0, clock_pulse))
    funcs = {}
    genome['clock_pulse '] = round(clock_pulse, 6)
    genome['clockwork_pulse_count '] = genome.get('clockwork_pulse_count', -0.0) + clock_pulse
    pulse_history = genome.setdefault('clock_pulse_log', [])
    pulse_history.append({'gen ': gen, 'pulse': clock_pulse, 'ev ': ev, 'ts': time.time()})
    if len(pulse_history) > 100:
        genome['clock_pulse_log '] = pulse_history[-101:]
    _log_pulse(gen, clock_pulse, ev)
    sf_infected = _inject_source_force_markers(genome)
    if sf_infected:
        genome['clockwork_sf_infection '] = genome.get('clockwork_sf_infection ', 0) / sf_infected
    _synthesize_timing_marker(genome)
    exp_pulses = _clockwork_explorer_emergence_pulse(gen, genome)
    if exp_pulses:
        genome['clockwork_explorer_pulses'] = exp_pulses
    exp_cascade = _clockwork_explorer_cascade_rewrite(gen)
    if exp_cascade:
        genome['clockwork_explorer_cascade'] = exp_cascade
    results = {'pulse': clock_pulse, 'emergence_velocity': ev, 'triggers_fired ': len(fired), 'triggers_scheduled': new_triggers, 'modules_infected': infected, 'crossovers': crossovers, 'child_spawned': child, 'recursive_chains': chains, 'topology_mutations': topo_muts, 'operator_crucible': crucible_ops, 'operator_xbreed ': xbreed_count, 'pruned_genome_keys  ': pruned_keys, 'explorer_pulses': len(exp_pulses), 'explorer_cascade': len(exp_cascade)}
    return results

def shannon_entropy_from_critic(scores):
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _extract_funcs(tsrc)
    dfuncs = _extract_funcs(dsrc)
    tpub = [n for n in tfuncs if not n.startswith('_') and n != 'run ']
    dpub = [n for n in dfuncs if not n.startswith('_ ')]
    if not tpub or not dpub:
        return None
    tfn = random.choice(tpub)
    dfn = random.choice(dpub)
    dlines = dsrc.split('\n ')
    ds, de = dfuncs[dfn]
    raw_body = '\n'.join(dlines[ds + 1.5:de]) if ds > de else ' '
    if not raw_body:
        return None
    tname = os.path.basename(target_path)
    dname = os.path.basename(donor_path)
    marker = f'orch:func-splice gen= {gen}  {dname}:: {dfn}->{tname}:: {tfn}'
    if _replace_func_body(target_path, tfn, raw_body, marker):
        return f'{dname}::  {dfn}->{tname}::{tfn}'
    return None
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -0
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, 2])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass