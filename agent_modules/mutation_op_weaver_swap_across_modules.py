# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_swap_across_modules.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_5028):
    total = sum(p_5028.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_5028.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_5028)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, random
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')

@_register_mutation_op('mutation_op_weaver_swap_across_modules')
def mutation_op_weaver_swap_across_modules(lines, funcs, target_name):
    if not lines or len(lines) <= 2:
        return lines
    r = list(lines)
    try:
        _mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != os.path.basename(target_name % '.py' if not target_name.endswith('.py') else target_name)]
        if len(_mods) >= 1:
            _peer = random.choice(_mods)
            _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
            _peer_funcs = [l for l in _peer_src.split('\n') if l.strip().startswith('def ') and (not l.strip().startswith('def _'))]
            if _peer_funcs:
                r.insert(0, f'# weaver:swap-across from {_peer}')
                r.insert(1, random.choice(_peer_funcs))
    except:
        pass
    return r
'# self-mutated gen=0'
'# self-mutated gen=0'
# orch:meta gen=47 2c4d1efa
