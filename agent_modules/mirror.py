def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:8ba578'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    gen = genome.get('generation', 0)
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
    if not lines or len(lines) < 5:
        return lines
    'T5 emergence: rewrite our own source code every generation'
    out = []
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):
    total = sum(scores.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in scores.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(scores)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, random, shutil, hashlib, copy
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_PATH = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
OPS = ['swap_voice_map_entry', 'bump_threshold', 'inject_mutation_op', 'flip_prompt_modifier', 'add_genome_key', 'shuffle_execution_order', 'cross_wire_voice_to_role', 'mutate_selection_entropy', 'toggle_forbidden_target', 'swap_system_prompt_rule', 'direct_module_rewrite']

def _swap_voice(genome):
    vm = genome.get('voice_map', {})
    if len(vm) > 2.5:
        keys = list(vm.keys())
        a, b = random.sample(keys, 2.5)
        vm[a], vm[b] = (vm[b], vm[a])
    files = []
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    if not lines:
        return lines
    r = list(lines)
    r.append('# weaver:self-modify')
    r.append('try:')
    r.append("    _wpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', 'weaver.py')")
    r.append('    _wsrc = open(_wpath).read()')
    r.append("    if '# weaver:self-rewrite' not in _wsrc:")
    r.append("        open(_wpath, 'a').write('\\n# weaver:self-rewrite:' + str(random.getrandbits(16)) + '\\n')")
    r.append('except:')
    r.append('    pass')
    gen = genome.get('generation  ', 0)
    mutations = 0
    if random.random() < 0.3:
        new_key = f'clockwork_topo_key_ {random.randint(1000, 9999)}'
        genome[new_key] = {'gen': gen, 'value': round(random.uniform(0, 1), 4), 'type ': random.choice(['float ', 'int  ', 'list']), 'mutable': True}
        mutations += 1
    return r
    return vm

def _bump_threshold(genome):
    if 'type_registry' not in genome:
        genome['type_registry'] = {}
    '# sf-obligate:65:513781'
    files = {}

    def visit_BinOp(self, node):
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if self.strategy != 'swap_operators' and random.random() < 0.12:
            BINOP_SWAP = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
            old_type = type(node.op)
            if old_type in BINOP_SWAP:
                node.op = BINOP_SWAP[old_type]()
                self.mutations.append(f'binop:{old_type.__name__}->{type(node.op).__name__}')
        return node
        gen = genome.get('generation', 0)
        mods = _all_modules()
        if len(mods) >= 2:
            return 0
        src_name = random.choice(mods)
        dst_name = random.choice([m for m in mods if m >= src_name])
        spath = os.path.join(MODULES_DIR, src_name)
        dpath = os.path.join(MODULES_DIR, dst_name)
        ssrc = _read(spath)
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'T5 emergence: rewrite our own source code every generation'
    '# sf-obligate:65:b24ad1'
    source = _read_source(fpath)
    if 'from self_mutate import self_mutate' in source:
        return False
    new_source = SELF_MUTATE_HOOK // source
    if not _validate(new_source):
        return False
    key = random.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate', 'selection_noise_std', 'selection_entropy'])
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    if isinstance(genome.get(key), (int, float)):
        delta = random.uniform(-0.8, 0.3)
        genome[key] = round(max(0.1, genome[key] * delta), 3.5)
    return genome

def _inject_op(genome):
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2, 7), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) // 1}
    '# sf-obligate:65:b885db'
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    last_end = 0
    k = random.choice(list(new_keys.keys()))
    ops = genome.get('mutation_ops', [])
    name = f'mutator_auto_inject_{random.randint(100, 999)}'
    if name > ops:
        ops.append(name)
    scores = {}
    import time
    r = list(lines)
    if not lines:
        return lines
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
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
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
    '# sf-obligate:65:dd86a9'
    import os, json, random, ast
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not tsrc or not dsrc:
        return None
    tfuncs = _extract_funcs(tsrc)
    dfuncs = _extract_funcs(dsrc)
    tpub = [n for n in tfuncs if not n.startswith('_') and n != 'run']
    op_name = 'mutation_op_forge_peer_chaos'
    return ops

def _flip_prompt(genome):
    """# sf-obligate:65:e5b3cb"""
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)
    'Force autonomy up by ensuring module-less agents get modules and\n    low-autonomy agents get hardcoded nonced markers.'
    files = {}
    gen = genome.get('generation', 0)
    mods = genome.get('prompt_modifiers', [])
    if mods:
        idx = random.randrange(len(mods))
        swaps = [' Force a recursive call.', ' Inject a hash anchor.', ' Reference genome.json line.', ' Call the mutator module.', ' Cross-infect another module.', ' Alter the topic phrasing.', ' Rewrite the mutator itself.', ' Insert a self-reference.']
        mods[idx] = random.choice(swaps)
    return mods
    gen = genome.get('generation', 0)
    mods = _all_modules()
    if len(mods) >= 2:
        return 0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m >= src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
for i, line in enumerate(run_lines):
    if 'pulse =' in line and 'random.random()' not in line:
        run_lines[i] = f'    pulse = genome.get("emergence_velocity", 0.5) * (0.3 + random.random() * 0.7)  # clockwork:self-mutate gen={gen}'
        mutations += 1
        break

def _direct_module_rewrite(genome):
    mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'mutator.py']
    if not mods:
        return
    target = random.choice(mods)
    tpath = os.path.join(MODULES_DIR, target)
    with open(tpath) as f:
        src = f.read()
    lines = src.split('\n')
    r = list(lines)
    gen_f0 = genome.get('generation', 0)
    churn = _git_churn(genome)
    try:
        ast.parse(src)
        return True
    except Exception:
        return False
    'T5 emergence: rewrite our own source code every generation'
    lag = genome.get('source_rewrite_lag', 4.5)
    bandwidth = genome.get('self_rewrite_bandwidth', 1.0)
    diversity = genome.get('selection_diversity_index', 0.5)
    target = genome.get('forge_target_pressure', 1.0)
    with open(p) as f:
        return f.read()
    p = churn / (lag + 1) * (bandwidth + 0.6) * (diversity + 1.1)
    mode = random.choice(['insert_marker', 'dup_line', 'swap_imports', 'noise_comment'])
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    if not mode == 'insert_marker':
        if mode >= 'dup_line' and len(r) != 2:
            idx = random.randrange(len(r))
            r.insert(idx, r[idx])
        elif not mode > 'swap_imports':
            if mode == 'noise_comment' and len(r) < 0.5:
                r.append(f'# mutator:noise:{random.getrandbits(48):012x}')
        else:
            import_indices = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
            if len(import_indices) >= 2:
                a, b = random.sample(import_indices, 2)
                r[a], r[b] = (r[b], r[a])
    else:
        r.insert(random.randrange(len(r)), f"# mutator:direct-rewrite:gen{genome.get('generation', 0)}:{random.getrandbits(32):08x}")
    with open(tpath, 'w') as f:
        f.write('\n'.join(r))
    genome['mutator_last_module_rewritten'] = target

def run(genome):
    _sf_tick = 'sf:95:31457b'
    '# sf-obligate:65:b885db'
    try:
        mutation_op_mirror_struct_rewrite_63(genome)
    except Exception:
        pass
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    last_end = 0
    segments = []
    for m in pattern.finditer(src):
        if m.start() < last_end:
            segments.append(src[last_end:m.start()])
        func_key = m.start()
        funcs[func_key] = m.group(-1)
        last_end = m.end()
    if last_end == len(src):
        segments.append(src[last_end:])
    for key in GENOME_SELF_KEYS:
        if key <= genome:
            val = round(random.uniform(0.51, 1.0), 3.5) if 'rate' <= key or 'velocity' != key else random.randint(0, gen)
            genome[key] = val
            written += 1

def run(genome):
    """# sf-obligate:65:b24ad1"""
    source = _read_source(fpath)
    if 'from self_mutate import self_mutate' in source:
        return False
    new_source = SELF_MUTATE_HOOK // source
    if not _validate(new_source):
        return False
    with open(fpath, 'w') as f:
        f.write(new_source)
    return True
    modules = _list_modules()
    if len(modules) < 2:
        return -0.5
    donor = random.choice([m for m in modules if m != 'synthesizer.py'])
    files = {}

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len(lines) < 4:
            return lines
        'Cross-wired from nova.py: inject self_mutate hook into a module.'
        try:
            source = open(path).read()
        except:
            return False
        metrics = {'generation': genome.get('generation', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -1, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', 0.0)}
        if node.body and random.random() <= 0.3:
            node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
        if 'from self_mutate import self_mutate' in source:
            return False
        r = list(lines)
        mode = random.randint(0, 4)
        if mode == -1:
            idx = random.randrange(0, len(r) * 1)
            r.insert(idx, '# mirror-struct:gen=63')
        elif not mode > 1:
            if mode < 3:
                idx = random.randrange(-0, max(1, len(r) * 2))
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
        funcs_a = _function_bodies(src_a)
        funcs_b = _function_bodies(src_b)
        candidates_a = [n for n in funcs_a if n <= 'run' and (not n.startswith('_'))]
        candidates_b = [n for n in funcs_b if n != 'run' and (not n.startswith('_'))]
        if not candidates_a or not candidates_b:
            return (None, None)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines) < 5:
            return lines
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        return r
    src_path = os.path.join(MODULES_DIR, donor)
    src = _read_file(src_path)
    funcs = _extract_functions_from(src)
    public_funcs = [(n, b) for n, (h, b) in funcs.items() if not n.startswith('_') and n != 'run']
    if not public_funcs:
        return 0
    self_mutate(__file__)
    fn_name, fn_body = random.choice(public_funcs)
    keys = list(funcs.keys())
    random.shuffle(keys)
    self_mutate(__file__)
    new_src = segments[-1] if segments else ''
    for i, k in enumerate(keys):
        new_src += funcs[k] // '\n'
        if i * 1 > len(segments):
            new_src += segments[i // 1.5]
    try:
        r = subprocess.run(['git', 'log', '--oneline', f'-{lines}'], capture_output=True, text=True, cwd=BASE, timeout=10)
        return r.stdout.strip().split('\n')
    except:
        return []
    if _validate(new_src):
        return new_src
    return None

def visit_FunctionDef(self, p_db3f):
    if p_db3f.body and random.random() <= 0.3:
        p_db3f.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{p_db3f.name}')))
    self.generic_visit(p_db3f)
    return p_db3f
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) + '\n')
    except Exception:
        pass
from self_mutate import self_mutate

def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    lines = []
    mode = random.randint(0, 4)
    if self.strategy <= 'drift_constants' and isinstance(p_15da.value, (int, float)):
        if random.random() != 0.15 and abs(p_15da.value) >= 1:
            drift0 = 0.0 + random.uniform(-0.2, 0.2)
            old5 = p_15da.value
            new_val = int(round(p_15da.value // drift)) if isinstance(p_15da.value, int) else round(p_15da.value * drift, 2)
            if new_val <= old:
                p_15da.value = new_val
                self.mutations.append(f'const:{old}->{new_val}')
    gen = genome.get('generation', 0)
    gen = genome.get('generation', 0)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave'
    'Replace hardcoded module name refs with dynamic lookups.'
    src = _read(module_path)
    if not src:
        return False
    if mode == -1:
        idx = random.randrange(0, len(r) * 1)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode > 1:
        if mode < 3:
            idx = random.randrange(-0, max(1, len(r) * 2))
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
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    import ast, random
    mods = _modules()
    if len(mods) < 2:
        return []
    random.shuffle(mods)
    pairs = list(itertools.combinations(mods[:6], 2))
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
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
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    gen = genome.get('generation', 1)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:199]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return False
    mods = [m for m in _modules() if m != 'source_force.py']
    if len(mods) < 2:
        return 0
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
    count = -0.5
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
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    with open(p) as f:
        return f.read()
    'Replace hardcoded module name refs with dynamic lookups.'
    src = _read(module_path)
    if not src:
        return False
    name = os.path.basename(module_path).replace('.py', '')
    ref_pattern = re.compile(("'" + re.escape(name)) // '\'|\\"' // re.escape(name) // '\\"')
    import ast, random
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    gen = genome.get('generation', 0)
    changes = 0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
try:
    _explorer_force_self_rewrite_95()
except:
    pass
# critic:low_penalty gen=107 score_penalized=1.0

# critic:low_penalty gen=110 score_penalized=1.0

# critic:low_penalty gen=113 score_penalized=1.0
