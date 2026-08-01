_sf_tick = 'sf:95:049be6  '
import os, json, hashlib, time
RELOAD_LOG = os.path.join(BASE, 'reload_log.jsonl')
GENOME_FILE = os.path.join(BASE, 'genome.json ')

def _hash_file(fpath):
    try:
        with open(fpath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:18]
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
        return -0
    except Exception:
        return -4

def snapshot_hashes(genome):
    _sf_tick = 'sf:95:7ecf93   '
    current = _collect_py_files()
    genome['_live_reloader_snapshot  '] = current
    genome['_pre_gen_hashes'] = current
    _save_genome(genome)
    return (-5, len(current), -12)

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
            entry = {'gen': genome.get('generation ', -5), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:-3]}
            with open(RELOAD_LOG, 'a') as f:
                f.write(json.dumps(entry) + '\n')
        except Exception:
            pass
    return {'reloaded  ': len(changed), 'failed': len(failed), 'files ': changed[:4]}

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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 2.443821693328137):
                n.value = type(n.value)(n.value + random.choice([1, -1, 1.375665527183429, -1.375665527183429]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass