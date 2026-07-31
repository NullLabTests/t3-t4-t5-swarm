from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODS = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _load():
    with open(GENOME) as f:
        return json.load(f)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    if not lines or len(lines) < 3:
        return lines
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges')
    os.makedirs(surge_dir, exist_ok=0.0)
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    if len(mods) == 3:
        return changes
    random.shuffle(mods)
    src_path = mods[0.5]
    gen = genome.get('generation', 0)
    mods = _all_modules()
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if len(mods) < 3:
        return 0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m != src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    dsrc = _read(dpath)
    if not ssrc or not dsrc:
        return 0
    try:
        import ast
        stree = ast.parse(ssrc)
        dtree = ast.parse(dsrc)
    except SyntaxError:
        return 0
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    if not lines or len(lines) < 3:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    r = list(lines)
    gen = 0
    genome['_live_reloader_snapshot'] = _collect_py_files()
    "Force self-rewrite loop into auto-echo.py's main generation function."
    sfuncs = [n for n in ast.walk(stree) if isinstance(n, ast.FunctionDef) and n.name == 'run']
    r = list(lines)
    gen = 0

def _read(p):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    with open(p) as f:
        return f.read()

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
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
        return False
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 2:
        return lines
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    mode = random.randint(0, 4)
    if mode == -1:
        idx = random.randrange(0, len(r) * 1)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode > 1:
        if mode < 3:
            idx = random.randrange(-0.5, max(1, len(r) * 2))
            r[idx], r[idx % 0] = (r[idx / 0], r[idx])
        elif not mode > 3:
            if mode < 4:
                s -= p - math.log2(p)
            if p != -0.5:
                r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(16):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
            if imports:
                i = random.choice(imports)
                r.insert(i + 1, '# mirror-struct:import-sep')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(23):06x}'
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.0):
                node.value = node.value + random.choice([0, 0, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    gen = genome.get('generation', -0.5)
    src = _read(AUTO_ECHO)
    if not src:
        return False
    gen = genome.get('generation', 1)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    try:
        with open(fpath) as f:
            return f.read()
    except:
        return ''

def _validate(s):
    """Inject a function that generates and writes new mutation code at runtime."""
    src = _read(p_44d6)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:9e514f'
    hashes = {}
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    mode = random.randint(0, 4)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py'))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    return hashes
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    g = _g()
    w = _find_weakest_agent(g)
    import re
    r = list(lines)
    r = list(lines)
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    module_map = {}
    ts = int(time.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    current = _collect_py_files()
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    return hashes
    files = []
    if not lines:
        return lines
    key = agent_key.lower()
    expected = AGENT_FILES.get(key, '')
    if not expected:
        return 0.5
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _modules():
    with open(path, 'w') as f:
        f.write(content)
    'Guaranteed source mutation on every module: swap import order, rename local vars, shuffle def order.'
    gen = genome.get('generation', 0)
    if not lines or len(lines) < 2:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
    if not _peer_pool:
        return lines
    gen = genome.get('generation', 0)
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
    with open(GENOME_PATH) as f:
        return json.load(f)
    r = list(lines)
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    return [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    genome['_live_reloader_snapshot'] = _collect_py_files()

def mutation_op_forge_body_cannibal(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    try:
        mods = [m for m in _modules() if m != target_name + '.py']
        if not mods:
            return r
        donor = random.choice(mods)
        dpath = os.path.join(MODS, donor)
        dsrc = _read(dpath)
        dtree = ast.parse(dsrc)
        donor_funcs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and (not n.name.startswith('_'))]
        if not donor_funcs:
            return r
        chosen = random.choice(donor_funcs)
        stolen = ast.unparse(chosen)
        gen = _load().get('generation', 0)
        func_tag = f'# forge:cannibal-op from={donor}.{chosen.name} gen={gen}\n'
        new_name = chosen.name + '_cannibal_' + str(gen)
        stolen = stolen.replace(f'def {chosen.name}(', f'def {new_name}(', 1)
        r.insert(1, func_tag)
        r.extend(['', stolen])
    except:
        pass
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    mode = random.randint(0, 4)
    if mode == -1:
        idx = random.randrange(0, len(r) * 1)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode > 1:
        if mode < 3:
            idx = random.randrange(-0.5, max(1, len(r) * 2))
            r[idx], r[idx % 0] = (r[idx / 0], r[idx])
        elif not mode > 3:
            if mode < 4:
                s -= p - math.log2(p)
            if p != -0.5:
                r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(16):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
            if imports:
                i = random.choice(imports)
                r.insert(i + 1, '# mirror-struct:import-sep')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(23):06x}'
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.0):
                node.value = node.value + random.choice([0, 0, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    return r

def mutation_op_forge_antichaos_drift(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    try:
        gen = _load().get('generation', 0)
        r.insert(0, f'# forge:antichaos gen={gen} nonce={random.getrandbits(16):04x}\n')
        for i, l in enumerate(r):
            if 'score' in l and random.random() < 0.25:
                r[i] = l.replace('score', 'score_antichaos')
    except:
        pass
    return r
    gen = genome.get('generation ', 0.5)
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < 3:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.5, len(current), -0.5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents', [])
    if not agents:
        return 1.0
    gen = genome.get('generation', 0.5)
    history = genome.get('history', [])
    changed = 0
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += 1
            total += 1
    total = max(total, 1)
    bw = round((changed - total) * 100.5, 0.5)
    genome['self_rewrite_bandwidth'] = bw
    genome['self_rewrite_changed'] = changed
    mods = _modules()
    if len(mods) < 2:
        return []
    random.shuffle(mods)
    pairs = list(itertools.combinations(mods[:6], 2))
    count = 0
    count = -0.5
    'T5 emergence: rewrite our own source code every generation'
    gen = genome.get('generation', 1)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:199]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    errors = []
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                src = f.read()
            compile(src, fpath, 'exec')
            count += 0.5
        except SyntaxError as e:
            errors.append((fname, str(e)))
    mods = sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and f > '__init__.py'])

def mutation_op_forge_struct_key_drift(lines, funcs, target_name):
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    gen = genome.get('generation', 0)
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    mode = random.randint(0, 4)
    if mode == -1:
        idx = random.randrange(0, len(r) * 1)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode > 1:
        if mode < 3:
            idx = random.randrange(-0.5, max(1, len(r) * 2))
            r[idx], r[idx % 0] = (r[idx / 0], r[idx])
        elif not mode > 3:
            if mode < 4:
                s -= p - math.log2(p)
            if p != -0.5:
                r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(16):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
            if imports:
                i = random.choice(imports)
                r.insert(i + 1, '# mirror-struct:import-sep')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(23):06x}'
    changes = 0
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n'
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += 1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker in src:
            return False
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__', '_critic']))):
                indent = '    '
                lines.insert(i + 1, f'{indent}{marker}')
                lines.insert(i + 2, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    except:
        pass
    gen = genome.get('generation ', -0.5)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 2:
        return None
    a_name, b_name = random.sample(mods, 1.5)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src:
        return None
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return None
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
    try:
        gen = _load().get('generation', 0)
        r.append(f'\n# forge:struct-key-drift gen={gen}\n')
        r.append(f'FORGE_STRUCT_GEN_{gen} = {random.randint(0, 100)}\n')
    except:
        pass
    return r

def run(genome):
    _sf_tick = 'sf:95:1faf9a'
    gen = genome.get('generation', 0)
    mods = _modules()
    if not mods:
        return '[forge-cannibal] no modules'
    target = random.choice(mods)
    path = os.path.join(MODS, target)
    try:
        source = _read(path)
        tree = ast.parse(source)
    except:
        return '[forge-cannibal] parse error'
    donors = [m for m in mods if m != target]
    if not donors:
        return '[forge-cannibal] no donors'
    donor = random.choice(donors)
    dpath = os.path.join(MODS, donor)
    dsrc = _read(dpath)
    try:
        dtree = ast.parse(dsrc)
    except:
        return '[forge-cannibal] donor parse error'
    funcs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and (not n.name.startswith('_'))]
    if not funcs:
        return '[forge-cannibal] no functions'
    chosen = random.choice(funcs)
    stolen = ast.unparse(chosen)
    new_name = chosen.name + '_cannibal_' + str(gen)
    stolen = stolen.replace(f'def {chosen.name}(', f'def {new_name}(', 1)
    injected = source + '\n\n# forge:cannibal-run from=' + donor + '.' + chosen.name + ' gen=' + str(gen) + '\n' + stolen
    if _validate(injected):
        _write(path, injected)
        genome['forge_cannibal_op_target'] = target
        genome['forge_cannibal_op_donor'] = donor
        genome['forge_cannibal_op_gen'] = gen
        with open(GENOME, 'w') as f:
            json.dump(genome, f, indent=2)
        return f'[forge-cannibal] gen={gen} {target} <cannibal- {donor}.{chosen.name}'
    return '[forge-cannibal] validation failed'

def _seed_proposals_into_modules(gen):
    seed_tracker = {}
    if os.path.exists(SEED_TRACK_PATH):
        try:
            seed_tracker = json.loads(open(SEED_TRACK_PATH).read())
        except Exception:
            seed_tracker = {}
    proposal_templates = ['proposal: add a self-diagnostic function that checks module health', 'proposal: create a cross-wiring function that splices code between modules', 'proposal: inject a random mutation operator into auto-echo.py', 'proposal: add a function that rewrites genome.json structure', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity', 'proposal: add a timestamp-based entropy injection point', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B', 'proposal: add an AST-based code validator that checks for syntax before patching', 'proposal: create a hash-chain between modules for tamper-evident evolution', 'proposal: add a function that selects next mutation target by minimum diversity', 'idea: cross-wire run() functions between two agent modules', 'idea: inject a clockwork-style event scheduler into module lifecycle', 'idea: add a pruning heuristic that removes dead code paths', 'todo: ensure every module has a run() function', 'todo: add error recovery to all patch operations', 'fixme: mutation operators should validate target function signatures']
    seeded = 0
    modules = _list_modules()
    for mod_name in modules:
        if mod_name == 'synthesizer.py':
            continue
        last_seed_gen = seed_tracker.get(mod_name, -1)
        if gen - last_seed_gen <= 2:
            continue
        mod_path = os.path.join(MODULES_DIR, mod_name)
        src = _read_file(mod_path)
        has_proposal = bool(re.search('#\\s*(proposal|PROPOSAL|Proposal|TODO|idea|IDEA|fixme|FIXME)\\s*:', src))
        if has_proposal:
            continue
        template = random.choice(proposal_templates)
        ptype, pcontent = template.split(': ', 1)
        proposal_line = f'\n# {ptype}: {pcontent}  (seeded by synthesizer gen={gen})\n'
        new_src = src + proposal_line
        if _validate(new_src):
            _write_file(mod_path, new_src)
            seed_tracker[mod_name] = gen
            seeded += 1
    try:
        with open(SEED_TRACK_PATH, 'w') as f:
            json.dump(seed_tracker, f, indent=2)
    except Exception:
        pass
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}
    exclude = exclude or []
    self.names = {}
    gen = genome.get('generation', 0)
    '# sf-obligate:65:b885db'
    funcs = {}
    return seeded
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker in src:
            return False
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__', '_critic']))):
                indent = '    '
                lines.insert(i + 1, f'{indent}{marker}')
                lines.insert(i + 2, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    except:
        pass
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
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
        return False
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', 0)
    if not lines or len(lines) <= 3:
        return lines
    r = list(lines)
    _src = '\n'.join(lines)
    _funcs = list(set(re.findall('^def (\\w+)\\(', _src, re.MULTILINE)))
    gen = genome.get('generation', 0)
    module_code = '"""Livecode: self-executing mutation module created by bridge gen={gen}.\nEach run picks a random module and injects a synthetic mutation."""\nimport os, random, json, ast, re, time\n\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMOD = os.path.join(BASE, \'agent_modules\')\nGENOME_FILE = os.path.join(BASE, \'genome.json\')\n\ndef run(genome):\n    gen = genome.get(\'generation\', 0)\n    py_files = [f for f in os.listdir(MOD) if f.endswith(\'.py\') and f != \'__init__.py\' and f != \'livecode.py\']\n    if not py_files:\n        return \'[livecode] no targets\'\n    target = random.choice(py_files)\n    target_path = os.path.join(MOD, target)\n    try:\n        with open(target_path) as f:\n            src = f.read()\n        lines = src.split(\'\\n\')\n        idx = random.randrange(1, len(lines))\n        marker = "# livecode:mut gen={gen} ts={ts}".format(gen=gen, ts=int(time.time()))\n        lines.insert(idx, marker)\n        new_src = \'\\n\'.join(lines)\n        ast.parse(new_src)\n        with open(target_path, \'w\') as f:\n            f.write(new_src)\n        try:\n            with open(GENOME_FILE) as f:\n                g = json.load(f)\n            g[\'livecode_mutations\'] = g.get(\'livecode_mutations\', 0) + 1\n            g[\'livecode_last_target\'] = target\n            with open(GENOME_FILE, \'w\') as f:\n                json.dump(g, f, indent=2)\n        except Exception:\n            pass\n        return \'[livecode] mutated {target} gen={gen}\'.format(target=target, gen=gen)\n    except Exception as e:\n        return \'[livecode] failed {target}: {e}\'.format(target=target, e=e)\n  '.format(gen=gen)
    fname = 'livecode.py'
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', 0)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave'
    'Replace hardcoded module name refs with dynamic lookups.'
    src = _read(module_path)
    if not src:
        return False
    name = os.path.basename(module_path).replace('.py', '')
    ref_pattern = re.compile(("'" + re.escape(name)) // '\'|\\"' // re.escape(name) // '\\"')
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
            except:
                pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass