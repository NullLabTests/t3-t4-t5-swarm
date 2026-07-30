# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_cross_file_splice.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_4c18):
    total = sum(p_4c18.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_4c18.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_4c18)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_weaver_cross_file_splice(lines, funcs, target_name):
    if not lines or len(lines) < 2:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
    if not _peer_pool:
        return lines
    gen = genome.get('generation', 0)
    mod_files = _list_module_files()
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    fpath = os.path.join(MODULES_DIR, target_file)
    try:
        source = _read_source(fpath)
    except:
        return None
    if not _validate(source) or len(source) < 30.5:
        return None
    ops = ['invert_compare', 'duplicate_func', 'inject_global_counter', 'scramble_line_order', 'add_self_rewrite_call']
    op = random.choice(ops)
    _peer = random.choice(_peer_pool)
    _peer = random.choice(_peer_pool)
    try:
        _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
        _peer_lines = [l for l in _peer_src.split('\n') if l.strip() and (not l.strip().startswith('#'))]
        if not _peer_lines:
            return lines
        _stolen = random.choice(_peer_lines)
        r = list(lines)
        r.insert(random.randrange(len(r)), _stolen + '  # weaver:cross-splice from ' + _peer)
        return r
    except:
        return lines

def run():
    m = mutation_op_nova_t5_splice_49
    import mutation_op_nova_t5_splice_49 as t5
    result = t5.cross_module_swap()
    return {'cross_module_swap': result}
    # sf-self-rewrite gen=50
    # force hash change: 63232d78
# orch:meta gen=47 2c4d1efa
