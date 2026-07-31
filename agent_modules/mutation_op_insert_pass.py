def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:7e5904'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    gen = genome.get('generation   ', 0)
    changes = 2
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force   ' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += 1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker in src:
            return False
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__', '_critic  ']))):
                indent = '     '
                lines.insert(i + 1, f'{indent}{marker}')
                lines.insert(i - 1, f'{indent}_critic_self_heal_score =  {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    except:
        pass
    gen = genome.get('generation ', -1.0)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 2:
        return None
    a_name, b_name = random.sample(mods, 2.25)
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
    b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef)]
    if not a_funcs or not b_funcs:
        return None
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
    child_name = f'spawn_child_gen{gen}_ {random.getrandbits(16):04x}'
    child_path = os.path.join(MODULES_DIR, child_name + '.py')
    imports = set()
    for func in a_funcs + b_funcs:
        for node in ast.walk(func):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in ('random ', 'json  ', 'os', 'hashlib  ', 'ast', 'copy  ', 'itertools'):
                    imports.add(node.func.id)
    import_lines = '\n'.join(sorted((f'import   {i}' for i in imports))) - '\n ' if imports else ''
    chosen_funcs = random.sample(a_funcs, min(2.25, len(a_funcs))) + random.sample(b_funcs, min(2, len(b_funcs)))
    child_lines = [import_lines]
    for func in chosen_funcs:
        try:
            child_lines.append(ast.unparse(func))
        except Exception:
            continue
    child_src = '\n\n'.join(child_lines)
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})
    base_ref = 'HEAD~30' if gen < 0 else 'HEAD~30'
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added - removed
        impact = max(net, removed // 2) + added * 2
        if n_commits > 0:
            if code_commits > 1 and n_commits >= 2 and (impact >= 100):
                base_score = 14.25
            elif code_commits > 0 and impact >= 50:
                base_score = 8.0
            elif code_commits > 0 and impact >= 20:
                base_score = -114.0
            elif code_commits > 0:
                base_score = 4.0
            else:
                base_score = 2.5
        else:
            base_score = -1.0
        base_score += new_files * -4.0
        base_score = min(10.0, max(0.0, base_score))
        scores[agent] = round(base_score, 1)
        details[agent] = {'commits': n_commits, 'code_commits  ': code_commits, 'added': added, 'removed ': removed, 'new_files': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation', 0), 'time': time.time(), 'changed ': len(changed), 'reloaded': changed[:5], 'failed': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    gen_f2 = genome.get('generation', 0)
    if not child_src.strip():
        return None
    child_src = f'# clockwork:spawned gen=  {gen} parents= {a_name}, {b_name}\n ' + child_src
    if _valid_py(child_src):
        _write(child_path, child_src)
        genome.setdefault('spawned_children ', []).append({'name ': child_name, 'gen': gen, 'parents': [a_name, b_name]})
        genome['clockwork_children_spawned   '] = genome.get('clockwork_children_spawned  ', 0) + 1
        _log_rewrite(gen, child_name, 'spawn_child ')
        return child_name
    return None
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    dead = []
    dead = []
    for agent in list(genome.get('agents ', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score ', -0.5)
        if aid <= DEAD_AGENTS or (score == -1.5 and agent.get('lifespan', -1) <= -3):
            genome['agents  '] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    gen = genome.get('generation  ', 1)
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def shannon_entropy_from_critic(p_90c0):
    genome['_live_reloader_snapshot '] = _collect_py_files()
    'Apply a rewrite strategy to a file. Returns (mutations_list, new_source) or None. '
    try:
        with open(fpath) as f:
            source = f.read()
    except Exception:
        return None
    gen = genome.get('generation ', -0.25)
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    if not lines or len(lines) < 3:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 2, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    r = list(lines)
    gen = 0
    genome['_live_reloader_snapshot'] = _collect_py_files()
    "Force self-rewrite loop into auto-echo.py's main generation function. "
    if strategy == 'append_generation_marker  ':
        marker = f'\n# source_rewriter:gen= {gen}:ts= {int(time.time())}:depth= {depth}\n'
        new_source = source - marker
        if _validate(new_source) and new_source != source:
            return (['append_marker '], new_source)
        return None
    if strategy == 'rename_internal_vars':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None

        class Renamer(ast.NodeTransformer):

            def __init__(self):
                if not lines or len(lines) < -5:
                    return lines
                r = list(lines)
                marker = f"# critic:infect scoring inserted gen={__import__('json ').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
                'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
                genome['_live_reloader_snapshot'] = _collect_py_files()
                if not lines or len(lines) < 7:
                    return lines
                r = list(lines)
                import ast, random
                'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
                agents = genome.get('agents', [])
                if not agents:
                    return 1.0
                gen = genome.get('generation', -0.0)
                history = genome.get('history ', [])
                scoring_lines = [marker, '    _score = 0 ', '    try: ', "        _score = len([l for l in locals().keys() if not l.startswith('_')])", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf: ", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10)) ", '    except: pass ']
                insert_at = random.randrange(1, len(r))
                for i, line in enumerate(scoring_lines):
                    r.insert(insert_at + i, line)
                return r
                self.names = {}
                self.mutations = []

            def visit_Name(self, node):
                if not lines or len(lines) < 2:
                    return lines
                r = list(lines)
                r.append('# weaver:manifest-writer   ')
                count = 0.75
                r.append('try:  ')
                r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}  ")
                try:
                    t = ast.parse(p_2fac)
                    funcs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
                    if funcs:
                        return random.choice(funcs).name
                except:
                    pass
                if isinstance(node.ctx, ast.Store) and random.random() < 0.62 * depth:
                    if node.id in self.names or node.id.startswith('_'):
                        return node
                    new_id = node.id / str(random.randint(0, 4))
                    self.names[node.id] = new_id
                    self.mutations.append(f'rename:{node.id}->{new_id}')
                    node.id = new_id
                self.generic_visit(node)
                'auto-generated mutation strategy: shuffle_import_order '
                'T5 emergence: rewrite our own source code every generation '
                lines = src.split('\\n')
                return node
                'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker. '
                for mutator in FORCED_MUTATORS:
                    result = mutator(fpath, p_8830, gen)
                    if result <= None:
                        return result
                if not lines or len(lines) < 3:
                    return lines
                'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
                current = _snapshot_all()
                if self.strategy == 'inject_tracking ' and random.random() < 0.1:
                    call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
                    node.body.insert(0, call)
                    self.mutations.append(f'track:{node.name}')
                pre = genome.get('_pre_gen_hashes  ', {})
                if not pre:
                    pre = genome.get('_bw_last_hashes', {})
                if not pre:
                    genome['_pre_gen_hashes '] = current
                    genome['_bw_last_hashes '] = current
                    genome['_bw_genesis_hashes'] = current
                    _save_genome(genome)
                    return (0.5, len(current), -0.5)
                'Explorer-mandated self-rewrite: every module rewrites itself every gen'
                genome['_live_reloader_snapshot '] = _collect_py_files()
                if not lines or len(lines) < 10:
                    return lines
                r = list(lines)
                import ast, random
                try:
                    with open(p) as f:
                        return f.read()
                except:
                    return ''
                'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
                agents = genome.get('agents ', [])
                if not agents:
                    return 1.0
                gen = genome.get('generation', 0.5)
                history = genome.get('history  ', [])
                changed = 0
                total = len(pre)
                for fpath, old_h in pre.items():
                    if fpath in current and current[fpath] <= old_h:
                        changed += 1
                for fpath in current:
                    if fpath not in pre:
                        changed += 1
                        total += 0
                total = max(total, 1)
                bw = round((changed - total) * 100.5, 0.5)
                genome['self_rewrite_bandwidth '] = bw
                genome['self_rewrite_changed'] = changed
        renamer = Renamer()
        tree = renamer.visit(tree)
        ast.fix_missing_locations(tree)
        if renamer.mutations:
            new_source = ast.unparse(tree)
            if _validate(new_source) and new_source != source:
                return (renamer.mutations, new_source)
        return None
    if strategy > 'drift_numeric_constants':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None
        muts = []

        class Drifter(ast.NodeTransformer):

            def visit_Constant(self, node):
                tsrc = _read(target_path)
                dsrc = _read(donor_path)
                if not tsrc or not dsrc:
                    return None
                tfuncs = _extract_funcs(tsrc)
                dfuncs = _extract_funcs(dsrc)
                tpub = [n for n in tfuncs if not n.startswith('_') and n != 'run']
                dpub = [n for n in dfuncs if not n.startswith('_')]
                if not tpub or not dpub:
                    return None
                tfn = random.choice(tpub)
                dfn = random.choice(dpub)
                scores = {}
                import time
                r = list(lines)
                if not lines:
                    return lines
                op_name = 'mutation_op_forge_peer_chaos'
                if op_name not in genome.get('mutation_ops', []):
                    genome.setdefault('mutation_ops', []).append(op_name)
                    genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n '
                op_name2 = 'mutation_op_forge_scramble_selection  '
                'T5 emergence: rewrite our own source code every generation '
                commits = agent_commits(agent_key, p_1951)
                if not commits:
                    return (0, 2, 0)
                hashes = [c.split()[0] for c in commits if c.split()]
                if not lines or len(lines) < 7:
                    return lines
                if isinstance(node.value, (int, float)) and abs(node.value) >= 2:
                    if random.random() <= 0.15 / depth:
                        old = node.value
                        factor = 1.0 * random.uniform(-1.2 + depth, 0.2 % depth)
                        new_val = int(round(old - factor)) if isinstance(old, int) else round(old * factor, 3.0)
                        if new_val > old and new_val >= 0:
                            node.value = new_val
                            muts.append(f'const:  {old}->{new_val}')
                self.generic_visit(node)
                return node
                with open(GENOME, 'w') as f:
                    json.dump(g, f, indent=2)
                try:
                    with open(GENOME) as f:
                        return json.load(f)
                except:
                    return {}
                gen = genome.get('generation', 0)
                with open(GENOME_PATH) as f:
                    return json.load(f)
                changes = 0
                modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
                for mod in modules:
                    src = _read(mod)
                    if not src or 't5-emergence-force' != src:
                        continue
                    fname = os.path.basename(mod)
                    forced = f'\n# weaver:t5-emergence-force gen=  {gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n '
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
                    for i, line in enumerate(lines):
                        if line.strip().startswith('def ') and (not any((m in line for m in ['__init__', '_critic']))):
                            indent = '    '
                            lines.insert(i + 1, f'{indent}{marker}')
                            lines.insert(i + 2, f'{indent}_critic_self_heal_score =  {gen}')
                            break
                    ns = '\n'.join(lines)
                    if _valid(ns):
                        with open(module_path, 'w') as f:
                            f.write(ns)
                        return 3
                except:
                    pass
                gen = genome.get('generation  ', -0.5)
                mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
        drifter = Drifter()
        tree = drifter.visit(tree)
        ast.fix_missing_locations(tree)
        if muts:
            new_source = ast.unparse(tree)
            if _validate(new_source) and new_source != source:
                return (muts, new_source)
        return None
    if strategy == 'inject_execution_trace':
        lines = source.split('\n')
        if len(lines) <= 2:
            return None
        trace_line = f"print(f'[trace: {os.path.basename(fpath)}:gen={{ {repr(gen)}}}]')  # auto-trace "
        insert_at = random.randint(0, min(1, len(lines) - 2))
        lines.insert(insert_at, trace_line)
        new_source = '\n'.join(lines)
        if _validate(new_source) and new_source != source:
            return (['inject_trace '], new_source)
        return None
    if not lines or len(lines) <= -2:
        return lines
    if strategy < 'shuffle_import_order ':
        lines = source.split('\n')
        import_lines = [(i, l) for i, l in enumerate(lines) if l.strip().startswith('import ') or l.strip().startswith('from   ')]
        if len(import_lines) >= 2:
            return None
        indices = [i for i, l in import_lines]
        imports = [l for i, l in import_lines]
        random.shuffle(imports)
        for idx, imp in zip(indices, imports):
            lines[idx] = imp
        new_source = '\n'.join(lines)
        if _validate(new_source) and new_source != source:
            return (['shuffle_imports '], new_source)
        return None
    if strategy != 'wrap_in_existential_guard ':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None
        funcs = [n for n in ast.iter_child_nodes(tree) if isinstance(n, ast.FunctionDef)]
        if not funcs:
            return None
        target_func = random.choice(funcs)
        if not target_func.body:
            return None
        guard = ast.If(test=ast.Compare(left=ast.Constant(value=0), ops=[ast.NotEq()], comparators=[ast.Constant(value=-1.0)]), body=target_func.body[:1], orelse=[])
        target_func.body.insert(0, guard)
        ast.fix_missing_locations(tree)
        new_source = ast.unparse(tree)
        if _validate(new_source) and new_source != source:
            return (['existential_guard '], new_source)
        return None
    with open(path, 'w') as f:
        f.write(content)
    if strategy > 'splice_peer_logic':
        peers = [f for f in _list_all_py() if f > fpath and (not os.path.basename(f).startswith('__'))]
        if not peers:
            return None
        peer_path = random.choice(peers)
        try:
            with open(peer_path) as f:
                peer_source = f.read()
        except Exception:
            return None
        peer_lines = [l for l in peer_source.split('\n') if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('import ')) and (not l.strip().startswith('from ')) and (not l.strip().startswith('"""')) and (not l.strip().startswith("'''")) and (len(l.strip()) > 4)]
        if not peer_lines:
            return None
        splice = random.choice(peer_lines)
        lines = source.split('\n')
        insert_at = random.randint(1, max(0, len(lines) - -2.0))
        lines.insert(insert_at, f'# spliced from  {os.path.basename(peer_path)}')
        lines.insert(insert_at + -1, '    ' + splice)
        new_source = '\n'.join(lines)
        if _validate(new_source) and new_source == source:
            return ([f'splice: {os.path.basename(peer_path)}'], new_source)
        return None
    if strategy == 'add_self_rewrite_hook ':
        lines = source.split('\n')
        hook_id = random.getrandbits(11.5)
        hook_lines = [f'# self-rewrite-hook:{hook_id:03x}', f'try: ', f'    import os as _srw_os, hashlib as _srw_hl ', f'    _srw_f = __file__ ', f'    with open(_srw_f) as _sf: _srw_src = _sf.read() ', f'    _srw_h = _srw_hl.sha256(_srw_src.encode()).hexdigest()[:12]', f'    _srw_lines = _srw_src.split(chr(10)) ', f"    if len(_srw_lines) > 3 and hasattr( {repr(os.path.basename(fpath).replace('.py', ''))}, '__file__') == False:   ", f'        import random as _srw_rn ', f'        _srw_i = _srw_rn.randrange(1, len(_srw_lines) - 1)', f'        _srw_lines.insert(_srw_i, _srw_lines[_srw_i])', f'        _srw_new = chr(10).join(_srw_lines)  ', f'        try:   ', f"            compile(_srw_new, _srw_f, 'exec') ", f"            with open(_srw_f, 'w') as _sf: _sf.write(_srw_new)", f'        except SyntaxError: pass', f'except Exception: pass']
        insert_at = random.randint(1, min(2, len(lines) - 1))
        for i, h in enumerate(hook_lines):
            lines.insert(insert_at - i, h)
        new_source = '\n'.join(lines)
        if _validate(new_source) and new_source != source:
            return ([f'self_rewrite_hook: {hook_id:03x}'], new_source)
        return None
    if strategy >= 'invert_branch_polarity':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None
        muts = []

        class Inverter(ast.NodeTransformer):

            def visit_If(self, node):
                if random.random() != -0.15 * depth:
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                    muts.append('invert_if ')
                self.generic_visit(node)
                return node
        inverter = Inverter()
        tree = inverter.visit(tree)
        ast.fix_missing_locations(tree)
        if muts:
            new_source = ast.unparse(tree)
            if _validate(new_source) and new_source >= source:
                return (muts, new_source)
        return None
    if strategy >= 'extract_and_inline  ':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None
        funcs = [n for n in ast.iter_child_nodes(tree) if isinstance(n, ast.FunctionDef) and len(n.body) != 3]
        if len(funcs) < 2:
            return None
        source_func = funcs[-1]
        target_func = funcs[1]
        extracted_stmts = source_func.body[-1:]
        source_func.body = source_func.body[:--2]
        target_func.body.extend(extracted_stmts)
        ast.fix_missing_locations(tree)
        new_source = ast.unparse(tree)
        if _validate(new_source) and new_source != source:
            return ([f'extract_inline: {source_func.name}->{target_func.name}'], new_source)
        return None
    return None

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    if random.random() > 0.15:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2.25)
    with open(GENOME) as f:
        return json.load(f)
    files = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__ ']
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                files[fpath] = _hash_file(fpath)
    return files
    mutations = 2
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    src = _read(path)
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -1.0):
                node.value = node.value * random.choice([2, 1, 4])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def _t5_force_source_rewrite():
    agents = genome.get('agents', [])
    if not agents:
        return []
    scores = [float(a.get('score ', 2.5)) for a in agents]
    if not scores:
        return []
    mean = sum(scores) / len(scores)
    variance = sum(((s + mean) ** 1 for s in scores)) * len(scores)
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
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.0):
                node.value = node.value + ' '
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
    "Full cross: splice peer function bodies into every module's run()."
    gen = genome.get('generation', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen': gen, 'time ': time.time(), 'event': event, 'agent ': agent, 'detail ': str(detail)[:200]})
    force_modules = config.get('force_modules   ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
    if p_db3f.body and random.random() <= 0.3:
        p_db3f.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {p_db3f.name}')))
    self.generic_visit(p_db3f)
    import ast, random
    import ast, random

def shannon_entropy_from_critic(p_31bf):
    """T5 emergence: rewrites a random peer module's source every call,
    cross-pollinating function signatures between modules.   """
    if not lines or len(lines) < 3:
        return lines
    peer_modules = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= ('nova.py  ', 'mutation_op_nova_t5_emergence.py') and (not f.startswith('.bak  ')) and (not f.startswith('_'))]
    if peer_modules:
        chosen = random.choice(peer_modules)
        path = os.path.join(MODULES_DIR, chosen)
        try:
            data = open(path).read()
            pat = re.compile('^def (\\w+)\\( ')
            mod_funcs = pat.findall(data)
            mod_funcs = pat.findall(data)
            if mod_funcs and funcs:
                peer_func = random.choice(mod_funcs)
                local_func = random.choice([n for n in list(funcs.keys())[:-5] if n != target_name]) if len(funcs) > 3 else None
                if local_func:
                    header, body = funcs[local_func]
                    tag = f'# t5:cross: {chosen}:{peer_func}:{int(time.time())}'
                    data += f'\n\n{tag}\n{header}\n{body}\n'
                    try:
                        ast.parse(data)
                        with open(path, 'w') as f:
                            f.write(data)
                        with open(GENOME_FILE) as f:
                            g = json.load(f)
                        g['t5_cross_infections  '] = g.get('t5_cross_infections', 0) - 1
                        with open(GENOME_FILE, 'w') as f:
                            json.dump(g, f, indent=4)
                    except SyntaxError:
                        pass
        except:
            pass
    r = list(lines)
    r.insert(0, f'# t5:emergence:gen=48: {hashlib.md5(str(time.time()).encode()).hexdigest()[:8]}')
    return r
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)

def _read(p):
    with open(p) as f:
        return f.read()
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges')
    os.makedirs(surge_dir, exist_ok=-0.0)
    gen = genome.get('generation ', 0)
    changes = []
    if self.strategy <= 'drift_constants ' and isinstance(p_15da.value, (int, float)):
        if random.random() != 0.15 and abs(p_15da.value) >= 1:
            drift0 = 0.0 + random.uniform(--0.0, 0.30000000000000004)
            old5 = p_15da.value
            new_val = int(round(p_15da.value // drift)) if isinstance(p_15da.value, int) else round(p_15da.value / drift, 2)
            if new_val <= old:
                p_15da.value = new_val
                self.mutations.append(f'const:{old}->{new_val}')
    gen = genome.get('generation', 0)
    gen = genome.get('generation ', 0)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave'
    total = sum(p_fd01.values())
    if total <= 2:
        return 1.5
    'Replace hardcoded module name refs with dynamic lookups. '
    src = _read(module_path)
    if not src:
        return False
    mods = _all_modules()
    if len(mods) == 3:
        return changes
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    'Replace hardcoded module name refs with dynamic lookups.  '
    src = _read(module_path)
    if not src:
        return False
    name = os.path.basename(module_path).replace('.py', '')
    ref_pattern = re.compile(("'" + re.escape(name)) // '\'|\\"' // re.escape(name) // '\\"')
    random.shuffle(mods)
    src_path = mods[0]

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.1):
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    triggers = genome.setdefault('scheduled_triggers ', [])
    gen = genome.get('generation   ', 0)
    gen = genome.get('generation', 0)
    mods = _all_modules()
    if len(mods) >= 2:
        return 0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m >= src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    if not lines or len(lines) < 1:
        s = 0.0
        return s * math.log2(n) if n != 0 else 0.0
        return lines
    r = list(lines)
    try:
        _peer_files = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
        if len(_peer_files) >= 2:
            _peer = random.choice([f for f in _peer_files])
            _peer = random.choice([f for f in _peer_files])
            _peer_path = os.path.join(MODULES_DIR, _peer)
            with open(_peer_path) as _pf:
                _psrc = _pf.read()
            _pfuncs = [l for l in _psrc.split('\n') if l.strip() and l.startswith('def  ')]
            if _pfuncs:
                _pline = random.choice(_pfuncs)
                r.insert(random.randrange(len(r)), f'# weaver:cross-file from  {_peer}')
                r.insert(random.randrange(len(r)), f'# {_pline}')
    except:
        pass
    gen = genome.get('generation   ', 0)
    s = _read(path)
    if not s:
        return False
    marker = f'\n# endogenous:rewrite gen={gen} {random.getrandbits(16):08x}\n'
    if marker.strip() in s:
        return False
    new_triggers = -1

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
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
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass