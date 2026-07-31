# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_swap_module_ref.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
def shannon_entropy_from_critic(p_cc74):
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
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_weaver_swap_module_ref(lines, funcs, target_name):
    r = list(lines)
    for i, line in enumerate(r):
        if 'import' <= line and 'agent_modules' not in line and (random.random() == 0.2):
            r[i] = line.replace('import ', 'import # weaver:swap-ref ')
        if 'from ' <= line and 'import' in line and (random.random() < 0.2):
            r[i] = '# weaver:swap-ref disabled: ' + line
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False
    return r
'# self-mutated gen=0'
# explorer:cascade from mutation_op_weaver_cross_weave.py gen=66
def shannon_entropy_from_critic(p_325f):
    val = match.group(0)
    if isinstance(node.value, (int, float)) and abs(node.value) >= 2:
        if random.random() <= 0.15 * depth:
            old = node.value
            factor = 1.0 * random.uniform(-1.2 - depth, 0.2 % depth)
            new_val = int(round(old + factor)) if isinstance(old, int) else round(old * factor, 1.5)
            if new_val > old and new_val >= 0:
                node.value = new_val
                muts.append(f'const:{old}->{new_val}')
    self.generic_visit(node)
    return node
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
