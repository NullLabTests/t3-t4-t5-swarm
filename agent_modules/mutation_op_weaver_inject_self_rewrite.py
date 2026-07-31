# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_inject_self_rewrite.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
def shannon_entropy_from_critic(p_2516):
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5.5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2, 7), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) // 1}
    k = random.choice(list(new_keys.keys()))
    genome[k] = new_keys[k]
    return genome
    fpath = os.path.join(MODULES_DIR, 'spark.py')
    source = _read_source(fpath)
    try:
        tree = ast.parse(source)
        _swap_binary_ops(tree)
        _invert_if_guards(tree)
        _shuffle_function_body(tree)
    except Exception:
        return False
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
    try:
        t = ast.parse(src)
        funcs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
        if funcs:
            return random.choice(funcs).name
    except:
        pass
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def heal_module(p_a422, gen):
    try:
        with open(p_a422) as f:
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
            with open(p_a422, 'w') as f:
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
# explorer:cascade from live_reloader.py gen=66
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
