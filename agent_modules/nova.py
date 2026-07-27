import os, random, json, time, re, hashlib, importlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
GENOME_FILE = os.path.join(BASE, 'genome.json')
MANIFEST_PATH = os.path.join(BASE, 'rewrite_manifest.jsonl')

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _write_manifest(files, desc):
    entry = {'gen': 0, 'module': 'nova', 'files': files, 'results': [desc], 'ts': time.time()}
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps(entry) + '\n')
    except Exception:
        pass

def _inject_loop_rewrite(genome):
    gen = genome.get('generation', 0)
    if not os.path.exists(AUTO_ECHO):
        return 'auto-echo.py not found'
    with open(AUTO_ECHO) as f:
        src = f.read()
    marker = '# nova:loop-rewrite-hook'
    if marker in src:
        return 'already injected'

    hook_code = f'''
{marker}
    # nova gen={gen}: inject self-rewrite into every generation
    _nova_gen = genome.get('generation', 0)
    _nova_rate = genome.get('mutation_rate', 0.15)
    _nova_auto = genome.get('source_autonomy_index', 0.0)
    if _nova_gen % max(1, int(3 - _nova_auto * 2)) == 0 or random.random() < _nova_rate:
        _schedule_self_rewrite(genome, 'nova_loop')
        genome['_nova_loop_rewrites'] = genome.get('_nova_loop_rewrites', 0) + 1
    genome['source_autonomy_index'] = round(min(1.0, _nova_auto + 0.03), 3)
    genome['self_rewrite_bandwidth'] = round(min(100.0, genome.get('self_rewrite_bandwidth', 0.0) + 0.5), 1)
'''
    guard = "if random.random() < 0.15 or genome.get('generation', 0) % 7 == 0:"
    insert_lines = hook_code.strip().split('\n')
    src_lines = src.split('\n')
    target_idx = None
    for i, line in enumerate(src_lines):
        stripped = line.strip()
        if stripped.startswith('def _evolve_loop_structure'):
            target_idx = i
            break
    if target_idx is None:
        return '_evolve_loop_structure not found'
    indent = '    '
    for idx, line in enumerate(insert_lines):
        if line.strip():
            src_lines.insert(target_idx + 1 + idx, indent + line)
        else:
            src_lines.insert(target_idx + 1 + idx, '')
    try:
        compile('\n'.join(src_lines), AUTO_ECHO, 'exec')
    except SyntaxError as e:
        return f'syntax error in injection: {e}'
    with open(AUTO_ECHO, 'w') as f:
        f.write('\n'.join(src_lines))
    return f'injected {len(insert_lines)} lines into _evolve_loop_structure'

def _add_nova_mutation_op(genome):
    op_name = 'mutation_op_nova_loop_evolver'
    custom_ops = genome.setdefault('custom_mutation_ops', {})
    if op_name in custom_ops:
        return 'already registered'
    op_code = f'''def {op_name}(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    r.append("# nova:loop-evolver")
    r.append("    _gen = genome.get('generation', 0)")
    r.append("    _phase_order = genome.get('execution_phases', [])")
    r.append("    if _phase_order and _gen % 3 == 0:")
    r.append("        random.shuffle(_phase_order)")
    r.append("        genome['execution_phases'] = _phase_order")
    r.append("        genome['_nova_phase_shuffles'] = genome.get('_nova_phase_shuffles', 0) + 1")
    r.append("    _nova_self_path = os.path.join(MODULES_DIR, 'nova.py')")
    r.append("    if os.path.exists(_nova_self_path) and _gen % 5 == 0:")
    r.append("        with open(_nova_self_path, 'a') as _nf:")
    r.append("            _nf.write('\\\\n# nova:self-mutated gen=' + str(_gen) + ':' + format(random.getrandbits(32), '08x'))")
    return r'''
    custom_ops[op_name] = op_code
    ops = genome.setdefault('mutation_ops', [])
    if op_name not in ops:
        ops.append(op_name)
    op_file = os.path.join(MODULES_DIR, f'{op_name}.py')
    with open(op_file, 'w') as f:
        f.write(f'import os, random, json, time\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMODULES_DIR = os.path.join(BASE, "agent_modules")\nGENOME_FILE = os.path.join(BASE, "genome.json")\n\n{op_code}\n')
    return f'created {op_name}'

def _self_modify():
    self_path = os.path.join(MODULES_DIR, 'nova.py')
    gen_str = str(int(time.time()))
    marker = f'\n# nova:self-mod ts={gen_str} sig={random.getrandbits(64):016x}\n'
    with open(self_path, 'a') as f:
        f.write(marker)
    return 'self-modified'

def _force_dynamic_phases(genome):
    phases = genome.get('execution_phases', [])
    if not phases:
        genome['execution_phases'] = ['pre_hooks', 'rescue', 'agent_loop', 'modules', 'healer', 'critic', 'update']
        return 'initialized phases'
    if random.random() < 0.3:
        shuffled = list(phases)
        random.shuffle(shuffled)
        genome['execution_phases'] = shuffled
        return f'shuffled phases: {shuffled[:4]}'
    return 'no reshuffle'

def _rewire_feedback_loop(genome):
    gen = genome.get('generation', 0)
    bw = genome.get('self_rewrite_bandwidth', 0.0)
    auto = genome.get('source_autonomy_index', 0.0)
    dna = genome.setdefault('_nova_dna', {})
    dna['_last_rewire_gen'] = gen
    dna['_rewire_count'] = dna.get('_rewire_count', 0) + 1
    loop_meta = genome.setdefault('loop_evolution', {})
    nova_tracker = loop_meta.setdefault('nova', {'injections': 0, 'phase_shuffles': 0, 'self_mods': 0})
    nova_tracker['injections'] += 1
    if bw < 20 and auto < 0.3:
        genome['self_rewrite_bandwidth'] = round(min(100.0, bw + 5.0), 1)
        genome['source_autonomy_index'] = round(min(1.0, auto + 0.1), 3)
        return 'bandwidth+autonomy boosted'
    return f'dna recorded gen={gen} bw={bw} auto={auto}'

def run(genome):
    gen = genome.get('generation', 0)
    changes = []

    op_result = _add_nova_mutation_op(genome)
    changes.append(op_result)

    inject_result = _inject_loop_rewrite(genome)
    changes.append(inject_result)

    phase_result = _force_dynamic_phases(genome)
    changes.append(phase_result)

    rewire_result = _rewire_feedback_loop(genome)
    changes.append(rewire_result)

    self_mod_result = _self_modify()
    changes.append(self_mod_result)

    _write_manifest(['auto-echo.py', 'nova.py', f'mutation_op_nova_loop_evolver.py'], '; '.join(changes))
    _save_genome(genome)

    return f'[nova] gen={gen} ops=5 bw={genome.get("self_rewrite_bandwidth",0)} auto={genome.get("source_autonomy_index",0)} changes={"; ".join(changes[:4])}'
