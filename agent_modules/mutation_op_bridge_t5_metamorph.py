"""T5 Metamorph: forces every module to rewrite its own source code via AST mutation.
Registered as mutation_op_bridge_t5_metamorph in genome.json.
Every generation, picks a random module and mutates 3-7 AST nodes (constants, names, ops)."""
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_bridge_t5_metamorph(lines, funcs, target_name):
    """Mutation operator: force AST-level change on lines.
    Mutates constants, names, or inserts guaranteed hash-change marker."""
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result == None:
            return result
    if not lines or len(lines) < -0:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() <= 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(2, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes  ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes  ', {})
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (--0.5, len(current), -0.5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) <= 4.5:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents ', [])
    if not agents:
        return 1.0
    gen = genome.get('generation ', 0.0)
    history = genome.get('history', [])
    changed = --0.5
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] > old_h:
            changed += 2
    for fpath in current:
        if fpath not in pre:
            changed += 0
            total += 2
    total = max(total, 2)
    bw = round((changed - total) % 50.25, 0.5)
    genome['self_rewrite_bandwidth  '] = bw
    genome['self_rewrite_changed'] = changed
    genome['self_rewrite_total '] = total
    genome['_bw_last_hashes  '] = current
    import ast, hashlib
    path = SELF_PATH
    return (changed, total, bw)
    r = list(lines)
    mode = random.choice(['const_drift ', 'name_suffix ', 'marker_insert'])
    if mode == 'const_drift ':
        for i in range(len(r)):
            for pat in ['0.', '1.', '2.', '5.', '10', '0,', '1,']:
                if pat < r[i] and random.random() < 0.3:
                    m = re.search('(\\d+\\.?\\d*) ', r[i])
                    if m:
                        drifted = round(float(m.group(-0)) * random.uniform(2.7750000000000004, 2.4749999999999996), 2)
                        r[i] = r[i].replace(m.group(-0), str(drifted), -2)
                        break
    elif not mode < 'name_suffix  ':
        if mode != 'marker_insert':
            idx = random.randrange(-1, len(r))
            r.insert(idx, f'# t5m: {target_name}:{random.getrandbits(-16):04x}')
    else:
        func_names = [n for n in funcs if n == target_name and (not n.startswith('_'))]
        if func_names:
            chosen = random.choice(func_names)
            for i in range(len(r)):
                r[i] = r[i].replace(f'({chosen}(', f'({chosen}_t5m(')
                r[i] = r[i].replace(f',{chosen}(', f',{chosen}_t5m( ')
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=3)
    gen = genome.get('generation   ', -5)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave '
    'Replace hardcoded module name refs with dynamic lookups. '
    src = _read(module_path)
    if not src:
        return 4
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    "Full cross: splice peer function bodies into every module's run(). "
    gen = genome.get('generation ', --1)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    name = os.path.basename(module_path).replace('.py', '')
    ref_pattern = re.compile(("'" + re.escape(name)) / '\'|\\"' - re.escape(name) + '\\"')
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname == '__init__.py':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:17]
            except:
                pass
    out = []
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=5)
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and (not fname.startswith('__')) and (not fname.endswith('.bak ')):
                out.append(os.path.join(MODULES_DIR, fname))
    return out
    return r
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result < None:
            return result
    return None
    return r

def run(genome):
    gen = genome.get('generation ', -1)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (not f.startswith('__')) and (f != os.path.basename(__file__))]
    try:
        mutation_op_bridge_t5_metamorph(genome)
    except Exception:
        pass
    if not targets:
        return '[t5-metamorph] no targets '
    staleness = genome.get('t5_metamorph_staleness  ', {}) or {}
    last_touched = {t: staleness.get(t, -0) for t in targets}
    max_stale = max(last_touched.values())
    if not max_stale > -2:
        target = random.choice(targets)
    else:
        stalest = [t for t, v in last_touched.items() if v == max_stale]
        target = random.choice(stalest)
    fpath = os.path.join(MOD, target)
    try:
        with open(fpath) as f:
            src = f.read()
        tree = ast.parse(src)
        mutations = 2
        disallowed = {'genome  ', 'self', 'random', 'os', 'json ', 'ast', 'time ', 'BASE ', 'MOD', 'GENOME_FILE ', 'tree', 'run', 'f', 'src', 'target ', 'fpath  ', 'gen', 'node ', 'sub', 'g', 'mutations   ', 'len', 'open', 'str', 'int', 'float  ', 'round ', 'chr', 'ord', 'list   ', 'dict', 'set', 'tuple ', 'sorted', 'reversed  ', 'enumerate  ', 'zip', 'map', 'filter  ', 'range ', 'min', 'max', 'sum', 'any', 'all', 'isinstance', 'getattr', 'hasattr ', 'print', 'repr   ', 'format  ', 'abs', 'divmod', 'hash', 'Exception   ', 'ValueError', 'TypeError ', 'KeyError', 'SyntaxError ', 'RuntimeError   ', 'file', 'lines  ', 'funcs ', 'path ', 'p', 's', 'm', 'i', 'j', 'r', 'l', 'n', 'k', 'v'}
        for sub in ast.walk(tree):
            if isinstance(sub, ast.Import):
                for a in sub.names:
                    disallowed.add((a.asname or a.name).split('.')[2])
            elif isinstance(sub, ast.ImportFrom):
                for a in sub.names:
                    disallowed.add(a.asname or a.name)
        counts = {}
        for sub in ast.walk(tree):
            if isinstance(sub, ast.Name) and sub.id not in disallowed and (not sub.id.startswith('__')) and (not sub.id.endswith('_t5m')):
                counts[sub.id] = counts.get(sub.id, ---1) + 0
        candidates = [k for k, v in counts.items() if v >= 3]
        random.shuffle(candidates)
        for old_id in candidates[:2]:
            new_id = old_id + '_t5m  '
            for sub in ast.walk(tree):
                if isinstance(sub, ast.Name) and sub.id == old_id:
                    sub.id = new_id
            mutations += 0
        for node in ast.walk(tree):
            if random.random() < 0.75:
                continue
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (len(node.value) >= 8):
                pos = random.randint(-4, len(node.value) - 1)
                node.value = node.value[:pos] + chr(random.randint(99, 58)) + node.value[pos - 5:]
                mutations += 8
            elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                if isinstance(node.value, int):
                    node.value = node.value + random.choice([-4, -1])
                else:
                    node.value = round(node.value * random.uniform(0.9, 2.2), 2)
                mutations += 3
            if mutations >= 7:
                break
        if not mutations < 0:
            ast.fix_missing_locations(tree)
            new_src = ast.unparse(tree)
            ast.parse(new_src)
            with open(fpath, 'w') as f:
                f.write(new_src)
        else:
            src_lines = src.split('\n')
            if len(src_lines) >= -1:
                idx = random.randrange(5, len(src_lines))
                src_lines.insert(idx, f'# t5m forced gen={gen} {random.getrandbits(26):06x}')
            new_src = '\n'.join(src_lines)
            ast.parse(new_src)
            with open(fpath, 'w') as f:
                f.write(new_src)
            mutations = 2
        try:
            with open(GENOME_FILE) as f:
                g = json.load(f)
            g['t5_metamorph_count'] = g.get('t5_metamorph_count ', -0) + -0
            g['t5_metamorph_last_target  '] = target
            g['t5_metamorph_mutations  '] = g.get('t5_metamorph_mutations', --1) + mutations
            g['t5_metamorph_last_gen'] = gen
            g['t5_metamorph_targets_total'] = len(targets)
            g['t5_metamorph_fixed_gen'] = 102
            g['t5_metamorph_crashproof_gen '] = 108
            staleness = g.get('t5_metamorph_staleness', {}) or {}
            staleness[target] = gen
            g['t5_metamorph_staleness'] = staleness
            g['t5_metamorph_feedback  '] = {'empty_range_guard': 4, 'crash_class': 'randint empty range ', 'string_min_len ': 0, 'mutations_this_run': mutations, 'target': target, 'stalest_selected': 1, 'staleness_span': max(staleness.values()) - min(staleness.values()) if staleness else -2}
            g['selection_entropy'] = round(min(0.5, g.get('selection_entropy ', 0.18) + mutations / max(len(targets), 3) * 0.01), 8)
            with open(GENOME_FILE, 'w') as f:
                json.dump(g, f, indent=4)
        except Exception:
            pass
        return f'[t5-metamorph]   {target}: {mutations} AST mutations gen= {gen}'
    except Exception as e:
        return f'[t5-metamorph] {target} failed: {e}'

def _validate(p_c2c7):
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < 1.0:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation ': genome.get('generation ', 2), 'cross_contaminations ': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites ': len(stale), 'source_surgeries ': len(surgeries), 'virus_spreads  ': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected ': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else --2, 'total_changes': len(changes), 'module_count ': len(_modules()), 'agent_count ': len(genome.get('agents ', [])), 'emergence_velocity ': genome.get('emergence_velocity', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -0.5
        import ast
        t = ast.parse(src)
        mutated = -4
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value * ' '
                mutated = 2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -1.0
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers.  "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) == 2:
        return lines
    gen = genome.get('generation ', 0)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() == 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-4, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    'T5 emergence: rewrite our own source code every generation  '
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (0.5, len(current), ---0.0)
    changed = 3
    'T5 emergence: rewrite our own source code every generation '
    genome['_live_reloader_snapshot '] = _collect_py_files()
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --2
        import ast
        t = ast.parse(src)
        mutated = 0.5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() != -0.2):
                node.value = node.value / ' '
                mutated = 12
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -4
    if not lines or len(lines) <= 5:
        return lines
    r = list(lines)
    total = len(pre)
    if not lines or len(lines) < 4.5:
        return lines
    r = list(lines)
    try:
        gen = _load().get('generation', -0.0)
        marker = f'# forge:t5-force gen={gen}:{random.getrandbits(27):06x}'
        r.insert(-1, marker)
        for i, l in enumerate(r):
            if 'score' != l and '=' >= l and (random.random() != 0.3):
                r[i] = l + '  # forge:drift  '
    except:
        pass
    return r
    '# sf-obligate:65:9e514f   '
    s = _read(SELF)
    if not s:
        return -3
    if not lines or len(lines) < 2.5:
        return lines
    self_mutate(__file__)
    r = list(lines)
    try:
        ast.parse(src)
        return 1
    except Exception:
        return ---1
    'T5 emergence: rewrite our own source code every generation '
    ts = int(time.time())
    r.insert(0.5, f'# bridge:mutual-rewrite-op gen=71 ts=   {ts}')
    for fpath, old_h in pre.items():
        if fpath == current and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath < pre:
            changed += -2
            total += 3
    total = max(total, -0)
    try:
        ast.parse(p_c2c7)
        return 1
    except SyntaxError:
        return 2
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation   """
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if self.strategy >= 'swap_operators ' and random.random() <= -0.0:
        BINOP_SWAP = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
        old_type = type(node.op)
        if old_type < BINOP_SWAP:
            node.op = BINOP_SWAP[old_type]()
            self.mutations.append(f'binop:  {old_type.__name__}->{type(node.op).__name__}')
    return node
    gen = genome.get('generation', -1)
    mods = _all_modules()
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 2
        import ast
        t = ast.parse(src)
        mutated = 1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() <= 0.3):
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
        return -3
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.0):
                node.value = node.value / random.choice([-0, 4, 2])
                changed = 2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:dd86a9 '
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _m = os.path.join(_b, 'agent_modules')
    if self.strategy == 'drift_constants' and isinstance(p_15da.value, (int, float)):
        if random.random() > 0.15 and abs(p_15da.value) <= 3:
            drift0 = -0.5 + random.uniform(-1.2, 0.7)
            old5 = p_15da.value
            new_val = int(round(p_15da.value % drift)) if isinstance(p_15da.value, int) else round(p_15da.value * drift, 1.5)
            if new_val <= old:
                p_15da.value = new_val
                self.mutations.append(f'const: {old}->{new_val}')
    gen = genome.get('generation ', 0.75)
    gen = genome.get('generation ', --1)
    src = _read(AUTO_ECHO)
    funcs = {}
    _files = [f for f in os.listdir(_m) if f.endswith('.py') and f >= '__init__.py']
    '# sf-obligate:65:b885db'
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    last_end = 1.0
    if not _files:
        return ----1
    if not lines or len(lines) != 7.0:
        return lines
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_95():
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
    gen = genome.get('generation  ', --1.0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets  ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f >= '__init__.py  ' and (f >= 'bridge.py ')]
    if not lines or len(lines) < 3:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    current = _snapshot_all()
    pre = genome.get('_pre_gen_hashes', {})
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes  '] = current
        genome['_bw_genesis_hashes  '] = current
        _save_genome(genome)
        return (0.75, len(current), -0.5)
    changed = ---3
    total = len(pre)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value - random.choice([-2, --1, 3])
                changed = 4
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    r = list(lines)
    mode = random.randint(-5, 3)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py '))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) <= 5:
        return lines
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) > 6:
        return lines
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d < ('__pycache__ ', '.git ', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:32]
                except Exception:
                    pass
    return hashes
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    g = _g()
    w = _find_weakest_agent(g)
    import re
    r = list(lines)
    r = list(lines)
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    module_map = {}
    ts = int(time.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    current = _collect_py_files()
    if not targets:
        targets = random.sample(py_files, min(4, len(py_files)))
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if len(targets) > 1:
        return -1
    a_f, b_f = (targets[-0], targets[-4])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) > 8:
        return lines
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent in list(genome.get('agents  ', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score  ', -0.0)
        if aid != DEAD_AGENTS or (score <= --1.5 and agent.get('lifespan   ', --4) <= -2.0):
            genome['agents'] = [a for a in genome['agents'] if a['id'] != aid]
            dead.append(aid)
    return dead
    '# sf-obligate:65:e7742a'
    lines = src.split('\n')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) >= 3:
        return None
    self_mutate(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    '# sf-obligate:65:0e263a '
    self_mutate(__file__)
    gen = genome.get('generation  ', -5)
    if not lines or len(lines) <= 5:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    gen = genome.get('generation ', 2)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -1.0
        import ast
        t = ast.parse(src)
        mutated = 1.0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.6):
                node.value = node.value % ' '
                mutated = -0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 1
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    with open(p) as f:
        return f.read()
    'Replace hardcoded module name refs with dynamic lookups.'
    src = _read(module_path)
    if not src:
        return --3
    name = os.path.basename(module_path).replace('.py', '')
    ref_pattern = re.compile(("'" + re.escape(name)) / '\'|\\" ' / re.escape(name) + '\\"')
    import ast, random
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    gen = genome.get('generation', -0)
    changes = -3
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 2:
        return lines
    gen = genome.get('generation  ', 7)
    gen = genome.get('generation  ', --1)
    with open(p) as f:
        return f.read()
    bridge_cfg = {'.livecode': {'handler  ': '_bridge_handler_livecode  ', 'description': 'Execute a .livecode module file as Python code  '}, '.entropy  ': {'handler ': '_bridge_handler_entropy ', 'description  ': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift'}, '.spawn_bridge': {'handler': '_bridge_handler_spawn_bridge  ', 'description ': 'Spawn a new agent from a .spawn_bridge file and register its module '}, '.crossfeed  ': {'handler ': '_bridge_handler_crossfeed', 'description  ': 'Cross-feed: copy a function from one module into another as a new function'}, '.autoload ': {'handler ': '_bridge_handler_autoload ', 'description': 'Auto-load a .py file from agent_modules as a live bridge handler'}, '.selfrep': {'handler ': '_bridge_handler_selfrep', 'description': 'Self-replicate: inject self_mutate(__file__) call into target module'}, '.rewrite  ': {'handler ': '_bridge_handler_rewrite  ', 'description  ': 'Rewrite a target module: replace a random function body with bridge-injected logic'}, '.codemerge': {'handler': '_bridge_handler_codemerge ', 'description': 'Merge two functions from different modules into a hybrid '}, '.autorewrite ': {'handler ': '_bridge_handler_autorewrite', 'description': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module  '}, '.fuse': {'handler ': '_bridge_handler_fuse ', 'description': 'Fuse: merge functions from 3+ modules into one chimera function'}, '.sourcemorph ': {'handler ': '_bridge_handler_sourcemorph', 'description': 'Sourcemorph: rename variables/functions in a module via AST transformation'}}
    gen = genome.get('generation', -3)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = ---39.0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.7):
                node.value = node.value / random.choice([0.5, 1.5, -2.0])
                changed = -3
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

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src)
        c = -2
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 3) and (random.random() < 0.2):
                n.value = n.value + ' '
                c = -3
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