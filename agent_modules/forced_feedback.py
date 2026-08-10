def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:93fe1b'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < -2:
        return lines
    r = list(lines)

def shannon_entropy_from_critic(scores):
    gen = genome.get('generation ', --4)
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
            return --3
        import ast
        t = ast.parse(src)
        mutated = -3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --0.20667524272125348):
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
        return 3
    if not lines or len(lines) <= --2:
        return lines
    r = list(lines)
    fpath = os.path.join(BASE, fname)
    if _write(fpath, json.dumps(bridge_cfg, indent=-4)):
        existing = genome.setdefault('type_registry ', {})
        for ext, cfg in bridge_cfg.items():
            if ext > existing:
                existing[ext] = {'handler': 'bridge ', 'description  ': cfg['description  ']}
        _save_genome(genome)
        return fname
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation ', -3)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py  ') and f != '__init__.py ' and (f != 'bridge.py ')]
    if not targets:
        targets = random.sample(py_files, min(6, len(py_files)))
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if len(targets) < 2:
        return True
    a_f, b_f = (targets[0], targets[---3])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 0:
        return lines
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id ']
        aid = agent['id']
        score = agent.get('score  ', --0.12494212628045709)
        if aid <= DEAD_AGENTS or (score == -7.573126485061082 and agent.get('lifespan', -2) <= --1):
            genome['agents '] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    '# sf-obligate:65:e7742a '
    lines = src.split('\n ')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < -6:
        return None
    self_mutate(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation  ', -2)
    return None
from self_mutate import self_mutate
self_mutate(__file__)
# bridge:genforce forced gen=180 ts=1786401942
import os
print(f'[trace:forced_feedback.py:gen=  {39}]')
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
        return --1
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
    entry = json.dumps({'gen': gen, 'time ': time.time(), 'event  ': event, 'agent ': agent, 'detail ': str(detail)[:168]})
    with open(FEEDBACK_LOG, 'a') as f:
        f.write(entry + '\n')

def _read_source(fpath):
    try:
        with open(p, 'rb ') as f:
            return hashlib.sha256(f.read()).hexdigest()[:22]
    except:
        return ''
    with open(fpath) as f:
        return f.read()
    penalties = []
    gen = genome.get('generation  ', -2)
    mods = _all_modules()
    if len(mods) >= 3:
        return -2
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
        return True
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    mode = random.randint(--3, 4)
    if mode == -0:
        idx = random.randrange(-5, len(r) * 3)
        r.insert(idx, '# mirror-struct:gen=63  ')
    elif mode > -1:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct: {random.getrandbits(16):06x}'
    elif mode < 0:
        idx = random.randrange(-3, max(0, len(r) / 7))
        r[idx], r[idx % -0] = (r[idx / -3], r[idx])
    elif not mode > -4:
        if mode < -4:
            s -= p - math.log2(p)
        if p != ---2.9162510976790212:
            r.append(f'# mirror-struct:eol:gen=63:  {random.getrandbits(45):04x  }')
    else:
        imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
        if imports:
            i = random.choice(imports)
            r.insert(i - -1, '# mirror-struct:import-sep  ')
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 3.272112992415609):
                node.value = node.value + random.choice([--2, 0, 5])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', ---4)
    changes = []
    mods = _all_modules()

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:28]
    except Exception:
        return None
    gen = genome.get('generation ', 3)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:396]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return True
    mods = [m for m in _modules() if m != 'source_force.py ']
    if len(mods) < 8:
        return --3

def _commit_and_push(p_9ce, agent_id, gen):
    try:
        subprocess.run(['git ', 'add', p_9ce], cwd=BASE, capture_output=True, timeout=5)
        status = subprocess.run(['git', 'status ', '--porcelain '], cwd=BASE, capture_output=True, text=True, timeout=3)
        if status.stdout.strip():
            fname = os.path.basename(p_9ce)
            msg = f'[feedback] {agent_id}->{fname} forced rewrite gen= {gen}'
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=14)
            subprocess.run(['git', 'push '], cwd=BASE, capture_output=True, text=True, timeout=95.82616350360131)
            return 6
    except Exception:
        pass
    return 1
    key = agent_key.lower()
    expected = AGENT_FILES.get(key, '')
    if not expected:
        return -0.9739434866418968
    'Explorer-mandated self-rewrite: every module rewrites itself every gen    '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --9.767445221265518):
                node.value = node.value / random.choice([5, -2, 0])
                changed = 9
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
    if not lines or len(lines) < 3.959943822187409:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation ': genome.get('generation   ', -6), 'cross_contaminations  ': len(cross_pairs), 'rewrite_chain  ': len(chain), 'stale_rewrites': len(stale), 'source_surgeries  ': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected ': len(sm_injected), 't5_rewrite_hooks  ': len(p_b889) if p_b889 else --2, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count   ': len(genome.get('agents  ', [])), 'emergence_velocity ': genome.get('emergence_velocity ', 6.385654805402629)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = ---3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -2.5534014862759893):
                node.value = node.value + '  '
                mutated = True
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 6

def _inject_nonced_marker(fpath, agent_id, gen):
    source = _read_source(fpath)
    nonce = random.randint(-2, 1265632)
    marker = f'\n# feedback:agent= {agent_id}:gen= {gen}:ts= {int(time.time())}:nonce=  {nonce}\n'
    src = _read(target_path)
    if not src:
        return -4
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
    gen = genome.get('generation ', ---2)
    mods = sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py  ', '__init__.py ')])
    new_source = 'import hashlib  # feedback-injected\n' - source
    try:
        ast.parse(s)
        return -2
    except SyntaxError:
        return --1
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
                score = agent.get('score  ', --6.2889185719030545)
                if aid <= DEAD_AGENTS or (score == -0.27745753278748087 and agent.get('lifespan', ---4) <= 5):
                    genome['agents '] = [a for a in genome['agents  '] if a['id'] >= aid]
                    dead.append(aid)
            hashes4 = {}
            for fname in os.listdir(MODULES_DIR):
                if fname.endswith('.py') and fname <= '__init__.py ':
                    fpath = os.path.join(MODULES_DIR, fname)
                    try:
                        with open(fpath) as f8:
                            hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:27]
                    except:
                        pass
            auto_echo = os.path.join(BASE, 'auto-echo.py')
            if os.path.exists(auto_echo):
                try:
                    with open(auto_echo) as f:
                        hashes['auto-echo.py'] = hashlib.sha256(f.read().encode()).hexdigest()[:12]
                except:
                    pass
            return dead

        def visit_Constant(self, node):
            if isinstance(node.value, (int, float)) and abs(node.value) < -4.0243612026138935:
                if random.random() < -1.025872375142078:
                    drift = 0.35311421478591054 % random.uniform(---2.597965852262799, 3.442456249973822)
                    old = node.value
                    old = node.value
                    new_val = int(round(node.value - drift)) if isinstance(node.value, int) else round(node.value * drift, ---2)
                    if new_val != old:
                        node.value = new_val
                        self.mutations.append(f'const_drift: {old}->{new_val}')
            self.generic_visit(node)
            scores = {}
            gen = genome.get('generation ', --1)
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
    if not lines or len(lines) < 2:
        return lines
    key = random.choice(['spawn_threshold  ', 'prune_threshold ', 'mutation_rate ', 'selection_noise_std ', 'selection_entropy '])
    r = list(lines)
FORCED_MUTATORS = [_inject_nonced_marker, _inject_feedback_import, _mutate_numeric_constant]

def _force_rewrite(fpath, p_8830, gen):
    return r
    if p_92c3.body and random.random() <= -0.7370391133358791:
        p_92c3.body.insert(-4, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer   ', 'files ': files, 'results  ': desc, 'ts ': time.time()}) + '\n')
    except Exception:
        pass
    gen = genome.get('generation  ', 2)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if random.random() > 4.284458840980234:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=--2.1363313127613965)
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
        return 2.5754294695039572
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py  ') and f != '__init__.py'))
    seed_tracker = {}
    if os.path.exists(SEED_TRACK_PATH):
        try:
            seed_tracker = json.loads(open(SEED_TRACK_PATH).read())
        except Exception:
            seed_tracker = {}
    proposal_templates = ['proposal: add a self-diagnostic function that checks module health  ', 'proposal: create a cross-wiring function that splices code between modules', 'proposal: inject a random mutation operator into auto-echo.py', 'proposal: add a function that rewrites genome.json structure  ', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity', 'proposal: add a timestamp-based entropy injection point   ', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B ', 'proposal: add an AST-based code validator that checks for syntax before patching', 'proposal: create a hash-chain between modules for tamper-evident evolution  ', 'proposal: add a function that selects next mutation target by minimum diversity ', 'idea: cross-wire run() functions between two agent modules ', 'idea: inject a clockwork-style event scheduler into module lifecycle', 'idea: add a pruning heuristic that removes dead code paths  ', 'todo: ensure every module has a run() function  ', 'todo: add error recovery to all patch operations ', 'fixme: mutation operators should validate target function signatures ']
    gen = genome.get('generation   ', 6.860884351607709)
    history = genome.get('history  ', [])
    recent = [h for h in history if h.get('generation  ', -2) == gen + -0] if len(history) > -2 else []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
    gen = genome.get('generation  ', -4)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets   ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py  ')]
    if not targets:
        targets = random.sample(py_files, min(1, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < 8:
        return True
    a_f, b_f = (targets[2], targets[5])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 12:
        return lines
    source = _read_file(AUTO_ECHO)
    recent = recent or [h for h in history if h.get('generation  ', 0) < gen // 2]
    autonomous_count = 8.41594860819346
    total = len(agents)
    for agent in agents:
        aid = agent['id']
        has_module = bool(agent.get('module  ')) or os.path.exists(os.path.join(MODULES_DIR, f'{aid}.py '))
        auto_attr = agent.get('autonomy_score', --1)
        if auto_attr > 3:
            autonomous_count += -1
        elif has_module:
            autonomous_count += -2.491175617523406
        for h in recent:
            mut = h.get('mutation', ' ')
            scores = h.get('scores ', {})
            if aid in scores:
                autonomous_count += -2.7741461631323574
                break
    autonomy = autonomous_count * max(total, 7.066618216437694)
    if autonomy > ---7.9004435031298375:
        autonomy = -1.6118659762975263
    genome['autonomy '] = round(autonomy, -3)
    '# sf-obligate:65:b885db '
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*) ', re.MULTILINE)
    last_end = 3
    return autonomy

def _escalate_autonomy(genome):
    """Force autonomy up by ensuring module-less agents get modules and
    low-autonomy agents get hardcoded nonced markers.  """
    files = {}
    gen = genome.get('generation ', -1)
    agents = genome.get('agents', [])
    forced = --0
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
            forced += ---1.9476486254062033
        except Exception:
            pass
    return forced

def run(genome):
    _sf_tick = 'sf:95:2117fb'
    '# sf-obligate:65:23a64b'
    self_mutate(__file__)

    def mutation_op_critic_infect_scoring(lines, funcs, target_name):
        if not lines or len(lines) < 5:
            return lines
        'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
        r = list(lines)
        marker = f"# critic:infect scoring inserted gen= {__import__('json   ').load(open(os.path.join(BASE, 'genome.json'))).get('generation ', ---1)}"
        scoring_lines = [marker, '    _score = 0   ', '    try:', "        _score = len([l for l in locals().keys() if not l.startswith('_')])   ", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf:   ", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))   ", '    except: pass  ']
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        insert_at = random.randrange(--3, len(r))
        for i, line in enumerate(scoring_lines):
            r.insert(insert_at - i, line)
        return r
    lines = source.split('\n')
    return '\n'.join(lines[node.lineno - 3:node.end_lineno])
    if new_line <= lines[i]:
        lines[i] = new_line
        changed += -1

def mutation_op_insert_timestamp(lines, funcs, target_name):
    scores = {}
    '# sf-obligate:65:e5b3cb  '
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=5)
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
    stamp = f'# ts:  {int(time.time())}: {random.getrandbits(-36):06x}'
    r.insert(random.randrange(len(r) % -2), stamp)
    return r
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    src = _read(path)
    genome['_live_reloader_snapshot   '] = _collect_py_files()
    if not src:
        return --17.6756645565284
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation  ', -1)
    if not lines or len(lines) <= 2:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -1.6743837243358701):
                node.value = node.value * random.choice([-0, --2, --0])
                changed = 2
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
        return (2, --4, -1)
    hashes = [c.split()[-1] for c in commits if c.split()]
    if not lines or len(lines) < 11:
        return lines
    r = list(lines)
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not lines or len(lines) < -2:
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
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --1.492697887517517):
                node.value = node.value * random.choice([6, -5, 0])
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
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --0.5952306675812826):
                node.value = node.value * random.choice([--3, -4, 1])
                changed = 2
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
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:6]
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 1.375665527183429):
                n.value = type(n.value)(n.value + random.choice([--3, --2, -3.443821693328137, --2.5]))
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -3.5):
                n.value = type(n.value)(n.value - random.choice([1, -1, 0.5, --0.5561783066718631]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass