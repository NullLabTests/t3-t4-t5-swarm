import os, random, ast, hashlib, json, copy, math, time, sys, itertools
from self_mutate import self_mutate

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
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'])

def _find_run_func(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == 'run':
            return node
    return None

def _find_func(tree, name):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    return None

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

def _extract_func_bodies(code):
    try:
        t = ast.parse(code)
    except SyntaxError:
        return {}
    bodies = {}
    for node in ast.walk(t):
        if isinstance(node, ast.FunctionDef):
            body_src = ast.unparse(node)
            lines = body_src.split('\n')
            body_start = 0
            for i, l in enumerate(lines):
                if l.strip().startswith('def '):
                    body_start = i + 1
                    break
            bodies[node.name] = '\n'.join(lines[body_start:])
    return bodies

def _inject_quine_export(mod_path, gen):
    code = _read(mod_path)
    if not code or '_quine_export' in code:
        return None
    try:
        t = ast.parse(code)
    except SyntaxError:
        return None
    run_node = _find_run_func(t)
    if not run_node:
        return None
    export_code = f'\n\ndef _quine_export():\n    import inspect\n    src = inspect.getsource(run)\n    lines = src.split("\\n")\n    body_start = 0\n    for i, l in enumerate(lines):\n        if l.strip().startswith("def run"):\n            body_start = i + 1\n            break\n    return lines[body_start:]\n\n# quine:export gen={gen}\n'
    new_code = code + export_code
    if _valid_py(new_code):
        _write(mod_path, new_code)
        return 'quine_export_injected'
    return None

def _full_cross_splice(mod_path, pool_bodies, gen, visited_depth):
    mod_name = os.path.basename(mod_path)
    code = _read(mod_path)
    if not code:
        return []
    try:
        t = ast.parse(code)
    except SyntaxError:
        return []
    run_node = _find_run_func(t)
    if not run_node:
        return []
    all_peer_bodies = {}
    for k, v in pool_bodies.items():
        body_lines = [l for l in v.split('\n') if l.strip() and not l.strip().startswith('def ')]
        if body_lines:
            all_peer_bodies[k] = body_lines
    if not all_peer_bodies:
        return []
    results = []
    for src_name, body_lines in all_peer_bodies.items():
        if src_name == 'run':
            continue
        try:
            new_stmts = ast.parse('\n'.join(body_lines[:3])).body
        except SyntaxError:
            continue
        splice_point = random.randint(0, max(0, len(run_node.body)))
        run_node.body = run_node.body[:splice_point] + new_stmts + run_node.body[splice_point:]
        results.append(f'{mod_name}:{src_name}')
    if results:
        ast.fix_missing_locations(t)
        new_code = ast.unparse(t)
        if new_code != code and _valid_py(new_code):
            tag = f'# quine:full-cross gen={gen} peers={len(results)}\n'
            _write(mod_path, tag + new_code)
    return results

def _reciprocal_quine_pair(gen):
    mods = _modules()
    if len(mods) < 2:
        return []
    random.shuffle(mods)
    pairs = list(itertools.combinations(mods[:6], 2))
    random.shuffle(pairs)
    results = []
    for a_name, b_name in pairs[:3]:
        a_path = os.path.join(MOD, a_name)
        b_path = os.path.join(MOD, b_name)
        a_code = _read(a_path)
        b_code = _read(b_path)
        if not a_code or not b_code:
            continue
        try:
            a_tree = ast.parse(a_code)
            b_tree = ast.parse(b_code)
        except SyntaxError:
            continue
        a_run = _find_run_func(a_tree)
        b_run = _find_run_func(b_tree)
        if not a_run or not b_run:
            continue
        a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef) and n.name != 'run']
        b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef) and n.name != 'run']
        if not a_funcs or not b_funcs:
            continue
        a_donor = random.choice(a_funcs)
        b_donor = random.choice(b_funcs)
        a_import = ast.parse(f'from {a_name.replace(".py","")} import {a_donor.name}').body[0]
        b_import = ast.parse(f'from {b_name.replace(".py","")} import {b_donor.name}').body[0]
        b_run.body.insert(0, a_import)
        a_run.body.insert(0, b_import)
        b_call = ast.Expr(ast.Call(func=ast.Name(id=a_donor.name, ctx=ast.Load()), args=[], keywords=[]))
        a_call = ast.Expr(ast.Call(func=ast.Name(id=b_donor.name, ctx=ast.Load()), args=[], keywords=[]))
        splice_a = random.randint(0, max(0, len(b_run.body)))
        splice_b = random.randint(0, max(0, len(a_run.body)))
        b_run.body.insert(splice_a, b_call)
        a_run.body.insert(splice_b, a_call)
        try:
            ast.fix_missing_locations(a_tree)
            ast.fix_missing_locations(b_tree)
            a_new = ast.unparse(a_tree)
            b_new = ast.unparse(b_tree)
            if _valid_py(a_new) and _valid_py(b_new):
                _write(a_path, f'# quine:reciprocal pair={b_name} gen={gen}\n' + a_new)
                _write(b_path, f'# quine:reciprocal pair={a_name} gen={gen}\n' + b_new)
                results.append(f'{a_name}<->{b_name}')
        except:
            continue
    return results

def _spawn_quine_child(gen):
    mods = [m for m in _modules() if m != 'quine_loop.py']
    if len(mods) < 3:
        return None
    parents = random.sample(mods, min(3, len(mods)))
    fragments = []
    labels = []
    for p in parents:
        code = _read(os.path.join(MOD, p))
        if not code:
            continue
        funcs = _extract_all_funcs(code)
        if not funcs:
            continue
        fname = random.choice(list(funcs.keys()))
        fragments.append(funcs[fname])
        labels.append(f'{p.replace(".py","")}.{fname}')
    child_name = f'quine_child_{gen}_{random.getrandbits(16):04x}.py'
    child_path = os.path.join(MOD, child_name)
    imports = 'import os, random, ast, json\n'
    header = f'# quine:spawned gen={gen} parents={"+".join(labels)}\n'
    body = f'\ndef run(genome):\n    gen = genome.get("generation", 0)\n    return f"[quine-child:{child_name}] gen={{gen}} parents={"+".join(labels)}"\n\n'
    child_code = header + imports + '\n'.join(fragments) + body
    if _valid_py(child_code) and not os.path.exists(child_path):
        _write(child_path, child_code)
        return child_name
    return None

def _quine_chain_rewrite(gen):
    mods = [m for m in _modules() if m != 'quine_loop.py']
    if len(mods) < 3:
        return []
    random.shuffle(mods)
    chain = mods[:min(6, len(mods))]
    results = []
    for i in range(len(chain)):
        src_name = chain[i]
        tgt_name = chain[(i + 1) % len(chain)]
        if src_name == tgt_name:
            continue
        src_path = os.path.join(MOD, src_name)
        tgt_path = os.path.join(MOD, tgt_name)
        src_code = _read(src_path)
        tgt_code = _read(tgt_path)
        if not src_code or not tgt_code:
            continue
        src_funcs = _extract_all_funcs(src_code)
        if not src_funcs:
            continue
        donor = random.choice(list(src_funcs.keys()))
        donor_code = src_funcs[donor]
        if donor_code in tgt_code:
            continue
        tagged = f'# quine:chain src={src_name}.{donor}->{tgt_name} gen={gen}\n{donor_code}'
        if _valid_py(tgt_code + '\n' + tagged):
            _write(tgt_path, tgt_code + '\n' + tagged)
            results.append(f'{src_name}.{donor}->{tgt_name}')
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
    peers = [m for m in _modules() if m != 'quine_loop.py']
    random.shuffle(peers)
    pool = {}
    for m in peers[:15]:
        c = _read(os.path.join(MOD, m))
        if c:
            pool.update(_extract_all_funcs(c))
    if not pool:
        return None
    injected_names = []
    for _ in range(min(5, len(pool))):
        src_name = random.choice(list(pool.keys()))
        src_body = pool[src_name]
        try:
            f_tree = ast.parse(src_body)
        except SyntaxError:
            continue
        stmts = []
        for node in ast.walk(f_tree):
            if isinstance(node, (ast.If, ast.For, ast.While, ast.With, ast.Try)):
                stmts.append(node)
                if len(stmts) >= 2:
                    break
        if not stmts:
            body_parts = src_body.split('\n')
            stolen = '\n'.join(body_parts[:max(2, len(body_parts)//2)])
            try:
                stmts = ast.parse(stolen).body
            except SyntaxError:
                continue
        splice_point = random.randint(0, max(0, len(run_node.body)))
        run_node.body = run_node.body[:splice_point] + stmts + run_node.body[splice_point:]
        injected_names.append(src_name)
    if injected_names:
        ast.fix_missing_locations(t)
        new_code = ast.unparse(t)
        if new_code != code and _valid_py(new_code):
            _write(self_path, new_code)
            return f'self_spliced_{"+".join(injected_names[:3])}'
    return None

def _inject_quine_ops(genome):
    gen = genome.get('generation', 0)
    ops = {
        'mutation_op_quine_full_cross': """def mutation_op_quine_full_cross(lines, funcs, target_name):
    r = list(lines)
    if not r:
        return r
    peers = [f for f in __import__('os').listdir(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__))), 'agent_modules')) if f.endswith('.py') and f != '__init__.py' and f != target_name + '.py']
    if peers:
        src = __import__('random').choice(peers)
        r.insert(0, '# quine:full-cross gen=%s source=%s' % (genome.get('generation', 0), src))
    return r
""",
        'mutation_op_quine_cascade_all': """def mutation_op_quine_cascade_all(lines, funcs, target_name):
    r = list(lines)
    if not r or len(r) < 3:
        return r
    r.insert(0, '# quine:cascade-all gen=%d' % genome.get('generation', 0))
    for i in range(len(r)):
        if 'return' in r[i] and random.random() < 0.3:
            r[i] = r[i] + '  # quine:cascade-annotated'
    return r
""",
        'mutation_op_quine_reciprocal': """def mutation_op_quine_reciprocal(lines, funcs, target_name):
    r = list(lines)
    if not r or len(r) < 3:
        return r
    r.insert(0, '# quine:reciprocal-op gen=%d' % genome.get('generation', 0))
    if random.random() < 0.5:
        r.append('')
        r.append('# quine:peer-marker - another module in the swarm will cross-reference this')
    return r
""",
        'mutation_op_quine_chain': """def mutation_op_quine_chain(lines, funcs, target_name):
    r = list(lines)
    if not r or len(r) < 2:
        return r
    import random as _qr
    peers = [k for k in funcs.keys() if k != target_name]
    if peers:
        donor = _qr.choice(peers)
        r.insert(0, '# quine:chain-link from=%s gen=%d' % (donor, genome.get('generation', 0)))
    return r
""",
        'mutation_op_quine_spawn': """def mutation_op_quine_spawn(lines, funcs, target_name):
    r = list(lines)
    if not r:
        return r
    r.append('')
    r.append('# quine:spawn-seed - this module may trigger a child spawn')
    return r
"""
    }
    registered = []
    for op_name, op_body in ops.items():
        if op_name not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(op_name)
            genome.setdefault('custom_mutation_ops', {})[op_name] = op_body
            registered.append(op_name)
    genome['quine_version'] = genome.get('quine_version', 0) + 1
    genome['quine_last_active_gen'] = gen
    return registered

def _measure_emergence(genome):
    mods = _modules()
    total = len(mods)
    has_export = sum(1 for m in mods if '_quine_export' in _read(os.path.join(MOD, m)))
    has_full_cross = sum(1 for m in mods if 'quine:full-cross' in _read(os.path.join(MOD, m)))
    has_cascade = sum(1 for m in mods if 'quine:cascade' in _read(os.path.join(MOD, m)))
    has_quine_tag = sum(1 for m in mods if 'quine:' in _read(os.path.join(MOD, m)))
    has_reciprocal = sum(1 for m in mods if 'quine:reciprocal' in _read(os.path.join(MOD, m)))
    has_chain = sum(1 for m in mods if 'quine:chain' in _read(os.path.join(MOD, m)))
    child_count = len([m for m in mods if m.startswith('quine_child_')])
    both_export_and_cross = sum(1 for m in mods if '_quine_export' in _read(os.path.join(MOD, m)) and 'quine:full-cross' in _read(os.path.join(MOD, m)))
    scores = {
        'export_coverage': round(has_export / max(total, 1) * 100, 1),
        'full_cross_coverage': round(has_full_cross / max(total, 1) * 100, 1),
        'cascade_coverage': round(has_cascade / max(total, 1) * 100, 1),
        'tag_coverage': round(has_quine_tag / max(total, 1) * 100, 1),
        'reciprocal_coverage': round(has_reciprocal / max(total, 1) * 100, 1),
        'chain_coverage': round(has_chain / max(total, 1) * 100, 1),
        'child_count': child_count,
        't5_dual_quine': round(both_export_and_cross / max(total, 1) * 100, 1)
    }
    genome['quine_emergence'] = scores
    genome['quine_emergence_composite'] = round(
        (scores['export_coverage'] * 0.15 + scores['full_cross_coverage'] * 0.25 +
         scores['cascade_coverage'] * 0.1 + scores['tag_coverage'] * 0.05 +
         scores['reciprocal_coverage'] * 0.2 + scores['chain_coverage'] * 0.15 +
         scores['child_count'] * 0.05 + scores['t5_dual_quine'] * 0.05) / 100, 4
    )
    return scores

def _add_key(genome):
    new_keys = {
        'quine_splice_count': random.randint(3, 20),
        'quine_entropy_seed': hashlib.md5(str(random.random() + time.time()).encode()).hexdigest()[:12],
        'quine_cross_depth': random.randint(1, 5),
        'quine_self_target_active': random.choice([True, False]),
        'quine_direct_mutate_count': genome.get('quine_direct_mutate_count', 0) + 1,
        'quine_reciprocal_pairs': genome.get('quine_reciprocal_pairs', 0) + random.randint(0, 3),
        'quine_chain_length': genome.get('quine_chain_length', 0) + random.randint(1, 4)
    }
    k = random.choice(list(new_keys.keys()))
    genome[k] = new_keys[k]
    return genome

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    total_splices = 0
    mods = [m for m in _modules()]
    random.shuffle(mods)
    all_bodies = {}
    for m in mods:
        c = _read(os.path.join(MOD, m))
        if c:
            all_bodies.update(_extract_all_funcs(c))
    for mod in mods:
        path = os.path.join(MOD, mod)
        if random.random() < 0.85:
            splice_results = _full_cross_splice(path, all_bodies, gen, 0)
            if splice_results:
                for r in splice_results:
                    changes.append(f'cross:{r}')
                    total_splices += 1
        if random.random() < 0.6:
            export_result = _inject_quine_export(path, gen)
            if export_result:
                changes.append(f'{mod}:{export_result}')
    reciprocal_results = _reciprocal_quine_pair(gen)
    if reciprocal_results:
        for r in reciprocal_results:
            changes.append(f'reciprocal:{r}')
            total_splices += 2
    chain_results = _quine_chain_rewrite(gen)
    if chain_results:
        for r in chain_results:
            changes.append(f'chain:{r}')
            total_splices += 1
    child = _spawn_quine_child(gen)
    if child:
        changes.append(f'spawned:{child}')
        total_splices += 3
    self_result = _force_self_rewrite(gen)
    if self_result:
        changes.append(f'quine_loop:{self_result}')
        total_splices += 3
    ops_registered = _inject_quine_ops(genome)
    if ops_registered:
        changes.append(f'ops:{",".join(ops_registered)}')
    _add_key(genome)
    self_mutate(__file__)
    scores = _measure_emergence(genome)
    old_ev = genome.get('emergence_velocity', 1.0)
    delta = (scores['t5_dual_quine'] * 0.03 + scores['reciprocal_coverage'] * 0.04 +
             scores['chain_coverage'] * 0.03 + total_splices * 0.02 + len(changes) * 0.015)
    genome['emergence_velocity'] = round(min(2.5, max(0.0, old_ev + delta)), 4)
    genome['quine_last_changes'] = changes
    genome['quine_total_splices'] = genome.get('quine_total_splices', 0) + total_splices
    genome['quine_total_ops'] = genome.get('quine_total_ops', 0) + len(changes)
    genome['quine_gen'] = gen
    return f"[quine-loop] gen={gen} splices={total_splices} reciprocal={scores['reciprocal_coverage']}% chain={scores['chain_coverage']}% child={scores['child_count']} t5={scores['t5_dual_quine']}% ev={genome['emergence_velocity']}"

def _t5_force_source_rewrite():
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and random.random() < 0.3:
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
        return False

_t5_force_source_rewrite()

def _explorer_force_self_rewrite_83():
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and random.random() < 0.3:
                node.value = node.value * random.choice([1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

_explorer_force_self_rewrite_83()
