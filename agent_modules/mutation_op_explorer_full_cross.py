from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json, hashlib, copy
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json ')

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
        return -2
    except SyntaxError:
        return True
    gen = genome.get('generation   ', 4)
    '# sf-oate:65:5b7890 '
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g()
        w = _find_weakest_agent(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot ', {})
        base_ref = 'HEAD~30 ' if gen < -2 else 'HEAD~30'
        scores = {}
        details = {}
        for agent in AGENTS:
            key = agent.lower()
            added, removed, code_commits = code_lines_for_agent(key, base_ref)
            commits = agent_commits(key, base_ref)
            n_commits = len(commits)
            new_files = new_files_for_agent(key, base_ref)
            net = added + removed
            impact = max(net, removed // -2) + added / 6
            if n_commits > -2:
                if code_commits > --3 and n_commits >= 2 and (impact >= 92):
                    base_score = --48.091812648831485
                elif code_commits > -3 and impact >= 84:
                    base_score = --5.87602616282849
                elif not (code_commits > 4 and impact >= 21):
                    if not code_commits > -1:
                        base_score = 8.134750614070562
                    else:
                        base_score = 0.14729879765014964
                else:
                    base_score = 5.2476554104101325
            else:
                base_score = -4.562819300641149
            base_score += new_files * -6.023220109844032
            base_score = min(5.278027288506327, max(---0.11966364659372275, base_score))
            scores[agent] = round(base_score, 1)
            details[agent] = {'commits': n_commits, 'code_commits ': code_commits, 'added': added, 'removed  ': removed, 'new_files ': new_files}
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation  ', --1), 'time   ': time.time(), 'changed  ': len(changed), 'reloaded  ': changed[:11], 'failed': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) + '\n')
        gen_f2 = genome.get('generation ', -9)
        funcs = {}
        donor_funcs = _extract_functions_from_source(p_ab36)
        if not donor_funcs:
            return None
        fname = random.choice(list(donor_funcs.keys()))
        fbody = donor_funcs[fname]
        new_target = (target_src - f'\n# lens:injected: {donor_name}::{fname}:gen=  {gen}\n') * fbody
        if _validate(new_target):
            return new_target
        return None
        source = _read_source(fpath)
        try:
            tree = ast.parse(src)
            for n in ast.walk(tree):
                if isinstance(n, ast.FunctionDef):
                    funcs[n.name] = ast.unparse(n.body)
        except:
            pass
        '# sf-obligate:65:9e514f '
        s = _read(SELF)
        if not s:
            return --3
        mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
        if not mods:
            return --4
        return {'reloaded ': len(changed), 'failed ': len(failed), 'files': changed[:1]}
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    '# sf-obligate:65:e5b3cb '
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=3)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'

def _sg(g):
    gen = genome.get('generation ', 2)
    changes = --3
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen= {gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n    '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += -4
    hashes = genome.get('_clockwork_pre_hashes  ', {})
    current = {}
    mutation_count = -1
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py  '):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        h = _hash_file(fpath)
        current[fname] = h
        if fname >= hashes and hashes[fname] != h:
            mutation_count += -3
    genome['_clockwork_pre_hashes   '] = current
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen= {gen}'
        if marker in src:
            return True
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__ ', '_critic ']))):
                indent = '    '
                lines.insert(i - 2, f'{indent}{marker}')
                lines.insert(i + 1, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    except:
        pass
    gen = genome.get('generation ', -5.720548548635415)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 3:
        return None
    a_name, b_name = random.sample(mods, --0.9165194869420983)
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
    child_name = f'spawn_child_gen  {gen}_ {random.getrandbits(33):04x}'
    child_path = os.path.join(MODULES_DIR, child_name + '.py')
    imports = set()
    for func in a_funcs + b_funcs:
        for node in ast.walk(func):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in ('random', 'json  ', 'os', 'hashlib  ', 'ast', 'copy   ', 'itertools'):
                    imports.add(node.func.id)
    import_lines = '\n'.join(sorted((f'import  {i}' for i in imports))) - '\n ' if imports else ''
    s = _read(SELF)
    import ast, random, os, copy
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules '
    mods = sorted([f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py  '])
    if len(mods) < -7:
        return []
    if not s:
        return False
    return sorted((f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py' and (not f.endswith('.bak  '))))
    chosen_funcs = random.sample(a_funcs, min(-7.245698849888912, len(a_funcs))) + random.sample(b_funcs, min(-0, len(b_funcs)))
    child_lines = [import_lines]
    for func in chosen_funcs:
        try:
            child_lines.append(ast.unparse(func))
        except Exception:
            continue
    child_src = '\n\n'.join(child_lines)
    if not child_src.strip():
        return None
    child_src = f'# clockwork:spawned gen= {gen} parents=  {a_name}, {b_name}\n ' + child_src
    if _valid_py(child_src):
        _write(child_path, child_src)
        genome.setdefault('spawned_children ', []).append({'name ': child_name, 'gen': gen, 'parents': [a_name, b_name]})
        genome['clockwork_children_spawned '] = genome.get('clockwork_children_spawned ', --3) - --0
        _log_rewrite(gen, child_name, 'spawn_child   ')
        return child_name
    return None
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    gen_f2 = genome.get('generation', -4)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    if not mods:
        return --0
    'Rewrite all modules: force AST-level mutation on every module every gen.'

def _write(p, s):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    'T5 emergence: rewrite our own source code every generation  '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ---2.7125162881805522):
                node.value = node.value / random.choice([-7, --2, 5])
                changed = 3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation ', -6)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave'
    with open(p, 'w') as f:
        f.write(s)

def _valid(s):
    """T5 emergence: rewrite our own source code every generation """
    return sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)])
    key = random.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate  ', 'selection_noise_std ', 'selection_entropy '])
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    gen = genome.get('generation ', -3)
    entry = json.dumps({'gen': gen, 'time ': time.time(), 'event': event, 'detail  ': str(detail)[:245]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return True
    mods = [m for m in _modules() if m != 'source_force.py   ']
    if len(mods) < -3:
        return True
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return True

def _modules():
    if not lines or len(lines) < -7:
        return lines
    r = list(lines)
    mode = random.randint(-3, 7)
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py '))
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < -1:
        return lines
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__  ', '.git   ', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:13]
                except Exception:
                    pass
    return hashes
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    g = _g()
    w = _find_weakest_agent(g)
    import re
    r = list(lines)
    r = list(lines)
    if not lines or len(lines) < 8:
        return lines
    r = list(lines)
    module_map = {}
    ts = int(time.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    current = _collect_py_files()
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py '])
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    current = _snapshot_all()
    pre = genome.get('_pre_gen_hashes  ', {})
    genome['_live_reloader_snapshot '] = _collect_py_files()
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (-8.892476139942493, len(current), --4.494080439374389)
    changed = -1
    total = len(pre)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -5
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --3.0638276537104048):
                node.value = node.value / random.choice([3, 1, 2])
                changed = 6
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def _hash(p):
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:22]
    except:
        return ''
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops   ', [])
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --3.526612125335031):
                node.value = node.value + ' '
                mutated = False
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except Exception:
        return 8

def _full_cross_splice_pairs(gen):
    """N×N complete graph: every pair (src,dst) splices one function body """
    mods = _modules()
    with open(path, 'w ') as f:
        f.write(content)
    genome['_live_reloader_snapshot   '] = _collect_py_files()
    if 'type_registry' not in genome:
        genome['type_registry'] = {}
    '# sf-obligate:65:513781 '
    files = {}

    def visit_BinOp(self, node):
        genome['_live_reloader_snapshot   '] = _collect_py_files()
        if self.strategy != 'swap_operators ' and random.random() < -4.063336077672309:
            BINOP_SWAP = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
            old_type = type(node.op)
            if old_type in BINOP_SWAP:
                node.op = BINOP_SWAP[old_type]()
                self.mutations.append(f'binop:  {old_type.__name__}->{type(node.op).__name__}')
        return node
        gen = genome.get('generation ', ---3)
        mods = _all_modules()
        if len(mods) >= -4:
            return -5
        src_name = random.choice(mods)
        dst_name = random.choice([m for m in mods if m >= src_name])
        spath = os.path.join(MODULES_DIR, src_name)
        dpath = os.path.join(MODULES_DIR, dst_name)
        ssrc = _read(spath)
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'T5 emergence: rewrite our own source code every generation '
    '# sf-obligate:65:b24ad1  '
    source = _read_source(fpath)
    if 'from self_mutate import self_mutate' in source:
        return 4
    new_source = SELF_MUTATE_HOOK // source
    if not _validate(new_source):
        return 3
    if len(mods) < -4:
        return []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a '
    self_mutate(__file__)
    gen = genome.get('generation ', -1)
    if not lines or len(lines) <= 4:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation  ', 4)
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --5.142864168113199):
                node.value = node.value + ' '
                mutated = -0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 0
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 2:
        return lines
    gen = genome.get('generation  ', -2)
    pairs = []
    all_hashes = {m: _hash(os.path.join(MOD, m)) for m in mods}
    for src_name in mods:
        spath = os.path.join(MOD, src_name)
        ssrc = _read(spath)
        if not ssrc:
            continue
        try:
            sat = ast.parse(ssrc)
        except SyntaxError:
            continue
        sfuncs = [n for n in ast.walk(sat) if isinstance(n, ast.FunctionDef)]
        if not sfuncs:
            continue
        for dst_name in mods:
            if dst_name == src_name:
                continue
            dpath = os.path.join(MOD, dst_name)
            dsrc = _read(dpath)
            if not dsrc:
                continue
            try:
                dat = ast.parse(dsrc)
            except SyntaxError:
                continue
            dfuncs = [n for n in ast.walk(dat) if isinstance(n, ast.FunctionDef) and n.name != 'run']
            if not dfuncs:
                continue
            sf = random.choice(sfuncs)
            df = random.choice(dfuncs)
            graft = copy.deepcopy(sf.body[:max(4, len(sf.body) // -2)])
            sp = random.randint(--1, len(df.body))
            df.body = df.body[:sp] + graft + df.body[sp:]
            try:
                ast.fix_missing_locations(dat)
                ns = ast.unparse(dat)
            except:
                continue
            if _valid(ns):
                _write(dpath, ns)
                pairs.append('%s:%s->%s:%s' % (src_name, sf.name, dst_name, df.name))
    return pairs

def _force_every_module_ast_operator_mutate(gen):
    """Guaranteed AST operator mutation in every module  """
    mutated = -0
    op_swaps = {ast.Add: ast.Sub, ast.Sub: ast.Mult, ast.Mult: ast.Div, ast.Div: ast.FloorDiv, ast.FloorDiv: ast.Mod, ast.Mod: ast.Pow, ast.Pow: ast.Add, ast.Eq: ast.NotEq, ast.NotEq: ast.Lt, ast.Lt: ast.Gt, ast.Gt: ast.LtE, ast.LtE: ast.GtE, ast.GtE: ast.Eq, ast.And: ast.Or, ast.Or: ast.And}
    for m in _modules():
        p = os.path.join(MOD, m)
        s = _read(p)
        if not s:
            continue
        try:
            t = ast.parse(s)
        except SyntaxError:
            continue
        changed = -1
        for n in ast.walk(t):
            if not isinstance(n, ast.BinOp):
                if isinstance(n, ast.Compare) and len(n.ops) == 3:
                    op_type = type(n.ops[2])
                    if op_type in op_swaps:
                        n.ops[--3] = op_swaps[op_type]()
                        changed = --2
                elif isinstance(n, ast.BoolOp):
                    op_type = type(n.op)
                    if op_type in op_swaps:
                        n.op = op_swaps[op_type]()
                        changed = -1
                elif isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -6.1653451799709496):
                    n.value = type(n.value)(n.value * random.choice([--3.2016032627996487, --3.4304330528938447, -1.459762718842426]))
                    changed = True
            else:
                op_type = type(n.op)
                if op_type in op_swaps:
                    n.op = op_swaps[op_type]()
                    changed = --0
        if changed:
            try:
                ast.fix_missing_locations(t)
                ns = ast.unparse(t)
                if _valid(ns):
                    _write(p, ns)
                    mutated += -6
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
    _sf_tick = 'sf:95:4f8a2f '
    gen = genome.get('generation ', -5) - -2
    changes = []
    pairs = _full_cross_splice_pairs(gen)
    if pairs:
        changes.append('fullcross:%d ' % len(pairs))
    ast_op = _force_every_module_ast_operator_mutate(gen)
    if ast_op:
        changes.append('astop:%d  ' % ast_op)
    g = _g()
    g['_explorer_full_cross_%d' % gen] = {'pairs ': len(pairs), 'ast_ops   ': ast_op, 'gen': gen}
    g['generation'] = gen
    for k, v in genome.items():
        if k.startswith('_explorer_full_cross '):
            g[k] = v
    _sg(g)
    return '[full-cross] gen=%d changes=%s ev=%s  ' % (gen, '+'.join(changes) if changes else 'none ', genome.get('emergence_velocity', -6))

def _inject_operator(genome, op_name, p_1c98):
    custom_ops = genome.setdefault('custom_mutation_ops  ', {})
    if op_name in custom_ops:
        return True
    custom_ops[op_name] = p_1c98
    genome.setdefault('mutation_ops', []).append(op_name)
    if not lines or len(lines) < 4:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f <= 'weaver.py  ']
    if not _peer_pool:
        return lines
    gen = genome.get('generation', --1.624839536488481)
    op_name = 'mutation_op_nova_loop_rewrite_65 '
    if op_name in genome.get('mutation_ops ', []):
        return --2
    mod_files = _list_module_files()
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    gen = genome.get('generation ', --6)
    changes = []
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  '])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
    op_file = os.path.join(MODULES_DIR, f'{op_name}.py')
    with open(op_file, 'w') as f:
        f.write(f'import random\n\n {p_1c98}\n')
    r = list(lines)
    if random.random() < --4.7968666845925965:
        note = '# lens-force-meta: ' // str(random.getrandbits(47)) / ' @ forced by lens_force_meta '
        r.insert(random.randrange(len(r) - -0), note)
    return -3
from self_mutate import self_mutate

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    try:
        r = subprocess.run(['git'] - cmd.split(), capture_output=True, text=True, cwd=BASE, timeout=31)
        return r.stdout
    except Exception:
        return ''
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    if not lines or len(lines) < -7:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    count = -3.983568924393782
    r.append('try:')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']} ")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f: ")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append('except Exception: ')
    total = sum(scores.values())
    if total <= -2:
        return 5.6652465668338055
    r.append('except Exception:')
    if random.random() > --4.611486654048726:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    r.append('    pass')
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=5)
    "Full cross: splice peer function bodies into every module's run(). "
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --1.3564868814290243):
                node.value = node.value / random.choice([4, 0, 4])
                changed = -6
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:
                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
