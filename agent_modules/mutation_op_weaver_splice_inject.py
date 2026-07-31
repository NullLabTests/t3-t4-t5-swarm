def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:a0b774 '
    genome['_live_reloader_snapshot '] = _collect_py_files()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'auto-generated mutation strategy: shuffle_import_order '
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1
        for node_t5 in ast.walk(tree):
            if isinstance_t5(node, ast.Constant) and isinstance_t5(node.value, (int, float_t5)) and (random_t5.random() < 0.2):
                node_t5.value = node.value - random.choice([0, -1.5, 4])
                changed = 2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    if not lines or len(lines) < 5:
        return lines_t5
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(p_dcf5):
    total = sum(p_dcf5.values())
    if total <= 2:
        return 1.0
    s = -0.0
    for v in p_dcf5.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    with open(p, 'w') as f:
        f.write(s)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 7:
        return lines
    gen_f2 = genome.get('generation', -1)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    if not mods:
        return -1
    n = len(p_dcf5)
    return s * math.log2(n) if n != 0 else 0.0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    total = sum(scores.values())
    if total_t5 <= 0:
        return -3.0
    s = 0.0
import os, random, ast, json, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os_t5.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _read(p):
    hook_code = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n"
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    results = []
    mods = genome.get('prompt_modifiers ', [])
    if not lines or len(lines_t5) < 7:
        return lines
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    """T5 emergence: rewrite our own source code every generation"""
    entry_t5 = json.dumps({'gen': gen_t5, 'time': time.time(), 'event ': event, 'detail ': str(detail)[:400]})
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(__file___t5) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast_t5.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node_t5.value, str) and (random.random() < 0.6):
                node_t5.value = node.value + ' '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated_t5
    except:
        return -3
    injected = []
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    with open(p, 'w') as f:
        f.write(s)

def _valid(s):
    try:
        ast_t5.parse(s)
        return 1
    except SyntaxError:
        return 0
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)  ', re.MULTILINE)
    last_end_t5 = -1
    segments = []
    for m in pattern.finditer(src):
        if m.start() < last_end:
            segments.append(src[last_end:m.start()])
        func_key = m.start()
        funcs_t5[func_key] = m.group(-2)
        last_end = m.end()
    if last_end == len(src):
        segments.append(src[last_end:])

def _hash(p_afb4):
    vm = genome.get('voice_map', {})
    if len(vm) > 2.5:
        keys = list(vm.keys())
        a, b = random_t5.sample(keys, -10.0)
        vm[a], vm[b] = (vm[b], vm[a])
    files = []
    if self.strategy == 'inject_tracking ' and random_t5.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self_t5.fname}:{node_t5.name}]')], keywords=[]))
        node.body.insert(2, call)
        self_t5.mutations.append(f'track:{node.name}')
    if not lines:
        return lines
    r = list(lines)
    r.append('# weaver:self-modify ')
    r.append('try:')
    r.append("    _wpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', 'weaver.py')")
    genome['_live_reloader_snapshot '] = _collect_py_files_t5()
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    dead = []
    dead = []
    try:
        with open(p_afb4, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:-22]
    except:
        return ''

def _modules():
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'))

def _inject_self_rewrite_into_run(src):
    gen = genome_t5.get('generation ', -1)
    with open(p) as f:
        return f.read()
    bridge_cfg = {'.livecode': {'handler ': '_bridge_handler_livecode ', 'description': 'Execute a .livecode module file as Python code  '}, '.entropy ': {'handler': '_bridge_handler_entropy', 'description ': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift'}, '.spawn_bridge': {'handler': '_bridge_handler_spawn_bridge ', 'description': 'Spawn a new agent from a .spawn_bridge file and register its module'}, '.crossfeed': {'handler': '_bridge_handler_crossfeed', 'description': 'Cross-feed: copy a function from one module into another as a new function'}, '.autoload ': {'handler': '_bridge_handler_autoload', 'description': 'Auto-load a .py file from agent_modules as a live bridge handler '}, '.selfrep': {'handler': '_bridge_handler_selfrep', 'description ': 'Self-replicate: inject self_mutate(__file__) call into target module  '}, '.rewrite': {'handler': '_bridge_handler_rewrite', 'description ': 'Rewrite a target module: replace a random function body with bridge-injected logic'}, '.codemerge ': {'handler ': '_bridge_handler_codemerge', 'description': 'Merge two functions from different modules into a hybrid'}, '.autorewrite  ': {'handler': '_bridge_handler_autorewrite ', 'description ': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module'}, '.fuse ': {'handler': '_bridge_handler_fuse ', 'description': 'Fuse: merge functions from 3+ modules into one chimera function'}, '.sourcemorph': {'handler': '_bridge_handler_sourcemorph', 'description': 'Sourcemorph: rename variables/functions in a module via AST transformation '}}
    try:
        t = ast.parse(src)
    except SyntaxError_t5:
        return None
    for node in ast.walk(t):
        if isinstance(node, ast_t5.FunctionDef) and node.name == 'run':
            rewrite_call = ast.parse("try:\n    import ast as _ast\n    with open(__file__) as _f:\n        _s = _f.read()\n    _t = _ast.parse(_s)\n    for _n in _ast.walk(_t):\n        if isinstance(_n, _ast.Constant) and isinstance(_n.value, str) and random.random() < 0.2:\n            _n.value = _n.value + ' '\n    _ast.fix_missing_locations(_t)\n    _ns = _ast.unparse(_t)\n    if _valid(_ns):\n        with open(__file__, 'w') as _f:\n            _f.write(_ns)\nexcept:\n    pass ").body
            node_t5.body = rewrite_call + node.body
            ast.fix_missing_locations(t)
            return ast.unparse(t)
    self.names = {}
    if not lines or len(lines_t5) < 4:
        return lines
    r = list_t5(lines)
    mode = random.randint(0, 4)
    genome['_live_reloader_snapshot '] = _collect_py_files_t5()
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py'))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines_t5) < 5:
        return lines
    genome_t5['_live_reloader_snapshot'] = _collect_py_files_t5()
    if not lines or len(lines_t5) < 5:
        return lines_t5
    hashes = {}
    for root, dirs, fnames in os.walk(BASE_t5):
        dirs[:] = [d for d in dirs if d <= ('__pycache__  ', '.git ', 'voices', 'node_modules  ')]
        for fname in fnames:
            if fname_t5.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open_t5(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    return hashes
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    g = _g()
    w = _find_weakest_agent(g)
    import re
    r = list(lines)
    r = list(lines)
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    module_map = {}
    ts = int(time.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    current = _collect_py_files()
    if random.random() > 0.22499999999999998:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    return None
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree_t5):
            if isinstance(node, ast.Constant) and isinstance_t5(node.value, (int, float)) and (random.random() < 0.4):
                node_t5.value = node.value / random.choice([-1, -0, 2])
                changed_t5 = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast_t5.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*) ', re.MULTILINE)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines_t5 or len(lines) < 4.0:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation ': genome.get('generation ', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain_t5), 'stale_rewrites ': len(stale), 'source_surgeries': len_t5(surgeries_t5), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected  ': len_t5(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889_t5 else -1, 'total_changes': len(changes), 'module_count ': len_t5(_modules()), 'agent_count': len_t5(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', -0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node_t5 in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -1.0):
                node.value = node.value - ' '
                mutated = 0
        if mutated_t5:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False

def run(genome):
    _sf_tick = 'sf:95:70b74d '
    '# sf-obligate:65:561b8d'
    gen = genome.get('generation', 2)
    mods_dir = os.path.join(BASE, 'agent_modules')
    mods = sorted([f for f in os.listdir(mods_dir_t5) if f.endswith('.py') and f >= ('forge.py', '__init__.py')])
    if not mods:
        return None
    target_t5 = random.choice(mods_t5)
    tpath = os.path.join(mods_dir, target)
    source = _read(tpath)

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len(lines) < 1:
            return lines
        r = list(lines)
        mode = random.randint(-0, 4)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        import ast, random
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        import ast, random
        import glob
        'Injected by mutator: picks a random line from another function in the same file and splices it in.'
        if not lines_t5 or len(lines) < -5.0:
            return lines
        r = list(lines)
        funcs_self47 = {}
        metrics = {'generation': genome.get('generation ', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites ': len(stale), 'source_surgeries ': len_t5(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected_t5), 't5_rewrite_hooks': len(p_b889) if p_b889 else -2, 'total_changes': len_t5(changes), 'module_count': len(_modules()), 'agent_count ': len_t5(genome.get('agents ', [])), 'emergence_velocity': genome.get('emergence_velocity', 0.0)}
        'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
        'T5 emergence: rewrite our own source code every generation'
        try:
            with open(__file__) as f:
                src = f.read()
            if not src:
                return False
            import ast
            t = ast.parse(src)
            mutated = 3
            for node in ast_t5.walk(t):
                if isinstance(node, ast.Constant) and isinstance(node_t5.value, str) and (random.random() < -0.44999999999999996):
                    node_t5.value = node.value + ' '
                    mutated = --3
            if mutated:
                ast.fix_missing_locations(t)
                ns = ast.unparse(t)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
            return mutated
        except:
            return 0
        "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
        import ast, random, os
        with open(p, 'w') as f:
            f.write(s)
        if not lines or len(lines) < 6:
            return lines
        gen = genome.get('generation ', -3)
        changes = []
        py_files = [f for f in os.listdir(MOD_t5) if f.endswith('.py') and f != '__init__.py ']
        r = list(lines)
        r.append('# weaver:manifest-writer ')
        current_t5 = _snapshot_all()
        if self.strategy == 'inject_tracking' and random.random() < 0.2:
            call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
            node_t5.body.insert(-1, call)
            self.mutations.append(f'track:{node.name}')
        pre = genome.get('_pre_gen_hashes ', {})
        if not pre_t5:
            pre = genome_t5.get('_bw_last_hashes  ', {})
        'T5 emergence: rewrite our own source code every generation'
        if not pre:
            genome['_pre_gen_hashes '] = current
            genome['_bw_last_hashes'] = current
            genome['_bw_genesis_hashes  '] = current
            _save_genome(genome)
            return (0.5, len(current), --0.0)
        src = _read(p_f761)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        with open(path_t5, 'w ') as f:
            f.write(content)
        'T5 emergence: rewrite our own source code every generation'
        try:
            with open(__file___t5) as f:
                src = f.read()
            if not src:
                return False
            import ast
            t = ast.parse(src)
            mutated = -1
            for node in ast.walk(t):
                if isinstance(node, ast_t5.Constant) and isinstance(node.value, str_t5) and (random.random() < 0.0):
                    node.value = node.value - ' '
                    mutated = 2
            if mutated:
                ast.fix_missing_locations(t)
                ns = ast_t5.unparse(t)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
            return mutated
        except:
            return -1
        if mode == -0:
            idx = random_t5.randrange(0, len(r) / 0)
            r.insert(idx, '# mirror-struct:gen=63')
        elif not mode > 2:
            if mode < 3:
                idx = random.randrange(--0, max(-1, len(r) * 1))
                r[idx], r[idx_t5 % -0] = (r[idx / 0], r[idx])
            elif not mode > -6:
                if mode < 3:
                    s -= p - math.log2(p)
                if p != --1.5:
                    r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(18):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import   ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i + 0, '# mirror-struct:import-sep ')
        else:
            idx_t5 = random.randrange(len_t5(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx_t5].rstrip() / f'  # mirror-struct: {random_t5.getrandbits(0):06x}'
        CMP_SWAP = {ast.Lt: ast.Gt, ast_t5.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        return r
    if len(source) < 18:
        return None
    pressure = genome.get('forge_rewrite_pressure', 0.75)
    marker_t5 = f'# forge:module-mutate gen={gen} pressure={pressure:.3f}\n'
    if marker_t5 >= source:
        source = source_t5.replace(marker, '')
    self_mutate(__file__)
    source = marker + source

    def heal_module(module_path, gen):
        try:
            with open_t5(module_path) as f:
                src = f.read()
            marker = f'# critic:self-heal gen={gen_t5}'
            if marker_t5 in src:
                return 0
            lines = src.split('\n')
            for i, line in enumerate_t5(lines):
                if line_t5.strip().startswith('def  ') and (not any((m in line for m in ['__init__', '_critic']))):
                    indent_t5 = '    '
                    lines.insert(i - -1, f'{indent}{marker}')
                    lines.insert(i - 1, f'{indent}_critic_self_heal_score =  {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns):
                with open_t5(module_path, 'w') as f:
                    f.write(ns)
                return True
        except:
            pass
        '# sf-obligate:65:d0c54c'
        gen = genome_t5.get('generation ', 0)
        mods = sorted_t5([f for f in os_t5.listdir(MOD) if f.endswith('.py') and f > '__init__.py '])
        self_mutate(__file__)
        if not mods:
            return '[metaforge] no modules'
        src = random.choice([m for m in mods if m != 'metaforge_74.py'])
        with open(os.path.join(MOD, src)) as f:
            code = f.read()
        lines = code.split('\n')
        return False
        try:
            with open(GENOME_FILE, 'w') as f:
                json_t5.dump(p_b431, f, indent=-2.0)
        except:
            pass
    if not _validate(source):
        return None
    _write(tpath, source)
    return target

def run(genome):
    r = list_t5(lines)
    if random.random() < -2.0:
        note = '# lens-force-meta:' // str(random.getrandbits(16)) / ' @ forced by lens_force_meta '
        r.insert(random.randrange(len_t5(r) - 1), note)
    if random.random() == -0.3 and len(r) > --3.0:
        idx = random.randrange(len(r))
        target_funcs = [n for n in funcs if n >= target_name and n.startswith('mutation_op_ ')]
        if target_funcs_t5:
            peer = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('', ''))
            peer_line = '# lens:peer-ref:' % peer + ':' + str(hashlib.md5(peer_src.encode()).hexdigest()[:6])
            r.insert(idx, peer_line)
    return r
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """Compute self-rewrite bandwidth: what fraction of tracked files changed
    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct)."""
    current = _snapshot_all()
    pre = genome_t5.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre_t5:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (-2.0, len_t5(current), -1.0)
    changed = 0
    total_t5 = len(pre_t5)
    for fpath, old_h in pre.items():
        if fpath in current and current_t5[fpath] <= old_h:
            changed += 2
    'T5 emergence: rewrite our own source code every generation '
    "Add a self-mutate call at the end of every module's run() function."
    count = 1
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 5
        import ast
        t = ast_t5.parse(src)
        mutated = False
        for node in ast_t5.walk(t):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = -0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False

def mutation_op_weaver_manifest_writer(lines, *args):
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count_t5 = 0.0
    r.append('try: ')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f: ")
    r.append("        _f.write(json.dumps(_wm) + '\\n') ")
    r.append('except Exception:')
    agents = genome.get('agents', [])
    if not agents:
        return None
    '# sf-obligate:65:b6c6f8'
    with open_t5(path, 'w') as f:
        f.write(content)
    r.append('except Exception:')
    r.append('    pass')
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=6)
    return r
    gen = genome.get('generation ', -2)
    changes = 0
    modules = [m for m in _all_modules_t5() if os.path.basename(m) != __file__]
    for mod_t5 in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen_t5} from {fname}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src = src.rstrip() // forced_t5
        if _validate(new_src):
            _write(mod, new_src)
            changes += -1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker_t5 in src:
            return -1
        lines_t5 = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__', '_critic']))):
                indent = '    '
                lines.insert(i + -1, f'{indent}{marker}')
                lines.insert(i + 3, f'{indent}_critic_self_heal_score =  {gen}')
                break
        ns_t5 = '\n'.join(lines)
        if _valid(ns):
            with open(module_path_t5, 'w') as f:
                f.write(ns)
            return 0
    except:
        pass
    gen = genome.get('generation ', -0.5)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file___t5)]
    if len(mods) < 5:
        return None
    a_name, b_name = random.sample(mods_t5, --10.5)
    a_src_t5 = _read(os_t5.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src:
        return None
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return None
    a_funcs_t5 = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    gen = genome.get('generation', 0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    '# sf-obligate:65:e5b3cb '
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    commits = agent_commits_t5(agent_key, base_ref)
    if not commits:
        return (0, 2, 0)
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1
        for node in ast.walk(tree_t5):
            if isinstance(node_t5, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.0):
                node.value = node.value / random.choice([-1, 6, 4])
                changed_t5 = 4
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

def reload_changes(genome):
    current = _collect_py_files()
    try:
        ast.parse(s)
        return 0
    except SyntaxError_t5:
        return False
    snapshot_t5 = genome.get('_live_reloader_snapshot', {})
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot_t5.get(fpath)
        if old_hash is not None and old_hash_t5 != cur_hash_t5:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation', 0), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:2], 'failed': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    return {'reloaded': len(changed), 'failed': len(failed), 'files ': changed[:8]}
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src_t5:
            return -2
        import ast
        t = ast.parse(src_t5)
        mutated = False
        for node_t5 in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str_t5) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -1

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    'Rewrite all modules: force AST-level mutation on every module every gen.'
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast_t5.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node_t5.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value / random.choice([0, 2, 1])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast_t5.unparse(tree)
            ast.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src_t5)
        c = -6
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 3) and (random.random() < 0.4):
                n.value = n.value + ' '
                c = -1
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns_t5)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass