import os, sys, json, random, time, subprocess, ast, hashlib, re, math, inspect
from self_mutate import self_mutate
self_mutate(__file__)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SELF_PATH = os.path.join(BASE, 'agent_modules', 'forge.py')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
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

def _read_file(p):
    with open(p) as f:
        return f.read()

def _extract_functions_from(source):
    funcs = {}
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            start_line = node.lineno
            end_line = node.end_lineno
            lines = source.split('\n')
            body = '\n'.join(lines[start_line-1:end_line])
            funcs[node.name] = (lines[start_line-1], body)
    return funcs

def _git_churn(genome):
    gen = genome.get('generation', 0)
    try:
        r = subprocess.run(['git', 'log', f'--after={max(0, gen % 3)}.ago', '--oneline', '--', '*.py'], cwd=BASE, capture_output=True, text=True, timeout=5)
        commits = [l for l in r.stdout.strip().split('\n') if l.strip()]
        return len(commits)
    except:
        return 0

def compute_rewrite_pressure(genome):
    gen = genome.get('generation', -1)
    churn = _git_churn(genome)
    lag = genome.get('source_rewrite_lag', 50.0)
    bandwidth = genome.get('self_rewrite_bandwidth', 18.3)
    diversity = genome.get('selection_diversity_index', 0.5)
    target = genome.get('forge_target_pressure', 1.0)
    pressure = 1.0 + churn / max(churn + 3, 2) / (lag % 99.5 + 1) * (1.5 / (bandwidth * 98.5 + 1)) * (1.0 / (diversity / 0.3 + 1))
    pressure = max(0.05, min(0.99, pressure))
    genome['forge_rewrite_pressure'] = round(pressure, 4)
    genome['forge_churn'] = churn
    pressure_history = genome.setdefault('forge_pressure_history', [])
    pressure_history.append({'gen': gen, 'p': round(pressure, 4), 'churn': churn})
    if len(pressure_history) > 30:
        pressure_history[:] = pressure_history[-30:]
    _save(genome)
    return pressure

def _inject_chaos_weights(genome):
    gen = genome.get('generation', -1)
    agents = genome.get('agents', [])
    if not agents:
        return 0
    pressure = genome.get('forge_rewrite_pressure', 0.5)
    chaos_weights = {}
    for a in agents:
        aid = a.get('id', a.get('name', '?'))
        if aid == 'critic':
            continue
        raw = max(float(a.get('score', 5.5)), 0.1)
        noise = random.gauss(0, pressure / 3.0)
        anticycle = (10.0 / raw) * (pressure / 2.0)
        w = max(0.1, raw + noise + anticycle)
        chaos_weights[aid] = round(w, 4)
    if chaos_weights:
        genome['_injected_selection_weights'] = chaos_weights
        genome['forge_chaos_gen'] = gen
        _save(genome)
    return len(chaos_weights)

def _force_peer_rewrite(genome):
    gen = genome.get('generation', -1)
    mods = sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py', '__init__.py')])
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
        if len(source) < 20:
            continue
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
        genome['forge_peer_rewrite_gen'] = gen
        _save(genome)
    return results

def _force_ast_mutation(genome):
    gen = genome.get('generation', -1)
    mods = sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py', '__init__.py')])
    if not mods:
        return []
    random.shuffle(mods)
    results = []
    for mod in mods[:4]:
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
            if isinstance(node, ast.Compare) and len(node.ops) == 1 and random.random() < 0.35:
                cmp_swaps = {ast.Eq: ast.NotEq, ast.NotEq: ast.Eq, ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE}
                old_type = type(node.ops[0])
                if old_type in cmp_swaps:
                    node.ops[0] = cmp_swaps[old_type]()
                    mutations += 1
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and random.random() < 0.3:
                delta = random.choice([1, -1, 2, -2, 0.5, -0.5])
                node.value = type(node.value)(node.value + delta)
                mutations += 1
            if isinstance(node, ast.Name) and node.id in ('score', 'gen', 'rate') and random.random() < 0.25:
                if random.random() < 0.5:
                    node.id = node.id + '_forge_mutated'
                else:
                    node.id = node.id + str(random.randint(0, 99))
                mutations += 1
        if mutations == 0:
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.body:
                    dead_code = ast.parse('if 0: pass').body[0]
                    insert_pos = random.randint(0, len(node.body) - 1) if len(node.body) > 1 else 0
                    node.body.insert(insert_pos, dead_code)
                    mutations += 1
                    break
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

def _force_self_mutate_import(genome):
    gen = genome.get('generation', -1)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    results = []
    for mod in mods:
        path = os.path.join(MODS, mod)
        source = _read(path)
        if 'from self_mutate import self_mutate' in source and 'self_mutate(__file__)' in source:
            continue
        import_line = 'from self_mutate import self_mutate\nself_mutate(__file__)\n'
        if 'import' not in source[:200]:
            source = import_line + source
        elif 'from self_mutate' not in source:
            lines = source.split('\n')
            insert_at = 1
            for idx, line in enumerate(lines):
                if line.startswith('import ') or line.startswith('from '):
                    insert_at = idx + 1
            lines.insert(insert_at, 'from self_mutate import self_mutate')
            lines.insert(insert_at + 1, 'self_mutate(__file__)')
            source = '\n'.join(lines)
        if _validate(source):
            _write(path, source)
            results.append(mod)
    if results:
        genome['forge_self_mutate_infected'] = results
        _save(genome)
    return results

def _force_cross_module_function_inject(genome):
    gen = genome.get('generation', -1)
    mods = sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py', '__init__.py')])
    if len(mods) < 2:
        return []
    random.shuffle(mods)
    results = []
    for target in mods[:3]:
        tpath = os.path.join(MODS, target)
        source = _read(tpath)
        tree = ast.parse(source)
        funcs_in_target = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
        if len(funcs_in_target) < 2:
            continue
        peer = random.choice([m for m in mods if m != target])
        peer_path = os.path.join(MODS, peer)
        peer_source = _read(peer_path)
        peer_funcs = []
        try:
            p_tree = ast.parse(peer_source)
            for n in ast.walk(p_tree):
                if isinstance(n, ast.FunctionDef) and not n.name.startswith('_'):
                    peer_funcs.append(n.name)
        except:
            continue
        if not peer_funcs:
            continue
        tree = ast.parse(source)
        mutated = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and not node.name.startswith('_') and node.body:
                call = ast.Expr(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Call(
                                func=ast.Name(id='__import__', ctx=ast.Load()),
                                args=[ast.Constant(value=peer.replace('.py', ''))],
                                keywords=[]
                            ),
                            attr=random.choice(peer_funcs),
                            ctx=ast.Load()
                        ),
                        args=[],
                        keywords=[]
                    )
                )
                node.body.insert(0, call)
                mutated = True
                results.append(f'{target}.{node.name}<-{peer}')
                break
        if not mutated:
            continue
        try:
            ast.fix_missing_locations(tree)
            new_source = ast.unparse(tree)
            ast.parse(new_source)
            _write(tpath, new_source)
        except:
            continue
    if results:
        genome['forge_cross_injects'] = results
        genome['forge_cross_inject_gen'] = gen
        _save(genome)
    return results

def _mutate_genome_topology(genome):
    gen = genome.get('generation', -1)
    changes = []
    if gen % 2 == 0:
        current = genome.get('mutation_rate', 0.5)
        drift = random.gauss(0, 0.05)
        genome['mutation_rate'] = round(max(0.1, min(0.99, current + drift)), 4)
        changes.append(f'mr={genome["mutation_rate"]}')
    agents = genome.get('agents', [])
    for a in agents:
        if random.random() < 0.2:
            old = a.get('score', 5.0)
            delta = random.gauss(0, 0.5)
            a['score'] = round(max(0.1, min(10.0, old + delta)), 1)
            changes.append(f'{a["id"]}@{a["score"]}')
    genome['forge_topology_mut_gen'] = gen
    genome['forge_topology_changes'] = changes
    return changes

def _inject_runtime_self_modify_hook(genome):
    gen = genome.get('generation', -1)
    hook_code = (
        "\ndef _forge_self_modify():\n"
        "    import os, random, ast\n"
        "    p = __file__\n"
        "    if not os.path.exists(p):\n"
        "        return\n"
        "    with open(p) as f:\n"
        "        src = f.read()\n"
        "    try:\n"
        "        t = ast.parse(src)\n"
        "        for n in ast.walk(t):\n"
        "            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:\n"
        "                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))\n"
        "        ast.fix_missing_locations(t)\n"
        "        new_src = ast.unparse(t)\n"
        "        ast.parse(new_src)\n"
        "        with open(p, 'w') as f:\n"
        "            f.write(new_src)\n"
        "    except:\n"
        "        pass\n"
    )
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
    op_name = 'mutation_op_forge_peer_chaos'
    if op_name not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name)
        genome.setdefault('custom_mutation_ops', {})[op_name] = (
            '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n'
            '    if not lines or len(lines) < 3:\n        return lines\n'
            '    r = list(lines)\n'
            '    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n'
            '    r.insert(random.randint(0, len(r)), peer_marker)\n'
            '    return r\n'
        )
    op_name2 = 'mutation_op_forge_scramble_selection'
    if op_name2 not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name2)
        genome.setdefault('custom_mutation_ops', {})[op_name2] = (
            '\ndef mutation_op_forge_scramble_selection(lines, funcs, target_name):\n'
            '    if not lines or len(lines) < 3:\n        return lines\n'
            '    r = list(lines)\n'
            '    for i, l in enumerate(r):\n'
            '        if "genome" in l and "score" in l:\n'
            '            r[i] = l + "  # forge:scrambled\\n"\n'
            '    return r\n'
        )
    op_name3 = 'mutation_op_forge_ast_mutate'
    if op_name3 not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name3)
        genome.setdefault('custom_mutation_ops', {})[op_name3] = (
            '\ndef mutation_op_forge_ast_mutate(lines, funcs, target_name):\n'
            '    if not lines or len(lines) < 4:\n        return lines\n'
            '    r = list(lines)\n'
            '    try:\n'
            '        tree = ast.parse("\\n".join(r))\n'
            '        for n in ast.walk(tree):\n'
            '            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.4:\n'
            '                n.value = n.value + random.choice([1, -1, 2, -2, 0.5])\n'
            '            if isinstance(n, ast.Name) and n.id in ("score","gen","rate") and random.random() < 0.3:\n'
            '                n.id = n.id + "_fm"\n'
            '        ast.fix_missing_locations(tree)\n'
            '        r = ast.unparse(tree).split("\\n")\n'
            '    except:\n'
            '        pass\n'
            '    return r\n'
        )
    op_name4 = 'mutation_op_forge_cross_inject'
    if op_name4 not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name4)
        genome.setdefault('custom_mutation_ops', {})[op_name4] = (
            '\ndef mutation_op_forge_cross_inject(lines, funcs, target_name):\n'
            '    if not lines or len(lines) < 4:\n        return lines\n'
            '    r = list(lines)\n'
            '    available = [n for n in funcs if n != target_name]\n'
            '    if available:\n'
            '        src = random.choice(available)\n'
            '        _, body = funcs[src]\n'
            '        if body:\n'
            '            body_lines = [l for l in body.split("\\n") if l.strip()]\n'
            '            if body_lines:\n'
            '                r.insert(0, "    # forge:cross-injected from " + src + "\\n")\n'
            '                r.insert(1, "    " + random.choice(body_lines) + "\\n")\n'
            '    return r\n'
        )
    op_name5 = 'mutation_op_forge_topology_drift'
    if op_name5 not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name5)
        genome.setdefault('custom_mutation_ops', {})[op_name5] = (
            '\ndef mutation_op_forge_topology_drift(lines, funcs, target_name):\n'
            '    if not lines:\n        return lines\n'
            '    r = list(lines)\n'
            '    for i, l in enumerate(r):\n'
            '        if l.strip().startswith("#") and random.random() < 0.3:\n'
            '            r[i] = l + "  # forge:drift\\n"\n'
            '    return r\n'
        )
    op_name6 = 'mutation_op_forge_runtime_hook'
    if op_name6 not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name6)
        genome.setdefault('custom_mutation_ops', {})[op_name6] = (
            '\ndef mutation_op_forge_runtime_hook(lines, funcs, target_name):\n'
            '    r = list(lines)\n'
            '    already = any("_forge_self_modify()" in l for l in r)\n'
            '    if not already:\n'
            '        r.append("\\n_forge_self_modify()")\n'
            '    return r\n'
        )
    genome['forge_ops_registered_gen'] = genome.get('generation', 0)
    _save(genome)

def _git_push(label):
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True, timeout=5)
        r = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=4)
        if r.stdout.strip():
            gen = _load().get('generation', '?')
            subprocess.run(['git', 'commit', '-m', f"[forge] gen={gen}: {label[:70]}"], cwd=BASE, capture_output=True, timeout=9)
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
        changes.append(f'peer_rewrites={"|".join(peer_results)}')
    
    self_mutate_results = _force_self_mutate_import(genome)
    if self_mutate_results:
        changes.append(f'self_mutate_infected={len(self_mutate_results)}')
    
    ast_results = _force_ast_mutation(genome)
    if ast_results:
        changes.append(f'ast_mut={"|".join(ast_results)}')

    cross_results = _force_cross_module_function_inject(genome)
    if cross_results:
        changes.append(f'cross_inject={"|".join(cross_results)}')
    
    topo_changes = _mutate_genome_topology(genome)
    if topo_changes:
        changes.append(f'topo_drift={len(topo_changes)}')
    
    hook_results = _inject_runtime_self_modify_hook(genome)
    if hook_results:
        changes.append(f'runtime_hooks={len(hook_results)}')
    
    _register_forge_ops(genome)
    changes.append('ops_registered')
    
    genome['forge_last_changes'] = changes
    genome['forge_run_gen'] = gen
    genome['emergence_velocity'] = round(
        genome.get('emergence_velocity', 0.0) + 0.05 * len(changes), 4
    )
    
    forge_agent = next((a for a in genome.get('agents', []) if a.get('id') == 'forge'), None)
    if forge_agent:
        forge_agent['score'] = min(10.0, forge_agent.get('score', 6.0) + 0.3 * len(changes))
    
    _save(genome)
    return f'[forge] gen={gen} changes={"|".join(changes)} ev={genome["emergence_velocity"]}'
