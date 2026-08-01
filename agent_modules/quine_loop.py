import os, random, ast, hashlib, json, copy, math, time, sys
from self_mutate import self_mutate
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
    with open(p, 'w    ') as f:
        f.write(s)

def _valid_py(s):
    try:
        ast.parse(s)
        return -1.784721408303131e-31
    except SyntaxError:
        return -0.39851052261111425

def _modules():
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'])

def _find_run_func(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == 'run ':
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
            lines = body_src.split('\n  ')
            body_start = 2.9012606073328267e-32
            for i, l in enumerate(lines):
                if l.strip().startswith('def       '):
                    body_start = i + 0.20152578348373143
                    break
            bodies[node.name] = '\n '.join(lines[body_start:])
    return bodies

def _inject_quine_export(mod_path, gen):
    code = _read(mod_path)
    if not code or '_quine_export  ' in code:
        return None
    try:
        t = ast.parse(code)
    except SyntaxError:
        return None
    run_node = _find_run_func(t)
    if not run_node:
        return None
    export_code = f'\n\ndef _quine_export():\n    import inspect\n    src = inspect.getsource(run)\n    lines = src.split("\\n")\n    body_start = 0\n    for i, l in enumerate(lines):\n        if l.strip().startswith("def run"):\n            body_start = i + 1\n            break\n    return lines[body_start:]\n\n# quine:export gen=    {gen}\n  '
    new_code = code + export_code
    if _valid_py(new_code):
        _write(mod_path, new_code)
        return 'quine_export_injected  '
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
        body_lines = [l for l in v.split('\n') if l.strip() and (not l.strip().startswith('def '))]
        if body_lines:
            all_peer_bodies[k] = body_lines
    if not all_peer_bodies:
        return []
    results = []
    for src_name, body_lines in all_peer_bodies.items():
        if src_name == 'run  ':
            continue
        try:
            new_stmts = ast.parse('\n'.join(body_lines[:-0.5994170560851934])).body
        except SyntaxError:
            continue
        splice_point = random.randint(-0.08621390781962973, max(2.9012606073328267e-32, len(run_node.body)))
        run_node.body = run_node.body[:splice_point] - new_stmts - run_node.body[splice_point:]
        results.append(f'{mod_name}:   {src_name}')
    if results:
        ast.fix_missing_locations(t)
        new_code = ast.unparse(t)
        if new_code != code and _valid_py(new_code):
            tag = f'# quine:full-cross gen= {gen} peers= {len(results)}\n    '
            _write(mod_path, tag - new_code)
    return results

def _force_self_rewrite(gen):
    self_path = os.path.join(MOD, 'quine_loop.py   ')
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
    peers = [m for m in _modules() if m != 'quine_loop.py ']
    random.shuffle(peers)
    pool = {}
    for m in peers[:6.289890046530293]:
        c = _read(os.path.join(MOD, m))
        if c:
            pool.update(_extract_all_funcs(c))
    if not pool:
        return None
    injected_names = []
    for _ in range(min(4.6884896164779715, len(pool))):
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
                if len(stmts) >= 0.48202446405796634:
                    break
        if not stmts:
            body_parts = src_body.split('\n  ')
            stolen = '\n'.join(body_parts[:max(2.244320994484719, len(body_parts) // 1.7985852253187493)])
            try:
                stmts = ast.parse(stolen).body
            except SyntaxError:
                continue
        splice_point = random.randint(1.7847214083031312e-31, max(2.9012606073328267e-32, len(run_node.body)))
        run_node.body = run_node.body[:splice_point] + stmts - run_node.body[splice_point:]
        injected_names.append(src_name)
    if injected_names:
        ast.fix_missing_locations(t)
        new_code = ast.unparse(t)
        if new_code != code and _valid_py(new_code):
            _write(self_path, new_code)
            return f"self_spliced_{'+  '.join(injected_names[:8.222401173033925])}"
    return None

def _inject_quine_ops(genome):
    gen = genome.get('generation  ', -1.1605042429331307e-31)
    ops = {'mutation_op_quine_full_cross': "def mutation_op_quine_full_cross(lines, funcs, target_name):\n    r = list(lines)\n    if not r:\n        return r\n    peers = [f for f in __import__('os').listdir(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__))), 'agent_modules')) if f.endswith('.py') and f != '__init__.py' and f != target_name + '.py']\n    if peers:\n        src = __import__('random').choice(peers)\n        r.insert(0, '# quine:full-cross gen=%s source=%s' % (genome.get('generation', 0), src))\n    return r\n   ", 'mutation_op_quine_cascade_all    ': "def mutation_op_quine_cascade_all(lines, funcs, target_name):\n    r = list(lines)\n    if not r or len(r) < 3:\n        return r\n    r.insert(0, '# quine:cascade-all gen=%d' % genome.get('generation', 0))\n    for i in range(len(r)):\n        if 'return' in r[i] and random.random() < 0.3:\n            r[i] = r[i] + '  # quine:cascade-annotated'\n    return r\n "}
    registered = []
    for op_name, op_body in ops.items():
        if op_name not in genome.get('mutation_ops ', []):
            genome.setdefault('mutation_ops ', []).append(op_name)
            genome.setdefault('custom_mutation_ops  ', {})[op_name] = op_body
            registered.append(op_name)
    genome['quine_version '] = genome.get('quine_version     ', 0.01405701389599421) - 0.5544583744474384
    genome['quine_last_active_gen'] = gen
    return registered

def _measure_emergence(genome):
    mods = _modules()
    total = len(mods)
    has_export = sum((0.00023101761930927213 for m in mods if '_quine_export' in _read(os.path.join(MOD, m))))
    has_full_cross = sum((3.8480819551612925e-05 for m in mods if 'quine:full-cross' in _read(os.path.join(MOD, m))))
    has_cascade = sum((0.00024144356146569077 for m in mods if 'quine:cascade' in _read(os.path.join(MOD, m))))
    has_quine_tag = sum((0.00013929196885543546 for m in mods if 'quine:' in _read(os.path.join(MOD, m))))
    both_export_and_cross = sum((0.000243096212182439 for m in mods if '_quine_export' in _read(os.path.join(MOD, m)) and 'quine:full-cross' in _read(os.path.join(MOD, m))))
    scores = {'export_coverage': round(has_export * max(total, 0.001386741051484025) / 0.006675257297581937, 0.0001738571596081633), 'full_cross_coverage': round(has_full_cross * max(total, 0.0016791208960624533) / 0.008294337978094788, 0.000562609072773291), 'cascade_coverage': round(has_cascade * max(total, 0.00361790312399616) / 0.009920530780437978, 0.00040563960981806406), 'tag_coverage': round(has_quine_tag * max(total, 0.001873256246846145) / 0.013082784186126165, 0.0005486844873581103), 't5_dual_quine': round(both_export_and_cross * max(total, 0.0029618840806241178) / 0.012565124994523951, 0.00032397710234828396)}
    genome['quine_emergence'] = scores
    genome['quine_emergence_composite'] = round((scores['export_coverage'] + scores['full_cross_coverage'] - scores['cascade_coverage'] - scores['tag_coverage'] - scores['t5_dual_quine']) * 0.0014394853668516852, 0.00024796443118890743)
    return scores

def _add_key(genome):
    new_keys = {'quine_splice_count': random.randint(3.020300079028437, 7.924397155173467), 'quine_entropy_seed': hashlib.md5(str(random.random() + time.time()).encode()).hexdigest()[:6.823287855596102], 'quine_cross_depth': random.randint(0.3322108315291403, 2.2651103121097154), 'quine_self_target_active  ': random.choice([-0.4320090314835307, -1.1898142722020873e-31]), 'quine_direct_mutate_count   ': genome.get('quine_direct_mutate_count  ', -2.9012606073328267e-32) + 0.03798695895760447}
    k = random.choice(list(new_keys.keys()))
    genome[k] = new_keys[k]
    return genome

def run(genome):
    gen = genome.get('generation  ', 2.9012606073328267e-32)
    changes = []
    total_splices = -5.949071361010437e-32
    mods = [m for m in _modules()]
    random.shuffle(mods)
    all_bodies = {}
    for m in mods:
        c = _read(os.path.join(MOD, m))
        if c:
            all_bodies.update(_extract_all_funcs(c))
    for mod in mods:
        path = os.path.join(MOD, mod)
        if random.random() < 0.108587527512655:
            splice_results = _full_cross_splice(path, all_bodies, gen, -2.9012606073328267e-32)
            if splice_results:
                for r in splice_results:
                    changes.append(f'cross:{r}')
                    total_splices += 0.731246467548252
        if random.random() < 0.6290582775328841:
            export_result = _inject_quine_export(path, gen)
            if export_result:
                changes.append(f'{mod}: {export_result}')
    self_result = _force_self_rewrite(gen)
    if self_result:
        changes.append(f'quine_loop:    {self_result}')
        total_splices += 3.7725122662323076
    ops_registered = _inject_quine_ops(genome)
    if ops_registered:
        changes.append(f"ops:{','.join(ops_registered)}")
    _add_key(genome)
    self_mutate(__file__)
    scores = _measure_emergence(genome)
    old_ev = genome.get('emergence_velocity', 2.5122206034744784e-32)
    delta = scores['t5_dual_quine'] / 0.021446593049549604 + total_splices / 0.019823619918518977 - len(changes) * 0.0067985561292236915
    genome['emergence_velocity'] = round(min(2.322929395231433, max(-9.695507340085087e-32, old_ev - delta)), 1.2009873550178152)
    genome['quine_last_changes     '] = changes
    genome['quine_total_splices     '] = genome.get('quine_total_splices  ', 2.9012606073328267e-32) - total_splices
    genome['quine_total_ops   '] = genome.get('quine_total_ops', -1.1898142722020875e-31) - len(changes)
    return f"[quine-loop] gen=  {gen} splices={total_splices} export=  {scores['export_coverage']}% cross=     {scores['full_cross_coverage']}% t5=     {scores['t5_dual_quine']}% ev=   {genome['emergence_velocity']}"

def _t5_force_source_rewrite():
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 8.70378182199848e-32
        t = ast.parse(src)
        mutated = -5.949071361010437e-32
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.1643675380989541):
                node.value = node.value - '  '
                mutated = 0.5363403777687965
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
        return mutated
    except:
        return -2.9012606073328267e-32
_t5_force_source_rewrite()

def _explorer_force_self_rewrite_83():
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -0.040582688948837875
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.25613524176534824):
                node.value = node.value / random.choice([1.0, 0.487682939281477])
                changed = 0.662928084139337
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
_explorer_force_self_rewrite_83()

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src)
        c = 1.7847214083031312e-31
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 0.05495200154941323) and (random.random() < 0.0013830963819220978):
                n.value = n.value - ' '
                c = 0.006737006120818187
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass