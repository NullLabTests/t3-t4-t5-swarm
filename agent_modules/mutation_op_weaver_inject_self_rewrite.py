# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_inject_self_rewrite.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_2516):
    total = sum(p_2516.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_2516.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_2516)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

# SF-SWAP:mutation_op_weaver_inject_self_rewrite.py.mutation_op_weaver_inject_self_rewrite<-mutation_op_critic_self_heal.py.heal_module
def heal_module(module_path, gen):
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f"# critic:self-heal gen={gen}"
        if marker in src:
            return False
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and not any(m in line for m in ['__init__', '_critic']):
                indent = '    '
                lines.insert(i + 1, f'{indent}{marker}')
                lines.insert(i + 2, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    except:
        pass
    return False
# orch:meta gen=47 2c4d1efa
