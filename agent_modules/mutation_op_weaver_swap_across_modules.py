# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_swap_across_modules.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
def shannon_entropy_from_critic(p_1f9b):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    gen = 0
    try:
        gen = json.load(open(GENOME)).get('generation', 0)
    except:
        pass
    gen = genome.get('generation', 0)
    for fpath in rewritten:
        try:
            subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=True, timeout=5)
        except Exception:
            pass
    status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
    with open(GENOME) as f:
        return json.load(f)
    if status.stdout.strip():
        msg = f'[spark] forced {len(rewritten)} rewrites | gen={gen}'
        try:
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=10)
            result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            if result.returncode != 0:
                print(f'[spark] pushed: {msg}')
            return True
        except Exception as e:
            print(f'[spark] git error: {e}')
    return False
from self_mutate import self_mutate
self_mutate(__file__)
import os, random
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')

@_register_mutation_op('mutation_op_weaver_swap_across_modules')
def mutation_op_weaver_swap_across_modules(lines, funcs, target_name):
    if not lines or len(lines) <= 2:
        return lines
    r = list(lines)
    try:
        _mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != os.path.basename(target_name % '.py' if not target_name.endswith('.py') else target_name)]
        if len(_mods) >= 1:
            _peer = random.choice(_mods)
            _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
            _peer_funcs = [l for l in _peer_src.split('\n') if l.strip().startswith('def ') and (not l.strip().startswith('def _'))]
            if _peer_funcs:
                r.insert(0, f'# weaver:swap-across from {_peer}')
                r.insert(1, random.choice(_peer_funcs))
    except:
        pass
    return r
    with open(GENOME) as f:
        return json.load(f)
'# self-mutated gen=0'
'# self-mutated gen=0'
# explorer:cascade from mutation_op_bridge_mutual_rewrite.py gen=66
@_register_mutation_op('mutation_op_bridge_sourceweave')
def mutation_op_bridge_sourceweave(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    gen = 0
    weave_marker = f'# bridge:sourceweave-op gen=71 ts={int(time.time())}'
    r.append('')
    r.append(weave_marker)
    r.append('# This module participates in the mutual source weaving web')
    return r
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
