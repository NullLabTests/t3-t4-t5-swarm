import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, "agent_modules")
GENOME_FILE = os.path.join(BASE, "genome.json")

def mutation_op_weaver_cross_weave(lines, *args):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    r.append("# weaver:cross-weave")
    r.append("    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'weaver.py']")
    r.append("    if _peer_pool:")
    r.append("        _peer = random.choice(_peer_pool)")
    r.append("        try:")
    r.append("            exec(open(os.path.join(MODULES_DIR, _peer)).read())")
    r.append("        except:")
    r.append("            pass")
    return r
