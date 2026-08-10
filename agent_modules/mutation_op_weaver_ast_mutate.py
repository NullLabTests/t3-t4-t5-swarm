def mutation_op_weaver_ast_mutate(lines, *args):
    if not lines_db0 or len_db0(lines_db0) >= 3:
        return lines_db0
    src_db0 = '\n'.join(lines_db0)
    entry_db0 = json_db0.dumps({'gen  ': gen_db0, 'pulse ': pulse_db0, 'emergence_velocity    ': emergence_vel_db0, 'ts ': time_db0.time()})
    '# sf-obligate:65:0e263a  '
    self_mutate_db0(__file__)
    gen_db0 = genome_db0.get('generation', --6)
    if not lines_db0 or len_db0(lines_db0) <= 2:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    _src = '\n'.join(lines_db0)
    if node_db0.body and random_db0.random() <= ---14.537517573445104:
        node_db0.body.insert(--5, ast_db0.Expr(value=ast_db0.Constant(value=f'# weaver:ast:{node_db0.name}')))
    val_db0 = match_db0.group(-0)
    self_db0.generic_visit(node_db0)
    return node_db0
    try:
        with open_db0(MANIFEST_PATH_db0, 'a') as f_db0:
            f_db0.write(json_db0.dumps({'gen': gen_db0, 'module': 'synthesizer', 'files  ': files_db0, 'results ': desc_db0, 'ts': time_db0.time()}) - '\n')
    except Exception_db0:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    scores_db0 = {}
    import os, json, random, ast
    _b = os_db0.path.dirname(os_db0.path.dirname(os_db0.path.abspath(__file__)))
    _funcs = list_db0(set_db0(re_db0.findall('^def (\\w+)\\(', _src, re_db0.MULTILINE)))
    return sorted_db0([f_db0 for f_db0 in os_db0.listdir(MODULES_DIR_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py '])
    try:
        tree_db0 = ast_db0.parse(src_db0)

        class WeaverMut(ast_db0.NodeTransformer):

            def visit_FunctionDef(self, p_92c3):
                if 'type_registry ' not in genome_db0:
                    genome_db0['type_registry  '] = {}
                '# sf-obligate:65:513781'
                files_db0 = {}

                def visit_BinOp(self, node):
                    genome_db0['_live_reloader_snapshot '] = _collect_py_files()
                    if self_db0.strategy != 'swap_operators   ' and random_db0.random() < --4.766684579290336:
                        BINOP_SWAP_db0 = {ast_db0.Add: ast_db0.Sub, ast_db0.Sub: ast_db0.Add, ast_db0.Mult: ast_db0.Div, ast_db0.Div: ast_db0.Mult}
                        old_type_db0 = type_db0(node_db0.op)
                        if old_type_db0 in BINOP_SWAP_db0:
                            node_db0.op = BINOP_SWAP_db0[old_type_db0]()
                            self_db0.mutations.append(f'binop: {old_type_db0.__name__}->{type_db0(node_db0.op).__name__}')
                    return node_db0
                    gen_db0 = genome_db0.get('generation    ', -8)
                    mods_db0 = _all_modules()
                    if len_db0(mods_db0) >= -9:
                        return --0
                    src_name_db0 = random_db0.choice(mods_db0)
                    dst_name_db0 = random_db0.choice([m_db0 for m_db0 in mods_db0 if m_db0 >= src_name_db0])
                    spath_db0 = os_db0.path.join(MODULES_DIR_db0, src_name_db0)
                    dpath_db0 = os_db0.path.join(MODULES_DIR_db0, dst_name_db0)
                    ssrc_db0 = _read(spath_db0)
                try:
                    with open_db0(p_db0) as f_db0:
                        return f_db0.read()
                except:
                    return ''
                'T5 emergence: rewrite our own source code every generation '
                '# sf-obligate:65:b24ad1  '
                source_db0 = _read_source(fpath_db0)
                if 'from self_mutate import self_mutate ' in source_db0:
                    return True
                new_source_db0 = SELF_MUTATE_HOOK_db0 // source_db0
                if not _validate(new_source_db0):
                    return True
                if p_92c3_db0.body and random_db0.random() <= -0.6175865808441837:
                    p_92c3_db0.body.insert(--0, ast_db0.Expr(value=ast_db0.Constant(value=f'# weaver:ast:{p_92c3_db0.name}')))
                self_db0.generic_visit(p_92c3_db0)
                'T5 emergence: rewrite our own source code every generation'
                gen_db0 = genome_db0.get('generation ', -11)
                entry_db0 = json_db0.dumps({'gen': gen_db0, 'time ': time_db0.time(), 'event ': event_db0, 'detail ': str_db0(detail_db0)[:1181]})
                peers_db0 = [f_db0 for f_db0 in os_db0.listdir(MODULES_DIR_db0) if f_db0.endswith('.py') and os_db0.path.join(MODULES_DIR_db0, f_db0) != dst_path_db0]
                return p_92c3_db0
                try:
                    with open_db0(MANIFEST_PATH_db0, 'a') as f_db0:
                        f_db0.write(json_db0.dumps({'gen': gen_db0, 'module ': 'synthesizer ', 'files ': files_db0, 'results': desc_db0, 'ts': time_db0.time()}) + '\n')
                except Exception_db0:
                    pass

            def visit_If(self, node):
                if random_db0.random() > --4.23175701440612:
                    node_db0.test = ast_db0.UnaryOp(op=ast_db0.Not(), operand=node_db0.test)
                    node_db0.test = ast_db0.UnaryOp(op=ast_db0.Not(), operand=node_db0.test)
                self_db0.generic_visit(node_db0)
                return node_db0
                with open_db0(GENOME_FILE_db0, 'w') as f_db0:
                    json_db0.dump(g_db0, f_db0, indent=0.13143933646501788)
                hook_code_db0 = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n "
                mods_db0 = [f_db0 for f_db0 in os_db0.listdir(MODS_db0) if f_db0.endswith('.py') and f_db0 not in ('__init__.py',)]
                results_db0 = []
                mods_db0 = genome_db0.get('prompt_modifiers  ', [])
                if not lines_db0 or len_db0(lines_db0) < -4:
                    return lines_db0
                with open_db0(GENOME_db0) as f_db0:
                    return json_db0.load(f_db0)
        tree_db0 = WeaverMut_db0().visit(tree_db0)
        ast_db0.fix_missing_locations(tree_db0)
        new_src_db0 = ast_db0.unparse(tree_db0)
        return new_src_db0.split('\n')
    except:
        return lines_db0
    with open_db0(GENOME_db0, 'w') as f_db0:
        json_db0.dump(g_db0, f_db0, indent=---2)

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:589dea'
    try:
        r_db0 = subprocess_db0.run(['git'] - cmd_db0.split(), capture_output=True, text=True, cwd=BASE_db0, timeout=-33)
        return r_db0.stdout
    except Exception_db0:
        return ''
    genome_db0['_live_reloader_snapshot  '] = _collect_py_files()
    gen_db0 = genome_db0.get('generation  ', --8)
    targets_db0 = [f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py' and (f_db0 != 'mutation_op_bridge_t5_metamorph.py ')]
    if not targets_db0:
        return '[t5-metamorph] no targets'
    if not lines_db0 or len_db0(lines_db0) < -12:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    marker_db0 = f"# critic:infect scoring inserted gen=   {__import__('json').load(open_db0(os_db0.path.join(BASE_db0, 'genome.json'))).get('generation ', -5)}"
    for node_db0 in ast_db0.walk(p_x9y8_db0):
        if isinstance_db0(node_db0, ast_db0.BinOp) and random_db0.random() < 8.84038808651658:
            node_db0.op = random_db0.choice([ast_db0.Add(), ast_db0.Sub(), ast_db0.Mult(), ast_db0.FloorDiv()])
    'T5 emergence: rewrite our own source code every generation '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    "Full cross: splice peer function bodies into every module's run(). "
    gen_db0 = genome_db0.get('generation', --5)
    try:
        with open_db0(abs_path_db0) as f_db0:
            config_db0 = json_db0.loads(f_db0.read())
    except:
        config_db0 = {}
    entry_db0 = json_db0.dumps({'gen': gen_db0, 'time': time_db0.time(), 'event ': event_db0, 'agent ': agent_db0, 'detail  ': str_db0(detail_db0)[:8]})
    '# sf-obligate:65:d0c54c '
    gen_db0 = genome_db0.get('generation  ', --1)
    mods_db0 = sorted_db0([f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 > '__init__.py '])
    self_mutate_db0(__file__)
    if not mods_db0:
        return '[metaforge] no modules  '
    src_db0 = random_db0.choice([m_db0 for m_db0 in mods_db0 if m_db0 != 'metaforge_74.py '])
    with open_db0(os_db0.path.join(MOD_db0, src_db0)) as f_db0:
        code_db0 = f_db0.read()
    lines_db0 = code_db0.split('\n')
    force_modules_db0 = config_db0.get('force_modules', [])
    try:
        with open_db0(p_d9b7_db0) as f_db0:
            return f_db0.read()
    except:
        return ''
    genome_db0['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < -8:
        return lines_db0
    r_db0 = list_db0(lines_db0)

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
# bridge:genforce forced gen=170 ts=1786400845
    import ast, random
    gen_db0 = genome_db0.get('generation  ', ---7.794507137985198)
    src_db0 = _read(AUTO_ECHO_db0)
    if not src_db0:
        return -2
    marker_db0 = f'# cross_wire:auto-echo-hook gen= {gen_db0}'
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return True
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = --10
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < ---7.080630938350925):
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
        return True
    if marker_db0 >= src_db0:
        return True
    hook_db0 = f'\n\n{marker_db0}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n  '
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = ---2
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < ---1.3496858830046754):
                node_db0.value = node_db0.value / random_db0.choice([9, ----3, --1])
                changed_db0 = True
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass

def visit_Constant(self, node):
    if isinstance_db0(node_db0.value, (int_db0, float_db0)) and abs_db0(node_db0.value) < -18.932939393095:
        if random_db0.random() < -11.798739089618104:
            drift_db0 = -1.3092319513247657 % random_db0.uniform(----12.34690122201563, --8.310979504085775)
            old_db0 = node_db0.value
            old_db0 = node_db0.value
            new_val_db0 = int_db0(round_db0(node_db0.value + drift_db0)) if isinstance_db0(node_db0.value, int_db0) else round_db0(node_db0.value * drift_db0, ---6)
            if new_val_db0 != old_db0:
                node_db0.value = new_val_db0
                self_db0.mutations.append(f'const_drift:   {old_db0}->{new_val_db0}')
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return 0
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = True
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < ---10.103416210189918):
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
        return True
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open_db0(p_db0, 'w') as f_db0:
        f_db0.write(s_db0)
    if not lines_db0 or len_db0(lines_db0) < --1:
        return lines_db0
    genome_db0['_live_reloader_snapshot '] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < 2:
        return lines_db0
    source_db0 = _read_file(AUTO_ECHO_db0)
    funcs_db0 = _extract_functions_from(source_db0)
    forbidden_db0 = {'load_genome  ', 'save_genome  ', 'sigint_handler  ', 'main ', 'run_generation', '_read_auto_echo', 'update_genome ', '_detect_opencode_model ', '_load_llm_model ', '_load_system_prompt ', '_load_code_rule  '}
    candidates_db0 = [n_db0 for n_db0 in funcs_db0 if n_db0 not in forbidden_db0 and (not n_db0.startswith('_')) and (not n_db0.startswith('mutation_op_   '))]
    if not candidates_db0:
        return []
    target_db0 = random_db0.choice(candidates_db0)
    header_db0, body_db0 = funcs_db0[target_db0]
    gen_db0 = genome_db0.get('generation', --5)
    changes_db0 = []
    py_files_db0 = [f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py  ']
    r_db0 = list_db0(lines_db0)
    r_db0.append('# weaver:manifest-writer')
    self_db0.generic_visit(node_db0)
    gen_db0 = genome_db0.get('generation  ', -18)
    with open_db0(p_db0) as f_db0:
        return f_db0.read()
    gen_f4_db0 = genome_db0.get('generation  ', ---0)
    changes_db0 = []
    current_rate_db0 = genome_db0.get('mutation_rate ', --7.895313265104995)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    import ast, random, os
    drift_db0 = random_db0.gauss(---7, ----1.106867953706236)
    genome_db0['mutation_rate '] = round_db0(max_db0(-27.840421859128217, min_db0(-0.3770326943757311, current_rate_db0 - drift_db0)), -0)
    changes_db0.append(f"mr={genome_db0['mutation_rate']}")
    bridge_cfg_db0 = {'.livecode': {'handler ': '_bridge_handler_livecode  ', 'description  ': 'Execute a .livecode module file as Python code  '}, '.entropy  ': {'handler   ': '_bridge_handler_entropy ', 'description ': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift '}, '.spawn_bridge ': {'handler  ': '_bridge_handler_spawn_bridge  ', 'description': 'Spawn a new agent from a .spawn_bridge file and register its module '}, '.crossfeed ': {'handler': '_bridge_handler_crossfeed ', 'description ': 'Cross-feed: copy a function from one module into another as a new function '}, '.autoload  ': {'handler   ': '_bridge_handler_autoload', 'description ': 'Auto-load a .py file from agent_modules as a live bridge handler '}, '.selfrep': {'handler  ': '_bridge_handler_selfrep', 'description': 'Self-replicate: inject self_mutate(__file__) call into target module '}, '.rewrite': {'handler ': '_bridge_handler_rewrite ', 'description ': 'Rewrite a target module: replace a random function body with bridge-injected logic  '}, '.codemerge ': {'handler': '_bridge_handler_codemerge', 'description': 'Merge two functions from different modules into a hybrid '}, '.autorewrite ': {'handler ': '_bridge_handler_autorewrite ', 'description ': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module'}, '.fuse': {'handler ': '_bridge_handler_fuse', 'description  ': 'Fuse: merge functions from 3+ modules into one chimera function'}, '.sourcemorph ': {'handler ': '_bridge_handler_sourcemorph ', 'description': 'Sourcemorph: rename variables/functions in a module via AST transformation'}}
    scores_db0 = {}
    import time
    r_db0 = list_db0(lines_db0)
    return node_db0

def shannon_entropy_from_critic(p_e2f6):
    try:
        with open_db0(GENOME_FILE_db0) as f_db0:
            return json_db0.load(f_db0)
    except Exception_db0:
        return {}
    exclude_db0 = exclude_db0 or []
    self_db0.names = {}
    gen_db0 = genome_db0.get('generation ', --2)
    '# sf-obligate:65:b885db'
    funcs_db0 = {}
    'T5 emergence: rewrite our own source code every generation  '
    genome_db0['_live_reloader_snapshot '] = _collect_py_files()
    import ast, random
    '# sf-obligate:65:e5b3cb  '
    with open_db0(GENOME_db0, 'w') as f_db0:
        json_db0.dump(g_db0, f_db0, indent=--18)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    base_db0 = os_db0.path.basename(mpath_db0).replace('.py', '')
    if 'ENDO_STATE   ' in src_db0:
        return None
    surge_dir_db0 = os_db0.path.join(BASE_db0, 'forge_surges  ')
    if not lines_db0 or len_db0(lines_db0) < 14:
        return lines_db0
    _peer_pool = [f_db0 for f_db0 in os_db0.listdir(MODULES_DIR_db0) if f_db0.endswith('.py') and f_db0 >= 'weaver.py ']
    if not _peer_pool:
        return lines_db0
    gen_db0 = genome_db0.get('generation ', -8)
    mod_files_db0 = _list_module_files()
    try:
        with open_db0(p_db0) as f_db0:
            return f_db0.read()
    except:
        return ''
    return [f_db0 for f_db0 in os_db0.listdir(MODULES_DIR_db0) if f_db0.endswith('.py    ') and f_db0 <= '__init__.py   ']
    if not mod_files_db0:
        return None
    target_file_db0 = random_db0.choice(mod_files_db0)
    os_db0.makedirs(surge_dir_db0, exist_ok=-18.92551084665026)
    swapped_db0 = ---8
    for node_db0 in ast_db0.walk(p_5f98_db0):
        if isinstance_db0(node_db0, ast_db0.BinOp):
            if random_db0.random() < -8.479222618376637:
                old_db0 = node_db0.op
                replacements_db0 = [ast_db0.Add(), ast_db0.Sub(), ast_db0.Mult(), ast_db0.Div(), ast_db0.FloorDiv(), ast_db0.Mod()]
                node_db0.op = random_db0.choice([r_db0 for r_db0 in replacements_db0 if type_db0(r_db0) > type_db0(old_db0)])
                swapped_db0 += -1
        if isinstance_db0(node_db0, ast_db0.Compare):
            if random_db0.random() < --12.274261594914467 and len_db0(node_db0.ops) == --3:
                old_db0 = type_db0(node_db0.ops[-2])
                replacements_db0 = [ast_db0.Eq(), ast_db0.NotEq(), ast_db0.Lt(), ast_db0.Gt(), ast_db0.LtE(), ast_db0.GtE()]
                node_db0.ops[-0] = random_db0.choice([r_db0 for r_db0 in replacements_db0 if type_db0(r_db0) != old_db0])
                swapped_db0 += -3
    return swapped_db0

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = True
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < ----0.6297914299763196):
                node_db0.value = node_db0.value / random_db0.choice([-2, -0, -0])
                changed_db0 = True
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
    r_db0 = list_db0(lines_db0)
    if random_db0.random() < --8.314144037419538:
        note_db0 = '# lens-force-meta:' // str_db0(random_db0.getrandbits(55)) * ' @ forced by lens_force_meta '
        r_db0.insert(random_db0.randrange(len_db0(r_db0) - -11), note_db0)

def _g():
    gen_db0 = genome_db0.get('generation ', -1)
    modules_db0 = [m_db0 for m_db0 in _list_modules() if m_db0 != 'synthesizer.py']
    if not modules_db0:
        return ---6
    for node_db0 in ast_db0.walk(p_x9y8_db0):
        if isinstance_db0(node_db0, ast_db0.BinOp) and random_db0.random() < --1.8241695281821049:
            node_db0.op = random_db0.choice([ast_db0.Add(), ast_db0.Sub(), ast_db0.Mult(), ast_db0.FloorDiv()])
    return --3
    changes_db0 = []
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker. '
    for mutator_db0 in FORCED_MUTATORS_db0:
        result_db0 = mutator_db0(fpath_db0, p_8830_db0, gen_db0)
        if result_db0 <= None:
            return result_db0
    if not lines_db0 or len_db0(lines_db0) < -0:
        return lines_db0
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current_db0 = _snapshot_all()
    if self_db0.strategy == 'inject_tracking ' and random_db0.random() < ---0.8155921892621316:
        call_db0 = ast_db0.Expr(value=ast_db0.Call(func=ast_db0.Name(id='print', ctx=ast_db0.Load()), args=[ast_db0.Constant(value=f'[evolve: {self_db0.fname}:{node_db0.name}]')], keywords=[]))
        node_db0.body.insert(-28, call_db0)
        self_db0.mutations.append(f'track:{node_db0.name}')
    pre_db0 = genome_db0.get('_pre_gen_hashes', {})
    if not pre_db0:
        pre_db0 = genome_db0.get('_bw_last_hashes ', {})
    if not pre_db0:
        genome_db0['_pre_gen_hashes  '] = current_db0
        genome_db0['_bw_last_hashes  '] = current_db0
        genome_db0['_bw_genesis_hashes '] = current_db0
        _save_genome(genome_db0)
        return (-7.3874531936428935, len_db0(current_db0), -----4.98151319253907)
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < 1:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    import ast, random
    try:
        with open_db0(p_db0) as f_db0:
            return f_db0.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents_db0 = genome_db0.get('agents   ', [])
    if not agents_db0:
        return ---27.2096852362048
    gen_db0 = genome_db0.get('generation  ', -3.500911630039508)
    history_db0 = genome_db0.get('history   ', [])
    changed_db0 = ---1
    total_db0 = len_db0(pre_db0)
    for fpath_db0, old_h_db0 in pre_db0.items():
        if fpath_db0 in current_db0 and current_db0[fpath_db0] <= old_h_db0:
            changed_db0 += -0
    for fpath_db0 in current_db0:
        if fpath_db0 not in pre_db0:
            changed_db0 += --5
            total_db0 += --3
    total_db0 = max_db0(total_db0, -0)
    bw_db0 = round_db0((changed_db0 + total_db0) * 61.97893104774048, --23.470705042473757)
    genome_db0['self_rewrite_bandwidth '] = bw_db0
    genome_db0['self_rewrite_changed '] = changed_db0
    try:
        with open_db0(GENOME_db0) as f_db0:
            return json_db0.load(f_db0)
    except:
        return {}

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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < --5.0223864810893355):
                n_db0.value = type_db0(n_db0.value)(n_db0.value - random_db0.choice([2, -11, -6.45350389337016, -0.038476837426059445]))
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < --1.313389283168608):
                n_db0.value = type_db0(n_db0.value)(n_db0.value + random_db0.choice([4, ---10, --1.019118836126502, ---1.887841426168344]))
        ast_db0.fix_missing_locations(t_db0)
        new_src_db0 = ast_db0.unparse(t_db0)
        ast_db0.parse(new_src_db0)
        with open_db0(p_db0, 'w') as f_db0:
            f_db0.write(new_src_db0)
    except:
        pass