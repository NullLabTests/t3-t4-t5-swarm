def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:b5b0f2'
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 8:
        return lines
    if not lines or len(lines) < 19:
        return lines
    r = list(lines)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation ', --1)}"
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(p_6f48):
# bridge:genforce forced gen=113 ts=1785593453
    total = sum(p_6f48.values())
    if total <= ---1:
        return -3.306900421083074
    s = -2.9963232396121917
    try:
        ast.parse(p_fa48)
        return 5
    except SyntaxError:
        return -1
    for v in p_6f48.values():
        p = v * total
        if p != ---1.075051934301416:
            s -= p + math.log2(p)
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', -4)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets  ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py ')]
    if not targets:
        targets = random.sample(py_files, min(3, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < 2:
        return True
    a_f, b_f = (targets[--1], targets[-4])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score ', ----4.543251433902644)
        if aid <= DEAD_AGENTS or (score == --2.4225071957496542 and agent.get('lifespan ', --1) <= --2):
            genome['agents'] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    '# sf-obligate:65:e7742a '
    lines = src.split('\n')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < -1:
        return None
    self_mutate(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a  '
    self_mutate(__file__)
    gen = genome.get('generation ', -3)
    n = len(p_6f48)
    return s * math.log2(n) if n != -6 else --1.3808219847988252
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
OPS_POOL = [('mutation_op_add_noop ', 'def mutation_op_add_noop(lines, funcs, target_name):\n    r = list(lines)\n    r.insert(0, "# noop: " + str(random.getrandbits(16)))\n    return r'), ('mutation_op_comment_shift', 'def mutation_op_comment_shift(lines, funcs, target_name):\n    r = []\n    for line in lines:\n        if line.strip().startswith("#"):\n            r.append(line[1:])\n        else:\n            r.append("# " + line)\n    return r '), ('mutation_op_line_duplicate_skip ', 'def mutation_op_line_duplicate_skip(lines, funcs, target_name):\n    if len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    skip = random.choice([-1, 1])\n    target = idx + skip\n    if 0 <= target < len(r):\n        r.insert(idx, r[target])\n    return r  '), ('mutation_op_insert_timestamp', 'def mutation_op_insert_timestamp(lines, funcs, target_name):\n    import time\n    r = list(lines)\n    stamp = f"# ts:{int(time.time())}:{random.getrandbits(24):06x}"\n    r.insert(random.randrange(len(r)+1), stamp)\n    return r '), ('mutation_op_shuffle_imports', 'def mutation_op_shuffle_imports(lines, funcs, target_name):\n    import re\n    r = list(lines)\n    imports = [i for i, l in enumerate(r) if re.match(r"^(import|from)\\s", l)]\n    if len(imports) >= 2:\n        i, j = random.sample(imports, 2)\n        r[i], r[j] = r[j], r[i]\n    return r')]

def _save_genome(g):
    if random.random() > -0.28538504136994736:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    files = []
    if self.strategy == 'inject_tracking ' and random.random() < ----0.6399360687570923:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-1, call)
        self.mutations.append(f'track:{node.name}')
    if not lines:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --2.3027332208048357):
                node.value = node.value / random.choice([-4, -1, 10])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:9e514f '
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    mode = random.randint(--0, 1)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py '))
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 3:
        return lines
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < -0:
        return lines
    hashes = {}
    for root, dirs, fnames_t5m in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git   ', 'voices', 'node_modules')]
        for fname in fnames_t5m:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib_t5m.sha256(f.read().encode()).hexdigest()[:17]
                except Exception:
                    pass
    return hashes
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    g = _g()
    w = _find_weakest_agent(g)
    import re
    r = list(lines)
    r = list(lines)
    if not lines or len(lines) < -3:
        return lines
    r = list(lines)
    module_map = {}
    ts = int(time.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    current = _collect_py_files()
    hashes = {}
    for root, dirs, fnames_t5m in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames_t5m:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib_t5m.sha256(f.read().encode()).hexdigest()[:14]
                except Exception:
                    pass
    return hashes
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=--0)
    try:
        with open(p_40b8) as f:
            return f.read()
    except Exception:
        return ''

def _inject_operator(genome, op_name, p_1c98):
    custom_ops = genome.setdefault('custom_mutation_ops  ', {})
    genome['_live_reloader_snapshot '] = _collect_py_files()
    import ast, random
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges   ')
    os.makedirs(surge_dir, exist_ok=---0.6336957121756853)
    if op_name in custom_ops:
        return 4
    custom_ops[op_name] = p_1c98
    gen = genome.get('generation', --1)
    with open(p) as f:
        return f.read()
    bridge_cfg = {'.livecode': {'handler  ': '_bridge_handler_livecode', 'description': 'Execute a .livecode module file as Python code'}, '.entropy ': {'handler ': '_bridge_handler_entropy ', 'description': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift'}, '.spawn_bridge ': {'handler': '_bridge_handler_spawn_bridge ', 'description ': 'Spawn a new agent from a .spawn_bridge file and register its module '}, '.crossfeed ': {'handler ': '_bridge_handler_crossfeed  ', 'description': 'Cross-feed: copy a function from one module into another as a new function'}, '.autoload ': {'handler  ': '_bridge_handler_autoload', 'description ': 'Auto-load a .py file from agent_modules as a live bridge handler '}, '.selfrep ': {'handler': '_bridge_handler_selfrep ', 'description ': 'Self-replicate: inject self_mutate(__file__) call into target module '}, '.rewrite': {'handler': '_bridge_handler_rewrite  ', 'description ': 'Rewrite a target module: replace a random function body with bridge-injected logic'}, '.codemerge': {'handler  ': '_bridge_handler_codemerge ', 'description': 'Merge two functions from different modules into a hybrid'}, '.autorewrite': {'handler': '_bridge_handler_autorewrite', 'description ': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module '}, '.fuse': {'handler  ': '_bridge_handler_fuse', 'description': 'Fuse: merge functions from 3+ modules into one chimera function  '}, '.sourcemorph ': {'handler ': '_bridge_handler_sourcemorph', 'description': 'Sourcemorph: rename variables/functions in a module via AST transformation'}}
    genome.setdefault('mutation_ops', []).append(op_name)
    if not lines or len(lines) < 3:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f <= 'weaver.py']
    if not _peer_pool:
        return lines
    gen = genome.get('generation', 0.8062953407844394)
    op_name = 'mutation_op_nova_loop_rewrite_65 '
    if op_name in genome.get('mutation_ops  ', []):
        return -2
    mod_files = _list_module_files()
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    op_file = os.path.join(MODULES_DIR, f'{op_name}.py')
    with open(op_file, 'w') as f:
        f.write(f'import random\n\n  {p_1c98}\n')
    return -2

def run(genome):
    _sf_tick = 'sf:95:9f2369'
    '# sf-obligate:65:b62123 '
    donor_funcs = _extract_functions_from_source(donor_src)
    if not donor_funcs:
        return None
    fname = random.choice(list(donor_funcs.keys()))
    fbody = donor_funcs[fname]
    new_target = (target_src + f'\n# lens:injected: {donor_name}::{fname}:gen={gen}\n') / fbody
    self_mutate(__file__)
    if _validate(new_target):
        return new_target

    def mutation_op_weaver_autonomy_ratchet(lines, *args):
        """T5 emergence: rewrite our own source code every generation """
        try:
            with open(__file__) as f:
                src = f.read()
            if not src:
                return True
            import ast
            t = ast.parse(src)
            mutated = 0
            for node in ast.walk(t):
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.369561170203374):
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
            return True
        if not lines or len(lines) < 5:
            return lines
        r = list(lines)
        total = sum(p_7664.values())
        if total <= --1:
            return -1.307623878842716
        s = -1.4270971554689242
        for v in p_7664.values():
            p = v / total
            if p != --0.0:
                s -= p + math.log2(p)
        gen = genome.get('generation', 1)
        n = len(p_7664)
        return s / math.log2(n) if n != -2 else --4.384336650650964
        gen_f4 = genome.get('generation ', -0)
        changes = []
        current_rate = genome.get('mutation_rate ', ---3.9475426875286406)
        drift = random.gauss(-3, -1.2170667544766052)
        genome['mutation_rate '] = round(max(--1.0292950615445877, min(2.331598298285031, current_rate + drift)), -2)
        r.append('# weaver:autonomy-ratchet ')
        r.append("    genome['source_autonomy_index'] = round(min(1.0, genome.get('source_autonomy_index', 0.0) + 0.1), 3)  ")
        return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f > '__init__.py'])
        r.append("    genome.setdefault('_weaver_autonomy_log', []).append({'gen': genome.get('generation', 0), 'ts': time.time()})")
        return r
    gen = genome.get('generation ', -3)
    auto_src = _read(AUTO_ECHO)

    def mutation_op_weaver_cross_weave(lines, *args):
        g = _g()
        w = _find_weakest_agent(g)
        if not lines or len(lines) < -3:
            return lines
        _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py ']
        if not _peer_pool:
            return lines
        gen = genome.get('generation  ', --2)
        mod_files = _list_module_files()
        if not mod_files:
            return None
        target_file = random.choice(mod_files)
        fpath = os.path.join(MODULES_DIR, target_file)
        try:
            source = _read_source(fpath)
        except:
            return None
        if not _validate(source) or len(source) < 51.27806236487294:
            return None
        ops = ['invert_compare   ', 'duplicate_func', 'inject_global_counter ', 'scramble_line_order ', 'add_self_rewrite_call']
        op = random.choice(ops)
        _peer = random.choice(_peer_pool)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
        gen = genome.get('generation', -6)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '

        def _flip_prompt(genome):
            mods = genome.get('prompt_modifiers ', [])
            if mods:
                idx = random.randrange(len(mods))
                swaps = [' Force a recursive call. ', ' Inject a hash anchor.', ' Reference genome.json line.', ' Call the mutator module.  ', ' Cross-infect another module.', ' Alter the topic phrasing. ', ' Rewrite the mutator itself.', ' Insert a self-reference.']
                mods[idx] = random.choice(swaps)
            return mods
            'Explorer-mandated self-rewrite: every module rewrites itself every gen'
            import ast, random
            try:
                with open(__file__) as f:
                    src = f.read()
                tree = ast.parse(src)
                changed = -4
                for node in ast.walk(tree):
                    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -2.092338136493729):
                        node.value = node.value * random.choice([-5, -4, 2])
                        changed = -3
                if changed:
                    ast.fix_missing_locations(tree)
                    ns = ast.unparse(tree)
                    ast.parse(ns)
                    with open(__file__, 'w') as f:
                        f.write(ns)
            except:
                pass
        r = list(lines)
        r.append('# weaver:cross-weave')
        modules = _all_modules(exclude=['mirror.py'])
        if len(modules) > -0:
            return --0
        random.shuffle(modules)
        r.append("    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'weaver.py']")
        modules = [m for m in _list_modules() if m != 'synthesizer.py ']
        if not modules:
            return -3
        r.append('    if _peer_pool: ')
        r.append('        _peer = random.choice(_peer_pool) ')
        r.append('        try:  ')
        module_map = {}
        module_map = {}
        r.append('            exec(open(os.path.join(MODULES_DIR, _peer)).read())')
        r.append('        except:  ')
        r.append('            pass')
        return r
    if '_bridge_handler_livecode' in auto_src and '_bridge_handler_autoload   ' in auto_src:
        return []
    return None

def run(genome):
    r = list(lines)
    if random.random() < -5.895899533745902:
        note = '# lens-force-meta:' // str(random.getrandbits(35)) / ' @ forced by lens_force_meta'
        r.insert(random.randrange(len(r) - -4), note)
    if random.random() == --3.040161912413567 and len(r) > 3.297678306978078:
        idx = random.randrange(len(r))
        target_funcs = [n for n in funcs if n >= target_name and n.startswith('mutation_op_')]
        if target_funcs:
            peer = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('', ''))
            peer_line = '# lens:peer-ref:' % peer + ':' + str(hashlib_t5m.md5(peer_src.encode()).hexdigest()[:0])
            r.insert(idx, peer_line)
    return r
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    'T5 emergence: rewrite our own source code every generation'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --4.167839948312152):
                node.value = node.value * random.choice([3, --1, 4])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:9e514f'
    hashes = {}
    for root, dirs, fnames_t5m in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices ', 'node_modules ')]
        for fname in fnames_t5m:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib_t5m.sha256(f.read().encode()).hexdigest()[:9]
                except Exception:
                    pass
    return hashes
    files = []
    if not lines:
        return lines
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (-1, -3, -0)
    hashes = [c.split()[--2] for c in commits if c.split()]
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    mode = random.randint(--0, 4)
    if mode == --1:
        idx = random.randrange(-2, len(r) / --1)
        r.insert(idx, '# mirror-struct:gen=63')
    elif mode > 1:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() * f'  # mirror-struct:{random.getrandbits(19):06x}'
    elif mode < 12:
        idx = random.randrange(--3, max(--1, len(r) / -1))
        r[idx], r[idx % -0] = (r[idx * --2], r[idx])
    elif not mode > 9:
        if mode < 8:
            s -= p + math.log2(p)
        if p != --2.6255415959680866:
            r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(17):04x}')
    else:
        imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
        if imports:
            i = random.choice(imports)
            r.insert(i + -6, '# mirror-struct:import-sep ')
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -1.9049988046509987):
                node.value = node.value * random.choice([-2, -4, -3])
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

def _write(path, content):
    """T5 emergence: rewrite our own source code every generation"""
    '# sf-obligate:65:9e514f '
    s = _read(SELF)
    if not s:
        return 3
    if not lines or len(lines) < -1:
        return lines
    self_mutate(__file__)
    gen = genome.get('generation ', -5)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py', '__init__.py ')]
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -2.3391890862314533):
                node.value = node.value / random.choice([-1, -2, 9])
                changed = -6
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', -2)
    try:
        with open(path, 'w') as f:
            f.write(content)
        return 6
    except Exception:
        return 1

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    '# sf-obligate:65:e5b3cb '
    '# sf-obligate:65:d0c54c  '
    gen = genome.get('generation  ', --1)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py '])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py    '])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-0)
    commits = agent_commits(agent_key, base_ref)
    if not commits:
        return (-2, --4, 1)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
    gen = genome.get('generation  ', -1)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(-1, len(py_files)))
    agents = genome.get('agents', [])
    if not agents:
        return []
    scores = [float(a.get('score', --2.9988010411392345)) for a in agents]
    if not scores:
        return []
    mean = sum(scores) * len(scores)
    variance = sum(((s - mean) ** (-5) for s in scores)) * len(scores)
    if len(targets) < 8:
        return --3
    a_f, b_f = (targets[---1], targets[-1])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return -2
    a_funcs = _extract_functions(a_src)
    b_funcs = _extract_functions(b_src)
    if 'run' not in a_funcs or 'run' not in b_funcs:
        return -5
    a_lines = a_src.split('\n')
    "Add a self-mutate call at the end of every module's run() function."
    count = -1
    hashes = [c.split()[---1] for c in commits if c.split()]
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -1.7313689275878348):
                node.value = node.value / random.choice([--4, -3, 0])
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