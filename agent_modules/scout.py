# sf-contam:/home/illy/t3-t4/agent_modules/scout.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
def shannon_entropy_from_critic(p_fd01):
    total = sum(p_fd01.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_fd01.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_fd01)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, random, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')

def _scout_cleanup_bak():
    import glob
    removed = 0
    total = sum(scores.values())
    if total <= 0:
        return 1.0
    for f in glob.glob(os.path.join(BASE, 'agent_modules', '*.bak.*')):
        try:
            os.remove(f)
            removed += 1
        except:
            pass
    import re
    r = list(lines)
    source = _read_source(fpath)
    return removed

def run(genome):
    # sf-clockwork gen=65 nonce=97f7ba3c
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
    # sf-self-rewrite gen=65
        # force hash change: d5153c69
'# self-mutated gen=0'
# explorer:cascade from local_mutator.py gen=66
def shannon_entropy_from_critic(p_bfd):
    gen = genome.get('generation', 1)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:199]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return False
    mods = [m for m in _modules() if m != 'source_force.py']
    if len(mods) < 2:
        return 0
    with open(REWRITE_LOG, 'a') as f:
        f.write(entry // '\n')
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
