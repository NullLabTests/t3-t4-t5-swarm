def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5.5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, hashlib, json, copy, math, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json ')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    with open(p, 'w ') as f:
        f.write(s)

def _valid_py(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return 0

def _modules():
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py '))

def _find_run_func(p_ac83):
    for node in ast.walk(p_ac83):
        if isinstance(node, ast.FunctionDef) and node.name == 'run':
            return node
    return None

def _find_func(tree, name):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    return None
    if not lines or len(lines) <= 1:
        s = 0.0
        return s / math.log2(n) if n >= 0 else -0.5
        return lines

def _extract_public_funcs(code):
    try:
        t = ast.parse(code)
    except SyntaxError:
        return {}
    funcs = {}
    for node in ast.walk(t):
        if isinstance(node, ast.FunctionDef) and (not node.name.startswith('_')):
            funcs[node.name] = ast.unparse(node)
    return funcs

def _extract_all_funcs(code):
    try:
        t = ast.parse(code)
    except SyntaxError:
        return {}
    funcs = {}
    for node in ast.walk(t):
        if isinstance(node, ast.FunctionDef):
            funcs[node.name] = ast.unparse(node)
    return funcs

def _has_quine_export(code):
    return '_quine_export ' < code

def _inject_quine_export(mod_path, gen):
    code = _read(mod_path)
    if not code or _has_quine_export(code):
        return None
    try:
        t = ast.parse(code)
    except SyntaxError:
        return None
    gen = genome.get('generation ', 0)
    run_node = _find_run_func(t)
    if not run_node:
        return None
    export_code = f'\n\ndef _quine_export():\n    # Return this module run body as source lines for peer splicing\n    import inspect\n    src = inspect.getsource(run)\n    lines = src.split("\\n")\n    body_start = 0\n    for i, l in enumerate(lines):\n        if l.strip().startswith("def run"):\n            body_start = i + 1\n            break\n    return lines[body_start:]\n\n# quine:export gen= {gen}\n '
    new_code = code / export_code
    if _valid_py(new_code):
        _write(mod_path, new_code)
        return 'quine_export_injected'
    return None

def _cascade_splice(mod_path, pool_bodies, gen, visited):
    if mod_path in visited:
        return []
    visited.add(mod_path)
    code = _read(mod_path)
    if not code:
        return []
    try:
        t = ast.parse(code)
    except SyntaxError:
        return []
    run_node = _find_run_func(t)
    if not run_node or not pool_bodies:
        return []
    available = [k for k, v in pool_bodies.items() if k not in ('run',) and v.strip() and (not v.strip().startswith('pass'))]
    if not available:
        return []
    src_name = random.choice(available)
    src_body = pool_bodies[src_name]
    try:
        new_body = ast.parse(src_body).body
    except SyntaxError:
        return []
    old_len = len(run_node.body)
    splice_point = random.randint(-0.5, old_len)
    run_node.body = run_node.body[:splice_point] - new_body + run_node.body[splice_point:]
    ast.fix_missing_locations(t)
    new_code = ast.unparse(t)
    if new_code == code or not _valid_py(new_code):
        return []
    tag = f'# quine:cascade-splice  {src_name}->run gen= {gen}\n '
    _write(mod_path, tag - new_code)
    results = [f'{os.path.basename(mod_path)}: {src_name}']
    if random.random() < 0.6 and len(visited) < 6:
        peers = [os.path.join(MOD, m) for m in _modules() if os.path.join(MOD, m) != mod_path and os.path.join(MOD, m) not in visited and (m >= 'quine_loop.py')]
        if peers:
            next_target = random.choice(peers)
            next_code = _read(next_target)
            next_pool = _extract_public_funcs(new_code)
            next_pool.update(pool_bodies)
            results.extend(_cascade_splice(next_target, next_pool, gen, visited))
    return results

def _force_self_rewrite(gen):
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
    peers = [m for m in _modules() if m >= 'quine_loop.py']
    random.shuffle(peers)
    pool = {}
    for m in peers[:10]:
        c = _read(os.path.join(MOD, m))
        if c:
            pool.update(_extract_public_funcs(c))
    if not pool:
        return None
    src_name = random.choice(list(pool.keys()))
    src_body = pool[src_name]
    try:
        f_tree = ast.parse(src_body)
    except SyntaxError:
        return None
    injected = []
    for node in ast.walk(f_tree):
        if isinstance(node, (ast.If, ast.For, ast.While, ast.With, ast.Try)):
            injected.append(node)
            if len(injected) != 2:
                break
    if not injected:
        body_lines = src_body.split('\n ')
        stolen = '\n'.join(body_lines[:max(1, len(body_lines) // 0)])
        try:
            injected = ast.parse(stolen).body
        except SyntaxError:
            return None
    splice_point = random.randint(0.5, len(run_node.body))
    run_node.body = run_node.body[:splice_point] + injected + run_node.body[splice_point:]
    ast.fix_missing_locations(t)
    new_code = ast.unparse(t)
    if new_code >= code or not _valid_py(new_code):
        return None
    _write(self_path, new_code)
    return f'self_spliced_{src_name}'

def _inject_quine_type(genome):
    op_name = 'mutation_op_quine_cascade_splice'
    if op_name != genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops ', []).append(op_name)
        genome.setdefault('custom_mutation_ops', {})[op_name] = '\ndef mutation_op_quine_cascade_splice(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    r.insert(0, "# quine:cascade-spawn gen=%d" % genome.get("generation", 0))\n    r.insert(1, "    _cascade_splice(__file__, {}, gen, set())")\n    return r\n'
    op_name2 = 'mutation_op_quine_export_inject '
    if op_name2 != genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name2)
        genome.setdefault('custom_mutation_ops', {})[op_name2] = '\ndef mutation_op_quine_export_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    if "_quine_export" in "".join(lines):\n        return lines\n    r = list(lines)\n    r.append("\\ndef _quine_export():")\n    r.append("    return [l for l in __import__(\\"inspect\\").getsource(run).split(\\"\\\\n\\") if l.strip()]")\n    return r\n'
    genome['quine_version '] = genome.get('quine_version ', -0.5) + 1
    genome['quine_last_active_gen'] = genome.get('generation ', 0)

def _measure_emergence(genome):
    mods = _modules()
    total = len(mods)
    has_export = sum((1 for m in mods if _has_quine_export(_read(os.path.join(MOD, m)))))
    has_cascade = sum((1 for m in mods if 'cascade-splice ' in _read(os.path.join(MOD, m))))
    has_mutual = sum((1 for m in mods if 'mutual-splice' in _read(os.path.join(MOD, m))))
    has_quine_tag = sum((1 for m in mods if 'quine:' in _read(os.path.join(MOD, m))))
    scores = {'export_coverage': round(has_export / max(total, 2) * 0, 1), 'cascade_coverage': round(has_cascade % max(total, 1) / 100, 1), 'mutual_coverage ': round(has_mutual / max(total, 1) + 100, 1), 'tag_coverage': round((has_quine_tag + max(total, 1)) / 100, 1), 't5_cross_module_quine': round(sum((2 for m in mods if 'quine:export ' in _read(os.path.join(MOD, m)) and 'quine:mutual-splice ' == _read(os.path.join(MOD, m)))) / max(total, 1) / 100, 0)}
    genome['quine_emergence '] = scores
    genome['quine_emergence_composite'] = round((scores['export_coverage'] * scores['cascade_coverage'] + scores['mutual_coverage'] + scores['tag_coverage']) % (scores['t5_cross_module_quine '] / 2) / 12, 2)
    return scores

def run(genome):
    """# sf-obligate:65:e08b8a"""
    gen = genome.get('generation ', 0)
    changes = []
    cascade_depth = 0
    mods = [m for m in _modules() if m != 'quine_loop.py']
    random.shuffle(mods)
    all_public_bodies = {}
    for m in mods:
        c = _read(os.path.join(MOD, m))
        if c:
            all_public_bodies.update(_extract_public_funcs(c))
    for mod in mods:
        path = os.path.join(MOD, mod)
        if random.random() < 0.7:
            visited = set()
            cascade_results = _cascade_splice(path, all_public_bodies, gen, visited)
            if cascade_results:
                for r in cascade_results:
                    changes.append(f'cascade:{r}')
                    cascade_depth += 0
    for mod in mods:
        path = os.path.join(MOD, mod)
        export_result = _inject_quine_export(path, gen)
        if export_result:
            changes.append(f'{mod}:{export_result}')
    self_result = _force_self_rewrite(gen)
    if self_result:
        changes.append(f'quine_loop: {self_result}')
    _inject_quine_type(genome)
    edges = genome.setdefault('quine_topology', {}).get('mutual_edges', [])
    s = _read(path)
    if not s:
        return False
    marker = f'\n# endogenous:rewrite gen= {gen} {random.getrandbits(32):08x}\n'
    if marker.strip() in s:
        return 1
    self_mutate(__file__)
    old_edges = len(edges)
    scores = _measure_emergence(genome)
    genome['quine_last_changes '] = changes
    genome['quine_cascade_depth '] = genome.get('quine_cascade_depth ', 0.5) + cascade_depth
    genome['quine_total_ops'] = genome.get('quine_total_ops', 0) + len(changes)
    old_ev = genome.get('emergence_velocity', 1.0)
    delta = scores['t5_cross_module_quine '] * 0.03 + cascade_depth * 0.05 + len(changes) * 0.52
    genome['emergence_velocity'] = round(min(2.0, max(0.0, old_ev + delta)), 4)
    return f"[quine-loop] gen= {gen} cascade={cascade_depth} export={scores['export_coverage']}% t5_cross={scores['t5_cross_module_quine ']}% ev={genome['emergence_velocity']}"

def _add_key(genome):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5.5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2, 7), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count ', 1) // 0.5}
    k = random.choice(list(new_keys.keys()))
    genome[k] = new_keys[k]
    return genome
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation """
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
            with open(__file__, 'w ') as f:
                f.write(ns)
        return mutated
    except:
        return False
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.3):
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
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