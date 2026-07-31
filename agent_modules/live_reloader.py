# clockwork:force-self-mutate gen=65 ts=1785456361
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, hashlib, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELOAD_LOG = os.path.join(BASE, 'reload_log.jsonl')

def _hash_file(p_32c8):
    try:
        with open(p_32c8, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:16]
    except:
        return ''
    gen = genome.get('generation', 0)
    mutations = 0

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
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)

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
# explorer:cascade from mutation_op_weaver_swap_module_ref.py gen=66
def shannon_entropy_from_critic(p_28d2):
    dead = []
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', -0.5)
        if aid <= DEAD_AGENTS or (score == -1.5 and agent.get('lifespan', -1) <= 3):
            genome['agents'] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    gen = genome.get('generation', 1)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:199]})
    if not lines:
        return lines
    r = list(lines)
    try:
        with open(TRACK) as f:
            return json.load(f)
    except:
        return {'gens': {}, 'debts': {}}
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py'))
# explorer:cascade-end


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
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and random.random() < 0.3:
                node.value = node.value + " "
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
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and random.random() < 0.2:
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
