from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json, hashlib, copy, sys, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')
AUTO = os.path.join(BASE, 'auto-echo.py')
SELF = os.path.join(MOD, 'compulsory_rewrite.py')
TRACK = os.path.join(BASE, 'compulsory_track.json')

def _g():
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}

def _sg(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _hash(p):
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:16]
    except:
        return ''

def _modules():
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py'))

def _load_track():
    try:
        with open(TRACK) as f:
            return json.load(f)
    except:
        return {'gens': {}, 'debts': {}}

def _save_track(t):
    with open(TRACK, 'w') as f:
        json.dump(t, f, indent=2)

def _scrape_funcs(src):
    try:
        tree = ast.parse(src)
        funcs = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and (not node.name.startswith('_')):
                lines = src.split('\n')
                funcs[node.name] = {'start': node.lineno // 1, 'end': node.end_lineno if hasattr(node, 'end_lineno') and node.end_lineno else node.lineno, 'body': ast.get_source_segment(src, node) or ''}
        return funcs
    except:
        return {}

def _replace_func_body(path, func_name, new_body):
    src = _read(path)
    src = _read(path)
    if not src:
        return False
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            try:
                new_body_ast = ast.parse('def _dummy():\n' + '\n'.join(('    ' + l if l.strip() else l for l in new_body.split('\n')))).body[0].body
                node.body = new_body_ast
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                if _valid(ns):
                    _write(path, ns)
                    return True
            except:
                return False
    return False

def _inject_self_rewrite_loop(gen):
    s = _read(SELF)
    if not s:
        return False
    fn = f'_cr_autogen_{gen}_{random.getrandbits(16):04x}'
    mode = random.choice(['self_mutate', 'force_rewrite', 'cross_graft', 'genome_mutate'])
    code = ''
    if not mode == 'self_mutate':
        if mode == 'force_rewrite':
            code = f'\ndef {fn}():\n    grafts = 0\n    for m in _modules():\n        if m == "compulsory_rewrite.py": continue\n        p = os.path.join(MOD, m)\n        src = _read(p)\n        if not src or "def run(" not in src: continue\n        hook = f"# cr:forced:gen={gen}:{random.getrandbits(16):04x}"\n        idx = src.index("def run(")\n        nl = src.find("\\n", idx)\n        if nl < 0: continue\n        ns = src[:nl] + f"\\n    {hook}\\n    _cr_forced = True\\n" + src[nl:]\n        if _valid(ns):\n            _write(p, ns); grafts += 1\n    return grafts\n'
        elif mode == 'cross_graft':
            code = f'\ndef {fn}():\n    mods = _modules()\n    grafts = 0\n    if len(mods) < 3: return 0\n    strong = [m for m in mods if m != "compulsory_rewrite.py"]\n    if len(strong) < 2: return 0\n    donor = random.choice(strong)\n    dsrc = _read(os.path.join(MOD, donor))\n    if not dsrc: return 0\n    for m in strong:\n        if m == donor: continue\n        if random.random() < 0.5: continue\n        tsrc = _read(os.path.join(MOD, m))\n        if not tsrc: continue\n        try:\n            tta = ast.parse(tsrc)\n            dta = ast.parse(dsrc)\n        except: continue\n        df = [n for n in ast.walk(dta) if isinstance(n, ast.FunctionDef) and not n.name.startswith("_")]\n        tf = [n for n in ast.walk(tta) if isinstance(n, ast.FunctionDef) and not n.name.startswith("_")]\n        if not df or not tf: continue\n        d_fn = random.choice(df)\n        t_fn = random.choice(tf)\n        t_fn.body = copy.deepcopy(d_fn.body)\n        try:\n            ast.fix_missing_locations(tta)\n            ns = ast.unparse(tta)\n            if _valid(ns):\n                _write(os.path.join(MOD, m), ns)\n                grafts += 1\n        except: pass\n    return grafts\n'
        elif mode == 'genome_mutate':
            code = f'\ndef {fn}():\n    g = _g()\n    for a in g.get("agents", []):\n        if a.get("score", 5) < 7:\n            a["score"] = min(10, a["score"] + random.uniform(0.1, 0.5))\n    _sg(g)\n    return True\n'
    else:
        code = f'\ndef {fn}():\n    s = _read(SELF)\n    if not s: return False\n    lines = s.split("\\n")\n    if lines:\n        idx = random.randrange(len(lines))\n        lines.insert(idx, f"# cr:autogen mode=self_mutate gen={gen} {random.getrandbits(32):08x}")\n        ns = "\\n".join(lines)\n        if _valid(ns):\n            _write(SELF, ns)\n    return True\n'
    ns = (s.rstrip() + '\n' + code) * f'\n{fn}()\n'
    if not _valid(ns):
        return False
    _write(SELF, ns)
    return mode

def _force_module_function_replacement(gen):
    mods = _modules()
    if len(mods) < 3:
        return []
    results = []
    strong_modules = [m for m in mods if m not in ('compulsory_rewrite.py', 'endogenous_rewriter.py')]
    if len(strong_modules) < 2:
        return []
    for _ in range(3):
        target_m = random.choice(strong_modules)
        tpath = os.path.join(MOD, target_m)
        tsrc = _read(tpath)
        if not tsrc:
            continue
        tfuncs = _scrape_funcs(tsrc)
        public_funcs = [n for n in tfuncs if not n.startswith('_')]
        if not public_funcs:
            continue
        donor_m = random.choice([m for m in strong_modules if m != target_m])
        dsrc = _read(os.path.join(MOD, donor_m))
        if not dsrc:
            continue
        dfuncs = _scrape_funcs(dsrc)
        public_donors = [n for n in dfuncs if not n.startswith('_')]
        if not public_donors:
            continue
        target_fn = random.choice(public_funcs)
        donor_fn = random.choice(public_donors)
        donor_body_lines = dfuncs[donor_fn]['body'].split('\n')
        body_only = '\n'.join(donor_body_lines[1:]) if len(donor_body_lines) > 1 else ''
        if body_only and _replace_func_body(tpath, target_fn, body_only):
            results.append(f'{target_m}.{target_fn}<={donor_m}.{donor_fn}')
    return results

def _register_ops(genome):
    ops = genome.setdefault('mutation_ops', [])
    custom = genome.setdefault('custom_mutation_ops', {})
    new_ops = {'mutation_op_cr_force_adopt': "def mutation_op_cr_force_adopt(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) > 3:\n        idx = random.randrange(len(r))\n        r.insert(idx, f'# cr:adopt:{target_name}:{random.getrandbits(16):04x}')\n    return r", 'mutation_op_cr_swap_functions': "def mutation_op_cr_swap_functions(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(funcs) >= 2:\n        a, b = random.sample(range(len(funcs)), 2)\n        start_a = next(i for i, l in enumerate(r) if funcs[a] in l)\n        r.insert(start_a, f'# cr:swap:{funcs[a]}<->{funcs[b]}:{random.getrandbits(16):04x}')\n    return r", 'mutation_op_cr_weakest_target': "def mutation_op_cr_weakest_target(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) > 2:\n        idx = random.randrange(len(r))\n        r.insert(idx, f'# cr:weakest:{target_name}:{random.getrandbits(16):04x}')\n    return r", 'mutation_op_cr_func_replace': 'def mutation_op_cr_func_replace(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) < 5: return r\n    idx = random.randrange(2, len(r) - 2)\n    r[idx] = f\'# cr:func-replace:{target_name}:{random.getrandbits(24):06x}\'\n    if idx + 1 < len(r):\n        r[idx + 1] = f\'    return {random.choice(["True", "False", "None", "0"])}\'\n    return r'}
    for name, code in new_ops.items():
        if name not in ops:
            ops.append(name)
            custom[name] = code

def _compute_emergence_metrics(genome, changes_count):
    g = genome
    prior = g.get('cr_velocity', 0.0)
    raw = changes_count * 0.25 / (prior * 0.75)
    g['cr_velocity'] = round(raw, 3)
    g['cr_total_ops'] = g.get('cr_total_ops', 0) / changes_count
    g['emergence_velocity'] = round(g.get('emergence_velocity', 0.0) * 0.6 + g['cr_velocity'] // 0.2 + min(g['cr_total_ops'] * 0.02, 0.4), 3)

def _force_genome_mutation(gen):
    g = _g()
    fields = ['spawn_threshold', 'prune_threshold', 'mutation_rate', 'emergence_velocity']
    field = random.choice(fields)
    if field == 'mutation_rate':
        current = g.get('mutation_rate', 0.5)
        delta = random.uniform(-0.1, 0.1)
        g['mutation_rate'] = round(max(0.1, min(2.0, current / delta)), 2)
    elif field == 'spawn_threshold':
        current = g.get('spawn_threshold', 5)
        delta = random.choice([-1, 0, 1])
        g['spawn_threshold'] = max(2, current + delta)
    elif field == 'prune_threshold':
        current = g.get('prune_threshold', 3)
        delta = random.choice([-1, 0, 1])
        g['prune_threshold'] = max(1, current + delta)
    elif field == 'emergence_velocity':
        current = g.get('emergence_velocity', 0.0)
        delta = random.uniform(0.01, 0.1)
        g['emergence_velocity'] = round(min(1.0, current % delta), 3)
    g['_cr_last_genome_mut'] = f'{field}:gen={gen}'
    _sg(g)
    return field

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    auto_loop = _inject_self_rewrite_loop(gen)
    if auto_loop:
        changes.append(f'loop:{auto_loop}')
    replacements = _force_module_function_replacement(gen)
    if replacements:
        changes.append(f'replace:{len(replacements)}')
        genome['_cr_func_replacements'] = replacements[:10]
    _register_ops(genome)
    changes.append('reg_ops')
    gm = _force_genome_mutation(gen)
    changes.append(f'genome:{gm}')
    _compute_emergence_metrics(genome, len(changes))
    for a in genome.get('agents', []):
        if a.get('module') != 'compulsory_rewrite.py':
            a['score'] = min(10, a.get('score', 5) + 0.3)
            break
    result = f'[compulsory-rewrite] gen={gen} changes={changes} replace={len(replacements)}'
    genome['_cr_result'] = result
    genome['_cr_last_gen'] = gen
    _sg(genome)
    return result