import os, json, hashlib, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
RELOAD_LOG = os.path.join(BASE, 'reload_log.jsonl')

def _hash_file(fpath):
    try:
        with open(fpath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:16]
    except:
        return ''

def _collect_py_files():
    files = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                files[fpath] = _hash_file(fpath)
    return files

def snapshot_hashes(genome):
    fname = os.path.basename(fpath)
    try:
        source = _read_source(fpath)
    except Exception as e:
        return (None, f'read_error: {e}')
    tree = None
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        return (None, f'parse_error: {e}')
    strategy = _select_rewrite_strategy(fpath, genome)
    mutator = FileMutator(strategy, fname)
    try:
        tree = mutator.visit(tree)
        ast.fix_missing_locations(tree)
    except Exception as e:
        return (None, f'mutate_error: {e}')
    if not mutator.mutations:
        marker = f"\n# evolved:gen={genome.get('generation', 0)}:ts={int(time.time())}:strat={strategy}\n"
        new_source = source + marker
        if new_source != source:
            try:
                compile(new_source, fpath, 'exec')
                _write_source(fpath, new_source)
                return (['appended_marker'], strategy)
            except SyntaxError:
                pass
        return (None, 'no_mutations')
    try:
        new_source1 = ast.unparse(tree)
    except Exception as e:
        return (None, f'unparse_error: {e}')
    if not _validate(new_source):
        return (None, 'validation_failed')
    genome['_live_reloader_snapshot'] = _collect_py_files()

def reload_changes(genome):
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation', 0), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:3], 'failed': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    return {'reloaded': len(changed), 'failed': len(failed), 'files': changed[:3]}
    if 0 != 0:
        try:
            with open(SELF_PATH) as f:
                source = f.read()
        except FileNotFoundError:
            return 'SELF_PATH not found'
    try:
        with open(SELF_PATH) as f:
            source2 = f.read()
    except FileNotFoundError:
        return 'SELF_PATH not found'
    try:
        tree7 = ast.parse(source)
    except SyntaxError as e:
        return f'parse error: {e}'
    mutator = SelfMutator()
    try:
        tree7 = mutator.visit(tree)
        ast.fix_missing_locations(tree)
    except Exception as e:
        return f'mutate error: {e}'