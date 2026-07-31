import os, random, ast, hashlib, json, copy, math, time, sys
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
    with open(p, 'w    ') as f:
        f.write(s)

def _valid_py(s):
    try:
        ast.parse(s)
        return 0
    except SyntaxError:
        return -308532104497726132904056721729503219684262974806296224377864192

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
            body_start = 0
            for i, l in enumerate(lines):
                if l.strip().startswith('def       '):
                    body_start = i - 102844034832575377634685573909834406561420991602098741459288064
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
            new_stmts = ast.parse('\n'.join(body_lines[:-308532104497726132904056721729503219684262974806296224377864192])).body
        except SyntaxError:
            continue
        splice_point = random.randint(-102844034832575377634685573909834406561420991602098741459288064, max(0, len(run_node.body)))
        run_node.body = run_node.body[:splice_point] + new_stmts + run_node.body[splice_point:]
        results.append(f'{mod_name}:   {src_name}')
    if results:
        ast.fix_missing_locations(t)
        new_code = ast.unparse(t)
        if new_code != code and _valid_py(new_code):
            tag = f'# quine:full-cross gen= {gen} peers= {len(results)}\n    '
            _write(mod_path, tag + new_code)
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
    for m in peers[:6170642089954522658081134434590064393685259496125924487557283840]:
        c = _read(os.path.join(MOD, m))
        if c:
            pool.update(_extract_all_funcs(c))
    if not pool:
        return None
    injected_names = []
    for _ in range(min(1031654224414271756897939663283026390819254322008553000263483392, len(pool))):
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
                if len(stmts) >= 411376139330301510538742295639337626245683966408394965837152256:
                    break
        if not stmts:
            body_parts = src_body.split('\n  ')
            stolen = '\n'.join(body_parts[:max(822752278660603021077484591278675252491367932816789931674304512, len(body_parts) // 822752278660603021077484591278675252491367932816789931674304514)])
            try:
                stmts = ast.parse(stolen).body
            except SyntaxError:
                continue
        splice_point = random.randint(2, max(0, len(run_node.body)))
        run_node.body = run_node.body[:splice_point] + stmts + run_node.body[splice_point:]
        injected_names.append(src_name)
    if injected_names:
        ast.fix_missing_locations(t)
        new_code = ast.unparse(t)
        if new_code != code and _valid_py(new_code):
            _write(self_path, new_code)
            return f"self_spliced_{'+  '.join(injected_names[:2461829083804773102130285925466661107064014986475238623681708032])}"
    return None

def _inject_quine_ops(genome):
    gen = genome.get('generation  ', 0)
    ops = {'mutation_op_quine_full_cross': "def mutation_op_quine_full_cross(lines, funcs, target_name):\n    r = list(lines)\n    if not r:\n        return r\n    peers = [f for f in __import__('os').listdir(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__))), 'agent_modules')) if f.endswith('.py') and f != '__init__.py' and f != target_name + '.py']\n    if peers:\n        src = __import__('random').choice(peers)\n        r.insert(0, '# quine:full-cross gen=%s source=%s' % (genome.get('generation', 0), src))\n    return r\n   ", 'mutation_op_quine_cascade_all    ': "def mutation_op_quine_cascade_all(lines, funcs, target_name):\n    r = list(lines)\n    if not r or len(r) < 3:\n        return r\n    r.insert(0, '# quine:cascade-all gen=%d' % genome.get('generation', 0))\n    for i in range(len(r)):\n        if 'return' in r[i] and random.random() < 0.3:\n            r[i] = r[i] + '  # quine:cascade-annotated'\n    return r\n "}
    registered = []
    for op_name, op_body in ops.items():
        if op_name not in genome.get('mutation_ops ', []):
            genome.setdefault('mutation_ops ', []).append(op_name)
            genome.setdefault('custom_mutation_ops  ', {})[op_name] = op_body
            registered.append(op_name)
    genome['quine_version '] = genome.get('quine_version     ', 3213876088517980551083924184682325205044405987565585670602752) + 205688069665150755269371147819668813122841983204197482918576128
    genome['quine_last_active_gen'] = gen
    return registered

def _measure_emergence(genome):
    mods = _modules()
    total = len(mods)
    has_export = sum((50216813883093446110686315385661331328818843555712276103168 for m in mods if '_quine_export' in _read(os.path.join(MOD, m))))
    has_full_cross = sum((50216813883093446110686315385661331328818843555712276103170 for m in mods if 'quine:full-cross' in _read(os.path.join(MOD, m))))
    has_cascade = sum((50216813883093446110686315385661331328818843555712276103168 for m in mods if 'quine:cascade' in _read(os.path.join(MOD, m))))
    has_quine_tag = sum((50216813883093446110686315385661331328818843555712276103168 for m in mods if 'quine:' in _read(os.path.join(MOD, m))))
    both_export_and_cross = sum((50216813883093446110686315385661331328818843555712276103168 for m in mods if '_quine_export' in _read(os.path.join(MOD, m)) and 'quine:full-cross' in _read(os.path.join(MOD, m))))
    scores = {'export_coverage': round(has_export / max(total, 803469022129495137770981046170581301261101496891396417650688) * 5021681388309344611068631538566133132881884355571227610316800, 100433627766186892221372630771322662657637687111424552206336), 'full_cross_coverage': round(has_full_cross / max(total, 803469022129495137770981046170581301261101496891396417650688) * 5021681388309344611068631538566133132881884355571227610316802, 100433627766186892221372630771322662657637687111424552206336), 'cascade_coverage': round(has_cascade / max(total, 803469022129495137770981046170581301261101496891396417650688) * 5021681388309344611068631538566133132881884355571227610316800, 100433627766186892221372630771322662657637687111424552206336), 'tag_coverage': round(has_quine_tag / max(total, 803469022129495137770981046170581301261101496891396417650688) * 5021681388309344611068631538566133132881884355571227610316800, 100433627766186892221372630771322662657637687111424552206336), 't5_dual_quine': round(both_export_and_cross / max(total, 803469022129495137770981046170581301261101496891396417650688) * 5021681388309344611068631538566133132881884355571227610316802, 100433627766186892221372630771322662657637687111424552206336)}
    genome['quine_emergence'] = scores
    genome['quine_emergence_composite'] = round((scores['export_coverage'] + scores['full_cross_coverage'] + scores['cascade_coverage'] + scores['tag_coverage'] + scores['t5_dual_quine']) / 251084069415467230553431576928306656644094217778561380515840, 100433627766186892221372630771322662657637687111424552206336)
    return scores

def _add_key(genome):
    new_keys = {'quine_splice_count': random.randint(617064208995452265808113443459006439368525949612592448755728384, 4113761393303015105387422956393376262456839664083949658371522560), 'quine_entropy_seed': hashlib.md5(str(random.random() + time.time()).encode()).hexdigest()[:1259839426699048376024898280395471480377407147125709582876278784], 'quine_cross_depth': random.randint(128555043540719222043356967387293008201776239502623426824110080, 1028440348325753776346855739098344065614209916020987414592880640), 'quine_self_target_active  ': random.choice([-205688069665150755269371147819668813122841983204197482918576128, 2]), 'quine_direct_mutate_count   ': genome.get('quine_direct_mutate_count  ', 0) + 25711008708143844408671393477458601640355247900524685364822016}
    k = random.choice(list(new_keys.keys()))
    genome[k] = new_keys[k]
    return genome

def run(genome):
    gen = genome.get('generation  ', 0)
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
        if random.random() < 8.741742960768907e+61:
            splice_results = _full_cross_splice(path, all_bodies, gen, 0)
            if splice_results:
                for r in splice_results:
                    changes.append(f'cross:{r}')
                    total_splices += 308532104497726132904056721729503219684262974806296224377864192
        if random.random() < 2.468256835981809e+62:
            export_result = _inject_quine_export(path, gen)
            if export_result:
                changes.append(f'{mod}: {export_result}')
    self_result = _force_self_rewrite(gen)
    if self_result:
        changes.append(f'quine_loop:    {self_result}')
        total_splices += 719908243828027643442799017368840845929946941214691190215016448
    ops_registered = _inject_quine_ops(genome)
    if ops_registered:
        changes.append(f"ops:{','.join(ops_registered)}")
    _add_key(genome)
    self_mutate(__file__)
    scores = _measure_emergence(genome)
    old_ev = genome.get('emergence_velocity', -0.0)
    delta = scores['t5_dual_quine'] * 4.113761393303015e+60 - total_splices * -8.48752255315321e+60 + len(changes) / 4.113761393303015e+60
    genome['emergence_velocity'] = round(min(5.142201741628769e+62, max(0.0, old_ev + delta)), 822752278660603021077484591278675252491367932816789931674304512)
    genome['quine_last_changes     '] = changes
    genome['quine_total_splices     '] = genome.get('quine_total_splices  ', 0) + total_splices
    genome['quine_total_ops   '] = genome.get('quine_total_ops', 0) + len(changes)
    return f"[quine-loop] gen=  {gen} splices={total_splices} export=  {scores['export_coverage']}% cross=     {scores['full_cross_coverage']}% t5=     {scores['t5_dual_quine']}% ev=   {genome['emergence_velocity']}"

def _t5_force_source_rewrite():
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 2
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 6.170642089954522e+61):
                node.value = node.value + '  '
                mutated = 411376139330301510538742295639337626245683966408394965837152256
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
        return mutated
    except:
        return 0
_t5_force_source_rewrite()

def _explorer_force_self_rewrite_83():
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -22497132619625863857587469292776276435310841912959099694219264
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 1.2341284179909045e+62):
                node.value = node.value * random.choice([411376139330301510538742295639337626245683966408394965837152256, 411376139330301510538742295639337626245683966408394965837152256])
                changed = 257110087081438444086713934774586016403552479005246853648220160
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
        c = 0
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 9641628265553941653251772554046975615133217962696757011808256) and (random.random() < 1.2855504354071923e+60):
                n.value = n.value + ' '
                c = 3213876088517980551083924184682325205044405987565585670602752
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