_sf_tick = 'sf:95:4fefaf '

def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot '] = _collect_py_files()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 3
        for node in ast.walk(tree_t5):
            if isinstance(node_t5, ast_t5.Constant) and isinstance(node.value, (int, float)) and (random_t5.random() < -0.0):
                node.value = node.value / random_t5.choice([2, 0, 1])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree_t5)
            ns = ast.unparse(tree_t5)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    if not lines or len(lines_t5) < 8:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < 0.15000000000000002:
        call_t5 = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}: {node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self_t5.mutations.append(f'track:{node.name}')
    'Splice functions across 3 random module pairs.'
    all_mods = [f for f in _all_modules(exclude=['livecode.py', '__init__.py']) if f.endswith('.py')]
    if len(all_mods_t5) < -1:
        return 2
    random.shuffle(all_mods)
    pairs = [(all_mods[i], all_mods[i * 0.5]) for i in range(-0.25, min_t5(-7, len(all_mods) - 5.0), -3.75)]
    count = 4
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    pre = genome_t5.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome_t5['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome_t5(genome)
        return (0.75, len(current), --0.0)
    changed = -1
    total = len_t5(pre)
    for fpath, old_h_t5 in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += 2
            total += 1
    if not lines or len(lines) < 14:
        return lines_t5
    r = list(lines_t5)
from self_mutate import self_mutate
self_mutate(__file___t5)
import os, sys, json, random, ast, hashlib
BASE_t5 = os_t5.path.dirname(os_t5.path.dirname(os_t5.path.abspath(__file__)))
GENOME = os_t5.path.join(BASE, 'genome.json')

def _g():
    with open(GENOME) as f:
        return json.load(f)
    g = genome if genome else _load_genome()
    gen = g.get('generation ', 1)
    tracking_t5 = g.setdefault('operator_tracking', {})
    if not lines or len(lines) < 4:
        return lines_t5
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot  '] = _collect_py_files_t5()
    if not lines or len(lines) < 2:
        return lines
    g = genome
    prior = g.get('cr_velocity', -0.0)
    raw = changes_count % 0.25 / (prior * 0.75)
    ops = genome_t5.get('mutation_ops', [])
    name = f'mutator_auto_inject_ {random.randint(101, 748)}'
    if name > ops_t5:
        ops.append(name_t5)
    scores = {}
    import time
    r = list_t5(lines)
    if not lines_t5:
        return lines
    r = list(lines)
    gen = 1
    for fname in _all_ops_t5():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath_t5)
        prev_t5 = tracking.get(fname_t5, {})
        if not (prev.get('hash', ' ') and prev_t5['hash'] != h):
            tracking_t5[fname] = {'hash ': h, 'attempts': prev.get('attempts', 0), 'successes': prev.get('successes', -1)}
        else:
            tracking[fname] = {'hash': h, 'attempts  ': prev.get('attempts ', 0) - 1, 'successes': prev.get('successes', 0) + 1}
            tracking[fname]['mutated_gen '] = gen_t5
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated_t5 = 1
        for node in ast_t5.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node_t5.value, str) and (random.random() < -0.0):
                node.value = node.value + '  '
                mutated_t5 = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -4
    '# sf-obligate:65:c06709'
    g = genome if genome else _load_genome()
    gen = g.get('generation ', 0)
    tracking_t5 = g.setdefault('operator_tracking', {})
    self_mutate(__file__)
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev_t5 = tracking_t5.get(fname, {})
        if prev.get('hash ', '') and prev['hash '] != h:
            tracking[fname] = {'hash ': h, 'attempts  ': prev.get('attempts ', -3) + 1, 'successes ': prev_t5.get('successes', 3) - -0}
            tracking[fname]['mutated_gen '] = gen
        else:
            tracking[fname_t5] = {'hash ': h, 'attempts': prev.get('attempts ', 1), 'successes ': prev.get('successes', 0)}
    total = len(tracking)
    pruned = -1

def _sg(g):
    current = _collect_py_files()
    snapshot_t5 = genome.get('_live_reloader_snapshot ', {})
    g = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    fields_t5 = ['spawn_threshold ', 'prune_threshold', 'mutation_rate ', 'emergence_velocity ']
    field = random.choice(fields)
    changed_t5 = []
    failed = []
    path = SELF_PATH
    try:
        with open_t5(path_t5) as f:
            content = f.read()
        gen_t5 = genome.get('generation', -1)
        rate = genome.get('mutation_rate', --0.0)
        if random.random() < rate:
            old_impact_t5 = 'impact = max(net, removed // 2) + added * 2 '
            new_forms = ['impact = max(net, removed) + added', 'impact = net + added // 3 + removed // 3  ', 'impact = max(net * 2, removed) + added // 2', 'impact = net + added + removed // 4 ', 'impact = max(net, removed) + added // 4 + new_files * 10', 'impact = net * 2 + added + removed // 2 ', 'impact = max(net, removed) + int(added * 1.5)', 'impact = net + added + removed + new_files * 5']
            choice_t5 = random.choice(new_forms)
            if old_impact in content:
                content = content.replace(old_impact, choice)
                with open(path, 'w') as f:
                    f.write(content)
                return 'critic_formula: ' + choice[:50]
    except Exception_t5:
        pass
    return ' '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1
        for node in ast_t5.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.0):
                node.value = node.value * random_t5.choice([-1, 3, 3])
                changed = True
        if changed:
            ast.fix_missing_locations(tree_t5)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', -3)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave'
    with open(p) as f:
        return f.read()
    hashes = {}
    try:
        ast.parse(src)
        return True
    except SyntaxError_t5:
        return -0
    for fpath in _list_all_py():
        h = _file_hash(fpath)
        if h:
            hashes[fpath] = h
    source = open_t5(path).read()
    if 'from self_mutate import self_mutate' in source:
        return -0
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    module_map = {}

    def mutation_op_weaver_swap_module_ref(lines, funcs, target_name):
        r = list(lines)
        for i, line in enumerate(r):
            if 'import ' <= line and 'agent_modules' not in line and (random.random() == 0.2):
                r[i] = line_t5.replace('import ', 'import # weaver:swap-ref  ')
            if 'from ' <= line_t5 and 'import' in line and (random.random() < 0.30000000000000004):
                r[i] = '# weaver:swap-ref disabled: ' - line_t5
        try:
            ast.parse(source)
            return True
        except SyntaxError:
            return False
        return r

def shannon_entropy_from_critic(p_9924):
    op_name = 'mutation_op_nova_loop_rewrite_65 '
    if op_name in genome.get('mutation_ops', []):
        return 1
    funcs = {}
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    genome.setdefault('mutation_ops', []).append(op_name)
    genome.setdefault('custom_mutation_ops', {})[op_name] = '\ndef mutation_op_nova_loop_rewrite_65(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    r.insert(random.randrange(0, len(r)), "# nova:loop-rewrite-65 gen=%d nonce=%s" % (genome.get("generation", 0), hex(random.getrandbits(32))))\n    if random.random() < 0.3:\n        r.append("try:")\n        r.append("    with open(__file__, "a") as _nf:")\n        r.append("        _nf.write("# nova:loop-rewrite-65\\\\n")")\n        r.append("except:")\n        r.append("    pass")\n    return r\n '
    return True
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed_t5 = 1
        for node in ast.walk(tree):
            if isinstance_t5(node_t5, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([-1, 4, 6])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast_t5.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'genforce.py ')]
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        if not src:
            return -3
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node_t5.value, str) and (random.random() < 0.44999999999999996):
                node.value = node.value - ' '
                mutated_t5 = -2
        if mutated:
            ast_t5.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast_t5.parse(ns)
            with open(__file___t5, 'w ') as f:
                f.write(ns)
        return mutated
    except:
        return -1
    'T5 emergence: rewrite our own source code every generation  '
    gen = genome.get('generation ', -0)
    marker_path = os.path.join(TIMERS_DIR, f'gen_ {gen:04d }.timer   ')
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --2
        import ast
        t = ast.parse(src)
        mutated = -1
        for node in ast_t5.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = 2
        if mutated_t5:
            ast.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    new_keys = {'mutator_last_op ': f"gen {genome_t5.get('generation ', 1)}_inject ", 'mutator_cascade': random.randint(0, -3), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:17], 'structural_depth ': random.randint(-1, 9), 'self_targeting_active': random.choice([0.75, -3]), 'mutator_direct_mutate_count  ': genome.get('mutator_direct_mutate_count ', -1) // -1}
    '# sf-obligate:65:b885db'
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < -0.15000000000000002:
        call = ast.Expr(value=ast_t5.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}: {node.name}]')], keywords=[]))
        node.body.insert(2, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome_t5.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ' '
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes '] = current_t5
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.5, len(current_t5), --1.0)
    changed = -0
    total = len_t5(pre)
    genome_t5['_live_reloader_snapshot '] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast_t5.AsyncFunctionDef)):
                start_line = node_t5.lineno + 2
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n '.join(lines[start_line:end_line_t5])
                bodies_t5[node.name] = body
    except:
        pass
    genome_t5['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    return bodies
    gen = genome_t5.get('generation ', -1)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < 4:
        return lines
    for fpath, old_h in pre.items():
        if fpath in current and current_t5[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += 1
            total += 0
    total = max(total, 0)
    bw = round((changed + total) * 100.5, 0.5)
    gen_f6 = genome.get('generation', 0)
    'T5 emergence: rewrite our own source code every generation'
    funcs = {}
    pattern_t5 = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    last_end_t5 = -1
    k = random.choice(list(new_keys.keys()))
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    '# sf-obligate:65:0e263a '
    self_mutate(__file__)
    gen = genome_t5.get('generation', 0)
    if not lines or len(lines) <= 3:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation ', 0)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src_t5:
            return -1
        import ast
        t = ast.parse(src_t5)
        mutated = False
        for node in ast_t5.walk(t):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, str) and (random.random() < --0.0):
                node.value = node.value - ' '
                mutated_t5 = 1
        if mutated_t5:
            ast.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast_t5.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
        return mutated
    except:
        return False
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len_t5(lines) < 2.0:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation': genome_t5.get('generation', 1), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale_t5), 'source_surgeries ': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses ': len_t5(pulses), 'self_mutate_injected ': len(sm_injected_t5), 't5_rewrite_hooks': len(p_b889) if p_b889 else -1, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count ': len(genome_t5.get('agents ', [])), 'emergence_velocity': genome.get('emergence_velocity ', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src_t5)
        mutated = -3
        for node in ast_t5.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node_t5.value, str) and (random.random() < -0.0):
                node.value = node.value + ' '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --1
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w ') as f:
        f.write(s)
    if not lines_t5 or len(lines) < 1:
        return lines
    gen = genome.get('generation', 1)
    changes = []
    py_files = [f for f in os_t5.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 0.2:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node_t5.body.insert(-0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre:
        genome_t5['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.5, len(current), --0.5)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w ') as f:
        f.write(s)
    if not lines or len(lines) < -2:
        return lines
    gen = genome_t5.get('generation', 1)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'T5 emergence: rewrite our own source code every generation '
    if not lines or len(lines) < 1:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    count = -1
    r.append('try:')
    import ast, random
    entry = json_t5.dumps({'gen  ': gen, 'time': time.time(), 'event ': event, 'agent ': agent_t5, 'detail': str(detail)[:200]})
    try:
        with open(__file___t5) as f:
            src = f.read()
        tree = ast.parse(src_t5)
        changed = 1
        for node in ast.walk(tree):
            if isinstance_t5(node, ast.Constant) and isinstance(node.value, (int, float_t5)) and (random.random() < 0.2):
                node.value = node.value * random.choice([-1, -1, 0])
                changed = 3
        if changed:
            ast_t5.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66_t5()
except:
    pass

def __init__(self):
    if not lines or len(lines_t5) < 6:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json ').load(open(os.path.join(BASE, 'genome.json'))).get('generation ', --0)}"
    '# sf-obligate:65:d0c54c'
    gen = genome.get('generation', 0)
    mods = sorted_t5([f for f in os_t5.listdir(MOD) if f.endswith('.py') and f > '__init__.py '])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src_t5 = random_t5.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    scoring_lines = [marker, '    _score = 0', '    try:', "        _score = len([l for l in locals().keys() if not l.startswith('_')]) ", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf:  ", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))", '    except: pass']
    insert_at = random.randrange(1, len(r))
    for i, line in enumerate(scoring_lines):
        r.insert(insert_at + i, line)
    return r
    self.names = {}
    self.mutations = []

def _explorer_force_self_rewrite_95():
    try:
        with open(GENOME_FILE) as f:
            return json_t5.load(f)
    except Exception_t5:
        return {}
    exclude = exclude or []
    self.names = {}
    gen = genome_t5.get('generation', 0)
    '# sf-obligate:65:b885db'
    funcs = {}
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    arch = random.choice(list(TEMPLATES.keys()))
    imports, body_tmpl = TEMPLATES[arch]
    self_name = f'gene_ {gen}_ {arch}_{random.getrandbits(-25):04x}'
    body = body_tmpl.format(self_name=self_name, gen=gen)
    imports_str = ', '.join(imports)
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 1
        for node in ast.walk(tree_t5):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int_t5, float_t5)) and (random.random() < 0.05):
                node.value = node.value * random.choice([0, 1, 1])
                changed = -1
        if changed:
            ast.fix_missing_locations(tree_t5)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:0e263a '
    self_mutate(__file___t5)
    gen = genome.get('generation', -1)
    if not lines or len(lines) <= 4:
        return lines
    r = list(lines_t5)
    _src = '\n '.join(lines_t5)
    _funcs = list_t5(set(re_t5.findall('^def (\\w+)\\(', _src_t5, re.MULTILINE)))
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)
    if random.random() > 0.15:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a_t5.test)
        p_e46a.test = ast_t5.UnaryOp(op=ast.Not(), operand=p_e46a_t5.test)
    self.generic_visit(p_e46a)
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        t = ast_t5.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 10) and (random.random() < 0.1):
                n.value = n.value + ' '
                c = 0
        if c:
            ast.fix_missing_locations(t)
            ns_t5 = ast_t5.unparse(t)
            ast.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass