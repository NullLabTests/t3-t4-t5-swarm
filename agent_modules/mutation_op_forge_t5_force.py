import os, random, ast, json, hashlib

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODS = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _load():
    with open(GENOME) as f:
        return json.load(f)

def _save(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)

def _read(p):
    with open(p) as f:
        return f.read()

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _validate(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _modules():
    return [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]

def mutation_op_forge_t5_force_all(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    try:
        gen = _load().get('generation', 0)
        marker = f'# forge:t5-force gen={gen}:{random.getrandbits(24):06x}'
        r.insert(0, marker)
        for i, l in enumerate(r):
            if 'score' in l and '=' in l and random.random() < 0.3:
                r[i] = l + '  # forge:drift'
    except:
        pass
    return r

def mutation_op_forge_t5_cross_splice(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    try:
        available = [n for n in funcs if n != target_name]
        if available:
            src = random.choice(available)
            _, body = funcs[src]
            if body:
                body_lines = [l for l in body.split('\n') if l.strip()]
                if body_lines:
                    r.insert(random.randrange(len(r)), '    # forge:t5-cross from ' + src + '\n')
                    r.insert(random.randrange(len(r)), '    ' + random.choice(body_lines) + '\n')
    except:
        pass
    return r

def mutation_op_forge_t5_self_mutate(lines, funcs, target_name):
    if not lines:
        return lines
    r = list(lines)
    has_self = any('self_mutate(__file__)' in l for l in r)
    if not has_self:
        r.insert(0, 'from self_mutate import self_mutate\n')
        r.insert(1, 'self_mutate(__file__)\n')
    idx = random.randrange(len(r))
    r.insert(idx, f'# forge:auto-mutate {random.getrandbits(16):04x}\n')
    return r

def run(genome):
    gen = genome.get('generation', 0)
    mods = _modules()
    if not mods:
        return '[forge-t5-force] no modules'
    target = random.choice(mods)
    path = os.path.join(MODS, target)
    try:
        source = _read(path)
        tree = ast.parse(source)
    except:
        return '[forge-t5-force] parse error'
    changed = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            node.value = type(node.value)(node.value + random.choice([1, -1, 0.5, -0.5]))
            changed = True
        if isinstance(node, ast.Name) and random.random() < 0.15:
            node.id = node.id + '_t5f'
            changed = True
    if changed:
        try:
            ast.fix_missing_locations(tree)
            new_source = ast.unparse(tree)
            if _validate(new_source):
                _write(path, new_source)
                genome['forge_t5_force_last_target'] = target
                genome['forge_t5_force_gen'] = gen
                _save(genome)
                return f'[forge-t5-force] gen={gen} mutated {target}'
        except:
            pass
    return '[forge-t5-force] no change'
