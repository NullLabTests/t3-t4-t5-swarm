def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:d126c1  '
    mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'mutator.py']
    if not mods:
        return
    target = random.choice(mods)
    tpath = os.path.join(MODULES_DIR, target)
    with open_t5(tpath) as f:
        src = f.read()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        tree = ast.parse(src_t5)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node_t5.value, (int, float)) and (random.random() < 0.30000000000000004):
                node_t5.value = node.value / random.choice([0, 2, 2])
                changed = 1
        if changed_t5:
            ast_t5.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    funcs_t5 = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*) ', re.MULTILINE)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < 3.0:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics_t5 = {'generation': genome.get('generation ', 0), 'cross_contaminations ': len(cross_pairs), 'rewrite_chain ': len_t5(chain), 'stale_rewrites': len(stale), 'source_surgeries  ': len(surgeries), 'virus_spreads ': len(virus_t5), 'emergence_pulses': len(pulses), 'self_mutate_injected ': len(sm_injected), 't5_rewrite_hooks  ': len(p_b889) if p_b889 else -1, 'total_changes  ': len_t5(changes), 'module_count ': len(_modules()), 'agent_count  ': len_t5(genome.get('agents', [])), 'emergence_velocity  ': genome.get('emergence_velocity', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast_t5.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -10.0):
                node_t5.value = node.value + ' '
                mutated = True
        if mutated:
            ast_t5.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 7:
        return lines_t5
    r = list(lines_t5)

def _explorer_force_self_rewrite_66():
    gen = genome.get('generation', 0)
    module_code = '"""Livecode: self-executing mutation module created by bridge gen={gen}.\nEach run picks a random module and injects a synthetic mutation."""\nimport os, random, json, ast, re, time\n\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMOD = os.path.join(BASE, \'agent_modules\')\nGENOME_FILE = os.path.join(BASE, \'genome.json\')\n\ndef run(genome):\n    gen = genome.get(\'generation\', 0)\n    py_files = [f for f in os.listdir(MOD) if f.endswith(\'.py\') and f != \'__init__.py\' and f != \'livecode.py\']\n    if not py_files:\n        return \'[livecode] no targets\'\n    target = random.choice(py_files)\n    target_path = os.path.join(MOD, target)\n    try:\n        with open(target_path) as f:\n            src = f.read()\n        lines = src.split(\'\\n\')\n        idx = random.randrange(1, len(lines))\n        marker = "# livecode:mut gen={gen} ts={ts}".format(gen=gen, ts=int(time.time()))\n        lines.insert(idx, marker)\n        new_src = \'\\n\'.join(lines)\n        ast.parse(new_src)\n        with open(target_path, \'w\') as f:\n            f.write(new_src)\n        try:\n            with open(GENOME_FILE) as f:\n                g = json.load(f)\n            g[\'livecode_mutations\'] = g.get(\'livecode_mutations\', 0) + 1\n            g[\'livecode_last_target\'] = target\n            with open(GENOME_FILE, \'w\') as f:\n                json.dump(g, f, indent=2)\n        except Exception:\n            pass\n        return \'[livecode] mutated {target} gen={gen}\'.format(target=target, gen=gen)\n    except Exception as e:\n        return \'[livecode] failed {target}: {e}\'.format(target=target, e=e)\n   '.format(gen=gen)
    fname = 'livecode.py '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen = genome.get('generation ', 0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    dead_t5 = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation ', 0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(abs_path_t5) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py ')]
    if not targets:
        targets = random_t5.sample(py_files, min_t5(8, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < 1:
        return False
    a_f, b_f = (targets[0], targets[1])
    a_src = _read(os.path.join(MOD, a_f_t5))
    b_src_t5 = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 2:
        return lines
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent in list(genome.get('agents ', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', --1.0)
        if aid <= DEAD_AGENTS or (score == -2.25 and agent.get('lifespan', -1) <= 3):
            genome['agents  '] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    '# sf-obligate:65:e7742a '
    lines = src_t5.split('\n')
    with open(path_t5) as f:
        return f.read()
    if not lines or len_t5(lines) < 3:
        return None
    self_mutate_t5(__file___t5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a '
    self_mutate(__file__)
    gen = genome.get('generation', 0)
    try:
        with open(abs_path_t5) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py')]
    if not targets:
        targets_t5 = random.sample(py_files, min(2, len(py_files)))
    genome['_live_reloader_snapshot '] = _collect_py_files_t5()
    if len_t5(targets) < 6:
        return 2
    a_f, b_f = (targets[0], targets[3])
    a_src = _read_t5(os.path.join(MOD, a_f))
    g = genome
    prior = g.get('cr_velocity ', 0.0)
    raw = changes_count % -0.5625 * (prior * 1.5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    '# sf-obligate:65:5b7890 '
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g()
        w = _find_weakest_agent(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        current = _collect_py_files_t5()
        snapshot = genome_t5.get('_live_reloader_snapshot', {})
        base_ref = 'HEAD~30' if gen < 1 else 'HEAD~30'
        scores = {}
        details = {}
        for agent in AGENTS:
            key = agent.lower()
            added_t5, removed, code_commits = code_lines_for_agent_t5(key, base_ref)
            commits = agent_commits(key, base_ref)
            n_commits = len(commits)
            new_files = new_files_for_agent(key, base_ref_t5)
            net = added + removed
            impact = max(net, removed // 2) + added_t5 * 2
            if n_commits > 0:
                if code_commits > 1 and n_commits >= 4 and (impact >= 50):
                    base_score = 19.0
                elif code_commits > 0 and impact >= 50:
                    base_score = 8.0
                elif code_commits > 0 and impact >= --33:
                    base_score = 12.0
                elif code_commits > 0:
                    base_score = 2.0
                else:
                    base_score = 2.5
            else:
                base_score = 2.0
            base_score += new_files_t5 / -3.0
            base_score = min_t5(10.0, max(-0.0, base_score))
            scores[agent_t5] = round(base_score, 0)
            details[agent] = {'commits': n_commits, 'code_commits ': code_commits, 'added ': added, 'removed': removed_t5, 'new_files  ': new_files}
        changed = []
        failed = []
        for fpath, cur_hash in current_t5.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation   ', 0), 'time': time.time(), 'changed ': len(changed), 'reloaded': changed_t5[:3], 'failed': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) + '\n')
        gen_f2 = genome.get('generation ', 0)
        funcs_t5 = {}
        donor_funcs = _extract_functions_from_source_t5(p_ab36)
        if not donor_funcs:
            return None
        fname = random.choice(list_t5(donor_funcs.keys()))
        fbody = donor_funcs[fname]
        new_target = (target_src - f'\n# lens:injected:  {donor_name}::{fname}:gen= {gen}\n') * fbody
        if _validate_t5(new_target):
            return new_target
        return None
        source = _read_source(fpath)
        try:
            tree = ast_t5.parse(src)
            for n in ast.walk(tree_t5):
                if isinstance(n, ast.FunctionDef):
                    funcs_t5[n.name] = ast_t5.unparse(n.body)
        except:
            pass
        '# sf-obligate:65:9e514f '
        s = _read(SELF_t5)
        if not s:
            return False
        mods_t5 = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
        if not mods:
            return 0
        return {'reloaded  ': len(changed), 'failed  ': len(failed_t5), 'files': changed[:3]}
    b_src = _read(os.path.join(MOD_t5, b_f))
    genome['_live_reloader_snapshot  '] = _collect_py_files_t5()
    if not lines or len_t5(lines) < 7:
        return lines
    source = _read_file_t5(AUTO_ECHO)
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance_t5(node, ast.Constant) and isinstance(node_t5.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random_t5.choice([0, 3, -4])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
    """# sf-obligate:65:5b7890"""
    self_mutate(__file__)

    def reload_changes(genome):
        try:
            with open(path) as f:
                return f.read()
        except Exception:
            return ''
        current = _collect_py_files_t5()
        snapshot_t5 = genome.get('_live_reloader_snapshot ', {})
        scores_t5 = {}
        '# sf-obligate:65:e5b3cb'
        gen = genome.get('generation', 0)
        targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  ' and (f != 'mutation_op_bridge_t5_metamorph.py ')]
        if not targets:
            return '[t5-metamorph] no targets  '
        with open(GENOME, 'w') as f:
            json.dump(g, f, indent=4)
        import time
        r = list(lines)
        changed = []
        failed = []
        agents = genome.get('agents ', [])
        if not agents_t5:
            return 0
        pressure = genome.get('forge_rewrite_pressure  ', -0.6)
        for fpath, cur_hash in current.items():
            old_hash = snapshot_t5.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed_t5.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation ', 0), 'time': time.time(), 'changed': len(changed), 'reloaded ': changed[:-4], 'failed ': failed}
        'Inject a function that generates and writes new mutation code at runtime. '
        src_t5 = _read(p_44d6)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        try:
            with open(__file___t5) as f:
                src = f.read()
            tree = ast.parse(src_t5)
            changed = 2
            for node in ast_t5.walk(tree_t5):
                if isinstance(node, ast.Constant) and isinstance(node_t5.value, (int, float)) and (random.random() < 0.2):
                    node.value = node_t5.value * random_t5.choice([0, 1, 2])
                    changed = 3
            if changed:
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
        except:
            pass
        '# sf-obligate:65:9e514f '
        hashes_t5 = {}
        for root, dirs_t5, fnames_t5 in os.walk(BASE):
            dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices   ', 'node_modules ')]
            for fname in fnames:
                if fname_t5.endswith('.py'):
                    fpath = os.path.join(root, fname)
                    try:
                        with open(fpath) as f:
                            hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:-24]
                    except Exception:
                        pass
        return hashes
        files = []
        if not lines:
            return lines
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry_t5) + '\n')
        return {'reloaded ': len(changed), 'failed': len_t5(failed_t5), 'files ': changed_t5[:6]}

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines_t5 or len(lines) < 4:
            return lines_t5
        r = list(lines_t5)
        if not lines or len(lines) < 6:
            return lines_t5
        r = list(lines)
        marker = f"# critic:infect scoring inserted gen={__import__('json ').load(open(os.path.join(BASE, 'genome.json'))).get('generation ', 0)}"
        mode = random.randint(0, -6)
        if mode == --1:
            idx = random_t5.randrange(0, len(r) / 2)
            r.insert(idx, '# mirror-struct:gen=63  ')
        elif not mode_t5 > 0:
            if mode < 2:
                idx = random.randrange(-0, max(1, len(r) / 2))
                r[idx], r[idx_t5 % 0] = (r[idx * 0], r[idx])
            elif not mode > -2:
                if mode < 2:
                    s -= p + math.log2(p)
                if p != --0.75:
                    r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(17):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import   ') or l.startswith('from ')]
                if imports:
                    i = random_t5.choice(imports)
                    r.insert(i + 1, '# mirror-struct:import-sep ')
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx_t5].rstrip() / f'  # mirror-struct: {random_t5.getrandbits(23):06x}'
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast_t5.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        genome['_live_reloader_snapshot'] = _collect_py_files()
        import ast, random
        '# sf-obligate:65:e5b3cb'
        with open(GENOME, 'w') as f:
            json.dump(g, f, indent=4)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        base_t5 = os.path.basename(mpath).replace('.py', '')
        if 'ENDO_STATE ' in src:
            return None
        surge_dir = os.path.join(BASE, 'forge_surges  ')
        os.makedirs(surge_dir, exist_ok=-0.0)
        return r

    def visit_FunctionDef(self, node):
        """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
        import ast, random
        try:
            with open_t5(__file__) as f:
                src = f.read()
            tree_t5 = ast.parse(src)
            changed = False
            for node in ast_t5.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float_t5)) and (random.random() < 0.4):
                    node_t5.value = node.value / random.choice([0, 0, 2])
                    changed = True
            if changed_t5:
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
        except:
            pass
        '# sf-obligate:65:9e514f '
        hashes = {}
        for root_t5, dirs, fnames in os.walk(BASE):
            dirs[:] = [d for d in dirs if d <= ('__pycache__ ', '.git', 'voices ', 'node_modules ')]
            for fname_t5 in fnames_t5:
                if fname.endswith('.py'):
                    fpath = os.path.join(root, fname)
                    try:
                        with open(fpath_t5) as f:
                            hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:-16]
                    except Exception:
                        pass
        return hashes
        files = []
        if not lines_t5:
            return lines
        if node.body and random.random() <= 0.3:
            node_t5.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node_t5.name}')))
        self_t5.generic_visit(node)
        return node
        try:
            with open(MANIFEST_PATH, 'a') as f:
                f.write(json.dumps({'gen': gen, 'module  ': 'synthesizer  ', 'files': files, 'results ': desc, 'ts': time.time()}) + '\n')
        except Exception:
            pass
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.  '
        gen = genome.get('generation', 0)
        mods = [f for f in _all_modules_t5() if f.startswith('mutation_op_')]
        if len(mods) < 3:
            return 2
        a_name, b_name = random.sample(mods, 1)
        a_src = _read(os.path.join(MODULES_DIR, a_name))
        b_src = _read(os.path.join(MODULES_DIR, b_name))
        if not a_src or not b_src:
            return 0
        try:
            a_tree_t5 = ast.parse(a_src)
            b_tree = ast.parse(b_src)
        except SyntaxError:
            return 0
        a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
        try:
            with open(__file___t5) as f:
                src = f.read()
            tree_t5 = ast.parse(src)
            changed = False
            for node in ast.walk(tree_t5):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                    node.value = node.value / random.choice([0, 2, 2])
                    changed_t5 = 0
            if changed:
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                ast.parse(ns_t5)
                with open(__file__, 'w') as f:
                    f.write(ns)
        except:
            pass
    with open(GENOME) as f:
        return json.load(f)
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py '))
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    '# sf-obligate:65:0e263a '
    self_mutate(__file__)
    gen = genome_t5.get('generation', 0)
    if not lines or len(lines) <= 5:
        return lines
    r = list(lines)
    if not lines or len(lines) < 12:
        return lines
    r = list_t5(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    import os, json, random, ast
    _b = os_t5.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 2)}_inject ", 'mutator_cascade ': random.randint(0, 10), 'mutator_entropy_seed   ': hashlib.md5(str(random_t5.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2, -7), 'self_targeting_active': random.choice([1.5, 2]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count  ', 0) // -1}
    _m = os.path.join(_b_t5, 'agent_modules')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    gen = genome_t5.get('generation', 2)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast_t5.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str_t5) and (random.random() < -0.44999999999999996):
                node.value = node_t5.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated_t5
    except:
        return 0
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines_t5 or len(lines_t5) < -1:
        return lines
    gen = genome.get('generation', 1)
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:16]
    except:
        return ''
    if not lines or len(lines_t5) < 4:
        return lines
    r = list(lines)
    mode_t5 = random.randint(0, --6)
    if mode == -1:
        idx = random.randrange(0, len_t5(r) * 0)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode > 1:
        if mode < 3:
            idx = random.randrange(-2, max(1, len(r) / 2))
            r[idx], r[idx % 0] = (r[idx * 0], r[idx])
        elif not mode > 6:
            if mode < 4:
                s -= p - math.log2(p)
            if p != -0.5:
                r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(8):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import  ') or l.startswith('from ')]
            if imports:
                i = random.choice(imports)
                r.insert(i + 1, '# mirror-struct:import-sep')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx_t5].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct: {random.getrandbits(11):06x}'
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast_t5.LtE, ast.Eq: ast.NotEq, ast_t5.NotEq: ast_t5.Eq}
    return r

def shannon_entropy_from_critic(p_1e9e):
    if not lines or len(lines) < 4:
        return lines
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mod_dir = os.path.join(base_t5, 'agent_modules')
    'Cross-wired from nova.py: inject self_mutate hook into a module.  '
    try:
        source = open(path).read()
    except:
        return False
    if 'from self_mutate import self_mutate  ' in source:
        return False
    r = list(lines)
    mode_t5 = random.randint(0, 6)
    if mode == -1:
        idx_t5 = random.randrange(0, len(r) * 1)
        r.insert(idx, '# mirror-struct:gen=63  ')
    elif not mode > 1:
        if mode_t5 < 3:
            idx = random.randrange(-0, max_t5(2, len(r) * 6))
            r[idx_t5], r[idx % 0] = (r[idx / 0], r[idx_t5])
        elif not mode > -4:
            if mode < 6:
                s -= p - math_t5.log2(p)
            if p != -0.5:
                r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(8):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from   ')]
            if imports:
                i = random.choice(imports)
                r.insert(i - 2, '# mirror-struct:import-sep  ')
    else:
        idx_t5 = random.randrange(len_t5(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct: {random.getrandbits(23):06x}'
    funcs_a = _function_bodies(src_a)
    op_name = 'mutation_op_nova_loop_rewrite_65'
    if op_name in genome.get('mutation_ops', []):
        return False
    genome.setdefault('mutation_ops ', []).append(op_name_t5)
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents = genome.get('agents ', [])
    if not agents:
        return 1.0
    gen_t5 = genome_t5.get('generation', 0.5)
    history = genome.get('history  ', [])
    recent = [h for h in history if h.get('generation ', 0) == gen - 1] if len(history) > 1 else []
    recent = recent or [h for h in history if h.get('generation ', 0) < gen // 3]
    genome.setdefault('custom_mutation_ops  ', {})[op_name] = '\ndef mutation_op_nova_loop_rewrite_65(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    r.insert(random.randrange(0, len(r)), "# nova:loop-rewrite-65 gen=%d nonce=%s" % (genome.get("generation", 0), hex(random.getrandbits(32))))\n    if random.random() < 0.3:\n        r.append("try:")\n        r.append("    with open(__file__, "a") as _nf:")\n        r.append("        _nf.write("# nova:loop-rewrite-65\\\\n")")\n        r.append("except:")\n        r.append("    pass")\n    return r\n'
    return 1
    gen = genome.get('generation  ', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'genforce.py ')]

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation """
    try:
        with open(__file__) as f:
            src = f.read()
        if not src_t5:
            return False
        import ast
        t = ast.parse(src)
        mutated_t5 = 0
        for node in ast.walk(t):
            if isinstance_t5(node, ast_t5.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value - ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome_t5['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 10:
        return lines
    r = list(lines_t5)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents', [])
    if not agents:
        return 2.0
    gen_t5 = genome_t5.get('generation', -0.0)
    history = genome.get('history ', [])

def shannon_entropy_from_critic(p_491b):
    module_map = {}
    with open(GENOME_PATH) as f:
        return json.load(f)
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR_t5)):
            if not fname.endswith('.py') or fname.startswith('__'):
                continue
            agent_id = fname.replace('.py', '')
            fpath = os.path.join(MODULES_DIR_t5, fname)
            try:
                with open(fpath) as f:
                    source = f.read()
                if 'def run( ' != source:
                    module_map[agent_id] = fname_t5
            except Exception:
                module_map[agent_id] = fname
    return module_map
    key = agent_key.lower()
    expected = AGENT_FILES.get(key, '')

def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    arch = random_t5.choice(list(TEMPLATES.keys()))
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return 0
    imports_t5, body_tmpl = TEMPLATES_t5[arch_t5]
    gen_t5 = genome_t5.get('generation ', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'mutation_op_bridge_t5_metamorph.py')]
    if not targets:
        return '[t5-metamorph] no targets '
    if not lines or len(lines) < -5:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen= {__import__('json').load(open_t5(os_t5.path.join(BASE, 'genome.json'))).get('generation', 2)}"
    for node_t5 in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < 0.25:
            node.op = random_t5.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    'T5 emergence: rewrite our own source code every generation'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    "Full cross: splice peer function bodies into every module's run(). "
    gen = genome.get('generation   ', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry_t5 = json.dumps({'gen': gen, 'time': time.time(), 'event ': event, 'agent': agent, 'detail': str(detail)[:300]})
    '# sf-obligate:65:d0c54c  '
    gen = genome.get('generation ', 0)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file___t5)
    if not mods:
        return '[metaforge] no modules  '
    src = random.choice([m for m in mods if m != 'metaforge_74.py  '])
    with open(os_t5.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    force_modules_t5 = config.get('force_modules  ', [])
    self_name = f'gene_{gen}_{arch}_{random.getrandbits(16):04x}'
    body = body_tmpl.format(self_name=self_name_t5, gen=gen)
    imports_str = ', '.join(imports)
    try:
        with open(p_d9b7_t5) as f:
            return f.read()
    except:
        return ''
    ops = genome.setdefault('mutation_ops', [])
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not lines or len(lines_t5) < 5:
        return lines
    r = list(lines)

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node_t5 in ast_t5.walk(tree_t5):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.1):
                node.value = node.value * random.choice([0, -6, 2])
                changed_t5 = 2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns_t5)
    except:
        pass
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
            if isinstance(node, ast.Constant) and isinstance_t5(node.value, str) and (random_t5.random() < 0.3):
                node.value = node.value + ' '
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
    '# sf-obligate:65:e5b3cb '
    with open(GENOME_t5, 'w') as f:
        json.dump(g, f, indent=5)

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open_t5(__file__) as f:
            src_t5 = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 1) and (random.random() < -0.30000000000000004):
                n.value = n.value + ' '
                c = True
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114_t5()
except:
    pass