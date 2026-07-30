def shannon_entropy_factor(p_a2b3):
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < 0.25:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    return 0
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, ast, hashlib, copy
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
    with open(p, 'w') as f:
        f.write(s)

def _hash(p):
    try:
        with open(p, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()[:12]
    except:
        return ''

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _load_genome():
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}

def _save_genome(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)

def _all_ops():
    return sorted(f for f in os.listdir(MOD) if f.startswith('mutation_op_') and f.endswith('.py'))

def run(genome):
    g = genome if genome else _load_genome()
    gen = g.get('generation', 0)
    tracking = g.setdefault('operator_tracking', {})
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev = tracking.get(fname, {})
        if prev.get('hash', '') and prev['hash'] != h:
            tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', 0) + 1, 'successes': prev.get('successes', 0) + 1}
            tracking[fname]['mutated_gen'] = gen
        else:
            tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', 1), 'successes': prev.get('successes', 0)}
    total = len(tracking)
    pruned = 0
    if total >= 8 and random.random() < 0.2:
        sorted_by_rate = sorted(tracking.items(), key=lambda kv: kv[1].get('successes', 0) / max(kv[1].get('attempts', 1), 1))
        kill_list = sorted_by_rate[:max(1, total // 8)]
        os.makedirs(os.path.join(MOD, '_pruned'), exist_ok=True)
        for name, _ in kill_list:
            src_path = os.path.join(MOD, name)
            dst_path = os.path.join(MOD, '_pruned', name)
            if os.path.exists(src_path) and not os.path.exists(dst_path):
                os.rename(src_path, dst_path)
                pruned += 1
    cross_spawned = 0
    if total >= 4 and random.random() < 0.15:
        alive = [f for f in _all_ops() if not tracking.get(f, {}).get('pruned', False)]
        if len(alive) >= 3:
            a_name, b_name = random.sample(alive, 2)
            a_src = _read(os.path.join(MOD, a_name))
            b_src = _read(os.path.join(MOD, b_name))
            if a_src and b_src:
                try:
                    a_t = ast.parse(a_src)
                    b_t = ast.parse(b_src)
                    a_funcs = [n for n in ast.walk(a_t) if isinstance(n, ast.FunctionDef)]
                    b_funcs = [n for n in ast.walk(b_t) if isinstance(n, ast.FunctionDef)]
                    if a_funcs and b_funcs:
                        child_name = f'mutation_op_crucible_cross_gen{gen}_{random.getrandbits(16):04x}'
                        child_path = os.path.join(MOD, child_name + '.py')
                        combined = ast.unparse(random.choice(a_funcs)) + '\n\n' + ast.unparse(random.choice(b_funcs))
                        header = f'from self_mutate import self_mutate\nself_mutate(__file__)\nimport os,random,json,ast\n'
                        child_src = header + '\n' + combined
                        if _valid(child_src):
                            _write(child_path, child_src)
                            g.setdefault('mutation_ops', []).append(child_name)
                            cross_spawned += 1
                except:
                    pass
    g['operator_crucible_pruned'] = g.get('operator_crucible_pruned', 0) + pruned
    g['operator_crucible_crossed'] = g.get('operator_crucible_crossed', 0) + cross_spawned
    _save_genome(g)
    return {'pruned': pruned, 'cross_spawned': cross_spawned}
