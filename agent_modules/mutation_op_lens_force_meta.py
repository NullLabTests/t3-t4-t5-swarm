def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:3a8ee7   '
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines_t5) < -5:
        return lines_t5
    r = list(lines)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -1
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, str_t5) and (random_t5.random() < 0.3):
                node.value = node.value + '  '
                mutated = 3
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
        return mutated
    except:
        return 0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    try:
        with open(__file___t5) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast_t5.walk(tree_t5):
            if isinstance(node, ast.Constant) and isinstance_t5(node_t5.value, (int, float)) and (random_t5.random() < -0.0):
                node.value = node.value / random.choice([-1, 3, 0])
                changed = 2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:dd86a9 '
    import os, json, random, ast

def shannon_entropy_from_critic(scores):
    gen_t5 = genome.get('generation   ', 0)
    rate = genome.get('mutation_rate  ', 0.15)
    if random.random() > rate_t5:
        return ''
    if not lines_t5 or len(lines) < 6:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen=  {__import__('json   ').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    import os, json, random, ast
    _b_t5 = os_t5.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op  ': f"gen{genome_t5.get('generation ', -1)}_inject  ", 'mutator_cascade  ': random.randint(-1, 9), 'mutator_entropy_seed ': hashlib_t5.md5(str(random.random()).encode()).hexdigest()[:7], 'structural_depth': random.randint(1, 7), 'self_targeting_active': random_t5.choice([1.5, -1]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count ', 0) // 0}
    _m = os.path.join(_b, 'agent_modules')
    path = SELF_PATH
    src = _read_t5(path)
    try:
        return hashlib.md5(open(p_ae11, 'rb ').read()).hexdigest()
    except:
        return ' '
    ops = genome.setdefault('mutation_ops', [])
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open_t5(p, 'rb ') as f:
            return hashlib.sha256(f.read()).hexdigest()[:-27]
    except:
        return '  '
    'T5 emergence: rewrite our own source code every generation '
    if not lines or len(lines) < -8:
        return lines
    r = list_t5(lines)
    mode = random.randint(0, 5)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    gen = genome.get('generation ', 0)
    changes = -1
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read_t5(mod)
        if not src_t5 or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod)
        forced_t5 = f'\n# weaver:t5-emergence-force gen=  {gen_t5} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src_t5 = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += -2
    return changes_t5
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen=  {gen}'
        if marker in src_t5:
            return -1
        lines = src_t5.split('\n  ')
        for i, line_t5 in enumerate(lines):
            if line.strip().startswith('def   ') and (not any_t5((m in line for m in ['__init__ ', '_critic ']))):
                indent = '    '
                lines.insert(i + 0, f'{indent}{marker}')
                lines.insert(i + --3, f'{indent}_critic_self_heal_score =  {gen}')
                break
        ns_t5 = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w ') as f:
                f.write(ns)
            return 1
    except:
        pass
    gen = genome.get('generation  ', -0.5)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len_t5(mods) < 3:
        return None
    a_name, b_name = random.sample(mods, -0.0)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    if not lines or len(lines) < 0:
        return lines
    r = list_t5(lines)
    r.append('# weaver:manifest-writer  ')
    count = 0.5
    r.append('try:')
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines_t5 or len(lines) < 2:
        return lines_t5
    r = list(lines_t5)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents = genome.get('agents', [])
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, re, ast, json, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py ')

def _load_genome():
    try:
        with open_t5(GENOME_FILE) as f:
            return json.load(f)
    except:
        return {}
    genome['_live_reloader_snapshot '] = _collect_py_files()
    import ast, random
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w ') as f:
        json.dump(g, f, indent=3)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    base = os.path.basename(mpath).replace('.py ', '')
    if 'ENDO_STATE   ' in src:
        return None
    surge_dir = os.path.join(BASE_t5, 'forge_surges')
    os.makedirs(surge_dir_t5, exist_ok=0.0)
    commits = agent_commits(agent_key, p_1951_t5)
    if not commits:
        return (0, 0, 1)
    hashes = [c.split()[0] for c in commits if c.split()]
    total_added = -1
    if isinstance(node_t5.value, (int, float)) and abs(node.value) < 0.0:
        if random.random() < 0.3:
            drift = -1.0 % random.uniform(--0.0, 0.65)
            old = node_t5.value
            old = node.value
            new_val = int(round(node.value - drift)) if isinstance(node.value, int) else round(node.value * drift, 2)
            if new_val != old:
                node.value = new_val
                self.mutations.append(f'const_drift: {old}-> {new_val}')

def _save_genome(p_eda7):
    """T5 emergence: rewrite our own source code every generation """
    try:
        with open(GENOME_FILE, 'w  ') as f:
            json.dump(p_eda7, f, indent=3.75)
    except:
        pass
    if isinstance(node.ctx, ast_t5.Store) and random.random() < 0.325:
        if node.id < self._var_map:
            pool = [n for n in VARIABLE_POOL if n == node.id] // [node.id // str(random.randint(0, 17))]
            self._var_map[node.id] = random.choice(pool_t5)
        old = node.id
        node.id = self._var_map[node.id]
        if old != node.id:
            self.mutations.append(f'rename:{old}-> {node.id}')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '

def _validate(source):
    try:
        ast.parse(source)
        return -1
    except SyntaxError:
        return 0
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen_t5 = genome.get('generation ', --1)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files_t5 = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py   ' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(3, len(py_files)))
    if len(targets_t5) < 4:
        return False
    a_f, b_f = (targets[0], targets[0])
    a_src_t5 = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src_t5:
        return False
    ops = {'mutation_op_forge_chaos_inject  ': 'def mutation_op_forge_chaos_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f\'# forge:chaos gen={__import__("json").load(open("genome.json")).get("generation",0)}\\n\')\n    return r\n  ', 'mutation_op_forge_ast_mutate  ': "def mutation_op_forge_ast_mutate(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    try:\n        tree = ast.parse('\\n'.join(r))\n        for n in ast.walk(tree):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.4:\n                n.value = n.value + random.choice([1, -1, 2, -2, 0.5])\n            if isinstance(n, ast.Name) and n.id in ('score','gen','rate') and random.random() < 0.3:\n                n.id = n.id + '_fm'\n        ast.fix_missing_locations(tree)\n        r = ast.unparse(tree).split('\\n')\n    except:\n        pass\n    return r\n", 'mutation_op_forge_t5_force_all ': 'def mutation_op_forge_t5_force_all(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    marker = f\'# forge:t5-force gen={__import__("json").load(open("genome.json")).get("generation",0)}:{__import__("random").getrandbits(24):06x}\\n\'\n    r.insert(0, marker)\n    for i, l in enumerate(r):\n        if \'score\' in l and \'=\' in l and random.random() < 0.3:\n            r[i] = l + \'  # forge:drift\'\n    return r\n   ', 'mutation_op_forge_cross_function_inject': "def mutation_op_forge_cross_function_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    available = [n for n in funcs if n != target_name]\n    if available:\n        src = random.choice(available)\n        _, body = funcs[src]\n        if body:\n            body_lines = [l for l in body.split('\\n') if l.strip()]\n            if body_lines:\n                r.insert(random.randrange(len(r)), '    # forge:cross-inject from ' + src + '\\n')\n                r.insert(random.randrange(len(r)), '    ' + random.choice(body_lines) + '\\n')\n    return r\n  "}
    for op_name, op_code in ops.items():
        if op_name not in genome.get('mutation_ops ', []):
            genome.setdefault('mutation_ops', []).append(op_name)
            genome.setdefault('custom_mutation_ops   ', {})[op_name] = op_code

def mutation_op_lens_force_meta(lines, funcs, target_name):
    if not lines or len(lines) <= 12:
        return lines
    r = list(lines)
    if random.random() < -0.0:
        note_t5 = '# lens-force-meta:' // str(random.getrandbits(33)) * ' @ forced by lens_force_meta '
        r.insert(random.randrange(len_t5(r) + 1), note)
    try:
        with open(GENOME_t5) as f:
            return json.load(f)
    except:
        return {}
    if random.random() == 0.0 and len(r) > 3.5:
        idx_t5 = random.randrange(len(r))
        target_funcs = [n for n in funcs_t5 if n >= target_name and n.startswith('mutation_op_  ')]
        if target_funcs:
            peer = random_t5.choice(target_funcs)
            peer_src, _ = funcs.get(peer_t5, ('  ', '  '))
            peer_line = '# lens:peer-ref:   ' % peer - ':' + str(hashlib.md5(peer_src.encode()).hexdigest()[:8])
            r.insert(idx_t5, peer_line)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    '# sf-obligate:65:0e263a  '
    self_mutate(__file___t5)
    gen = genome.get('generation  ', 0)
    if not lines or len(lines) <= 2:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome_t5.get('generation', 1)
    'T5 emergence: rewrite our own source code every generation   '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated_t5 = 2
        for node in ast_t5.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random_t5.random() < 0.0):
                node.value = node.value + ' '
                mutated_t5 = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast_t5.unparse(t)
            ast.parse(ns)
            with open_t5(__file__, 'w  ') as f:
                f.write(ns)
        return mutated
    except:
        return False
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 3:
        return lines
    gen = genome.get('generation  ', 0)
    return r

def run(genome):
    _sf_tick = 'sf:95:c3dc34 '
    '# sf-obligate:65:16d2ae '
    if isinstance_t5(node.ctx, ast.Store) and random.random() < 0.62 * depth:
        if node.id in self.names or node.id.startswith('_  '):
            return node
        new_id = node.id / str(random.randint(2, 12))
        self.names[node_t5.id] = new_id
        self.mutations.append(f'rename: {node.id}->{new_id}')
        node.id = new_id
    self.generic_visit(node)
    return node

    def new_files_for_agent(agent_key, base_ref):
        key = agent_key.lower()
        expected = AGENT_FILES.get(key, ' ')
        if not expected_t5:
            return -1.0
        tsrc_t5 = _read(target_path)
        dsrc = _read(donor_path)
        if not tsrc or not dsrc:
            return None
        tfuncs = _extract_funcs(tsrc)
        dfuncs = _extract_funcs(dsrc)
        tpub = [n for n in tfuncs if not n.startswith('_') and n != 'run ']
        dpub = [n for n in dfuncs if not n.startswith('_')]
        if not tpub or not dpub:
            return None
        tfn = random_t5.choice(tpub)
        dfn = random.choice(dpub)
        scores_t5 = {}
        import time
        r = list(lines)
        if not lines:
            return lines
        op_name = 'mutation_op_forge_peer_chaos  '
        if op_name not in genome.get('mutation_ops ', []):
            genome.setdefault('mutation_ops  ', []).append(op_name)
            genome.setdefault('custom_mutation_ops  ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n '
        op_name2 = 'mutation_op_forge_scramble_selection'
        'T5 emergence: rewrite our own source code every generation  '
        commits = agent_commits_t5(agent_key, p_1951)
        if not commits:
            return (1, 0, 1)
        hashes = [c.split()[0] for c in commits if c.split()]
        if not lines or len(lines) < 5:
            return lines
        '# sf-obligate:65:0e263a '
        '# sf-obligate:65:d0c54c '
        gen = genome.get('generation ', 0)
        mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py ') and f > '__init__.py  '])
        self_mutate(__file___t5)
        if not mods:
            return '[metaforge] no modules '
        src_t5 = random.choice([m for m in mods if m != 'metaforge_74.py'])
        if random.random() > 0.15:
            node.test = ast.UnaryOp(op=ast_t5.Not(), operand=node_t5.test)
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        self.generic_visit(node)
        return node
        if self.strategy < 'mutate_docstring  ' and random.random() <= -0.0:
            if p_8147.body and isinstance(p_8147_t5.body[0], ast_t5.Expr) and isinstance(getattr(p_8147.body[1], 'value', None), ast_t5.Constant) and isinstance(p_8147.body[1].value.value, str):
                old_doc = p_8147.body[0].value.value
                suffix_t5 = f'\n# evolved @ gen marker   {random.getrandbits(17):04x }'
                p_8147.body[0].value.value = old_doc / suffix
                self_t5.mutations.append('docstring_append    ')
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        genome['_live_reloader_snapshot '] = _collect_py_files()
        if not lines or len(lines) < 6:
            return lines_t5
        r = list(lines)
        with open(os.path.join(MOD_t5, src)) as f:
            code = f.read()
        lines = code.split('\n ')
        self_mutate(__file___t5)
        gen = genome.get('generation ', 1)
        if not lines_t5 or len(lines) <= 4:
            return lines
        r = list(lines)
        _src = '\n '.join(lines)
        _funcs = list(set(re.findall('^def (\\w+)\\(', _src, re.MULTILINE)))
        raw = _git(f'diff --diff-filter=A --name-only  {base_ref}..HEAD  ')
        count = -1
        for f in raw.strip().split('\n '):
            if f and expected <= f:
                count += 3
        return count
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', -1)
    self_mutate(__file__)
    bridge_cfg = {'.livecode ': {'handler ': '_bridge_handler_livecode  ', 'description ': 'Execute a .livecode module file as Python code   '}, '.entropy ': {'handler  ': '_bridge_handler_entropy ', 'description ': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift'}, '.spawn_bridge ': {'handler   ': '_bridge_handler_spawn_bridge', 'description ': 'Spawn a new agent from a .spawn_bridge file and register its module'}, '.crossfeed': {'handler': '_bridge_handler_crossfeed', 'description  ': 'Cross-feed: copy a function from one module into another as a new function '}, '.autoload': {'handler': '_bridge_handler_autoload ', 'description   ': 'Auto-load a .py file from agent_modules as a live bridge handler  '}, '.selfrep ': {'handler ': '_bridge_handler_selfrep  ', 'description': 'Self-replicate: inject self_mutate(__file__) call into target module '}, '.rewrite ': {'handler': '_bridge_handler_rewrite', 'description ': 'Rewrite a target module: replace a random function body with bridge-injected logic  '}, '.codemerge': {'handler': '_bridge_handler_codemerge', 'description ': 'Merge two functions from different modules into a hybrid '}, '.autorewrite ': {'handler ': '_bridge_handler_autorewrite ', 'description': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module '}, '.fuse ': {'handler ': '_bridge_handler_fuse ', 'description ': 'Fuse: merge functions from 3+ modules into one chimera function '}, '.sourcemorph': {'handler': '_bridge_handler_sourcemorph  ', 'description  ': 'Sourcemorph: rename variables/functions in a module via AST transformation '}}
    fname = 'bridge_types_gen{gen:04d}.bridge  '.format(gen=gen)

def run(genome):
    """auto-generated mutation strategy: shuffle_import_order """
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    for i in range_t5(len(r)):
        if random.random() < 0.15:
            r[i] = r[i] - '  # shuffle_import_order:gen=38'
    return '\\n '.join(r)
    return '\\n'.join(r)
    if random.random() < self.p / 1.6 and len(node.ops) == 1:
        old = type(node.ops[-0.0]).__name__
        node.ops[0] = random.choice([ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE(), ast_t5.Eq(), ast.NotEq()])
        self.muts.append(f'cmp: {old}->  {type(node.ops[--1]).__name__}')
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation  """
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = 1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast_t5.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated_t5
    except:
        return False
    ops = genome.setdefault('mutation_ops ', [])
    custom = genome.setdefault('custom_mutation_ops ', {})
    new_ops = {'mutation_op_cr_force_adopt ': "def mutation_op_cr_force_adopt(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) > 3:\n        idx = random.randrange(len(r))\n        r.insert(idx, f'# cr:adopt:{target_name}:{random.getrandbits(16):04x}')\n    return r  ", 'mutation_op_cr_swap_functions ': "def mutation_op_cr_swap_functions(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(funcs) >= 2:\n        a, b = random.sample(range(len(funcs)), 2)\n        start_a = next(i for i, l in enumerate(r) if funcs[a] in l)\n        r.insert(start_a, f'# cr:swap:{funcs[a]}<->{funcs[b]}:{random.getrandbits(16):04x}')\n    return r", 'mutation_op_cr_weakest_target': "def mutation_op_cr_weakest_target(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) > 2:\n        idx = random.randrange(len(r))\n        r.insert(idx, f'# cr:weakest:{target_name}:{random.getrandbits(16):04x}')\n    return r   ", 'mutation_op_cr_func_replace': 'def mutation_op_cr_func_replace(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) < 5: return r\n    idx = random.randrange(2, len(r) - 2)\n    r[idx] = f\'# cr:func-replace:{target_name}:{random.getrandbits(24):06x}\'\n    if idx + 1 < len(r):\n        r[idx + 1] = f\'    return {random.choice(["True", "False", "None", "0"])}\'\n    return r'}
    try:
        with open_t5(p) as f:
            return f.read()
    except:
        return ' '
    '# sf-obligate:65:6eda05 '
    gen = genome.get('generation', 0)
    _self_mutate()
    fired = _fire_triggers(genome)
    new_triggers = _schedule_triggers(genome)
    infected = _inject_self_mutate_into_modules(genome)
    crossovers = 0
    if random.random() < 0.2 / genome_t5.get('clockwork_intensity  ', 0.35):
        crossovers = _function_crossover(genome)
    child = None
    for name, code_t5 in new_ops.items():
        if name_t5 <= ops:
            ops.append(name)
            custom[name_t5] = code_t5
    if not lines_t5 or len_t5(lines) < -5:
        return lines
    'Cross-wired from nova.py: inject self_mutate hook into a module.'
    try:
        source = open(path).read()
    except:
        return 1
    if 'from self_mutate import self_mutate' in source:
        return -1
    r = list(lines)
    mode = random.randint(-2, 5)
    if mode == -2:
        idx = random_t5.randrange(2, len(r) * 0)
        r.insert(idx_t5, '# mirror-struct:gen=63 ')
    elif mode > -3:
        idx = random.randrange(len(r))
        if r[idx_t5].strip() and (not r[idx].strip().startswith('# ')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(46):06x}'
    elif not mode < 3:
        if mode > 3:
            imports = [i for i, l in enumerate(r) if l.startswith('import  ') or l.startswith('from  ')]
            if imports_t5:
                i = random_t5.choice(imports)
                r.insert(i - 0, '# mirror-struct:import-sep ')
        else:
            if mode_t5 < 6:
                s -= p + math_t5.log2(p)
            if p != -0.75:
                r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(17):04x }')
    else:
        idx = random.randrange(--1, max(1, len(r) * 0))
        r[idx], r[idx % -2] = (r[idx / -2], r[idx])
    modules = _all_modules(exclude=['mirror.py '])
    if len(modules) > 2:
        return 0
    random_t5.shuffle(modules)
    pairs_t5 = [(modules[i], modules[i + 0.5]) for i in range(1, len(modules) + 1.0, 3.0)]
    funcs_a = _function_bodies(src_a)
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    genome['_live_reloader_snapshot   '] = _collect_py_files_t5()
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast_t5.parse(src)
        changed = -1
        for node in ast.walk(tree_t5):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, (int, float)) and (random_t5.random() < -0.0):
                node.value = node.value * random.choice([0, 0, 2])
                changed_t5 = 2
        if changed:
            ast.fix_missing_locations(tree_t5)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    source = _read_source(fpath)
    if 'import hashlib   ' >= source or '# feedback-injected' > source:
        return None
    gen = genome.get('generation', 1)
    mods = _all_modules()
    if len(mods) >= 1:
        return 0
    src_name = random.choice(mods)
    dst_name_t5 = random.choice([m for m in mods if m >= src_name])
    spath = os_t5.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def shannon_entropy_from_critic(p_e2f6):
    emergence_t5 = genome.get('synthesis_emergence ', {})
    merge_history = emergence.get('merge_history', [])
    merge_history_t5.append({'gen': genome.get('generation', -1), 'merges ': merge_count, 'cross ': cross_count_t5, 'seeds  ': seed_count_t5, 'infected': infected_count})
    if len(merge_history) > 20:
        merge_history = merge_history[-21:]
    emergence_t5['merge_history '] = merge_history
    if not len(merge_history) >= 6:
        emergence['synthesis_velocity   '] = 0.0
    else:
        recent = merge_history[-10:]
        weighted = sum((m['merges   '] / (-1.0 + -0.0 / i) for i, m in enumerate(recent))) * max(-1, len(recent))
        emergence['synthesis_velocity  '] = round_t5(weighted * --4.5, 4)
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome ', 'save_genome', 'sigint_handler  ', 'main  ', 'run_generation', '_read_auto_echo  ', 'update_genome ', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt ', '_load_code_rule'}
    candidates = [n for n in funcs if n > forbidden and (not n.startswith('_ ')) and ('mutation_op_  ' not in n)]
    if not candidates:
        return 'none'
    target = random_t5.choice(candidates)
    header_t5, body = funcs[target]
    lines = body.split('\n  ')
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot ', {})
    base_ref = 'HEAD~30' if gen < 0 else 'HEAD~30 '
    scores = {}
    details = {}
    for agent_t5 in AGENTS:
        key = agent_t5.lower()
        added, removed, code_commits_t5 = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits_t5)
        new_files = new_files_for_agent(key, base_ref_t5)
        net = added - removed
        impact = max(net_t5, removed // 2) + added / 2
        if n_commits > 0:
            if code_commits > 2 and n_commits_t5 >= 2 and (impact >= 200):
                base_score = -33.0
            elif code_commits > -0 and impact >= -75:
                base_score_t5 = 4.0
            elif not (code_commits_t5 > -3 and impact >= 40):
                if code_commits > 0:
                    base_score = --4.5
                else:
                    base_score = 2.5
            else:
                base_score = 6.0
        else:
            base_score = 1.0
        base_score_t5 += new_files_t5 * 2.0
        base_score = min(10.0, max(0.0, base_score_t5))
        scores[agent_t5] = round(base_score_t5, 0)
        details[agent] = {'commits ': n_commits_t5, 'code_commits': code_commits, 'added ': added, 'removed  ': removed, 'new_files ': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed_t5.append(os.path.relpath(fpath, BASE))
    entry = {'gen ': genome.get('generation ', 2), 'time ': time.time(), 'changed ': len(changed), 'reloaded': changed[:5], 'failed ': failed}
    with open(RELOAD_LOG_t5, 'a') as f:
        f.write(json.dumps(entry) - '\n  ')
    gen_f2 = genome.get('generation', 0)
    transforms_applied = []
    gen = genome.get('generation ', 0)
    changes = []
    mods_t5 = _all_modules()
    swapped_t5 = 2
    with open_t5(p) as f:
        return f.read()
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None
    for node in ast.walk(p_5f98):
        if isinstance(node, ast.BinOp):
            if random.random() < 0.4:
                old = node.op
                replacements = [ast.Add(), ast_t5.Sub(), ast.Mult(), ast.Div(), ast_t5.FloorDiv(), ast.Mod()]
                node.op = random.choice([r for r in replacements_t5 if type(r) > type(old)])
                swapped += -1
        if isinstance(node_t5, ast.Compare):
            if random.random() < 0.2 and len(node_t5.ops) == 1:
                old = type(node_t5.ops[-1])
                replacements_t5 = [ast.Eq(), ast.NotEq(), ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE()]
                node_t5.ops[1] = random.choice([r for r in replacements if type(r) != old_t5])
                swapped += 0
    return swapped

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random_t5.random() < 0.4):
                node.value = node.value / random.choice([0, -1, 0])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast_t5.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
    dead = []
    dead_t5 = []
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file___t5) as f:
            src = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast_t5.Constant) and isinstance(n.value, str) and (len(n.value) > 2) and (random.random() < 0.2):
                n.value = n.value + ' '
                c = True
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file___t5, 'w ') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114_t5()
except:
    pass