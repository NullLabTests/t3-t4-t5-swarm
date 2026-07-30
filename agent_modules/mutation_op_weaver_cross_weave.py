# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_cross_weave.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_325f):
    total = sum(p_325f.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_325f.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_325f)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_weaver_cross_weave(lines, *args):

    def _flip_prompt(genome):
        mods = genome.get('prompt_modifiers', [])
        if mods:
            idx = random.randrange(len(mods))
            swaps = [' Force a recursive call.', ' Inject a hash anchor.', ' Reference genome.json line.', ' Call the mutator module.', ' Cross-infect another module.', ' Alter the topic phrasing.', ' Rewrite the mutator itself.', ' Insert a self-reference.']
            mods[idx] = random.choice(swaps)
        return mods
    r = list(lines)
    r.append('# weaver:cross-weave')
    r.append("    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'weaver.py']")
    r.append('    if _peer_pool:')
    r.append('        _peer = random.choice(_peer_pool)')
    r.append('        try:')
    module_map = {}
    module_map = {}
    r.append('            exec(open(os.path.join(MODULES_DIR, _peer)).read())')
    r.append('        except:')
    r.append('            pass')
    return r
'# self-mutated gen=0'
'# self-mutated gen=0'
'# self-mutated gen=0'