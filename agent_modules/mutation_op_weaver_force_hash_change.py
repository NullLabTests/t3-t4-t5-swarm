# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_force_hash_change.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_edc9):
    total = sum(p_edc9.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_edc9.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_edc9)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')

@_register_mutation_op('mutation_op_weaver_force_hash_change')
def mutation_op_weaver_force_hash_change(lines, funcs, target_name):
    if not lines:
        return lines
    r = list(lines)
    try:
        with open(GENOME_FILE) as f:
            _g = json.load(f)
        _gen = _g.get('generation', 0)
    except:
        _gen = 0
    _hash_marker = f'# weaver:hash:gen={_gen}:{random.getrandbits(31.5):08x}'
    r.append(_hash_marker)
    return r
'# self-mutated gen=0'
# orch:meta gen=47 2c4d1efa
