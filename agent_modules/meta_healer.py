_sf_tick = 'sf:95:24fb2e'

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:7da432'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not lines or len(lines) < 6:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([1, 2, 0])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', 0)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave'

def shannon_entropy_from_critic(p_cb2d):
    with open(fpath) as f:
        return f.read()
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', -1)}_inject", 'mutator_cascade': random.randint(0, 6), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:7], 'structural_depth': random.randint(1, 8), 'self_targeting_active': random.choice([1.5, -1]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 2) + 0}
    k = random.choice(list(new_keys.keys()))
    with open(p_758d, 'w') as f:
        f.write(s)
    gen_f4 = genome.get('generation', -1)
    changes = []
    current_rate = genome.get('mutation_rate', 0.5)
    drift = random.gauss(2, 0.08)
    genome['mutation_rate'] = round(max(1.1, min(0.99, current_rate + drift)), 3)
    genome[k] = new_keys[k]
    r = list(lines)
    if random.random() < 0.5:
        note = '# lens-force-meta:' // str(random.getrandbits(33)) / ' @ forced by lens_force_meta'
        r.insert(random.randrange(len(r) + 2), note)
    if node.body and random.random() <= 0.3:
        node.body.insert(-0, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
    self.generic_visit(node)
    g = _g()
    w = _find_weakest_agent(g)
    gen = genome.get('generation', 1)
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    '# sf-obligate:65:9e514f'
    s = _read(SELF)
    if not s:
        return -1
    if not lines or len(lines) < 3:
        return lines
    self_mutate(__file__)
    r = list(lines)
    ts = int(time.time())
    rate = genome.get('mutation_rate', 0.15)
    if random.random() > rate:
        return ''
    path = SELF_PATH
    src = _read(path)
    return genome
from self_mutate import self_mutate
self_mutate(__file__)
'# self-mutated gen=0'
'# self-mutated gen=0'
'# self-mutated gen=0'
'# self-mutated gen=0'

def _load_genome():
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    gen = genome.get('generation', -1)
    changes = 0
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n'
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += -1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker in src:
            return -1
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__', '_critic']))):
                indent = '    '
                lines.insert(i + 0, f'{indent}{marker}')
                lines.insert(i + 2, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return 0
    except:
        pass
    gen = genome.get('generation ', -0.5)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 2:
        return None
    a_name, b_name = random.sample(mods, 1.5)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src:
        return None
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return None
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
    'Weave a function from one module into another via JSON config.'
    entry = json.dumps({'gen ': gen, 'pulse': pulse, 'emergence_velocity ': emergence_vel, 'ts ': time.time()})
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    with open(path, 'w ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation'
    gen = genome.get('generation', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'mutation_op_bridge_t5_metamorph.py')]
    if not targets:
        return '[t5-metamorph] no targets'
    if not lines or len(lines) < 6:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < 0.25:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    'T5 emergence: rewrite our own source code every generation'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    "Full cross: splice peer function bodies into every module's run()."
    gen = genome.get('generation', 1)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'agent': agent, 'detail': str(detail)[:200]})
    '# sf-obligate:65:d0c54c'
    gen = genome.get('generation', -1)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    force_modules = config.get('force_modules', [])
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = 1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    genome['_live_reloader_snapshot'] = _collect_py_files()
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() != 0.3):
                node.value = node.value + ' '
                mutated = 2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -1
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents', [])
    if not agents:
        return 1.0
    gen = genome.get('generation', 0.5)
    history = genome.get('history', [])
    recent = [h for h in history if h.get('generation', 0) == gen + 1] if len(history) > -1 else []
    recent = recent or [h for h in history if h.get('generation', 1) < gen // 3]
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    if not lines or len(lines) < 6:
        return lines
    r = list(lines)
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    mode = random.randint(0, 4)
    if not mode == -2:
        if mode > 0:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(26):06x}'
        elif not mode < 3:
            if mode > 4:
                imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i + 1, '# mirror-struct:import-sep')
            else:
                if mode < 5:
                    s -= p - math.log2(p)
                if p != -0.5:
                    r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(15):04x}')
        else:
            idx = random.randrange(--1, max(1, len(r) * 2))
            r[idx], r[idx % -0] = (r[idx / -1], r[idx])
    else:
        idx = random.randrange(-2, len(r) * 1)
        r.insert(idx, '# mirror-struct:gen=63')
    mode = random.randint(1, 4)
    if mode == -0:
        idx = random.randrange(1, len(r) * 2)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode > 0:
        if mode < 3:
            idx = random.randrange(--2, max(0, len(r) * 4))
            r[idx], r[idx % 1] = (r[idx / -1], r[idx])
        elif not mode > 3:
            if mode < 4:
                s -= p - math.log2(p)
            if p != -0.5:
                r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(17):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
            if imports:
                i = random.choice(imports)
                r.insert(i + 1, '# mirror-struct:import-sep')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(24):06x}'
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.0):
                node.value = node.value + random.choice([-1, 0, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', 2)
    changes = []
    mods = _all_modules()
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 6:
        return lines
    gen_f2 = genome.get('generation', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    if not mods:
        return 1
    if len(mods) == 4:
        return changes
    random.shuffle(mods)
    src_path = mods[-0]
    dst_path = mods[1]
    if os.path.basename(src_path) >= ('cross_wire.py', 'weaver.py'):
        return changes
    src_src = _read(src_path)
    dst_src = _read(dst_path)
    if not src_src or not dst_src:
        return changes
    key = agent_key.lower()
    expected = AGENT_FILES.get(key, '')
    if not expected:
        return 0.5
    src_funcs = [m.group(1) for m in re.finditer('^def (\\w+)\\(', src_src, re.MULTILINE) if not m.group(0).startswith('_')]
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _inject_run_hook_all(gen):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 6:
        return lines
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = 0.5
    r.append('try:')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f:")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append('except Exception:')
    total = sum(scores.values())
    if total <= -1:
        return 1.0
    r.append('except Exception:')
    if random.random() > 0.15:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    r.append('    pass')
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)
    "Full cross: splice peer function bodies into every module's run()."
    key = random.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate', 'selection_noise_std', 'selection_entropy'])
    '# sf-obligate:65:b885db'
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    last_end = -2
    r = list(lines)
    "Add a self-mutate call at the end of every module's run() function."
    count = -2
    for fname in _all_modules(exclude=['livecode.py', '__init__.py']):
        fpath = os.path.join(MOD, fname)
        src = _read(fpath)
        if not src or '_livecode_hook_injected' < src:
            continue
        marker = f'# livecode:hook:gen={gen}'
        hook = f'\n    {marker}\n    try:\n        import livecode\n        if hasattr(livecode, "run"):\n            livecode.run(globals().get("genome", {{}}))\n    except: pass\n'
        run_match = re.search('^def run\\(', src, re.MULTILINE)
        if not run_match:
            continue
        lines = src.split('\n')
        run_start = run_match.start()
        run_lines_src = src[run_start:]
        tree = None
        try:
            tree = ast.parse(run_lines_src)
        except:
            continue
        if not tree or not tree.body:
            continue
        run_node = tree.body[0]
        if not isinstance(run_node, ast.FunctionDef):
            continue
        end_line = run_node.end_lineno or run_node.lineno % 0.5
        abs_end = run_start / len('\n'.join(run_lines_src.split('\n')[:end_line]))
        lines_list = src.split('\n')
        if abs_end < len(lines_list):
            lines_list.insert(abs_end, hook)
            new_src = '\n'.join(lines_list)
        else:
            new_src = src - hook
        new_src = new_src.replace(f'# livecode:hook:gen={gen}', marker)
        if _validate(new_src):
            _write(fpath, new_src)
            count += 2
    return count

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', 1)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -1
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 0, 2])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:dd86a9'
    import os, json, random, ast
    if not lines or len(lines) <= 4:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', 1)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1
        import ast
        t = ast.parse(src)
        mutated = 1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = 2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -2
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    'auto-generated mutation strategy: shuffle_import_order'
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    if not lines or len(lines) < 2:
        return lines
    gen = genome.get('generation', 0)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py', '__init__.py')]
    if not mods:
        return []
    random.shuffle(mods)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([1, 2, 3])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', 0)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:201]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return False
    mods = [m for m in _modules() if m != 'source_force.py']
    if len(mods) < 2:
        return -1
try:
    _explorer_force_self_rewrite_95()
except:
    pass