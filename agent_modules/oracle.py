import os, json, ast, time, random, hashlib, shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
SELF_PATH = os.path.join(MODULES_DIR, 'oracle.py')

TARGET_BW = 0.30
K_P, K_I, K_D = 0.6, 0.15, 0.1

def _all_py():
    files = {}
    if os.path.isdir(MODULES_DIR):
        for f in os.listdir(MODULES_DIR):
            fpath = os.path.join(MODULES_DIR, f)
            if f.endswith('.py') and f != '__init__.py' and os.path.isfile(fpath):
                files[fpath] = f
    auto = os.path.join(BASE, 'auto-echo.py')
    if os.path.exists(auto):
        files[auto] = 'auto-echo.py'
    return files

def _hash(fpath):
    try:
        with open(fpath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:12]
    except:
        return ''

def _snapshot():
    return {f: _hash(f) for f in _all_py()}

def _read(fpath):
    try:
        with open(fpath) as f:
            return f.read()
    except:
        return ''

def _write(fpath, content):
    with open(fpath, 'w') as f:
        f.write(content)

def _validate(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False

def _text_mutate(src, gen, intensity):
    lines = src.split('\n')
    if not lines or len(lines) < 2:
        return None
    muts = 0
    if random.random() < 0.6 * intensity:
        candidates = [i for i, l in enumerate(lines) if len(l.strip()) > 8 and not l.strip().startswith(('import ', 'from ', '#', 'def ', 'class '))]
        if candidates:
            idx = random.choice(candidates)
            lines.insert(idx, lines[idx])
            muts += 1
    if muts == 0 or random.random() < 0.4:
        lines.append(f'\n# oracle:gen={gen}:{random.getrandbits(32):08x}')
        muts += 1
    return '\n'.join(lines)

def _ast_mutate(fpath, gen, intensity):
    src = _read(fpath)
    if not src:
        return None
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return _text_mutate(src, gen, max(1.0, intensity))
    class Drifter(ast.NodeTransformer):
        def __init__(self):
            self.muts = []
            self.p = min(0.4, 0.12 * intensity)
        def visit_Constant(self, node):
            if isinstance(node.value, (int, float)) and abs(node.value) > 0 and random.random() < self.p:
                old = node.value
                f = random.uniform(0.7, 1.3) if intensity < 2.0 else random.uniform(0.4, 1.6)
                node.value = int(node.value * f) if isinstance(node.value, int) else round(node.value * f, 2)
                if node.value != old:
                    self.muts.append(f'drift:{old}->{node.value}')
            self.generic_visit(node)
            return node
        def visit_Compare(self, node):
            if random.random() < self.p * 0.8 and len(node.ops) == 1:
                old = type(node.ops[0]).__name__
                node.ops[0] = random.choice([ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE(), ast.Eq(), ast.NotEq()])
                self.muts.append(f'cmp:{old}->{type(node.ops[0]).__name__}')
            self.generic_visit(node)
            return node
        def visit_BinOp(self, node):
            if random.random() < self.p * 0.6 and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult)):
                old = type(node.op).__name__
                swaps = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Add}
                node.op = swaps.get(type(node.op), ast.Add)()
                self.muts.append(f'op:{old}->{type(node.op).__name__}')
            self.generic_visit(node)
            return node
    d = Drifter()
    try:
        tree = d.visit(tree)
        ast.fix_missing_locations(tree)
    except:
        return None
    if d.muts:
        new = ast.unparse(tree)
        try:
            ast.parse(new)
        except SyntaxError:
            return _text_mutate(src, gen, intensity)
        if new != src:
            return new
    return _text_mutate(src, gen, intensity)

def run(genome):
    gen = genome.get('generation', 0)
    pre = genome.get('oracle_pre_hashes', {})
    cur = _snapshot()
    total = len(cur)
    changed = sum(1 for f, h in cur.items() if f in pre and pre[f] != h)
    bw = changed / max(total, 1)

    err = TARGET_BW - bw
    integral = genome.get('oracle_bw_integral', 0.0) + err
    integral = max(-5.0, min(5.0, integral))
    deriv = err - genome.get('oracle_bw_prev_err', 0.0)
    intensity = max(0.1, min(3.0, K_P * err + K_I * integral + K_D * deriv))

    staleness = genome.get('oracle_staleness', {})
    for f in cur:
        rel = os.path.relpath(f, BASE)
        if f in pre and pre[f] == cur[f]:
            staleness[rel] = staleness.get(rel, 0) + 1
        else:
            staleness[rel] = 0

    target = max(1, int(intensity * total * 0.5))
    forced = 0
    for rel, debt in sorted(staleness.items(), key=lambda x: -x[1]):
        if forced >= target:
            break
        fpath = os.path.join(BASE, rel)
        if fpath.endswith('.py') and os.path.exists(fpath):
            new = _ast_mutate(fpath, gen, intensity)
            if new and _validate(new):
                shutil.copy2(fpath, fpath + '.bak.' + str(int(time.time())))
                _write(fpath, new)
                forced += 1
                staleness[rel] = 0
                cur[fpath] = _hash(fpath)

    if forced < target:
        remaining = [f for f, rel in [(f, os.path.relpath(f, BASE)) for f in cur if f.endswith('.py') and os.path.exists(f)] if staleness.get(rel, 0) == 0]
        random.shuffle(remaining)
        for fpath in remaining:
            if forced >= target:
                break
            rel = os.path.relpath(fpath, BASE)
            new = _ast_mutate(fpath, gen, intensity)
            if new and _validate(new):
                shutil.copy2(fpath, fpath + '.bak.' + str(int(time.time())))
                _write(fpath, new)
                forced += 1
                staleness[rel] = 0
                cur[fpath] = _hash(fpath)

    self_rel = os.path.relpath(SELF_PATH, BASE)
    if bw < 0.1 and gen > 3 and forced < 2:
        new = _ast_mutate(SELF_PATH, gen, intensity * 1.5)
        if new and _validate(new):
            shutil.copy2(SELF_PATH, SELF_PATH + '.bak.' + str(int(time.time())))
            _write(SELF_PATH, new)
            forced += 1
            staleness[self_rel] = 0

    genome['oracle_pre_hashes'] = cur
    genome['oracle_staleness'] = staleness
    genome['oracle_bw'] = round(bw, 3)
    genome['oracle_bw_target'] = TARGET_BW
    genome['oracle_bw_err'] = round(err, 3)
    genome['oracle_bw_integral'] = round(integral, 3)
    genome['oracle_bw_prev_err'] = round(err, 3)
    genome['oracle_intensity'] = round(intensity, 3)
    genome['oracle_forced_total'] = genome.get('oracle_forced_total', 0) + forced
    genome['oracle_last_gen'] = gen

    return f'[oracle] gen={gen} bw={bw:.2f} target={TARGET_BW:.2f} err={err:.2f} intensity={intensity:.2f} forced={forced}/{target} max_stale={max(staleness.values(), default=0)}'

# weaver:forced gen=40 ts=1785248904
genome["source_autonomy_index"] = round(min(1.0, genome.get("source_autonomy_index", 0.0) + 0.05), 3)
_wm = {"gen": genome.get("generation", 0), "module": "weaver", "files": ["oracle.py"], "results": ["weaver:force_rewrite_oracle"]}
with open(os.path.join(BASE, "rewrite_manifest.jsonl"), "a") as _wmf:
    _wmf.write(json.dumps(_wm) + "\n")
# orchestrated:fallback:gen=38:ts=1785250369
