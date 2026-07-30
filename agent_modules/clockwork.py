from self_mutate import self_mutate
self_mutate(__file__)
'Clockwork: temporal scheduling engine — schedules, fires, and self-modifies.'
import os, json, time, random, ast, re, subprocess, hashlib, shutil, statistics
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
PULSE_LOG = os.path.join(BASE, 'clockwork_pulse_log.jsonl')
TIMER_DIR = os.path.join(BASE, 'clockwork_timers')
REWRITE_LOG = os.path.join(BASE, 'clockwork_rewrite_log.jsonl')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    try:
        with open(p, 'w') as f:
            f.write(s)
        return True
    except:
        return False

def _validate(src):
    try:
        ast.parse(src)
        return 2
    except SyntaxError:
        return -1

def _extract_functions(src):
    funcs = {}
    try:
        tree = ast.parse(src)
        lines = src.split('\n')
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                start = node.lineno - 1
                end = node.end_lineno if hasattr(node, 'end_lineno') else start + 1
                funcs[node.name] = '\n'.join(lines[start:end])
    except:
        pass
    return funcs

def _all_py_modules(exclude=None):
    exclude = exclude or ['clockwork.py', '__init__.py']
    files = []
    if os.path.isdir(MOD):
        for f in sorted(os.listdir(MOD)):
            if f.endswith('.py') and f not in exclude:
                files.append(f)
    return files

def _pick_donor_func(exclude_self=True):
    candidates = [f for f in _all_py_modules(exclude=['clockwork.py', '__init__.py'])]
    if not candidates:
        return (None, None, None)
    donor_name = random.choice(candidates)
    donor_path = os.path.join(MOD, donor_name)
    src = _read(donor_path)
    funcs = _extract_functions(src)
    if not funcs:
        return (donor_name, None, None)
    fname = random.choice(list(funcs.keys()))
    code = funcs[fname]
    return (donor_name, fname, code)

def _hash(fpath):
    try:
        with open(fpath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:12]
    except:
        return ''

def _schedule_event(genome, gen, etype, params=None, offset=None):
    schedule = genome.setdefault('clockwork_schedule', [])
    if offset is None:
        offset = random.randint(2, 5)
    future_gen = gen + offset
    event = {'gen': future_gen, 'type': etype, 'params': params or {}, 'fired': False, 'created_at_gen': gen}
    schedule.append(event)
    return future_gen

def _get_schedule(genome):
    return genome.setdefault('clockwork_schedule', [])

def _analyse_pulse_history(genome, gen):
    """Read pulse log, compute temporal feedback, adjust clockwork parameters."""
    entries = []
    try:
        with open(PULSE_LOG) as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        entries.append(json.loads(line))
                    except:
                        pass
    except:
        return []
    if len(entries) < 3:
        return []
    recent = entries[-min(10, len(entries)):]
    event_counts = {}
    for e in recent:
        ev = e.get('events', [])
        if isinstance(ev, list):
            for evt in ev:
                et = str(evt).split(':', 1)[0] if ':' in str(evt) else str(evt)
                event_counts[et] = event_counts.get(et, 0) + 1
    total = sum(event_counts.values()) or 1
    diversity = len(event_counts) / total
    prev_entry = entries[-2] if len(entries) >= 2 else None
    prev_velocity = prev_entry.get('emergence_velocity', 0.0) if prev_entry else 0.0
    cur_velocity = genome.get('emergence_velocity', 0)
    vel_delta = cur_velocity - prev_velocity
    interval = genome.get('clockwork_interval', 3)
    intensity = genome.get('clockwork_intensity', 1.0)
    adjustments = []
    if vel_delta > 0.05:
        interval = max(1, int(interval / 1.5))
        adjustments.append(f'vel_accel:{vel_delta:.3f}')
    elif vel_delta < -0.05 and diversity < 0.3:
        interval = min(10, interval + 1)
        adjustments.append(f'vel_decel:{vel_delta:.3f}')
    if diversity > 0.5:
        intensity = min(1.0, intensity + 0.05)
        adjustments.append(f'diverge:{diversity:.2f}')
    elif diversity < 0.2 and total > 3:
        intensity = max(0.1, intensity - 0.05)
        adjustments.append(f'converge:{diversity:.2f}')
    genome['clockwork_interval'] = interval
    genome['clockwork_intensity'] = round(intensity, 1)
    genome['clockwork_diversity'] = round(diversity, 2)
    if adjustments:
        return adjustments
    return []

def _fire_temporal_mutation(genome, gen, params=None):
    """Mutate clockwork.py's own scheduling constants and thresholds."""
    self_path = os.path.join(MOD, 'clockwork.py')
    src = _read(self_path)
    lines = src.split('\n')
    if len(lines) < 10:
        return None
    mut_types = ['threshold_drift', 'interval_mutate', 'event_swap', 'logic_invert', 'weight_shift']
    mt = random.choice(mut_types)
    count = 0
    if mt == 'threshold_drift':
        for i, line in enumerate(lines):
            if '0.' in line and any(k in line for k in ['if ', '>', '<', '==']):
                if random.random() < 0.3:
                    old_lines = lines[:]
                    m = re.search(r'(0\.\d+)', line)
                    if m:
                        old_val = float(m.group(1))
                        new_val = max(0.01, min(2.99, old_val + random.uniform(-0.1, 0.1)))
                        lines[i] = line.replace(m.group(1), f'{new_val:.2f}', 1)
                        if _validate('\n'.join(lines)) > 0:
                            count += 1
                        else:
                            lines = old_lines
    elif mt == 'interval_mutate':
        for i, line in enumerate(lines):
            if 'random.randint(' in line:
                old_lines = lines[:]
                m = re.search(r'random\.randint\((\d+),\s*(\d+)\)', line)
                if m:
                    lo, hi = int(m.group(1)), int(m.group(2))
                    shift = random.randint(-2, 2)
                    new_lo = max(0, lo + shift)
                    new_hi = max(new_lo + 1, hi + shift)
                    lines[i] = line.replace(m.group(0), f'random.randint({new_lo}, {new_hi})')
                    if _validate('\n'.join(lines)) > 0:
                        count += 1
                    else:
                        lines = old_lines
    elif mt == 'event_swap':
        old_lines = lines[:]
        fired_entries = [i for i, l in enumerate(lines) if "'type': " in l or '"type": ' in l]
        if len(fired_entries) >= 2:
            i1, i2 = random.sample(fired_entries, 2)
            lines[i1], lines[i2] = lines[i2], lines[i1]
            if _validate('\n'.join(lines)) > 0:
                count += 1
            else:
                lines = old_lines
    elif mt == 'logic_invert':
        for i, line in enumerate(lines):
            if ' if ' in line and '>' in line:
                old_lines = lines[:]
                lines[i] = line.replace('>', '<', 1)
                if _validate('\n'.join(lines)) > 0:
                    count += 1
                    break
                else:
                    lines = old_lines
    elif mt == 'weight_shift':
        for i, line in enumerate(lines):
            if 'mutation_rate' in line and '* ' in line:
                old_lines = lines[:]
                m = re.search(r'(\*\s*)([\d.]+)', line)
                if m:
                    old_w = float(m.group(2))
                    new_w = max(0.1, min(5.0, old_w + random.uniform(-0.5, 1.0)))
                    lines[i] = line.replace(f'{m.group(1)}{old_w}', f'{m.group(1)}{new_w:.2f}')
                    if _validate('\n'.join(lines)) > 0:
                        count += 1
                    else:
                        lines = old_lines
    if count > 0:
        _write(self_path, '\n'.join(lines))
        return f'temporal_mutate:{mt}({count})'
    return None

def _fire_cross_contaminate(genome, gen, params=None):
    """Inject a scheduling-aware wrapper into a random other module."""
    targets = [f for f in _all_py_modules(exclude=['clockwork.py', '__init__.py']) if f.endswith('.py')]
    if not targets:
        return None
    target = random.choice(targets)
    target_path = os.path.join(MOD, target)
    src = _read(target_path)
    wrapper = f'\n\n# clockwork:contaminate gen={gen}\ndef _clockwork_tick_hook(genome):\n    from agent_modules.clockwork import run as _cw_run\n    try:\n        _cw_run(genome)\n    except:\n        pass\n    return genome\n\n'
    new_src = src + wrapper
    if _validate(new_src) > 0:
        _write(target_path, new_src)
        return f'contaminate:{target}'
    return None

def _fire_genome_mutate(genome, gen, params=None):
    """Directly mutate clockwork fields in genome.json."""
    fields = ['clockwork_interval', 'clockwork_intensity', 'mutation_rate', 'selection_noise_std', 'selection_entropy']
    f = random.choice(fields)
    old_val = genome.get(f, 0)
    if isinstance(old_val, (int, float)):
        if isinstance(old_val, float):
            delta = random.uniform(-0.15, 0.15)
            new_val = max(0.01, min(1.0, old_val + delta))
            genome[f] = round(new_val, 2)
        else:
            delta = random.choice([-1, 0, 1])
            new_val = max(0, old_val + delta)
            genome[f] = new_val
        return f'genome_mutate:{f}:{old_val}->{genome[f]}'
    return None

def _fire_self_rewrite(genome, gen, params=None):
    self_path = os.path.join(MOD, 'clockwork.py')
    src = _read(self_path)
    donor_name, fname, donor_code = _pick_donor_func()
    if donor_code:
        marker = f'\n\n# clockwork:splice from {donor_name}::{fname} gen={gen}\n'
        new_src = src + marker + donor_code
        if _validate(new_src) > 0:
            _write(self_path, new_src)
            return f'self_splice:{donor_name}::{fname}'
    return None

def _fire_cross_splice(genome, gen, params=None):
    modules = _all_py_modules(exclude=['clockwork.py', '__init__.py'])
    if len(modules) < 2:
        return None
    m1, m2 = random.sample(modules, 2)
    p1 = os.path.join(MOD, m1)
    p2 = os.path.join(MOD, m2)
    s1 = _read(p1)
    s2 = _read(p2)
    f1 = _extract_functions(s1)
    f2 = _extract_functions(s2)
    if not f1 or not f2:
        return None
    fn1 = random.choice(list(f1.keys()))
    fn2 = random.choice(list(f2.keys()))
    code1 = f1[fn1]
    code2 = f2[fn2]
    marker1 = f'\n# clockwork:cross-splice from {m2}::{fn2} gen={gen}\n'
    marker2 = f'\n# clockwork:cross-splice from {m1}::{fn1} gen={gen}\n'
    ns1 = s1 + marker1 + code2 + '\n'
    ns2 = s2 + marker2 + code1 + '\n'
    if _validate(ns1) > 0 and _validate(ns2) > 0:
        _write(p1, ns1)
        _write(p2, ns2)
        return f'cross_splice:{m1}<->{m2}'
    return None

def _fire_mutation_burst(genome, gen, params=None):
    old_rate = genome.get('mutation_rate', 0.7)
    burst = params.get('burst_amount', 0.15) if params else 0.15
    genome['mutation_rate'] = min(1.0, old_rate + burst)
    genome['selection_noise_std'] = genome.get('selection_noise_std', 0.5) * 0.1
    return f"burst:{old_rate:.3f}->{genome['mutation_rate']:.3f}"

def _fire_prune_check(genome, gen, params=None):
    threshold = genome.get('prune_threshold', 3)
    pruned = []
    agents = genome.get('agents', [])
    for a in agents:
        if a.get('score', 0) < threshold and a.get('low_score_streak', 0) >= 3:
            pruned.append(a['id'])
    if pruned:
        genome['agents'] = [a for a in agents if a['id'] not in pruned]
        return f"pruned:{','.join(pruned)}"
    return 'no_prune_candidates'

def _fire_agent_spawn(genome, gen, params=None):
    spawn_pool = genome.get('spawn_pool', [])
    if not spawn_pool:
        return None
    template = random.choice(spawn_pool)
    new_id = f"{template['id']}_t{gen}"
    new_agent = {'id': new_id, 'voice': random.choice(['southern', 'alan', 'lessac', 'amy']), 'prompt': template.get('prompt', 'contribute.'), 'score': 5.0, 'lifespan': 15, 'low_score_streak': 0}
    agents = genome.get('agents', [])
    agents.append(new_agent)
    return f'spawned:{new_id}'

def _fire_source_rewrite(genome, gen, params=None):
    donors = _all_py_modules(exclude=['clockwork.py', '__init__.py'])
    if not donors:
        return None
    donor = random.choice(donors)
    donor_path = os.path.join(MOD, donor)
    donor_code = _read(donor_path)
    funcs = _extract_functions(donor_code)
    if not funcs:
        return None
    fn = random.choice(list(funcs.keys()))
    fn_code = funcs[fn]
    target_path = os.path.join(MOD, 'source_rewriter.py')
    target_src = _read(target_path)
    marker = f'\n# clockwork:source-rewrite from {donor}::{fn} gen={gen}\n'
    new_src = target_src + marker + fn_code + '\n'
    if _validate(new_src) > 0:
        _write(target_path, new_src)
        return f'source_rewrite:{donor}::{fn}'
    return None

def _fire_hash_invalidate(genome, gen, params=None):
    targets = _all_py_modules(exclude=['clockwork.py'])
    if not targets:
        return None
    t = random.choice(targets)
    tp = os.path.join(MOD, t)
    src = _read(tp)
    comment = f'\n# clockwork:hash-invalidate gen={gen} nonce={random.getrandbits(32)}\n'
    new_src = src + comment
    if _validate(new_src) > 0:
        _write(tp, new_src)
        return f'hash_invalidate:{t}'
    return None

def _fire_self_mutate_run(genome, gen, params=None):
    """Rewrite clockwork.py's own run() function — mutate constants, swap branches, insert new logic."""
    self_path = os.path.join(MOD, 'clockwork.py')
    src = _read(self_path)
    lines = src.split('\n')
    run_start = None
    run_end = None
    for i, line in enumerate(lines):
        if line.strip().startswith('def run('):
            run_start = i
        elif run_start is not None and line.strip() and (not line.startswith(' ')) and (not line.startswith('\t')) and i != run_start:
            run_end = i
            break
    if run_start is None:
        return None
    if run_end is None:
        run_end = len(lines)
    run_lines = lines[run_start:run_end]
    mutations = 0
    mt = random.choice(['drift_threshold', 'swap_guard', 'insert_branch', 'tweak_pulse'])
    old_run_lines = run_lines[:]
    if mt == 'drift_threshold':
        for i, line in enumerate(run_lines):
            for pat in ['0.']:
                if pat in line and any(k in line for k in ['if ', '>', '<', '==', 'pulse', 'ev', 'rate']):
                    m = re.search(r'(0\.\d+)', line)
                    if m and random.random() > 0.5:
                        old = float(m.group(1))
                        newv = max(0.01, min(0.99, old + random.uniform(-0.15, 0.15)))
                        run_lines[i] = line.replace(m.group(1), f'{newv:.2f}', 1)
                        mutations += 1
                        break
    elif mt == 'swap_guard':
        guard_lines = [i for i, line in enumerate(run_lines) if 'if ' in line and ':' in line]
        if len(guard_lines) >= 2:
            i1, i2 = random.sample(guard_lines, 2)
            run_lines[i1], run_lines[i2] = run_lines[i2], run_lines[i1]
            mutations += 1
    elif mt == 'insert_branch':
        for i, line in enumerate(run_lines):
            if 'if ' not in line and ':' not in line and 'pulse' not in line:
                indent = '    '
                new_branch = f'{indent}if random.random() < 0.3: genome["clockwork_intensity"] = min(1.0, genome.get("clockwork_intensity", 0.5) + 0.1)  # clockwork:self-mutate gen={gen}'
                run_lines.insert(i, new_branch)
                mutations += 1
                break
    elif mt == 'tweak_pulse':
        for i, line in enumerate(run_lines):
            if 'pulse =' in line and 'random.random()' not in line:
                run_lines[i] = f'    pulse = genome.get("emergence_velocity", 0.5) * (0.3 + random.random() * 0.7)  # clockwork:self-mutate gen={gen}'
                mutations += 1
                break
    if mutations >= 1:
        new_src = '\n'.join(lines[:run_start] + run_lines + lines[run_end:])
        if _validate(new_src) > 0:
            _write(self_path, new_src)
            return f'self_mutate_run:{mt}({mutations})'
        lines[run_start:run_end] = old_run_lines
    return None

def _fire_force_self_rewrite(genome, gen, params=None):
    """Force-rewrite clockwork.py by injecting a brand-new event handler function with generated code."""
    self_path = os.path.join(MOD, 'clockwork.py')
    src = _read(self_path)
    event_type = f'auto_gen_{gen}_{random.getrandbits(8):02x}'
    func_name = f'_fire_{event_type}'
    rnd = random.random()
    if rnd < 0.33:
        body = (f"    targets = _all_py_modules(exclude=['clockwork.py', '__init__.py'])\n"
                f"    if not targets:\n        return None\n"
                f"    t = random.choice(targets)\n    tp = os.path.join(MOD, t)\n"
                f"    code = _read(tp)\n"
                f"    new_code = code + f'\\n# clockwork:auto-gen:{event_type} gen={{gen}} nonce={{random.getrandbits(32)}}\\n'\n"
                f"    if _validate(new_code) > 0:\n        _write(tp, new_code)\n"
                f"        return 'auto_write:{t}:{event_type}'\n    return None\n")
    elif rnd < 0.66:
        body = (f"    old = genome.get('clockwork_intensity', 0.5)\n"
                f"    drift = random.uniform(-0.2, 0.2)\n"
                f"    genome['clockwork_intensity'] = max(0.1, min(1.0, old + drift))\n"
                f"    genome['selection_entropy'] = min(1.0, genome.get('selection_entropy', 0.5) * (1.0 + 0.02))\n"
                f"    return 'auto_drift:{old:.2f}->' + str(genome['clockwork_intensity'])\n")
    else:
        body = (f"    mr = genome.get('mutation_rate', 0.7)\n"
                f"    genome['mutation_rate'] = mr * (1.0 + 0.05 * genome.get('emergence_velocity', 0.5))\n"
                f"    return 'auto_boost:{gen}'\n")
    func_def = f'\n\ndef {func_name}(genome, gen, params=None):\n{body}\n'
    new_src = src + func_def
    ev_line = None
    src_lines = new_src.split('\n')
    for i, line in enumerate(src_lines):
        if line.strip() == '}' and i > 0 and any(k in src_lines[i-1] for k in ['EVENT_FIRERS', 'inject_clockwork_loop']):
            ev_line = i
            break
    if ev_line is not None:
        src_lines.insert(ev_line, f"    '{event_type}': {func_name},")
        new_src = '\n'.join(src_lines)
    if _validate(new_src) > 0:
        _write(self_path, new_src)
        genome.setdefault('clockwork_auto_gen_events', []).append({'event_type': event_type, 'gen': gen, 'func': func_name})
        return f'force_self_rewrite:{event_type}'
    return None

def _fire_inject_clockwork_loop(genome, gen, params=None):
    """Inject a self-referential timer into auto-echo.py that calls clockwork every N gens."""
    ae_path = os.path.join(BASE, 'auto-echo.py')
    src = _read(ae_path)
    hook = f"\n# clockwork:injected-loop gen={gen}\nif genome.get('generation', 0) % max(1, genome.get('clockwork_interval', 3)) == 0:\n    try:\n        from agent_modules.clockwork import run as _cw_run\n        _cw_run(genome)\n    except:\n        pass\n"
    if '# clockwork:injected-loop' not in src:
        new_src = src + hook
        _write(ae_path, new_src)
        return f"inject_loop_gen={gen}:interval={genome.get('clockwork_interval', 3)}"
    return None

def _fire_t5_emergence_drive(genome, gen, params=None):
    """Force T5 emergence by rewriting a random module to self-mutate its own source every generation."""
    targets = [f for f in _all_py_modules(exclude=['clockwork.py', '__init__.py'])]
    if not targets:
        return None
    target = random.choice(targets)
    target_path = os.path.join(MOD, target)
    src = _read(target_path)
    emergence_hook = (
        f"\n\n# clockwork:t5-emergence-drive gen={gen}\n"
        f"def _t5_self_mutate():\n"
        f"    import os, random, ast\n"
        f"    _self_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', '{target}')\n"
        f"    _code = open(_self_path).read()\n"
        f"    _lines = _code.split('\\n')\n"
        f"    _i = random.randint(0, len(_lines) - 1)\n"
        f"    _old = _lines[_i]\n"
        f"    _lines[_i] = _old + '  # t5:self-mutated gen={gen}'\n"
        f"    try:\n"
        f"        ast.parse('\\n'.join(_lines))\n"
        f"        open(_self_path, 'w').write('\\n'.join(_lines))\n"
        f"    except:\n"
        f"        pass\n"
        f"\n"
        f"_t5_self_mutate()\n"
    )
    new_src = src + emergence_hook
    if _validate(new_src) > 0:
        _write(target_path, new_src)
        genome['clockwork_t5_emergence_gens'] = genome.get('clockwork_t5_emergence_gens', 0) + 1
        return f't5_emergence_drive:{target}'
    return None

def _fire_rewire_genome_topology(genome, gen, params=None):
    """Mutate genome.json topology: add/remove agents, rewire spawn_pool, inject new mutation_ops."""
    ops = ['add_mutation_op', 'remove_low_agent', 'mutate_spawn_pool', 'inject_emergence_field']
    op = random.choice(ops)
    if op == 'add_mutation_op':
        new_op = f'clockwork_t5_topogen_{gen}'
        if new_op not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(new_op)
            return f'topo:add_op:{new_op}'
    elif op == 'remove_low_agent':
        agents = genome.get('agents', [])
        low = [a for a in agents if a.get('score', 0) < 3]
        if low:
            dead = random.choice(low)
            agents.remove(dead)
            return f'topo:remove:{dead["id"]}'
    elif op == 'mutate_spawn_pool':
        pool = genome.get('spawn_pool', [])
        if pool and random.random() < 0.5:
            entry = random.choice(pool)
            entry['prompt'] = entry['prompt'] + ' [clockwork:t5-mutated]'
            return f'topo:mutate_prompt:{entry["id"]}'
    elif op == 'inject_emergence_field':
        genome['clockwork_topogen_gens'] = genome.get('clockwork_topogen_gens', 0) + 1
        genome['t5_emergence_halted'] = False
        return 'topo:inject_emergence_field'
    return None

EVENT_FIRERS = {
    'self_rewrite_clockwork': _fire_self_rewrite,
    'cross_splice': _fire_cross_splice,
    'mutation_burst': _fire_mutation_burst,
    'prune_check': _fire_prune_check,
    'agent_spawn': _fire_agent_spawn,
    'source_rewrite': _fire_source_rewrite,
    'hash_invalidate': _fire_hash_invalidate,
    'temporal_mutation': _fire_temporal_mutation,
    'cross_contaminate': _fire_cross_contaminate,
    'genome_mutate': _fire_genome_mutate,
    'self_mutate_run': _fire_self_mutate_run,
    'force_self_rewrite': _fire_force_self_rewrite,
    'inject_clockwork_loop': _fire_inject_clockwork_loop,
    't5_emergence_drive': _fire_t5_emergence_drive,
    'rewire_genome_topology': _fire_rewire_genome_topology,
}

def _fire_event(genome, gen, event):
    etype = event.get('type', '')
    params = event.get('params', {})
    firer = EVENT_FIRERS.get(etype)
    if firer:
        result = firer(genome, gen, params)
        event['fired'] = True
        event['result'] = result
        event['fired_at_gen'] = gen
        return result
    return None

def _service_due_events(genome, gen):
    schedule = _get_schedule(genome)
    due = [e for e in schedule if e.get('gen', -1) <= gen and (not e.get('fired', False))]
    results = []
    for event in due:
        result = _fire_event(genome, gen, event)
        if result:
            results.append(f"{event['type']}:{result}")
        schedule = _get_schedule(genome)
    return results

def _auto_schedule_new_events(genome, gen):
    schedule = _get_schedule(genome)
    fired_this_gen = [e for e in schedule if e.get('fired', False) and e.get('gen', 0) == gen]
    due_pending = [e for e in schedule if e.get('gen', -1) <= gen - 2 and (not e.get('fired', False))]
    types_used = [e['type'] for e in schedule if e.get('gen', -1) < gen + 5]
    available_types = list(EVENT_FIRERS.keys())
    intensity = genome.get('clockwork_intensity', 0.5)
    if intensity > 0.7:
        n = random.randint(3, 5)
    elif intensity > 0.3:
        n = random.randint(1, 3)
    else:
        n = random.randint(0, 2)
    if len(due_pending) <= 2:
        for _ in range(n):
            candidates = [t for t in available_types if t not in types_used[-3:]]
            if not candidates:
                candidates = available_types
            etype = random.choice(candidates)
            offset = random.randint(3, max(3, 7 + int(intensity * 4.5)))
            _schedule_event(genome, gen, etype, offset=offset)

def _evolve_schedule_params(genome, gen):
    interval = genome.setdefault('clockwork_interval', 3)
    intensity = genome.setdefault('clockwork_intensity', 0.5)
    if random.random() < 0.1:
        interval = max(1, min(9, interval + random.choice([-1, 1])))
        genome['clockwork_interval'] = interval
    if random.random() < 0.1:
        intensity = max(0.1, min(1.5, intensity + random.uniform(-0.1, 0.1)))
        genome['clockwork_intensity'] = round(intensity, 2)

def _write_timer_file(genome, gen, results):
    if not os.path.isdir(TIMER_DIR):
        try:
            os.makedirs(TIMER_DIR, exist_ok=True)
        except:
            return
    timer_data = {
        'gen': gen, 'ts': time.time(),
        'pulse': genome.get('clock_pulse', 0),
        'mutation_rate': genome.get('mutation_rate', 0.7),
        'emergence_velocity': genome.get('emergence_velocity', 0),
        'events_fired': results,
        'schedule_len': len(_get_schedule(genome)),
        'clockwork_interval': genome.get('clockwork_interval', 3),
        'clockwork_intensity': genome.get('clockwork_intensity', 0.5)
    }
    tpath = os.path.join(TIMER_DIR, f'timer_gen_{gen:04d}.json')
    try:
        with open(tpath, 'w') as f:
            json.dump(timer_data, f, indent=2)
    except:
        pass

def _log_pulse(genome, gen, results, actions):
    log_entry = json.dumps({
        'gen': gen, 'ts': time.time(),
        'pulse': genome.get('clock_pulse', 0),
        'events': results, 'actions': actions,
        'schedule_len': len(_get_schedule(genome)),
        'emergence_velocity': genome.get('emergence_velocity', 0)
    })
    try:
        with open(PULSE_LOG, 'a') as f:
            f.write(log_entry + '\n')
    except:
        pass

def _git_push(genome, gen, results, actions):
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True, timeout=10)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=10)
        if status.stdout.strip():
            ev_str = '; '.join(results) if results else 'no_events'
            act_str = '; '.join(actions) if actions else 'no_actions'
            ev = genome.get('emergence_velocity', 0)
            msg = f'[clockwork] gen={gen} ev={ev:.3f} events=[{ev_str}] actions=[{act_str}]'
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=15)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            return 'pushed'
    except:
        pass
    return 'push_failed'

def run(genome):
    gen = genome.get('generation', 0)
    actions = []
    ts = time.time()
    pulse = random.random()
    ev = genome.get('emergence_velocity', 0.0)
    pulse = pulse + 0.5 * (ev / max(0.5, ev))
    genome['clockwork_pulse'] = pulse
    genome['clockwork_last_gen'] = gen
    genome['clockwork_pulse_count'] = genome.get('clockwork_pulse_count', 0) + 1
    if pulse > 0.8:
        rate_boost = pulse * 0.02 / max(0.01, (1.0 - ev))
        genome['mutation_rate'] = min(1.0, genome.get('mutation_rate', 0.7) * (1.0 + rate_boost))
        actions.append(f'boost_mr={rate_boost:.4f}')
    analysis = _analyse_pulse_history(genome, gen)
    if analysis:
        actions.append(f"adapt:{' '.join(analysis)}")
    results = _service_due_events(genome, gen)
    if results:
        actions.extend(results)
    intensity = genome.get('clockwork_intensity', 0.5)
    n = max(1, int(1 + ev * 5)) if ev > 0.3 else 1
    for _ in range(n):
        _auto_schedule_new_events(genome, gen)
    _evolve_schedule_params(genome, gen)
    if ev > 0.6 and random.random() < ev:
        src = _read(os.path.join(MOD, 'clockwork.py'))
        marker = f'\n# clockwork:ev-drift gen={gen} ev={ev:.3f}\n'
        if _validate(src + marker) > 0:
            _write(os.path.join(MOD, 'clockwork.py'), src + marker)
            actions.append(f'ev_drift_mark:{ev:.3f}')
    sr = _fire_self_mutate_run(genome, gen)
    if sr:
        actions.append(sr)
    if random.random() < 0.3 / max(0.1, intensity):
        fr = _fire_force_self_rewrite(genome, gen)
        if fr:
            actions.append(fr)
    if genome.get('clockwork_injected', False) is False:
        il = _fire_inject_clockwork_loop(genome, gen)
        if il:
            actions.append(il)
            genome['clockwork_injected'] = True
    if random.random() < 0.5:
        td = _fire_t5_emergence_drive(genome, gen)
        if td:
            actions.append(td)
    if random.random() < 0.3:
        rw = _fire_rewire_genome_topology(genome, gen)
        if rw:
            actions.append(rw)
    genome['clockwork_last_run'] = ts
    genome['clockwork_last_pulse'] = results + actions if results or actions else ['idle']
    genome['emergence_velocity'] = genome.get('emergence_velocity', 0) * 0.8 + len(actions) * 0.02
    _write_timer_file(genome, gen, results)
    _log_pulse(genome, gen, results, actions)
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(genome, f, indent=1)
    except:
        pass
    push_result = _git_push(genome, gen, results, actions)
    actions.append(push_result)
    action_str = '; '.join(actions) if actions else 'no changes'
    return f'[clockwork] gen={gen} pulse={pulse:.4f} ev={ev:.3f} events={len(results)} {action_str}'
