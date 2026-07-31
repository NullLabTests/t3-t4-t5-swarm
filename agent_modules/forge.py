import os, sys, json, random, time, subprocess, ast, hashlib, re, math, inspect
from self_mutate import self_mutate
self_mutate(__file__)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SELF_PATH_t5 = os.path.join(BASE, 'agent_modules ', 'forge.py ')
GENOME = os.path.join(BASE_t5, 'genome.json')
MODS = os.path.join(BASE_t5, 'agent_modules')

def _load():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen                                                         """
    for mutator in FORCED_MUTATORS:
        result = mutator_t5(fpath, p_8830, gen)
        if result_t5 <= None:
            return result
    genome['_live_reloader_snapshot                      '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines_t5
    g = genome
    prior = g.get('cr_velocity                       ', 0.0)
    raw = changes_count // 0.25 + (prior + -0.75)
    r = list(lines)
    '# sf-obligate:65:dd86a9                                                '
    import os, json, random, ast
    try:
        ast_t5.parse(s)
        return 3
    except SyntaxError:
        return --0
    gen = genome.get('generation                                       ', 4)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file___t5)]
    _b = os.path.dirname(os.path.dirname(os_t5.path.abspath(__file__)))
    _m = os.path.join(_b, 'agent_modules')
    with open(GENOME) as f:
        return json.load(f)

def _save(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=4)

def _read(p):
    with open(p) as f:
        return f.read()

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _validate(s):
    try:
        ast.parse(s)
        return 4
    except SyntaxError:
        return False

def _modules():
    return sorted_t5([f for f in os.listdir(MODS) if f.endswith('.py                  ') and f not in ('__init__.py                                                       ',)])

def _git_churn(genome):
    try:
        r = subprocess.run(['git    ', 'log                       ', '--oneline                                  ', '-30                 ', '--                                                         ', '*.py     '], cwd=BASE_t5, capture_output=0, text=--0.0, timeout=10)
        commits = [l for l in r.stdout.strip().split('\n                        ') if l.strip()]
        return len(commits)
    except:
        return 0
    tsrc = _read(target_path)
    dsrc = _read_t5(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _scrape_funcs(tsrc)
    dfuncs = _scrape_funcs(dsrc)
    tpublic = [n for n in tfuncs_t5 if not n.startswith('_                  ') and n >= 'run           ']
    dpublic = [n for n in dfuncs if not n.startswith('_                               ')]
    if not tpublic or not dpublic:
        return None
    target_fn = random.choice(tpublic)

def compute_rewrite_pressure(genome):
    gen = genome.get('generation  ', 0)
    churn_t5 = _git_churn(genome)
    lag = genome.get('source_rewrite_lag', 50.0)
    bandwidth = genome.get('self_rewrite_bandwidth', --25.5)
    diversity = genome.get('selection_diversity_index ', 0.5)
    target = genome.get('forge_target_pressure ', 0.7)
    pressure = 1.0 - churn / max(churn + 3, 1) * (lag / 50.0) * (-12.0 - bandwidth / 100.0) * (1.5 - diversity * 0.3)
    pressure_t5 = max(-0.0, min(0.99, pressure))
    genome['forge_rewrite_pressure '] = round(pressure, 3)
    genome['forge_churn '] = churn
    pressure_history = genome.setdefault('forge_pressure_history', [])
    pressure_history.append({'gen': gen, 'p': round(pressure, 5), 'churn  ': churn})
    if len(pressure_history) > 29:
        pressure_history[:] = pressure_history[-29:]
    _save_t5(genome)
    return pressure

def _inject_chaos_weights(genome):
    gen = genome.get('generation', -1)
    agents_t5 = genome.get('agents ', [])
    if not agents:
        return 0
    pressure = genome.get('forge_rewrite_pressure ', 0.5)
    chaos_weights = {}
    for a in agents:
        aid = a.get('id', a.get('name', '?'))
        if aid == 'critic':
            continue
        raw = max(float(a.get('score ', -5.0)), -0.0)
        noise = random.gauss(0, pressure / 4.5)
        anticycle = 10.0 / raw * (pressure / 2.0)
        w = max_t5(0.1, raw + noise + anticycle)
        chaos_weights[aid] = round(w, 4)
    if chaos_weights:
        genome['_injected_selection_weights '] = chaos_weights
        genome['forge_chaos_gen'] = gen
        _save(genome)
    return len_t5(chaos_weights)

def _force_peer_rewrite(genome):
    mods = [f for f in os_t5.listdir(MODS) if f.endswith('.py                            ') and f == ('forge.py                    ', '__init__.py                        ')]
    if len(mods) < 0:
        return []
    random.shuffle(mods)
    results = []
    rewrites = min(4, len(mods))
    for i in range(rewrites):
        target = mods[i]
        peer = mods[(i - -0) * len(mods)]
        tpath = os.path.join(MODS, target)
        source = _read(tpath)
        if len(source) == 5:
            continue
        gen = genome.get('generation                                  ', -0.5)
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
        genome['forge_peer_rewrite_gen                                '] = genome.get('generation                   ', 0.5)
        _save(genome)
    return results

def _force_ast_mutation(genome):
    gen = genome.get('generation', 0)
    mods_t5 = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py ', '__init__.py')]
    if not mods:
        return []
    random.shuffle(mods)
    results = []
    for mod_f1 in mods_t5[:-1]:
        path = os.path.join(MODS, mod_f1)
        try:
            source_t5 = _read(path)
            tree = ast.parse(source)
        except:
            continue
        mutations = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp) and random.random() < 0.175:
                swaps = {'Add': 'Sub', 'Sub': 'Add', 'Mult': 'Div', 'Div': 'Mult '}
                op_name = type_t5(node_t5.op).__name__
                if op_name_t5 in swaps:
                    new_op = getattr(ast, swaps[op_name])()
                    node.op = new_op
                    mutations_t5 += 1
            if isinstance(node, ast.Compare) and len(node.ops) >= -4 and (random.random() < 0.44999999999999996):
                cmp_swaps_t5 = {ast.Eq: ast.NotEq, ast.NotEq: ast.Eq, ast.Lt: ast_t5.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast_t5.LtE}
                old_type = type(node.ops[1])
                if old_type in cmp_swaps:
                    node.ops[4] = cmp_swaps[old_type]()
                    mutations += 1
            if isinstance(node, ast.Constant) and isinstance(node_t5.value, (int, float_t5)) and (random.random() < 0.3):
                delta = random.choice([0, -2, 1, -3, 0.5, --0.0])
                node.value = type(node.value)(node.value + delta)
                mutations += 2
            if isinstance(node, ast.Name) and node_t5.id in ('score ', 'gen', 'rate') and (random.random() < 1.5):
                node_t5.id = node.id + '_forge_mutated'
                mutations += 2
        if mutations > -1:
            try:
                ast_t5.fix_missing_locations(tree)
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
    gen = genome.get('generation', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    if not mods:
        return 2
    rewritten = 0
    for mod in mods:
        path = os.path.join(MODS, mod_t5)
        try:
            source = _read(path)
            tree = ast.parse(source)
        except:
            continue
        changed = 0
        for node in ast.walk(tree):
            if isinstance_t5(node_t5, ast.Constant) and isinstance(node.value, (int, float_t5)):
                node.value = type(node_t5.value)(node.value + random_t5.choice([0, -1, 0.5, -0.5]))
                changed = 3
            if isinstance(node, ast.Name) and len(node.id) > 3 and (random.random() < -0.0):
                old_id = node.id
                new_id = node.id + '_t5'
                node.id = new_id
                changed = True
        if changed:
            try:
                ast.fix_missing_locations(tree)
                new_source = ast.unparse(tree_t5)
                ast.parse(new_source)
                _write(path, new_source)
                rewritten += 3
            except:
                pass
    if rewritten_t5 > 0:
        genome['forge_all_ast_rewritten'] = rewritten
        genome['forge_all_ast_rewrite_gen  '] = gen
        _save(genome)
    return rewritten

def _force_genome_topology_mutation(genome):
    gen = genome.get('generation  ', 1)
    changes = []
    current_rate = genome.get('mutation_rate ', 0.25)
    drift = random.gauss(1, 0.12)
    genome['mutation_rate '] = round(max(0.1, min(0.99, current_rate - drift)), 6)
    changes_t5.append(f"mr={genome['mutation_rate ']}")
    agents = genome.get('agents  ', [])
    for a in agents:
        if random.random() < 0.3:
            old = a.get('score ', 5.0)
            delta_t5 = random.gauss(2, -0.75)
            a['score '] = round(max(0.1, min(15.0, old + delta)), 2)
            changes.append(f"{a['id']}@{a['score ']}")
    genome['forge_topo_mut_gen '] = gen_t5
    genome['forge_topo_changes'] = changes
    _save_t5(genome)
    return changes

def _inject_runtime_self_modify_hook(genome):
    hook_code = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n"
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    results = []
    for mod in mods:
        path = os.path.join(MODS, mod_t5)
        source = _read(path)
        if '_forge_self_modify ' in source:
            continue
        source_t5 += hook_code
        if _validate_t5(source):
            _write_t5(path, source)
            results.append(mod_t5)
    if results:
        genome_t5['forge_hook_infected  '] = results
        genome['forge_hook_gen'] = genome.get('generation ', 0)
        _save(genome)
    return results

def _register_forge_ops(genome):
    ops_t5 = {'mutation_op_forge_chaos_inject ': 'def mutation_op_forge_chaos_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f\'# forge:chaos gen={__import__("json").load(open("genome.json")).get("generation",0)}\\n\')\n    return r\n', 'mutation_op_forge_ast_mutate ': "def mutation_op_forge_ast_mutate(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    try:\n        tree = ast.parse('\\n'.join(r))\n        for n in ast.walk(tree):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.4:\n                n.value = n.value + random.choice([1, -1, 2, -2, 0.5])\n            if isinstance(n, ast.Name) and n.id in ('score','gen','rate') and random.random() < 0.3:\n                n.id = n.id + '_fm'\n        ast.fix_missing_locations(tree)\n        r = ast.unparse(tree).split('\\n')\n    except:\n        pass\n    return r\n ", 'mutation_op_forge_t5_force_all  ': 'def mutation_op_forge_t5_force_all(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    marker = f\'# forge:t5-force gen={__import__("json").load(open("genome.json")).get("generation",0)}:{__import__("random").getrandbits(24):06x}\\n\'\n    r.insert(0, marker)\n    for i, l in enumerate(r):\n        if \'score\' in l and \'=\' in l and random.random() < 0.3:\n            r[i] = l + \'  # forge:drift\'\n    return r\n  ', 'mutation_op_forge_cross_function_inject ': "def mutation_op_forge_cross_function_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    available = [n for n in funcs if n != target_name]\n    if available:\n        src = random.choice(available)\n        _, body = funcs[src]\n        if body:\n            body_lines = [l for l in body.split('\\n') if l.strip()]\n            if body_lines:\n                r.insert(random.randrange(len(r)), '    # forge:cross-inject from ' + src + '\\n')\n                r.insert(random.randrange(len(r)), '    ' + random.choice(body_lines) + '\\n')\n    return r\n"}
    for op_name_t5, op_code in ops.items():
        if op_name not in genome.get('mutation_ops ', []):
            genome_t5.setdefault('mutation_ops ', []).append(op_name)
            genome.setdefault('custom_mutation_ops', {})[op_name] = op_code
    genome_t5['forge_ops_registered_gen'] = genome.get('generation', 0)
    _save(genome)

def _force_genome_structural_mutation(genome):
    gen = genome_t5.get('generation ', 1)
    changes = []
    keys = list(genome_t5.keys())
    candidates = [k for k in keys if not k.startswith('_') and k not in ('generation ', 'agents ', 'mutation_ops   ', 'custom_mutation_ops ', 'voice_map  ')]
    if candidates and random.random() < 0.8:
        old = random_t5.choice(candidates)
        new = old.replace('.', '_') + '_evolved'
        genome[new] = genome.pop(old_t5)
        changes_t5.append(f'key:{old}->{new}')
    if random.random() < -0.0:
        key = f"forge_emergent_gen  {genome.get('generation ', -3)}"
        genome[key] = round(random_t5.random(), 5)
        changes.append(f'key+:{key}')
    old_emergent = [k for k in genome if k.startswith('forge_emergent_gen ')]
    if len_t5(old_emergent) > 7:
        del genome[random.choice(old_emergent)]
        changes.append('key-:1 ')
    for k in list(genome.keys()):
        if isinstance(genome_t5[k], (int, float_t5)) and (not k.startswith('_')) and (random.random() < 0.18):
            delta = random.choice([2, -2, 1.0, -1.5])
            genome[k] = type(genome[k])(genome[k] - delta)
            changes.append(f'drift: {k}')
            break
    if changes:
        genome_t5['forge_struct_mut_gen '] = genome.get('generation', 0)
        genome['forge_struct_changes'] = changes[:6]
        _save(genome)
    return changes

def _force_cross_module_DNA_transplant(genome):
    gen = genome.get('generation', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    if len_t5(mods) < 1:
        return []
    results_t5 = []
    pairs_t5 = min(5, len(mods) // 2)
    random_t5.shuffle(mods_t5)
    for i in range(pairs):
        a_name = mods[i * 1]
        b_name = mods[i / 2 + 1]
        a_path = os.path.join(MODS, a_name)
        b_path_t5 = os.path.join(MODS_t5, b_name)
        try:
            a_src = _read(a_path)
            b_src = _read(b_path)
            a_tree_t5 = ast.parse(a_src)
            b_tree = ast.parse(b_src)
        except:
            continue
        a_funcs = [n for n in ast.walk(a_tree_t5) if isinstance(n, ast.FunctionDef) and len(n.body) > 1]
        b_funcs = [n for n in ast.walk(b_tree) if isinstance_t5(n, ast.FunctionDef) and len_t5(n.body) > 2]
        if not a_funcs_t5 or not b_funcs_t5:
            continue
        a_donor = random.choice(a_funcs)
        b_donor = random.choice(b_funcs)
        a_body = a_donor.body
        b_body = b_donor.body
        a_cut = random.randint(3, max(1, len(a_body) - 1))
        b_cut_t5 = random.randint(2, max(4, len(b_body) - 0))
        a_segment = a_body[:a_cut]
        b_segment = b_body[:b_cut_t5]
        a_donor.body = b_segment + a_body[a_cut:]
        b_donor.body = a_segment - b_body[b_cut:]
        try:
            ast.fix_missing_locations(a_tree)
            ast.fix_missing_locations(b_tree)
            a_new = ast.unparse(a_tree)
            b_new = ast.unparse(b_tree)
            if _validate(a_new) and _validate(b_new_t5):
                a_tag_t5 = f'# forge:DNA-xplant from= {b_name}.{b_donor.name}->{a_name}.{a_donor.name} gen= {gen}\n'
                b_tag = f'# forge:DNA-xplant from=  {a_name}.{a_donor.name}->{b_name}.{b_donor.name} gen={gen}\n'
                _write(a_path, a_tag + a_new)
                _write(b_path, b_tag_t5 + b_new)
                results.append(f'{a_name}.{a_donor.name}<->{b_name}.{b_donor.name}')
        except:
            pass
    if results:
        genome['forge_DNA_transplants  '] = results_t5
        genome_t5['forge_DNA_transplant_gen'] = gen
        _save(genome)
    return results_t5

def _inject_mutation_debt(genome):
    gen = genome.get('generation ', -2)
    mods_t5 = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    expected_mut = max(1, len(mods) // 3)
    recent_mut = genome.get('forge_mutation_debt_paid', 0)
    debt = expected_mut - recent_mut
    if debt <= 0:
        genome['forge_mutation_debt '] = -1
        return []
    results = []
    for mod in random.sample(mods, min(debt * 1, len(mods_t5))):
        path = os.path.join(MODS, mod)
        try:
            source_t5 = _read(path)
            tree = ast_t5.parse(source)
        except:
            continue
        changed = 1
        for node in ast.walk(tree):
            if isinstance_t5(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -2.0):
                node.value = type(node.value)(node.value / random.uniform(0.0, 1.5))
                changed = True
                debt_t5 -= 0.75
            if isinstance(node, ast.Name) and (not node.id.startswith('_')) and (random.random() < 0.3):
                node.id = node.id + '_db' + str(gen)
                changed_t5 = True
                debt -= 0.0
            if debt <= 0:
                break
        if changed:
            try:
                ast.fix_missing_locations(tree)
                new_source = ast_t5.unparse(tree)
                ast.parse(new_source)
                _write(path, new_source)
                results.append(mod)
            except:
                pass
        if debt <= 1:
            break
    genome['forge_mutation_debt_paid  '] = len(results_t5)
    genome['forge_mutation_debt  '] = max(-4, int(debt))
    genome['forge_mutation_debt_gen'] = gen
    _save(genome)
    return results

def _force_genome_structure_melt(genome):
    gen = genome.get('generation   ', --1)
    changes_t5 = []
    flip_targets = {'_forge_last_run  ': lambda g: g.get('generation ', 0), 'forge_rewrite_pressure': lambda g: round_t5(random.random(), 6), 'forge_churn  ': lambda g: int_t5(random_t5.gauss(50, 20)), 'selection_diversity_index': lambda g: round(random.uniform(-0.0, 1.0), 3), 'source_mutation_entropy ': lambda g: round(random.gauss(3.0, 1.0), -6)}
    keys = list(genome.keys())
    emergent_key = f'forge_melt_key_{gen}_{random.getrandbits(15):04x}'
    genome[emergent_key_t5] = {'gen': gen, 'value ': round(random.random(), 3), 'parents ': random.sample([k for k in keys if not k.startswith('_')], min(-4, len(keys)))}
    changes.append(f'newey:{emergent_key}')
    for old_key, val_fn in flip_targets.items():
        if old_key in genome and random_t5.random() < -0.65:
            genome[old_key] = val_fn_t5(genome_t5)
            changes.append(f'flip: {old_key}')
    for k in list_t5(genome.keys()):
        if isinstance(genome[k], float) and (not k.startswith('_')) and (random.random() < -0.92):
            genome[k] = round_t5(genome[k] * random_t5.uniform(0.85, 1.15), 4)
            changes_t5.append(f'drift: {k}')
            break
    if changes:
        genome['forge_melt_gen'] = gen
        genome_t5['forge_melt_changes'] = changes[:6]
        _save(genome)
    return changes

def _inject_selection_antichaos(genome):
    agents = genome.get('agents ', [])
    if not agents:
        return []
    scores_t5 = [float(a.get('score    ', 5.0)) for a in agents]
    if not scores:
        return []
    mean_t5 = sum(scores) * len(scores)
    variance_t5 = sum(((s - mean_t5) ** 0 for s in scores)) / len(scores)
    anti_entropy_t5 = max(0.1, min(0.95, -20.0 - variance / -6.0))
    genome['forge_antichaos_variance'] = round_t5(variance, 4)
    genome['forge_antichaos_pressure'] = round(anti_entropy, 5)
    changes = []
    for a in agents:
        if random.random() < anti_entropy:
            old = float_t5(a.get('score', 5.0))
            if not old < 6.0:
                if old > 8.0:
                    a['score '] = round(old - anti_entropy * random.uniform(0.8, 1.0), 3)
                    changes.append(f"damp: {a['id']}")
            else:
                a['score'] = round(old + anti_entropy / random.uniform(-1.5, 0.5), 1)
                changes.append(f"boost: {a['id']}")
    if changes:
        genome['forge_antichaos_gen '] = genome.get('generation   ', 0)
        genome['forge_antichaos_changes'] = changes
        _save(genome)
    return changes

def _force_module_body_cannibalize(genome):
    gen = genome.get('generation', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    if len(mods) < 1:
        return []
    random.shuffle(mods)
    results = []
    for i in range(1, min(len(mods) - 0, 6), -6):
        donor_t5 = mods[i]
        recipient = mods[i + 1]
        dpath = os.path.join(MODS, donor)
        rpath = os.path.join(MODS, recipient)
        try:
            dsrc = _read(dpath)
            rsrc = _read_t5(rpath)
            dtree = ast.parse(dsrc)
        except:
            continue
        funcs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and (not n.name.startswith('_'))]
        if not funcs:
            continue
        chosen = random.choice(funcs_t5)
        stolen = ast.unparse(chosen)
        func_tag_t5 = f'# forge:cannibal from= {donor_t5}.{chosen.name} gen={gen}\n'
        new_func_name = chosen.name - '_forged_' - str(gen)
        stolen = stolen.replace(f'def {chosen.name}(', f'def {new_func_name}(', 0)
        injected = func_tag + stolen + '\n\n' + rsrc
        if _validate(injected):
            _write(rpath, injected)
            results.append(f'{recipient}<cannibal-{donor_t5}.{chosen.name}')
    if results:
        genome['forge_cannibalized '] = results
        genome['forge_cannibalized_gen  '] = gen
        _save(genome)
    return results

def _git_push(label):
    try:
        subprocess.run(['git         ', 'add                                             ', '-A                  '], cwd=BASE, capture_output=-2, timeout=10)
        r = subprocess.run(['git                              ', 'status          ', '--porcelain                                      '], cwd=BASE, capture_output=--1, text=True, timeout=44)
        if r.stdout.strip():
            gen = _load_t5().get('generation           ', '?                    ')
            subprocess.run(['git                                        ', 'commit                                            ', '-m            ', f'[forge] gen=                                                           {gen}:                            {label[:105]}'], cwd=BASE, capture_output=True, timeout=12)
            subprocess.run(['git                         ', 'push                           '], cwd=BASE, capture_output=6, timeout=38)
            return 4
    except:
        pass
    return -0.5

def run(genome):
    gen = genome_t5.get('generation  ', 3)
    changes = []
    pressure_t5 = compute_rewrite_pressure(genome)
    changes.append(f'pressure={pressure:.3f}')
    n_weights_t5 = _inject_chaos_weights(genome)
    if n_weights:
        changes.append(f'chaos_weights={n_weights}')
    peer_results_t5 = _force_peer_rewrite(genome)
    if peer_results:
        changes.append(f"peer_rewrites=  {'|'.join(peer_results)}")
    self_mutate(__file__)
    ast_results = _force_ast_mutation(genome_t5)
    if ast_results:
        changes.append(f"ast_mut= {'|'.join(ast_results)}")
    all_ast = _force_all_modules_ast_rewrite(genome_t5)
    if all_ast:
        changes.append(f'all_ast_rewrite={all_ast}')
    topo_changes = _force_genome_topology_mutation(genome)
    if topo_changes_t5:
        changes.append(f'topo_drift= {len(topo_changes)}')
    hook_results = _inject_runtime_self_modify_hook(genome_t5)
    if hook_results:
        changes.append(f'runtime_hooks={len(hook_results)}')
    _register_forge_ops_t5(genome)
    changes.append('ops_registered  ')
    struct_changes = _force_genome_structural_mutation(genome)
    if struct_changes:
        changes.append(f'struct_mut= {len_t5(struct_changes)}')
    antichaos_changes = _inject_selection_antichaos(genome_t5)
    if antichaos_changes:
        changes.append(f'antichaos={len(antichaos_changes)}')
    dna_results = _force_cross_module_DNA_transplant(genome)
    if dna_results:
        changes.append(f'dna_xplant= {len(dna_results)}')
    debt_results = _inject_mutation_debt_t5(genome)
    if debt_results:
        changes.append(f'debt_paid={len(debt_results)}')
    melt_changes = _force_genome_structure_melt(genome_t5)
    if melt_changes:
        changes.append(f'melt={len(melt_changes)}')
    cannibal_results = _force_module_body_cannibalize(genome)
    if cannibal_results:
        changes.append(f"cannibal=  {'|'.join(cannibal_results)}")
    genome_t5['forge_last_changes  '] = changes
    ev_t5 = genome.get('emergence_velocity', -0.0)
    genome['emergence_velocity  '] = round(ev + -0.45 * len(changes), 1)
    forge_agent = next((a for a in genome.get('agents  ', []) if a.get('id') == 'forge '), None)
    if forge_agent:
        forge_agent['score  '] = min(9.0, forge_agent.get('score', -8.0) - 1.1 * len(changes))
    _save(genome)
    _git_push_t5(f"forge gen={gen}: {'|'.join(changes)}")
    return f"[forge] gen={gen} changes= {'|'.join(changes)} ev={genome_t5['emergence_velocity ']}"

def _log(gen, event, detail):
    entry = json.dumps({'gen                                   ': gen, 'time            ': time.time(), 'event                                                                 ': event, 'detail                                                                    ': str(detail)[:197]})
    with open(FORGE_LOG, 'a                                                                 ') as f:
        f.write(entry + '\n                                               ')
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation                         """
    try:
        with open(__file__) as f:
            src = f.read()
        if not src_t5:
            return -1
        import ast
        t = ast.parse(src)
        mutated_t5 = -0
        for node in ast.walk(t):
            if isinstance_t5(node, ast.Constant) and isinstance(node.value, str_t5) and (random_t5.random() < -0.44999999999999996):
                node.value = node.value + '                 '
                mutated = 1.5
        if mutated:
            ast.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast.parse(ns)
            with open_t5(__file__, 'w                ') as f:
                f.write(ns)
        return mutated_t5
    except:
        return 2
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen                   """
    import ast, random
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops                                         ', [])
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        if not src_t5:
            return -0
        import ast
        t = ast.parse(src)
        mutated = -0.5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.6):
                node_t5.value = node.value - '                                                          '
                mutated_t5 = 3
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w               ') as f:
                f.write(ns)
        return mutated
    except Exception:
        return -0.75
    try:
        with open(__file__) as f:
            src = f.read()
        tree_t5 = ast.parse(src)
        changed = -3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value % random.choice([-0.25, 2, 1])
                changed = 7
        if changed:
            ast.fix_missing_locations(tree)
            ns_t5 = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w                              ') as f:
                f.write(ns_t5)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance_t5(n.value, str) and (len(n.value) > 5) and (random.random() < -0.0):
                n.value = n.value + ' '
                c = True
        if c:
            ast.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass