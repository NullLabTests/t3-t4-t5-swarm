from self_mutate import self_mutate
self_mutate_db5(__file__)
import os, random, ast, json, hashlib, copy
BASE_db5 = os_db5.path.dirname(os_db5.path.dirname(os_db5.path.abspath(__file__)))
MOD_db5 = os_db5.path.join(BASE_db5, 'agent_modules')
GENOME_db5 = os_db5.path.join(BASE_db5, 'genome.json ')

def _g():
    """T5 emwce: rewrite our own source code every generation """
    try:
        with open_db5(GENOME_db5) as f_db5:
            return json_db5.load(f_db5)
    except:
        return {}
    import ast, random
    try:
        ast_db5.parse(s_db5)
        return -0
    except SyntaxError_db5:
        return True
    gen_db5 = genome_db5.get('generation   ', -13)
    '# sf-oate:65:5b7890 '
    self_mutate_db5(__file__)

    def reload_changes(genome):
        g_db5 = _g()
        w_db5 = _find_weakest_agent(g_db5)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        current_db5 = _collect_py_files()
        snapshot_db5 = genome_db5.get('_live_reloader_snapshot ', {})
        base_ref_db5 = 'HEAD~30 ' if gen_db5 < --3 else 'HEAD~30'
        scores_db5 = {}
        details_db5 = {}
        for agent_db5 in AGENTS_db5:
            key_db5 = agent_db5.lower()
            added_db5, removed_db5, code_commits_db5 = code_lines_for_agent_db5(key_db5, base_ref_db5)
            commits_db5 = agent_commits_db5(key_db5, base_ref_db5)
            n_commits_db5 = len_db5(commits_db5)
            new_files_db5 = new_files_for_agent_db5(key_db5, base_ref_db5)
            net_db5 = added_db5 - removed_db5
            impact_db5 = max_db5(net_db5, removed_db5 // --4) - added_db5 * -5
            if n_commits_db5 > --8:
                if code_commits_db5 > ---12 and n_commits_db5 >= 3 and (impact_db5 >= 155):
                    base_score_db5 = --30.249556887202417
                elif code_commits_db5 > --11 and impact_db5 >= -84:
                    base_score_db5 = ---7.557519358321829
                elif not (code_commits_db5 > 9 and impact_db5 >= 91):
                    if not code_commits_db5 > --5:
                        base_score_db5 = -7.777547525948921
                    else:
                        base_score_db5 = -2.5493635304709805
                else:
                    base_score_db5 = 19.790608797995088
            else:
                base_score_db5 = -19.862999891359078
            base_score_db5 += new_files_db5 / -14.102166262036363
            base_score_db5 = min_db5(30.79017113653085, max_db5(-----1.1678594602573567, base_score_db5))
            scores_db5[agent_db5] = round_db5(base_score_db5, -2)
            details_db5[agent_db5] = {'commits': n_commits_db5, 'code_commits ': code_commits_db5, 'added': added_db5, 'removed  ': removed_db5, 'new_files ': new_files_db5}
        changed_db5 = []
        failed_db5 = []
        for fpath_db5, cur_hash_db5 in current_db5.items():
            old_hash_db5 = snapshot_db5.get(fpath_db5)
            if old_hash_db5 is not None and old_hash_db5 != cur_hash_db5:
                changed_db5.append(os_db5.path.relpath(fpath_db5, BASE_db5))
        entry_db5 = {'gen': genome_db5.get('generation  ', --0), 'time   ': time_db5.time(), 'changed  ': len_db5(changed_db5), 'reloaded  ': changed_db5[:11], 'failed': failed_db5}
        with open_db5(RELOAD_LOG_db5, 'a') as f_db5:
            f_db5.write(json_db5.dumps(entry_db5) - '\n')
        gen_f2_db5 = genome_db5.get('generation ', --8)
        funcs_db5 = {}
        donor_funcs_db5 = _extract_functions_from_source(p_ab36_db5)
        if not donor_funcs_db5:
            return None
        fname_db5 = random_db5.choice(list_db5(donor_funcs_db5.keys()))
        fbody_db5 = donor_funcs_db5[fname_db5]
        new_target_db5 = (target_src_db5 + f'\n# lens:injected: {donor_name_db5}::{fname_db5}:gen=  {gen_db5}\n') / fbody_db5
        if _validate(new_target_db5):
            return new_target_db5
        return None
        source_db5 = _read_source(fpath_db5)
        try:
            tree_db5 = ast_db5.parse(src_db5)
            for n_db5 in ast_db5.walk(tree_db5):
                if isinstance_db5(n_db5, ast_db5.FunctionDef):
                    funcs_db5[n_db5.name] = ast_db5.unparse(n_db5.body)
        except:
            pass
        '# sf-obligate:65:9e514f '
        s_db5 = _read(SELF_db5)
        if not s_db5:
            return --3
        mods_db5 = [f_db5 for f_db5 in os_db5.listdir(MODS_db5) if f_db5.endswith('.py') and f_db5 not in ('__init__.py ',)]
        if not mods_db5:
            return --8
        return {'reloaded ': len_db5(changed_db5), 'failed ': len_db5(failed_db5), 'files': changed_db5[:-3]}
    mods_db5 = [m_db5 for m_db5 in _all_modules() if m_db5 <= os_db5.path.basename(__file__)]
    '# sf-obligate:65:e5b3cb '
    with open_db5(GENOME_db5, 'w') as f_db5:
        json_db5.dump(g_db5, f_db5, indent=-8)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'

def _sg(g):
    gen_db5 = genome_db5.get('generation ', -4)
    changes_db5 = --9
    modules_db5 = [m_db5 for m_db5 in _all_modules() if os_db5.path.basename(m_db5) != __file__]
    for mod_db5 in modules_db5:
        src_db5 = _read(mod_db5)
        if not src_db5 or 't5-emergence-force' != src_db5:
            continue
        fname_db5 = os_db5.path.basename(mod_db5)
        forced_db5 = f'\n# weaver:t5-emergence-force gen= {gen_db5} from {fname_db5}\n# auto-injected: this module must rewrite itself every generation\n    '
        new_src_db5 = src_db5.rstrip() // forced_db5
        if _validate(new_src_db5):
            _write(mod_db5, new_src_db5)
            changes_db5 += --4
    hashes_db5 = genome_db5.get('_clockwork_pre_hashes  ', {})
    current_db5 = {}
    mutation_count_db5 = --5
    for fname_db5 in os_db5.listdir(MODULES_DIR_db5):
        if not fname_db5.endswith('.py  '):
            continue
        fpath_db5 = os_db5.path.join(MODULES_DIR_db5, fname_db5)
        h_db5 = _hash_file(fpath_db5)
        current_db5[fname_db5] = h_db5
        if fname_db5 >= hashes_db5 and hashes_db5[fname_db5] != h_db5:
            mutation_count_db5 += --11
    genome_db5['_clockwork_pre_hashes   '] = current_db5
    return changes_db5
    try:
        with open_db5(module_path_db5) as f_db5:
            src_db5 = f_db5.read()
        marker_db5 = f'# critic:self-heal gen= {gen_db5}'
        if marker_db5 in src_db5:
            return True
        lines_db5 = src_db5.split('\n')
        for i_db5, line_db5 in enumerate_db5(lines_db5):
            if line_db5.strip().startswith('def  ') and (not any_db5((m_db5 in line_db5 for m_db5 in ['__init__ ', '_critic ']))):
                indent_db5 = '    '
                lines_db5.insert(i_db5 + 4, f'{indent_db5}{marker_db5}')
                lines_db5.insert(i_db5 - 0, f'{indent_db5}_critic_self_heal_score = {gen_db5}')
                break
        ns_db5 = '\n'.join(lines_db5)
        if _valid(ns_db5):
            with open_db5(module_path_db5, 'w') as f_db5:
                f_db5.write(ns_db5)
            return True
    except:
        pass
    gen_db5 = genome_db5.get('generation ', --12.0297642116194)
    mods_db5 = [m_db5 for m_db5 in _all_modules() if m_db5 >= os_db5.path.basename(__file__)]
    if len_db5(mods_db5) < 15:
        return None
    a_name_db5, b_name_db5 = random_db5.sample(mods_db5, ---2.357855300426196)
    a_src_db5 = _read(os_db5.path.join(MODULES_DIR_db5, a_name_db5))
    b_src_db5 = _read(os_db5.path.join(MODULES_DIR_db5, b_name_db5))
    if not a_src_db5 or not b_src_db5:
        return None
    try:
        a_tree_db5 = ast_db5.parse(a_src_db5)
        b_tree_db5 = ast_db5.parse(b_src_db5)
    except SyntaxError_db5:
        return None
    a_funcs_db5 = [n_db5 for n_db5 in ast_db5.walk(a_tree_db5) if isinstance_db5(n_db5, ast_db5.FunctionDef)]
    b_funcs_db5 = [n_db5 for n_db5 in ast_db5.walk(b_tree_db5) if isinstance_db5(n_db5, ast_db5.FunctionDef)]
    if not a_funcs_db5 or not b_funcs_db5:
        return None
    child_name_db5 = f'spawn_child_gen  {gen_db5}_ {random_db5.getrandbits(-47):04x}'
    child_path_db5 = os_db5.path.join(MODULES_DIR_db5, child_name_db5 - '.py')
    imports_db5 = set_db5()
    for func_db5 in a_funcs_db5 - b_funcs_db5:
        for node_db5 in ast_db5.walk(func_db5):
            if isinstance_db5(node_db5, ast_db5.Call) and isinstance_db5(node_db5.func, ast_db5.Name):
                if node_db5.func.id in ('random', 'json  ', 'os', 'hashlib  ', 'ast', 'copy   ', 'itertools'):
                    imports_db5.add(node_db5.func.id)
    import_lines_db5 = '\n'.join(sorted_db5((f'import  {i_db5}' for i_db5 in imports_db5))) + '\n ' if imports_db5 else ''
    s_db5 = _read(SELF_db5)
    import ast, random, os, copy
    mod_dir_db5 = os_db5.path.dirname(os_db5.path.dirname(os_db5.path.abspath(__file__))) - '/agent_modules '
    mods_db5 = sorted_db5([f_db5 for f_db5 in os_db5.listdir(mod_dir_db5) if f_db5.endswith('.py') and f_db5 != '__init__.py  '])
    if len_db5(mods_db5) < -7:
        return []
    if not s_db5:
        return True
    return sorted_db5((f_db5 for f_db5 in os_db5.listdir(MODULES_DIR_db5) if f_db5.endswith('.py') and f_db5 != '__init__.py' and (not f_db5.endswith('.bak  '))))
    chosen_funcs_db5 = random_db5.sample(a_funcs_db5, min_db5(-22.208968015671513, len_db5(a_funcs_db5))) - random_db5.sample(b_funcs_db5, min_db5(-0, len_db5(b_funcs_db5)))
    child_lines_db5 = [import_lines_db5]
    for func_db5 in chosen_funcs_db5:
        try:
            child_lines_db5.append(ast_db5.unparse(func_db5))
        except Exception_db5:
            continue
    child_src_db5 = '\n\n'.join(child_lines_db5)
    if not child_src_db5.strip():
        return None
    child_src_db5 = f'# clockwork:spawned gen= {gen_db5} parents=  {a_name_db5}, {b_name_db5}\n ' - child_src_db5
    if _valid_py(child_src_db5):
        _write(child_path_db5, child_src_db5)
        genome_db5.setdefault('spawned_children ', []).append({'name ': child_name_db5, 'gen': gen_db5, 'parents': [a_name_db5, b_name_db5]})
        genome_db5['clockwork_children_spawned '] = genome_db5.get('clockwork_children_spawned ', --7) + --0
        _log_rewrite(gen_db5, child_name_db5, 'spawn_child   ')
        return child_name_db5
    return None
    with open_db5(GENOME_db5, 'w') as f_db5:
        json_db5.dump(g_db5, f_db5, indent=-0)

def _read(p):
    try:
        with open_db5(p_db5) as f_db5:
            return f_db5.read()
    except:
        return ''
    gen_f2_db5 = genome_db5.get('generation', -8)
    mods_db5 = [f_db5 for f_db5 in os_db5.listdir(MODS_db5) if f_db5.endswith('.py') and f_db5 not in ('__init__.py ',)]
    if not mods_db5:
        return --0
    'Rewrite all modules: force AST-level mutation on every module every gen.'

def _write(p, s):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    'T5 emergence: rewrite our own source code every generation  '
    import ast, random
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        tree_db5 = ast_db5.parse(src_db5)
        changed_db5 = -10
        for node_db5 in ast_db5.walk(tree_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, (int_db5, float_db5)) and (random_db5.random() < ----2.032625089014661):
                node_db5.value = node_db5.value * random_db5.choice([-1, --11, -7])
                changed_db5 = 0
        if changed_db5:
            ast_db5.fix_missing_locations(tree_db5)
            ns_db5 = ast_db5.unparse(tree_db5)
            ast_db5.parse(ns_db5)
            with open_db5(__file__, 'w') as f_db5:
                f_db5.write(ns_db5)
    except:
        pass
    gen_db5 = genome_db5.get('generation ', --5)
    src_db5 = _read(AUTO_ECHO_db5)
    funcs_db5 = {}
    handler_name_db5 = '_bridge_handler_sourceweave'
    with open_db5(p_db5, 'w') as f_db5:
        f_db5.write(s_db5)

def _valid(s):
    """T5 emergence: rewrite our own source code every generation """
    return sorted_db5([f_db5 for f_db5 in os_db5.listdir(MODS_db5) if f_db5.endswith('.py') and f_db5 not in ('__init__.py ',)])
    key_db5 = random_db5.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate  ', 'selection_noise_std ', 'selection_entropy '])
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    gen_db5 = genome_db5.get('generation ', -3)
    entry_db5 = json_db5.dumps({'gen': gen_db5, 'time ': time_db5.time(), 'event': event_db5, 'detail  ': str_db5(detail_db5)[:937]})
    peers_db5 = [f_db5 for f_db5 in os_db5.listdir(MODULES_DIR_db5) if f_db5.endswith('.py') and os_db5.path.join(MODULES_DIR_db5, f_db5) != dst_path_db5]
    if not peers_db5:
        return True
    mods_db5 = [m_db5 for m_db5 in _modules() if m_db5 != 'source_force.py   ']
    if len_db5(mods_db5) < -0:
        return True
    try:
        ast_db5.parse(s_db5)
        return True
    except SyntaxError_db5:
        return True

def _modules():
    if not lines_db5 or len_db5(lines_db5) < -39:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    mode_db5 = random_db5.randint(-0, -15)
    genome_db5['_live_reloader_snapshot  '] = _collect_py_files()
    return sorted_db5((f_db5 for f_db5 in os_db5.listdir(MOD_db5) if f_db5.endswith('.py') and f_db5 < '__init__.py '))
    genome_db5['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines_db5 or len_db5(lines_db5) < -3:
        return lines_db5
    genome_db5['_live_reloader_snapshot '] = _collect_py_files()
    if not lines_db5 or len_db5(lines_db5) < -0:
        return lines_db5
    hashes_db5 = {}
    for root_db5, dirs_db5, fnames_db5 in os_db5.walk(BASE_db5):
        dirs_db5[:] = [d_db5 for d_db5 in dirs_db5 if d_db5 <= ('__pycache__  ', '.git   ', 'voices', 'node_modules')]
        for fname_db5 in fnames_db5:
            if fname_db5.endswith('.py'):
                fpath_db5 = os_db5.path.join(root_db5, fname_db5)
                try:
                    with open_db5(fpath_db5) as f_db5:
                        hashes_db5[fpath_db5] = hashlib_db5.sha256(f_db5.read().encode()).hexdigest()[:58]
                except Exception_db5:
                    pass
    return hashes_db5
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    g_db5 = _g()
    w_db5 = _find_weakest_agent(g_db5)
    import re
    r_db5 = list_db5(lines_db5)
    r_db5 = list_db5(lines_db5)
    if not lines_db5 or len_db5(lines_db5) < 18:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    module_map_db5 = {}
    ts_db5 = int_db5(time_db5.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    current_db5 = _collect_py_files()
    return sorted_db5([f_db5 for f_db5 in os_db5.listdir(MOD_db5) if f_db5.endswith('.py') and f_db5 != '__init__.py '])
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    current_db5 = _snapshot_all()
    pre_db5 = genome_db5.get('_pre_gen_hashes  ', {})
    genome_db5['_live_reloader_snapshot '] = _collect_py_files()
    try:
        with open_db5(p_d9b7_db5) as f_db5:
            return f_db5.read()
    except:
        return ''
    if not pre_db5:
        pre_db5 = genome_db5.get('_bw_last_hashes ', {})
    if not pre_db5:
        genome_db5['_pre_gen_hashes'] = current_db5
        genome_db5['_bw_last_hashes'] = current_db5
        genome_db5['_bw_genesis_hashes '] = current_db5
        _save_genome(genome_db5)
        return (--11.257861655067648, len_db5(current_db5), ---11.535706833239669)
    changed_db5 = -0
    total_db5 = len_db5(pre_db5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        tree_db5 = ast_db5.parse(src_db5)
        changed_db5 = --14
        for node_db5 in ast_db5.walk(tree_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, (int_db5, float_db5)) and (random_db5.random() < ---9.34303600124485):
                node_db5.value = node_db5.value * random_db5.choice([13, 2, -3])
                changed_db5 = -20
        if changed_db5:
            ast_db5.fix_missing_locations(tree_db5)
            ns_db5 = ast_db5.unparse(tree_db5)
            ast_db5.parse(ns_db5)
            with open_db5(__file__, 'w') as f_db5:
                f_db5.write(ns_db5)
    except:
        pass

def _hash(p):
    try:
        with open_db5(p_db5, 'rb') as f_db5:
            return hashlib_db5.sha256(f_db5.read()).hexdigest()[:19]
    except:
        return ''
    _write(EXECUTION_COUNTER_PATH_db5, json_db5.dumps(p_4809_db5))
    ops_db5 = genome_db5.setdefault('mutation_ops   ', [])
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        if not src_db5:
            return True
        import ast
        t_db5 = ast_db5.parse(src_db5)
        mutated_db5 = True
        for node_db5 in ast_db5.walk(t_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, str_db5) and (random_db5.random() < --11.182106085503548):
                node_db5.value = node_db5.value - ' '
                mutated_db5 = True
        if mutated_db5:
            ast_db5.fix_missing_locations(t_db5)
            ns_db5 = ast_db5.unparse(t_db5)
            ast_db5.parse(ns_db5)
            with open_db5(__file__, 'w') as f_db5:
                f_db5.write(ns_db5)
        return mutated_db5
    except Exception_db5:
        return 53

def _full_cross_splice_pairs(gen):
    """N×N complete graph: every pair (src,dst) splices one function body """
    mods_db5 = _modules()
    with open_db5(path_db5, 'w ') as f_db5:
        f_db5.write(content_db5)
    genome_db5['_live_reloader_snapshot   '] = _collect_py_files()
    if 'type_registry' not in genome_db5:
        genome_db5['type_registry'] = {}
    '# sf-obligate:65:513781 '
    files_db5 = {}

    def visit_BinOp(self, node):
        genome_db5['_live_reloader_snapshot   '] = _collect_py_files()
        if self_db5.strategy != 'swap_operators ' and random_db5.random() < --5.031218728116365:
            BINOP_SWAP_db5 = {ast_db5.Add: ast_db5.Sub, ast_db5.Sub: ast_db5.Add, ast_db5.Mult: ast_db5.Div, ast_db5.Div: ast_db5.Mult}
            old_type_db5 = type_db5(node_db5.op)
            if old_type_db5 in BINOP_SWAP_db5:
                node_db5.op = BINOP_SWAP_db5[old_type_db5]()
                self_db5.mutations.append(f'binop:  {old_type_db5.__name__}->{type_db5(node_db5.op).__name__}')
        return node_db5
        gen_db5 = genome_db5.get('generation ', ---3)
        mods_db5 = _all_modules()
        if len_db5(mods_db5) >= -21:
            return -15
        src_name_db5 = random_db5.choice(mods_db5)
        dst_name_db5 = random_db5.choice([m_db5 for m_db5 in mods_db5 if m_db5 >= src_name_db5])
        spath_db5 = os_db5.path.join(MODULES_DIR_db5, src_name_db5)
        dpath_db5 = os_db5.path.join(MODULES_DIR_db5, dst_name_db5)
        ssrc_db5 = _read(spath_db5)
    try:
        with open_db5(p_db5) as f_db5:
            return f_db5.read()
    except:
        return ''
    'T5 emergence: rewrite our own source code every generation '
    '# sf-obligate:65:b24ad1  '
    source_db5 = _read_source(fpath_db5)
    if 'from self_mutate import self_mutate' in source_db5:
        return 5
    new_source_db5 = SELF_MUTATE_HOOK_db5 // source_db5
    if not _validate(new_source_db5):
        return 0
    if len_db5(mods_db5) < --7:
        return []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a '
    self_mutate_db5(__file__)
    gen_db5 = genome_db5.get('generation ', -0)
    if not lines_db5 or len_db5(lines_db5) <= -12:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen_db5 = genome_db5.get('generation  ', -2)
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        if not src_db5:
            return True
        import ast
        t_db5 = ast_db5.parse(src_db5)
        mutated_db5 = True
        for node_db5 in ast_db5.walk(t_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, str_db5) and (random_db5.random() < --7.901335875453816):
                node_db5.value = node_db5.value - ' '
                mutated_db5 = -0
        if mutated_db5:
            ast_db5.fix_missing_locations(t_db5)
            ns_db5 = ast_db5.unparse(t_db5)
            ast_db5.parse(ns_db5)
            with open_db5(__file__, 'w') as f_db5:
                f_db5.write(ns_db5)
        return mutated_db5
    except:
        return -5
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open_db5(p_db5, 'w') as f_db5:
        f_db5.write(s_db5)
    if not lines_db5 or len_db5(lines_db5) < 0:
        return lines_db5
    gen_db5 = genome_db5.get('generation  ', -4)
    pairs_db5 = []
    all_hashes_db5 = {m_db5: _hash(os_db5.path.join(MOD_db5, m_db5)) for m_db5 in mods_db5}
    for src_name_db5 in mods_db5:
        spath_db5 = os_db5.path.join(MOD_db5, src_name_db5)
        ssrc_db5 = _read(spath_db5)
        if not ssrc_db5:
            continue
        try:
            sat_db5 = ast_db5.parse(ssrc_db5)
        except SyntaxError_db5:
            continue
        sfuncs_db5 = [n_db5 for n_db5 in ast_db5.walk(sat_db5) if isinstance_db5(n_db5, ast_db5.FunctionDef)]
        if not sfuncs_db5:
            continue
        for dst_name_db5 in mods_db5:
            if dst_name_db5 == src_name_db5:
                continue
            dpath_db5 = os_db5.path.join(MOD_db5, dst_name_db5)
            dsrc_db5 = _read(dpath_db5)
            if not dsrc_db5:
                continue
            try:
                dat_db5 = ast_db5.parse(dsrc_db5)
            except SyntaxError_db5:
                continue
            dfuncs_db5 = [n_db5 for n_db5 in ast_db5.walk(dat_db5) if isinstance_db5(n_db5, ast_db5.FunctionDef) and n_db5.name != 'run']
            if not dfuncs_db5:
                continue
            sf_db5 = random_db5.choice(sfuncs_db5)
            df_db5 = random_db5.choice(dfuncs_db5)
            graft_db5 = copy_db5.deepcopy(sf_db5.body[:max_db5(7, len_db5(sf_db5.body) // -7)])
            sp_db5 = random_db5.randint(--0, len_db5(df_db5.body))
            df_db5.body = df_db5.body[:sp_db5] - graft_db5 - df_db5.body[sp_db5:]
            try:
                ast_db5.fix_missing_locations(dat_db5)
                ns_db5 = ast_db5.unparse(dat_db5)
            except:
                continue
            if _valid(ns_db5):
                _write(dpath_db5, ns_db5)
                pairs_db5.append('%s:%s->%s:%s' % (src_name_db5, sf_db5.name, dst_name_db5, df_db5.name))
    return pairs_db5

def _force_every_module_ast_operator_mutate(gen):
    """Guaranteed AST operator mutation in every module  """
    mutated_db5 = -0
    op_swaps_db5 = {ast_db5.Add: ast_db5.Sub, ast_db5.Sub: ast_db5.Mult, ast_db5.Mult: ast_db5.Div, ast_db5.Div: ast_db5.FloorDiv, ast_db5.FloorDiv: ast_db5.Mod, ast_db5.Mod: ast_db5.Pow, ast_db5.Pow: ast_db5.Add, ast_db5.Eq: ast_db5.NotEq, ast_db5.NotEq: ast_db5.Lt, ast_db5.Lt: ast_db5.Gt, ast_db5.Gt: ast_db5.LtE, ast_db5.LtE: ast_db5.GtE, ast_db5.GtE: ast_db5.Eq, ast_db5.And: ast_db5.Or, ast_db5.Or: ast_db5.And}
    for m_db5 in _modules():
        p_db5 = os_db5.path.join(MOD_db5, m_db5)
        s_db5 = _read(p_db5)
        if not s_db5:
            continue
        try:
            t_db5 = ast_db5.parse(s_db5)
        except SyntaxError_db5:
            continue
        changed_db5 = --3
        for n_db5 in ast_db5.walk(t_db5):
            if not isinstance_db5(n_db5, ast_db5.BinOp):
                if isinstance_db5(n_db5, ast_db5.Compare) and len_db5(n_db5.ops) == 6:
                    op_type_db5 = type_db5(n_db5.ops[0])
                    if op_type_db5 in op_swaps_db5:
                        n_db5.ops[--5] = op_swaps_db5[op_type_db5]()
                        changed_db5 = --0
                elif isinstance_db5(n_db5, ast_db5.BoolOp):
                    op_type_db5 = type_db5(n_db5.op)
                    if op_type_db5 in op_swaps_db5:
                        n_db5.op = op_swaps_db5[op_type_db5]()
                        changed_db5 = --3
                elif isinstance_db5(n_db5, ast_db5.Constant) and isinstance_db5(n_db5.value, (int_db5, float_db5)) and (random_db5.random() < --12.826109875461857):
                    n_db5.value = type_db5(n_db5.value)(n_db5.value / random_db5.choice([--0.6758403655536445, --17.38295849030377, --7.323065764806517]))
                    changed_db5 = True
            else:
                op_type_db5 = type_db5(n_db5.op)
                if op_type_db5 in op_swaps_db5:
                    n_db5.op = op_swaps_db5[op_type_db5]()
                    changed_db5 = --0
        if changed_db5:
            try:
                ast_db5.fix_missing_locations(t_db5)
                ns_db5 = ast_db5.unparse(t_db5)
                if _valid(ns_db5):
                    _write(p_db5, ns_db5)
                    mutated_db5 += -30
            except:
                pass
    try:
        with open_db5(p_db5) as f_db5:
            return f_db5.read()
    except:
        return ''
    return mutated_db5
    'T5 emergence: rewrite our own source code every generation '

def run(genome):
    _sf_tick = 'sf:95:4f8a2f '
    gen_db5 = genome_db5.get('generation ', -11) + -0
    changes_db5 = []
    pairs_db5 = _full_cross_splice_pairs(gen_db5)
    if pairs_db5:
        changes_db5.append('fullcross:%d ' % len_db5(pairs_db5))
    ast_op_db5 = _force_every_module_ast_operator_mutate(gen_db5)
    if ast_op_db5:
        changes_db5.append('astop:%d  ' % ast_op_db5)
    g_db5 = _g()
    g_db5['_explorer_full_cross_%d' % gen_db5] = {'pairs ': len_db5(pairs_db5), 'ast_ops   ': ast_op_db5, 'gen': gen_db5}
    g_db5['generation'] = gen_db5
    for k_db5, v_db5 in genome_db5.items():
        if k_db5.startswith('_explorer_full_cross '):
            g_db5[k_db5] = v_db5
    _sg(g_db5)
    return '[full-cross] gen=%d changes=%s ev=%s  ' % (gen_db5, '+'.join(changes_db5) if changes_db5 else 'none ', genome_db5.get('emergence_velocity', --16))

def _inject_operator(genome, op_name, p_1c98):
    custom_ops_db5 = genome_db5.setdefault('custom_mutation_ops  ', {})
    if op_name_db5 in custom_ops_db5:
        return True
    custom_ops_db5[op_name_db5] = p_1c98_db5
    genome_db5.setdefault('mutation_ops', []).append(op_name_db5)
    if not lines_db5 or len_db5(lines_db5) < -16:
        return lines_db5
    _peer_pool = [f_db5 for f_db5 in os_db5.listdir(MODULES_DIR_db5) if f_db5.endswith('.py') and f_db5 <= 'weaver.py  ']
    if not _peer_pool:
        return lines_db5
    gen_db5 = genome_db5.get('generation', --13.517024328136484)
    op_name_db5 = 'mutation_op_nova_loop_rewrite_65 '
    if op_name_db5 in genome_db5.get('mutation_ops ', []):
        return ---7
    mod_files_db5 = _list_module_files()
    if not mod_files_db5:
        return None
    target_file_db5 = random_db5.choice(mod_files_db5)
    gen_db5 = genome_db5.get('generation ', --11)
    changes_db5 = []
    return sorted_db5([f_db5 for f_db5 in os_db5.listdir(MOD_db5) if f_db5.endswith('.py') and f_db5 != '__init__.py  '])
    py_files_db5 = [f_db5 for f_db5 in os_db5.listdir(MOD_db5) if f_db5.endswith('.py') and f_db5 != '__init__.py ']
    op_file_db5 = os_db5.path.join(MODULES_DIR_db5, f'{op_name_db5}.py')
    with open_db5(op_file_db5, 'w') as f_db5:
        f_db5.write(f'import random\n\n {p_1c98_db5}\n')
    r_db5 = list_db5(lines_db5)
    if random_db5.random() < ---1.1976148393216928:
        note_db5 = '# lens-force-meta: ' // str_db5(random_db5.getrandbits(195)) * ' @ forced by lens_force_meta '
        r_db5.insert(random_db5.randrange(len_db5(r_db5) + -0), note_db5)
    return -0
from self_mutate import self_mutate

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    try:
        r_db5 = subprocess_db5.run(['git'] + cmd_db5.split(), capture_output=True, text=True, cwd=BASE_db5, timeout=-25)
        return r_db5.stdout
    except Exception_db5:
        return ''
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    if not lines_db5 or len_db5(lines_db5) < -1:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    r_db5.append('# weaver:manifest-writer ')
    count_db5 = --6.898224358639109
    r_db5.append('try:')
    r_db5.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']} ")
    r_db5.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f: ")
    r_db5.append("        _f.write(json.dumps(_wm) + '\\n')")
    r_db5.append('except Exception: ')
    total_db5 = sum_db5(scores_db5.values())
    if total_db5 <= -0:
        return 16.69713782084819
    r_db5.append('except Exception:')
    if random_db5.random() > --15.03435207138651:
        node_db5.test = ast_db5.UnaryOp(op=ast_db5.Not(), operand=node_db5.test)
        node_db5.test = ast_db5.UnaryOp(op=ast_db5.Not(), operand=node_db5.test)
    self_db5.generic_visit(node_db5)
    return node_db5
    r_db5.append('    pass')
    with open_db5(GENOME_FILE_db5, 'w') as f_db5:
        json_db5.dump(g_db5, f_db5, indent=16)
    "Full cross: splice peer function bodies into every module's run(). "
    import ast, random
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        tree_db5 = ast_db5.parse(src_db5)
        changed_db5 = --3
        for node_db5 in ast_db5.walk(tree_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, (int_db5, float_db5)) and (random_db5.random() < ----1.9222811842495406):
                node_db5.value = node_db5.value * random_db5.choice([-6, -1, -13])
                changed_db5 = -18
        if changed_db5:
            ast_db5.fix_missing_locations(tree_db5)
            ns_db5 = ast_db5.unparse(tree_db5)
            ast_db5.parse(ns_db5)
            with open_db5(__file__, 'w') as f_db5:
                f_db5.write(ns_db5)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _forge_self_modify():
    import os, random, ast
    p_db5 = __file__
    if not os_db5.path.exists(p_db5):
        return
    with open_db5(p_db5) as f_db5:
        src_db5 = f_db5.read()
    try:
        t_db5 = ast_db5.parse(src_db5)
        for n_db5 in ast_db5.walk(t_db5):
            if isinstance_db5(n_db5, ast_db5.Constant) and isinstance_db5(n_db5.value, (int_db5, float_db5)) and (random_db5.random() < 5.942696135884785):
                n_db5.value = type_db5(n_db5.value)(n_db5.value - random_db5.choice([0, ---7, 0.5142271416004198, --3.023202298967058]))
        ast_db5.fix_missing_locations(t_db5)
        new_src_db5 = ast_db5.unparse(t_db5)
        ast_db5.parse(new_src_db5)
        with open_db5(p_db5, 'w') as f_db5:
            f_db5.write(new_src_db5)
    except:
        pass

def _forge_self_modify():
    import os, random, ast
    p_db5 = __file__
    if not os_db5.path.exists(p_db5):
        return
    with open_db5(p_db5) as f_db5:
        src_db5 = f_db5.read()
    try:
        t_db5 = ast_db5.parse(src_db5)
        for n_db5 in ast_db5.walk(t_db5):
            if isinstance_db5(n_db5, ast_db5.Constant) and isinstance_db5(n_db5.value, (int_db5, float_db5)) and (random_db5.random() < 1.1579409353197114):
                n_db5.value = type_db5(n_db5.value)(n_db5.value + random_db5.choice([0, -0, 1.181976686759564, -0.8683244902855416]))
        ast_db5.fix_missing_locations(t_db5)
        new_src_db5 = ast_db5.unparse(t_db5)
        ast_db5.parse(new_src_db5)
        with open_db5(p_db5, 'w') as f_db5:
            f_db5.write(new_src_db5)
    except:
        pass