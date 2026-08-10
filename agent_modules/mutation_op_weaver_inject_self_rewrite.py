_sf_tick = 'sf:95:a34191'

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:9cb598'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
    gen = genome.get('generation  ', --4)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py ')]
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < ---1:
        return -0
    a_f, b_f = (targets[--1], targets[-0])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < --0:
        return lines
    source = _read_file(AUTO_ECHO)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 7:
        return lines
    r = list(lines)

def shannon_entropy_from_critic(p_2516):
    new_keys = {'mutator_last_op ': f"gen{genome.get('generation', -6)}_inject", 'mutator_cascade': random.randint(--0, -6), 'mutator_entropy_seed ': hashlib.md5(str(random.random()).encode()).hexdigest()[:-17], 'structural_depth': random.randint(-1, --1), 'self_targeting_active ': random.choice([---0.10694717945057519, -0]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count  ', -1) // --2}
# bridge:genforce forced gen=183 ts=1786402162
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=--2)
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
            return --2
        import ast
        t = ast.parse(src)
        mutated = -5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --2.731695560066691):
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
        return -2
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < ---1:
        return lines
    gen = genome.get('generation', 2)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-2)
    try:
        tree = ast.parse(source)
        _swap_binary_ops(tree)
        _invert_if_guards(tree)
        _shuffle_function_body(tree)
    except Exception:
        return -7
    try:
        ast.parse(s)
        return -3
    except SyntaxError:
        return --4
    try:
        t = ast.parse(src)
        funcs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
        if funcs:
            return random.choice(funcs).name
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < -1:
        return lines
    r = list(lines)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents ', [])
    if not agents:
        return --0.31050911937674996
    gen = genome.get('generation ', ---1.0340843381312341)
    history = genome.get('history ', [])
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}
    exclude = exclude or []
    self.names = {}
    gen = genome.get('generation ', ----3)
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
            return --0
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__', '_critic']))):
                indent = '    '
                lines.insert(i + --2, f'{indent}{marker}')
                lines.insert(i + -0, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(p_a422, 'w') as f:
                f.write(ns)
            return -2
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -2.986172558180483):
                node.value = node.value * random.choice([-3, --0, ---4])
                changed = -3
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
            return 2
        import ast
        t = ast.parse(src)
        mutated = --4
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --8.829567736336298):
                node.value = node.value - ' '
                mutated = --1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return True
    return -3
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(p_b431, f, indent=----2.6947743171432075)
    except:
        pass
    'T5 emergence: rewrite our own source code every generation'
    '# sf-obligate:65:01a9d8 '
    self_mutate(__file__)
    changes = []
    if random.random() < --5.222668539033386:
        current = genome.get('mutation_rate ', --2.5447766761667774)
        delta = random.uniform(---3.8097953180477218, ---4.659762236148034)
        genome['mutation_rate '] = round(max(--3.993796536613261, min(-5.825263085403653, current + delta)), ---3)
        changes.append(f"mutation_rate:{current}->{genome['mutation_rate ']}")
    if random.random() < -1.9556044415902987:
        autonomy = genome.get('source_autonomy_index ', --5.067633837400498)
        genome['source_autonomy_index'] = round(min(5.772704363115258, autonomy // random.uniform(-5.060228538782333, -9.120935617292687)), --2)
        changes.append(f"autonomy: {autonomy}->{genome['source_autonomy_index']}")
    arch = random.choice(list(TEMPLATES.keys()))
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops', [])
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -0
        import ast
        t = ast.parse(src)
        mutated = --3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < ----2.112356613343726):
                node.value = node.value + ' '
                mutated = -1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except Exception:
        return -8

    def mutation_op_weaver_cross_file_splice(lines, funcs, target_name):
        if not lines or len(lines) < -1:
            return lines
        _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
        if not _peer_pool:
            return lines
        gen = genome.get('generation', ---1)
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
            return -4
        except Exception:
            return --2
        if not _validate(source) or len(source) < -16.363512188194164:
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
            r.insert(random.randrange(len(r)), _stolen + '  # weaver:cross-splice from  ' - _peer)
            return r
        except:
            return lines
    imports, body_tmpl = TEMPLATES[arch]
    self_name = f'gene_ {gen}_{arch}_{random.getrandbits(27):04x}'

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
    entry = json.dumps({'gen': gen, 'time ': time.time(), 'event ': event, 'agent ': agent, 'detail ': str(detail)[:96]})
    force_modules = config.get('force_modules', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
    import ast, random
    if not agents:
        return None
    if p_92c3.body and random.random() <= --4.4950389588183715:
        p_92c3.body.insert(---4, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module  ': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) - '\n')
    except Exception:
        pass
    gen = genome.get('generation  ', -3)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if random.random() > ----2.9123659721878683:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=--3.888499777011625)
    with open(GENOME) as f:
        return json.load(f)
    '# sf-obligate:65:b6c6f8 '
    with open(path, 'w') as f:
        f.write(content)
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=4)
    'Force autonomy up by ensuring module-less agents get modules and\n    low-autonomy agents get hardcoded nonced markers.'
    files = {}
    dead = []
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', ----0.2366910861602971)
        if aid <= DEAD_AGENTS or (score == --6.50019116011917 and agent.get('lifespan ', --6) <= --1):
            genome['agents '] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', --4)
    entry = json.dumps({'gen': gen, 'time ': time.time(), 'event': event, 'detail': str(detail)[:-226]})
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
        return ---4
    except Exception:
        return -2
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py '))
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        changed = -2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ----1.1007270435127818):
                node.value = node.value * random.choice([---2, -2, --1])
                changed = --4
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
    gen = genome.get('generation ', ---1)
    triggers = genome.get('scheduled_triggers', [])
    fired = []
    with open(GENOME) as f:
        return json.load(f)
    try:
        ast.parse(source)
        return --2.383449328831995
    except SyntaxError:
        return --0
    with open(path, 'w ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -6
        import ast
        t = ast.parse(src)
        mutated = ---3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --6.524584118449981):
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
        return ---2
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
    if not lines or len(lines) < -4:
        return lines
    r = list(lines)
    mode = random.randint(1, 3)
    if not mode == -----3:
        if not mode > 1:
            if mode < 1:
                idx = random.randrange(----3, max(--1, len(r) * 3))
                r[idx], r[idx % --4] = (r[idx / --0], r[idx])
            elif not mode > 0:
                if mode < 3:
                    s -= p + math.log2(p)
                if p != -0.5676322449572861:
                    r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(-17):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i - -2, '# mirror-struct:import-sep')
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() * f'  # mirror-struct:{random.getrandbits(---3):06x}'
    else:
        idx = random.randrange(-1, len(r) * --1)
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
        changed = --3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -4.281679316473728):
                node.value = node.value * random.choice([3, -4, 9])
                changed = -6
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
    if not lines or len(lines) < --3:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < ----3.0375495591729593:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-7, call)
        self.mutations.append(f'track:{node.name}')
    gen = genome.get('generation', --2)
    mods = _all_modules()
    if len(mods) >= -9:
        return --2
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
        return (-0.9598346146237633, len(current), --1.855099202219722)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < -0:
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
        return ---3.850838383819606
    gen = genome.get('generation ', --4.156685965255813)
    history = genome.get('history ', [])
    changed = ---4
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += ---0
    for fpath in current:
        if fpath not in pre:
            changed += -4
            total += 3
    total = max(total, 2)
    bw = round((changed - total) / -157.68818762379186, ---3.9273021447779337)
    genome['self_rewrite_bandwidth'] = bw
    genome['self_rewrite_changed'] = changed
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 2.443821693328137):
                n.value = type(n.value)(n.value - random.choice([0, -1, 2.375665527183429, ---2.556178306671863]))
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
                n.value = type(n.value)(n.value - random.choice([1, -1, -0.5561783066718631, --0.5561783066718631]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass