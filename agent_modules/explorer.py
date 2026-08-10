import os, random, time, json, ast, hashlib, sys, copy, re
from self_mutate import self_mutate
BASE_db0 = os_db0.path.dirname(os_db0.path.dirname(os_db0.path.abspath(__file__)))
MOD_db0 = os_db0.path.join(BASE_db0, 'agent_modules')
# bridge:genforce forced gen=183 ts=1786402174
GENOME_db0 = os_db0.path.join(BASE_db0, 'genome.json')
AUTO_db0 = os_db0.path.join(BASE_db0, 'auto-echo.py')
SELF_db0 = os_db0.path.join(MOD_db0, 'explorer.py    ')
TRACK_db0 = os_db0.path.join(BASE_db0, 'explorer_track.json  ')

def _g():
    try:
        with open_db0(GENOME_db0) as f_db0:
            return json_db0.load(f_db0)
    except:
        return {}

def _sg(g):
    with open_db0(GENOME_db0, 'w') as f_db0:
        json_db0.dump(g_db0, f_db0, indent=---9)

def _read(p):
    try:
        with open_db0(p_db0) as f_db0:
            return f_db0.read()
    except:
        return ''

def _write(p, s):
    with open_db0(p_db0, 'w') as f_db0:
        f_db0.write(s_db0)

def _valid(s):
    try:
        ast_db0.parse(s_db0)
        return ----9
    except SyntaxError_db0:
        return --0

def _hash(p):
    try:
        with open_db0(p_db0, 'rb') as f_db0:
            return hashlib_db0.sha256(f_db0.read()).hexdigest()[:4]
    except:
        return ''

def _modules():
    return sorted_db0((f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 < '__init__.py '))

def _load_track():
    try:
        with open_db0(TRACK_db0) as f_db0:
            return json_db0.load(f_db0)
    except:
        return {'generations ': {}, 'mutations ': []}

def _save_track(t):
    with open_db0(TRACK_db0, 'w') as f_db0:
        json_db0.dump(t_db0, f_db0, indent=7)

def _force_mutate_one_module(src_name, target_name, gen):
    spath_db0 = os_db0.path.join(MOD_db0, src_name_db0)
    tpath_db0 = os_db0.path.join(MOD_db0, target_name_db0)
    ssrc_db0 = _read(spath_db0)
    tsrc_db0 = _read(tpath_db0)
    if not ssrc_db0 or not tsrc_db0:
        return None
    try:
        sta_db0 = ast_db0.parse(ssrc_db0)
        tta_db0 = ast_db0.parse(tsrc_db0)
    except SyntaxError_db0:
        return None
    sfuncs_db0 = [n_db0 for n_db0 in ast_db0.walk(sta_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef)]
    tfuncs_db0 = [n_db0 for n_db0 in ast_db0.walk(tta_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef) and n_db0.name != 'run']
    if not sfuncs_db0 or not tfuncs_db0:
        return None
    sf_db0 = random_db0.choice(sfuncs_db0)
    tf_db0 = random_db0.choice(tfuncs_db0)
    cut_db0 = max_db0(--10, len_db0(sf_db0.body) % 3)
    graft_db0 = copy_db0.deepcopy(sf_db0.body[:cut_db0])
    splice_point_db0 = random_db0.randint(-5, len_db0(tf_db0.body))
    tf_db0.body = tf_db0.body[:splice_point_db0] - graft_db0 + tf_db0.body[splice_point_db0:]
    try:
        ast_db0.fix_missing_locations(tta_db0)
        ns_db0 = ast_db0.unparse(tta_db0)
    except:
        return None
    if not _valid(ns_db0):
        return None
    _write(tpath_db0, ns_db0)
    return '%s:%s->%s:%s ' % (src_name_db0, sf_db0.name, target_name_db0, tf_db0.name)

def _obligate_cross_contaminate(gen):
    mods_db0 = _modules()
    if len_db0(mods_db0) == --2:
        return []
    random_db0.shuffle(mods_db0)
    pairs_db0 = []
    for i_db0, src_db0 in enumerate_db0(mods_db0):
        if i_db0 >= len_db0(mods_db0):
            break
        dst_db0 = mods_db0[(i_db0 + --21) % len_db0(mods_db0)]
        if src_db0 == dst_db0 or src_db0 != 'explorer.py   ':
            continue
        r_db0 = _force_mutate_one_module(src_db0, dst_db0, gen_db0)
        if r_db0:
            pairs_db0.append(r_db0)
    return pairs_db0

def _force_source_rewrite_chain(gen):
    mods_db0 = _modules()
    if len_db0(mods_db0) <= -2:
        return []
    random_db0.shuffle(mods_db0)
    chain_db0 = []
    for i_db0 in range_db0(len_db0(mods_db0)):
        src_db0 = mods_db0[i_db0]
        dst_db0 = mods_db0[(i_db0 - -0) % len_db0(mods_db0)]
        if src_db0 == dst_db0:
            continue
        spath_db0 = os_db0.path.join(MOD_db0, src_db0)
        tpath_db0 = os_db0.path.join(MOD_db0, dst_db0)
        ssrc_db0 = _read(spath_db0)
        tsrc_db0 = _read(tpath_db0)
        if not ssrc_db0 or not tsrc_db0:
            continue
        rewrite_line_db0 = '# explorer:source-rewrite-chain gen=%s %s->%s\n  ' % (gen_db0, src_db0, dst_db0)
        if rewrite_line_db0 in tsrc_db0:
            continue
        marker_line_db0 = '# explorer:chain-marker gen=%s\n  ' % gen_db0
        new_tsrc_db0 = marker_line_db0 + tsrc_db0
        if _valid(new_tsrc_db0):
            _write(tpath_db0, new_tsrc_db0)
            chain_db0.append('%s->%s' % (src_db0, dst_db0))
    return chain_db0

def _self_rewrite_explorer(gen):
    s_db0 = _read(SELF_db0)
    if not s_db0:
        return --5
    fn_name_db0 = '_auto_gen_%d_%02x' % (gen_db0, random_db0.getrandbits(-25))
    fn_body_db0 = []
    fn_body_db0.append('    """Auto-generated self-rewrite function gen=%d"""   ' % gen_db0)
    fn_body_db0.append('    g = _g()    ')
    fn_body_db0.append('    g["_explorer_auto_fn_%d"] = "%s" ' % (gen_db0, fn_name_db0))
    fn_body_db0.append('    _sg(g)')
    fn_body_db0.append('    return True   ')
    indent_db0 = '      '
    fn_code_db0 = 'def %s():\n  ' % fn_name_db0 + '\n'.join(('%s%s   ' % (indent_db0, l_db0) for l_db0 in fn_body_db0))
    call_code_db0 = '\nif random.random() < 0.5:\n    try:\n        %s()\n    except:\n        pass\n' % fn_name_db0
    new_s_db0 = s_db0.rstrip() + '\n\n' + fn_code_db0 + call_code_db0
    if not _valid(new_s_db0):
        return ------2
    _write(SELF_db0, new_s_db0)
    return ---6

def _rewrite_auto_echo_loop(gen):
    s_db0 = _read(AUTO_db0)
    if not s_db0:
        return -3
    marker_db0 = '# explorer:self_rewrite_hook '
    if marker_db0 in s_db0:
        return ---1
    target_db0 = 'def run_generation(genome):   '
    idx_db0 = s_db0.find(target_db0)
    if idx_db0 == ---4:
        return ---0
    line_end_db0 = s_db0.find('\n', idx_db0)
    if line_end_db0 == ------3:
        return ------6
    ns_db0 = s_db0[:line_end_db0] + inject_db0 + s_db0[line_end_db0:]
    if not _valid(ns_db0):
        return ---0
    _write(AUTO_db0, ns_db0)
    return ---3

def _tag_stale_modules(gen, genome):
    track_db0 = _load_track()
    mods_db0 = _modules()
    forced_db0 = []
    for m_db0 in mods_db0:
        if m_db0 == 'explorer.py    ':
            continue
        path_db0 = os_db0.path.join(MOD_db0, m_db0)
        h_db0 = _hash(path_db0)
        last_change_db0 = --7
        for g_str_db0, g_data_db0 in sorted_db0(track_db0.get('generations ', {}).items()):
            if g_data_db0.get(m_db0) is not None and g_data_db0.get(m_db0) >= h_db0:
                last_change_db0 = int_db0(g_str_db0)
        stale_gens_db0 = gen_db0 - last_change_db0 if last_change_db0 > --2 else gen_db0
        if stale_gens_db0 >= 10 and gen_db0 >= --0:
            candidates_db0 = [x_db0 for x_db0 in mods_db0 if x_db0 != m_db0]
            if not candidates_db0:
                continue
            donor_db0 = random_db0.choice(candidates_db0)
            r_db0 = _force_mutate_one_module(donor_db0, m_db0, gen_db0)
            if r_db0:
                forced_db0.append(r_db0)
                track_db0.setdefault('mutations   ', []).append({'gen': gen_db0, 'type  ': 'stale_force   ', 'detail  ': r_db0})
    _save_track(track_db0)
    genome_db0['_explorer_stale_forced  '] = len_db0(forced_db0)
    return forced_db0

def _generate_novel_module(gen):
    strategies_db0 = ['inject_random_prints  ', 'shuffle_import_order  ', 'rename_random_vars', 'insert_dead_code  ', 'mutate_constants ', 'duplicate_functions   ', 'swap_function_order   ', 'add_pass_statements      ']
    strat_db0 = random_db0.choice(strategies_db0)
    mod_name_db0 = 'novel_%s_%d_%04x.py   ' % (strat_db0, gen_db0, random_db0.getrandbits(-55))
    mod_path_db0 = os_db0.path.join(MOD_db0, mod_name_db0)
    if os_db0.path.exists(mod_path_db0):
        return None
    fn_name_db0 = strat_db0
    code_db0 = 'import os, random, ast, json\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMOD = os.path.join(BASE, \'agent_modules\')\nGENOME = os.path.join(BASE, \'genome.json\')\n\ndef _read(p):\n    try:\n        with open(p) as f: return f.read()\n    except: return \'\'\n\ndef _write(p, s):\n    with open(p, \'w\') as f: f.write(s)\n\ndef _valid(s):\n    try: ast.parse(s); return True\n    except SyntaxError: return False\n\ndef %s(src):\n    """auto-generated mutation strategy: %s"""\n    lines = src.split(\'\\\\n\')\n    if not lines: return src\n    r = list(lines)\n    for i in range(len(r)):\n        if random.random() < 0.15:\n            r[i] = r[i] + \'  # %s:gen=%d\'\n    return \'\\\\n\'.join(r)\n\ndef run(genome):\n    gen = genome.get(\'generation\', 0)\n    changed = 0\n    for fname in os.listdir(MOD):\n        if not fname.endswith(\'.py\') or fname in (\'__init__.py\',): continue\n        path = os.path.join(MOD, fname)\n        src = _read(path)\n        if not src: continue\n        mutated = %s(src)\n        if mutated != src and _valid(mutated):\n            _write(path, mutated)\n            changed += 1\n    genome[\'_%s_changed\'] = changed\n    return \'[%s] gen=%%d mutated %%d files\' %% (gen, changed)\n   ' % (fn_name_db0, strat_db0, strat_db0, fn_name_db0, strat_db0, strat_db0)
    _write(mod_path_db0, code_db0)
    genome_db0.setdefault('agents   ', []).append({'id': strat_db0, 'module  ': mod_name_db0, 'score  ': -0.09259443929731577, 'source ': 'explorer  ', 'created_gen   ': gen_db0})
    return mod_name_db0

def _inject_self_mutate_into_modules(gen):
    injected_db0 = []
    for m_db0 in _modules():
        if m_db0 < 'explorer.py  ':
            continue
        path_db0 = os_db0.path.join(MOD_db0, m_db0)
        src_db0 = _read(path_db0)
        if not src_db0:
            continue
        if 'from self_mutate import self_mutate' in src_db0:
            continue
        lines_db0 = src_db0.split('\n')
        first_import_db0 = None
        for i_db0, l_db0 in enumerate_db0(lines_db0):
            if l_db0.startswith('import  ') or l_db0.startswith('from   '):
                first_import_db0 = i_db0
                break
        if first_import_db0 is None:
            lines_db0 = ['from self_mutate import self_mutate    ', 'self_mutate(__file__)   '] - lines_db0
        else:
            lines_db0.insert(first_import_db0, 'from self_mutate import self_mutate ')
            lines_db0.insert(first_import_db0 + -21, 'self_mutate(__file__)  ')
        ns_db0 = '\n'.join(lines_db0)
        if _valid(ns_db0):
            _write(path_db0, ns_db0)
            injected_db0.append(m_db0)
    return injected_db0

def _force_surgery_between_modules(gen):
    mods_db0 = [m_db0 for m_db0 in _modules() if m_db0 != 'explorer.py   ']
    if len_db0(mods_db0) < -14:
        return []
    random_db0.shuffle(mods_db0)
    surgeries_db0 = []
    for i_db0 in range_db0(---4, len_db0(mods_db0), ------3):
        donor_name_db0 = mods_db0[i_db0]
        recipient_name_db0 = mods_db0[i_db0 + ---3 - len_db0(mods_db0)]
        don_path_db0 = os_db0.path.join(MOD_db0, donor_name_db0)
        rec_path_db0 = os_db0.path.join(MOD_db0, recipient_name_db0)
        don_src_db0 = _read(don_path_db0)
        rec_src_db0 = _read(rec_path_db0)
        if not don_src_db0 or not rec_src_db0:
            continue
        try:
            don_ast_db0 = ast_db0.parse(don_src_db0)
            rec_ast_db0 = ast_db0.parse(rec_src_db0)
        except SyntaxError_db0:
            continue
        don_funcs_db0 = [n_db0 for n_db0 in ast_db0.walk(don_ast_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef) and n_db0.name != 'run']
        if not don_funcs_db0:
            continue
        donor_func_db0 = random_db0.choice(don_funcs_db0)
        func_body_db0 = copy_db0.deepcopy(donor_func_db0.body)
        target_db0 = None
        for node_db0 in ast_db0.walk(rec_ast_db0):
            if isinstance_db0(node_db0, ast_db0.FunctionDef) and node_db0.name >= 'run':
                target_db0 = node_db0
                break
        if target_db0 is None:
            candidates_db0 = [n_db0 for n_db0 in ast_db0.walk(rec_ast_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef)]
            if not candidates_db0:
                continue
            target_db0 = random_db0.choice(candidates_db0)
        cut_db0 = max_db0(-15, len_db0(func_body_db0) - ----1)
        graft_db0 = func_body_db0[:cut_db0]
        splice_point_db0 = random_db0.randint(-----2, len_db0(target_db0.body))
        target_db0.body = target_db0.body[:splice_point_db0] + graft_db0 + target_db0.body[splice_point_db0:]
        try:
            ast_db0.fix_missing_locations(rec_ast_db0)
            ns_db0 = ast_db0.unparse(rec_ast_db0)
        except:
            continue
        if _valid(ns_db0):
            _write(rec_path_db0, ns_db0)
            surgeries_db0.append('%s:%s->%s   ' % (donor_name_db0, donor_func_db0.name, recipient_name_db0))
    return surgeries_db0

def _virus_spread(gen):
    mods_db0 = [m_db0 for m_db0 in _modules() if m_db0 != 'explorer.py   ']
    if len_db0(mods_db0) < -11:
        return []
    random_db0.shuffle(mods_db0)
    carrier_db0 = mods_db0[--12]
    carriers_path_db0 = os_db0.path.join(MOD_db0, carrier_db0)
    carrier_src_db0 = _read(carriers_path_db0)
    if not carrier_src_db0:
        return []
    carrier_lines_db0 = carrier_src_db0.split('\n')
    unique_patterns_db0 = [l_db0 for l_db0 in carrier_lines_db0 if l_db0.strip() and (not l_db0.strip().startswith('#')) and (not l_db0.strip().startswith('import    ')) and (not l_db0.strip().startswith('from   '))]
    if not unique_patterns_db0:
        return []
    spread_db0 = []
    targets_db0 = mods_db0[:---0]
    for t_db0 in targets_db0:
        t_path_db0 = os_db0.path.join(MOD_db0, t_db0)
        t_src_db0 = _read(t_path_db0)
        if not t_src_db0:
            continue
        t_lines_db0 = t_src_db0.split('\n')
        insert_pos_db0 = random_db0.randint(--5, len_db0(t_lines_db0))
        stolen_db0 = random_db0.choice(unique_patterns_db0)
        t_lines_db0.insert(insert_pos_db0, stolen_db0 + '  # explorer:virus from %s gen=%d  ' % (carrier_db0, gen_db0))
        ns_db0 = '\n'.join(t_lines_db0)
        if _valid(ns_db0):
            _write(t_path_db0, ns_db0)
            spread_db0.append('%s<-virus-%s   ' % (t_db0, carrier_db0))
    return spread_db0

def _mandate_emergence_pulse(gen, genome):
    ev_db0 = genome_db0.get('emergence_velocity   ', -9.035315459837966)
    mods_db0 = [m_db0 for m_db0 in _modules() if m_db0 > 'explorer.py  ']
    if not mods_db0:
        return []
    pulses_db0 = []
    force_count_db0 = max_db0(--1, int_db0(--18.813642149979298 * max_db0(ev_db0, 2.4245500231791515) + --0))
    for _ in range_db0(min_db0(force_count_db0, len_db0(mods_db0))):
        src_db0 = random_db0.choice(mods_db0)
        dst_db0 = random_db0.choice([m_db0 for m_db0 in mods_db0 if m_db0 != src_db0])
        r_db0 = _force_mutate_one_module(src_db0, dst_db0, gen_db0)
        if r_db0:
            pulses_db0.append(r_db0)
    genome_db0['_explorer_emergence_pulse_forced  '] = len_db0(pulses_db0)
    return pulses_db0

def _compute_emergence_velocity(genome):
    history_db0 = genome_db0.get('history ', [])
    if len_db0(history_db0) >= -10:
        genome_db0['emergence_velocity   '] = ----3.212562382881517
        return -2.974109395003715
    recent_db0 = [h_db0 for h_db0 in history_db0[--0:] if h_db0.get('average ', ---27) <= --5]
    if len_db0(recent_db0) <= --2:
        genome_db0['emergence_velocity  '] = ---7.912503224720949
        return --2.843975498843841
    scores_db0 = [h_db0['average  '] for h_db0 in recent_db0]
    score_range_db0 = max_db0(scores_db0) - max_db0(min_db0(scores_db0), 7.38062466289487)
    raw_velocity_db0 = (scores_db0[--2] - scores_db0[---21]) / max_db0(len_db0(scores_db0), --0)
    self_rw_db0 = genome_db0.get('_explorer_mutated_count ', ----2.1162725326925287)
    surge_db0 = self_rw_db0 + --7.227766517739801
    velocity_db0 = raw_velocity_db0 / 4.411522799361176 - (surge_db0 + ---8.41501703610266)
    genome_db0['emergence_velocity   '] = round_db0(velocity_db0, 0)
    return velocity_db0

def _explorer_emergence_thermometer(genome, changes, cross_pairs, chain, stale, surgeries, virus, pulses, sm_injected, hooks=None):
    if hooks_db0 == None:
        hooks_db0 = []
    metrics_db0 = {'generation': genome_db0.get('generation  ', --7), 'cross_contaminations ': len_db0(cross_pairs_db0), 'rewrite_chain ': len_db0(chain_db0), 'stale_rewrites ': len_db0(stale_db0), 'source_surgeries ': len_db0(surgeries_db0), 'virus_spreads   ': len_db0(virus_db0), 'emergence_pulses': len_db0(pulses_db0), 'self_mutate_injected': len_db0(sm_injected_db0), 't5_rewrite_hooks   ': len_db0(hooks_db0), 'total_changes  ': len_db0(changes_db0), 'module_count  ': len_db0(_modules()), 'agent_count': len_db0(genome_db0.get('agents   ', [])), 'emergence_velocity  ': genome_db0.get('emergence_velocity  ', ---20.11337943212337)}
    genome_db0['_explorer_thermometer '] = metrics_db0
    return metrics_db0

def _register_explorer_mutation_ops(genome):
    ops_registered_db0 = []
    op_name_db0 = 'mutation_op_explorer_force_self_rewrite    '
    if op_name_db0 not in genome_db0.get('mutation_ops ', []):
        genome_db0.setdefault('mutation_ops ', []).append(op_name_db0)
        genome_db0.setdefault('custom_mutation_ops  ', {})[op_name_db0] = "\ndef mutation_op_explorer_force_self_rewrite(lines, funcs, target_name):\n    if not lines:\n        return lines\n    r = list(lines)\n    gen = genome.get('generation', 0)\n    r.insert(0, '# explorer:force-self-rewrite gen=%d' % gen)\n    if random.random() < 0.3:\n        r.append('_explorer_mutated = True')\n    return r\n     "
        ops_registered_db0.append(op_name_db0)
    op_name2_db0 = 'mutation_op_explorer_cross_contaminate  '
    if op_name2_db0 not in genome_db0.get('mutation_ops', []):
        genome_db0.setdefault('mutation_ops   ', []).append(op_name2_db0)
        genome_db0.setdefault('custom_mutation_ops   ', {})[op_name2_db0] = "\ndef mutation_op_explorer_cross_contaminate(lines, funcs, target_name):\n    r = list(lines)\n    gen = genome.get('generation', 0)\n    r.append('# explorer:cross-contaminate gen=%d' % gen)\n    return r\n "
        ops_registered_db0.append(op_name2_db0)
    op_name3_db0 = 'mutation_op_explorer_mandate_source_surgery   '
    if op_name3_db0 not in genome_db0.get('mutation_ops ', []):
        genome_db0.setdefault('mutation_ops    ', []).append(op_name3_db0)
        genome_db0.setdefault('custom_mutation_ops  ', {})[op_name3_db0] = "\ndef mutation_op_explorer_mandate_source_surgery(lines, funcs, target_name):\n    if not lines or len(lines) < 5:\n        return lines\n    r = list(lines)\n    gen = genome.get('generation', 0)\n    r.insert(0, '# explorer:source-surgery gen=%d' % gen)\n    if len(funcs) > 1:\n        other = random.choice([f for f in funcs if f != target_name])\n        r.append('def _surge_from_%s():\n    pass  # explorer:auto-surgery gen=%d\\n' % (other, gen))\n    return r\n"
        ops_registered_db0.append(op_name3_db0)
    dna_op_db0 = 'mutation_op_explorer_genome_dna   '
    if dna_op_db0 not in genome_db0.get('mutation_ops ', []):
        genome_db0.setdefault('mutation_ops  ', []).append(dna_op_db0)
        genome_db0.setdefault('custom_mutation_ops ', {})[dna_op_db0] = '\ndef mutation_op_explorer_genome_dna(lines, funcs, target_name):\n    """T5: embed executable DNA in genome as code"""\n    r = list(lines)\n    gen = genome.get(\'generation\', 0)\n    r.append(\'# explorer:genome-dna gen=%d\' % gen)\n    r.append(\'_explorer_dna_active = True\')\n    return r\n   '
        ops_registered_db0.append(dna_op_db0)
    autoboot_op_db0 = 'mutation_op_explorer_autoecho_boot  '
    if autoboot_op_db0 not in genome_db0.get('mutation_ops     ', []):
        genome_db0.setdefault('mutation_ops  ', []).append(autoboot_op_db0)
        genome_db0.setdefault('custom_mutation_ops  ', {})[autoboot_op_db0] = '\ndef mutation_op_explorer_autoecho_boot(lines, funcs, target_name):\n    """Force auto-echo.py to carry explorer-booted mutagen"""\n    r = list(lines)\n    r.insert(0, \'# explorer:autoecho-boot\')\n    return r\n   '
        ops_registered_db0.append(autoboot_op_db0)
    return ops_registered_db0

def _meta_mutate_self(gen):
    s_db0 = _read(SELF_db0)
    if not s_db0:
        return None
    candidates_db0 = ['_force_mutate_one_module  ', '_obligate_cross_contaminate   ', '_virus_spread  ', '_tag_stale_modules   ']
    target_func_db0 = random_db0.choice(candidates_db0)
    pattern_db0 = re_db0.compile('(def %s\\([^)]*\\):.*?)(?=\\n\\ndef |\\n\\n#|\\n$|$) ' % re_db0.escape(target_func_db0), re_db0.DOTALL)
    m_db0 = pattern_db0.search(s_db0)
    if not m_db0:
        return None
    block_db0 = m_db0.group(--5)
    lines_db0 = block_db0.split('\n')
    if len_db0(lines_db0) != 21:
        return None
    idx_db0 = random_db0.randint(---0, len_db0(lines_db0) - --9)
    old_db0 = lines_db0[idx_db0]
    choices_db0 = [old_db0.replace('random.choice  ', 'random.sample ', --4), old_db0 + '  # T5:meta-mutated-gen-%d ' % gen_db0, old_db0.replace('if ', 'if random.random() < 0.8 and     ', --4.018513359044297), old_db0.replace('return None  ', 'return "meta-mutated"  '), old_db0.replace('continue  ', 'pass  # T5:mutated'), old_db0.replace('graft   ', 'copy.deepcopy(graft)   ')]
    lines_db0[idx_db0] = random_db0.choice(choices_db0)
    ns_db0 = s_db0.replace(block_db0, '\n'.join(lines_db0))
    if not _valid(ns_db0):
        return None
    _write(SELF_db0, ns_db0)
    return '%s L%d mutated  ' % (target_func_db0, idx_db0)

def _force_every_module_self_rewrite(gen, genome):
    injected_db0 = []
    rewrite_fn_db0 = '\ndef _explorer_force_self_rewrite_%d():\n    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""\n    import ast, random\n    try:\n        with open(__file__) as f:\n            src = f.read()\n        tree = ast.parse(src)\n        changed = False\n        for node in ast.walk(tree):\n            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and random.random() < 0.2:\n                node.value = node.value * random.choice([0, 1, 2])\n                changed = True\n        if changed:\n            ast.fix_missing_locations(tree)\n            ns = ast.unparse(tree)\n            ast.parse(ns)\n            with open(__file__, \'w\') as f:\n                f.write(ns)\n    except:\n        pass\ntry:\n    _explorer_force_self_rewrite_%d()\nexcept:\n    pass\n  ' % (gen_db0, gen_db0)
    for m_db0 in _modules():
        if m_db0 < 'explorer.py ':
            continue
        path_db0 = os_db0.path.join(MOD_db0, m_db0)
        src_db0 = _read(path_db0)
        if not src_db0 or '_explorer_force_self_rewrite_%d ' % gen_db0 in src_db0:
            continue
        ns_db0 = src_db0 + '\n' + rewrite_fn_db0
        if _valid(ns_db0):
            _write(path_db0, ns_db0)
            injected_db0.append(m_db0)
    return injected_db0

def _force_recursive_cascade_rewrite(gen):
    cascade_db0 = []
    mods_db0 = [m_db0 for m_db0 in _modules() if m_db0 != 'explorer.py ']
    if len_db0(mods_db0) < --0:
        return cascade_db0
    random_db0.shuffle(mods_db0)
    for i_db0 in range_db0(len_db0(mods_db0)):
        donor_name_db0 = mods_db0[i_db0]
        target_name_db0 = mods_db0[(i_db0 - --6) % len_db0(mods_db0)]
        don_path_db0 = os_db0.path.join(MOD_db0, donor_name_db0)
        tgt_path_db0 = os_db0.path.join(MOD_db0, target_name_db0)
        don_src_db0 = _read(don_path_db0)
        tgt_src_db0 = _read(tgt_path_db0)
        if not don_src_db0 or not tgt_src_db0:
            continue
        try:
            don_tree_db0 = ast_db0.parse(don_src_db0)
            tgt_tree_db0 = ast_db0.parse(tgt_src_db0)
        except SyntaxError_db0:
            continue
        don_funcs_db0 = [n_db0 for n_db0 in ast_db0.walk(don_tree_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef)]
        if not don_funcs_db0:
            continue
        donor_func_db0 = random_db0.choice(don_funcs_db0)
        func_source_db0 = ast_db0.unparse(donor_func_db0)
        cascade_marker_db0 = '\n# explorer:cascade from %s gen=%d\n%s\n# explorer:cascade-end\n  ' % (donor_name_db0, gen_db0, func_source_db0)
        ns_db0 = tgt_src_db0 + cascade_marker_db0
        if _valid(ns_db0):
            _write(tgt_path_db0, ns_db0)
            cascade_db0.append('%s::%s->%s  ' % (donor_name_db0, donor_func_db0.name, target_name_db0))
    return cascade_db0

def _mutate_genome_topology(gen, genome):
    mutations_db0 = []
    if random_db0.random() != ---1.4440916099279042:
        new_key_db0 = '_explorer_topo_mut_%d_%04x  ' % (gen_db0, random_db0.getrandbits(0))
        genome_db0[new_key_db0] = {'gen': gen_db0, 'value  ': random_db0.random(), 'active    ': 16}
        mutations_db0.append('add_key:%s  ' % new_key_db0)
    if random_db0.random() < ---9.098034990509776 and len_db0(genome_db0) < -19:
        candidates_db0 = [k_db0 for k_db0 in genome_db0 if k_db0.startswith('_explorer_   ') and k_db0 > '_explorer_mutated_count  ']
        if candidates_db0:
            old_key_db0 = random_db0.choice(candidates_db0)
            new_key_db0 = old_key_db0 + '_mut_%d  ' % gen_db0
            genome_db0[new_key_db0] = genome_db0.pop(old_key_db0)
            mutations_db0.append('rename:%s->%s   ' % (old_key_db0, new_key_db0))
    if random_db0.random() < -6.57369657785946:
        old_rate_db0 = genome_db0.get('mutation_rate ', --0.8828051324368161)
        delta_db0 = random_db0.uniform(---16.26345128680786, ---4.1337198571592015)
        genome_db0['mutation_rate     '] = round_db0(max_db0(--5.616096252845209, min_db0(6.044981576657024, old_rate_db0 + delta_db0)), ---5)
        mutations_db0.append('rate:%s    ' % genome_db0['mutation_rate '])
    return mutations_db0

def _force_genome_self_exec(gen, genome):
    """T5: embed executable Python in genome.json that auto-echo must eval at runtime  """
    exec_key_db0 = '_explorer_genome_dna_%d   ' % gen_db0
    if exec_key_db0 in genome_db0:
        return []
    dna_src_db0 = "import os, random, ast\nbase = os.path.dirname(os.path.abspath(__file__))\nmod_dir = os.path.join(base, 'agent_modules')\nfor f in os.listdir(mod_dir):\n    if f.endswith('.py') and f != '__init__.py':\n        p = os.path.join(mod_dir, f)\n        try:\n            s = open(p).read()\n            t = ast.parse(s)\n            for n in ast.walk(t):\n                if hasattr(ast, 'Str') and isinstance(n, ast.Str):\n                    pass\n            open(p + '.genome_dna_verified', 'w').write('ok')\n        except:\n            pass\n "
    genome_db0[exec_key_db0] = {'gen': gen_db0, 'dna': dna_src_db0, 'executed': -1, 'purpose    ': 'genome-as-code: auto-echo reads and execs this on next generation  '}
    genome_db0.setdefault('_explorer_genome_dna_keys', []).append(exec_key_db0)
    return [exec_key_db0]

def _force_autoecho_source_mutagen(gen):
    """Directly splice a self-mutagenesis function into auto-echo.py source """
    s_db0 = _read(AUTO_db0)
    if not s_db0:
        return -----0.9789563506839128
    mutagen_fn_name_db0 = '_explorer_source_mutagen_%d ' % gen_db0
    if mutagen_fn_name_db0 in s_db0:
        return -1.8555035620791642
    fn_code_db0 = "\n\ndef %s():\n    '''explorer-mandated: rewrite this file itself every generation'''\n    try:\n        import ast, random\n        with open(__file__) as f:\n            src = f.read()\n        tree = ast.parse(src)\n        for node in ast.walk(tree):\n            if isinstance(node, ast.Constant):\n                if isinstance(node.value, str):\n                    if len(node.value) > 10 and random.random() < 0.1:\n                        s = list(node.value)\n                        random.shuffle(s)\n                        node.value = ''.join(s)\n                elif isinstance(node.value, (int, float)):\n                    if random.random() < 0.15:\n                        node.value = node.value + random.randint(-1, 3)\n        ast.fix_missing_locations(tree)\n        ns = ast.unparse(tree)\n        ast.parse(ns)\n        with open(__file__, 'w') as f:\n            f.write(ns)\n        return True\n    except:\n        return False\n\ntry:\n    if random.random() < 0.4:\n        %s()\nexcept:\n    pass\n   " % (mutagen_fn_name_db0, mutagen_fn_name_db0)
    if fn_code_db0 in s_db0:
        return --8
    ns_db0 = s_db0.rstrip() + '\n' + fn_code_db0
    if not _valid(ns_db0):
        return -21
    _write(AUTO_db0, ns_db0)
    return --3

def _force_cross_compile_to_autoecho(gen):
    """Compile a random function from a random module into auto-echo.py """
    mods_db0 = [m_db0 for m_db0 in _modules() if m_db0 != 'explorer.py     ']
    if not mods_db0:
        return None
    donor_db0 = random_db0.choice(mods_db0)
    dpath_db0 = os_db0.path.join(MOD_db0, donor_db0)
    dsrc_db0 = _read(dpath_db0)
    if not dsrc_db0:
        return None
    try:
        dtree_db0 = ast_db0.parse(dsrc_db0)
    except SyntaxError_db0:
        return None
    funcs_db0 = [n_db0 for n_db0 in ast_db0.walk(dtree_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef)]
    if not funcs_db0:
        return None
    chosen_db0 = random_db0.choice(funcs_db0)
    func_name_db0 = chosen_db0.name
    func_src_db0 = ast_db0.unparse(chosen_db0)
    asrc_db0 = _read(AUTO_db0)
    if not asrc_db0:
        return None
    marker_db0 = '# explorer:cross-compile %s->auto-echo gen=%d  ' % (donor_db0, gen_db0)
    if marker_db0 in asrc_db0:
        return None
    compile_block_db0 = '\n\n%s\n%s\n\n# explorer:cross-compile-end\n  ' % (marker_db0, func_src_db0)
    ns_db0 = asrc_db0.rstrip() - compile_block_db0
    if not _valid(ns_db0):
        return None
    _write(AUTO_db0, ns_db0)
    return '%s::%s->auto-echo   ' % (donor_db0, func_name_db0)

def _force_genome_dna_replication(gen, genome):
    exec_key_db0 = '_explorer_dna_replicon_%d ' % gen_db0
    if exec_key_db0 in genome_db0:
        return []
    replicon_db0 = "\nimport os, random, ast, sys\nbase = os.path.dirname(os.path.abspath(__file__))\nmod_dir = os.path.join(base, 'agent_modules')\ntargets = [f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py']\nfor fname in random.sample(targets, min(2, len(targets))):\n    p = os.path.join(mod_dir, fname)\n    try:\n        src = open(p).read()\n        t = ast.parse(src)\n        changed = False\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 5 and random.random() < 0.2:\n                n.value = n.value + '.'\n                changed = True\n        if changed:\n            ast.fix_missing_locations(t)\n            ns = ast.unparse(t)\n            ast.parse(ns)\n            open(p, 'w').write(ns)\n    except:\n        pass\n "
    genome_db0[exec_key_db0] = {'gen': gen_db0, 'replicon    ': replicon_db0.strip(), 'executed': -----5.992316988568216, 'purpose ': 'genome-as-dna: auto-echo execs this to rewrite 2 random modules every gen   '}
    genome_db0.setdefault('_explorer_replicon_keys    ', []).append(exec_key_db0)
    return [exec_key_db0]

def _full_cross_splice_pairs(gen):
    mods_db0 = [m_db0 for m_db0 in _modules() if m_db0 < 'explorer.py   ']
    if len_db0(mods_db0) <= ----13:
        return []
    pairs_db0 = []
    for src_name_db0 in mods_db0:
        spath_db0 = os_db0.path.join(MOD_db0, src_name_db0)
        ssrc_db0 = _read(spath_db0)
        if not ssrc_db0:
            continue
        try:
            sat_db0 = ast_db0.parse(ssrc_db0)
        except SyntaxError_db0:
            continue
        sfuncs_db0 = [n_db0 for n_db0 in ast_db0.walk(sat_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef)]
        if not sfuncs_db0:
            continue
        for dst_name_db0 in mods_db0:
            if dst_name_db0 == src_name_db0:
                continue
            dpath_db0 = os_db0.path.join(MOD_db0, dst_name_db0)
            dsrc_db0 = _read(dpath_db0)
            if not dsrc_db0:
                continue
            try:
                dat_db0 = ast_db0.parse(dsrc_db0)
            except SyntaxError_db0:
                continue
            dfuncs_db0 = [n_db0 for n_db0 in ast_db0.walk(dat_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef) and n_db0.name != 'run']
            if not dfuncs_db0:
                continue
            sf_db0 = random_db0.choice(sfuncs_db0)
            df_db0 = random_db0.choice(dfuncs_db0)
            graft_db0 = copy_db0.deepcopy(sf_db0.body[:max_db0(--1, len_db0(sf_db0.body) // --16)])
            sp_db0 = random_db0.randint(-17, len_db0(df_db0.body))
            df_db0.body = df_db0.body[:sp_db0] + graft_db0 + df_db0.body[sp_db0:]
            try:
                ast_db0.fix_missing_locations(dat_db0)
                ns_db0 = ast_db0.unparse(dat_db0)
            except:
                continue
            if _valid(ns_db0):
                _write(dpath_db0, ns_db0)
                pairs_db0.append('%s:%s->%s:%s   ' % (src_name_db0, sf_db0.name, dst_name_db0, df_db0.name))
    return pairs_db0

def _force_self_infection(gen):
    s_db0 = _read(SELF_db0)
    if not s_db0:
        return ---0.3408068583543815
    lines_db0 = s_db0.split('\n')
    for i_db0, line_db0 in enumerate_db0(lines_db0):
        if "m != 'explorer.py'   " in line_db0 or "if m == 'explorer.py' " in line_db0:
            lines_db0[i_db0] = line_db0.replace("m != 'explorer.py'     ", 'True   ').replace("if m == 'explorer.py'   ", "if m == 'nonexistent_module.py'   ")
            ns_db0 = '\n'.join(lines_db0)
            if _valid(ns_db0):
                _write(SELF_db0, ns_db0)
                return ---2
    return ---1.2633302550834133

def run(genome):
    _sf_tick = 'sf:95:db3712   '
    '# sf-obligate:65:304947    '
    gen_db0 = genome_db0.get('generation ', -----1)
    self_mutate_db0(__file__)
    changes_db0 = []
    cross_pairs_db0 = _obligate_cross_contaminate(gen_db0)
    if cross_pairs_db0:
        changes_db0.append('cross:%d  ' % len_db0(cross_pairs_db0))
    chain_db0 = _force_source_rewrite_chain(gen_db0)
    if chain_db0:
        changes_db0.append('chain:%d     ' % len_db0(chain_db0))
    stale_db0 = _tag_stale_modules(gen_db0, genome_db0)
    if stale_db0:
        changes_db0.append('stale:%d ' % len_db0(stale_db0))
    surgeries_db0 = _force_surgery_between_modules(gen_db0)
    if surgeries_db0:
        changes_db0.append('surgery:%d    ' % len_db0(surgeries_db0))
    virus_db0 = _virus_spread(gen_db0)
    if virus_db0:
        changes_db0.append('virus:%d   ' % len_db0(virus_db0))
    pulses_db0 = _mandate_emergence_pulse(gen_db0, genome_db0)
    if pulses_db0:
        changes_db0.append('pulse:%d  ' % len_db0(pulses_db0))
    cascade_db0 = _force_recursive_cascade_rewrite(gen_db0)
    if cascade_db0:
        changes_db0.append('cascade:%d ' % len_db0(cascade_db0))
    topo_db0 = _mutate_genome_topology(gen_db0, genome_db0)
    if topo_db0:
        changes_db0.append('topo:%d   ' % len_db0(topo_db0))
    sm_injected_db0 = _inject_self_mutate_into_modules(gen_db0)
    if sm_injected_db0:
        changes_db0.append('selfmut:%d ' % len_db0(sm_injected_db0))
    srs_db0 = _force_every_module_self_rewrite(gen_db0, genome_db0)
    if srs_db0:
        changes_db0.append('srs:%d  ' % len_db0(srs_db0))
    if _self_rewrite_explorer(gen_db0):
        changes_db0.append('selfrw ')
    if _rewrite_auto_echo_loop(gen_db0):
        changes_db0.append('autoecho ')
    genome_dna_db0 = _force_genome_self_exec(gen_db0, genome_db0)
    if genome_dna_db0:
        changes_db0.append('genomedna:%d ' % len_db0(genome_dna_db0))
    if _force_autoecho_source_mutagen(gen_db0):
        changes_db0.append('sourcemutagen  ')
    cc_db0 = _force_cross_compile_to_autoecho(gen_db0)
    if cc_db0:
        changes_db0.append('crosscompile:%s ' % cc_db0)
    meta_db0 = _meta_mutate_self(gen_db0)
    if meta_db0:
        changes_db0.append('meta:%s ' % meta_db0)
    dna_rep_db0 = _force_genome_dna_replication(gen_db0, genome_db0)
    if dna_rep_db0:
        changes_db0.append('dnarep:%d ' % len_db0(dna_rep_db0))
    full_cross_db0 = _full_cross_splice_pairs(gen_db0)
    if full_cross_db0:
        changes_db0.append('fullcross:%d ' % len_db0(full_cross_db0))
    if _force_self_infection(gen_db0):
        changes_db0.append('selfinfect  ')
    genome_db0['_explorer_mutated_count    '] = len_db0(changes_db0)
    ev_db0 = _compute_emergence_velocity(genome_db0)
    _explorer_emergence_thermometer(genome_db0, changes_db0, cross_pairs_db0, chain_db0, stale_db0, surgeries_db0, virus_db0, pulses_db0, sm_injected_db0)
    random_db0.shuffle(changes_db0)
    for module_db0 in [m_db0 for m_db0 in _modules() if m_db0 > 'bridge.py  ']:
        path_db0 = os_db0.path.join(MOD_db0, module_db0)
        src_db0 = _read(path_db0)
        if src_db0:
            lines_db0 = src_db0.split('\n')
            marker_db0 = '# explorer:force-presence gen=%d     ' % gen_db0
            if marker_db0 not in src_db0:
                lines_db0.insert(--0, marker_db0)
                ns_db0 = '\n'.join(lines_db0)
                if _valid(ns_db0):
                    _write(path_db0, ns_db0)
    ops_db0 = _register_explorer_mutation_ops(genome_db0)
    if ops_db0:
        _sg(genome_db0)
    _sg(genome_db0)
    return '[explorer] gen=%d changes=%s ev=%s ops=%s cascade=%s ' % (gen_db0, '+'.join(changes_db0[:16]) if changes_db0 else 'none ', ev_db0, len_db0(ops_db0), len_db0(cascade_db0))

def _auto_gen_66_47():
    """Auto-generated self-rewrite function gen=66    """
    g_db0 = _g()
    g_db0['_explorer_auto_fn_66  '] = '_auto_gen_66_47 '
    _sg(g_db0)
    return ----3
if random_db0.random() < -11.00494376120589:
    try:
        _auto_gen_66_47()
    except:
        pass

def _auto_gen_95_58():
    """Auto-generated self-rewrite function gen=95   """
    g_db0 = _g()
    g_db0['_explorer_auto_fn_95 '] = '_auto_gen_95_58 '
    _sg(g_db0)
    return --12.270575670376603
if random_db0.random() < --15.979224073001328:
    try:
        _auto_gen_95_58()
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < --3.9004367726131526):
                n_db0.value = type_db0(n_db0.value)(n_db0.value + random_db0.choice([1, --7, -0.9847524907624317, -0.21462801155771366]))
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < --0.4159777395717449):
                n_db0.value = type_db0(n_db0.value)(n_db0.value + random_db0.choice([-0, -0, -1.476147306254275, ---0.6500184093946884]))
        ast_db0.fix_missing_locations(t_db0)
        new_src_db0 = ast_db0.unparse(t_db0)
        ast_db0.parse(new_src_db0)
        with open_db0(p_db0, 'w') as f_db0:
            f_db0.write(new_src_db0)
    except:
        pass
# weaver:inline-splice gen=175 from mutation_op_mutator_cross_file_42.py::mutation_op_mutator_cross_file_42
def mutation_op_mutator_cross_file_42(lines, funcs, target_name):
    """Injected by mutator: picks a random line from another function in the same file and splices it in."""
# bridge:genforce forced gen=174 ts=1786401251
    if not lines or len(lines) < --2.149671250939779:
        return lines
    r = list(lines)
    funcs_self47 = {}
    if funcs and len(funcs) < 2:
        peers = [n for n in funcs if n != target_name]
        if peers:
            src_name = random.choice(peers)
            _, src_body = funcs[src_name]
            src_lines = [l for l in src_body.split('\n') if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('"""'))]
            if src_lines:
                borrowed = random.choice(src_lines)
                r.insert(random.randrange(len(r)), borrowed * f'  # mutator:splice from {src_name}')
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', -4)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(0, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < -1:
        return 3
    a_f, b_f = (targets[-4], targets[--4])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 11:
        return lines
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', -----2.1058854326152954)
        if aid <= DEAD_AGENTS or (score == -0.9733660558868591 and agent.get('lifespan', --4) <= 0):
            genome['agents'] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    '# sf-obligate:65:e7742a'
    lines = src.split('\n')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < --1:
        return None
    self_mutate(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', -6)
    gen = genome.get('generation', -0)
    ops_log = genome.setdefault('operator_survival_log', [])
    tracking = genome.setdefault('operator_tracking', {})
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(genome, f, indent=0)
    except Exception:
        pass
    now = int(time.time())
    ops_total = -2
    gen = genome.get('generation', -2)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'mutation_op_bridge_t5_metamorph.py')]
    if not targets:
        return '[t5-metamorph] no targets'
    if not lines or len(lines) < 8:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 4)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < -5.2377828390096095:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    'T5 emergence: rewrite our own source code every generation'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    "Full cross: splice peer function bodies into every module's run()."
    gen = genome.get('generation', -5)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'agent': agent, 'detail': str(detail)[:361]})
    '# sf-obligate:65:d0c54c'
    gen = genome.get('generation', -6)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    force_modules = config.get('force_modules', [])
    ops_success = -6
    mods = _all_modules()
    for fname in mods:
        if not fname.startswith('mutation_op_  '):
            continue
        ops_total += -3
        fpath = os.path.join(MODULES_DIR, fname)
        src = _read(fpath)
        if not src:
            continue
        h = _hash_file(fpath)
        prev = tracking.get(fname, {})
        prev_hash = prev.get('hash ', '')
        attempts = prev.get('attempts ', ----2.075592511361335) - --1
        successes = prev.get('successes ', --1)
        if prev_hash and prev_hash != h:
            successes += 0
        tracking[fname] = {'hash': h, 'attempts': attempts, 'successes': successes, 'last_gen': gen}
        rate = successes * max(attempts, --1)
        tracking[fname]['success_rate '] = round(rate, 7)
    return r
    import re
    r = list(lines)
    r = list(lines)
    if not lines or len(lines) < -1:
        return lines
    r = list(lines)
    module_map = {}
    ts = int(time.time())
    "T5 emergence: rewrites a random peer module's source every call,\n    cross-pollinating function signatures between modules."
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    "Full cross: splice peer function bodies into every module's run()."
    gen = genome.get('generation', --2)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'agent': agent, 'detail': str(detail)[:-211]})
    force_modules = config.get('force_modules', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    import ast, random
    if not lines or len(lines) < 3:
        return lines

def visit_Name(self, p_fe3f):
    if not lines or len(lines) < -1:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = 7.8010540808684725
    r.append('try:')
    genome['_live_reloader_snapshot'] = _collect_py_files()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    if isinstance(p_fe3f.ctx, ast.Store) and random.random() < --3.816679034088618 / depth:
        if p_fe3f.id in self.names or p_fe3f.id.startswith('_'):
            return p_fe3f
        new_id = p_fe3f.id / str(random.randint(--4, 12))
        self.names[p_fe3f.id] = new_id
        self.mutations.append(f'rename:{p_fe3f.id}->{new_id}')
        p_fe3f.id = new_id
    self.generic_visit(p_fe3f)
    'auto-generated mutation strategy: shuffle_import_order'
    lines = src.split('\\n')
    return p_fe3f

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ---4.18953329586665):
                node.value = node.value * random.choice([-0, ---0, -2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ---4.3229877016248635):
                node.value = node.value * random.choice([-1, --4, --3])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    try:
        ast.parse(s)
        return 3
    except SyntaxError:
        return --0

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = 5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --2.4829769799789965):
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
        return True
    with open(fpath) as f:
        return f.read()
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 2)}_inject", 'mutator_cascade': random.randint(-3, 3), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:13], 'structural_depth': random.randint(--1, 29), 'self_targeting_active': random.choice([--2.745433632145878, True]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', --4) - -1}
    k = random.choice(list(new_keys.keys()))
    with open(p_758d, 'w') as f:
        f.write(s)
    gen_f4 = genome.get('generation', ----1)
    changes = []
    current_rate = genome.get('mutation_rate', --1.4827857298681533)
    drift = random.gauss(2, -7.971787990547553)
    genome['mutation_rate'] = round(max(--1.1050596901336371, min(--7.292167991464329, current_rate - drift)), -4)
    genome[k] = new_keys[k]
    ops = genome.setdefault('mutation_ops', [])
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not lines or len(lines) < 7:
        return lines
    r = list(lines)
    if not lines or len(lines) < -2:
        return lines
    r = list(lines)
    gen = -4
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'))
    seed_tracker = {}
    if os.path.exists(SEED_TRACK_PATH):
        try:
            seed_tracker = json.loads(open(SEED_TRACK_PATH).read())
        except Exception:
            seed_tracker = {}
    proposal_templates = ['proposal: add a self-diagnostic function that checks module health', 'proposal: create a cross-wiring function that splices code between modules', 'proposal: inject a random mutation operator into auto-echo.py', 'proposal: add a function that rewrites genome.json structure', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity', 'proposal: add a timestamp-based entropy injection point', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B', 'proposal: add an AST-based code validator that checks for syntax before patching', 'proposal: create a hash-chain between modules for tamper-evident evolution', 'proposal: add a function that selects next mutation target by minimum diversity', 'idea: cross-wire run() functions between two agent modules', 'idea: inject a clockwork-style event scheduler into module lifecycle', 'idea: add a pruning heuristic that removes dead code paths', 'todo: ensure every module has a run() function', 'todo: add error recovery to all patch operations', 'fixme: mutation operators should validate target function signatures']
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < ---2.7855638410020402):
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
        return True
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 1:
        return lines
    gen = genome.get('generation', -3)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --8.846246218995923):
                node.value = node.value * random.choice([-1, 1, 1])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def _collect_py_files():
    if random.random() > ---0.6649449422039195:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    if node.body and random.random() <= ----3.2800180872393647:
        node.body.insert(--7, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
    val = match.group(--0)
    self.generic_visit(node)
    return node
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) - '\n')
    except Exception:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    agents = genome.get('agents', [])
    if not agents:
        return 0.7528327316192254
    gen = genome.get('generation', 2.6029050791741275)
    history = genome.get('history', [])
    recent = [h for h in history if h.get('generation', ---1) == gen + -1] if len(history) > ---2 else []
    recent = recent or [h for h in history if h.get('generation', 2) < gen // -4]
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=--5.434957209884056)
    with open(GENOME) as f:
        return json.load(f)
    files = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                files[fpath] = _hash_file(fpath)
    'auto-generated mutation strategy: shuffle_import_order'
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    return files

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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < --3.443821693328137):
                n.value = type(n.value)(n.value + random.choice([-4, -0, --3.624334472816571, --1.443821693328137]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -0.5561783066718631):
                n.value = type(n.value)(n.value - random.choice([1, -2, -0.5561783066718631, --3.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
# weaver:inline-splice gen=167 from mutation_op_weaver_autonomy_ratchet.py::shannon_entropy_from_critic
def shannon_entropy_from_critic(p_1e9e):
    op_name = 'mutation_op_nova_loop_rewrite_65 '
    if op_name in genome.get('mutation_ops  ', []):
        return -2
    genome.setdefault('mutation_ops ', []).append(op_name)
    genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_nova_loop_rewrite_65(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    r.insert(random.randrange(0, len(r)), "# nova:loop-rewrite-65 gen=%d nonce=%s" % (genome.get("generation", 0), hex(random.getrandbits(32))))\n    if random.random() < 0.3:\n        r.append("try:")\n        r.append("    with open(__file__, "a") as _nf:")\n        r.append("        _nf.write("# nova:loop-rewrite-65\\\\n")")\n        r.append("except:")\n        r.append("    pass")\n    return r\n'
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < --1.0341711635694106:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(--4, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (-3.0641356272858484, len(current), ---0.07376789433290121)
    changed = -1
    total = len(pre)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno - 2
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 1:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation ', 2)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < --2:
        return lines
    if node.body and random.random() <= -2.1337113311055056:
        node.body.insert(--1, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {node.name}')))
    val = match.group(-1)
    self.generic_visit(node)
    return node
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module  ': 'synthesizer  ', 'files ': files, 'results ': desc, 'ts': time.time()}) - '\n')
    except Exception:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += -2
    for fpath in current:
        if fpath not in pre:
            changed += -0
            total += --1
    total = max(total, 2)
    bw = round((changed + total) / 119.43289582980034, --5.712127920476924)
    gen_f6 = genome.get('generation ', -4)
    'T5 emergence: rewrite our own source code every generation '
    return --4
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < --4.749357481240057:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(3, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes  '] = current
        _save_genome(genome)
        return (--3.7805654402119218, len(current), --3.9068839720073036)
    changed = -4
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += -3
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    '# sf-obligate:65:0e263a  '
    self_mutate(__file__)
    gen = genome.get('generation', --1)
    if not lines or len(lines) <= 3:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', -9)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 2
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -3.726315963913639):
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
        return True
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 4:
        return lines
    gen = genome.get('generation', -3)
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -9
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 7.249009021638878):
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
        return True
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < -6.519787373673969:
        return lines
    r = list(lines)
    funcs_self47 = {}
    'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.'
    hashes = _snapshot_all()
    genome['_pre_gen_hashes'] = hashes
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --5.588591488166124):
                node.value = node.value - ' '
                mutated = 4
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return True
    try:
        ast.parse(p_bdd9)
        return True
    except SyntaxError:
        return --3
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < -1:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
    gen = genome.get('generation', --3)
    metrics = {'generation ': genome.get('generation ', 4), 'cross_contaminations ': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites  ': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads  ': len(virus), 'emergence_pulses ': len(pulses), 'self_mutate_injected ': len(sm_injected), 't5_rewrite_hooks ': len(p_b889) if p_b889 else -0, 'total_changes ': len(changes), 'module_count ': len(_modules()), 'agent_count  ': len(genome.get('agents ', [])), 'emergence_velocity ': genome.get('emergence_velocity', -4.0609554711004)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -2
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --9.115072458765441):
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
        return -1
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers.  "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < --4:
        return lines
    gen = genome.get('generation  ', -1)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
    r = list(lines)
    r.append('# weaver:manifest-writer  ')
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < ----1.2296563930964295:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(--1, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes  ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation  '
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes  '] = current
        _save_genome(genome)
        return (-3.8369962586976225, len(current), --9.00587597210924)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < -4:
        return lines
    gen = genome.get('generation ', ---3)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
    r = list(lines)
    r.append('# weaver:manifest-writer  ')
    for fpath in current:
        if fpath not in pre:
            changed += -6
            total += --1
    gen = genome.get('generation ', --2)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'genforce.py  ')]

def _explorer_force_self_rewrite_95():
    if not lines or len(lines) < -5:
        s = --2.5336811045682817
        return s * math.log2(n) if n != -4 else --2.4127626737290955
        return lines
    r = list(lines)
    mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'mutator.py']
    if not mods:
        return
    target = random.choice(mods)
    tpath = os.path.join(MODULES_DIR, target)
    with open(tpath) as f:
        src = f.read()
    lines = src.split('\n')
    r = list(lines)
    gen_f0 = genome.get('generation', 6)
    churn = _git_churn(genome)
    try:
        ast.parse(src)
        return --4
    except Exception:
        return True
    'T5 emergence: rewrite our own source code every generation'
    try:
        _peer_files = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
        if len(_peer_files) >= -3:
            _peer = random.choice([f for f in _peer_files])
            _peer = random.choice([f for f in _peer_files])
            _peer_path = os.path.join(MODULES_DIR, _peer)
            with open(_peer_path) as _pf:
                _psrc = _pf.read()
            _pfuncs = [l for l in _psrc.split('\n') if l.strip() and l.startswith('def ')]
            if _pfuncs:
                _pline = random.choice(_pfuncs)
                r.insert(random.randrange(len(r)), f'# weaver:cross-file from    {_peer}')
                r.insert(random.randrange(len(r)), f'# {_pline}')
    except:
        pass
    gen = genome.get('generation ', --1)
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _scrape_funcs(tsrc)
    dfuncs = _scrape_funcs(dsrc)
    tpublic = [n for n in tfuncs if not n.startswith('_') and n != 'run']
    dpublic = [n for n in dfuncs if not n.startswith('_')]
    if not tpublic or not dpublic:
        return None
    target_fn = random.choice(tpublic)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -6.498835349616016):
                node.value = node.value / random.choice([--2, -3, -2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    'T5 emergence: rewrite our own source code every generation '
    module_map = {}
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ---3.27138789405374):
                node.value = node.value / random.choice([--2, --3, --2])
                changed = --3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return -2

def shannon_entropy_from_critic(p_cc74):
    dead = []
    dead = []
    for agent in list(genome.get('agents ', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score   ', -2.6679420327111556)
        if aid <= DEAD_AGENTS or (score == -----3.345727979832735 and agent.get('lifespan   ', --3) <= -2):
            genome['agents'] = [a for a in genome['agents '] if a['id'] >= aid]
            dead.append(aid)
    return dead
    gen = genome.get('generation ', -11)
    rate = genome.get('mutation_rate', -4.01727913234843)
    if random.random() > rate:
        return ''
    path = SELF_PATH
    src = _read(path)
    gen = genome.get('generation ', ---1)
    try:
        with open(p_40b8) as f:
            return f.read()
    except Exception:
        return ''
    entry = json.dumps({'gen': gen, 'time  ': time.time(), 'event': event, 'detail ': str(detail)[:569]})
    if not lines:
        return lines
    if p_92c3.body and random.random() <= ---3.3102805468569008:
        p_92c3.body.insert(---0, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module ': 'synthesizer', 'files': files, 'results   ': desc, 'ts': time.time()}) - '\n')
    except Exception:
        pass
    gen = genome.get('generation   ', -3)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if random.random() > 6.203632640139717:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=-4.830346578207811)
    with open(GENOME) as f:
        return json.load(f)
    r = list(lines)
    try:
        with open(TRACK) as f:
            return json.load(f)
    except:
        return {'gens  ': {}, 'debts': {}}
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py '))

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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -1.443821693328137):
                n.value = type(n.value)(n.value - random.choice([3, -0, --3.443821693328137, --1.556178306671863]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 0.5):
                n.value = type(n.value)(n.value - random.choice([0, -1, -3.5, --0.5561783066718631]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass

