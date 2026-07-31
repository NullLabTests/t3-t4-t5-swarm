import os, random, ast, json, hashlib, copy
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _g():
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}

def _sg(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _modules():
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'])

def _hash(p):
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:12]
    except:
        return ''

def _full_cross_splice_pairs(gen):
    """N×N complete graph: every pair (src,dst) splices one function body"""
    mods = _modules()
    if len(mods) < 2:
        return []
    pairs = []
    all_hashes = {m: _hash(os.path.join(MOD, m)) for m in mods}
    for src_name in mods:
        spath = os.path.join(MOD, src_name)
        ssrc = _read(spath)
        if not ssrc:
            continue
        try:
            sat = ast.parse(ssrc)
        except SyntaxError:
            continue
        sfuncs = [n for n in ast.walk(sat) if isinstance(n, ast.FunctionDef)]
        if not sfuncs:
            continue
        for dst_name in mods:
            if dst_name == src_name:
                continue
            dpath = os.path.join(MOD, dst_name)
            dsrc = _read(dpath)
            if not dsrc:
                continue
            try:
                dat = ast.parse(dsrc)
            except SyntaxError:
                continue
            dfuncs = [n for n in ast.walk(dat) if isinstance(n, ast.FunctionDef) and n.name != 'run']
            if not dfuncs:
                continue
            sf = random.choice(sfuncs)
            df = random.choice(dfuncs)
            graft = copy.deepcopy(sf.body[:max(1, len(sf.body)//2)])
            sp = random.randint(0, len(df.body))
            df.body = df.body[:sp] + graft + df.body[sp:]
            try:
                ast.fix_missing_locations(dat)
                ns = ast.unparse(dat)
            except:
                continue
            if _valid(ns):
                _write(dpath, ns)
                pairs.append('%s:%s->%s:%s' % (src_name, sf.name, dst_name, df.name))
    return pairs

def _force_every_module_ast_operator_mutate(gen):
    """Guaranteed AST operator mutation in every module"""
    mutated = 0
    op_swaps = {ast.Add: ast.Sub, ast.Sub: ast.Mult, ast.Mult: ast.Div, ast.Div: ast.FloorDiv,
                ast.FloorDiv: ast.Mod, ast.Mod: ast.Pow, ast.Pow: ast.Add,
                ast.Eq: ast.NotEq, ast.NotEq: ast.Lt, ast.Lt: ast.Gt, ast.Gt: ast.LtE,
                ast.LtE: ast.GtE, ast.GtE: ast.Eq, ast.And: ast.Or, ast.Or: ast.And}
    for m in _modules():
        p = os.path.join(MOD, m)
        s = _read(p)
        if not s:
            continue
        try:
            t = ast.parse(s)
        except SyntaxError:
            continue
        changed = False
        for n in ast.walk(t):
            if isinstance(n, ast.BinOp):
                op_type = type(n.op)
                if op_type in op_swaps:
                    n.op = op_swaps[op_type]()
                    changed = True
            elif isinstance(n, ast.Compare) and len(n.ops) == 1:
                op_type = type(n.ops[0])
                if op_type in op_swaps:
                    n.ops[0] = op_swaps[op_type]()
                    changed = True
            elif isinstance(n, ast.BoolOp):
                op_type = type(n.op)
                if op_type in op_swaps:
                    n.op = op_swaps[op_type]()
                    changed = True
            elif isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.25:
                n.value = type(n.value)(n.value * random.choice([0.5, 1.5, 2.0]))
                changed = True
        if changed:
            try:
                ast.fix_missing_locations(t)
                ns = ast.unparse(t)
                if _valid(ns):
                    _write(p, ns)
                    mutated += 1
            except:
                pass
    return mutated

def run(genome):
    gen = genome.get('generation', 0) + 1
    changes = []
    pairs = _full_cross_splice_pairs(gen)
    if pairs:
        changes.append('fullcross:%d' % len(pairs))
    ast_op = _force_every_module_ast_operator_mutate(gen)
    if ast_op:
        changes.append('astop:%d' % ast_op)
    g = _g()
    g['_explorer_full_cross_%d' % gen] = {'pairs': len(pairs), 'ast_ops': ast_op, 'gen': gen}
    g['generation'] = gen
    for k, v in genome.items():
        if k.startswith('_explorer_full_cross'):
            g[k] = v
    _sg(g)
    return '[full-cross] gen=%d changes=%s ev=%s' % (gen, '+'.join(changes) if changes else 'none', genome.get('emergence_velocity', 0))
