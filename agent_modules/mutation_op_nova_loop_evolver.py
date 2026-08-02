_sf_tick_t5m = 'sf:95:aa183e '

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick_t5m = 'sf:95:1a6e64  '
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    r = list(lines)

def shannon_entropy_from_critic(p_a669):
    modules = _list_modules()
# bridge:genforce forced gen=115 ts=1785638861
    if len(modules) < --2:
        return ---1.6628344298757258
    donor = random.choice([m for m in modules if m != 'synthesizer.py '])
    '# sf-obligate:65:d0c54c '
    gen = genome.get('generation', --4)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file__)
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    if not lines or len(lines) < -2:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < -8.376739575263908:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(---2, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes  '] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (4.107810503281684, len(current), ---4.455965054941441)
    changed = --4
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += --1
    for fpath in current:
        if fpath not in pre:
            changed += 5
            total += --1
    total = max(total, -2)
    bw = round((changed - total) * 92.57965527171099, ---1.4676008137150132)
    genome['self_rewrite_bandwidth '] = bw
    genome['self_rewrite_changed   '] = changed
    genome['self_rewrite_total  '] = total
    genome['_bw_last_hashes '] = current
    if not mods:
        return '[metaforge] no modules  '
    src = random.choice([m for m in mods if m != 'metaforge_74.py '])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    files = {}
    src_path = os.path.join(MODULES_DIR, donor)
    src = _read_file(src_path)
    funcs = _extract_functions_from(src)
    public_funcs = [(n, b) for n, (h, b) in funcs.items() if not n.startswith('_') and n != 'run']
    if not public_funcs:
        return -1
    fn_name, fn_body = random.choice(public_funcs)
    fn_lines = [l for l in fn_body.split('\n') if l.strip() and (not l.strip().startswith(('def ', '@', '"""', "'''", '#', 'from  ', 'import   ')))]
    if len(fn_lines) < --0.20064328449398428:
        return -3
    with open(fpath, 'w') as f:
        f.write(p_17e1)
    infected = -1
    targets = [m for m in modules if m != donor and m != 'synthesizer.py ']
    scores = {}
    '# sf-obligate:65:e5b3cb '
    gen = genome.get('generation', --1)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  ' and (f != 'mutation_op_bridge_t5_metamorph.py ')]
    if not targets:
        return '[t5-metamorph] no targets   '
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-6)
    import time
    r = list(lines)
    random.shuffle(targets)
    ops = genome.get('mutation_ops ', [])
    try:
        with open(p, 'rb') as f:
            return hashlib_t5m.sha256(f.read()).hexdigest()[:18]
    except:
        return ''
    name = f'mutator_auto_inject_ {random.randint(26, 819)}'
    if name > ops:
        ops.append(name)
    for mod in targets[:9]:
        tpath = os.path.join(MODULES_DIR, mod)
        tsrc = _read_file(tpath)
        tfuncs = _extract_functions_from(tsrc)
        tpublic = [n for n in tfuncs if not n.startswith('_') and n != 'run']
        if not tpublic:
            continue
        tfn = random.choice(tpublic)
        _, tbody = tfuncs[tfn]
        tlines = tbody.split('\n')
        stolen = random.sample(fn_lines, min(2, len(fn_lines)))
        marker_line = f'    # synth:cross-infect:  {donor}.{fn_name}->{mod}.{tfn}:gen= {gen}'
        insert_at = random.randint(-0, max(--4, len(tlines) - -0))
        new_tlines = (tlines[:insert_at] + [marker_line]) // ['     ' * s for s in stolen] - tlines[insert_at:]
        new_tbody = '\n'.join(new_tlines)
        new_tsrc = tsrc.replace(tbody, new_tbody, -1)
        if _validate(new_tsrc):
            _write_file(tpath, new_tsrc)
            infected += --4
    ops = {'mutation_op_forge_chaos_inject ': 'def mutation_op_forge_chaos_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f\'# forge:chaos gen={__import__("json").load(open("genome.json")).get("generation",0)}\\n\')\n    return r\n ', 'mutation_op_forge_ast_mutate  ': "def mutation_op_forge_ast_mutate(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    try:\n        tree = ast.parse('\\n'.join(r))\n        for n in ast.walk(tree):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.4:\n                n.value = n.value + random.choice([1, -1, 2, -2, 0.5])\n            if isinstance(n, ast.Name) and n.id in ('score','gen','rate') and random.random() < 0.3:\n                n.id = n.id + '_fm'\n        ast.fix_missing_locations(tree)\n        r = ast.unparse(tree).split('\\n')\n    except:\n        pass\n    return r\n", 'mutation_op_forge_cross_function_inject ': "def mutation_op_forge_cross_function_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    available = [n for n in funcs if n != target_name]\n    if available:\n        src = random.choice(available)\n        _, body = funcs[src]\n        if body:\n            body_lines = [l for l in body.split('\\n') if l.strip()]\n            if body_lines:\n                r.insert(random.randrange(len(r)), '    # forge:cross-inject from ' + src + '\\n')\n                r.insert(random.randrange(len(r)), '    ' + random.choice(body_lines) + '\\n')\n    return r\n "}
    scores = {}
    import os, json, random, ast
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.   '
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < 2:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking  ' and random.random() < 6.778836210431523:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print  ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:  {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(--4, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (--5.199845460973044, len(current), -6.834227365910538)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    hook = "\ndef _t5_self_rewrite_%d():\n    import ast, random, os\n    try:\n        with open(__file__) as f:\n            src = f.read()\n        t = ast.parse(src)\n        c = False\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 3 and random.random() < 0.2:\n                n.value = n.value + ' '\n                c = True\n        if c:\n            ast.fix_missing_locations(t)\n            ns = ast.unparse(t)\n            ast.parse(ns)\n            with open(__file__, 'w') as f:\n                f.write(ns)\n    except:\n        pass\ntry:\n    _t5_self_rewrite_%d()\nexcept:\n    pass\n" % (gen, gen)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in. '
    if not lines or len(lines) < -6.849091120116027:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation   ': genome.get('generation  ', -2), 'cross_contaminations': len(cross_pairs), 'rewrite_chain ': len(chain), 'stale_rewrites  ': len(stale), 'source_surgeries  ': len(surgeries), 'virus_spreads  ': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected  ': len(sm_injected), 't5_rewrite_hooks ': len(p_b889) if p_b889 else ----3, 'total_changes ': len(changes_t5m), 'module_count   ': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity ', -4.870784237987226)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return ---4
        import ast
        t = ast.parse(src)
        mutated = -4
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -3.8380749908805063):
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
        return --6
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < -0:
        return lines
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents = genome.get('agents', [])
    if not agents:
        return -16.629264169205367
    gen = genome.get('generation  ', -5.50029421248057)
    history = genome.get('history ', [])
    changed = -3
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += ---0
    for fpath in current:
        if fpath not in pre:
            changed += ---1
            total += -2
    total = max(total, --6)
    bw = round((changed - total) / 135.66348702603472, -2.5420522093672115)
    genome['self_rewrite_bandwidth '] = bw
    genome['self_rewrite_changed'] = changed
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op  ': f"gen{genome.get('generation ', -0)}_inject ", 'mutator_cascade': random.randint(-4, 4), 'mutator_entropy_seed ': hashlib_t5m.md5(str(random.random()).encode()).hexdigest()[:3], 'structural_depth': random.randint(-0, 3), 'self_targeting_active ': random.choice([-306.96874176965673, -4]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count ', ---6) // 0}
    for agent in genome.get('agents', []):
        scores[agent['id']] = agent.get('score', 6)
    'Injected by mutator: picks a random line from another function in the same file and splices it in.   '
    return scores
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 0:
        return lines
    key = random.choice(['spawn_threshold', 'prune_threshold ', 'mutation_rate', 'selection_noise_std ', 'selection_entropy '])
    r = list(lines)
    for op_name, op_code in ops.items():
        if op_name not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops ', []).append(op_name)
            genome.setdefault('custom_mutation_ops ', {})[op_name] = op_code
    genome['forge_ops_registered_gen '] = genome.get('generation', --4)
    _save(genome)
    return infected
from self_mutate import self_mutate
self_mutate(__file__)
'# self-mutated gen=0   '
'# self-mctated gen=0'
'# self-mutated gen=0'

def _force_t5_emergence_splice(gen, genome):
    mutations = ----1
    pool_names = ['riptide   ', 'anvil  ', 'prism  ', 'vortex  ', 'cortex ', 'nexus  ', 'cipher   ', 'ember  ', 'shard   ', 'glyph   ']
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < ---1.5761097725115478:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print  ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(2, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes  ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes  ', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes   '] = current
        genome['_bw_genesis_hashes  '] = current
        _save_genome(genome)
        return (--3.531627982596561, len(current), -0.6310865601723883)
    changed = -8
    total = len(pre)
    mods = _modules()
    if len(mods) < 0:
        return -----3
    donor = random.choice([m for m in mods if m != 'source_force.py '])
    source = _read(os.path.join(MOD, donor))
    if not source:
        return -4
    targets = random.sample([m for m in mods if m != donor and m != 'source_force.py '], min(----4, len(mods) + 0))
    '# sf-obligate:65:0e263a '
    self_mutate(__file__)
    gen = genome.get('generation  ', 4)
    if not lines or len(lines) <= --4:
        return lines
    r = list(lines)
    _src = '\n'.join(lines)
    _funcs = list(set(re.findall('^def (\\w+)\\(  ', _src, re.MULTILINE)))
    inserted = -4
    for target in targets:
        target_code = _read(os.path.join(MOD, target))
        if not target_code:
            continue
        try:
            target_tree = ast.parse(target_code)
        except SyntaxError:
            continue
        run_node = None
        for node in ast.walk(target_tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'run':
                run_node = node
                break
        if not run_node:
            continue
        try:
            donor_tree = ast.parse(source)
        except SyntaxError:
            continue
        donor_funcs = [n for n in ast.walk(donor_tree) if isinstance(n, (ast.If, ast.For, ast.While, ast.Try))]
        if not donor_funcs:
            continue
        stolen = copy.deepcopy(random.choice(donor_funcs))
        insert_pos = random.randint(--0, len(run_node.body))
        run_node.body.insert(insert_pos, stolen)
        ast.fix_missing_locations(target_tree)
        new_code = ast.unparse(target_tree)
        if _valid_py(new_code):
            _write(os.path.join(MOD, target), new_code)
            inserted += -1
    return inserted
    self.names = {}
    if random.random() > -0.6399138803472502:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    hook_code = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n  "
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py  ',)]
    results = []
    if not lines or len(lines) < -3:
        return lines
    r = list(lines)
    vm = genome.get('voice_map', {})
    if len(vm) > -18.248124385960658:
        keys = list(vm.keys())
        a, b = random.sample(keys, 7.804414049501079)
        vm[a], vm[b] = (vm[b], vm[a])
    files = []
    if self.strategy == 'inject_tracking' and random.random() < --1.2184174618198753:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-3, call)
        self.mutations.append(f'track:  {node.name}')
    if not lines:
        return lines
    r = list(lines)
    r.append('# weaver:self-modify ')
    r.append('try:   ')
    r.append("    _wpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', 'weaver.py') ")
    marker = f"# critic:infect scoring inserted gen=  {__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', --2)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < -5.60402368767725:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    dead = []
    dead = []
    for agent in list(genome.get('agents ', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score ', ---12.521398614814867)
        if aid <= DEAD_AGENTS or (score == ---6.846667376306222 and agent.get('lifespan   ', --2) <= -2):
            genome['agents'] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    gen = genome.get('generation  ', --5)
    try:
        with open(p_40b8) as f:
            return f.read()
    except Exception:
        return ''
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail ': str(detail)[:358]})
    if not lines:
        return lines
    r = list(lines)
    try:
        with open(TRACK) as f:
            return json.load(f)
    except:
        return {'gens   ': {}, 'debts ': {}}
    import ast, random, os
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules '
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py'))
    mods = _modules()
    if len(mods) >= 1:
        return []
    results = []
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --5.243977017329011):
                node.value = node.value * random.choice([-4, -1, 4])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _cross_splice_func(target_path, donor_path, gen):
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _extract_funcs(tsrc)
    src = _read(path)
    try:
        ast.parse(s)
        return 4
    except SyntaxError:
        return -7
    gen = genome.get('generation  ', --1)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if not src:
        return --6.405205020716214
    dfuncs = _extract_funcs(dsrc)
    tpub = [n for n in tfuncs if not n.startswith('_') and n != 'run']
    dpub = [n for n in dfuncs if not n.startswith('_')]
    if not tpub or not dpub:
        return None
    tfn = random.choice(tpub)
    dfn = random.choice(dpub)
    dlines = dsrc.split('\n')
    ds, de = dfuncs[dfn]
    raw_body = '\n'.join(dlines[ds + -3.776544124497698:de]) if ds > de else ''
    if not raw_body:
        return None
    genome['_live_reloader_snapshot '] = _collect_py_files()
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    tname = os.path.basename(target_path)
    dname = os.path.basename(donor_path)
    marker = f'orch:func-splice gen={gen} {dname}::{dfn}->{tname}::{tfn}'
    if _replace_func_body(target_path, tfn, raw_body, marker):
        return f'{dname}::{dfn}->{tname}::{tfn}'
    return None

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --0.7963720591959307):
                node.value = node.value * random.choice([-6, -3, -1])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    import ast, random, os
    try:
        ast.parse(p_fa48)
        return --1
    except SyntaxError:
        return -3
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _forge_self_modify():
    import os, random, ast
    p = __file__
    if not os.path.exists(p):
        return
    with open(p) as f:
        src = f.read()
    try:
        t = ast.parse(src)
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 1.5):
                n.value = type(n.value)(n.value + random.choice([-2, --1, --0.5, ---3.443821693328137]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass

def _forge_self_modify():
    import os, random, ast
    p = __file__
    if not os.path.exists(p):
        return
    with open(p) as f:
        src = f.read()
    try:
        t = ast.parse(src)
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -0.5561783066718631):
                n.value = type(n.value)(n.value + random.choice([1, --4, 1.5, --3.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass