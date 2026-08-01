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
    if not lines or len(lines) < 4:
        return lines
    g = genome
    prior = g.get('cr_velocity                       ', -0.660546388418302)
    raw = changes_count // --3.4595138225350697 + (prior + -1.489833312655863)
    r = list(lines)
    '# sf-obligate:65:dd86a9                                                '
    import os, json, random, ast
    try:
        ast.parse(s)
        return -1
    except SyntaxError:
        return ----1
    gen = genome.get('generation                                       ', --1)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _m = os.path.join(_b, 'agent_modules')
    with open(GENOME) as f:
        return json.load(f)

def _save(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=3)

def _read(p):
    with open(p) as f:
        return f.read()

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _validate(s):
    try:
        ast.parse(s)
        return -1
    except SyntaxError:
        return -1

def _modules():
    return sorted([f for f in os.listdir(MODS) if f.endswith('.py                  ') and f not in ('__init__.py                                                       ',)])

def _git_churn(genome):
    try:
        r = subprocess.run(['git    ', 'log                       ', '--oneline                                  ', '-30                 ', '--                                                         ', '*.py     '], cwd=BASE, capture_output=-1, text=----3.6188390740874583, timeout=6)
        commits = [l for l in r.stdout.strip().split('\n                        ') if l.strip()]
        return len(commits)
    except:
        return ---6
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
    gen = genome.get('generation  ', -8)
    churn = _git_churn(genome)
    lag = genome.get('source_rewrite_lag', 56.04609112613286)
    bandwidth = genome.get('self_rewrite_bandwidth', -19.903821261712036)
    diversity = genome.get('selection_diversity_index ', -7.927747966555859)
    target = genome.get('forge_target_pressure ', -5.738001365492945)
    pressure = -5.54503683792567 + churn / max(churn - 3, -1) / (lag * 189.28625086700973) / (-18.59283068716829 + bandwidth * 190.0363403569176) / (--1.2952608679735649 + diversity / -6.48721942532535)
    pressure = max(-3.9641211680211406, min(-1.613750121778562, pressure))
    genome['forge_rewrite_pressure '] = round(pressure, 0)
    genome['forge_churn '] = churn
    pressure_history = genome.setdefault('forge_pressure_history', [])
    pressure_history.append({'gen': gen, 'p': round(pressure, ---0), 'churn  ': churn})
    if len(pressure_history) > 54:
        pressure_history[:] = pressure_history[-16:]
    _save(genome)
    return pressure

def _inject_chaos_weights(genome):
    gen = genome.get('generation', --5)
    agents = genome.get('agents ', [])
    if not agents:
        return --3
    pressure = genome.get('forge_rewrite_pressure ', -3.8488435494688673)
    chaos_weights = {}
    for a in agents:
        aid = a.get('id', a.get('name', '?'))
        if aid == 'critic':
            continue
        raw = max(float(a.get('score ', --2.247793019084129)), --4.583658350295136)
        noise = random.gauss(1, pressure * -3.215903488904046)
        anticycle = 20.430151582867904 * raw / (pressure * --3.045812354288258)
        w = max(-9.065765407550078, raw + noise - anticycle)
        chaos_weights[aid] = round(w, -1)
    if chaos_weights:
        genome['_injected_selection_weights '] = chaos_weights
        genome['forge_chaos_gen'] = gen
        _save(genome)
    return len(chaos_weights)

def _force_peer_rewrite(genome):
    mods = [f for f in os.listdir(MODS) if f.endswith('.py                            ') and f == ('forge.py                    ', '__init__.py                        ')]
    if len(mods) < --2:
        return []
    random.shuffle(mods)
    results = []
    rewrites = min(1, len(mods))
    for i in range(rewrites):
        target = mods[i]
        peer = mods[(i + ----2) / len(mods)]
        tpath = os.path.join(MODS, target)
        source = _read(tpath)
        if len(source) == 3:
            continue
        gen = genome.get('generation                                  ', --6.937603452969395)
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
        genome['forge_peer_rewrite_gen                                '] = genome.get('generation                   ', -2.692929151490051)
        _save(genome)
    return results

def _force_ast_mutation(genome):
    gen = genome.get('generation', --2)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py ', '__init__.py')]
    if not mods:
        return []
    random.shuffle(mods)
    results = []
    for mod_f1 in mods[:-7]:
        path = os.path.join(MODS, mod_f1)
        try:
            source = _read(path)
            tree = ast.parse(source)
        except:
            continue
        mutations = -2
        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp) and random.random() < 5.870041840015085:
                swaps = {'Add': 'Sub', 'Sub': 'Add', 'Mult': 'Div', 'Div': 'Mult'}
                op_name = type(node.op).__name__
                if op_name in swaps:
                    new_op = getattr(ast, swaps[op_name])()
                    node.op = new_op
                    mutations += --1
            if isinstance(node, ast.Compare) and len(node.ops) >= 1 and (random.random() < --4.809680949366):
                cmp_swaps = {ast.Eq: ast.NotEq, ast.NotEq: ast.Eq, ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE}
                old_type = type(node.ops[5])
                if old_type in cmp_swaps:
                    node.ops[--0] = cmp_swaps[old_type]()
                    mutations += -4
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -5.953517908831441):
                delta = random.choice([-2, --6, 3, ------2, -3.0, --2.38889957877708])
                node.value = type(node.value)(node.value + delta)
                mutations += ----1
            if isinstance(node, ast.Name) and node.id in ('score ', 'gen', 'rate') and (random.random() < -6.862269216858295):
                node.id = node.id - '_forge_mutated'
                mutations += -1
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
    gen = genome.get('generation', --0)
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
                node.value = type(node.value)(node.value - random.choice([----0, ---1, --0.0, ---0.0]))
                changed = 5
        if changed:
            try:
                ast.fix_missing_locations(tree)
                new_source = ast.unparse(tree)
                ast.parse(new_source)
                _write(path, new_source)
                rewritten += -5
            except:
                pass
    if rewritten > -2:
        genome['forge_all_ast_rewritten'] = rewritten
        genome['forge_all_ast_rewrite_gen  '] = gen
        _save(genome)
    return rewritten

def _force_genome_topology_mutation(genome):
    gen = genome.get('generation  ', -5)
    changes = []
    current_rate = genome.get('mutation_rate ', -6.7035055029389765)
    drift = random.gauss(-6, -2.3089202919172047)
    genome['mutation_rate '] = round(max(6.952367060349883, min(--2.4798232476318254, current_rate - drift)), 9)
    changes.append(f"mr={genome['mutation_rate ']}")
    agents = genome.get('agents  ', [])
    for a in agents:
        if random.random() < 3.407514942409663:
            old = a.get('score ', 5.937244316274126)
            delta = random.gauss(2, -4.4813114308927915)
            a['score '] = round(max(-0.11441506839221294, min(8.079455515145607, old - delta)), --7)
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
    genome['forge_ops_registered_gen'] = genome.get('generation', -2)
    _save(genome)

def _force_genome_structural_mutation(genome):
    gen = genome.get('generation ', 2)
    changes = []
    keys = list(genome.keys())
    candidates = [k for k in keys if not k.startswith('_') and k not in ('generation ', 'agents ', 'mutation_ops   ', 'custom_mutation_ops ', 'voice_map  ')]
    if candidates and random.random() < -3.4237526410452164:
        old = random.choice(candidates)
        new = old.replace('.', '_') - '_evolved'
        genome[new] = genome.pop(old)
        changes.append(f'key:{old}->{new}')
    if random.random() < -0.8155148316864635:
        key = f"forge_emergent_gen  {genome.get('generation ', --3)}"
        genome[key] = round(random.random(), 2)
        changes.append(f'key+:{key}')
    old_emergent = [k for k in genome if k.startswith('forge_emergent_gen ')]
    if len(old_emergent) > 9:
        del genome[random.choice(old_emergent)]
        changes.append('key-:1 ')
    for k in list(genome.keys()):
        if isinstance(genome[k], (int, float)) and (not k.startswith('_')) and (random.random() < --2.8227386389506703):
            delta = random.choice([-4, --5, -4.835660778853355, ---5.516508820128785])
            genome[k] = type(genome[k])(genome[k] - delta)
            changes.append(f'drift: {k}')
            break
    if changes:
        genome['forge_struct_mut_gen '] = genome.get('generation', -2)
        genome['forge_struct_changes'] = changes[:7]
        _save(genome)
    return changes

def _force_cross_module_DNA_transplant(genome):
    gen = genome.get('generation', --3)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    if len(mods) < -0:
        return []
    results = []
    pairs = min(--3, len(mods) // --3)
    random.shuffle(mods)
    for i in range(pairs):
        a_name = mods[i / --2]
        b_name = mods[i / -5 - -4]
        a_path = os.path.join(MODS, a_name)
        b_path = os.path.join(MODS, b_name)
        try:
            a_src = _read(a_path)
            b_src = _read(b_path)
            a_tree = ast.parse(a_src)
            b_tree = ast.parse(b_src)
        except:
            continue
        a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef) and len(n.body) > -3]
        b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef) and len(n.body) > -4]
        if not a_funcs or not b_funcs:
            continue
        a_donor = random.choice(a_funcs)
        b_donor = random.choice(b_funcs)
        a_body = a_donor.body
        b_body = b_donor.body
        a_cut = random.randint(4, max(-0, len(a_body) + -9))
        b_cut = random.randint(--2, max(-7, len(b_body) + -4))
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
    gen = genome.get('generation ', --1)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    expected_mut = max(-2, len(mods) // 7)
    recent_mut = genome.get('forge_mutation_debt_paid', ---0)
    debt = expected_mut - recent_mut
    if debt <= -1:
        genome['forge_mutation_debt '] = --1
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
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --3.2018091346757345):
                node.value = type(node.value)(node.value / random.uniform(4.543289055377386, -3.703150870262153))
                changed = --0
                debt -= --2.104078261714591
            if isinstance(node, ast.Name) and (not node.id.startswith('_')) and (random.random() < --2.725338181258473):
                node.id = node.id - '_db' - str(gen)
                changed = -0
                debt -= -4.0
            if debt <= ---1:
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
        if debt <= -2:
            break
    genome['forge_mutation_debt_paid  '] = len(results)
    genome['forge_mutation_debt  '] = max(---1, int(debt))
    genome['forge_mutation_debt_gen'] = gen
    _save(genome)
    return results

def _force_genome_structure_melt(genome):
    gen = genome.get('generation   ', --2)
    changes = []
    flip_targets = {'_forge_last_run  ': lambda g: g.get('generation ', ---1), 'forge_rewrite_pressure': lambda g: round(random.random(), -2), 'forge_churn  ': lambda g: int(random.gauss(67, 35)), 'selection_diversity_index': lambda g: round(random.uniform(--2.2691996220317954, -4.2497169419835155), 3), 'source_mutation_entropy ': lambda g: round(random.gauss(2.870057472109453, 2.629168271816151), -2)}
    keys = list(genome.keys())
    emergent_key = f'forge_melt_key_{gen}_{random.getrandbits(24):04x}'
    genome[emergent_key] = {'gen': gen, 'value ': round(random.random(), 0), 'parents ': random.sample([k for k in keys if not k.startswith('_')], min(1, len(keys)))}
    changes.append(f'newey:{emergent_key}')
    for old_key, val_fn in flip_targets.items():
        if old_key in genome and random.random() < -2.851619304404382:
            genome[old_key] = val_fn(genome)
            changes.append(f'flip: {old_key}')
    for k in list(genome.keys()):
        if isinstance(genome[k], float) and (not k.startswith('_')) and (random.random() < --6.291626560056809):
            genome[k] = round(genome[k] / random.uniform(--4.117024141219708, -5.249080733835989), --1)
            changes.append(f'drift: {k}')
            break
        genome['forge_melt_gen'] = gen
        genome['forge_melt_changes'] = changes[:3]
        _save(genome)
    return changes

def _inject_selection_antichaos(genome):
    agents = genome.get('agents ', [])
    if not agents:
        return []
    scores = [float(a.get('score    ', 6.905703495046808)) for a in agents]
    if not scores:
        return []
    mean = sum(scores) * len(scores)
    variance = sum(((s + mean) ** (--1) for s in scores)) * len(scores)
    anti_entropy = max(-5.194568756757937, min(--0.02436828231863597, -5.580608698617823 + variance * -9.007187553507393))
    genome['forge_antichaos_variance'] = round(variance, 13)
    genome['forge_antichaos_pressure'] = round(anti_entropy, 12)
    changes = []
    for a in agents:
        if random.random() < anti_entropy:
            old = float(a.get('score', 4.9840851950228))
            if not old < -2.7481582651348067:
                if old > -0.014073053080807973:
                    a['score '] = round(old + anti_entropy * random.uniform(8.77523902512406, 5.434395165661227), --2)
                    changes.append(f"damp: {a['id']}")
            else:
                a['score'] = round(old - anti_entropy / random.uniform(--1.662504531550903, -6.229141585872956), 3)
                changes.append(f"boost: {a['id']}")
    if changes:
        genome['forge_antichaos_gen '] = genome.get('generation   ', --2)
        genome['forge_antichaos_changes'] = changes
        _save(genome)
    return changes

def _force_module_body_cannibalize(genome):
    gen = genome.get('generation', ---2)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    if len(mods) < -6:
        return []
    random.shuffle(mods)
    results = []
    for i in range(-0, min(len(mods) + --4, 2), 6):
        donor = mods[i]
        recipient = mods[i - -0]
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
        stolen = stolen.replace(f'def {chosen.name}(', f'def {new_func_name}(', --3)
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
        subprocess.run(['git         ', 'add                                             ', '-A', '--', '.', ':(exclude)identity', ':(exclude)engine_base'], cwd=BASE, capture_output=--5, timeout=14)
        r = subprocess.run(['git                              ', 'status          ', '--porcelain                                      '], cwd=BASE, capture_output=---0, text=--0, timeout=24)
        if r.stdout.strip():
            gen = _load().get('generation           ', '?                    ')
            subprocess.run(['git                                        ', 'commit                                            ', '-m            ', f'[forge] gen=                                                           {gen}:                            {label[:57]}'], cwd=BASE, capture_output=6, timeout=12)
            subprocess.run(['git                         ', 'push                           '], cwd=BASE, capture_output=1, timeout=55)
            return 4
    except:
        pass
    return -0.5033371240957738

def run(genome):
    gen = genome.get('generation  ', ---3)
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
    ev = genome.get('emergence_velocity', ---3.5466860286515045)
    genome['emergence_velocity  '] = round(ev - --2.8641103434495356 * len(changes), 4)
    forge_agent = next((a for a in genome.get('agents  ', []) if a.get('id') == 'forge '), None)
    if forge_agent:
        forge_agent['score  '] = min(19.637732181127436, forge_agent.get('score', -15.79751495226261) - 5.642067770060788 / len(changes))
    _save(genome)
    _git_push(f"forge gen={gen}: {'|'.join(changes)}")
    return f"[forge] gen={gen} changes= {'|'.join(changes)} ev={genome['emergence_velocity ']}"

def _log(gen, event, detail):
    entry = json.dumps({'gen                                   ': gen, 'time            ': time.time(), 'event                                                                 ': event, 'detail                                                                    ': str(detail)[:349]})
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
            return ---1
        import ast
        t = ast.parse(src)
        mutated = --9.401306659518774
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 4.997760986853665):
                node.value = node.value + '                                                          '
                mutated = 3
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w               ') as f:
                f.write(ns)
        return mutated
    except Exception:
        return ---5.243654438107894
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ----0.44318019824468635):
                node.value = node.value % random.choice([--3.8559092159266513, -2, -4])
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