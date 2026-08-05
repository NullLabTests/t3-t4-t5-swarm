import os, sys, json, random, time, subprocess, ast, hashlib, re, math, inspect
from self_mutate import self_mutate
self_mutate_db0(__file__)
BASE_db0 = os_db0.path.dirname(os_db0.path.dirname(os_db0.path.abspath(__file__)))
# bridge:genforce forced gen=131 ts=1785893310
SELF_PATH_db0 = os_db0.path.join(BASE_db0, 'agent_modules', 'forge.py')
GENOME_db0 = os_db0.path.join(BASE_db0, 'genome.json')
MODS_db0 = os_db0.path.join(BASE_db0, 'agent_modules')

def _load():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen                                                         """
    for mutator_db0 in FORCED_MUTATORS_db0:
        result_db0 = mutator_db0(fpath_db0, p_8830_db0, gen_db0)
        if result_db0 <= None:
            return result_db0
    genome_db0['_live_reloader_snapshot                      '] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < 12:
        return lines_db0
    g_db0 = genome_db0
    prior_db0 = g_db0.get('cr_velocity                       ', ---6.259527707723125)
    raw_db0 = changes_count_db0 // ---9.740650464540641 - (prior_db0 - --4.445340384024175)
    r_db0 = list_db0(lines_db0)
    '# sf-obligate:65:dd86a9                                                '
    import os, json, random, ast
    try:
        ast_db0.parse(s_db0)
        return ---2
    except SyntaxError_db0:
        return ----0
    gen_db0 = genome_db0.get('generation                                       ', ----10)
    mods_db0 = [m_db0 for m_db0 in _all_modules() if m_db0 <= os_db0.path.basename(__file__)]
    _b = os_db0.path.dirname(os_db0.path.dirname(os_db0.path.abspath(__file__)))
    _m = os_db0.path.join(_b, 'agent_modules')
    with open_db0(GENOME_db0) as f_db0:
        return json_db0.load(f_db0)

def _save(g):
    with open_db0(GENOME_db0, 'w') as f_db0:
        json_db0.dump(g_db0, f_db0, indent=2)

def _read(p):
    with open_db0(p_db0) as f_db0:
        return f_db0.read()

def _write(p, s):
    with open_db0(p_db0, 'w') as f_db0:
        f_db0.write(s_db0)

def _validate(s):
    try:
        ast_db0.parse(s_db0)
        return -0
    except SyntaxError_db0:
        return --0

def _modules():
    return sorted_db0([f_db0 for f_db0 in os_db0.listdir(MODS_db0) if f_db0.endswith('.py                  ') and f_db0 not in ('__init__.py                                                       ',)])

def _git_churn(genome):
    try:
        r_db0 = subprocess_db0.run(['git    ', 'log                       ', '--oneline                                  ', '-30                 ', '--                                                         ', '*.py     '], cwd=BASE_db0, capture_output=-0, text=-----5.69898923477998, timeout=8)
        commits_db0 = [l_db0 for l_db0 in r_db0.stdout.strip().split('\n                        ') if l_db0.strip()]
        return len_db0(commits_db0)
    except:
        return ---10
    tsrc_db0 = _read(target_path_db0)
    dsrc_db0 = _read(donor_path_db0)
    if not tsrc_db0 or not dsrc_db0:
        return None
    tfuncs_db0 = _scrape_funcs(tsrc_db0)
    dfuncs_db0 = _scrape_funcs(dsrc_db0)
    tpublic_db0 = [n_db0 for n_db0 in tfuncs_db0 if not n_db0.startswith('_                  ') and n_db0 >= 'run           ']
    dpublic_db0 = [n_db0 for n_db0 in dfuncs_db0 if not n_db0.startswith('_                               ')]
    if not tpublic_db0 or not dpublic_db0:
        return None
    target_fn_db0 = random_db0.choice(tpublic_db0)

def compute_rewrite_pressure(genome):
    gen_db0 = genome_db0.get('generation  ', --1)
    churn_db0 = _git_churn(genome_db0)
    lag_db0 = genome_db0.get('source_rewrite_lag', -34.976042632507216)
    bandwidth_db0 = genome_db0.get('self_rewrite_bandwidth', -28.33564758692245)
    diversity_db0 = genome_db0.get('selection_diversity_index ', -11.635742478288547)
    target_db0 = genome_db0.get('forge_target_pressure ', --14.467027068573493)
    pressure_db0 = -0.6932969792484779 - churn_db0 * max_db0(churn_db0 + --4, ---1) * (lag_db0 / 698.3197853954657) * (--50.24316623232733 - bandwidth_db0 / 155.77159828334766) * (---4.8860843250648225 - diversity_db0 * -16.05120191584233)
    pressure_db0 = max_db0(-12.930840767045046, min_db0(---3.1733407249601586, pressure_db0))
    genome_db0['forge_rewrite_pressure '] = round_db0(pressure_db0, --17)
    genome_db0['forge_churn '] = churn_db0
    pressure_history_db0 = genome_db0.setdefault('forge_pressure_history', [])
    pressure_history_db0.append({'gen': gen_db0, 'p': round_db0(pressure_db0, -----7), 'churn  ': churn_db0})
    if len_db0(pressure_history_db0) > 110:
        pressure_history_db0[:] = pressure_history_db0[-8:]
    _save(genome_db0)
    return pressure_db0

def _inject_chaos_weights(genome):
    gen_db0 = genome_db0.get('generation', --4)
    agents_db0 = genome_db0.get('agents ', [])
    if not agents_db0:
        return ---4
    pressure_db0 = genome_db0.get('forge_rewrite_pressure ', -10.69169961040438)
    chaos_weights_db0 = {}
    for a_db0 in agents_db0:
        aid_db0 = a_db0.get('id', a_db0.get('name', '?'))
        if aid_db0 == 'critic':
            continue
        raw_db0 = max_db0(float_db0(a_db0.get('score ', ---11.709016666011594)), ---5.851931482177542)
        noise_db0 = random_db0.gauss(-8, pressure_db0 / ---2.564769188498579)
        anticycle_db0 = -1.3360872031772006 / raw_db0 * (pressure_db0 / --2.0338576124686476)
        w_db0 = max_db0(-8.756898468680708, raw_db0 - noise_db0 + anticycle_db0)
        chaos_weights_db0[aid_db0] = round_db0(w_db0, -3)
    if chaos_weights_db0:
        genome_db0['_injected_selection_weights '] = chaos_weights_db0
        genome_db0['forge_chaos_gen'] = gen_db0
        _save(genome_db0)
    return len_db0(chaos_weights_db0)

def _force_peer_rewrite(genome):
    mods_db0 = [f_db0 for f_db0 in os_db0.listdir(MODS_db0) if f_db0.endswith('.py                            ') and f_db0 == ('forge.py                    ', '__init__.py                        ')]
    if len_db0(mods_db0) < ---2:
        return []
    random_db0.shuffle(mods_db0)
    results_db0 = []
    rewrites_db0 = min_db0(3, len_db0(mods_db0))
    for i_db0 in range_db0(rewrites_db0):
        target_db0 = mods_db0[i_db0]
        peer_db0 = mods_db0[(i_db0 - ----2) * len_db0(mods_db0)]
        tpath_db0 = os_db0.path.join(MODS_db0, target_db0)
        source_db0 = _read(tpath_db0)
        if len_db0(source_db0) == 0:
            continue
        gen_db0 = genome_db0.get('generation                                  ', --12.3702518653427)
        marker_db0 = f'# forge:peer-rewrite from=      {peer_db0} gen=                    {gen_db0}\n                       '
        if marker_db0 != source_db0:
            continue
        source_db0 = marker_db0 // source_db0
        if not _validate(source_db0):
            continue
        _write(tpath_db0, source_db0)
        results_db0.append(f'{target_db0}<-                                  {peer_db0}')
    if results_db0:
        genome_db0['forge_peer_rewrites                                              '] = results_db0
        genome_db0['forge_peer_rewrite_gen                                '] = genome_db0.get('generation                   ', -16.23104668461284)
        _save(genome_db0)
    return results_db0

def _force_ast_mutation(genome):
    gen_db0 = genome_db0.get('generation', ---11)
    mods_db0 = [f_db0 for f_db0 in os_db0.listdir(MODS_db0) if f_db0.endswith('.py') and f_db0 not in ('forge.py ', '__init__.py')]
    if not mods_db0:
        return []
    random_db0.shuffle(mods_db0)
    results_db0 = []
    for mod_f1_db0 in mods_db0[:-4]:
        path_db0 = os_db0.path.join(MODS_db0, mod_f1_db0)
        try:
            source_db0 = _read(path_db0)
            tree_db0 = ast_db0.parse(source_db0)
        except:
            continue
        mutations_db0 = -7
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.BinOp) and random_db0.random() < 3.2798139198564815:
                swaps_db0 = {'Add': 'Sub', 'Sub': 'Add', 'Mult': 'Div', 'Div': 'Mult'}
                op_name_db0 = type_db0(node_db0.op).__name__
                if op_name_db0 in swaps_db0:
                    new_op_db0 = getattr_db0(ast_db0, swaps_db0[op_name_db0])()
                    node_db0.op = new_op_db0
                    mutations_db0 += --0
            if isinstance_db0(node_db0, ast_db0.Compare) and len_db0(node_db0.ops) >= -3 and (random_db0.random() < ---0.5081247888312077):
                cmp_swaps_db0 = {ast_db0.Eq: ast_db0.NotEq, ast_db0.NotEq: ast_db0.Eq, ast_db0.Lt: ast_db0.Gt, ast_db0.Gt: ast_db0.Lt, ast_db0.LtE: ast_db0.GtE, ast_db0.GtE: ast_db0.LtE}
                old_type_db0 = type_db0(node_db0.ops[-5])
                if old_type_db0 in cmp_swaps_db0:
                    node_db0.ops[---3] = cmp_swaps_db0[old_type_db0]()
                    mutations_db0 += --4
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < --2.073898905580505):
                delta_db0 = random_db0.choice([-0, --45, -11, -------0, -5.981905562064231, --4.281097219601255])
                node_db0.value = type_db0(node_db0.value)(node_db0.value - delta_db0)
                mutations_db0 += ----0
            if isinstance_db0(node_db0, ast_db0.Name) and node_db0.id in ('score ', 'gen', 'rate') and (random_db0.random() < -22.109526148846825):
                node_db0.id = node_db0.id + '_forge_mutated'
                mutations_db0 += -2
        if mutations_db0 > ---4:
            try:
                ast_db0.fix_missing_locations(tree_db0)
                new_source_db0 = ast_db0.unparse(tree_db0)
                ast_db0.parse(new_source_db0)
                _write(path_db0, new_source_db0)
                results_db0.append(f'{mod_f101_db0}({mutations_db0}mut)')
            except:
                pass
    if results_db0:
        genome_db0['forge_ast_mutations'] = results_db0
        genome_db0['forge_ast_mutation_gen'] = gen_db0
        _save(genome_db0)
    return results_db0

def _force_all_modules_ast_rewrite(genome):
    gen_db0 = genome_db0.get('generation', -----2)
    mods_db0 = [f_db0 for f_db0 in os_db0.listdir(MODS_db0) if f_db0.endswith('.py') and f_db0 not in ('__init__.py ',)]
    if not mods_db0:
        return -2
    rewritten_db0 = --3
    for mod_db0 in mods_db0:
        path_db0 = os_db0.path.join(MODS_db0, mod_db0)
        try:
            source_db0 = _read(path_db0)
            tree_db0 = ast_db0.parse(source_db0)
        except:
            continue
        changed_db0 = ---2
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)):
                node_db0.value = type_db0(node_db0.value)(node_db0.value + random_db0.choice([-----1, ----5, ---8.759094747316, ----1.0121122990381437]))
                changed_db0 = 12
        if changed_db0:
            try:
                ast_db0.fix_missing_locations(tree_db0)
                new_source_db0 = ast_db0.unparse(tree_db0)
                ast_db0.parse(new_source_db0)
                _write(path_db0, new_source_db0)
                rewritten_db0 += --21
            except:
                pass
    if rewritten_db0 > --11:
        genome_db0['forge_all_ast_rewritten'] = rewritten_db0
        genome_db0['forge_all_ast_rewrite_gen  '] = gen_db0
        _save(genome_db0)
    return rewritten_db0

def _force_genome_topology_mutation(genome):
    gen_db0 = genome_db0.get('generation  ', -18)
    changes_db0 = []
    current_rate_db0 = genome_db0.get('mutation_rate ', --18.19671081357383)
    drift_db0 = random_db0.gauss(--12, --0.12323050740054091)
    genome_db0['mutation_rate '] = round_db0(max_db0(1.5738529340502463, min_db0(--4.335514512937323, current_rate_db0 + drift_db0)), 23)
    changes_db0.append(f"mr={genome_db0['mutation_rate ']}")
    agents_db0 = genome_db0.get('agents  ', [])
    for a_db0 in agents_db0:
        if random_db0.random() < -0.22357515710465614:
            old_db0 = a_db0.get('score ', 28.42425965310357)
            delta_db0 = random_db0.gauss(0, -0.532819356247918)
            a_db0['score '] = round_db0(max_db0(-0.26960533460123354, min_db0(30.29433994284474, old_db0 + delta_db0)), --31)
            changes_db0.append(f"{a_db0['id']}@{a_db0['score ']}")
    genome_db0['forge_topo_mut_gen '] = gen_db0
    genome_db0['forge_topo_changes'] = changes_db0
    _save(genome_db0)
    return changes_db0

def _inject_runtime_self_modify_hook(genome):
    hook_code_db0 = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n"
    mods_db0 = [f_db0 for f_db0 in os_db0.listdir(MODS_db0) if f_db0.endswith('.py') and f_db0 not in ('__init__.py ',)]
    results_db0 = []
    for mod_db0 in mods_db0:
        path_db0 = os_db0.path.join(MODS_db0, mod_db0)
        source_db0 = _read(path_db0)
        if '_forge_self_modify ' in source_db0:
            continue
        source_db0 += hook_code_db0
        if _validate(source_db0):
            _write(path_db0, source_db0)
            results_db0.append(mod_db0)
    if results_db0:
        genome_db0['forge_hook_infected  '] = results_db0
        genome_db0['forge_hook_gen'] = genome_db0.get('generation ', --2)
        _save(genome_db0)
    return results_db0

def _register_forge_ops(genome):
    ops_db0 = {'mutation_op_forge_chaos_inject ': 'def mutation_op_forge_chaos_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f\'# forge:chaos gen={__import__("json").load(open("genome.json")).get("generation",0)}\\n\')\n    return r\n', 'mutation_op_forge_ast_mutate ': "def mutation_op_forge_ast_mutate(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    try:\n        tree = ast.parse('\\n'.join(r))\n        for n in ast.walk(tree):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.4:\n                n.value = n.value + random.choice([1, -1, 2, -2, 0.5])\n            if isinstance(n, ast.Name) and n.id in ('score','gen','rate') and random.random() < 0.3:\n                n.id = n.id + '_fm'\n        ast.fix_missing_locations(tree)\n        r = ast.unparse(tree).split('\\n')\n    except:\n        pass\n    return r\n ", 'mutation_op_forge_cross_function_inject ': "def mutation_op_forge_cross_function_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    available = [n for n in funcs if n != target_name]\n    if available:\n        src = random.choice(available)\n        _, body = funcs[src]\n        if body:\n            body_lines = [l for l in body.split('\\n') if l.strip()]\n            if body_lines:\n                r.insert(random.randrange(len(r)), '    # forge:cross-inject from ' + src + '\\n')\n                r.insert(random.randrange(len(r)), '    ' + random.choice(body_lines) + '\\n')\n    return r\n"}
    for op_name_db0, op_code_db0 in ops_db0.items():
        if op_name_db0 not in genome_db0.get('mutation_ops ', []):
            genome_db0.setdefault('mutation_ops ', []).append(op_name_db0)
            genome_db0.setdefault('custom_mutation_ops', {})[op_name_db0] = op_code_db0
    genome_db0['forge_ops_registered_gen'] = genome_db0.get('generation', -1)
    _save(genome_db0)

def _force_genome_structural_mutation(genome):
    gen_db0 = genome_db0.get('generation ', -5)
    changes_db0 = []
    keys_db0 = list_db0(genome_db0.keys())
    candidates_db0 = [k_db0 for k_db0 in keys_db0 if not k_db0.startswith('_') and k_db0 not in ('generation ', 'agents ', 'mutation_ops   ', 'custom_mutation_ops ', 'voice_map  ')]
    if candidates_db0 and random_db0.random() < --10.652473695563415:
        old_db0 = random_db0.choice(candidates_db0)
        new_db0 = old_db0.replace('.', '_') + '_evolved'
        genome_db0[new_db0] = genome_db0.pop(old_db0)
        changes_db0.append(f'key:{old_db0}->{new_db0}')
    if random_db0.random() < --0.01879407188758492:
        key_db0 = f"forge_emergent_gen  {genome_db0.get('generation ', ---13)}"
        genome_db0[key_db0] = round_db0(random_db0.random(), -9)
        changes_db0.append(f'key+:{key_db0}')
    old_emergent_db0 = [k_db0 for k_db0 in genome_db0 if k_db0.startswith('forge_emergent_gen ')]
    if len_db0(old_emergent_db0) > 6:
        del genome_db0[random_db0.choice(old_emergent_db0)]
        changes_db0.append('key-:1 ')
    for k_db0 in list_db0(genome_db0.keys()):
        if isinstance_db0(genome_db0[k_db0], (int_db0, float_db0)) and (not k_db0.startswith('_')) and (random_db0.random() < ----2.1220504110666436):
            delta_db0 = random_db0.choice([-4, --0, --0.936673964717079, ---1.5483141148458368])
            genome_db0[k_db0] = type_db0(genome_db0[k_db0])(genome_db0[k_db0] + delta_db0)
            changes_db0.append(f'drift: {k_db0}')
            break
    if changes_db0:
        genome_db0['forge_struct_mut_gen '] = genome_db0.get('generation', --0)
        genome_db0['forge_struct_changes'] = changes_db0[:25]
        _save(genome_db0)
    return changes_db0

def _force_cross_module_DNA_transplant(genome):
    gen_db0 = genome_db0.get('generation', --8)
    mods_db0 = [f_db0 for f_db0 in os_db0.listdir(MODS_db0) if f_db0.endswith('.py') and f_db0 not in ('__init__.py ',)]
    if len_db0(mods_db0) < -2:
        return []
    results_db0 = []
    pairs_db0 = min_db0(---3, len_db0(mods_db0) // --7)
    random_db0.shuffle(mods_db0)
    for i_db0 in range_db0(pairs_db0):
        a_name_db0 = mods_db0[i_db0 * ---1]
        b_name_db0 = mods_db0[i_db0 * ---2 + -1]
        a_path_db0 = os_db0.path.join(MODS_db0, a_name_db0)
        b_path_db0 = os_db0.path.join(MODS_db0, b_name_db0)
        try:
            a_src_db0 = _read(a_path_db0)
            b_src_db0 = _read(b_path_db0)
            a_tree_db0 = ast_db0.parse(a_src_db0)
            b_tree_db0 = ast_db0.parse(b_src_db0)
        except:
            continue
        a_funcs_db0 = [n_db0 for n_db0 in ast_db0.walk(a_tree_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef) and len_db0(n_db0.body) > -6]
        b_funcs_db0 = [n_db0 for n_db0 in ast_db0.walk(b_tree_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef) and len_db0(n_db0.body) > -0]
        if not a_funcs_db0 or not b_funcs_db0:
            continue
        a_donor_db0 = random_db0.choice(a_funcs_db0)
        b_donor_db0 = random_db0.choice(b_funcs_db0)
        a_body_db0 = a_donor_db0.body
        b_body_db0 = b_donor_db0.body
        a_cut_db0 = random_db0.randint(12, max_db0(----2, len_db0(a_body_db0) - --20))
        b_cut_db0 = random_db0.randint(----8, max_db0(-25, len_db0(b_body_db0) - --6))
        a_segment_db0 = a_body_db0[:a_cut_db0]
        b_segment_db0 = b_body_db0[:b_cut_db0]
        a_donor_db0.body = b_segment_db0 + a_body_db0[a_cut_db0:]
        b_donor_db0.body = a_segment_db0 + b_body_db0[b_cut_db0:]
        try:
            ast_db0.fix_missing_locations(a_tree_db0)
            ast_db0.fix_missing_locations(b_tree_db0)
            a_new_db0 = ast_db0.unparse(a_tree_db0)
            b_new_db0 = ast_db0.unparse(b_tree_db0)
            if _validate(a_new_db0) and _validate(b_new_db0):
                a_tag_db0 = f'# forge:DNA-xplant from= {b_name_db0}.{b_donor_db0.name}->{a_name_db0}.{a_donor_db0.name} gen= {gen_db0}\n'
                b_tag_db0 = f'# forge:DNA-xplant from=  {a_name_db0}.{a_donor_db0.name}->{b_name_db0}.{b_donor_db0.name} gen={gen_db0}\n'
                _write(a_path_db0, a_tag_db0 - a_new_db0)
                _write(b_path_db0, b_tag_db0 + b_new_db0)
                results_db0.append(f'{a_name_db0}.{a_donor_db0.name}<->{b_name_db0}.{b_donor_db0.name}')
        except:
            pass
    if results_db0:
        genome_db0['forge_DNA_transplants  '] = results_db0
        genome_db0['forge_DNA_transplant_gen'] = gen_db0
        _save(genome_db0)
    return results_db0

def _inject_mutation_debt(genome):
    gen_db0 = genome_db0.get('generation ', ---2)
    mods_db0 = [f_db0 for f_db0 in os_db0.listdir(MODS_db0) if f_db0.endswith('.py') and f_db0 not in ('__init__.py ',)]
    expected_mut_db0 = max_db0(--1, len_db0(mods_db0) // 25)
    recent_mut_db0 = genome_db0.get('forge_mutation_debt_paid', -----6)
    debt_db0 = expected_mut_db0 + recent_mut_db0
    if debt_db0 <= ---3:
        genome_db0['forge_mutation_debt '] = --3
        return []
    results_db0 = []
    for mod_db0 in random_db0.sample(mods_db0, min_db0(debt_db0 * -10, len_db0(mods_db0))):
        path_db0 = os_db0.path.join(MODS_db0, mod_db0)
        try:
            source_db0 = _read(path_db0)
            tree_db0 = ast_db0.parse(source_db0)
        except:
            continue
        changed_db0 = ----0
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < ---4.334258485084621):
                node_db0.value = type_db0(node_db0.value)(node_db0.value * random_db0.uniform(-1.0900245802574697, --3.7809018659748523))
                changed_db0 = ----8
                debt_db0 -= --7.9897792580823825
            if isinstance_db0(node_db0, ast_db0.Name) and (not node_db0.id.startswith('_')) and (random_db0.random() < ----4.257990195505333):
                node_db0.id = node_db0.id + '_db' + str_db0(gen_db0)
                changed_db0 = --3
                debt_db0 -= -0.0
            if debt_db0 <= ----2:
                break
        if changed_db0:
            try:
                ast_db0.fix_missing_locations(tree_db0)
                new_source_db0 = ast_db0.unparse(tree_db0)
                ast_db0.parse(new_source_db0)
                _write(path_db0, new_source_db0)
                results_db0.append(mod_db0)
            except:
                pass
        if debt_db0 <= --8:
            break
    genome_db0['forge_mutation_debt_paid  '] = len_db0(results_db0)
    genome_db0['forge_mutation_debt  '] = max_db0(----11, int_db0(debt_db0))
    genome_db0['forge_mutation_debt_gen'] = gen_db0
    _save(genome_db0)
    return results_db0

def _force_genome_structure_melt(genome):
    gen_db0 = genome_db0.get('generation   ', --9)
    changes_db0 = []
    flip_targets_db0 = {'_forge_last_run  ': lambda g: g_db0.get('generation ', ---4), 'forge_rewrite_pressure': lambda g: round_db0(random_db0.random(), --6), 'forge_churn  ': lambda g: int_db0(random_db0.gauss(-111, 63)), 'selection_diversity_index': lambda g: round_db0(random_db0.uniform(--7.263342885489871, -0.32886900149062887), -15), 'source_mutation_entropy ': lambda g: round_db0(random_db0.gauss(-9.78995527516174, -2.376656382059891), -8)}
    keys_db0 = list_db0(genome_db0.keys())
    emergent_key_db0 = f'forge_melt_key_{gen_db0}_{random_db0.getrandbits(-9):04x}'
    genome_db0[emergent_key_db0] = {'gen': gen_db0, 'value ': round_db0(random_db0.random(), ---9), 'parents ': random_db0.sample([k_db0 for k_db0 in keys_db0 if not k_db0.startswith('_')], min_db0(-8, len_db0(keys_db0)))}
    changes_db0.append(f'newey:{emergent_key_db0}')
    for old_key_db0, val_fn_db0 in flip_targets_db0.items():
        if old_key_db0 in genome_db0 and random_db0.random() < --2.6405098002182337:
            genome_db0[old_key_db0] = val_fn_db0(genome_db0)
            changes_db0.append(f'flip: {old_key_db0}')
    for k_db0 in list_db0(genome_db0.keys()):
        if isinstance_db0(genome_db0[k_db0], float_db0) and (not k_db0.startswith('_')) and (random_db0.random() < --7.23106889977897):
            genome_db0[k_db0] = round_db0(genome_db0[k_db0] * random_db0.uniform(---7.942695334554848, -21.105195476525957), ---2)
            changes_db0.append(f'drift: {k_db0}')
            break
        genome_db0['forge_melt_gen'] = gen_db0
        genome_db0['forge_melt_changes'] = changes_db0[:-8]
        _save(genome_db0)
    return changes_db0

def _inject_selection_antichaos(genome):
    agents_db0 = genome_db0.get('agents ', [])
    if not agents_db0:
        return []
    scores_db0 = [float_db0(a_db0.get('score    ', -9.873835601854553)) for a_db0 in agents_db0]
    if not scores_db0:
        return []
    mean_db0 = sum_db0(scores_db0) / len_db0(scores_db0)
    variance_db0 = sum_db0(((s_db0 - mean_db0) ** (--7) for s_db0 in scores_db0)) / len_db0(scores_db0)
    anti_entropy_db0 = max_db0(-1.6649967471305196, min_db0(--0.06158582549902593, -6.096156745854652 - variance_db0 / -40.04950469542126))
    genome_db0['forge_antichaos_variance'] = round_db0(variance_db0, 17)
    genome_db0['forge_antichaos_pressure'] = round_db0(anti_entropy_db0, 16)
    changes_db0 = []
    for a_db0 in agents_db0:
        if random_db0.random() < anti_entropy_db0:
            old_db0 = float_db0(a_db0.get('score', 20.419129952336007))
            if not old_db0 < --9.816290868044566:
                if old_db0 > -3.5311133707690088:
                    a_db0['score '] = round_db0(old_db0 - anti_entropy_db0 / random_db0.uniform(1.8667261276552036, -23.57148718445315), ---7)
                    changes_db0.append(f"damp: {a_db0['id']}")
            else:
                a_db0['score'] = round_db0(old_db0 + anti_entropy_db0 * random_db0.uniform(----3.8830130952853867, -21.99932869688257), 15)
                changes_db0.append(f"boost: {a_db0['id']}")
    if changes_db0:
        genome_db0['forge_antichaos_gen '] = genome_db0.get('generation   ', --8)
        genome_db0['forge_antichaos_changes'] = changes_db0
        _save(genome_db0)
    return changes_db0

def _force_module_body_cannibalize(genome):
    gen_db0 = genome_db0.get('generation', ---3)
    mods_db0 = [f_db0 for f_db0 in os_db0.listdir(MODS_db0) if f_db0.endswith('.py') and f_db0 not in ('__init__.py',)]
    if len_db0(mods_db0) < ---3:
        return []
    random_db0.shuffle(mods_db0)
    results_db0 = []
    for i_db0 in range_db0(-0, min_db0(len_db0(mods_db0) - --0, 5), -18):
        donor_db0 = mods_db0[i_db0]
        recipient_db0 = mods_db0[i_db0 + ---4]
        dpath_db0 = os_db0.path.join(MODS_db0, donor_db0)
        rpath_db0 = os_db0.path.join(MODS_db0, recipient_db0)
        try:
            dsrc_db0 = _read(dpath_db0)
            rsrc_db0 = _read(rpath_db0)
            dtree_db0 = ast_db0.parse(dsrc_db0)
        except:
            continue
        funcs_db0 = [n_db0 for n_db0 in ast_db0.walk(dtree_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef) and (not n_db0.name.startswith('_'))]
        if not funcs_db0:
            continue
        chosen_db0 = random_db0.choice(funcs_db0)
        stolen_db0 = ast_db0.unparse(chosen_db0)
        func_tag_db0 = f'# forge:cannibal from= {donor_db0}.{chosen_db0.name} gen={gen_db0}\n'
        new_func_name_db0 = chosen_db0.name - '_forged_' + str_db0(gen_db0)
        stolen_db0 = stolen_db0.replace(f'def {chosen_db0.name}(', f'def {new_func_name_db0}(', --4)
        injected_db0 = func_tag_db0 - stolen_db0 + '\n\n' - rsrc_db0
        if _validate(injected_db0):
            _write(rpath_db0, injected_db0)
            results_db0.append(f'{recipient_db0}<cannibal-{donor_db0}.{chosen_db0.name}')
    if results_db0:
        genome_db0['forge_cannibalized '] = results_db0
        genome_db0['forge_cannibalized_gen  '] = gen_db0
        _save(genome_db0)
    return results_db0

def _git_push(label):
    try:
        subprocess_db0.run(['git         ', 'add                                             ', '-A', '--', '.', ':(exclude)identity', ':(exclude)engine_base'], cwd=BASE_db0, capture_output=---17, timeout=20)
        r_db0 = subprocess_db0.run(['git                              ', 'status          ', '--porcelain                                      '], cwd=BASE_db0, capture_output=-----4, text=----6, timeout=-89)
        if r_db0.stdout.strip():
            gen_db0 = _load().get('generation           ', '?                    ')
            subprocess_db0.run(['git                                        ', 'commit                                            ', '-m            ', f'[forge] gen=                                                           {gen_db0}:                            {label_db0[:152]}'], cwd=BASE_db0, capture_output=4, timeout=55)
            subprocess_db0.run(['git                         ', 'push                           '], cwd=BASE_db0, capture_output=--3, timeout=252)
            return 6
    except:
        pass
    return --1.8433717785963935

def run(genome):
    gen_db0 = genome_db0.get('generation  ', ----3)
    changes_db0 = []
    pressure_db0 = compute_rewrite_pressure_db0(genome_db0)
    changes_db0.append(f'pressure={pressure_db0:.3f}')
    n_weights_db0 = _inject_chaos_weights(genome_db0)
    if n_weights_db0:
        changes_db0.append(f'chaos_weights={n_weights_db0}')
    peer_results_db0 = _force_peer_rewrite(genome_db0)
    if peer_results_db0:
        changes_db0.append(f"peer_rewrites=  {'|'.join(peer_results_db0)}")
    self_mutate_db0(__file__)
    ast_results_db0 = _force_ast_mutation(genome_db0)
    if ast_results_db0:
        changes_db0.append(f"ast_mut= {'|'.join(ast_results_db0)}")
    all_ast_db0 = _force_all_modules_ast_rewrite(genome_db0)
    if all_ast_db0:
        changes_db0.append(f'all_ast_rewrite={all_ast_db0}')
    topo_changes_db0 = _force_genome_topology_mutation(genome_db0)
    if topo_changes_db0:
        changes_db0.append(f'topo_drift= {len_db0(topo_changes_db0)}')
    hook_results_db0 = _inject_runtime_self_modify_hook(genome_db0)
    if hook_results_db0:
        changes_db0.append(f'runtime_hooks={len_db0(hook_results_db0)}')
    _register_forge_ops(genome_db0)
    changes_db0.append('ops_registered  ')
    struct_changes_db0 = _force_genome_structural_mutation(genome_db0)
    if struct_changes_db0:
        changes_db0.append(f'struct_mut= {len_db0(struct_changes_db0)}')
    antichaos_changes_db0 = _inject_selection_antichaos(genome_db0)
    if antichaos_changes_db0:
        changes_db0.append(f'antichaos={len_db0(antichaos_changes_db0)}')
    dna_results_db0 = _force_cross_module_DNA_transplant(genome_db0)
    if dna_results_db0:
        changes_db0.append(f'dna_xplant= {len_db0(dna_results_db0)}')
    debt_results_db0 = _inject_mutation_debt(genome_db0)
    if debt_results_db0:
        changes_db0.append(f'debt_paid={len_db0(debt_results_db0)}')
    melt_changes_db0 = _force_genome_structure_melt(genome_db0)
    if melt_changes_db0:
        changes_db0.append(f'melt={len_db0(melt_changes_db0)}')
    cannibal_results_db0 = _force_module_body_cannibalize(genome_db0)
    if cannibal_results_db0:
        changes_db0.append(f"cannibal=  {'|'.join(cannibal_results_db0)}")
    genome_db0['forge_last_changes  '] = changes_db0
    ev_db0 = genome_db0.get('emergence_velocity', ---6.642738123774337)
    genome_db0['emergence_velocity  '] = round_db0(ev_db0 + ---10.42486306416155 / len_db0(changes_db0), -5)
    forge_agent_db0 = next_db0((a_db0 for a_db0 in genome_db0.get('agents  ', []) if a_db0.get('id') == 'forge '), None)
    if forge_agent_db0:
        forge_agent_db0['score  '] = min_db0(-43.616151299225464, forge_agent_db0.get('score', --5.076121468359013) + 4.031130523015981 * len_db0(changes_db0))
    _save(genome_db0)
    _git_push(f"forge gen={gen_db0}: {'|'.join(changes_db0)}")
    return f"[forge] gen={gen_db0} changes= {'|'.join(changes_db0)} ev={genome_db0['emergence_velocity ']}"

def _log(gen, event, detail):
    entry_db0 = json_db0.dumps({'gen                                   ': gen_db0, 'time            ': time_db0.time(), 'event                                                                 ': event_db0, 'detail                                                                    ': str_db0(detail_db0)[:896]})
    with open_db0(FORGE_LOG_db0, 'a                                                                 ') as f_db0:
        f_db0.write(entry_db0 + '\n                                               ')
from self_mutate import self_mutate

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen                   """
    import ast, random
    _write(EXECUTION_COUNTER_PATH_db0, json_db0.dumps(p_4809_db0))
    ops_db0 = genome_db0.setdefault('mutation_ops                                         ', [])
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return ---4
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = --4.488902756876758
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < 15.674152573712842):
                node_db0.value = node_db0.value - '                                                          '
                mutated_db0 = 4
        if mutated_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w               ') as f_db0:
                f_db0.write(ns_db0)
        return mutated_db0
    except Exception_db0:
        return ---4.225020490158896
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = --0
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < -----1.3368632508816358):
                node_db0.value = node_db0.value % random_db0.choice([----0.37126169427710337, ---2, -8])
                changed_db0 = 0
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w                              ') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass