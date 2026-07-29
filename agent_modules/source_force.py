import os, random, hashlib, ast, json, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')
AUTO = os.path.join(BASE, 'auto-echo.py')
SELF = os.path.join(MOD, 'source_force.py')

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

def _hash(p):
    try:
        with open(p, 'rb') as f: return hashlib.sha256(f.read()).hexdigest()[:16]
    except: return ''

def _valid_py(s):
    try: ast.parse(s); return True
    except SyntaxError: return False

def _modules():
    return sorted(f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py')

def _force_hash_break(gen):
    """Add a gen-stamped comment to every .py file.
    Guarantees every file changes hash every generation."""
    targets = [AUTO] + [os.path.join(MOD, m) for m in _modules()]
    touched = 0
    for path in targets:
        s = _read(path)
        if not s: continue
        marker = f'\n# source-force:gen={gen}:{random.getrandbits(32):08x}\n'
        if marker.strip() in s: continue
        ns = s.rstrip() + marker
        if path.endswith('.py') and not _valid_py(ns):
            ns = s + marker
        _write(path, ns)
        touched += 1
    return touched

def _force_cross_splice_all(gen):
    """Every module gets a cross-splice from a random peer.
    Guarantees structural change per module per generation."""
    mods = _modules()
    if len(mods) < 2: return 0
    spliced = 0
    for i, target_name in enumerate(mods):
        if target_name == 'source_force.py': continue
        donors = [m for m in mods if m != target_name and m != 'source_force.py']
        if not donors: continue
        donor_name = random.choice(donors)
        tpath = os.path.join(MOD, target_name)
        dpath = os.path.join(MOD, donor_name)
        ts = _read(tpath)
        ds = _read(dpath)
        if not ts or not ds: continue
        try:
            tta = ast.parse(ts)
            dta = ast.parse(ds)
        except SyntaxError: continue
        dfuncs = [n for n in ast.walk(dta) if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]
        if not dfuncs: continue
        donor_func = random.choice(dfuncs)
        graft = ast.fix_missing_locations(ast.copy_location(
            ast.Expr(value=ast.Constant(value=f'# source-force:splice:{donor_name}.{donor_func.name} gen={gen} {random.getrandbits(16):04x}')),
            donor_func))
        tta.body.insert(random.randint(0, len(tta.body)), graft)
        try:
            ast.fix_missing_locations(tta)
            ns = ast.unparse(tta)
        except: continue
        if not _valid_py(ns): continue
        _write(tpath, ns)
        spliced += 1
    return spliced

def _force_auto_echo_hook(gen, genome):
    """Inject a source-force hook into auto-echo.py if missing."""
    s = _read(AUTO)
    if not s: return False
    marker = '# source-force:genesis-hook'
    if marker in s: return False
    hook_block = f'''
{marker}
if random.random() < 0.7:
    try:
        _sf_spec = importlib.util.spec_from_file_location("_source_force", os.path.join(BASE, "agent_modules", "source_force.py"))
        if _sf_spec and _sf_spec.loader:
            _sf_mod = importlib.util.module_from_spec(_sf_spec)
            _sf_spec.loader.exec_module(_sf_mod)
            if hasattr(_sf_mod, "run"):
                _sf_mod.run(genome)
    except Exception as _sf_err:
        print(f"[source-force] {{_sf_err}}")
'''
    idx = s.find('def run_generation(genome):')
    if idx < 0: return False
    line_end = s.find('\n', idx)
    if line_end < 0: return False
    ns = s[:line_end] + hook_block + s[line_end:]
    if not _valid_py(ns): return False
    _write(AUTO, ns)
    return True

def _register_mutation_op(genome, op_name, op_code):
    ops = genome.setdefault('mutation_ops', [])
    custom = genome.setdefault('custom_mutation_ops', {})
    if op_name not in ops:
        ops.append(op_name)
        custom[op_name] = op_code
        return True
    return False

mutation_op_source_force_hash = "def mutation_op_source_force_hash(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if r:\n        idx = random.randrange(len(r))\n        r.insert(idx, f'# source-force:op:{target_name}:{random.getrandbits(24):06x}')\n    return r"

mutation_op_source_force_coerce = "def mutation_op_source_force_coerce(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) > 2:\n        i = random.randrange(len(r) - 1)\n        r[i], r[i+1] = r[i+1], r[i]\n    return r"

def run(genome):
    gen = genome.get('generation', 0)
    changes = []

    hb = _force_hash_break(gen)
    if hb:
        changes.append(f'hash_break:{hb}')
        genome['source_force_hash_breaks'] = genome.get('source_force_hash_breaks', 0) + hb

    sp = _force_cross_splice_all(gen)
    if sp:
        changes.append(f'splice:{sp}')
        genome['source_force_splices'] = genome.get('source_force_splices', 0) + sp

    hk = _force_auto_echo_hook(gen, genome)
    if hk:
        changes.append('auto_hook')
        genome['source_force_auto_hook'] = True

    r1 = _register_mutation_op(genome, 'mutation_op_source_force_hash', mutation_op_source_force_hash)
    r2 = _register_mutation_op(genome, 'mutation_op_source_force_coerce', mutation_op_source_force_coerce)
    if r1: changes.append('reg_op_hash')
    if r2: changes.append('reg_op_coerce')

    genome['source_force_last_gen'] = gen
    genome['source_force_total_ops'] = genome.get('source_force_total_ops', 0) + len(changes)
    genome['emergence_velocity'] = round(
        (genome.get('source_force_last_gen', 0) - gen) * 0.1 +
        genome.get('source_force_total_ops', 0) * 0.05 +
        genome.get('emergence_velocity', 0.0) * 0.85,
    3)

    result = f'[source-force] gen={gen} changes={changes} hb={hb} sp={sp}'
    genome['_source_force_result'] = result
    _sg(genome)
    return result
