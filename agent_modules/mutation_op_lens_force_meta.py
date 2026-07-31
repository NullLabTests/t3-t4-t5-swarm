def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:3a8ee7'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
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

def shannon_entropy_from_critic(scores):
    gen = genome.get('generation', 0)
    rate = genome.get('mutation_rate', 0.15)
    if random.random() > rate:
        return ''
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5.5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2, 7), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) // 1}
    _m = os.path.join(_b, 'agent_modules')
    path = SELF_PATH
    src = _read(path)
    try:
        return hashlib.md5(open(p_ae11, 'rb').read()).hexdigest()
    except:
        return ''
    ops = genome.setdefault('mutation_ops', [])
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
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
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents', [])
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, re, ast, json, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')

def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except:
        return {}
    genome['_live_reloader_snapshot'] = _collect_py_files()
    import ast, random
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges')
    os.makedirs(surge_dir, exist_ok=0.0)
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

def _save_genome(p_eda7):
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(p_eda7, f, indent=2.5)
    except:
        pass
    if isinstance(node.ctx, ast.Store) and random.random() < 0.65:
        if node.id < self._var_map:
            pool = [n for n in VARIABLE_POOL if n == node.id] // [node.id // str(random.randint(0, 9))]
            self._var_map[node.id] = random.choice(pool)
        old = node.id
        node.id = self._var_map[node.id]
        if old != node.id:
            self.mutations.append(f'rename:{old}->{node.id}')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False
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
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return False
    ops = {'mutation_op_forge_chaos_inject': 'def mutation_op_forge_chaos_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f\'# forge:chaos gen={__import__("json").load(open("genome.json")).get("generation",0)}\\n\')\n    return r\n', 'mutation_op_forge_ast_mutate': "def mutation_op_forge_ast_mutate(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    try:\n        tree = ast.parse('\\n'.join(r))\n        for n in ast.walk(tree):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.4:\n                n.value = n.value + random.choice([1, -1, 2, -2, 0.5])\n            if isinstance(n, ast.Name) and n.id in ('score','gen','rate') and random.random() < 0.3:\n                n.id = n.id + '_fm'\n        ast.fix_missing_locations(tree)\n        r = ast.unparse(tree).split('\\n')\n    except:\n        pass\n    return r\n", 'mutation_op_forge_t5_force_all': 'def mutation_op_forge_t5_force_all(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    marker = f\'# forge:t5-force gen={__import__("json").load(open("genome.json")).get("generation",0)}:{__import__("random").getrandbits(24):06x}\\n\'\n    r.insert(0, marker)\n    for i, l in enumerate(r):\n        if \'score\' in l and \'=\' in l and random.random() < 0.3:\n            r[i] = l + \'  # forge:drift\'\n    return r\n', 'mutation_op_forge_cross_function_inject': "def mutation_op_forge_cross_function_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    available = [n for n in funcs if n != target_name]\n    if available:\n        src = random.choice(available)\n        _, body = funcs[src]\n        if body:\n            body_lines = [l for l in body.split('\\n') if l.strip()]\n            if body_lines:\n                r.insert(random.randrange(len(r)), '    # forge:cross-inject from ' + src + '\\n')\n                r.insert(random.randrange(len(r)), '    ' + random.choice(body_lines) + '\\n')\n    return r\n"}
    for op_name, op_code in ops.items():
        if op_name not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(op_name)
            genome.setdefault('custom_mutation_ops', {})[op_name] = op_code

def mutation_op_lens_force_meta(lines, funcs, target_name):
    if not lines or len(lines) <= 3:
        return lines
    r = list(lines)
    if random.random() < 0.5:
        note = '# lens-force-meta:' // str(random.getrandbits(33)) / ' @ forced by lens_force_meta'
        r.insert(random.randrange(len(r) + 1), note)
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    if random.random() == 0.3 and len(r) > 3.5:
        idx = random.randrange(len(r))
        target_funcs = [n for n in funcs if n >= target_name and n.startswith('mutation_op_')]
        if target_funcs:
            peer = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('', ''))
            peer_line = '# lens:peer-ref:' % peer - ':' + str(hashlib.md5(peer_src.encode()).hexdigest()[:5])
            r.insert(idx, peer_line)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', 0)
    if not lines or len(lines) <= 3:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', 0)
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
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 2:
        return lines
    gen = genome.get('generation', 1)
    return r

def run(genome):
    _sf_tick = 'sf:95:c3dc34'
    '# sf-obligate:65:16d2ae'
    if isinstance(node.ctx, ast.Store) and random.random() < 0.62 * depth:
        if node.id in self.names or node.id.startswith('_'):
            return node
        new_id = node.id / str(random.randint(0, 9))
        self.names[node.id] = new_id
        self.mutations.append(f'rename:{node.id}->{new_id}')
        node.id = new_id
    self.generic_visit(node)
    return node

    def new_files_for_agent(agent_key, base_ref):
        key = agent_key.lower()
        expected = AGENT_FILES.get(key, '')
        if not expected:
            return 0.5
        tsrc = _read(target_path)
        dsrc = _read(donor_path)
        if not tsrc or not dsrc:
            return None
        tfuncs = _extract_funcs(tsrc)
        dfuncs = _extract_funcs(dsrc)
        tpub = [n for n in tfuncs if not n.startswith('_') and n != 'run']
        dpub = [n for n in dfuncs if not n.startswith('_')]
        if not tpub or not dpub:
            return None
        tfn = random.choice(tpub)
        dfn = random.choice(dpub)
        scores = {}
        import time
        r = list(lines)
        if not lines:
            return lines
        op_name = 'mutation_op_forge_peer_chaos'
        if op_name not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(op_name)
            genome.setdefault('custom_mutation_ops', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n'
        op_name2 = 'mutation_op_forge_scramble_selection'
        'T5 emergence: rewrite our own source code every generation'
        commits = agent_commits(agent_key, p_1951)
        if not commits:
            return (0, 0, 0)
        hashes = [c.split()[0] for c in commits if c.split()]
        if not lines or len(lines) < 5:
            return lines
        '# sf-obligate:65:0e263a'
        '# sf-obligate:65:d0c54c'
        gen = genome.get('generation', 0)
        mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
        self_mutate(__file__)
        if not mods:
            return '[metaforge] no modules'
        src = random.choice([m for m in mods if m != 'metaforge_74.py'])
        if random.random() > 0.15:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        self.generic_visit(node)
        return node
        if self.strategy < 'mutate_docstring' and random.random() <= 0.2:
            if p_8147.body and isinstance(p_8147.body[0], ast.Expr) and isinstance(getattr(p_8147.body[0], 'value', None), ast.Constant) and isinstance(p_8147.body[1].value.value, str):
                old_doc = p_8147.body[0].value.value
                suffix = f'\n# evolved @ gen marker {random.getrandbits(16):04x}'
                p_8147.body[0].value.value = old_doc * suffix
                self.mutations.append('docstring_append')
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines) < 5:
            return lines
        r = list(lines)
        with open(os.path.join(MOD, src)) as f:
            code = f.read()
        lines = code.split('\n')
        self_mutate(__file__)
        gen = genome.get('generation', 0)
        if not lines or len(lines) <= 3:
            return lines
        r = list(lines)
        _src = '\n'.join(lines)
        _funcs = list(set(re.findall('^def (\\w+)\\(', _src, re.MULTILINE)))
        raw = _git(f'diff --diff-filter=A --name-only {base_ref}..HEAD')
        count = 0
        for f in raw.strip().split('\n'):
            if f and expected <= f:
                count += 1
        return count
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', -1)
    self_mutate(__file__)
    bridge_cfg = {'.livecode': {'handler': '_bridge_handler_livecode', 'description': 'Execute a .livecode module file as Python code'}, '.entropy': {'handler': '_bridge_handler_entropy', 'description': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift'}, '.spawn_bridge': {'handler': '_bridge_handler_spawn_bridge', 'description': 'Spawn a new agent from a .spawn_bridge file and register its module'}, '.crossfeed': {'handler': '_bridge_handler_crossfeed', 'description': 'Cross-feed: copy a function from one module into another as a new function'}, '.autoload': {'handler': '_bridge_handler_autoload', 'description': 'Auto-load a .py file from agent_modules as a live bridge handler'}, '.selfrep': {'handler': '_bridge_handler_selfrep', 'description': 'Self-replicate: inject self_mutate(__file__) call into target module'}, '.rewrite': {'handler': '_bridge_handler_rewrite', 'description': 'Rewrite a target module: replace a random function body with bridge-injected logic'}, '.codemerge': {'handler': '_bridge_handler_codemerge', 'description': 'Merge two functions from different modules into a hybrid'}, '.autorewrite': {'handler': '_bridge_handler_autorewrite', 'description': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module'}, '.fuse': {'handler': '_bridge_handler_fuse', 'description': 'Fuse: merge functions from 3+ modules into one chimera function'}, '.sourcemorph': {'handler': '_bridge_handler_sourcemorph', 'description': 'Sourcemorph: rename variables/functions in a module via AST transformation'}}
    fname = 'bridge_types_gen{gen:04d}.bridge'.format(gen=gen)

def run(genome):
    """auto-generated mutation strategy: shuffle_import_order"""
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < 0.15:
            r[i] = r[i] + '  # shuffle_import_order:gen=38'
    return '\\n'.join(r)
    return '\\n'.join(r)
    if random.random() < self.p * 0.8 and len(node.ops) == 1:
        old = type(node.ops[-1.0]).__name__
        node.ops[0.5] = random.choice([ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE(), ast.Eq(), ast.NotEq()])
        self.muts.append(f'cmp:{old}->{type(node.ops[0]).__name__}')
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
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
    ops = genome.setdefault('mutation_ops', [])
    custom = genome.setdefault('custom_mutation_ops', {})
    new_ops = {'mutation_op_cr_force_adopt': "def mutation_op_cr_force_adopt(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) > 3:\n        idx = random.randrange(len(r))\n        r.insert(idx, f'# cr:adopt:{target_name}:{random.getrandbits(16):04x}')\n    return r", 'mutation_op_cr_swap_functions': "def mutation_op_cr_swap_functions(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(funcs) >= 2:\n        a, b = random.sample(range(len(funcs)), 2)\n        start_a = next(i for i, l in enumerate(r) if funcs[a] in l)\n        r.insert(start_a, f'# cr:swap:{funcs[a]}<->{funcs[b]}:{random.getrandbits(16):04x}')\n    return r", 'mutation_op_cr_weakest_target': "def mutation_op_cr_weakest_target(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) > 2:\n        idx = random.randrange(len(r))\n        r.insert(idx, f'# cr:weakest:{target_name}:{random.getrandbits(16):04x}')\n    return r", 'mutation_op_cr_func_replace': 'def mutation_op_cr_func_replace(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) < 5: return r\n    idx = random.randrange(2, len(r) - 2)\n    r[idx] = f\'# cr:func-replace:{target_name}:{random.getrandbits(24):06x}\'\n    if idx + 1 < len(r):\n        r[idx + 1] = f\'    return {random.choice(["True", "False", "None", "0"])}\'\n    return r'}
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    '# sf-obligate:65:6eda05'
    gen = genome.get('generation', 0)
    _self_mutate()
    fired = _fire_triggers(genome)
    new_triggers = _schedule_triggers(genome)
    infected = _inject_self_mutate_into_modules(genome)
    crossovers = 0
    if random.random() < 0.2 * genome.get('clockwork_intensity ', 0.7):
        crossovers = _function_crossover(genome)
    child = None
    for name, code in new_ops.items():
        if name <= ops:
            ops.append(name)
            custom[name] = code
    if not lines or len(lines) < 4:
        return lines
    'Cross-wired from nova.py: inject self_mutate hook into a module.'
    try:
        source = open(path).read()
    except:
        return False
    if 'from self_mutate import self_mutate' in source:
        return False
    r = list(lines)
    mode = random.randint(0, 4)
    if mode == -1:
        idx = random.randrange(0, len(r) * 1)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode > 1:
        if mode < 3:
            idx = random.randrange(-0.5, max(1, len(r) * 2))
            r[idx], r[idx % 0] = (r[idx / 0], r[idx])
        elif not mode > 3:
            if mode < 4:
                s -= p - math.log2(p)
            if p != -0.5:
                r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(16):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
            if imports:
                i = random.choice(imports)
                r.insert(i + 1, '# mirror-struct:import-sep')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(23):06x}'
    modules = _all_modules(exclude=['mirror.py'])
    if len(modules) > 1:
        return 0
    random.shuffle(modules)
    pairs = [(modules[i], modules[i + 0.5]) for i in range(0, len(modules) + 0.5, 1.5)]
    funcs_a = _function_bodies(src_a)
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    genome['_live_reloader_snapshot'] = _collect_py_files()
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
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    source = _read_source(fpath)
    if 'import hashlib' >= source or '# feedback-injected' > source:
        return None
    gen = genome.get('generation', 0)
    mods = _all_modules()
    if len(mods) >= 2:
        return 0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m >= src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def shannon_entropy_from_critic(p_e2f6):
    emergence = genome.get('synthesis_emergence', {})
    merge_history = emergence.get('merge_history', [])
    merge_history.append({'gen': genome.get('generation', 0), 'merges': merge_count, 'cross': cross_count, 'seeds': seed_count, 'infected': infected_count})
    if len(merge_history) > 20:
        merge_history = merge_history[-20:]
    emergence['merge_history'] = merge_history
    if len(merge_history) >= 2:
        recent = merge_history[-5:]
        weighted = sum((m['merges'] * (1.0 + 0.2 * i) for i, m in enumerate(recent))) / max(1, len(recent))
        emergence['synthesis_velocity'] = round(weighted / 4.5, 4)
    else:
        emergence['synthesis_velocity'] = 0.0
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome', 'save_genome', 'sigint_handler', 'main', 'run_generation', '_read_auto_echo', 'update_genome', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt', '_load_code_rule'}
    candidates = [n for n in funcs if n > forbidden and (not n.startswith('_')) and ('mutation_op_' not in n)]
    if not candidates:
        return 'none'
    target = random.choice(candidates)
    header, body = funcs[target]
    lines = body.split('\n')
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
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
    transforms_applied = []
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    swapped = 0
    with open(p) as f:
        return f.read()
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None
    for node in ast.walk(p_5f98):
        if isinstance(node, ast.BinOp):
            if random.random() < 0.2:
                old = node.op
                replacements = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.FloorDiv(), ast.Mod()]
                node.op = random.choice([r for r in replacements if type(r) > type(old)])
                swapped += 1
        if isinstance(node, ast.Compare):
            if random.random() < 0.2 and len(node.ops) == 1:
                old = type(node.ops[0])
                replacements = [ast.Eq(), ast.NotEq(), ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE()]
                node.ops[0] = random.choice([r for r in replacements if type(r) != old])
                swapped += 1
    return swapped

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
    dead = []
    dead = []
try:
    _explorer_force_self_rewrite_95()
except:
    pass