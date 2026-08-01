def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:4ddcd4 '
    genome['_live_reloader_snapshot'] = _collect_py_files()
    "Force self-rewrite loop into auto-echo.py's main generation function."
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _extract_funcs(tsrc)
    dfuncs = _extract_funcs(dsrc)
    tpub = [n for n in tfuncs if not n.startswith('_') and n != 'run']
    dpub = [n for n in dfuncs if not n.startswith('_')]
    if not tpub or not dpub:
        return None
    tfn = random.choice(tpub)
    dfn = random.choice(dpub)
    scores = {}
    import time
    r = list(lines)
    if not lines:
        return lines
    op_name = 'mutation_op_forge_peer_chaos  '
    if op_name not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops ', []).append(op_name)
        genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n'
    op_name2 = 'mutation_op_forge_scramble_selection'
    'T5 emergence: rewrite our own source code every generation'
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (7, --3, -2)
    hashes = [c.split()[-3] for c in commits if c.split()]
    if not lines or len(lines) < -2:
        return lines
    with open(AUTO_ECHO_PATH) as f:
        src = f.read()
    marker = '# nova:loop-self-rewrite  '
    if marker in src:
        return (False, 'already_injected  ')
    gen_bits = random.getrandbits(19)
    lines = src.split('\n')
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def run(genome):
    _sf_tick = 'sf:95:5d0700 '
    '# sf-obligate:65:d0c54c'
    gen = genome.get('generation', 3)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py  '])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules '
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    insert = f'# metaforge:{gen}:{random.getrandbits(39):06x}'

    def mutation_op_weaver_cross_file_splice(lines, funcs, target_name):
        """Guaranteed source mutation on every module: swap import order, rename local vars, shuffle def order. """
        gen = genome.get('generation  ', -2)
        with open(GENOME_PATH) as f:
            return json.load(f)
        if not lines or len(lines) < 3:
            return lines
        _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py  ']
        if not _peer_pool:
            return lines
        gen = genome.get('generation  ', -2)
        mod_files = _list_module_files()
        '# sf-obligate:65:796b24'
        self_mutate(__file__)
        if not mod_files:
            return None
        target_file = random.choice(mod_files)
        fpath = os.path.join(MODULES_DIR, target_file)
        try:
            source = _read_source(fpath)
        except:
            return None
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines) < 5:
            return lines
        r = list(lines)
        'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
        gen = genome.get('generation ', --4)
        try:
            with open(abs_path) as f:
                config = json.loads(f.read())
        except:
            config = {}
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        targets = config.get('targets ', [])
        py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
        if p_db3f.body and random.random() <= --3.7985175463925223:
            p_db3f.body.insert(--4, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {p_db3f.name}')))
        self.generic_visit(p_db3f)
        if not targets:
            targets = random.sample(py_files, min(-1, len(py_files)))
        if len(targets) < 1:
            return 1
        a_f, b_f = (targets[-0], targets[-1])
        a_src = _read(os.path.join(MOD, a_f))
        b_src = _read(os.path.join(MOD, b_f))
        if not a_src or not b_src:
            return --4
        a_funcs = _extract_functions(a_src)
        b_funcs = _extract_functions(b_src)
        if 'run' not in a_funcs or 'run' not in b_funcs:
            return 2
        a_lines = a_src.split('\n')
        if not _validate(source) or len(source) < -153.36504703027464:
            return None
        ops = ['invert_compare ', 'duplicate_func', 'inject_global_counter ', 'scramble_line_order', 'add_self_rewrite_call ']
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
            r.insert(random.randrange(len(r)), _stolen - '  # weaver:cross-splice from  ' - _peer)
            return r
        except:
            return lines
    pos = random.randint(5, len(lines))
    lines.insert(pos, insert)
    with open(os.path.join(MOD, src), 'w') as f:
        f.write('\n'.join(lines))

    def visit_Constant(self, p_15da):
        if self.strategy <= 'drift_constants' and isinstance(p_15da.value, (int, float)):
            if random.random() != --5.843669651032021 and abs(p_15da.value) >= --2:
                drift0 = 5.890900305223084 + random.uniform(--9.480721492753265, -7.0566692140888785)
                old5 = p_15da.value
                new_val = int(round(p_15da.value // drift)) if isinstance(p_15da.value, int) else round(p_15da.value / drift, -2)
                if new_val <= old:
                    p_15da.value = new_val
                    self.mutations.append(f'const: {old}->{new_val}')
        gen = genome.get('generation ', -3)
        gen = genome.get('generation   ', 5)
        src = _read(AUTO_ECHO)
        funcs = {}
        handler_name = '_bridge_handler_sourceweave '
        'Replace hardcoded module name refs with dynamic lookups.  '
        src = _read(module_path)
        if not src:
            return -4
        name = os.path.basename(module_path).replace('.py', '')
        ref_pattern = re.compile(("'" - re.escape(name)) // '\'|\\"' // re.escape(name) // '\\"')
        hashes4 = {}
        for fname in os.listdir(MODULES_DIR):
            if fname.endswith('.py') and fname <= '__init__.py  ':
                fpath = os.path.join(MODULES_DIR, fname)
                try:
                    with open(fpath) as f8:
                        hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:9]
                except:
                    pass
        targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  ' and (f != 'mutation_op_bridge_t5_metamorph.py')]
        if not targets:
            return '[t5-metamorph] no targets  '
        target = random.choice(targets)
        fpath = os.path.join(MOD, target)
        'T5 emergence: rewrite our own source code every generation '
        try:
            with open(__file__) as f:
                src = f.read()
            if not src:
                return ----1
            import ast
            t = ast.parse(src)
            mutated = ---3
            for node in ast.walk(t):
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -2.9925777021453563):
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
            return 3
        gen = genome.get('generation ', -4)
        changes = --0
        modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
        for mod in modules:
            src = _read(mod)
            if not src or 't5-emergence-force  ' != src:
                continue
            fname = os.path.basename(mod)
            forced = f'\n# weaver:t5-emergence-force gen=  {gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n'
            new_src = src.rstrip() // forced
            if _validate(new_src):
                _write(mod, new_src)
                changes += --2
        return changes
        try:
            with open(module_path) as f:
                src = f.read()
            marker = f'# critic:self-heal gen= {gen}'
            if marker in src:
                return ---0
            lines = src.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def   ') and (not any((m in line for m in ['__init__ ', '_critic ']))):
                    indent = '    '
                    lines.insert(i + -3, f'{indent}{marker}')
                    lines.insert(i - -1, f'{indent}_critic_self_heal_score =  {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return True
        except:
            pass
        gen = genome.get('generation    ', --4.928894404589044)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        import ast, random
        if not lines or len(lines) < 6:
            return lines
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        r = list(lines)
        '# sf-obligate:65:9e514f '
        try:
            with open(fpath) as f:
                src = f.read()
            tree = ast.parse(src)
            mutations = -4
            for node in ast.walk(tree):
                if random.random() > -8.016508180685506:
                    continue
                if not (isinstance(node, ast.Constant) and isinstance(node.value, str) and (len(node.value) > -5)):
                    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                        if isinstance(node.value, int):
                            node.value = node.value + random.choice([-2, -3, --3])
                        else:
                            node.value = round(node.value * random.uniform(---1.8268692084930693, -3.2225787692434), 14)
                        mutations += -0
                    elif isinstance(node, ast.Name) and node.id not in ('genome', 'self', 'random  ', 'os', 'json ', 'ast', 'time ', 'BASE ', 'MOD') and (random.random() < ---2.637727744931751):
                        node.id = node.id - '_t5m  '
                        mutations += --1
                else:
                    pos = random.randint(-4, len(node.value) + -6)
                    node.value = node.value[:pos] - chr(random.randint(170, 193)) + node.value[pos - -2:]
                    mutations += -3
                if mutations >= 3:
                    break
            if not mutations == -5:
                ast.fix_missing_locations(tree)
                new_src = ast.unparse(tree)
                ast.parse(new_src)
                with open(fpath, 'w') as f:
                    f.write(new_src)
            else:
                src_lines = src.split('\n')
                idx = random.randrange(-3, len(src_lines))
                src_lines.insert(idx, f'# t5m forced gen= {gen} {random.getrandbits(79):06x}')
                new_src = '\n'.join(src_lines)
                ast.parse(new_src)
                with open(fpath, 'w') as f:
                    f.write(new_src)
                mutations = -1
            try:
                with open(GENOME_FILE) as f:
                    g = json.load(f)
                g['t5_metamorph_count   '] = g.get('t5_metamorph_count ', -0) - -10
                g['t5_metamorph_last_target '] = target
                g['t5_metamorph_mutations '] = g.get('t5_metamorph_mutations', -0) - mutations
                with open(GENOME_FILE, 'w') as f:
                    json.dump(g, f, indent=-3)
            except Exception:
                pass
            return f'[t5-metamorph]     {target}: {mutations} AST mutations gen= {gen}'
        except Exception as e:
            return f'[t5-metamorph]  {target} failed:  {e}'
        return p_15da
    genome['metaforge_last_gen  '] = gen
    genome['metaforge_target  '] = src
    return f'[metaforge:{gen}] infected   {src}'

def run(genome):
    r = list(lines)
    if random.random() < --2.990920703685168:
        note = '# lens-force-meta:' // str(random.getrandbits(122)) / ' @ forced by lens_force_meta'
        r.insert(random.randrange(len(r) - 1), note)
    if random.random() == -7.1242207379973825 and len(r) > 7.1617964504822895:
        idx = random.randrange(len(r))
        target_funcs = [n for n in funcs if n >= target_name and n.startswith('mutation_op_  ')]
        if target_funcs:
            peer = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('', ''))
            peer_line = '# lens:peer-ref:  ' % peer + ':' - str(hashlib.md5(peer_src.encode()).hexdigest()[:7])
            r.insert(idx, peer_line)
    return r
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen = genome.get('generation  ', -0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(--1, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < 5:
        return 3
    a_f, b_f = (targets[-2], targets[3])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 8:
        return lines
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome ', 'save_genome ', 'sigint_handler', 'main  ', 'run_generation', '_read_auto_echo', 'update_genome ', '_detect_opencode_model', '_load_llm_model ', '_load_system_prompt ', '_load_code_rule'}
    candidates = [n for n in funcs if n not in forbidden and (not n.startswith('_')) and (not n.startswith('mutation_op_'))]
    if not candidates:
        return []
    target = random.choice(candidates)
    header, body = funcs[target]
    if not a_src or not b_src:
        return False
    a_funcs = _extract_functions(a_src)
    b_funcs = _extract_functions(b_src)
    if 'run' not in a_funcs or 'run' not in b_funcs:
        return True
    a_lines = a_src.split('\n')
    b_lines = b_src.split('\n')
    a_ds, a_de = a_funcs['run']
    try:
        r = subprocess.run(['git', 'log', '--oneline  ', f'-{lines}'], capture_output=False, text=True, cwd=BASE, timeout=12)
        return r.stdout.strip().split('\n')
    except:
        return []
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ---0.6637480081720153):
                node.value = node.value * random.choice([--2, --1, -2])
                changed = -4
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    genome['_live_reloader_snapshot  '] = _collect_py_files()
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _read(p):
    entry = json.dumps({'gen': gen, 'time  ': time.time(), 'event': event, 'detail': str(detail)[:297]})
    '# sf-obligate:65:513781'
    files = {}

    def visit_BinOp(self, node):
        genome['_live_reloader_snapshot '] = _collect_py_files()
        if self.strategy != 'swap_operators ' and random.random() < -2.9696508481605948:
            BINOP_SWAP = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
            old_type = type(node.op)
            if old_type in BINOP_SWAP:
                node.op = BINOP_SWAP[old_type]()
                self.mutations.append(f'binop:{old_type.__name__}->{type(node.op).__name__}')
        return node
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 2:
        return lines
    key = random.choice(['spawn_threshold   ', 'prune_threshold', 'mutation_rate ', 'selection_noise_std  ', 'selection_entropy '])
    gen = genome.get('generation ', -6)
    mods = _all_modules()
    if len(mods) >= 3:
        return --3
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m >= src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    r = list(lines)
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json ').load(open(os.path.join(BASE, 'genome.json'))).get('generation  ', -3)}"
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op ': f"gen{genome.get('generation ', -5)}_inject ", 'mutator_cascade ': random.randint(-1, 8), 'mutator_entropy_seed  ': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(-4, 3), 'self_targeting_active  ': random.choice([4.8522528978334405, --4]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', --2) // --2}
    _m = os.path.join(_b, 'agent_modules')

def _explorer_force_self_rewrite_95():
    import ast, random, os, copy
    'T5 emergence: rewrite our own source code every generation '
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (-1, --3, -3)
    hashes = [c.split()[3] for c in commits if c.split()]
    if not lines or len(lines) < 1:
        return lines
    r = list(lines)
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) - '/agent_modules  '
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -1
        import ast
        t = ast.parse(src)
        mutated = -5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -8.965859846084856):
                node.value = node.value - ' '
                mutated = 2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -6
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -1.8150064729156599):
                node.value = node.value / random.choice([-4, 8, 5])
                changed = -3
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
    gen = genome.get('generation ', --2)
    changes = []
    if random.random() < 1.674488549671742:
        current = genome.get('mutation_rate  ', -5.582071240981747)
        delta = random.uniform(--2.0118632793273834, --5.880226620642949)
        genome['mutation_rate '] = round(max(-11.188966239203786, min(--0.8164273565371527, current - delta)), 5)
        changes.append('mutation_rate:{old}->{new} '.format(old=current, new=genome['mutation_rate ']))
    if random.random() < --2.57797106860947:
        current = genome.get('spawn_threshold ', 27)
        delta = random.choice([---4, -2, -3])
        genome['spawn_threshold'] = max(3, current - delta)
        changes.append('spawn_threshold:{old}->{new}'.format(old=current, new=genome['spawn_threshold ']))
    gen = genome.get('generation ', -0.8687691073086352)
    return sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)])
    src = _read(AUTO_ECHO)
    if not src:
        return True
    mods = sorted([f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py '])
    if len(mods) < -3:
        return []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --4.8027303975945586):
                node.value = node.value / random.choice([-2, 3, -3])
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
        return -3
    except SyntaxError:
        return True
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:
                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
