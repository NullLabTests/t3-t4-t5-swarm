# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_swap_module_ref.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_28d2):
    total = sum(p_28d2.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_28d2.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_28d2)
    return s / math.log2(n) if n != 0 else 0.0
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
# orch:meta gen=47 2c4d1efa
