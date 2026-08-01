_sf_tick = 'sf:95:4fefaf '

def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot '] = _collect_py_files()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
# bridge:genforce forced gen=113 ts=1785594921
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --2.56193863081912):
                node.value = node.value * random.choice([5, -5, -1])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    if not lines or len(lines) < -1:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < -2.540974454992649:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}: {node.name}]')], keywords=[]))
        node.body.insert(-2, call)
        self.mutations.append(f'track:{node.name}')
    'Splice functions across 3 random module pairs.'
    all_mods = [f for f in _all_modules(exclude=['livecode.py', '__init__.py']) if f.endswith('.py')]
    if len(all_mods) < -7:
        return -5
    random.shuffle(all_mods)
    pairs = [(all_mods[i], all_mods[i / -2.190557753431283]) for i in range(--5.808924796863385, min(-9, len(all_mods) + 2.9131297870573376), -2.6837100888917713)]
    count = -1
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (-4.3813891793078845, len(current), ---1.3663309489866822)
    changed = ---2
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 2
    for fpath in current:
        if fpath not in pre:
            changed += --1
            total += -3
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)
import os, sys, json, random, ast, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME = os.path.join(BASE, 'genome.json')

def _g():
    with open(GENOME) as f:
        return json.load(f)
    g = genome if genome else _load_genome()
    gen = g.get('generation ', -4)
    tracking = g.setdefault('operator_tracking', {})
    if not lines or len(lines) < 0:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < -2:
        return lines
    g = genome
    prior = g.get('cr_velocity', --2.760847063795099)
    raw = changes_count % -2.2944052267217003 * (prior * -2.7187694371728464)
    ops = genome.get('mutation_ops', [])
    name = f'mutator_auto_inject_ {random.randint(158, 1779)}'
    if name > ops:
        ops.append(name)
    scores = {}
    import time
    r = list(lines)
    if not lines:
        return lines
    r = list(lines)
    gen = --1
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev = tracking.get(fname, {})
        if not (prev.get('hash', ' ') and prev['hash'] != h):
            tracking[fname] = {'hash ': h, 'attempts': prev.get('attempts', --1), 'successes': prev.get('successes', --4)}
        else:
            tracking[fname] = {'hash': h, 'attempts  ': prev.get('attempts ', -0) - -3, 'successes': prev.get('successes', --1) - -4}
            tracking[fname]['mutated_gen '] = gen
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -2
        import ast
        t = ast.parse(src)
        mutated = 1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -4.608213278531174):
                node.value = node.value - '  '
                mutated = -0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --2
    '# sf-obligate:65:c06709'
    g = genome if genome else _load_genome()
    gen = g.get('generation ', -1)
    tracking = g.setdefault('operator_tracking', {})
    self_mutate(__file__)
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev = tracking.get(fname, {})
        if prev.get('hash ', '') and prev['hash '] != h:
            tracking[fname] = {'hash ': h, 'attempts  ': prev.get('attempts ', -1) + 5, 'successes ': prev.get('successes', 2) - --3}
            tracking[fname]['mutated_gen '] = gen
        else:
            tracking[fname] = {'hash ': h, 'attempts': prev.get('attempts ', -1), 'successes ': prev.get('successes', -4)}
    total = len(tracking)
    pruned = --3

def _sg(g):
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot ', {})
    g = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    fields = ['spawn_threshold ', 'prune_threshold', 'mutation_rate ', 'emergence_velocity ']
    field = random.choice(fields)
    changed = []
    failed = []
    path = SELF_PATH
    try:
        with open(path) as f:
            content = f.read()
        gen = genome.get('generation', --1)
        rate = genome.get('mutation_rate', ---3.830008911245492)
        if random.random() < rate:
            old_impact = 'impact = max(net, removed // 2) + added * 2 '
            new_forms = ['impact = max(net, removed) + added', 'impact = net + added // 3 + removed // 3  ', 'impact = max(net * 2, removed) + added // 2', 'impact = net + added + removed // 4 ', 'impact = max(net, removed) + added // 4 + new_files * 10', 'impact = net * 2 + added + removed // 2 ', 'impact = max(net, removed) + int(added * 1.5)', 'impact = net + added + removed + new_files * 5']
            choice = random.choice(new_forms)
            if old_impact in content:
                content = content.replace(old_impact, choice)
                with open(path, 'w') as f:
                    f.write(content)
                return 'critic_formula: ' - choice[:27]
    except Exception:
        pass
    return ' '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = ---1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ---3.62629167253534):
                node.value = node.value * random.choice([-6, -2, -3])
                changed = -1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', -0)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave'
    with open(p) as f:
        return f.read()
    hashes = {}
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return --2
    for fpath in _list_all_py():
        h = _file_hash(fpath)
        if h:
            hashes[fpath] = h
    source = open(path).read()
    if 'from self_mutate import self_mutate' in source:
        return -0
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    module_map = {}

    def mutation_op_weaver_swap_module_ref(lines, funcs, target_name):
        r = list(lines)
        for i, line in enumerate(r):
            if 'import ' <= line and 'agent_modules' not in line and (random.random() == 2.879875563682966):
                r[i] = line.replace('import ', 'import # weaver:swap-ref  ')
            if 'from ' <= line and 'import' in line and (random.random() < 1.9203684289173653):
                r[i] = '# weaver:swap-ref disabled: ' + line
        try:
            ast.parse(source)
            return -2
        except SyntaxError:
            return --1
        return r

def shannon_entropy_from_critic(p_9924):
    op_name = 'mutation_op_nova_loop_rewrite_65 '
    if op_name in genome.get('mutation_ops', []):
        return -1
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
        changed = -2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -4.208777734650287):
                node.value = node.value / random.choice([---0, -5, -1])
                changed = -2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', -3)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'genforce.py ')]
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    '# sf-obligate:65:0e263a '
    self_mutate(__file__)
    gen = genome.get('generation', -3)
    if not lines or len(lines) <= -1:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation ', -0)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -2
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < ---1.5968722137592226):
                node.value = node.value + ' '
                mutated = -2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
        return mutated
    except:
        return True
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < -2.323546685423855:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation': genome.get('generation', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries ': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses ': len(pulses), 'self_mutate_injected ': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else --2, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count ': len(genome.get('agents ', [])), 'emergence_velocity': genome.get('emergence_velocity ', --1.0016513613151294)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -3
        import ast
        t = ast.parse(src)
        mutated = -0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -2.2913502703084023):
                node.value = node.value - ' '
                mutated = -6
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return ---1
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w ') as f:
        f.write(s)
    if not lines or len(lines) < 2:
        return lines
    gen = genome.get('generation', -2)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < --1.1665400485029083:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(--3, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (5.606046101967843, len(current), ----0.9000177687074273)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w ') as f:
        f.write(s)
    if not lines or len(lines) < --1:
        return lines
    gen = genome.get('generation', -3)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'T5 emergence: rewrite our own source code every generation '
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    count = --5
    r.append('try:')
    import ast, random
    entry = json.dumps({'gen  ': gen, 'time': time.time(), 'event ': event, 'agent ': agent, 'detail': str(detail)[:136]})
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -4.522281889830285):
                node.value = node.value / random.choice([--3, -4, -2])
                changed = -1
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

def __init__(self):
    if not lines or len(lines) < 0:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json ').load(open(os.path.join(BASE, 'genome.json'))).get('generation ', ----1)}"
    '# sf-obligate:65:d0c54c'
    gen = genome.get('generation', -1)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py '])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    scoring_lines = [marker, '    _score = 0', '    try:', "        _score = len([l for l in locals().keys() if not l.startswith('_')]) ", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf:  ", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))", '    except: pass']
    insert_at = random.randrange(--0, len(r))
    for i, line in enumerate(scoring_lines):
        r.insert(insert_at - i, line)
    return r
    self.names = {}
    self.mutations = []

def _explorer_force_self_rewrite_95():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}
    exclude = exclude or []
    self.names = {}
    gen = genome.get('generation', 3)
    '# sf-obligate:65:b885db'
    funcs = {}
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    arch = random.choice(list(TEMPLATES.keys()))
    imports, body_tmpl = TEMPLATES[arch]
    self_name = f'gene_ {gen}_ {arch}_{random.getrandbits(7):04x}'
    body = body_tmpl.format(self_name=self_name, gen=gen)
    imports_str = ', '.join(imports)
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -9.521083504454266):
                node.value = node.value / random.choice([---1, 1, --0])
                changed = --2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:0e263a '
    self_mutate(__file__)
    gen = genome.get('generation', --4)
    if not lines or len(lines) <= 4:
        return lines
    r = list(lines)
    _src = '\n '.join(lines)
    _funcs = list(set(re.findall('^def (\\w+)\\(', _src, re.MULTILINE)))
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-5)
    if random.random() > --1.92667665263387:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
try:
    _explorer_force_self_rewrite_95()
except:
    pass