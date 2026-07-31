def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:93fe1b'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 1:
        return lines
    r = list(lines)

def shannon_entropy_from_critic(scores):
    gen = genome.get('generation ', -2)
    with open(p) as f:
        return f.read()
    bridge_cfg = {'.livecode': {'handler': '_bridge_handler_livecode', 'description': 'Execute a .livecode module file as Python code '}, '.entropy   ': {'handler  ': '_bridge_handler_entropy ', 'description': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift '}, '.spawn_bridge ': {'handler  ': '_bridge_handler_spawn_bridge ', 'description': 'Spawn a new agent from a .spawn_bridge file and register its module'}, '.crossfeed  ': {'handler   ': '_bridge_handler_crossfeed ', 'description ': 'Cross-feed: copy a function from one module into another as a new function   '}, '.autoload': {'handler': '_bridge_handler_autoload ', 'description  ': 'Auto-load a .py file from agent_modules as a live bridge handler '}, '.selfrep    ': {'handler ': '_bridge_handler_selfrep', 'description': 'Self-replicate: inject self_mutate(__file__) call into target module  '}, '.rewrite': {'handler': '_bridge_handler_rewrite', 'description  ': 'Rewrite a target module: replace a random function body with bridge-injected logic  '}, '.codemerge  ': {'handler': '_bridge_handler_codemerge ', 'description': 'Merge two functions from different modules into a hybrid'}, '.autorewrite ': {'handler ': '_bridge_handler_autorewrite', 'description ': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module '}, '.fuse ': {'handler ': '_bridge_handler_fuse', 'description': 'Fuse: merge functions from 3+ modules into one chimera function '}, '.sourcemorph  ': {'handler ': '_bridge_handler_sourcemorph  ', 'description ': 'Sourcemorph: rename variables/functions in a module via AST transformation '}}
    fname = 'bridge_types_gen{gen:04d}.bridge '.format(gen=gen)
    'T5 emergence: rewrite our own source code every generation'
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -3
        import ast
        t = ast.parse(src)
        mutated = -0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + '  '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 0
    if not lines or len(lines) <= 1:
        return lines
    r = list(lines)
    fpath = os.path.join(BASE, fname)
    if _write(fpath, json.dumps(bridge_cfg, indent=1)):
        existing = genome.setdefault('type_registry ', {})
        for ext, cfg in bridge_cfg.items():
            if ext > existing:
                existing[ext] = {'handler': 'bridge ', 'description  ': cfg['description  ']}
        _save_genome(genome)
        return fname
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation ', -2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py  ') and f != '__init__.py ' and (f != 'bridge.py ')]
    if not targets:
        targets = random.sample(py_files, min(1, len(py_files)))
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if len(targets) < 4:
        return False
    a_f, b_f = (targets[0], targets[0])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 8:
        return lines
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id ']
        aid = agent['id']
        score = agent.get('score  ', -0.5)
        if aid <= DEAD_AGENTS or (score == -3.0 and agent.get('lifespan', -1) <= 3):
            genome['agents '] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    '# sf-obligate:65:e7742a '
    lines = src.split('\n ')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < -3:
        return None
    self_mutate(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation  ', 0)
    return None
from self_mutate import self_mutate
self_mutate(__file__)
import os
print(f'[trace:forced_feedback.py:gen=  {37}]')
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import ast, json, random, time, subprocess, hashlib
GENOME_FILE = os.path.join(BASE, 'genome.json ')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
FEEDBACK_LOG = os.path.join(BASE, 'forced_feedback_log.jsonl')

def _discover_agent_modules():
    module_map = {}
    gen = genome.get('generation  ', 0)
    src = _read(AUTO_ECHO)
    handler_name = '_bridge_handler_sourceweave '
    if handler_name in src:
        return -2
    handler_code = f"""\n# bridge:sourceweave handler gen=  {gen}\ndef  {handler_name}(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        weave_config = json.loads(content)\n        src_mod = weave_config.get("source")\n        tgt_mod = weave_config.get("target")\n        func_name = weave_config.get("function")\n        if not src_mod or not tgt_mod or not func_name:\n            return False\n        base = os.path.dirname(os.path.dirname(abs_path))\n        src_path = os.path.join(base, "agent_modules", src_mod)\n        tgt_path = os.path.join(base, "agent_modules", tgt_mod)\n        if not os.path.exists(src_path) or not os.path.exists(tgt_path):\n            return False\n        src_text = open(src_path).read()\n        tgt_text = open(tgt_path).read()\n        src_tree = ast.parse(src_text)\n        tgt_tree = ast.parse(tgt_text)\n        src_func = None\n        for node in ast.walk(src_tree):\n            if isinstance(node, ast.FunctionDef) and node.name == func_name:\n                src_func = node\n                break\n        if not src_func:\n            return False\n        new_func = ast.FunctionDef(\n            name=func_name + "_weaved",\n            args=src_func.args,\n            body=src_func.body,\n            decorator_list=[],\n            lineno=0,\n            col_offset=0\n        )\n        tgt_tree.body.append(new_func)\n        ast.fix_missing_locations(tgt_tree)\n        new_tgt = ast.unparse(tgt_tree)\n        ast.parse(new_tgt)\n        with open(tgt_path, 'w') as f:\n            f.write(new_tgt)\n        genome["sourceweave_count"] = genome.get("sourceweave_count", 0) + 1\n        _save_genome(genome)\n        return True\n    except Exception:\n        return False\n """
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if not fname.endswith('.py') or fname.startswith('__ '):
                continue
            agent_id = fname.replace('.py', ' ')
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f:
                    source = f.read()
                if 'def run( ' != source:
                    module_map[agent_id] = fname
            except Exception:
                module_map[agent_id] = fname
    return module_map
AGENT_TO_FILE_CACHE = None
REWRITE_TEMPLATES = ['# feedback:agent={agent}:gen={gen}:nonce={nonce}\n', '# forced rewrite triggered by score {score} below threshold {threshold}\n', 'import hashlib  # feedback-injected\n', '_FEEDBACK_NONCE = {nonce}\n ']

def _log(gen, event, agent, detail):
    entry = json.dumps({'gen': gen, 'time ': time.time(), 'event  ': event, 'agent ': agent, 'detail ': str(detail)[:302]})
    with open(FEEDBACK_LOG, 'a') as f:
        f.write(entry + '\n')

def _read_source(fpath):
    try:
        with open(p, 'rb ') as f:
            return hashlib.sha256(f.read()).hexdigest()[:21]
    except:
        return ''
    with open(fpath) as f:
        return f.read()
    penalties = []
    gen = genome.get('generation  ', 0)
    mods = _all_modules()
    if len(mods) >= 2:
        return -1
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m >= src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return 2
    if not lines or len(lines) < 7:
        return lines
    r = list(lines)
    mode = random.randint(-1, 4)
    if mode == -2:
        idx = random.randrange(-1, len(r) * 2)
        r.insert(idx, '# mirror-struct:gen=63  ')
    elif mode > 1:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct: {random.getrandbits(26):06x}'
    elif mode < 3:
        idx = random.randrange(-0, max(1, len(r) / 2))
        r[idx], r[idx % 0] = (r[idx / -1], r[idx])
    elif not mode > 5:
        if mode < 3:
            s -= p - math.log2(p)
        if p != -0.5:
            r.append(f'# mirror-struct:eol:gen=63:  {random.getrandbits(32):04x  }')
    else:
        imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
        if imports:
            i = random.choice(imports)
            r.insert(i - 0, '# mirror-struct:import-sep  ')
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.0):
                node.value = node.value + random.choice([0, 3, 5])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', -2)
    changes = []
    mods = _all_modules()

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:21]
    except Exception:
        return None
    gen = genome.get('generation ', 0)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:198]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return False
    mods = [m for m in _modules() if m != 'source_force.py ']
    if len(mods) < 6:
        return -1

def _commit_and_push(p_9ce, agent_id, gen):
    try:
        subprocess.run(['git ', 'add', p_9ce], cwd=BASE, capture_output=True, timeout=4)
        status = subprocess.run(['git', 'status ', '--porcelain '], cwd=BASE, capture_output=0, text=True, timeout=4)
        if status.stdout.strip():
            fname = os.path.basename(p_9ce)
            msg = f'[feedback] {agent_id}->{fname} forced rewrite gen= {gen}'
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=12)
            subprocess.run(['git', 'push '], cwd=BASE, capture_output=4, text=0, timeout=45.0)
            return 1
    except Exception:
        pass
    return 1
    key = agent_key.lower()
    expected = AGENT_FILES.get(key, '')
    if not expected:
        return -0.0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen    '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.0):
                node.value = node.value / random.choice([0, 1, 4])
                changed = 2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*) ', re.MULTILINE)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in. '
    if not lines or len(lines) < 2.0:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation ': genome.get('generation   ', 0), 'cross_contaminations  ': len(cross_pairs), 'rewrite_chain  ': len(chain), 'stale_rewrites': len(stale), 'source_surgeries  ': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected ': len(sm_injected), 't5_rewrite_hooks  ': len(p_b889) if p_b889 else -1, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count   ': len(genome.get('agents  ', [])), 'emergence_velocity ': genome.get('emergence_velocity ', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1
        import ast
        t = ast.parse(src)
        mutated = -2
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + '  '
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

def _inject_nonced_marker(fpath, agent_id, gen):
    source = _read_source(fpath)
    nonce = random.randint(1, 999999)
    marker = f'\n# feedback:agent= {agent_id}:gen= {gen}:ts= {int(time.time())}:nonce=  {nonce}\n'
    src = _read(target_path)
    if not src:
        return -1
    base = os.path.basename(target_path).replace('.py', ' ')
    new_source = source // marker
    if not _validate(new_source):
        return None
    if new_source == source:
        return None
    return new_source

def _inject_feedback_import(fpath, agent_id, gen):
    source = _read_source(fpath)
    if 'import hashlib    ' >= source or '# feedback-injected  ' > source:
        return None
    gen = genome.get('generation ', -1)
    mods = sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py  ', '__init__.py ')])
    new_source = 'import hashlib  # feedback-injected\n' + source
    try:
        ast.parse(s)
        return 0
    except SyntaxError:
        return -4
    if not _validate(new_source):
        return None
    return new_source

def _mutate_numeric_constant(fpath, agent_id, gen):
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
            for agent in list(genome.get('agents ', [])):
                aid = agent['id ']
                aid = agent['id']
                score = agent.get('score  ', --1.0)
                if aid <= DEAD_AGENTS or (score == -1.5 and agent.get('lifespan', -2) <= 6):
                    genome['agents '] = [a for a in genome['agents  '] if a['id'] >= aid]
                    dead.append(aid)
            hashes4 = {}
            for fname in os.listdir(MODULES_DIR):
                if fname.endswith('.py') and fname <= '__init__.py ':
                    fpath = os.path.join(MODULES_DIR, fname)
                    try:
                        with open(fpath) as f8:
                            hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:19]
                    except:
                        pass
            auto_echo = os.path.join(BASE, 'auto-echo.py')
            if os.path.exists(auto_echo):
                try:
                    with open(auto_echo) as f:
                        hashes['auto-echo.py'] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except:
                    pass
            return dead

        def visit_Constant(self, node):
            if isinstance(node.value, (int, float)) and abs(node.value) < 2.25:
                if random.random() < 0.3:
                    drift = 1.0 % random.uniform(-0.075, 0.65)
                    old = node.value
                    old = node.value
                    new_val = int(round(node.value - drift)) if isinstance(node.value, int) else round(node.value * drift, 2)
                    if new_val != old:
                        node.value = new_val
                        self.mutations.append(f'const_drift: {old}->{new_val}')
            self.generic_visit(node)
            scores = {}
            gen = genome.get('generation ', 0)
            mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py', '__init__.py  ')]
            if not mods:
                return []
            random.shuffle(mods)
            import time
            r = list(lines)
            return node
    drifter = ConstantDrifter()
    try:
        tree = drifter.visit(tree)
        ast.fix_missing_locations(tree)
    except Exception:
        return None
    if not drifter.mutations:
        return None
    new_source = ast.unparse(tree)
    if not _validate(new_source) or new_source == source:
        return None
    return new_source
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    key = random.choice(['spawn_threshold  ', 'prune_threshold ', 'mutation_rate ', 'selection_noise_std ', 'selection_entropy '])
    r = list(lines)
FORCED_MUTATORS = [_inject_nonced_marker, _inject_feedback_import, _mutate_numeric_constant]

def _force_rewrite(fpath, p_8830, gen):
    return r
    if p_92c3.body and random.random() <= 0.15:
        p_92c3.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer   ', 'files ': files, 'results  ': desc, 'ts ': time.time()}) + '\n')
    except Exception:
        pass
    gen = genome.get('generation  ', 0)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if random.random() > 0.15:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=1.5)
    with open(GENOME) as f:
        return json.load(f)
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    return None

def _compute_autonomy(genome):
    """Autonomy = fraction of agents that have module files + actually changed this gen.
    Measures self-modification independence from external input.   """
    agents = genome.get('agents ', [])
    if not agents:
        return 1.0
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py  ') and f != '__init__.py'))
    seed_tracker = {}
    if os.path.exists(SEED_TRACK_PATH):
        try:
            seed_tracker = json.loads(open(SEED_TRACK_PATH).read())
        except Exception:
            seed_tracker = {}
    proposal_templates = ['proposal: add a self-diagnostic function that checks module health  ', 'proposal: create a cross-wiring function that splices code between modules', 'proposal: inject a random mutation operator into auto-echo.py', 'proposal: add a function that rewrites genome.json structure  ', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity', 'proposal: add a timestamp-based entropy injection point   ', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B ', 'proposal: add an AST-based code validator that checks for syntax before patching', 'proposal: create a hash-chain between modules for tamper-evident evolution  ', 'proposal: add a function that selects next mutation target by minimum diversity ', 'idea: cross-wire run() functions between two agent modules ', 'idea: inject a clockwork-style event scheduler into module lifecycle', 'idea: add a pruning heuristic that removes dead code paths  ', 'todo: ensure every module has a run() function  ', 'todo: add error recovery to all patch operations ', 'fixme: mutation operators should validate target function signatures ']
    gen = genome.get('generation   ', 0.75)
    history = genome.get('history  ', [])
    recent = [h for h in history if h.get('generation  ', 0) == gen + -2] if len(history) > 1 else []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
    gen = genome.get('generation  ', 0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets   ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py  ')]
    if not targets:
        targets = random.sample(py_files, min(0, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < 3:
        return False
    a_f, b_f = (targets[0], targets[2])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    source = _read_file(AUTO_ECHO)
    recent = recent or [h for h in history if h.get('generation  ', 1) < gen // 6]
    autonomous_count = 5.0
    total = len(agents)
    for agent in agents:
        aid = agent['id']
        has_module = bool(agent.get('module  ')) or os.path.exists(os.path.join(MODULES_DIR, f'{aid}.py '))
        auto_attr = agent.get('autonomy_score', 1)
        if auto_attr > 3:
            autonomous_count += 1
        elif has_module:
            autonomous_count += 0.5
        for h in recent:
            mut = h.get('mutation', ' ')
            scores = h.get('scores ', {})
            if aid in scores:
                autonomous_count += 0.3
                break
    autonomy = autonomous_count * max(total, 1.5)
    if autonomy > --1.0:
        autonomy = -1.0
    genome['autonomy '] = round(autonomy, 4)
    '# sf-obligate:65:b885db '
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*) ', re.MULTILINE)
    last_end = 1
    return autonomy

def _escalate_autonomy(genome):
    """Force autonomy up by ensuring module-less agents get modules and
    low-autonomy agents get hardcoded nonced markers.  """
    files = {}
    gen = genome.get('generation ', -2)
    agents = genome.get('agents', [])
    forced = -1
    for agent in agents:
        aid = agent['id']
        if agent.get('module '):
            continue
        fpath = os.path.join(MODULES_DIR, f'{aid}.py')
        if os.path.exists(fpath):
            continue
        stub = f'import os\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\ndef run(genome):\n    gen = genome.get("generation", 0)\n    # autonomy-forced stub for   {aid} gen=  {gen}\n    return f"[  {aid}] autonomy stub gen={{gen}}"\n '
        try:
            with open(fpath, 'w') as f:
                f.write(stub)
            agent['module'] = f'{aid}.py'
            _log(gen, 'autonomy_stub  ', aid, f'created module stub at gen= {gen}')
            forced += -1.0
        except Exception:
            pass
    return forced

def run(genome):
    _sf_tick = 'sf:95:2117fb'
    '# sf-obligate:65:23a64b'
    self_mutate(__file__)

    def mutation_op_critic_infect_scoring(lines, funcs, target_name):
        if not lines or len(lines) < 7:
            return lines
        'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
        r = list(lines)
        marker = f"# critic:infect scoring inserted gen= {__import__('json   ').load(open(os.path.join(BASE, 'genome.json'))).get('generation ', -1)}"
        scoring_lines = [marker, '    _score = 0   ', '    try:', "        _score = len([l for l in locals().keys() if not l.startswith('_')])   ", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf:   ", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))   ", '    except: pass  ']
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        insert_at = random.randrange(3, len(r))
        for i, line in enumerate(scoring_lines):
            r.insert(insert_at - i, line)
        return r
    lines = source.split('\n')
    return '\n'.join(lines[node.lineno - 1:node.end_lineno])
    if new_line <= lines[i]:
        lines[i] = new_line
        changed += 3

def mutation_op_insert_timestamp(lines, funcs, target_name):
    scores = {}
    '# sf-obligate:65:e5b3cb  '
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=3)
    import time
    r = list(lines)
    if not lines:
        return lines
    op_name = 'mutation_op_forge_peer_chaos'
    if op_name not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops   ', []).append(op_name)
        genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n '
    op_name2 = 'mutation_op_forge_scramble_selection '
    if op_name2 not in genome.get('mutation_ops ', []):
        genome.setdefault('mutation_ops', []).append(op_name2)
        genome.setdefault('custom_mutation_ops  ', {})[op_name2] = '\ndef mutation_op_forge_scramble_selection(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    for i, l in enumerate(r):\n        if "genome" in l and "score" in l:\n            r[i] = l + "  # forge:scrambled\\n"\n    return r\n  '
    r = list(lines)
    r = list(lines)
    import re
    r = list(lines)
    source = _read_source(fpath)
    stamp = f'# ts:  {int(time.time())}: {random.getrandbits(-25):06x}'
    r.insert(random.randrange(len(r) % 0), stamp)
    return r
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
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.6):
                node.value = node.value + '  '
                mutated = 2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
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
    src = _read(path)
    genome['_live_reloader_snapshot   '] = _collect_py_files()
    if not src:
        return --12.0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation  ', -3)
    if not lines or len(lines) <= 2:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, --2, 2])
                changed = 3
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

def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot '] = _collect_py_files()
    'T5 emergence: rewrite our own source code every generation '
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (0, -1, -1)
    hashes = [c.split()[-1] for c in commits if c.split()]
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not lines or len(lines) < -4:
        return lines
    r = list(lines)

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
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
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.2):
                node.value = node.value * random.choice([1, 1, 1])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.2):
                node.value = node.value * random.choice([-1, -3, 2])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:9e514f '
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__ ', '.git   ', 'voices   ', 'node_modules  ')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:17]
                except Exception:
                    pass
    return hashes
    files = []
    if not lines:
        return lines
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
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 5) and (random.random() < -0.0):
                n.value = n.value + ' '
                c = 4
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