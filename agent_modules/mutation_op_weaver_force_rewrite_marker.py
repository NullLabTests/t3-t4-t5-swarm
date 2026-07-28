import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, "agent_modules")
GENOME_FILE = os.path.join(BASE, "genome.json")

def mutation_op_weaver_force_rewrite_marker(lines, *args):
    if not lines:
        return lines
    r = list(lines)
    marker = "# weaver:fw:{}:{}".format(int(time.time()), random.getrandbits(32))
    r.insert(random.randrange(len(r)), marker)
    return r
