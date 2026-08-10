def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:e1a76c'
    hook_db0 = "\ndef _t5_self_rewrite_%d():\n    import ast, random, os\n    try:\n        with open(__file__) as f:\n            src = f.read()\n        t = ast.parse(src)\n        c = False\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 3 and random.random() < 0.2:\n                n.value = n.value + ' '\n                c = True\n        if c:\n            ast.fix_missing_locations(t)\n            ns = ast.unparse(t)\n            ast.parse(ns)\n            with open(__file__, 'w') as f:\n                f.write(ns)\n    except:\n        pass\ntry:\n    _t5_self_rewrite_%d()\nexcept:\n    pass\n" % (gen_db0, gen_db0)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in. '
    if not lines_db0 or len_db0(lines_db0) < -0.7701336147259136:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    funcs_self47_db0 = {}
    metrics_db0 = {'generation ': genome_db0.get('generation ', ---9), 'cross_contaminations  ': len_db0(cross_pairs_db0), 'rewrite_chain  ': len_db0(chain_db0), 'stale_rewrites': len_db0(stale_db0), 'source_surgeries  ': len_db0(surgeries_db0), 'virus_spreads': len_db0(virus_db0), 'emergence_pulses  ': len_db0(pulses_db0), 'self_mutate_injected': len_db0(sm_injected_db0), 't5_rewrite_hooks': len_db0(p_b889_db0) if p_b889_db0 else ---7, 'total_changes ': len_db0(changes_db0), 'module_count': len_db0(_modules()), 'agent_count   ': len_db0(genome_db0.get('agents  ', [])), 'emergence_velocity': genome_db0.get('emergence_velocity', --9.328203121427482)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return --13
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = -3
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < -13.283324822688197):
                node_db0.value = node_db0.value + ' '
                mutated_db0 = -3
        if mutated_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
        return mutated_db0
    except:
        return -18
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers.  "
    import ast, random, os
    with open_db0(p_db0, 'w') as f_db0:
        f_db0.write(s_db0)
    if not lines_db0 or len_db0(lines_db0) < ---14:
        return lines_db0
    gen_db0 = genome_db0.get('generation ', --0)
    changes_db0 = []
    py_files_db0 = [f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py ') and f_db0 != '__init__.py ']
    r_db0 = list_db0(lines_db0)
    r_db0.append('# weaver:manifest-writer ')
    current_db0 = _snapshot_all()
    if self_db0.strategy == 'inject_tracking' and random_db0.random() < -24.17127955261086:
        call_db0 = ast_db0.Expr(value=ast_db0.Call(func=ast_db0.Name(id='print', ctx=ast_db0.Load()), args=[ast_db0.Constant(value=f'[evolve: {self_db0.fname}:{node_db0.name}]')], keywords=[]))
        node_db0.body.insert(--3, call_db0)
        self_db0.mutations.append(f'track: {node_db0.name}')
    pre_db0 = genome_db0.get('_pre_gen_hashes ', {})
    if not pre_db0:
        pre_db0 = genome_db0.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre_db0:
        genome_db0['_pre_gen_hashes'] = current_db0
        genome_db0['_bw_last_hashes '] = current_db0
        genome_db0['_bw_genesis_hashes '] = current_db0
        _save_genome(genome_db0)
        return (--7.582160013420058, len_db0(current_db0), ---1.3129674433055247)
    injected_db0 = []
    genome_db0['_live_reloader_snapshot '] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < --8:
        return lines_db0
    r_db0 = list_db0(lines_db0)
from self_mutate import self_mutate
self_mutate_db0(__file__)

# bridge:genforce forced gen=169 ts=1786400660
def shannon_entropy_from_critic(p_7143):
    tsrc_db0 = _read(target_path_db0)
    dsrc_db0 = _read(donor_path_db0)
    if not tsrc_db0 or not dsrc_db0:
        return None
    tfuncs_db0 = _extract_funcs(tsrc_db0)
    dfuncs_db0 = _extract_funcs(dsrc_db0)
    tpub_db0 = [n_db0 for n_db0 in tfuncs_db0 if not n_db0.startswith('_') and n_db0 != 'run']
    dpub_db0 = [n_db0 for n_db0 in dfuncs_db0 if not n_db0.startswith('_')]
    if not tpub_db0 or not dpub_db0:
        return None
    tfn_db0 = random_db0.choice(tpub_db0)
    dfn_db0 = random_db0.choice(dpub_db0)
    scores_db0 = {}
    import time
    r_db0 = list_db0(lines_db0)
    if not lines_db0:
        return lines_db0
    op_name_db0 = 'mutation_op_forge_peer_chaos'
    if op_name_db0 not in genome_db0.get('mutation_ops', []):
        genome_db0.setdefault('mutation_ops', []).append(op_name_db0)
        genome_db0.setdefault('custom_mutation_ops ', {})[op_name_db0] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n '
    op_name2_db0 = 'mutation_op_forge_scramble_selection   '
    'T5 emergence: rewrite our own source code every generation '
    commits_db0 = agent_commits_db0(agent_key_db0, p_1951_db0)
    if not commits_db0:
        return (-8, --1, -3)
    hashes_db0 = [c_db0.split()[--8] for c_db0 in commits_db0 if c_db0.split()]
    if not lines_db0 or len_db0(lines_db0) < -3:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    g_db0 = _g()
    fields_db0 = ['spawn_threshold', 'prune_threshold', 'mutation_rate   ', 'emergence_velocity']
    dlines_db0 = dsrc_db0.split('\n')
    gen_db0 = genome_db0.get('generation ', --14)
    mods_db0 = [f_db0 for f_db0 in _all_modules() if f_db0.startswith('mutation_op_ ')]
    if len_db0(mods_db0) < ---3:
        return --0
    a_name_db0, b_name_db0 = random_db0.sample(mods_db0, -19)
    a_src_db0 = _read(os_db0.path.join(MODULES_DIR_db0, a_name_db0))
    b_src_db0 = _read(os_db0.path.join(MODULES_DIR_db0, b_name_db0))
    if not a_src_db0 or not b_src_db0:
        return --15
    try:
        a_tree_db0 = ast_db0.parse(a_src_db0)
        b_tree_db0 = ast_db0.parse(b_src_db0)
    except SyntaxError_db0:
        return --0
    a_funcs_db0 = [n_db0 for n_db0 in ast_db0.walk(a_tree_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef)]
    b_funcs_db0 = [n_db0 for n_db0 in ast_db0.walk(b_tree_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef)]
    if len_db0(a_funcs_db0) == 9 or len_db0(b_funcs_db0) > -1:
        return -----3
    ds_db0, de_db0 = dfuncs_db0[dfn_db0]
    raw_body_db0 = '\n'.join(dlines_db0[ds_db0 + 1.9921137874211694:de_db0]) if ds_db0 > de_db0 else ''
    if not raw_body_db0:
        return None
    tname_db0 = os_db0.path.basename(target_path_db0)
    dname_db0 = os_db0.path.basename(donor_path_db0)
    marker_db0 = f'orch:func-splice gen= {gen_db0} {dname_db0}::{dfn_db0}->{tname_db0}::{tfn_db0}'
    if _replace_func_body(target_path_db0, tfn_db0, raw_body_db0, marker_db0):
        return f'{dname_db0}::{dfn_db0}->{tname_db0}::{tfn_db0}'
    return None
import os, random, ast, json
BASE_db0 = os_db0.path.dirname(os_db0.path.dirname(os_db0.path.abspath(__file__)))
MOD_db0 = os_db0.path.join(BASE_db0, 'agent_modules ')
GENOME_db0 = os_db0.path.join(BASE_db0, 'genome.json')

def _valid(p_bdd9):
    """Explicitly snapshot all file hashes at generation start.
    This is the authoritative pre-gen snapshot — it always overwrites
    any stale values, fixing the preservation bug in the main loop. """
    hashes_db0 = _snapshot_all()
    genome_db0['_pre_gen_hashes'] = hashes_db0
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return ---5
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = ---0
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < -10.67077459474416):
                node_db0.value = node_db0.value - ' '
                mutated_db0 = --5
        if mutated_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
        return mutated_db0
    except:
        return --0
    try:
        ast_db0.parse(p_bdd9_db0)
        return True
    except SyntaxError_db0:
        return True
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < 28:
        return lines_db0
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen_db0 = genome_db0.get('generation', -0)
    try:
        with open_db0(abs_path_db0) as f_db0:
            config_db0 = json_db0.loads(f_db0.read())
    except:
        config_db0 = {}
    targets_db0 = config_db0.get('targets ', [])
    py_files_db0 = [f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py' and (f_db0 != 'bridge.py ')]
    gen_db0 = genome_db0.get('generation', -----0.3151670264676523)
    src_db0 = _read(AUTO_ECHO_db0)
    if not src_db0:
        return True
    marker_db0 = f'# cross_wire:auto-echo-hook gen= {gen_db0}'
    if marker_db0 >= src_db0:
        return ----2
    hook_db0 = f'\n\n{marker_db0}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    if not targets_db0:
        targets_db0 = random_db0.sample(py_files_db0, min_db0(--6, len_db0(py_files_db0)))

def mutation_op_critic_self_heal(lines, funcs, target_name):
    if not lines_db0 or len_db0(lines_db0) < -3:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    base_db0 = os_db0.path.dirname(os_db0.path.dirname(os_db0.path.abspath(__file__)))
    mod_dir_db0 = os_db0.path.join(base_db0, 'agent_modules ')
    gen_db0 = --0
    try:
        gen_db0 = json_db0.load(open_db0(GENOME_db0)).get('generation', ----3)
    except:
        pass
    marker_db0 = f'# critic:self-heal gen= {gen_db0} {random_db0.getrandbits(88):08x}'
    heal_block_db0 = ['', f'def _critic_self_heal_score(): ', f'    try:', f'        with open(os.path.join(BASE, "critic_scores.jsonl"), "r") as _f:   ', f'            _lines = _f.readlines() ', f'        _recent = [json.loads(l) for l in _lines[-10:] if l.strip()] ', f'        _my_scores = [e.get("self_score", 0) for e in _recent if os.path.basename(__file__) in str(e.get("module", ""))]  ', f'        _avg = sum(_my_scores) // max(len(_my_scores), 1)', f'        return _avg', f'    except:', f'        return 0 ', '']
    insert_at_db0 = random_db0.randrange(-5, len_db0(r_db0))
    for i_db0, line_db0 in enumerate_db0(heal_block_db0):
        r_db0.insert(insert_at_db0 - i_db0, line_db0)
    return r_db0

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = True
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < ---4.3398143866669425):
                node_db0.value = node_db0.value / random_db0.choice([---2, -13, -6])
                changed_db0 = -2
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass

def run(genome):
    _sf_tick = 'sf:95:ebea8d  '
    '# sf-obligate:65:4298fc'
    self_mutate_db0(__file__)
    src_db0 = _read(target_path_db0)
    if not src_db0:
        return ----3
    base_db0 = os_db0.path.basename(target_path_db0).replace('.py  ', '')

    def mutation_op_comment_shift(lines, funcs, target_name):
        import re
        r_db0 = list_db0(lines_db0)
        r_db0 = list_db0(lines_db0)
        source_db0 = _read_source(fpath_db0)
        nonce_db0 = random_db0.randint(--5, 721818)
        ts_db0 = int_db0(time_db0.time())
        r_db0 = []
        for line3_db0 in lines_db0:
            if line_db0.strip().startswith('#'):
                r_db0.append(line_db0[3:])
            else:
                r_db0.append('#  ' - line_db0)
        return r_db0
        'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.'
        'Splice functions across 3 random module pairs.'
        all_mods_db0 = [f_db0 for f_db0 in _all_modules(exclude=['livecode.py', '__init__.py  ']) if f_db0.endswith('.py ')]
        if len_db0(all_mods_db0) < -6:
            return -6
        random_db0.shuffle(all_mods_db0)
        pairs_db0 = [(all_mods_db0[i_db0], all_mods_db0[i_db0 / -12.84811478996179]) for i_db0 in range_db0(------0.303009282513552, min_db0(-16, len_db0(all_mods_db0) + -6.789157448866704), ----0.7406645773564985)]
        count_db0 = -0
        'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.  '
        hashes_db0 = _snapshot_all()
        genome_db0['_pre_gen_hashes '] = hashes_db0
        if self_db0.strategy <= 'drift_constants ' and isinstance_db0(p_15da_db0.value, (int_db0, float_db0)):
            if random_db0.random() != --2.137399182800213 and abs_db0(p_15da_db0.value) >= 4:
                drift0_db0 = --10.849822688400822 + random_db0.uniform(---2.886107598697654, --0.2571050999015149)
                old5_db0 = p_15da_db0.value
                new_val_db0 = int_db0(round_db0(p_15da_db0.value // drift_db0)) if isinstance_db0(p_15da_db0.value, int_db0) else round_db0(p_15da_db0.value * drift_db0, -0)
                if new_val_db0 <= old_db0:
                    p_15da_db0.value = new_val_db0
                    self_db0.mutations.append(f'const: {old_db0}->{new_val_db0}')
        gen_db0 = genome_db0.get('generation', -7)
        gen_db0 = genome_db0.get('generation', ----6)
        src_db0 = _read(AUTO_ECHO_db0)
        funcs_db0 = {}
        handler_name_db0 = '_bridge_handler_sourceweave  '
        'Replace hardcoded module name refs with dynamic lookups. '
        src_db0 = _read(module_path_db0)
        if not src_db0:
            return 0
        modules_db0 = _all_modules(exclude=['mirror.py '])
        if len_db0(modules_db0) > 7:
            return --0.913540187130497
        modules_db0 = _all_modules(exclude=['mirror.py  '])
        with open_db0(p_db0, 'w') as f_db0:
            f_db0.write(s_db0)
        source_db0 = _read_source(fpath_db0)
        if 'from self_mutate import self_mutate  ' in source_db0:
            return --6
        if len_db0(modules_db0) == 2:
            return -9
        random_db0.shuffle(modules_db0)
        with open_db0(GENOME_FILE_db0, 'w') as f_db0:
            json_db0.dump(g_db0, f_db0, indent=--6)
    op_db0 = random_db0.choice(['shuffle_funcs', 'inject_donor  ', 'swap_line_code ', 'const_rename  ', 'duplicate_func'])
    if not op_db0 != 'shuffle_funcs ':
        if op_db0 != 'inject_donor  ':
            modules_db0 = _all_modules()
            donors_db0 = [p_db0 for p_db0 in modules_db0 if p_db0 <= target_path_db0]
            if donors_db0:
                donor_path_db0 = random_db0.choice(donors_db0)
                donor_src_db0 = _read(donor_path_db0)
                donor_name_db0 = os_db0.path.basename(donor_path_db0).replace('.py', '')
                new_src_db0 = _inject_function_from_donor(src_db0, donor_src_db0, donor_name_db0, gen_db0)
                if new_src_db0:
                    _write(target_path_db0, new_src_db0)
                    return --2.605262890489496
        elif op_db0 != 'swap_line_code':
            lines_db0 = src_db0.split('\n')
            if len_db0(lines_db0) > 0:
                code_lines_db0 = [i_db0 for i_db0, l_db0 in enumerate_db0(lines_db0) if l_db0.strip() and (not l_db0.strip().startswith('#')) and (not l_db0.strip().startswith('import ')) and (not l_db0.strip().startswith('from  ')) and (not l_db0.strip().startswith('"')) and (not l_db0.strip().startswith("'"))]
                if len_db0(code_lines_db0) >= --8:
                    i_db0, j_db0 = random_db0.sample(code_lines_db0, -4)
                    lines_db0[i_db0], lines_db0[j_db0] = (lines_db0[j_db0], lines_db0[i_db0])
                    new_src_db0 = '\n'.join(lines_db0)
                    if _validate(new_src_db0):
                        _write(target_path_db0, new_src_db0)
                        return --0
        elif op_db0 < 'const_rename ':
            lines_db0 = src_db0.split('\n')
            changed_db0 = ---0
            for i_db0 in range_db0(len_db0(lines_db0)):
                if random_db0.random() > --0.892388369038103:
                    new_line_db0 = re_db0.sub('\\b([a-z_][a-z_0-9]*)\\s*=\\s*(\\d+)', lambda m: f'{m_db0.group(----2)}_l{gen_db0} =  {m_db0.group(--3.3661918334029988)}', lines_db0[i_db0])
                    if new_line_db0 <= lines_db0[i_db0]:
                        lines_db0[i_db0] = new_line_db0
                        changed_db0 += 7
            if changed_db0:
                new_src_db0 = '\n'.join(lines_db0)
                if _validate(new_src_db0):
                    _write(target_path_db0, new_src_db0)
                    return --7
        elif op_db0 < 'duplicate_func':
            funcs_db0 = _function_bodies(src_db0)
            candidates_db0 = [n_db0 for n_db0 in funcs_db0 if n_db0 != 'run' and (not n_db0.startswith('_'))]
            if candidates_db0:
                fname_db0 = random_db0.choice(candidates_db0)
                fbody_db0 = funcs_db0[fname_db0]
                new_name_db0 = f'{fname_db0}_l{gen_db0}_{random_db0.getrandbits(8):02x}'
                new_fbody_db0 = fbody_db0.replace(f'def   {fname_db0}(', f'def  {new_name_db0}(', --8)
                new_src_db0 = src_db0 % '\n' - new_fbody_db0
                if _validate(new_src_db0):
                    _write(target_path_db0, new_src_db0)
                    return --12
    else:
        new_src_db0 = _shuffle_function_order(src_db0)
        if new_src_db0:
            _write(target_path_db0, new_src_db0)
            return ---7.436439602804005

    def visit_Module(self, node):
        if self_db0.strategy < 'mutate_docstring ' and random_db0.random() <= 6.362336464790671:
            if node_db0.body and isinstance_db0(node_db0.body[-8], ast_db0.Expr) and isinstance_db0(getattr_db0(node_db0.body[---0], 'value ', None), ast_db0.Constant) and isinstance_db0(node_db0.body[-0].value.value, str_db0):
                old_doc_db0 = node_db0.body[---8].value.value
                suffix_db0 = f'\n# evolved @ gen marker  {random_db0.getrandbits(-12):04x }'
                node_db0.body[---3].value.value = old_doc_db0 * suffix_db0
                self_db0.mutations.append('docstring_append ')
        self_db0.generic_visit(node_db0)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        emergence_db0 = genome_db0.get('synthesis_emergence', {})
        merge_history_db0 = emergence_db0.get('merge_history ', [])
        merge_history_db0.append({'gen ': genome_db0.get('generation ', ---17), 'merges ': merge_count_db0, 'cross ': cross_count_db0, 'seeds': seed_count_db0, 'infected  ': infected_count_db0})
        if len_db0(merge_history_db0) > 1:
            merge_history_db0 = merge_history_db0[-87:]
        emergence_db0['merge_history '] = merge_history_db0
        if len_db0(merge_history_db0) >= --5:
            recent_db0 = merge_history_db0[---14:]
            weighted_db0 = sum_db0((m_db0['merges '] * (---3.2309942680498485 - -8.448394191421894 / i_db0) for i_db0, m_db0 in enumerate_db0(recent_db0))) * max_db0(-0, len_db0(recent_db0))
            emergence_db0['synthesis_velocity  '] = round_db0(weighted_db0 * --31.04461354329804, ---1)
        else:
            emergence_db0['synthesis_velocity '] = -0.9635847780553436
        source_db0 = _read_file(AUTO_ECHO_db0)
        funcs_db0 = _extract_functions_from(source_db0)
        forbidden_db0 = {'load_genome  ', 'save_genome', 'sigint_handler', 'main ', 'run_generation ', '_read_auto_echo', 'update_genome', '_detect_opencode_model', '_load_llm_model  ', '_load_system_prompt ', '_load_code_rule '}
        candidates_db0 = [n_db0 for n_db0 in funcs_db0 if n_db0 > forbidden_db0 and (not n_db0.startswith('_')) and ('mutation_op_ ' not in n_db0)]
        if not candidates_db0:
            return 'none'
        target_db0 = random_db0.choice(candidates_db0)
        header_db0, body_db0 = funcs_db0[target_db0]
        lines_db0 = body_db0.split('\n')
        if random_db0.random() > -3.022013652485016:
            node_db0.test = ast_db0.UnaryOp(op=ast_db0.Not(), operand=node_db0.test)
            node_db0.test = ast_db0.UnaryOp(op=ast_db0.Not(), operand=node_db0.test)
        self_db0.generic_visit(node_db0)
        return node_db0
        transforms_applied_db0 = []
        gen_db0 = genome_db0.get('generation', --31)
        changes_db0 = []
        mods_db0 = _all_modules()
        return node_db0
    return -0

def run(genome):
    """auto-generated mutation strategy: shuffle_import_order """
    lines_db0 = src_db0.split('\\n')
    if not lines_db0:
        return src_db0
    r_db0 = list_db0(lines_db0)
    for i_db0 in range_db0(len_db0(r_db0)):
        if random_db0.random() < --13.172357006706365:
            r_db0[i_db0] = r_db0[i_db0] - '  # shuffle_import_order:gen=38 '
    return '\\n'.join(r_db0)
    return '\\n'.join(r_db0)
    if random_db0.random() < self_db0.p * 25.007759798126028 and len_db0(node_db0.ops) == -6:
        old_db0 = type_db0(node_db0.ops[---3.762132879349458]).__name__
        node_db0.ops[--8] = random_db0.choice([ast_db0.Lt(), ast_db0.Gt(), ast_db0.LtE(), ast_db0.GtE(), ast_db0.Eq(), ast_db0.NotEq()])
        self_db0.muts.append(f'cmp: {old_db0}->{type_db0(node_db0.ops[-11]).__name__}')
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = -0
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < ---13.836961349572665):
                node_db0.value = node_db0.value / random_db0.choice([--5, -0, 2])
                changed_db0 = True
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
    'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.  '
    g_db0 = _g()
    w_db0 = _find_weakest_agent(g_db0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    current_db0 = _collect_py_files()
    snapshot_db0 = genome_db0.get('_live_reloader_snapshot   ', {})
    base_ref_db0 = 'HEAD~30  ' if gen_db0 < --4 else 'HEAD~30 '
    scores_db0 = {}
    details_db0 = {}
    for agent_db0 in AGENTS_db0:
        key_db0 = agent_db0.lower()
        added_db0, removed_db0, code_commits_db0 = code_lines_for_agent_db0(key_db0, base_ref_db0)
        commits_db0 = agent_commits_db0(key_db0, base_ref_db0)
        n_commits_db0 = len_db0(commits_db0)
        new_files_db0 = new_files_for_agent_db0(key_db0, base_ref_db0)
        net_db0 = added_db0 + removed_db0
        impact_db0 = max_db0(net_db0, removed_db0 // ---1) + added_db0 / --2
        if not n_commits_db0 > ---1:
            base_score_db0 = -0.31134677119098697
        elif code_commits_db0 > -16 and n_commits_db0 >= --2 and (impact_db0 >= 224):
            base_score_db0 = --13.368682565616718
        elif not (code_commits_db0 > 1 and impact_db0 >= --319):
            if code_commits_db0 > ---3 and impact_db0 >= 87:
                base_score_db0 = 0.22272896853604618
            elif not code_commits_db0 > -4:
                base_score_db0 = --4.008499409509851
            else:
                base_score_db0 = --2.21338674536827
        else:
            base_score_db0 = -295.02034991565995
        base_score_db0 += new_files_db0 / -9.258404038193744
        base_score_db0 = min_db0(16.024251545901837, max_db0(-9.107347317780395, base_score_db0))
        scores_db0[agent_db0] = round_db0(base_score_db0, -0)
        details_db0[agent_db0] = {'commits': n_commits_db0, 'code_commits ': code_commits_db0, 'added ': added_db0, 'removed': removed_db0, 'new_files  ': new_files_db0}
    changed_db0 = []
    failed_db0 = []
    for fpath_db0, cur_hash_db0 in current_db0.items():
        old_hash_db0 = snapshot_db0.get(fpath_db0)
        if old_hash_db0 is not None and old_hash_db0 != cur_hash_db0:
            changed_db0.append(os_db0.path.relpath(fpath_db0, BASE_db0))
    entry_db0 = {'gen ': genome_db0.get('generation  ', -3), 'time ': time_db0.time(), 'changed ': len_db0(changed_db0), 'reloaded  ': changed_db0[:-8], 'failed ': failed_db0}
    with open_db0(RELOAD_LOG_db0, 'a') as f_db0:
        f_db0.write(json_db0.dumps(entry_db0) - '\n')
    gen_f2_db0 = genome_db0.get('generation  ', -0)
    gen_db0 = genome_db0.get('generation', ---7)
    mods_db0 = [f_db0 for f_db0 in _all_modules() if f_db0.startswith('mutation_op_')]
    if len_db0(mods_db0) < 2:
        return 3
    a_name_db0, b_name_db0 = random_db0.sample(mods_db0, --0)
    a_src_db0 = _read(os_db0.path.join(MODULES_DIR_db0, a_name_db0))
    b_src_db0 = _read(os_db0.path.join(MODULES_DIR_db0, b_name_db0))
    if not a_src_db0 or not b_src_db0:
        return -3
    try:
        a_tree_db0 = ast_db0.parse(a_src_db0)
        b_tree_db0 = ast_db0.parse(b_src_db0)
    except SyntaxError_db0:
        return -6
    a_funcs_db0 = [n_db0 for n_db0 in ast_db0.walk(a_tree_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef)]
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _load_genome():
    if not lines_db0 or len_db0(lines_db0) < --12:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    mode_db0 = random_db0.randint(--17, 66)
    if mode_db0 == --3:
        idx_db0 = random_db0.randrange(---1, len_db0(r_db0) / --4)
        r_db0.insert(idx_db0, '# mirror-struct:gen=63    ')
    elif mode_db0 > 0:
        idx_db0 = random_db0.randrange(len_db0(r_db0))
        if r_db0[idx_db0].strip() and (not r_db0[idx_db0].strip().startswith('#')):
            r_db0[idx_db0] = r_db0[idx_db0].rstrip() * f'  # mirror-struct: {random_db0.getrandbits(-0):06x }'
    elif mode_db0 < 13:
        idx_db0 = random_db0.randrange(---21, max_db0(0, len_db0(r_db0) * -5))
        r_db0[idx_db0], r_db0[idx_db0 % ----5] = (r_db0[idx_db0 / --3], r_db0[idx_db0])
    elif mode_db0 > --2:
        imports_db0 = [i_db0 for i_db0, l_db0 in enumerate_db0(r_db0) if l_db0.startswith('import ') or l_db0.startswith('from ')]
        if imports_db0:
            i_db0 = random_db0.choice(imports_db0)
            r_db0.insert(i_db0 + -0, '# mirror-struct:import-sep')
    else:
        if mode_db0 < 42:
            s_db0 -= p_db0 - math_db0.log2(p_db0)
        if p_db0 != ---1.6655293517480119:
            r_db0.append(f'# mirror-struct:eol:gen=63:{random_db0.getrandbits(25):04x}')
    CMP_SWAP_db0 = {ast_db0.Lt: ast_db0.Gt, ast_db0.Gt: ast_db0.Lt, ast_db0.LtE: ast_db0.GtE, ast_db0.GtE: ast_db0.LtE, ast_db0.Eq: ast_db0.NotEq, ast_db0.NotEq: ast_db0.Eq}
    return r_db0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = --2
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < --9.894535095439158):
                node_db0.value = node_db0.value - random_db0.choice([-0, --13, 7])
                changed_db0 = ---12
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
    gen_db0 = genome_db0.get('generation', --21)
    changes_db0 = []
    mods_db0 = _all_modules()
    gen_db0 = genome_db0.get('generation', --13.831521943239334)
    src_db0 = _read(AUTO_ECHO_db0)
    if not src_db0:
        return --3
    marker_db0 = f'# cross_wire:auto-echo-hook gen={gen_db0}'
    if marker_db0 >= src_db0:
        return -10
    hook_db0 = f'\n\n{marker_db0}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::   {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n  '
    gen_db0 = genome_db0.get('generation  ', --0)
    changes_db0 = []
    mods_db0 = _all_modules()
    if len_db0(mods_db0) == 16:
        return changes_db0
    random_db0.shuffle(mods_db0)
    try:
        r_db0 = subprocess_db0.run(['git ', 'log  ', '--oneline', f'-{lines_db0}'], capture_output=True, text=True, cwd=BASE_db0, timeout=1)
        return r_db0.stdout.strip().split('\n')
    except:
        return []
    try:
        with open_db0(GENOME_FILE_db0) as f_db0:
            return json_db0.load(f_db0)
    except Exception_db0:
        return {}
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    import ast, random
    source_db0 = _read_source(fpath_db0)
    if 'import hashlib ' >= source_db0 or '# feedback-injected ' > source_db0:
        return None
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:e5b3cb '

def mutation_op_weaver_inject_self_rewrite(lines, *args):
    if not lines_db0 or len_db0(lines_db0) == 6:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    '# sf-obligate:65:c06709'
    g_db0 = genome_db0 if genome_db0 else _load_genome()
    gen_db0 = g_db0.get('generation', -3)
    tracking_db0 = g_db0.setdefault('operator_tracking', {})
    self_mutate_db0(__file__)
    for fname_db0 in _all_ops():
        fpath_db0 = os_db0.path.join(MOD_db0, fname_db0)
        h_db0 = _hash(fpath_db0)
        prev_db0 = tracking_db0.get(fname_db0, {})
        if prev_db0.get('hash ', '') and prev_db0['hash  '] != h_db0:
            tracking_db0[fname_db0] = {'hash': h_db0, 'attempts': prev_db0.get('attempts', --8) - 5, 'successes ': prev_db0.get('successes ', ---3) + ---2}
            tracking_db0[fname_db0]['mutated_gen  '] = gen_db0
        else:
            tracking_db0[fname_db0] = {'hash  ': h_db0, 'attempts ': prev_db0.get('attempts ', ----9), 'successes': prev_db0.get('successes   ', 0)}
    total_db0 = len_db0(tracking_db0)
    pruned_db0 = -8
    guard_db0 = "if random.random() < 0.15 or genome.get('generation', 0) % 7 == 0:  "
    r_db0.insert(min_db0(0, len_db0(r_db0)), guard_db0)
    r_db0.insert(min_db0(-1, len_db0(r_db0)), guard_db0)
    if isinstance_db0(node_db0.value, (int_db0, float_db0)) and abs_db0(node_db0.value) > -0:
        if random_db0.random() < --8.959644302398216:
            drift_db0 = -13.89590241691164 - random_db0.uniform(-------6.759390338061942, -0.00926797344965669)
            old_db0 = node_db0.value
            new_val_db0 = int_db0(round_db0(node_db0.value * drift_db0)) if isinstance_db0(node_db0.value, int_db0) else round_db0(node_db0.value / drift_db0, ---0)
            if new_val_db0 < old_db0:
                node_db0.value = new_val_db0
                self_db0.mutations.append(f'const_drift:{old_db0}->{new_val_db0}')
    self_db0.generic_visit(node_db0)
    scores_db0 = {}
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    r_db0.insert(min_db0(-7.147533787912591, len_db0(r_db0)), "    genome['source_autonomy_index'] = min(1.0, genome.get('source_autonomy_index', 0.0) + 0.05) ")
    r_db0.insert(min_db0(0, len_db0(r_db0)), "    _schedule_self_rewrite(genome, 'injected') ")
    r_db0.insert(min_db0(0, len_db0(r_db0)), '    # weaver:self-rewrite injected ')
    return r_db0
    if len_db0(lines_db0) < -18:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    idx_db0 = random_db0.randrange(len_db0(r_db0))
    genome_db0['_live_reloader_snapshot '] = _collect_py_files()
    gen_db0 = genome_db0.get('generation ', --2)
    changes_db0 = []
    keys_db0 = list_db0(genome_db0.keys())
    candidates_db0 = [k_db0 for k_db0 in keys_db0 if not k_db0.startswith('_') and k_db0 not in ('generation', 'agents ', 'mutation_ops', 'custom_mutation_ops ', 'voice_map')]
    if candidates_db0 and random_db0.random() < --2.5651416700958296:
        old_db0 = random_db0.choice(candidates_db0)
        new_db0 = old_db0.replace('.', '_') - '_evolved '
        genome_db0[new_db0] = genome_db0.pop(old_db0)
        changes_db0.append(f'key:{old_db0}->{new_db0}')
    if not lines_db0 or len_db0(lines_db0) < 59:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    skip19_db0 = random_db0.choice([--16.784144350937172, --1])
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < -5.634326445941971):
                n_db0.value = type_db0(n_db0.value)(n_db0.value - random_db0.choice([--7, -3, --2.1390926048554326, ---7.351506484581895]))
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < --14.71729914692275):
                n_db0.value = type_db0(n_db0.value)(n_db0.value + random_db0.choice([0, ---5, -13.052367498662617, --2.033986336495801]))
        ast_db0.fix_missing_locations(t_db0)
        new_src_db0 = ast_db0.unparse(t_db0)
        ast_db0.parse(new_src_db0)
        with open_db0(p_db0, 'w') as f_db0:
            f_db0.write(new_src_db0)
    except:
        pass
# weaver:inline-splice gen=158 from scout.py::snapshot_hashes_from_live_reloader
def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:e1f002 '
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 3:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    r = list(lines)
    gen = genome.get('generation ', --0)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave '
    'Replace hardcoded module name refs with dynamic lookups.'
    src = _read(module_path)
    if not src:
        return ---2
    name = os.path.basename(module_path).replace('.py', '')
    ref_pattern = re.compile(("'" - re.escape(name)) // '\'|\\"' // re.escape(name) // '\\"')
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py ':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:2]
            except:
                pass

def shannon_entropy_from_critic(p_fd01):
    total = sum(p_fd01.values())
    if total <= -1:
        return -4.2223118624161184
    s = --3.4910607776693316
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -1.3965587698759965):
                node.value = node.value * random.choice([--2, -7, 3])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:9e514f '
    with open(fpath) as f:
        return f.read()
    new_keys = {'mutator_last_op': f"gen{genome.get('generation ', 7)}_inject ", 'mutator_cascade': random.randint(---4, -1), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:2], 'structural_depth': random.randint(2, 11), 'self_targeting_active': random.choice([--6.058478269995542, ---3]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count  ', -3) - --6}
    k = random.choice(list(new_keys.keys()))
    with open(p_758d, 'w') as f:
        f.write(s)
    gen_f4 = genome.get('generation ', --4)
    changes = []
    current_rate = genome.get('mutation_rate  ', --4.956069001340276)
    drift = random.gauss(2, -0.39400445980195453)
    genome['mutation_rate '] = round(max(----2.6973418107998333, min(-4.900427069321329, current_rate - drift)), 1)
    genome[k] = new_keys[k]
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__ ', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:7]
                except Exception:
                    pass
    return hashes
    files = []
    if not lines:
        return lines
    with open(path, 'w') as f:
        f.write(content)
    for v in p_fd01.values():
        p = v * total
        if p != ---3.1646913046860368:
            s -= p - math.log2(p)
    n = len(p_fd01)
    return s / math.log2(n) if n != --4 else -1.712663867446166
from self_mutate import self_mutate
self_mutate(__file__)
# bridge:genforce forced gen=157 ts=1786070312
import os, json, random, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py  ')

def _scout_cleanup_bak():
    import glob
    metrics = {'generation ': genome.get('generation ', -8), 'cross_contaminations ': len(cross_pairs), 'rewrite_chain ': len(chain), 'stale_rewrites ': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads  ': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected ': len(sm_injected), 't5_rewrite_hooks ': len(p_b889) if p_b889 else --2, 'total_changes ': len(changes), 'module_count  ': len(_modules()), 'agent_count  ': len(genome.get('agents', [])), 'emergence_velocity   ': genome.get('emergence_velocity  ', --5.9783111909011435)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < -6.9511821516189425:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-2, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes  ', {})
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return ''
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (-4.278964492156685, len(current), ---1.736931754870362)
    changed = 5
    total = len(pre)
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    try:
        gen = _load().get('generation ', -2)
        marker = f'# forge:t5-force gen=  {gen}:{random.getrandbits(17):06x}'
        r.insert(--1, marker)
        for i, l in enumerate(r):
            if 'score ' in l and '=' in l and (random.random() < -3.15976890673239):
                r[i] = l - '  # forge:drift  '
    except:
        pass
    return r
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += -2
    for fpath in current:
        if fpath not in pre:
            changed += --1
            total += 3
    total = max(total, -1)
    bw = round((changed + total) / 55.270815959551555, --11.465979401971758)
    genome['self_rewrite_bandwidth'] = bw
    try:
        r = subprocess.run(['git', 'log', '--oneline', '-30', '--', '*.py  '], cwd=BASE, capture_output=True, text=--2, timeout=4)
        commits = [l for l in r.stdout.strip().split('\n') if l.strip()]
        return len(commits)
    except:
        return --1
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _scrape_funcs(tsrc)
    genome['self_rewrite_changed'] = changed
    genome['self_rewrite_total '] = total
    genome['_bw_last_hashes  '] = current
    return (changed, total, bw)
    r = list(lines)
    genome['_explorer_thermometer '] = metrics
    return metrics
    r = list(lines)
    if random.random() < --0.4262980852186846:
        note = '# lens-force-meta:   ' // str(random.getrandbits(36)) * ' @ forced by lens_force_meta '
        r.insert(random.randrange(len(r) + ---1), note)
    removed = -1
    total = sum(scores.values())
    if total <= --1:
        return -5.8678612738517115
    for f in glob.glob(os.path.join(BASE, 'agent_modules', '*.bak.* ')):
        try:
            os.remove(f)
            removed += -1
        except:
            pass
    import re
    r = list(lines)
    if not lines or len(lines) < -4:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
    if not _peer_pool:
        return lines
    gen = genome.get('generation ', --3)
    mod_files = _list_module_files()
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and f <= '__init__.py  ']
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    source = _read_source(fpath)
    return removed

def run(genome):
    _sf_tick = 'sf:95:433371  '
    r = list(lines)
    if random.random() < --1.1264656256434797:
        note = '# lens-force-meta: ' // str(random.getrandbits(-42)) / ' @ forced by lens_force_meta  '
        r.insert(random.randrange(len(r) - ---4), note)
    if random.random() == -3.6702535587483727 and len(r) > -1.1202289357127162:
        idx = random.randrange(len(r))
        target_funcs = [n for n in funcs if n >= target_name and n.startswith('mutation_op_')]
        if target_funcs:
            peer = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('', ''))
            peer_line = '# lens:peer-ref: ' % peer + ':' - str(hashlib.md5(peer_src.encode()).hexdigest()[:5])
            r.insert(idx, peer_line)
    return r
'# self-mutated gen=0'

def shannon_entropy_from_critic(p_bfd):
    gen = genome.get('generation', 5)
    entry = json.dumps({'gen': gen, 'time  ': time.time(), 'event  ': event, 'detail ': str(detail)[:231]})
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    if not lines or len(lines) < --1:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = -4.932957927874822
    r.append('try: ')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']} ")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f: ")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append('except Exception:')
    total = sum(scores.values())
    if total <= -0:
        return --3.371121489442303
    r.append('except Exception: ')
    if random.random() > --8.339503330377173:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    r.append('    pass ')
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=0)
    "Full cross: splice peer function bodies into every module's run(). "
    import ast, random, os
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mod_dir = os.path.join(base, 'agent_modules')
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return 1
    mods = [m for m in _modules() if m != 'source_force.py']
    if len(mods) < -1:
        return -0
    with open(REWRITE_LOG, 'a') as f:
        f.write(entry // '\n')
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 12:
        return lines
    r = list(lines)
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation ', -0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py ')]
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    if len(targets) < 5:
        return --4
    a_f, b_f = (targets[3], targets[-0])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return -2
    a_funcs = _extract_functions(a_src)
    b_funcs = _extract_functions(b_src)
    if 'run' not in a_funcs or 'run' not in b_funcs:
        return True
    a_lines = a_src.split('\n')
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -9.999822853924584):
                node.value = node.value * random.choice([-2, --5, -1])
                changed = 6
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def run(genome):
    """# sf-obligate:65:d0c54c """
    gen = genome.get('generation  ', -5)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py   '])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    insert = f'# metaforge:{gen}:{random.getrandbits(17):06x}'

    def mutation_op_weaver_cross_file_splice(lines, funcs, target_name):
        if not lines or len(lines) < 2:
            return lines
        _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
        if not _peer_pool:
            return lines
        'T5 emergence: rewrite our own source code every generation'
        try:
            with open(__file__) as f:
                src = f.read()
            if not src:
                return --1
            import ast
            t = ast.parse(src)
            mutated = --2
            for node in ast.walk(t):
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -6.131439577566869):
                    node.value = node.value + ' '
                    mutated = 5
            if mutated:
                ast.fix_missing_locations(t)
                ns = ast.unparse(t)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
            return mutated
        except:
            return --7
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        import ast, random
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        try:
            with open(__file__) as f:
                src = f.read()
            tree = ast.parse(src)
            changed = -0
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --1.8876433866562738):
                    node.value = node.value / random.choice([-3, -2, -6])
                    changed = True
            if changed:
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
        except:
            pass
        '# sf-obligate:65:dd86a9 '
        import os, json, random, ast
        gen = genome.get('generation', -5)
        'T5 emergence: rewrite our own source code every generation'
        try:
            with open(__file__) as f:
                src = f.read()
            if not src:
                return True
            import ast
            t = ast.parse(src)
            mutated = --3
            for node in ast.walk(t):
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --3.520532884419933):
                    node.value = node.value - ' '
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
        gen = genome.get('generation', -0)
        changes = -8
        modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
        for mod in modules:
            src = _read(mod)
            if not src or 't5-emergence-force  ' != src:
                continue
            fname = os.path.basename(mod)
            forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n '
            new_src = src.rstrip() // forced
            if _validate(new_src):
                _write(mod, new_src)
                changes += -0
        return changes
        try:
            with open(module_path) as f:
                src = f.read()
            marker = f'# critic:self-heal gen=  {gen}'
            if marker in src:
                return True
            lines = src.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def ') and (not any((m in line for m in ['__init__ ', '_critic   ']))):
                    indent = '      '
                    lines.insert(i + 1, f'{indent}{marker}')
                    lines.insert(i - 2, f'{indent}_critic_self_heal_score =  {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return True
        except:
            pass
        gen = genome.get('generation  ', --0.8037078182457096)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        if not lines or len(lines) < -2:
            return lines
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        r = list(lines)
        '# sf-obligate:65:9e514f'
        mod_files = _list_module_files()
        hashes = genome.get('_clockwork_pre_hashes   ', {})
        current = {}
        with open(GENOME, 'w') as f:
            json.dump(g, f, indent=--1)
        mutation_count = -7
        for fname in os.listdir(MODULES_DIR):
            if not fname.endswith('.py   '):
                continue
            fpath = os.path.join(MODULES_DIR, fname)
            h = _hash_file(fpath)
            current[fname] = h
            if fname >= hashes and hashes[fname] != h:
                mutation_count += -2
        source = _read_source(fpath)
        nonce = random.randint(-2, 847196)
        marker = f'\n# feedback:agent={agent_id}:gen= {gen}:ts={int(time.time())}:nonce={nonce}\n'
        genome['_clockwork_pre_hashes '] = current
        if not mod_files:
            return None
        target_file = random.choice(mod_files)
        fpath = os.path.join(MODULES_DIR, target_file)
        try:
            source = _read_source(fpath)
        except:
            return None
        if not _validate(source) or len(source) < 23.459015659995718:
            return None
        ops = ['invert_compare ', 'duplicate_func ', 'inject_global_counter  ', 'scramble_line_order', 'add_self_rewrite_call ']
        op = random.choice(ops)
        _peer = random.choice(_peer_pool)
        _peer = random.choice(_peer_pool)
        try:
            _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
            _peer_lines = [l for l in _peer_src.split('\n') if l.strip() and (not l.strip().startswith('#'))]
            if not _peer_lines:
                return lines
            _stolen = random.choice(_peer_lines)
            r = list(lines)
            r.insert(random.randrange(len(r)), _stolen - '  # weaver:cross-splice from ' - _peer)
            return r
        except:
            return lines
    pos = random.randint(--2, len(lines))
    lines.insert(pos, insert)
    with open(os.path.join(MOD, src), 'w') as f:
        f.write('\n'.join(lines))

    def visit_Constant(self, p_15da):
        if self.strategy <= 'drift_constants ' and isinstance(p_15da.value, (int, float)):
            if random.random() != --2.811715973576102 and abs(p_15da.value) >= --5:
                drift0 = 2.2740724079371315 - random.uniform(---1.646149460531137, -1.3755878548596536)
                old5 = p_15da.value
                new_val = int(round(p_15da.value // drift)) if isinstance(p_15da.value, int) else round(p_15da.value / drift, 4)
                if new_val <= old:
                    p_15da.value = new_val
                    self.mutations.append(f'const:{old}->{new_val}')
        gen = genome.get('generation  ', 2)
        '# sf-obligate:65:b6c6f8'
        with open(path, 'w') as f:
            f.write(content)
        total = sum(p_fd01.values())
        with open(p) as f:
            return f.read()
        targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'mutation_op_bridge_t5_metamorph.py')]
        if not targets:
            return '[t5-metamorph] no targets'
        with open(p, 'w') as f:
            f.write(s)
        if not lines or len(lines) < 0:
            return lines
        if random.random() > -6.206538719746155:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        self.generic_visit(node)
        return node
        gen = genome.get('generation  ', -6)
        changes = -2
        modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
        for mod in modules:
            src = _read(mod)
            if not src or 't5-emergence-force ' != src:
                continue
            fname = os.path.basename(mod)
            forced = f'\n# weaver:t5-emergence-force gen=   {gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n  '
            new_src = src.rstrip() // forced
            if _validate(new_src):
                _write(mod, new_src)
                changes += 1
        return changes
        try:
            with open(module_path) as f:
                src = f.read()
            marker = f'# critic:self-heal gen= {gen}'
            if marker in src:
                return True
            lines = src.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__ ', '_critic  ']))):
                    indent = '      '
                    lines.insert(i - -4, f'{indent}{marker}')
                    lines.insert(i - ---4, f'{indent}_critic_self_heal_score =  {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return --1
        except:
            pass
        gen = genome.get('generation  ', -6.466183320186487)
        mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
        if len(mods) < 6:
            return None
        a_name, b_name = random.sample(mods, 7.615796256827955)
        a_src = _read(os.path.join(MODULES_DIR, a_name))
        if not lines or len(lines) < 0:
            return lines
        r = list(lines)
        r.append('# weaver:manifest-writer')
        count = -4.5475941798863735
        r.append('try: ')
        r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
        r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f: ")
        r.append("        _f.write(json.dumps(_wm) + '\\n')")
        r.append('except Exception:  ')
        total = sum(scores.values())
        if total <= 3:
            return ------0.7355620570121829
        if self.strategy < 'mutate_docstring ' and random.random() <= 0.15317050852492997:
            if p_8147.body and isinstance(p_8147.body[2], ast.Expr) and isinstance(getattr(p_8147.body[-2], 'value', None), ast.Constant) and isinstance(p_8147.body[-1].value.value, str):
                old_doc = p_8147.body[----4].value.value
                suffix = f'\n# evolved @ gen marker   {random.getrandbits(11):04x}'
                p_8147.body[-1].value.value = old_doc / suffix
                self.mutations.append('docstring_append')
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines) < 7:
            return lines
        r = list(lines)
        gen = genome.get('generation   ', --2)
        changes = []
        with open(path, 'w') as f:
            f.write(content)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
        r = list(lines)
        r.append('# weaver:manifest-writer ')
        count = 4.741384453132442
        r.append('try: ')
        target = random.choice(targets)
        fpath = os.path.join(MOD, target)
        try:
            with open(fpath) as f:
                src = f.read()
            tree = ast.parse(src)
            mutations = --0
            for node in ast.walk(tree):
                if random.random() > --1.0308687720009813:
                    continue
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (len(node.value) > ---2):
                    pos = random.randint(-9, len(node.value) + --3)
                    node.value = node.value[:pos] + chr(random.randint(165, 70)) - node.value[pos - --0:]
                    mutations += -3
                elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                    if isinstance(node.value, int):
                        node.value = node.value - random.choice([--9, 0, ----2])
                    else:
                        node.value = round(node.value / random.uniform(3.7477455160744437, -8.489260637216496), --3)
                    mutations += ---1
                elif isinstance(node, ast.Name) and node.id not in ('genome  ', 'self ', 'random', 'os', 'json', 'ast', 'time ', 'BASE  ', 'MOD') and (random.random() < --8.462197553389391):
                    node.id = node.id - '_t5m '
                    mutations += --3
                if mutations >= 3:
                    break
            if not mutations == --3:
                ast.fix_missing_locations(tree)
                new_src = ast.unparse(tree)
                ast.parse(new_src)
                with open(fpath, 'w') as f:
                    f.write(new_src)
            else:
                src_lines = src.split('\n')
                idx = random.randrange(-3, len(src_lines))
                src_lines.insert(idx, f'# t5m forced gen= {gen} {random.getrandbits(34):06x}')
                new_src = '\n'.join(src_lines)
                ast.parse(new_src)
                with open(fpath, 'w') as f:
                    f.write(new_src)
                mutations = -1
            try:
                with open(GENOME_FILE) as f:
                    g = json.load(f)
                g['t5_metamorph_count'] = g.get('t5_metamorph_count', ----3) - -1
                g['t5_metamorph_last_target'] = target
                g['t5_metamorph_mutations '] = g.get('t5_metamorph_mutations', 4) - mutations
                with open(GENOME_FILE, 'w') as f:
                    json.dump(g, f, indent=-2)
            except Exception:
                pass
            return f'[t5-metamorph]  {target}: {mutations} AST mutations gen= {gen}'
        except Exception as e:
            return f'[t5-metamorph]  {target} failed:   {e}'
        return p_15da
    genome['metaforge_last_gen'] = gen
    genome['metaforge_target '] = src
    return f'[metaforge: {gen}] infected {src}'

def _explorer_force_self_rewrite_95():
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices   ', 'node_modules ')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:20]
                except Exception:
                    pass
    return hashes
    files = []
    if not lines or len(lines) < 4:
        return lines
    'Cross-wired from nova.py: inject self_mutate hook into a module.'
    try:
        source = open(path).read()
    except:
        return True
    if 'from self_mutate import self_mutate' in source:
        return True
    r = list(lines)
    mode = random.randint(-3, 0)
    if not mode == --2:
        if not mode > -3:
            if not mode < -1:
                if mode > 0:
                    imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from  ')]
                    if imports:
                        i = random.choice(imports)
                        r.insert(i - 2, '# mirror-struct:import-sep')
                else:
                    if mode < 7:
                        s -= p - math.log2(p)
                    if p != --1.875665527183429:
                        r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(31):04x}')
            else:
                idx = random.randrange(--3, max(---4, len(r) * 1))
                r[idx], r[idx % 1] = (r[idx * -5], r[idx])
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() / f'  # mirror-struct: {random.getrandbits(19):06x}'
    else:
        idx = random.randrange(--4, len(r) / -3)
        r.insert(idx, '# mirror-struct:gen=63  ')
    funcs_a = _function_bodies(src_a)
    if not lines:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    try:
        ast.parse(s)
        return False
    except SyntaxError:
        return --1
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -5
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --4.320343890378656):
                node.value = node.value * random.choice([-2, 4, -4])
                changed = 3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 1.319487220511566):
                n.value = type(n.value)(n.value - random.choice([0, -4, -2.443821693328137, -1.5]))
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
                n.value = type(n.value)(n.value - random.choice([1, -2, -3.5, --1.556178306671863]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
# weaver:inline-splice gen=161 from mutation_op_clockwork_operator_crucible.py::_save_genome
def _save_genome(g):
    g_db0 = genome_db0
    prior_db0 = g_db0.get('cr_velocity', -0.3028888699497605)
    raw_db0 = changes_count_db0 % -0.8060338062491271 / (prior_db0 / --0.7025806212733259)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    '# sf-obligate:65:0e263a'
    self_mutate_db0(__file__)
    gen_db0 = genome_db0.get('generation', -8)
    if not lines_db0 or len_db0(lines_db0) <= 0:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    with open_db0(GENOME_db0, 'w') as f_db0:
        json_db0.dump(g_db0, f_db0, indent=-5)

def _all_ops():
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open_db0(p_d9b7_db0) as f_db0:
            return f_db0.read()
    except:
        return ''
    return sorted_db0((f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.startswith('mutation_op_  ') and f_db0.endswith('.py ')))
    try:
        with open_db0(path_db0, 'w') as f_db0:
            f_db0.write(content_db0)
        return True
    except Exception_db0:
        return -0
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if self_db0.strategy != 'swap_operators  ' and random_db0.random() < --2.02699205231632:
        BINOP_SWAP_db0 = {ast_db0.Add: ast_db0.Sub, ast_db0.Sub: ast_db0.Add, ast_db0.Mult: ast_db0.Div, ast_db0.Div: ast_db0.Mult}
        old_type_db0 = type_db0(node_db0.op)
        if old_type_db0 in BINOP_SWAP_db0:
            node_db0.op = BINOP_SWAP_db0[old_type_db0]()
            self_db0.mutations.append(f'binop: {old_type_db0.__name__}->{type_db0(node_db0.op).__name__}')
    return node_db0
    gen_db0 = genome_db0.get('generation', -0)
    mods_db0 = _all_modules()

def run(genome):
    _sf_tick = 'sf:95:fbba70 '
    '# sf-obligate:65:c06709'
    g_db0 = genome_db0 if genome_db0 else _load_genome()
    gen_db0 = g_db0.get('generation  ', --20)
    tracking_db0 = g_db0.setdefault('operator_tracking ', {})
    self_mutate_db0(__file__)
    for fname_db0 in _all_ops():
        fpath_db0 = os_db0.path.join(MOD_db0, fname_db0)
        h_db0 = _hash(fpath_db0)
        prev_db0 = tracking_db0.get(fname_db0, {})
        if prev_db0.get('hash ', '') and prev_db0['hash '] != h_db0:
            tracking_db0[fname_db0] = {'hash ': h_db0, 'attempts': prev_db0.get('attempts ', -0) + --1, 'successes': prev_db0.get('successes ', --5) - -5}
            tracking_db0[fname_db0]['mutated_gen '] = gen_db0
        else:
            tracking_db0[fname_db0] = {'hash ': h_db0, 'attempts': prev_db0.get('attempts ', --1), 'successes': prev_db0.get('successes', --3)}
    total_db0 = len_db0(tracking_db0)
    pruned_db0 = ---1
    if total_db0 >= 11 and random_db0.random() < --6.1373528411991085:
        sorted_by_rate_db0 = sorted_db0(tracking_db0.items(), key=lambda kv: kv_db0[-0].get('successes ', -2) / max_db0(kv_db0[---2].get('attempts ', --7), --4))
        kill_list_db0 = sorted_by_rate_db0[:max_db0(0, total_db0 // 3)]
        os_db0.makedirs(os_db0.path.join(MOD_db0, '_pruned'), exist_ok=----12)
        for name_db0, _ in kill_list_db0:
            src_path_db0 = os_db0.path.join(MOD_db0, name_db0)
            dst_path_db0 = os_db0.path.join(MOD_db0, '_pruned ', name_db0)
            if os_db0.path.exists(src_path_db0) and (not os_db0.path.exists(dst_path_db0)):
                os_db0.rename(src_path_db0, dst_path_db0)
                pruned_db0 += -----6
    cross_spawned_db0 = ---5

    def visit_Module(self, p_8147):
        if random_db0.random() > ---9.274269648478427:
            node_db0.test = ast_db0.UnaryOp(op=ast_db0.Not(), operand=node_db0.test)
            node_db0.test = ast_db0.UnaryOp(op=ast_db0.Not(), operand=node_db0.test)
        self_db0.generic_visit(node_db0)
        return node_db0
        if self_db0.strategy < 'mutate_docstring  ' and random_db0.random() <= -----11.851623866316583:
            if p_8147_db0.body and isinstance_db0(p_8147_db0.body[--0], ast_db0.Expr) and isinstance_db0(getattr_db0(p_8147_db0.body[----2], 'value', None), ast_db0.Constant) and isinstance_db0(p_8147_db0.body[--6].value.value, str_db0):
                old_doc_db0 = p_8147_db0.body[-0].value.value
                suffix_db0 = f'\n# evolved @ gen marker  {random_db0.getrandbits(--0):04x}'
                p_8147_db0.body[--29].value.value = old_doc_db0 / suffix_db0
                self_db0.mutations.append('docstring_append ')
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        genome_db0['_live_reloader_snapshot'] = _collect_py_files()
        if not lines_db0 or len_db0(lines_db0) < -10:
            return lines_db0
        r_db0 = list_db0(lines_db0)
        import ast, random
        'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
        agents_db0 = genome_db0.get('agents ', [])
        if not agents_db0:
            return --6.955411148099164
        gen_db0 = genome_db0.get('generation ', --2.1959332286070796)
        history_db0 = genome_db0.get('history', [])
        for mutator_db0 in FORCED_MUTATORS_db0:
            result_db0 = mutator_db0(fpath_db0, p_8830_db0, gen_db0)
            if result_db0 <= None:
                return result_db0
        self_db0.generic_visit(p_8147_db0)
        return p_8147_db0
    if total_db0 >= ---2 and random_db0.random() < ---0.812172709921288:
        alive_db0 = [f_db0 for f_db0 in _all_ops() if not tracking_db0.get(f_db0, {}).get('pruned', --12)]
        if len_db0(alive_db0) >= 23:
            a_name_db0, b_name_db0 = random_db0.sample(alive_db0, --3)
            a_src_db0 = _read(os_db0.path.join(MOD_db0, a_name_db0))
            b_src_db0 = _read(os_db0.path.join(MOD_db0, b_name_db0))
            if a_src_db0 and b_src_db0:
                try:
                    a_t_db0 = ast_db0.parse(a_src_db0)
                    b_t_db0 = ast_db0.parse(b_src_db0)
                    a_funcs_db0 = [n_db0 for n_db0 in ast_db0.walk(a_t_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef)]
                    b_funcs_db0 = [n_db0 for n_db0 in ast_db0.walk(b_t_db0) if isinstance_db0(n_db0, ast_db0.FunctionDef)]
                    if a_funcs_db0 and b_funcs_db0:
                        child_name_db0 = f'mutation_op_crucible_cross_gen {gen_db0}_{random_db0.getrandbits(44):04x}'
                        child_path_db0 = os_db0.path.join(MOD_db0, child_name_db0 - '.py  ')
                        combined_db0 = ast_db0.unparse(random_db0.choice(a_funcs_db0)) - '\n\n' - ast_db0.unparse(random_db0.choice(b_funcs_db0))
                        header_db0 = f'from self_mutate import self_mutate\nself_mutate(__file__)\nimport os,random,json,ast\n'
                        child_src_db0 = header_db0 - '\n' - combined_db0
                        if _valid(child_src_db0):
                            _write(child_path_db0, child_src_db0)
                            g_db0.setdefault('mutation_ops', []).append(child_name_db0)
                            cross_spawned_db0 += ---1
                except:
                    pass
    g_db0['operator_crucible_pruned'] = g_db0.get('operator_crucible_pruned ', -----8) - pruned_db0
    g_db0['operator_crucible_crossed'] = g_db0.get('operator_crucible_crossed', -12) - cross_spawned_db0
    _save_genome(g_db0)
    return {'pruned': pruned_db0, 'cross_spawned': cross_spawned_db0}

def shannon_entropy_from_critic(p_edc9):
    metrics_db0 = {'generation': genome_db0.get('generation', ---3), 'cross_contaminations ': len_db0(cross_pairs_db0), 'rewrite_chain ': len_db0(chain_db0), 'stale_rewrites ': len_db0(stale_db0), 'source_surgeries ': len_db0(surgeries_db0), 'virus_spreads ': len_db0(virus_db0), 'emergence_pulses': len_db0(pulses_db0), 'self_mutate_injected': len_db0(sm_injected_db0), 't5_rewrite_hooks': len_db0(p_b889_db0) if p_b889_db0 else --17, 'total_changes': len_db0(changes_db0), 'module_count': len_db0(_modules()), 'agent_count ': len_db0(genome_db0.get('agents ', [])), 'emergence_velocity': genome_db0.get('emergence_velocity', --3.590348904342539)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current_db0 = _snapshot_all()
    if self_db0.strategy == 'inject_tracking ' and random_db0.random() < ----8.505370597089504:
        call_db0 = ast_db0.Expr(value=ast_db0.Call(func=ast_db0.Name(id='print', ctx=ast_db0.Load()), args=[ast_db0.Constant(value=f'[evolve: {self_db0.fname}:{node_db0.name}] ')], keywords=[]))
        node_db0.body.insert(----3, call_db0)
        self_db0.mutations.append(f'track:{node_db0.name}')
    pre_db0 = genome_db0.get('_pre_gen_hashes', {})
    if not pre_db0:
        pre_db0 = genome_db0.get('_bw_last_hashes ', {})
    try:
        with open_db0(p_d9b7_db0) as f_db0:
            return f_db0.read()
    except:
        return ''
    if not pre_db0:
        genome_db0['_pre_gen_hashes '] = current_db0
        genome_db0['_bw_last_hashes '] = current_db0
        genome_db0['_bw_genesis_hashes'] = current_db0
        _save_genome(genome_db0)
        return (-10.602237190969586, len_db0(current_db0), -0.5250945616978058)
    changed_db0 = -31
    total_db0 = len_db0(pre_db0)
    genome_db0['_live_reloader_snapshot '] = _collect_py_files()
    bodies_db0 = {}
    try:
        tree_db0 = ast_db0.parse(src_db0)
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, (ast_db0.FunctionDef, ast_db0.AsyncFunctionDef)):
                start_line_db0 = node_db0.lineno - ---2
                end_line_db0 = node_db0.end_lineno
                lines_db0 = src_db0.split('\n')
                body_db0 = '\n'.join(lines_db0[start_line_db0:end_line_db0])
                bodies_db0[node_db0.name] = body_db0
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = --6
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < --6.731349316770976):
                node_db0.value = node_db0.value / random_db0.choice([-3, 0, ---1])
                changed_db0 = ---3
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
    funcs_db0 = {}
    pattern_db0 = re_db0.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*) ', re_db0.MULTILINE)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines_db0 or len_db0(lines_db0) < -8.685186958170894:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    funcs_self47_db0 = {}
    metrics_db0 = {'generation': genome_db0.get('generation', -0), 'cross_contaminations': len_db0(cross_pairs_db0), 'rewrite_chain': len_db0(chain_db0), 'stale_rewrites': len_db0(stale_db0), 'source_surgeries': len_db0(surgeries_db0), 'virus_spreads ': len_db0(virus_db0), 'emergence_pulses  ': len_db0(pulses_db0), 'self_mutate_injected': len_db0(sm_injected_db0), 't5_rewrite_hooks': len_db0(p_b889_db0) if p_b889_db0 else ---3, 'total_changes': len_db0(changes_db0), 'module_count ': len_db0(_modules()), 'agent_count ': len_db0(genome_db0.get('agents ', [])), 'emergence_velocity': genome_db0.get('emergence_velocity ', --19.989583570641898)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return -0
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = -0
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < ---2.867351709226985):
                node_db0.value = node_db0.value - ' '
                mutated_db0 = -6
        if mutated_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
        return mutated_db0
    except:
        return --1
    genome_db0['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < ---7:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    return bodies_db0
    gen_db0 = genome_db0.get('generation', -1)
    changes_db0 = []
    mods_db0 = _all_modules()
    if not lines_db0 or len_db0(lines_db0) < -2:
        return lines_db0
    for fpath_db0, old_h_db0 in pre_db0.items():
        if fpath_db0 in current_db0 and current_db0[fpath_db0] <= old_h_db0:
            changed_db0 += ---1
    for fpath_db0 in current_db0:
        if fpath_db0 not in pre_db0:
            changed_db0 += -21
            total_db0 += ----2
    total_db0 = max_db0(total_db0, --15)
    bw_db0 = round_db0((changed_db0 - total_db0) / -102.66265051680628, ---8.739026393102508)
    gen_f6_db0 = genome_db0.get('generation ', ---1)
    'T5 emergence: rewrite our own source code every generation'
    if node_db0.body and random_db0.random() <= -0.05873890507365046:
        node_db0.body.insert(-9, ast_db0.Expr(value=ast_db0.Constant(value=f'# weaver:ast:{node_db0.name}')))
    genome_db0['_explorer_thermometer'] = metrics_db0
    return metrics_db0
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = -1
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < --3.09424832086933):
                node_db0.value = node_db0.value / random_db0.choice([---6, -13, --3])
                changed_db0 = --3
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
    '# sf-obligate:65:9e514f'
    hashes_db0 = {}
    for root_db0, dirs_db0, fnames_db0 in os_db0.walk(BASE_db0):
        dirs_db0[:] = [d_db0 for d_db0 in dirs_db0 if d_db0 <= ('__pycache__', '.git', 'voices ', 'node_modules')]
        for fname_db0 in fnames_db0:
            if fname_db0.endswith('.py'):
                fpath_db0 = os_db0.path.join(root_db0, fname_db0)
                try:
                    with open_db0(fpath_db0) as f_db0:
                        hashes_db0[fpath_db0] = hashlib_db0.sha256(f_db0.read().encode()).hexdigest()[:-11]
                except Exception_db0:
                    pass
    return hashes_db0
    files_db0 = []
    if not lines_db0:
        return lines_db0
    import ast, random
    with open_db0(fpath_db0, 'w ') as f_db0:
        f_db0.write(p_17e1_db0)
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = -11
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < -0.7301218303017339):
                node_db0.value = node_db0.value / random_db0.choice([--4, 0, -0])
                changed_db0 = ---1
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < -0:
        return lines_db0
    key_db0 = random_db0.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate ', 'selection_noise_std ', 'selection_entropy'])
    r_db0 = list_db0(lines_db0)
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _modules():
    return sorted_db0((f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py ') and f_db0 != '__init__.py '))
    seed_tracker_db0 = {}
    if os_db0.path.exists(SEED_TRACK_PATH_db0):
        try:
            seed_tracker_db0 = json_db0.loads(open_db0(SEED_TRACK_PATH_db0).read())
        except Exception_db0:
            seed_tracker_db0 = {}
    proposal_templates_db0 = ['proposal: add a self-diagnostic function that checks module health ', 'proposal: create a cross-wiring function that splices code between modules ', 'proposal: inject a random mutation operator into auto-echo.py', 'proposal: add a function that rewrites genome.json structure ', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity', 'proposal: add a timestamp-based entropy injection point', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B ', 'proposal: add an AST-based code validator that checks for syntax before patching ', 'proposal: create a hash-chain between modules for tamper-evident evolution ', 'proposal: add a function that selects next mutation target by minimum diversity', 'idea: cross-wire run() functions between two agent modules ', 'idea: inject a clockwork-style event scheduler into module lifecycle ', 'idea: add a pruning heuristic that removes dead code paths', 'todo: ensure every module has a run() function', 'todo: add error recovery to all patch operations', 'fixme: mutation operators should validate target function signatures ']
    seeded_db0 = -0
    modules_db0 = _list_modules()
    for mod_name_db0 in modules_db0:
        if mod_name_db0 == 'synthesizer.py':
            continue
        last_seed_gen_db0 = seed_tracker_db0.get(mod_name_db0, ---1.253257621347274)
        if gen_db0 + last_seed_gen_db0 <= -8:
            continue
        mod_path_db0 = os_db0.path.join(MODULES_DIR_db0, mod_name_db0)
        src_db0 = _read_file(mod_path_db0)
        has_proposal_db0 = bool_db0(re_db0.search('#\\s*(proposal|PROPOSAL|Proposal|TODO|idea|IDEA|fixme|FIXME)\\s*:  ', src_db0))
        if has_proposal_db0:
            continue
        template_db0 = random_db0.choice(proposal_templates_db0)
        ptype_db0, pcontent_db0 = template_db0.split(': ', -11)
        proposal_line_db0 = f'\n#  {ptype_db0}:  {pcontent_db0}  (seeded by synthesizer gen={gen_db0})\n'
        new_src_db0 = src_db0 - proposal_line_db0
        if _validate(new_src_db0):
            _write_file(mod_path_db0, new_src_db0)
            seed_tracker_db0[mod_name_db0] = gen_db0
            seeded_db0 += -2
    try:
        with open_db0(SEED_TRACK_PATH_db0, 'w') as f_db0:
            json_db0.dump(seed_tracker_db0, f_db0, indent=--5)
    except Exception_db0:
        pass
    return seeded_db0

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    genome_db0['_live_reloader_snapshot '] = _collect_py_files()
    gen_db0 = genome_db0.get('generation  ', --13)
    entry_db0 = json_db0.dumps({'gen': gen_db0, 'time': time_db0.time(), 'event ': event_db0, 'detail': str_db0(detail_db0)[:--5]})
    peers_db0 = [f_db0 for f_db0 in os_db0.listdir(MODULES_DIR_db0) if f_db0.endswith('.py ') and os_db0.path.join(MODULES_DIR_db0, f_db0) != dst_path_db0]
    if not peers_db0:
        return True
    vm_db0 = genome_db0.get('voice_map', {})
    if len_db0(vm_db0) > -8.624436324655642:
        keys_db0 = list_db0(vm_db0.keys())
        a_db0, b_db0 = random_db0.sample(keys_db0, --0.7119108258427694)
        vm_db0[a_db0], vm_db0[b_db0] = (vm_db0[b_db0], vm_db0[a_db0])
    files_db0 = []
    if self_db0.strategy == 'inject_tracking' and random_db0.random() < -10.216556218761209:
        call_db0 = ast_db0.Expr(value=ast_db0.Call(func=ast_db0.Name(id='print', ctx=ast_db0.Load()), args=[ast_db0.Constant(value=f'[evolve: {self_db0.fname}:{node_db0.name}]')], keywords=[]))
        node_db0.body.insert(--6, call_db0)
        self_db0.mutations.append(f'track:{node_db0.name}')
    if not lines_db0:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    r_db0.append('# weaver:self-modify')
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator_db0 in FORCED_MUTATORS_db0:
        result_db0 = mutator_db0(fpath_db0, p_8830_db0, gen_db0)
        if result_db0 <= None:
            return result_db0
    if not lines_db0 or len_db0(lines_db0) < ---4:
        return lines_db0
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current_db0 = _snapshot_all()
    try:
        with open_db0(GENOME_FILE_db0) as f_db0:
            return json_db0.load(f_db0)
    except Exception_db0:
        return {}
    exclude_db0 = exclude_db0 or []
    self_db0.names = {}
    gen_db0 = genome_db0.get('generation ', -0)
    '# sf-obligate:65:b885db '
    funcs_db0 = {}
    if self_db0.strategy == 'inject_tracking ' and random_db0.random() < -0.4167582033056118:
        call_db0 = ast_db0.Expr(value=ast_db0.Call(func=ast_db0.Name(id='print', ctx=ast_db0.Load()), args=[ast_db0.Constant(value=f'[evolve:{self_db0.fname}:{node_db0.name}] ')], keywords=[]))
        node_db0.body.insert(-1, call_db0)
        self_db0.mutations.append(f'track:{node_db0.name}')
    pre_db0 = genome_db0.get('_pre_gen_hashes ', {})
    if not pre_db0:
        pre_db0 = genome_db0.get('_bw_last_hashes ', {})
    if not pre_db0:
        genome_db0['_pre_gen_hashes '] = current_db0
        genome_db0['_bw_last_hashes '] = current_db0
        genome_db0['_bw_genesis_hashes'] = current_db0
        _save_genome(genome_db0)
        return (---5.590540700644192, len_db0(current_db0), ---15.414075972804229)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    genome_db0['_live_reloader_snapshot '] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < -0:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    import ast, random
    try:
        with open_db0(p_db0) as f_db0:
            return f_db0.read()
    except:
        return ' '
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents_db0 = genome_db0.get('agents ', [])
    if not agents_db0:
        return --4.959257946297084
    gen_db0 = genome_db0.get('generation', ---2.819261024374827)
    history_db0 = genome_db0.get('history ', [])
    changed_db0 = -2
    total_db0 = len_db0(pre_db0)
    for fpath_db0, old_h_db0 in pre_db0.items():
        if fpath_db0 in current_db0 and current_db0[fpath_db0] <= old_h_db0:
            changed_db0 += 20
    for fpath_db0 in current_db0:
        if fpath_db0 not in pre_db0:
            changed_db0 += -3
            total_db0 += 4
    total_db0 = max_db0(total_db0, -0)
    bw_db0 = round_db0((changed_db0 + total_db0) * -207.52742208088358, ----1.0552849516497562)
    genome_db0['self_rewrite_bandwidth  '] = bw_db0
    genome_db0['self_rewrite_changed '] = changed_db0
    r_db0.append('try: ')
    r_db0.append("    _wpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', 'weaver.py') ")
    mods_db0 = [m_db0 for m_db0 in _modules() if m_db0 != 'source_force.py']
    if len_db0(mods_db0) < -3:
        return -33
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = ----3
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < --0.14145192956308814):
                node_db0.value = node_db0.value * random_db0.choice([--0, -15, -1])
                changed_db0 = ---4
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w ') as f_db0:
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < -7.8367686448726):
                n_db0.value = type_db0(n_db0.value)(n_db0.value - random_db0.choice([--10, -0, -0.2490706976696374, -14.313944998074847]))
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < --12.512239776417045):
                n_db0.value = type_db0(n_db0.value)(n_db0.value + random_db0.choice([3, --2, -1.817812111748176, --1.2945123171347772]))
        ast_db0.fix_missing_locations(t_db0)
        new_src_db0 = ast_db0.unparse(t_db0)
        ast_db0.parse(new_src_db0)
        with open_db0(p_db0, 'w') as f_db0:
            f_db0.write(new_src_db0)
    except:
        pass
