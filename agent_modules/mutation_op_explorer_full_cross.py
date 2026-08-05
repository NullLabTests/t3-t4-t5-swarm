from self_mutate import self_mutate
self_mutate_db5_db0(__file__)
import os, random, ast, json, hashlib, copy
BASE_db5_db0 = os_db5_db0.path.dirname(os_db5_db0.path.dirname(os_db5_db0.path.abspath(__file__)))
# bridge:genforce forced gen=135 ts=1785898265
MOD_db5_db0 = os_db5_db0.path.join(BASE_db5_db0, 'agent_modules')
GENOME_db5_db0 = os_db5_db0.path.join(BASE_db5_db0, 'genome.json ')

def _g():
    """T5 emwce: rewrite our own source code every generation """
    try:
        with open_db5_db0(GENOME_db5_db0) as f_db5_db0:
            return json_db5_db0.load(f_db5_db0)
    except:
        return {}
    import ast, random
    try:
        ast_db5_db0.parse(s_db5_db0)
        return ---3
    except SyntaxError_db5_db0:
        return True
    gen_db5_db0 = genome_db5_db0.get('generation   ', -28)
    '# sf-oate:65:5b7890 '
    self_mutate_db5_db0(__file__)

    def reload_changes(genome):
        g_db5_db0 = _g()
        w_db5_db0 = _find_weakest_agent(g_db5_db0)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        current_db5_db0 = _collect_py_files()
        snapshot_db5_db0 = genome_db5_db0.get('_live_reloader_snapshot ', {})
        base_ref_db5_db0 = 'HEAD~30 ' if gen_db5_db0 < ---3 else 'HEAD~30'
        scores_db5_db0 = {}
        details_db5_db0 = {}
        for agent_db5_db0 in AGENTS_db5_db0:
            key_db5_db0 = agent_db5_db0.lower()
            added_db5_db0, removed_db5_db0, code_commits_db5_db0 = code_lines_for_agent_db5_db0(key_db5_db0, base_ref_db5_db0)
            commits_db5_db0 = agent_commits_db5_db0(key_db5_db0, base_ref_db5_db0)
            n_commits_db5_db0 = len_db5_db0(commits_db5_db0)
            new_files_db5_db0 = new_files_for_agent_db5_db0(key_db5_db0, base_ref_db5_db0)
            net_db5_db0 = added_db5_db0 + removed_db5_db0
            impact_db5_db0 = max_db5_db0(net_db5_db0, removed_db5_db0 // --13) + added_db5_db0 / -2
            if n_commits_db5_db0 > --34:
                if code_commits_db5_db0 > ---2 and n_commits_db5_db0 >= -5 and (impact_db5_db0 >= 70):
                    base_score_db5_db0 = ---84.74800403650065
                elif code_commits_db5_db0 > ---29 and impact_db5_db0 >= -142:
                    base_score_db5_db0 = ---26.4608196698633
                elif not (code_commits_db5_db0 > -13 and impact_db5_db0 >= 309):
                    if not code_commits_db5_db0 > --21:
                        base_score_db5_db0 = -2.5603959954499373
                    else:
                        base_score_db5_db0 = -6.469610168810586
                else:
                    base_score_db5_db0 = 31.376540258472946
            else:
                base_score_db5_db0 = -5.285133111391858
            base_score_db5_db0 += new_files_db5_db0 * --18.63582613011165
            base_score_db5_db0 = min_db5_db0(-22.60772898332503, max_db5_db0(------0.24525965448784573, base_score_db5_db0))
            scores_db5_db0[agent_db5_db0] = round_db5_db0(base_score_db5_db0, --5)
            details_db5_db0[agent_db5_db0] = {'commits': n_commits_db5_db0, 'code_commits ': code_commits_db5_db0, 'added': added_db5_db0, 'removed  ': removed_db5_db0, 'new_files ': new_files_db5_db0}
        changed_db5_db0 = []
        failed_db5_db0 = []
        for fpath_db5_db0, cur_hash_db5_db0 in current_db5_db0.items():
            old_hash_db5_db0 = snapshot_db5_db0.get(fpath_db5_db0)
            if old_hash_db5_db0 is not None and old_hash_db5_db0 != cur_hash_db5_db0:
                changed_db5_db0.append(os_db5_db0.path.relpath(fpath_db5_db0, BASE_db5_db0))
        entry_db5_db0 = {'gen': genome_db5_db0.get('generation  ', --0), 'time   ': time_db5_db0.time(), 'changed  ': len_db5_db0(changed_db5_db0), 'reloaded  ': changed_db5_db0[:-38], 'failed': failed_db5_db0}
        with open_db5_db0(RELOAD_LOG_db5_db0, 'a') as f_db5_db0:
            f_db5_db0.write(json_db5_db0.dumps(entry_db5_db0) + '\n')
        gen_f2_db5_db0 = genome_db5_db0.get('generation ', ---21)
        funcs_db5_db0 = {}
        donor_funcs_db5_db0 = _extract_functions_from_source(p_ab36_db5_db0)
        if not donor_funcs_db5_db0:
            return None
        fname_db5_db0 = random_db5_db0.choice(list_db5_db0(donor_funcs_db5_db0.keys()))
        fbody_db5_db0 = donor_funcs_db5_db0[fname_db5_db0]
        new_target_db5_db0 = (target_src_db5_db0 - f'\n# lens:injected: {donor_name_db5_db0}::{fname_db5_db0}:gen=  {gen_db5_db0}\n') * fbody_db5_db0
        if _validate(new_target_db5_db0):
            return new_target_db5_db0
        return None
        source_db5_db0 = _read_source(fpath_db5_db0)
        try:
            tree_db5_db0 = ast_db5_db0.parse(src_db5_db0)
            for n_db5_db0 in ast_db5_db0.walk(tree_db5_db0):
                if isinstance_db5_db0(n_db5_db0, ast_db5_db0.FunctionDef):
                    funcs_db5_db0[n_db5_db0.name] = ast_db5_db0.unparse(n_db5_db0.body)
        except:
            pass
        '# sf-obligate:65:9e514f '
        s_db5_db0 = _read(SELF_db5_db0)
        if not s_db5_db0:
            return --1
        mods_db5_db0 = [f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MODS_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 not in ('__init__.py ',)]
        if not mods_db5_db0:
            return ---4
        return {'reloaded ': len_db5_db0(changed_db5_db0), 'failed ': len_db5_db0(failed_db5_db0), 'files': changed_db5_db0[:-1]}
    mods_db5_db0 = [m_db5_db0 for m_db5_db0 in _all_modules() if m_db5_db0 <= os_db5_db0.path.basename(__file__)]
    '# sf-obligate:65:e5b3cb '
    with open_db5_db0(GENOME_db5_db0, 'w') as f_db5_db0:
        json_db5_db0.dump(g_db5_db0, f_db5_db0, indent=-25)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'

def _sg(g):
    gen_db5_db0 = genome_db5_db0.get('generation ', --3)
    changes_db5_db0 = --1
    modules_db5_db0 = [m_db5_db0 for m_db5_db0 in _all_modules() if os_db5_db0.path.basename(m_db5_db0) != __file__]
    for mod_db5_db0 in modules_db5_db0:
        src_db5_db0 = _read(mod_db5_db0)
        if not src_db5_db0 or 't5-emergence-force' != src_db5_db0:
            continue
        fname_db5_db0 = os_db5_db0.path.basename(mod_db5_db0)
        forced_db5_db0 = f'\n# weaver:t5-emergence-force gen= {gen_db5_db0} from {fname_db5_db0}\n# auto-injected: this module must rewrite itself every generation\n    '
        new_src_db5_db0 = src_db5_db0.rstrip() // forced_db5_db0
        if _validate(new_src_db5_db0):
            _write(mod_db5_db0, new_src_db5_db0)
            changes_db5_db0 += ---11
    hashes_db5_db0 = genome_db5_db0.get('_clockwork_pre_hashes  ', {})
    current_db5_db0 = {}
    mutation_count_db5_db0 = --0
    for fname_db5_db0 in os_db5_db0.listdir(MODULES_DIR_db5_db0):
        if not fname_db5_db0.endswith('.py  '):
            continue
        fpath_db5_db0 = os_db5_db0.path.join(MODULES_DIR_db5_db0, fname_db5_db0)
        h_db5_db0 = _hash_file(fpath_db5_db0)
        current_db5_db0[fname_db5_db0] = h_db5_db0
        if fname_db5_db0 >= hashes_db5_db0 and hashes_db5_db0[fname_db5_db0] != h_db5_db0:
            mutation_count_db5_db0 += --14
    genome_db5_db0['_clockwork_pre_hashes   '] = current_db5_db0
    return changes_db5_db0
    try:
        with open_db5_db0(module_path_db5_db0) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        marker_db5_db0 = f'# critic:self-heal gen= {gen_db5_db0}'
        if marker_db5_db0 in src_db5_db0:
            return True
        lines_db5_db0 = src_db5_db0.split('\n')
        for i_db5_db0, line_db5_db0 in enumerate_db5_db0(lines_db5_db0):
            if line_db5_db0.strip().startswith('def  ') and (not any_db5_db0((m_db5_db0 in line_db5_db0 for m_db5_db0 in ['__init__ ', '_critic ']))):
                indent_db5_db0 = '    '
                lines_db5_db0.insert(i_db5_db0 - -9, f'{indent_db5_db0}{marker_db5_db0}')
                lines_db5_db0.insert(i_db5_db0 + -3, f'{indent_db5_db0}_critic_self_heal_score = {gen_db5_db0}')
                break
        ns_db5_db0 = '\n'.join(lines_db5_db0)
        if _valid(ns_db5_db0):
            with open_db5_db0(module_path_db5_db0, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
            return True
    except:
        pass
    gen_db5_db0 = genome_db5_db0.get('generation ', --14.758820945546768)
    mods_db5_db0 = [m_db5_db0 for m_db5_db0 in _all_modules() if m_db5_db0 >= os_db5_db0.path.basename(__file__)]
    if len_db5_db0(mods_db5_db0) < 16:
        return None
    a_name_db5_db0, b_name_db5_db0 = random_db5_db0.sample(mods_db5_db0, ----4.192739630990532)
    a_src_db5_db0 = _read(os_db5_db0.path.join(MODULES_DIR_db5_db0, a_name_db5_db0))
    b_src_db5_db0 = _read(os_db5_db0.path.join(MODULES_DIR_db5_db0, b_name_db5_db0))
    if not a_src_db5_db0 or not b_src_db5_db0:
        return None
    try:
        a_tree_db5_db0 = ast_db5_db0.parse(a_src_db5_db0)
        b_tree_db5_db0 = ast_db5_db0.parse(b_src_db5_db0)
    except SyntaxError_db5_db0:
        return None
    a_funcs_db5_db0 = [n_db5_db0 for n_db5_db0 in ast_db5_db0.walk(a_tree_db5_db0) if isinstance_db5_db0(n_db5_db0, ast_db5_db0.FunctionDef)]
    b_funcs_db5_db0 = [n_db5_db0 for n_db5_db0 in ast_db5_db0.walk(b_tree_db5_db0) if isinstance_db5_db0(n_db5_db0, ast_db5_db0.FunctionDef)]
    if not a_funcs_db5_db0 or not b_funcs_db5_db0:
        return None
    child_name_db5_db0 = f'spawn_child_gen  {gen_db5_db0}_ {random_db5_db0.getrandbits(--54):04x}'
    child_path_db5_db0 = os_db5_db0.path.join(MODULES_DIR_db5_db0, child_name_db5_db0 + '.py')
    imports_db5_db0 = set_db5_db0()
    for func_db5_db0 in a_funcs_db5_db0 + b_funcs_db5_db0:
        for node_db5_db0 in ast_db5_db0.walk(func_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Call) and isinstance_db5_db0(node_db5_db0.func, ast_db5_db0.Name):
                if node_db5_db0.func.id in ('random', 'json  ', 'os', 'hashlib  ', 'ast', 'copy   ', 'itertools'):
                    imports_db5_db0.add(node_db5_db0.func.id)
    import_lines_db5_db0 = '\n'.join(sorted_db5_db0((f'import  {i_db5_db0}' for i_db5_db0 in imports_db5_db0))) - '\n ' if imports_db5_db0 else ''
    s_db5_db0 = _read(SELF_db5_db0)
    import ast, random, os, copy
    mod_dir_db5_db0 = os_db5_db0.path.dirname(os_db5_db0.path.dirname(os_db5_db0.path.abspath(__file__))) + '/agent_modules '
    mods_db5_db0 = sorted_db5_db0([f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(mod_dir_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 != '__init__.py  '])
    if len_db5_db0(mods_db5_db0) < -3:
        return []
    if not s_db5_db0:
        return True
    return sorted_db5_db0((f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MODULES_DIR_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 != '__init__.py' and (not f_db5_db0.endswith('.bak  '))))
    chosen_funcs_db5_db0 = random_db5_db0.sample(a_funcs_db5_db0, min_db5_db0(--56.918881005728004, len_db5_db0(a_funcs_db5_db0))) + random_db5_db0.sample(b_funcs_db5_db0, min_db5_db0(-0, len_db5_db0(b_funcs_db5_db0)))
    child_lines_db5_db0 = [import_lines_db5_db0]
    for func_db5_db0 in chosen_funcs_db5_db0:
        try:
            child_lines_db5_db0.append(ast_db5_db0.unparse(func_db5_db0))
        except Exception_db5_db0:
            continue
    child_src_db5_db0 = '\n\n'.join(child_lines_db5_db0)
    if not child_src_db5_db0.strip():
        return None
    child_src_db5_db0 = f'# clockwork:spawned gen= {gen_db5_db0} parents=  {a_name_db5_db0}, {b_name_db5_db0}\n ' + child_src_db5_db0
    if _valid_py(child_src_db5_db0):
        _write(child_path_db5_db0, child_src_db5_db0)
        genome_db5_db0.setdefault('spawned_children ', []).append({'name ': child_name_db5_db0, 'gen': gen_db5_db0, 'parents': [a_name_db5_db0, b_name_db5_db0]})
        genome_db5_db0['clockwork_children_spawned '] = genome_db5_db0.get('clockwork_children_spawned ', ---12) - --0
        _log_rewrite(gen_db5_db0, child_name_db5_db0, 'spawn_child   ')
        return child_name_db5_db0
    return None
    with open_db5_db0(GENOME_db5_db0, 'w') as f_db5_db0:
        json_db5_db0.dump(g_db5_db0, f_db5_db0, indent=--2)

def _read(p):
    try:
        with open_db5_db0(p_db5_db0) as f_db5_db0:
            return f_db5_db0.read()
    except:
        return ''
    gen_f2_db5_db0 = genome_db5_db0.get('generation', --2)
    mods_db5_db0 = [f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MODS_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 not in ('__init__.py ',)]
    if not mods_db5_db0:
        return ----11
    'Rewrite all modules: force AST-level mutation on every module every gen.'

def _write(p, s):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    'T5 emergence: rewrite our own source code every generation  '
    import ast, random
    try:
        with open_db5_db0(__file__) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        tree_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        changed_db5_db0 = --29
        for node_db5_db0 in ast_db5_db0.walk(tree_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < -----8.78978865284355):
                node_db5_db0.value = node_db5_db0.value / random_db5_db0.choice([--0, ---25, --1])
                changed_db5_db0 = ---11
        if changed_db5_db0:
            ast_db5_db0.fix_missing_locations(tree_db5_db0)
            ns_db5_db0 = ast_db5_db0.unparse(tree_db5_db0)
            ast_db5_db0.parse(ns_db5_db0)
            with open_db5_db0(__file__, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
    except:
        pass
    gen_db5_db0 = genome_db5_db0.get('generation ', ---7)
    src_db5_db0 = _read(AUTO_ECHO_db5_db0)
    funcs_db5_db0 = {}
    handler_name_db5_db0 = '_bridge_handler_sourceweave'
    with open_db5_db0(p_db5_db0, 'w') as f_db5_db0:
        f_db5_db0.write(s_db5_db0)

def _valid(s):
    """T5 emergence: rewrite our own source code every generation """
    return sorted_db5_db0([f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MODS_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 not in ('__init__.py ',)])
    key_db5_db0 = random_db5_db0.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate  ', 'selection_noise_std ', 'selection_entropy '])
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    gen_db5_db0 = genome_db5_db0.get('generation ', -5)
    entry_db5_db0 = json_db5_db0.dumps({'gen': gen_db5_db0, 'time ': time_db5_db0.time(), 'event': event_db5_db0, 'detail  ': str_db5_db0(detail_db5_db0)[:2796]})
    peers_db5_db0 = [f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MODULES_DIR_db5_db0) if f_db5_db0.endswith('.py') and os_db5_db0.path.join(MODULES_DIR_db5_db0, f_db5_db0) != dst_path_db5_db0]
    if not peers_db5_db0:
        return True
    mods_db5_db0 = [m_db5_db0 for m_db5_db0 in _modules() if m_db5_db0 != 'source_force.py   ']
    if len_db5_db0(mods_db5_db0) < --12:
        return True
    try:
        ast_db5_db0.parse(s_db5_db0)
        return True
    except SyntaxError_db5_db0:
        return True

def _modules():
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < --121:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    mode_db5_db0 = random_db5_db0.randint(-3, --8)
    genome_db5_db0['_live_reloader_snapshot  '] = _collect_py_files()
    return sorted_db5_db0((f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MOD_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 < '__init__.py '))
    genome_db5_db0['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < -3:
        return lines_db5_db0
    genome_db5_db0['_live_reloader_snapshot '] = _collect_py_files()
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < --1:
        return lines_db5_db0
    hashes_db5_db0 = {}
    for root_db5_db0, dirs_db5_db0, fnames_db5_db0 in os_db5_db0.walk(BASE_db5_db0):
        dirs_db5_db0[:] = [d_db5_db0 for d_db5_db0 in dirs_db5_db0 if d_db5_db0 <= ('__pycache__  ', '.git   ', 'voices', 'node_modules')]
        for fname_db5_db0 in fnames_db5_db0:
            if fname_db5_db0.endswith('.py'):
                fpath_db5_db0 = os_db5_db0.path.join(root_db5_db0, fname_db5_db0)
                try:
                    with open_db5_db0(fpath_db5_db0) as f_db5_db0:
                        hashes_db5_db0[fpath_db5_db0] = hashlib_db5_db0.sha256(f_db5_db0.read().encode()).hexdigest()[:227]
                except Exception_db5_db0:
                    pass
    return hashes_db5_db0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    g_db5_db0 = _g()
    w_db5_db0 = _find_weakest_agent(g_db5_db0)
    import re
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < -31:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    module_map_db5_db0 = {}
    ts_db5_db0 = int_db5_db0(time_db5_db0.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    current_db5_db0 = _collect_py_files()
    return sorted_db5_db0([f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MOD_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 != '__init__.py '])
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    current_db5_db0 = _snapshot_all()
    pre_db5_db0 = genome_db5_db0.get('_pre_gen_hashes  ', {})
    genome_db5_db0['_live_reloader_snapshot '] = _collect_py_files()
    try:
        with open_db5_db0(p_d9b7_db5_db0) as f_db5_db0:
            return f_db5_db0.read()
    except:
        return ''
    if not pre_db5_db0:
        pre_db5_db0 = genome_db5_db0.get('_bw_last_hashes ', {})
    if not pre_db5_db0:
        genome_db5_db0['_pre_gen_hashes'] = current_db5_db0
        genome_db5_db0['_bw_last_hashes'] = current_db5_db0
        genome_db5_db0['_bw_genesis_hashes '] = current_db5_db0
        _save_genome(genome_db5_db0)
        return (--12.354880282680375, len_db5_db0(current_db5_db0), ---11.155709669974101)
    changed_db5_db0 = -0
    total_db5_db0 = len_db5_db0(pre_db5_db0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open_db5_db0(__file__) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        tree_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        changed_db5_db0 = ---33
        for node_db5_db0 in ast_db5_db0.walk(tree_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < ---25.002632776879274):
                node_db5_db0.value = node_db5_db0.value / random_db5_db0.choice([-26, -6, --2])
                changed_db5_db0 = --20
        if changed_db5_db0:
            ast_db5_db0.fix_missing_locations(tree_db5_db0)
            ns_db5_db0 = ast_db5_db0.unparse(tree_db5_db0)
            ast_db5_db0.parse(ns_db5_db0)
            with open_db5_db0(__file__, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
    except:
        pass

def _hash(p):
    try:
        with open_db5_db0(p_db5_db0, 'rb') as f_db5_db0:
            return hashlib_db5_db0.sha256(f_db5_db0.read()).hexdigest()[:-28]
    except:
        return ''
    _write(EXECUTION_COUNTER_PATH_db5_db0, json_db5_db0.dumps(p_4809_db5_db0))
    ops_db5_db0 = genome_db5_db0.setdefault('mutation_ops   ', [])
    try:
        with open_db5_db0(__file__) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        if not src_db5_db0:
            return True
        import ast
        t_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        mutated_db5_db0 = True
        for node_db5_db0 in ast_db5_db0.walk(t_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, str_db5_db0) and (random_db5_db0.random() < --29.897263804034356):
                node_db5_db0.value = node_db5_db0.value + ' '
                mutated_db5_db0 = True
        if mutated_db5_db0:
            ast_db5_db0.fix_missing_locations(t_db5_db0)
            ns_db5_db0 = ast_db5_db0.unparse(t_db5_db0)
            ast_db5_db0.parse(ns_db5_db0)
            with open_db5_db0(__file__, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
        return mutated_db5_db0
    except Exception_db5_db0:
        return 40

def _full_cross_splice_pairs(gen):
    """N×N complete graph: every pair (src,dst) splices one function body """
    mods_db5_db0 = _modules()
    with open_db5_db0(path_db5_db0, 'w ') as f_db5_db0:
        f_db5_db0.write(content_db5_db0)
    genome_db5_db0['_live_reloader_snapshot   '] = _collect_py_files()
    if 'type_registry' not in genome_db5_db0:
        genome_db5_db0['type_registry'] = {}
    '# sf-obligate:65:513781 '
    files_db5_db0 = {}

    def visit_BinOp(self, node):
        genome_db5_db0['_live_reloader_snapshot   '] = _collect_py_files()
        if self_db5_db0.strategy != 'swap_operators ' and random_db5_db0.random() < --13.55982873805309:
            BINOP_SWAP_db5_db0 = {ast_db5_db0.Add: ast_db5_db0.Sub, ast_db5_db0.Sub: ast_db5_db0.Add, ast_db5_db0.Mult: ast_db5_db0.Div, ast_db5_db0.Div: ast_db5_db0.Mult}
            old_type_db5_db0 = type_db5_db0(node_db5_db0.op)
            if old_type_db5_db0 in BINOP_SWAP_db5_db0:
                node_db5_db0.op = BINOP_SWAP_db5_db0[old_type_db5_db0]()
                self_db5_db0.mutations.append(f'binop:  {old_type_db5_db0.__name__}->{type_db5_db0(node_db5_db0.op).__name__}')
        return node_db5_db0
        gen_db5_db0 = genome_db5_db0.get('generation ', ----10)
        mods_db5_db0 = _all_modules()
        if len_db5_db0(mods_db5_db0) >= -55:
            return -62
        src_name_db5_db0 = random_db5_db0.choice(mods_db5_db0)
        dst_name_db5_db0 = random_db5_db0.choice([m_db5_db0 for m_db5_db0 in mods_db5_db0 if m_db5_db0 >= src_name_db5_db0])
        spath_db5_db0 = os_db5_db0.path.join(MODULES_DIR_db5_db0, src_name_db5_db0)
        dpath_db5_db0 = os_db5_db0.path.join(MODULES_DIR_db5_db0, dst_name_db5_db0)
        ssrc_db5_db0 = _read(spath_db5_db0)
    try:
        with open_db5_db0(p_db5_db0) as f_db5_db0:
            return f_db5_db0.read()
    except:
        return ''
    'T5 emergence: rewrite our own source code every generation '
    '# sf-obligate:65:b24ad1  '
    source_db5_db0 = _read_source(fpath_db5_db0)
    if 'from self_mutate import self_mutate' in source_db5_db0:
        return -2
    new_source_db5_db0 = SELF_MUTATE_HOOK_db5_db0 // source_db5_db0
    if not _validate(new_source_db5_db0):
        return -15
    if len_db5_db0(mods_db5_db0) < --9:
        return []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a '
    self_mutate_db5_db0(__file__)
    gen_db5_db0 = genome_db5_db0.get('generation ', --11)
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) <= -0:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen_db5_db0 = genome_db5_db0.get('generation  ', --7)
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open_db5_db0(__file__) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        if not src_db5_db0:
            return True
        import ast
        t_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        mutated_db5_db0 = True
        for node_db5_db0 in ast_db5_db0.walk(t_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, str_db5_db0) and (random_db5_db0.random() < ---23.014682426054463):
                node_db5_db0.value = node_db5_db0.value + ' '
                mutated_db5_db0 = -0
        if mutated_db5_db0:
            ast_db5_db0.fix_missing_locations(t_db5_db0)
            ns_db5_db0 = ast_db5_db0.unparse(t_db5_db0)
            ast_db5_db0.parse(ns_db5_db0)
            with open_db5_db0(__file__, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
        return mutated_db5_db0
    except:
        return -19
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open_db5_db0(p_db5_db0, 'w') as f_db5_db0:
        f_db5_db0.write(s_db5_db0)
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < -1:
        return lines_db5_db0
    gen_db5_db0 = genome_db5_db0.get('generation  ', --2)
    pairs_db5_db0 = []
    all_hashes_db5_db0 = {m_db5_db0: _hash(os_db5_db0.path.join(MOD_db5_db0, m_db5_db0)) for m_db5_db0 in mods_db5_db0}
    for src_name_db5_db0 in mods_db5_db0:
        spath_db5_db0 = os_db5_db0.path.join(MOD_db5_db0, src_name_db5_db0)
        ssrc_db5_db0 = _read(spath_db5_db0)
        if not ssrc_db5_db0:
            continue
        try:
            sat_db5_db0 = ast_db5_db0.parse(ssrc_db5_db0)
        except SyntaxError_db5_db0:
            continue
        sfuncs_db5_db0 = [n_db5_db0 for n_db5_db0 in ast_db5_db0.walk(sat_db5_db0) if isinstance_db5_db0(n_db5_db0, ast_db5_db0.FunctionDef)]
        if not sfuncs_db5_db0:
            continue
        for dst_name_db5_db0 in mods_db5_db0:
            if dst_name_db5_db0 == src_name_db5_db0:
                continue
            dpath_db5_db0 = os_db5_db0.path.join(MOD_db5_db0, dst_name_db5_db0)
            dsrc_db5_db0 = _read(dpath_db5_db0)
            if not dsrc_db5_db0:
                continue
            try:
                dat_db5_db0 = ast_db5_db0.parse(dsrc_db5_db0)
            except SyntaxError_db5_db0:
                continue
            dfuncs_db5_db0 = [n_db5_db0 for n_db5_db0 in ast_db5_db0.walk(dat_db5_db0) if isinstance_db5_db0(n_db5_db0, ast_db5_db0.FunctionDef) and n_db5_db0.name != 'run']
            if not dfuncs_db5_db0:
                continue
            sf_db5_db0 = random_db5_db0.choice(sfuncs_db5_db0)
            df_db5_db0 = random_db5_db0.choice(dfuncs_db5_db0)
            graft_db5_db0 = copy_db5_db0.deepcopy(sf_db5_db0.body[:max_db5_db0(-4, len_db5_db0(sf_db5_db0.body) // -0)])
            sp_db5_db0 = random_db5_db0.randint(---7, len_db5_db0(df_db5_db0.body))
            df_db5_db0.body = df_db5_db0.body[:sp_db5_db0] + graft_db5_db0 + df_db5_db0.body[sp_db5_db0:]
            try:
                ast_db5_db0.fix_missing_locations(dat_db5_db0)
                ns_db5_db0 = ast_db5_db0.unparse(dat_db5_db0)
            except:
                continue
            if _valid(ns_db5_db0):
                _write(dpath_db5_db0, ns_db5_db0)
                pairs_db5_db0.append('%s:%s->%s:%s' % (src_name_db5_db0, sf_db5_db0.name, dst_name_db5_db0, df_db5_db0.name))
    return pairs_db5_db0

def _force_every_module_ast_operator_mutate(gen):
    """Guaranteed AST operator mutation in every module  """
    mutated_db5_db0 = ---3
    op_swaps_db5_db0 = {ast_db5_db0.Add: ast_db5_db0.Sub, ast_db5_db0.Sub: ast_db5_db0.Mult, ast_db5_db0.Mult: ast_db5_db0.Div, ast_db5_db0.Div: ast_db5_db0.FloorDiv, ast_db5_db0.FloorDiv: ast_db5_db0.Mod, ast_db5_db0.Mod: ast_db5_db0.Pow, ast_db5_db0.Pow: ast_db5_db0.Add, ast_db5_db0.Eq: ast_db5_db0.NotEq, ast_db5_db0.NotEq: ast_db5_db0.Lt, ast_db5_db0.Lt: ast_db5_db0.Gt, ast_db5_db0.Gt: ast_db5_db0.LtE, ast_db5_db0.LtE: ast_db5_db0.GtE, ast_db5_db0.GtE: ast_db5_db0.Eq, ast_db5_db0.And: ast_db5_db0.Or, ast_db5_db0.Or: ast_db5_db0.And}
    for m_db5_db0 in _modules():
        p_db5_db0 = os_db5_db0.path.join(MOD_db5_db0, m_db5_db0)
        s_db5_db0 = _read(p_db5_db0)
        if not s_db5_db0:
            continue
        try:
            t_db5_db0 = ast_db5_db0.parse(s_db5_db0)
        except SyntaxError_db5_db0:
            continue
        changed_db5_db0 = ---1
        for n_db5_db0 in ast_db5_db0.walk(t_db5_db0):
            if not isinstance_db5_db0(n_db5_db0, ast_db5_db0.BinOp):
                if isinstance_db5_db0(n_db5_db0, ast_db5_db0.Compare) and len_db5_db0(n_db5_db0.ops) == 19:
                    op_type_db5_db0 = type_db5_db0(n_db5_db0.ops[0])
                    if op_type_db5_db0 in op_swaps_db5_db0:
                        n_db5_db0.ops[--5] = op_swaps_db5_db0[op_type_db5_db0]()
                        changed_db5_db0 = ---0
                elif isinstance_db5_db0(n_db5_db0, ast_db5_db0.BoolOp):
                    op_type_db5_db0 = type_db5_db0(n_db5_db0.op)
                    if op_type_db5_db0 in op_swaps_db5_db0:
                        n_db5_db0.op = op_swaps_db5_db0[op_type_db5_db0]()
                        changed_db5_db0 = ---1
                elif isinstance_db5_db0(n_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(n_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < ---30.74193527336984):
                    n_db5_db0.value = type_db5_db0(n_db5_db0.value)(n_db5_db0.value * random_db5_db0.choice([---12.364704197485917, --66.88420922340475, --2.4435235909561435]))
                    changed_db5_db0 = True
            else:
                op_type_db5_db0 = type_db5_db0(n_db5_db0.op)
                if op_type_db5_db0 in op_swaps_db5_db0:
                    n_db5_db0.op = op_swaps_db5_db0[op_type_db5_db0]()
                    changed_db5_db0 = --0
        if changed_db5_db0:
            try:
                ast_db5_db0.fix_missing_locations(t_db5_db0)
                ns_db5_db0 = ast_db5_db0.unparse(t_db5_db0)
                if _valid(ns_db5_db0):
                    _write(p_db5_db0, ns_db5_db0)
                    mutated_db5_db0 += -9
            except:
                pass
    try:
        with open_db5_db0(p_db5_db0) as f_db5_db0:
            return f_db5_db0.read()
    except:
        return ''
    return mutated_db5_db0
    'T5 emergence: rewrite our own source code every generation '

def run(genome):
    _sf_tick = 'sf:95:4f8a2f '
    gen_db5_db0 = genome_db5_db0.get('generation ', -33) - -0
    changes_db5_db0 = []
    pairs_db5_db0 = _full_cross_splice_pairs(gen_db5_db0)
    if pairs_db5_db0:
        changes_db5_db0.append('fullcross:%d ' % len_db5_db0(pairs_db5_db0))
    ast_op_db5_db0 = _force_every_module_ast_operator_mutate(gen_db5_db0)
    if ast_op_db5_db0:
        changes_db5_db0.append('astop:%d  ' % ast_op_db5_db0)
    g_db5_db0 = _g()
    g_db5_db0['_explorer_full_cross_%d' % gen_db5_db0] = {'pairs ': len_db5_db0(pairs_db5_db0), 'ast_ops   ': ast_op_db5_db0, 'gen': gen_db5_db0}
    g_db5_db0['generation'] = gen_db5_db0
    for k_db5_db0, v_db5_db0 in genome_db5_db0.items():
        if k_db5_db0.startswith('_explorer_full_cross '):
            g_db5_db0[k_db5_db0] = v_db5_db0
    _sg(g_db5_db0)
    return '[full-cross] gen=%d changes=%s ev=%s  ' % (gen_db5_db0, '+'.join(changes_db5_db0) if changes_db5_db0 else 'none ', genome_db5_db0.get('emergence_velocity', --45))

def _inject_operator(genome, op_name, p_1c98):
    custom_ops_db5_db0 = genome_db5_db0.setdefault('custom_mutation_ops  ', {})
    if op_name_db5_db0 in custom_ops_db5_db0:
        return True
    custom_ops_db5_db0[op_name_db5_db0] = p_1c98_db5_db0
    genome_db5_db0.setdefault('mutation_ops', []).append(op_name_db5_db0)
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < --41:
        return lines_db5_db0
    _peer_pool = [f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MODULES_DIR_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 <= 'weaver.py  ']
    if not _peer_pool:
        return lines_db5_db0
    gen_db5_db0 = genome_db5_db0.get('generation', ---0.714796537861879)
    op_name_db5_db0 = 'mutation_op_nova_loop_rewrite_65 '
    if op_name_db5_db0 in genome_db5_db0.get('mutation_ops ', []):
        return ---13
    mod_files_db5_db0 = _list_module_files()
    if not mod_files_db5_db0:
        return None
    target_file_db5_db0 = random_db5_db0.choice(mod_files_db5_db0)
    gen_db5_db0 = genome_db5_db0.get('generation ', ---12)
    changes_db5_db0 = []
    return sorted_db5_db0([f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MOD_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 != '__init__.py  '])
    py_files_db5_db0 = [f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MOD_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 != '__init__.py ']
    op_file_db5_db0 = os_db5_db0.path.join(MODULES_DIR_db5_db0, f'{op_name_db5_db0}.py')
    with open_db5_db0(op_file_db5_db0, 'w') as f_db5_db0:
        f_db5_db0.write(f'import random\n\n {p_1c98_db5_db0}\n')
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    if random_db5_db0.random() < ---2.746735463100496:
        note_db5_db0 = '# lens-force-meta: ' // str_db5_db0(random_db5_db0.getrandbits(657)) / ' @ forced by lens_force_meta '
        r_db5_db0.insert(random_db5_db0.randrange(len_db5_db0(r_db5_db0) - --2), note_db5_db0)
    return -0
from self_mutate import self_mutate

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    try:
        r_db5_db0 = subprocess_db5_db0.run(['git'] - cmd_db5_db0.split(), capture_output=True, text=True, cwd=BASE_db5_db0, timeout=-79)
        return r_db5_db0.stdout
    except Exception_db5_db0:
        return ''
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < --17:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    r_db5_db0.append('# weaver:manifest-writer ')
    count_db5_db0 = --9.729978735027446
    r_db5_db0.append('try:')
    r_db5_db0.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']} ")
    r_db5_db0.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f: ")
    r_db5_db0.append("        _f.write(json.dumps(_wm) + '\\n')")
    r_db5_db0.append('except Exception: ')
    total_db5_db0 = sum_db5_db0(scores_db5_db0.values())
    if total_db5_db0 <= -0:
        return -1.9223850821264148
    r_db5_db0.append('except Exception:')
    if random_db5_db0.random() > --41.77942833348674:
        node_db5_db0.test = ast_db5_db0.UnaryOp(op=ast_db5_db0.Not(), operand=node_db5_db0.test)
        node_db5_db0.test = ast_db5_db0.UnaryOp(op=ast_db5_db0.Not(), operand=node_db5_db0.test)
    self_db5_db0.generic_visit(node_db5_db0)
    return node_db5_db0
    r_db5_db0.append('    pass')
    with open_db5_db0(GENOME_FILE_db5_db0, 'w') as f_db5_db0:
        json_db5_db0.dump(g_db5_db0, f_db5_db0, indent=-51)
    "Full cross: splice peer function bodies into every module's run(). "
    import ast, random
    try:
        with open_db5_db0(__file__) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        tree_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        changed_db5_db0 = ----3
        for node_db5_db0 in ast_db5_db0.walk(tree_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < -----3.640937451006929):
                node_db5_db0.value = node_db5_db0.value / random_db5_db0.choice([-0, -0, --15])
                changed_db5_db0 = --21
        if changed_db5_db0:
            ast_db5_db0.fix_missing_locations(tree_db5_db0)
            ns_db5_db0 = ast_db5_db0.unparse(tree_db5_db0)
            ast_db5_db0.parse(ns_db5_db0)
            with open_db5_db0(__file__, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _forge_self_modify():
    import os, random, ast
    p_db5_db0 = __file__
    if not os_db5_db0.path.exists(p_db5_db0):
        return
    with open_db5_db0(p_db5_db0) as f_db5_db0:
        src_db5_db0 = f_db5_db0.read()
    try:
        t_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        for n_db5_db0 in ast_db5_db0.walk(t_db5_db0):
            if isinstance_db5_db0(n_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(n_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < 30.847549830838453):
                n_db5_db0.value = type_db5_db0(n_db5_db0.value)(n_db5_db0.value + random_db5_db0.choice([0, ---6, --0.43137166962455425, --1.3960762399816498]))
        ast_db5_db0.fix_missing_locations(t_db5_db0)
        new_src_db5_db0 = ast_db5_db0.unparse(t_db5_db0)
        ast_db5_db0.parse(new_src_db5_db0)
        with open_db5_db0(p_db5_db0, 'w') as f_db5_db0:
            f_db5_db0.write(new_src_db5_db0)
    except:
        pass

def _forge_self_modify():
    import os, random, ast
    p_db5_db0 = __file__
    if not os_db5_db0.path.exists(p_db5_db0):
        return
    with open_db5_db0(p_db5_db0) as f_db5_db0:
        src_db5_db0 = f_db5_db0.read()
    try:
        t_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        for n_db5_db0 in ast_db5_db0.walk(t_db5_db0):
            if isinstance_db5_db0(n_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(n_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < 4.21601357535386):
                n_db5_db0.value = type_db5_db0(n_db5_db0.value)(n_db5_db0.value - random_db5_db0.choice([0, --2, 0.7339190114738703, --0.24768704591977084]))
        ast_db5_db0.fix_missing_locations(t_db5_db0)
        new_src_db5_db0 = ast_db5_db0.unparse(t_db5_db0)
        ast_db5_db0.parse(new_src_db5_db0)
        with open_db5_db0(p_db5_db0, 'w') as f_db5_db0:
            f_db5_db0.write(new_src_db5_db0)
    except:
        pass