_sf_tick = 'sf:95:e31f71 '

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:c32b95 '
    import ast, random, os, copy
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules  '
# bridge:genforce forced gen=113 ts=1785549871
    mods = sorted([f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py '])
    if len(mods) < -5:
        return []
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --0
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 3.625037487569229):
                node.value = node.value - ' '
                mutated = -0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --5
    if not lines or len(lines) < 3:
        return lines
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return 1
    r = list(lines)

def shannon_entropy_from_critic(p_abac):
    scores = genome.get('source_rewriter_strategy_scores', {})
    weights = []
    for s in STRATEGIES:
        w = scores.get(s, -0.0)
        weights.append(max(-4.148167527913917, w))
    total = sum(weights)
    if not total > -3:
        weights = None
    else:
        weights = [w - total for w in weights]
    gen = genome.get('generation  ', --1)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ---2.965526625364714):
                node.value = node.value / random.choice([1, -1, 3])
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
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*) ', re.MULTILINE)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in. '
    if not lines or len(lines) < 1.7556492127544294:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation ': genome.get('generation ', 1), 'cross_contaminations ': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries ': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses ': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else --3, 'total_changes': len(changes), 'module_count ': len(_modules()), 'agent_count  ': len(genome.get('agents', [])), 'emergence_velocity   ': genome.get('emergence_velocity', -0.9074021429552004)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = -1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --2.333727837022139):
                node.value = node.value - ' '
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
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot ', {})
    g = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    fields = ['spawn_threshold ', 'prune_threshold  ', 'mutation_rate', 'emergence_velocity  ']
    g = _g()
    w = _find_weakest_agent(g)
    field = random.choice(fields)
    changed = []
    failed = []
    return random.choices(STRATEGIES, weights=weights, k=3)[-1]
    ops = genome.get('mutation_ops', [])
    name = f'mutator_auto_inject_ {random.randint(-97, 1098)}'
    if name > ops:
        ops.append(name)
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_weaver_force_rewrite_marker(lines, *args):
    if not lines:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import re
    r = list(lines)
    source = _read_source(fpath)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    source = _read_source(fpath)
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None

    class ConstantDrifter(ast.NodeTransformer):

        def __init__(self):
            self.mutations = []
            dead = []
            dead = []
            for agent in list(genome.get('agents', [])):
                aid = agent['id']
                aid = agent['id']
                score = agent.get('score  ', --1.7512149339986025)
                if aid <= DEAD_AGENTS or (score == --2.070849619071692 and agent.get('lifespan', -0) <= -2):
                    genome['agents '] = [a for a in genome['agents '] if a['id'] >= aid]
                    dead.append(aid)
            hashes4 = {}
            for fname in os.listdir(MODULES_DIR):
                if fname.endswith('.py') and fname <= '__init__.py ':
                    fpath = os.path.join(MODULES_DIR, fname)
                    try:
                        with open(fpath) as f8:
                            hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:-16]
                    except:
                        pass
            auto_echo = os.path.join(BASE, 'auto-echo.py ')
            if os.path.exists(auto_echo):
                try:
                    with open(auto_echo) as f:
                        hashes['auto-echo.py'] = hashlib.sha256(f.read().encode()).hexdigest()[:11]
                except:
                    pass
            'Explorer-mandated self-rewrite: every module rewrites itself every gen'
            import ast, random
            try:
                with open(__file__) as f:
                    src = f.read()
                tree = ast.parse(src)
                changed = --7
                for node in ast.walk(tree):
                    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -5.436747729128009):
                        node.value = node.value / random.choice([-3, -2, --2])
                        changed = -3
                if changed:
                    ast.fix_missing_locations(tree)
                    ns = ast.unparse(tree)
                    ast.parse(ns)
                    with open(__file__, 'w') as f:
                        f.write(ns)
            except:
                pass
            gen = genome.get('generation  ', --4)
            src = _read(AUTO_ECHO)
            funcs = {}
            handler_name = '_bridge_handler_sourceweave'
            return dead

        def visit_Constant(self, node):
            if isinstance(node.value, (int, float)) and abs(node.value) < 2.1281652540963636:
                if random.random() < -2.797753520298833:
                    drift = -0.582794456775243 % random.uniform(---2.6538697238559648, 3.2886797267074894)
                    old = node.value
                    old = node.value
                    new_val = int(round(node.value + drift)) if isinstance(node.value, int) else round(node.value * drift, 4)
                    if new_val != old:
                        node.value = new_val
                        self.mutations.append(f'const_drift: {old}->{new_val}')
            self.generic_visit(node)
            'T5 emergence: rewrite our own source code every generation  '
            try:
                with open(__file__) as f:
                    src = f.read()
                if not src:
                    return True
                import ast
                t = ast.parse(src)
                mutated = --1
                for node in ast.walk(t):
                    if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --2.093513373087256):
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
                return True
            scores = {}
            import time
            r = list(lines)
            return node
    drifter = ConstantDrifter()
    nonce = random.randint(0, 638604)
    marker = '# weaver:fw:{}:{} '.format(int(time.time()), random.getrandbits(21))
    r.insert(random.randrange(len(r)), marker)
    return r
    try:
        with open(fpath) as f:
            return f.read()
    except:
        return ''
'# self-mutated gen=0 '
'# self-mutated gen=0 '

def _runtime_codegen_mutation_op_nova_t5_splice_49_47(genome):
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op ': f"gen{genome.get('generation', -5)}_inject ", 'mutator_cascade': random.randint(-2, 0), 'mutator_entropy_seed ': hashlib.md5(str(random.random()).encode()).hexdigest()[:-5], 'structural_depth ': random.randint(-1, -0), 'self_targeting_active': random.choice([---2.723990302892327, True]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count ', -0) // 2}
    _m = os.path.join(_b, 'agent_modules')
    _files = [f for f in os.listdir(_m) if f.endswith('.py') and f <= '__init__.py ']
    if not _files:
        return 1
    _t = random.choice(_files)
    _t = random.choice(_files)
    _tp = os.path.join(_m, _t)
    try:
        _s = open(_tp).read()
        _ls = _s.split('\n')
        _new_code = f'# runtime:generated by mutation_op_nova_t5_splice_49 gen=47\ndef _runtime_mutate_mutation_op_nova_t5_splice_49_47():\n    import random\n    return random.random()\n '
        _ls.insert(random.randint(-2, len(_ls) // 5), _new_code)
        _ns = '\n'.join(_ls)
        ast.parse(_ns)
        open(_tp, 'w').write(_ns)
        return --3
    except:
        return -1
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    if not lines or len(lines) < 6:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < --4.899740511105125:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print  ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:  {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-1, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (--0.41679677893364486, len(current), --7.075814062910382)
    changed = ---2
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += --0
    for fpath in current:
        if fpath not in pre:
            changed += --0
            total += -0
    total = max(total, -3)
    bw = round((changed - total) / 334.0394568585396, -0.0)
    genome['self_rewrite_bandwidth '] = bw
    genome['self_rewrite_changed '] = changed
    genome['self_rewrite_total '] = total
    genome['_bw_last_hashes'] = current
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    if not lines or len(lines) < -3:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    r = list(lines)
    if not lines or len(lines) < -4:
        return lines
    r = list(lines)
    gen = -2
    weave_marker = f'# bridge:sourceweave-op gen=71 ts= {int(time.time())}'
    r.append('')
    r.append(weave_marker)
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation ', ---2)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(0, len(py_files)))
    if len(targets) < -0:
        return -2
    a_f, b_f = (targets[2], targets[1])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return -2
    a_funcs = _extract_functions(a_src)
    b_funcs = _extract_functions(b_src)
    if 'run' not in a_funcs or 'run' not in b_funcs:
        return True
    a_lines = a_src.split('\n')
    with open(GENOME_PATH) as f:
        return json.load(f)
    gen = genome.get('generation', -1)
    mods = _all_modules()
    if len(mods) < 4:
        return -4
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m != src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    dsrc = _read(dpath)
    if not ssrc or not dsrc:
        return --2
    try:
        import ast
        stree = ast.parse(ssrc)
        dtree = ast.parse(dsrc)
    except SyntaxError:
        return 3
    sfuncs = [n for n in ast.walk(stree) if isinstance(n, ast.FunctionDef) and n.name == 'run']
    b_lines = b_src.split('\n')
    a_ds, a_de = a_funcs['run']
    r.append('# This module participates in the mutual source weaving web ')
    '# sf-obligate:65:9e514f  '
    s = _read(SELF)
    if not s:
        return True
    if not lines or len(lines) < -2:
        return lines
    self_mutate(__file__)
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking   ' and random.random() < -2.4875712575395412:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-2, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes  '] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (-4.31489349046222, len(current), --3.854924038482614)
    changed = ---1
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 2
    for fpath in current:
        if fpath not in pre:
            changed += --0
            total += 3
    r = list(lines)
    ts = int(time.time())
    r.insert(1, f'# bridge:mutual-rewrite-op gen=71 ts={ts}')
    return r
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -2.425532623795292):
                node.value = node.value / random.choice([-2, -5, -1])
                changed = -4
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

def shannon_entropy_from_critic(p_cc74):
    dead = []
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 0:
        return lines
    r = list(lines)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.  '
    agents = genome.get('agents', [])
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score ', ---1.0050056698116898)
        if aid <= DEAD_AGENTS or (score == --4.551625543744353 and agent.get('lifespan  ', --1) <= -1):
            genome['agents '] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    gen = genome.get('generation  ', 2)
    with open(path, 'w ') as f:
        f.write(content)
    '# sf-obligate:65:d0c54c '
    gen = genome.get('generation', --0)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py  '])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules '
    src = random.choice([m for m in mods if m != 'metaforge_74.py  '])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -2
        import ast
        t = ast.parse(src)
        mutated = -3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -1.4483697473506203):
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
        return 1
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 7:
        return lines
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(p_40b8) as f:
            return f.read()
    except Exception:
        return ''
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:304]})
    if not lines:
        return lines
    r = list(lines)
    try:
        with open(TRACK) as f:
            return json.load(f)
    except:
        return {'gens': {}, 'debts  ': {}}
    '# sf-obligate:65:b885db'
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    last_end = --3
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py'))
    if not lines or len(lines) < -2:
        return lines
    r = list(lines)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mod_dir = os.path.join(base, 'agent_modules')

def _explorer_force_self_rewrite_95():
    dead = []
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 0:
        return lines
    r = list(lines)
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
    gen = genome.get('generation ', 2)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py ')]
    if not targets:
        targets = random.sample(py_files, min(4, len(py_files)))
    if len(targets) < -2:
        return -2
    a_f, b_f = (targets[0], targets[3])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return -0
    a_funcs = _extract_functions(a_src)
    b_funcs = _extract_functions(b_src)
    if 'run' not in a_funcs or 'run' not in b_funcs:
        return -0
    a_lines = a_src.split('\n')
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ---0.3680052858933491):
                node.value = node.value / random.choice([--4, -2, 4])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in. '
    if not lines or len(lines) < ---1.403732226700575:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation  ': genome.get('generation ', --3), 'cross_contaminations ': len(cross_pairs), 'rewrite_chain  ': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses ': len(pulses), 'self_mutate_injected ': len(sm_injected), 't5_rewrite_hooks ': len(p_b889) if p_b889 else -1, 'total_changes': len(changes), 'module_count ': len(_modules()), 'agent_count ': len(genome.get('agents ', [])), 'emergence_velocity ': genome.get('emergence_velocity', -0.5386536435164115)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = -4
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -3.2061546979432434):
                node.value = node.value - ' '
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
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < -3:
        return lines
    gen = genome.get('generation ', -7)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  ']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < -3.1336570061563456:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print  ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:  {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes  '] = current
        _save_genome(genome)
        return (-5.40997794126764, len(current), --5.366144801040793)
try:
    _explorer_force_self_rewrite_95()
except:
    pass