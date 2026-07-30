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