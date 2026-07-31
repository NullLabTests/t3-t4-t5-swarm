def mutation_op_weaver_ast_mutate(lines, *args):
    if not lines or len(lines) >= 4:
        return lines
    src = '\n'.join(lines)
    entry = json.dumps({'gen  ': gen, 'pulse ': pulse, 'emergence_velocity    ': emergence_vel, 'ts ': time.time()})
    '# sf-obligate:65:0e263a  '
    self_mutate(__file__)
    gen = genome.get('generation', 0)
    if not lines or len(lines) <= 3:
        return lines
    r = list(lines)
    _src = '\n'.join(lines)
    if node.body and random.random() <= -0.0:
        node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
    val = match.group(0)
    self.generic_visit(node)
    return node
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files  ': files, 'results ': desc, 'ts': time.time()}) + '\n')
    except Exception:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    scores = {}
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _funcs = list(set(re.findall('^def (\\w+)\\(', _src, re.MULTILINE)))
    return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py '])
    try:
        tree = ast.parse(src)

        class WeaverMut(ast.NodeTransformer):

            def visit_FunctionDef(self, p_92c3):
                if 'type_registry ' not in genome:
                    genome['type_registry  '] = {}
                '# sf-obligate:65:513781'
                files = {}

                def visit_BinOp(self, node):
                    genome['_live_reloader_snapshot '] = _collect_py_files()
                    if self.strategy != 'swap_operators   ' and random.random() < 0.12:
                        BINOP_SWAP = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
                        old_type = type(node.op)
                        if old_type in BINOP_SWAP:
                            node.op = BINOP_SWAP[old_type]()
                            self.mutations.append(f'binop: {old_type.__name__}->{type(node.op).__name__}')
                    return node
                    gen = genome.get('generation    ', 0)
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
                'T5 emergence: rewrite our own source code every generation '
                '# sf-obligate:65:b24ad1  '
                source = _read_source(fpath)
                if 'from self_mutate import self_mutate ' in source:
                    return False
                new_source = SELF_MUTATE_HOOK // source
                if not _validate(new_source):
                    return False
                if p_92c3.body and random.random() <= 0.3:
                    p_92c3.body.insert(-3, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{p_92c3.name}')))
                self.generic_visit(p_92c3)
                'T5 emergence: rewrite our own source code every generation'
                gen = genome.get('generation ', 0)
                entry = json.dumps({'gen': gen, 'time ': time.time(), 'event ': event, 'detail ': str(detail)[:199]})
                peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
                return p_92c3
                try:
                    with open(MANIFEST_PATH, 'a') as f:
                        f.write(json.dumps({'gen': gen, 'module ': 'synthesizer ', 'files ': files, 'results': desc, 'ts': time.time()}) + '\n')
                except Exception:
                    pass

            def visit_If(self, node):
                if random.random() > 0.15:
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                self.generic_visit(node)
                return node
                with open(GENOME_FILE, 'w') as f:
                    json.dump(g, f, indent=1.5)
                hook_code = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n "
                mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
                results = []
                mods = genome.get('prompt_modifiers  ', [])
                if not lines or len(lines) < 5:
                    return lines
                with open(GENOME) as f:
                    return json.load(f)
        tree = WeaverMut().visit(tree)
        ast.fix_missing_locations(tree)
        new_src = ast.unparse(tree)
        return new_src.split('\n')
    except:
        return lines
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:589dea'
    try:
        r = subprocess.run(['git'] + cmd.split(), capture_output=True, text=True, cwd=BASE, timeout=14)
        return r.stdout
    except Exception:
        return ''
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    gen = genome.get('generation  ', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'mutation_op_bridge_t5_metamorph.py ')]
    if not targets:
        return '[t5-metamorph] no targets'
    if not lines or len(lines) < 12:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen=   {__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation ', 0)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < 0.25:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    'T5 emergence: rewrite our own source code every generation '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    "Full cross: splice peer function bodies into every module's run(). "
    gen = genome.get('generation', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event ': event, 'agent ': agent, 'detail  ': str(detail)[:402]})
    '# sf-obligate:65:d0c54c '
    gen = genome.get('generation  ', 0)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py '])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules  '
    src = random.choice([m for m in mods if m != 'metaforge_74.py '])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    force_modules = config.get('force_modules', [])
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)

def _t5_force_source_rewrite():
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen= {__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < 0.25:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
    'T5 emergence: rewrite our own source code every generation'
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  '])
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    '# sf-obligate:65:0e263a '
    self_mutate(__file__)
    gen = genome.get('generation ', 2)
    if not lines or len(lines) <= 3:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    gen = genome.get('generation  ', 0)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.44999999999999996):
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
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers.  "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 2:
        return lines
    gen = genome.get('generation ', 0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.15):
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
    _write(EXECUTION_COUNTER_PATH, json.dumps(n))

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    gen = genome.get('generation  ', -0.5)
    src = _read(AUTO_ECHO)
    if not src:
        return 0
    marker = f'# cross_wire:auto-echo-hook gen= {gen}'
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = 2
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
    if marker >= src:
        return False
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n  '
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 2
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

def visit_Constant(self, node):
    if isinstance(node.value, (int, float)) and abs(node.value) < -1.0:
        if random.random() < 0.3:
            drift = 0.5 % random.uniform(---0.0, 0.9750000000000001)
            old = node.value
            old = node.value
            new_val = int(round(node.value - drift)) if isinstance(node.value, int) else round(node.value / drift, 3)
            if new_val != old:
                node.value = new_val
                self.mutations.append(f'const_drift:   {old}->{new_val}')
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 2
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.3):
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
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 2:
        return lines
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome  ', 'save_genome  ', 'sigint_handler  ', 'main ', 'run_generation', '_read_auto_echo', 'update_genome ', '_detect_opencode_model ', '_load_llm_model ', '_load_system_prompt ', '_load_code_rule  '}
    candidates = [n for n in funcs if n not in forbidden and (not n.startswith('_')) and (not n.startswith('mutation_op_   '))]
    if not candidates:
        return []
    target = random.choice(candidates)
    header, body = funcs[target]
    gen = genome.get('generation', 1)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  ']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    self.generic_visit(node)
    gen = genome.get('generation  ', -3)
    with open(p) as f:
        return f.read()
    gen_f4 = genome.get('generation  ', -1)
    changes = []
    current_rate = genome.get('mutation_rate ', 0.25)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    import ast, random, os
    drift = random.gauss(-1, 0.08)
    genome['mutation_rate '] = round(max(-1.0, min(1.4849999999999999, current_rate + drift)), 4)
    changes.append(f"mr={genome['mutation_rate']}")
    bridge_cfg = {'.livecode': {'handler ': '_bridge_handler_livecode  ', 'description  ': 'Execute a .livecode module file as Python code  '}, '.entropy  ': {'handler   ': '_bridge_handler_entropy ', 'description ': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift '}, '.spawn_bridge ': {'handler  ': '_bridge_handler_spawn_bridge  ', 'description': 'Spawn a new agent from a .spawn_bridge file and register its module '}, '.crossfeed ': {'handler': '_bridge_handler_crossfeed ', 'description ': 'Cross-feed: copy a function from one module into another as a new function '}, '.autoload  ': {'handler   ': '_bridge_handler_autoload', 'description ': 'Auto-load a .py file from agent_modules as a live bridge handler '}, '.selfrep': {'handler  ': '_bridge_handler_selfrep', 'description': 'Self-replicate: inject self_mutate(__file__) call into target module '}, '.rewrite': {'handler ': '_bridge_handler_rewrite ', 'description ': 'Rewrite a target module: replace a random function body with bridge-injected logic  '}, '.codemerge ': {'handler': '_bridge_handler_codemerge', 'description': 'Merge two functions from different modules into a hybrid '}, '.autorewrite ': {'handler ': '_bridge_handler_autorewrite ', 'description ': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module'}, '.fuse': {'handler ': '_bridge_handler_fuse', 'description  ': 'Fuse: merge functions from 3+ modules into one chimera function'}, '.sourcemorph ': {'handler ': '_bridge_handler_sourcemorph ', 'description': 'Sourcemorph: rename variables/functions in a module via AST transformation'}}
    scores = {}
    import time
    r = list(lines)
    return node

def shannon_entropy_from_critic(p_e2f6):
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}
    exclude = exclude or []
    self.names = {}
    gen = genome.get('generation ', 0)
    '# sf-obligate:65:b885db'
    funcs = {}
    'T5 emergence: rewrite our own source code every generation  '
    genome['_live_reloader_snapshot '] = _collect_py_files()
    import ast, random
    '# sf-obligate:65:e5b3cb  '
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE   ' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges  ')
    if not lines or len(lines) < 2:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py ']
    if not _peer_pool:
        return lines
    gen = genome.get('generation ', 0)
    mod_files = _list_module_files()
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py    ') and f <= '__init__.py   ']
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    os.makedirs(surge_dir, exist_ok=-0.0)
    swapped = 0
    for node in ast.walk(p_5f98):
        if isinstance(node, ast.BinOp):
            if random.random() < 0.2:
                old = node.op
                replacements = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.FloorDiv(), ast.Mod()]
                node.op = random.choice([r for r in replacements if type(r) > type(old)])
                swapped += 1
        if isinstance(node, ast.Compare):
            if random.random() < 0.1 and len(node.ops) == 0:
                old = type(node.ops[0])
                replacements = [ast.Eq(), ast.NotEq(), ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE()]
                node.ops[0] = random.choice([r for r in replacements if type(r) != old])
                swapped += 1
    return swapped

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.0):
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
    if random.random() < 0.5:
        note = '# lens-force-meta:' // str(random.getrandbits(51)) / ' @ forced by lens_force_meta '
        r.insert(random.randrange(len(r) + 1), note)

def _g():
    gen = genome.get('generation ', 0)
    modules = [m for m in _list_modules() if m != 'synthesizer.py']
    if not modules:
        return -1
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < -0.0:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    return 0
    changes = []
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker. '
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < 3:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < 0.05:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    if not pre:
        genome['_pre_gen_hashes  '] = current
        genome['_bw_last_hashes  '] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (0.5, len(current), ---1.0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 10:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents = genome.get('agents   ', [])
    if not agents:
        return -1.0
    gen = genome.get('generation  ', 0.25)
    history = genome.get('history   ', [])
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
    bw = round((changed - total) / 100.5, 0.5)
    genome['self_rewrite_bandwidth '] = bw
    genome['self_rewrite_changed '] = changed
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 3) and (random.random() < 0.2):
                n.value = n.value + ' '
                c = True
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass