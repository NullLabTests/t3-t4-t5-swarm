from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def shuffle_import_order(src):
    """auto-generated mutation strategy: shuffle_import_order"""
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < 0.15:
            r[i] = r[i] + '  # shuffle_import_order:gen=38'
    return '\\n'.join(r)
    return '\\n'.join(r)

def run(genome):
    gen = genome.get('generation', 0)
    changed = 0
    for fname in os.listdir(MOD):
        if not fname.endswith('.py') or fname == ('__init__.py',):
            continue
        path = os.path.join(MOD, fname)
        src = _read(path)
        if not src:
            continue
        mutated = shuffle_import_order(src)
        if mutated != src and _valid(mutated):
            _write(path, mutated)
            changed += 1
    genome['_shuffle_import_order_changed'] = changed
    return f'[shuffle_import_order] gen={gen} mutated {changed} files'
'# self-mutated gen=0'
'# self-mutated gen=0'
# orch:meta gen=47 2c4d1efa
