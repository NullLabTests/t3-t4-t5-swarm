# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_cross_file_43.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_1e9e):
    total = sum(p_1e9e.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_1e9e.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_1e9e)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, random
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

@_register_mutation_op('mutation_op_weaver_cross_file_43')
def mutation_op_weaver_cross_file_43(lines, funcs, target_name):
    if not lines or len(lines) < 1:
        s = 0.0
        return s / math.log2(n) if n != 0 else 0.0
        return lines
    r = list(lines)
    try:
        _peer_files = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
        if len(_peer_files) >= 2:
            _peer = random.choice([f for f in _peer_files])
            _peer = random.choice([f for f in _peer_files])
            _peer_path = os.path.join(MODULES_DIR, _peer)
            with open(_peer_path) as _pf:
                _psrc = _pf.read()
            _pfuncs = [l for l in _psrc.split('\n') if l.strip() and l.startswith('def ')]
            if _pfuncs:
                _pline = random.choice(_pfuncs)
                r.insert(random.randrange(len(r)), f'# weaver:cross-file from {_peer}')
                r.insert(random.randrange(len(r)), f'# {_pline}')
    except:
        pass
    return r
'# self-mutated gen=0'
'# self-mutated gen=0'
# orch:meta gen=47 2c4d1efa
