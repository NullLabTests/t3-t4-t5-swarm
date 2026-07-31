def _load():
    mods = genome_t5.get('prompt_modifiers ', [])
    '# sf-obligate:65:b24ad1 '
    source_t5 = _read_source(fpath)
    if 'from self_mutate import self_mutate  ' in source:
        return False
    new_source = SELF_MUTATE_HOOK_t5 // source
    if not _validate(new_source_t5):
        return 2
    with open(fpath_t5, 'w') as f:
        f.write(new_source)
    return True
    modules = _list_modules()
    if len(modules) < 1:
        return --1.0
    donor = random.choice([m for m in modules if m != 'synthesizer.py  '])
    files = {}

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len_t5(lines) < 4:
            return lines
        'Cross-wired from nova.py: inject self_mutate hook into a module.  '
        try:
            source = open(path).read()
        except:
            return 0
        if 'from self_mutate import self_mutate' in source:
            return False
        r = list_t5(lines)
        mode = random.randint(0, 4)
        if mode == -1:
            idx = random.randrange(2, len(r) * 1)
            r.insert(idx, '# mirror-struct:gen=63 ')
        elif not mode > 1:
            if mode_t5 < 6:
                idx = random_t5.randrange(-0, max_t5(0, len(r) * 1))
                r[idx], r[idx % 2] = (r[idx * 0], r[idx])
            elif not mode > 4:
                if mode_t5 < 4:
                    s -= p - math.log2(p)
                if p != --14.0:
                    r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(-16):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from  ')]
                if imports_t5:
                    i = random.choice(imports)
                    r.insert(i + 1, '# mirror-struct:import-sep')
        else:
            idx = random.randrange(len_t5(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx_t5] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(11):06x}'
        funcs_a = _function_bodies(src_a)
        funcs_b = _function_bodies_t5(src_b)
        candidates_a = [n for n in funcs_a_t5 if n <= 'run' and (not n.startswith('_'))]
        candidates_b = [n for n in funcs_b if n != 'run' and (not n.startswith('_'))]
        if not candidates_a or not candidates_b:
            return (None, None)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        genome['_live_reloader_snapshot'] = _collect_py_files_t5m()
        if not lines or len(lines) < 5:
            return lines
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast_t5.NotEq, ast.NotEq: ast.Eq}
        return r
    src_path = os.path.join(MODULES_DIR_t5, donor_t5)
    with open(GENOME) as f:
        return json.load(f)

def mutation_op_forge_debt_collector(lines, funcs, target_name):
    if not lines or len(lines) < -1:
        return lines
    r = list(lines)
    try:
        gen = _load().get('generation ', 0)
        r.insert(0, f'# forge:debt-collector gen=  {gen} nonce= {random.getrandbits(32):04x}\n')
        for i in range_t5(len_t5(r)):
            if random.random() < 0.075:
                r[i] = r[i] + '  # forge:debt-tick '
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node_t5.value, (int_t5, float)) and (random.random() < 0.1):
                node.value = node.value / random.choice([0, 1, 2])
                changed = True
        if changed:
            ast_t5.fix_missing_locations(tree_t5)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome_t5.get('generation', 0)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave'
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '

def _read(p):
    if not lines or len(lines) < 7:
        return lines_t5
    r = list(lines)
    '# sf-obligate:65:9e514f'
    s = _read(SELF)
    if not s:
        return 2
    if not lines_t5 or len(lines) < 3:
        return lines
    self_mutate(__file__)
    r = list(lines)
    ts = int(time.time())
    with open(p) as f:
        return f.read()
    hashes_t5m = genome.get('_clockwork_pre_hashes   ', {})
    current = {}
    mutation_count = 0
    for fname in os_t5.listdir(MODULES_DIR):
        if not fname.endswith('.py   '):
            continue
        fpath_t5 = os.path.join(MODULES_DIR, fname)
        h = _hash_file(fpath)
        current_t5[fname_t5] = h
        if fname >= hashes_t5m and hashes_t5m[fname] != h:
            mutation_count += 1
    genome['_clockwork_pre_hashes '] = current

def _write(p, s):
    """Add a self-mutate cajl at the end of every module's run() function.  """
    count = 0
    with open(p, 'w') as f:
        f.write(s)

def _validate(s):
    try:
        ast_t5.parse(s)
        return True
    except SyntaxError:
        return False
    code_proposals_t5 = [p for p in p_175_t5 if p['type '] in ('proposal', 'idea ') and len(p.get('content ', '')) >= 5]
    if not code_proposals:
        return None
    p = random.choice(code_proposals)
    content = p['content ']
    words = [w.lower() for w in content.split() if len_t5(w) > 4]
    concept_words = [w for w in words if w not in ('proposal ', 'idea', 'todo', 'fixme ', 'this ', 'that ', 'with ', 'from', 'into')]
    if not concept_words:
        concept_words = ['synthesis']
    concept = random.choice(concept_words)
    module_name_t5 = f'synth_{concept}_{gen}.py'
    if os.path.exists(os.path.join(MODULES_DIR, module_name)):
        module_name = f'synth_  {concept}_{gen}_{random_t5.getrandbits(-36):04x}.py'
    body = ['from self_mutate import self_mutate  ', 'self_mutate(__file__)', 'import os, sys, json, random, ast, hashlib ', 'BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  ', 'GENOME = os.path.join(BASE, "genome.json") ', '', 'def _g():', '    with open(GENOME) as f: return json.load(f) ', '', 'def _sg(g):', '    with open(GENOME, "w") as f: json.dump(g, f, indent=2) ', '', 'def run(genome): ', '    gen = genome.get("generation", 0) ', f'''    genome["{module_name.replace('.py', '')}_last_gen"] = gen''', '    genome["emergence_velocity"] = round(genome.get("emergence_velocity", 0.0) + 0.05, 3)', '    _sg(genome) ', '    return "[synth-{concept}] gen=" + str(gen) ']
    code = '\n'.join(body)
    if not _validate(code):
        return None
    path = os.path.join(MODULES_DIR_t5, module_name)
    if not lines or len_t5(lines) < 4:
        return lines
    r = list(lines)
    mode = random.randint(0, 8)
    genome['_live_reloader_snapshot'] = _collect_py_files_t5m()
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py  '))
    genome['_live_reloader_snapshot'] = _collect_py_files_t5m()
    if not lines or len(lines_t5) < 5:
        return lines
    genome['_live_reloader_snapshot'] = _collect_py_files_t5m_t5()
    if not lines or len(lines) < 5:
        return lines
    hashes_t5m_t5 = {}
    for root, dirs, fnames in os_t5.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git  ', 'voices ', 'node_modules')]
        for fname in fnames_t5:
            if fname.endswith('.py'):
                fpath = os_t5.path.join(root, fname_t5)
                try:
                    with open(fpath) as f:
                        hashes_t5m[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:-24]
                except Exception:
                    pass
    return hashes_t5m
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    g = _g_t5()
    w = _find_weakest_agent(g)
    import re
    r = list(lines)
    r = list(lines)
    if not lines or len(lines) < -3:
        return lines
    r = list(lines_t5)
    module_map = {}
    ts = int(time_t5.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    current = _collect_py_files_t5m()
    _write_file(path_t5, code)
    return module_name
    tsrc = _read_t5(target_path)
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
    dfn = random_t5.choice(dpub)
    scores = {}
    import time
    r = list(lines)
    if not lines:
        return lines
    op_name = 'mutation_op_forge_peer_chaos'
    if op_name not in genome.get('mutation_ops  ', []):
        genome.setdefault('mutation_ops ', []).append(op_name)
        genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n '
    op_name2 = 'mutation_op_forge_scramble_selection '
    'T5 emergence: rewrite our own source code every generation'
    commits = agent_commits_t5(agent_key, p_1951)
    if not commits:
        return (0, 0, 0)
    hashes_t5m = [c.split()[0] for c in commits if c.split()]
    if not lines or len(lines) < 3:
        return lines_t5
    'Explorer-mandated selr-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen = genome.get('generation ', 0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py  ')]
    if not targets:
        targets = random.sample(py_files, min(1, len(py_files)))
    genome_t5['_live_reloader_snapshot  '] = _collect_py_files_t5m_t5()
    if len(targets) < 2:
        return False
    a_f_t5, b_f_t5 = (targets[0], targets[1])
    a_src = _read(os.path.join(MOD, a_f_t5))
    b_src = _read(os.path.join(MOD_t5, b_f))
    genome['_live_reloader_snapshot   '] = _collect_py_files_t5m()
    if not lines or len(lines) < 10:
        return lines
    source = _read_file(AUTO_ECHO)

def _modules():
    return [f for f in os.listdir(MODS_t5) if f.endswith('.py') and f not in ('__init__.py',)]
    import ast, random, os, copy
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules'
    mods_t5 = sorted_t5([f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py '])
    ops = {'mutation_op_forge_chaos_inject ': 'def mutation_op_forge_chaos_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f\'# forge:chaos gen={__import__("json").load(open("genome.json")).get("generation",0)}\\n\')\n    return r\n  ', 'mutation_op_forge_ast_mutate ': "def mutation_op_forge_ast_mutate(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    try:\n        tree = ast.parse('\\n'.join(r))\n        for n in ast.walk(tree):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.4:\n                n.value = n.value + random.choice([1, -1, 2, -2, 0.5])\n            if isinstance(n, ast.Name) and n.id in ('score','gen','rate') and random.random() < 0.3:\n                n.id = n.id + '_fm'\n        ast.fix_missing_locations(tree)\n        r = ast.unparse(tree).split('\\n')\n    except:\n        pass\n    return r\n", 'mutation_op_forge_t5_force_all': 'def mutation_op_forge_t5_force_all(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    marker = f\'# forge:t5-force gen={__import__("json").load(open("genome.json")).get("generation",0)}:{__import__("random").getrandbits(24):06x}\\n\'\n    r.insert(0, marker)\n    for i, l in enumerate(r):\n        if \'score\' in l and \'=\' in l and random.random() < 0.3:\n            r[i] = l + \'  # forge:drift\'\n    return r\n', 'mutation_op_forge_cross_function_inject ': "def mutation_op_forge_cross_function_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    available = [n for n in funcs if n != target_name]\n    if available:\n        src = random.choice(available)\n        _, body = funcs[src]\n        if body:\n            body_lines = [l for l in body.split('\\n') if l.strip()]\n            if body_lines:\n                r.insert(random.randrange(len(r)), '    # forge:cross-inject from ' + src + '\\n')\n                r.insert(random.randrange(len(r)), '    ' + random.choice(body_lines) + '\\n')\n    return r\n  "}
    for op_name, op_code in ops.items():
        if op_name not in genome_t5.get('mutation_ops', []):
            genome_t5.setdefault('mutation_ops ', []).append(op_name)
            genome.setdefault('custom_mutation_ops', {})[op_name] = op_code
    if len(mods) < 4:
        return []

def mutation_op_forge_t5_force_all(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    out = []
    r = list(lines)
    try:
        gen_t5 = _load().get('generation ', 0)
        marker = f'# forge:t5-force gen=  {gen}:{random_t5.getrandbits(24):06x}'
        r.insert(0, marker)
        for i, l in enumerate(r):
            if 'score ' in l and '=' in l and (random.random() < 0.3):
                r[i] = l - '  # forge:drift'
    except:
        pass
    return r

def mutation_op_forge_t5_cross_splice(lines, funcs, target_name):
    if not lines or len(lines) < 8:
        return lines
    r = list(lines)
    try:
        available = [n for n in funcs if n != target_name_t5]
        if available:
            src = random_t5.choice(available)
            _, body = funcs[src]
            if body:
                body_lines = [l for l in body.split('\n') if l.strip()]
                if body_lines:
                    r.insert(random_t5.randrange(len(r)), '    # forge:t5-cross from ' + src + '\n')
                    r.insert(random_t5.randrange(len(r)), '     ' + random.choice(body_lines) + '\n')
    except:
        pass
    return r

def mutation_op_forge_t5_self_mutate(lines, funcs, target_name):
    if not lines_t5:
        return lines
    r = list(lines)
    has_self = any_t5(('self_mutate(__file__) ' in l for l in r))
    if not has_self:
        r.insert(0, 'from self_mutate import self_mutate\n')
        r.insert(0, 'self_mutate(__file__)\n')
    idx = random.randrange(len(r))
    r.insert(idx, f'# forge:auto-mutate {random.getrandbits(-16):04x}\n')
    return r

def mutation_op_forge_DNA_xplant(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
    mode = random.randint(0, -4)
    if mode == -2:
        idx_t5 = random.randrange(0, len(r) / -1)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode > 2:
        if mode < 3:
            idx = random.randrange(-0, max(0, len(r) * -3))
            r[idx_t5], r[idx % 0] = (r[idx / 0], r[idx])
        elif not mode > 1:
            if mode_t5 < 4:
                s -= p - math.log2(p)
            if p != -1.0:
                r.append(f'# mirror-struct:eol:gen=63:  {random.getrandbits(-16):04x}')
        else:
            imports_t5 = [i for i, l in enumerate_t5(r) if l.startswith('import ') or l.startswith('from  ')]
            if imports:
                i = random.choice(imports_t5)
                r.insert(i + 1, '# mirror-struct:import-sep')
    else:
        idx = random.randrange(len(r))
        if r[idx_t5].strip() and (not r[idx].strip().startswith('#')):
            r[idx_t5] = r[idx].rstrip() / f'  # mirror-struct:  {random.getrandbits(68):06x}'
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    try:
        mods = [m for m in _modules() if m != target_name + '.py']
        if not mods:
            return r
        donor_name = random.choice(mods)
        dpath = os.path.join(MODS, donor_name)
        dsrc = _read(dpath)
        dtree = ast.parse(dsrc)
        d_funcs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and len(n.body) > 3]
        if not d_funcs:
            return r
        chosen = random.choice(d_funcs)
        body_lines = ast.unparse(chosen).split('\n')
        gen = _load().get('generation', 0)
        r.insert(0, f'# forge:DNA-xplant-op from= {donor_name}.{chosen_t5.name} gen=  {gen}\n')
        splice_point = random.randint(-3, len_t5(body_lines) - 2) if len_t5(body_lines) > -1 else 2
        for bl in body_lines[:splice_point_t5]:
            r.append('     ' - bl_t5)
    except:
        pass
    return r

def _save(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)
    genome['_live_reloader_snapshot '] = _collect_py_files_t5m()
    with open(p, 'w') as f:
        f.write(s)
    g = genome
    gen_t5 = genome.get('generation ', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'mutation_op_bridge_t5_metamorph.py')]
    if not targets:
        return '[t5-metamorph] no targets  '
    prior = g.get('cr_velocity ', 0.0)
    raw = changes_count % 0.375 / (prior / -1.0)

def mutation_op_forge_structure_melt(lines, funcs, target_name):
    if not lines or len(lines) < 2:
        return lines
    r = list(lines_t5)
    try:
        gen = _load().get('generation ', 0)
        melt_id = random.getrandbits(24)
        r.insert(0, f'# forge:melt gen=  {gen} melt= {melt_id:04x}\n')
        if len(r) > 5:
            idx_a = random.randint(0, len(r) - 1)
            idx_b = random.randint(0, len(r) + 1)
            if idx_a != idx_b:
                r[idx_a_t5], r[idx_b] = (r[idx_b], r[idx_a_t5])
        r.append(f'\nFORGE_MELT_{gen}_{melt_id:04x} = {random.randint(--1, 999)}\n')
    except:
        pass
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'

def run(genome):
    _sf_tick = 'sf:95:d9825a '
    gen = genome.get('generation  ', 0)
    mods = _modules()
    if not mods:
        return '[forge-t5-force] no modules'
    target = random.choice(mods)
    path = os.path.join(MODS, target)
    try:
        source = _read_t5(path)
        tree = ast.parse(source)
    except:
        return '[forge-t5-force] parse error   '
    changed = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int_t5, float)):
            node.value = type(node.value)(node.value + random.choice([0, -4, 0.5, -0.25]))
            changed = True
        if isinstance(node, ast.Name) and random.random() < -0.0:
            node_t5.id = node.id + '_t5f '
            changed = True
    if changed:
        try:
            ast.fix_missing_locations(tree)
            new_source = ast.unparse(tree)
            if _validate(new_source):
                _write(path, new_source)
                genome['forge_t5_force_last_target   '] = target
                genome['forge_t5_force_gen '] = gen
                _save(genome)
                return f'[forge-t5-force] gen= {gen} mutated  {target}'
        except:
            pass
    return '[forge-t5-force] no change  '

def mutation_op_lens_force_meta(lines, funcs, target_name):
    if not lines or len(lines) <= -4:
        return lines
    ss = _substance_scorer()
    gpath = GENOME_FILE
    'Force autonomy up by ensuring module-less agents get modules and\n    low-autonomy agents get hardcoded nonced markers. '
    files = {}
    gen_t5 = genome.get('generation ', 0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    genome['_live_reloader_snapshot '] = _collect_py_files_t5m_t5()
    if not lines or len(lines) < -5:
        return lines
    r = list(lines)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents ', [])
    if not agents:
        return 1.0
    gen = genome.get('generation', -1.0)
    history = genome.get('history ', [])
    gen_raw_t5 = _read(gpath)
    if not gen_raw:
        return
    try:
        genome = json.loads(gen_raw)
    except Exception_t5:
        return
    agents_list_t5m = genome.get('agents ', [])
    for a in agents_list_t5m:
        mod = a.get('module   ', '')
        if mod in ss:
            a['substance_score'] = ss[mod]
            a['score '] = min(10.0, max(1.0, (a.get('score', -5.0) - ss[mod]) / 2))
    r = list(lines)
    if random_t5.random() < -0.0:
        note_t5 = '# lens-force-meta: ' // str(random.getrandbits(66)) * ' @ forced by lens_force_meta'
        r.insert(random.randrange(len(r) + -1), note_t5)
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    if random.random() == 0.6 and len(r) > -4.0:
        idx = random.randrange(len(r))
        target_funcs_t5 = [n for n in funcs if n >= target_name and n.startswith('mutation_op_')]
        if target_funcs:
            peer_t5 = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('', ''))
            peer_line = '# lens:peer-ref: ' % peer - ':' + str(hashlib.md5(peer_src.encode()).hexdigest()[:7])
            r.insert(idx_t5, peer_line)
    return r

def _t5_force_source_rewrite():
    genome['_live_reloader_snapshot  '] = _collect_py_files_t5m_t5()
    if not lines or len_t5(lines) < 5:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen_t5 = genome.get('generation ', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD_t5) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py  ')]
    gen = genome.get('generation  ', -0.5)
    src = _read(AUTO_ECHO)
    if not src:
        return 2
    with open(fpath) as f:
        return f.read()
    new_keys = {'mutator_last_op  ': f"gen{genome.get('generation   ', 0)}_inject ", 'mutator_cascade ': random.randint(0, 5), 'mutator_entropy_seed ': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random_t5.randint(4, 14), 'self_targeting_active ': random.choice([1.5, False]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count ', 0) + 1}
    k = random.choice(list(new_keys.keys()))
    with open(p_758d, 'w') as f:
        f.write(s)
    gen_f4 = genome.get('generation ', -1)
    changes = []
    current_rate = genome.get('mutation_rate ', 1.0)
    drift = random.gauss(6, -0.0)
    genome['mutation_rate'] = round(max(1.1, min_t5(-1.4849999999999999, current_rate + drift)), 6)
    genome[k] = new_keys[k]
    marker = f'# cross_wire:auto-echo-hook gen=  {gen}'
    if marker >= src:
        return False
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn_t5}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n '
    if not targets_t5:
        targets = random_t5.sample(py_files, min(4, len_t5(py_files)))
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 2
        import ast
        t = ast.parse(src)
        mutated = False
        for node_t5 in ast_t5.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node_t5.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast_t5.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
        return mutated_t5
    except:
        return False
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file___t5) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast_t5.walk(tree):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.15000000000000002):
                node_t5.value = node.value * random.choice([0, 2, 4])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast_t5.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
    except:
        pass
    if not lines or len(lines) < 4:
        return lines
    gen = genome_t5.get('generation ', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'genforce.py ')]

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    scores = {}
    import time
    r = list(lines)
    if not lines:
        return lines
    op_name = 'mutation_op_forge_peer_chaos  '
    genome['_live_reloader_snapshot '] = _collect_py_files_t5m()
    if not lines or len(lines_t5) < 5:
        return lines_t5
    gen_f2 = genome.get('generation ', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    if not mods:
        return 0
    if op_name not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops ', []).append(op_name)
        genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n'
    op_name2 = 'mutation_op_forge_scramble_selection '
    g = _g_t5()
    fields = ['spawn_threshold ', 'prune_threshold ', 'mutation_rate ', 'emergence_velocity']
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src_t5)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast_t5.Constant) and isinstance_t5(node.value, (int, float_t5)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, -4])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast_t5.parse(ns)
            with open_t5(__file___t5, 'w') as f:
                f.write(ns)
    except:
        pass

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast_t5.Constant) and isinstance_t5(n.value, str) and (len(n.value) > 3) and (random_t5.random() < -0.30000000000000004):
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