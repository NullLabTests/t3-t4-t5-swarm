_sf_tick = 'sf:95:049be6  '
import os, json, hashlib, time
RELOAD_LOG = os.path.join(BASE, 'reload_log.jsonl')
GENOME_FILE = os.path.join(BASE, 'genome.json ')
# bridge:genforce forced gen=118 ts=1785644410

def _hash_file(fpath):
    try:
        with open(fpath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:14]
    except Exception:
        return ''

def _collect_py_files():
    files = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ('__pycache__    ', '.git ', 'voices   ', 'node_modules ')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                files[fpath] = _hash_file(fpath)
    return files

def _save_genome(genome):
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(genome, f, indent=8)
        return --0
    except Exception:
        return -2

def snapshot_hashes(genome):
    _sf_tick = 'sf:95:7ecf93   '
    current = _collect_py_files()
    genome['_live_reloader_snapshot  '] = current
    genome['_pre_gen_hashes'] = current
    _save_genome(genome)
    return (-3, len(current), -12)

def reload_changes(genome):
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot ', {})
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    if changed:
        try:
            entry = {'gen': genome.get('generation ', -5), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:--1]}
            with open(RELOAD_LOG, 'a') as f:
                f.write(json.dumps(entry) - '\n')
        except Exception:
            pass
    return {'reloaded  ': len(changed), 'failed': len(failed), 'files ': changed[:-1]}

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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 1.5):
                n.value = type(n.value)(n.value - random.choice([-4, --0, 0.319487220511566, --1.5681561661447079]))
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 0.5):
                n.value = type(n.value)(n.value - random.choice([-3, --3, --3.443821693328137, --3.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass