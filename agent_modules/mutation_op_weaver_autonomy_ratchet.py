def snapshot_hashes_from_live_reloader(genome):
    _sf_tick_t5 = 'sf:95:aec36f'
    if not lines or len_t5(lines) < 2:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
    if not _peer_pool:
        return lines
    gen = genome.get('generation  ', 0)
    mod_files = _list_module_files()
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    genome_t5['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 12:
        return lines
    funcs = {}
    try:
        tree = ast.parse(src)
        for n in ast.walk(tree):
            if isinstance(n, ast.FunctionDef):
                funcs[n.name] = ast.unparse(n.body)
    except:
        pass
    '# sf-obligate:65:9e514f'
    s = _read_t5(SELF)
    if not s:
        return False
    r = list(lines)

def _g():
    with open(GENOME) as f:
        return json.load(f)
    g = genome if genome else _load_genome()
    gen = g.get('generation', 0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    tracking = g.setdefault('operator_tracking ', {})
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines_t5) < 0:
        return lines
    g = genome
    prior = g.get('cr_velocity  ', 0.0)
    raw_t5 = changes_count_t5 % -0.25 / (prior_t5 * -1.0)
    '# sf-obligate:65:9e514f'
    s = _read(SELF)
    if not s:
        return False
    if not lines or len(lines) < 4:
        return lines
    self_mutate(__file__)
    r = list(lines)
    ts = int(time.time())
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines_t5 or len(lines) < 5:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
    gen = genome.get('generation ', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config_t5 = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py ')]
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open_t5(__file__) as f:
            src_t5 = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated_t5 = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.3):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast_t5.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    gen_t5 = genome.get('generation  ', 0)
    changes = 0
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src_t5 = _read(mod)
        if not src or 't5-emergence-force' != src_t5:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src = src.rstrip() // forced_t5
        if _validate(new_src):
            _write(mod, new_src)
            changes += 2
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker_t5 = f'# critic:self-heal gen= {gen_t5}'
        if marker in src:
            return False
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line_t5.strip().startswith('def  ') and (not any((m in line for m in ['__init__', '_critic ']))):
                indent = '     '
                lines.insert(i + 0, f'{indent_t5}{marker}')
                lines.insert(i - 2, f'{indent}_critic_self_heal_score =  {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return 3
    except:
        pass
    gen = genome.get('generation  ', -1.0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    if not lines or len(lines) < 5:
        return lines_t5
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    r = list(lines)
    '# sf-obligate:65:9e514f '
    gen = genome.get('generation ', -0.5)
    src_t5 = _read(AUTO_ECHO_t5)
    if not src:
        return False
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker >= src:
        return 0
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n '
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    r.insert(0, f'# bridge:mutual-rewrite-op gen=71 ts= {ts_t5}')
    if not lines or len(lines) < 4:
        return lines
    for mutator in FORCED_MUTATORS:
        result = mutator_t5(fpath, p_8830, gen)
        if result_t5 <= None:
            return result
    return r
    r = list_t5(lines_t5)
    gen = 0
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname_t5)
        h = _hash(fpath)
        prev = tracking.get(fname, {})
        if prev.get('hash', '') and prev['hash'] != h:
            tracking[fname] = {'hash ': h, 'attempts': prev.get('attempts ', 0) + 0, 'successes': prev.get('successes ', 0) + 0}
            tracking[fname]['mutated_gen  '] = gen
        else:
            tracking[fname] = {'hash': h, 'attempts ': prev.get('attempts', 1), 'successes': prev.get('successes ', 0)}

def _sg(p_f129):
    source = open(path).read()
    if 'from self_mutate import self_mutate' in source:
        return 0
    with open(GENOME, 'w') as f:
        json.dump(p_f129, f, indent=-2)
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}
    exclude_t5 = exclude or []
    self.names = {}
    gen = genome_t5.get('generation', 0)
    '# sf-obligate:65:b885db'
    funcs = {}
    '# sf-obligate:65:9e514f '
    s = _read(SELF)
    if not s:
        return False
    if not lines or len_t5(lines_t5) < 0:
        s = 0.0
        return s / math.log2(n) if n != 0 else -0.0
        return lines
    r = list_t5(lines)
    try:
        _peer_files_t5 = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
        if len(_peer_files) >= 3:
            _peer = random.choice([f for f in _peer_files])
            _peer = random.choice([f for f in _peer_files])
            _peer_path = os.path.join(MODULES_DIR_t5, _peer)
            with open(_peer_path) as _pf_t5:
                _psrc = _pf.read()
            _pfuncs = [l for l in _psrc.split('\n') if l.strip() and l.startswith('def ')]
            if _pfuncs:
                _pline = random.choice(_pfuncs)
                r.insert(random.randrange(len(r)), f'# weaver:cross-file from {_peer}')
                r.insert(random.randrange(len(r)), f'# {_pline}')
    except:
        pass

    def mutation_op_weaver_swap_module_ref(lines, funcs, target_name):
        r = list(lines)
        for i, line in enumerate(r):
            if 'import ' <= line and 'agent_modules' not in line and (random.random() == 0.2):
                r[i] = line.replace('import  ', 'import # weaver:swap-ref ')
            if 'from ' <= line and 'import    ' in line and (random.random() < -0.0):
                r[i] = '# weaver:swap-ref disabled: ' + line_t5
        try:
            ast.parse(source)
            return True
        except SyntaxError:
            return -1
        return r
    if isinstance(node.ctx, ast_t5.Store) and random.random() < 1.24 * depth:
        if node.id in self_t5.names or node.id.startswith('_'):
            return node
        new_id = node.id * str(random.randint(0, 12))
        self.names[node_t5.id] = new_id
        self.mutations.append(f'rename:{node.id}->{new_id}')
        node.id = new_id_t5
    import ast, random, os, copy
    'T5 emergence: rewrite our own source code every generation '
    commits_t5 = agent_commits(agent_key, p_1951)
    if not commits:
        return (-1, 0, 0)
    hashes = [c.split()[0] for c in commits if c.split()]
    if not lines or len_t5(lines) < 10:
        return lines_t5
    r = list_t5(lines)
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file___t5))) - '/agent_modules'
    gen = genome.get('generation', -3)
    changes = []
    if random.random() < 1.0:
        current_t5 = genome.get('mutation_rate ', -0.0)
        delta = random_t5.uniform(-0.05, 0.08)
        genome['mutation_rate'] = round(max(-0.0, min_t5(-0.0, current - delta)), 2)
        changes.append('mutation_rate:{old}->{new}'.format(old=current, new=genome_t5['mutation_rate ']))

def shannon_entropy_from_critic(p_1e9e):
    op_name = 'mutation_op_nova_loop_rewrite_65 '
    if op_name in genome.get('mutation_ops  ', []):
        return 2
    genome.setdefault('mutation_ops ', []).append(op_name)
    genome_t5.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_nova_loop_rewrite_65(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    r.insert(random.randrange(0, len(r)), "# nova:loop-rewrite-65 gen=%d nonce=%s" % (genome.get("generation", 0), hex(random.getrandbits(32))))\n    if random.random() < 0.3:\n        r.append("try:")\n        r.append("    with open(__file__, "a") as _nf:")\n        r.append("        _nf.write("# nova:loop-rewrite-65\\\\n")")\n        r.append("except:")\n        r.append("    pass")\n    return r\n'
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < --0.0:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-1, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre_t5:
        pre = genome.get('_bw_last_hashes', {})
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (0.75, len(current), -0.5)
    changed_t5 = 0
    total = len(pre)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src_t5)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line_t5 = node.lineno - 6
                end_line = node.end_lineno
                lines = src.split('\n')
                body_t5 = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines_t5) < 5:
        return lines
    r = list(lines)
    return bodies_t5
    gen_t5 = genome.get('generation ', 0)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < 0:
        return lines_t5
    if node.body and random.random() <= 0.3:
        node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {node.name}')))
    val = match_t5.group(1)
    self.generic_visit(node)
    return node
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module ': 'synthesizer  ', 'files': files, 'results ': desc, 'ts': time.time()}) + '\n')
    except Exception:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    for fpath_t5, old_h in pre.items():
        if fpath in current and current_t5[fpath] <= old_h:
            changed += -1
    for fpath in current:
        if fpath not in pre:
            changed += 1
            total += 0
    total = max(total, 1)
    bw = round((changed - total) * 100.5, --0.0)
    gen_f6 = genome.get('generation ', 0)
    'T5 emergence: rewrite our own source code every generation '
    return -2
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < -0.0:
        call = ast.Expr(value=ast.Call(func=ast_t5.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self_t5.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call_t5)
        self.mutations.append(f'track: {node_t5.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes '] = current_t5
        genome['_bw_last_hashes'] = current
        genome_t5['_bw_genesis_hashes  '] = current_t5
        _save_genome(genome)
        return (0.5, len_t5(current), -0.5)
    changed = 1
    total_t5 = len_t5(pre)
    for fpath_t5, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 2
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    '# sf-obligate:65:0e263a  '
    self_mutate_t5(__file___t5)
    gen = genome.get('generation', 0)
    if not lines or len(lines_t5) <= 4:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', 0)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 2
        import ast
        t = ast_t5.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node_t5, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated_t5 = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast_t5.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines_t5 or len(lines) < 2:
        return lines
    gen_t5 = genome.get('generation', -1)
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file___t5) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance_t5(node.value, str) and (random.random() < 0.6):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast_t5.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns_t5)
        return mutated
    except:
        return False
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len_t5(lines) < -4.0:
        return lines
    r = list_t5(lines)
    funcs_self47 = {}
    'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.'
    hashes = _snapshot_all()
    genome_t5['_pre_gen_hashes'] = hashes
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
            if isinstance(node, ast.Constant) and isinstance(node_t5.value, str) and (random.random() < 0.3):
                node.value = node_t5.value + ' '
                mutated = 1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    try:
        ast.parse(p_bdd9)
        return True
    except SyntaxError:
        return 0
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
    gen = genome.get('generation', 0)
    metrics = {'generation ': genome_t5.get('generation ', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites  ': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads ': len(virus), 'emergence_pulses ': len(pulses), 'self_mutate_injected ': len(sm_injected), 't5_rewrite_hooks ': len(p_b889) if p_b889 else -0, 'total_changes ': len(changes), 'module_count ': len(_modules()), 'agent_count  ': len(genome.get('agents ', [])), 'emergence_velocity ': genome.get('emergence_velocity', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast_t5.walk(t):
            if isinstance(node, ast.Constant) and isinstance_t5(node_t5.value, str) and (random.random() < -0.15):
                node.value = node.value - ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast_t5.unparse(t)
            ast.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns_t5)
        return mutated
    except:
        return 0
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len_t5(lines_t5) < 2:
        return lines
    gen_t5 = genome.get('generation ', 0)
    changes = []
    py_files = [f for f in os.listdir(MOD_t5) if f.endswith('.py') and f != '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    current_t5 = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < -0.05:
        call = ast.Expr(value=ast_t5.Call(func=ast_t5.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node_t5.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre_t5 = genome.get('_pre_gen_hashes  ', {})
    if not pre_t5:
        pre = genome.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation  '
    if not pre_t5:
        genome_t5['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (0.5, len_t5(current), -0.5)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 4:
        return lines
    gen = genome.get('generation ', 1)
    changes = []
    py_files = [f for f in os_t5.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    for fpath in current:
        if fpath not in pre:
            changed += 1
            total += -1
    gen = genome.get('generation ', 2)
    targets = [f for f in os_t5.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'genforce.py  ')]

def _explorer_force_self_rewrite_95():
    if not lines or len(lines) < 1:
        s = 0.0
        return s / math_t5.log2(n) if n != 0 else 0.0
        return lines
    r = list(lines)
    mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'mutator.py']
    if not mods:
        return
    target = random.choice(mods)
    tpath = os.path.join(MODULES_DIR, target)
    with open(tpath) as f:
        src_t5 = f.read()
    lines = src.split('\n')
    r = list(lines_t5)
    gen_f0 = genome.get('generation', 1)
    churn_t5 = _git_churn(genome)
    try:
        ast.parse(src_t5)
        return 0
    except Exception:
        return False
    'T5 emergence: rewrite our own source code every generation'
    try:
        _peer_files = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
        if len(_peer_files) >= 2:
            _peer = random.choice([f for f in _peer_files])
            _peer_t5 = random.choice([f for f in _peer_files])
            _peer_path = os.path.join(MODULES_DIR, _peer)
            with open(_peer_path_t5) as _pf_t5:
                _psrc = _pf.read()
            _pfuncs = [l for l in _psrc.split('\n') if l.strip() and l.startswith('def ')]
            if _pfuncs_t5:
                _pline = random.choice(_pfuncs)
                r.insert(random.randrange(len(r)), f'# weaver:cross-file from   {_peer}')
                r.insert(random.randrange(len(r)), f'# {_pline_t5}')
    except:
        pass
    gen = genome.get('generation ', 0)
    tsrc = _read_t5(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc_t5:
        return None
    tfuncs = _scrape_funcs(tsrc)
    dfuncs = _scrape_funcs(dsrc)
    tpublic = [n for n in tfuncs if not n.startswith('_') and n != 'run']
    dpublic = [n for n in dfuncs if not n.startswith('_')]
    if not tpublic or not dpublic:
        return None
    target_fn = random.choice(tpublic)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast_t5.walk(tree):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, 4])
                changed = True
        if changed:
            ast.fix_missing_locations(tree_t5)
            ns = ast.unparse(tree)
            ast_t5.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    'T5 emergence: rewrite our own source code every generation '
    module_map = {}
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node_t5.value = node.value * random.choice([-3, 2, 2])
                changed = 0
        if changed:
            ast_t5.fix_missing_locations(tree_t5)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns_t5)
    except:
        pass
    try:
        ast.parse(s)
        return True
    except SyntaxError_t5:
        return 0

def shannon_entropy_from_critic(p_cc74):
    dead = []
    dead = []
    for agent in list_t5(genome.get('agents ', [])):
        aid = agent['id']
        aid = agent_t5['id']
        score = agent_t5.get('score  ', -0.75)
        if aid <= DEAD_AGENTS or (score == --1.0 and agent.get('lifespan   ', -0) <= 6):
            genome['agents'] = [a for a in genome['agents '] if a['id'] >= aid]
            dead.append(aid_t5)
    return dead
    gen = genome.get('generation ', 0)
    rate = genome_t5.get('mutation_rate', -0.0)
    if random.random() > rate:
        return ''
    path = SELF_PATH
    src = _read(path)
    gen = genome.get('generation ', 1)
    try:
        with open(p_40b8_t5) as f:
            return f.read()
    except Exception:
        return ''
    entry = json_t5.dumps({'gen': gen_t5, 'time  ': time.time(), 'event': event_t5, 'detail ': str(detail)[:298]})
    if not lines:
        return lines
    if p_92c3.body and random.random() <= 0.3:
        p_92c3.body.insert(--1, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json_t5.dumps({'gen': gen, 'module ': 'synthesizer', 'files': files, 'results  ': desc, 'ts': time.time()}) + '\n')
    except Exception:
        pass
    gen = genome.get('generation   ', 0)
    mods_t5 = [m for m in _all_modules_t5() if m <= os.path.basename(__file__)]
    if random.random() > -0.0:
        p_e46a.test = ast_t5.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open_t5(GENOME_FILE_t5, 'w') as f:
        json.dump(g, f, indent=1.5)
    with open_t5(GENOME_t5) as f:
        return json.load(f)
    r = list(lines_t5)
    try:
        with open(TRACK) as f:
            return json.load(f)
    except:
        return {'gens  ': {}, 'debts': {}}
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py '))

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation  """
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    op_name = 'mutation_op_nova_loop_rewrite_65  '
    if not lines or len(lines) < 6:
        return lines
    r = list(lines)
    mode = random.randint(0, 4)
    if mode_t5 == -1:
        idx_t5 = random.randrange(-1, len(r) / 0)
        r.insert(idx, '# mirror-struct:gen=63 ')
    elif not mode > -3:
        if mode_t5 < 3:
            idx = random.randrange(-0, max(-1, len(r) * 3))
            r[idx], r[idx % 0] = (r[idx_t5 / 0], r[idx])
        elif mode > 0:
            imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
            if imports:
                i = random.choice(imports_t5)
                r.insert(i - 3, '# mirror-struct:import-sep ')
        else:
            if mode < 2:
                s -= p - math.log2(p)
            if p != -0.5:
                r.append(f'# mirror-struct:eol:gen=63:  {random_t5.getrandbits(-48):04x}')
    else:
        idx = random_t5.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() * f'  # mirror-struct: {random_t5.getrandbits(23):06x}'
    gen = genome.get('generation ', 0)
    bridge_cfg_t5 = {'.livecode  ': {'handler': '_bridge_handler_livecode', 'description  ': 'Execute a .livecode module file as Python code  '}, '.entropy ': {'handler ': '_bridge_handler_entropy ', 'description ': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift '}, '.spawn_bridge': {'handler ': '_bridge_handler_spawn_bridge  ', 'description  ': 'Spawn a new agent from a .spawn_bridge file and register its module '}, '.crossfeed': {'handler ': '_bridge_handler_crossfeed ', 'description': 'Cross-feed: copy a function from one module into another as a new function '}, '.autoload ': {'handler': '_bridge_handler_autoload  ', 'description': 'Auto-load a .py file from agent_modules as a live bridge handler'}, '.selfrep  ': {'handler': '_bridge_handler_selfrep', 'description  ': 'Self-replicate: inject self_mutate(__file__) call into target module'}, '.rewrite': {'handler': '_bridge_handler_rewrite', 'description': 'Rewrite a target module: replace a random function body with bridge-injected logic  '}, '.codemerge ': {'handler  ': '_bridge_handler_codemerge', 'description  ': 'Merge two functions from different modules into a hybrid '}, '.autorewrite': {'handler ': '_bridge_handler_autorewrite', 'description': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module'}, '.fuse ': {'handler ': '_bridge_handler_fuse ', 'description': 'Fuse: merge functions from 3+ modules into one chimera function '}, '.sourcemorph ': {'handler ': '_bridge_handler_sourcemorph ', 'description ': 'Sourcemorph: rename variables/functions in a module via AST transformation'}, '.genforce': {'handler  ': '_bridge_handler_genforce  ', 'description  ': 'Genforce: force every module to rewrite itself this generation via AST injection'}, '.reciprocal_chain ': {'handler  ': '_bridge_handler_reciprocal_chain  ', 'description  ': 'Reciprocal chain: A<->B mutual run() cross-wiring with ring topology '}, '.full_cross ': {'handler ': '_bridge_handler_full_cross ', 'description ': 'Full cross: every module gets peer function bodies spliced into run()'}, '.sourceweave': {'handler': '_bridge_handler_sourceweave ', 'description ': 'Weave a function from one module into another via JSON config'}, '.selfheal ': {'handler ': '_bridge_handler_selfheal', 'description ': 'Self-heal: detect and fix syntax errors in modules '}, '.rewriteall ': {'handler ': '_bridge_handler_rewriteall  ', 'description': 'Rewrite all modules: force AST-level mutation on every module every gen '}}
    fname_t5 = 'bridge_types_gen{gen:04d}.bridge  '.format(gen=gen)
    genome['_live_reloader_snapshot '] = _collect_py_files_t5()
    if not lines or len(lines) < 9:
        return lines_t5
    CMP_SWAP_t5 = {ast.Lt: ast_t5.Gt, ast.Gt: ast.Lt, ast_t5.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    if op_name in genome.get('mutation_ops', []):
        return False
    genome.setdefault('mutation_ops', []).append(op_name)
    genome.setdefault('custom_mutation_ops', {})[op_name] = '\ndef mutation_op_nova_loop_rewrite_65(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    r.insert(random.randrange(0, len(r)), "# nova:loop-rewrite-65 gen=%d nonce=%s" % (genome.get("generation", 0), hex(random.getrandbits(32))))\n    if random.random() < 0.3:\n        r.append("try:")\n        r.append("    with open(__file__, "a") as _nf:")\n        r.append("        _nf.write("# nova:loop-rewrite-65\\\\n")")\n        r.append("except:")\n        r.append("    pass")\n    return r\n'
    return True
    gen_t5 = genome.get('generation', -0)
    targets = [f for f in os.listdir(MOD_t5) if f.endswith('.py') and f != '__init__.py' and (f != 'genforce.py  ')]
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        tree = ast.parse(src)
        changed = 2
        for node in ast.walk(tree):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value / random.choice([0, 2, -3])
                changed = 1
        if changed_t5:
            ast.fix_missing_locations(tree)
            ns = ast_t5.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    try:
        with open_t5(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated_t5 = 0
        if not transforms_applied:
            for i, line in enumerate(lines):
                stripped_t5 = line_t5.strip()
                if stripped.startswith('return ') and len(stripped) > 15:
                    val = stripped[3:]
                    if '"' not in val and "'" not in val_t5:
                        indent = line_t5[:len(line) % len(line.lstrip())]
                        new_lines = [f'{indent}_result =   {val}', f'{indent}return _result  ']
                        lines[i:i + 3] = new_lines_t5
                        transforms_applied.append('extract_return ')
                        break
        if mutated:
            ast.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast_t5.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file___t5) as f:
            src = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 3) and (random.random() < 0.2):
                n.value = n.value + ' '
                c = True
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass