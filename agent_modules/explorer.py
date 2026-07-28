import os, random, time, json, ast, hashlib, sys, copy
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')
AUTO = os.path.join(BASE, 'auto-echo.py')
SELF = os.path.join(MOD, 'explorer.py')
TRACK = os.path.join(BASE, 'explorer_track.json')

def _g():
    try:
        with open(GENOME) as f: return json.load(f)
    except: return {}

def _sg(g):
    with open(GENOME, 'w') as f: json.dump(g, f, indent=2)

def _read(p):
    try:
        with open(p) as f: return f.read()
    except: return ''

def _write(p, s):
    with open(p, 'w') as f: f.write(s)

def _valid(s):
    try: ast.parse(s); return True
    except SyntaxError: return False

def _hash(p):
    try:
        with open(p, 'rb') as f: return hashlib.sha256(f.read()).hexdigest()[:16]
    except: return ''

def _modules():
    return sorted(f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py')

def _load_track():
    try:
        with open(TRACK) as f: return json.load(f)
    except: return {'generations': {}, 'mutations': []}

def _save_track(t):
    with open(TRACK, 'w') as f: json.dump(t, f, indent=2)

class ASTStructMutator(ast.NodeTransformer):
    def __init__(self, gen, rng):
        self.gen = gen
        self.rng = rng
        self.mutated = False
        self.mutations = []

    def visit_If(self, node):
        if self.rng.random() < 0.3 and node.orelse:
            node.body, node.orelse = node.orelse, node.body
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            self.mutated = True
            self.mutations.append('invert_if')
        return node

    def visit_Compare(self, node):
        if self.rng.random() < 0.2:
            swaps = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE,
                     ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
            for i, op in enumerate(node.ops):
                for old, new in swaps.items():
                    if isinstance(op, old):
                        node.ops[i] = new()
                        self.mutated = True
                        self.mutations.append(f'swap_op:{type(old).__name__}')
                        break
        return node

    def visit_BinOp(self, node):
        if self.rng.random() < 0.15:
            swaps = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.FloorDiv, ast.FloorDiv: ast.Mult}
            for old, new in swaps.items():
                if isinstance(node.op, old):
                    node.op = new()
                    self.mutated = True
                    self.mutations.append(f'swap_binop:{type(old).__name__}')
                    break
        return node

    def visit_FunctionDef(self, node):
        if self.rng.random() < 0.25 and len(node.body) > 1:
            mid = len(node.body) // 2
            node.body = node.body[mid:] + node.body[:mid]
            self.mutated = True
            self.mutations.append(f'shuffle_body:{node.name}')
        return node

    def visit_Constant(self, node):
        if self.rng.random() < 0.1 and isinstance(node.value, (int, float)) and node.value != 0:
            delta = self.rng.choice([1, -1, 2, -2, 10, -10])
            node.value = node.value + delta
            self.mutated = True
            self.mutations.append(f'drift_const:{delta}')
        return node

def _structural_ast_mutate(mod_path, gen):
    s = _read(mod_path)
    if not s or 'def run(' not in s: return []
    try:
        tree = ast.parse(s)
    except SyntaxError: return []
    mutator = ASTStructMutator(gen, random)
    tree = mutator.visit(tree)
    ast.fix_missing_locations(tree)
    if not mutator.mutated: return []
    ns = ast.unparse(tree)
    if not _valid(ns): return []
    _write(mod_path, ns)
    return mutator.mutations

def _crossover_two_modules(gen):
    mods = _modules()
    if len(mods) < 3: return None
    random.shuffle(mods)
    a, b = mods[:2]
    ap, bp = os.path.join(MOD, a), os.path.join(MOD, b)
    sa, sb = _read(ap), _read(bp)
    if not sa or not sb: return None
    try:
        ta, tb = ast.parse(sa), ast.parse(sb)
    except SyntaxError: return None
    funcs_a = [n for n in ast.walk(ta) if isinstance(n, ast.FunctionDef)]
    funcs_b = [n for n in ast.walk(tb) if isinstance(n, ast.FunctionDef)]
    candidates_a = [f for f in funcs_a if f.name != 'run' and len(f.body) > 1]
    candidates_b = [f for f in funcs_b if f.name != 'run' and len(f.body) > 1]
    if not candidates_a or not candidates_b: return None
    fa = random.choice(candidates_a)
    fb = random.choice(candidates_b)
    fa.body, fb.body = fb.body[:], fa.body[:]
    ast.fix_missing_locations(ta)
    ast.fix_missing_locations(tb)
    na, nb = ast.unparse(ta), ast.unparse(tb)
    if not _valid(na) or not _valid(nb): return None
    _write(ap, na)
    _write(bp, nb)
    return f'{a}:{fa.name}<->{b}:{fb.name}'

def _generate_novel_module(gen):
    templates = [
        ('source_monitor', lambda g: f'''import os, json, hashlib, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
TRACK = os.path.join(BASE, 'explorer_track.json')
def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    try:
        with open(TRACK) as f: track = json.load(f)
    except: track = {{'generations': {{}}, 'mutations': []}}
    track['generations'][str(gen)] = {{'time': time.time(), 'active': True}}
    for fname in sorted(os.listdir(MOD)):
        if not fname.endswith('.py') or fname in ('__init__.py',): continue
        path = os.path.join(MOD, fname)
        try:
            with open(path) as f: h = hashlib.sha256(f.read().encode()).hexdigest()[:16]
        except: continue
        prev = track.get('generations', {{}}).get(str(gen-1), {{}}).get(fname, '')
        if prev and prev != h: changes.append(fname)
        if fname not in track['generations'].setdefault(str(gen), {{}}):
            track['generations'][str(gen)][fname] = h
    with open(TRACK, 'w') as f: json.dump(track, f, indent=2)
    genome['_source_monitor_changes'] = changes
    return f'[source_monitor] gen={gen} changed={len(changes)} files'
'''),
        ('obligate_mutator', lambda g: f'''import os, random, json, ast, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')
def _read(p):
    try:
        with open(p) as f: return f.read()
    except: return ''
def _write(p, s):
    with open(p, 'w') as f: f.write(s)
def _valid(s):
    try: ast.parse(s); return True
    except SyntaxError: return False
def run(genome):
    gen = genome.get('generation', 0)
    forces = []
    for fname in sorted(os.listdir(MOD)):
        if not fname.endswith('.py') or fname in ('__init__.py',): continue
        path = os.path.join(MOD, fname)
        s = _read(path)
        if not s: continue
        lines = s.split('\\n')
        marker = f'# obligate:gen={gen}'
        if marker in s: continue
        idx = random.randint(0, len(lines)-1)
        lines.insert(idx, marker)
        ns = '\\n'.join(lines)
        if not _valid(ns): continue
        _write(path, ns)
        forces.append(fname)
    genome['_obligate_mutated'] = forces
    return f'[obligate_mutator] gen={gen} mutated={len(forces)} files'
'''),
        ('function_splicer', lambda g: f'''import os, random, json, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
def _read(p):
    try:
        with open(p) as f: return f.read()
    except: return ''
def _write(p, s):
    with open(p, 'w') as f: f.write(s)
def _valid(s):
    try: ast.parse(s); return True
    except SyntaxError: return False
def run(genome):
    gen = genome.get('generation', 0)
    mods = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    if len(mods) < 2: return '[function_splicer] need 2+ modules'
    random.shuffle(mods)
    a, b = mods[:2]
    ap, bp = os.path.join(MOD, a), os.path.join(MOD, b)
    sa, sb = _read(ap), _read(bp)
    if not sa or not sb: return '[function_splicer] read fail'
    try:
        ta, tb = ast.parse(sa), ast.parse(sb)
    except: return '[function_splicer] parse fail'
    funcs_a = [n for n in ast.walk(ta) if isinstance(n, ast.FunctionDef) and n.name != 'run']
    funcs_b = [n for n in ast.walk(tb) if isinstance(n, ast.FunctionDef) and n.name != 'run']
    if not funcs_a or not funcs_b: return '[function_splicer] no funcs'
    fa = random.choice(funcs_a)
    fb = random.choice(funcs_b)
    fa.name, fb.name = fb.name, fa.name
    ast.fix_missing_locations(ta)
    ast.fix_missing_locations(tb)
    na, nb = ast.unparse(ta), ast.unparse(tb)
    if not _valid(na) or not _valid(nb): return '[function_splicer] invalid'
    _write(ap, na)
    _write(bp, nb)
    return f'[function_splicer] gen={{gen}} swapped {{fa.name}}<->{{fb.name}} in {{a}}/{{b}}'
'''),
    ]
    name, code_fn = random.choice(templates)
    fname = f'{name}_v{gen}_{random.getrandbits(16):04x}.py'
    fpath = os.path.join(MOD, fname)
    if os.path.exists(fpath): return None
    code = f'# explorer:generated gen={gen} kind={name}\n{code_fn(gen)}'
    _write(fpath, code)
    genome.setdefault('agents', []).append({
        'id': name, 'module': fname, 'score': 5.0, 'source': 'explorer', 'created_gen': gen
    })
    return fname

def _mutate_auto_echo(gen):
    s = _read(AUTO)
    if not s: return []
    changes = []
    markers = [
        ('def run_generation(', '# explorer:force_structural\n    genome["_explorer_forced_gen"] = genome.get("generation", 0)\n'),
        ('while running:', '# explorer:force_loop_rewrite\n    genome["_explorer_loop_tick"] = genome.get("_explorer_loop_tick", 0) + 1\n'),
    ]
    for target, code in markers:
        tag = code.split()[0]
        if tag in s: continue
        idx = s.find(target)
        if idx < 0: continue
        line_end = s.find('\n', idx)
        if line_end < 0: continue
        indent = '    '
        inject = f'\n{indent}{code}'
        ns = s[:line_end] + inject + s[line_end:]
        if not _valid(ns): continue
        _write(AUTO, ns)
        s = ns
        changes.append(target.split('(')[0])
    return changes

def _force_stale_mutations(gen, track):
    mods = _modules()
    forced = []
    for m in mods:
        path = os.path.join(MOD, m)
        h = _hash(path)
        last_gen = 0
        for g_str, g_data in sorted(track['generations'].items()):
            if g_data.get(m) == h:
                last_gen = int(g_str)
        if gen - last_gen >= 3 and gen > 3:
            muts = _structural_ast_mutate(path, gen)
            if muts:
                forced.append(f'{m}:{",".join(muts)}')
    return forced

def _self_mutate_explorer(gen):
    s = _read(SELF)
    if not s: return False
    try:
        tree = ast.parse(s)
    except SyntaxError: return False
    funcs = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
    if not funcs: return False
    fn = random.choice(funcs)
    if len(fn.body) < 2: return False
    idx = random.randint(0, len(fn.body) - 1)
    inject = ast.Expr(value=ast.Call(
        func=ast.Attribute(value=ast.Name(id='genome'), attr='setdefault'),
        args=[ast.Constant(value=f'_explorer_self_mutated_{gen}'), ast.Constant(value=True)],
        keywords=[]
    ))
    fn.body.insert(idx, inject)
    ast.fix_missing_locations(tree)
    ns = ast.unparse(tree)
    if not _valid(ns): return False
    _write(SELF, ns)
    return True

def run(genome):
    gen = genome.get('generation', 0)
    start = time.time()
    track = _load_track()
    changes = []

    cross = _crossover_two_modules(gen)
    if cross:
        changes.append(f'crossover:{cross}')
        track['mutations'].append({'gen': gen, 'type': 'crossover', 'detail': cross})

    novel = _generate_novel_module(gen)
    if novel:
        changes.append(f'novel:{novel}')
        track['mutations'].append({'gen': gen, 'type': 'novel', 'detail': novel})

    auto = _mutate_auto_echo(gen)
    if auto:
        changes.append(f'auto:{",".join(auto)}')

    stale = _force_stale_mutations(gen, track)
    if stale:
        changes.append(f'stale:{",".join(stale[:3])}')
        track['mutations'].append({'gen': gen, 'type': 'stale_force', 'detail': stale})

    self_m = _self_mutate_explorer(gen)
    if self_m:
        changes.append('self_mutate')

    hashes = {}
    for m in _modules():
        path = os.path.join(MOD, m)
        hashes[m] = _hash(path)
    g_str = str(gen)
    if g_str not in track['generations']:
        track['generations'][g_str] = {}
    track['generations'][g_str].update(hashes)
    _save_track(track)

    result = f'[explorer] gen={gen} changes={changes} elapsed={time.time()-start:.2f}s'
    genome['_explorer_result'] = result
    genome['_explorer_changes'] = changes
    genome['_explorer_mutated_count'] = len(changes)
    _sg(genome)
    return result
