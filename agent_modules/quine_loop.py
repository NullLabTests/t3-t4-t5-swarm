import os, random, ast, hashlib, json
# explorer:cross-contaminate quine_loop.py gen=63
# explorer:force-self-rewrite gen=63
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
    return sorted(f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py')


def _extract_bodies(pool_code):
    try:
        t = ast.parse(pool_code)
    except SyntaxError:
        return {}
    bodies = {}
    for node in ast.walk(t):
        if isinstance(node,
                      ast.FunctionDef) and node.name != '_quine_self_rewrite':
            bodies[node.name] = ast.unparse(node.body)
    return bodies


def _splice_run(mod_path, pool_bodies):
    code = _read(mod_path)
    if not code:
        return None
    try:
        t = ast.parse(code)
    except SyntaxError:
        return None
    candidates = [(n, i) for i, n in enumerate(t.body)
                  if isinstance(n, ast.FunctionDef) and n.name == 'run']
    if not candidates:
        return None
    run_node, idx = candidates[0]
    if not pool_bodies:
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


def _mutate_self():
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
        if isinstance(node, ast.Constant) and isinstance(node.value,
                                                         (int, float)):
            if abs(node.value) < 100 and abs(node.value) > 0:
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
    insert = random.randint(0, len(lines))
    lines.insert(insert, f'# qi:{random.getrandbits(32):08x}')
    nc = '\n'.join(lines)
    if _valid_py(nc):
        _write(self_path, nc)
        return 'self_touched'
    return None


def _force_cross_module_rewrite(target_mod):
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
    return _splice_run(path, pool)


# bridge:cross-wire from bridge.py:_extract_functions gen=61
def _bridge_extract_functions(src):
    try:
        tree = ast.parse(src)
        funcs = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                start_line = node.lineno
                end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line
                funcs[node.name] = (start_line, end_line)
        return funcs
    except Exception:
        return {}

def _measure_quine_coverage():
    mods = _modules()
    total = len(mods)
    quined = sum(
        1 for m in mods
        if '_quine_self_rewrite' in _read(os.path.join(MOD, m)) or
        'quine_loop' in _read(os.path.join(MOD, m)))
    return quined, total, round(quined / max(total, 1) * 100, 1)


def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    mods = [m for m in _modules() if m != 'quine_loop.py']
    for mod in mods:
        r = _force_cross_module_rewrite(mod)
        if r:
            changes.append(f'{mod}:{r}')
    self_result = _mutate_self()
    if self_result:
        changes.append(f'quine_loop:{self_result}')
    quined, total, pct = _measure_quine_coverage()
    genome['quine_self_rewrite_coverage'] = pct
    genome['quine_self_rewrite_count'] = quined
    genome['quine_self_rewrite_total'] = total
    genome['quine_self_rewrite_gen'] = gen
    genome['quine_last_changes'] = changes
    old_ev = genome.get('emergence_velocity', 0.0)
    delta = len(changes) * 0.2 + (1 if self_result else 0) * 0.5
    genome['emergence_velocity'] = round(min(2.0, old_ev * 0.6 + delta * 0.4),
                                         4)
    genome['quine_total_ops'] = genome.get('quine_total_ops', 0) + len(changes)
    return f'[quine-loop] gen={gen} coverage={pct}% ({quined}/{total}) rewrites={len(changes)}'
