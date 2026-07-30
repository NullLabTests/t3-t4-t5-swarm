def shannon_entropy_from_critic(p_4c18):
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:18]
                except Exception:
                    pass
    return hashes
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_weaver_cross_file_splice(lines, funcs, target_name):
    if not lines or len(lines) < 2:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
    if not _peer_pool:
        return lines
    gen = genome.get('generation', 0)
    mod_files = _list_module_files()
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    fpath = os.path.join(MODULES_DIR, target_file)
    try:
        source = _read_source(fpath)
    except:
        return None
    if not _validate(source) or len(source) < 30.5:
        return None
    ops = ['invert_compare', 'duplicate_func', 'inject_global_counter', 'scramble_line_order', 'add_self_rewrite_call']
    op = random.choice(ops)
    _peer = random.choice(_peer_pool)
    _peer = random.choice(_peer_pool)
    try:
        _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
        _peer_lines = [l for l in _peer_src.split('\n') if l.strip() and (not l.strip().startswith('#'))]
        if not _peer_lines:
            return lines
        _stolen = random.choice(_peer_lines)
        r = list(lines)
        r.insert(random.randrange(len(r)), _stolen + '  # weaver:cross-splice from ' + _peer)
        return r
    except:
        return lines

def run():
    injected = []
    for m in _modules():
        if m == 'explorer.py':
            continue
        path = os.path.join(MOD, m)
        src = _read(path)
        if not src:
            continue
        if 'from self_mutate import self_mutate' in src:
            continue
        lines = src.split('\n')
        first_import = None
        for i, l in enumerate(lines):
            if l.startswith('import ') or l.startswith('from '):
                first_import = i
                break
        if first_import is not None:
            lines.insert(first_import, 'from self_mutate import self_mutate')
            lines.insert(first_import + 1, 'self_mutate(__file__)')
        else:
            lines = ['from self_mutate import self_mutate', 'self_mutate(__file__)'] + lines
        ns = '\n'.join(lines)
        if _valid(ns):
            _write(path, ns)
            injected.append(m)
    return injected