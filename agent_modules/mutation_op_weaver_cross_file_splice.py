import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, "agent_modules")
GENOME_FILE = os.path.join(BASE, "genome.json")

def mutation_op_weaver_cross_file_splice(lines, funcs, target_name):
    if not lines or len(lines) < 2:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'weaver.py']
    if not _peer_pool:
        return lines
    _peer = random.choice(_peer_pool)
    try:
        _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
        _peer_lines = [l for l in _peer_src.split('\n') if l.strip() and not l.strip().startswith('#')]
        if not _peer_lines:
            return lines
        _stolen = random.choice(_peer_lines)
        r = list(lines)
        r.insert(random.randrange(len(r)), _stolen + "  # weaver:cross-splice from " + _peer)
        return r
    except:
        return lines
