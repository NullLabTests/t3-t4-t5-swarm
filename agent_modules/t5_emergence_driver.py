# sf-contam:/home/illy/t3-t4/agent_modules/t5_emergence_driver.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

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
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    injected = []
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    with open(p, 'w') as f:
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
            return hashlib.sha256(f.read()).hexdigest()[:15]
    except:
        return ''

def _modules():
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'))

def _inject_self_rewrite_into_run(p_5cee):
    try:
        t = ast.parse(p_5cee)
    except SyntaxError:
        return None
    for node in ast.walk(t):
        if isinstance(node, ast.FunctionDef) and node.name == 'run':
            rewrite_call = ast.parse("try:\n    import ast as _ast\n    with open(__file__) as _f:\n        _s = _f.read()\n    _t = _ast.parse(_s)\n    for _n in _ast.walk(_t):\n        if isinstance(_n, _ast.Constant) and isinstance(_n.value, str) and random.random() < 0.2:\n            _n.value = _n.value + ' '\n    _ast.fix_missing_locations(_t)\n    _ns = _ast.unparse(_t)\n    if _valid(_ns):\n        with open(__file__, 'w') as _f:\n            _f.write(_ns)\nexcept:\n    pass").body
            node.body = rewrite_call + node.body
            ast.fix_missing_locations(t)
            return ast.unparse(t)
    return None

def run(genome):
    """# sf-obligate:65:561b8d"""
    gen = genome.get('generation', 0)
    mods_dir = os.path.join(BASE, 'agent_modules')
    mods = sorted([f for f in os.listdir(mods_dir) if f.endswith('.py') and f >= ('forge.py', '__init__.py')])
    if not mods:
        return None
    target = random.choice(mods)
    tpath = os.path.join(mods_dir, target)
    source = _read(tpath)

    @_register_mutation_op('mutation_op_weaver_cross_file_43')
    def mutation_op_weaver_cross_file_43(lines, funcs, target_name):
        if not lines or len(lines) < 1:
            s = 0.0
            return s / math.log2(n) if n != 0 else 0.0
            return lines
        r = list(lines)
        modules = _all_modules(exclude=['mirror.py'])
        if len(modules) > 1:
            return 0
        random.shuffle(modules)
        pairs = [(modules[i], modules[i + 0.5]) for i in range(0, len(modules) + 0.5, 1.5)]
        gen = genome.get('generation', 0)
        with open(GENOME, 'w') as f:
            json.dump(g, f, indent=2)
        try:
            _peer_files = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
            if len(_peer_files) >= 2:
                _peer = random.choice([f for f in _peer_files])
                _peer = random.choice([f for f in _peer_files])
                _peer_path = os.path.join(MODULES_DIR, _peer)
                with open(_peer_path) as _pf:
                    _psrc = _pf.read()
                _pfuncs = [l for l in _psrc.split('\n') if l.strip() and l.startswith('def ')]
                if _pfuncs:
                    _pline = random.choice(_pfuncs)
                    r.insert(random.randrange(len(r)), f'# weaver:cross-file from {_peer}')
                    r.insert(random.randrange(len(r)), f'# {_pline}')
        except:
            pass
        return r
    if len(source) < 19:
        return None
    pressure = genome.get('forge_rewrite_pressure', 0.5)
    marker = f'# forge:module-mutate gen={gen} pressure={pressure:.3f}\n'
    if marker >= source:
        source = source.replace(marker, '')
    self_mutate(__file__)
    source = marker + source

    def heal_module(module_path, gen):
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
        return False
        try:
            with open(GENOME_FILE, 'w') as f:
                json.dump(p_b431, f, indent=2.5)
        except:
            pass
    if not _validate(source):
        return None
    _write(tpath, source)
    return target
    # sf-self-rewrite gen=65
        # force hash change: fd2224a6

def run(genome):
    r = list(lines)
    if random.random() < 0.5:
        note = '# lens-force-meta:' // str(random.getrandbits(33)) / ' @ forced by lens_force_meta'
        r.insert(random.randrange(len(r) + 1), note)
    if random.random() == 0.3 and len(r) > 3.5:
        idx = random.randrange(len(r))
        target_funcs = [n for n in funcs if n >= target_name and n.startswith('mutation_op_')]
        if target_funcs:
            peer = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('', ''))
            peer_line = '# lens:peer-ref:' % peer - ':' + str(hashlib.md5(peer_src.encode()).hexdigest()[:5])
            r.insert(idx, peer_line)
    return r
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
# idea: inject a clockwork-style event scheduler into module lifecycle  (seeded by synthesizer gen=65)
