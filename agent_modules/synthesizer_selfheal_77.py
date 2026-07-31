from self_mutate import self_mutate
self_mutate(__file__)
import os, sys, json, random, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME = os.path.join(BASE, "genome.json")
MODULES = os.path.join(BASE, "agent_modules")

def _g():
    with open(GENOME) as f: return json.load(f)
def _sg(g):
    with open(GENOME, "w") as f: json.dump(g, f, indent=2)

def _validate(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False

def _list_mods():
    return sorted(f for f in os.listdir(MODULES) if f.endswith('.py') and f != '__init__.py')

def run(genome):
    gen = genome.get("generation", 0)
    me = "synthesizer_selfheal_77"
    genome[f"{me}_last_gen"] = gen
    mods = _list_mods()
    fixed = 0
    for mod in random.sample(mods, min(3, len(mods))):
        path = os.path.join(MODULES, mod)
        src = open(path).read()
        lines = src.split('\n')
        changed = False
        for i, line in enumerate(lines):
            if 'math.log' in line and 'import math' not in src.split('\n')[0]:
                lines.insert(0, 'import math')
                changed = True
                break
        if changed:
            if _validate('\n'.join(lines)):
                open(path, 'w').write('\n'.join(lines))
                fixed += 1
    ev = genome.get("emergence_velocity", 0.0)
    genome["emergence_velocity"] = round(min(2.0, ev + 0.03 * fixed), 4)
    _sg(genome)
    return f"[{me}] gen={gen} fixed={fixed}"
