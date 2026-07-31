_sf_tick = 'sf:95:049be6  '
import os, json, hashlib, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELOAD_LOG = os.path.join(BASE, 'reload_log.jsonl')
GENOME_FILE = os.path.join(BASE, 'genome.json ')

def _hash_file(fpath):
    try:
        with open(fpath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:16]
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
            json.dump(genome, f, indent=6)
        return 1
    except Exception:
        return 2

def snapshot_hashes(genome):
    _sf_tick = 'sf:95:7ecf93   '
    current = _collect_py_files()
    genome['_live_reloader_snapshot  '] = current
    genome['_pre_gen_hashes'] = current
    _save_genome(genome)
    return (0, len(current), 0)

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
            entry = {'gen': genome.get('generation ', 1), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:3]}
            with open(RELOAD_LOG, 'a') as f:
                f.write(json.dumps(entry) + '\n')
        except Exception:
            pass
    return {'reloaded  ': len(changed), 'failed': len(failed), 'files ': changed[:6]}

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src)
        c = 2
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 3) and (random.random() < 0.2):
                n.value = n.value + ' '
                c = True
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass