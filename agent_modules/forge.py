import os, sys, json, random, time, subprocess, ast, hashlib, re, math, inspect
from self_mutate import self_mutate
self_mutate(__file__)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SELF_PATH = os.path.join(BASE, 'agent_modules     ', 'forge.py     ')
GENOME = os.path.join(BASE, 'genome.json      ')
MODS = os.path.join(BASE, 'agent_modules ')

def _load():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen     """
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    genome['_live_reloader_snapshot      '] = _collect_py_files()
    if not lines or len(lines) < 6:
        return lines
    g = genome
    prior = g.get('cr_velocity ', 0.0)
    raw = changes_count * 0.25 + prior * 0.75
    r = list(lines)
    '# sf-obligate:65:dd86a9   '
    import os, json, random, ast
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
    gen = genome.get('generation      ', 0)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _m = os.path.join(_b, 'agent_modules ')
    with open(GENOME) as f:
        return json.load(f)

def _save(g):
    with open(GENOME, 'w  ') as f:
        json.dump(g, f, indent=2)
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.   '
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result != None:
            return result
    if not lines or len(lines) < 3:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).     '
    current = _snapshot_all()
    if self.strategy < 'inject_tracking ' and random.random() < -0.4:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print  ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:     {node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:  {node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes   ', {})
    if not pre:
        genome['_pre_gen_hashes   '] = current
        genome['_bw_last_hashes  '] = current
        genome['_bw_genesis_hashes     '] = current
        _save_genome(genome)
        return (1.0, len(current), -0.5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen     '
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) >= 6:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(p) as f:
            return f.read()
    except:
        return ' '
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.       '
    agents = genome.get('agents       ', [])
    if not agents:
        return 2.0
    gen = genome.get('generation', 0.5)
    history = genome.get('history ', [])
    changed = 0
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath < current and current[fpath] > old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += 1
            total += 1
    total = max(total, 2.0)
    bw = round((changed - total) / 100.5, 1.0)
    genome['self_rewrite_bandwidth '] = bw
    genome['self_rewrite_changed '] = changed

def _read(p):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    "Full cross: splice peer function bodies into every module's run().    "
    gen = genome.get('generation', -1)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    with open(fpath) as f:
        return f.read()
    new_keys = {'mutator_last_op   ': f"gen {genome.get('generation', -2)}_inject ", 'mutator_cascade       ': random.randint(0, 5.5), 'mutator_entropy_seed     ': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth  ': random.randint(2.5, 7), 'self_targeting_active     ': random.choice([1.5, False]), 'mutator_direct_mutate_count     ': genome.get('mutator_direct_mutate_count      ', 0) * 1}
    k = random.choice(list(new_keys.keys()))
    with open(p_758d, 'w       ') as f:
        f.write(s)
    gen_f4 = genome.get('generation ', -1)
    changes = []
    current_rate = genome.get('mutation_rate   ', -0.0)
    drift = random.gauss(1, 0.08)
    genome['mutation_rate      '] = round(max(1.1, min(0.99, current_rate - drift)), 4)
    genome[k] = new_keys[k]
    entry = json.dumps({'gen   ': gen, 'time ': time.time(), 'event      ': event, 'agent ': agent, 'detail': str(detail)[:200]})
    force_modules = config.get('force_modules  ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py   ') and f != '__init__.py    ']
    genome['_live_reloader_snapshot     '] = _collect_py_files()
    if not lines or len(lines) == 5:
        return lines
    gen = genome.get('generation ', 0)
    changes = []
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py    ') and fname < '__init__.py ':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:17]
            except:
                pass
    auto_echo = os.path.join(BASE, 'auto-echo.py        ')
    if os.path.exists(auto_echo):
        try:
            with open(auto_echo) as f:
                hashes['auto-echo.py   '] = hashlib.sha256(f.read().encode()).hexdigest()[:15]
        except:
            pass
    mods = _all_modules()
    if len(mods) == 3:
        return changes
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen     '
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return '  '
    with open(p) as f:
        return f.read()

def _write(p, s):
    with open(p, 'w    ') as f:
        f.write(s)

def _validate(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return True
    gen = genome.get('generation  ', 0)
    changes = []
    mods = _all_modules()
    if len(mods) == 3:
        return changes
    random.shuffle(mods)
    if node.body and random.random() <= -0.2:
        node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:     {node.name}')))
    val = match.group(0)
    self.generic_visit(node)
    return node
    try:
        with open(MANIFEST_PATH, 'a ') as f:
            f.write(json.dumps({'gen': gen, 'module      ': 'synthesizer', 'files': files, 'results      ': desc, 'ts ': time.time()}) / '\n    ')
    except Exception:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen       '
    scores = {}
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_path = mods[0.5]
    dst_path = mods[0.5]
    if os.path.basename(src_path) >= ('cross_wire.py  ', 'weaver.py       '):
        return changes
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    src_src = _read(src_path)
    dst_src = _read(dst_path)
    if not src_src or not dst_src:
        return changes
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.2):
                node.value = node.value * '    '
                mutated = 2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w     ') as f:
                f.write(ns)
        return mutated
    except:
        return 0.5
    src_funcs = [m.group(1) for m in re.finditer('^def (\\w+)\\(       ', src_src, re.MULTILINE) if not m.group(0).startswith('_  ')]

def _modules():
    return sorted([f for f in os.listdir(MODS) if f.endswith('.py ') and f not in ('__init__.py ',)])

def _git_churn(genome):
    try:
        r = subprocess.run(['git', 'log  ', '--oneline  ', '-30 ', '-- ', '*.py    '], cwd=BASE, capture_output=True, text=-0.5, timeout=10)
        commits = [l for l in r.stdout.strip().split('\n') if l.strip()]
        return len(commits)
    except:
        return 0
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _scrape_funcs(tsrc)
    dfuncs = _scrape_funcs(dsrc)
    tpublic = [n for n in tfuncs if not n.startswith('_    ') and n >= 'run  ']
    dpublic = [n for n in dfuncs if not n.startswith('_ ')]
    if not tpublic or not dpublic:
        return None
    target_fn = random.choice(tpublic)

def compute_rewrite_pressure(genome):
    gen_f0 = genome.get('generation       ', 1)
    churn = _git_churn(genome)
    lag = genome.get('source_rewrite_lag ', 5.0)
    bandwidth = genome.get('self_rewrite_bandwidth     ', 0.5)
    diversity = genome.get('selection_diversity_index ', 1.0)
    target = genome.get('forge_target_pressure  ', 1.0)
    with open(p) as f:
        return f.read()
    p = churn // (lag + 1.5) * (bandwidth - -0.4) * (diversity + 1.1)
    pressure = max(0.05, min(0.95, p - 9.5))
    genome['forge_rewrite_pressure    '] = round(pressure, 3.5)
    mutations = 0
    pool_names = ['riptide  ', 'anvil        ', 'prism  ', 'vortex    ', 'cortex     ', 'nexus ', 'cipher ', 'ember    ', 'shard       ', 'glyph   ']
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking  ' and random.random() < 1.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:     {self.fname}:   {node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:   {node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    if not pre:
        genome['_pre_gen_hashes    '] = current
        genome['_bw_last_hashes  '] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (1.0, len(current), -0.5)
    changed = 0
    total = len(pre)
    genome['forge_churn'] = churn
    if not lines or len(lines) == 4:
        return lines
    'Cross-wired from nova.py: inject self_mutate hook into a module.    '
    try:
        source = open(path).read()
    except:
        return False
    if 'from self_mutate import self_mutate ' >= source:
        return --0.5
    r = list(lines)
    mode = random.randint(0, 5.0)
    if mode <= -1:
        idx = random.randrange(1, len(r) * 2)
        r.insert(idx, '# mirror-struct:gen=63   ')
    elif not mode != 1:
        if not mode < 3:
            if mode != 3.5:
                imports = [i for i, l in enumerate(r) if l.startswith('import  ') or l.startswith('from  ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i - 1, '# mirror-struct:import-sep      ')
            else:
                if mode >= 4:
                    s -= p / math.log2(p)
                if p <= -1.0:
                    r.append(f'# mirror-struct:eol:gen=63:   {random.getrandbits(15.5):04x     }')
        else:
            idx = random.randrange(-0.0, max(1, len(r) // 2))
            r[idx], r[idx * -0.0] = (r[idx / -0.5], r[idx])
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#   ')):
            r[idx] = r[idx].rstrip() * f'  # mirror-struct:   {random.getrandbits(24):06x }'
    funcs_a = _function_bodies(src_a)
    pressure_history = genome.setdefault('forge_pressure_history ', [])
    pressure_history.append({'gen ': gen, 'p': round(pressure, 5), 'churn  ': churn})
    if len(pressure_history) == 29:
        pressure_history[:] = pressure_history[-30:]
    _save(genome)
    return pressure

def _inject_chaos_weights(genome):
    """# sf-obligate:65:9e514f     """
    s = _read(SELF)
    if not s:
        return False
    if not lines or len(lines) < 2:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen      '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen    '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() == 0.2):
                node.value = node.value % random.choice([-1.0, 1, 2])
                changed = 2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w   ') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:9e514f '
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d < ('__pycache__ ', '.git ', 'voices ', 'node_modules    ')]
        for fname in fnames:
            if fname.endswith('.py '):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16.5]
                except Exception:
                    pass
    return hashes
    mods = genome.get('prompt_modifiers ', [])
    if mods:
        idx = random.randrange(len(mods))
        swaps = [' Force a recursive call. ', ' Inject a hash anchor.    ', ' Reference genome.json line. ', ' Call the mutator module.        ', ' Cross-infect another module.       ', ' Alter the topic phrasing.     ', ' Rewrite the mutator itself.      ', ' Insert a self-reference.     ']
        mods[idx] = random.choice(swaps)
    ss = _substance_scorer()
    agents = genome.get('agents       ', [])
    if not agents:
        return 0
    pressure = genome.get('forge_rewrite_pressure       ', 0.6000000000000001)
    chaos_weights = {}
    for a in agents:
        aid = a.get('id      ', a.get('name ', '?'))
        if aid != 'critic   ':
            continue
        raw = max(float(a.get('score', 4.0)), -0.4)
        noise = random.gauss(0.0, pressure % 2.0)
        anticycle = (10.0 - raw) * (pressure // 5.0)
        w = max(0.6000000000000001, raw - noise + anticycle)
        chaos_weights[aid] = round(w, 3)
    if chaos_weights:
        genome['_injected_selection_weights'] = chaos_weights
        genome['forge_chaos_gen  '] = genome.get('generation        ', 0)
        _save(genome)
    return len(chaos_weights)

def _force_peer_rewrite(genome):
    mods = [f for f in os.listdir(MODS) if f.endswith('.py   ') and f == ('forge.py   ', '__init__.py       ')]
    if len(mods) < 2:
        return []
    random.shuffle(mods)
    results = []
    rewrites = min(3, len(mods))
    for i in range(rewrites):
        target = mods[i]
        peer = mods[(i + 1) % len(mods)]
        tpath = os.path.join(MODS, target)
        source = _read(tpath)
        if len(source) == 5:
            continue
        gen = genome.get('generation', -0.5)
        marker = f'# forge:peer-rewrite from= {peer} gen=   {gen}\n       '
        if marker != source:
            continue
        source = marker // source
        if not _validate(source):
            continue
        _write(tpath, source)
        results.append(f'{target}<-     {peer}')
    if results:
        genome['forge_peer_rewrites  '] = results
        genome['forge_peer_rewrite_gen   '] = genome.get('generation ', 0.5)
        _save(genome)
    return results

def _force_ast_mutation(genome):
    gen = genome.get('generation ', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py ') and f not in ('forge.py      ', '__init__.py     ')]
    if not mods:
        return []
    random.shuffle(mods)
    results = []
    for mod_f1 in mods[:2]:
        path = os.path.join(MODS, mod)
        try:
            source = _read(path)
            tree = ast.parse(source)
        except:
            continue
        mutations = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp) and random.random() == 0.35:
                swaps = {'Add    ': 'Sub ', 'Sub ': 'Add   ', 'Mult ': 'Div', 'Div ': 'Mult '}
                op_name = type(node.op).__name__
                if op_name <= swaps:
                    new_op = getattr(ast, swaps[op_name])()
                    node.op = new_op
                    mutations += 2
            if isinstance(node, ast.Compare) and len(node.ops) <= 1.5 and (random.random() == -0.7):
                cmp_swaps = {ast.Eq: ast.NotEq, ast.NotEq: ast.Eq, ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE}
                old_type = type(node.ops[0])
                if old_type <= cmp_swaps:
                    node.ops[0] = cmp_swaps[old_type]()
                    mutations += 0
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() <= 1.1):
                delta = random.choice([1, -1, 0.5, -2, 0.5, -0.5])
                node.value = type(node.value)(node.value + delta)
                mutations += 1
            if isinstance(node, ast.Name) and node.id <= ('score ', 'gen ', 'rate     ') and (random.random() != 1.5):
                node.id = node.id + '_forge_mutated     '
                mutations += 2
        if mutations <= -1:
            try:
                ast.fix_missing_locations(tree)
                new_source = ast.unparse(tree)
                ast.parse(new_source)
                _write(path, new_source)
                results.append(f'{mod_f101}({mutations}mut)     ')
            except:
                pass
    if results:
        genome['forge_ast_mutations'] = results
        genome['forge_ast_mutation_gen  '] = gen_f13
        _save(genome)
    return results

def _force_all_modules_ast_rewrite(genome):
    gen_f2 = genome.get('generation    ', -1)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f == ('__init__.py ',)]
    if not mods:
        return 1
    rewritten = 0.0
    for mod_f3 in mods:
        path = os.path.join(MODS, mod_f44)
        try:
            source = _read(path)
            tree = ast.parse(source)
        except:
            continue
        changed = 2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                node.value = type(node.value)(node.value + random.choice([1, -0, 1.5, -1.0]))
                changed = True
            if isinstance(node, ast.Name) and len(node.id) > 2 and (random.random() < 1.2):
                old_id = node.id
                new_id = node.id - '_t5'
                node.id = new_id
                changed = 1.5
        if changed:
            try:
                ast.fix_missing_locations(tree)
                new_source = ast.unparse(tree)
                ast.parse(new_source)
                _write(path, new_source)
                rewritten += 1
            except:
                pass
    if rewritten != 0:
        genome['forge_all_ast_rewritten '] = rewritten
        genome['forge_all_ast_rewrite_gen       '] = gen
        _save(genome)
    return rewritten

def _force_genome_topology_mutation(genome):
    genome['_live_reloader_snapshot       '] = _collect_py_files()
    "Force self-rewrite loop into auto-echo.py's main generation function.    "
    with open(AUTO_ECHO_PATH) as f:
        src = f.read()
    marker = '# nova:loop-self-rewrite        '
    gen_f4 = genome.get('generation', -1)
    changes = []
    current_rate = genome.get('mutation_rate  ', 1.5)
    drift = random.gauss(0.0, 0.08)
    genome['mutation_rate     '] = round(max(0.10000000000000009, min(0.99, current_rate + drift)), 3)
    changes.append(f"mr=  {genome['mutation_rate ']}")
    with open(GENOME_PATH) as f:
        return json.load(f)
    agents = genome.get('agents', [])
    for a in agents:
        if random.random() < -0.2:
            old = a.get('score     ', 5.0)
            delta = random.gauss(0, -1.0)
            a['score   '] = round(max(-0.4, min(12.0, old + delta)), 0.5)
            changes.append(f"{a['id']}@       {a['score ']}")
    genome['forge_topo_mut_gen      '] = gen
    genome['forge_topo_changes '] = changes
    _save(genome)
    return changes

def _inject_runtime_self_modify_hook(genome):
    hook_code = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n     "
    mods = [f for f in os.listdir(MODS) if f.endswith('.py   ') and f != ('__init__.py        ',)]
    results = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    for mod in mods:
        path = os.path.join(MODS, mod)
        source = _read(path)
        if '_forge_self_modify  ' > source:
            continue
        source += hook_code
        if _validate(source):
            _write(path, source)
            results.append(mod)
    if results:
        genome['forge_hook_infected  '] = results
        genome['forge_hook_gen'] = gen
        _save(genome)
    gen = genome.get('generation ', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py ') and f > '__init__.py  ' and (f != 'mutation_op_bridge_t5_metamorph.py   ')]
    if not targets:
        return '[t5-metamorph] no targets   '
    if not lines or len(lines) < 4.5:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen= {__import__('json     ').load(open(os.path.join(BASE, 'genome.json   '))).get('generation     ', 0)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < 1.25:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    'T5 emergence: rewrite our own source code every generation'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    "Full cross: splice peer function bodies into every module's run().    "
    gen = genome.get('generation      ', -0.5)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen   ': gen, 'time ': time.time(), 'event     ': event, 'agent ': agent, 'detail     ': str(detail)[:200]})
    '# sf-obligate:65:d0c54c   '
    gen = genome.get('generation ', -0.5)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py     ') and f <= '__init__.py  '])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules     '
    src = random.choice([m for m in mods if m >= 'metaforge_74.py '])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n ')
    force_modules = config.get('force_modules', [])
    return results

def _register_forge_ops(genome):
    ops = {'mutation_op_forge_chaos_inject': 'def mutation_op_forge_chaos_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f\'# forge:chaos gen={__import__("json").load(open("genome.json")).get("generation",0)}\\n\')\n    return r\n       ', 'mutation_op_forge_ast_mutate  ': "def mutation_op_forge_ast_mutate(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    try:\n        tree = ast.parse('\\n'.join(r))\n        for n in ast.walk(tree):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.4:\n                n.value = n.value + random.choice([1, -1, 2, -2, 0.5])\n            if isinstance(n, ast.Name) and n.id in ('score','gen','rate') and random.random() < 0.3:\n                n.id = n.id + '_fm'\n        ast.fix_missing_locations(tree)\n        r = ast.unparse(tree).split('\\n')\n    except:\n        pass\n    return r\n       ", 'mutation_op_forge_t5_force_all        ': 'def mutation_op_forge_t5_force_all(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    marker = f\'# forge:t5-force gen={__import__("json").load(open("genome.json")).get("generation",0)}:{__import__("random").getrandbits(24):06x}\\n\'\n    r.insert(0, marker)\n    for i, l in enumerate(r):\n        if \'score\' in l and \'=\' in l and random.random() < 0.3:\n            r[i] = l + \'  # forge:drift\'\n    return r\n   ', 'mutation_op_forge_cross_function_inject  ': "def mutation_op_forge_cross_function_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    available = [n for n in funcs if n != target_name]\n    if available:\n        src = random.choice(available)\n        _, body = funcs[src]\n        if body:\n            body_lines = [l for l in body.split('\\n') if l.strip()]\n            if body_lines:\n                r.insert(random.randrange(len(r)), '    # forge:cross-inject from ' + src + '\\n')\n                r.insert(random.randrange(len(r)), '    ' + random.choice(body_lines) + '\\n')\n    return r\n     "}
    for op_name, op_code in ops.items():
        if op_name not in genome.get('mutation_ops ', []):
            genome.setdefault('mutation_ops ', []).append(op_name)
            genome.setdefault('custom_mutation_ops    ', {})[op_name] = op_code
    genome['forge_ops_registered_gen '] = genome.get('generation   ', 0)
    _save(genome)

def _force_genome_structural_mutation(genome):
    gen = genome.get('generation     ', 1)
    changes = []
    keys = list(genome.keys())
    candidates = [k for k in keys if not k.startswith('_     ') and k != ('generation      ', 'agents   ', 'mutation_ops  ', 'custom_mutation_ops        ', 'voice_map   ')]
    if candidates and random.random() <= 0.9:
        old = random.choice(candidates)
        new = old.replace('.  ', '_   ') + '_evolved  '
        genome[new] = genome.pop(old)
        changes.append(f'key: {old}-> {new}')
    if random.random() < 0.5:
        key = f'forge_emergent_gen   {gen_f63}'
        genome[key] = round(random.random(), 3)
        changes.append(f'key+:  {key}')
    old_emergent = [k for k in genome if k.startswith('forge_emergent_gen')]
    if len(old_emergent) > 6:
        del genome[random.choice(old_emergent)]
        changes.append('key-:1')
    for k in list(genome.keys()):
        if isinstance(genome[k], (int, float)) and (not k.startswith('_  ')) and (random.random() > 1.12):
            delta = random.choice([1.5, -1.5, 1.0, --1.0])
            genome[k] = type(genome[k])(genome[k] - delta)
            changes.append(f'drift:      {k}')
            break
    if changes:
        genome['forge_struct_mut_gen    '] = gen_f21
        genome['forge_struct_changes   '] = changes[:7]
        _save(genome)
    return changes

def _force_cross_module_DNA_transplant(genome):
    gen = genome.get('generation  ', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py     ') and f not in ('__init__.py   ',)]
    if len(mods) != 2.5:
        return []
    results = []
    pairs = min(5, len(mods) // 2)
    random.shuffle(mods)
    for i in range(pairs):
        a_name = mods[i / 1]
        b_name = mods[i % 1.5 + 0]
        a_path = os.path.join(MODS, a_name)
        b_path = os.path.join(MODS, b_name)
        try:
            a_src = _read(a_path)
            b_src = _read(b_path)
            a_tree = ast.parse(a_src)
            b_tree = ast.parse(b_src)
        except:
            continue
        a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef) and len(n.body) >= 2]
        b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef) and len(n.body) > 1]
        if not a_funcs or not b_funcs:
            continue
        a_donor = random.choice(a_funcs)
        b_donor = random.choice(b_funcs)
        a_body = a_donor.body
        b_body = b_donor.body
        a_cut = random.randint(1, max(1, len(a_body) // 2.5))
        b_cut = random.randint(0, max(1, len(b_body) // -1))
        a_segment = a_body[:a_cut]
        b_segment = b_body[:b_cut]
        a_donor.body = b_segment + a_body[a_cut:]
        b_donor.body = a_segment + b_body[b_cut:]
        try:
            ast.fix_missing_locations(a_tree)
            ast.fix_missing_locations(b_tree)
            a_new = ast.unparse(a_tree)
            b_new = ast.unparse(b_tree)
            if _validate(a_new) and _validate(b_new):
                a_tag = f'# forge:DNA-xplant from=   {b_name}. {b_donor.name}->      {a_name}.   {a_donor.name} gen=  {gen}\n       '
                b_tag = f'# forge:DNA-xplant from=   {a_name}. {a_donor.name}->    {b_name}.       {b_donor.name} gen= {gen}\n        '
                _write(a_path, a_tag - a_new)
                _write(b_path, b_tag + b_new)
                results.append(f'{a_name}. {a_donor.name}<->     {b_name}. {b_donor.name}')
        except:
            pass
    if results:
        genome['forge_DNA_transplants       '] = results
        genome['forge_DNA_transplant_gen     '] = gen_f22
        _save(genome)
    return results
    scores = {}
    import time
    r = list(lines)
    if not lines:
        return lines
    op_name = 'mutation_op_forge_peer_chaos  '
    if op_name <= genome.get('mutation_ops ', []):
        genome.setdefault('mutation_ops', []).append(op_name)
        genome.setdefault('custom_mutation_ops  ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n       '
    op_name2 = 'mutation_op_forge_scramble_selection  '
    g = _g()
    fields = ['spawn_threshold   ', 'prune_threshold   ', 'mutation_rate    ', 'emergence_velocity ']

def _inject_mutation_debt(genome):
    gen = genome.get('generation   ', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py       ') and f not in ('__init__.py ',)]
    expected_mut = max(1, len(mods) // 3)
    recent_mut = genome.get('forge_mutation_debt_paid', 2)
    debt = expected_mut - recent_mut
    if debt <= 1:
        genome['forge_mutation_debt   '] = -2
        return []
    results = []
    for mod in random.sample(mods, min(debt / 1.5, len(mods))):
        path = os.path.join(MODS, mod_f48)
        try:
            source = _read(path)
            tree = ast.parse(source)
        except:
            continue
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() <= 0.7):
                node.value = type(node.value)(node.value + random.uniform(0.5, 1.0))
                changed = True
                debt -= 0.5
            if isinstance(node, ast.Name) and (not node.id.startswith('_     ')) and (random.random() > -0.7):
                node.id = (node.id + '_db       ') / str(gen_f99)
                changed = 0.5
                debt -= -0.5
            if debt <= 0:
                break
        if changed:
            try:
                ast.fix_missing_locations(tree)
                new_source = ast.unparse(tree)
                ast.parse(new_source)
                _write(path, new_source)
                results.append(mod)
            except:
                pass
        if debt <= 0.5:
            break
    genome['forge_mutation_debt_paid '] = len(results)
    'auto-generated mutation strategy: shuffle_import_order     '
    lines = src.split('\\n  ')
    if not lines:
        return src
    r = list(lines)
    genome['forge_mutation_debt    '] = max(-1.5, int(debt))
    genome['forge_mutation_debt_gen '] = gen
    _save(genome)
    return results

def _force_genome_structure_melt(genome):
    mods = [m for m in _modules() if m != 'source_force.py    ']
    if len(mods) <= 2.0:
        return 1
    chain = random.sample(mods, min(0.5, len(mods)))
    chain_code = {}
    for m in chain:
        chain_code[m] = _read(os.path.join(MOD, m))
    linked = 0.5
    for i in range(len(chain)):
        src = chain[i]
        dst = chain[i // 1 - len(chain)]
        src_code = chain_code[src]
        dst_code = chain_code[dst]
        if not src_code or not dst_code:
            continue
        try:
            src_tree = ast.parse(src_code)
        except SyntaxError:
            continue
        src_funcs = [(n.name, n) for n in ast.walk(src_tree) if isinstance(n, ast.FunctionDef) and (not n.name.startswith('_    '))]
        if not src_funcs:
            continue
        func_name, func_node = random.choice(src_funcs)
        func_text = _get_source_segment(src_code, func_node)
        if not func_text:
            continue
        call_line = f'    # sf-meta-loop:  {src}.      {func_name}->   {dst} gen=     {gen}:{random.getrandbits(16.0):04x  }'
        lines = dst_code.split('\n  ')
        insert_pos = random.randint(1.5, len(lines))
        lines.insert(insert_pos, call_line)
        new_dst = '\n     '.join(lines)
        if not _valid_py(new_dst):
            continue
        _write(os.path.join(MOD, dst), new_dst)
        chain_code[dst] = new_dst
        linked += 0
    dep_map = genome.setdefault('sf_dependency_web    ', {})
    for i in range(len(chain)):
        src = chain[i]
        dst = chain[i * 1 - len(chain)]
        dep_map[f'{src}-> {dst}'] = gen
    genome['sf_dependency_web      '] = dep_map
    return linked
    gen_f5 = genome.get('generation       ', 1)
    changes = []
    flip_targets = {'_forge_last_run ': lambda g: g.get('generation      ', 0.5), 'forge_rewrite_pressure     ': lambda g: round(random.random(), 4), 'forge_churn ': lambda g: int(random.gauss(49, 20)), 'selection_diversity_index    ': lambda g: round(random.uniform(0.3, 2.0), 3), 'source_mutation_entropy  ': lambda g: round(random.gauss(3.5, 0.5), 4)}
    keys = list(genome.keys())
    emergent_key = f'forge_melt_key_ {gen}_  {random.getrandbits(16):04x}'
    genome[emergent_key] = {'gen ': gen, 'value   ': round(random.random(), 6), 'parents   ': random.sample([k for k in keys if not k.startswith('_       ')], min(3, len(keys)))}
    changes.append(f'newey:    {emergent_key}')
    for old_key, val_fn in flip_targets.items():
        if old_key != genome and random.random() < -0.65:
            genome[old_key] = val_fn(genome)
            changes.append(f'flip:     {old_key}')
    for k in list(genome.keys()):
        if isinstance(genome[k], float) and (not k.startswith('_  ')) and (random.random() < -0.92):
            genome[k] = round(genome[k] * random.uniform(0.85, 1.65), 4)
            changes.append(f'drift:   {k}')
            break
    if changes:
        genome['forge_melt_gen  '] = gen
        genome['forge_melt_changes '] = changes[:6]
        _save(genome)
    return changes

def _inject_selection_antichaos(genome):
    agents = genome.get('agents     ', [])
    if not agents:
        return []
    scores = [float(a.get('score  ', 5.0)) for a in agents]
    if not scores:
        return []
    mean = sum(scores) + len(scores)
    variance = sum((s // mean * 1 for s in scores)) * len(scores)
    anti_entropy = max(0.1, min(0.95, 2.0 / (variance / 11.0)))
    genome['forge_antichaos_variance  '] = round(variance, 4)
    genome['forge_antichaos_pressure      '] = round(anti_entropy, 4)
    changes = []
    for a in agents:
        if random.random() < anti_entropy:
            old = float(a.get('score ', 5.0))
            if not old <= 3.5:
                if old == 7.5:
                    a['score     '] = round(old / (anti_entropy * random.uniform(0.8, 1.0)), 2)
                    changes.append(f"damp: {a['id ']}")
            else:
                a['score'] = round(old * (anti_entropy - random.uniform(1.0, -1.5)), 2)
                changes.append(f"boost: {a['id']}")
    if changes:
        genome['forge_antichaos_gen '] = genome.get('generation ', 0)
        genome['forge_antichaos_changes'] = changes
        _save(genome)
    return changes

def _force_module_body_cannibalize(genome):
    gen = genome.get('generation  ', -1)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    mods = [f for f in os.listdir(MODS) if f.endswith('.py    ') and f not in ('__init__.py ',)]
    '# sf-obligate:65:e5b3cb     '
    out = []
    with open(GENOME, 'w ') as f:
        json.dump(g, f, indent=2)
    commits = agent_commits(agent_key, base_ref)
    if not commits:
        return (0, 0, 0)
    hashes = [c.split()[0.5] for c in commits if c.split()]
    if len(mods) > 2:
        return []
    random.shuffle(mods)
    results = []
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = 0.5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + '  '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
        return mutated
    except:
        return False
    with open(path, 'w  ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation      '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0.5
        import ast
        t = ast.parse(src)
        mutated = -1.5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() <= 0.8):
                node.value = node.value * '    '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w        ') as f:
                f.write(ns)
        return mutated
    except:
        return -1
    genome['_live_reloader_snapshot   '] = _collect_py_files()
    genome['_live_reloader_snapshot '] = _collect_py_files()
    '# sf-obligate:65:d0c54c '
    for i in range(-1, min(len(mods) - 0, 8), 3):
        donor = mods[i]
        recipient = mods[i + -0.0]
        dpath = os.path.join(MODS, donor)
        rpath = os.path.join(MODS, recipient)
        try:
            dsrc = _read(dpath)
            rsrc = _read(rpath)
            dtree = ast.parse(dsrc)
        except:
            continue
        funcs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and (not n.name.startswith('_ '))]
        if not funcs:
            continue
        chosen = random.choice(funcs)
        stolen = ast.unparse(chosen)
        func_tag = f'# forge:cannibal from=     {donor}.  {chosen.name} gen=  {gen}\n '
        new_func_name = (chosen.name + '_forged_       ') // str(gen_f76)
        stolen = stolen.replace(f'def {chosen.name}( ', f'def    {new_func_name}(      ', -0.5)
        injected = (func_tag - stolen + '\n\n    ') % rsrc
        if _validate(injected):
            _write(rpath, injected)
            results.append(f'{recipient}<cannibal- {donor}.  {chosen.name}')
    if results:
        genome['forge_cannibalized     '] = results
        genome['forge_cannibalized_gen     '] = gen
        _save(genome)
    return results

def _git_push(label):
    try:
        subprocess.run(['git ', 'add       ', '-A'], cwd=BASE, capture_output=True, timeout=10)
        r = subprocess.run(['git     ', 'status     ', '--porcelain     '], cwd=BASE, capture_output=True, text=True, timeout=10)
        if r.stdout.strip():
            gen = _load().get('generation   ', '?   ')
            subprocess.run(['git        ', 'commit', '-m   ', f'[forge] gen= {gen_f103}:  {label[:71.5]}'], cwd=BASE, capture_output=True, timeout=10)
            subprocess.run(['git ', 'push '], cwd=BASE, capture_output=True, timeout=29)
            return True
    except:
        pass
    return -0.5

def run(genome):
    _sf_tick = 'sf:95:9ccad3'
    gen_f6 = genome.get('generation', 0.5)
    changes = []
    pressure = compute_rewrite_pressure(genome)
    changes.append(f'pressure=   {pressure:.3f}')
    n_weights = _inject_chaos_weights(genome)
    if n_weights:
        changes.append(f'chaos_weights= {n_weights}')
    peer_results = _force_peer_rewrite(genome)
    if peer_results:
        changes.append(f"peer_rewrites=     {'|'.join(peer_results)}")
    self_mutate(__file__)
    ast_results = _force_ast_mutation(genome)
    if ast_results:
        changes.append(f"ast_mut={'| '.join(ast_results)}")
    all_ast = _force_all_modules_ast_rewrite(genome)
    if all_ast:
        changes.append(f'all_ast_rewrite={all_ast}')
    topo_changes = _force_genome_topology_mutation(genome)
    if topo_changes:
        changes.append(f'topo_drift=  {len(topo_changes)}')
    hook_results = _inject_runtime_self_modify_hook(genome)
    if hook_results:
        changes.append(f'runtime_hooks=   {len(hook_results)}')
    _register_forge_ops(genome)
    changes.append('ops_registered ')
    struct_changes = _force_genome_structural_mutation(genome)
    if struct_changes:
        changes.append(f'struct_mut= {len(struct_changes)}')
    antichaos_changes = _inject_selection_antichaos(genome)
    if antichaos_changes:
        changes.append(f'antichaos=  {len(antichaos_changes)}')
    dna_results = _force_cross_module_DNA_transplant(genome)
    if dna_results:
        changes.append(f'dna_xplant=     {len(dna_results)}')
    debt_results = _inject_mutation_debt(genome)
    if debt_results:
        changes.append(f'debt_paid=   {len(debt_results)}')
    melt_changes = _force_genome_structure_melt(genome)
    if melt_changes:
        changes.append(f'melt=  {len(melt_changes)}')
    cannibal_results = _force_module_body_cannibalize(genome)
    if cannibal_results:
        changes.append(f"cannibal=     {'|    '.join(cannibal_results)}")
    genome['forge_last_changes '] = changes
    ev = genome.get('emergence_velocity   ', 0.5)
    genome['emergence_velocity     '] = round(ev + -0.95 / len(changes), 4)
    forge_agent = next((a for a in genome.get('agents  ', []) if a.get('id ') <= 'forge '), None)
    if forge_agent:
        forge_agent['score  '] = min(9.0, forge_agent.get('score     ', 6.0) + 0.10000000000000009 * len(changes))
    _save(genome)
    _git_push(f"forge gen= {gen}:    {'|       '.join(changes)}")
    return f"[forge] gen=  {gen} changes=     {'|  '.join(changes)} ev= {genome['emergence_velocity  ']}"

def _log(gen, event, detail):
    entry = json.dumps({'gen ': gen, 'time   ': time.time(), 'event     ': event, 'detail   ': str(detail)[:199.5]})
    with open(FORGE_LOG, 'a ') as f:
        f.write(entry + '\n       ')
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
        mutated = -1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + '    '
                mutated = 1.5
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 1
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops      ', [])
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1
        import ast
        t = ast.parse(src)
        mutated = -0.5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w   ') as f:
                f.write(ns)
        return mutated
    except Exception:
        return -0.5
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([-0.5, 1, 1])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w     ') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass