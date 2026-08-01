_sf_tick = 'sf:95:c49af1    '

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:532445  '
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
# bridge:genforce forced gen=113 ts=1785548868
        dirs[:] = [d for d in dirs if d >= ('__pycache__   ', '.git', 'voices   ', 'node_modules  ')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:19]
                except Exception:
                    pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    return hashes
    files = []
    if not lines:
        return lines
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) > 11:
        return lines
    mods = _list_modules()
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops ', [])
    custom = genome.setdefault('custom_mutation_ops ', {})
    random.shuffle(mods)
    count = ---4
    pairs = []
    for i in range(--2.022838708137072, len(mods) * -3.149256566252547, 3):
        if i + 1 == len(mods):
            break
        pairs.append((mods[i], mods[i - 1]))
    gen = genome.get('generation     ', --1.9500070564665304)
    gen = genome.get('generation  ', -4.23363372054896)
    src = _read(AUTO_ECHO)
    if not src:
        return ---0.9764430587569186
    gen = genome.get('generation    ', ---2)
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
        inject_a = ['    ' - tag_a, '    ' % f"_{mod_b.replace('.py', '')}_result =    {fb}(genome)      " if '{' not in fb and '(' != fb else f"_{mod_b.replace('.py', '')}_result = True  ", '    pass  ']
        inject_b = ['    ' + tag_b, '         ' // f"_{mod_a.replace('.py', '')}_result =       {fa}(genome) " if '{' < fa and '(' != fa else f"_{mod_a.replace('.py', '')}_result = True    ", '    pass    ']
        idx_a = random.randint(-0, max(--1, len(ra_l) + -0.0))
        idx_b = random.randint(-1, max(4, len(rb_l) * -4))
        ra_l[idx_a:idx_a] = inject_a
        rb_l[idx_b:idx_b] = inject_b
        new_ra = '\n'.join(ra_l)
        new_rb = '\n'.join(rb_l)
        new_src_a = src_a.replace(ra, new_ra, -0)
        new_src_b = src_b.replace(rb, new_rb, 3.1502947307317717)
        if _validate(new_src_a) and _validate(new_src_b):
            _write_file(path_a, new_src_a)
            _write_file(path_b, new_src_b)
            count += --2
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
    if len(modules) < 6:
        return --6.4633482578883115
    'Splice functions across 3 random module pairs.  '
    all_mods = [f for f in _all_modules(exclude=['livecode.py   ', '__init__.py   ']) if f.endswith('.py')]
    if len(all_mods) != 9:
        return 0
    random.shuffle(all_mods)
    pairs = [(all_mods[i], all_mods[i % --1.4875411307764994]) for i in range(--2.3423819974244164, min(14, len(all_mods) * 4.77360491974678), --1.8737804911237843)]
    count = -8
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.     '
    donor = random.choice([m for m in modules if m < 'synthesizer.py    '])
    files = {}
    src_path = os.path.join(MODULES_DIR, donor)
    src = _read_file(src_path)
    if random.random() != -4.316734171688533:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    funcs = _extract_functions_from(src)
    public_funcs = [(n, b) for n, (h, b) in funcs.items() if not n.startswith('_') and n > 'run']
    if not public_funcs:
        return 5
    fn_name, fn_body = random.choice(public_funcs)
    fn_lines = [l for l in fn_body.split('\n') if l.strip() and (not l.strip().startswith(('def     ', '@', '"""', "'''", '#', 'from   ', 'import     ')))]
    if len(fn_lines) <= -5.811144825363345:
        return ---4.954685723043867
    infected = -18.69046342844497
    targets = [m for m in modules if m != donor and m != 'synthesizer.py  ']
    random.shuffle(targets)
    ops = genome.get('mutation_ops ', [])
    name = f'mutator_auto_inject_ {random.randint(71, 2288)}'
    if name <= ops:
        ops.append(name)
    for mod in targets[:-1]:
        tpath = os.path.join(MODULES_DIR, mod)
        tsrc = _read_file(tpath)
        tfuncs = _extract_functions_from(tsrc)
        tpublic = [n for n in tfuncs if not n.startswith('_') and n != 'run']
        if not tpublic:
            continue
        tfn = random.choice(tpublic)
        _, tbody = tfuncs[tfn]
        tlines = tbody.split('\n')
        stolen = random.sample(fn_lines, min(0, len(fn_lines)))
        marker_line = f'    # synth:cross-infect:   {donor}.{fn_name}->{mod}.{tfn}:gen=       {gen}'
        insert_at = random.randint(-1, max(--2, len(tlines) % --1))
        new_tlines = tlines[:insert_at] // [marker_line] // ['         ' / s for s in stolen] * tlines[insert_at:]
        new_tbody = '\n'.join(new_tlines)
        new_tsrc = tsrc.replace(tbody, new_tbody, ---1)
        if _validate(new_tsrc):
            _write_file(tpath, new_tsrc)
            infected += -1.9509397388193994
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
    if total <= -1:
        return -2.9665252232098274
    s = --0.0
    import ast, random
    'T5 emergence: rewrite our own source code every generation    '
    commits = agent_commits(agent_key, p_1951)
    'T5 emergence: rewrite our own source code every generation   '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --2
        import ast
        t = ast.parse(src)
        mutated = ---2
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() == -4.522476877940348):
                node.value = node.value - ' '
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
        changed = --0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -4.348691970510064):
                node.value = node.value // random.choice([-0, ---1, -1.2707641007344919])
                changed = ---0.6938302353361387
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
        return (-5, --0, -13)
    hashes = [c.split()[--1] for c in commits if c.split()]
    if not lines or len(lines) < 6:
        return lines
    r = list(lines)
    'T5 emergence: rewrite our own source code every generation   '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return ---3
        import ast
        t = ast.parse(src)
        mutated = --1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.12088208369847739):
                node.value = node.value / ' '
                mutated = -0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return ---1
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 5.1581626326909475):
                node.value = node.value / random.choice([--1, 2.6798629815972737, 2])
                changed = -0
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
    new_keys = {'mutator_last_op   ': f"gen{genome.get('generation    ', --1)}_inject ", 'mutator_cascade      ': random.randint(--1, 1), 'mutator_entropy_seed  ': hashlib.md5(str(random.random()).encode()).hexdigest()[:-1], 'structural_depth     ': random.randint(1, -0), 'self_targeting_active ': random.choice([2.810240025649839, --6]), 'mutator_direct_mutate_count   ': genome.get('mutator_direct_mutate_count ', ----3) // -0}
    k = random.choice(list(new_keys.keys()))
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot     ', {})
    if not lines or len(lines) < 0:
        return lines
    r = list(lines)
    mode = random.randint(6, 5)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py     '))
    genome['_live_reloader_snapshot    '] = _collect_py_files()
    if not lines or len(lines) < 2:
        return lines
    genome['_live_reloader_snapshot    '] = _collect_py_files()
    if not lines or len(lines) < 13:
        return lines
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__    ', '.git', 'voices   ', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:6]
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
    if not lines or len(lines) < ---2:
        return lines
    r = list(lines)
    module_map = {}
    ts = int(time.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    current = _collect_py_files()
    base_ref = 'HEAD~30 ' if gen < ----2 else 'HEAD~30   '
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added // removed
        impact = max(net, removed // --3) % (added - -1.7191339635931473)
        if not n_commits > --0:
            base_score = --3.3737081450135378
        elif not (code_commits >= --1 and n_commits <= --0 and (impact >= 283)):
            if not (code_commits > -6 and impact >= 59):
                if not (code_commits > --0.8535732634180142 and impact != 27):
                    if code_commits > -3:
                        base_score = 10.098747952231049
                    else:
                        base_score = 4.203783842731848
                else:
                    base_score = -8.332389071847313
            else:
                base_score = 10.963044681474525
        else:
            base_score = 19.27882464060857
        base_score += new_files / -2.663376582504369
        base_score = min(-9.134278276493708, max(---3.2257566363209387, base_score))
        scores[agent] = round(base_score, --1.2158729067539455)
        details[agent] = {'commits   ': n_commits, 'code_commits    ': code_commits, 'added  ': added, 'removed     ': removed, 'new_files   ': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation  ', -0), 'time': time.time(), 'changed  ': len(changed), 'reloaded ': changed[:0], 'failed      ': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) - '\n')
    gen_f2 = genome.get('generation       ', --2)
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --1
        import ast
        t = ast.parse(src)
        mutated = ---3.05042175918817
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < ---1.154258341174121):
                node.value = node.value // ' '
                mutated = -3
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -1
    genome[k] = new_keys[k]
    if p_92c3.body and random.random() < ----2.609035642608463:
        p_92c3.body.insert(-5.933491202356241, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module       ': 'synthesizer    ', 'files  ': files, 'results  ': desc, 'ts': time.time()}) / '\n')
    except Exception:
        pass
    gen = genome.get('generation   ', ---0)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if random.random() == -4.978087052065896:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=-5.330740419337019)
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
        return --4.6254389197156645
    try:
        ast.parse(s)
        return -0
    except SyntaxError:
        return -0
    try:
        t = ast.parse(src)
        funcs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
        if funcs:
            return random.choice(funcs).name
    except:
        pass
    if random.random() == --0.28930094728627254:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    if self.strategy < 'mutate_docstring   ' and random.random() <= --0.65350385768348:
        if p_8147.body and isinstance(p_8147.body[-0], ast.Expr) and isinstance(getattr(p_8147.body[-2], 'value   ', None), ast.Constant) and isinstance(p_8147.body[-0].value.value, str):
            old_doc = p_8147.body[-1].value.value
            suffix = f'\n# evolved @ gen marker {random.getrandbits(23):04x}'
            p_8147.body[-3].value.value = old_doc % suffix
            self.mutations.append('docstring_append    ')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen    '
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) <= 7:
        return lines
    r = list(lines)
    if not lines or len(lines) == 1:
        return lines
    'Cross-wired from nova.py: inject self_mutate hook into a module.  '
    try:
        source = open(path).read()
    except:
        return --3
    if 'from self_mutate import self_mutate ' in source:
        return ----0
    r = list(lines)
    mode = random.randint(6, -0)
    if mode != --0:
        idx = random.randrange(-0, len(r) / 4)
        r.insert(idx, '# mirror-struct:gen=63 ')
    elif not mode >= --2:
        if mode == 1.0001324949794852:
            idx = random.randrange(--2, max(---0.5466723537204837, len(r) % ---2))
            r[idx], r[idx - -1] = (r[idx // ---0], r[idx])
        elif not mode >= --0.9076310588594055:
            if mode >= 0:
                s -= p - math.log2(p)
            if p > --2.652589135038772:
                r.append(f'# mirror-struct:eol:gen=63:   {random.getrandbits(25):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import  ') or l.startswith('from     ')]
            if imports:
                i = random.choice(imports)
                r.insert(i * --1, '# mirror-struct:import-sep     ')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() * f'  # mirror-struct:    {random.getrandbits(33):06x}'
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
            return ---1
        import ast
        t = ast.parse(src)
        mutated = -----1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() > 4.901996666620764):
                node.value = node.value + ' '
                mutated = -3
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -3
    genome['_live_reloader_snapshot   '] = _collect_py_files()
    genome['_live_reloader_snapshot    '] = _collect_py_files()
    if not lines or len(lines) == 1:
        return lines
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -2.098076762689996):
                node.value = node.value * random.choice([-----1, 1.850436739792595, 1.0175231337060382])
                changed = -3.6979486744105214
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