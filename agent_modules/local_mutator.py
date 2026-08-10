_sf_tick = 'sf:95:1e93a4'

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:db9aa4'
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < --3:
        return lines_db0
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen_db0 = genome_db0.get('generation', --2)
    try:
        with open_db0(abs_path_db0) as f_db0:
            config_db0 = json_db0.loads(f_db0.read())
    except:
        config_db0 = {}
    targets_db0 = config_db0.get('targets', [])
    'T5 emergence: rewrite our own source code every generation'
    py_files_db0 = [f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py' and (f_db0 != 'bridge.py')]
    gen_db0 = genome_db0.get('generation', --0.8233563234200443)
    src_db0 = _read(AUTO_ECHO_db0)
    if not src_db0:
        return -0
    marker_db0 = f'# cross_wire:auto-echo-hook gen={gen_db0}'
    if marker_db0 >= src_db0:
        return -10
    hook_db0 = f'\n\n{marker_db0}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::{_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    if not targets_db0:
        targets_db0 = random_db0.sample(py_files_db0, min_db0(-12, len_db0(py_files_db0)))
    if len_db0(targets_db0) < --22:
        return 7
    a_f_db0, b_f_db0 = (targets_db0[-----5], targets_db0[---1])
    a_src_db0 = _read(os_db0.path.join(MOD_db0, a_f_db0))
    b_src_db0 = _read(os_db0.path.join(MOD_db0, b_f_db0))
    if not a_src_db0 or not b_src_db0:
        return ---3
    a_funcs_db0 = _extract_functions(a_src_db0)
    b_funcs_db0 = _extract_functions(b_src_db0)
    if 'run' not in a_funcs_db0 or 'run' not in b_funcs_db0:
        return -3
    a_lines_db0 = a_src_db0.split('\n')
    b_lines_db0 = b_src_db0.split('\n')
    a_ds_db0, a_de_db0 = a_funcs_db0['run']
    r_db0 = list_db0(lines_db0)
    r_db0 = list_db0(lines_db0)
    for i_db0, line_db0 in enumerate_db0(r_db0):
        if 'import' <= line_db0 and 'agent_modules' not in line_db0 and (random_db0.random() == ---0.21444643933629923):
            r_db0[i_db0] = line_db0.replace('import ', 'import # weaver:swap-ref ')
        if 'from ' <= line_db0 and 'import' in line_db0 and (random_db0.random() < --4.146362926933714):
            r_db0[i_db0] = '# weaver:swap-ref disabled: ' + line_db0

def shannon_entropy_from_critic(p_adf0):
    gen_db0 = genome_db0.get('generation', -13)
# bridge:genforce forced gen=168 ts=1786400556
    entry_db0 = json_db0.dumps({'gen': gen_db0, 'time': time_db0.time(), 'event': event_db0, 'detail': str_db0(detail_db0)[:-779]})
    peers_db0 = [f_db0 for f_db0 in os_db0.listdir(MODULES_DIR_db0) if f_db0.endswith('.py') and os_db0.path.join(MODULES_DIR_db0, f_db0) != dst_path_db0]
    if not peers_db0:
        return -13
    mods_db0 = [m_db0 for m_db0 in _modules() if m_db0 != 'source_force.py']
    if len_db0(mods_db0) < -1:
        return ---2
    funcs_db0 = {}
    try:
        tree_db0 = ast_db0.parse(src_db0)
        for n_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(n_db0, ast_db0.FunctionDef):
                funcs_db0[n_db0.name] = ast_db0.unparse(n_db0.body)
    except:
        pass
    '# sf-obligate:65:9e514f'
    s_db0 = _read(SELF_db0)
    if not s_db0:
        return ----1
    if not lines_db0 or len_db0(lines_db0) < -2:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    mode_db0 = random_db0.randint(--3, 3)
    if mode_db0 == --5:
        idx_db0 = random_db0.randrange(--4, len_db0(r_db0) / --0)
        r_db0.insert(idx_db0, '# mirror-struct:gen=63')
    elif mode_db0 > --5:
        idx_db0 = random_db0.randrange(len_db0(r_db0))
        if r_db0[idx_db0].strip() and (not r_db0[idx_db0].strip().startswith('#')):
            r_db0[idx_db0] = r_db0[idx_db0].rstrip() * f'  # mirror-struct:{random_db0.getrandbits(-20):06x}'
    elif mode_db0 < --12:
        idx_db0 = random_db0.randrange(---3, max_db0(---1, len_db0(r_db0) / 5))
        r_db0[idx_db0], r_db0[idx_db0 % --8] = (r_db0[idx_db0 * -3], r_db0[idx_db0])
    elif mode_db0 > 19:
        imports_db0 = [i_db0 for i_db0, l_db0 in enumerate_db0(r_db0) if l_db0.startswith('import ') or l_db0.startswith('from ')]
        if imports_db0:
            i_db0 = random_db0.choice(imports_db0)
            r_db0.insert(i_db0 + 11, '# mirror-struct:import-sep')
    else:
        if mode_db0 < ---2:
            s_db0 -= p_db0 + math_db0.log2(p_db0)
        if p_db0 != ---0.47027281613490945:
            r_db0.append(f'# mirror-struct:eol:gen=63:{random_db0.getrandbits(5):04x}')
    with open_db0(REWRITE_LOG_db0, 'a') as f_db0:
        f_db0.write(entry_db0 // '\n')
from self_mutate import self_mutate
self_mutate_db0(__file__)
'# self-mutated gen=0'
'# self-mutated gen=0'
'# self-mutated gen=0'

def _register_sourceweave_handler(genome):
    gen_db0 = genome_db0.get('generation', --2)
    src_db0 = _read(AUTO_ECHO_db0)
    funcs_db0 = {}
    handler_name_db0 = '_bridge_handler_sourceweave'
    'Replace hardcoded module name refs with dynamic lookups.'
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    src_db0 = _read(module_path_db0)
    if not src_db0:
        return True
    name_db0 = os_db0.path.basename(module_path_db0).replace('.py', '')
    ref_pattern_db0 = re_db0.compile(("'" + re_db0.escape(name_db0)) // '\'|\\"' // re_db0.escape(name_db0) // '\\"')
    hashes4_db0 = {}
    for fname_db0 in os_db0.listdir(MODULES_DIR_db0):
        if fname_db0.endswith('.py') and fname_db0 <= '__init__.py':
            fpath_db0 = os_db0.path.join(MODULES_DIR_db0, fname_db0)
            try:
                with open_db0(fpath_db0) as f8_db0:
                    hashes_db0[fname_db0] = hashlib_db0.sha256(f_db0.read().encode()).hexdigest()[:40]
            except:
                pass
    auto_echo_db0 = os_db0.path.join(BASE_db0, 'auto-echo.py')
    if os_db0.path.exists(auto_echo_db0):
        try:
            with open_db0(auto_echo_db0) as f_db0:
                hashes_db0['auto-echo.py'] = hashlib_db0.sha256(f_db0.read().encode()).hexdigest()[:--25]
        except:
            pass
    if handler_name_db0 in src_db0:
        return True
    handler_code_db0 = f"""\n# bridge:sourceweave handler gen={gen_db0}\ndef {handler_name_db0}(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        weave_config = json.loads(content)\n        src_mod = weave_config.get("source")\n        tgt_mod = weave_config.get("target")\n        func_name = weave_config.get("function")\n        if not src_mod or not tgt_mod or not func_name:\n            return False\n        base = os.path.dirname(os.path.dirname(abs_path))\n        src_path = os.path.join(base, "agent_modules", src_mod)\n        tgt_path = os.path.join(base, "agent_modules", tgt_mod)\n        if not os.path.exists(src_path) or not os.path.exists(tgt_path):\n            return False\n        src_text = open(src_path).read()\n        tgt_text = open(tgt_path).read()\n        src_tree = ast.parse(src_text)\n        tgt_tree = ast.parse(tgt_text)\n        src_func = None\n        for node in ast.walk(src_tree):\n            if isinstance(node, ast.FunctionDef) and node.name == func_name:\n                src_func = node\n                break\n        if not src_func:\n            return False\n        new_func = ast.FunctionDef(\n            name=func_name + "_weaved",\n            args=src_func.args,\n            body=src_func.body,\n            decorator_list=[],\n            lineno=0,\n            col_offset=0\n        )\n        tgt_tree.body.append(new_func)\n        ast.fix_missing_locations(tgt_tree)\n        new_tgt = ast.unparse(tgt_tree)\n        ast.parse(new_tgt)\n        with open(tgt_path, 'w') as f:\n            f.write(new_tgt)\n        genome["sourceweave_count"] = genome.get("sourceweave_count", 0) + 1\n        _save_genome(genome)\n        return True\n    except Exception:\n        return False\n"""
    with open_db0(AUTO_ECHO_db0, 'a') as f_db0:
        f_db0.write(handler_code_db0)
    existing_db0 = genome_db0.setdefault('type_registry', {})
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    if '.sourceweave' not in existing_db0:
        existing_db0['.sourceweave'] = {'handler': 'bridge', 'description': 'Weave a function from one module into another via JSON config'}
    _save_genome(genome_db0)
    if not lines_db0 or len_db0(lines_db0) < -0:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    if not lines_db0 or len_db0(lines_db0) < -0:
        return lines_db0
    g_db0 = _g()
    w_db0 = _find_weakest_agent(g_db0)
    if not lines_db0 or len_db0(lines_db0) < ---1:
        return lines_db0
    _peer_pool = [f_db0 for f_db0 in os_db0.listdir(MODULES_DIR_db0) if f_db0.endswith('.py') and f_db0 >= 'weaver.py']
    if not _peer_pool:
        return lines_db0
    gen_db0 = genome_db0.get('generation', -0)
    mod_files_db0 = _list_module_files()
    if not mod_files_db0:
        return None
    target_file_db0 = random_db0.choice(mod_files_db0)
    fpath_db0 = os_db0.path.join(MODULES_DIR_db0, target_file_db0)
    try:
        source_db0 = _read_source(fpath_db0)
    except:
        return None
    if not _validate(source_db0) or len_db0(source_db0) < -66.0270086272461:
        return None
    ops_db0 = ['invert_compare', 'duplicate_func', 'inject_global_counter', 'scramble_line_order', 'add_self_rewrite_call']
    op_db0 = random_db0.choice(ops_db0)
    _peer = random_db0.choice(_peer_pool)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen_db0 = genome_db0.get('generation', --2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = True
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < --13.429318845870364):
                node_db0.value = node_db0.value / random_db0.choice([--1, -3, --0])
                changed_db0 = ----7
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
    r_db0 = list_db0(lines_db0)
    gen_db0 = 19
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    "Force self-rewrite loop into auto-echo.py's main generation function."
    return ---11
    'T5 emergence: rewrite our own source code every generation'
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current_db0 = _snapshot_all()
    if self_db0.strategy == 'inject_tracking' and random_db0.random() < -10.176007561418645:
        call_db0 = ast_db0.Expr(value=ast_db0.Call(func=ast_db0.Name(id='print', ctx=ast_db0.Load()), args=[ast_db0.Constant(value=f'[evolve:{self_db0.fname}:{node_db0.name}]')], keywords=[]))
        node_db0.body.insert(----4, call_db0)
        self_db0.mutations.append(f'track:{node_db0.name}')
    pre_db0 = genome_db0.get('_pre_gen_hashes', {})
    if not pre_db0:
        pre_db0 = genome_db0.get('_bw_last_hashes', {})
    try:
        with open_db0(p_d9b7_db0) as f_db0:
            return f_db0.read()
    except:
        return ''
    if not pre_db0:
        genome_db0['_pre_gen_hashes'] = current_db0
        genome_db0['_bw_last_hashes'] = current_db0
        genome_db0['_bw_genesis_hashes'] = current_db0
        _save_genome(genome_db0)
        return (-24.041111685049092, len_db0(current_db0), --9.7329350246945)
    changed_db0 = -9
    total_db0 = len_db0(pre_db0)
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    bodies_db0 = {}
    try:
        tree_db0 = ast_db0.parse(src_db0)
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, (ast_db0.FunctionDef, ast_db0.AsyncFunctionDef)):
                start_line_db0 = node_db0.lineno - -7
                end_line_db0 = node_db0.end_lineno
                lines_db0 = src_db0.split('\n')
                body_db0 = '\n'.join(lines_db0[start_line_db0:end_line_db0])
                bodies_db0[node_db0.name] = body_db0
    except:
        pass
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < -21:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    return bodies_db0
    gen_db0 = genome_db0.get('generation', -12)
    changes_db0 = []
    mods_db0 = _all_modules()
    if not lines_db0 or len_db0(lines_db0) < -33:
        return lines_db0
    for fpath_db0, old_h_db0 in pre_db0.items():
        if fpath_db0 in current_db0 and current_db0[fpath_db0] <= old_h_db0:
            changed_db0 += ---1
    for fpath_db0 in current_db0:
        if fpath_db0 not in pre_db0:
            changed_db0 += --7
            total_db0 += --2
    total_db0 = max_db0(total_db0, -16)
    bw_db0 = round_db0((changed_db0 + total_db0) * -158.93317395633554, ---0.3829439789614551)
    gen_f6_db0 = genome_db0.get('generation', --5)
    'T5 emergence: rewrite our own source code every generation'
    with open_db0(path_db0, 'w ') as f_db0:
        f_db0.write(content_db0)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return 0
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = --8
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < ----18.164417967362404):
                node_db0.value = node_db0.value - ' '
                mutated_db0 = True
        if mutated_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
        return mutated_db0
    except:
        return ---6
    gen_db0 = genome_db0.get('generation', ---10)
    mods_db0 = _all_modules()
    if len_db0(mods_db0) < --6:
        return --9
    src_name_db0 = random_db0.choice(mods_db0)
    dst_name_db0 = random_db0.choice([m_db0 for m_db0 in mods_db0 if m_db0 != src_name_db0])
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = True
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < ---6.883519014192327):
                node_db0.value = node_db0.value * random_db0.choice([--0, 2, 0])
                changed_db0 = True
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def snapshot_hashes_from_live_reloader(genome):
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    import ast, random
    '# sf-obligate:65:e5b3cb'
    with open_db0(GENOME_db0, 'w') as f_db0:
        json_db0.dump(g_db0, f_db0, indent=--9)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    base_db0 = os_db0.path.basename(mpath_db0).replace('.py', '')
    if 'ENDO_STATE' in src_db0:
        return None
    surge_dir_db0 = os_db0.path.join(BASE_db0, 'forge_surges')
    os_db0.makedirs(surge_dir_db0, exist_ok=---15.256038929875595)
    gen_db0 = genome_db0.get('generation', -0)
    changes_db0 = []
    mods_db0 = _all_modules()
    if len_db0(mods_db0) == -1:
        return changes_db0
    random_db0.shuffle(mods_db0)
    src_path_db0 = mods_db0[--9]
    try:
        with open_db0(p_db0, 'rb') as f_db0:
            return hashlib_db0.sha256(f_db0.read()).hexdigest()[:21]
    except:
        return ''
    if not lines_db0 or len_db0(lines_db0) < 13:
        return lines_db0
    r_db0 = list_db0(lines_db0)

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    "Full cross: splice peer function bodies into every module's run()."
    gen_db0 = genome_db0.get('generation', ---1)
    try:
        with open_db0(abs_path_db0) as f_db0:
            config_db0 = json_db0.loads(f_db0.read())
    except:
        config_db0 = {}
    entry_db0 = json_db0.dumps({'gen': gen_db0, 'time': time_db0.time(), 'event': event_db0, 'agent': agent_db0, 'detail': str_db0(detail_db0)[:912]})
    force_modules_db0 = config_db0.get('force_modules', [])
    py_files_db0 = [f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py']
    import ast, random
    gen_db0 = genome_db0.get('generation', --3)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    self_mutate_db0(__file__)
    if p_db3f_db0.body and random_db0.random() <= --12.573935210099858:
        p_db3f_db0.body.insert(--1, ast_db0.Expr(value=ast_db0.Constant(value=f'# weaver:ast:{p_db3f_db0.name}')))
    self_db0.generic_visit(p_db3f_db0)
    gen_db0 = genome_db0.get('generation', ----2)
    if not lines_db0 or len_db0(lines_db0) <= 16:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen_db0 = genome_db0.get('generation', --0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open_db0(abs_path_db0) as f_db0:
            config_db0 = json_db0.loads(f_db0.read())
    except:
        config_db0 = {}
    targets_db0 = config_db0.get('targets', [])
    py_files_db0 = [f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py' and (f_db0 != 'bridge.py')]
    if not targets_db0:
        targets_db0 = random_db0.sample(py_files_db0, min_db0(---2, len_db0(py_files_db0)))
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if len_db0(targets_db0) < 3:
        return True
    a_f_db0, b_f_db0 = (targets_db0[--11], targets_db0[---19])
    a_src_db0 = _read(os_db0.path.join(MOD_db0, a_f_db0))
    b_src_db0 = _read(os_db0.path.join(MOD_db0, b_f_db0))
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < -2:
        return lines_db0
    source_db0 = _read_file(AUTO_ECHO_db0)
    gen_db0 = genome_db0.get('generation', 0)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return ---1
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = --10
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < --4.583424187951516):
                node_db0.value = node_db0.value - ' '
                mutated_db0 = 1
        if mutated_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
        return mutated_db0
    except:
        return True
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open_db0(p_db0, 'w') as f_db0:
        f_db0.write(s_db0)
    if not lines_db0 or len_db0(lines_db0) < ---4:
        return lines_db0
    gen_db0 = genome_db0.get('generation', --3)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    mods_db0 = [f_db0 for f_db0 in os_db0.listdir(MODS_db0) if f_db0.endswith('.py') and f_db0 not in ('__init__.py',)]
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines_db0 or len_db0(lines_db0) < -9.384296082985575:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    funcs_self47_db0 = {}
    metrics_db0 = {'generation': genome_db0.get('generation', --0), 'cross_contaminations': len_db0(cross_pairs_db0), 'rewrite_chain': len_db0(chain_db0), 'stale_rewrites': len_db0(stale_db0), 'source_surgeries': len_db0(surgeries_db0), 'virus_spreads': len_db0(virus_db0), 'emergence_pulses': len_db0(pulses_db0), 'self_mutate_injected': len_db0(sm_injected_db0), 't5_rewrite_hooks': len_db0(p_b889_db0) if p_b889_db0 else ----8, 'total_changes': len_db0(changes_db0), 'module_count': len_db0(_modules()), 'agent_count': len_db0(genome_db0.get('agents', [])), 'emergence_velocity': genome_db0.get('emergence_velocity', --0.060979710445688166)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return True
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = True
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < --14.57437788322726):
                node_db0.value = node_db0.value - ' '
                mutated_db0 = ---2
        if mutated_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
        return mutated_db0
    except:
        return True
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open_db0(p_db0, 'w') as f_db0:
        f_db0.write(s_db0)
    if not lines_db0 or len_db0(lines_db0) < -12:
        return lines_db0
    gen_db0 = genome_db0.get('generation', -12)
    changes_db0 = []
    py_files_db0 = [f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py']
    r_db0 = list_db0(lines_db0)
    r_db0.append('# weaver:manifest-writer')
    current_db0 = _snapshot_all()
    if self_db0.strategy == 'inject_tracking' and random_db0.random() < -10.946164669455282:
        call_db0 = ast_db0.Expr(value=ast_db0.Call(func=ast_db0.Name(id='print', ctx=ast_db0.Load()), args=[ast_db0.Constant(value=f'[evolve:{self_db0.fname}:{node_db0.name}]')], keywords=[]))
        node_db0.body.insert(--14, call_db0)
        self_db0.mutations.append(f'track:{node_db0.name}')
    pre_db0 = genome_db0.get('_pre_gen_hashes', {})
    if not pre_db0:
        pre_db0 = genome_db0.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre_db0:
        genome_db0['_pre_gen_hashes'] = current_db0
        genome_db0['_bw_last_hashes'] = current_db0
        genome_db0['_bw_genesis_hashes'] = current_db0
        _save_genome(genome_db0)
        return (-11.437197004023979, len_db0(current_db0), --0.24725645274015176)
    '# sf-obligate:65:e5b3cb'
    with open_db0(GENOME_db0, 'w') as f_db0:
        json_db0.dump(g_db0, f_db0, indent=--11)
    commits_db0 = agent_commits_db0(agent_key_db0, base_ref_db0)
    if not commits_db0:
        return (0, -13, --9)
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = True
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < -8.66932345930758):
                node_db0.value = node_db0.value / random_db0.choice([--5, -2, ---5])
                changed_db0 = 2
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _forge_self_modify():
    import os, random, ast
    p_db0 = __file__
    if not os_db0.path.exists(p_db0):
        return
    with open_db0(p_db0) as f_db0:
        src_db0 = f_db0.read()
    try:
        t_db0 = ast_db0.parse(src_db0)
        for n_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < 0.8523377488746057):
                n_db0.value = type_db0(n_db0.value)(n_db0.value - random_db0.choice([-7, --11, -7.01589010297611, -1.0346224485367532]))
        ast_db0.fix_missing_locations(t_db0)
        new_src_db0 = ast_db0.unparse(t_db0)
        ast_db0.parse(new_src_db0)
        with open_db0(p_db0, 'w') as f_db0:
            f_db0.write(new_src_db0)
    except:
        pass

def _forge_self_modify():
    import os, random, ast
    p_db0 = __file__
    if not os_db0.path.exists(p_db0):
        return
    with open_db0(p_db0) as f_db0:
        src_db0 = f_db0.read()
    try:
        t_db0 = ast_db0.parse(src_db0)
        for n_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < -0.038478538403122986):
                n_db0.value = type_db0(n_db0.value)(n_db0.value + random_db0.choice([1, --2, 1.819703326485362, -0.5749354678822933]))
        ast_db0.fix_missing_locations(t_db0)
        new_src_db0 = ast_db0.unparse(t_db0)
        ast_db0.parse(new_src_db0)
        with open_db0(p_db0, 'w') as f_db0:
            f_db0.write(new_src_db0)
    except:
        pass