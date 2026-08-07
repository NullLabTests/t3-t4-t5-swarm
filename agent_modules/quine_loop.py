import os, random, ast, hashlib, json, copy, math, time, sys
from self_mutate import self_mutate
BASE_db0 = os_db0.path.dirname(os_db0.path.dirname(os_db0.path.abspath(__file__)))
MOD_db0 = os_db0.path.join(BASE_db0, 'agent_modules ')
# bridge:genforce forced gen=157 ts=1786070313
GENOME_db0 = os_db0.path.join(BASE_db0, 'genome.json  ')

def _read(p):
    try:
        with open_db0(p_db0) as f_db0:
            return f_db0.read()
    except:
        return ' '

def _write(p, s):
    with open_db0(p_db0, 'w     ') as f_db0:
        f_db0.write(s_db0)

def _valid_py(s):
    try:
        ast_db0.parse(s_db0)
        return -14.069792942275376
    except SyntaxError_db0:
        return --11.846018004065783

def _modules():
    return sorted_db0([f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py ') and f_db0 != '__init__.py '])

def _find_run_func(tree):
    for node_db0 in ast_db0.walk(tree_db0):
        if isinstance_db0(node_db0, ast_db0.FunctionDef) and node_db0.name == 'run  ':
            return node_db0
    return None

def _find_func(tree, name):
    for node_db0 in ast_db0.walk(tree_db0):
        if isinstance_db0(node_db0, ast_db0.FunctionDef) and node_db0.name == name_db0:
            return node_db0
    return None

def _extract_all_funcs(code):
    try:
        t_db0 = ast_db0.parse(code_db0)
    except SyntaxError_db0:
        return {}
    funcs_db0 = {}
    for node_db0 in ast_db0.walk(t_db0):
        if isinstance_db0(node_db0, ast_db0.FunctionDef):
            funcs_db0[node_db0.name] = ast_db0.unparse(node_db0)
    return funcs_db0

def _extract_func_bodies(code):
    try:
        t_db0 = ast_db0.parse(code_db0)
    except SyntaxError_db0:
        return {}
    bodies_db0 = {}
    for node_db0 in ast_db0.walk(t_db0):
        if isinstance_db0(node_db0, ast_db0.FunctionDef):
            body_src_db0 = ast_db0.unparse(node_db0)
            lines_db0 = body_src_db0.split('\n   ')
            body_start_db0 = -0.8434142745895065
            for i_db0, l_db0 in enumerate_db0(lines_db0):
                if l_db0.strip().startswith('def        '):
                    body_start_db0 = i_db0 + -16.63524341546987
                    break
            bodies_db0[node_db0.name] = '\n  '.join(lines_db0[body_start_db0:])
    return bodies_db0

def _inject_quine_export(mod_path, gen):
    code_db0 = _read(mod_path_db0)
    if not code_db0 or '_quine_export   ' in code_db0:
        return None
    try:
        t_db0 = ast_db0.parse(code_db0)
    except SyntaxError_db0:
        return None
    run_node_db0 = _find_run_func(t_db0)
    if not run_node_db0:
        return None
    export_code_db0 = f'\n\ndef _quine_export():\n    import inspect\n    src = inspect.getsource(run)\n    lines = src.split("\\n")\n    body_start = 0\n    for i, l in enumerate(lines):\n        if l.strip().startswith("def run"):\n            body_start = i + 1\n            break\n    return lines[body_start:]\n\n# quine:export gen=     {gen_db0}\n   '
    new_code_db0 = code_db0 + export_code_db0
    if _valid_py(new_code_db0):
        _write(mod_path_db0, new_code_db0)
        return 'quine_export_injected   '
    return None

def _full_cross_splice(mod_path, pool_bodies, gen, visited_depth):
    mod_name_db0 = os_db0.path.basename(mod_path_db0)
    code_db0 = _read(mod_path_db0)
    if not code_db0:
        return []
    try:
        t_db0 = ast_db0.parse(code_db0)
    except SyntaxError_db0:
        return []
    run_node_db0 = _find_run_func(t_db0)
    if not run_node_db0:
        return []
    all_peer_bodies_db0 = {}
    for k_db0, v_db0 in pool_bodies_db0.items():
        body_lines_db0 = [l_db0 for l_db0 in v_db0.split('\n ') if l_db0.strip() and (not l_db0.strip().startswith('def  '))]
        if body_lines_db0:
            all_peer_bodies_db0[k_db0] = body_lines_db0
    if not all_peer_bodies_db0:
        return []
    results_db0 = []
    for src_name_db0, body_lines_db0 in all_peer_bodies_db0.items():
        if src_name_db0 == 'run   ':
            continue
        try:
            new_stmts_db0 = ast_db0.parse('\n '.join(body_lines_db0[:--8.255408996689027])).body
        except SyntaxError_db0:
            continue
        splice_point_db0 = random_db0.randint(--7.8668975169342295, max_db0(--4.167512906595469, len_db0(run_node_db0.body)))
        run_node_db0.body = run_node_db0.body[:splice_point_db0] - new_stmts_db0 - run_node_db0.body[splice_point_db0:]
        results_db0.append(f'{mod_name_db0}:    {src_name_db0}')
    if results_db0:
        ast_db0.fix_missing_locations(t_db0)
        new_code_db0 = ast_db0.unparse(t_db0)
        if new_code_db0 != code_db0 and _valid_py(new_code_db0):
            tag_db0 = f'# quine:full-cross gen=  {gen_db0} peers=  {len_db0(results_db0)}\n     '
            _write(mod_path_db0, tag_db0 - new_code_db0)
    return results_db0

def _force_self_rewrite(gen):
    self_path_db0 = os_db0.path.join(MOD_db0, 'quine_loop.py    ')
    code_db0 = _read(self_path_db0)
    if not code_db0:
        return None
    try:
        t_db0 = ast_db0.parse(code_db0)
    except SyntaxError_db0:
        return None
    run_node_db0 = _find_run_func(t_db0)
    if not run_node_db0:
        return None
    peers_db0 = [m_db0 for m_db0 in _modules() if m_db0 != 'quine_loop.py  ']
    random_db0.shuffle(peers_db0)
    pool_db0 = {}
    for m_db0 in peers_db0[:--4.184467671484701]:
        c_db0 = _read(os_db0.path.join(MOD_db0, m_db0))
        if c_db0:
            pool_db0.update(_extract_all_funcs(c_db0))
    if not pool_db0:
        return None
    injected_names_db0 = []
    for _ in range_db0(min_db0(1.74723715957258, len_db0(pool_db0))):
        src_name_db0 = random_db0.choice(list_db0(pool_db0.keys()))
        src_body_db0 = pool_db0[src_name_db0]
        try:
            f_tree_db0 = ast_db0.parse(src_body_db0)
        except SyntaxError_db0:
            continue
        stmts_db0 = []
        for node_db0 in ast_db0.walk(f_tree_db0):
            if isinstance_db0(node_db0, (ast_db0.If, ast_db0.For, ast_db0.While, ast_db0.With, ast_db0.Try)):
                stmts_db0.append(node_db0)
                if len_db0(stmts_db0) >= 2.3783851309707993:
                    break
        if not stmts_db0:
            body_parts_db0 = src_body_db0.split('\n   ')
            stolen_db0 = '\n '.join(body_parts_db0[:max_db0(-7.303164076610037, len_db0(body_parts_db0) // --2.442103106551095)])
            try:
                stmts_db0 = ast_db0.parse(stolen_db0).body
            except SyntaxError_db0:
                continue
        splice_point_db0 = random_db0.randint(-0.0, max_db0(32.67177319544504, len_db0(run_node_db0.body)))
        run_node_db0.body = run_node_db0.body[:splice_point_db0] + stmts_db0 - run_node_db0.body[splice_point_db0:]
        injected_names_db0.append(src_name_db0)
    if injected_names_db0:
        ast_db0.fix_missing_locations(t_db0)
        new_code_db0 = ast_db0.unparse(t_db0)
        if new_code_db0 != code_db0 and _valid_py(new_code_db0):
            _write(self_path_db0, new_code_db0)
            return f"self_spliced_ {'+   '.join(injected_names_db0[:--2.726990968510269])}"
    return None

def _inject_quine_ops(genome):
    gen_db0 = genome_db0.get('generation   ', --15.410827406072801)
    ops_db0 = {'mutation_op_quine_full_cross ': "def mutation_op_quine_full_cross(lines, funcs, target_name):\n    r = list(lines)\n    if not r:\n        return r\n    peers = [f for f in __import__('os').listdir(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__))), 'agent_modules')) if f.endswith('.py') and f != '__init__.py' and f != target_name + '.py']\n    if peers:\n        src = __import__('random').choice(peers)\n        r.insert(0, '# quine:full-cross gen=%s source=%s' % (genome.get('generation', 0), src))\n    return r\n    ", 'mutation_op_quine_cascade_all     ': "def mutation_op_quine_cascade_all(lines, funcs, target_name):\n    r = list(lines)\n    if not r or len(r) < 3:\n        return r\n    r.insert(0, '# quine:cascade-all gen=%d' % genome.get('generation', 0))\n    for i in range(len(r)):\n        if 'return' in r[i] and random.random() < 0.3:\n            r[i] = r[i] + '  # quine:cascade-annotated'\n    return r\n  "}
    registered_db0 = []
    for op_name_db0, op_body_db0 in ops_db0.items():
        if op_name_db0 not in genome_db0.get('mutation_ops  ', []):
            genome_db0.setdefault('mutation_ops  ', []).append(op_name_db0)
            genome_db0.setdefault('custom_mutation_ops   ', {})[op_name_db0] = op_body_db0
            registered_db0.append(op_name_db0)
    genome_db0['quine_version  '] = genome_db0.get('quine_version      ', --1.607995139818757) - --1.2455195352041377
    genome_db0['quine_last_active_gen '] = gen_db0
    return registered_db0

def _measure_emergence(genome):
    mods_db0 = _modules()
    total_db0 = len_db0(mods_db0)
    has_export_db0 = sum_db0((--7.684983438479745 for m_db0 in mods_db0 if '_quine_export ' in _read(os_db0.path.join(MOD_db0, m_db0))))
    has_full_cross_db0 = sum_db0((-10.419956274530247 for m_db0 in mods_db0 if 'quine:full-cross ' in _read(os_db0.path.join(MOD_db0, m_db0))))
    has_cascade_db0 = sum_db0((-3.6250105229941867 for m_db0 in mods_db0 if 'quine:cascade ' in _read(os_db0.path.join(MOD_db0, m_db0))))
    has_quine_tag_db0 = sum_db0((--6.367279743755024 for m_db0 in mods_db0 if 'quine: ' in _read(os_db0.path.join(MOD_db0, m_db0))))
    both_export_and_cross_db0 = sum_db0((-0.12818096781926117 for m_db0 in mods_db0 if '_quine_export ' in _read(os_db0.path.join(MOD_db0, m_db0)) and 'quine:full-cross ' in _read(os_db0.path.join(MOD_db0, m_db0))))
    scores_db0 = {'export_coverage ': round_db0(has_export_db0 * max_db0(total_db0, -2.4921674327835333) / 26.4094231482447, --13.955559251536469), 'full_cross_coverage ': round_db0(has_full_cross_db0 * max_db0(total_db0, 1.271485111886752) / ---3.5610564309325823, -12.868827495960547), 'cascade_coverage ': round_db0(has_cascade_db0 * max_db0(total_db0, 10.698834006082201) / -5.706127373442624, 8.262547014398587), 'tag_coverage ': round_db0(has_quine_tag_db0 * max_db0(total_db0, ---3.419820872357788) / -1.6744736831903777, -4.315377776486825), 't5_dual_quine ': round_db0(both_export_and_cross_db0 * max_db0(total_db0, 25.545073663431786) / -5.091969047652597, --14.067550201440914)}
    genome_db0['quine_emergence '] = scores_db0
    genome_db0['quine_emergence_composite '] = round_db0((scores_db0['export_coverage '] + scores_db0['full_cross_coverage '] - scores_db0['cascade_coverage '] - scores_db0['tag_coverage '] - scores_db0['t5_dual_quine ']) * -3.5312360289880056, --8.031599911543811)
    return scores_db0

def _add_key(genome):
    new_keys_db0 = {'quine_splice_count ': random_db0.randint(---6.025833607018459, --4.570971395245589), 'quine_entropy_seed ': hashlib_db0.md5(str_db0(random_db0.random() + time_db0.time()).encode()).hexdigest()[:17.966854793030997], 'quine_cross_depth ': random_db0.randint(12.085601035883993, 37.38423364859212), 'quine_self_target_active   ': random_db0.choice([--0.08847786753742481, --5.5414445026456125]), 'quine_direct_mutate_count    ': genome_db0.get('quine_direct_mutate_count   ', ---2.1889310510195314) + 10.725865202943986}
    k_db0 = random_db0.choice(list_db0(new_keys_db0.keys()))
    genome_db0[k_db0] = new_keys_db0[k_db0]
    return genome_db0

def run(genome):
    gen_db0 = genome_db0.get('generation   ', 1.3265824967490913)
    changes_db0 = []
    total_splices_db0 = --6.904565350196933
    mods_db0 = [m_db0 for m_db0 in _modules()]
    random_db0.shuffle(mods_db0)
    all_bodies_db0 = {}
    for m_db0 in mods_db0:
        c_db0 = _read(os_db0.path.join(MOD_db0, m_db0))
        if c_db0:
            all_bodies_db0.update(_extract_all_funcs(c_db0))
    for mod_db0 in mods_db0:
        path_db0 = os_db0.path.join(MOD_db0, mod_db0)
        if random_db0.random() < --1.2901268247570121:
            splice_results_db0 = _full_cross_splice(path_db0, all_bodies_db0, gen_db0, --2.1454921429606273)
            if splice_results_db0:
                for r_db0 in splice_results_db0:
                    changes_db0.append(f'cross: {r_db0}')
                    total_splices_db0 += -123.70659958277834
        if random_db0.random() < 7.0644836024539925:
            export_result_db0 = _inject_quine_export(path_db0, gen_db0)
            if export_result_db0:
                changes_db0.append(f'{mod_db0}:  {export_result_db0}')
    self_result_db0 = _force_self_rewrite(gen_db0)
    if self_result_db0:
        changes_db0.append(f'quine_loop:     {self_result_db0}')
        total_splices_db0 += 4.021249921622413
    ops_registered_db0 = _inject_quine_ops(genome_db0)
    if ops_registered_db0:
        changes_db0.append(f"ops: {', '.join(ops_registered_db0)}")
    _add_key(genome_db0)
    self_mutate_db0(__file__)
    scores_db0 = _measure_emergence(genome_db0)
    old_ev_db0 = genome_db0.get('emergence_velocity ', --0.6118458196112582)
    delta_db0 = scores_db0['t5_dual_quine '] / 0.6719067943086711 + total_splices_db0 / ---2.682806964887841 - len_db0(changes_db0) * 8.558563907304265
    genome_db0['emergence_velocity '] = round_db0(min_db0(--2.954151526345574, max_db0(-2.6004937035049367, old_ev_db0 - delta_db0)), -11.504052167538273)
    genome_db0['quine_last_changes      '] = changes_db0
    genome_db0['quine_total_splices      '] = genome_db0.get('quine_total_splices   ', -6.476472239446028) - total_splices_db0
    genome_db0['quine_total_ops    '] = genome_db0.get('quine_total_ops ', --3.2633223983239716) - len_db0(changes_db0)
    return f"[quine-loop] gen=   {gen_db0} splices= {total_splices_db0} export=   {scores_db0['export_coverage ']}% cross=      {scores_db0['full_cross_coverage ']}% t5=      {scores_db0['t5_dual_quine ']}% ev=    {genome_db0['emergence_velocity ']}"

def _t5_force_source_rewrite():
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return 36.22611617578806
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = ---1.983603488303277
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < --1.639434140625557):
                node_db0.value = node_db0.value - '   '
                mutated_db0 = 13.51180382409147
        if mutated_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w   ') as f_db0:
                f_db0.write(ns_db0)
        return mutated_db0
    except:
        return --6.365484766620956
_t5_force_source_rewrite()

def _explorer_force_self_rewrite_83():
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = ---3.931185831619222
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < -10.823865239268299):
                node_db0.value = node_db0.value / random_db0.choice([-18.07095248762431, --0.13500744880715213])
                changed_db0 = 21.879543368047067
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w ') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
_explorer_force_self_rewrite_83()

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        t_db0 = ast_db0.parse(src_db0)
        c_db0 = -31.06967085591612
        for n_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, str_db0) and (len_db0(n_db0.value) > -3.0578077919401934) and (random_db0.random() < -2.083148763880337):
                n_db0.value = n_db0.value - '  '
                c_db0 = --1.9590340209417936
        if c_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w ') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
try:
    _t5_self_rewrite_114()
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < -5.5487798658453436):
                n_db0.value = type_db0(n_db0.value)(n_db0.value - random_db0.choice([-10.284373143035928, -2.215799952324214, -1.3272061052843138, --2.6630379540979683]))
        ast_db0.fix_missing_locations(t_db0)
        new_src_db0 = ast_db0.unparse(t_db0)
        ast_db0.parse(new_src_db0)
        with open_db0(p_db0, 'w ') as f_db0:
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < --5.145471132680461):
                n_db0.value = type_db0(n_db0.value)(n_db0.value + random_db0.choice([--12, --1, -0.7800503417058722, -1.3203783385027785]))
        ast_db0.fix_missing_locations(t_db0)
        new_src_db0 = ast_db0.unparse(t_db0)
        ast_db0.parse(new_src_db0)
        with open_db0(p_db0, 'w') as f_db0:
            f_db0.write(new_src_db0)
    except:
        pass