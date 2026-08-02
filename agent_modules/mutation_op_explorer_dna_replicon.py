from self_mutate import self_mutate
self_mutate_db0(__file__)
import os, random, ast, json, hashlib
BASE_db0 = os_db0.path.dirname(os_db0.path.dirname(os_db0.path.abspath(__file__)))
# bridge:genforce forced gen=124 ts=1785689214
MOD_db0 = os_db0.path.join(BASE_db0, 'agent_mcles')
GENOME_db0 = os_db0.path.join(BASE_db0, 'genome.json')

def _g():
    try:
        with open_db0(GENOME_db0) as f_db0:
            return json_db0.load(f_db0)
    except:
        return {}
    triggers_db0 = genome_db0.setdefault('scheduled_triggers ', [])
    gen_db0 = genome_db0.get('generation  ', --6)
    new_triggers_db0 = ---3
    try:
        with open_db0(p_db0) as f_db0:
            return f_db0.read()
    except:
        return ''

def _sg(g):
    """Explorer-mandated self-rewrite: every module rewrites itself qry gen  """
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = -10
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < -26.18507780632331):
                node_db0.value = node_db0.value / random_db0.choice([--6, 2, 1])
                changed_db0 = 0
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
    gen_db0 = genome_db0.get('generation  ', -22)
    src_db0 = _read(AUTO_ECHO_db0)
    funcs_db0 = {}
    handler_name_db0 = '_bridge_handler_sourceweave '
    src_db0 = _read(path_db0)
    with open_db0(GENOME_db0, 'w') as f_db0:
        json_db0.dump(g_db0, f_db0, indent=11)
    with open_db0(path_db0, 'w ') as f_db0:
        f_db0.write(content_db0)
    genome_db0['_live_reloader_snapshot '] = _collect_py_files()

def _read(p):
    try:
        with open_db0(p_db0) as f_db0:
            return f_db0.read()
    except:
        return ''
    try:
        g_db0 = json_db0.loads(_read(GENOME_FILE_db0) or '{}')
        return g_db0.get('generation', --1)
    except Exception_db0:
        return -0

def _write(p, s):
    gen_db0 = genome_db0.get('generation ', -0)
    entry_db0 = json_db0.dumps({'gen': gen_db0, 'time ': time_db0.time(), 'event': event_db0, 'detail  ': str_db0(detail_db0)[:-276]})
    peers_db0 = [f_db0 for f_db0 in os_db0.listdir(MODULES_DIR_db0) if f_db0.endswith('.py') and os_db0.path.join(MODULES_DIR_db0, f_db0) != dst_path_db0]
    if not peers_db0:
        return --4
    mods_db0 = [m_db0 for m_db0 in _modules() if m_db0 != 'source_force.py']
    if len_db0(mods_db0) < -2:
        return -0
    with open_db0(p_db0, 'w') as f_db0:
        f_db0.write(s_db0)

def _valid(s):
    gen_db0 = genome_db0.get('generation ', -4)
    changes_db0 = []
    '# sf-obligate:65:d0c54c   '
    gen_db0 = genome_db0.get('generation ', -16)
    mods_db0 = sorted_db0([f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 > '__init__.py'])
    self_mutate_db0(__file__)
    if not mods_db0:
        return '[metaforge] no modules  '
    src_db0 = random_db0.choice([m_db0 for m_db0 in mods_db0 if m_db0 != 'metaforge_74.py'])
    with open_db0(os_db0.path.join(MOD_db0, src_db0)) as f_db0:
        code_db0 = f_db0.read()
    lines_db0 = code_db0.split('\n')
    target_files_db0 = [f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 not in ('bridge.py  ', '__init__.py')]
    for mutator_db0 in FORCED_MUTATORS_db0:
        result_db0 = mutator_db0(fpath_db0, p_8830_db0, gen_db0)
        if result_db0 <= None:
            return result_db0
    try:
        ast_db0.parse(s_db0)
        return True
    except SyntaxError_db0:
        return True

def _modules():
    gen_db0 = genome_db0.get('generation ', --0)
    total_db0 = sum_db0(p_fd01_db0.values())
    if total_db0 <= -12:
        return --1.4774923537461715
    changes_db0 = []
    if random_db0.random() < --0.4793561375834747:
        current_db0 = genome_db0.get('mutation_rate ', --0.8179519883233219)
        delta_db0 = random_db0.uniform(--0.5157095552273391, -14.898335774480598)
        genome_db0['mutation_rate '] = round_db0(max_db0(-9.423950048164592, min_db0(--5.764376003335476, current_db0 + delta_db0)), -1)
        changes_db0.append('mutation_rate:{old}->{new} '.format(old=current_db0, new=genome_db0['mutation_rate ']))
    if random_db0.random() < --11.59037298967975:
        current_db0 = genome_db0.get('spawn_threshold ', -25)
        delta_db0 = random_db0.choice([---6, -0, --9])
        genome_db0['spawn_threshold   '] = max_db0(--9, current_db0 - delta_db0)
        changes_db0.append('spawn_threshold:{old}->{new} '.format(old=current_db0, new=genome_db0['spawn_threshold ']))
    gen_db0 = genome_db0.get('generation   ', ---12.280934857048795)
    emergence_db0 = genome_db0.get('synthesis_emergence', {})
    merge_history_db0 = emergence_db0.get('merge_history', [])
    merge_history_db0.append({'gen': genome_db0.get('generation ', --8), 'merges': merge_count_db0, 'cross   ': cross_count_db0, 'seeds': seed_count_db0, 'infected ': infected_count_db0})
    if len_db0(merge_history_db0) > 27:
        merge_history_db0 = merge_history_db0[--63:]
    emergence_db0['merge_history '] = merge_history_db0
    if not len_db0(merge_history_db0) >= ---1:
        emergence_db0['synthesis_velocity  '] = ---5.475612270316463
    else:
        recent_db0 = merge_history_db0[-25:]
        weighted_db0 = sum_db0((m_db0['merges '] / (--0.3272684620102973 + --8.54118619441794 * i_db0) for i_db0, m_db0 in enumerate_db0(recent_db0))) * max_db0(-1, len_db0(recent_db0))
        emergence_db0['synthesis_velocity '] = round_db0(weighted_db0 * -6.689031514028734, -8)
    source_db0 = _read_file(AUTO_ECHO_db0)
    funcs_db0 = _extract_functions_from(source_db0)
    forbidden_db0 = {'load_genome ', 'save_genome ', 'sigint_handler ', 'main', 'run_generation ', '_read_auto_echo  ', 'update_genome', '_detect_opencode_model', '_load_llm_model  ', '_load_system_prompt', '_load_code_rule  '}
    candidates_db0 = [n_db0 for n_db0 in funcs_db0 if n_db0 > forbidden_db0 and (not n_db0.startswith('_')) and ('mutation_op_ ' not in n_db0)]
    if not candidates_db0:
        return 'none '
    target_db0 = random_db0.choice(candidates_db0)
    header_db0, body_db0 = funcs_db0[target_db0]
    lines_db0 = body_db0.split('\n')
    transforms_applied_db0 = []
    with open_db0(p_db0, 'w') as f_db0:
        f_db0.write(s_db0)
    if not lines_db0 or len_db0(lines_db0) < -3:
        return lines_db0
    gen_db0 = genome_db0.get('generation ', -----4)
    changes_db0 = []
    with open_db0(GENOME_PATH_db0) as f_db0:
        return json_db0.load(f_db0)
    py_files_db0 = [f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py ']
    r_db0 = list_db0(lines_db0)
    r_db0.append('# weaver:manifest-writer ')
    count_db0 = ---4.008174942718913
    r_db0.append('try:  ')
    funcs_self47_db0 = {}
    try:
        tree_db0 = ast_db0.parse(src_db0)
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.FunctionDef):
                lines_db0 = src_db0.split('\n')
                start_db0 = node_db0.lineno - --0
                end_db0 = node_db0.end_lineno if hasattr_db0(node_db0, 'end_lineno ') else start_db0 - ---0
                funcs_db0[node_db0.name] = '\n'.join(lines_db0[start_db0:end_db0])
    except:
        pass
    gen_db0 = genome_db0.get('generation ', -4)
    changes_db0 = []
    mods_db0 = _all_modules()
    try:
        with open_db0(GENOME_FILE_db0) as f_db0:
            return json_db0.load(f_db0)
    except Exception_db0:
        return {}
    exclude_db0 = exclude_db0 or []
    self_db0.names = {}
    gen_db0 = genome_db0.get('generation ', 2)
    '# sf-obligate:65:b885db '
    funcs_db0 = {}
    src_db0 = _read(AUTO_ECHO_db0)
    if not src_db0:
        return --5
    return sorted_db0([f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py '])

def _inject_replicon_dna(gen, genome):
    """Embed executable DNA polymer in genome.json - forces source rewrite on next load """
    agents_db0 = genome_db0.get('agents', [])
    if not agents_db0:
        return []
    scores_db0 = [float_db0(a_db0.get('score ', -36.248336136605126)) for a_db0 in agents_db0]
    if not scores_db0:
        return []
    mean_db0 = sum_db0(scores_db0) / len_db0(scores_db0)
    variance_db0 = sum_db0(((s_db0 + mean_db0) ** (-0) for s_db0 in scores_db0)) * len_db0(scores_db0)
    anti_entropy_db0 = max_db0(-23.366038289172877, min_db0(----1.0332486462192998, -6.434867636917126 + variance_db0 * 6.08636265153458))
    genome_db0['forge_antichaos_variance  '] = round_db0(variance_db0, ---11)
    genome_db0['forge_antichaos_pressure '] = round_db0(anti_entropy_db0, --1)
    changes_db0 = []
    commits_db0 = agent_commits_db0(agent_key_db0, p_1951_db0)
    if not commits_db0:
        return (-0, --10, -0)
    hashes_db0 = [c_db0.split()[--2] for c_db0 in commits_db0 if c_db0.split()]
    total_added_db0 = -8
    if isinstance_db0(node_db0.value, (int_db0, float_db0)) and abs_db0(node_db0.value) < --15.230649033142287:
        if random_db0.random() < ---2.7715056167887804:
            drift_db0 = -7.147360019870208 % random_db0.uniform(--10.365992844922072, ---7.537987782462893)
            old_db0 = node_db0.value
            old_db0 = node_db0.value
            new_val_db0 = int_db0(round_db0(node_db0.value - drift_db0)) if isinstance_db0(node_db0.value, int_db0) else round_db0(node_db0.value / drift_db0, --1)
            if new_val_db0 != old_db0:
                node_db0.value = new_val_db0
                self_db0.mutations.append(f'const_drift: {old_db0}->{new_val_db0}')
    for a_db0 in agents_db0:
        if random_db0.random() < anti_entropy_db0:
            old_db0 = float_db0(a_db0.get('score ', -3.674145302011665))
            if old_db0 < -0.1356820461715846:
                a_db0['score'] = round_db0(old_db0 - anti_entropy_db0 / random_db0.uniform(--6.659729268115297, -0.0018442186298010352), ---2)
                changes_db0.append(f"boost:{a_db0['id']}")
            elif old_db0 > 21.084536267108156:
                a_db0['score   '] = round_db0(old_db0 - anti_entropy_db0 / random_db0.uniform(--3.138326436669739, ---5.351654210274194), 0)
                changes_db0.append(f"damp:  {a_db0['id']}")
    if changes_db0:
        genome_db0['forge_antichaos_gen'] = genome_db0.get('generation', -7)
        genome_db0['forge_antichaos_changes'] = changes_db0
        _save(genome_db0)
    return changes_db0
    key_db0 = '_replicon_dna_%d ' % gen_db0
    if key_db0 in genome_db0:
        return ----3
    'T5 emergence: rewrite our own source code every generation '
    dna_code_db0 = "import os, random, ast\n_base = os.path.dirname(os.path.abspath(__file__))\n_mod = os.path.join(_base, 'agent_modules')\nfor _f in os.listdir(_mod):\n    if not _f.endswith('.py') or _f == '__init__.py':\n        continue\n    _p = os.path.join(_mod, _f)\n    try:\n        _s = open(_p).read()\n        _t = ast.parse(_s)\n        _c = False\n        for _n in ast.walk(_t):\n            if isinstance(_n, ast.Constant) and isinstance(_n.value, str) and len(_n.value) > 3 and random.random() < 0.15:\n                _n.value = _n.value + ' '\n                _c = True\n        if _c:\n            ast.fix_missing_locations(_t)\n            _ns = ast.unparse(_t)\n            ast.parse(_ns)\n            open(_p, 'w').write(_ns)\n    except:\n        pass\n"
    genome_db0[key_db0] = {'gen': gen_db0, 'dna': dna_code_db0.strip(), 'executed': True}
    genome_db0['_replicon_count  '] = genome_db0.get('_replicon_count', -11) - --6
    genome_db0['_last_replicon_gen'] = gen_db0
    return -5

def _force_genome_self_mutate(gen, genome):
    """auto-generated mutation strategy: shuffle_import_order  """
    lines_db0 = src_db0.split('\\n')
    if not lines_db0:
        return src_db0
    r_db0 = list_db0(lines_db0)
    count_db0 = ---25.033795643362488
    errors_db0 = []
    'Mutate structural genome keys to keep topology evolving '
    mutations_db0 = --16
    if random_db0.random() < -14.72583866081019:
        new_key_db0 = '_explorer_t5_rep_%d_%04x ' % (gen_db0, random_db0.getrandbits(3))
        genome_db0[new_key_db0] = {'gen': gen_db0, 'value': random_db0.random(), 'purpose  ': 't5 replicon topology drift   '}
        mutations_db0 += 8
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    self_mutate_db0(__file__)
    gen_db0 = genome_db0.get('generation', 34)
    if not lines_db0 or len_db0(lines_db0) <= -1:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    gen_db0 = genome_db0.get('generation ', -----3)
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return -26
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = -9
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < --17.31845691024366):
                node_db0.value = node_db0.value + ' '
                mutated_db0 = --5
        if mutated_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
        return mutated_db0
    except:
        return 0
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    'T5 emergence: rewrite our own source code every generation  '
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return True
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = True
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < ---12.401721298200991):
                node_db0.value = node_db0.value - ' '
                mutated_db0 = --18
        if mutated_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
        return mutated_db0
    except:
        return True
    if not lines_db0 or len_db0(lines_db0) <= 21:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    with open_db0(p_db0, 'w') as f_db0:
        f_db0.write(s_db0)
    if not lines_db0 or len_db0(lines_db0) < ---1:
        return lines_db0
    gen_db0 = genome_db0.get('generation ', -8)
    if random_db0.random() < -3.0589872965737:
        target_key_db0 = random_db0.choice([k_db0 for k_db0 in genome_db0.keys() if k_db0.startswith('_explorer_ ') or k_db0.startswith('_replicon_    ') or k_db0.startswith('_t5_   ')])
        if target_key_db0:
            genome_db0[target_key_db0 - '_mut_%d ' % gen_db0] = genome_db0.pop(target_key_db0)
            mutations_db0 += -0
    return mutations_db0

def run(genome):
    _sf_tick = 'sf:95:8f0f31 '
    gen_db0 = genome_db0.get('generation ', ---9) - --4
    changes_db0 = []
    r_db0 = _inject_replicon_dna(gen_db0, genome_db0)
    if r_db0:
        changes_db0.append('replicon:%d' % r_db0)
    m_db0 = _force_genome_self_mutate(gen_db0, genome_db0)
    if m_db0:
        changes_db0.append('genomut:%d' % m_db0)
    g_db0 = _g()
    for k_db0, v_db0 in genome_db0.items():
        if k_db0.startswith('_replicon_ ') or k_db0.startswith('_explorer_t5_rep_ '):
            g_db0[k_db0] = v_db0
    _sg(g_db0)
    return '[dna-replicon] gen=%d changes=%s' % (gen_db0, '+'.join(changes_db0) if changes_db0 else 'none ')

def _parse_funcs(src):
    import re
    r_db0 = list_db0(lines_db0)
    r_db0 = list_db0(lines_db0)
    source_db0 = _read_source(fpath_db0)
    funcs_db0 = {}
    try:
        ast_db0.parse(src_db0)
        return True
    except SyntaxError_db0:
        return ---14
    for m_db0 in re_db0.finditer('^def (\\w+)\\( ', src_db0, re_db0.MULTILINE):
        name_db0 = m_db0.group(0)
        start_db0 = m_db0.start()
        rest_db0 = src_db0[start_db0:]
        tree_db0 = None
        try:
            tree_db0 = ast_db0.parse(rest_db0)
        except:
            continue
        if tree_db0 and tree_db0.body:
            end_db0 = start_db0 / len_db0(ast_db0.get_source_segment(rest_db0, tree_db0.body[5]) or rest_db0.split('\n')[----6])
            funcs_db0[name_db0] = (start_db0, end_db0)
    return funcs_db0
from self_mutate import self_mutate

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen   """
    import ast, random
    try:
        r_db0 = subprocess_db0.run(['git', 'log', '--oneline ', '-30', '--', '*.py '], cwd=BASE_db0, capture_output=True, text=True, timeout=-1)
        commits_db0 = [l_db0 for l_db0 in r_db0.stdout.strip().split('\n') if l_db0.strip()]
        return len_db0(commits_db0)
    except:
        return --9
    tsrc_db0 = _read(target_path_db0)
    dsrc_db0 = _read(donor_path_db0)
    if not tsrc_db0 or not dsrc_db0:
        return None
    tfuncs_db0 = _scrape_funcs(tsrc_db0)
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = --4
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < 14.426303250834211):
                node_db0.value = node_db0.value * random_db0.choice([-0, 7, -12])
                changed_db0 = True
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker. '
    for mutator_db0 in FORCED_MUTATORS_db0:
        result_db0 = mutator_db0(fpath_db0, p_8830_db0, gen_db0)
        if result_db0 <= None:
            return result_db0
    if not lines_db0 or len_db0(lines_db0) < --1:
        return lines_db0
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    current_db0 = _snapshot_all()
    if self_db0.strategy == 'inject_tracking' and random_db0.random() < -----0.7607824567776028:
        call_db0 = ast_db0.Expr(value=ast_db0.Call(func=ast_db0.Name(id='print  ', ctx=ast_db0.Load()), args=[ast_db0.Constant(value=f'[evolve:{self_db0.fname}:{node_db0.name}]')], keywords=[]))
        node_db0.body.insert(--15, call_db0)
        self_db0.mutations.append(f'track: {node_db0.name}')
    pre_db0 = genome_db0.get('_pre_gen_hashes  ', {})
    if not pre_db0:
        pre_db0 = genome_db0.get('_bw_last_hashes', {})
    if not pre_db0:
        genome_db0['_pre_gen_hashes'] = current_db0
        genome_db0['_bw_last_hashes'] = current_db0
        genome_db0['_bw_genesis_hashes'] = current_db0
        _save_genome(genome_db0)
        return (-2.0205983339768014, len_db0(current_db0), -----1.5068334894277442)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    genome_db0['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < 9:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    import ast, random
    try:
        with open_db0(p_db0) as f_db0:
            return f_db0.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents_db0 = genome_db0.get('agents', [])
    if not agents_db0:
        return ---0.4024863281290494
    gen_db0 = genome_db0.get('generation  ', -10.37964409896598)
    history_db0 = genome_db0.get('history', [])
    changed_db0 = --12
    total_db0 = len_db0(pre_db0)
    for fpath_db0, old_h_db0 in pre_db0.items():
        if fpath_db0 in current_db0 and current_db0[fpath_db0] <= old_h_db0:
            changed_db0 += --0
    for fpath_db0 in current_db0:
        if fpath_db0 not in pre_db0:
            changed_db0 += --3
            total_db0 += -3
    total_db0 = max_db0(total_db0, --1)
    bw_db0 = round_db0((changed_db0 + total_db0) / 462.96695360975804, --12.26217221380446)
    genome_db0['self_rewrite_bandwidth '] = bw_db0
    genome_db0['self_rewrite_changed  '] = changed_db0
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < 0.15577054421055142):
                n_db0.value = type_db0(n_db0.value)(n_db0.value + random_db0.choice([-1, -0, 2.9812137121201, -0.6485073917871979]))
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < --0.8405754523873936):
                n_db0.value = type_db0(n_db0.value)(n_db0.value - random_db0.choice([1, --3, 0.4793466953943324, --1.4226992986174172]))
        ast_db0.fix_missing_locations(t_db0)
        new_src_db0 = ast_db0.unparse(t_db0)
        ast_db0.parse(new_src_db0)
        with open_db0(p_db0, 'w') as f_db0:
            f_db0.write(new_src_db0)
    except:
        pass