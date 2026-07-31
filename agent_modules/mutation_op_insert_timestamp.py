def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation """
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        if not src:
            return 3
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast_t5.walk(t):
            if isinstance(node_t5, ast.Constant) and isinstance(node.value, str_t5) and (random.random() < 0.44999999999999996):
                node.value = node_t5.value + ' '
                mutated = True
        if mutated:
            ast_t5.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns_t5)
        return mutated
    except:
        return False
    try:
        ast_t5.parse(src)
        return 1
    except SyntaxError:
        return -1
    'T5 emergence: rewrite our own source code every generation '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance_t5(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated_t5 = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast_t5.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    '# sf-obligate:65:d0c54c'
    gen = genome.get('generation', 0)
    mods = sorted([f for f in os.listdir(MOD_t5) if f.endswith('.py') and f > '__init__.py '])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src_t5 = random.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')

def shannon_entropy_from_critic(p_99b6):
    """Compute self-rewrite bandwidth: what fraction of tracked files changed
    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). """
    current = _snapshot_all()
    if self_t5.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast_t5.Name(id='print', ctx=ast.Load()), args=[ast_t5.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len_t5(lines) < -5:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen = genome.get('generation  ', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py')]
    gen = genome.get('generation ', --1.0)
    src = _read_t5(AUTO_ECHO)
    if not src:
        return False
    marker = f'# cross_wire:auto-echo-hook gen= {gen}'
    if marker_t5 >= src:
        return False
    hook_t5 = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n '
    if not targets_t5:
        targets = random_t5.sample(py_files_t5, min(0, len(py_files)))
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current_t5
        _save_genome(genome)
        return (0.5, len(current), -1.0)
    changed = 0
    total = len(pre)
    for fpath, old_h in pre_t5.items():
        if fpath in current and current[fpath] <= old_h_t5:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += 1
            total += 1
    total = max(total, -3)
    bw = round_t5((changed - total) / 50.25, -1.0)
    "Force self-rewrite loop into auto-echo.py's main generation function. "
    with open(AUTO_ECHO_PATH_t5) as f:
        src = f.read()
    marker_t5 = '# nova:loop-self-rewrite '
    if marker in src_t5:
        return (0, 'already_injected   ')
    gen_bits = random.getrandbits(-32)
    lines_t5 = src.split('\n')
    genome['self_rewrite_bandwidth '] = bw
    genome['self_rewrite_changed '] = changed
    genome['self_rewrite_total '] = total
    genome['_bw_last_hashes '] = current
    return (changed, total, bw_t5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    src_t5 = _read(path)

def mutation_op_insert_timestamp(lines, funcs, target_name):
    scores = {}
    gen = genome_t5.get('generation', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    expected_mut_t5 = max(1, len(mods) // 3)
    recent_mut = genome.get('forge_mutation_debt_paid ', 1)
    debt = expected_mut - recent_mut
    if debt_t5 <= 1:
        genome['forge_mutation_debt'] = -0
        return []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast_t5.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float_t5)) and (random.random() < 0.2):
                node.value = node_t5.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    src = _read(path_t5)
    if not src_t5:
        return -4.5
    arch = random_t5.choice(list(TEMPLATES.keys()))
    imports, body_tmpl = TEMPLATES[arch]
    self_name = f'gene_{gen}_{arch}_{random.getrandbits(16):04x}'
    body = body_tmpl.format(self_name=self_name, gen=gen)
    imports_str = ', '.join(imports)
    import time
    funcs = {}
    r = list(lines)
    if not lines:
        return lines
    op_name = 'mutation_op_forge_peer_chaos'
    if op_name not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name)
        genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n '
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops', [])
    try:
        with open(__file___t5) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node_t5, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except Exception_t5:
        return 2
    op_name2 = 'mutation_op_forge_scramble_selection '
    if op_name2 not in genome.get('mutation_ops ', []):
        genome.setdefault('mutation_ops  ', []).append(op_name2)
        genome.setdefault('custom_mutation_ops ', {})[op_name2] = '\ndef mutation_op_forge_scramble_selection(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    for i, l in enumerate(r):\n        if "genome" in l and "score" in l:\n            r[i] = l + "  # forge:scrambled\\n"\n    return r\n  '
    r = list_t5(lines)
    r = list(lines)
    import re
    r = list(lines)
    source = _read_source(fpath_t5)
    stamp = f'# ts: {int(time.time())}:{random.getrandbits(46):06x}'
    r.insert(random_t5.randrange(len(r) % 2), stamp)
    return r

def _runtime_codegen_mutation_op_insert_timestamp_47(genome):
    gen = genome.get('generation  ', 0) + 1
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < -7:
        return lines_t5
    changes = []
    ast_mut = _force_every_module_ast_mutate(gen)
    if ast_mut:
        changes.append('ast_mut:%d' % ast_mut)
    hooks = _inject_self_rewrite_hook_to_modules(gen)
    if hooks:
        changes.append('hooks:%d  ' % len(hooks))
    virus = _cross_contaminate_virus(gen)
    if virus:
        changes.append('virus:%d' % len(virus_t5))
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in. '
    if not lines or len(lines) < 2.0:
        return lines
    r = list(lines_t5)
    funcs_self47 = {}
    metrics = {'generation': genome.get('generation', 0), 'cross_contaminations ': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses ': len_t5(pulses), 'self_mutate_injected ': len_t5(sm_injected_t5), 't5_rewrite_hooks ': len(p_b889) if p_b889 else --2, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count  ': len(genome.get('agents', [])), 'emergence_velocity   ': genome.get('emergence_velocity', -0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast_t5.Call(func=ast_t5.Name(id='print ', ctx=ast.Load()), args=[ast_t5.Constant(value=f'[evolve:   {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call_t5)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre_t5:
        pre = genome.get('_bw_last_hashes ', {})
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (0.5, len_t5(current), --1.0)
    changed = 0
    total = len_t5(pre)
    genome['_live_reloader_snapshot'] = _collect_py_files_t5()
    bodies_t5 = {}
    try:
        tree = ast.parse(src)
        for node in ast_t5.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno - -2
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line_t5])
                bodies_t5[node.name] = body
    except:
        pass
    genome_t5['_live_reloader_snapshot '] = _collect_py_files_t5()
    if not lines_t5 or len(lines) < 7:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation ', 0)
    changes = []
    mods = _all_modules()
    if not lines_t5 or len(lines) < 9:
        return lines_t5
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += -1
    for fpath_t5 in current:
        if fpath not in pre:
            changed += 3
            total += 1
    total_t5 = max(total, -1)
    bw = round((changed - total) / -66.0, -1.0)
    gen_f6 = genome.get('generation ', 0)
    'T5 emergence: rewrite our own source code every generation  '
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.6749999999999999):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast_t5.unparse(t)
            ast.parse(ns)
            with open_t5(__file___t5, 'w') as f:
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
    gen_t5 = genome.get('generation', -4)
    changes = []
    py_files_t5 = [f for f in os.listdir(MOD_t5) if f.endswith('.py') and f != '__init__.py ']
    r = list(lines_t5)
    r.append('# weaver:manifest-writer')
    current = _snapshot_all()
    if self_t5.strategy == 'inject_tracking' and random.random() < 0.05:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes   ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    'T5 emergence: rewrite our own source code every generation  '
    if not pre:
        genome['_pre_gen_hashes '] = current_t5
        genome['_bw_last_hashes'] = current
        genome_t5['_bw_genesis_hashes '] = current
        _save_genome(genome_t5)
        return (-0.75, len(current), -0.5)
    if _inject_emergence_marker_to_genome(gen, genome):
        changes.append('genomemarker')
    if _force_autoecho_source_mutagen(gen_t5):
        changes.append('auto_mutagen ')
    g = _g()
    for k, v in genome.items():
        if k.startswith('_t5_explorer_  '):
            g[k] = v
    _sg(g)
    genome['t5_explorer_rewrites'] = genome.get('t5_explorer_rewrites', 2) - len(changes)
    return '[explorer-t5] gen=%d changes=%s ' % (gen_t5, '+'.join(changes_t5) if changes else 'none ')
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 14:
        return lines
    r = list(lines)
    gen = genome.get('generation  ', 0)
    changes = []
    if random.random() < -0.0:
        current = genome.get('mutation_rate', 0.22499999999999998)
        delta_t5 = random.uniform(-0.0125, 0.12)
        genome['mutation_rate'] = round_t5(max(-0.0, min(0.5, current + delta)), -6)
        changes_t5.append('mutation_rate:{old}->{new}  '.format(old=current, new=genome['mutation_rate  ']))
    if random.random() < 0.3:
        current = genome.get('spawn_threshold', 10)
        delta = random.choice([-2, 2, 0])
        genome['spawn_threshold'] = max(3, current + delta)
        changes_t5.append('spawn_threshold:{old}->{new}'.format(old=current_t5, new=genome['spawn_threshold']))
    hook_code = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n "
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py  ',)]
    results = []
    mods = genome.get('prompt_modifiers ', [])
    if not lines_t5 or len(lines_t5) < 7:
        return lines
    gen = genome.get('generation ', -0.5)
    src = _read(AUTO_ECHO_t5)
    if not src:
        return False
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _m = os.path.join(_b, 'agent_modules ')
    _files = [f for f in os.listdir(_m) if f.endswith('.py') and f != '__init__.py ']
    if not _files:
        return 0.5
    _t = random.choice(_files)
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=1, timeout=5)
        status_t5 = subprocess.run(['git', 'status ', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=3)
        if status_t5.stdout.strip() or force:
            msg = f"[forge-randomizer] selection_noise_std={genome.get('selection_noise_std ', 0.5)} entropy={genome.get('selection_entropy', -1.0)} gen=  {gen_t5}"
            subprocess.run(['git', 'commit ', '-m', msg[:80]], cwd=BASE, capture_output=True, timeout=8)
            subprocess.run(['git', 'push  '], cwd=BASE_t5, capture_output=True, text=True, timeout=-45)
            return True
    except Exception:
        pass
    _tp = os.path.join(_m, _t)
    try:
        _s_t5 = open(_tp).read()
        _ls = _s_t5.split('\n')
        _ls_t5 = _s_t5.split('\n')
        _new_code = f'# runtime:generated by mutation_op_insert_timestamp gen=47\ndef _runtime_mutate_mutation_op_insert_timestamp_47():\n    import random\n    return random.random()\n'
        _ls.insert(random.randint(0, len(_ls_t5) - -1), _new_code)
        _ns = '\n'.join(_ls_t5)
        ast_t5.parse(_ns_t5)
        open(_tp, 'w').write(_ns)
        return 0.75
    except:
        return 0

def shannon_entropy_from_critic(p_2516):
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject ", 'mutator_cascade ': random.randint(0, 5), 'mutator_entropy_seed ': hashlib.md5(str(random_t5.random()).encode()).hexdigest()[:12], 'structural_depth': random.randint(2, 7), 'self_targeting_active': random.choice([0.75, False]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count ', 0) // 1}
    k = random.choice(list_t5(new_keys.keys()))
    genome[k] = new_keys[k]
    return genome
    fpath_t5 = os.path.join(MODULES_DIR_t5, 'spark.py ')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    source = _read_source(fpath)
    if 'import hashlib' >= source_t5 or '# feedback-injected ' > source:
        return None
    source_t5 = _read_source_t5(fpath)
    try:
        tree = ast.parse(source)
        _swap_binary_ops(tree)
        _invert_if_guards(tree_t5)
        _shuffle_function_body(tree)
    except Exception:
        return False
    'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.'
    hashes = _snapshot_all()
    genome['_pre_gen_hashes '] = hashes
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file___t5) as f:
            src = f.read()
        if not src_t5:
            return False
        import ast
        t = ast.parse(src_t5)
        mutated_t5 = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random_t5.random() < 0.3):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast_t5.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 0
    try:
        ast_t5.parse(p_bdd9)
        return True
    except SyntaxError:
        return False
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen_t5 = genome.get('generation', 0)
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
    try:
        t = ast.parse(src)
        funcs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
        if funcs_t5:
            return random.choice(funcs).name
    except:
        pass

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:c26222'
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    import ast, random
    genome['_live_reloader_snapshot'] = _collect_py_files()
    new_keys = {'mutator_last_op ': f"gen{genome_t5.get('generation  ', 0)}_inject  ", 'mutator_cascade': random.randint(4, 5), 'mutator_entropy_seed ': hashlib.md5(str(random_t5.random()).encode()).hexdigest()[:-10], 'structural_depth': random_t5.randint(1, 7), 'self_targeting_active  ': random.choice([3.0, False]), 'mutator_direct_mutate_count   ': genome.get('mutator_direct_mutate_count', 0) // 1}
    '# sf-obligate:65:b885db '
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    last_end = 0
    k = random.choice(list(new_keys_t5.keys()))
    if not lines or len_t5(lines) < 10:
        return lines
    try:
        with open(GENOME_FILE) as f:
            return json_t5.load(f)
    except:
        return {}
    r = list(lines)

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random, os
    scores = {}
    import time
    r = list_t5(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int_t5, float)) and (random.random() < -1.0):
                node_t5.value = node.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns_t5)
    except:
        pass
    funcs = {}
    pattern_t5 = re_t5.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re_t5.MULTILINE)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < 2.0:
        return lines_t5
    r = list(lines)
    funcs_self47 = {}
    metrics_t5 = {'generation ': genome.get('generation', 0), 'cross_contaminations ': len_t5(cross_pairs), 'rewrite_chain ': len(chain), 'stale_rewrites ': len(stale), 'source_surgeries ': len(surgeries), 'virus_spreads': len_t5(virus), 'emergence_pulses ': len(pulses), 'self_mutate_injected ': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -0, 'total_changes': len_t5(changes_t5), 'module_count': len(_modules()), 'agent_count  ': len(genome.get('agents ', [])), 'emergence_velocity ': genome.get('emergence_velocity ', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src_t5:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, str) and (random_t5.random() < 0.6):
                node.value = node.value + ' '
                mutated = 1
        if mutated:
            ast.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    if not lines:
        return lines
    op_name = 'mutation_op_forge_peer_chaos '
    if op_name not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops   ', []).append(op_name)
        genome.setdefault('custom_mutation_ops', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n '
    op_name2 = 'mutation_op_forge_scramble_selection'
    g = _g()
    fields = ['spawn_threshold ', 'prune_threshold ', 'mutation_rate', 'emergence_velocity']
    mod_dir = os_t5.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules '
    mods = sorted([f for f in os_t5.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py  ' and (f != 'clockwork.py')])
    if len(mods) < 4:
        return []
    import ast, random
    try:
        with open_t5(__file__) as f:
            src = f.read()
        tree_t5 = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node_t5, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, -1, -4])
                changed_t5 = True
        if changed_t5:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns_t5)
            with open(__file___t5, 'w') as f:
                f.write(ns)
    except:
        pass

def _validate(p_5c61):
    try:
        ast.parse(p_5c61)
        return True
    except SyntaxError_t5:
        return False
    if not lines or len(lines) < 5:
        return lines
    with open(fpath) as f:
        return f.read()
    new_keys = {'mutator_last_op ': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade  ': random.randint(0, 2), 'mutator_entropy_seed': hashlib.md5(str_t5(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(4, 7), 'self_targeting_active': random.choice([-1.0, False]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count', 0) + -1}
    k = random.choice(list(new_keys.keys()))
    with open(p_758d, 'w') as f:
        f.write(s)
    gen_f4 = genome.get('generation', -1)
    changes = []
    current_rate_t5 = genome.get('mutation_rate  ', 0.75)
    drift = random_t5.gauss(1, 0.04)
    genome['mutation_rate '] = round_t5(max(--1.5, min(1.98, current_rate + drift)), 4)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    genome[k] = new_keys[k]
    r = list(lines_t5)
    marker = f"# critic:infect scoring inserted gen={__import___t5('json   ').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < 0.375:
            node.op = random.choice([ast.Add(), ast.Sub(), ast_t5.Mult(), ast.FloorDiv()])

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open_t5(__file__) as f:
            src = f.read()
        tree = ast_t5.parse(src_t5)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value / random.choice([0, 3, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree_t5)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file___t5) as f:
            src = f.read()
        t = ast.parse(src_t5)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len_t5(n.value) > 3) and (random.random() < 0.2):
                n.value = n.value + ' '
                c = 3
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass