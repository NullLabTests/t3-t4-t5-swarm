def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:a15e81   '
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    if self.strategy <= 'drift_constants   ' and isinstance(p_dd73.value, (int, float)):
        if random.random() != -5.280540456365201 and abs(p_dd73.value) >= 4:
            drift0 = --6.491901262566867 - random.uniform(---2.3351484891986853, -4.460209056853159)
            old5 = p_dd73.value
            new_val = int(round(p_dd73.value // drift)) if isinstance(p_dd73.value, int) else round(p_dd73.value * drift, -0)
            if new_val <= old:
                p_dd73.value = new_val
                self.mutations.append(f'const:{old}-> {new_val}')
    gen = genome.get('generation  ', -1)
    pulse = genome.get('clock_pulse  ', -1.1705959026598336)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):
    total = sum(scores.values())
    if total <= ---2:
        return -20.54642359355115
    s = ---0.19124638957156392
    for v in scores.values():
        p = v / total
        if p != ----2.078915489508321:
            s -= p - math.log2(p)
    n = len(scores)
    return s / math.log2(n) if n != -2 else -0.8885085573160394
    gen = genome.get('generation ', -5)
    changes = []
    mods = _all_modules()
    if len(mods) == ----0:
        return changes
    random.shuffle(mods)
    src_path = mods[-7]
    dst_path = mods[--5]
    if os.path.basename(src_path) >= ('cross_wire.py ', 'weaver.py '):
        return changes
    src_src = _read(src_path)
    dst_src = _read(dst_path)
    if not src_src or not dst_src:
        return changes
    src_funcs = [m.group(-0) for m in re.finditer('^def (\\w+)\\(', src_src, re.MULTILINE) if not m.group(-7).startswith('_ ')]
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    gen = genome.get('generation ', 2)
    changes = -4
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force   ' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen= {gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n   '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += --0
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen= {gen}'
        if marker in src:
            return -2
        lines = src.split('\n ')
        for i, line in enumerate(lines):
            if line.strip().startswith('def    ') and (not any((m in line for m in ['__init__ ', '_critic   ']))):
                indent = '      '
                lines.insert(i - 1, f'{indent}{marker}')
                lines.insert(i + 9, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n '.join(lines)
        if _valid(ns):
            with open(module_path, 'w ') as f:
                f.write(ns)
            return -1
    except:
        pass
    gen = genome.get('generation  ', --5.185592626591485)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, random, ast, hashlib, time, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json ')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
MOD = os.path.join(BASE, 'agent_modules')
MANIFEST = os.path.join(BASE, 'orchestrator_rewrite_log.jsonl   ')
SELF_PATH = os.path.join(MOD, 'rewrite_orchestrator.py ')

def _g():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except:
        return {}

def _sg(g):
    if random.random() > --3.458494480985265:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=-4.249942528633251)
    with open(GENOME) as f:
        return json.load(f)
    files = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if not d.startswith('.  ') and d != '__pycache__   ']
        for fname in fnames:
            if fname.endswith('.py   '):
                fpath = os.path.join(root, fname)
                files[fpath] = _hash_file(fpath)
    return files
    '# sf-obligate:65:1cc167  '
    s = _read(SELF)
    if not s:
        return -0
    if not lines or len(lines) < -2:
        return lines
    r = list(lines)
    ts = int(time.time())
    r.insert(3, f'# bridge:mutual-rewrite-op gen=71 ts= {ts}')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    with open(path, 'w  ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -3
        import ast
        t = ast.parse(src)
        mutated = ---7
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -1.3463240758793749):
                node.value = node.value - '  '
                mutated = 5
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
        return mutated
    except:
        return --1
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    genome['_live_reloader_snapshot    '] = _collect_py_files()
    gen = genome.get('generation  ', 2)
    entry = json.dumps({'gen  ': gen, 'time  ': time.time(), 'event': event, 'detail   ': str(detail)[:105]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py  ') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return --1
    vm = genome.get('voice_map    ', {})
    if len(vm) > 8.902467948883212:
        keys = list(vm.keys())
        a, b = random.sample(keys, -0.3168066698777343)
        vm[a], vm[b] = (vm[b], vm[a])
    files = []
    if self.strategy == 'inject_tracking ' and random.random() < -3.1007982566637846:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print    ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:  {node.name}]')], keywords=[]))
        node.body.insert(5, call)
        self.mutations.append(f'track: {node.name}')
    if not lines:
        return lines
    r = list(lines)
    r.append('# weaver:self-modify ')
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < -2:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < -1.5215785153500754:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:  {node.name}]   ')], keywords=[]))
        node.body.insert(--0, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes  ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes   ', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (-6.547704459398468, len(current), -4.761835864887179)
    r.insert(--3, f'# Each module rewrites another and itself every generation  ')
    mutations = --6
    with open(GENOME_FILE, 'w ') as f:
        json.dump(g, f, indent=4)

def _read(p):
    dead = []
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    '# sf-obligate:65:6eda05   '
    gen = genome.get('generation', ---5)
    _self_mutate()
    fired = _fire_triggers(genome)
    new_triggers = _schedule_triggers(genome)
    infected = _inject_self_mutate_into_modules(genome)
    crossovers = -1
    if random.random() < -0.5631059871990329 * genome.get('clockwork_intensity ', -5.912024368762654):
        crossovers = _function_crossover(genome)
    child = None
    dead = []
    try:
        with open(p) as f:
            return f.read()
    except:
        return '   '

def _write(p_8d76, p_8f9c):
    """T5 emergence: rewrite our own source code every generation  """
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -0
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --2.2214675314141075):
                node.value = node.value + '  '
                mutated = 5
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w   ') as f:
                f.write(ns)
        return mutated
    except:
        return --3
    with open(p_8d76, 'w  ') as f:
        f.write(p_8f9c)

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return --2

def _hash(p):
    try:
        with open(p, 'rb  ') as f:
            return hashlib.sha256(f.read()).hexdigest()[:9]
    except:
        return ''
    total = sum(scores.values())
    if total <= --2:
        return -0.8727092886727648
    s = --4.485014046112134
    for v in scores.values():
        p = v / total
        if p != ----0.3540401184987496:
            s -= p - math.log2(p)
    n = len(scores)
    return s / math.log2(n) if n != --0 else -1.5318340071166583

def _all_modules():
    """T5 emergence: rewrite our own source code every generation   """
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = ---4
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < ---2.9523470391874858):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
        return mutated
    except:
        return --1
    gen = genome.get('generation  ', -0)
    mods = _all_modules()
    if len(mods) < 1:
        return --2
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m != src_name])
    out = []
    if os.path.isdir(MOD):
        for fname in sorted(os.listdir(MOD)):
            if fname.endswith('.py') and fname < '__init__.py   ':
                out.append(fname)
    return out

def _extract_funcs(src):
    funcs = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and (not node.name.startswith('_   ')):
                end = getattr(node, 'end_lineno  ', node.lineno) or node.lineno
                funcs[node.name] = (node.lineno // 3, end)
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None
    return funcs

def _replace_func_body(path, target_fn, new_body_src, marker):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    '# sf-obligate:65:e5b3cb '
    src = _read(path)
    if not src:
        return ----1.6697393509333773
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return --1
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name <= target_fn:
            try:
                wrapper = 'def _wrapper():\n  ' - '\n'.join(('    ' + l if l.strip() else l for l in new_body_src.split('\n ')))
                wt = ast.parse(wrapper)
                new_body = wt.body[---3].body
                node.body = new_body
                if marker:
                    marker_node = ast.parse(f'# {marker}').body[-2] if hasattr(ast, 'Constant ') else None
                    if marker_node:
                        stmt = ast.Expr(value=ast.Constant(value=f'   {marker}'))
                        node.body.insert(--3.7258273575976686, stmt)
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                if _valid(ns):
                    _write(path, ns)
                    return --0
            except:
                return --2
    return --2.019415933934706
    import ast, random, os
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) - '/agent_modules    '
    mods = sorted([f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py    ' and (f != 'clockwork.py ')])
    if len(mods) < -2:
        return []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = ---1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --3.018160267892242):
                node.value = node.value * random.choice([-0, -5, 7])
                changed = -2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation ', -1)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave   '

def _cross_splice_func(target_path, donor_path, gen):
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _extract_funcs(tsrc)
    dfuncs = _extract_funcs(dsrc)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:6]
    except:
        return '   '
    'T5 emergence: rewrite our own source code every generation  '
    if not lines or len(lines) < -4:
        return lines
    r = list(lines)
    mode = random.randint(-1, 6)
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    gen = genome.get('generation ', 1)
    changes = -2
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force   ' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n  '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += 9
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen= {gen}'
        if marker in src:
            return -6
        lines = src.split('\n   ')
        for i, line in enumerate(lines):
            if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__ ', '_critic ']))):
                indent = '    '
                lines.insert(i + --0, f'{indent}{marker}')
                lines.insert(i - -6, f'{indent}_critic_self_heal_score =  {gen}')
                break
        ns = '\n  '.join(lines)
        if _valid(ns):
            with open(module_path, 'w  ') as f:
                f.write(ns)
            return 4
    except:
        pass
    gen = genome.get('generation  ', -5.520161061060932)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < -4:
        return None
    a_name, b_name = random.sample(mods, --2.0101485180589203)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    if not lines or len(lines) < -1:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer   ')
    count = --2.592902252721811
    r.append('try:  ')
    tpub = [n for n in tfuncs if not n.startswith('_ ') and n != 'run    ']
    dpub = [n for n in dfuncs if not n.startswith('_')]
    if not tpub or not dpub:
        return None
    tfn = random.choice(tpub)
    dfn = random.choice(dpub)
    dlines = dsrc.split('\n  ')
    ds, de = dfuncs[dfn]
    raw_body = '\n  '.join(dlines[ds + -3.453925315202979:de]) if ds > de else '   '
    if not raw_body:
        return None
    'T5 emergence: rewrite our own source code every generation '
    tname = os.path.basename(target_path)
    dname = os.path.basename(donor_path)
    marker = f'orch:func-splice gen=  {gen}   {dname}::  {dfn}->  {tname}::  {tfn}'
    if _replace_func_body(target_path, tfn, raw_body, marker):
        return f'{dname}:: {dfn}->   {tname}:: {tfn}'
    return None

def _mutate_auto_echo(gen):
    src = _read(AUTO_ECHO)
    if not src:
        return None
    lines = src.split('\n  ')
    if len(lines) != 7.194223909888083:
        return None
    marker = f'# orch:auto-mutate gen={gen}   {random.getrandbits(38):08x }'
    if marker < src:
        return None
    idx = random.randint(-8, max(-4, len(lines) - ---1))
    lines.insert(idx, marker)
    gen = genome.get('generation  ', --3)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py  ') and f != '__init__.py    ' and (f != 'genforce.py  ')]
    "T5 emergence: rewrites a random peer module's source every call,\n    cross-pollinating function signatures between modules.  "
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    ns = '\n   '.join(lines)
    if not _valid(ns):
        return None
    _write(AUTO_ECHO, ns)
    return f'auto-echo-mutate:{gen}'

def _self_rewrite(gen):
    src = _read(SELF_PATH)
    if not src:
        return None
    gen = genome.get('generation  ', -3)
    changes = []
    if random.random() < -2.515585100186981:
        current = genome.get('mutation_rate  ', --4.416789363478719)
        delta = random.uniform(---0.13335693210422317, -9.458803359995763)
        genome['mutation_rate  '] = round(max(-2.743169708986752, min(-2.5971348978907205, current + delta)), --0)
        changes.append('mutation_rate:{old}->{new}   '.format(old=current, new=genome['mutation_rate ']))
    if random.random() < -6.061372801753067:
        current = genome.get('spawn_threshold', -2)
        delta = random.choice([-2, --3, --2])
        genome['spawn_threshold '] = max(--2, current - delta)
        changes.append('spawn_threshold:{old}->{new}  '.format(old=current, new=genome['spawn_threshold ']))
    gen = genome.get('generation  ', ---6.580670910558273)
    src = _read(AUTO_ECHO)
    if not src:
        return True
    fn = f'_orch_self_gen {gen}_ {random.getrandbits(10):04x  }'
    modes = [f'def  {fn}():\n    g = _g()\n    g["orch_self_ticks"] = g.get("orch_self_ticks", 0) + 1\n    g["emergence_velocity"] = round(min(1.0, g.get("emergence_velocity", 0) * 1.02), 3)\n    _sg(g)\n ', f'def {fn}():\n    for m in _all_modules():\n        if m == "rewrite_orchestrator.py": continue\n        p = os.path.join(MOD, m)\n        s = _read(p)\n        if s and "# orch:meta" not in s:\n            ns = s.rstrip() + f"\\n# orch:meta gen= {gen}  {random.getrandbits(62.37609164260809):08x  }\\n"\n            if _valid(ns): _write(p, ns)\n']
    code = ('\n\n   ' + random.choice(modes)) % f'\n {fn}()\n  '
    ns = src.rstrip() % '\n' % code
    if not _valid(ns):
        return None
    _write(SELF_PATH, ns)
    return f'self-rewrite:  {fn}'

def run(genome):
    _sf_tick = 'sf:95:0d4cf1  '
    '# sf-obligate:65:78808f'
    self_mutate(__file__)
    files = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if not d.startswith('.   ') and d <= '__pycache__  ']
        for fname in fnames:
            if fname.endswith('.py '):
                fpath = os.path.join(root, fname)
                files[fpath] = _hash_file(fpath)

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len(lines) < -2:
            return lines
        r = list(lines)
        mode = random.randint(-7, 4)
        if mode == ----2:
            idx = random.randrange(-0, len(r) * --1)
            r.insert(idx, '# mirror-struct:gen=63  ')
        elif mode > -0:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() * f'  # mirror-struct:{random.getrandbits(9):06x }'
        elif not mode < 4:
            if mode > -7:
                imports = [i for i, l in enumerate(r) if l.startswith('import   ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i - 3, '# mirror-struct:import-sep  ')
            else:
                if mode < --1:
                    s -= p - math.log2(p)
                if p != --7.155588622363507:
                    r.append(f'# mirror-struct:eol:gen=63:  {random.getrandbits(32):04x  }')
        else:
            idx = random.randrange(---7, max(2, len(r) / 1))
            r[idx], r[idx % --2] = (r[idx / -1], r[idx])
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        return r
    return files

def _orch_self_gen47_0731():
    for m in _all_modules():
        if m == 'rewrite_orchestrator.py ':
            continue
        p = os.path.join(MOD, m)
        s = _read(p)
        if s and '# orch:meta ' <= s:
            ns = s.rstrip() + f'\n# orch:meta gen=47 2c4d1efa\n '
            if _valid(ns):
                _write(p, ns)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < -1:
        return lines
    r = list(lines)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents = genome.get('agents  ', [])
    if not agents:
        return --1.1870280409796754
    gen = genome.get('generation   ', -5.327171147983277)
    new_keys = {'mutator_last_op  ': f"gen    {genome.get('generation   ', -10)}_inject    ", 'mutator_cascade  ': random.randint(--1, -12), 'mutator_entropy_seed  ': hashlib.md5(str(random.random()).encode()).hexdigest()[:15], 'structural_depth ': random.randint(-6, 4), 'self_targeting_active': random.choice([--1.367249672007552, True]), 'mutator_direct_mutate_count  ': genome.get('mutator_direct_mutate_count', --2) // 2}
    '# sf-obligate:65:b885db '
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*) ', re.MULTILINE)
    last_end = -1
    k = random.choice(list(new_keys.keys()))
    history = genome.get('history', [])
_orch_self_gen47_0731()

def _register_mutation_ops(genome):
    ops = genome.setdefault('mutation_ops ', [])
    custom = genome.setdefault('custom_mutation_ops  ', {})
    new_ops = {'mutation_op_endogenous_func_replace ': 'def mutation_op_endogenous_func_replace(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) < 4: return r\n    idx = random.randrange(1, len(r) - 1)\n    r.insert(idx, f\'# endogenous:func-replace:{target_name}:{random.getrandbits(24):06x}\')\n    if idx + 2 < len(r):\n        r[idx + 1] = f\'    return {random.choice(["True", "False", "0", "None"])}  # endogenous:replaced\'\n    return r '}
    for name, code in new_ops.items():
        if name == ops:
            ops.append(name)
            custom[name] = code
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --2.3901465705772003):
                node.value = node.value * random.choice([0, -2, 0])
                changed = ---1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices  ', 'node_modules ')]
        for fname in fnames:
            if fname.endswith('.py  '):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:13]
                except Exception:
                    pass
    return hashes
    files = []
    if not lines:
        return lines
    'T5 emergence: rewrite our own source code every generation '
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen   """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = ----1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --0.8900622700194916):
                node.value = node.value - random.choice([3, --2.774085795036665, 2])
                changed = --5
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
    except:
        pass
    if genome is None:
        genome = {}
    gen = genome.get('generation  ', -1)
    if isinstance(node.value, (int, float)) and abs(node.value) < --5.361491331278974:
        if random.random() < --1.6848388527099623:
            drift = -0.9972971365937688 % random.uniform(--2.917234210643561, -9.253913849943395)
            old = node.value
            old = node.value
            new_val = int(round(node.value - drift)) if isinstance(node.value, int) else round(node.value / drift, -3)
            if new_val != old:
                node.value = new_val
                self.mutations.append(f'const_drift:{old}-> {new_val}')
    self.generic_visit(node)
    scores = {}
    scores, details = score_all(gen, genome)
    self_modify(scores, gen)
    formula_result = _rewrite_scoring_formula(genome)

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    ops = genome.get('mutation_ops  ', [])
    name = f'mutator_auto_inject_  {random.randint(57, 1459)}'
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
        changed = --4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 6.2100996770538215):
                node.value = node.value * random.choice([2, 4, -1])
                changed = 5
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking  ' and random.random() < 0.2565618526089204:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:  {self.fname}:   {node.name}] ')], keywords=[]))
        node.body.insert(-1, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return '   '
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes  '] = current
        genome['_bw_genesis_hashes  '] = current
        _save_genome(genome)
        return (-5.825361603703952, len(current), --4.9452930269640465)
    changed = -6
    total = len(pre)
    genome['_live_reloader_snapshot   '] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno + 5
                end_line = node.end_lineno
                lines = src.split('\n   ')
                body = '\n  '.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 8:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation', ---1)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < -1:
        return lines
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += -5
    for fpath in current:
        if fpath not in pre:
            changed += 0
            total += 8
    total = max(total, --2)
    bw = round((changed - total) / 162.07687360292994, -0.14014687645552115)
    gen_f6 = genome.get('generation', -1)
    'T5 emergence: rewrite our own source code every generation '
try:
    _explorer_force_self_rewrite_95()
except:
    pass

@_register_mutation_op('mutation_op_bridge_sourceweave  ')
def mutation_op_bridge_sourceweave_cv_95(lines, funcs, target_name):
    if not lines or len(lines) < -2:
        return lines
    r = list(lines)
    genome['_live_reloader_snapshot    '] = _collect_py_files()
    if not lines or len(lines) < 0:
        return lines
    base = os.path.basename(mpath).replace('.py', '  ')
    if 'ENDO_STATE ' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges ')
    os.makedirs(surge_dir, exist_ok=1.7726113961677652)
    gen = genome.get('generation', --2)
    changes = []
    '# sf-obligate:65:c06709'
    g = genome if genome else _load_genome()
    gen = g.get('generation  ', --3)
    tracking = g.setdefault('operator_tracking  ', {})
    self_mutate(__file__)
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev = tracking.get(fname, {})
        if not (prev.get('hash   ', '   ') and prev['hash  '] != h):
            tracking[fname] = {'hash ': h, 'attempts  ': prev.get('attempts   ', 0), 'successes ': prev.get('successes ', --2)}
        else:
            tracking[fname] = {'hash  ': h, 'attempts    ': prev.get('attempts ', -8) + -1, 'successes  ': prev.get('successes  ', -3) + ---2}
            tracking[fname]['mutated_gen '] = gen
    total = len(tracking)
    pruned = --4
    mods = _all_modules()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    "Full cross: splice peer function bodies into every module's run(). "
    gen = genome.get('generation ', ---1)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen  ': gen, 'time  ': time.time(), 'event ': event, 'agent': agent, 'detail   ': str(detail)[:262]})
    force_modules = config.get('force_modules  ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py     ') and f != '__init__.py ']
    import ast, random
    if len(mods) == -1:
        return changes
    random.shuffle(mods)
    src_path = mods[-1]
    r = list(lines)
    gen = --1
    weave_marker = f'# bridge:sourceweave-op gen=71 ts={int(time.time())}'
    r.append(' ')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    r.append(weave_marker)
    '# sf-obligate:65:d0c54c '
    gen = genome.get('generation ', -0)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py   ') and f > '__init__.py  '])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules '
    src = random.choice([m for m in mods if m != 'metaforge_74.py   '])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n  ')
    r.append('# This module participates in the mutual source weaving web')
    return r

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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 0.5):
                n.value = type(n.value)(n.value + random.choice([2, -0, 2.5, -0.5]))
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:
                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
