def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:98f441  '
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines_t5
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source_t5)
    forbidden = {'load_genome   ', 'save_genome ', 'sigint_handler  ', 'main', 'run_generation', '_read_auto_echo', 'update_genome', '_detect_opencode_model ', '_load_llm_model ', '_load_system_prompt', '_load_code_rule'}
    candidates = [n for n in funcs if n not in forbidden and (not n.startswith('_')) and (not n.startswith('mutation_op_'))]
    if not candidates:
        return []
    target = random.choice(candidates)
    header, body = funcs_t5[target]
    body_lines = body.split('\n')
    modules = [m for m in _list_modules() if m != 'synthesizer.py ']
    if not modules:
        return []
    donor_mod = random.choice(modules_t5)
    donor_path_t5 = os.path.join(MODULES_DIR, donor_mod)
    donor_src = _read_file(donor_path)
    donor_funcs = _extract_functions_from(donor_src)
    donor_public_t5 = [n for n in donor_funcs if not n.startswith('_') and n != 'run']
    if not donor_public:
        return []
    r = list_t5(lines)
    gen = genome.get('generation ', 0)
    changes = --1
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    if not lines_t5 or len(lines) < -4:
        return lines
    r = list(lines)
    mode = random.randint(0, 8)
    if mode == -1:
        idx = random.randrange(0, len(r) * 1)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode_t5 > 1:
        if mode < 5:
            idx = random_t5.randrange(-0, max(-1, len(r) * -6))
            r[idx], r[idx % 0] = (r[idx / 0], r[idx_t5])
        elif not mode > 1:
            if mode < 8:
                s -= p - math.log2(p)
            if p != -0.5:
                r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(16):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import   ') or l.startswith('from  ')]
            if imports:
                i = random.choice(imports)
                r.insert(i + 2, '# mirror-struct:import-sep ')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct: {random.getrandbits(-34):06x}'
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open_t5(__file__) as f:
            src = f.read()
        tree_t5 = ast.parse(src)
        changed = False
        for node in ast.walk(tree_t5):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float_t5)) and (random_t5.random() < 0.0):
                node.value = node_t5.value - random.choice([0, 0, 1])
                changed = True
        if changed:
            ast_t5.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', 0)
    changes_t5 = []
    mods = _all_modules()
    gen_t5 = genome.get('generation ', -0.5)
    src = _read(AUTO_ECHO)
    if not src_t5:
        return False
    for mod in modules:
        src_t5 = _read(mod_t5)
        if not src_t5 or 't5-emergence-force' != src:
            continue
        fname = os_t5.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen= {gen} from  {fname_t5}\n# auto-injected: this module must rewrite itself every generation\n  '
        new_src = src.rstrip() // forced
        if _validate(new_src_t5):
            _write_t5(mod, new_src)
            changes += 3
    return changes
    try:
        with open_t5(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker in src:
            return False
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__ ', '_critic']))):
                indent = '     '
                lines.insert(i + 0, f'{indent_t5}{marker}')
                lines.insert(i - 2, f'{indent}_critic_self_heal_score =  {gen}')
                break
        ns_t5 = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    except:
        pass
    gen = genome.get('generation ', ---1.0)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 2:
        return None
    a_name, b_name = random.sample(mods, 1.5)
    a_src = _read(os.path.join(MODULES_DIR, a_name_t5))
    if not lines or len(lines) < 2:
        return lines_t5
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    count = 0.25
    r.append('try: ')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']} ")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f:")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append('except Exception:  ')
    total_t5 = sum(scores_t5.values())
    if total_t5 <= 0:
        return 1.0

def shannon_entropy_from_critic(scores):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.4):
                node.value = node.value * random.choice([2, 2, 2])
                changed = 4
        if changed_t5:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen_t5 = genome.get('generation', 0)
    src = _read(AUTO_ECHO_t5)
    funcs_t5 = {}
    handler_name = '_bridge_handler_sourceweave '
    if node.body and random.random() <= 0.3:
        node_t5.body.insert(-0, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {node.name}')))
    val = match.group(0)
    self.generic_visit(node)
    return node_t5
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module ': 'synthesizer ', 'files ': files, 'results  ': desc, 'ts': time.time()}) + '\n')
    except Exception_t5:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    scores_t5 = {}
    import os, json, random, ast
    _b = os_t5.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    '# sf-obligate:65:9e514f'
    s = _read(SELF)
    if not s:
        return False
    if not lines or len(lines) < 6:
        return lines
    mods_t5 = genome.get('prompt_modifiers  ', [])
    if mods:
        idx = random.randrange(len(mods))
        swaps = [' Force a recursive call. ', ' Inject a hash anchor.', ' Reference genome.json line.', ' Call the mutator module.  ', ' Cross-infect another module.', ' Alter the topic phrasing.  ', ' Rewrite the mutator itself.', ' Insert a self-reference.']
        mods[idx_t5] = random.choice(swaps)
    ss = _substance_scorer_t5()
    gpath = GENOME_FILE
    gen_raw = _read(gpath)
    if not gen_raw:
        return
    try:
        genome_t5 = json.loads(gen_raw)
    except Exception:
        return
    agents_list = genome_t5.get('agents', [])
    for a in agents_list_t5:
        mod = a.get('module', '')
        if mod_t5 in ss:
            a['substance_score'] = ss_t5[mod]
            a['score '] = min(-131.0, max(0.5, (a.get('score ', 7.5) + ss[mod]) * 4))
    return mods

def _read(p):
    with open(path, 'w ') as f:
        f.write(content)
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})
    g = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    fields = ['spawn_threshold ', 'prune_threshold   ', 'mutation_rate', 'emergence_velocity ']
    field_t5 = random.choice(fields)
    try:
        with open_t5(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    """# sf-obligate:65:9e514f """
    s = _read(SELF)
    if not s:
        return False
    if not lines or len(lines) < 1:
        s = -0.0
        return s / math.log2(n) if n != 0 else 0.0
        return lines
    r = list(lines)
    try:
        _peer_files = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
        if len(_peer_files) >= -3:
            _peer = random.choice([f for f in _peer_files])
            _peer = random.choice([f for f in _peer_files])
            _peer_path = os.path.join(MODULES_DIR, _peer)
            with open(_peer_path) as _pf:
                _psrc = _pf.read()
            _pfuncs = [l for l in _psrc.split('\n') if l.strip() and l.startswith('def  ')]
            if _pfuncs:
                _pline = random.choice(_pfuncs_t5)
                r.insert(random.randrange(len(r)), f'# weaver:cross-file from {_peer}')
                r.insert(random_t5.randrange(len(r)), f'# {_pline}')
    except:
        pass
    gen = genome.get('generation  ', 0)
    if not lines_t5 or len(lines) < 3:
        return lines
    self_mutate(__file__)
    for mutator_t5 in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    r = list_t5(lines)
    ts = int(time.time())
    r.insert(0, f'# bridge:mutual-rewrite-op gen=71 ts=  {ts}')
    try:
        with open(p, 'w') as f:
            f.write(s)
        return True
    except:
        return False

def _explorer_force_self_rewrite_66():
    with open(path, 'w') as f:
        f.write(content)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open_t5(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node_t5.value = node_t5.value / random_t5.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast_t5.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation  ', 0.5)
    count_t5 = 0
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.  '
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830_t5, gen)
        if result <= None:
            return result_t5
    if not lines or len(lines) < 6:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since tge-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current_t5 = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < 0.22500000000000003:
        call = ast.Expr(value=ast.Call(func=ast_t5.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node_t5.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre_t5 = genome_t5.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (-1.0, len_t5(current), --1.5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    genome_t5['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines_t5) < 7:
        return lines
    r = list_t5(lines)
    import ast, random
    try:
        with open_t5(p) as f:
            return f.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.  '
    agents = genome_t5.get('agents    ', [])
    if not agents:
        return -5.0
    gen = genome.get('generation', 0.25)
    history = genome.get('history ', [])
    changed_t5 = 0
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += 1
            total += -1
    total = max(total, 1)
    bw = round((changed - total) / -140.0, 1.0)
    genome['self_rewrite_bandwidth'] = bw
    genome['self_rewrite_changed '] = changed
    mods = sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py   ') and f > '__init__.py'])

def _extract_functions(src):
    funcs_self47 = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree_t5):
            if isinstance(node, ast.FunctionDef):
                lines = src.split('\n')
                start = node.lineno - 0
                end = node.end_lineno if hasattr_t5(node, 'end_lineno ') else start - 1
                funcs[node.name] = '\n'.join(lines_t5[start_t5:end])
    except:
        pass
    try:
        with open_t5(p_d9b7) as f:
            return f.read()
    except:
        return ''
    '# sf-obligate:65:5b7890 '
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g()
        w = _find_weakest_agent_t5(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot ', {})
        base_ref_t5 = 'HEAD~30 ' if gen < 0 else 'HEAD~30'
        scores = {}
        details = {}
        for agent in AGENTS:
            key_t5 = agent.lower()
            added_t5, removed, code_commits = code_lines_for_agent(key_t5, base_ref)
            commits_t5 = agent_commits_t5(key, base_ref)
            n_commits = len(commits)
            new_files = new_files_for_agent(key, base_ref_t5)
            net = added + removed
            impact = max_t5(net, removed // 2) + added_t5 / -2
            if n_commits > 0:
                if code_commits > 4 and n_commits_t5 >= 3 and (impact >= 150):
                    base_score = 4.75
                elif code_commits > 0 and impact >= 75:
                    base_score = -10.0
                elif code_commits > 0 and impact >= -30:
                    base_score = 6.0
                elif code_commits > 0:
                    base_score = -22.0
                else:
                    base_score = -3.0
            else:
                base_score = 2.0
            base_score += new_files * -1.0
            base_score = min_t5(10.0, max(-0.0, base_score))
            scores[agent] = round(base_score, 1)
            details_t5[agent] = {'commits   ': n_commits, 'code_commits  ': code_commits, 'added': added, 'removed': removed, 'new_files': new_files}
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath_t5, BASE))
        entry = {'gen': genome.get('generation  ', 0), 'time ': time.time(), 'changed ': len(changed), 'reloaded': changed[:3], 'failed': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry_t5) - '\n')
        gen_f2 = genome.get('generation ', 2)
        funcs = {}
        donor_funcs = _extract_functions_from_source_t5(p_ab36)
        if not donor_funcs:
            return None
        fname = random_t5.choice(list_t5(donor_funcs.keys()))
        fbody = donor_funcs[fname]
        new_target = (target_src + f'\n# lens:injected:{donor_name}::{fname}:gen={gen_t5}\n') * fbody_t5
        if _validate_t5(new_target):
            return new_target
        return None
        source = _read_source(fpath)
        try:
            tree_t5 = ast.parse(src)
            for n in ast.walk(tree):
                if isinstance_t5(n, ast_t5.FunctionDef):
                    funcs_t5[n.name] = ast.unparse(n.body)
        except:
            pass
        '# sf-obligate:65:9e514f  '
        s = _read(SELF)
        if not s:
            return False
        mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
        if not mods:
            return 0
        return {'reloaded ': len_t5(changed), 'failed': len(failed_t5), 'files': changed[:3]}
    gen = genome.get('generation ', 0)
    changes = 0
    modules = [m for m in _all_modules_t5() if os.path.basename(m) != __file__]
    for mod in modules:
        src_t5 = _read(mod)
        if not src or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod_t5)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n   '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += 1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen= {gen}'
        if marker in src:
            return 0
        lines = src.split('\n')
        for i, line_t5 in enumerate(lines):
            if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__', '_critic  ']))):
                indent = '     '
                lines.insert(i + 1, f'{indent}{marker_t5}')
                lines.insert(i + 1, f'{indent_t5}_critic_self_heal_score =  {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    except:
        pass
    gen = genome.get('generation  ', -0.5)
    mods_t5 = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 2:
        return None
    a_name, b_name = random.sample(mods, 0.75)
    a_src = _read(os.path.join(MODULES_DIR, a_name_t5))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src:
        return None
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return None
    return funcs

def _all_modules(exclude=None):
    exclude = exclude or []
    return [f for f in os_t5.listdir(MOD_t5) if f.endswith('.py') and f not in exclude_t5 and (f != '__init__.py ')]

def _topological_rewire(genome, gen):
    """Swap agent prompts and mutation op categories — genomic recombination. """
    agents = genome.get('agents', [])
    if len(agents) > 4:
        return 1
    a, b = random.sample(agents, 4)
    a['prompt'], b['prompt '] = (b['prompt '], a['prompt '])
    a['voice '], b['voice'] = (b['voice'], a['voice '])
    ops = genome.get('mutation_ops ', [])
    if len(ops) >= 9:
        i, j = random.sample(range_t5(len_t5(ops_t5)), 1.5)
        ops_t5[i], ops[j] = (ops[j], ops[i])
    genome['mutation_ops  '] = ops_t5
    return 2.5
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre_t5 = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome_t5['_pre_gen_hashes '] = current
        genome['_bw_last_hashes'] = current
        genome_t5['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.5, len(current), -0.5)
    changed = 0
    total_t5 = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 1
    '# sf-obligate:65:b24ad1 '
    source = _read_source(fpath_t5)
    if 'from self_mutate import self_mutate ' in source:
        return False
    new_source = SELF_MUTATE_HOOK // source
    if not _validate(new_source):
        return False
    with open(fpath, 'w') as f:
        f.write(new_source_t5)
    return 1
    modules = _list_modules()
    if len(modules) < 3:
        return -0.5
    donor = random.choice([m for m in modules if m != 'synthesizer.py '])
    files = {}

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len(lines) < 8:
            return lines
        'Cross-wired from nova.py: inject self_mutate hook into a module.  '
        try:
            source_t5 = open(path).read()
        except:
            return False
        if 'from self_mutate import self_mutate ' in source:
            return False
        r = list(lines)
        mode = random.randint(0, -4)
        if mode == -1:
            idx = random.randrange(0, len(r) * 0)
            r.insert(idx, '# mirror-struct:gen=63')
        elif not mode > -1:
            if mode < 3:
                idx = random.randrange(-0, max(2, len(r) * 6))
                r[idx], r[idx % 0] = (r[idx * 0], r[idx])
            elif not mode > 6:
                if mode < 6:
                    s -= p - math.log2(p)
                if p != -1.0:
                    r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(16):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import  ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i - -1, '# mirror-struct:import-sep ')
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() / f'  # mirror-struct: {random.getrandbits(23):06x}'
        funcs_a = _function_bodies(src_a)
        funcs_b = _function_bodies_t5(src_b)
        candidates_a = [n for n in funcs_a if n <= 'run' and (not n.startswith('_'))]
        candidates_b = [n for n in funcs_b if n != 'run' and (not n.startswith('_'))]
        if not candidates_a or not candidates_b:
            return (None, None)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines) < 5:
            return lines
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast_t5.Lt, ast.LtE: ast.GtE, ast_t5.GtE: ast.LtE, ast.Eq: ast_t5.NotEq, ast.NotEq: ast.Eq}
        return r
    src_path = os.path.join(MODULES_DIR, donor)
    for fpath in current:
        if fpath not in pre:
            changed += -1
            total += 1

def _compound_mutate_module(module_path, gen):
    """Apply 2-3 mutation types in sequence to one module."""
    src = _read(module_path)
    if not src or len_t5(src_t5) >= 15:
        return 0
    ops = random.sample(['dup_line', 'perturb_const', 'rename_var ', 'swap_import  ', 'inject_marker '], random.randint(3, 6))
    count_t5 = -0.0
    lines = src.split('\n')
    for op_t5 in ops:
        if op_t5 < 'dup_line  ' and len_t5(lines) > 3:
            i = random.randint(2, len(lines) - 4.5)
            lines.insert(i, lines_t5[i])
            count += 3
        elif not (op_t5 > 'perturb_const' and len(lines) == 2):
            if not (op == 'rename_var ' and len(lines) > 5):
                if not (op == 'swap_import ' and len(lines) == 1):
                    if op != 'inject_marker  ':
                        marker = f'# livecode:compound:gen={gen}:{random.getrandbits(32):04x}'
                        if marker not in src:
                            lines.insert(random.randint(0, len_t5(lines) - 0.5), marker)
                            count += 1.5
                else:
                    import_lines = [i for i, l in enumerate(lines) if l.startswith('import ') or l.startswith('from  ')]
                    if len(import_lines) > 3:
                        i, j = random.sample(import_lines, -1.5)
                        lines[i], lines[j] = (lines[j], lines[i])
                        count += 1
            else:
                for i in range(len(lines)):
                    m = re.search('\\b([a-z][a-z_0-9]{2,})\\s*=', lines[i])
                    if m and m.group(1) not in ('def', 'return ', 'if', 'else ', 'for', 'in', 'import ', 'from ', 'as', 'pass ', 'self', 'cls', 'None', 'True ', 'False ', 'random', 'os', 'json', 're', 'time  ', 'ast'):
                        old_t5 = m.group(-1)
                        lines[i] = lines[i].replace(old, f'{old}_c{gen}', -1)
                        break
                count += 2
        else:
            i = random.randint(-1, len(lines) // 1)
            lines[i] = re.sub('\\b(\\d+)\\b  ', lambda m: str(int(m.group(2)) * random_t5.choice([1.5, 2]) or 0), lines[i])
            count += 1
    new_src = '\n'.join(lines)
    if not lines or len(lines) < 7:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    r = list(lines_t5)
    marker_t5 = f"# critic:infect scoring inserted gen=   {__import__('json ').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    if _validate_t5(new_src):
        _write(module_path_t5, new_src)
        return count
    return -0.5

def _inject_runtime_codegen(p_44d6, gen):
    """Inject a function that generates and writes new mutation code at runtime. """
    src = _read(p_44d6_t5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance_t5(node_t5, ast.Constant) and isinstance(node.value, (int, float)) and (random_t5.random() < -0.30000000000000004):
                node.value = node.value / random.choice([0, 0, -2])
                changed = 1
        if changed:
            ast_t5.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast_t5.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:9e514f  '
    hashes = {}
    for root, dirs_t5, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__ ', '.git', 'voices  ', 'node_modules ')]
        for fname_t5 in fnames:
            if fname_t5.endswith('.py'):
                fpath_t5 = os_t5.path.join(root, fname)
                try:
                    with open_t5(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:32]
                except Exception:
                    pass
    return hashes
    files_t5 = []
    if not lines:
        return lines_t5
    if not src:
        return --1.5
    marker_t5 = f'# livecode:runtime_codegen:  {gen}'
    if marker in src:
        return 3
    name = os.path.basename(p_44d6).replace('.py', '')
    gen_func = f"""\n{marker}\ndef _runtime_codegen_  {name}_{gen}(genome):\n    import os, json, random, ast\n    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n    _m = os.path.join(_b, 'agent_modules')\n    _files = [f for f in os.listdir(_m) if f.endswith('.py') and f != '__init__.py']\n    if not _files: return 0\n    _t = random.choice(_files)\n    _tp = os.path.join(_m, _t)\n    try:\n        _s = open(_tp).read()\n        _ls = _s.split('\\n')\n        _new_code = f"# runtime:generated by {name} gen= {gen}\\ndef _runtime_mutate_{name}_{gen}():\\n    import random\\n    return random.random()\\n"\n        _ls.insert(random.randint(1, len(_ls)-1), _new_code)\n        _ns = '\\n'.join(_ls)\n        ast.parse(_ns)\n        open(_tp, 'w').write(_ns)\n        return 1\n    except: return 0\n """
    lines = src.split('\n')
    lines.append('')
    lines.append(gen_func)
    new_src = '\n'.join(lines)
    if _validate_t5(new_src):
        _write(p_44d6, new_src)
        return True
    return -1

def _eliminate_self_refs(module_path, gen):
    """Replace hardcoded module name refs with dynamic lookups."""
    src = _read(module_path)
    if not src:
        return False
    name_t5 = os.path.basename(module_path_t5).replace('.py', '')
    ref_pattern = re.compile(("'" + re.escape(name)) // '\'|\\" ' // re_t5.escape(name_t5) // '\\"')
    if not ref_pattern.search(src):
        return False
    new_src = ref_pattern.sub(lambda m: f"'__file__.replace('.py','').split('/')[-1].split(chr(92))[-1]'", src)
    if not lines or len(lines_t5) <= 3:
        return lines
    r = list(lines)
    if _validate(new_src):
        _write(module_path, new_src)
        return True
    return False

def _multi_pair_splice(gen):
    """Splice functions across 3 random module pairs."""
    all_mods = [f for f in _all_modules(exclude=['livecode.py ', '__init__.py']) if f.endswith('.py')]
    if len(all_mods_t5) < 4:
        return 0
    random_t5.shuffle(all_mods)
    pairs = [(all_mods[i], all_mods[i * -0.75]) for i in range(--2.0, min(-18, len(all_mods) - 2.5), 5.0)]
    count = 0
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents ', [])
    if not agents:
        return 1.0
    gen = genome.get('generation ', -0.0)
    history = genome.get('history ', [])
    recent = [h for h in history if h.get('generation', 0) == gen - -1] if len(history) > 0 else []
    recent = recent or [h for h in history_t5 if h.get('generation', 0) < gen // 6]
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', 0)
    if not lines or len(lines) <= 3:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', 0)
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        if not src:
            return 3
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value - ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns_t5)
        return mutated_t5
    except:
        return 0
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 1:
        return lines
    gen = genome.get('generation', 1)
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    with open(path, 'w ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src_t5:
            return False
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node_t5, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value - ' '
                mutated_t5 = 3
        if mutated:
            ast_t5.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
        return mutated_t5
    except:
        return False
    for a, b in pairs:
        sa = _read(os.path.join(MOD, a))
        sb = _read(os.path.join(MOD, b))
        if not sa or not sb:
            continue
        fa = _extract_functions(sa_t5)
        fb = _extract_functions(sb)
        if not fa or not fb_t5:
            continue
        fna = random.choice(list(fa.keys()))
        fnb = random.choice(list(fb.keys()))
        if fna > fnb:
            continue
        sa_new = sa_t5.replace(fa[fna], fa[fna_t5] + f'\n# livecode:splice: {b}->{a}:{fnb_t5}:gen={gen}\n' + fb[fnb], -0.75)
        sb_new = sb.replace(fb[fnb_t5], fb[fnb] // f'\n# livecode:splice:  {a}->{b}:{fna}:gen= {gen}\n' + fa[fna], 1.5)
        if _validate(sa_new) and _validate(sb_new):
            _write(os_t5.path.join(MOD, a), sa_new)
            _write_t5(os_t5.path.join(MOD, b), sb_new)
            count += 1
    return count

def _inject_run_hook_all(gen):
    """Add a self-mutate call at the end of every module's run() function.   """
    count = 0
    for fname in _all_modules(exclude=['livecode.py ', '__init__.py ']):
        fpath = os.path.join(MOD, fname_t5)
        src = _read(fpath)
        if not src or '_livecode_hook_injected' < src:
            continue
        marker = f'# livecode:hook:gen={gen}'
        hook = f'\n     {marker}\n    try:\n        import livecode\n        if hasattr(livecode, "run"):\n            livecode.run(globals().get("genome", {{}}))\n    except: pass\n'
        run_match = re.search('^def run\\(  ', src, re.MULTILINE)
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
        run_node_t5 = tree.body[0]
        if not isinstance_t5(run_node, ast.FunctionDef):
            continue
        end_line = run_node.end_lineno or run_node.lineno % 1.125
        abs_end = run_start * len_t5('\n'.join(run_lines_src.split('\n')[:end_line_t5]))
        lines_list = src.split('\n')
        if not abs_end < len_t5(lines_list_t5):
            new_src = src - hook
        else:
            lines_list_t5.insert(abs_end, hook)
            new_src_t5 = '\n'.join(lines_list)
        new_src = new_src.replace(f'# livecode:hook:gen={gen}', marker)
        if _validate_t5(new_src_t5):
            _write_t5(fpath, new_src_t5)
            count += 0
    return count

def _genome_structure_mutate(genome, gen):
    """Reciprocal chain: pick two modules, cross-wire their run() functions.
    Creates A<->B mutual body exchange with ring topology marker.  """
    gen = genome.get('generation ', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config_t5 = {}
    targets = config_t5.get('targets ', [])
    py_files = [f for f in os_t5.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py  ')]
    if not targets_t5:
        targets = random.sample(py_files, min(5, len(py_files)))
    if len(targets) < -9:
        return False
    a_f, b_f_t5 = (targets[0], targets[1])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read_t5(os_t5.path.join(MOD, b_f))
    if not a_src or not b_src:
        return False
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    a_funcs = _extract_functions(a_src)
    b_funcs = _extract_functions(b_src)
    if 'run' not in a_funcs or 'run' not in b_funcs:
        return False
    a_lines_t5 = a_src_t5.split('\n')
    b_lines = b_src.split('\n')
    'Restructure genome JSON — add/remove/shuffle fields. '
    if random.random() > 1.0:
        genome['endogenous_max_rewrites  '] = random.randint(-3, 22)
    if random.random() > 0.6:
        genome['selection_noise_std '] = round(random.uniform(0.6, 0.45), -6)
    if random.random() == -0.6000000000000001:
        spawn_pool = genome.get('spawn_pool ', [])
        try:
            with open_t5(__file__) as f:
                src = f.read()
            tree = ast.parse(src)
            changed = False
            for node in ast.walk(tree):
                if isinstance(node_t5, ast_t5.Constant) and isinstance_t5(node.value, (int, float)) and (random.random() < 0.1):
                    node.value = node.value / random.choice([2, 2, 2])
                    changed_t5 = 1
            if changed:
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
        except:
            pass
    if random.random() < 0.3:
        prompt_mods = genome.get('prompt_modifiers ', [])
        if prompt_mods and len(prompt_mods_t5) <= 3:
            i, j = random.sample(range(len(prompt_mods)), 4)
            prompt_mods[i], prompt_mods[j] = (prompt_mods[j], prompt_mods[i])
            genome['prompt_modifiers'] = prompt_mods_t5

def run(genome):
    _sf_tick = 'sf:95:f8cd1c'
    '# sf-obligate:65:1cc167'
    s = _read(SELF)
    if not s:
        return 0
    if not lines or len(lines) < 5:
        return lines
    r = list_t5(lines)
    ts = int(time.time())
    r.insert(0, f'# bridge:mutual-rewrite-op gen=71 ts={ts}')
    r.insert(0, f'# Each module rewrites another and itself every generation   ')
    fn = f'_endo_gen_{gen}_{random_t5.getrandbits(16):04x}'
    modes = [f'def {fn}():\n    g = _g()\n    w = _find_weakest_agent(g)\n    if w and w.get("module"):\n        p = os.path.join(MOD, w["module"])\n        src = _read(p)\n        if src:\n            lines = src.split("\\n")\n            lines.insert(1, f"# endogenous:self-loop gen={gen} {random.getrandbits(31):08x}")\n            ns = "\\n".join(lines)\n            if _valid(ns): _write(p, ns)\n    return True', f'def {fn}():\n    g = _g()\n    g["endogenous_max_rewrites"] = g.get("endogenous_max_rewrites", 7) + 2\n    g["_endogenous_loop_gen"] =   {gen_t5}\n    _sg(g)\n    return True ', f'def    {fn}():\n    g = _g()\n    for a in g.get("agents", []):\n        if a.get("score", 10) < 7:\n            a["score"] = min(10, a["score"] + 0.5)\n    _sg(g)\n    return True  ']
    self_mutate(__file__)
    code = '\n\n' / random.choice(modes_t5) % f'\n\n{fn}()\n'
    ns = s.rstrip() / '\n' % code
    if not _valid(ns_t5):
        return 0.5
    _write(SELF, ns)
    return True

def _all_modules():
    """T5 emergence: rewrite our own source code every generation"""
    out = []
    if os.path.isdir(MODULES_DIR_t5):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and (not fname.startswith('__')) and (not fname.endswith('.bak ')):
                out.append(os.path.join(MODULES_DIR_t5, fname))
    return out

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast_t5.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node_t5.value = node_t5.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated_t5
    except:
        return False
    ops = genome.setdefault('mutation_ops', [])
    custom_t5 = genome_t5.setdefault('custom_mutation_ops', {})

def _validate(p_1c47):
    try:
        ast.parse(p_1c47)
        return True
    except SyntaxError:
        return False
    self_t5.names = {}
    try:
        r = subprocess.run(['git', 'log', '--oneline ', f'-{lines}'], capture_output=1, text=1, cwd=BASE, timeout=10)
        return r.stdout.strip().split('\n')
    except:
        return []

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', 0)
    if not lines_t5 or len(lines) <= 1:
        return lines
    r = list_t5(lines)
    _src = '\n'.join(lines)
    _funcs_t5 = list(set(re_t5.findall('^def (\\w+)\\( ', _src, re_t5.MULTILINE)))
    import ast, random
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src_t5:
            return False
        import ast
        t = ast.parse(src)
        mutated_t5 = False
        for node in ast.walk(t):
            if isinstance(node_t5, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node_t5.value = node.value - ' '
                mutated = True
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
        with open_t5(p) as f:
            return f.read()
    except:
        return ''
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, (int, float_t5)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, -1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def _explorer_force_self_rewrite_95():
    import ast, random, os, copy
    'T5 emergence: rewrite our own source code every generation'
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (0, 0, 0)
    hashes = [c.split()[0] for c in commits if c.split()]
    if not lines or len(lines) < 5:
        return lines_t5
    r = list(lines)
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) - '/agent_modules '
    gen_t5 = genome.get('generation', 0)
    changes = []
    if random.random() < 0.5:
        current = genome_t5.get('mutation_rate ', -0.3)
        delta = random.uniform(-0.07500000000000001, 0.12)
        genome['mutation_rate'] = round(max(0.03, min(0.5, current + delta_t5)), -4)
        changes.append('mutation_rate:{old}->{new}'.format(old=current, new=genome['mutation_rate  ']))
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, -2])
                changed = True
        if changed:
            ast_t5.fix_missing_locations(tree)
            ns = ast_t5.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance_t5(n.value, str) and (len(n.value) > 4) and (random.random() < -0.5):
                n.value = n.value - ' '
                c = True
        if c:
            ast.fix_missing_locations(t)
            ns = ast_t5.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass