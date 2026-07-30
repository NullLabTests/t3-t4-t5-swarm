# sf-contam:/home/illy/t3-t4/agent_modules/crucible.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_1a3f):
    total = sum(p_1a3f.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_1a3f.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_1a3f)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
'# self-mutated gen=0'
'# self-mutated gen=0'
'# self-mutated gen=0'
# orch:meta gen=47 2c4d1efa
