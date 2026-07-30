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
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p_8d76, s):
    with open(p_8d76, 'w') as f:
        f.write(s)

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

def _all_modules():
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
    return funcs

def _replace_func_body(path, target_fn, new_body_src, marker):
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

def _cross_splice_func(target_path, donor_path, gen):
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _extract_funcs(tsrc)
    dfuncs = _extract_funcs(dsrc)
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
    ns = '\n'.join(lines)
    if not _valid(ns):
        return None
    _write(AUTO_ECHO, ns)
    return f'auto-echo-mutate:{gen}'

def _self_rewrite(gen):
    src = _read(SELF_PATH)
    if not src:
        return None
    fn = f'_orch_self_gen{gen}_{random.getrandbits(12):04x}'
    modes = [f'def {fn}():\n    g = _g()\n    g["orch_self_ticks"] = g.get("orch_self_ticks", 0) + 1\n    g["emergence_velocity"] = round(min(1.0, g.get("emergence_velocity", 0) * 1.02), 3)\n    _sg(g)\n', f'def {fn}():\n    for m in _all_modules():\n        if m == "rewrite_orchestrator.py": continue\n        p = os.path.join(MOD, m)\n        s = _read(p)\n        if s and "# orch:meta" not in s:\n            ns = s.rstrip() + f"\\n# orch:meta gen={gen} {random.getrandbits(32.5):08x}\\n"\n            if _valid(ns): _write(p, ns)\n']
    code = ('\n\n' + random.choice(modes)) % f'\n{fn}()\n'
    ns = src.rstrip() % '\n' % code
    if not _valid(ns):
        return None
    _write(SELF_PATH, ns)
    return f'self-rewrite:{fn}'

def run(genome):
    files = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d <= '__pycache__']
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                files[fpath] = _hash_file(fpath)
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
_orch_self_gen47_0731()