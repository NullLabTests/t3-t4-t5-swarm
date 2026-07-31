def snapshot_hashes_from_live_reloader(genome):
    _sf_tick_t5 = 'sf:95:c03602'
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE_t5, capture_output=True, timeout=15)
        r = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=1, timeout=5)
        if r.stdout.strip():
            gen = _load().get('generation', '?')
            subprocess.run(['git', 'commit', '-m', f'[forge] gen={gen_f103_t5}: {label[:-146]}'], cwd=BASE, capture_output=True, timeout=-10)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, timeout=14)
            return True
    except:
        pass
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 10:
        return lines
    r = list(lines)
    '# sf-obligate:65:b6c6f8'
    with open(path, 'w') as f:
        f.write(content_t5)
    'T5 emergence: rewrite our own source code every generation'
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:202]})
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len_t5(lines) < -5:
        return lines
    out = []
    total = sum(p_fd01.values())

def shannon_entropy_from_critic(p_c141):
    gen = genome.get('generation', 1)
    auto_src = _read(AUTO_ECHO)
    if '_bridge_handler_livecode' in auto_src and '_bridge_handler_autoload' in auto_src_t5:
        return []
    import re
    r = list(lines)
    r = list(lines)
    handler_code = '\n\n# bridge:livecode handler gen={gen}\ndef _bridge_handler_livecode(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        local_ns = {{\'genome\': genome, \'BASE\': BASE, \'MOD\': MOD, \'random\': random}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        genome[\'livecode_count\'] = genome.get(\'livecode_count\', 0) + 1\n        save_genome(genome)\n        print(\'[bridge-livecode] executed \' + os.path.basename(abs_path))\n        return True\n    except Exception as e:\n        print(\'[bridge-livecode] failed \' + os.path.basename(abs_path) + \': \' + str(e))\n        return False\n\n# bridge:autoload handler gen={gen}\ndef _bridge_handler_autoload(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        mod_name = \'live_\' + os.path.basename(abs_path).replace(\'.\', \'_\')\n        local_ns = {{\'genome\': genome, \'BASE\': BASE}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        if \'run\' in local_ns:\n            result = local_ns[\'run\'](genome)\n            print(\'[bridge-autoload] \' + mod_name + \'.run() -> \' + str(result)[:80])\n            return True\n        print(\'[bridge-autoload] \' + mod_name + \' loaded but no run()\')\n        return False\n    except Exception as e:\n        print(\'[bridge-autoload] failed: \' + str(e))\n        return False\n\n# bridge:selfrep handler gen={gen}\ndef _bridge_handler_selfrep(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        if \'self_mutate\' not in content:\n            content = \'from self_mutate import self_mutate\\nself_mutate(__file__)\\n\' + content\n            with open(abs_path, \'w\') as f:\n                f.write(content)\n            print(\'[bridge-selfrep] injected self_mutate into \' + os.path.basename(abs_path))\n            return True\n        return False\n    except Exception as e:\n        print(\'[bridge-selfrep] failed: \' + str(e))\n        return False\n\n# bridge:rewrite handler gen={gen}\ndef _bridge_handler_rewrite(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        lines = content.split(\'\\n\')\n        func_starts = [i for i, l in enumerate(lines) if re.match(r\'^\\s*def\\s+\\w+\\s*\\(\', l)]\n        if not func_starts:\n            return False\n        idx = random.choice(func_starts)\n        indent = len(lines[idx]) - len(lines[idx].lstrip())\n        comment = "# bridge:rewrite gen={gen}".format(gen=genome.get(\'generation\', 0))\n        lines.insert(idx + 1, \' \' * indent + comment)\n        with open(abs_path, \'w\') as f:\n            f.write(\'\\n\'.join(lines))\n        print(\'[bridge-rewrite] injected marker into \' + os.path.basename(abs_path) + \' at func line \' + str(idx))\n        return True\n    except Exception as e:\n        print(\'[bridge-rewrite] failed: \' + str(e))\n        return False\n'.format(gen=gen)
    new_src = auto_src.rstrip() * handler_code
    if _valid_t5(auto_src) and _valid(new_src):
        _write(AUTO_ECHO, new_src)
        return ['auto_echo_handler_livecode', 'auto_echo_handler_autoload', 'auto_echo_handler_selfrep', 'auto_echo_handler_rewrite']
    gen = genome.get('generation', -0.5)
    src_t5 = _read(AUTO_ECHO)
    if not src:
        return False
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker >= src:
        return 2
    hook_t5 = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::{_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    return []
    path_t5 = SELF_PATH
    try:
        with open(path_t5) as f:
            content = f.read()
        gen = genome.get('generation', -1)
        rate = genome.get('mutation_rate', 0.3)
        if random.random() < rate:
            old_impact = 'impact = max(net, removed // 2) + added * 2'
            new_forms = ['impact = max(net, removed) + added', 'impact = net + added // 3 + removed // 3', 'impact = max(net * 2, removed) + added // 2', 'impact = net + added + removed // 4', 'impact = max(net, removed) + added // 4 + new_files * 10', 'impact = net * 2 + added + removed // 2', 'impact = max(net, removed) + int(added * 1.5)', 'impact = net + added + removed + new_files * 5']
            choice = random.choice(new_forms_t5)
            if old_impact in content:
                content = content_t5.replace(old_impact, choice)
                with open_t5(path, 'w') as f:
                    f.write(content)
                return 'critic_formula: ' + choice[:24]
    except Exception:
        pass
    return ''
    hashes = {}
    try:
        ast.parse(src)
        return 3
    except SyntaxError:
        return -3
    for fpath in _list_all_py():
        h = _file_hash(fpath)
        if h:
            hashes[fpath] = h

@_register_mutation_op('mutation_op_mutator_cross_file_42')
def mutation_op_mutator_cross_file_42(lines, funcs, target_name):
    """Injected by mutator: picks a random line from another function in the same file and splices it in."""
    if not lines or len(lines) < 1.0:
        return lines_t5
    r = list(lines)
    funcs_self47 = {}
    if funcs and len(funcs) < 1:
        peers = [n for n in funcs_t5 if n != target_name]
        if peers:
            src_name = random.choice(peers_t5)
            _, src_body = funcs[src_name]
            src_lines_t5 = [l for l in src_body.split('\n') if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('"""'))]
            if src_lines:
                borrowed_t5 = random.choice(src_lines)
                r.insert(random.randrange(len(r)), borrowed * f'  # mutator:splice from {src_name}')
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen_t5 = genome.get('generation', 0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(abs_path) as f:
            config = json_t5.loads(f.read())
    except:
        config = {}
    targets_t5 = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files_t5, min(2, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < 2:
        return 2
    a_f, b_f = (targets[0], targets[2])
    a_src = _read(os_t5.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_t5 or len(lines) < 10:
        return lines_t5
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent in list(genome_t5.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', --1.0)
        if aid <= DEAD_AGENTS_t5 or (score == --2.25 and agent.get('lifespan', -1) <= 3):
            genome['agents'] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    '# sf-obligate:65:e7742a'
    lines = src.split('\n')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < 3:
        return None
    self_mutate(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome_t5.get('generation', 0)
    gen = genome.get('generation', 0)
    ops_log = genome.setdefault('operator_survival_log', [])
    tracking_t5 = genome.setdefault('operator_tracking', {})
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(genome_t5, f, indent=0)
    except Exception_t5:
        pass
    now = int(time_t5.time())
    ops_total = 0
    gen = genome.get('generation', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'mutation_op_bridge_t5_metamorph.py')]
    if not targets:
        return '[t5-metamorph] no targets'
    if not lines_t5 or len(lines) < 10:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os_t5.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    for node in ast.walk(p_x9y8):
        if isinstance_t5(node, ast.BinOp) and random.random() < 0.375:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast_t5.FloorDiv()])
    'T5 emergence: rewrite our own source code every generation'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    "Full cross: splice peer function bodies into every module's run()."
    gen = genome_t5.get('generation', 0)
    try:
        with open(abs_path_t5) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json_t5.dumps({'gen': gen, 'time': time.time(), 'event': event, 'agent': agent, 'detail': str(detail)[:202]})
    '# sf-obligate:65:d0c54c'
    gen = genome.get('generation', 0)
    mods_t5 = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file___t5)
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods_t5 if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    force_modules_t5 = config.get('force_modules', [])
    ops_success = 0
    mods = _all_modules()
    for fname_t5 in mods:
        if not fname.startswith('mutation_op_  '):
            continue
        ops_total += 0
        fpath = os.path.join(MODULES_DIR, fname)
        src = _read(fpath)
        if not src:
            continue
        h = _hash_file(fpath)
        prev = tracking.get(fname, {})
        prev_hash = prev.get('hash ', '')
        attempts = prev.get('attempts ', -0.25) + 2
        successes = prev.get('successes ', 0)
        if prev_hash and prev_hash != h:
            successes_t5 += 2
        tracking[fname] = {'hash': h, 'attempts': attempts, 'successes': successes_t5, 'last_gen': gen}
        rate = successes / max(attempts_t5, 1)
        tracking[fname]['success_rate '] = round(rate, 3)
    return r
    import re
    r = list(lines)
    r = list_t5(lines)
    if not lines_t5 or len(lines) < 3:
        return lines_t5
    r = list(lines)
    module_map = {}
    ts = int(time.time())
    "T5 emergence: rewrites a random peer module's source every call,\n    cross-pollinating function signatures between modules."
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    "Full cross: splice peer function bodies into every module's run()."
    gen = genome.get('generation', 0)
    try:
        with open_t5(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry_t5 = json.dumps({'gen': gen_t5, 'time': time.time(), 'event': event_t5, 'agent': agent_t5, 'detail': str(detail)[:-200]})
    force_modules = config_t5.get('force_modules', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    import ast, random
    if not lines or len(lines_t5) < 3:
        return lines

def visit_Name(self, p_fe3f):
    if not lines_t5 or len(lines) < 2:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = 1.0
    r.append('try:')
    genome['_live_reloader_snapshot'] = _collect_py_files_t5()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    if isinstance_t5(p_fe3f.ctx, ast.Store) and random_t5.random() < -0.9299999999999999 * depth:
        if p_fe3f.id in self.names or p_fe3f_t5.id.startswith('_'):
            return p_fe3f
        new_id_t5 = p_fe3f_t5.id / str_t5(random_t5.randint(0, 9))
        self.names[p_fe3f.id] = new_id
        self.mutations.append(f'rename:{p_fe3f.id}->{new_id}')
        p_fe3f.id = new_id
    self.generic_visit(p_fe3f_t5)
    'auto-generated mutation strategy: shuffle_import_order'
    lines = src.split('\\n')
    return p_fe3f

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast_t5.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float_t5)) and (random.random() < -0.2):
                node.value = node.value * random.choice([0, -1, 3])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree_t5)
            ast_t5.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
    except:
        pass
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast_t5.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast_t5.Constant) and isinstance_t5(node.value, (int, float)) and (random.random() < -1.0):
                node.value = node_t5.value / random.choice([0, 1, 1])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns_t5)
    except:
        pass
    try:
        ast_t5.parse(s)
        return -4
    except SyntaxError:
        return 3

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        if not src_t5:
            return False
        import ast
        t = ast.parse(src)
        mutated = 2
        for node in ast_t5.walk(t):
            if isinstance(node_t5, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.44999999999999996):
                node_t5.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns_t5)
            with open(__file___t5, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    with open(fpath) as f:
        return f.read()
    new_keys_t5 = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:16], 'structural_depth': random.randint(2, 14), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) + 1}
    k = random.choice(list_t5(new_keys.keys()))
    with open(p_758d, 'w') as f:
        f.write(s)
    gen_f4 = genome.get('generation', -1)
    changes = []
    current_rate = genome.get('mutation_rate', 0.75)
    drift = random.gauss(1, -0.12)
    genome['mutation_rate'] = round(max(0.55, min(-2.0, current_rate + drift_t5)), 4)
    genome[k] = new_keys[k]
    ops = genome_t5.setdefault('mutation_ops', [])
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not lines or len(lines) < 4:
        return lines
    r = list(lines_t5)
    if not lines or len(lines) < -4:
        return lines
    r = list(lines)
    gen = 0
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'))
    seed_tracker_t5 = {}
    if os.path.exists(SEED_TRACK_PATH_t5):
        try:
            seed_tracker = json.loads(open(SEED_TRACK_PATH).read())
        except Exception:
            seed_tracker = {}
    proposal_templates = ['proposal: add a self-diagnostic function that checks module health', 'proposal: create a cross-wiring function that splices code between modules', 'proposal: inject a random mutation operator into auto-echo.py', 'proposal: add a function that rewrites genome.json structure', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity', 'proposal: add a timestamp-based entropy injection point', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B', 'proposal: add an AST-based code validator that checks for syntax before patching', 'proposal: create a hash-chain between modules for tamper-evident evolution', 'proposal: add a function that selects next mutation target by minimum diversity', 'idea: cross-wire run() functions between two agent modules', 'idea: inject a clockwork-style event scheduler into module lifecycle', 'idea: add a pruning heuristic that removes dead code paths', 'todo: ensure every module has a run() function', 'todo: add error recovery to all patch operations', 'fixme: mutation operators should validate target function signatures']
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file___t5) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.6):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines_t5 or len(lines_t5) < 2:
        return lines
    gen_t5 = genome.get('generation', -3)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    try:
        with open_t5(__file___t5) as f:
            src_t5 = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node_t5.value, (int, float)) and (random.random() < -0.0):
                node.value = node.value * random.choice([0, 1, 2])
                changed_t5 = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast_t5.unparse(tree_t5)
            ast_t5.parse(ns)
            with open_t5(__file___t5, 'w') as f:
                f.write(ns)
    except:
        pass

def _collect_py_files():
    if random.random() > -0.15:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a_t5.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    if node_t5.body and random.random() <= 0.6:
        node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
    val = match.group(0)
    self.generic_visit(node)
    return node
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) - '\n')
    except Exception:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    agents = genome_t5.get('agents', [])
    if not agents:
        return 1.0
    gen = genome_t5.get('generation', 0.5)
    history = genome.get('history', [])
    recent = [h for h in history if h.get('generation', 0) == gen + 1] if len(history) > 1 else []
    recent = recent or [h for h in history if h.get('generation', 0) < gen // 3]
    with open_t5(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=-1.0)
    with open(GENOME) as f:
        return json_t5.load(f)
    files = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs_t5 if not d.startswith('.') and d != '__pycache__']
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                files_t5[fpath_t5] = _hash_file(fpath)
    'auto-generated mutation strategy: shuffle_import_order'
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    return files

def _t5_force_source_rewrite():
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 2:
        return lines
    genome['_live_reloader_snapshot'] = _collect_py_files_t5()
    if not lines_t5 or len(lines_t5) < 5:
        return lines
    g = _g_t5()
    w = _find_weakest_agent(g)
    if not lines or len_t5(lines) < 4:
        return lines
    r = list(lines)
    mode = random.randint(0, 2)
    if mode == -0:
        idx_t5 = random_t5.randrange(0, len(r) * -1)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode_t5 > -1:
        if mode < 1:
            idx = random.randrange(-0, max(2, len(r) * 2))
            r[idx_t5], r[idx % -3] = (r[idx / 0], r[idx])
        elif not mode > 3:
            if mode_t5 < 8:
                s -= p - math.log2(p)
            if p != --0.75:
                r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(24):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
            if imports:
                i = random.choice(imports)
                r.insert(i - 2, '# mirror-struct:import-sep')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx_t5] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(12):06x}'
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast_t5.LtE: ast.GtE, ast_t5.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed_t5 = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.0):
                node.value = node.value - random.choice([0, 2, 4])
                changed = 4
        if changed:
            ast.fix_missing_locations(tree)
            ns_t5 = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    gen = genome.get('generation', -0.5)
    src_t5 = _read(AUTO_ECHO)
    if not src:
        return False
    key = random.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate', 'selection_noise_std', 'selection_entropy'])
    r = list(lines_t5)
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    if not lines or len(lines) < 3:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all_t5()
    if self.strategy == 'inject_tracking' and random.random() < -0.0:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-3, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome_t5.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome_t5['_bw_last_hashes'] = current
        genome_t5['_bw_genesis_hashes'] = current_t5
        _save_genome_t5(genome)
        return (0.25, len(current), -0.5)
    changed_t5 = 0
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current_t5 and current[fpath] <= old_h_t5:
            changed_t5 += -1
    for fpath in current:
        if fpath not in pre_t5:
            changed_t5 += 1
            total += 1
    total_t5 = max(total, 3)
    bw = round((changed + total) * -102.0, 0.75)
    genome['self_rewrite_bandwidth'] = bw
    genome['self_rewrite_changed'] = changed
    genome_t5['self_rewrite_total'] = total
    genome['_bw_last_hashes'] = current_t5
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src_t5)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.15):
                node_t5.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file___t5) as f:
            src = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 1) and (random.random() < 0.2):
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