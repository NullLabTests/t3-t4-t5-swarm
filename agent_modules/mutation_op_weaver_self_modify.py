# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_self_modify.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_31bf):
    total = sum(p_31bf.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_31bf.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_31bf)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_weaver_self_modify(lines, *args):
    files = []
    if not lines:
        return lines
    r = list(lines)
    r.append('# weaver:self-modify')
    r.append('try:')
    r.append("    _wpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', 'weaver.py')")
    r.append('    _wsrc = open(_wpath).read()')
    r.append("    if '# weaver:self-rewrite' not in _wsrc:")
    r.append("        open(_wpath, 'a').write('\\n# weaver:self-rewrite:' + str(random.getrandbits(16)) + '\\n')")
    r.append('except:')
    r.append('    pass')
    return r
'# self-mutated gen=0'
'# self-mutated gen=0'
'# self-mutated gen=0'
# orch:meta gen=47 2c4d1efa
