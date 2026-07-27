import os, random, json, time, importlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, "agent_modules")
GENOME_FILE = os.path.join(BASE, "genome.json")

def mutation_op_weaver_self_modify(lines, *args):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    r.append("# weaver:self-mod")
    r.append("    _self_path = os.path.join(MODULES_DIR, 'weaver.py')")
    r.append("    with open(_self_path, 'a') as _f:")
    r.append("        _f.write('\\n# weaver:self-mod:gen=' + str(genome.get('generation', 0)) + ':' + format(random.getrandbits(32), '08x'))")
    return r
