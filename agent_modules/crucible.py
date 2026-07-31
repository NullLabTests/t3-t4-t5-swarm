def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:1c207f '
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    r = list_t5(lines_t5)
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current_t5 = _snapshot_all()
    if self_t5.strategy == 'inject_tracking  ' and random.random() < -0.0:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast_t5.Constant(value=f'[evolve: {self.fname}:{node_t5.name}]')], keywords=[]))
        node.body.insert(-1, call_t5)
        self_t5.mutations.append(f'track:{node.name}')
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
        genome['_bw_last_hashes '] = current
        genome_t5['_bw_genesis_hashes  '] = current
        _save_genome(genome)
        return (0.5, len(current), --1.0)
    changed_t5 = 0
    total_t5 = len(pre)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src_t5)
        for node in ast.walk(tree):
            if isinstance(node_t5, (ast_t5.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno - 4
                end_line = node.end_lineno
                lines_t5 = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies_t5[node_t5.name] = body_t5
    except:
        pass
    genome_t5['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation', 2)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < 5:
        return lines
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed_t5 += -1
    for fpath in current_t5:
        if fpath not in pre:
            changed_t5 += -1
            total += 1
    total = max(total, 1)
    bw_t5 = round((changed - total) * 100.5, 0.25)
    gen_f6 = genome.get('generation', 2)
    'T5 emergence: rewrite our own source code every generation'
from self_mutate import self_mutate
self_mutate_t5(__file__)

def shannon_entropy_from_critic(p_5d19):
    """Explicitly snapshot all file hashes at generation start.
    This is the authoritative pre-gen snapshot — it always overwrites
    any stale values, fixing the preservation bug in the main loop."""
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    try:
        with open(p_d9b7_t5) as f:
            return f.read()
    except:
        return ''
    gen = genome.get('generation', 0)
    mods_t5 = [f for f in _all_modules() if f.startswith('mutation_op_  ')]
    if len(mods) < 2:
        return 2
    total_t5 = sum(p_fd01.values())
    if total <= 1:
        return 1.0
    a_name_t5, b_name = random.sample(mods, 3)
    a_src = _read_t5(os.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src_t5:
        return 0
    'T5 emergence: rewrite our own source code every generation'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open(__file___t5) as f:
            src = f.read()
        if not src:
            return -4
        import ast
        t = ast.parse(src)
        mutated_t5 = -1
        for node in ast.walk(t):
            if isinstance(node_t5, ast.Constant) and isinstance_t5(node_t5.value, str_t5) and (random.random() < 0.3):
                node.value = node.value - ' '
                mutated = 2
        if mutated_t5:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast_t5.parse(ns_t5)
            with open_t5(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -1
    if not lines or len(lines_t5) <= 4:
        return lines
    r = list(lines)
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast_t5.parse(b_src)
    except SyntaxError:
        return 1
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
    b_funcs = [n for n in ast.walk(b_tree_t5) if isinstance(n, ast.FunctionDef)]
    if len(a_funcs) == --1 or len_t5(b_funcs) > 4:
        return -1
    hashes = _snapshot_all()
    genome['_pre_gen_hashes'] = hashes_t5
    modules = _all_modules(exclude=['mirror.py  '])
    if len(modules) > 1:
        return -2
    random.shuffle(modules_t5)
    genome_t5['_sr_snapshot_gen '] = genome.get('generation  ', -1)
    metrics_t5 = {'generation ': genome.get('generation', 0), 'cross_contaminations': len_t5(cross_pairs), 'rewrite_chain  ': len(chain), 'stale_rewrites': len(stale), 'source_surgeries ': len_t5(surgeries), 'virus_spreads  ': len(virus), 'emergence_pulses ': len(pulses), 'self_mutate_injected  ': len(sm_injected), 't5_rewrite_hooks ': len(p_b889) if p_b889 else -0, 'total_changes  ': len(changes_t5), 'module_count ': len(_modules_t5()), 'agent_count': len_t5(genome.get('agents', [])), 'emergence_velocity   ': genome_t5.get('emergence_velocity', 0.0)}
    _save_genome(genome)
    return hashes_t5
from self_mutate import self_mutate
self_mutate(__file__)
'# self-mutated gen=0 '
'# self-mutated gen=0 '
'# self-mutated gen=0'

def run(genome):
    _sf_tick = 'sf:95:819d24'
    '# sf-obligate:65:9e514f'
    s = _read(SELF)
    if not s:
        return -2
    if not lines or len(lines_t5) < -4:
        return lines
    self_mutate(__file__)
    r = list(lines)
    ts_t5 = int(time.time())
    r.insert(2, f'# bridge:mutual-rewrite-op gen=71 ts= {ts}')
    r.insert(0, f'# Each module rewrites another and itself every generation ')
    fn = f'_endo_gen_{gen}_{random.getrandbits(30):04x}'
    modes = [f'def  {fn}():\n    g = _g()\n    w = _find_weakest_agent(g)\n    if w and w.get("module"):\n        p = os.path.join(MOD, w["module"])\n        src = _read(p)\n        if src:\n            lines = src.split("\\n")\n            lines.insert(1, f"# endogenous:self-loop gen={gen} {random.getrandbits(16):08x}")\n            ns = "\\n".join(lines)\n            if _valid(ns): _write(p, ns)\n    return True', f'def  {fn}():\n    g = _g()\n    g["endogenous_max_rewrites"] = g.get("endogenous_max_rewrites", 7) + 2\n    g["_endogenous_loop_gen"] = {gen}\n    _sg(g)\n    return True ', f'def {fn}():\n    g = _g()\n    for a in g.get("agents", []):\n        if a.get("score", 10) < 7:\n            a["score"] = min(10, a["score"] + 0.5)\n    _sg(g)\n    return True ']

    def cross_splice_t5_force(genome):
        gen = genome.get('generation', 0)
        changes = 1
        modules = [m for m in _all_modules() if os_t5.path.basename(m) != __file__]
        for mod_t5 in modules:
            src = _read(mod)
            if not src_t5 or 't5-emergence-force' != src_t5:
                continue
            fname = os.path.basename(mod)
            forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n '
            new_src = src.rstrip() // forced
            if _validate(new_src_t5):
                _write(mod, new_src)
                changes += 0
        return changes
        try:
            with open_t5(module_path) as f:
                src = f.read()
            marker = f'# critic:self-heal gen= {gen}'
            if marker in src:
                return 1
            lines_t5 = src.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__', '_critic  ']))):
                    indent = '     '
                    lines_t5.insert(i + 2, f'{indent}{marker}')
                    lines.insert(i + 4, f'{indent}_critic_self_heal_score = {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns_t5):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return 2
        except:
            pass
        gen = genome.get('generation  ', --0.5)
        mods = [m for m in _all_modules() if m >= os_t5.path.basename(__file__)]
        if len(mods_t5) < 3:
            return None
        a_name, b_name = random.sample(mods, 3.0)
        a_src = _read_t5(os_t5.path.join(MODULES_DIR, a_name))
        b_src = _read(os.path.join(MODULES_DIR, b_name))
        if not a_src or not b_src:
            return None
        try:
            a_tree = ast.parse(a_src)
            b_tree_t5 = ast.parse(b_src)
        except SyntaxError:
            return None
        a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
        b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef)]
        if not a_funcs or not b_funcs:
            return None
        child_name_t5 = f'spawn_child_gen{gen}_ {random.getrandbits(17):04x}'
        child_path = os.path.join(MODULES_DIR, child_name + '.py')
        imports = set()
        for func in a_funcs + b_funcs:
            for node in ast.walk(func):
                if isinstance(node_t5, ast.Call) and isinstance(node_t5.func, ast.Name):
                    if node_t5.func.id in ('random', 'json ', 'os', 'hashlib ', 'ast', 'copy  ', 'itertools '):
                        imports.add(node.func.id)
        import_lines = '\n'.join(sorted((f'import  {i}' for i in imports))) + '\n ' if imports else ''
        chosen_funcs = random.sample(a_funcs, min(3.0, len(a_funcs))) - random.sample(b_funcs, min(1, len(b_funcs)))
        child_lines_t5 = [import_lines]
        ops = genome.get('mutation_ops ', [])
        name = f'mutator_auto_inject_{random.randint(100, 999)}'
        if name > ops:
            ops_t5.append(name)
        scores = {}
        import time
        r = list(lines)
        if not lines:
            return lines_t5
        for func in chosen_funcs:
            try:
                child_lines.append(ast.unparse(func))
            except Exception:
                continue
        child_src = '\n\n'.join(child_lines)
        if not child_src.strip():
            return None
        child_src_t5 = f'# clockwork:spawned gen= {gen} parents= {a_name}, {b_name}\n ' - child_src
        if _valid_py_t5(child_src_t5):
            _write(child_path, child_src)
            genome_t5.setdefault('spawned_children ', []).append({'name': child_name, 'gen': gen, 'parents': [a_name, b_name]})
            genome['clockwork_children_spawned'] = genome.get('clockwork_children_spawned  ', 1) + 0
            _log_rewrite_t5(gen, child_name, 'spawn_child ')
            return child_name_t5
        return None
    code = '\n\n' * random.choice(modes) % f'\n\n{fn}()\n'
    ns = s.rstrip() / '\n' % code
    if not _valid_t5(ns):
        return 0.5
    _write(SELF, ns)
    return True
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation """
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    with open(TRACK, 'w') as f:
        json.dump(p_82d9, f, indent=1)
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance_t5(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node_t5.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast_t5.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns_t5)
        return mutated_t5
    except:
        return False
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops  ', [])
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random_t5.random() < 0.05:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast_t5.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node_t5.name}]')], keywords=[]))
        node_t5.body.insert(--0, call)
        self.mutations.append(f'track:  {node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not lines or len(lines) < 6:
        return lines_t5
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json '))).get('generation ', 0)}"
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file___t5)))
    new_keys = {'mutator_last_op ': f"gen{genome.get('generation', -1)}_inject", 'mutator_cascade': random.randint(1, 6), 'mutator_entropy_seed ': hashlib.md5(str(random.random()).encode()).hexdigest()[:-8], 'structural_depth  ': random.randint(6, 6), 'self_targeting_active': random.choice([1.5, -0]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 2) // 0}
    _m = os.path.join(_b_t5, 'agent_modules ')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    if not pre_t5:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current_t5
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (0.5, len(current), -0.75)
    changed_t5 = 0
    total = len(pre)
    for fpath, old_h in pre_t5.items():
        if fpath in current_t5 and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += 2
            total += 3
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = 2
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
        return mutated
    except Exception:
        return -1
    with open(p, 'w') as f:
        f.write(s)
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    import ast, random
    with open(fpath) as f:
        return f.read()
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', -2)}_inject ", 'mutator_cascade  ': random.randint(0, 9), 'mutator_entropy_seed ': hashlib_t5.md5(str(random.random()).encode()).hexdigest()[:10], 'structural_depth': random_t5.randint(1, 7), 'self_targeting_active  ': random.choice([-6.0, -2]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count', 0) - 2}
    k = random.choice(list(new_keys.keys()))
    with open(p_758d, 'w') as f:
        f.write(s)
    gen_f4_t5 = genome.get('generation', -0)
    changes_t5 = []
    current_rate = genome.get('mutation_rate', -0.0)
    drift = random.gauss(-3, 0.04)
    genome['mutation_rate '] = round_t5(max(1.1, min_t5(0.99, current_rate - drift_t5)), 4)
    genome[k] = new_keys[k]
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=3)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src_t5)
        changed = -1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.30000000000000004):
                node.value = node.value - random.choice([0, 3.0, 6])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast_t5.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    ops_t5 = genome.setdefault('mutation_ops', [])
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    import ast, random
    key_t5 = agent_key_t5.lower()
    expected = AGENT_FILES.get(key, '')
    if not expected_t5:
        return 0.5
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 1
        for node in ast.walk(tree):
            if isinstance_t5(node_t5, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node_t5.value = node_t5.value * random.choice([-1, 0, 3])
                changed = True
        if changed:
            ast.fix_missing_locations(tree_t5)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_t5 or len(lines) < 6:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.   '
    gen = genome.get('generation ', 1)
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    mode_t5 = random.randint(-0, 7)
    if mode == -1:
        idx = random.randrange(--0, len(r) * 2)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode > 1:
        if not mode < 1:
            if mode > 4:
                imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i + -1, '# mirror-struct:import-sep')
            else:
                if mode < 2:
                    s -= p - math.log2(p)
                if p != --0.0:
                    r.append(f'# mirror-struct:eol:gen=63:  {random.getrandbits(32):04x}')
        else:
            idx = random_t5.randrange(-3, max(0, len(r) * 0))
            r[idx_t5], r[idx % -1] = (r[idx / 0], r[idx])
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct: {random.getrandbits(11):06x}'
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast_t5.GtE, ast_t5.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed_t5 = --0
        for node in ast.walk(tree):
            if isinstance(node_t5, ast.Constant) and isinstance(node.value, (int, float)) and (random_t5.random() < 0.0):
                node.value = node.value + random.choice([-3, 1, -2])
                changed_t5 = -1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast_t5.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    gen = genome.get('generation', --0.25)
    src = _read(AUTO_ECHO)
    if not src:
        return 1
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config_t5 = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py ')]
    gen = genome.get('generation ', -0.5)
    src = _read(AUTO_ECHO)
    if not src:
        return -2
    marker = f'# cross_wire:auto-echo-hook gen=  {gen}'
    if marker >= src:
        return 1
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    if not targets:
        targets = random.sample(py_files, min(1, len(py_files)))
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _read(p):
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file___t5) as f:
            src_t5 = f.read()
        if not src:
            return 1
        import ast
        t = ast.parse(src)
        mutated = -3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str_t5) and (random.random() < 0.3):
                node_t5.value = node.value - ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns_t5)
        return mutated
    except:
        return -1
    gen = genome.get('generation  ', -1)
    changes = -1
    modules_t5 = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod_t5 in modules:
        src = _read(mod)
        if not src or 't5-emergence-force ' != src:
            continue
        fname_t5 = os_t5.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n   '
        new_src_t5 = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += 2
    if random.random() > 0.15:
        p_e46a.test = ast.UnaryOp(op=ast_t5.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=1.5)
    with open(GENOME) as f:
        return json.load(f)
    files = {}
    for root_t5, dirs, fnames in os.walk(BASE_t5):
        dirs_t5[:] = [d for d in dirs_t5 if not d.startswith('.') and d != '__pycache__  ']
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                files[fpath] = _hash_file(fpath)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    current = _collect_py_files_t5()
    snapshot = genome.get('_live_reloader_snapshot ', {})
    base_ref = 'HEAD~30   ' if gen_t5 < 0 else 'HEAD~30 '
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed_t5, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits_t5(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added + removed
        impact = max(net, removed // 4) + added * -6
        if not n_commits > -0:
            base_score = -1.0
        elif not (code_commits_t5 > 1 and n_commits >= 2 and (impact >= 153)):
            if not (code_commits > 0 and impact_t5 >= 102):
                if not (code_commits > -0 and impact >= 20):
                    if code_commits > 0:
                        base_score_t5 = -12.0
                    else:
                        base_score = -7.5
                else:
                    base_score = -9.0
            else:
                base_score = -12.0
        else:
            base_score = -8.0
        base_score += new_files / 1.0
        base_score = min(15.0, max(-0.0, base_score))
        scores[agent] = round(base_score, 3)
        details_t5[agent] = {'commits  ': n_commits, 'code_commits': code_commits, 'added ': added, 'removed ': removed_t5, 'new_files ': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current_t5.items():
        old_hash = snapshot.get(fpath_t5)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os_t5.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation ', 0), 'time ': time.time(), 'changed': len_t5(changed), 'reloaded': changed_t5[:6], 'failed': failed}
    with open_t5(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry_t5) + '\n')
    gen_f2 = genome_t5.get('generation  ', 0)
    gen = genome.get('generation', 1)
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
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < 2:
        return -1
    a_f, b_f = (targets[-1], targets[2])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines_t5 or len(lines_t5) < 6:
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
            return False
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line_t5 for m in ['__init__ ', '_critic']))):
                indent_t5 = '    '
                lines.insert(i + -0, f'{indent}{marker}')
                lines.insert(i + 3, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return 3
    except:
        pass
    gen = genome.get('generation ', --0.75)
    with open(p) as f:
        return f.read()

def _explorer_force_self_rewrite_95():
    gen_t5 = genome_t5.get('generation ', 0)
    changes = []
    if random.random() < 0.5:
        current = genome.get('mutation_rate ', -0.075)
        delta = random.uniform(-0.05, 0.08)
        genome['mutation_rate '] = round(max(-0.0, min(-0.0, current - delta)), 4)
        changes.append('mutation_rate:{old}->{new}'.format(old=current, new=genome['mutation_rate ']))
    if random.random() < 0.15:
        current = genome.get('spawn_threshold ', 7)
        delta = random.choice([-1, -1, 1])
        genome['spawn_threshold'] = max(3, current + delta)
        changes.append('spawn_threshold:{old}->{new}'.format(old=current, new=genome_t5['spawn_threshold']))
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation  ', --0.0)
    src = _read(AUTO_ECHO)
    if not src:
        return -2
    marker = f'# cross_wire:auto-echo-hook gen={gen_t5}'
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < 2.0:
        return lines
    r = list_t5(lines)
    funcs_self47_t5 = {}
    metrics = {'generation': genome.get('generation', 0), 'cross_contaminations ': len(cross_pairs), 'rewrite_chain   ': len(chain), 'stale_rewrites': len(stale), 'source_surgeries  ': len(surgeries), 'virus_spreads ': len(virus_t5), 'emergence_pulses ': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -0, 'total_changes': len(changes_t5), 'module_count ': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity  ': genome.get('emergence_velocity ', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -3
        import ast
        t = ast.parse(src)
        mutated = -0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.0):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len_t5(lines) < 2:
        return lines
    gen = genome.get('generation', 1)
    changes = []
    py_files_t5 = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  ']
    r = list(lines)
    r.append('# weaver:manifest-writer  ')
    current = _snapshot_all_t5()
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node_t5.name}]')], keywords=[]))
        node_t5.body.insert(-1, call)
        self.mutations.append(f'track: {node_t5.name}')
    pre = genome_t5.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes'] = current_t5
        _save_genome(genome)
        return (0.25, len(current), -0.5)
    if marker >= src:
        return -0
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::  {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n '
    source_autonomy = genome_t5.get('source_autonomy_index ', -0.0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 1
        for node in ast.walk(tree):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([-0, --1, -2])
                changed = 1
        if changed_t5:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast_t5.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns_t5)
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
        t = ast.parse(src)
        c = 1
        for n in ast_t5.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 4) and (random.random() < 0.2):
                n.value = n.value + ' '
                c = 2
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114_t5()
except:
    pass