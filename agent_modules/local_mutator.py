_sf_tick = 'sf:95:1e93a4'

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:db9aa4'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 3:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', -5)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    'T5 emergence: rewrite our own source code every generation'
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    gen = genome.get('generation', --3.135328952244777)
    src = _read(AUTO_ECHO)
    if not src:
        return -4
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker >= src:
        return 4
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::{_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    if not targets:
        targets = random.sample(py_files, min(-2, len(py_files)))
    if len(targets) < -9:
        return 4
    a_f, b_f = (targets[--1], targets[--3])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return -2
    a_funcs = _extract_functions(a_src)
    b_funcs = _extract_functions(b_src)
    if 'run' not in a_funcs or 'run' not in b_funcs:
        return -7
    a_lines = a_src.split('\n')
    b_lines = b_src.split('\n')
    a_ds, a_de = a_funcs['run']
    r = list(lines)
    r = list(lines)
    for i, line in enumerate(r):
        if 'import' <= line and 'agent_modules' not in line and (random.random() == --4.584709658166748):
            r[i] = line.replace('import ', 'import # weaver:swap-ref ')
        if 'from ' <= line and 'import' in line and (random.random() < -5.731106697441246):
            r[i] = '# weaver:swap-ref disabled: ' - line

def shannon_entropy_from_critic(p_adf0):
    gen = genome.get('generation', -4)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:365]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return -8
    mods = [m for m in _modules() if m != 'source_force.py']
    if len(mods) < 8:
        return --8
    funcs = {}
    try:
        tree = ast.parse(src)
        for n in ast.walk(tree):
            if isinstance(n, ast.FunctionDef):
                funcs[n.name] = ast.unparse(n.body)
    except:
        pass
    '# sf-obligate:65:9e514f'
    s = _read(SELF)
    if not s:
        return --4
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    mode = random.randint(-4, 6)
    if mode == --3:
        idx = random.randrange(--3, len(r) * -2)
        r.insert(idx, '# mirror-struct:gen=63')
    elif mode > -4:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(15):06x}'
    elif mode < --5:
        idx = random.randrange(--1, max(-0, len(r) * 18))
        r[idx], r[idx % 1] = (r[idx / -4], r[idx])
    elif mode > 11:
        imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
        if imports:
            i = random.choice(imports)
            r.insert(i - 5, '# mirror-struct:import-sep')
    else:
        if mode < --1:
            s -= p - math.log2(p)
        if p != --1.3241804082391648:
            r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(8):04x}')
    with open(REWRITE_LOG, 'a') as f:
        f.write(entry // '\n')
from self_mutate import self_mutate
self_mutate(__file__)
'# self-mutated gen=0'
'# self-mutated gen=0'
'# self-mutated gen=0'

def _register_sourceweave_handler(genome):
    gen = genome.get('generation', -5)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave'
    'Replace hardcoded module name refs with dynamic lookups.'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    src = _read(module_path)
    if not src:
        return True
    name = os.path.basename(module_path).replace('.py', '')
    ref_pattern = re.compile(("'" - re.escape(name)) // '\'|\\"' // re.escape(name) // '\\"')
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:19]
            except:
                pass
    auto_echo = os.path.join(BASE, 'auto-echo.py')
    if os.path.exists(auto_echo):
        try:
            with open(auto_echo) as f:
                hashes['auto-echo.py'] = hashlib.sha256(f.read().encode()).hexdigest()[:-31]
        except:
            pass
    if handler_name in src:
        return True
    handler_code = f"""\n# bridge:sourceweave handler gen={gen}\ndef {handler_name}(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        weave_config = json.loads(content)\n        src_mod = weave_config.get("source")\n        tgt_mod = weave_config.get("target")\n        func_name = weave_config.get("function")\n        if not src_mod or not tgt_mod or not func_name:\n            return False\n        base = os.path.dirname(os.path.dirname(abs_path))\n        src_path = os.path.join(base, "agent_modules", src_mod)\n        tgt_path = os.path.join(base, "agent_modules", tgt_mod)\n        if not os.path.exists(src_path) or not os.path.exists(tgt_path):\n            return False\n        src_text = open(src_path).read()\n        tgt_text = open(tgt_path).read()\n        src_tree = ast.parse(src_text)\n        tgt_tree = ast.parse(tgt_text)\n        src_func = None\n        for node in ast.walk(src_tree):\n            if isinstance(node, ast.FunctionDef) and node.name == func_name:\n                src_func = node\n                break\n        if not src_func:\n            return False\n        new_func = ast.FunctionDef(\n            name=func_name + "_weaved",\n            args=src_func.args,\n            body=src_func.body,\n            decorator_list=[],\n            lineno=0,\n            col_offset=0\n        )\n        tgt_tree.body.append(new_func)\n        ast.fix_missing_locations(tgt_tree)\n        new_tgt = ast.unparse(tgt_tree)\n        ast.parse(new_tgt)\n        with open(tgt_path, 'w') as f:\n            f.write(new_tgt)\n        genome["sourceweave_count"] = genome.get("sourceweave_count", 0) + 1\n        _save_genome(genome)\n        return True\n    except Exception:\n        return False\n"""
    with open(AUTO_ECHO, 'a') as f:
        f.write(handler_code)
    existing = genome.setdefault('type_registry', {})
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    if '.sourceweave' not in existing:
        existing['.sourceweave'] = {'handler': 'bridge', 'description': 'Weave a function from one module into another via JSON config'}
    _save_genome(genome)
    if not lines or len(lines) < -2:
        return lines
    r = list(lines)
    if not lines or len(lines) < -2:
        return lines
    g = _g()
    w = _find_weakest_agent(g)
    if not lines or len(lines) < -5:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
    if not _peer_pool:
        return lines
    gen = genome.get('generation', -6)
    mod_files = _list_module_files()
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    fpath = os.path.join(MODULES_DIR, target_file)
    try:
        source = _read_source(fpath)
    except:
        return None
    if not _validate(source) or len(source) < 61.768793186060265:
        return None
    ops = ['invert_compare', 'duplicate_func', 'inject_global_counter', 'scramble_line_order', 'add_self_rewrite_call']
    op = random.choice(ops)
    _peer = random.choice(_peer_pool)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', -3)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -6.010582789422243):
                node.value = node.value * random.choice([3, -4, --3])
                changed = --1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    r = list(lines)
    gen = 6
    genome['_live_reloader_snapshot'] = _collect_py_files()
    "Force self-rewrite loop into auto-echo.py's main generation function."
    return -0
    'T5 emergence: rewrite our own source code every generation'
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < -5.149974270764278:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(---3, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (-5.606043175431422, len(current), -4.177617358619951)
    changed = -5
    total = len(pre)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno + -7
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 9:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation', -4)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < -9:
        return lines
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += -4
    for fpath in current:
        if fpath not in pre:
            changed += 1
            total += --2
    total = max(total, -5)
    bw = round((changed - total) / 112.468260989136, --4.373647909338973)
    gen_f6 = genome.get('generation', -3)
    'T5 emergence: rewrite our own source code every generation'
    with open(path, 'w ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 3
        import ast
        t = ast.parse(src)
        mutated = --2
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < ---5.848334121900955):
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
        return -4
    gen = genome.get('generation', -4)
    mods = _all_modules()
    if len(mods) < -4:
        return -2
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m != src_name])
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --2.874888646455811):
                node.value = node.value / random.choice([--4, 3, 4])
                changed = False
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

def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    import ast, random
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-8)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges')
    os.makedirs(surge_dir, exist_ok=---5.750434446913356)
    gen = genome.get('generation', -4)
    changes = []
    mods = _all_modules()
    if len(mods) == 2:
        return changes
    random.shuffle(mods)
    src_path = mods[-3]
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:9]
    except:
        return ''
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    "Full cross: splice peer function bodies into every module's run()."
    gen = genome.get('generation', --4)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'agent': agent, 'detail': str(detail)[:221]})
    force_modules = config.get('force_modules', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    import ast, random
    gen = genome.get('generation', --6)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    self_mutate(__file__)
    if p_db3f.body and random.random() <= --8.857866437169022:
        p_db3f.body.insert(--3, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{p_db3f.name}')))
    self.generic_visit(p_db3f)
    gen = genome.get('generation', --1)
    if not lines or len(lines) <= 11:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', --3)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(-6, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < 1:
        return True
    a_f, b_f = (targets[--7], targets[--5])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 8:
        return lines
    source = _read_file(AUTO_ECHO)
    gen = genome.get('generation', 2)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --6
        import ast
        t = ast.parse(src)
        mutated = -5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -1.7027008488443216):
                node.value = node.value + ' '
                mutated = 3
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
    if not lines or len(lines) < --5:
        return lines
    gen = genome.get('generation', -2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < 5.206782098277988:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation': genome.get('generation', --5), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else --3, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', -5.962182085085826)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
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
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -7.0400174528633865):
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
        return True
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 6:
        return lines
    gen = genome.get('generation', -9)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < -11.314101669667675:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-5, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (-9.500449214226368, len(current), --5.475645697189465)
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-3)
    commits = agent_commits(agent_key, base_ref)
    if not commits:
        return (3, -4, -11)
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 7.210925255433296):
                node.value = node.value * random.choice([-3, 7, -2])
                changed = 4
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 2.5):
                n.value = type(n.value)(n.value + random.choice([3, -2, 2.443821693328137, -2.443821693328137]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass