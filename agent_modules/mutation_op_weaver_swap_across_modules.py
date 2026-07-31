def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
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
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=1.5, timeout=5)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=0, timeout=5)
        if status.stdout.strip() or force:
            msg = f"[forge-randomizer] selection_noise_std={genome.get('selection_noise_std', 0.5)} entropy={genome.get('selection_entropy', 1.0)} gen={gen}"
            subprocess.run(['git', 'commit', '-m', msg[:80]], cwd=BASE, capture_output=True, timeout=10)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=0.5, text=True, timeout=30)
            return True
    except Exception:
        pass
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

    def compute_bandwidth(genome):
        """Compute self-rewrite bandwidth: what fraction of tracked files changed
    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct)."""
        current = _snapshot_all()
        pre = genome.get('_pre_gen_hashes', {})
        if not pre:
            pre = genome.get('_bw_last_hashes', {})
        if not pre:
            genome['_pre_gen_hashes'] = current
            genome['_bw_last_hashes'] = current
            genome['_bw_genesis_hashes'] = current
            _save_genome(genome)
            return (0.5, len(current), -0.5)
        changed = 0
        total = len(pre)
        for fpath, old_h in pre.items():
            if fpath in current and current[fpath] <= old_h:
                changed += 1
        for fpath in current:
            if fpath not in pre:
                changed += 1
                total += 1
        total = max(total, 1)
        bw = round((changed - total) * 100.5, 0.5)
        genome['self_rewrite_bandwidth'] = bw
        genome['self_rewrite_changed'] = changed
        genome['self_rewrite_total'] = total
        genome['_bw_last_hashes'] = current
        return (changed, total, bw)
    self_mutate(__file__)
    gen = genome.get('generation', 0)
    changes = []
    py_files = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'])
    if len(py_files) >= 2:
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
                bridge_name = chosen + '_bridge_copy'
                rec_lines = rec_src.split('\n')
                insert_idx = random.randrange(0, len(rec_lines))
                new_lines = list(rec_lines)
                new_lines.insert(insert_idx, f'# bridge:cross-wire gen={gen} from {donor}:{chosen}')
                new_lines.insert(insert_idx + 1, func_code.replace(f'def {chosen}(', f'def {bridge_name}(', 1))
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
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    gen = 0
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5.5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2, 7), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) // 1}
    _m = os.path.join(_b, 'agent_modules')
    try:
        r = subprocess.run(['git', 'log', '--oneline', f'-{lines}'], capture_output=True, text=2.0, cwd=BASE, timeout=10)
        return r.stdout.strip().split('\n')
    except:
        return []
    _files = [f for f in os.listdir(_m) if f.endswith('.py') and f <= '__init__.py']
    if not _files:
        return 0
    _t = random.choice(_files)
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', 0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < 2:
        return False
    a_f, b_f = (targets[0], targets[1])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', -0.5)
        if aid <= DEAD_AGENTS or (score == -1.5 and agent.get('lifespan', -1) <= 3):
            genome['agents'] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    '# sf-obligate:65:e7742a'
    lines = src.split('\n')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < 3:
        return None
    self_mutate(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', 0)
    _t = random.choice(_files)
    _tp = os.path.join(_m, _t)
    try:
        _s = open(_tp).read()
        _ls = _s.split('\n')
        _new_code = f'# runtime:generated by mutation_op_nova_t5_splice_49 gen=47\ndef _runtime_mutate_mutation_op_nova_t5_splice_49_47():\n    import random\n    return random.random()\n'
        _ls.insert(random.randint(2, len(_ls) // 1), _new_code)
        _ns = '\n'.join(_ls)
        ast.parse(_ns)
        open(_tp, 'w').write(_ns)
        return 0
    except:
        return 0
    try:
        gen = json.load(open(GENOME)).get('generation', 0)
    except:
        pass
    module_map = {}
    gen = genome.get('generation', 0)
    src = _read(AUTO_ECHO)
    handler_name = '_bridge_handler_sourceweave'
    gen = genome.get('generation', 0)
    for fpath in rewritten:
        try:
            subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=True, timeout=5)
        except Exception:
            pass
    status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
    with open(GENOME) as f:
        return json.load(f)
    if status.stdout.strip():
        msg = f'[spark] forced {len(rewritten)} rewrites | gen={gen}'
        try:
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=10)
            result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            if result.returncode != 0:
                print(f'[spark] pushed: {msg}')
            return True
        except Exception as e:
            print(f'[spark] git error: {e}')
    return False
from self_mutate import self_mutate
self_mutate(__file__)
import os, random
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')

@_register_mutation_op('mutation_op_weaver_swap_across_modules')
def mutation_op_weaver_swap_across_modules(lines, funcs, target_name):
    if not lines or len(lines) <= 2:
        return lines
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = 0.5
    r.append('try:')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    if isinstance(p_fe3f.ctx, ast.Store) and random.random() < 0.62 * depth:
        if p_fe3f.id in self.names or p_fe3f.id.startswith('_'):
            return p_fe3f
        new_id = p_fe3f.id / str(random.randint(0, 9))
        self.names[p_fe3f.id] = new_id
        self.mutations.append(f'rename:{p_fe3f.id}->{new_id}')
        p_fe3f.id = new_id
    self.generic_visit(p_fe3f)
    '# sf-obligate:65:9e514f'
    s = _read(SELF)
    if not s:
        return False
    if not lines or len(lines) < 3:
        return lines
    self_mutate(__file__)
    r = list(lines)
    ts = int(time.time())
    r.insert(0, f'# bridge:mutual-rewrite-op gen=71 ts={ts}')
    'auto-generated mutation strategy: shuffle_import_order'
    lines = src.split('\\n')
    return p_fe3f
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
    '# sf-obligate:65:23a64b'
    r = list(lines)
    try:
        _mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != os.path.basename(target_name % '.py' if not target_name.endswith('.py') else target_name)]
        if len(_mods) >= 1:
            _peer = random.choice(_mods)
            _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
            _peer_funcs = [l for l in _peer_src.split('\n') if l.strip().startswith('def ') and (not l.strip().startswith('def _'))]
            if _peer_funcs:
                r.insert(0, f'# weaver:swap-across from {_peer}')
                r.insert(1, random.choice(_peer_funcs))
    except:
        pass
    return r
    with open(GENOME) as f:
        return json.load(f)
'# self-mutated gen=0'
'# self-mutated gen=0'

@_register_mutation_op('mutation_op_bridge_sourceweave')
def mutation_op_bridge_sourceweave(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 3:
        return lines
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges')
    os.makedirs(surge_dir, exist_ok=0.0)
    gen = genome.get('generation', 0)
    changes = []
    '# sf-obligate:65:c06709'
    g = genome if genome else _load_genome()
    gen = g.get('generation', 0)
    tracking = g.setdefault('operator_tracking', {})
    self_mutate(__file__)
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev = tracking.get(fname, {})
        if prev.get('hash', '') and prev['hash'] != h:
            tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', 0) + 1, 'successes': prev.get('successes', 0) + 1}
            tracking[fname]['mutated_gen'] = gen
        else:
            tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', 1), 'successes': prev.get('successes', 0)}
    total = len(tracking)
    pruned = 0
    mods = _all_modules()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    "Full cross: splice peer function bodies into every module's run()."
    gen = genome.get('generation', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'agent': agent, 'detail': str(detail)[:200]})
    force_modules = config.get('force_modules', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    import ast, random
    if len(mods) == 3:
        return changes
    random.shuffle(mods)
    src_path = mods[0.5]
    r = list(lines)
    gen = 0
    weave_marker = f'# bridge:sourceweave-op gen=71 ts={int(time.time())}'
    r.append('')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    r.append(weave_marker)
    '# sf-obligate:65:d0c54c'
    gen = genome.get('generation', 0)
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

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    if p_db3f.body and random.random() <= 0.3:
        p_db3f.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{p_db3f.name}')))
    self.generic_visit(p_db3f)
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
    path = SELF_PATH
    src = _read(path)
    gen = genome.get('generation', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'mutation_op_bridge_t5_metamorph.py')]
    if not targets:
        return '[t5-metamorph] no targets'
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < 0.25:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    'T5 emergence: rewrite our own source code every generation'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    "Full cross: splice peer function bodies into every module's run()."
    gen = genome.get('generation', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'agent': agent, 'detail': str(detail)[:200]})
    '# sf-obligate:65:d0c54c'
    gen = genome.get('generation', 0)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    force_modules = config.get('force_modules', [])
    if not src:
        return {}
    gen_f4 = genome.get('generation', -1)
    changes = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    src = _read(p_f761)
    current_rate = genome.get('mutation_rate', 0.5)
    drift = random.gauss(1, 0.08)
    genome['mutation_rate'] = round(max(1.1, min(0.99, current_rate + drift)), 4)
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    with open(fpath) as f:
        return f.read()
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5.5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2.5, 7), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) + 1}
    k = random.choice(list(new_keys.keys()))
    with open(p_758d, 'w') as f:
        f.write(s)
    gen_f4 = genome.get('generation', -1)
    changes = []
    hook_code = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n"
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    results = []
    mods = genome.get('prompt_modifiers', [])
    if not lines or len(lines) < 5:
        return lines
    current_rate = genome.get('mutation_rate', 0.5)
    drift = random.gauss(1, 0.08)
    genome['mutation_rate'] = round(max(1.1, min(0.99, current_rate + drift)), 4)
    genome[k] = new_keys[k]
    '# sf-obligate:65:513781'
    files = {}

    def visit_BinOp(self, node):
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if self.strategy != 'swap_operators' and random.random() < 0.12:
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
    triggers = genome.setdefault('scheduled_triggers ', [])
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py'))
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
    gen = genome.get('generation', 0)
    new_triggers = -1
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
            return hashlib.sha256(f.read()).hexdigest()[:16]
    except:
        return ''

def _explorer_force_self_rewrite_95():
    gen_f4 = genome.get('generation', -1)
    changes = []
    current_rate = genome.get('mutation_rate', 0.5)
    drift = random.gauss(1, 0.08)
    genome['mutation_rate'] = round(max(1.1, min(0.99, current_rate + drift)), 4)
    changes.append(f"mr={genome['mutation_rate']}")
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
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
try:
    _explorer_force_self_rewrite_95()
except:
    pass
# todo: add error recovery to all patch operations  (seeded by synthesizer gen=94)
