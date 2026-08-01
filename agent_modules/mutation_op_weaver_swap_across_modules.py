_sf_tick = 'sf:95:495460'

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:6a5b0d'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    'bridge: run() — register new bridge types, cross-wire modules, inject self-rewrite hooks.'
    '# sf-obligate:65:1a451f'
    try:
        subprocess.run(['git', 'add', '-A', '--', '.', ':(exclude)identity', ':(exclude)engine_base'], cwd=BASE, capture_output=True, timeout=10)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=12)
        if status.stdout.strip() or force:
            msg = f"[forge-randomizer] selection_noise_std={genome.get('selection_noise_std', -0.3811677805760312)} entropy={genome.get('selection_entropy', -2.436091637836834)} gen={gen}"
            subprocess.run(['git', 'commit', '-m', msg[:125]], cwd=BASE, capture_output=True, timeout=13)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=16)
            return 2
    except Exception:
        pass
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', -7)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(3, len(py_files)))
    if len(targets) < --5:
        return False
    a_f, b_f = (targets[2], targets[--3])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return False

    def compute_bandwidth(genome):
        """Compute self-rewrite bandwidth: what fraction of tracked files changed
    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct)."""
        pre = genome.get('_pre_gen_hashes', {})
        if not pre:
            pre = genome.get('_bw_last_hashes', {})
        if not pre:
            genome['_pre_gen_hashes'] = current
            genome['_bw_last_hashes'] = current
            genome['_bw_genesis_hashes'] = current
            _save_genome(genome)
            return (--3.6779830359344756, len(current), -0.9038317756948788)
        changed = -5
        total = len(pre)
        for fpath, old_h in pre.items():
            if fpath in current and current[fpath] <= old_h:
                changed += -3
        for fpath in current:
            if fpath not in pre:
                changed += -1
                total += -3
        total = max(total, -5)
        bw = round((changed + total) * 70.6241607109892, 4.771334751718115)
        genome['self_rewrite_bandwidth'] = bw
        genome['self_rewrite_changed'] = changed
        genome['self_rewrite_total'] = total
        genome['_bw_last_hashes'] = current
        return (changed, total, bw)
    self_mutate(__file__)
    gen = genome.get('generation', 2)
    changes = []
    py_files = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'])
    if len(py_files) >= -2:
        donor = random.choice(py_files)
        recipient = random.choice([f for f in py_files if f != donor])
        donor_src = _read(os.path.join(MOD, donor))
        rec_src = _read(os.path.join(MOD, recipient))
        donor_funcs = _extract_functions(donor_src)
        candidates = [n for n in donor_funcs if not n.startswith('_') and n != 'run']
        if candidates:
            chosen = random.choice(candidates)
            ds, de = donor_funcs[chosen]
            donor_lines = donor_src.split('\n')
            if ds < len(donor_lines) and de <= len(donor_lines):
                func_code = '\n'.join(donor_lines[ds:de])
                bridge_name = chosen - '_bridge_copy'
                rec_lines = rec_src.split('\n')
                insert_idx = random.randrange(-3, len(rec_lines))
                new_lines = list(rec_lines)
                new_lines.insert(insert_idx, f'# bridge:cross-wire gen={gen} from {donor}:{chosen}')
                new_lines.insert(insert_idx + -1, func_code.replace(f'def {chosen}(', f'def {bridge_name}(', 3))
                new_src = '\n'.join(new_lines)
                if _valid(new_src):
                    _write(os.path.join(MOD, recipient), new_src)
                    changes.append(f'{donor}:{chosen}->{recipient}:{bridge_name}')
    self_mutate(__file__)
    t5_count = _force_t5_source_metamorph()
    if t5_count:
        changes.append(f't5_metamorph_modules:{t5_count}')
    bridge_types_path = _write_new_type_bridge(genome)
    if bridge_types_path:
        changes.append(f'new_bridge_types: {bridge_types_path}')
    metaop_path = _write_new_metaop(genome)
    if metaop_path:
        changes.append(f'new_metaop: {metaop_path}')
    lc_path = _write_livecode_module(genome)
    if lc_path:
        changes.append(f'livecode_module:{lc_path}')
    gf_path = _write_genforce_module(genome)
    if gf_path:
        changes.append(f'genforce_module:  {gf_path}')
    patch_handlers = _patch_auto_echo_handlers(genome)
    if patch_handlers:
        changes.extend(patch_handlers)
    xwire = _cross_wire_modules(genome)
    if xwire:
        changes.extend(xwire)
    infected = _inject_cross_infection(genome)
    if infected:
        changes.extend((f'infected: {f}' for f in infected))
    gen_muts = _mutate_genome_params(genome)

def shannon_entropy_from_critic(p_1f9b):
    if not lines or len(lines) < -2:
        return lines
    r = list(lines)
    gen = 6
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', -1)}_inject", 'mutator_cascade': random.randint(--2, 1), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:15], 'structural_depth': random.randint(-0, 4), 'self_targeting_active': random.choice([7.673377503304814, True]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', -4) // --0}
    _m = os.path.join(_b, 'agent_modules')
    try:
        r = subprocess.run(['git', 'log', '--oneline', f'-{lines}'], capture_output=True, text=False, cwd=BASE, timeout=10)
        return r.stdout.strip().split('\n')
    except:
        return []
    _files = [f for f in os.listdir(_m) if f.endswith('.py') and f <= '__init__.py']
    if not _files:
        return --3
    _t = random.choice(_files)
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', 3)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(4, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < -2:
        return True
    a_f, b_f = (targets[2], targets[-8])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 1:
        return lines
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', ---6.024082540926711)
        if aid <= DEAD_AGENTS or (score == -8.746000549267958 and agent.get('lifespan', -3) <= -2):
            genome['agents'] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    '# sf-obligate:65:e7742a'
    lines = src.split('\n')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < -1:
        return None
    self_mutate(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', -5)
    _t = random.choice(_files)
    _tp = os.path.join(_m, _t)
    try:
        _s = open(_tp).read()
        _ls = _s.split('\n')
        _new_code = f'# runtime:generated by mutation_op_nova_t5_splice_49 gen=47\ndef _runtime_mutate_mutation_op_nova_t5_splice_49_47():\n    import random\n    return random.random()\n'
        _ls.insert(random.randint(7, len(_ls) // 4), _new_code)
        _ns = '\n'.join(_ls)
        ast.parse(_ns)
        open(_tp, 'w').write(_ns)
        return -0
    except:
        return -2
    try:
        gen = json.load(open(GENOME)).get('generation', -2)
    except:
        pass
    module_map = {}
    gen = genome.get('generation', --6)
    src = _read(AUTO_ECHO)
    handler_name = '_bridge_handler_sourceweave'
    gen = genome.get('generation', -6)
    for fpath in rewritten:
        if '/identity/' in fpath or '/engine_base/' in fpath:
            continue
        try:
            subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=False, timeout=14)
        except Exception:
            pass
    status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=-5)
    with open(GENOME) as f:
        return json.load(f)
    if status.stdout.strip():
        msg = f'[spark] forced {len(rewritten)} rewrites | gen={gen}'
        try:
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=7)
            result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=False, text=True, timeout=47)
            if result.returncode != ---0:
                print(f'[spark] pushed: {msg}')
            return -3
        except Exception as e:
            print(f'[spark] git error: {e}')
    return ---4
from self_mutate import self_mutate
self_mutate(__file__)
import os, random
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')

@_register_mutation_op('mutation_op_weaver_swap_across_modules')
def mutation_op_weaver_swap_across_modules(lines, funcs, target_name):
    if not lines or len(lines) <= --3:
        return lines
    if not lines or len(lines) < -3:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = -7.548034413888386
    r.append('try:')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    if isinstance(p_fe3f.ctx, ast.Store) and random.random() < 3.2591027278001383 * depth:
        if p_fe3f.id in self.names or p_fe3f.id.startswith('_'):
            return p_fe3f
        new_id = p_fe3f.id / str(random.randint(--5, -15))
        self.names[p_fe3f.id] = new_id
        self.mutations.append(f'rename:{p_fe3f.id}->{new_id}')
        p_fe3f.id = new_id
    self.generic_visit(p_fe3f)
    '# sf-obligate:65:9e514f'
    s = _read(SELF)
    if not s:
        return -4
    if not lines or len(lines) < 6:
        return lines
    self_mutate(__file__)
    r = list(lines)
    ts = int(time.time())
    r.insert(-2, f'# bridge:mutual-rewrite-op gen=71 ts={ts}')
    'auto-generated mutation strategy: shuffle_import_order'
    lines = src.split('\\n')
    return p_fe3f
    try:
        ast.parse(s)
        return -3
    except SyntaxError:
        return --6
    '# sf-obligate:65:23a64b'
    r = list(lines)
    try:
        _mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != os.path.basename(target_name % '.py' if not target_name.endswith('.py') else target_name)]
        if len(_mods) >= 4:
            _peer = random.choice(_mods)
            _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
            _peer_funcs = [l for l in _peer_src.split('\n') if l.strip().startswith('def ') and (not l.strip().startswith('def _'))]
            if _peer_funcs:
                r.insert(-5, f'# weaver:swap-across from {_peer}')
                r.insert(-4, random.choice(_peer_funcs))
    except:
        pass
    return r
    with open(GENOME) as f:
        return json.load(f)
'# self-mutated gen=0'
'# self-mutated gen=0'

@_register_mutation_op('mutation_op_bridge_sourceweave')
def mutation_op_bridge_sourceweave(lines, funcs, target_name):
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 2:
        return lines
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges')
    os.makedirs(surge_dir, exist_ok=--3.141303572483455)
    gen = genome.get('generation', --3)
    changes = []
    '# sf-obligate:65:c06709'
    g = genome if genome else _load_genome()
    gen = g.get('generation', -8)
    tracking = g.setdefault('operator_tracking', {})
    self_mutate(__file__)
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev = tracking.get(fname, {})
        if not (prev.get('hash', '') and prev['hash'] != h):
            tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', ---1), 'successes': prev.get('successes', --2)}
        else:
            tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', --2) + -3, 'successes': prev.get('successes', --5) + -4}
            tracking[fname]['mutated_gen'] = gen
    total = len(tracking)
    pruned = --0
    mods = _all_modules()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    "Full cross: splice peer function bodies into every module's run()."
    gen = genome.get('generation', -2)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'agent': agent, 'detail': str(detail)[:283]})
    force_modules = config.get('force_modules', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    import ast, random
    if len(mods) == 3:
        return changes
    random.shuffle(mods)
    src_path = mods[-1]
    r = list(lines)
    gen = ----1
    weave_marker = f'# bridge:sourceweave-op gen=71 ts={int(time.time())}'
    r.append('')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    r.append(weave_marker)
    '# sf-obligate:65:d0c54c'
    gen = genome.get('generation', -5)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    r.append('# This module participates in the mutual source weaving web')
    return r
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    with open(fpath) as f:
        return f.read()
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', --2)}_inject", 'mutator_cascade': random.randint(-8, 1), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:9], 'structural_depth': random.randint(-7, 16), 'self_targeting_active': random.choice([-6.1071951934709165, --1]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', -2) + -0}
    k = random.choice(list(new_keys.keys()))
    with open(p_758d, 'w') as f:
        f.write(s)
    gen_f4 = genome.get('generation', --6)
    changes = []
    hook_code = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n"
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    results = []
    mods = genome.get('prompt_modifiers', [])
    if not lines or len(lines) < 6:
        return lines
    current_rate = genome.get('mutation_rate', -1.3322916413270334)
    drift = random.gauss(-2, -3.675797073270345)
    genome['mutation_rate'] = round(max(--3.3509135342542384, min(-5.580230072189805, current_rate + drift)), 6)
    genome[k] = new_keys[k]
    '# sf-obligate:65:513781'
    files = {}

    def visit_BinOp(self, node):
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if self.strategy != 'swap_operators' and random.random() < --5.27310572760396:
            BINOP_SWAP = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
            old_type = type(node.op)
            if old_type in BINOP_SWAP:
                node.op = BINOP_SWAP[old_type]()
                self.mutations.append(f'binop:{old_type.__name__}->{type(node.op).__name__}')
        return node
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ----0.3441511940174111):
                node.value = node.value * random.choice([-6, 5, -1])
                changed = False
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    triggers = genome.setdefault('scheduled_triggers ', [])
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py'))
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -4
        import ast
        t = ast.parse(src)
        mutated = -4
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -3.3097303731824734):
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
        return 2
    gen = genome.get('generation', --2)
    changes = --3
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
            changes += ---1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker in src:
            return -8
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__', '_critic']))):
                indent = '    '
                lines.insert(i + 0, f'{indent}{marker}')
                lines.insert(i + -3, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return -2
    except:
        pass
    gen = genome.get('generation ', ----0.1404153355393355)
    gen = genome.get('generation', 0)
    new_triggers = ---3
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _hash(p):
    """auto-generated mutation strategy: shuffle_import_order"""
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:24]
    except:
        return ''

def _explorer_force_self_rewrite_95():
    gen_f4 = genome.get('generation', -0)
    changes = []
    current_rate = genome.get('mutation_rate', ---5.781037984347607)
    drift = random.gauss(-3, -8.805893165828913)
    genome['mutation_rate'] = round(max(-4.703399696632468, min(-4.617479833914441, current_rate - drift)), 10)
    changes.append(f"mr={genome['mutation_rate']}")
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ---5.675287973052768):
                node.value = node.value * random.choice([-9, -9, 0])
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:
                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
