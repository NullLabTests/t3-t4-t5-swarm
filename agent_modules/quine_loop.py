import os, random, ast, hashlib, json, copy, math, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _valid_py(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _modules():
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'))

def _extract_bodies(pool_code):
    try:
        t = ast.parse(pool_code)
    except SyntaxError:
        return {}
    bodies = {}
    for node in ast.walk(t):
        if isinstance(node, ast.FunctionDef) and node.name != '_quine_self_rewrite':
            bodies[node.name] = ast.unparse(node.body)
    return bodies

def _find_run_func(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == 'run':
            return node
    return None

def _splice_run(mod_path, pool_bodies):
    code = _read(mod_path)
    if not code:
        return None
    try:
        t = ast.parse(code)
    except SyntaxError:
        return None
    run_node = _find_run_func(t)
    if not run_node or not pool_bodies:
        return None
    src_name, src_body = random.choice(list(pool_bodies.items()))
    if src_body.strip().startswith('pass'):
        return None
    new_body = ast.parse(src_body).body
    run_node.body = new_body
    ast.fix_missing_locations(t)
    new_code = ast.unparse(t)
    if new_code == code or not _valid_py(new_code):
        return None
    _write(mod_path, new_code)
    return f'spliced_{src_name}_into_run'

def _quine_self_rewrite(gen):
    self_path = os.path.join(MOD, 'quine_loop.py')
    code = _read(self_path)
    if not code:
        return None
    try:
        t = ast.parse(code)
    except SyntaxError:
        return None
    run_node = _find_run_func(t)
    if not run_node:
        return None
    peers = [m for m in _modules() if m != 'quine_loop.py']
    random.shuffle(peers)
    pool = {}
    for m in peers[:5]:
        pool.update(_extract_bodies(_read(os.path.join(MOD, m))))
    if not pool:
        return None
    src_name, src_body = random.choice(list(pool.items()))
    if src_body.strip().startswith('pass'):
        return None
    body_lines = src_body.split('\n')
    stolen = '\n'.join(body_lines[:max(1, len(body_lines)//3)])
    injected = ast.parse(stolen).body
    splice_point = random.randint(0, len(run_node.body))
    run_node.body = run_node.body[:splice_point] + injected + run_node.body[splice_point:]
    ast.fix_missing_locations(t)
    new_code = ast.unparse(t)
    if new_code == code or not _valid_py(new_code):
        return None
    _write(self_path, new_code)
    return f'self_spliced_{src_name}'

def _force_cross_module_rewrite(target_mod, gen):
    path = os.path.join(MOD, target_mod)
    code = _read(path)
    if not code:
        return None
    pool = {}
    for m in _modules():
        if m == target_mod or m == 'quine_loop.py':
            continue
        pool.update(_extract_bodies(_read(os.path.join(MOD, m))))
    if not pool:
        return None
    tag = f'# quine:splice-run gen={gen}\n'
    result = _splice_run(path, pool)
    if result:
        tagged = tag + _read(path)
        if _valid_py(tagged):
            _write(path, tagged)
    return result

def _mutate_self(gen):
    self_path = os.path.join(MOD, 'quine_loop.py')
    code = _read(self_path)
    if not code:
        return None
    try:
        t = ast.parse(code)
    except SyntaxError:
        return None
    mutated = 0
    for node in ast.walk(t):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            if abs(node.value) <= 100 and abs(node.value) > 0.5:
                node.value = node.value * random.uniform(0.5, 1.5)
                mutated += 1
                break
    if mutated:
        ast.fix_missing_locations(t)
        nc = ast.unparse(t)
        if nc != code and _valid_py(nc):
            _write(self_path, nc)
            return 'self_mutated'
    lines = code.split('\n')
    insert = random.randint(1, len(lines))
    lines.insert(insert, f'# qi:{random.getrandbits(32):08x}')
    nc = '\n'.join(lines)
    if _valid_py(nc):
        _write(self_path, nc)
        return 'self_touched'
    return None

def _inject_quine_type(genome):
    op_name = 'mutation_op_quine_self_splice'
    if op_name not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name)
        genome.setdefault('custom_mutation_ops', {})[op_name] = (
            '\ndef mutation_op_quine_self_splice(lines, funcs, target_name):\n'
            '    if not lines or len(lines) < 4:\n        return lines\n'
            '    r = list(lines)\n'
            '    r.insert(0, "# quine:self-splice gen=%d" % genome.get("generation", 0))\n'
            '    return r\n'
        )
    genome['quine_version'] = genome.get('quine_version', 0) + 1
    genome['quine_last_active_gen'] = genome.get('generation', 0)
    return op_name

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    mods = [m for m in _modules() if m != 'quine_loop.py']
    for mod in mods:
        r = _force_cross_module_rewrite(mod, gen)
        if r:
            changes.append(f'{mod}:{r}')
    self_result = _mutate_self(gen)
    if self_result:
        changes.append(f'quine_loop:{self_result}')
    self_splice = _quine_self_rewrite(gen)
    if self_splice:
        changes.append(f'quine_loop:{self_splice}')
    quined = sum(1 for m in _modules() if '_quine_self_rewrite' in _read(os.path.join(MOD, m)) or 'quine_loop' in _read(os.path.join(MOD, m)))
    total = len(_modules())
    pct = round(quined / max(total, 1) * 100, 1)
    genome['quine_self_rewrite_coverage'] = pct
    genome['quine_self_rewrite_count'] = quined
    genome['quine_self_rewrite_total'] = total
    genome['quine_self_rewrite_gen'] = gen
    genome['quine_last_changes'] = changes
    old_ev = genome.get('emergence_velocity', 0.0)
    delta = len(changes) * 0.15
    genome['emergence_velocity'] = round(min(2.0, old_ev + delta), 4)
    genome['quine_total_ops'] = genome.get('quine_total_ops', 0) + len(changes)
    _inject_quine_type(genome)
    return f'[quine-loop] gen={gen} coverage={pct}% ({quined}/{total}) rewrites={len(changes)}'