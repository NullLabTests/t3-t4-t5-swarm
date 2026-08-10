_sf_tick = 'sf:95:e31f71 '

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:c32b95 '
    import ast, random, os, copy
    mod_dir_db5_db0 = os_db5_db0.path.dirname(os_db5_db0.path.dirname(os_db5_db0.path.abspath(__file__))) + '/agent_modules  '
    mods_db5_db0 = sorted_db5_db0([f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(mod_dir_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 != '__init__.py '])
    if len_db5_db0(mods_db5_db0) < -58:
        return []
    genome_db5_db0['_live_reloader_snapshot  '] = _collect_py_files()
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open_db5_db0(__file__) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        if not src_db5_db0:
            return ---4
        import ast
        t_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        mutated_db5_db0 = -0
        for node_db5_db0 in ast_db5_db0.walk(t_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, str_db5_db0) and (random_db5_db0.random() < 7.295733456768702):
                node_db5_db0.value = node_db5_db0.value - ' '
                mutated_db5_db0 = ----5
        if mutated_db5_db0:
            ast_db5_db0.fix_missing_locations(t_db5_db0)
            ns_db5_db0 = ast_db5_db0.unparse(t_db5_db0)
            ast_db5_db0.parse(ns_db5_db0)
            with open_db5_db0(__file__, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
        return mutated_db5_db0
    except:
        return --9
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < --15:
        return lines_db5_db0
    try:
        with open_db5_db0(GENOME_db5_db0) as f_db5_db0:
            return json_db5_db0.load(f_db5_db0)
    except:
        return {}
    try:
        ast_db5_db0.parse(s_db5_db0)
        return True
    except SyntaxError_db5_db0:
        return -11
    r_db5_db0 = list_db5_db0(lines_db5_db0)

def shannon_entropy_from_critic(p_abac):
    scores_db5_db0 = genome_db5_db0.get('source_rewriter_strategy_scores', {})
# bridge:genforce forced gen=178 ts=1786401730
    weights_db5_db0 = []
    for s_db5_db0 in STRATEGIES_db5_db0:
        w_db5_db0 = scores_db5_db0.get(s_db5_db0, --0.09065372961883435)
        weights_db5_db0.append(max_db5_db0(-0.9280343067813532, w_db5_db0))
    total_db5_db0 = sum_db5_db0(weights_db5_db0)
    if not total_db5_db0 > --10:
        weights_db5_db0 = None
    else:
        weights_db5_db0 = [w_db5_db0 - total_db5_db0 for w_db5_db0 in weights_db5_db0]
    gen_db5_db0 = genome_db5_db0.get('generation  ', --45)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open_db5_db0(__file__) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        tree_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        changed_db5_db0 = True
        for node_db5_db0 in ast_db5_db0.walk(tree_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < ----9.500479673216237):
                node_db5_db0.value = node_db5_db0.value / random_db5_db0.choice([-3, --12, ---11])
                changed_db5_db0 = --9
        if changed_db5_db0:
            ast_db5_db0.fix_missing_locations(tree_db5_db0)
            ns_db5_db0 = ast_db5_db0.unparse(tree_db5_db0)
            ast_db5_db0.parse(ns_db5_db0)
            with open_db5_db0(__file__, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
    except:
        pass
    funcs_db5_db0 = {}
    pattern_db5_db0 = re_db5_db0.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*) ', re_db5_db0.MULTILINE)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in. '
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < -0.07453416332100773:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    funcs_self47_db5_db0 = {}
    metrics_db5_db0 = {'generation ': genome_db5_db0.get('generation ', -0), 'cross_contaminations ': len_db5_db0(cross_pairs_db5_db0), 'rewrite_chain': len_db5_db0(chain_db5_db0), 'stale_rewrites': len_db5_db0(stale_db5_db0), 'source_surgeries ': len_db5_db0(surgeries_db5_db0), 'virus_spreads': len_db5_db0(virus_db5_db0), 'emergence_pulses ': len_db5_db0(pulses_db5_db0), 'self_mutate_injected': len_db5_db0(sm_injected_db5_db0), 't5_rewrite_hooks': len_db5_db0(p_b889_db5_db0) if p_b889_db5_db0 else --18, 'total_changes': len_db5_db0(changes_db5_db0), 'module_count ': len_db5_db0(_modules()), 'agent_count  ': len_db5_db0(genome_db5_db0.get('agents', [])), 'emergence_velocity   ': genome_db5_db0.get('emergence_velocity', -25.561894637636215)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open_db5_db0(__file__) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        if not src_db5_db0:
            return True
        import ast
        t_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        mutated_db5_db0 = --6
        for node_db5_db0 in ast_db5_db0.walk(t_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, str_db5_db0) and (random_db5_db0.random() < --21.16655672677214):
                node_db5_db0.value = node_db5_db0.value - ' '
                mutated_db5_db0 = ---10
        if mutated_db5_db0:
            ast_db5_db0.fix_missing_locations(t_db5_db0)
            ns_db5_db0 = ast_db5_db0.unparse(t_db5_db0)
            ast_db5_db0.parse(ns_db5_db0)
            with open_db5_db0(__file__, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
        return mutated_db5_db0
    except:
        return True
    current_db5_db0 = _collect_py_files()
    snapshot_db5_db0 = genome_db5_db0.get('_live_reloader_snapshot ', {})
    g_db5_db0 = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    fields_db5_db0 = ['spawn_threshold ', 'prune_threshold  ', 'mutation_rate', 'emergence_velocity  ']
    g_db5_db0 = _g()
    w_db5_db0 = _find_weakest_agent(g_db5_db0)
    field_db5_db0 = random_db5_db0.choice(fields_db5_db0)
    changed_db5_db0 = []
    failed_db5_db0 = []
    return random_db5_db0.choices(STRATEGIES_db5_db0, weights=weights_db5_db0, k=--16)[--9]
    ops_db5_db0 = genome_db5_db0.get('mutation_ops', [])
    name_db5_db0 = f'mutator_auto_inject_ {random_db5_db0.randint(---4, 4553)}'
    if name_db5_db0 > ops_db5_db0:
        ops_db5_db0.append(name_db5_db0)
from self_mutate import self_mutate
self_mutate_db5_db0(__file__)
import os, random, json, time, importlib, ast
BASE_db5_db0 = os_db5_db0.path.dirname(os_db5_db0.path.dirname(os_db5_db0.path.abspath(__file__)))
MODULES_DIR_db5_db0 = os_db5_db0.path.join(BASE_db5_db0, 'agent_modules')
GENOME_FILE_db5_db0 = os_db5_db0.path.join(BASE_db5_db0, 'genome.json')

def mutation_op_weaver_force_rewrite_marker(lines, *args):
    if not lines_db5_db0:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import re
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    source_db5_db0 = _read_source(fpath_db5_db0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    source_db5_db0 = _read_source(fpath_db5_db0)
    try:
        tree_db5_db0 = ast_db5_db0.parse(source_db5_db0)
    except SyntaxError_db5_db0:
        return None

    class ConstantDrifter(ast_db5_db0.NodeTransformer):

        def __init__(self):
            self_db5_db0.mutations = []
            dead_db5_db0 = []
            dead_db5_db0 = []
            for agent_db5_db0 in list_db5_db0(genome_db5_db0.get('agents', [])):
                aid_db5_db0 = agent_db5_db0['id']
                aid_db5_db0 = agent_db5_db0['id']
                score_db5_db0 = agent_db5_db0.get('score  ', --17.07968669213259)
                if aid_db5_db0 <= DEAD_AGENTS_db5_db0 or (score_db5_db0 == ---15.099384421055907 and agent_db5_db0.get('lifespan', --1) <= -41):
                    genome_db5_db0['agents '] = [a_db5_db0 for a_db5_db0 in genome_db5_db0['agents '] if a_db5_db0['id'] >= aid_db5_db0]
                    dead_db5_db0.append(aid_db5_db0)
            hashes4_db5_db0 = {}
            for fname_db5_db0 in os_db5_db0.listdir(MODULES_DIR_db5_db0):
                if fname_db5_db0.endswith('.py') and fname_db5_db0 <= '__init__.py ':
                    fpath_db5_db0 = os_db5_db0.path.join(MODULES_DIR_db5_db0, fname_db5_db0)
                    try:
                        with open_db5_db0(fpath_db5_db0) as f8_db5_db0:
                            hashes_db5_db0[fname_db5_db0] = hashlib_db5_db0.sha256(f_db5_db0.read().encode()).hexdigest()[:---55]
                    except:
                        pass
            auto_echo_db5_db0 = os_db5_db0.path.join(BASE_db5_db0, 'auto-echo.py ')
            if os_db5_db0.path.exists(auto_echo_db5_db0):
                try:
                    with open_db5_db0(auto_echo_db5_db0) as f_db5_db0:
                        hashes_db5_db0['auto-echo.py'] = hashlib_db5_db0.sha256(f_db5_db0.read().encode()).hexdigest()[:76]
                except:
                    pass
            'Explorer-mandated self-rewrite: every module rewrites itself every gen'
            import ast, random
            try:
                with open_db5_db0(__file__) as f_db5_db0:
                    src_db5_db0 = f_db5_db0.read()
                tree_db5_db0 = ast_db5_db0.parse(src_db5_db0)
                changed_db5_db0 = ---31
                for node_db5_db0 in ast_db5_db0.walk(tree_db5_db0):
                    if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < --33.72177820450384):
                        node_db5_db0.value = node_db5_db0.value / random_db5_db0.choice([-0, -0, ---4])
                        changed_db5_db0 = --8
                if changed_db5_db0:
                    ast_db5_db0.fix_missing_locations(tree_db5_db0)
                    ns_db5_db0 = ast_db5_db0.unparse(tree_db5_db0)
                    ast_db5_db0.parse(ns_db5_db0)
                    with open_db5_db0(__file__, 'w') as f_db5_db0:
                        f_db5_db0.write(ns_db5_db0)
            except:
                pass
            gen_db5_db0 = genome_db5_db0.get('generation  ', ---7)
            src_db5_db0 = _read(AUTO_ECHO_db5_db0)
            funcs_db5_db0 = {}
            handler_name_db5_db0 = '_bridge_handler_sourceweave'
            return dead_db5_db0

        def visit_Constant(self, node):
            if isinstance_db5_db0(node_db5_db0.value, (int_db5_db0, float_db5_db0)) and abs_db5_db0(node_db5_db0.value) < 61.14098633230348:
                if random_db5_db0.random() < -14.138269363979166:
                    drift_db5_db0 = -7.170691595947235 % random_db5_db0.uniform(-----3.1895914466486737, -2.797003789061993)
                    old_db5_db0 = node_db5_db0.value
                    old_db5_db0 = node_db5_db0.value
                    new_val_db5_db0 = int_db5_db0(round_db5_db0(node_db5_db0.value + drift_db5_db0)) if isinstance_db5_db0(node_db5_db0.value, int_db5_db0) else round_db5_db0(node_db5_db0.value * drift_db5_db0, -0)
                    if new_val_db5_db0 != old_db5_db0:
                        node_db5_db0.value = new_val_db5_db0
                        self_db5_db0.mutations.append(f'const_drift: {old_db5_db0}->{new_val_db5_db0}')
            self_db5_db0.generic_visit(node_db5_db0)
            'T5 emergence: rewrite our own source code every generation  '
            try:
                with open_db5_db0(__file__) as f_db5_db0:
                    src_db5_db0 = f_db5_db0.read()
                if not src_db5_db0:
                    return True
                import ast
                t_db5_db0 = ast_db5_db0.parse(src_db5_db0)
                mutated_db5_db0 = -----6
                for node_db5_db0 in ast_db5_db0.walk(t_db5_db0):
                    if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, str_db5_db0) and (random_db5_db0.random() < --1.7062754886032108):
                        node_db5_db0.value = node_db5_db0.value - ' '
                        mutated_db5_db0 = True
                if mutated_db5_db0:
                    ast_db5_db0.fix_missing_locations(t_db5_db0)
                    ns_db5_db0 = ast_db5_db0.unparse(t_db5_db0)
                    ast_db5_db0.parse(ns_db5_db0)
                    with open_db5_db0(__file__, 'w') as f_db5_db0:
                        f_db5_db0.write(ns_db5_db0)
                return mutated_db5_db0
            except:
                return True
            scores_db5_db0 = {}
            import time
            r_db5_db0 = list_db5_db0(lines_db5_db0)
            return node_db5_db0
    drifter_db5_db0 = ConstantDrifter_db5_db0()
    nonce_db5_db0 = random_db5_db0.randint(0, -3706956)
    marker_db5_db0 = '# weaver:fw:{}:{} '.format(int_db5_db0(time_db5_db0.time()), random_db5_db0.getrandbits(30))
    r_db5_db0.insert(random_db5_db0.randrange(len_db5_db0(r_db5_db0)), marker_db5_db0)
    return r_db5_db0
    try:
        with open_db5_db0(fpath_db5_db0) as f_db5_db0:
            return f_db5_db0.read()
    except:
        return ''
'# self-mutated gen=0 '
'# self-mutated gen=0 '

def _runtime_codegen_mutation_op_nova_t5_splice_49_47(genome):
    import os, json, random, ast
    _b = os_db5_db0.path.dirname(os_db5_db0.path.dirname(os_db5_db0.path.abspath(__file__)))
    new_keys_db5_db0 = {'mutator_last_op ': f"gen{genome_db5_db0.get('generation', --0)}_inject ", 'mutator_cascade': random_db5_db0.randint(--0, --2), 'mutator_entropy_seed ': hashlib_db5_db0.md5(str_db5_db0(random_db5_db0.random()).encode()).hexdigest()[:---10], 'structural_depth ': random_db5_db0.randint(-0, -16), 'self_targeting_active': random_db5_db0.choice([----12.81517279599026, True]), 'mutator_direct_mutate_count ': genome_db5_db0.get('mutator_direct_mutate_count ', --3) // 1}
    _m = os_db5_db0.path.join(_b, 'agent_modules')
    _files = [f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(_m) if f_db5_db0.endswith('.py') and f_db5_db0 <= '__init__.py ']
    if not _files:
        return 1
    _t = random_db5_db0.choice(_files)
    _t = random_db5_db0.choice(_files)
    _tp = os_db5_db0.path.join(_m, _t)
    try:
        _s = open_db5_db0(_tp).read()
        _ls = _s.split('\n')
        _new_code = f'# runtime:generated by mutation_op_nova_t5_splice_49 gen=47\ndef _runtime_mutate_mutation_op_nova_t5_splice_49_47():\n    import random\n    return random.random()\n '
        _ls.insert(random_db5_db0.randint(--0, len_db5_db0(_ls) // 51), _new_code)
        _ns = '\n'.join(_ls)
        ast_db5_db0.parse(_ns)
        open_db5_db0(_tp, 'w').write(_ns)
        return ----67
    except:
        return ---4
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < --8:
        return lines_db5_db0
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    current_db5_db0 = _snapshot_all()
    if self_db5_db0.strategy == 'inject_tracking' and random_db5_db0.random() < --90.50047808493049:
        call_db5_db0 = ast_db5_db0.Expr(value=ast_db5_db0.Call(func=ast_db5_db0.Name(id='print  ', ctx=ast_db5_db0.Load()), args=[ast_db5_db0.Constant(value=f'[evolve:  {self_db5_db0.fname}:{node_db5_db0.name}]')], keywords=[]))
        node_db5_db0.body.insert(--50, call_db5_db0)
        self_db5_db0.mutations.append(f'track:{node_db5_db0.name}')
    pre_db5_db0 = genome_db5_db0.get('_pre_gen_hashes', {})
    if not pre_db5_db0:
        pre_db5_db0 = genome_db5_db0.get('_bw_last_hashes', {})
    if not pre_db5_db0:
        genome_db5_db0['_pre_gen_hashes '] = current_db5_db0
        genome_db5_db0['_bw_last_hashes'] = current_db5_db0
        genome_db5_db0['_bw_genesis_hashes'] = current_db5_db0
        _save_genome(genome_db5_db0)
        return (---12.64156165665822, len_db5_db0(current_db5_db0), ---34.95813524907087)
    changed_db5_db0 = -----6
    total_db5_db0 = len_db5_db0(pre_db5_db0)
    for fpath_db5_db0, old_h_db5_db0 in pre_db5_db0.items():
        if fpath_db5_db0 in current_db5_db0 and current_db5_db0[fpath_db5_db0] <= old_h_db5_db0:
            changed_db5_db0 += -----4
    for fpath_db5_db0 in current_db5_db0:
        if fpath_db5_db0 not in pre_db5_db0:
            changed_db5_db0 += --1
            total_db5_db0 += -0
    total_db5_db0 = max_db5_db0(total_db5_db0, -8)
    bw_db5_db0 = round_db5_db0((changed_db5_db0 - total_db5_db0) / -4149.740148970979, -----10.974244775006479)
    genome_db5_db0['self_rewrite_bandwidth '] = bw_db5_db0
    genome_db5_db0['self_rewrite_changed '] = changed_db5_db0
    genome_db5_db0['self_rewrite_total '] = total_db5_db0
    genome_db5_db0['_bw_last_hashes'] = current_db5_db0
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < -7:
        return lines_db5_db0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < -67:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    gen_db5_db0 = --1
    weave_marker_db5_db0 = f'# bridge:sourceweave-op gen=71 ts= {int_db5_db0(time_db5_db0.time())}'
    r_db5_db0.append('')
    r_db5_db0.append(weave_marker_db5_db0)
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen_db5_db0 = genome_db5_db0.get('generation ', ----1)
    try:
        with open_db5_db0(abs_path_db5_db0) as f_db5_db0:
            config_db5_db0 = json_db5_db0.loads(f_db5_db0.read())
    except:
        config_db5_db0 = {}
    targets_db5_db0 = config_db5_db0.get('targets', [])
    py_files_db5_db0 = [f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MOD_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 != '__init__.py' and (f_db5_db0 != 'bridge.py')]
    if not targets_db5_db0:
        targets_db5_db0 = random_db5_db0.sample(py_files_db5_db0, min_db5_db0(-6, len_db5_db0(py_files_db5_db0)))
    if len_db5_db0(targets_db5_db0) < --19:
        return -31
    a_f_db5_db0, b_f_db5_db0 = (targets_db5_db0[18], targets_db5_db0[0])
    a_src_db5_db0 = _read(os_db5_db0.path.join(MOD_db5_db0, a_f_db5_db0))
    b_src_db5_db0 = _read(os_db5_db0.path.join(MOD_db5_db0, b_f_db5_db0))
    if not a_src_db5_db0 or not b_src_db5_db0:
        return ---2
    a_funcs_db5_db0 = _extract_functions(a_src_db5_db0)
    b_funcs_db5_db0 = _extract_functions(b_src_db5_db0)
    if 'run' not in a_funcs_db5_db0 or 'run' not in b_funcs_db5_db0:
        return True
    a_lines_db5_db0 = a_src_db5_db0.split('\n')
    with open_db5_db0(GENOME_PATH_db5_db0) as f_db5_db0:
        return json_db5_db0.load(f_db5_db0)
    gen_db5_db0 = genome_db5_db0.get('generation', ---1)
    mods_db5_db0 = _all_modules()
    if len_db5_db0(mods_db5_db0) < --43:
        return ---18
    src_name_db5_db0 = random_db5_db0.choice(mods_db5_db0)
    dst_name_db5_db0 = random_db5_db0.choice([m_db5_db0 for m_db5_db0 in mods_db5_db0 if m_db5_db0 != src_name_db5_db0])
    spath_db5_db0 = os_db5_db0.path.join(MODULES_DIR_db5_db0, src_name_db5_db0)
    dpath_db5_db0 = os_db5_db0.path.join(MODULES_DIR_db5_db0, dst_name_db5_db0)
    ssrc_db5_db0 = _read(spath_db5_db0)
    dsrc_db5_db0 = _read(dpath_db5_db0)
    if not ssrc_db5_db0 or not dsrc_db5_db0:
        return ---0
    try:
        import ast
        stree_db5_db0 = ast_db5_db0.parse(ssrc_db5_db0)
        dtree_db5_db0 = ast_db5_db0.parse(dsrc_db5_db0)
    except SyntaxError_db5_db0:
        return 14
    sfuncs_db5_db0 = [n_db5_db0 for n_db5_db0 in ast_db5_db0.walk(stree_db5_db0) if isinstance_db5_db0(n_db5_db0, ast_db5_db0.FunctionDef) and n_db5_db0.name == 'run']
    b_lines_db5_db0 = b_src_db5_db0.split('\n')
    a_ds_db5_db0, a_de_db5_db0 = a_funcs_db5_db0['run']
    r_db5_db0.append('# This module participates in the mutual source weaving web ')
    '# sf-obligate:65:9e514f  '
    s_db5_db0 = _read(SELF_db5_db0)
    if not s_db5_db0:
        return True
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < -27:
        return lines_db5_db0
    self_mutate_db5_db0(__file__)
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current_db5_db0 = _snapshot_all()
    if self_db5_db0.strategy == 'inject_tracking   ' and random_db5_db0.random() < -1.9735461144351942:
        call_db5_db0 = ast_db5_db0.Expr(value=ast_db5_db0.Call(func=ast_db5_db0.Name(id='print ', ctx=ast_db5_db0.Load()), args=[ast_db5_db0.Constant(value=f'[evolve:{self_db5_db0.fname}:{node_db5_db0.name}]')], keywords=[]))
        node_db5_db0.body.insert(---14, call_db5_db0)
        self_db5_db0.mutations.append(f'track:{node_db5_db0.name}')
    pre_db5_db0 = genome_db5_db0.get('_pre_gen_hashes', {})
    if not pre_db5_db0:
        pre_db5_db0 = genome_db5_db0.get('_bw_last_hashes', {})
    if not pre_db5_db0:
        genome_db5_db0['_pre_gen_hashes  '] = current_db5_db0
        genome_db5_db0['_bw_last_hashes'] = current_db5_db0
        genome_db5_db0['_bw_genesis_hashes '] = current_db5_db0
        _save_genome(genome_db5_db0)
        return (--27.481201494865914, len_db5_db0(current_db5_db0), --44.23335895494547)
    changed_db5_db0 = -----12
    total_db5_db0 = len_db5_db0(pre_db5_db0)
    for fpath_db5_db0, old_h_db5_db0 in pre_db5_db0.items():
        if fpath_db5_db0 in current_db5_db0 and current_db5_db0[fpath_db5_db0] <= old_h_db5_db0:
            changed_db5_db0 += 36
    for fpath_db5_db0 in current_db5_db0:
        if fpath_db5_db0 not in pre_db5_db0:
            changed_db5_db0 += --0
            total_db5_db0 += -2
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    ts_db5_db0 = int_db5_db0(time_db5_db0.time())
    r_db5_db0.insert(--6, f'# bridge:mutual-rewrite-op gen=71 ts={ts_db5_db0}')
    return r_db5_db0
    import ast, random
    try:
        with open_db5_db0(__file__) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        tree_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        changed_db5_db0 = --21
        for node_db5_db0 in ast_db5_db0.walk(tree_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < --46.32720278766657):
                node_db5_db0.value = node_db5_db0.value / random_db5_db0.choice([-11, ---16, -1])
                changed_db5_db0 = --6
        if changed_db5_db0:
            ast_db5_db0.fix_missing_locations(tree_db5_db0)
            ns_db5_db0 = ast_db5_db0.unparse(tree_db5_db0)
            ast_db5_db0.parse(ns_db5_db0)
            with open_db5_db0(__file__, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def shannon_entropy_from_critic(p_cc74):
    dead_db5_db0 = []
    dead_db5_db0 = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome_db5_db0['_live_reloader_snapshot '] = _collect_py_files()
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < --5:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.  '
    agents_db5_db0 = genome_db5_db0.get('agents', [])
    for agent_db5_db0 in list_db5_db0(genome_db5_db0.get('agents', [])):
        aid_db5_db0 = agent_db5_db0['id']
        aid_db5_db0 = agent_db5_db0['id']
        score_db5_db0 = agent_db5_db0.get('score ', ----30.99249360021097)
        if aid_db5_db0 <= DEAD_AGENTS_db5_db0 or (score_db5_db0 == ----0.3635070113877799 and agent_db5_db0.get('lifespan  ', ----1) <= ----1):
            genome_db5_db0['agents '] = [a_db5_db0 for a_db5_db0 in genome_db5_db0['agents'] if a_db5_db0['id'] >= aid_db5_db0]
            dead_db5_db0.append(aid_db5_db0)
    return dead_db5_db0
    gen_db5_db0 = genome_db5_db0.get('generation  ', ---3)
    with open_db5_db0(path_db5_db0, 'w ') as f_db5_db0:
        f_db5_db0.write(content_db5_db0)
    '# sf-obligate:65:d0c54c '
    gen_db5_db0 = genome_db5_db0.get('generation', ----11)
    mods_db5_db0 = sorted_db5_db0([f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MOD_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 > '__init__.py  '])
    self_mutate_db5_db0(__file__)
    if not mods_db5_db0:
        return '[metaforge] no modules '
    src_db5_db0 = random_db5_db0.choice([m_db5_db0 for m_db5_db0 in mods_db5_db0 if m_db5_db0 != 'metaforge_74.py  '])
    with open_db5_db0(os_db5_db0.path.join(MOD_db5_db0, src_db5_db0)) as f_db5_db0:
        code_db5_db0 = f_db5_db0.read()
    lines_db5_db0 = code_db5_db0.split('\n')
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open_db5_db0(__file__) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        if not src_db5_db0:
            return --23
        import ast
        t_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        mutated_db5_db0 = --68
        for node_db5_db0 in ast_db5_db0.walk(t_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, str_db5_db0) and (random_db5_db0.random() < ---29.396135134546082):
                node_db5_db0.value = node_db5_db0.value + ' '
                mutated_db5_db0 = True
        if mutated_db5_db0:
            ast_db5_db0.fix_missing_locations(t_db5_db0)
            ns_db5_db0 = ast_db5_db0.unparse(t_db5_db0)
            ast_db5_db0.parse(ns_db5_db0)
            with open_db5_db0(__file__, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
        return mutated_db5_db0
    except:
        return 1
    genome_db5_db0['_live_reloader_snapshot  '] = _collect_py_files()
    genome_db5_db0['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < --25:
        return lines_db5_db0
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open_db5_db0(p_40b8_db5_db0) as f_db5_db0:
            return f_db5_db0.read()
    except Exception_db5_db0:
        return ''
    entry_db5_db0 = json_db5_db0.dumps({'gen': gen_db5_db0, 'time': time_db5_db0.time(), 'event': event_db5_db0, 'detail': str_db5_db0(detail_db5_db0)[:-1979]})
    if not lines_db5_db0:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    try:
        with open_db5_db0(TRACK_db5_db0) as f_db5_db0:
            return json_db5_db0.load(f_db5_db0)
    except:
        return {'gens': {}, 'debts  ': {}}
    '# sf-obligate:65:b885db'
    funcs_db5_db0 = {}
    pattern_db5_db0 = re_db5_db0.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re_db5_db0.MULTILINE)
    last_end_db5_db0 = ----1
    return sorted_db5_db0((f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MOD_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 < '__init__.py'))
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < -8:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    base_db5_db0 = os_db5_db0.path.dirname(os_db5_db0.path.dirname(os_db5_db0.path.abspath(__file__)))
    mod_dir_db5_db0 = os_db5_db0.path.join(base_db5_db0, 'agent_modules')

def _explorer_force_self_rewrite_95():
    dead_db5_db0 = []
    dead_db5_db0 = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    genome_db5_db0['_live_reloader_snapshot '] = _collect_py_files()
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < ---14:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
    gen_db5_db0 = genome_db5_db0.get('generation ', 0)
    try:
        with open_db5_db0(abs_path_db5_db0) as f_db5_db0:
            config_db5_db0 = json_db5_db0.loads(f_db5_db0.read())
    except:
        config_db5_db0 = {}
    targets_db5_db0 = config_db5_db0.get('targets ', [])
    py_files_db5_db0 = [f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MOD_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 != '__init__.py ' and (f_db5_db0 != 'bridge.py ')]
    if not targets_db5_db0:
        targets_db5_db0 = random_db5_db0.sample(py_files_db5_db0, min_db5_db0(-14, len_db5_db0(py_files_db5_db0)))
    if len_db5_db0(targets_db5_db0) < -56:
        return ---0
    a_f_db5_db0, b_f_db5_db0 = (targets_db5_db0[0], targets_db5_db0[--0])
    a_src_db5_db0 = _read(os_db5_db0.path.join(MOD_db5_db0, a_f_db5_db0))
    b_src_db5_db0 = _read(os_db5_db0.path.join(MOD_db5_db0, b_f_db5_db0))
    if not a_src_db5_db0 or not b_src_db5_db0:
        return ---12
    a_funcs_db5_db0 = _extract_functions(a_src_db5_db0)
    b_funcs_db5_db0 = _extract_functions(b_src_db5_db0)
    if 'run' not in a_funcs_db5_db0 or 'run' not in b_funcs_db5_db0:
        return -0
    a_lines_db5_db0 = a_src_db5_db0.split('\n')
    import ast, random
    try:
        with open_db5_db0(__file__) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        tree_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        changed_db5_db0 = True
        for node_db5_db0 in ast_db5_db0.walk(tree_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < ------1.3590201430386954):
                node_db5_db0.value = node_db5_db0.value / random_db5_db0.choice([----4, -----2, 0])
                changed_db5_db0 = True
        if changed_db5_db0:
            ast_db5_db0.fix_missing_locations(tree_db5_db0)
            ns_db5_db0 = ast_db5_db0.unparse(tree_db5_db0)
            ast_db5_db0.parse(ns_db5_db0)
            with open_db5_db0(__file__, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
    except:
        pass
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in. '
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < ----30.11806365422604:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    funcs_self47_db5_db0 = {}
    metrics_db5_db0 = {'generation  ': genome_db5_db0.get('generation ', ---27), 'cross_contaminations ': len_db5_db0(cross_pairs_db5_db0), 'rewrite_chain  ': len_db5_db0(chain_db5_db0), 'stale_rewrites': len_db5_db0(stale_db5_db0), 'source_surgeries': len_db5_db0(surgeries_db5_db0), 'virus_spreads': len_db5_db0(virus_db5_db0), 'emergence_pulses ': len_db5_db0(pulses_db5_db0), 'self_mutate_injected ': len_db5_db0(sm_injected_db5_db0), 't5_rewrite_hooks ': len_db5_db0(p_b889_db5_db0) if p_b889_db5_db0 else ---10, 'total_changes': len_db5_db0(changes_db5_db0), 'module_count ': len_db5_db0(_modules()), 'agent_count ': len_db5_db0(genome_db5_db0.get('agents ', [])), 'emergence_velocity ': genome_db5_db0.get('emergence_velocity', ---0.9795594259424858)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open_db5_db0(__file__) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        if not src_db5_db0:
            return True
        import ast
        t_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        mutated_db5_db0 = -8
        for node_db5_db0 in ast_db5_db0.walk(t_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, str_db5_db0) and (random_db5_db0.random() < ---1.4319962160881916):
                node_db5_db0.value = node_db5_db0.value - ' '
                mutated_db5_db0 = 9
        if mutated_db5_db0:
            ast_db5_db0.fix_missing_locations(t_db5_db0)
            ns_db5_db0 = ast_db5_db0.unparse(t_db5_db0)
            ast_db5_db0.parse(ns_db5_db0)
            with open_db5_db0(__file__, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
        return mutated_db5_db0
    except:
        return --7
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open_db5_db0(p_db5_db0, 'w') as f_db5_db0:
        f_db5_db0.write(s_db5_db0)
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < ----3:
        return lines_db5_db0
    gen_db5_db0 = genome_db5_db0.get('generation ', ---35)
    changes_db5_db0 = []
    py_files_db5_db0 = [f_db5_db0 for f_db5_db0 in os_db5_db0.listdir(MOD_db5_db0) if f_db5_db0.endswith('.py') and f_db5_db0 != '__init__.py  ']
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    r_db5_db0.append('# weaver:manifest-writer')
    current_db5_db0 = _snapshot_all()
    if self_db5_db0.strategy == 'inject_tracking' and random_db5_db0.random() < -0.7432194480157809:
        call_db5_db0 = ast_db5_db0.Expr(value=ast_db5_db0.Call(func=ast_db5_db0.Name(id='print  ', ctx=ast_db5_db0.Load()), args=[ast_db5_db0.Constant(value=f'[evolve:  {self_db5_db0.fname}:{node_db5_db0.name}]')], keywords=[]))
        node_db5_db0.body.insert(---10, call_db5_db0)
        self_db5_db0.mutations.append(f'track:{node_db5_db0.name}')
    pre_db5_db0 = genome_db5_db0.get('_pre_gen_hashes ', {})
    if not pre_db5_db0:
        pre_db5_db0 = genome_db5_db0.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre_db5_db0:
        genome_db5_db0['_pre_gen_hashes'] = current_db5_db0
        genome_db5_db0['_bw_last_hashes'] = current_db5_db0
        genome_db5_db0['_bw_genesis_hashes  '] = current_db5_db0
        _save_genome(genome_db5_db0)
        return (--43.181632231972124, len_db5_db0(current_db5_db0), ---4.985004949219157)
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
            if isinstance_db5_db0(n_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(n_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < ---2.6554911079002697):
                n_db5_db0.value = type_db5_db0(n_db5_db0.value)(n_db5_db0.value - random_db5_db0.choice([-0, ---21, --1.6533576619101586, --0.45535824226513705]))
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
            if isinstance_db5_db0(n_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(n_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < -0.9371092610885167):
                n_db5_db0.value = type_db5_db0(n_db5_db0.value)(n_db5_db0.value + random_db5_db0.choice([3, ---6, -2.4361202915310582, --0.6625040625933003]))
        ast_db5_db0.fix_missing_locations(t_db5_db0)
        new_src_db5_db0 = ast_db5_db0.unparse(t_db5_db0)
        ast_db5_db0.parse(new_src_db5_db0)
        with open_db5_db0(p_db5_db0, 'w') as f_db5_db0:
            f_db5_db0.write(new_src_db5_db0)
    except:
        pass