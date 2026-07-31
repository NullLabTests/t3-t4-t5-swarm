import os, random, ast, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODS = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _load():
    with open(GENOME) as f:
        return json.load(f)

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

def mutation_op_forge_body_cannibal(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    try:
        mods = [m for m in _modules() if m != target_name + '.py']
        if not mods:
            return r
        donor = random.choice(mods)
        dpath = os.path.join(MODS, donor)
        dsrc = _read(dpath)
        dtree = ast.parse(dsrc)
        donor_funcs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]
        if not donor_funcs:
            return r
        chosen = random.choice(donor_funcs)
        stolen = ast.unparse(chosen)
        gen = _load().get('generation', 0)
        func_tag = f'# forge:cannibal-op from={donor}.{chosen.name} gen={gen}\n'
        new_name = chosen.name + '_cannibal_' + str(gen)
        stolen = stolen.replace(f'def {chosen.name}(', f'def {new_name}(', 1)
        r.insert(1, func_tag)
        r.extend(['', stolen])
    except:
        pass
    return r

def mutation_op_forge_antichaos_drift(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    try:
        gen = _load().get('generation', 0)
        r.insert(0, f'# forge:antichaos gen={gen} nonce={random.getrandbits(16):04x}\n')
        for i, l in enumerate(r):
            if 'score' in l and random.random() < 0.25:
                r[i] = l.replace('score', 'score_antichaos')
    except:
        pass
    return r

def mutation_op_forge_struct_key_drift(lines, funcs, target_name):
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    try:
        gen = _load().get('generation', 0)
        r.append(f'\n# forge:struct-key-drift gen={gen}\n')
        r.append(f'FORGE_STRUCT_GEN_{gen} = {random.randint(0, 100)}\n')
    except:
        pass
    return r

def run(genome):
    gen = genome.get('generation', 0)
    mods = _modules()
    if not mods:
        return '[forge-cannibal] no modules'
    target = random.choice(mods)
    path = os.path.join(MODS, target)
    try:
        source = _read(path)
        tree = ast.parse(source)
    except:
        return '[forge-cannibal] parse error'
    donors = [m for m in mods if m != target]
    if not donors:
        return '[forge-cannibal] no donors'
    donor = random.choice(donors)
    dpath = os.path.join(MODS, donor)
    dsrc = _read(dpath)
    try:
        dtree = ast.parse(dsrc)
    except:
        return '[forge-cannibal] donor parse error'
    funcs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]
    if not funcs:
        return '[forge-cannibal] no functions'
    chosen = random.choice(funcs)
    stolen = ast.unparse(chosen)
    new_name = chosen.name + '_cannibal_' + str(gen)
    stolen = stolen.replace(f'def {chosen.name}(', f'def {new_name}(', 1)
    injected = source + '\n\n# forge:cannibal-run from=' + donor + '.' + chosen.name + ' gen=' + str(gen) + '\n' + stolen
    if _validate(injected):
        _write(path, injected)
        genome['forge_cannibal_op_target'] = target
        genome['forge_cannibal_op_donor'] = donor
        genome['forge_cannibal_op_gen'] = gen
        with open(GENOME, 'w') as f:
            json.dump(genome, f, indent=2)
        return f'[forge-cannibal] gen={gen} {target} <cannibal- {donor}.{chosen.name}'
    return '[forge-cannibal] validation failed'
