# sf-contam:/home/illy/t3-t4/agent_modules/rewrite_orchestrator.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
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
    dead = []
    dead = []
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p_8d76, p_8f9c):
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
    gen = genome.get('generation', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'genforce.py')]
    "T5 emergence: rewrites a random peer module's source every call,\n    cross-pollinating function signatures between modules."
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
    # sf-self-rewrite gen=65
        # force hash change: 76a32cc3

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
try:
    _explorer_force_self_rewrite_66()
except:
    pass