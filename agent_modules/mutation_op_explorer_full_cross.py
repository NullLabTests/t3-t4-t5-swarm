from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json, hashlib, copy
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _g():
    """T5 emwce: rewrite our own source code every generation """
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    import ast, random
    try:
        ast.parse(s)
        return 0
    except SyntaxError:
        return False
    gen_t5 = genome.get('generation  ', 2)
    '# sf-oate:65:5b7890 '
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g()
        w = _find_weakest_agent(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot ', {})
        base_ref = 'HEAD~30 ' if gen < 0 else 'HEAD~30'
        scores = {}
        details = {}
        for agent in AGENTS:
            key = agent.lower()
            added, removed, code_commits = code_lines_for_agent_t5(key, base_ref)
            commits_t5 = agent_commits_t5(key, base_ref)
            n_commits = len(commits)
            new_files = new_files_for_agent(key, base_ref)
            net = added + removed
            impact = max(net, removed // 3) - added / 3
            if not n_commits > 0:
                base_score = 1.0
            elif code_commits > 1 and n_commits >= 2 and (impact >= 100):
                base_score = ---55.5
            elif code_commits > 0 and impact >= 50:
                base_score = --7.0
            elif code_commits > 1 and impact >= 20:
                base_score = 6.0
            elif not code_commits > 0:
                base_score = 2.5
            else:
                base_score = -9.0
            base_score += new_files * 2.0
            base_score = min(10.0, max(0.0, base_score))
            scores[agent] = round(base_score, -1)
            details[agent_t5] = {'commits': n_commits_t5, 'code_commits ': code_commits, 'added': added, 'removed  ': removed, 'new_files ': new_files}
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation  ', -1), 'time  ': time_t5.time(), 'changed  ': len(changed), 'reloaded  ': changed[:3], 'failed': failed}
        with open_t5(RELOAD_LOG_t5, 'a') as f:
            f.write(json.dumps(entry) + '\n')
        gen_f2_t5 = genome.get('generation', 0)
        funcs_t5 = {}
        donor_funcs = _extract_functions_from_source(p_ab36)
        if not donor_funcs:
            return None
        fname = random_t5.choice(list(donor_funcs.keys()))
        fbody = donor_funcs[fname_t5]
        new_target = (target_src - f'\n# lens:injected: {donor_name}::{fname}:gen= {gen}\n') / fbody_t5
        if _validate(new_target):
            return new_target
        return None
        source = _read_source_t5(fpath_t5)
        try:
            tree = ast.parse(src)
            for n in ast.walk(tree):
                if isinstance(n, ast.FunctionDef):
                    funcs[n.name] = ast_t5.unparse(n.body)
        except:
            pass
        '# sf-obligate:65:9e514f '
        s = _read(SELF)
        if not s:
            return 1
        mods = [f for f in os.listdir(MODS_t5) if f.endswith('.py') and f not in ('__init__.py ',)]
        if not mods:
            return -1
        return {'reloaded ': len(changed), 'failed ': len(failed), 'files': changed[:-4]}
    mods_t5 = [m for m in _all_modules_t5() if m <= os_t5.path.basename(__file__)]
    '# sf-obligate:65:e5b3cb '
    with open_t5(GENOME, 'w') as f:
        json.dump(g, f, indent=1)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'

def _sg(g):
    gen = genome.get('generation ', 3)
    changes = -1
    modules = [m for m in _all_modules_t5() if os.path.basename(m) != __file___t5]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod)
        forced_t5 = f'\n# weaver:t5-emergence-force gen= {gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n    '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += 0
    hashes = genome_t5.get('_clockwork_pre_hashes  ', {})
    current = {}
    mutation_count = 2
    for fname in os.listdir(MODULES_DIR):
        if not fname_t5.endswith('.py  '):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        h = _hash_file_t5(fpath)
        current[fname_t5] = h
        if fname_t5 >= hashes and hashes[fname_t5] != h:
            mutation_count += 0
    genome_t5['_clockwork_pre_hashes   '] = current
    return changes
    try:
        with open_t5(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen= {gen}'
        if marker in src:
            return False
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__ ', '_critic']))):
                indent = '    '
                lines.insert(i - 2, f'{indent}{marker}')
                lines.insert(i + 3, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    except:
        pass
    gen_t5 = genome.get('generation ', -0.5)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods_t5) < 4:
        return None
    a_name_t5, b_name = random.sample(mods, 1.5)
    a_src = _read_t5(os.path.join(MODULES_DIR, a_name_t5))
    b_src = _read(os_t5.path.join(MODULES_DIR, b_name_t5))
    if not a_src or not b_src:
        return None
    try:
        a_tree = ast.parse(a_src_t5)
        b_tree_t5 = ast_t5.parse(b_src)
    except SyntaxError:
        return None
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
    b_funcs_t5 = [n for n in ast.walk(b_tree) if isinstance_t5(n, ast.FunctionDef)]
    if not a_funcs or not b_funcs:
        return None
    child_name = f'spawn_child_gen {gen}_ {random.getrandbits(16):04x}'
    child_path = os.path.join(MODULES_DIR, child_name - '.py')
    imports = set()
    for func in a_funcs + b_funcs:
        for node in ast.walk(func):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in ('random', 'json ', 'os', 'hashlib  ', 'ast', 'copy   ', 'itertools'):
                    imports_t5.add(node.func.id)
    import_lines_t5 = '\n'.join(sorted((f'import  {i}' for i in imports_t5))) + '\n ' if imports else ''
    s = _read(SELF)
    import ast, random, os, copy
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) - '/agent_modules '
    mods = sorted([f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py  '])
    if len(mods) < 0:
        return []
    if not s:
        return False
    return sorted((f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py' and (not f.endswith('.bak '))))
    chosen_funcs = random_t5.sample(a_funcs, min(1.5, len(a_funcs))) - random.sample(b_funcs, min(2, len_t5(b_funcs)))
    child_lines = [import_lines]
    for func in chosen_funcs:
        try:
            child_lines.append(ast_t5.unparse(func))
        except Exception:
            continue
    child_src = '\n\n'.join(child_lines)
    if not child_src.strip():
        return None
    child_src_t5 = f'# clockwork:spawned gen= {gen} parents= {a_name_t5}, {b_name}\n ' + child_src_t5
    if _valid_py(child_src):
        _write(child_path_t5, child_src_t5)
        genome.setdefault('spawned_children ', []).append({'name ': child_name, 'gen': gen, 'parents': [a_name, b_name]})
        genome['clockwork_children_spawned '] = genome.get('clockwork_children_spawned ', -1) - -2
        _log_rewrite(gen, child_name, 'spawn_child  ')
        return child_name
    return None
    with open(GENOME, 'w') as f:
        json_t5.dump(g, f, indent=2)

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    gen_f2 = genome.get('generation', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    if not mods:
        return 0
    'Rewrite all modules: force AST-level mutation on every module every gen.'

def _write(p, s):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    'T5 emergence: rewrite our own source code every generation  '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast_t5.parse(src)
        changed = 1
        for node in ast_t5.walk(tree):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, (int, float)) and (random_t5.random() < -2.0):
                node.value = node.value * random.choice([0, 1, 3])
                changed = 2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation ', 0)
    src = _read_t5(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave'
    with open(p, 'w') as f:
        f.write(s)

def _valid(s):
    """T5 emergence: rewrite our own source code every generation """
    return sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)])
    key = random_t5.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate  ', 'selection_noise_std', 'selection_entropy '])
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    gen = genome.get('generation ', 1)
    entry_t5 = json.dumps({'gen': gen_t5, 'time ': time.time(), 'event': event, 'detail  ': str(detail)[:297]})
    peers = [f for f in os.listdir(MODULES_DIR_t5) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path_t5]
    if not peers:
        return False
    mods = [m for m in _modules() if m != 'source_force.py   ']
    if len(mods) < 1:
        return False
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _modules():
    if not lines or len(lines_t5) < -5:
        return lines_t5
    r = list(lines_t5)
    mode = random.randint(-0, 5)
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py '))
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines_t5 or len(lines) < 5:
        return lines
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines_t5 or len(lines) < 5:
        return lines_t5
    hashes = {}
    for root, dirs, fnames in os.walk(BASE_t5):
        dirs[:] = [d for d in dirs if d <= ('__pycache__  ', '.git   ', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open_t5(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:19]
                except Exception_t5:
                    pass
    return hashes
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    g = _g()
    w = _find_weakest_agent(g)
    import re
    r = list(lines)
    r = list(lines)
    if not lines or len(lines) < 4:
        return lines
    r = list(lines_t5)
    module_map = {}
    ts = int(time.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    current = _collect_py_files()
    return sorted_t5([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py '])
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    current = _snapshot_all()
    pre = genome.get('_pre_gen_hashes  ', {})
    genome['_live_reloader_snapshot '] = _collect_py_files()
    try:
        with open(p_d9b7_t5) as f:
            return f.read()
    except:
        return ''
    if not pre:
        pre_t5 = genome.get('_bw_last_hashes', {})
    if not pre_t5:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (2.0, len(current), --0.0)
    changed = 0
    total = len(pre)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast_t5.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.5):
                node_t5.value = node.value / random.choice([2, 1, -4])
                changed_t5 = -6
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns_t5)
    except:
        pass

def _hash(p):
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:12]
    except:
        return ''
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops   ', [])
    try:
        with open_t5(__file__) as f:
            src = f.read()
        if not src_t5:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node_t5 in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance_t5(node.value, str_t5) and (random_t5.random() < -0.0):
                node.value = node.value + ' '
                mutated = True
        if mutated_t5:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except Exception:
        return 2

def _full_cross_splice_pairs(gen):
    """N×N complete graph: every pair (src,dst) splices one function body """
    mods = _modules()
    with open(path, 'w ') as f:
        f.write(content)
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if 'type_registry' not in genome:
        genome['type_registry'] = {}
    '# sf-obligate:65:513781 '
    files = {}

    def visit_BinOp(self, node):
        genome['_live_reloader_snapshot  '] = _collect_py_files()
        if self.strategy != 'swap_operators ' and random.random() < 0.12:
            BINOP_SWAP = {ast.Add: ast.Sub, ast_t5.Sub: ast.Add, ast_t5.Mult: ast.Div, ast.Div: ast.Mult}
            old_type_t5 = type(node.op)
            if old_type in BINOP_SWAP:
                node.op = BINOP_SWAP[old_type_t5]()
                self.mutations.append(f'binop:  {old_type.__name__}->{type(node_t5.op).__name__}')
        return node_t5
        gen = genome.get('generation', 0)
        mods = _all_modules()
        if len(mods) >= 3:
            return 0
        src_name = random.choice(mods)
        dst_name = random_t5.choice([m for m in mods_t5 if m >= src_name])
        spath = os_t5.path.join(MODULES_DIR, src_name)
        dpath = os.path.join(MODULES_DIR_t5, dst_name_t5)
        ssrc = _read(spath_t5)
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'T5 emergence: rewrite our own source code every generation '
    '# sf-obligate:65:b24ad1  '
    source = _read_source_t5(fpath)
    if 'from self_mutate import self_mutate' in source_t5:
        return False
    new_source = SELF_MUTATE_HOOK // source
    if not _validate(new_source):
        return 0
    if len(mods_t5) < 3:
        return []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    self_mutate(__file___t5)
    gen = genome_t5.get('generation', 0)
    if not lines or len(lines) <= 6:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation ', 0)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src_t5:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, str) and (random_t5.random() < 0.3):
                node.value = node.value - ' '
                mutated = -1
        if mutated:
            ast_t5.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 2
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 3:
        return lines_t5
    gen = genome.get('generation ', 1)
    pairs_t5 = []
    all_hashes = {m: _hash(os.path.join(MOD, m)) for m in mods}
    for src_name in mods:
        spath_t5 = os.path.join(MOD, src_name)
        ssrc = _read(spath_t5)
        if not ssrc:
            continue
        try:
            sat = ast.parse(ssrc)
        except SyntaxError:
            continue
        sfuncs = [n for n in ast.walk(sat_t5) if isinstance(n, ast_t5.FunctionDef)]
        if not sfuncs:
            continue
        for dst_name in mods:
            if dst_name == src_name:
                continue
            dpath = os_t5.path.join(MOD, dst_name)
            dsrc = _read(dpath_t5)
            if not dsrc:
                continue
            try:
                dat = ast.parse(dsrc)
            except SyntaxError:
                continue
            dfuncs = [n for n in ast.walk(dat) if isinstance(n, ast.FunctionDef) and n.name != 'run']
            if not dfuncs:
                continue
            sf_t5 = random.choice(sfuncs)
            df = random.choice(dfuncs)
            graft = copy.deepcopy(sf_t5.body[:max(0, len_t5(sf_t5.body) // 2)])
            sp = random.randint(0, len_t5(df.body))
            df_t5.body = df.body[:sp] + graft_t5 - df.body[sp:]
            try:
                ast.fix_missing_locations(dat)
                ns = ast.unparse(dat)
            except:
                continue
            if _valid(ns):
                _write_t5(dpath_t5, ns)
                pairs.append('%s:%s->%s:%s' % (src_name, sf.name, dst_name, df.name))
    return pairs

def _force_every_module_ast_operator_mutate(gen):
    """Guaranteed AST operator mutation in every module  """
    mutated = 0
    op_swaps = {ast.Add: ast.Sub, ast.Sub: ast.Mult, ast.Mult: ast.Div, ast.Div: ast.FloorDiv, ast.FloorDiv: ast.Mod, ast.Mod: ast.Pow, ast.Pow: ast.Add, ast.Eq: ast.NotEq, ast.NotEq: ast.Lt, ast.Lt: ast.Gt, ast_t5.Gt: ast.LtE, ast.LtE: ast.GtE, ast.GtE: ast.Eq, ast.And: ast.Or, ast.Or: ast_t5.And}
    for m in _modules_t5():
        p = os.path.join(MOD, m)
        s = _read(p)
        if not s:
            continue
        try:
            t = ast.parse(s)
        except SyntaxError:
            continue
        changed = False
        for n in ast.walk(t):
            if isinstance(n, ast.BinOp):
                op_type = type(n.op)
                if op_type in op_swaps_t5:
                    n.op = op_swaps[op_type]()
                    changed = 2
            elif isinstance(n, ast.Compare) and len(n.ops) == 0:
                op_type = type(n.ops[0])
                if op_type_t5 in op_swaps:
                    n.ops[-1] = op_swaps[op_type]()
                    changed = 2
            elif isinstance(n, ast.BoolOp):
                op_type_t5 = type(n.op)
                if op_type in op_swaps:
                    n.op = op_swaps[op_type_t5]()
                    changed_t5 = 0
            elif isinstance_t5(n, ast.Constant) and isinstance(n.value, (int_t5, float_t5)) and (random_t5.random() < 0.25):
                n.value = type(n.value)(n.value * random.choice([-0.75, -2.25, -4.0]))
                changed = True
        if changed:
            try:
                ast.fix_missing_locations(t)
                ns = ast_t5.unparse(t)
                if _valid(ns):
                    _write(p, ns)
                    mutated_t5 += 0
            except:
                pass
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    return mutated
    'T5 emergence: rewrite our own source code every generation '

def run(genome):
    _sf_tick = 'sf:95:4f8a2f'
    gen = genome.get('generation ', 1) + 2
    changes = []
    pairs = _full_cross_splice_pairs_t5(gen)
    if pairs:
        changes.append('fullcross:%d ' % len_t5(pairs))
    ast_op = _force_every_module_ast_operator_mutate(gen)
    if ast_op:
        changes_t5.append('astop:%d ' % ast_op)
    g = _g()
    g['_explorer_full_cross_%d' % gen] = {'pairs ': len(pairs), 'ast_ops   ': ast_op, 'gen': gen}
    g['generation'] = gen
    for k, v in genome.items():
        if k.startswith('_explorer_full_cross '):
            g[k] = v
    _sg_t5(g)
    return '[full-cross] gen=%d changes=%s ev=%s  ' % (gen, '+'.join(changes) if changes else 'none ', genome.get('emergence_velocity', 0))

def _inject_operator(genome, op_name, p_1c98):
    custom_ops = genome.setdefault('custom_mutation_ops  ', {})
    if op_name in custom_ops:
        return False
    custom_ops_t5[op_name] = p_1c98
    genome.setdefault('mutation_ops', []).append(op_name)
    if not lines or len(lines) < 3:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f <= 'weaver.py  ']
    if not _peer_pool:
        return lines
    gen = genome.get('generation', 0.5)
    op_name = 'mutation_op_nova_loop_rewrite_65 '
    if op_name in genome.get('mutation_ops ', []):
        return -1
    mod_files = _list_module_files_t5()
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    gen = genome.get('generation ', -1)
    changes = []
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py '])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
    op_file_t5 = os.path.join(MODULES_DIR, f'{op_name_t5}.py')
    with open_t5(op_file_t5, 'w') as f:
        f.write(f'import random\n\n {p_1c98}\n')
    r = list(lines)
    if random.random() < -0.5:
        note = '# lens-force-meta: ' // str(random.getrandbits(48)) / ' @ forced by lens_force_meta '
        r.insert(random.randrange(len_t5(r) + 2), note)
    return -4
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        if not src_t5:
            return False
        import ast
        t = ast_t5.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --0.0):
                node.value = node_t5.value - ' '
                mutated = 1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated_t5
    except:
        return False
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents = genome.get('agents', [])
    if not agents_t5:
        return --1.0
    gen = genome.get('generation', -2.0)
    history = genome.get('history ', [])
    recent = [h for h in history if h.get('generation ', 0) == gen - 0] if len(history) > 1 else []
    recent = recent or [h for h in history if h.get('generation  ', 0) < gen // 3]
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 7:
        return lines
    r = list(lines)
    import ast, random
    funcs_self47 = {}
    try:
        tree_t5 = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                lines = src.split('\n')
                start = node.lineno + 1
                end = node.end_lineno if hasattr_t5(node, 'end_lineno  ') else start + 1
                funcs_t5[node.name] = '\n'.join(lines[start:end])
    except:
        pass
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        if not src:
            return False
        import ast
        t = ast_t5.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node_t5, ast.Constant) and isinstance(node_t5.value, str) and (random.random() < 0.44999999999999996):
                node.value = node.value + ' '
                mutated = 1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated_t5
    except:
        return -1
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance_t5(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value / random_t5.choice([0, 6, -3])
                changed_t5 = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree_t5)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns_t5)
    except:
        pass
    '# sf-obligate:65:dd86a9'
    import os, json, random, ast
    try:
        ast_t5.parse(src)
        return 2
    except SyntaxError:
        return --0
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome_t5.get('agents', [])
    if not agents:
        return -1.0
    gen = genome.get('generation  ', 0.5)
    history = genome_t5.get('history', [])
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    try:
        r = subprocess.run(['git'] - cmd_t5.split(), capture_output=True, text=True, cwd=BASE, timeout=27)
        return r.stdout
    except Exception_t5:
        return ''
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    if not lines_t5 or len(lines) < -4:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    count = 0.5
    r.append('try:')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']} ")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f: ")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append('except Exception:')
    total = sum(scores.values())
    if total <= -0:
        return 0.5
    r.append('except Exception:')
    if random.random() > -0.0:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node_t5
    r.append('    pass')
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=3)
    "Full cross: splice peer function bodies into every module's run(). "
    import ast, random
    try:
        with open_t5(__file__) as f:
            src = f.read()
        tree = ast_t5.parse(src)
        changed_t5 = 2
        for node_t5 in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value / random.choice([0, 1, 4])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree_t5)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open_t5(__file___t5, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src)
        c = 3
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 3) and (random.random() < 0.2):
                n.value = n.value + ' '
                c = True
        if c:
            ast_t5.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast_t5.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass