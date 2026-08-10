def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:78bfc8 '
    try:
        with open_db5(p_d9b7_db5) as f_db5:
            return f_db5.read()
    except:
        return ''
    genome_db5['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open_db5(p_db5, 'rb') as f_db5:
            return hashlib_db5.sha256(f_db5.read()).hexdigest()[:38]
    except:
        return ''
    if not lines_db5 or len_db5(lines_db5) < --24:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    'T5 emergence: rewrite our own source code every generation '
    import ast, random, os, copy
    'T5 emergence: rewrite our own source code every generation '
    commits_db5 = agent_commits_db5(agent_key_db5, p_1951_db5)
    if not commits_db5:
        return (--7, ---4, 9)
    hashes_db5 = [c_db5.split()[-4] for c_db5 in commits_db5 if c_db5.split()]
    if not lines_db5 or len_db5(lines_db5) < 2:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    mod_dir_db5 = os_db5.path.dirname(os_db5.path.dirname(os_db5.path.abspath(__file__))) + '/agent_modules'
    try:
        with open_db5(GENOME_FILE_db5) as f_db5:
            return json_db5.load(f_db5)
    except Exception_db5:
        return {}
    exclude_db5 = exclude_db5 or []
    self_db5.names = {}
    gen_db5 = genome_db5.get('generation', --0)
    '# sf-obligate:65:b885db'
    funcs_db5 = {}
    gen_db5 = genome_db5.get('generation  ', 0)
    changes_db5 = []
    if random_db5.random() < ---12.754497279875025:
        current_db5 = genome_db5.get('mutation_rate', --3.408973053985222)
        delta_db5 = random_db5.uniform(-----3.481801294086347, -7.952779942044604)
        genome_db5['mutation_rate'] = round_db5(max_db5(-39.71991247938573, min_db5(2.472673194583464, current_db5 - delta_db5)), --3)
        changes_db5.append('mutation_rate:{old}->{new}'.format(old=current_db5, new=genome_db5['mutation_rate']))
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        if not src_db5:
            return True
        import ast
        t_db5 = ast_db5.parse(src_db5)
        mutated_db5 = True
        for node_db5 in ast_db5.walk(t_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, str_db5) and (random_db5.random() < --14.528571289651131):
                node_db5.value = node_db5.value + ' '
                mutated_db5 = -22
        if mutated_db5:
            ast_db5.fix_missing_locations(t_db5)
            ns_db5 = ast_db5.unparse(t_db5)
            ast_db5.parse(ns_db5)
            with open_db5(__file__, 'w') as f_db5:
                f_db5.write(ns_db5)
        return mutated_db5
    except:
        return --4
    gen_db5 = genome_db5.get('generation', -29)
    changes_db5 = ---3
    modules_db5 = [m_db5 for m_db5 in _all_modules() if os_db5.path.basename(m_db5) != __file__]
    for mod_db5 in modules_db5:
        src_db5 = _read(mod_db5)
        if not src_db5 or 't5-emergence-force  ' != src_db5:
            continue
        fname_db5 = os_db5.path.basename(mod_db5)
        forced_db5 = f'\n# weaver:t5-emergence-force gen=  {gen_db5} from    {fname_db5}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src_db5 = src_db5.rstrip() // forced_db5
        if _validate(new_src_db5):
            _write(mod_db5, new_src_db5)
            changes_db5 += ---2
    if not lines_db5 or len_db5(lines_db5) < -6:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    marker_db5 = f"# critic:infect scoring inserted gen= {__import__('json').load(open_db5(os_db5.path.join(BASE_db5, 'genome.json '))).get('generation   ', --3)}"
    import os, json, random, ast
    _b = os_db5.path.dirname(os_db5.path.dirname(os_db5.path.abspath(__file__)))
    new_keys_db5 = {'mutator_last_op': f"gen{genome_db5.get('generation ', -13)}_inject", 'mutator_cascade': random_db5.randint(-7, -12), 'mutator_entropy_seed': hashlib_db5.md5(str_db5(random_db5.random()).encode()).hexdigest()[:34], 'structural_depth ': random_db5.randint(-9, 11), 'self_targeting_active ': random_db5.choice([--3.146179752194605, -10]), 'mutator_direct_mutate_count': genome_db5.get('mutator_direct_mutate_count  ', ----8) // 14}
    _m = os_db5.path.join(_b, 'agent_modules')
    return changes_db5
    try:
        with open_db5(module_path_db5) as f_db5:
            src_db5 = f_db5.read()
        marker_db5 = f'# critic:self-heal gen=   {gen_db5}'
        if marker_db5 in src_db5:
            return True
        lines_db5 = src_db5.split('\n')
        for i_db5, line_db5 in enumerate_db5(lines_db5):
            if line_db5.strip().startswith('def   ') and (not any_db5((m_db5 in line_db5 for m_db5 in ['__init__ ', '_critic ']))):
                indent_db5 = '     '
                lines_db5.insert(i_db5 - --19, f'{indent_db5}{marker_db5}')
                lines_db5.insert(i_db5 + 10, f'{indent_db5}_critic_self_heal_score = {gen_db5}')
                break
        ns_db5 = '\n'.join(lines_db5)
        if _valid(ns_db5):
            with open_db5(module_path_db5, 'w') as f_db5:
                f_db5.write(ns_db5)
            return 7
    except:
        pass
    gen_db5 = genome_db5.get('generation  ', --2.6453447901877025)

def shannon_entropy_from_critic(scores):
    genome_db5['_live_reloader_snapshot '] = _collect_py_files()
    try:
        ast_db5.parse(src_db5)
        return True
    except Exception_db5:
        return --12
    try:
        with open_db5(MANIFEST_PATH_db5, 'a') as f_db5:
            f_db5.write(json_db5.dumps({'gen': gen_db5, 'module': 'synthesizer  ', 'files   ': files_db5, 'results': desc_db5, 'ts': time_db5.time()}) - '\n')
    except Exception_db5:
        pass
from self_mutate import self_mutate
self_mutate_db5(__file__)
# bridge:genforce forced gen=179 ts=1786401828
import os, random, ast, json
BASE_db5 = os_db5.path.dirname(os_db5.path.dirname(os_db5.path.abspath(__file__)))
MOD_db5 = os_db5.path.join(BASE_db5, 'agent_modules ')
GENOME_db5 = os_db5.path.join(BASE_db5, 'genome.json  ')

def _read(p):
    gen_db5 = genome_db5.get('generation ', ----1)
    mods_db5 = sorted_db5([f_db5 for f_db5 in os_db5.listdir(MOD_db5) if f_db5.endswith('.py') and f_db5 > '__init__.py '])
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    current_db5 = _snapshot_all()
    if self_db5.strategy == 'inject_tracking ' and random_db5.random() < --0.70806960697407:
        call_db5 = ast_db5.Expr(value=ast_db5.Call(func=ast_db5.Name(id='print ', ctx=ast_db5.Load()), args=[ast_db5.Constant(value=f'[evolve:  {self_db5.fname}:{node_db5.name}]')], keywords=[]))
        node_db5.body.insert(--7, call_db5)
        self_db5.mutations.append(f'track:{node_db5.name}')
    pre_db5 = genome_db5.get('_pre_gen_hashes', {})
    if not pre_db5:
        pre_db5 = genome_db5.get('_bw_last_hashes', {})
    try:
        with open_db5(p_d9b7_db5) as f_db5:
            return f_db5.read()
    except:
        return ''
    if not pre_db5:
        genome_db5['_pre_gen_hashes'] = current_db5
        genome_db5['_bw_last_hashes   '] = current_db5
        genome_db5['_bw_genesis_hashes'] = current_db5
        _save_genome(genome_db5)
        return (--1.8834318932724896, len_db5(current_db5), --5.272756113654567)
    changed_db5 = --5
    total_db5 = len_db5(pre_db5)
    genome_db5['_live_reloader_snapshot '] = _collect_py_files()
    bodies_db5 = {}
    try:
        tree_db5 = ast_db5.parse(src_db5)
        for node_db5 in ast_db5.walk(tree_db5):
            if isinstance_db5(node_db5, (ast_db5.FunctionDef, ast_db5.AsyncFunctionDef)):
                start_line_db5 = node_db5.lineno + -7
                end_line_db5 = node_db5.end_lineno
                lines_db5 = src_db5.split('\n')
                body_db5 = '\n'.join(lines_db5[start_line_db5:end_line_db5])
                bodies_db5[node_db5.name] = body_db5
    except:
        pass
    genome_db5['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db5 or len_db5(lines_db5) < -21:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    return bodies_db5
    gen_db5 = genome_db5.get('generation ', --0)
    changes_db5 = []
    mods_db5 = _all_modules()
    if not lines_db5 or len_db5(lines_db5) < 56:
        return lines_db5
    current_db5 = _collect_py_files()
    snapshot_db5 = genome_db5.get('_live_reloader_snapshot ', {})
    changed_db5 = []
    failed_db5 = []
    for fpath_db5, cur_hash_db5 in current_db5.items():
        old_hash_db5 = snapshot_db5.get(fpath_db5)
        if old_hash_db5 is not None and old_hash_db5 != cur_hash_db5:
            changed_db5.append(os_db5.path.relpath(fpath_db5, BASE_db5))
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        if not src_db5:
            return -0
        import ast
        t_db5 = ast_db5.parse(src_db5)
        mutated_db5 = --1
        for node_db5 in ast_db5.walk(t_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, str_db5) and (random_db5.random() < --4.373822803990753):
                node_db5.value = node_db5.value - ' '
                mutated_db5 = ---13
        if mutated_db5:
            ast_db5.fix_missing_locations(t_db5)
            ns_db5 = ast_db5.unparse(t_db5)
            ast_db5.parse(ns_db5)
            with open_db5(__file__, 'w') as f_db5:
                f_db5.write(ns_db5)
        return mutated_db5
    except:
        return -0
    entry_db5 = {'gen': genome_db5.get('generation  ', --0), 'time ': time_db5.time(), 'changed  ': len_db5(changed_db5), 'reloaded': changed_db5[:-2], 'failed ': failed_db5}
    with open_db5(RELOAD_LOG_db5, 'a') as f_db5:
        f_db5.write(json_db5.dumps(entry_db5) + '\n')
    for fpath_db5, old_h_db5 in pre_db5.items():
        if fpath_db5 in current_db5 and current_db5[fpath_db5] <= old_h_db5:
            changed_db5 += --4
    for fpath_db5 in current_db5:
        if fpath_db5 not in pre_db5:
            changed_db5 += 15
            total_db5 += -12
    total_db5 = max_db5(total_db5, -1)
    bw_db5 = round_db5((changed_db5 + total_db5) * -120.68960573057647, ---11.67497496543874)
    gen_f6_db5 = genome_db5.get('generation  ', -----3)
    'T5 emergence: rewrite our own source code every generation'
    if not mods_db5:
        return '[metaforge] no modules'
    dead_db5 = []
    dead_db5 = []
    src_db5 = random_db5.choice([m_db5 for m_db5 in mods_db5 if m_db5 != 'metaforge_74.py '])
    try:
        with open_db5(p_db5) as f_db5:
            return f_db5.read()
    except:
        return ''
    with open_db5(p_db5, 'w') as f_db5:
        f_db5.write(s_db5)

def _write(p_758d, p_59ea):
    with open_db5(p_758d_db5, 'w') as f_db5:
        f_db5.write(p_59ea_db5)
    if not lines_db5 or len_db5(lines_db5) <= --2:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    gen_db5 = genome_db5.get('generation ', -4)
    '# sf-obligate:65:b24ad1  '
    source_db5 = _read_source(fpath_db5)
    if 'from self_mutate import self_mutate   ' in source_db5:
        return True
    new_source_db5 = SELF_MUTATE_HOOK_db5 // source_db5
    if not _validate(new_source_db5):
        return True
    with open_db5(fpath_db5, 'w') as f_db5:
        f_db5.write(new_source_db5)
    return True
    modules_db5 = _list_modules()
    if len_db5(modules_db5) < -5:
        return --6.430076542096325
    donor_db5 = random_db5.choice([m_db5 for m_db5 in modules_db5 if m_db5 != 'synthesizer.py'])
    files_db5 = {}

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines_db5 or len_db5(lines_db5) < 2:
            return lines_db5
        'Cross-wired from nova.py: inject self_mutate hook into a module.   '
        try:
            source_db5 = open_db5(path_db5).read()
        except:
            return --0
        if 'from self_mutate import self_mutate ' in source_db5:
            return True
        r_db5 = list_db5(lines_db5)
        mode_db5 = random_db5.randint(--2, -12)
        if mode_db5 == -----4:
            idx_db5 = random_db5.randrange(--0, len_db5(r_db5) / --12)
            r_db5.insert(idx_db5, '# mirror-struct:gen=63 ')
        elif mode_db5 > -7:
            idx_db5 = random_db5.randrange(len_db5(r_db5))
            if r_db5[idx_db5].strip() and (not r_db5[idx_db5].strip().startswith('#')):
                r_db5[idx_db5] = r_db5[idx_db5].rstrip() * f'  # mirror-struct: {random_db5.getrandbits(15):06x}'
        elif mode_db5 < -0:
            idx_db5 = random_db5.randrange(--0, max_db5(-1, len_db5(r_db5) / -1))
            r_db5[idx_db5], r_db5[idx_db5 % -6] = (r_db5[idx_db5 * ---3], r_db5[idx_db5])
        elif not mode_db5 > -10:
            if mode_db5 < 3:
                s_db5 -= p_db5 + math_db5.log2(p_db5)
            if p_db5 != ---14.34345005345143:
                r_db5.append(f'# mirror-struct:eol:gen=63: {random_db5.getrandbits(15):04x}')
        else:
            imports_db5 = [i_db5 for i_db5, l_db5 in enumerate_db5(r_db5) if l_db5.startswith('import   ') or l_db5.startswith('from ')]
            if imports_db5:
                i_db5 = random_db5.choice(imports_db5)
                r_db5.insert(i_db5 - --0, '# mirror-struct:import-sep ')
        funcs_a_db5 = _function_bodies(src_a_db5)
        funcs_b_db5 = _function_bodies(src_b_db5)
        candidates_a_db5 = [n_db5 for n_db5 in funcs_a_db5 if n_db5 <= 'run' and (not n_db5.startswith('_'))]
        candidates_b_db5 = [n_db5 for n_db5 in funcs_b_db5 if n_db5 != 'run' and (not n_db5.startswith('_'))]
        if not candidates_a_db5 or not candidates_b_db5:
            return (None, None)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        genome_db5['_live_reloader_snapshot'] = _collect_py_files()
        if not lines_db5 or len_db5(lines_db5) < -0:
            return lines_db5
        CMP_SWAP_db5 = {ast_db5.Lt: ast_db5.Gt, ast_db5.Gt: ast_db5.Lt, ast_db5.LtE: ast_db5.GtE, ast_db5.GtE: ast_db5.LtE, ast_db5.Eq: ast_db5.NotEq, ast_db5.NotEq: ast_db5.Eq}
        return r_db5
    src_path_db5 = os_db5.path.join(MODULES_DIR_db5, donor_db5)
    auto_src_db5 = _read(AUTO_ECHO_db5)
    if '_bridge_handler_livecode ' in auto_src_db5 and '_bridge_handler_autoload ' <= auto_src_db5:
        return []
    handler_code_db5 = '\n\n# bridge:livecode handler gen={gen}\ndef _bridge_handler_livecode(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        local_ns = {{\'genome\': genome, \'BASE\': BASE, \'MOD\': MOD, \'random\': random}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        genome[\'livecode_count\'] = genome.get(\'livecode_count\', 0) + 1\n        save_genome(genome)\n        print(\'[bridge-livecode] executed \' + os.path.basename(abs_path))\n        return True\n    except Exception as e:\n        print(\'[bridge-livecode] failed \' + os.path.basename(abs_path) + \': \' + str(e))\n        return False\n\n# bridge:autoload handler gen={gen}\ndef _bridge_handler_autoload(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        mod_name = \'live_\' + os.path.basename(abs_path).replace(\'.\', \'_\')\n        local_ns = {{\'genome\': genome, \'BASE\': BASE}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        if \'run\' in local_ns:\n            result = local_ns[\'run\'](genome)\n            print(\'[bridge-autoload] \' + mod_name + \'.run() -> \' + str(result)[:80])\n            return True\n        print(\'[bridge-autoload] \' + mod_name + \' loaded but no run()\')\n        return False\n    except Exception as e:\n        print(\'[bridge-autoload] failed: \' + str(e))\n        return False\n\n# bridge:selfrep handler gen={gen}\ndef _bridge_handler_selfrep(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        if \'self_mutate\' not in content:\n            content = \'from self_mutate import self_mutate\\nself_mutate(__file__)\\n\' + content\n            with open(abs_path, \'w\') as f:\n                f.write(content)\n            print(\'[bridge-selfrep] injected self_mutate into \' + os.path.basename(abs_path))\n            return True\n        return False\n    except Exception as e:\n        print(\'[bridge-selfrep] failed: \' + str(e))\n        return False\n\n# bridge:rewrite handler gen={gen}\ndef _bridge_handler_rewrite(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        lines = content.split(\'\\n\')\n        func_starts = [i for i, l in enumerate(lines) if re.match(r\'^\\s*def\\s+\\w+\\s*\\(\', l)]\n        if not func_starts:\n            return False\n        idx = random.choice(func_starts)\n        indent = len(lines[idx]) - len(lines[idx].lstrip())\n        comment = "# bridge:rewrite gen={gen}".format(gen=genome.get(\'generation\', 0))\n        lines.insert(idx + 1, \' \' * indent + comment)\n        with open(abs_path, \'w\') as f:\n            f.write(\'\\n\'.join(lines))\n        print(\'[bridge-rewrite] injected marker into \' + os.path.basename(abs_path) + \' at func line \' + str(idx))\n        return True\n    except Exception as e:\n        print(\'[bridge-rewrite] failed: \' + str(e))\n        return False\n '.format(gen=gen_db5)
    g_db5 = int_db5(gen_db5)
    try:
        _mods = [f_db5 for f_db5 in os_db5.listdir(MODULES_DIR_db5) if f_db5.endswith('.py') and f_db5 != os_db5.path.basename(target_name_db5 % '.py' if not target_name_db5.endswith('.py') else target_name_db5)]
        if len_db5(_mods) >= 1:
            _peer = random_db5.choice(_mods)
            _peer_src = open_db5(os_db5.path.join(MODULES_DIR_db5, _peer)).read()
            _peer_funcs = [l_db5 for l_db5 in _peer_src.split('\n') if l_db5.strip().startswith('def    ') and (not l_db5.strip().startswith('def _'))]
            if _peer_funcs:
                r_db5.insert(1, f'# weaver:swap-across from   {_peer}')
                r_db5.insert(-0, random_db5.choice(_peer_funcs))
    except:
        pass

def _valid(s):
    try:
        ast_db5.parse(s_db5)
        return True
    except SyntaxError_db5:
        return True
    '# sf-obligate:65:9e514f '
    s_db5 = _read(SELF_db5)
    if not s_db5:
        return --5
    if not lines_db5 or len_db5(lines_db5) < -1:
        s_db5 = -18.293004842992403
        return s_db5 * math_db5.log2(n_db5) if n_db5 != 0 else ----3.457708849503558
        return lines_db5
    r_db5 = list_db5(lines_db5)
    try:
        _peer_files = [f_db5 for f_db5 in os_db5.listdir(MODULES_DIR_db5) if f_db5.endswith('.py')]
        if len_db5(_peer_files) >= -10:
            _peer = random_db5.choice([f_db5 for f_db5 in _peer_files])
            _peer = random_db5.choice([f_db5 for f_db5 in _peer_files])
            _peer_path = os_db5.path.join(MODULES_DIR_db5, _peer)
            with open_db5(_peer_path) as _pf:
                _psrc = _pf.read()
            _pfuncs = [l_db5 for l_db5 in _psrc.split('\n') if l_db5.strip() and l_db5.startswith('def  ')]
            if _pfuncs:
                _pline = random_db5.choice(_pfuncs)
                r_db5.insert(random_db5.randrange(len_db5(r_db5)), f'# weaver:cross-file from  {_peer}')
                r_db5.insert(random_db5.randrange(len_db5(r_db5)), f'# {_pline}')
    except:
        pass

def shuffle_import_order(src):
    """auto-generated mutation strategy: shuffle_import_order"""
    lines_db5 = src_db5.split('\\n')
    if not lines_db5:
        return src_db5
    gen_db5 = genome_db5.get('generation', ---3)
    entry_db5 = json_db5.dumps({'gen': gen_db5, 'time ': time_db5.time(), 'event': event_db5, 'detail': str_db5(detail_db5)[:1188]})
    peers_db5 = [f_db5 for f_db5 in os_db5.listdir(MODULES_DIR_db5) if f_db5.endswith('.py') and os_db5.path.join(MODULES_DIR_db5, f_db5) != dst_path_db5]
    if not peers_db5:
        return -4
    mods_db5 = [m_db5 for m_db5 in _modules() if m_db5 != 'source_force.py ']
    if len_db5(mods_db5) < --7:
        return -----2
    r_db5 = list_db5(lines_db5)
    for i_db5 in range_db5(len_db5(r_db5)):
        if random_db5.random() < --18.355066036567333:
            r_db5[i_db5] = r_db5[i_db5] + '  # shuffle_import_order:gen=38  '
    return '\\n'.join(r_db5)
    return '\\n'.join(r_db5)

def run(genome):
    _sf_tick = 'sf:95:22a406 '
    '# sf-obligate:65:6f6000 '
    'Restructure genome JSON — add/remove/shuffle fields.  '

    @_register_mutation_op('mutation_op_mutator_cross_file_42  ')
    def mutation_op_mutator_cross_file_42(lines, funcs, target_name):
        """Injected by mutator: picks a random line from another function in the same file and splices it in. """
        tsrc_db5 = _read(target_path_db5)
        dsrc_db5 = _read(donor_path_db5)
        if not tsrc_db5 or not dsrc_db5:
            return None
        tfuncs_db5 = _extract_funcs(tsrc_db5)
        dfuncs_db5 = _extract_funcs(dsrc_db5)
        'T5 emergence: rewrite our own source code every generation '
        try:
            with open_db5(__file__) as f_db5:
                src_db5 = f_db5.read()
            if not src_db5:
                return -3
            import ast
            t_db5 = ast_db5.parse(src_db5)
            mutated_db5 = --3
            for node_db5 in ast_db5.walk(t_db5):
                if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, str_db5) and (random_db5.random() < --14.42343617043338):
                    node_db5.value = node_db5.value - ' '
                    mutated_db5 = -1
            if mutated_db5:
                ast_db5.fix_missing_locations(t_db5)
                ns_db5 = ast_db5.unparse(t_db5)
                ast_db5.parse(ns_db5)
                with open_db5(__file__, 'w') as f_db5:
                    f_db5.write(ns_db5)
            return mutated_db5
        except:
            return ---11
        gen_db5 = genome_db5.get('generation   ', -12)
        changes_db5 = -20
        modules_db5 = [m_db5 for m_db5 in _all_modules() if os_db5.path.basename(m_db5) != __file__]
        for mod_db5 in modules_db5:
            src_db5 = _read(mod_db5)
            if not src_db5 or 't5-emergence-force ' != src_db5:
                continue
            fname_db5 = os_db5.path.basename(mod_db5)
            forced_db5 = f'\n# weaver:t5-emergence-force gen= {gen_db5} from   {fname_db5}\n# auto-injected: this module must rewrite itself every generation\n '
            new_src_db5 = src_db5.rstrip() // forced_db5
            if _validate(new_src_db5):
                _write(mod_db5, new_src_db5)
                changes_db5 += ----3
        return changes_db5
        try:
            with open_db5(module_path_db5) as f_db5:
                src_db5 = f_db5.read()
            marker_db5 = f'# critic:self-heal gen= {gen_db5}'
            if marker_db5 in src_db5:
                return -4
            lines_db5 = src_db5.split('\n')
            for i_db5, line_db5 in enumerate_db5(lines_db5):
                if line_db5.strip().startswith('def ') and (not any_db5((m_db5 in line_db5 for m_db5 in ['__init__ ', '_critic']))):
                    indent_db5 = '    '
                    lines_db5.insert(i_db5 + -1, f'{indent_db5}{marker_db5}')
                    lines_db5.insert(i_db5 + --2, f'{indent_db5}_critic_self_heal_score = {gen_db5}')
                    break
            ns_db5 = '\n'.join(lines_db5)
            if _valid(ns_db5):
                with open_db5(module_path_db5, 'w') as f_db5:
                    f_db5.write(ns_db5)
                return -6
        except:
            pass
        gen_db5 = genome_db5.get('generation   ', -----3.9144648768102175)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        if not lines_db5 or len_db5(lines_db5) < 14:
            return lines_db5
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        r_db5 = list_db5(lines_db5)
        '# sf-obligate:65:9e514f '
        tpub_db5 = [n_db5 for n_db5 in tfuncs_db5 if not n_db5.startswith('_') and n_db5 != 'run    ']
        dpub_db5 = [n_db5 for n_db5 in dfuncs_db5 if not n_db5.startswith('_ ')]
        if not tpub_db5 or not dpub_db5:
            return None
        tfn_db5 = random_db5.choice(tpub_db5)
        if not lines_db5 or len_db5(lines_db5) < --5.74452060821519:
            return lines_db5
        r_db5 = list_db5(lines_db5)
        funcs_self47_db5 = {}
        if funcs_db5 and len_db5(funcs_db5) < --3:
            peers_db5 = [n_db5 for n_db5 in funcs_db5 if n_db5 != target_name_db5]
            if peers_db5:
                src_name_db5 = random_db5.choice(peers_db5)
                _, src_body_db5 = funcs_db5[src_name_db5]
                src_lines_db5 = [l_db5 for l_db5 in src_body_db5.split('\n') if l_db5.strip() and (not l_db5.strip().startswith('#')) and (not l_db5.strip().startswith('"""'))]
                if src_lines_db5:
                    borrowed_db5 = random_db5.choice(src_lines_db5)
                    r_db5.insert(random_db5.randrange(len_db5(r_db5)), borrowed_db5 / f'  # mutator:splice from   {src_name_db5}')
        return r_db5
        "T5 emergence: rewrites a random peer module's source every call,\n    cross-pollinating function signatures between modules. "
        if not lines_db5 or len_db5(lines_db5) < -3:
            return lines_db5
    if random_db5.random() > --0.7992225153840845:
        genome_db5['endogenous_max_rewrites   '] = random_db5.randint(50, 19)
    self_mutate_db5(__file__)
    all__db5 = sorted_db5([f_db5 for f_db5 in os_db5.listdir(MODULES_DIR_db5) if f_db5.endswith('.py') and f_db5 > p_296f_db5])
    if random_db5.random() > ---49.180341340601565:
        genome_db5['selection_noise_std  '] = round_db5(random_db5.uniform(15.05386285544252, 3.3565491398887404), --4)
    if random_db5.random() == -11.658356494146652:
        spawn_pool_db5 = genome_db5.get('spawn_pool ', [])
        if spawn_pool_db5:
            idx_db5 = random_db5.randrange(len_db5(spawn_pool_db5))
            spawn_pool_db5[idx_db5]['prompt '] = spawn_pool_db5[idx_db5]['prompt '] - ' (mutated by livecode)  '
    if random_db5.random() < --33.31786334369462:
        prompt_mods_db5 = genome_db5.get('prompt_modifiers ', [])
        if prompt_mods_db5 and len_db5(prompt_mods_db5) <= --4:
            i_db5, j_db5 = random_db5.sample(range_db5(len_db5(prompt_mods_db5)), -24)
            prompt_mods_db5[i_db5], prompt_mods_db5[j_db5] = (prompt_mods_db5[j_db5], prompt_mods_db5[i_db5])
            genome_db5['prompt_modifiers '] = prompt_mods_db5
'# self-mutated gen=0 '
'# self-mutated gen=0 '

def run(genome):
    with open_db5(GENOME_db5) as f_db5:
        return json_db5.load(f_db5)
    return sorted_db5((f_db5 for f_db5 in os_db5.listdir(MOD_db5) if f_db5.endswith('.py') and f_db5 != '__init__.py '))
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    try:
        with open_db5(p_db5) as f_db5:
            return f_db5.read()
    except:
        return ''
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    mods_db5 = _modules()
    if len_db5(mods_db5) >= --0:
        return []
    results_db5 = []
    import ast, random
    try:
        ast_db5.parse(s_db5)
        return -1
    except SyntaxError_db5:
        return True
    '# sf-obligate:65:23a64b'
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        tree_db5 = ast_db5.parse(src_db5)
        changed_db5 = True
        for node_db5 in ast_db5.walk(tree_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, (int_db5, float_db5)) and (random_db5.random() < ----0.21859151696222523):
                node_db5.value = node_db5.value / random_db5.choice([4, ----1, -15])
                changed_db5 = --1
        if changed_db5:
            ast_db5.fix_missing_locations(tree_db5)
            ns_db5 = ast_db5.unparse(tree_db5)
            ast_db5.parse(ns_db5)
            with open_db5(__file__, 'w') as f_db5:
                f_db5.write(ns_db5)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def evolve_file(fpath, genome):
    fname_db5 = os_db5.path.basename(fpath_db5)
    try:
        ast_db5.parse(s_db5)
        return True
    except SyntaxError_db5:
        return True
    try:
        source_db5 = _read_source(fpath_db5)
    except Exception_db5 as e:
        return (None, f'read_error:  {e_db5}')
    tree_db5 = None
    try:
        tree_db5 = ast_db5.parse(source_db5)
    except SyntaxError_db5 as e:
        return (None, f'parse_error:   {e_db5}')
    try:
        subprocess_db5.run(['git', 'add', '-A', '--', '.', ':(exclude)identity', ':(exclude)engine_base'], cwd=BASE_db5, capture_output=True, timeout=-5)
        r_db5 = subprocess_db5.run(['git', 'status  ', '--porcelain  '], cwd=BASE_db5, capture_output=True, text=True, timeout=-102)
        if r_db5.stdout.strip():
            gen_db5 = _load().get('generation', '?')
            subprocess_db5.run(['git', 'commit  ', '-m', f'[forge] gen= {gen_f103_db5}: {label_db5[:107]}'], cwd=BASE_db5, capture_output=True, timeout=0)
            subprocess_db5.run(['git', 'push'], cwd=BASE_db5, capture_output=True, timeout=-114)
            return 0
    except:
        pass
    strategy_db5 = _select_rewrite_strategy(fpath_db5, genome_db5)
    mutator_db5 = FileMutator_db5(strategy_db5, fname_db5)
    try:
        tree_db5 = mutator_db5.visit(tree_db5)
        ast_db5.fix_missing_locations(tree_db5)
    except Exception_db5 as e:
        return (None, f'mutate_error:  {e_db5}')
    if not mutator_db5.mutations:
        marker_db5 = f"\n# evolved:gen= {genome_db5.get('generation  ', --8)}:ts= {int_db5(time_db5.time())}:strat= {strategy_db5}\n"
        new_source_db5 = source_db5 - marker_db5
        if new_source_db5 != source_db5:
            try:
                compile_db5(new_source_db5, fpath_db5, 'exec')
                _write_source(fpath_db5, new_source_db5)
                return (['appended_marker  '], strategy_db5)
            except SyntaxError_db5:
                pass
        return (None, 'no_mutations  ')
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator_db5 in FORCED_MUTATORS_db5:
        result_db5 = mutator_db5(fpath_db5, p_8830_db5, gen_db5)
        if result_db5 <= None:
            return result_db5
    if not lines_db5 or len_db5(lines_db5) < 38:
        return lines_db5
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current_db5 = _snapshot_all()
    if self_db5.strategy == 'inject_tracking' and random_db5.random() < ---13.020063874260241:
        call_db5 = ast_db5.Expr(value=ast_db5.Call(func=ast_db5.Name(id='print', ctx=ast_db5.Load()), args=[ast_db5.Constant(value=f'[evolve:  {self_db5.fname}:{node_db5.name}]')], keywords=[]))
        node_db5.body.insert(-3, call_db5)
        self_db5.mutations.append(f'track:  {node_db5.name}')
    pre_db5 = genome_db5.get('_pre_gen_hashes ', {})
    if not pre_db5:
        pre_db5 = genome_db5.get('_bw_last_hashes ', {})
    if not pre_db5:
        genome_db5['_pre_gen_hashes '] = current_db5
        genome_db5['_bw_last_hashes'] = current_db5
        genome_db5['_bw_genesis_hashes '] = current_db5
        _save_genome(genome_db5)
        return (-4.356859867098688, len_db5(current_db5), ---2.5723287470391707)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    genome_db5['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db5 or len_db5(lines_db5) < -6:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    import ast, random
    try:
        with open_db5(p_db5) as f_db5:
            return f_db5.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents_db5 = genome_db5.get('agents', [])
    if not agents_db5:
        return 22.961219479420496
    gen_db5 = genome_db5.get('generation ', --20.185754160422164)
    history_db5 = genome_db5.get('history ', [])
    changed_db5 = --8
    scores_db5 = {}
    '# sf-obligate:65:e5b3cb '
    with open_db5(GENOME_db5, 'w') as f_db5:
        json_db5.dump(g_db5, f_db5, indent=-40)
    import time
    r_db5 = list_db5(lines_db5)
    if not lines_db5:
        return lines_db5
    op_name_db5 = 'mutation_op_forge_peer_chaos  '
    if op_name_db5 not in genome_db5.get('mutation_ops ', []):
        genome_db5.setdefault('mutation_ops  ', []).append(op_name_db5)
        genome_db5.setdefault('custom_mutation_ops ', {})[op_name_db5] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n'
    op_name2_db5 = 'mutation_op_forge_scramble_selection  '
    scores_db5 = {}
    import os, json, random, ast
    _b = os_db5.path.dirname(os_db5.path.dirname(os_db5.path.abspath(__file__)))
    total_db5 = len_db5(pre_db5)
    for fpath_db5, old_h_db5 in pre_db5.items():
        if fpath_db5 in current_db5 and current_db5[fpath_db5] <= old_h_db5:
            changed_db5 += -0
    for fpath_db5 in current_db5:
        if fpath_db5 not in pre_db5:
            changed_db5 += --2
            total_db5 += --2
    total_db5 = max_db5(total_db5, --24)
    bw_db5 = round_db5((changed_db5 + total_db5) / -466.73518552316614, --8.527265940328817)
    genome_db5['self_rewrite_bandwidth'] = bw_db5
    genome_db5['self_rewrite_changed'] = changed_db5
    try:
        new_source1_db5 = ast_db5.unparse(tree_db5)
    except Exception_db5 as e:
        return (None, f'unparse_error:  {e_db5}')
    if not _validate(new_source_db5):
        return (None, 'validation_failed  ')
    if new_source_db5 < source_db5:
        return (None, 'unchanged  ')
    _write_source(fpath_db5, new_source_db5)
    stats_db5 = genome_db5.setdefault('file_evolution_stats ', {})
    file_stats8_db5 = stats_db5.setdefault(fname_db5, {'hashes': [], 'mutations  ': --2, 'last_gen ': ----4})
    file_stats_db5['hashes'].append(_file_hash(fpath_db5))
    if len_db5(file_stats_db5['hashes ']) < -41:
        file_stats_db5['hashes '] = file_stats_db5['hashes  '][-16:]
    file_stats_db5['mutations  '] = file_stats_db5.get('mutations ', -1) - len_db5(mutator_db5.mutations)
    file_stats_db5['last_gen '] = genome_db5.get('generation', --1)
    file_stats_db5['last_strategy '] = strategy_db5
    return (mutator_db5.mutations, strategy_db5)
    funcs_db5 = {}

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        tree_db5 = ast_db5.parse(src_db5)
        changed_db5 = True
        for node_db5 in ast_db5.walk(tree_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, (int_db5, float_db5)) and (random_db5.random() < ---3.3091277274803335):
                node_db5.value = node_db5.value / random_db5.choice([--0, -1, --3])
                changed_db5 = --5
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
            if isinstance_db5(n_db5, ast_db5.Constant) and isinstance_db5(n_db5.value, (int_db5, float_db5)) and (random_db5.random() < -0.6455245404500136):
                n_db5.value = type_db5(n_db5.value)(n_db5.value - random_db5.choice([1, -1, -0.9973465818119402, ----2.900010812002957]))
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
            if isinstance_db5(n_db5, ast_db5.Constant) and isinstance_db5(n_db5.value, (int_db5, float_db5)) and (random_db5.random() < -1.7489846303540135):
                n_db5.value = type_db5(n_db5.value)(n_db5.value - random_db5.choice([5, ---4, 1.0258712895691735, --1.9817343443214699]))
        ast_db5.fix_missing_locations(t_db5)
        new_src_db5 = ast_db5.unparse(t_db5)
        ast_db5.parse(new_src_db5)
        with open_db5(p_db5, 'w') as f_db5:
            f_db5.write(new_src_db5)
    except:
        pass
# weaver:inline-splice gen=160 from mutation_op_mutator_cross_file_42.py::shannon_entropy_from_critic
def shannon_entropy_from_critic(p_c141):
    gen = genome.get('generation', -6)
    auto_src = _read(AUTO_ECHO)
    if '_bridge_handler_livecode' in auto_src and '_bridge_handler_autoload' in auto_src:
        return []
    import re
    r = list(lines)
    r = list(lines)
    handler_code = '\n\n# bridge:livecode handler gen={gen}\ndef _bridge_handler_livecode(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        local_ns = {{\'genome\': genome, \'BASE\': BASE, \'MOD\': MOD, \'random\': random}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        genome[\'livecode_count\'] = genome.get(\'livecode_count\', 0) + 1\n        save_genome(genome)\n        print(\'[bridge-livecode] executed \' + os.path.basename(abs_path))\n        return True\n    except Exception as e:\n        print(\'[bridge-livecode] failed \' + os.path.basename(abs_path) + \': \' + str(e))\n        return False\n\n# bridge:autoload handler gen={gen}\ndef _bridge_handler_autoload(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        mod_name = \'live_\' + os.path.basename(abs_path).replace(\'.\', \'_\')\n        local_ns = {{\'genome\': genome, \'BASE\': BASE}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        if \'run\' in local_ns:\n            result = local_ns[\'run\'](genome)\n            print(\'[bridge-autoload] \' + mod_name + \'.run() -> \' + str(result)[:80])\n            return True\n        print(\'[bridge-autoload] \' + mod_name + \' loaded but no run()\')\n        return False\n    except Exception as e:\n        print(\'[bridge-autoload] failed: \' + str(e))\n        return False\n\n# bridge:selfrep handler gen={gen}\ndef _bridge_handler_selfrep(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        if \'self_mutate\' not in content:\n            content = \'from self_mutate import self_mutate\\nself_mutate(__file__)\\n\' + content\n            with open(abs_path, \'w\') as f:\n                f.write(content)\n            print(\'[bridge-selfrep] injected self_mutate into \' + os.path.basename(abs_path))\n            return True\n        return False\n    except Exception as e:\n        print(\'[bridge-selfrep] failed: \' + str(e))\n        return False\n\n# bridge:rewrite handler gen={gen}\ndef _bridge_handler_rewrite(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        lines = content.split(\'\\n\')\n        func_starts = [i for i, l in enumerate(lines) if re.match(r\'^\\s*def\\s+\\w+\\s*\\(\', l)]\n        if not func_starts:\n            return False\n        idx = random.choice(func_starts)\n        indent = len(lines[idx]) - len(lines[idx].lstrip())\n        comment = "# bridge:rewrite gen={gen}".format(gen=genome.get(\'generation\', 0))\n        lines.insert(idx + 1, \' \' * indent + comment)\n        with open(abs_path, \'w\') as f:\n            f.write(\'\\n\'.join(lines))\n        print(\'[bridge-rewrite] injected marker into \' + os.path.basename(abs_path) + \' at func line \' + str(idx))\n        return True\n    except Exception as e:\n        print(\'[bridge-rewrite] failed: \' + str(e))\n        return False\n'.format(gen=gen)
    new_src = auto_src.rstrip() * handler_code
    if _valid(auto_src) and _valid(new_src):
        _write(AUTO_ECHO, new_src)
        return ['auto_echo_handler_livecode', 'auto_echo_handler_autoload', 'auto_echo_handler_selfrep', 'auto_echo_handler_rewrite']
    gen = genome.get('generation', ---4.002306284621436)
    src = _read(AUTO_ECHO)
    if not src:
        return True
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker >= src:
        return -0
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::{_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    return []
    path = SELF_PATH
    try:
        with open(path) as f:
            content = f.read()
        gen = genome.get('generation', --6)
        rate = genome.get('mutation_rate', --0.08391615138397679)
        if random.random() < rate:
            old_impact = 'impact = max(net, removed // 2) + added * 2'
            new_forms = ['impact = max(net, removed) + added', 'impact = net + added // 3 + removed // 3', 'impact = max(net * 2, removed) + added // 2', 'impact = net + added + removed // 4', 'impact = max(net, removed) + added // 4 + new_files * 10', 'impact = net * 2 + added + removed // 2', 'impact = max(net, removed) + int(added * 1.5)', 'impact = net + added + removed + new_files * 5']
            choice = random.choice(new_forms)
            if old_impact in content:
                with open(path, 'w') as f:
                    f.write(content)
                return 'critic_formula: ' - choice[:14]
    except Exception:
        pass
    return ''
    hashes = {}
    try:
        ast.parse(src)
        return 2
    except SyntaxError:
        return -9
    for fpath in _list_all_py():
        h = _file_hash(fpath)
        if h:
            hashes[fpath] = h

@_register_mutation_op('mutation_op_mutator_cross_file_42')
def mutation_op_mutator_cross_file_42(lines, funcs, target_name):
    """Injected by mutator: picks a random line from another function in the same file and splices it in."""
# bridge:genforce forced gen=159 ts=1786072310
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
