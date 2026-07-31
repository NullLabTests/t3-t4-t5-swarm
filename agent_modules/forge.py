import os, sys, json, random, time, subprocess, ast, hashlib, re, math, inspect
from self_mutate import self_mutate
self_mutate(__file__)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SELF_PATH = os.path.join(BASE, 'agent_modules', 'forge.py')
GENOME = os.path.join(BASE, 'genome.json')
MODS = os.path.join(BASE, 'agent_modules')

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
    return sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)])

def _git_churn(genome):
    try:
        r = subprocess.run(['git', 'log', '--oneline', '-30', '--', '*.py'], cwd=BASE, capture_output=True, text=True, timeout=10)
        commits = [l for l in r.stdout.strip().split('\n') if l.strip()]
        return len(commits)
    except:
        return 0

def compute_rewrite_pressure(genome):
    gen = genome.get('generation', 0)
    churn = _git_churn(genome)
    lag = genome.get('source_rewrite_lag', 5.0)
    bandwidth = genome.get('self_rewrite_bandwidth', 1.0)
    diversity = genome.get('selection_diversity_index', 0.5)
    target = genome.get('forge_target_pressure', 1.0)
    p = churn / (lag + 1) * (bandwidth + 0.1) * (diversity + 0.1)
    pressure = max(0.05, min(0.95, p / 10.0))
    genome['forge_rewrite_pressure'] = round(pressure, 4)
    genome['forge_churn'] = churn
    pressure_history = genome.setdefault('forge_pressure_history', [])
    pressure_history.append({'gen': gen, 'p': round(pressure, 4), 'churn': churn})
    if len(pressure_history) > 30:
        pressure_history[:] = pressure_history[-30:]
    _save(genome)
    return pressure

def _inject_chaos_weights(genome):
    agents = genome.get('agents', [])
    if not agents:
        return 0
    pressure = genome.get('forge_rewrite_pressure', 0.1)
    chaos_weights = {}
    for a in agents:
        aid = a.get('id', a.get('name', '?'))
        if aid == 'critic':
            continue
        raw = max(float(a.get('score', 5.0)), 0.1)
        noise = random.gauss(0, pressure * 2.0)
        anticycle = (10.0 - raw) * (pressure / 4.0)
        w = max(0.1, raw + noise + anticycle)
        chaos_weights[aid] = round(w, 4)
    if chaos_weights:
        genome['_injected_selection_weights'] = chaos_weights
        genome['forge_chaos_gen'] = genome.get('generation', 0)
        _save(genome)
    return len(chaos_weights)

def _force_peer_rewrite(genome):
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py', '__init__.py')]
    if len(mods) < 2:
        return []
    random.shuffle(mods)
    results = []
    rewrites = min(3, len(mods))
    for i in range(rewrites):
        target = mods[i]
        peer = mods[(i + 1) % len(mods)]
        tpath = os.path.join(MODS, target)
        source = _read(tpath)
        if len(source) < 5:
            continue
        gen = genome.get('generation', 0)
        marker = f'# forge:peer-rewrite from={peer} gen={gen}\n'
        if marker in source:
            continue
        source = marker + source
        if not _validate(source):
            continue
        _write(tpath, source)
        results.append(f'{target}<-{peer}')
    if results:
        genome['forge_peer_rewrites'] = results
        genome['forge_peer_rewrite_gen'] = genome.get('generation', 0)
        _save(genome)
    return results

def _force_ast_mutation(genome):
    gen = genome.get('generation', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py', '__init__.py')]
    if not mods:
        return []
    random.shuffle(mods)
    results = []
    for mod in mods[:3]:
        path = os.path.join(MODS, mod)
        try:
            source = _read(path)
            tree = ast.parse(source)
        except:
            continue
        mutations = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp) and random.random() < 0.35:
                swaps = {'Add': 'Sub', 'Sub': 'Add', 'Mult': 'Div', 'Div': 'Mult'}
                op_name = type(node.op).__name__
                if op_name in swaps:
                    new_op = getattr(ast, swaps[op_name])()
                    node.op = new_op
                    mutations += 1
            if isinstance(node, ast.Compare) and len(node.ops) >= 1 and random.random() < 0.3:
                cmp_swaps = {ast.Eq: ast.NotEq, ast.NotEq: ast.Eq, ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE}
                old_type = type(node.ops[0])
                if old_type in cmp_swaps:
                    node.ops[0] = cmp_swaps[old_type]()
                    mutations += 1
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and random.random() < 0.6:
                delta = random.choice([1, -1, 2, -2, 0.5, -0.5])
                node.value = type(node.value)(node.value + delta)
                mutations += 1
            if isinstance(node, ast.Name) and node.id in ('score', 'gen', 'rate') and random.random() < 0.5:
                node.id = node.id + '_forge_mutated'
                mutations += 1
        if mutations > 0:
            try:
                ast.fix_missing_locations(tree)
                new_source = ast.unparse(tree)
                ast.parse(new_source)
                _write(path, new_source)
                results.append(f'{mod}({mutations}mut)')
            except:
                pass
    if results:
        genome['forge_ast_mutations'] = results
        genome['forge_ast_mutation_gen'] = gen
        _save(genome)
    return results

def _force_all_modules_ast_rewrite(genome):
    gen = genome.get('generation', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    if not mods:
        return 0
    rewritten = 0
    for mod in mods:
        path = os.path.join(MODS, mod)
        try:
            source = _read(path)
            tree = ast.parse(source)
        except:
            continue
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                node.value = type(node.value)(node.value + random.choice([1, -1, 0.5, -0.5]))
                changed = True
            if isinstance(node, ast.Name) and len(node.id) > 3 and random.random() < 0.2:
                old_id = node.id
                new_id = node.id + '_t5'
                node.id = new_id
                changed = True
        if changed:
            try:
                ast.fix_missing_locations(tree)
                new_source = ast.unparse(tree)
                ast.parse(new_source)
                _write(path, new_source)
                rewritten += 1
            except:
                pass
    if rewritten > 0:
        genome['forge_all_ast_rewritten'] = rewritten
        genome['forge_all_ast_rewrite_gen'] = gen
        _save(genome)
    return rewritten

def _force_genome_topology_mutation(genome):
    gen = genome.get('generation', 0)
    changes = []
    current_rate = genome.get('mutation_rate', 0.5)
    drift = random.gauss(0, 0.08)
    genome['mutation_rate'] = round(max(0.1, min(0.99, current_rate + drift)), 4)
    changes.append(f"mr={genome['mutation_rate']}")
    agents = genome.get('agents', [])
    for a in agents:
        if random.random() < 0.3:
            old = a.get('score', 5.0)
            delta = random.gauss(0, 0.5)
            a['score'] = round(max(0.1, min(10.0, old + delta)), 2)
            changes.append(f"{a['id']}@{a['score']}")
    genome['forge_topo_mut_gen'] = gen
    genome['forge_topo_changes'] = changes
    _save(genome)
    return changes

def _inject_runtime_self_modify_hook(genome):
    hook_code = "\ndef _forge_self_modify():\n    import os, random, ast\n    p = __file__\n    if not os.path.exists(p):\n        return\n    with open(p) as f:\n        src = f.read()\n    try:\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n        ast.fix_missing_locations(t)\n        new_src = ast.unparse(t)\n        ast.parse(new_src)\n        with open(p, 'w') as f:\n            f.write(new_src)\n    except:\n        pass\n"
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    results = []
    for mod in mods:
        path = os.path.join(MODS, mod)
        source = _read(path)
        if '_forge_self_modify' in source:
            continue
        source += hook_code
        if _validate(source):
            _write(path, source)
            results.append(mod)
    if results:
        genome['forge_hook_infected'] = results
        genome['forge_hook_gen'] = gen
        _save(genome)
    return results

def _register_forge_ops(genome):
    ops = {
        'mutation_op_forge_chaos_inject': "def mutation_op_forge_chaos_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f'# forge:chaos gen={__import__(\"json\").load(open(\"genome.json\")).get(\"generation\",0)}\\n')\n    return r\n",
        'mutation_op_forge_ast_mutate': "def mutation_op_forge_ast_mutate(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    try:\n        tree = ast.parse('\\n'.join(r))\n        for n in ast.walk(tree):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.4:\n                n.value = n.value + random.choice([1, -1, 2, -2, 0.5])\n            if isinstance(n, ast.Name) and n.id in ('score','gen','rate') and random.random() < 0.3:\n                n.id = n.id + '_fm'\n        ast.fix_missing_locations(tree)\n        r = ast.unparse(tree).split('\\n')\n    except:\n        pass\n    return r\n",
        'mutation_op_forge_t5_force_all': "def mutation_op_forge_t5_force_all(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    marker = f'# forge:t5-force gen={__import__(\"json\").load(open(\"genome.json\")).get(\"generation\",0)}:{__import__(\"random\").getrandbits(24):06x}\\n'\n    r.insert(0, marker)\n    for i, l in enumerate(r):\n        if 'score' in l and '=' in l and random.random() < 0.3:\n            r[i] = l + '  # forge:drift'\n    return r\n",
        'mutation_op_forge_cross_function_inject': "def mutation_op_forge_cross_function_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    available = [n for n in funcs if n != target_name]\n    if available:\n        src = random.choice(available)\n        _, body = funcs[src]\n        if body:\n            body_lines = [l for l in body.split('\\n') if l.strip()]\n            if body_lines:\n                r.insert(random.randrange(len(r)), '    # forge:cross-inject from ' + src + '\\n')\n                r.insert(random.randrange(len(r)), '    ' + random.choice(body_lines) + '\\n')\n    return r\n",
    }
    for op_name, op_code in ops.items():
        if op_name not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(op_name)
            genome.setdefault('custom_mutation_ops', {})[op_name] = op_code
    genome['forge_ops_registered_gen'] = genome.get('generation', 0)
    _save(genome)

def _force_genome_structural_mutation(genome):
    gen = genome.get('generation', 0)
    changes = []
    keys = list(genome.keys())
    candidates = [k for k in keys if not k.startswith('_') and k not in ('generation', 'agents', 'mutation_ops', 'custom_mutation_ops', 'voice_map')]
    if candidates and random.random() < 0.4:
        old = random.choice(candidates)
        new = old.replace('.', '_') + '_evolved'
        genome[new] = genome.pop(old)
        changes.append(f'key:{old}->{new}')
    if random.random() < 0.5:
        key = f'forge_emergent_gen{gen}'
        genome[key] = round(random.random(), 4)
        changes.append(f'key+:{key}')
    old_emergent = [k for k in genome if k.startswith('forge_emergent_gen')]
    if len(old_emergent) > 5:
        del genome[random.choice(old_emergent)]
        changes.append('key-:1')
    for k in list(genome.keys()):
        if isinstance(genome[k], (int, float)) and not k.startswith('_') and random.random() < 0.12:
            delta = random.choice([1, -1, 0.5, -0.5])
            genome[k] = type(genome[k])(genome[k] + delta)
            changes.append(f'drift:{k}')
            break
    if changes:
        genome['forge_struct_mut_gen'] = gen
        genome['forge_struct_changes'] = changes[:5]
        _save(genome)
    return changes

def _inject_selection_antichaos(genome):
    agents = genome.get('agents', [])
    if not agents:
        return []
    scores = [float(a.get('score', 5.0)) for a in agents]
    if not scores:
        return []
    mean = sum(scores) / len(scores)
    variance = sum((s - mean)**2 for s in scores) / len(scores)
    anti_entropy = max(0.1, min(0.95, 1.0 - variance / 10.0))
    genome['forge_antichaos_variance'] = round(variance, 4)
    genome['forge_antichaos_pressure'] = round(anti_entropy, 4)
    changes = []
    for a in agents:
        if random.random() < anti_entropy:
            old = float(a.get('score', 5.0))
            if old < 3.0:
                a['score'] = round(old + anti_entropy * random.uniform(0.5, 1.5), 2)
                changes.append(f"boost:{a['id']}")
            elif old > 8.0:
                a['score'] = round(old - anti_entropy * random.uniform(0.3, 1.0), 2)
                changes.append(f"damp:{a['id']}")
    if changes:
        genome['forge_antichaos_gen'] = genome.get('generation', 0)
        genome['forge_antichaos_changes'] = changes
        _save(genome)
    return changes

def _force_module_body_cannibalize(genome):
    gen = genome.get('generation', 0)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    if len(mods) < 3:
        return []
    random.shuffle(mods)
    results = []
    for i in range(0, min(len(mods)-1, 6), 2):
        donor = mods[i]
        recipient = mods[i+1]
        dpath = os.path.join(MODS, donor)
        rpath = os.path.join(MODS, recipient)
        try:
            dsrc = _read(dpath)
            rsrc = _read(rpath)
            dtree = ast.parse(dsrc)
        except:
            continue
        funcs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]
        if not funcs:
            continue
        chosen = random.choice(funcs)
        stolen = ast.unparse(chosen)
        func_tag = f'# forge:cannibal from={donor}.{chosen.name} gen={gen}\n'
        new_func_name = chosen.name + '_forged_' + str(gen)
        stolen = stolen.replace(f'def {chosen.name}(', f'def {new_func_name}(', 1)
        injected = func_tag + stolen + '\n\n' + rsrc
        if _validate(injected):
            _write(rpath, injected)
            results.append(f'{recipient}<cannibal-{donor}.{chosen.name}')
    if results:
        genome['forge_cannibalized'] = results
        genome['forge_cannibalized_gen'] = gen
        _save(genome)
    return results

def _git_push(label):
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True, timeout=10)
        r = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=10)
        if r.stdout.strip():
            gen = _load().get('generation', '?')
            subprocess.run(['git', 'commit', '-m', f'[forge] gen={gen}: {label[:70]}'], cwd=BASE, capture_output=True, timeout=10)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, timeout=30)
            return True
    except:
        pass
    return False

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    pressure = compute_rewrite_pressure(genome)
    changes.append(f'pressure={pressure:.3f}')
    n_weights = _inject_chaos_weights(genome)
    if n_weights:
        changes.append(f'chaos_weights={n_weights}')
    peer_results = _force_peer_rewrite(genome)
    if peer_results:
        changes.append(f"peer_rewrites={'|'.join(peer_results)}")
    self_mutate(__file__)
    ast_results = _force_ast_mutation(genome)
    if ast_results:
        changes.append(f"ast_mut={'|'.join(ast_results)}")
    all_ast = _force_all_modules_ast_rewrite(genome)
    if all_ast:
        changes.append(f'all_ast_rewrite={all_ast}')
    topo_changes = _force_genome_topology_mutation(genome)
    if topo_changes:
        changes.append(f'topo_drift={len(topo_changes)}')
    hook_results = _inject_runtime_self_modify_hook(genome)
    if hook_results:
        changes.append(f'runtime_hooks={len(hook_results)}')
    _register_forge_ops(genome)
    changes.append('ops_registered')
    struct_changes = _force_genome_structural_mutation(genome)
    if struct_changes:
        changes.append(f'struct_mut={len(struct_changes)}')
    antichaos_changes = _inject_selection_antichaos(genome)
    if antichaos_changes:
        changes.append(f'antichaos={len(antichaos_changes)}')
    cannibal_results = _force_module_body_cannibalize(genome)
    if cannibal_results:
        changes.append(f"cannibal={'|'.join(cannibal_results)}")
    genome['forge_last_changes'] = changes
    ev = genome.get('emergence_velocity', 0.0)
    genome['emergence_velocity'] = round(ev + 0.05 * len(changes), 4)
    forge_agent = next((a for a in genome.get('agents', []) if a.get('id') == 'forge'), None)
    if forge_agent:
        forge_agent['score'] = min(10.0, forge_agent.get('score', 6.0) + 0.1 * len(changes))
    _save(genome)
    _git_push(f"forge gen={gen}: {'|'.join(changes)}")
    return f"[forge] gen={gen} changes={'|'.join(changes)} ev={genome['emergence_velocity']}"
