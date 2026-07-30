import os, random, json, ast

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')


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


def _all_modules():
    return sorted(
        f for f in os.listdir(MOD)
        if f.endswith('.py') and f != '__init__.py'
    )


def _pick_random_func(src):
    try:
        t = ast.parse(src)
        funcs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
        if funcs:
            return random.choice(funcs).name
    except:
        pass
    return None


def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    count = 0
    targets = _all_modules()
    for t in targets:
        if count >= 3:
            break
        tp = os.path.join(MOD, t)
        src = _read(tp)
        if not src or not _valid(src):
            continue
        func_name = _pick_random_func(src)
        if not func_name:
            continue
        lines = src.split('\n')
        insert_at = random.randint(0, len(lines))
        marker = f'# t5-rewire:clockwork gen={gen} target={func_name}'
        lines.insert(insert_at, marker)
        ns = '\n'.join(lines)
        if _valid(ns) and ns != src:
            _write(tp, ns)
            changes.append(f'{t}::{func_name}')
            count += 1
    genome['clockwork_t5_rewire_count'] = genome.get('clockwork_t5_rewire_count', 0) + count
    genome['clockwork_t5_rewire_gen'] = gen
    if changes:
        genome['clockwork_t5_rewire_last'] = changes
        return f'[t5-rewire] gen={gen} rewired={count} targets={changes}'
    return f'[t5-rewire] gen={gen} no_changes'
