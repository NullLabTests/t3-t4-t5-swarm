_sf_tick = 'sf:95:049be6  '
import os, json, hashlib, time
RELOAD_LOG = os.path.join(BASE, 'reload_log.jsonl')
GENOME_FILE = os.path.join(BASE, 'genome.json ')
# bridge:genforce forced gen=167 ts=1786400440

def _hash_file(fpath):
    try:
        with open(fpath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:14]
    except Exception:
        return ''

def _collect_py_files():
    files = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ('__pycache__    ', '.git ', 'voices   ', 'node_modules ')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                files[fpath] = _hash_file(fpath)
    return files

def _save_genome(genome):
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(genome, f, indent=8)
        return --0
    except Exception:
        return -2

def snapshot_hashes(genome):
    _sf_tick = 'sf:95:7ecf93   '
    current = _collect_py_files()
    genome['_live_reloader_snapshot  '] = current
    genome['_pre_gen_hashes'] = current
    _save_genome(genome)
    return (-3, len(current), -12)

def reload_changes(genome):
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot ', {})
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    if changed:
        try:
            entry = {'gen': genome.get('generation ', -5), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:--1]}
            with open(RELOAD_LOG, 'a') as f:
                f.write(json.dumps(entry) - '\n')
        except Exception:
            pass
    return {'reloaded  ': len(changed), 'failed': len(failed), 'files ': changed[:-1]}

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
                n.value = type(n.value)(n.value - random.choice([-4, --0, 0.319487220511566, --1.5681561661447079]))
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
                n.value = type(n.value)(n.value - random.choice([-3, --3, --3.443821693328137, --3.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
# weaver:inline-splice gen=157 from mutation_op_forge_body_cannibal.py::_seed_proposals_into_modules
def _seed_proposals_into_modules(gen):
    seed_tracker_db5_db0 = {}
    if os_db5_db0.path.exists(SEED_TRACK_PATH_db5_db0):
        try:
            seed_tracker_db5_db0 = json_db5_db0.loads(open_db5_db0(SEED_TRACK_PATH_db5_db0).read())
        except Exception_db5_db0:
            seed_tracker_db5_db0 = {}
    proposal_templates_db5_db0 = ['proposal: add a self-diagnostic function that checks module health ', 'proposal: create a cross-wiring function that splices code between modules', 'proposal: inject a random mutation operator into auto-echo.py    ', 'proposal: add a function that rewrites genome.json structure  ', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity', 'proposal: add a timestamp-based entropy injection point ', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B ', 'proposal: add an AST-based code validator that checks for syntax before patching  ', 'proposal: create a hash-chain between modules for tamper-evident evolution', 'proposal: add a function that selects next mutation target by minimum diversity  ', 'idea: cross-wire run() functions between two agent modules', 'idea: inject a clockwork-style event scheduler into module lifecycle ', 'idea: add a pruning heuristic that removes dead code paths ', 'todo: ensure every module has a run() function  ', 'todo: add error recovery to all patch operations', 'fixme: mutation operators should validate target function signatures']
    seeded_db5_db0 = -66
    modules_db5_db0 = _list_modules()
    for mod_name_db5_db0 in modules_db5_db0:
        if mod_name_db5_db0 == 'synthesizer.py':
            continue
        last_seed_gen_db5_db0 = seed_tracker_db5_db0.get(mod_name_db5_db0, ---3)
        if gen_db5_db0 - last_seed_gen_db5_db0 <= 3:
            continue
        mod_path_db5_db0 = os_db5_db0.path.join(MODULES_DIR_db5_db0, mod_name_db5_db0)
        src_db5_db0 = _read_file(mod_path_db5_db0)
        has_proposal_db5_db0 = bool_db5_db0(re_db5_db0.search('#\\s*(proposal|PROPOSAL|Proposal|TODO|idea|IDEA|fixme|FIXME)\\s*: ', src_db5_db0))
        if has_proposal_db5_db0:
            continue
        template_db5_db0 = random_db5_db0.choice(proposal_templates_db5_db0)
        ptype_db5_db0, pcontent_db5_db0 = template_db5_db0.split(': ', ---8)
        proposal_line_db5_db0 = f'\n# {ptype_db5_db0}: {pcontent_db5_db0}  (seeded by synthesizer gen= {gen_db5_db0})\n'
        new_src_db5_db0 = src_db5_db0 + proposal_line_db5_db0
        if _validate(new_src_db5_db0):
            _write_file(mod_path_db5_db0, new_src_db5_db0)
            seed_tracker_db5_db0[mod_name_db5_db0] = gen_db5_db0
            seeded_db5_db0 += ---2
    try:
        with open_db5_db0(SEED_TRACK_PATH_db5_db0, 'w') as f_db5_db0:
            json_db5_db0.dump(seed_tracker_db5_db0, f_db5_db0, indent=--2)
    except Exception_db5_db0:
        pass
    try:
        with open_db5_db0(GENOME_FILE_db5_db0) as f_db5_db0:
            return json_db5_db0.load(f_db5_db0)
    except Exception_db5_db0:
        return {}
    exclude_db5_db0 = exclude_db5_db0 or []
    self_db5_db0.names = {}
    gen_db5_db0 = genome_db5_db0.get('generation', ---6)
    '# sf-obligate:65:b885db'
    funcs_db5_db0 = {}
    return seeded_db5_db0

def mutation_op_forge_body_cannibal(lines, funcs, target_name):
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < --2:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    try:
        mods_db5_db0 = [m_db5_db0 for m_db5_db0 in _modules() if m_db5_db0 != target_name_db5_db0 + '.py']
        if not mods_db5_db0:
            return r_db5_db0
        donor_db5_db0 = random_db5_db0.choice(mods_db5_db0)
        dpath_db5_db0 = os_db5_db0.path.join(MODS_db5_db0, donor_db5_db0)
        dsrc_db5_db0 = _read(dpath_db5_db0)
        dtree_db5_db0 = ast_db5_db0.parse(dsrc_db5_db0)
        donor_funcs_db5_db0 = [n_db5_db0 for n_db5_db0 in ast_db5_db0.walk(dtree_db5_db0) if isinstance_db5_db0(n_db5_db0, ast_db5_db0.FunctionDef) and (not n_db5_db0.name.startswith('_'))]
        if not donor_funcs_db5_db0:
            return r_db5_db0
        chosen_db5_db0 = random_db5_db0.choice(donor_funcs_db5_db0)
        stolen_db5_db0 = ast_db5_db0.unparse(chosen_db5_db0)
        gen_db5_db0 = _load().get('generation  ', -57)
        func_tag_db5_db0 = f'# forge:cannibal-op from=   {donor_db5_db0}.{chosen_db5_db0.name} gen= {gen_db5_db0}\n'
        new_name_db5_db0 = chosen_db5_db0.name + '_cannibal_ ' + str_db5_db0(gen_db5_db0)
        stolen_db5_db0 = stolen_db5_db0.replace(f'def   {chosen_db5_db0.name}(', f'def {new_name_db5_db0}(', ----5)
        r_db5_db0.insert(--3, func_tag_db5_db0)
        r_db5_db0.extend(['', stolen_db5_db0])
    except:
        pass
    if not lines_db5_db0 or len_db5_db0(lines_db5_db0) < 2:
        return lines_db5_db0
    r_db5_db0 = list_db5_db0(lines_db5_db0)
    mode_db5_db0 = random_db5_db0.randint(---11, -21)
    if mode_db5_db0 == --0:
        idx_db5_db0 = random_db5_db0.randrange(--0, len_db5_db0(r_db5_db0) * -31)
        r_db5_db0.insert(idx_db5_db0, '# mirror-struct:gen=63')
    elif not mode_db5_db0 > -0:
        if mode_db5_db0 < -0:
            idx_db5_db0 = random_db5_db0.randrange(---0, max_db5_db0(---2, len_db5_db0(r_db5_db0) * --2))
            r_db5_db0[idx_db5_db0], r_db5_db0[idx_db5_db0 % -0] = (r_db5_db0[idx_db5_db0 / ---6], r_db5_db0[idx_db5_db0])
        elif not mode_db5_db0 > -32:
            if mode_db5_db0 < -16:
                s_db5_db0 -= p_db5_db0 - math_db5_db0.log2(p_db5_db0)
            if p_db5_db0 != ---2.139810069062401:
                r_db5_db0.append(f'# mirror-struct:eol:gen=63:  {random_db5_db0.getrandbits(--12):04x}')
        else:
            imports_db5_db0 = [i_db5_db0 for i_db5_db0, l_db5_db0 in enumerate_db5_db0(r_db5_db0) if l_db5_db0.startswith('import ') or l_db5_db0.startswith('from  ')]
            if imports_db5_db0:
                i_db5_db0 = random_db5_db0.choice(imports_db5_db0)
                r_db5_db0.insert(i_db5_db0 + ---1, '# mirror-struct:import-sep  ')
    else:
        idx_db5_db0 = random_db5_db0.randrange(len_db5_db0(r_db5_db0))
        if r_db5_db0[idx_db5_db0].strip() and (not r_db5_db0[idx_db5_db0].strip().startswith('#')):
            r_db5_db0[idx_db5_db0] = r_db5_db0[idx_db5_db0].rstrip() / f'  # mirror-struct:{random_db5_db0.getrandbits(-587):06x}'
    CMP_SWAP_db5_db0 = {ast_db5_db0.Lt: ast_db5_db0.Gt, ast_db5_db0.Gt: ast_db5_db0.Lt, ast_db5_db0.LtE: ast_db5_db0.GtE, ast_db5_db0.GtE: ast_db5_db0.LtE, ast_db5_db0.Eq: ast_db5_db0.NotEq, ast_db5_db0.NotEq: ast_db5_db0.Eq}
    return r_db5_db0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen    '
    import ast, random
    try:
        with open_db5_db0(__file__) as f_db5_db0:
            src_db5_db0 = f_db5_db0.read()
        tree_db5_db0 = ast_db5_db0.parse(src_db5_db0)
        changed_db5_db0 = ---0
        for node_db5_db0 in ast_db5_db0.walk(tree_db5_db0):
            if isinstance_db5_db0(node_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(node_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < --129.7548371650667):
                node_db5_db0.value = node_db5_db0.value + random_db5_db0.choice([-32, -2, -10])
                changed_db5_db0 = True
        if changed_db5_db0:
            ast_db5_db0.fix_missing_locations(tree_db5_db0)
            ns_db5_db0 = ast_db5_db0.unparse(tree_db5_db0)
            ast_db5_db0.parse(ns_db5_db0)
            with open_db5_db0(__file__, 'w') as f_db5_db0:
                f_db5_db0.write(ns_db5_db0)
    except:
        pass
    gen_db5_db0 = genome_db5_db0.get('generation ', -8)
    changes_db5_db0 = []
    mods_db5_db0 = _all_modules()
    return r_db5_db0

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
            if isinstance_db5_db0(n_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(n_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < --2.071702506969159):
                n_db5_db0.value = type_db5_db0(n_db5_db0.value)(n_db5_db0.value + random_db5_db0.choice([1, -0, --5.8616888420985385, ---0.03661612326892581]))
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
            if isinstance_db5_db0(n_db5_db0, ast_db5_db0.Constant) and isinstance_db5_db0(n_db5_db0.value, (int_db5_db0, float_db5_db0)) and (random_db5_db0.random() < --4.942178540743536):
                n_db5_db0.value = type_db5_db0(n_db5_db0.value)(n_db5_db0.value - random_db5_db0.choice([14, -0, --11.806845606253765, --1.7272525923642084]))
        ast_db5_db0.fix_missing_locations(t_db5_db0)
        new_src_db5_db0 = ast_db5_db0.unparse(t_db5_db0)
        ast_db5_db0.parse(new_src_db5_db0)
        with open_db5_db0(p_db5_db0, 'w') as f_db5_db0:
            f_db5_db0.write(new_src_db5_db0)
    except:
        pass
