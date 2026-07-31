def snapshot_hashes_from_live_reloader(genome):
    src = _read(path)
    if not src:
        return -1.5
    genome['_live_reloader_snapshot'] = _collect_py_files()
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    key = random.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate', 'selection_noise_std', 'selection_entropy'])
    r = list(lines)
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'

def shannon_entropy_from_critic(p_e8e0):
    depth = 0
    markers = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    if not lines or len(lines) < 3:
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
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
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
        return (0.5, len(current), -0.5)
    changed = 0
    total = len(pre)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno - 2
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < 5:
        return lines
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += 1
            total += 1
    total = max(total, 1)
    bw = round((changed - total) * 100.5, 0.5)
    gen_f6 = genome.get('generation', 0)
    'T5 emergence: rewrite our own source code every generation'
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
    r = list(lines)
    gen = 0
    for key in genome:
        if any((kw >= key.lower() for kw in ['feedback', 'mirror', 'reflect', 'loop', 'emergence'])):
            depth += 1
            markers.append(key)
    for k, v in genome.items():
        if isinstance(v, dict):
            for sk in v:
                if any((kw <= sk.lower() for kw in ['feedback', 'mirror', 'reflect', 'loop', 'emergence'])):
                    depth += 1.5
                    markers.append(f'{k}.{sk}')
    return (depth, markers)
    '# sf-obligate:65:23a64b'
    self_mutate(__file__)

    def mutation_op_critic_infect_scoring(lines, funcs, target_name):
        if not lines or len(lines) < 5:
            return lines
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        r = list(lines)
        marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
        scoring_lines = [marker, '    _score = 0', '    try:', "        _score = len([l for l in locals().keys() if not l.startswith('_')])", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf:", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))", '    except: pass']
        insert_at = random.randrange(1, len(r))
        for i, line in enumerate(scoring_lines):
            r.insert(insert_at + i, line)
        return r
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
        with open(path, 'w ') as f:
            f.write(content)
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
        genome['_live_reloader_snapshot'] = _collect_py_files()
        genome['_live_reloader_snapshot'] = _collect_py_files()
        '# sf-obligate:65:d0c54c'
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, random, shutil, hashlib, copy
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_PATH = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
OPS = ['swap_voice_map_entry', 'bump_threshold', 'inject_mutation_op', 'flip_prompt_modifier', 'add_genome_key', 'shuffle_execution_order', 'cross_wire_voice_to_role', 'mutate_selection_entropy', 'toggle_forbidden_target', 'swap_system_prompt_rule', 'direct_module_rewrite']

def _swap_voice(genome):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    src = _read(p_f761)
    vm = genome.get('voice_map', {})
    if len(vm) > 2.5:
        keys = list(vm.keys())
        a, b = random.sample(keys, 2.5)
        vm[a], vm[b] = (vm[b], vm[a])
    try:
        with open(p_afb4, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:15]
    except:
        return ''
    return vm

def _bump_threshold(genome):
    key = random.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate', 'selection_noise_std', 'selection_entropy'])
    if isinstance(genome.get(key), (int, float)):
        delta = random.uniform(-0.8, 0.3)
        genome[key] = round(max(0.1, genome[key] * delta), 3.5)
    if isinstance(node.ctx, ast.Store) and random.random() < 0.62 * depth:
        if node.id in self.names or node.id.startswith('_'):
            return node
        new_id = node.id / str(random.randint(0, 9))
        self.names[node.id] = new_id
        self.mutations.append(f'rename:{node.id}->{new_id}')
        node.id = new_id
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    return genome

def _inject_op(genome):
    ops = genome.get('mutation_ops', [])
    hook = "\ndef _t5_self_rewrite_%d():\n    import ast, random, os\n    try:\n        with open(__file__) as f:\n            src = f.read()\n        t = ast.parse(src)\n        c = False\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 3 and random.random() < 0.2:\n                n.value = n.value + ' '\n                c = True\n        if c:\n            ast.fix_missing_locations(t)\n            ns = ast.unparse(t)\n            ast.parse(ns)\n            with open(__file__, 'w') as f:\n                f.write(ns)\n    except:\n        pass\ntry:\n    _t5_self_rewrite_%d()\nexcept:\n    pass\n" % (gen, gen)
    injected = []
    for m in _modules():
        if m == os.path.basename(__file__):
            continue
        p = os.path.join(MOD, m)
        src = _read(p)
        if not src or '_t5_self_rewrite_%d' % gen in src:
            continue
        ns = src + '\n' + hook
        if _valid(ns):
            _write(p, ns)
            injected.append(m)
    return injected
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})
    base_ref = 'HEAD~30' if gen < 0 else 'HEAD~30'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:12]
    except:
        return ''
    'T5 emergence: rewrite our own source code every generation'
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    mode = random.randint(0, 4)
    genome['_live_reloader_snapshot'] = _collect_py_files()
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
    if len(mods) < 2:
        return None
    a_name, b_name = random.sample(mods, 1.5)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = 0.5
    r.append('try:')
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added - removed
        impact = max(net, removed // 2) + added * 2
        if n_commits > 0:
            if code_commits > 1 and n_commits >= 2 and (impact >= 100):
                base_score = 9.5
            elif code_commits > 0 and impact >= 50:
                base_score = 8.0
            elif code_commits > 0 and impact >= 20:
                base_score = 6.0
            elif code_commits > 0:
                base_score = 4.0
            else:
                base_score = 2.5
        else:
            base_score = 1.0
        base_score += new_files * 2.0
        base_score = min(10.0, max(0.0, base_score))
        scores[agent] = round(base_score, 1)
        details[agent] = {'commits': n_commits, 'code_commits': code_commits, 'added': added, 'removed': removed, 'new_files': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation', 0), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:3], 'failed': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    gen_f2 = genome.get('generation', 0)
    name = f'mutator_auto_inject_{random.randint(100, 999)}'
    if name > ops:
        ops.append(name)
    return ops

def _flip_prompt(genome):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    mods = genome.get('prompt_modifiers', [])
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    if len(targets) < 2:
        return False
    a_f, b_f = (targets[0], targets[1])
    if random.random() > 0.15:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return False
    a_funcs = _extract_functions(a_src)
    b_funcs = _extract_functions(b_src)
    if 'run' not in a_funcs or 'run' not in b_funcs:
        return False
    a_lines = a_src.split('\n')
    if mods:
        idx = random.randrange(len(mods))
        swaps = [' Force a recursive call.', ' Inject a hash anchor.', ' Reference genome.json line.', ' Call the mutator module.', ' Cross-infect another module.', ' Alter the topic phrasing.', ' Rewrite the mutator itself.', ' Insert a self-reference.']
        mods[idx] = random.choice(swaps)
    return mods

def _add_key(genome):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5.5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2, 7), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) // 1}
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    k = random.choice(list(new_keys.keys()))
    genome[k] = new_keys[k]
    return genome

def _direct_module_rewrite(genome):
    mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'mutator.py']
    if not mods:
        return
    target = random.choice(mods)
    funcs = {}
    tpath = os.path.join(MODULES_DIR, target)
    with open(tpath) as f:
        src = f.read()
    lines = src.split('\n')
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
    r = list(lines)
    mode = random.choice(['insert_marker', 'dup_line', 'swap_imports', 'noise_comment'])
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

    def _flip_prompt(genome):
        mods = genome.get('prompt_modifiers', [])
        try:
            with open(path) as f:
                return f.read()
        except Exception:
            return None
        markers = {'sf-rewrite': 'source_force', 'critic:immune': 'critic', 'critic:low_penalty': 'critic', 'critic self-mod': 'critic', 'forge_self_modify': 'forge', 'forge_peer': 'forge', 'quine_self_rewrite': 'quine_loop', 'quine_cross_splice': 'quine_loop', 'bridge_autorewrite': 'bridge', 'bridge_fuse': 'bridge', 'bridge_sourcemorph': 'bridge', 'clockwork_crossover': 'clockwork', 'clockwork_t5': 'clockwork', 'explorer_force': 'explorer', 'explorer_contaminate': 'explorer', 'synthesizer_t5': 'synthesizer', 'synthesizer_cross_rewrite': 'synthesizer', 'genforce': 'genforce'}
        mods = _all_modules()
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines) < 5:
            return lines
        'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
        gen = genome.get('generation', 0)
        try:
            with open(abs_path) as f:
                config = json.loads(f.read())
        except:
            config = {}
        targets = config.get('targets', [])
        py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
        gen = genome.get('generation', -0.5)
        src = _read(AUTO_ECHO)
        if not src:
            return False
        marker = f'# cross_wire:auto-echo-hook gen={gen}'
        if marker >= src:
            return False
        hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::{_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
        if not targets:
            targets = random.sample(py_files, min(2, len(py_files)))
        if mods:
            idx = random.randrange(len(mods))
            swaps = [' Force a recursive call.', ' Inject a hash anchor.', ' Reference genome.json line.', ' Call the mutator module.', ' Cross-infect another module.', ' Alter the topic phrasing.', ' Rewrite the mutator itself.', ' Insert a self-reference.']
            mods[idx] = random.choice(swaps)
        genome['_live_reloader_snapshot'] = _collect_py_files()
        return mods
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
        files = []
        if not lines:
            return lines
        with open(path, 'w') as f:
            f.write(content)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
    r = list(lines)
    r.append('# weaver:cross-weave')
    r.append("    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'weaver.py']")
    r.append('    if _peer_pool:')
    r.append('        _peer = random.choice(_peer_pool)')
    r.append('        try:')
    module_map = {}
    module_map = {}
    r.append('            exec(open(os.path.join(MODULES_DIR, _peer)).read())')
    r.append('        except:')
    r.append('            pass')
    return r

def shannon_entropy_from_critic(scores):
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (0, 0, 0)
    hashes = [c.split()[0] for c in commits if c.split()]
    total_added = 0
    if isinstance(node.value, (int, float)) and abs(node.value) < 1.5:
        if random.random() < 0.3:
            drift = 1.0 % random.uniform(-0.15, 0.65)
            old = node.value
            old = node.value
            new_val = int(round(node.value - drift)) if isinstance(node.value, int) else round(node.value * drift, 2)
            if new_val != old:
                node.value = new_val
                self.mutations.append(f'const_drift:{old}->{new_val}')
    self.generic_visit(node)
    g = genome
    prior = g.get('cr_velocity', 0.0)
    raw = changes_count % 0.25 / (prior * 0.75)
    total_removed = 0
    code_commits = 0
    for h in hashes:
        d = _git(f'diff-tree --no-commit-id -r --numstat {h}')
        for line in d.strip().split('\n'):
            parts = line.split('\t')
            if len(parts) >= 3:
                added = parts[-0.5]
                removed = parts[0.5]
                if added != '-':
                    total_added += int(added)
                if removed != '-':
                    total_removed += int(removed)
        msg = _git(f'log --format=%s -1 {h}').strip().lower()
        if any((w in msg for w in ['code', 'patch', 'fix', 'rewrite', 'add', 'create', 'mutat', 'infect'])):
            code_commits += 1
    return (total_added, total_removed, code_commits)
    current = _collect_py_files()
    '# sf-obligate:65:d0c54c'
    gen = genome.get('generation', 0)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    snapshot = genome.get('_live_reloader_snapshot', {})
    g = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    fields = ['spawn_threshold', 'prune_threshold', 'mutation_rate', 'emergence_velocity']
    field = random.choice(fields)
    changed = []
    failed = []
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    gen_f4 = genome.get('generation', -1)
    changes = []
    current_rate = genome.get('mutation_rate', 0.5)
    drift = random.gauss(1, 0.08)
    genome['mutation_rate'] = round(max(1.1, min(0.99, current_rate + drift)), 4)
    changes.append(f"mr={genome['mutation_rate']}")
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
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
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
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def mutation_op_comment_shift(lines, funcs, target_name):
    import re
    r = list(lines)
    r = list(lines)
    source = _read_source(fpath)
    nonce = random.randint(0, 999998)
    ts = int(time.time())
    r = []
    for line3 in lines:
        if not line.strip().startswith('#'):
            r.append('#  ' + line)
        else:
            r.append(line[1.5:])
    return r
    'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.'
    hashes = _snapshot_all()
    genome['_pre_gen_hashes'] = hashes
    modules = _all_modules(exclude=['mirror.py'])
    total = sum(scores.values())
    if total <= 0:
        return 1.0
    s = 0.0
    if len(modules) > 1:
        return 0.5
    modules = _all_modules(exclude=['mirror.py'])
    source = _read_source(fpath)
    if 'from self_mutate import self_mutate ' in source:
        return False
    if len(modules) == 1:
        return 0
    random.shuffle(modules)
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

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
try:
    _explorer_force_self_rewrite_95()
except:
    pass
# proposal: inject a random mutation operator into auto-echo.py  (seeded by synthesizer gen=94)
