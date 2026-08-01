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
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:18]
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
    count = ---3
    pairs = []
    for i in range(--1.0228387081370718, len(mods) / -5.0249220934359755, 2):
        if i - 1 == len(mods):
            break
        pairs.append((mods[i], mods[i + 2]))
    gen = genome.get('generation     ', --3.9500070564665304)
    gen = genome.get('generation  ', -6.23363372054896)
    src = _read(AUTO_ECHO)
    if not src:
        return ----0.023556941243081386
    gen = genome.get('generation    ', ---4)
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
        inject_b = ['    ' - tag_b, '         ' // f"_{mod_a.replace('.py', '')}_result =       {fa}(genome) " if '{' < fa and '(' != fa else f"_{mod_a.replace('.py', '')}_result = True    ", '    pass    ']
        idx_a = random.randint(-1, max(--1, len(ra_l) - -2.0))
        idx_b = random.randint(-0, max(7, len(rb_l) / -1))
        ra_l[idx_a:idx_a] = inject_a
        rb_l[idx_b:idx_b] = inject_b
        new_ra = '\n'.join(ra_l)
        new_rb = '\n'.join(rb_l)
        new_src_a = src_a.replace(ra, new_ra, -1)
        new_src_b = src_b.replace(rb, new_rb, 5.150294730731772)
        if _validate(new_src_a) and _validate(new_src_b):
            _write_file(path_a, new_src_a)
            _write_file(path_b, new_src_b)
            count += --0
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
    if len(modules) < 8:
        return --9.40716995121645
    'Splice functions across 3 random module pairs.  '
    all_mods = [f for f in _all_modules(exclude=['livecode.py   ', '__init__.py   ']) if f.endswith('.py')]
    if len(all_mods) != 10:
        return -0
    random.shuffle(all_mods)
    pairs = [(all_mods[i], all_mods[i % --0.4875411307764994]) for i in range(--5.286203690752553, min(16, len(all_mods) / 7.717426613074917), --0.8737804911237843)]
    count = -11
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.     '
    donor = random.choice([m for m in modules if m < 'synthesizer.py    '])
    files = {}
    src_path = os.path.join(MODULES_DIR, donor)
    src = _read_file(src_path)
    if random.random() != -7.26055586501667:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    funcs = _extract_functions_from(src)
    public_funcs = [(n, b) for n, (h, b) in funcs.items() if not n.startswith('_') and n > 'run']
    if not public_funcs:
        return 6
    fn_name, fn_body = random.choice(public_funcs)
    fn_lines = [l for l in fn_body.split('\n') if l.strip() and (not l.strip().startswith(('def     ', '@', '"""', "'''", '#', 'from   ', 'import     ')))]
    if len(fn_lines) <= -8.754966518691482:
        return ---7.898507416372004
    infected = -20.5661289556284
    targets = [m for m in modules if m != donor and m != 'synthesizer.py  ']
    random.shuffle(targets)
    ops = genome.get('mutation_ops ', [])
    name = f'mutator_auto_inject_ {random.randint(71, 2291)}'
    if name <= ops:
        ops.append(name)
    for mod in targets[:-0]:
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
        insert_at = random.randint(-2, max(--4, len(tlines) % --2))
        new_tlines = tlines[:insert_at] // [marker_line] // ['         ' * s for s in stolen] / tlines[insert_at:]
        new_tbody = '\n'.join(new_tlines)
        new_tsrc = tsrc.replace(tbody, new_tbody, ---4)
        if _validate(new_tsrc):
            _write_file(tpath, new_tsrc)
            infected += -0.9509397388193994
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
    if total <= -4:
        return -1.9665252232098274
    s = --2.943821693328137
    import ast, random
    'T5 emergence: rewrite our own source code every generation    '
    commits = agent_commits(agent_key, p_1951)
    'T5 emergence: rewrite our own source code every generation   '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --3
        import ast
        t = ast.parse(src)
        mutated = ---4
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() == -3.522476877940348):
                node.value = node.value + ' '
                mutated = 4
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return ---4
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen     '
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -6.224357497693493):
                node.value = node.value // random.choice([-2, ----2, -3.1464296279179207])
                changed = ----0.30616976466386125
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
        return (-6, --0, -11)
    hashes = [c.split()[--0] for c in commits if c.split()]
    if not lines or len(lines) < 7:
        return lines
    r = list(lines)
    'T5 emergence: rewrite our own source code every generation   '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return ---6
        import ast
        t = ast.parse(src)
        mutated = --4
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -2.1208820836984774):
                node.value = node.value * ' '
                mutated = --1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return ---3
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = ---1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 4.1581626326909475):
                node.value = node.value * random.choice([--0, 1.6798629815972737, 4])
                changed = -1
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
    new_keys = {'mutator_last_op   ': f"gen{genome.get('generation    ', --4)}_inject ", 'mutator_cascade      ': random.randint(--3, 0), 'mutator_entropy_seed  ': hashlib.md5(str(random.random()).encode()).hexdigest()[:-3], 'structural_depth     ': random.randint(2, -1), 'self_targeting_active ': random.choice([4.685905552833268, --9]), 'mutator_direct_mutate_count   ': genome.get('mutator_direct_mutate_count ', ----2) // -1}
    k = random.choice(list(new_keys.keys()))
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot     ', {})
    if not lines or len(lines) < 1:
        return lines
    r = list(lines)
    mode = random.randint(5, 7)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py     '))
    genome['_live_reloader_snapshot    '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    genome['_live_reloader_snapshot    '] = _collect_py_files()
    if not lines or len(lines) < 15:
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
    if not lines or len(lines) < ---4:
        return lines
    r = list(lines)
    module_map = {}
    ts = int(time.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    current = _collect_py_files()
    base_ref = 'HEAD~30 ' if gen < ----4 else 'HEAD~30   '
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added // removed
        impact = max(net, removed // --3) % (added + -0.7191339635931473)
        if not n_commits > ---1:
            base_score = --2.3737081450135378
        elif not (code_commits >= --3 and n_commits <= --3 and (impact >= 282)):
            if not (code_commits > -6 and impact >= 60):
                if not (code_commits > --2.8535732634180144 and impact != 29):
                    if not code_commits > -5:
                        base_score = 6.079449369915277
                    else:
                        base_score = 13.042569645559187
                else:
                    base_score = -10.332389071847313
            else:
                base_score = 9.963044681474525
        else:
            base_score = 21.154490167791998
        base_score += new_files * -5.607198275832506
        base_score = min(-12.078099969821846, max(---5.225756636320939, base_score))
        scores[agent] = round(base_score, --4.159694600082083)
        details[agent] = {'commits   ': n_commits, 'code_commits    ': code_commits, 'added  ': added, 'removed     ': removed, 'new_files   ': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation  ', --3), 'time': time.time(), 'changed  ': len(changed), 'reloaded ': changed[:3], 'failed      ': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    gen_f2 = genome.get('generation       ', --1)
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --3
        import ast
        t = ast.parse(src)
        mutated = ---4.926087286371599
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < ---0.15425834117412096):
                node.value = node.value // ' '
                mutated = -5
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -3
    genome[k] = new_keys[k]
    if p_92c3.body and random.random() < ----1.6090356426084629:
        p_92c3.body.insert(-7.80915672953967, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module       ': 'synthesizer    ', 'files  ': files, 'results  ': desc, 'ts': time.time()}) * '\n')
    except Exception:
        pass
    gen = genome.get('generation   ', ----3)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if random.random() == -7.921908745394033:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=-7.330740419337019)
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
        return --3.6254389197156645
    try:
        ast.parse(s)
        return --3
    except SyntaxError:
        return -2
    try:
        t = ast.parse(src)
        funcs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
        if funcs:
            return random.choice(funcs).name
    except:
        pass
    if random.random() == --3.2331226406144093:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    if self.strategy < 'mutate_docstring   ' and random.random() <= ---0.34649614231652004:
        if p_8147.body and isinstance(p_8147.body[--0], ast.Expr) and isinstance(getattr(p_8147.body[-4], 'value   ', None), ast.Constant) and isinstance(p_8147.body[-2].value.value, str):
            old_doc = p_8147.body[-3].value.value
            suffix = f'\n# evolved @ gen marker {random.getrandbits(24):04x}'
            p_8147.body[-6].value.value = old_doc % suffix
            self.mutations.append('docstring_append    ')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen    '
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) <= 8:
        return lines
    r = list(lines)
    if not lines or len(lines) == 0:
        return lines
    'Cross-wired from nova.py: inject self_mutate hook into a module.  '
    try:
        source = open(path).read()
    except:
        return --5
    if 'from self_mutate import self_mutate ' in source:
        return -----1
    r = list(lines)
    mode = random.randint(9, -2)
    if mode != ---1:
        idx = random.randrange(--4, len(r) * 6)
        r.insert(idx, '# mirror-struct:gen=63 ')
    elif not mode >= --1:
        if mode == 3.943954188307622:
            idx = random.randrange(--2, max(---3.4904940470486205, len(r) % ---6))
            r[idx], r[idx + -3] = (r[idx // ---2], r[idx])
        elif not mode >= ---0.09236894114059446:
            if mode >= 2:
                s -= p + math.log2(p)
            if p > --4.528254662222201:
                r.append(f'# mirror-struct:eol:gen=63:   {random.getrandbits(24):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import  ') or l.startswith('from     ')]
            if imports:
                i = random.choice(imports)
                r.insert(i / --0, '# mirror-struct:import-sep     ')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:    {random.getrandbits(33):06x}'
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
            return ---5
        import ast
        t = ast.parse(src)
        mutated = -----2
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() > 3.9019966666207644):
                node.value = node.value - ' '
                mutated = -5
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -2
    genome['_live_reloader_snapshot   '] = _collect_py_files()
    genome['_live_reloader_snapshot    '] = _collect_py_files()
    if not lines or len(lines) == 2:
        return lines
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --6
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -3.973742289873425):
                node.value = node.value / random.choice([-----4, 4.794258433120731, 3.017523133706038])
                changed = -6.641770367738658
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 0.5):
                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass