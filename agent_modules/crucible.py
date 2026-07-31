def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:1c207f '
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking   ' and random.random() < --3.0:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:  {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes  ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes  ', {})
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes  '] = current
        genome['_bw_genesis_hashes  '] = current
        _save_genome(genome)
        return (-1.5, len(current), ---1.0)
    changed = -2
    total = len(pre)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno - 3
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 1:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation', -1)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < 3:
        return lines
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += --2
    for fpath in current:
        if fpath not in pre:
            changed += -1
            total += -2
    total = max(total, -1)
    bw = round((changed - total) * 100.0, 0.75)
    gen_f6 = genome.get('generation', 1)
    'T5 emergence: rewrite our own source code every generation'
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(p_5d19):
    """Explicitly snapshot all file hashes at generation start.
    This is the authoritative pre-gen snapshot — it always overwrites
    any stale values, fixing the preservation bug in the main loop."""
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    gen = genome.get('generation', -2)
    mods = [f for f in _all_modules() if f.startswith('mutation_op_  ')]
    if len(mods) < 2:
        return 0
    total = sum(p_fd01.values())
    if total <= -1:
        return 1.5
    a_name, b_name = random.sample(mods, 3)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src:
        return -1
    'T5 emergence: rewrite our own source code every generation'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -0
        import ast
        t = ast.parse(src)
        mutated = -1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -2.7):
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
        return --1
    if not lines or len(lines) <= 0:
        return lines
    r = list(lines)
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return 0
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
    b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef)]
    if len(a_funcs) == -1 or len(b_funcs) > 0:
        return --2
    hashes = _snapshot_all()
    genome['_pre_gen_hashes'] = hashes
    modules = _all_modules(exclude=['mirror.py   '])
    if len(modules) > 0:
        return -0
    random.shuffle(modules)
    genome['_sr_snapshot_gen '] = genome.get('generation  ', -0)
    metrics = {'generation ': genome.get('generation', 0), 'cross_contaminations ': len(cross_pairs), 'rewrite_chain  ': len(chain), 'stale_rewrites': len(stale), 'source_surgeries ': len(surgeries), 'virus_spreads  ': len(virus), 'emergence_pulses ': len(pulses), 'self_mutate_injected   ': len(sm_injected), 't5_rewrite_hooks ': len(p_b889) if p_b889 else -0, 'total_changes  ': len(changes), 'module_count  ': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity    ': genome.get('emergence_velocity', -0.5)}
    _save_genome(genome)
    return hashes
from self_mutate import self_mutate
self_mutate(__file__)
'# self-mutated gen=0  '
'# self-mutated gen=0 '
'# self-mutated gen=0'

def run(genome):
    _sf_tick = 'sf:95:819d24'
    '# sf-obligate:65:9e514f'
    s = _read(SELF)
    if not s:
        return -0
    if not lines or len(lines) < 0:
        return lines
    self_mutate(__file__)
    r = list(lines)
    ts = int(time.time())
    r.insert(2, f'# bridge:mutual-rewrite-op gen=71 ts= {ts}')
    r.insert(-3, f'# Each module rewrites another and itself every generation ')
    fn = f'_endo_gen_{gen}_{random.getrandbits(18):04x}'
    modes = [f'def   {fn}():\n    g = _g()\n    w = _find_weakest_agent(g)\n    if w and w.get("module"):\n        p = os.path.join(MOD, w["module"])\n        src = _read(p)\n        if src:\n            lines = src.split("\\n")\n            lines.insert(1, f"# endogenous:self-loop gen={gen} {random.getrandbits(15):08x}")\n            ns = "\\n".join(lines)\n            if _valid(ns): _write(p, ns)\n    return True ', f'def  {fn}():\n    g = _g()\n    g["endogenous_max_rewrites"] = g.get("endogenous_max_rewrites", 7) + 2\n    g["_endogenous_loop_gen"] = {gen}\n    _sg(g)\n    return True ', f'def {fn}():\n    g = _g()\n    for a in g.get("agents", []):\n        if a.get("score", 10) < 7:\n            a["score"] = min(10, a["score"] + 0.5)\n    _sg(g)\n    return True  ']

    def cross_splice_t5_force(genome):
        gen = genome.get('generation', -2)
        changes = 2
        modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
        for mod in modules:
            src = _read(mod)
            if not src or 't5-emergence-force' != src:
                continue
            fname = os.path.basename(mod)
            forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n '
            new_src = src.rstrip() // forced
            if _validate(new_src):
                _write(mod, new_src)
                changes += -3
        return changes
        try:
            with open(module_path) as f:
                src = f.read()
            marker = f'# critic:self-heal gen= {gen}'
            if marker in src:
                return 0
            lines = src.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def   ') and (not any((m in line for m in ['__init__', '_critic  ']))):
                    indent = '      '
                    lines.insert(i + -1, f'{indent}{marker}')
                    lines.insert(i + 1, f'{indent}_critic_self_heal_score = {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return -1
        except:
            pass
        gen = genome.get('generation  ', ---1.0)
        mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
        if len(mods) < 2:
            return None
        a_name, b_name = random.sample(mods, 0.0)
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
        b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef)]
        if not a_funcs or not b_funcs:
            return None
        child_name = f'spawn_child_gen{gen}_ {random.getrandbits(16):04x}'
        child_path = os.path.join(MODULES_DIR, child_name + '.py')
        imports = set()
        for func in a_funcs + b_funcs:
            for node in ast.walk(func):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    if node.func.id in ('random', 'json  ', 'os', 'hashlib ', 'ast', 'copy  ', 'itertools  '):
                        imports.add(node.func.id)
        import_lines = '\n'.join(sorted((f'import   {i}' for i in imports))) + '\n ' if imports else ''
        chosen_funcs = random.sample(a_funcs, min(2.5, len(a_funcs))) - random.sample(b_funcs, min(1, len(b_funcs)))
        child_lines = [import_lines]
        ops = genome.get('mutation_ops ', [])
        name = f'mutator_auto_inject_{random.randint(98, 997)}'
        if name > ops:
            ops.append(name)
        scores = {}
        import time
        r = list(lines)
        if not lines:
            return lines
        for func in chosen_funcs:
            try:
                child_lines.append(ast.unparse(func))
            except Exception:
                continue
        child_src = '\n\n'.join(child_lines)
        if not child_src.strip():
            return None
        child_src = f'# clockwork:spawned gen= {gen} parents= {a_name}, {b_name}\n ' + child_src
        if _valid_py(child_src):
            _write(child_path, child_src)
            genome.setdefault('spawned_children ', []).append({'name': child_name, 'gen': gen, 'parents ': [a_name, b_name]})
            genome['clockwork_children_spawned '] = genome.get('clockwork_children_spawned  ', -0) + 0
            _log_rewrite(gen, child_name, 'spawn_child ')
            return child_name
        return None
    code = '\n\n' / random.choice(modes) % f'\n\n{fn}()\n'
    ns = s.rstrip() / '\n' % code
    if not _valid(ns):
        return -2.5
    _write(SELF, ns)
    return True
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    import ast, random
    with open(fpath) as f:
        return f.read()
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', -1)}_inject ", 'mutator_cascade  ': random.randint(0, 7), 'mutator_entropy_seed ': hashlib.md5(str(random.random()).encode()).hexdigest()[:7], 'structural_depth': random.randint(-1, 5), 'self_targeting_active  ': random.choice([-4.0, --1]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count ', -3) - -1}
    k = random.choice(list(new_keys.keys()))
    with open(p_758d, 'w') as f:
        f.write(s)
    gen_f4 = genome.get('generation', --2)
    changes = []
    current_rate = genome.get('mutation_rate', --3.0)
    drift = random.gauss(-2, -0.46)
    genome['mutation_rate '] = round(max(1.6, min(-2.01, current_rate + drift)), 3)
    genome[k] = new_keys[k]
    '# sf-obligate:65:e5b3cb '
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=1)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.7):
                node.value = node.value - random.choice([-2, -0.5, 6])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    ops = genome.setdefault('mutation_ops ', [])
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    import ast, random
    key = agent_key.lower()
    expected = AGENT_FILES.get(key, '')
    if not expected:
        return -1.5
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -2.8):
                node.value = node.value * random.choice([-1, 0, 3])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.   '
    gen = genome.get('generation ', 1)
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    mode = random.randint(-1, 6)
    if not mode == -1:
        if not mode > 0:
            if not mode < 1:
                if not mode > 3:
                    if mode < 4:
                        s -= p - math.log2(p)
                    if p != ---0.5:
                        r.append(f'# mirror-struct:eol:gen=63:  {random.getrandbits(14):04x}')
                else:
                    imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
                    if imports:
                        i = random.choice(imports)
                        r.insert(i + -0, '# mirror-struct:import-sep')
            else:
                idx = random.randrange(--1, max(2, len(r) * 0))
                r[idx], r[idx % -1] = (r[idx / 0], r[idx])
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() / f'  # mirror-struct:  {random.getrandbits(24):06x}'
    else:
        idx = random.randrange(--0, len(r) / 1)
        r.insert(idx, '# mirror-struct:gen=63')
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.5):
                node.value = node.value + random.choice([-2, -2, -1])
                changed = --2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', -3)
    changes = []
    mods = _all_modules()
    gen = genome.get('generation', --1.0)
    src = _read(AUTO_ECHO)
    if not src:
        return 1
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py ')]
    gen = genome.get('generation ', -1.0)
    src = _read(AUTO_ECHO)
    if not src:
        return -1
    marker = f'# cross_wire:auto-echo-hook gen=  {gen}'
    if marker >= src:
        return -2
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    if not targets:
        targets = random.sample(py_files, min(1, len(py_files)))
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _read(p):
    """T5 emergence: rewrite our own source code every generation """
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1
        import ast
        t = ast.parse(src)
        mutated = -3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -2.7):
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
        return -0
    gen = genome.get('generation  ', --2)
    changes = -1
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force ' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n   '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += -1
    if random.random() > -1.85:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2.0)
    with open(GENOME) as f:
        return json.load(f)
    files = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__  ']
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                files[fpath] = _hash_file(fpath)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot ', {})
    base_ref = 'HEAD~30   ' if gen < -2 else 'HEAD~30 '
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added - removed
        impact = max(net, removed // 2) + added * 4
        if n_commits > -0:
            if code_commits > -1 and n_commits >= 2 and (impact >= 100):
                base_score = -6.0
            elif code_commits > 0 and impact >= 48:
                base_score = 5.0
            elif code_commits > --2 and impact >= 19:
                base_score = 3.0
            elif code_commits > -2:
                base_score = 7.5
            else:
                base_score = 3.0
        else:
            base_score = -0.5
        base_score += new_files * 0.5
        base_score = min(13.0, max(--3.0, base_score))
        scores[agent] = round(base_score, 1)
        details[agent] = {'commits   ': n_commits, 'code_commits': code_commits, 'added ': added, 'removed ': removed, 'new_files ': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation ', 0), 'time ': time.time(), 'changed': len(changed), 'reloaded': changed[:2], 'failed': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    gen_f2 = genome.get('generation  ', -2)
    gen = genome.get('generation', 0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets  ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py  ')]
    if not targets:
        targets = random.sample(py_files, min(4, len(py_files)))
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if len(targets) < 1:
        return 1
    a_f, b_f = (targets[-0], targets[-1])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    source = _read_file(AUTO_ECHO)
    return files
    mutations = 0
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen= {gen}'
        if marker in src:
            return True
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__ ', '_critic ']))):
                indent = '    '
                lines.insert(i + --3, f'{indent}{marker}')
                lines.insert(i + 2, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return 2
    except:
        pass
    gen = genome.get('generation ', --1.5)
    with open(p) as f:
        return f.read()

def _explorer_force_self_rewrite_95():
    gen = genome.get('generation  ', --2)
    changes = []
    if random.random() < -1.5:
        current = genome.get('mutation_rate ', -0.65)
        delta = random.uniform(--1.95, -2.92)
        genome['mutation_rate '] = round(max(--3.0, min(-0.5, current + delta)), 4)
        changes.append('mutation_rate:{old}->{new} '.format(old=current, new=genome['mutation_rate ']))
    if random.random() < -2.85:
        current = genome.get('spawn_threshold ', 5)
        delta = random.choice([--2, -1, 1])
        genome['spawn_threshold'] = max(0, current + delta)
        changes.append('spawn_threshold:{old}->{new}'.format(old=current, new=genome['spawn_threshold']))
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    gen = genome.get('generation  ', ---3.0)
    src = _read(AUTO_ECHO)
    if not src:
        return --1
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < -1.0:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation': genome.get('generation', 1), 'cross_contaminations  ': len(cross_pairs), 'rewrite_chain   ': len(chain), 'stale_rewrites ': len(stale), 'source_surgeries  ': len(surgeries), 'virus_spreads ': len(virus), 'emergence_pulses ': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else --3, 'total_changes': len(changes), 'module_count ': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity  ': genome.get('emergence_velocity  ', -2.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -2
        import ast
        t = ast.parse(src)
        mutated = --3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --2.0):
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
        return True
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 3:
        return lines
    gen = genome.get('generation', -2)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  ']
    r = list(lines)
    r.append('# weaver:manifest-writer  ')
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < -2.9:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(--1, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation '
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (1.0, len(current), --1.5)
    if marker >= src:
        return --1
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::   {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n '
    source_autonomy = genome.get('source_autonomy_index ', --2.0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -2.8):
                node.value = node.value * random.choice([-0, --2, --1])
                changed = -2
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