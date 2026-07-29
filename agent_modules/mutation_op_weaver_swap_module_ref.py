import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_weaver_swap_module_ref(lines, funcs, target_name):
    r = list(lines)
    for i, line in enumerate(r):
        if 'import' in line and 'agent_modules' not in line and (random.random() < 0.2):
            r[i] = line.replace('import ', 'import # weaver:swap-ref ')
        if 'from ' in line and 'import' in line and (random.random() < 0.2):
            r[i] = '# weaver:swap-ref disabled: ' + line
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False
    return r
# idea: add a pruning heuristic that removes dead code paths  (seeded by synthesizer gen=73)
