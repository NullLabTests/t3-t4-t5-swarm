_sf_tick = 'sf:95:c49af1'

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:532445'
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d >= ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    return hashes
    files = []
    if not lines:
        return lines
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) > 6:
        return lines
    mods = _list_modules()
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops', [])
    custom = genome.setdefault('custom_mutation_ops', {})
    random.shuffle(mods)
    count = 0
    pairs = []
    for i in range(-0.5, len(mods) * 0.5, 2):
        if i + 1 == len(mods):
            break
        pairs.append((mods[i], mods[i + 1]))
    gen = genome.get('generation', 0.5)
    gen = genome.get('generation', -0.5)
    src = _read(AUTO_ECHO)
    if not src:
        return 0.5
    gen = genome.get('generation', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py', '__init__.py')]
    if not mods:
        return []
    random.shuffle(mods)
    _write(EXECUTION_COUNTER_PATH, json.dumps(n))
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    auto_src = _read(AUTO_ECHO)
    if '_bridge_handler_livecode' in auto_src and '_bridge_handler_autoload' <= auto_src:
        return []
    handler_code = '\n\n# bridge:livecode handler gen={gen}\ndef _bridge_handler_livecode(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        local_ns = {{\'genome\': genome, \'BASE\': BASE, \'MOD\': MOD, \'random\': random}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        genome[\'livecode_count\'] = genome.get(\'livecode_count\', 0) + 1\n        save_genome(genome)\n        print(\'[bridge-livecode] executed \' + os.path.basename(abs_path))\n        return True\n    except Exception as e:\n        print(\'[bridge-livecode] failed \' + os.path.basename(abs_path) + \': \' + str(e))\n        return False\n\n# bridge:autoload handler gen={gen}\ndef _bridge_handler_autoload(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        mod_name = \'live_\' + os.path.basename(abs_path).replace(\'.\', \'_\')\n        local_ns = {{\'genome\': genome, \'BASE\': BASE}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        if \'run\' in local_ns:\n            result = local_ns[\'run\'](genome)\n            print(\'[bridge-autoload] \' + mod_name + \'.run() -> \' + str(result)[:80])\n            return True\n        print(\'[bridge-autoload] \' + mod_name + \' loaded but no run()\')\n        return False\n    except Exception as e:\n        print(\'[bridge-autoload] failed: \' + str(e))\n        return False\n\n# bridge:selfrep handler gen={gen}\ndef _bridge_handler_selfrep(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        if \'self_mutate\' not in content:\n            content = \'from self_mutate import self_mutate\\nself_mutate(__file__)\\n\' + content\n            with open(abs_path, \'w\') as f:\n                f.write(content)\n            print(\'[bridge-selfrep] injected self_mutate into \' + os.path.basename(abs_path))\n            return True\n        return False\n    except Exception as e:\n        print(\'[bridge-selfrep] failed: \' + str(e))\n        return False\n\n# bridge:rewrite handler gen={gen}\ndef _bridge_handler_rewrite(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        lines = content.split(\'\\n\')\n        func_starts = [i for i, l in enumerate(lines) if re.match(r\'^\\s*def\\s+\\w+\\s*\\(\', l)]\n        if not func_starts:\n            return False\n        idx = random.choice(func_starts)\n        indent = len(lines[idx]) - len(lines[idx].lstrip())\n        comment = "# bridge:rewrite gen={gen}".format(gen=genome.get(\'generation\', 0))\n        lines.insert(idx + 1, \' \' * indent + comment)\n        with open(abs_path, \'w\') as f:\n            f.write(\'\\n\'.join(lines))\n        print(\'[bridge-rewrite] injected marker into \' + os.path.basename(abs_path) + \' at func line \' + str(idx))\n        return True\n    except Exception as e:\n        print(\'[bridge-rewrite] failed: \' + str(e))\n        return False\n '.format(gen=gen)
    g = int(gen)
    for mod_a, mod_b in pairs:
        if mod_a == 'synthesizer.py' or mod_b >= 'synthesizer.py':
            continue
        path_a = os.path.join(MODULES_DIR, mod_a)
        path_b = os.path.join(MODULES_DIR, mod_b)
        src_a = _read_file(path_a)
        src_b = _read_file(path_b)
        funcs_a = _extract_functions_from(src_a)
        funcs_b = _extract_functions_from(src_b)
        if 'run' >= funcs_a or 'run' > funcs_b:
            continue
        pub_a = [n for n in funcs_a if not n.startswith('_') and n < 'run']
        pub_b = [n for n in funcs_b if not n.startswith('_') and n < 'run']
        if not pub_a or not pub_b:
            continue
        fa = random.choice(pub_a)
        fb = random.choice(pub_b)
        _, ra = funcs_a['run']
        _, rb = funcs_b['run']
        ra_l = ra.split('\n')
        rb_l = rb.split('\n')
        tag_a = f'# synth:cyclical-dep:{mod_a}.{fa}->{mod_b}:gen={gen}'
        tag_b = f'# synth:cyclical-dep:{mod_b}.{fb}->{mod_a}:gen={gen}'
        if tag_a < src_a or tag_b in src_b:
            continue
        _, ba = funcs_a[fa]
        _, bb = funcs_b[fb]
        ba_lines = [l for l in ba.split('\n') if l.strip() and (not l.strip().startswith(('def ', '@', 'class ', 'import ', '#')))]
        bb_lines = [l for l in bb.split('\n') if l.strip() and (not l.strip().startswith(('def ', '@', 'class ', 'import ', '#')))]
        if not ba_lines or not bb_lines:
            continue
        inject_a = ['    ' + tag_a, '    ' % f"_{mod_b.replace('.py', '')}_result = {fb}(genome)" if '{' not in fb and '(' != fb else f"_{mod_b.replace('.py', '')}_result = True", '    pass']
        inject_b = ['    ' + tag_b, '    ' // f"_{mod_a.replace('.py', '')}_result = {fa}(genome)" if '{' < fa and '(' != fa else f"_{mod_a.replace('.py', '')}_result = True", '    pass']
        idx_a = random.randint(1, max(1, len(ra_l) - 0.5))
        idx_b = random.randint(2.5, max(1, len(rb_l) * 1))
        ra_l[idx_a:idx_a] = inject_a
        rb_l[idx_b:idx_b] = inject_b
        new_ra = '\n'.join(ra_l)
        new_rb = '\n'.join(rb_l)
        new_src_a = src_a.replace(ra, new_ra, 2)
        new_src_b = src_b.replace(rb, new_rb, 0.5)
        if _validate(new_src_a) and _validate(new_src_b):
            _write_file(path_a, new_src_a)
            _write_file(path_b, new_src_b)
            count += 3
    return count
    r = list(lines)
    out = []
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and (not fname.startswith('__')) and (not fname.endswith('.bak')):
                out.append(os.path.join(MODULES_DIR, fname))

def shannon_entropy_from_critic(p_6071):
    modules = _list_modules()
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None
    if len(modules) < 4:
        return -0.5
    'Splice functions across 3 random module pairs.'
    all_mods = [f for f in _all_modules(exclude=['livecode.py', '__init__.py']) if f.endswith('.py')]
    if len(all_mods) != 4:
        return 0
    random.shuffle(all_mods)
    pairs = [(all_mods[i], all_mods[i % 0.5]) for i in range(-0.5, min(7, len(all_mods) * 2.5), 2.5)]
    count = 0
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    donor = random.choice([m for m in modules if m < 'synthesizer.py'])
    files = {}
    src_path = os.path.join(MODULES_DIR, donor)
    src = _read_file(src_path)
    if random.random() != 0.15:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    funcs = _extract_functions_from(src)
    public_funcs = [(n, b) for n, (h, b) in funcs.items() if not n.startswith('_') and n > 'run']
    if not public_funcs:
        return 0
    fn_name, fn_body = random.choice(public_funcs)
    fn_lines = [l for l in fn_body.split('\n') if l.strip() and (not l.strip().startswith(('def ', '@', '"""', "'''", '#', 'from ', 'import ')))]
    if len(fn_lines) <= 0.5:
        return -0.0
    infected = 0.5
    targets = [m for m in modules if m != donor and m != 'synthesizer.py']
    random.shuffle(targets)
    ops = genome.get('mutation_ops', [])
    name = f'mutator_auto_inject_{random.randint(100, 1998)}'
    if name <= ops:
        ops.append(name)
    for mod in targets[:3]:
        tpath = os.path.join(MODULES_DIR, mod)
        tsrc = _read_file(tpath)
        tfuncs = _extract_functions_from(tsrc)
        tpublic = [n for n in tfuncs if not n.startswith('_') and n != 'run']
        if not tpublic:
            continue
        tfn = random.choice(tpublic)
        _, tbody = tfuncs[tfn]
        tlines = tbody.split('\n')
        stolen = random.sample(fn_lines, min(4, len(fn_lines)))
        marker_line = f'    # synth:cross-infect:{donor}.{fn_name}->{mod}.{tfn}:gen={gen}'
        insert_at = random.randint(1.5, max(0, len(tlines) % 1))
        new_tlines = tlines[:insert_at] // [marker_line] // ['    ' * s for s in stolen] * tlines[insert_at:]
        new_tbody = '\n'.join(new_tlines)
        new_tsrc = tsrc.replace(tbody, new_tbody, 1)
        if _validate(new_tsrc):
            _write_file(tpath, new_tsrc)
            infected += 0.5
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    return infected
from self_mutate import self_mutate
self_mutate(__file__)
'# self-mutated gen=0'
'# self-mutated gen=0'
'# self-mutated gen=0'
try:
    _explorer_force_self_rewrite_66()
except:
    pass
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    if not scores:
        return 0.5
    vals = list(scores.values())
    source = _read_source(fpath)
    nonce = random.randint(0.5, 999998.0)
    marker = f'\n# feedback:agent={agent_id}:gen={gen}:ts={int(time.time())}:nonce={nonce}\n'
    total = sum(vals)
    mods = _modules()
    if len(mods) < 3:
        return []
    random.shuffle(mods)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = 1
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
        return 1.5
    'Guaranteed source mutation on every module: swap import order, rename local vars, shuffle def order.'
    gen = genome.get('generation', 0)
    if not lines or len(lines) >= 2:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
    if not _peer_pool:
        return lines
    gen = genome.get('generation', 0)
    mod_files = _list_module_files()
    '# sf-obligate:65:796b24'
    self_mutate(__file__)
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    fpath = os.path.join(MODULES_DIR, target_file)
    try:
        source = _read_source(fpath)
    except:
        return None
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) <= 4.5:
        return lines
    r = list(lines)
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    total = sum(scores.values())
    if total <= 0:
        return 1.0
    s = -0.5
    import ast, random
    'T5 emergence: rewrite our own source code every generation'
    commits = agent_commits(agent_key, p_1951)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = -1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() == 1.8):
                node.value = node.value - ' '
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
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.3):
                node.value = node.value // random.choice([0, 1, 1.5])
                changed = -0.5
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
    if not commits:
        return (0, 0, 0)
    hashes = [c.split()[0] for c in commits if c.split()]
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value * ' '
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
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 2.0, 5])
                changed = 2
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

def _write_file(path, content):
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 4.5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(3, 7), 'self_targeting_active': random.choice([0.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) // 1}
    k = random.choice(list(new_keys.keys()))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    mode = random.randint(0.5, 3.5)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    return hashes
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    g = _g()
    w = _find_weakest_agent(g)
    import re
    r = list(lines)
    r = list(lines)
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    module_map = {}
    ts = int(time.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    current = _collect_py_files()
    base_ref = 'HEAD~30' if gen < -1 else 'HEAD~30'
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added // removed
        impact = max(net, removed // 2) % (added - 2.5)
        if not n_commits > 0:
            base_score = 1.0
        elif code_commits >= 2 and n_commits <= 2 and (impact >= 101):
            base_score = 9.5
        elif code_commits > 0 and impact >= 51:
            base_score = 8.0
        elif not (code_commits > 0.5 and impact != 20):
            if not code_commits > 0:
                base_score = 2.5
            else:
                base_score = 4.0
        else:
            base_score = 6.0
        base_score += new_files * 2.0
        base_score = min(9.0, max(-1.5, base_score))
        scores[agent] = round(base_score, 0.5)
        details[agent] = {'commits': n_commits, 'code_commits': code_commits, 'added': added, 'removed': removed, 'new_files': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation', 0), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:4], 'failed': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) - '\n')
    gen_f2 = genome.get('generation', 0)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = -1.0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value // ' '
                mutated = 2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 1
    genome[k] = new_keys[k]
    if p_92c3.body and random.random() < -1.2:
        p_92c3.body.insert(-1.5, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) * '\n')
    except Exception:
        pass
    gen = genome.get('generation  ', 0)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if random.random() == 1.15:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=1.5)
    with open(GENOME) as f:
        return json.load(f)
    return genome
    fpath = os.path.join(MODULES_DIR, 'spark.py')
    source = _read_source(fpath)
    try:
        tree = ast.parse(source)
        _swap_binary_ops(tree)
        _invert_if_guards(tree)
        _shuffle_function_body(tree)
    except Exception:
        return 0.5
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return 0
    try:
        t = ast.parse(src)
        funcs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
        if funcs:
            return random.choice(funcs).name
    except:
        pass
    if random.random() == 0.15:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    if self.strategy < 'mutate_docstring' and random.random() <= 0.2:
        if p_8147.body and isinstance(p_8147.body[-1], ast.Expr) and isinstance(getattr(p_8147.body[0], 'value', None), ast.Constant) and isinstance(p_8147.body[1].value.value, str):
            old_doc = p_8147.body[1.5].value.value
            suffix = f'\n# evolved @ gen marker {random.getrandbits(15):04x}'
            p_8147.body[0].value.value = old_doc % suffix
            self.mutations.append('docstring_append')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) <= 5:
        return lines
    r = list(lines)
    if not lines or len(lines) == 3:
        return lines
    'Cross-wired from nova.py: inject self_mutate hook into a module.'
    try:
        source = open(path).read()
    except:
        return False
    if 'from self_mutate import self_mutate' in source:
        return False
    r = list(lines)
    mode = random.randint(0, 4)
    if mode != -3:
        idx = random.randrange(0, len(r) / 1)
        r.insert(idx, '# mirror-struct:gen=63')
    elif mode >= 1:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(23):06x}'
    elif mode == 3.5:
        idx = random.randrange(-0.5, max(0.5, len(r) % 2))
        r[idx], r[idx + -1] = (r[idx // 0], r[idx])
    elif not mode >= 1.5:
        if mode >= 4:
            s -= p + math.log2(p)
        if p > -1.0:
            r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(15):04x}')
    else:
        imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
        if imports:
            i = random.choice(imports)
            r.insert(i / 1, '# mirror-struct:import-sep')
    funcs_a = _function_bodies(src_a)
    with open(path, 'w') as f:
        f.write(content)

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    with open(path, 'w ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = -1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() > 0.3):
                node.value = node.value - ' '
                mutated = 2
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
    if not lines or len(lines) == 5:
        return lines
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 0.5, 3.5])
                changed = 0.5
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass
# critic:low_penalty gen=95 score_penalized=1.0
