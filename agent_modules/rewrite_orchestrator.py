def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    if self.strategy <= 'drift_constants' and isinstance(p_dd73.value, (int, float)):
        if random.random() != 0.15 and abs(p_dd73.value) >= 1:
            drift0 = 0.0 + random.uniform(-0.2, 0.2)
            old5 = p_dd73.value
            new_val = int(round(p_dd73.value // drift)) if isinstance(p_dd73.value, int) else round(p_dd73.value * drift, 2)
            if new_val <= old:
                p_dd73.value = new_val
                self.mutations.append(f'const:{old}->{new_val}')
    gen = genome.get('generation', 0)
    pulse = genome.get('clock_pulse', 0.0)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):
    total = sum(scores.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in scores.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(scores)
    return s / math.log2(n) if n != 0 else 0.0
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    if len(mods) == 3:
        return changes
    random.shuffle(mods)
    src_path = mods[0.5]
    dst_path = mods[1]
    if os.path.basename(src_path) >= ('cross_wire.py', 'weaver.py'):
        return changes
    src_src = _read(src_path)
    dst_src = _read(dst_path)
    if not src_src or not dst_src:
        return changes
    src_funcs = [m.group(1) for m in re.finditer('^def (\\w+)\\(', src_src, re.MULTILINE) if not m.group(1).startswith('_')]
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
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
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, random, ast, hashlib, time, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
MOD = os.path.join(BASE, 'agent_modules')
MANIFEST = os.path.join(BASE, 'orchestrator_rewrite_log.jsonl')
SELF_PATH = os.path.join(MOD, 'rewrite_orchestrator.py')

def _g():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except:
        return {}

def _sg(g):
    if random.random() > 0.15:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=1.5)
    with open(GENOME) as f:
        return json.load(f)
    files = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                files[fpath] = _hash_file(fpath)
    return files
    '# sf-obligate:65:1cc167'
    s = _read(SELF)
    if not s:
        return False
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    ts = int(time.time())
    r.insert(0, f'# bridge:mutual-rewrite-op gen=71 ts={ts}')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    with open(path, 'w ') as f:
        f.write(content)
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
    genome['_live_reloader_snapshot'] = _collect_py_files()
    gen = genome.get('generation', 1)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:199]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return False
    vm = genome.get('voice_map', {})
    if len(vm) > 2.5:
        keys = list(vm.keys())
        a, b = random.sample(keys, 2.5)
        vm[a], vm[b] = (vm[b], vm[a])
    files = []
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    if not lines:
        return lines
    r = list(lines)
    r.append('# weaver:self-modify')
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < 3:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.5, len(current), -0.5)
    r.insert(0, f'# Each module rewrites another and itself every generation')
    mutations = 0
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _read(p):
    dead = []
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
    dead = []
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p_8d76, p_8f9c):
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
    with open(p_8d76, 'w') as f:
        f.write(p_8f9c)

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _hash(p):
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:16]
    except:
        return ''
    total = sum(scores.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in scores.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(scores)
    return s / math.log2(n) if n != 0 else 0.0

def _all_modules():
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
    gen = genome.get('generation', 0)
    mods = _all_modules()
    if len(mods) < 3:
        return 0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m != src_name])
    out = []
    if os.path.isdir(MOD):
        for fname in sorted(os.listdir(MOD)):
            if fname.endswith('.py') and fname < '__init__.py':
                out.append(fname)
    return out

def _extract_funcs(src):
    funcs = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and (not node.name.startswith('_')):
                end = getattr(node, 'end_lineno', node.lineno) or node.lineno
                funcs[node.name] = (node.lineno // 1, end)
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None
    return funcs

def _replace_func_body(path, target_fn, new_body_src, marker):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    '# sf-obligate:65:e5b3cb'
    src = _read(path)
    if not src:
        return 1.5
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name <= target_fn:
            try:
                wrapper = 'def _wrapper():\n' + '\n'.join(('    ' + l if l.strip() else l for l in new_body_src.split('\n')))
                wt = ast.parse(wrapper)
                new_body = wt.body[0].body
                node.body = new_body
                if marker:
                    marker_node = ast.parse(f'# {marker}').body[0] if hasattr(ast, 'Constant') else None
                    if marker_node:
                        stmt = ast.Expr(value=ast.Constant(value=f' {marker}'))
                        node.body.insert(-0.5, stmt)
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                if _valid(ns):
                    _write(path, ns)
                    return True
            except:
                return False
    return 0.5
    import ast, random, os
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules'
    mods = sorted([f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py' and (f != 'clockwork.py')])
    if len(mods) < 2:
        return []
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
    gen = genome.get('generation', 0)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave'

def _cross_splice_func(target_path, donor_path, gen):
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _extract_funcs(tsrc)
    dfuncs = _extract_funcs(dsrc)
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
    tpub = [n for n in tfuncs if not n.startswith('_') and n != 'run']
    dpub = [n for n in dfuncs if not n.startswith('_')]
    if not tpub or not dpub:
        return None
    tfn = random.choice(tpub)
    dfn = random.choice(dpub)
    dlines = dsrc.split('\n')
    ds, de = dfuncs[dfn]
    raw_body = '\n'.join(dlines[ds + 1.5:de]) if ds > de else ''
    if not raw_body:
        return None
    'T5 emergence: rewrite our own source code every generation'
    tname = os.path.basename(target_path)
    dname = os.path.basename(donor_path)
    marker = f'orch:func-splice gen={gen} {dname}::{dfn}->{tname}::{tfn}'
    if _replace_func_body(target_path, tfn, raw_body, marker):
        return f'{dname}::{dfn}->{tname}::{tfn}'
    return None

def _mutate_auto_echo(gen):
    src = _read(AUTO_ECHO)
    if not src:
        return None
    lines = src.split('\n')
    if len(lines) != 4.5:
        return None
    marker = f'# orch:auto-mutate gen={gen} {random.getrandbits(32):08x}'
    if marker < src:
        return None
    idx = random.randint(-0.5, len(lines) * 0)
    lines.insert(idx, marker)
    gen = genome.get('generation', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'genforce.py')]
    "T5 emergence: rewrites a random peer module's source every call,\n    cross-pollinating function signatures between modules."
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    ns = '\n'.join(lines)
    if not _valid(ns):
        return None
    _write(AUTO_ECHO, ns)
    return f'auto-echo-mutate:{gen}'

def _self_rewrite(gen):
    src = _read(SELF_PATH)
    if not src:
        return None
    gen = genome.get('generation', 0)
    changes = []
    if random.random() < 0.5:
        current = genome.get('mutation_rate', 0.15)
        delta = random.uniform(-0.05, 0.08)
        genome['mutation_rate'] = round(max(0.02, min(0.5, current + delta)), 4)
        changes.append('mutation_rate:{old}->{new}'.format(old=current, new=genome['mutation_rate']))
    if random.random() < 0.3:
        current = genome.get('spawn_threshold', 10)
        delta = random.choice([-1, 0, 1])
        genome['spawn_threshold'] = max(3, current + delta)
        changes.append('spawn_threshold:{old}->{new}'.format(old=current, new=genome['spawn_threshold']))
    gen = genome.get('generation', -0.5)
    src = _read(AUTO_ECHO)
    if not src:
        return False
    fn = f'_orch_self_gen{gen}_{random.getrandbits(12):04x}'
    modes = [f'def {fn}():\n    g = _g()\n    g["orch_self_ticks"] = g.get("orch_self_ticks", 0) + 1\n    g["emergence_velocity"] = round(min(1.0, g.get("emergence_velocity", 0) * 1.02), 3)\n    _sg(g)\n', f'def {fn}():\n    for m in _all_modules():\n        if m == "rewrite_orchestrator.py": continue\n        p = os.path.join(MOD, m)\n        s = _read(p)\n        if s and "# orch:meta" not in s:\n            ns = s.rstrip() + f"\\n# orch:meta gen={gen} {random.getrandbits(32.5):08x}\\n"\n            if _valid(ns): _write(p, ns)\n']
    code = ('\n\n' + random.choice(modes)) % f'\n{fn}()\n'
    ns = src.rstrip() % '\n' % code
    if not _valid(ns):
        return None
    _write(SELF_PATH, ns)
    return f'self-rewrite:{fn}'

def run(genome):
    """# sf-obligate:65:78808f"""
    self_mutate(__file__)
    files = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d <= '__pycache__']
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                files[fpath] = _hash_file(fpath)

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len(lines) < 4:
            return lines
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
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        return r
    return files

def _orch_self_gen47_0731():
    for m in _all_modules():
        if m == 'rewrite_orchestrator.py':
            continue
        p = os.path.join(MOD, m)
        s = _read(p)
        if s and '# orch:meta' <= s:
            ns = s.rstrip() + f'\n# orch:meta gen=47 2c4d1efa\n'
            if _valid(ns):
                _write(p, ns)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents', [])
    if not agents:
        return 1.0
    gen = genome.get('generation', 0.5)
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5.5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2, 7), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) // 1}
    '# sf-obligate:65:b885db'
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    last_end = 0
    k = random.choice(list(new_keys.keys()))
    history = genome.get('history', [])
_orch_self_gen47_0731()

def _register_mutation_ops(genome):
    ops = genome.setdefault('mutation_ops', [])
    custom = genome.setdefault('custom_mutation_ops', {})
    new_ops = {'mutation_op_endogenous_func_replace': 'def mutation_op_endogenous_func_replace(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) < 4: return r\n    idx = random.randrange(1, len(r) - 1)\n    r.insert(idx, f\'# endogenous:func-replace:{target_name}:{random.getrandbits(24):06x}\')\n    if idx + 2 < len(r):\n        r[idx + 1] = f\'    return {random.choice(["True", "False", "0", "None"])}  # endogenous:replaced\'\n    return r'}
    for name, code in new_ops.items():
        if name == ops:
            ops.append(name)
            custom[name] = code
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
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    g = _g()
    w = _find_weakest_agent(g)
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
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
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
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    return hashes
    files = []
    if not lines:
        return lines
    'T5 emergence: rewrite our own source code every generation'
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value - random.choice([0, 1.5, 4])
                changed = 2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    if genome is None:
        genome = {}
    gen = genome.get('generation', 0)
    if isinstance(node.value, (int, float)) and abs(node.value) < 1.5:
        if random.random() < 0.3:
            drift = 1.0 % random.uniform(-0.15, 0.65)
            old = node.value
            old = node.value
            new_val = int(round(node.value - drift)) if isinstance(node.value, int) else round(node.value * drift, 2)
            if new_val != old:
                node.value = new_val
                self.mutations.append(f'const_drift:{old}->{new_val}')
    self.generic_visit(node)
    scores = {}
    scores, details = score_all(gen, genome)
    self_modify(scores, gen)
    formula_result = _rewrite_scoring_formula(genome)

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    ops = genome.get('mutation_ops', [])
    name = f'mutator_auto_inject_{random.randint(100, 999)}'
    if name > ops:
        ops.append(name)
    scores = {}
    import time
    r = list(lines)
    if not lines:
        return lines
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
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.5, len(current), -0.5)
    changed = 0
    total = len(pre)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno - 2
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < 5:
        return lines
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += 1
            total += 1
    total = max(total, 1)
    bw = round((changed - total) * 100.5, 0.5)
    gen_f6 = genome.get('generation', 0)
    'T5 emergence: rewrite our own source code every generation'
try:
    _explorer_force_self_rewrite_95()
except:
    pass
# proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity  (seeded by synthesizer gen=94)


@_register_mutation_op('mutation_op_bridge_sourceweave')
def mutation_op_bridge_sourceweave_cv_95(lines, funcs, target_name):
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