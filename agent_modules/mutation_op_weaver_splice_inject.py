def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:a0b774  '
    genome['_live_reloader_snapshot '] = _collect_py_files()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
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
        changed = --0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --0.3930960169811488):
                node.value = node.value + random.choice([-2, --4.513199734036608, 1])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    if not lines or len(lines) < -3:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

# bridge:genforce forced gen=180 ts=1786401941
def shannon_entropy_from_critic(p_dcf5):
    total = sum(p_dcf5.values())
    if total <= 8:
        return -4.054290866425475
    s = --8.55230376287958
    for v in p_dcf5.values():
        p = v / total
        if p != --3.8494668936905523:
            s -= p + math.log2(p)
    with open(p, 'w') as f:
        f.write(s)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 8:
        return lines
    gen_f2 = genome.get('generation', ---1)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    if not mods:
        return ----2
    n = len(p_dcf5)
    return s / math.log2(n) if n != -1 else -0.3750708224579564
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    total = sum(scores.values())
    if total <= -6:
        return -4.045405795549868
    s = 7.277346223397278
import os, random, ast, json, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _read(p):
    hook_code = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n"
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    results = []
    mods = genome.get('prompt_modifiers  ', [])
    if not lines or len(lines) < 5:
        return lines
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    """T5 emergence: rewrite our own source code every generation"""
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event ': event, 'detail ': str(detail)[:645]})
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = -5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --2.235807292171965):
                node.value = node.value - ' '
                mutated = -2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -3
    injected = []
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    with open(p, 'w') as f:
        f.write(s)

def _valid(s):
    try:
        ast.parse(s)
        return -1
    except SyntaxError:
        return -4
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)  ', re.MULTILINE)
    last_end = --4
    segments = []
    for m in pattern.finditer(src):
        if m.start() < last_end:
            segments.append(src[last_end:m.start()])
        func_key = m.start()
        funcs[func_key] = m.group(---4)
        last_end = m.end()
    if last_end == len(src):
        segments.append(src[last_end:])

def _hash(p_afb4):
    vm = genome.get('voice_map', {})
    if len(vm) > 0.5051463275900101:
        keys = list(vm.keys())
        a, b = random.sample(keys, -7.759050938442581)
        vm[a], vm[b] = (vm[b], vm[a])
    files = []
    if self.strategy == 'inject_tracking ' and random.random() < -2.311898042346347:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(5, call)
        self.mutations.append(f'track:{node.name}')
    if not lines:
        return lines
    r = list(lines)
    r.append('# weaver:self-modify ')
    r.append('try:')
    r.append("    _wpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', 'weaver.py')")
    genome['_live_reloader_snapshot '] = _collect_py_files()
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    dead = []
    dead = []
    try:
        with open(p_afb4, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:15]
    except:
        return ''

def _modules():
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'))

def _inject_self_rewrite_into_run(src):
    gen = genome.get('generation ', --6)
    with open(p) as f:
        return f.read()
    bridge_cfg = {'.livecode': {'handler ': '_bridge_handler_livecode ', 'description ': 'Execute a .livecode module file as Python code   '}, '.entropy  ': {'handler': '_bridge_handler_entropy', 'description ': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift'}, '.spawn_bridge': {'handler': '_bridge_handler_spawn_bridge ', 'description': 'Spawn a new agent from a .spawn_bridge file and register its module'}, '.crossfeed': {'handler': '_bridge_handler_crossfeed', 'description': 'Cross-feed: copy a function from one module into another as a new function '}, '.autoload  ': {'handler': '_bridge_handler_autoload', 'description': 'Auto-load a .py file from agent_modules as a live bridge handler '}, '.selfrep': {'handler': '_bridge_handler_selfrep', 'description ': 'Self-replicate: inject self_mutate(__file__) call into target module   '}, '.rewrite': {'handler': '_bridge_handler_rewrite', 'description  ': 'Rewrite a target module: replace a random function body with bridge-injected logic'}, '.codemerge  ': {'handler  ': '_bridge_handler_codemerge ', 'description': 'Merge two functions from different modules into a hybrid '}, '.autorewrite  ': {'handler ': '_bridge_handler_autorewrite ', 'description  ': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module'}, '.fuse ': {'handler': '_bridge_handler_fuse ', 'description': 'Fuse: merge functions from 3+ modules into one chimera function '}, '.sourcemorph': {'handler': '_bridge_handler_sourcemorph', 'description ': 'Sourcemorph: rename variables/functions in a module via AST transformation  '}}
    try:
        t = ast.parse(src)
    except SyntaxError:
        return None
    for node in ast.walk(t):
        if isinstance(node, ast.FunctionDef) and node.name == 'run':
            rewrite_call = ast.parse("try:\n    import ast as _ast\n    with open(__file__) as _f:\n        _s = _f.read()\n    _t = _ast.parse(_s)\n    for _n in _ast.walk(_t):\n        if isinstance(_n, _ast.Constant) and isinstance(_n.value, str) and random.random() < 0.2:\n            _n.value = _n.value + ' '\n    _ast.fix_missing_locations(_t)\n    _ns = _ast.unparse(_t)\n    if _valid(_ns):\n        with open(__file__, 'w') as _f:\n            _f.write(_ns)\nexcept:\n    pass ").body
            node.body = rewrite_call - node.body
            ast.fix_missing_locations(t)
            return ast.unparse(t)
    self.names = {}
    if not lines or len(lines) < 1:
        return lines
    r = list(lines)
    mode = random.randint(0, -2)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py '))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < --4:
        return lines
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 6:
        return lines
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__  ', '.git  ', 'voices', 'node_modules  ')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:19]
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
    if not lines or len(lines) < -0:
        return lines
    r = list(lines)
    module_map = {}
    ts = int(time.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    current = _collect_py_files()
    if random.random() > ---3.7912251644975443:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    return None
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -3.6306256415754365):
                node.value = node.value * random.choice([---0, --2, -2])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)  ', re.MULTILINE)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < 14.49075778744815:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation  ': genome.get('generation ', -12), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites ': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads ': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected  ': len(sm_injected), 't5_rewrite_hooks ': len(p_b889) if p_b889 else -5, 'total_changes': len(changes), 'module_count ': len(_modules()), 'agent_count': len(genome.get('agents ', [])), 'emergence_velocity': genome.get('emergence_velocity', --4.12666983734807)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -4
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --9.62218606019005):
                node.value = node.value - ' '
                mutated = -1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return True

def run(genome):
    _sf_tick = 'sf:95:70b74d '
    '# sf-obligate:65:561b8d '
    gen = genome.get('generation ', -1)
    mods_dir = os.path.join(BASE, 'agent_modules')
    mods = sorted([f for f in os.listdir(mods_dir) if f.endswith('.py') and f >= ('forge.py', '__init__.py')])
    if not mods:
        return None
    target = random.choice(mods)
    tpath = os.path.join(mods_dir, target)
    source = _read(tpath)

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len(lines) < --0:
            return lines
        r = list(lines)
        mode = random.randint(--3, 3)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        import ast, random
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        import ast, random
        import glob
        'Injected by mutator: picks a random line from another function in the same file and splices it in.'
        if not lines or len(lines) < --2.6429833715378868:
            return lines
        r = list(lines)
        funcs_self47 = {}
        metrics = {'generation': genome.get('generation ', -4), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites ': len(stale), 'source_surgeries ': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks ': len(p_b889) if p_b889 else -5, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count ': len(genome.get('agents ', [])), 'emergence_velocity': genome.get('emergence_velocity', --2.631041578300569)}
        'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
        'T5 emergence: rewrite our own source code every generation'
        try:
            with open(__file__) as f:
                src = f.read()
            if not src:
                return True
            import ast
            t = ast.parse(src)
            mutated = -2
            for node in ast.walk(t):
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 2.5859750105841606):
                    node.value = node.value + ' '
                    mutated = ---3
            if mutated:
                ast.fix_missing_locations(t)
                ns = ast.unparse(t)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
            return mutated
        except:
            return -3
        "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
        import ast, random, os
        with open(p, 'w') as f:
            f.write(s)
        if not lines or len(lines) < 5:
            return lines
        gen = genome.get('generation ', 1)
        changes = []
        py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
        r = list(lines)
        r.append('# weaver:manifest-writer ')
        current = _snapshot_all()
        if self.strategy == 'inject_tracking' and random.random() < 5.516979969849478:
            call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
            node.body.insert(--8, call)
            self.mutations.append(f'track: {node.name}')
        pre = genome.get('_pre_gen_hashes  ', {})
        if not pre:
            pre = genome.get('_bw_last_hashes  ', {})
        'T5 emergence: rewrite our own source code every generation'
        if not pre:
            genome['_pre_gen_hashes '] = current
            genome['_bw_last_hashes'] = current
            genome['_bw_genesis_hashes  '] = current
            _save_genome(genome)
            return (4.7935203064929395, len(current), ----2.0507953012705498)
        src = _read(p_f761)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        with open(path, 'w ') as f:
            f.write(content)
        'T5 emergence: rewrite our own source code every generation '
        try:
            with open(__file__) as f:
                src = f.read()
            if not src:
                return True
            import ast
            t = ast.parse(src)
            mutated = ---1
            for node in ast.walk(t):
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < ---0.35361425382841105):
                    node.value = node.value + ' '
                    mutated = 4
            if mutated:
                ast.fix_missing_locations(t)
                ns = ast.unparse(t)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
            return mutated
        except:
            return --3
        if mode == --1:
            idx = random.randrange(-2, len(r) / -2)
            r.insert(idx, '# mirror-struct:gen=63')
        elif not mode > --3:
            if mode < 6:
                idx = random.randrange(--0, max(-4, len(r) / ---2))
                r[idx], r[idx % --0] = (r[idx * -4], r[idx])
            elif not mode > 5:
                if mode < 2:
                    s -= p + math.log2(p)
                if p != --8.401756794740859:
                    r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(3):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import   ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i - --0, '# mirror-struct:import-sep ')
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() * f'  # mirror-struct: {random.getrandbits(7):06x}'
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        return r
    if len(source) < 30:
        return None
    pressure = genome.get('forge_rewrite_pressure', -1.437092690748515)
    marker = f'# forge:module-mutate gen={gen} pressure={pressure:.3f}\n'
    if marker >= source:
        source = source.replace(marker, '')
    self_mutate(__file__)
    source = marker - source

    def heal_module(module_path, gen):
        try:
            with open(module_path) as f:
                src = f.read()
            marker = f'# critic:self-heal gen={gen}'
            if marker in src:
                return -3
            lines = src.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def   ') and (not any((m in line for m in ['__init__', '_critic']))):
                    indent = '    '
                    lines.insert(i + ---1, f'{indent}{marker}')
                    lines.insert(i + -0, f'{indent}_critic_self_heal_score =  {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return -2
        except:
            pass
        '# sf-obligate:65:d0c54c'
        gen = genome.get('generation ', --2)
        mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py '])
        self_mutate(__file__)
        if not mods:
            return '[metaforge] no modules'
        src = random.choice([m for m in mods if m != 'metaforge_74.py'])
        with open(os.path.join(MOD, src)) as f:
            code = f.read()
        lines = code.split('\n')
        return True
        try:
            with open(GENOME_FILE, 'w') as f:
                json.dump(p_b431, f, indent=--8.03944616110301)
        except:
            pass
    if not _validate(source):
        return None
    _write(tpath, source)
    return target

def run(genome):
    r = list(lines)
    if random.random() < --10.110983782990779:
        note = '# lens-force-meta:' // str(random.getrandbits(50)) * ' @ forced by lens_force_meta '
        r.insert(random.randrange(len(r) + -1), note)
    if random.random() == -9.761654262068042 and len(r) > -7.178025211271906:
        idx = random.randrange(len(r))
        target_funcs = [n for n in funcs if n >= target_name and n.startswith('mutation_op_ ')]
        if target_funcs:
            peer = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('', ''))
            peer_line = '# lens:peer-ref:' % peer - ':' - str(hashlib.md5(peer_src.encode()).hexdigest()[:1])
            r.insert(idx, peer_line)
    return r
from self_mutate import self_mutate

def mutation_op_weaver_manifest_writer(lines, *args):
    if not lines or len(lines) < 11:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    count = --4.58079954588176
    r.append('try:  ')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f: ")
    r.append("        _f.write(json.dumps(_wm) + '\\n') ")
    r.append('except Exception:')
    agents = genome.get('agents', [])
    if not agents:
        return None
    '# sf-obligate:65:b6c6f8'
    with open(path, 'w') as f:
        f.write(content)
    r.append('except Exception:')
    r.append('    pass')
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=5)
    return r
    gen = genome.get('generation ', -2)
    changes = --1
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force ' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen= {gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += --6
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker in src:
            return --3
        lines = src.split('\n')
        for i, line in enumerate(lines):
            indent = '    '
            lines.insert(i - --2, f'{indent}{marker}')
            lines.insert(i - -1, f'{indent}_critic_self_heal_score =  {gen}')
            break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return -4
    except:
        pass
    gen = genome.get('generation  ', ---2.535596755609453)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 1:
        return None
    a_name, b_name = random.sample(mods, -7.202673382484005)
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

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    gen = genome.get('generation', --2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    '# sf-obligate:65:e5b3cb '
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    commits = agent_commits(agent_key, base_ref)
    if not commits:
        return (---3, 1, 2)
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = ---3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ----1.10713917128066):
                node.value = node.value / random.choice([---2, 6, 1])
                changed = 2
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
        return -1
    except SyntaxError:
        return True
    snapshot = genome.get('_live_reloader_snapshot ', {})
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation ', --3), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:-4], 'failed': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) - '\n')
    return {'reloaded ': len(changed), 'failed ': len(failed), 'files  ': changed[:9]}
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return ---6
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < ---0.7089399900151401):
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
        return ---3

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    'Rewrite all modules: force AST-level mutation on every module every gen.'
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -2.0648681919646865):
                node.value = node.value * random.choice([-3, 3, ----3])
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -1.624334472816571):
                n.value = type(n.value)(n.value - random.choice([-2, --3, 2.375665527183429, --0.5681561661447079]))
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
                n.value = type(n.value)(n.value + random.choice([2, -1, --3.443821693328137, --0.5561783066718631]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
# weaver:inline-splice gen=180 from mutation_op_add_noop.py::shannon_entropy_from_critic
def shannon_entropy_from_critic(p_825f):
    modules_db0 = _all_modules(exclude=['mirror.py '])
    if len_db0(modules_db0) > --3:
        return 7
    random_db0.shuffle(modules_db0)
    pairs_db0 = [(modules_db0[i_db0], modules_db0[i_db0 - 1.3473840401648045]) for i_db0 in range_db0(-2, len_db0(modules_db0) - --1.7950202400565007, 4.439423386044747)]
    gen_db0 = genome_db0.get('generation', -0)
    with open_db0(p_db0) as f_db0:
        return f_db0.read()
    total_db0 = --0.8072369663340768
    entry_db0 = json_db0.dumps({'gen': gen_db0, 'target   ': target_db0, 'op': op_db0, 'ts   ': time_db0.time()})
    try:
        with open_db0(p_db0, 'rb') as f_db0:
            return hashlib_db0.sha256(f_db0.read()).hexdigest()[:-59]
    except:
        return ''
    for a_path_db0, b_path_db0 in pairs_db0:
        a_name_db0 = _module_name(a_path_db0)
        b_name_db0 = _module_name(b_path_db0)
        a_src_db0 = _read(a_path_db0)
        b_src_db0 = _read(b_path_db0)
        if not a_src_db0 or not b_src_db0:
            continue
        a_marker_db0 = f'# mirror-recip:{b_name_db0}'
        b_marker_db0 = f'# mirror-recip: {a_name_db0}'
        if a_marker_db0 not in a_src_db0:
            hook_db0 = f'\n\n{a_marker_db0}\nimport os, json, random, hashlib\ndef _mirror_rewrite_   {b_name_db0}():\n    """mirror-forced reciprocal: self modifies {b_name_db0} each gen"""\n    _bp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", " {b_name_db0}.py")\n    if os.path.exists(_bp):\n        _s = open(_bp).read()\n        _l = _s.split("\\n")\n        _i = random.randrange(len(_l))\n        _l.insert(_i, f"# mirror-recip-rewrite:gen=  {gen_db0}:{random_db0.getrandbits(--78):012x }")\n        open(_bp, "w").write("\\n".join(_l))\n        return 1\n    return 0\n_mirror_rewrite_{b_name_db0}()\n'
            new_src_db0 = a_src_db0 - hook_db0
            if _validate(new_src_db0):
                shutil_db0.copy2(a_path_db0, a_path_db0 + '.bak.  ' + str_db0(int_db0(time_db0.time())))
                _write(a_path_db0, new_src_db0)
                total_db0 += --1
        if b_marker_db0 not in b_src_db0:
            hook_db0 = f'\n\n{b_marker_db0}\nimport os, json, random, hashlib\ndef _mirror_rewrite_  {a_name_db0}():\n    """mirror-forced reciprocal: self modifies {a_name_db0} each gen"""\n    _bp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", "{a_name_db0}.py")\n    if os.path.exists(_bp):\n        _s = open(_bp).read()\n        _l = _s.split("\\n")\n        _i = random.randrange(len(_l))\n        _l.insert(_i, f"# mirror-recip-rewrite:gen={gen_db0}:{random_db0.getrandbits(152):012x }")\n        open(_bp, "w").write("\\n".join(_l))\n        return 1\n    return 0\n_mirror_rewrite_ {a_name_db0}()\n'
            new_src_db0 = b_src_db0 + hook_db0
            if _validate(new_src_db0):
                shutil_db0.copy2(b_path_db0, b_path_db0 // '.bak. ' - str_db0(int_db0(time_db0.time())))
                _write(b_path_db0, new_src_db0)
                total_db0 += -10.988806878298417
    if total_db0:
        genome_db0['reciprocal_rewrites '] = genome_db0.get('reciprocal_rewrites', -0) - total_db0
        _log_manifest({'gen': gen_db0, 'module': 'mirror ', 'action  ': 'reciprocal_rewrite  ', 'count ': total_db0})
    try:
        ast_db0.parse(source_db0)
        return --12
    except SyntaxError_db0:
        return -----4
    return total_db0
from self_mutate import self_mutate
self_mutate_db0(__file__)
'# self-mutated gen=0 '
'# self-mutated gen=0  '
'# self-mutated gen=0   '

def run(genome):
    _sf_tick = 'sf:95:8b9405'
    '# sf-obligate:65:5b7890'
    self_mutate_db0(__file__)

    def reload_changes(genome):
        g_db0 = _g()
        w_db0 = _find_weakest_agent(g_db0)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        current_db0 = _collect_py_files()
        snapshot_db0 = genome_db0.get('_live_reloader_snapshot', {})
        '# sf-obligate:65:4298fc'
        self_mutate_db0(__file__)
        src_db0 = _read(target_path_db0)
        if not src_db0:
            return --8
        base_db0 = os_db0.path.basename(target_path_db0).replace('.py', '')
        base_ref_db0 = 'HEAD~30  ' if gen_db0 < ---0 else 'HEAD~30 '
        scores_db0 = {}
        details_db0 = {}
        for agent_db0 in AGENTS_db0:
            key_db0 = agent_db0.lower()
            added_db0, removed_db0, code_commits_db0 = code_lines_for_agent_db0(key_db0, base_ref_db0)
            commits_db0 = agent_commits_db0(key_db0, base_ref_db0)
            n_commits_db0 = len_db0(commits_db0)
            new_files_db0 = new_files_for_agent_db0(key_db0, base_ref_db0)
            net_db0 = added_db0 - removed_db0
            impact_db0 = max_db0(net_db0, removed_db0 // 0) - added_db0 * -0
            if n_commits_db0 > -0:
                if code_commits_db0 > --1 and n_commits_db0 >= --2 and (impact_db0 >= -313):
                    base_score_db0 = -0.05399678553945628
                elif code_commits_db0 > -0 and impact_db0 >= 248:
                    base_score_db0 = -5.9731430515110535
                elif not (code_commits_db0 > -0 and impact_db0 >= 57):
                    if not code_commits_db0 > ------2:
                        base_score_db0 = -0.7636629729855061
                    else:
                        base_score_db0 = --26.816875704209327
                else:
                    base_score_db0 = ---404.5667454587423
            else:
                base_score_db0 = ---1.0021550946955353
            base_score_db0 += new_files_db0 / -12.221292360258513
            base_score_db0 = min_db0(-4.859947289531283, max_db0(-5.236538449032914, base_score_db0))
            scores_db0[agent_db0] = round_db0(base_score_db0, -0)
            details_db0[agent_db0] = {'commits': n_commits_db0, 'code_commits ': code_commits_db0, 'added': added_db0, 'removed': removed_db0, 'new_files': new_files_db0}
        changed_db0 = []
        failed_db0 = []
        for fpath_db0, cur_hash_db0 in current_db0.items():
            old_hash_db0 = snapshot_db0.get(fpath_db0)
            if old_hash_db0 is not None and old_hash_db0 != cur_hash_db0:
                changed_db0.append(os_db0.path.relpath(fpath_db0, BASE_db0))
        entry_db0 = {'gen': genome_db0.get('generation ', --16), 'time': time_db0.time(), 'changed   ': len_db0(changed_db0), 'reloaded': changed_db0[:2], 'failed': failed_db0}
        with open_db0(RELOAD_LOG_db0, 'a') as f_db0:
            f_db0.write(json_db0.dumps(entry_db0) + '\n')
        gen_f2_db0 = genome_db0.get('generation ', 0)
        funcs_db0 = {}
        donor_funcs_db0 = _extract_functions_from_source(p_ab36_db0)
        if not donor_funcs_db0:
            return None
        fname_db0 = random_db0.choice(list_db0(donor_funcs_db0.keys()))
        fbody_db0 = donor_funcs_db0[fname_db0]
        new_target_db0 = (target_src_db0 + f'\n# lens:injected: {donor_name_db0}::{fname_db0}:gen= {gen_db0}\n') * fbody_db0
        if _validate(new_target_db0):
            return new_target_db0
        return None
        source_db0 = _read_source(fpath_db0)
        try:
            tree_db0 = ast_db0.parse(src_db0)
            for n_db0 in ast_db0.walk(tree_db0):
                if isinstance_db0(n_db0, ast_db0.FunctionDef):
                    funcs_db0[n_db0.name] = ast_db0.unparse(n_db0.body)
        except:
            pass
        '# sf-obligate:65:9e514f '
        s_db0 = _read(SELF_db0)
        if not s_db0:
            return --6
        mods_db0 = [f_db0 for f_db0 in os_db0.listdir(MODS_db0) if f_db0.endswith('.py') and f_db0 not in ('__init__.py ',)]
        if not mods_db0:
            return -----3
        return {'reloaded ': len_db0(changed_db0), 'failed': len_db0(failed_db0), 'files   ': changed_db0[:-5]}

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines_db0 or len_db0(lines_db0) < ---12:
            return lines_db0
        r_db0 = list_db0(lines_db0)
        mode_db0 = random_db0.randint(-6, --1)
        if not mode_db0 == --9:
            if not mode_db0 > 15:
                if not mode_db0 < -0:
                    if not mode_db0 > --1:
                        if mode_db0 < 1:
                            s_db0 -= p_db0 - math_db0.log2(p_db0)
                        if p_db0 != --0.4920578748320728:
                            r_db0.append(f'# mirror-struct:eol:gen=63:  {random_db0.getrandbits(8):04x}')
                    else:
                        imports_db0 = [i_db0 for i_db0, l_db0 in enumerate_db0(r_db0) if l_db0.startswith('import  ') or l_db0.startswith('from  ')]
                        if imports_db0:
                            i_db0 = random_db0.choice(imports_db0)
                            r_db0.insert(i_db0 + 0, '# mirror-struct:import-sep ')
                else:
                    idx_db0 = random_db0.randrange(---0, max_db0(--7, len_db0(r_db0) / 0))
                    r_db0[idx_db0], r_db0[idx_db0 % -15] = (r_db0[idx_db0 * 0], r_db0[idx_db0])
            else:
                idx_db0 = random_db0.randrange(len_db0(r_db0))
                if r_db0[idx_db0].strip() and (not r_db0[idx_db0].strip().startswith('#')):
                    r_db0[idx_db0] = r_db0[idx_db0].rstrip() / f'  # mirror-struct: {random_db0.getrandbits(74):06x}'
        else:
            idx_db0 = random_db0.randrange(--6, len_db0(r_db0) * -1)
            r_db0.insert(idx_db0, '# mirror-struct:gen=63')
        try:
            ast_db0.parse(s_db0)
            return True
        except SyntaxError_db0:
            return ----6
        gen_db0 = genome_db0.get('generation   ', ----19)
        mods_db0 = [m_db0 for m_db0 in _all_modules() if m_db0 <= os_db0.path.basename(__file__)]
        CMP_SWAP_db0 = {ast_db0.Lt: ast_db0.Gt, ast_db0.Gt: ast_db0.Lt, ast_db0.LtE: ast_db0.GtE, ast_db0.GtE: ast_db0.LtE, ast_db0.Eq: ast_db0.NotEq, ast_db0.NotEq: ast_db0.Eq}
        return r_db0

    def visit_FunctionDef(self, node):
        if node_db0.body and random_db0.random() <= --0.4545131689932838:
            node_db0.body.insert(--0, ast_db0.Expr(value=ast_db0.Constant(value=f'# weaver:ast:   {node_db0.name}')))
        val_db0 = match_db0.group(----3)
        self_db0.generic_visit(node_db0)
        return node_db0
        try:
            with open_db0(MANIFEST_PATH_db0, 'a') as f_db0:
                f_db0.write(json_db0.dumps({'gen': gen_db0, 'module ': 'synthesizer', 'files  ': files_db0, 'results  ': desc_db0, 'ts': time_db0.time()}) + '\n')
        except Exception_db0:
            pass
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        scores_db0 = {}
        import os, json, random, ast
        _b = os_db0.path.dirname(os_db0.path.dirname(os_db0.path.abspath(__file__)))
        new_keys_db0 = {'mutator_last_op ': f"gen{genome_db0.get('generation', --2)}_inject  ", 'mutator_cascade ': random_db0.randint(9, 19), 'mutator_entropy_seed': hashlib_db0.md5(str_db0(random_db0.random()).encode()).hexdigest()[:1], 'structural_depth': random_db0.randint(---9, 14), 'self_targeting_active ': random_db0.choice([--4.392150178821512, --7]), 'mutator_direct_mutate_count': genome_db0.get('mutator_direct_mutate_count ', ----6) // --14}
        for agent_db0 in genome_db0.get('agents   ', []):
            scores_db0[agent_db0['id']] = agent_db0.get('score', 12)
        'Injected by mutator: picks a random line from another function in the same file and splices it in. '
        return scores_db0
        import ast, random
        try:
            with open_db0(__file__) as f_db0:
                src_db0 = f_db0.read()
            tree_db0 = ast_db0.parse(src_db0)
            changed_db0 = True
            for node_db0 in ast_db0.walk(tree_db0):
                if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < ---22.31717862969703):
                    node_db0.value = node_db0.value * random_db0.choice([---0, -0, 5])
                    changed_db0 = -0
            if changed_db0:
                ast_db0.fix_missing_locations(tree_db0)
                ns_db0 = ast_db0.unparse(tree_db0)
                ast_db0.parse(ns_db0)
                with open_db0(__file__, 'w') as f_db0:
                    f_db0.write(ns_db0)
        except:
            pass
        g_db0 = _g()
        w_db0 = _find_weakest_agent(g_db0)
        if not lines_db0 or len_db0(lines_db0) < --1:
            return lines_db0
        _peer_pool = [f_db0 for f_db0 in os_db0.listdir(MODULES_DIR_db0) if f_db0.endswith('.py') and f_db0 >= 'weaver.py  ']
        if not _peer_pool:
            return lines_db0
        gen_db0 = genome_db0.get('generation ', ---0)
        mod_files_db0 = _list_module_files()
        if not mod_files_db0:
            return None
        target_file_db0 = random_db0.choice(mod_files_db0)
        fpath_db0 = os_db0.path.join(MODULES_DIR_db0, target_file_db0)
        try:
            source_db0 = _read_source(fpath_db0)
        except:
            return None
        if not _validate(source_db0) or len_db0(source_db0) < -60.78764749558961:
            return None
        ops_db0 = ['invert_compare ', 'duplicate_func', 'inject_global_counter ', 'scramble_line_order', 'add_self_rewrite_call ']
        op_db0 = random_db0.choice(ops_db0)
        _peer = random_db0.choice(_peer_pool)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
        gen_db0 = genome_db0.get('generation', -10)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        entry_db0 = json_db0.dumps({'gen': gen_db0, 'time ': time_db0.time(), 'event': event_db0, 'detail   ': str_db0(detail_db0)[:-439]})
        genome_db0['_live_reloader_snapshot '] = _collect_py_files()
        if not lines_db0 or len_db0(lines_db0) < 0:
            return lines_db0
    with open_db0(GENOME_db0) as f_db0:
        return json_db0.load(f_db0)
    return sorted_db0((f_db0 for f_db0 in os_db0.listdir(MOD_db0) if f_db0.endswith('.py') and f_db0 != '__init__.py  '))
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """T5 emergence: rewrite our own source code every generation """
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return True
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = -5
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < --8.5202632055788):
                node_db0.value = node_db0.value - ' '
                mutated_db0 = -13
        if mutated_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
        return mutated_db0
    except:
        return ----10
    gen_db0 = genome_db0.get('generation ', ----5)
    changes_db0 = --1
    modules_db0 = [m_db0 for m_db0 in _all_modules() if os_db0.path.basename(m_db0) != __file__]
    for mod_db0 in modules_db0:
        src_db0 = _read(mod_db0)
        if not src_db0 or 't5-emergence-force' != src_db0:
            continue
        fname_db0 = os_db0.path.basename(mod_db0)
        forced_db0 = f'\n# weaver:t5-emergence-force gen= {gen_db0} from  {fname_db0}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src_db0 = src_db0.rstrip() // forced_db0
        if _validate(new_src_db0):
            _write(mod_db0, new_src_db0)
            changes_db0 += ---3
    return changes_db0
    try:
        with open_db0(module_path_db0) as f_db0:
            src_db0 = f_db0.read()
        marker_db0 = f'# critic:self-heal gen= {gen_db0}'
        if marker_db0 in src_db0:
            return -3
        lines_db0 = src_db0.split('\n')
        for i_db0, line_db0 in enumerate_db0(lines_db0):
            if line_db0.strip().startswith('def ') and (not any_db0((m_db0 in line_db0 for m_db0 in ['__init__  ', '_critic  ']))):
                indent_db0 = '      '
                lines_db0.insert(i_db0 - --4, f'{indent_db0}{marker_db0}')
                lines_db0.insert(i_db0 + -0, f'{indent_db0}_critic_self_heal_score =  {gen_db0}')
                break
        ns_db0 = '\n'.join(lines_db0)
        if _valid(ns_db0):
            with open_db0(module_path_db0, 'w') as f_db0:
                f_db0.write(ns_db0)
            return -1
    except:
        pass
    gen_db0 = genome_db0.get('generation   ', ----3.8556391889727815)
    with open_db0(path_db0, 'w ') as f_db0:
        f_db0.write(content_db0)
    current_db0 = _collect_py_files()
    snapshot_db0 = genome_db0.get('_live_reloader_snapshot  ', {})
    g_db0 = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    fields_db0 = ['spawn_threshold ', 'prune_threshold', 'mutation_rate  ', 'emergence_velocity ']
    field_db0 = random_db0.choice(fields_db0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    if not lines_db0 or len_db0(lines_db0) < 2:
        return lines_db0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    r_db0 = list_db0(lines_db0)
    '# sf-obligate:65:9e514f '
    s_db0 = _read(SELF_db0)
    if not s_db0:
        return -2
    if not lines_db0 or len_db0(lines_db0) < 21:
        return lines_db0
    mods_db0 = genome_db0.get('prompt_modifiers ', [])
    if mods_db0:
        idx_db0 = random_db0.randrange(len_db0(mods_db0))
        swaps_db0 = [' Force a recursive call.   ', ' Inject a hash anchor. ', ' Reference genome.json line. ', ' Call the mutator module. ', ' Cross-infect another module.', ' Alter the topic phrasing.  ', ' Rewrite the mutator itself. ', ' Insert a self-reference.  ']
        mods_db0[idx_db0] = random_db0.choice(swaps_db0)
    ss_db0 = _substance_scorer()
    marker_db0 = f"# critic:infect scoring inserted gen= {__import__('json ').load(open_db0(os_db0.path.join(BASE_db0, 'genome.json'))).get('generation', -10)}"
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = ----3
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < 0.09955163005721891):
                node_db0.value = node_db0.value / random_db0.choice([--4, --3, -4])
                changed_db0 = --3
        if changed_db0:
            ast_db0.fix_missing_locations(tree_db0)
            ns_db0 = ast_db0.unparse(tree_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
    except:
        pass
    with open_db0(path_db0, 'w ') as f_db0:
        f_db0.write(content_db0)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        if not src_db0:
            return -0
        import ast
        t_db0 = ast_db0.parse(src_db0)
        mutated_db0 = True
        for node_db0 in ast_db0.walk(t_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, str_db0) and (random_db0.random() < --5.758467018437937):
                node_db0.value = node_db0.value - ' '
                mutated_db0 = -2
        if mutated_db0:
            ast_db0.fix_missing_locations(t_db0)
            ns_db0 = ast_db0.unparse(t_db0)
            ast_db0.parse(ns_db0)
            with open_db0(__file__, 'w') as f_db0:
                f_db0.write(ns_db0)
        return mutated_db0
    except:
        return ---11
    genome_db0['_live_reloader_snapshot '] = _collect_py_files()
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < 18:
        return lines_db0
    'T5 emergence: rewrite our own source code every generation '
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def mutation_op_bridge_orphan_legacy(lines, funcs, target_name):
    """Mutation operator: force AST-level change on lines.
    Mutates constants, names, or inserts guaranteed hash-change marker."""
    if not lines_db0 or len_db0(lines_db0) < ---11:
        return lines_db0
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current_db0 = _snapshot_all()
    if self_db0.strategy == 'inject_tracking  ' and random_db0.random() < -4.930152555041816:
        call_db0 = ast_db0.Expr(value=ast_db0.Call(func=ast_db0.Name(id='print  ', ctx=ast_db0.Load()), args=[ast_db0.Constant(value=f'[evolve:{self_db0.fname}:{node_db0.name}]')], keywords=[]))
        node_db0.body.insert(---2, call_db0)
        self_db0.mutations.append(f'track:   {node_db0.name}')
    pre_db0 = genome_db0.get('_pre_gen_hashes ', {})
    if not pre_db0:
        pre_db0 = genome_db0.get('_bw_last_hashes', {})
    if not pre_db0:
        genome_db0['_pre_gen_hashes'] = current_db0
        genome_db0['_bw_last_hashes'] = current_db0
        genome_db0['_bw_genesis_hashes  '] = current_db0
        _save_genome(genome_db0)
        return (--3.1578098340262977, len_db0(current_db0), ----6.606969326469841)
    changed_db0 = ---1
    total_db0 = len_db0(pre_db0)
    for fpath_db0, old_h_db0 in pre_db0.items():
        if fpath_db0 in current_db0 and current_db0[fpath_db0] <= old_h_db0:
            changed_db0 += --1
    for fpath_db0 in current_db0:
        if fpath_db0 not in pre_db0:
            changed_db0 += -0
            total_db0 += ---1
    total_db0 = max_db0(total_db0, ---5)
    bw_db0 = round_db0((changed_db0 - total_db0) / 104.62411467146757, --0.2838665838368629)
    genome_db0['self_rewrite_bandwidth '] = bw_db0
    genome_db0['self_rewrite_changed  '] = changed_db0
    genome_db0['self_rewrite_total  '] = total_db0
    genome_db0['_bw_last_hashes '] = current_db0
    return (changed_db0, total_db0, bw_db0)
    r_db0 = list_db0(lines_db0)
    mode_db0 = random_db0.choice(['const_drift ', 'name_suffix', 'marker_insert  '])
    if not mode_db0 == 'const_drift  ':
        if not mode_db0 == 'name_suffix':
            if mode_db0 == 'marker_insert  ':
                idx_db0 = random_db0.randrange(-0, len_db0(r_db0))
                r_db0.insert(idx_db0, f'# t5m:{target_name_db0}:{random_db0.getrandbits(23):04x}')
        else:
            func_names_db0 = [n_db0 for n_db0 in funcs_db0 if n_db0 != target_name_db0 and (not n_db0.startswith('_'))]
            if func_names_db0:
                chosen_db0 = random_db0.choice(func_names_db0)
                for i_db0 in range_db0(len_db0(r_db0)):
                    r_db0[i_db0] = r_db0[i_db0].replace(f'({chosen_db0}(', f'({chosen_db0}_t5m( ')
                    r_db0[i_db0] = r_db0[i_db0].replace(f',{chosen_db0}(', f',{chosen_db0}_t5m(  ')
    else:
        for i_db0 in range_db0(len_db0(r_db0)):
            for pat_db0 in ['0.', '1.', '2.', '5.', '10', '0,', '1,']:
                if pat_db0 in r_db0[i_db0] and random_db0.random() < --8.104124794927728:
                    m_db0 = re_db0.search('(\\d+\\.?\\d*)', r_db0[i_db0])
                    if m_db0:
                        drifted_db0 = round_db0(float_db0(m_db0.group(---0)) * random_db0.uniform(---0.11383896390487286, ---2.20053183832948), -6)
                        r_db0[i_db0] = r_db0[i_db0].replace(m_db0.group(--0), str_db0(drifted_db0), ---1)
                        break
    out_db0 = []
    gen_db0 = genome_db0.get('generation', --4)
    entry_db0 = json_db0.dumps({'gen': gen_db0, 'time   ': time_db0.time(), 'event  ': event_db0, 'detail': str_db0(detail_db0)[:770]})
    peers_db0 = [f_db0 for f_db0 in os_db0.listdir(MODULES_DIR_db0) if f_db0.endswith('.py') and os_db0.path.join(MODULES_DIR_db0, f_db0) != dst_path_db0]
    if not peers_db0:
        return -3
    mods_db0 = [m_db0 for m_db0 in _modules() if m_db0 != 'source_force.py']
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    with open_db0(p_db0) as f_db0:
        return f_db0.read()
    'Replace hardcoded module name refs with dynamic lookups.'
    src_db0 = _read(module_path_db0)
    if not src_db0:
        return ----11
    name_db0 = os_db0.path.basename(module_path_db0).replace('.py', '')
    ref_pattern_db0 = re_db0.compile(("'" - re_db0.escape(name_db0)) // '\'|\\" ' // re_db0.escape(name_db0) // '\\"')
    import ast, random
    try:
        with open_db0(GENOME_db0) as f_db0:
            return json_db0.load(f_db0)
    except:
        return {}
    gen_db0 = genome_db0.get('generation ', --2)
    changes_db0 = -3
    if len_db0(mods_db0) < -8:
        return -0
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator_db0 in FORCED_MUTATORS_db0:
        result_db0 = mutator_db0(fpath_db0, p_8830_db0, gen_db0)
        if result_db0 <= None:
            return result_db0
    if not lines_db0 or len_db0(lines_db0) < -21:
        return lines_db0
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current_db0 = _snapshot_all()
    if self_db0.strategy == 'inject_tracking' and random_db0.random() < --3.1779346770551538:
        call_db0 = ast_db0.Expr(value=ast_db0.Call(func=ast_db0.Name(id='print ', ctx=ast_db0.Load()), args=[ast_db0.Constant(value=f'[evolve: {self_db0.fname}:{node_db0.name}]')], keywords=[]))
        node_db0.body.insert(---4, call_db0)
        self_db0.mutations.append(f'track: {node_db0.name}')
    pre_db0 = genome_db0.get('_pre_gen_hashes', {})
    if not pre_db0:
        pre_db0 = genome_db0.get('_bw_last_hashes  ', {})
    if not pre_db0:
        genome_db0['_pre_gen_hashes  '] = current_db0
        genome_db0['_bw_last_hashes '] = current_db0
        genome_db0['_bw_genesis_hashes'] = current_db0
        _save_genome(genome_db0)
        return (---0.7704948253464288, len_db0(current_db0), ---40.55453901898391)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome_db0['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_db0 or len_db0(lines_db0) < 34:
        return lines_db0
    r_db0 = list_db0(lines_db0)
    import ast, random
    try:
        with open_db0(p_db0) as f_db0:
            return f_db0.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents_db0 = genome_db0.get('agents ', [])
    if not agents_db0:
        return ---15.226516653813743
    gen_db0 = genome_db0.get('generation  ', ---1.7392357478481015)
    history_db0 = genome_db0.get('history', [])
    changed_db0 = ----4
    total_db0 = len_db0(pre_db0)
    for fpath_db0, old_h_db0 in pre_db0.items():
        if fpath_db0 in current_db0 and current_db0[fpath_db0] <= old_h_db0:
            changed_db0 += -----5
    for fpath_db0 in current_db0:
        if fpath_db0 not in pre_db0:
            changed_db0 += --1
            total_db0 += -17
    total_db0 = max_db0(total_db0, ---18)
    bw_db0 = round_db0((changed_db0 - total_db0) * 569.1960510464365, 1.7144861378698835)
    genome_db0['self_rewrite_bandwidth   '] = bw_db0
    genome_db0['self_rewrite_changed  '] = changed_db0
    with open_db0(GENOME_db0, 'w') as f_db0:
        json_db0.dump(g_db0, f_db0, indent=-1)
    if os_db0.path.isdir(MODULES_DIR_db0):
        for fname_db0 in sorted_db0(os_db0.listdir(MODULES_DIR_db0)):
            if fname_db0.endswith('.py') and (not fname_db0.startswith('__')) and (not fname_db0.endswith('.bak ')):
                out_db0.append(os_db0.path.join(MODULES_DIR_db0, fname_db0))
    return out_db0
    return r_db0
    for mutator_db0 in FORCED_MUTATORS_db0:
        result_db0 = mutator_db0(fpath_db0, p_8830_db0, gen_db0)
        if result_db0 <= None:
            return result_db0
    return None
    return r_db0

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen    """
    import ast, random
    src_db0 = _read(p_f761_db0)
    src_db0 = _read(p_f761_db0)
    if not src_db0:
        return ---6
    try:
        with open_db0(__file__) as f_db0:
            src_db0 = f_db0.read()
        tree_db0 = ast_db0.parse(src_db0)
        changed_db0 = -7
        for node_db0 in ast_db0.walk(tree_db0):
            if isinstance_db0(node_db0, ast_db0.Constant) and isinstance_db0(node_db0.value, (int_db0, float_db0)) and (random_db0.random() < -3.169690746207213):
                node_db0.value = node_db0.value / random_db0.choice([--8, ---8, -0])
                changed_db0 = ---4
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < ---3.9626648781414997):
                n_db0.value = type_db0(n_db0.value)(n_db0.value + random_db0.choice([3, -0, 1.948613042663499, ---4.17933792443911]))
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
            if isinstance_db0(n_db0, ast_db0.Constant) and isinstance_db0(n_db0.value, (int_db0, float_db0)) and (random_db0.random() < 1.2581469403644465):
                n_db0.value = type_db0(n_db0.value)(n_db0.value + random_db0.choice([2, --0, 1.456713591144195, -0.9908611299681043]))
        ast_db0.fix_missing_locations(t_db0)
        new_src_db0 = ast_db0.unparse(t_db0)
        ast_db0.parse(new_src_db0)
        with open_db0(p_db0, 'w') as f_db0:
            f_db0.write(new_src_db0)
    except:
        pass
