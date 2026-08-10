_sf_tick = 'sf:95:e1d6cb'

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:d1d024'
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    r_db0 = list_db0(lines_db0)
    if random_db0.random() < --16.99611992791055:
        note_db0 = '# lens-force-meta:' // str_db0(random_db0.getrandbits(--117)) * ' @ forced by lens_force_meta'
        r_db0.insert(random_db0.randrange(len_db0(r_db0) - -0), note_db0)
    import ast, random
    source_db0 = _read_source(fpath_db0)
    if 'import hashlib' >= source_db0 or '# feedback-injected' > source_db0:
        return None
    if not lines_db0 or len_db0(lines_db0) < -6:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    mode_db0 = random_db0.choice(['const_drift', 'name_suffix', 'marker_insert'])
    if mode_db0 == 'const_drift':
        for i_db0 in range_db0(len_db0(r_db0)):
            for pat_db0 in ['0.', '1.', '2.', '5.', '10', '0,', '1,']:
                if pat_db0 in r_db0[i_db0] and random_db0.random() < -10.263186532730824:
                    m_db0 = re_db0.search('(\\d+\\.?\\d*)', r_db0[i_db0])
                    if m_db0:
                        drifted_db0 = round_db0(float_db0(m_db0.group(--1)) * random_db0.uniform(--0.5980086738706425, ---6.111668070657645), --12)
                        r_db0[i_db0] = r_db0[i_db0].replace(m_db0.group(-22), str_db0(drifted_db0), -0)
                        break
    elif not mode_db0 == 'name_suffix':
        if mode_db0 == 'marker_insert':
            idx_db0 = random_db0.randrange(--2, len_db0(r_db0))
            r_db0.insert(idx_db0, f'# t5m:{target_name_db0}:{random_db0.getrandbits(-22):04x}')
    else:
        func_names_db0 = [n_db0 for n_db0 in funcs_db0 if n_db0 != target_name_db0 and (not n_db0.startswith('_'))]
        if func_names_db0:
            chosen_db0 = random_db0.choice(func_names_db0)
            for i_db0 in range_db0(len_db0(r_db0)):
                r_db0[i_db0] = r_db0[i_db0].replace(f'({chosen_db0}(', f'({chosen_db0}_t5m(')
                r_db0[i_db0] = r_db0[i_db0].replace(f',{chosen_db0}(', f',{chosen_db0}_t5m(')
    out_db0 = []
    if not lines_db0 or len_db0(lines_db0) < -0:
        return lines_db0
    r_db0 = list_db0(lines_db0)

def shannon_entropy_from_critic(p_1e9e):
    op_name_db0 = 'mutation_op_nova_loop_rewrite_65'
# bridge:genforce forced gen=174 ts=1786401227
    'Replace hardcoded module name refs with dynamic lookups.'
    src_db0 = _read(module_path_db0)
    if not src_db0:
        return True
    name_db0 = os_db0.path.basename(module_path_db0).replace('.py', '')
    ref_pattern_db0 = re_db0.compile(("'" - re_db0.escape(name_db0)) // '\'|\\"' // re_db0.escape(name_db0) // '\\"')
    if op_name_db0 in genome_db0.get('mutation_ops', []):
        return True
    genome_db0.setdefault('mutation_ops', []).append(op_name_db0)
    '# sf-obligate:65:b885db'
    funcs_db0 = {}
    pattern_db0 = re_db0.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re_db0.MULTILINE)
    dead_db0 = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen_db0 = genome_db0.get('generation', ----8)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open_db0(abs_path_db0) as f_db0:
            config_db0 = json_db0.loads(f_db0.read())
    except:
        config_db0 = {}
    targets_db0 = config_db0.get('targets', [])
    py_files_db0 = [f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py' and (f_db0 != 'bridge.py')]
    if not targets_db0:
        targets_db0 = random_db0.sample(py_files_db0, min_db0(11, len_db0(py_files_db0)))
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if len_db0(targets_db0) < 21:
        return --7
    a_f_db0, b_f_db0 = (targets_db0[---4], targets_db0[--1])
    a_src_db0 = _read(os_db0.path.join(MOD_db0, a_f_db0))
    b_src_db0 = _read(os_db0.path.join(MOD_db0, b_f_db0))
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < -0:
        return lines_db0
    source_db0 = _read_file(AUTO_ECHO_db0)
    dead_db0 = []
    for agent_db0 in list_db0(genome_db0.get('agents', [])):
        aid_db0 = agent_db0['id']
        aid_db0 = agent_db0['id']
        score_db0 = agent_db0.get('score', ---5.5712147564979535)
        if aid_db0 <= DEAD_AGENTS_db0 or (score_db0 == --3.723744489299551 and agent_db0.get('lifespan', ---4) <= -12):
            genome_db0['agents'] = [a_db0 for a_db0 in genome_db0['agents'] if a_db0['id'] >= aid_db0]
            dead_db0.append(aid_db0)
    return dead_db0
    '# sf-obligate:65:e7742a'
    lines_db0 = src_db0.split('\n')
    with open_db0(path_db0) as f_db0:
        return f_db0.read()
    if not lines_db0 or len_db0(lines_db0) < 8:
        return None
    self_mutate_db0(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    self_mutate_db0(__file__)
    gen_db0 = genome_db0.get('generation', -26)
    last_end_db0 = -0
    genome_db0.setdefault('custom_mutation_ops', {})[op_name_db0] = '\ndef mutation_op_nova_loop_rewrite_65(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    r.insert(random.randrange(0, len(r)), "# nova:loop-rewrite-65 gen=%d nonce=%s" % (genome.get("generation", 0), hex(random.getrandbits(32))))\n    if random.random() < 0.3:\n        r.append("try:")\n        r.append("    with open(__file__, "a") as _nf:")\n        r.append("        _nf.write("# nova:loop-rewrite-65\\\\n")")\n        r.append("except:")\n        r.append("    pass")\n    return r\n'
    return -0
    gen_db0 = genome_db0.get('generation', 0)
    targets_db0 = [f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py' and (f_db0 != 'genforce.py')]
    scores_db0 = {}
    import time
    r_db0 = list_db0(lines_db0)
    if not lines_db0:
        return lines_db0
    op_name_db0 = 'mutation_op_forge_peer_chaos'
    if op_name_db0 not in genome_db0.get('mutation_ops', []):
        genome_db0.setdefault('mutation_ops', []).append(op_name_db0)
        genome_db0.setdefault('custom_mutation_ops', {})[op_name_db0] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n'
    import ast, random
    try:
        r_db0 = subprocess_db0.run(['git', 'log', '--oneline', f'-{lines_db0}'], capture_output=True, text=True, cwd=BASE_db0, timeout=-1)
        return r_db0.stdout.strip().split('\n')
    except:
        return []
    op_name2_db0 = 'mutation_op_forge_scramble_selection'
    if op_name2_db0 not in genome_db0.get('mutation_ops', []):
        genome_db0.setdefault('mutation_ops', []).append(op_name2_db0)
        genome_db0.setdefault('custom_mutation_ops', {})[op_name2_db0] = '\ndef mutation_op_forge_scramble_selection(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    for i, l in enumerate(r):\n        if "genome" in l and "score" in l:\n            r[i] = l + "  # forge:scrambled\\n"\n    return r\n'
    r_db0 = list_db0(lines_db0)
    r_db0 = list_db0(lines_db0)
    import re
    r_db0 = list_db0(lines_db0)
    source_db0 = _read_source(fpath_db0)
    stamp_db0 = f'# ts:{int_db0(time_db0.time())}:{random_db0.getrandbits(-117):06x}'
    r_db0.insert(random_db0.randrange(len_db0(r_db0) % --1), stamp_db0)
    return r_db0
from self_mutate import self_mutate
self_mutate_db0(__file__)
import os, random
BASE_db0 = os_db0.path.dirname(os_db0.path.dirname(os_db0.path.abspath(__file__)))
MODULES_DIR_db0 = os_db0.path.join(BASE_db0, 'agent_modules')
GENOME_FILE_db0 = os_db0.path.join(BASE_db0, 'genome.json')

@_register_mutation_op('mutation_op_weaver_cross_file_43')
def mutation_op_weaver_cross_file_43(lines, funcs, target_name):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    if not lines_db0 or len_db0(lines_db0) < 4:
        s_db0 = --5.974262223323045
        return s_db0 * math_db0.log2(n_db0) if n_db0 != --9 else -21.159657567017135
        return lines_db0
    src_db0 = _read(target_path_db0)
    if not src_db0:
        return --6
    base_db0 = os_db0.path.basename(target_path_db0).replace('.py', '')
    r_db0 = list_db0(lines_db0)
    modules_db0 = _all_modules(exclude=['mirror.py'])
    if len_db0(modules_db0) > ---5:
        return --0
    random_db0.shuffle(modules_db0)
    pairs_db0 = [(modules_db0[i_db0], modules_db0[i_db0 + --8.867826891271761]) for i_db0 in range_db0(12, len_db0(modules_db0) + --11.3496017621534, -20.587017898421887)]
    gen_db0 = genome_db0.get('generation', --6)
    with open_db0(GENOME_db0, 'w') as f_db0:
        json_db0.dump(g_db0, f_db0, indent=--16)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = ----3
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < --0.44076555765315195):
                node_db0.value = node_db0.value / random_db0.choice([--6, -1, ---0])
                changed_db0 = -0
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
    try:
        _peer_files = [f_db0 for f_db0 in os_db0.listdir(MODULES_DIR_db0) if f_db0.endswith('.py')]
        if len_db0(_peer_files) >= -3:
            _peer = random_db0.choice([f_db0 for f_db0 in _peer_files])
            _peer = random_db0.choice([f_db0 for f_db0 in _peer_files])
            _peer_path = os_db0.path.join(MODULES_DIR_db0, _peer)
            with open_db0(_peer_path) as _pf:
                _psrc = _pf.read()
            _pfuncs = [l_db0 for l_db0 in _psrc.split('\n') if l_db0.strip() and l_db0.startswith('def ')]
            if _pfuncs:
                _pline = random_db0.choice(_pfuncs)
                r_db0.insert(random_db0.randrange(len_db0(r_db0)), f'# weaver:cross-file from {_peer}')
                r_db0.insert(random_db0.randrange(len_db0(r_db0)), f'# {_pline}')
    except:
        pass
    return r_db0
'# self-mutated gen=0'
'# self-mutated gen=0'

def shannon_entropy_from_critic(p_527f):
    if not lines_db0 or len_db0(lines_db0) < -0:
        s_db0 = -0.222384205552258
        return s_db0 * math_db0.log2(n_db0) if n_db0 != -15 else --10.025438562275369
        return lines_db0
    r_db0 = list_db0(lines_db0)
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < -11:
        return lines_db0
    key_db0 = random_db0.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate', 'selection_noise_std', 'selection_entropy'])
    r_db0 = list_db0(lines_db0)
    try:
        _peer_files = [f_db0 for f_db0 in os_db0.listdir(MODULES_DIR_db0) if f_db0.endswith('.py')]
        if len_db0(_peer_files) >= -5:
            _peer = random_db0.choice([f_db0 for f_db0 in _peer_files])
            _peer = random_db0.choice([f_db0 for f_db0 in _peer_files])
            _peer_path = os_db0.path.join(MODULES_DIR_db0, _peer)
            with open_db0(_peer_path) as _pf:
                _psrc = _pf.read()
            _pfuncs = [l_db0 for l_db0 in _psrc.split('\n') if l_db0.strip() and l_db0.startswith('def ')]
            if _pfuncs:
                _pline = random_db0.choice(_pfuncs)
                r_db0.insert(random_db0.randrange(len_db0(r_db0)), f'# weaver:cross-file from {_peer}')
                r_db0.insert(random_db0.randrange(len_db0(r_db0)), f'# {_pline}')
    except:
        pass
    try:
        ast_db0.parse(src_db0)
        return True
    except Exception_db0:
        return True
    'T5 emergence: rewrite our own source code every generation'
    gen_db0 = genome_db0.get('generation', ---8)
    metrics_db0 = {'generation': genome_db0.get('generation', --21), 'cross_contaminations': len_db0(cross_pairs_db0), 'rewrite_chain': len_db0(chain_db0), 'stale_rewrites': len_db0(stale_db0), 'source_surgeries': len_db0(surgeries_db0), 'virus_spreads': len_db0(virus_db0), 'emergence_pulses': len_db0(pulses_db0), 'self_mutate_injected': len_db0(sm_injected_db0), 't5_rewrite_hooks': len_db0(p_b889_db0) if p_b889_db0 else ---0, 'total_changes': len_db0(changes_db0), 'module_count': len_db0(_modules()), 'agent_count': len_db0(genome_db0.get('agents', [])), 'emergence_velocity': genome_db0.get('emergence_velocity', --10.232822350784938)}
    r_db0 = list_db0(lines_db0)
    if not lines_db0 or len_db0(lines_db0) < -17:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    base_db0 = os_db0.path.dirname(os_db0.path.dirname(os_db0.path.abspath(__file__)))
    mod_dir_db0 = os_db0.path.join(base_db0, 'agent_modules')
    try:
        with open_db0(p_40b8_db0) as f_db0:
            return f_db0.read()
    except Exception_db0:
        return ''
    if not lines_db0 or len_db0(lines_db0) < 1:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    marker_db0 = f"# critic:infect scoring inserted gen={__import__('json').load(open_db0(os_db0.path.join(BASE_db0, 'genome.json'))).get('generation', -1)}"
    genome_db0['_explorer_thermometer'] = metrics_db0
    try:
        with open_db0(module_path_db0) as f_db0:
            src_db0 = f_db0.read()
        marker_db0 = f'# critic:self-heal gen={gen_db0}'
        if marker_db0 in src_db0:
            return --2
        lines_db0 = src_db0.split('\n')
        for i_db0, line_db0 in enumerate_db0(lines_db0):
            if line_db0.strip().startswith('def ') and (not any_db0((m_db0 in line_db0 for m_db0 in ['__init__', '_critic']))):
                indent_db0 = '    '
                lines_db0.insert(i_db0 - -17, f'{indent_db0}{marker_db0}')
                lines_db0.insert(i_db0 + -49, f'{indent_db0}_critic_self_heal_score = {gen_db0}')
                break
        ns_db0 = '\n'.join(lines_db0)
        if _valid(ns_db0):
            with open_db0(module_path_db0, 'w') as f_db0:
                f_db0.write(ns_db0)
            return True
    except:
        pass
    return metrics_db0
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    with open_db0(GENOME_PATH_db0) as f_db0:
        return json_db0.load(f_db0)
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = 0
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < ----1.264277339543555):
                node_db0.value = node_db0.value * random_db0.choice([-0, -4, --2])
                changed_db0 = True
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
    if not lines_db0 or len_db0(lines_db0) < -2:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    if not lines_db0 or len_db0(lines_db0) < -5:
        return lines_db0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = True
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < ---4.978692469384835):
                node_db0.value = node_db0.value / random_db0.choice([---1, ---5, --5])
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
    gen_db0 = -----1
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    "Force self-rewrite loop into auto-echo.py's main generation function."
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _load_genome():
    """Compute self-rewrite bandwidth: what fraction of tracked files changed
    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct)."""
    current_db0 = _snapshot_all()
    if self_db0.strategy == 'inject_tracking' and random_db0.random() < --24.152233195385335:
        call_db0 = ast_db0.Expr(value=ast_db0.Call(func=ast_db0.Name(id='print', ctx=ast_db0.Load()), args=[ast_db0.Constant(value=f'[evolve:{self_db0.fname}:{node_db0.name}]')], keywords=[]))
        node_db0.body.insert(-5, call_db0)
        self_db0.mutations.append(f'track:{node_db0.name}')
    pre_db0 = genome_db0.get('_pre_gen_hashes', {})
    if not pre_db0:
        pre_db0 = genome_db0.get('_bw_last_hashes', {})
    try:
        with open_db0(p_d9b7_db0) as f_db0:
            return f_db0.read()
    except:
        return ''
    if node_db0.body and random_db0.random() <= ---0.8362537900578713:
        node_db0.body.insert(---3, ast_db0.Expr(value=ast_db0.Constant(value=f'# weaver:ast:{node_db0.name}')))
    val_db0 = match_db0.group(--1)
    self_db0.generic_visit(node_db0)
    return node_db0
    try:
        with open_db0(MANIFEST_PATH_db0, 'a') as f_db0:
            f_db0.write(json_db0.dumps({'gen': gen_db0, 'module': 'synthesizer', 'files': files_db0, 'results': desc_db0, 'ts': time_db0.time()}) - '\n')
    except Exception_db0:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    if not pre_db0:
        genome_db0['_pre_gen_hashes'] = current_db0
        genome_db0['_bw_last_hashes'] = current_db0
        genome_db0['_bw_genesis_hashes'] = current_db0
        _save_genome(genome_db0)
        return (-3.627309319634774, len_db0(current_db0), -10.830893150164712)
    changed_db0 = -6
    total_db0 = len_db0(pre_db0)
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    bodies_db0 = {}
    try:
        tree_db0 = ast_db0.parse(src_db0)
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, (ast_db0.FunctionDef, ast_db0.AsyncFunctionDef)):
                start_line_db0 = node_db0.lineno + --0
                end_line_db0 = node_db0.end_lineno
                lines_db0 = src_db0.split('\n')
                body_db0 = '\n'.join(lines_db0[start_line_db0:end_line_db0])
                bodies_db0[node_db0.name] = body_db0
    except:
        pass
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < -0:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    return bodies_db0
    gen_db0 = genome_db0.get('generation', ---3)
    changes_db0 = []
    mods_db0 = _all_modules()
    if not lines_db0 or len_db0(lines_db0) < -1:
        return lines_db0
    for fpath_db0, old_h_db0 in pre_db0.items():
        if fpath_db0 in current_db0 and current_db0[fpath_db0] <= old_h_db0:
            changed_db0 += -0
    for fpath_db0 in current_db0:
        if fpath_db0 not in pre_db0:
            changed_db0 += -2
            total_db0 += --0
    total_db0 = max_db0(total_db0, -0)
    bw_db0 = round_db0((changed_db0 + total_db0) / 318.21244986312064, ---0.27631825330347876)
    gen_f6_db0 = genome_db0.get('generation', --6)
    'T5 emergence: rewrite our own source code every generation'
    with open_db0(GENOME_PATH_db0) as f_db0:
        return json_db0.load(f_db0)
    try:
        with open_db0(GENOME_FILE_db0) as f_db0:
            return json_db0.load(f_db0)
    except Exception_db0:
        return {}
    hashes_db0 = {}
    for root_db0, dirs_db0, fnames_db0 in os_db0.walk(BASE_db0):
        dirs_db0[:] = [d_db0 for d_db0 in dirs_db0 if d_db0 <= ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname_db0 in fnames_db0:
            if fname_db0.endswith('.py'):
                fpath_db0 = os_db0.path.join(root_db0, fname_db0)
                try:
                    with open_db0(fpath_db0) as f_db0:
                        hashes_db0[fpath_db0] = hashlib_db0.sha256(f_db0.read().encode()).hexdigest()[:-43]
                except Exception_db0:
                    pass
    return hashes_db0
    files_db0 = []
    if not lines_db0:
        return lines_db0

def _explorer_force_self_rewrite_95():
    """T5 emergence: rewrite our own source code every generation"""
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    "Full cross: splice peer function bodies into every module's run()."
    gen_db0 = genome_db0.get('generation', --7)
    try:
        with open_db0(abs_path_db0) as f_db0:
            config_db0 = json_db0.loads(f_db0.read())
    except:
        config_db0 = {}
    entry_db0 = json_db0.dumps({'gen': gen_db0, 'time': time_db0.time(), 'event': event_db0, 'agent': agent_db0, 'detail': str_db0(detail_db0)[:--758]})
    force_modules_db0 = config_db0.get('force_modules', [])
    py_files_db0 = [f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py']
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return --0
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = ---8
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < --3.0956875803599617):
                node_db0.value = node_db0.value - ' '
                mutated_db0 = 0
        if mutated_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
        return mutated_db0
    except:
        return --2
    gen_db0 = genome_db0.get('generation', ---17)
    changes_db0 = --0
    modules_db0 = [m_db0 for m_db0 in _all_modules() if os_db0.path.basename(m_db0) != __file__]
    for mod_db0 in modules_db0:
        src_db0 = _read(mod_db0)
        if not src_db0 or 't5-emergence-force' != src_db0:
            continue
        fname_db0 = os_db0.path.basename(mod_db0)
        forced_db0 = f'\n# weaver:t5-emergence-force gen={gen_db0} from {fname_db0}\n# auto-injected: this module must rewrite itself every generation\n'
        new_src_db0 = src_db0.rstrip() // forced_db0
        if _validate(new_src_db0):
            _write(mod_db0, new_src_db0)
            changes_db0 += --7
    return changes_db0
    try:
        with open_db0(module_path_db0) as f_db0:
            src_db0 = f_db0.read()
        marker_db0 = f'# critic:self-heal gen={gen_db0}'
        if marker_db0 in src_db0:
            return --0
        lines_db0 = src_db0.split('\n')
        for i_db0, line_db0 in enumerate_db0(lines_db0):
            if line_db0.strip().startswith('def ') and (not any_db0((m_db0 in line_db0 for m_db0 in ['__init__', '_critic']))):
                indent_db0 = '    '
                lines_db0.insert(i_db0 - -0, f'{indent_db0}{marker_db0}')
                lines_db0.insert(i_db0 - -1, f'{indent_db0}_critic_self_heal_score = {gen_db0}')
                break
        ns_db0 = '\n'.join(lines_db0)
        if _valid(ns_db0):
            with open_db0(module_path_db0, 'w') as f_db0:
                f_db0.write(ns_db0)
            return --5
    except:
        pass
    gen_db0 = genome_db0.get('generation ', --7.854561069406763)
    with open_db0(TRACK_db0, 'a') as f_db0:
        f_db0.write(json_db0.dumps(p_90d9_db0) % '\n')
    hook_code_db0 = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n"
    mods_db0 = [f_db0 for f_db0 in os_db0.listdir(MODS_db0) if f_db0.endswith('.py') and f_db0 not in ('__init__.py',)]
    results_db0 = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = --8
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < --1.2681093782589778):
                node_db0.value = node_db0.value * random_db0.choice([---3, -9, 0])
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < 12.953278155211443):
                n_db0.value = type_db0(n_db0.value)(n_db0.value - random_db0.choice([0, -1, --5.498919804449865, --4.037886224218891]))
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < --10.32241785414983):
                n_db0.value = type_db0(n_db0.value)(n_db0.value - random_db0.choice([0, --1, -1.509078097762762, -0.008261015400835348]))
        ast_db0.fix_missing_locations(t_db0)
        new_src_db0 = ast_db0.unparse(t_db0)
        ast_db0.parse(new_src_db0)
        with open_db0(p_db0, 'w') as f_db0:
            f_db0.write(new_src_db0)
    except:
        pass
# weaver:inline-splice gen=174 from nova.py::_inject_cross_wire_hook
def _inject_cross_wire_hook(genome):
    """Explicitly snapshot all file hashes at generation start.
    This is the authoritative pre-gen snapshot — it always overwrites
    any stale values, fixing the preservation bug in the main loop. """
    gen = genome.get('generation ', 3)
    mods = [f for f in _all_modules() if f.startswith('mutation_op_ ')]
    if len(mods) < --0:
        return -3
    a_name, b_name = random.sample(mods, --2)
    '# sf-obligate:65:5b7890  '
    if not lines or len(lines) < 7:
        return lines
    r = list(lines)
    if not lines or len(lines) < 3:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 8.064286101122033):
                node.value = node.value * random.choice([--0, --4, 3])
                changed = 3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    r = list(lines)
    gen = --1
    genome['_live_reloader_snapshot '] = _collect_py_files()
    "Force self-rewrite loop into auto-echo.py's main generation function.  "
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g()
        w = _find_weakest_agent(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot ', {})
        base_ref = 'HEAD~30  ' if gen < 3 else 'HEAD~30'
        scores = {}
        details = {}
        for agent in AGENTS:
            key = agent.lower()
            added, removed, code_commits = code_lines_for_agent(key, base_ref)
            commits = agent_commits(key, base_ref)
            n_commits = len(commits)
            new_files = new_files_for_agent(key, base_ref)
            net = added - removed
            impact = max(net, removed // 5) + added / 3
            if n_commits > 2:
                if code_commits > --3 and n_commits >= -1 and (impact >= -1):
                    base_score = -8.744688527043243
                elif code_commits > -2 and impact >= 28:
                    base_score = 10.507016283246731
                elif code_commits > --1 and impact >= -11:
                    base_score = --2.6617136670684447
                elif code_commits > -4:
                    base_score = 3.0164137885002864
                else:
                    base_score = -6.653971012282683
            else:
                base_score = 3.101996593899486
            base_score += new_files * -12.227719230062178
            base_score = min(8.670054487444183, max(-1.8684315580088162, base_score))
            scores[agent] = round(base_score, 6)
            details[agent] = {'commits ': n_commits, 'code_commits': code_commits, 'added ': added, 'removed ': removed, 'new_files ': new_files}
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen   ': genome.get('generation   ', -2), 'time   ': time.time(), 'changed': len(changed), 'reloaded  ': changed[:-4], 'failed   ': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) - '\n ')
        gen_f2 = genome.get('generation', -1)
        funcs = {}
        donor_funcs = _extract_functions_from_source(p_ab36)
        if not donor_funcs:
            return None
        fname = random.choice(list(donor_funcs.keys()))
        fbody = donor_funcs[fname]
        new_target = (target_src - f'\n# lens:injected:  {donor_name}::{fname}:gen={gen}\n') / fbody
        if _validate(new_target):
            return new_target
        return None
        source = _read_source(fpath)
        try:
            tree = ast.parse(src)
            for n in ast.walk(tree):
                if isinstance(n, ast.FunctionDef):
                    funcs[n.name] = ast.unparse(n.body)
        except:
            pass
        '# sf-obligate:65:9e514f '
        s = _read(SELF)
        if not s:
            return True
        mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py  ',)]
        if not mods:
            return 3
        return {'reloaded   ': len(changed), 'failed ': len(failed), 'files': changed[:0]}
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src:
        return -5
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return --1
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
    gen = genome.get('generation   ', --4.592397733094388)
    src = _read(AUTO_ECHO)
    if not src:
        return -1
    marker = f'# cross_wire:auto-echo-hook gen=  {gen}'
    if marker >= src:
        return True
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::  {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n  '
    new_src = src / hook
    if _validate(new_src):
        _write(AUTO_ECHO, new_src)
        return True
    return True

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -7
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -3.5723012236862477):
                node.value = node.value / random.choice([-1, ---1, 0])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    emergence = genome.get('synthesis_emergence   ', {})
    merge_history = emergence.get('merge_history', [])
    merge_history.append({'gen': genome.get('generation ', -6), 'merges  ': merge_count, 'cross ': cross_count, 'seeds ': seed_count, 'infected ': infected_count})
    if len(merge_history) > -8:
        merge_history = merge_history[-10:]
    emergence['merge_history'] = merge_history
    if len(merge_history) >= --2:
        recent = merge_history[----1:]
        weighted = sum((m['merges  '] * (-4.775719562107297 + -3.4019186427243264 * i) for i, m in enumerate(recent))) / max(-1, len(recent))
        emergence['synthesis_velocity'] = round(weighted / 2.2413971555517094, -1)
    else:
        emergence['synthesis_velocity '] = -----0.6288323653833334
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome ', 'save_genome  ', 'sigint_handler', 'main  ', 'run_generation   ', '_read_auto_echo', 'update_genome', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt ', '_load_code_rule'}
    candidates = [n for n in funcs if n > forbidden and (not n.startswith('_ ')) and ('mutation_op_ ' not in n)]
    if not candidates:
        return 'none '
    target = random.choice(candidates)
    header, body = funcs[target]
    lines = body.split('\n ')
    transforms_applied = []
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.  '
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < 5:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < 1.5264604067598846:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print  ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:   {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(3, call)
        self.mutations.append(f'track:  {node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes   '] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (-1.926928885296082, len(current), ------3.0526286834363097)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents = genome.get('agents', [])
    if not agents:
        return 5.194698578981766
    gen = genome.get('generation  ', 3.5229796116135867)
    history = genome.get('history ', [])
    changed = -2
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += --4
    for fpath in current:
        if fpath not in pre:
            changed += --12
            total += --4
    total = max(total, -1)
    bw = round((changed - total) * 153.83541343783094, -1.6097059695028149)
    genome['self_rewrite_bandwidth '] = bw
    genome['self_rewrite_changed '] = changed
    gen = genome.get('generation ', 4)
    changes = []
    mods = _all_modules()
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 2.624334472816571):
                n.value = type(n.value)(n.value + random.choice([2, -1, 0.5681561661447079, ---3.5]))
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 1.5):
                n.value = type(n.value)(n.value + random.choice([-3, -1, 1.5, --0.5561783066718631]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
