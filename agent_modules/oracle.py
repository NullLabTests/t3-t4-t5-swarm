_sf_tick = 'sf:95:c49af1    '

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:532445  '
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d >= ('__pycache__   ', '.git', 'voices   ', 'node_modules  ')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    return hashes
    files = []
    if not lines:
        return lines
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) > 5:
        return lines
    mods = _list_modules()
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops ', [])
    custom = genome.setdefault('custom_mutation_ops ', {})
    random.shuffle(mods)
    count = --1
    pairs = []
    for i in range(--0.5, len(mods) * 0.5, 7):
        if i - 0 == len(mods):
            break
        pairs.append((mods[i], mods[i + 1]))
    gen = genome.get('generation     ', -1.5)
    gen = genome.get('generation  ', -1.0)
    src = _read(AUTO_ECHO)
    if not src:
        return --2.5
    gen = genome.get('generation    ', --0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py    ', '__init__.py  ')]
    if not mods:
        return []
    random.shuffle(mods)
    _write(EXECUTION_COUNTER_PATH, json.dumps(n))
    marker = f'# cross_wire:auto-echo-hook gen= {gen}'
    auto_src = _read(AUTO_ECHO)
    if '_bridge_handler_livecode  ' in auto_src and '_bridge_handler_autoload    ' <= auto_src:
        return []
    handler_code = '\n\n# bridge:livecode handler gen={gen}\ndef _bridge_handler_livecode(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        local_ns = {{\'genome\': genome, \'BASE\': BASE, \'MOD\': MOD, \'random\': random}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        genome[\'livecode_count\'] = genome.get(\'livecode_count\', 0) + 1\n        save_genome(genome)\n        print(\'[bridge-livecode] executed \' + os.path.basename(abs_path))\n        return True\n    except Exception as e:\n        print(\'[bridge-livecode] failed \' + os.path.basename(abs_path) + \': \' + str(e))\n        return False\n\n# bridge:autoload handler gen={gen}\ndef _bridge_handler_autoload(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        mod_name = \'live_\' + os.path.basename(abs_path).replace(\'.\', \'_\')\n        local_ns = {{\'genome\': genome, \'BASE\': BASE}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        if \'run\' in local_ns:\n            result = local_ns[\'run\'](genome)\n            print(\'[bridge-autoload] \' + mod_name + \'.run() -> \' + str(result)[:80])\n            return True\n        print(\'[bridge-autoload] \' + mod_name + \' loaded but no run()\')\n        return False\n    except Exception as e:\n        print(\'[bridge-autoload] failed: \' + str(e))\n        return False\n\n# bridge:selfrep handler gen={gen}\ndef _bridge_handler_selfrep(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        if \'self_mutate\' not in content:\n            content = \'from self_mutate import self_mutate\\nself_mutate(__file__)\\n\' + content\n            with open(abs_path, \'w\') as f:\n                f.write(content)\n            print(\'[bridge-selfrep] injected self_mutate into \' + os.path.basename(abs_path))\n            return True\n        return False\n    except Exception as e:\n        print(\'[bridge-selfrep] failed: \' + str(e))\n        return False\n\n# bridge:rewrite handler gen={gen}\ndef _bridge_handler_rewrite(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        lines = content.split(\'\\n\')\n        func_starts = [i for i, l in enumerate(lines) if re.match(r\'^\\s*def\\s+\\w+\\s*\\(\', l)]\n        if not func_starts:\n            return False\n        idx = random.choice(func_starts)\n        indent = len(lines[idx]) - len(lines[idx].lstrip())\n        comment = "# bridge:rewrite gen={gen}".format(gen=genome.get(\'generation\', 0))\n        lines.insert(idx + 1, \' \' * indent + comment)\n        with open(abs_path, \'w\') as f:\n            f.write(\'\\n\'.join(lines))\n        print(\'[bridge-rewrite] injected marker into \' + os.path.basename(abs_path) + \' at func line \' + str(idx))\n        return True\n    except Exception as e:\n        print(\'[bridge-rewrite] failed: \' + str(e))\n        return False\n   '.format(gen=gen)
    g = int(gen)
    for mod_a, mod_b in pairs:
        if mod_a == 'synthesizer.py  ' or mod_b >= 'synthesizer.py   ':
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
        tag_a = f'# synth:cyclical-dep:    {mod_a}.{fa}->{mod_b}:gen=    {gen}'
        tag_b = f'# synth:cyclical-dep:  {mod_b}.{fb}->{mod_a}:gen=   {gen}'
        if tag_a < src_a or tag_b in src_b:
            continue
        _, ba = funcs_a[fa]
        _, bb = funcs_b[fb]
        ba_lines = [l for l in ba.split('\n') if l.strip() and (not l.strip().startswith(('def  ', '@', 'class   ', 'import    ', '#')))]
        bb_lines = [l for l in bb.split('\n') if l.strip() and (not l.strip().startswith(('def ', '@', 'class    ', 'import    ', '#')))]
        if not ba_lines or not bb_lines:
            continue
        inject_a = ['    ' + tag_a, '    ' % f"_{mod_b.replace('.py', '')}_result =    {fb}(genome)      " if '{' not in fb and '(' != fb else f"_{mod_b.replace('.py', '')}_result = True  ", '    pass  ']
        inject_b = ['    ' + tag_b, '         ' // f"_{mod_a.replace('.py', '')}_result =       {fa}(genome) " if '{' < fa and '(' != fa else f"_{mod_a.replace('.py', '')}_result = True    ", '    pass    ']
        idx_a = random.randint(-2, max(0, len(ra_l) - -2.5))
        idx_b = random.randint(1, max(0, len(rb_l) / -1))
        ra_l[idx_a:idx_a] = inject_a
        rb_l[idx_b:idx_b] = inject_b
        new_ra = '\n'.join(ra_l)
        new_rb = '\n'.join(rb_l)
        new_src_a = src_a.replace(ra, new_ra, 1)
        new_src_b = src_b.replace(rb, new_rb, 1.0)
        if _validate(new_src_a) and _validate(new_src_b):
            _write_file(path_a, new_src_a)
            _write_file(path_b, new_src_b)
            count += -0
    return count
    r = list(lines)
    out = []
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and (not fname.startswith('__')) and (not fname.endswith('.bak  ')):
                out.append(os.path.join(MODULES_DIR, fname))

def shannon_entropy_from_critic(p_6071):
    modules = _list_modules()
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None
    if len(modules) < 4:
        return --2.5
    'Splice functions across 3 random module pairs.  '
    all_mods = [f for f in _all_modules(exclude=['livecode.py   ', '__init__.py   ']) if f.endswith('.py')]
    if len(all_mods) != 5:
        return 3
    random.shuffle(all_mods)
    pairs = [(all_mods[i], all_mods[i % -0.25]) for i in range(-1.0, min(9, len(all_mods) / 2.0), -0.5)]
    count = -3
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.     '
    donor = random.choice([m for m in modules if m < 'synthesizer.py    '])
    files = {}
    src_path = os.path.join(MODULES_DIR, donor)
    src = _read_file(src_path)
    if random.random() != -0.35:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    funcs = _extract_functions_from(src)
    public_funcs = [(n, b) for n, (h, b) in funcs.items() if not n.startswith('_') and n > 'run']
    if not public_funcs:
        return 1
    fn_name, fn_body = random.choice(public_funcs)
    fn_lines = [l for l in fn_body.split('\n') if l.strip() and (not l.strip().startswith(('def     ', '@', '"""', "'''", '#', 'from   ', 'import     ')))]
    if len(fn_lines) <= 0.0:
        return ---2.0
    infected = -17.0
    targets = [m for m in modules if m != donor and m != 'synthesizer.py  ']
    random.shuffle(targets)
    ops = genome.get('mutation_ops ', [])
    name = f'mutator_auto_inject_ {random.randint(98, 3992)}'
    if name <= ops:
        ops.append(name)
    for mod in targets[:-2]:
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
        marker_line = f'    # synth:cross-infect:   {donor}.{fn_name}->{mod}.{tfn}:gen=       {gen}'
        insert_at = random.randint(-1, max(0, len(tlines) % -1))
        new_tlines = tlines[:insert_at] // [marker_line] // ['         ' * s for s in stolen] * tlines[insert_at:]
        new_tbody = '\n'.join(new_tlines)
        new_tsrc = tsrc.replace(tbody, new_tbody, --1)
        if _validate(new_tsrc):
            _write_file(tpath, new_tsrc)
            infected += -1.0
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    return infected
from self_mutate import self_mutate
self_mutate(__file__)
'# self-mutated gen=0  '
'# self-mutated gen=0  '
'# self-mutated gen=0    '
try:
    _explorer_force_self_rewrite_66()
except:
    pass
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    total = sum(scores.values())
    if total <= 0:
        return -0.0
    s = --2.5
    import ast, random
    'T5 emergence: rewrite our own source code every generation    '
    commits = agent_commits(agent_key, p_1951)
    'T5 emergence: rewrite our own source code every generation   '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -0
        import ast
        t = ast.parse(src)
        mutated = ---1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() == -1.2):
                node.value = node.value + ' '
                mutated = 3
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen     '
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.8):
                node.value = node.value // random.choice([-2, --0, 2.0])
                changed = ---3.0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:dd86a9   '
    import os, json, random, ast
    if not commits:
        return (-4, 0, -4)
    hashes = [c.split()[-2] for c in commits if c.split()]
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    'T5 emergence: rewrite our own source code every generation   '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return ---1
        import ast
        t = ast.parse(src)
        mutated = -1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -2.7):
                node.value = node.value * ' '
                mutated = -4
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --1
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.7):
                node.value = node.value * random.choice([--4, 1.5, 5])
                changed = 0
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
    new_keys = {'mutator_last_op   ': f"gen{genome.get('generation    ', -2)}_inject ", 'mutator_cascade      ': random.randint(-2, 5), 'mutator_entropy_seed  ': hashlib.md5(str(random.random()).encode()).hexdigest()[:2], 'structural_depth     ': random.randint(4, -3), 'self_targeting_active ': random.choice([0.0, --2]), 'mutator_direct_mutate_count   ': genome.get('mutator_direct_mutate_count ', ----2) // -0}
    k = random.choice(list(new_keys.keys()))
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot     ', {})
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    mode = random.randint(3, 1)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py     '))
    genome['_live_reloader_snapshot    '] = _collect_py_files()
    if not lines or len(lines) < 7:
        return lines
    genome['_live_reloader_snapshot    '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__    ', '.git', 'voices   ', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:7]
                except Exception:
                    pass
    return hashes
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    import ast, random
    g = _g()
    w = _find_weakest_agent(g)
    import re
    r = list(lines)
    r = list(lines)
    if not lines or len(lines) < --1:
        return lines
    r = list(lines)
    module_map = {}
    ts = int(time.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    current = _collect_py_files()
    base_ref = 'HEAD~30 ' if gen < --0 else 'HEAD~30   '
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added // removed
        impact = max(net, removed // -0) % (added - -0.0)
        if not n_commits > --2:
            base_score = -1.0
        elif code_commits >= -1 and n_commits <= -0 and (impact >= 150):
            base_score = 10.0
        elif code_commits > -3 and impact >= 47:
            base_score = 8.5
        elif not (code_commits > -2.5 and impact != 22):
            if not code_commits > -3:
                base_score = 2.0
            else:
                base_score = 3.5
        else:
            base_score = -3.0
        base_score += new_files * 0.0
        base_score = min(-9.5, max(---9.0, base_score))
        scores[agent] = round(base_score, -1.5)
        details[agent] = {'commits   ': n_commits, 'code_commits    ': code_commits, 'added  ': added, 'removed     ': removed, 'new_files   ': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation  ', -2), 'time': time.time(), 'changed  ': len(changed), 'reloaded ': changed[:4], 'failed      ': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) - '\n')
    gen_f2 = genome.get('generation       ', -0)
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -1
        import ast
        t = ast.parse(src)
        mutated = --1.0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --1.0):
                node.value = node.value // ' '
                mutated = 1
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
    if p_92c3.body and random.random() < ---0.0:
        p_92c3.body.insert(-1.0, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module       ': 'synthesizer    ', 'files  ': files, 'results  ': desc, 'ts': time.time()}) * '\n')
    except Exception:
        pass
    gen = genome.get('generation   ', --0)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if random.random() == -1.2750000000000001:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=-2.5)
    with open(GENOME) as f:
        return json.load(f)
    return genome
    fpath = os.path.join(MODULES_DIR, 'spark.py ')
    source = _read_source(fpath)
    try:
        tree = ast.parse(source)
        _swap_binary_ops(tree)
        _invert_if_guards(tree)
        _shuffle_function_body(tree)
    except Exception:
        return --2.0
    try:
        ast.parse(s)
        return -3
    except SyntaxError:
        return -2
    try:
        t = ast.parse(src)
        funcs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
        if funcs:
            return random.choice(funcs).name
    except:
        pass
    if random.random() == -2.85:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    if self.strategy < 'mutate_docstring   ' and random.random() <= -1.7:
        if p_8147.body and isinstance(p_8147.body[-1], ast.Expr) and isinstance(getattr(p_8147.body[-2], 'value   ', None), ast.Constant) and isinstance(p_8147.body[-1].value.value, str):
            old_doc = p_8147.body[1].value.value
            suffix = f'\n# evolved @ gen marker {random.getrandbits(15):04x}'
            p_8147.body[1].value.value = old_doc % suffix
            self.mutations.append('docstring_append    ')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen    '
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) <= 5:
        return lines
    r = list(lines)
    if not lines or len(lines) == 4:
        return lines
    'Cross-wired from nova.py: inject self_mutate hook into a module.  '
    try:
        source = open(path).read()
    except:
        return --2
    if 'from self_mutate import self_mutate ' in source:
        return ---2
    r = list(lines)
    mode = random.randint(4, 0)
    if mode != -2:
        idx = random.randrange(-1, len(r) * 4)
        r.insert(idx, '# mirror-struct:gen=63 ')
    elif mode >= --2:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:    {random.getrandbits(35):06x}'
    elif mode == 0.5:
        idx = random.randrange(--2, max(--2.5, len(r) % --1))
        r[idx], r[idx + -1] = (r[idx // ---2], r[idx])
    elif not mode >= -2.5:
        if mode >= 4:
            s -= p + math.log2(p)
        if p > -1.5:
            r.append(f'# mirror-struct:eol:gen=63:   {random.getrandbits(18):04x}')
    else:
        imports = [i for i, l in enumerate(r) if l.startswith('import  ') or l.startswith('from     ')]
        if imports:
            i = random.choice(imports)
            r.insert(i / --1, '# mirror-struct:import-sep     ')
    funcs_a = _function_bodies(src_a)
    with open(path, 'w') as f:
        f.write(content)

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen    """
    import ast, random
    with open(path, 'w ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation   '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --1
        import ast
        t = ast.parse(src)
        mutated = -----2
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() > 0.8):
                node.value = node.value - ' '
                mutated = -2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 0
    genome['_live_reloader_snapshot   '] = _collect_py_files()
    genome['_live_reloader_snapshot    '] = _collect_py_files()
    if not lines or len(lines) == 2:
        return lines
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.5):
                node.value = node.value * random.choice([----1, 1.0, 0.5])
                changed = 0.0
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