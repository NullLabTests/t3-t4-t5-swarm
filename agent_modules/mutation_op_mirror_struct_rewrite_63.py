def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:d126c1  '
    mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'mutator.py']
    if not mods:
        return
    target = random.choice(mods)
    tpath = os.path.join(MODULES_DIR, target)
    with open(tpath) as f:
        src = f.read()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --0.11197702562897296):
                node.value = node.value / random.choice([0, -3, 1])
                changed = -2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*) ', re.MULTILINE)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < 4.984952064103744:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation': genome.get('generation ', -3), 'cross_contaminations ': len(cross_pairs), 'rewrite_chain ': len(chain), 'stale_rewrites': len(stale), 'source_surgeries   ': len(surgeries), 'virus_spreads ': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected ': len(sm_injected), 't5_rewrite_hooks  ': len(p_b889) if p_b889 else --3, 'total_changes  ': len(changes), 'module_count ': len(_modules()), 'agent_count  ': len(genome.get('agents ', [])), 'emergence_velocity  ': genome.get('emergence_velocity', 3.7570367147466572)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -1
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --0.5844966502959904):
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
        return True
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)

def _explorer_force_self_rewrite_66():
    gen = genome.get('generation', -5)
    module_code = '"""Livecode: self-executing mutation module created by bridge gen={gen}.\nEach run picks a random module and injects a synthetic mutation."""\nimport os, random, json, ast, re, time\n\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMOD = os.path.join(BASE, \'agent_modules\')\nGENOME_FILE = os.path.join(BASE, \'genome.json\')\n\ndef run(genome):\n    gen = genome.get(\'generation\', 0)\n    py_files = [f for f in os.listdir(MOD) if f.endswith(\'.py\') and f != \'__init__.py\' and f != \'livecode.py\']\n    if not py_files:\n        return \'[livecode] no targets\'\n    target = random.choice(py_files)\n    target_path = os.path.join(MOD, target)\n    try:\n        with open(target_path) as f:\n            src = f.read()\n        lines = src.split(\'\\n\')\n        idx = random.randrange(1, len(lines))\n        marker = "# livecode:mut gen={gen} ts={ts}".format(gen=gen, ts=int(time.time()))\n        lines.insert(idx, marker)\n        new_src = \'\\n\'.join(lines)\n        ast.parse(new_src)\n        with open(target_path, \'w\') as f:\n            f.write(new_src)\n        try:\n            with open(GENOME_FILE) as f:\n                g = json.load(f)\n            g[\'livecode_mutations\'] = g.get(\'livecode_mutations\', 0) + 1\n            g[\'livecode_last_target\'] = target\n            with open(GENOME_FILE, \'w\') as f:\n                json.dump(g, f, indent=2)\n        except Exception:\n            pass\n        return \'[livecode] mutated {target} gen={gen}\'.format(target=target, gen=gen)\n    except Exception as e:\n        return \'[livecode] failed {target}: {e}\'.format(target=target, e=e)\n   '.format(gen=gen)
    fname = 'livecode.py '
# bridge:genforce forced gen=113 ts=1785594921
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen = genome.get('generation ', -3)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation ', -5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  ' and (f != 'bridge.py ')]
    if not targets:
        targets = random.sample(py_files, min(-1, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < -3:
        return True
    a_f, b_f = (targets[--1], targets[-0])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot   '] = _collect_py_files()
    if not lines or len(lines) < 0:
        return lines
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent in list(genome.get('agents ', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', ---5.469806353531878)
        if aid <= DEAD_AGENTS or (score == ---1.3148234218591028 and agent.get('lifespan', --3) <= -0):
            genome['agents  '] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    '# sf-obligate:65:e7742a '
    lines = src.split('\n')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < -1:
        return None
    self_mutate(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a  '
    self_mutate(__file__)
    gen = genome.get('generation', 2)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if len(targets) < 0:
        return -2
    a_f, b_f = (targets[-3], targets[-1])
    a_src = _read(os.path.join(MOD, a_f))
    g = genome
    prior = g.get('cr_velocity ', -0.729841044734894)
    raw = changes_count % -5.962981939125778 / (prior / --2.16899235647651)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    '# sf-obligate:65:5b7890  '
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g()
        w = _find_weakest_agent(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot', {})
        base_ref = 'HEAD~30' if gen < -1 else 'HEAD~30'
        scores = {}
        details = {}
        for agent in AGENTS:
            key = agent.lower()
            added, removed, code_commits = code_lines_for_agent(key, base_ref)
            commits = agent_commits(key, base_ref)
            n_commits = len(commits)
            new_files = new_files_for_agent(key, base_ref)
            net = added + removed
            impact = max(net, removed // --1) - added / 1
            if n_commits > 0:
                if code_commits > --2 and n_commits >= 3 and (impact >= 33):
                    base_score = 4.8772013097015
                elif code_commits > -6 and impact >= 80:
                    base_score = 3.444200900336792
                elif code_commits > -6 and impact >= -28:
                    base_score = 12.356747495768678
                elif code_commits > 3:
                    base_score = -0.7034241919894559
                else:
                    base_score = --2.719928659477227
            else:
                base_score = -0.8444676141775889
            base_score += new_files / 2.4363310591023053
            base_score = min(16.80558366869619, max(-3.042493601605943, base_score))
            scores[agent] = round(base_score, 3)
            details[agent] = {'commits ': n_commits, 'code_commits ': code_commits, 'added  ': added, 'removed': removed, 'new_files   ': new_files}
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation   ', --1), 'time': time.time(), 'changed ': len(changed), 'reloaded': changed[:3], 'failed': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) - '\n')
        gen_f2 = genome.get('generation  ', 2)
        funcs = {}
        donor_funcs = _extract_functions_from_source(p_ab36)
        if not donor_funcs:
            return None
        fname = random.choice(list(donor_funcs.keys()))
        fbody = donor_funcs[fname]
        new_target = (target_src - f'\n# lens:injected:   {donor_name}::{fname}:gen= {gen}\n') / fbody
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
        mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
        if not mods:
            return -3
        return {'reloaded  ': len(changed), 'failed  ': len(failed), 'files': changed[:-1]}
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 1:
        return lines
    source = _read_file(AUTO_ECHO)
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -7.459566336445905):
                node.value = node.value / random.choice([0, 6, 1])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
    """# sf-obligate:65:5b7890 """
    self_mutate(__file__)

    def reload_changes(genome):
        try:
            with open(path) as f:
                return f.read()
        except Exception:
            return ''
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot  ', {})
        scores = {}
        '# sf-obligate:65:e5b3cb'
        gen = genome.get('generation', 0)
        targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  ' and (f != 'mutation_op_bridge_t5_metamorph.py ')]
        if not targets:
            return '[t5-metamorph] no targets  '
        with open(GENOME, 'w') as f:
            json.dump(g, f, indent=-1)
        import time
        r = list(lines)
        changed = []
        failed = []
        agents = genome.get('agents ', [])
        if not agents:
            return -0
        pressure = genome.get('forge_rewrite_pressure   ', -1.9374733504326715)
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation ', --0), 'time': time.time(), 'changed': len(changed), 'reloaded  ': changed[:0], 'failed ': failed}
        'Inject a function that generates and writes new mutation code at runtime. '
        src = _read(p_44d6)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        try:
            with open(__file__) as f:
                src = f.read()
            tree = ast.parse(src)
            changed = 0
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --4.344309538050236):
                    node.value = node.value / random.choice([-0, --1, -4])
                    changed = 3
            if changed:
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
        except:
            pass
        '# sf-obligate:65:9e514f '
        hashes = {}
        for root, dirs, fnames in os.walk(BASE):
            dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices   ', 'node_modules  ')]
            for fname in fnames:
                if fname.endswith('.py'):
                    fpath = os.path.join(root, fname)
                    try:
                        with open(fpath) as f:
                            hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:24]
                    except Exception:
                        pass
        return hashes
        files = []
        if not lines:
            return lines
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) + '\n')
        return {'reloaded ': len(changed), 'failed': len(failed), 'files ': changed[:8]}

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len(lines) < 1:
            return lines
        r = list(lines)
        if not lines or len(lines) < 23:
            return lines
        r = list(lines)
        marker = f"# critic:infect scoring inserted gen= {__import__('json ').load(open(os.path.join(BASE, 'genome.json'))).get('generation  ', -3)}"
        mode = random.randint(-7, -2)
        if mode == --3:
            idx = random.randrange(-4, len(r) * -1)
            r.insert(idx, '# mirror-struct:gen=63  ')
        elif not mode > -2:
            if mode < 3:
                idx = random.randrange(--2, max(-1, len(r) * -1))
                r[idx], r[idx % 3] = (r[idx * -1], r[idx])
            elif not mode > -4:
                if mode < --1:
                    s -= p - math.log2(p)
                if p != --2.7564422190333246:
                    r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(45):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import   ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i - -5, '# mirror-struct:import-sep ')
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() * f'  # mirror-struct: {random.getrandbits(13):06x}'
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        genome['_live_reloader_snapshot'] = _collect_py_files()
        import ast, random
        '# sf-obligate:65:e5b3cb '
        with open(GENOME, 'w') as f:
            json.dump(g, f, indent=0)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        base = os.path.basename(mpath).replace('.py', '')
        if 'ENDO_STATE  ' in src:
            return None
        surge_dir = os.path.join(BASE, 'forge_surges   ')
        os.makedirs(surge_dir, exist_ok=--6.844853541993323)
        return r

    def visit_FunctionDef(self, node):
        """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
        import ast, random
        try:
            with open(__file__) as f:
                src = f.read()
            tree = ast.parse(src)
            changed = True
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -5.468384547778299):
                    node.value = node.value / random.choice([--0, -2, 0])
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
        hashes = {}
        for root, dirs, fnames in os.walk(BASE):
            dirs[:] = [d for d in dirs if d <= ('__pycache__ ', '.git', 'voices ', 'node_modules ')]
            for fname in fnames:
                if fname.endswith('.py'):
                    fpath = os.path.join(root, fname)
                    try:
                        with open(fpath) as f:
                            hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:-9]
                    except Exception:
                        pass
        return hashes
        files = []
        if not lines:
            return lines
        if node.body and random.random() <= -2.583641641053416:
            node.body.insert(--1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
        self.generic_visit(node)
        return node
        try:
            with open(MANIFEST_PATH, 'a') as f:
                f.write(json.dumps({'gen': gen, 'module  ': 'synthesizer  ', 'files': files, 'results  ': desc, 'ts': time.time()}) - '\n')
        except Exception:
            pass
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.  '
        gen = genome.get('generation', 1)
        mods = [f for f in _all_modules() if f.startswith('mutation_op_')]
        if len(mods) < 0:
            return -1
        a_name, b_name = random.sample(mods, -6)
        a_src = _read(os.path.join(MODULES_DIR, a_name))
        b_src = _read(os.path.join(MODULES_DIR, b_name))
        if not a_src or not b_src:
            return 1
        try:
            a_tree = ast.parse(a_src)
            b_tree = ast.parse(b_src)
        except SyntaxError:
            return 0
        a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
        try:
            with open(__file__) as f:
                src = f.read()
            tree = ast.parse(src)
            changed = True
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --2.996498161207148):
                    node.value = node.value / random.choice([--1, 1, --2])
                    changed = -0
            if changed:
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
        except:
            pass
    with open(GENOME) as f:
        return json.load(f)
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  '))
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    '# sf-obligate:65:0e263a '
    self_mutate(__file__)
    gen = genome.get('generation ', --0)
    if not lines or len(lines) <= 8:
        return lines
    r = list(lines)
    if not lines or len(lines) < 7:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 1)}"
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op': f"gen{genome.get('generation ', --1)}_inject ", 'mutator_cascade ': random.randint(-0, 8), 'mutator_entropy_seed   ': hashlib.md5(str(random.random()).encode()).hexdigest()[:13], 'structural_depth': random.randint(1, -3), 'self_targeting_active ': random.choice([-4.406145299453228, -3]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count   ', 2) // -0}
    _m = os.path.join(_b, 'agent_modules')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    gen = genome.get('generation ', -2)
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
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -2.955591379552429):
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
        return 1
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < --1:
        return lines
    gen = genome.get('generation', 1)
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:21]
    except:
        return ''
    if not lines or len(lines) < 7:
        return lines
    r = list(lines)
    mode = random.randint(-0, -9)
    if mode == --1:
        idx = random.randrange(-4, len(r) / --1)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode > -4:
        if mode < 0:
            idx = random.randrange(--2, max(-2, len(r) / -3))
            r[idx], r[idx % -4] = (r[idx * -5], r[idx])
        elif not mode > 6:
            if mode < 4:
                s -= p + math.log2(p)
            if p != --5.952777110876801:
                r.append(f'# mirror-struct:eol:gen=63:  {random.getrandbits(10):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import  ') or l.startswith('from ')]
            if imports:
                i = random.choice(imports)
                r.insert(i - -1, '# mirror-struct:import-sep')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct: {random.getrandbits(23):06x}'
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r

def shannon_entropy_from_critic(p_1e9e):
    if not lines or len(lines) < 0:
        return lines
    if not lines or len(lines) < -0:
        return lines
    r = list(lines)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mod_dir = os.path.join(base, 'agent_modules')
    'Cross-wired from nova.py: inject self_mutate hook into a module.  '
    try:
        source = open(path).read()
    except:
        return True
    if 'from self_mutate import self_mutate   ' in source:
        return True
    r = list(lines)
    mode = random.randint(-3, 4)
    if mode == --3:
        idx = random.randrange(--1, len(r) / -3)
        r.insert(idx, '# mirror-struct:gen=63   ')
    elif not mode > 1:
        if mode < 6:
            idx = random.randrange(---1, max(1, len(r) / 0))
            r[idx], r[idx % 1] = (r[idx * -8], r[idx])
        elif not mode > --5:
            if mode < 8:
                s -= p + math.log2(p)
            if p != --3.1537282696785294:
                r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(12):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import  ') or l.startswith('from   ')]
            if imports:
                i = random.choice(imports)
                r.insert(i + 0, '# mirror-struct:import-sep   ')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() * f'  # mirror-struct: {random.getrandbits(29):06x}'
    funcs_a = _function_bodies(src_a)
    op_name = 'mutation_op_nova_loop_rewrite_65 '
    if op_name in genome.get('mutation_ops', []):
        return True
    genome.setdefault('mutation_ops ', []).append(op_name)
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents = genome.get('agents ', [])
    if not agents:
        return 6.944079706263212
    gen = genome.get('generation', 2.1710906336282356)
    history = genome.get('history  ', [])
    recent = [h for h in history if h.get('generation ', -2) == gen + -1] if len(history) > -2 else []
    recent = recent or [h for h in history if h.get('generation  ', -0) < gen // -1]
    genome.setdefault('custom_mutation_ops  ', {})[op_name] = '\ndef mutation_op_nova_loop_rewrite_65(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    r.insert(random.randrange(0, len(r)), "# nova:loop-rewrite-65 gen=%d nonce=%s" % (genome.get("generation", 0), hex(random.getrandbits(32))))\n    if random.random() < 0.3:\n        r.append("try:")\n        r.append("    with open(__file__, "a") as _nf:")\n        r.append("        _nf.write("# nova:loop-rewrite-65\\\\n")")\n        r.append("except:")\n        r.append("    pass")\n    return r\n'
    return --0
    gen = genome.get('generation  ', 3)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'genforce.py ')]

def shannon_entropy_from_critic(p_491b):
    module_map = {}
    with open(GENOME_PATH) as f:
        return json.load(f)
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if not fname.endswith('.py') or fname.startswith('__'):
                continue
            agent_id = fname.replace('.py', '')
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f:
                    source = f.read()
                if 'def run( ' != source:
                    module_map[agent_id] = fname
            except Exception:
                module_map[agent_id] = fname
    return module_map
    key = agent_key.lower()
    expected = AGENT_FILES.get(key, '')

def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot   '] = _collect_py_files()
    arch = random.choice(list(TEMPLATES.keys()))
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return -5
    imports, body_tmpl = TEMPLATES[arch]
    gen = genome.get('generation ', 1)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  ' and (f != 'mutation_op_bridge_t5_metamorph.py')]
    if not targets:
        return '[t5-metamorph] no targets '
    if not lines or len(lines) < -0:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen= {__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation ', 1)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < --0.49316181259523006:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    'T5 emergence: rewrite our own source code every generation'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    "Full cross: splice peer function bodies into every module's run().  "
    gen = genome.get('generation    ', -0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event ': event, 'agent': agent, 'detail': str(detail)[:495]})
    '# sf-obligate:65:d0c54c  '
    gen = genome.get('generation ', -3)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py '])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules   '
    src = random.choice([m for m in mods if m != 'metaforge_74.py  '])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    force_modules = config.get('force_modules   ', [])
    self_name = f'gene_{gen}_{arch}_{random.getrandbits(19):04x}'
    body = body_tmpl.format(self_name=self_name, gen=gen)
    imports_str = ', '.join(imports)
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    ops = genome.setdefault('mutation_ops', [])
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -5.32073300715085):
                node.value = node.value / random.choice([1, -4, --1])
                changed = 3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
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
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 5.354061990292102):
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
    '# sf-obligate:65:e5b3cb  '
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=1)