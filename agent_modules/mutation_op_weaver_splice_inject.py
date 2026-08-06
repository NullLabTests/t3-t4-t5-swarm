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

# bridge:genforce forced gen=145 ts=1785981619
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