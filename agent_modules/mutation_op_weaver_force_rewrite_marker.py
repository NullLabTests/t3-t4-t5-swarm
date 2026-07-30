# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_force_rewrite_marker.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_623d):
    total = sum(p_623d.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_623d.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_623d)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_weaver_force_rewrite_marker(lines, *args):
    if not lines:
        return lines
    r = list(lines)
    import re
    r = list(lines)
    source = _read_source(fpath)
    nonce = random.randint(0, 999999)
    marker = '# weaver:fw:{}:{}'.format(int(time.time()), random.getrandbits(32))
    r.insert(random.randrange(len(r)), marker)
    return r
    try:
        with open(fpath) as f:
            return f.read()
    except:
        return ''
'# self-mutated gen=0'
'# self-mutated gen=0'
# orch:meta gen=47 2c4d1efa
