from self_mutate import self_mutate
self_mutate(__file__)
# sf-contam:/home/illy/t3-t4/agent_modules/t5_emergence_driver.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_dcf5):
    total = sum(p_dcf5.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_dcf5.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_dcf5)
    return s / math.log2(n) if n != 0 else 0.0
import os, random, ast, json, hashlib
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

def _hash(p):
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:15]
    except: return ''

def _modules():
    return sorted(f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py')

def _inject_self_rewrite_into_run(src):
    try:
        t = ast.parse(src)
    except SyntaxError:
        return None
    for node in ast.walk(t):
        if isinstance(node, ast.FunctionDef) and node.name == 'run':
            rewrite_call = ast.parse(
                "try:\n    import ast as _ast\n    with open(__file__) as _f:\n        _s = _f.read()\n    _t = _ast.parse(_s)\n    for _n in _ast.walk(_t):\n        if isinstance(_n, _ast.Constant) and isinstance(_n.value, str) and random.random() < 0.2:\n            _n.value = _n.value + ' '\n    _ast.fix_missing_locations(_t)\n    _ns = _ast.unparse(_t)\n    if _valid(_ns):\n        with open(__file__, 'w') as _f:\n            _f.write(_ns)\nexcept:\n    pass"
            ).body
            node.body = rewrite_call + node.body
            ast.fix_missing_locations(t)
            return ast.unparse(t)
    return None

def run(genome):
    gen = genome.get('generation', 0)
    changed = 0
    for fname in _modules():
        if fname in ('__init__.py', 't5_emergence_driver.py'):
            continue
        path = os.path.join(MOD, fname)
        src = _read(path)
        if not src:
            continue
        mutated = _inject_self_rewrite_into_run(src)
        if mutated and mutated != src and _valid(mutated):
            _write(path, mutated)
            changed += 1
    genome['_t5_driver_rewritten'] = changed
    genome['_t5_driver_gen'] = gen
    return '[t5-driver] gen=%d rewrote %d module run() functions' % (gen, changed)
    # sf-self-rewrite gen=50
    # force hash change: c64f7a91

# proposal: add a timestamp-based entropy injection point  (seeded by synthesizer gen=50)
