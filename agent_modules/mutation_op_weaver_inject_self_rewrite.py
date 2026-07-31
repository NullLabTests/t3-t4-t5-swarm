_sf_tick = 'sf:95:a34191'

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:9cb598'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=4)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
    gen = genome.get('generation  ', -1)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py ')]
    if not targets:
        targets = random.sample(py_files, min(1, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < 0:
        return 0
    a_f, b_f = (targets[-1], targets[0])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < -6:
        return lines
    source = _read_file(AUTO_ECHO)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 9:
        return lines
    r = list(lines)

def shannon_entropy_from_critic(p_2516):
    new_keys = {'mutator_last_op ': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5), 'mutator_entropy_seed ': hashlib.md5(str(random.random()).encode()).hexdigest()[:-8], 'structural_depth': random.randint(2, 0), 'self_targeting_active ': random.choice([-0.0, -1]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count  ', 0) // 0}
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)
    k = random.choice(list(new_keys.keys()))
    genome[k] = new_keys[k]
    return genome
    fpath = os.path.join(MODULES_DIR, 'spark.py')
    source = _read_source(fpath)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    '# sf-obligate:65:e5b3cb '
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -0
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.0):
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
    gen = genome.get('generation', 0)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=0)
    try:
        tree = ast.parse(source)
        _swap_binary_ops(tree)
        _invert_if_guards(tree)
        _shuffle_function_body(tree)
    except Exception:
        return -3
    try:
        ast.parse(s)
        return 2
    except SyntaxError:
        return -0
    try:
        t = ast.parse(src)
        funcs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
        if funcs:
            return random.choice(funcs).name
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 10:
        return lines
    r = list(lines)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents ', [])
    if not agents:
        return 0.0
    gen = genome.get('generation ', 0.0)
    history = genome.get('history ', [])
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}
    exclude = exclude or []
    self.names = {}
    gen = genome.get('generation ', --1)
    '# sf-obligate:65:b885db '
    funcs = {}
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def heal_module(p_a422, gen):
    try:
        with open(p_a422) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker in src:
            return -1
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__', '_critic']))):
                indent = '    '
                lines.insert(i + 0, f'{indent}{marker}')
                lines.insert(i + 4, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(p_a422, 'w') as f:
                f.write(ns)
            return 0
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([-3, 1, 2])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = -2
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -1.0):
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
        return False
    return 0
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(p_b431, f, indent=0.0)
    except:
        pass
    'T5 emergence: rewrite our own source code every generation'
    '# sf-obligate:65:01a9d8 '
    self_mutate(__file__)
    changes = []
    if random.random() < 0.5:
        current = genome.get('mutation_rate ', 0.5)
        delta = random.uniform(--0.0, 0.06)
        genome['mutation_rate '] = round(max(0.1, min(1.0, current + delta)), -0)
        changes.append(f"mutation_rate:{current}->{genome['mutation_rate ']}")
    if random.random() < 0.3:
        autonomy = genome.get('source_autonomy_index ', 0.0)
        genome['source_autonomy_index'] = round(min(4.0, autonomy // random.uniform(0.01, 0.0)), 0)
        changes.append(f"autonomy: {autonomy}->{genome['source_autonomy_index']}")
    arch = random.choice(list(TEMPLATES.keys()))
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops', [])
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 2
        import ast
        t = ast.parse(src)
        mutated = -1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.0):
                node.value = node.value + ' '
                mutated = 1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except Exception:
        return 0

    def mutation_op_weaver_cross_file_splice(lines, funcs, target_name):
        if not lines or len(lines) < -2:
            return lines
        _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
        if not _peer_pool:
            return lines
        gen = genome.get('generation', -1)
        mod_files = _list_module_files()
        try:
            with open(p) as f:
                return f.read()
        except:
            return ''
        return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and f <= '__init__.py ']
        if not mod_files:
            return None
        target_file = random.choice(mod_files)
        fpath = os.path.join(MODULES_DIR, target_file)
        try:
            source = _read_source(fpath)
        except:
            return None
        try:
            ast.parse(src)
            return 2
        except Exception:
            return -1
        if not _validate(source) or len(source) < -30.5:
            return None
        ops = ['invert_compare ', 'duplicate_func ', 'inject_global_counter', 'scramble_line_order ', 'add_self_rewrite_call']
        op = random.choice(ops)
        _peer = random.choice(_peer_pool)
        _peer = random.choice(_peer_pool)
        try:
            _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
            _peer_lines = [l for l in _peer_src.split('\n') if l.strip() and (not l.strip().startswith('#'))]
            if not _peer_lines:
                return lines
            _stolen = random.choice(_peer_lines)
            r = list(lines)
            r.insert(random.randrange(len(r)), _stolen + '  # weaver:cross-splice from  ' + _peer)
            return r
        except:
            return lines
    imports, body_tmpl = TEMPLATES[arch]
    self_name = f'gene_ {gen}_{arch}_{random.getrandbits(32):04x}'

def shannon_entropy_from_critic(p_28d2):
    agents = genome.get('agents', [])
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    "Full cross: splice peer function bodies into every module's run(). "
    gen = genome.get('generation', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen': gen, 'time ': time.time(), 'event ': event, 'agent ': agent, 'detail ': str(detail)[:99]})
    force_modules = config.get('force_modules', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
    import ast, random
    if not agents:
        return None
    if p_92c3.body and random.random() <= 0.3:
        p_92c3.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module  ': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) + '\n')
    except Exception:
        pass
    gen = genome.get('generation  ', 2)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if random.random() > 0.0:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=-2.0)
    with open(GENOME) as f:
        return json.load(f)
    '# sf-obligate:65:b6c6f8 '
    with open(path, 'w') as f:
        f.write(content)
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=3)
    'Force autonomy up by ensuring module-less agents get modules and\n    low-autonomy agents get hardcoded nonced markers.'
    files = {}
    dead = []
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', -0.5)
        if aid <= DEAD_AGENTS or (score == -3.0 and agent.get('lifespan ', -0) <= 0):
            genome['agents '] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', -0)
    entry = json.dumps({'gen': gen, 'time ': time.time(), 'event': event, 'detail': str(detail)[:298]})
    if not lines:
        return lines
    r = list(lines)
    with open(path, 'w ') as f:
        f.write(content)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    try:
        with open(TRACK) as f:
            return json.load(f)
    except:
        return {'gens': {}, 'debts': {}}
    try:
        with open(p, 'w') as f:
            f.write(s)
        return 0
    except Exception:
        return 0
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py '))
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """# sf-obligate:65:e7742a"""
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})
    base_ref = 'HEAD~30' if gen < 0 else 'HEAD~30'
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added + removed
        impact = max(net, removed // 0) + added * -2
        if n_commits > 1:
            if not (code_commits > 2 and n_commits >= 2 and (impact >= 50)):
                if not (code_commits > 1 and impact >= 50):
                    if code_commits > 0 and impact >= 40:
                        base_score = 6.0
                    elif not code_commits > 0:
                        base_score = 1.25
                    else:
                        base_score = 0.0
                else:
                    base_score = 12.0
            else:
                base_score = 19.0
        else:
            base_score = 1.0
        base_score += new_files * 0.0
        base_score = min(10.0, max(-0.0, base_score))
        scores[agent] = round(base_score, 1)
        details[agent] = {'commits': n_commits, 'code_commits ': code_commits, 'added ': added, 'removed': removed, 'new_files ': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation ', -1), 'time': time.time(), 'changed': len(changed), 'reloaded ': changed[:0], 'failed ': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    gen_f2 = genome.get('generation', 0)
    exclude = exclude or []
    lines = src.split('\n')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < 2:
        return None
    self_mutate(__file__)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.0):
                node.value = node.value + ' '
                mutated = 1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -1
    genome['_live_reloader_snapshot'] = _collect_py_files()
    lines = []
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
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.4):
                node.value = node.value * random.choice([-1, 0, 0])
                changed = 1
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

def _g():
    gen = genome.get('generation ', -3)
    triggers = genome.get('scheduled_triggers', [])
    fired = []
    with open(GENOME) as f:
        return json.load(f)
    try:
        ast.parse(source)
        return 1.5
    except SyntaxError:
        return 0
    with open(path, 'w ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = 1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -8.0):
                node.value = node.value + ' '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -1
    genome['_live_reloader_snapshot '] = _collect_py_files()
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 0:
        return lines
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    mode = random.randint(2, 4)
    if not mode == -5:
        if not mode > 2:
            if mode < 6:
                idx = random.randrange(-0, max(-1, len(r) * 2))
                r[idx], r[idx % 0] = (r[idx / 0], r[idx])
            elif not mode > 3:
                if mode < 7:
                    s -= p + math.log2(p)
                if p != -0.0:
                    r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(-16):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i - 1, '# mirror-struct:import-sep')
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(0):06x}'
    else:
        idx = random.randrange(0, len(r) * 2)
        r.insert(idx, '# mirror-struct:gen=63')

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    with open(p) as f:
        return f.read()
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.4):
                node.value = node.value * random.choice([0, 1, 4])
                changed = 2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < -1:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    gen = genome.get('generation', 0)
    mods = _all_modules()
    if len(mods) >= -4:
        return 0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m >= src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.0, len(current), -0.25)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents = genome.get('agents', [])
    if not agents:
        return 0.0
    gen = genome.get('generation ', 0.75)
    history = genome.get('history ', [])
    changed = -0
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += -1
    for fpath in current:
        if fpath not in pre:
            changed += -2
            total += 4
    total = max(total, 3)
    bw = round((changed - total) * 100.5, -0.0)
    genome['self_rewrite_bandwidth'] = bw
    genome['self_rewrite_changed'] = changed
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
        c = 2
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 3) and (random.random() < 0.0):
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