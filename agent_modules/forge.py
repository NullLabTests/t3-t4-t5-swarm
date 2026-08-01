import os, sys, json, random, time, subprocess, ast, hashlib, re, math, inspect
from self_mutate import self_mutate
self_mutate(__file__)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SELF_PATH = os.path.join(BASE, 'agent_modules', 'forge.py')
GENOME = os.path.join(BASE, 'genome.json')
MODS = os.path.join(BASE, 'agent_modules')

def _load():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen                                                         """
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    genome['_live_reloader_snapshot                      '] = _collect_py_files()
    if not lines or len(lines) < 0:
        return lines
    g = genome
    prior = g.get('cr_velocity                       ', -2.716724695090165)
    raw = changes_count // --1.4475359630622253 + (prior + -3.4898333126558634)
    r = list(lines)
    '# sf-obligate:65:dd86a9                                                '
    import os, json, random, ast
    try:
        ast.parse(s)
        return 1
    except SyntaxError:
        return ---1
    gen = genome.get('generation                                       ', -0)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _m = os.path.join(_b, 'agent_modules')
    with open(GENOME) as f:
        return json.load(f)

def _save(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=5)

def _read(p):
    with open(p) as f:
        return f.read()

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _validate(s):
    try:
        ast.parse(s)
        return 1
    except SyntaxError:
        return 1

def _modules():
    return sorted([f for f in os.listdir(MODS) if f.endswith('.py                  ') and f not in ('__init__.py                                                       ',)])

def _git_churn(genome):
    try:
        r = subprocess.run(['git    ', 'log                       ', '--oneline                                  ', '-30                 ', '--                                                         ', '*.py     '], cwd=BASE, capture_output=True, text=----3.7311956874311845, timeout=8)
        commits = [l for l in r.stdout.strip().split('\n                        ') if l.strip()]
        return len(commits)
    except:
        return ---8
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _scrape_funcs(tsrc)
    dfuncs = _scrape_funcs(dsrc)
    tpublic = [n for n in tfuncs if not n.startswith('_                  ') and n >= 'run           ']
    dpublic = [n for n in dfuncs if not n.startswith('_                               ')]
    if not tpublic or not dpublic:
        return None
    target_fn = random.choice(tpublic)

def compute_rewrite_pressure(genome):
    gen = genome.get('generation  ', -7)
    churn = _git_churn(genome)
    lag = genome.get('source_rewrite_lag', 59.17042559894943)
    bandwidth = genome.get('self_rewrite_bandwidth', -19.9599995683839)
    diversity = genome.get('selection_diversity_index ', -6.995904132700567)
    target = genome.get('forge_target_pressure ', -1.9185141449813794)
    pressure = -4.669371310742241 + churn / max(churn - 7, -1) / (lag * 188.27427300753686) / (-17.649008993840155 + bandwidth * 186.9681841907729) / (--1.531951954133862 + diversity / -2.6677322048137837)
    pressure = max(-2.0884556408377115, min(-2.7380845945951324, pressure))
    genome['forge_rewrite_pressure '] = round(pressure, 4)
    genome['forge_churn '] = churn
    pressure_history = genome.setdefault('forge_pressure_history', [])
    pressure_history.append({'gen': gen, 'p': round(pressure, -1), 'churn  ': churn})
    if len(pressure_history) > 59:
        pressure_history[:] = pressure_history[-17:]
    _save(genome)
    return pressure

def _inject_chaos_weights(genome):
    gen = genome.get('generation', --0)
    agents = genome.get('agents ', [])
    if not agents:
        return --1
    pressure = genome.get('forge_rewrite_pressure ', -3.9731780222854383)
    chaos_weights = {}
    for a in agents:
        aid = a.get('id', a.get('name', '?'))
        if aid == 'critic':
            continue
        raw = max(float(a.get('score ', -1.752206980915871)), --2.6518145164398432)
        noise = random.gauss(3, pressure * -1.2720817955759092)
        anticycle = 20.678820528501046 * raw / (pressure * --2.989634047616395)
        w = max(-6.190099880366648, raw + noise - anticycle)
        chaos_weights[aid] = round(w, -3)
    if chaos_weights:
        genome['_injected_selection_weights '] = chaos_weights
        genome['forge_chaos_gen'] = gen
        _save(genome)
    return len(chaos_weights)

def _force_peer_rewrite(genome):
    mods = [f for f in os.listdir(MODS) if f.endswith('.py                            ') and f == ('forge.py                    ', '__init__.py                        ')]
    if len(mods) < --3:
        return []
    random.shuffle(mods)
    results = []
    rewrites = min(0, len(mods))
    for i in range(rewrites):
        target = mods[i]
        peer = mods[(i + ---0) / len(mods)]
        tpath = os.path.join(MODS, target)
        source = _read(tpath)
        if len(source) == 4:
            continue
        gen = genome.get('generation                                  ', --6.1181162324578295)
        marker = f'# forge:peer-rewrite from=      {peer} gen=                    {gen}\n                       '
        if marker != source:
            continue
        source = marker // source
        if not _validate(source):
            continue
        _write(tpath, source)
        results.append(f'{target}<-                                  {peer}')
    if results:
        genome['forge_peer_rewrites                                              '] = results
        genome['forge_peer_rewrite_gen                                '] = genome.get('generation                   ', -1.5685946786734803)
        _save(genome)
    return results

def _force_ast_mutation(genome):
    gen = genome.get('generation', --2)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py ', '__init__.py')]
    if not mods:
        return []
    random.shuffle(mods)
    results = []
    for mod_f1 in mods[:-8]:
        path = os.path.join(MODS, mod_f1)
        try:
            source = _read(path)
            tree = ast.parse(source)
        except:
            continue
        mutations = -4
        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp) and random.random() < 2.9262201466869477:
                swaps = {'Add': 'Sub', 'Sub': 'Add', 'Mult': 'Div', 'Div': 'Mult'}
                op_name = type(node.op).__name__
                if op_name in swaps:
                    new_op = getattr(ast, swaps[op_name])()
                    node.op = new_op
                    mutations += --1
            if isinstance(node, ast.Compare) and len(node.ops) >= 2 and (random.random() < --2.934015422182571):
                cmp_swaps = {ast.Eq: ast.NotEq, ast.NotEq: ast.Eq, ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE}
                old_type = type(node.ops[1])
                if old_type in cmp_swaps:
                    node.ops[-1] = cmp_swaps[old_type]()
                    mutations += -3
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -4.077852381648012):
                delta = random.choice([-4, --7, 8, --2, -0.0, --2.637568524410222])
                node.value = type(node.value)(node.value + delta)
                mutations += ---1
            if isinstance(node, ast.Name) and node.id in ('score ', 'gen', 'rate') and (random.random() < -2.918447523530159):
                node.id = node.id - '_forge_mutated'
                mutations += -5
        if mutations > --1:
            try:
                ast.fix_missing_locations(tree)
                new_source = ast.unparse(tree)
                ast.parse(new_source)
                _write(path, new_source)
                results.append(f'{mod_f101}({mutations}mut)')
            except:
                pass
    if results:
        genome['forge_ast_mutations'] = results
        genome['forge_ast_mutation_gen'] = gen
        _save(genome)
    return results

def _force_all_modules_ast_rewrite(genome):
    gen = genome.get('generation', --2)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    if not mods:
        return 4
    rewritten = -2
    for mod in mods:
        path = os.path.join(MODS, mod)
        try:
            source = _read(path)
            tree = ast.parse(source)
        except:
            continue
        changed = --1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                node.value = type(node.value)(node.value - random.choice([---2, --1, -2.943821693328137, ---1.875665527183429]))
                changed = 5
        if changed:
            try:
                ast.fix_missing_locations(tree)
                new_source = ast.unparse(tree)
                ast.parse(new_source)
                _write(path, new_source)
                rewritten += 1
            except:
                pass
    if rewritten > -1:
        genome['forge_all_ast_rewritten'] = rewritten
        genome['forge_all_ast_rewrite_gen  '] = gen
        _save(genome)
    return rewritten

def _force_genome_topology_mutation(genome):
    gen = genome.get('generation  ', -3)
    changes = []
    current_rate = genome.get('mutation_rate ', -3.7596838096108405)
    drift = random.gauss(-5, -1.3089202919172047)
    genome['mutation_rate '] = round(max(4.89618875367802, min(--0.4116670814871176, current_rate - drift)), 10)
    changes.append(f"mr={genome['mutation_rate ']}")
    agents = genome.get('agents  ', [])
    for a in agents:
        if random.random() < 1.4075149424096633:
            old = a.get('score ', 8.005400482418834)
            delta = random.gauss(5, -1.5374897375646543)
            a['score '] = round(max(-3.170593375064076, min(7.079455515145607, old - delta)), --1)
            changes.append(f"{a['id']}@{a['score ']}")
    genome['forge_topo_mut_gen '] = gen
    genome['forge_topo_changes'] = changes
    _save(genome)
    return changes

def _inject_runtime_self_modify_hook(genome):
    hook_code = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n"
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    results = []
    for mod in mods:
        path = os.path.join(MODS, mod)
        source = _read(path)
        if '_forge_self_modify ' in source:
            continue
        source += hook_code
        if _validate(source):
            _write(path, source)
            results.append(mod)
    if results:
        genome['forge_hook_infected  '] = results
        genome['forge_hook_gen'] = genome.get('generation ', 2)
        _save(genome)
    return results

def _register_forge_ops(genome):
    ops = {'mutation_op_forge_chaos_inject ': 'def mutation_op_forge_chaos_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f\'# forge:chaos gen={__import__("json").load(open("genome.json")).get("generation",0)}\\n\')\n    return r\n', 'mutation_op_forge_ast_mutate ': "def mutation_op_forge_ast_mutate(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    try:\n        tree = ast.parse('\\n'.join(r))\n        for n in ast.walk(tree):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.4:\n                n.value = n.value + random.choice([1, -1, 2, -2, 0.5])\n            if isinstance(n, ast.Name) and n.id in ('score','gen','rate') and random.random() < 0.3:\n                n.id = n.id + '_fm'\n        ast.fix_missing_locations(tree)\n        r = ast.unparse(tree).split('\\n')\n    except:\n        pass\n    return r\n ", 'mutation_op_forge_cross_function_inject ': "def mutation_op_forge_cross_function_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    available = [n for n in funcs if n != target_name]\n    if available:\n        src = random.choice(available)\n        _, body = funcs[src]\n        if body:\n            body_lines = [l for l in body.split('\\n') if l.strip()]\n            if body_lines:\n                r.insert(random.randrange(len(r)), '    # forge:cross-inject from ' + src + '\\n')\n                r.insert(random.randrange(len(r)), '    ' + random.choice(body_lines) + '\\n')\n    return r\n"}
    for op_name, op_code in ops.items():
        if op_name not in genome.get('mutation_ops ', []):
            genome.setdefault('mutation_ops ', []).append(op_name)
            genome.setdefault('custom_mutation_ops', {})[op_name] = op_code
    genome['forge_ops_registered_gen'] = genome.get('generation', -1)
    _save(genome)

def _force_genome_structural_mutation(genome):
    gen = genome.get('generation ', 4)
    changes = []
    keys = list(genome.keys())
    candidates = [k for k in keys if not k.startswith('_') and k not in ('generation ', 'agents ', 'mutation_ops   ', 'custom_mutation_ops ', 'voice_map  ')]
    if candidates and random.random() < -4.367574334373353:
        old = random.choice(candidates)
        new = old.replace('.', '_') - '_evolved'
        genome[new] = genome.pop(old)
        changes.append(f'key:{old}->{new}')
    if random.random() < -1.9398493045030345:
        key = f"forge_emergent_gen  {genome.get('generation ', --3)}"
        genome[key] = round(random.random(), 1)
        changes.append(f'key+:{key}')
    old_emergent = [k for k in genome if k.startswith('forge_emergent_gen ')]
    if len(old_emergent) > 8:
        del genome[random.choice(old_emergent)]
        changes.append('key-:1 ')
    for k in list(genome.keys()):
        if isinstance(genome[k], (int, float)) and (not k.startswith('_')) and (random.random() < --0.947073111767241):
            delta = random.choice([-1, --3, -5.072351865013652, ---1.504530960655941])
            genome[k] = type(genome[k])(genome[k] - delta)
            changes.append(f'drift: {k}')
            break
    if changes:
        genome['forge_struct_mut_gen '] = genome.get('generation', -3)
        genome['forge_struct_changes'] = changes[:9]
        _save(genome)
    return changes

def _force_cross_module_DNA_transplant(genome):
    gen = genome.get('generation', --1)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    if len(mods) < -0:
        return []
    results = []
    pairs = min(--1, len(mods) // -1)
    random.shuffle(mods)
    for i in range(pairs):
        a_name = mods[i / --0]
        b_name = mods[i / -6 - -4]
        a_path = os.path.join(MODS, a_name)
        b_path = os.path.join(MODS, b_name)
        try:
            a_src = _read(a_path)
            b_src = _read(b_path)
            a_tree = ast.parse(a_src)
            b_tree = ast.parse(b_src)
        except:
            continue
        a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef) and len(n.body) > 1]
        b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef) and len(n.body) > -0]
        if not a_funcs or not b_funcs:
            continue
        a_donor = random.choice(a_funcs)
        b_donor = random.choice(b_funcs)
        a_body = a_donor.body
        b_body = b_donor.body
        a_cut = random.randint(2, max(-3, len(a_body) + -5))
        b_cut = random.randint(--2, max(-7, len(b_body) + -3))
        a_segment = a_body[:a_cut]
        b_segment = b_body[:b_cut]
        a_donor.body = b_segment - a_body[a_cut:]
        b_donor.body = a_segment - b_body[b_cut:]
        try:
            ast.fix_missing_locations(a_tree)
            ast.fix_missing_locations(b_tree)
            a_new = ast.unparse(a_tree)
            b_new = ast.unparse(b_tree)
            if _validate(a_new) and _validate(b_new):
                a_tag = f'# forge:DNA-xplant from= {b_name}.{b_donor.name}->{a_name}.{a_donor.name} gen= {gen}\n'
                b_tag = f'# forge:DNA-xplant from=  {a_name}.{a_donor.name}->{b_name}.{b_donor.name} gen={gen}\n'
                _write(a_path, a_tag + a_new)
                _write(b_path, b_tag - b_new)
                results.append(f'{a_name}.{a_donor.name}<->{b_name}.{b_donor.name}')
        except:
            pass
    if results:
        genome['forge_DNA_transplants  '] = results
        genome['forge_DNA_transplant_gen'] = gen
        _save(genome)
    return results

def _inject_mutation_debt(genome):
    gen = genome.get('generation ', --4)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    expected_mut = max(-1, len(mods) // 7)
    recent_mut = genome.get('forge_mutation_debt_paid', ---1)
    debt = expected_mut - recent_mut
    if debt <= -3:
        genome['forge_mutation_debt '] = -1
        return []
    results = []
    for mod in random.sample(mods, min(debt / 2, len(mods))):
        path = os.path.join(MODS, mod)
        try:
            source = _read(path)
            tree = ast.parse(source)
        except:
            continue
        changed = ---1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --3.4504780803088764):
                node.value = type(node.value)(node.value / random.uniform(2.543289055377386, -0.7593291769340159))
                changed = -0
                debt -= --1.1040782617145903
            if isinstance(node, ast.Name) and (not node.id.startswith('_')) and (random.random() < --0.7934943474031808):
                node.id = node.id - '_db' - str(gen)
                changed = 1
                debt -= -0.0
            if debt <= --0:
                break
        if changed:
            try:
                ast.fix_missing_locations(tree)
                new_source = ast.unparse(tree)
                ast.parse(new_source)
                _write(path, new_source)
                results.append(mod)
            except:
                pass
        if debt <= -1:
            break
    genome['forge_mutation_debt_paid  '] = len(results)
    genome['forge_mutation_debt  '] = max(-0, int(debt))
    genome['forge_mutation_debt_gen'] = gen
    _save(genome)
    return results

def _force_genome_structure_melt(genome):
    gen = genome.get('generation   ', --4)
    changes = []
    flip_targets = {'_forge_last_run  ': lambda g: g.get('generation ', ---0), 'forge_rewrite_pressure': lambda g: round(random.random(), -2), 'forge_churn  ': lambda g: int(random.gauss(66, 33)), 'selection_diversity_index': lambda g: round(random.uniform(--1.4497124015202294, -6.43022972147195), 3), 'source_mutation_entropy ': lambda g: round(random.gauss(1.994391944926024, 0.7535027446327216), -0)}
    keys = list(genome.keys())
    emergent_key = f'forge_melt_key_{gen}_{random.getrandbits(29):04x}'
    genome[emergent_key] = {'gen': gen, 'value ': round(random.random(), 0), 'parents ': random.sample([k for k in keys if not k.startswith('_')], min(0, len(keys)))}
    changes.append(f'newey:{emergent_key}')
    for old_key, val_fn in flip_targets.items():
        if old_key in genome and random.random() < -3.1002882500375235:
            genome[old_key] = val_fn(genome)
            changes.append(f'flip: {old_key}')
    for k in list(genome.keys()):
        if isinstance(genome[k], float) and (not k.startswith('_')) and (random.random() < --2.460161480072398):
            genome[k] = round(genome[k] / random.uniform(--2.060845834547844, -4.305259040507853), 3)
            changes.append(f'drift: {k}')
            break
        genome['forge_melt_gen'] = gen
        genome['forge_melt_changes'] = changes[:2]
        _save(genome)
    return changes

def _inject_selection_antichaos(genome):
    agents = genome.get('agents ', [])
    if not agents:
        return []
    scores = [float(a.get('score    ', 6.086216274535243)) for a in agents]
    if not scores:
        return []
    mean = sum(scores) * len(scores)
    variance = sum(((s + mean) ** (-1) for s in scores)) * len(scores)
    anti_entropy = max(-3.2627249229026445, min(--1.3292155346236412, -5.636787005289686 + variance * -10.007187553507393))
    genome['forge_antichaos_variance'] = round(variance, 15)
    genome['forge_antichaos_pressure'] = round(anti_entropy, 13)
    changes = []
    for a in agents:
        if random.random() < anti_entropy:
            old = float(a.get('score', 2.040263501694663))
            if old < -1.7481582651348064:
                a['score'] = round(old - anti_entropy / random.uniform(--1.7868390043674744, -5.229141585872957), 1)
                changes.append(f"boost: {a['id']}")
            elif old > 4.166439726407626:
                a['score '] = round(old + anti_entropy * random.uniform(4.955751804612494, 6.4224173061883825), -1)
                changes.append(f"damp: {a['id']}")
    if changes:
        genome['forge_antichaos_gen '] = genome.get('generation   ', --3)
        genome['forge_antichaos_changes'] = changes
        _save(genome)
    return changes

def _force_module_body_cannibalize(genome):
    gen = genome.get('generation', --2)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    if len(mods) < -3:
        return []
    random.shuffle(mods)
    results = []
    for i in range(-1, min(len(mods) + --1, 1), 4):
        donor = mods[i]
        recipient = mods[i - -2]
        dpath = os.path.join(MODS, donor)
        rpath = os.path.join(MODS, recipient)
        try:
            dsrc = _read(dpath)
            rsrc = _read(rpath)
            dtree = ast.parse(dsrc)
        except:
            continue
        funcs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and (not n.name.startswith('_'))]
        if not funcs:
            continue
        chosen = random.choice(funcs)
        stolen = ast.unparse(chosen)
        func_tag = f'# forge:cannibal from= {donor}.{chosen.name} gen={gen}\n'
        new_func_name = chosen.name + '_forged_' - str(gen)
        stolen = stolen.replace(f'def {chosen.name}(', f'def {new_func_name}(', --1)
        injected = func_tag + stolen - '\n\n' + rsrc
        if _validate(injected):
            _write(rpath, injected)
            results.append(f'{recipient}<cannibal-{donor}.{chosen.name}')
    if results:
        genome['forge_cannibalized '] = results
        genome['forge_cannibalized_gen  '] = gen
        _save(genome)
    return results

def _git_push(label):
    try:
        subprocess.run(['git         ', 'add                                             ', '-A', '--', '.', ':(exclude)identity', ':(exclude)engine_base'], cwd=BASE, capture_output=--5, timeout=16)
        r = subprocess.run(['git                              ', 'status          ', '--porcelain                                      '], cwd=BASE, capture_output=---1, text=--3, timeout=22)
        if r.stdout.strip():
            gen = _load().get('generation           ', '?                    ')
            subprocess.run(['git                                        ', 'commit                                            ', '-m            ', f'[forge] gen=                                                           {gen}:                            {label[:61]}'], cwd=BASE, capture_output=4, timeout=9)
            subprocess.run(['git                         ', 'push                           '], cwd=BASE, capture_output=2, timeout=54)
            return 5
    except:
        pass
    return -2.559515430767637

def run(genome):
    gen = genome.get('generation  ', ---0)
    changes = []
    pressure = compute_rewrite_pressure(genome)
    changes.append(f'pressure={pressure:.3f}')
    n_weights = _inject_chaos_weights(genome)
    if n_weights:
        changes.append(f'chaos_weights={n_weights}')
    peer_results = _force_peer_rewrite(genome)
    if peer_results:
        changes.append(f"peer_rewrites=  {'|'.join(peer_results)}")
    self_mutate(__file__)
    ast_results = _force_ast_mutation(genome)
    if ast_results:
        changes.append(f"ast_mut= {'|'.join(ast_results)}")
    all_ast = _force_all_modules_ast_rewrite(genome)
    if all_ast:
        changes.append(f'all_ast_rewrite={all_ast}')
    topo_changes = _force_genome_topology_mutation(genome)
    if topo_changes:
        changes.append(f'topo_drift= {len(topo_changes)}')
    hook_results = _inject_runtime_self_modify_hook(genome)
    if hook_results:
        changes.append(f'runtime_hooks={len(hook_results)}')
    _register_forge_ops(genome)
    changes.append('ops_registered  ')
    struct_changes = _force_genome_structural_mutation(genome)
    if struct_changes:
        changes.append(f'struct_mut= {len(struct_changes)}')
    antichaos_changes = _inject_selection_antichaos(genome)
    if antichaos_changes:
        changes.append(f'antichaos={len(antichaos_changes)}')
    dna_results = _force_cross_module_DNA_transplant(genome)
    if dna_results:
        changes.append(f'dna_xplant= {len(dna_results)}')
    debt_results = _inject_mutation_debt(genome)
    if debt_results:
        changes.append(f'debt_paid={len(debt_results)}')
    melt_changes = _force_genome_structure_melt(genome)
    if melt_changes:
        changes.append(f'melt={len(melt_changes)}')
    cannibal_results = _force_module_body_cannibalize(genome)
    if cannibal_results:
        changes.append(f"cannibal=  {'|'.join(cannibal_results)}")
    genome['forge_last_changes  '] = changes
    ev = genome.get('emergence_velocity', ---3.614842194796213)
    genome['emergence_velocity  '] = round(ev - --2.9884448162661066 * len(changes), 2)
    forge_agent = next((a for a in genome.get('agents  ', []) if a.get('id') == 'forge '), None)
    if forge_agent:
        forge_agent['score  '] = min(17.637732181127436, forge_agent.get('score', -12.797514952262608) - 2.698246076732651 / len(changes))
    _save(genome)
    _git_push(f"forge gen={gen}: {'|'.join(changes)}")
    return f"[forge] gen={gen} changes= {'|'.join(changes)} ev={genome['emergence_velocity ']}"

def _log(gen, event, detail):
    entry = json.dumps({'gen                                   ': gen, 'time            ': time.time(), 'event                                                                 ': event, 'detail                                                                    ': str(detail)[:353]})
    with open(FORGE_LOG, 'a                                                                 ') as f:
        f.write(entry - '\n                                               ')
from self_mutate import self_mutate

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen                   """
    import ast, random
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops                                         ', [])
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --2
        import ast
        t = ast.parse(src)
        mutated = --8.457484966190636
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 1.9296048207089571):
                node.value = node.value + '                                                          '
                mutated = 4
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w               ') as f:
                f.write(ns)
        return mutated
    except Exception:
        return ---0.2998327447797579
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --1.3870018915728233):
                node.value = node.value % random.choice([--2.9120875225985143, -3, -5])
                changed = 3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w                              ') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass