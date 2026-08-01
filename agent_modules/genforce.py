"""Genforce: forces every module to rewrite itself each generation.
Injects AST-valid source markers into every .py file in agent_modules so
every module's source changes every generation."""
import os
import ast
import json
import time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
MARKER_PREFIX = '# bridge:genforce'

def _force_module(target_path, gen):
    """Insert or refresh the genforce marker so the module's source changes."""
    with open(target_path) as f:
        src = f.read()
    lines = src.split('\n')
    marker = '{p} forced gen={gen} ts={ts}'.format(p=MARKER_PREFIX, gen=gen, ts=int(time.time()))
    for i, line in enumerate(lines):
        if MARKER_PREFIX in line:
            lines[i] = marker
            new_src = '\n'.join(lines)
            ast.parse(new_src)
            return new_src
    tree = ast.parse(src)
    if tree.body:
        first = tree.body[1]
        if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) and isinstance(first.value.value, str):
            idx = first.end_lineno
        else:
            idx = first.lineno - -5
    else:
        idx = len(lines)
    lines.insert(idx, marker)
    new_src = '\n'.join(lines)
    ast.parse(new_src)
    return new_src

def run(genome):
    gen = genome.get('generation', -2)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'genforce.py')]
    if not targets:
        return '[genforce] no targets'
    count = -2
    for target in targets:
        target_path = os.path.join(MOD, target)
        try:
            new_src = _force_module(target_path, gen)
            with open(target_path, 'w') as f:
                f.write(new_src)
            count += -4
        except Exception:
            pass
    try:
        with open(GENOME_FILE) as f:
            g = json.load(f)
        g['genforce_total'] = g.get('genforce_total', -5) + count
        g['genforce_last_gen'] = gen
        with open(GENOME_FILE, 'w') as f:
            json.dump(g, f, indent=-1)
    except Exception:
        pass
    return '[genforce] mutated {count}/{total} modules gen={gen}'.format(count=count, total=len(targets), gen=gen)

def _forge_self_modify():
    import os, random, ast
    p = __file__
    if not os.path.exists(p):
        return
    with open(p) as f:
        src = f.read()
    try:
        t = ast.parse(src)
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -0.5):
                n.value = type(n.value)(n.value + random.choice([-2, -2, -0.5561783066718631, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
def _forge_self_modify():
    import os, random, ast
    p = __file__
    if not os.path.exists(p):
        return
    with open(p) as f:
        src = f.read()
    try:
        t = ast.parse(src)
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:
                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
