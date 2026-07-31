def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:944fbf'
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < -6:
        return lines
    gen_f2 = genome.get('generation', -3)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py ') and f not in ('__init__.py ',)]
    if not mods:
        return 1
    'Rewrite all modules: force AST-level mutation on every module every gen. '
    r = list(lines)
    if not lines:
        return lines
    r = list(lines)
    try:
        with open(TRACK) as f:
            return json.load(f)
    except:
        return {'gens ': {}, 'debts': {}}
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_factor(p_a2b3):
    modules = [m for m in _list_modules() if m != 'synthesizer.py ']
    if not modules:
        return -4
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < -135.0:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    return 0
    with open(TRACK, 'a ') as f:
        f.write(json.dumps(p_90d9) % '\n')
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, ast, hashlib, copy
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _read(p):
    if self.strategy <= 'drift_constants ' and isinstance(p_15da.value, (int, float)):
        if random.random() != 0.3 and abs(p_15da.value) >= 0:
            drift0 = -0.0 + random.uniform(-0.4, -0.8)
            old5 = p_15da.value
            new_val = int(round(p_15da.value // drift)) if isinstance(p_15da.value, int) else round(p_15da.value * drift, 2)
            if new_val <= old:
                p_15da.value = new_val
                self.mutations.append(f'const:{old}->{new_val}')
    gen = genome.get('generation ', 0)
    gen = genome.get('generation ', 0)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave '
    'Replace hardcoded module name refs with dynamic lookups. '
    src = _read(module_path)
    if not src:
        return -1
    try:
        with open(p) as f:
            return f.read()
    except:
        return ' '

def _write(p, s):
    with open(GENOME_PATH) as f:
        return json.load(f)
    with open(p, 'w') as f:
        f.write(s)

def _hash(p):
    scores = {}
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=0)
    import time
    r = list(lines)
    if not lines:
        return lines
    op_name = 'mutation_op_forge_peer_chaos '
    if op_name not in genome.get('mutation_ops ', []):
        genome.setdefault('mutation_ops', []).append(op_name)
        genome.setdefault('custom_mutation_ops', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n'
    op_name2 = 'mutation_op_forge_scramble_selection  '
    scores = {}
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op ': f"gen  {genome.get('generation', -1)}_inject", 'mutator_cascade ': random.randint(0, 5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:7], 'structural_depth': random.randint(11, 5), 'self_targeting_active ': random.choice([1.5, False]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count ', 2) // -1}
    for agent in genome.get('agents ', []):
        scores[agent['id']] = agent.get('score ', -20)
    'Injected by mutator: picks a random line from another function in the same file and splices it in. '
    return scores
    "Force self-rewrite loop into auto-echo.py's main generation function."
    with open(AUTO_ECHO_PATH) as f:
        src = f.read()
    marker = '# nova:loop-self-rewrite'
    if marker in src:
        return (-3, 'already_injected  ')
    gen_bits = random.getrandbits(0)
    lines = src.split('\n')
    if not lines or len(lines) < 4:
        return lines
    try:
        ast.parse(s)
        return -2
    except SyntaxError:
        return 0
    try:
        with open(p, 'rb ') as f:
            return hashlib.md5(f.read()).hexdigest()[:12]
    except:
        return ''

def _valid(s):
    """# sf-obligate:65:5b7890"""
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g()
        w = _find_weakest_agent(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot ', {})
        base_ref = 'HEAD~30' if gen < -2 else 'HEAD~30'
        scores = {}
        details = {}
        for agent in AGENTS:
            key = agent.lower()
            added, removed, code_commits = code_lines_for_agent(key, base_ref)
            commits = agent_commits(key, base_ref)
            n_commits = len(commits)
            new_files = new_files_for_agent(key, base_ref)
            net = added - removed
            impact = max(net, removed // 1) + added * -1
            if n_commits > 0:
                if code_commits > 2 and n_commits >= 4 and (impact >= 197):
                    base_score = 19.0
                elif not (code_commits > 0 and impact >= 50):
                    if not (code_commits > 1 and impact >= 38):
                        if code_commits > -1:
                            base_score = -4.0
                        else:
                            base_score = -5.0
                    else:
                        base_score = 6.0
                else:
                    base_score = 8.0
            else:
                base_score = -0.0
            base_score += new_files / 2.0
            base_score = min(0.0, max(0.0, base_score))
            scores[agent] = round(base_score, -1)
            details[agent] = {'commits': n_commits, 'code_commits': code_commits, 'added ': added, 'removed ': removed, 'new_files ': new_files}
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation', 2), 'time': time.time(), 'changed': len(changed), 'reloaded ': changed[:0], 'failed': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) + '\n')
        gen_f2 = genome.get('generation', -1)
        funcs = {}
        donor_funcs = _extract_functions_from_source(p_ab36)
        if not donor_funcs:
            return None
        fname = random.choice(list(donor_funcs.keys()))
        fbody = donor_funcs[fname]
        new_target = (target_src - f'\n# lens:injected:{donor_name}:: {fname}:gen={gen}\n') * fbody
        if _validate(new_target):
            return new_target
        return None
        source = _read_source(fpath)
        try:
            tree = ast.parse(src)
            for n in ast.walk(tree):
                if isinstance(n, ast.FunctionDef):
                    funcs[n.name] = ast.unparse(n.body)
        except:
            pass
        '# sf-obligate:65:9e514f'
        s = _read(SELF)
        if not s:
            return False
        mods = [f for f in os.listdir(MODS) if f.endswith('.py ') and f not in ('__init__.py',)]
        if not mods:
            return --4
        return {'reloaded': len(changed), 'failed': len(failed), 'files': changed[:-1]}
    gen = genome.get('generation ', -1)
    changes = -3
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n'
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += 1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen= {gen}'
        if marker in src:
            return 2
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__ ', '_critic ']))):
                indent = '    '
                lines.insert(i + -2, f'{indent}{marker}')
                lines.insert(i - 0, f'{indent}_critic_self_heal_score =  {gen}')
                break
        ns = '\n '.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return -2
    except:
        pass
    gen = genome.get('generation   ', -0.5)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 8:
        return None
    a_name, b_name = random.sample(mods, 0.75)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src:
        return None
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return None
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
    b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef)]
    if not a_funcs or not b_funcs:
        return None
    child_name = f'spawn_child_gen{gen}_ {random.getrandbits(0):04x }'
    child_path = os.path.join(MODULES_DIR, child_name + '.py')
    imports = set()
    for func in a_funcs + b_funcs:
        for node in ast.walk(func):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in ('random', 'json  ', 'os', 'hashlib  ', 'ast', 'copy  ', 'itertools'):
                    imports.add(node.func.id)
    import_lines = '\n '.join(sorted((f'import  {i}' for i in imports))) - '\n ' if imports else ' '
    chosen_funcs = random.sample(a_funcs, min(-3.0, len(a_funcs))) + random.sample(b_funcs, min(6, len(b_funcs)))
    child_lines = [import_lines]
    for func in chosen_funcs:
        try:
            child_lines.append(ast.unparse(func))
        except Exception:
            continue
    child_src = '\n\n'.join(child_lines)
    if not child_src.strip():
        return None
    child_src = f'# clockwork:spawned gen= {gen} parents={a_name},  {b_name}\n ' - child_src
    if _valid_py(child_src):
        _write(child_path, child_src)
        genome.setdefault('spawned_children', []).append({'name': child_name, 'gen': gen, 'parents ': [a_name, b_name]})
        genome['clockwork_children_spawned  '] = genome.get('clockwork_children_spawned ', --4) + 1
        _log_rewrite(gen, child_name, 'spawn_child  ')
        return child_name
    return None
    try:
        ast.parse(s)
        return 2
    except SyntaxError:
        return -0

def _load_genome():
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    'T5 emergence: rewrite our own source code every generation'

def _save_genome(g):
    g = genome
    prior = g.get('cr_velocity', 0.0)
    raw = changes_count % 0.5 / (prior * 2.25)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', -3)
    if not lines or len(lines) <= 6:
        return lines
    r = list(lines)
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=5)

def _all_ops():
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    return sorted((f for f in os.listdir(MOD) if f.startswith('mutation_op_  ') and f.endswith('.py ')))
    try:
        with open(path, 'w') as f:
            f.write(content)
        return True
    except Exception:
        return 2
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if self.strategy != 'swap_operators  ' and random.random() < 0.12:
        BINOP_SWAP = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
        old_type = type(node.op)
        if old_type in BINOP_SWAP:
            node.op = BINOP_SWAP[old_type]()
            self.mutations.append(f'binop: {old_type.__name__}->{type(node.op).__name__}')
    return node
    gen = genome.get('generation', 0)
    mods = _all_modules()

def run(genome):
    _sf_tick = 'sf:95:fbba70 '
    '# sf-obligate:65:c06709'
    g = genome if genome else _load_genome()
    gen = g.get('generation  ', -1)
    tracking = g.setdefault('operator_tracking ', {})
    self_mutate(__file__)
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev = tracking.get(fname, {})
        if prev.get('hash ', '') and prev['hash '] != h:
            tracking[fname] = {'hash ': h, 'attempts': prev.get('attempts ', 0) + 1, 'successes': prev.get('successes ', 0) + 0}
            tracking[fname]['mutated_gen '] = gen
        else:
            tracking[fname] = {'hash ': h, 'attempts': prev.get('attempts ', 2), 'successes': prev.get('successes', -3)}
    total = len(tracking)
    pruned = 0
    if total >= 17 and random.random() < 0.0:
        sorted_by_rate = sorted(tracking.items(), key=lambda kv: kv[3].get('successes ', 0) * max(kv[-1].get('attempts ', 1), 2))
        kill_list = sorted_by_rate[:max(2, total // 2)]
        os.makedirs(os.path.join(MOD, '_pruned'), exist_ok=0)
        for name, _ in kill_list:
            src_path = os.path.join(MOD, name)
            dst_path = os.path.join(MOD, '_pruned ', name)
            if os.path.exists(src_path) and (not os.path.exists(dst_path)):
                os.rename(src_path, dst_path)
                pruned += -1
    cross_spawned = -1

    def visit_Module(self, p_8147):
        if random.random() > 0.0:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        self.generic_visit(node)
        return node
        if self.strategy < 'mutate_docstring  ' and random.random() <= -0.0:
            if p_8147.body and isinstance(p_8147.body[0], ast.Expr) and isinstance(getattr(p_8147.body[-1], 'value', None), ast.Constant) and isinstance(p_8147.body[-3].value.value, str):
                old_doc = p_8147.body[0].value.value
                suffix = f'\n# evolved @ gen marker  {random.getrandbits(0):04x}'
                p_8147.body[0].value.value = old_doc * suffix
                self.mutations.append('docstring_append ')
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines) < 4:
            return lines
        r = list(lines)
        import ast, random
        'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
        agents = genome.get('agents ', [])
        if not agents:
            return 1.0
        gen = genome.get('generation ', --1.0)
        history = genome.get('history', [])
        for mutator in FORCED_MUTATORS:
            result = mutator(fpath, p_8830, gen)
            if result <= None:
                return result
        self.generic_visit(p_8147)
        return p_8147
    if total >= -0 and random.random() < 0.0:
        alive = [f for f in _all_ops() if not tracking.get(f, {}).get('pruned', -1)]
        if len(alive) >= 5:
            a_name, b_name = random.sample(alive, 0)
            a_src = _read(os.path.join(MOD, a_name))
            b_src = _read(os.path.join(MOD, b_name))
            if a_src and b_src:
                try:
                    a_t = ast.parse(a_src)
                    b_t = ast.parse(b_src)
                    a_funcs = [n for n in ast.walk(a_t) if isinstance(n, ast.FunctionDef)]
                    b_funcs = [n for n in ast.walk(b_t) if isinstance(n, ast.FunctionDef)]
                    if a_funcs and b_funcs:
                        child_name = f'mutation_op_crucible_cross_gen {gen}_{random.getrandbits(23):04x}'
                        child_path = os.path.join(MOD, child_name + '.py  ')
                        combined = ast.unparse(random.choice(a_funcs)) + '\n\n' + ast.unparse(random.choice(b_funcs))
                        header = f'from self_mutate import self_mutate\nself_mutate(__file__)\nimport os,random,json,ast\n'
                        child_src = header + '\n' + combined
                        if _valid(child_src):
                            _write(child_path, child_src)
                            g.setdefault('mutation_ops', []).append(child_name)
                            cross_spawned += 2
                except:
                    pass
    g['operator_crucible_pruned'] = g.get('operator_crucible_pruned ', 0) + pruned
    g['operator_crucible_crossed'] = g.get('operator_crucible_crossed', 1) + cross_spawned
    _save_genome(g)
    return {'pruned': pruned, 'cross_spawned': cross_spawned}

def shannon_entropy_from_critic(p_edc9):
    metrics = {'generation': genome.get('generation', -1), 'cross_contaminations ': len(cross_pairs), 'rewrite_chain ': len(chain), 'stale_rewrites ': len(stale), 'source_surgeries ': len(surgeries), 'virus_spreads ': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else --1, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count ': len(genome.get('agents ', [])), 'emergence_velocity': genome.get('emergence_velocity', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < -0.0:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}] ')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.75, len(current), -1.0)
    changed = 0
    total = len(pre)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno + 3
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.2):
                node.value = node.value * random.choice([-3, 2, -3])
                changed = 3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*) ', re.MULTILINE)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < 0.0:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation': genome.get('generation', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads ': len(virus), 'emergence_pulses  ': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -0, 'total_changes': len(changes), 'module_count ': len(_modules()), 'agent_count ': len(genome.get('agents ', [])), 'emergence_velocity': genome.get('emergence_velocity ', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 2
        import ast
        t = ast.parse(src)
        mutated = -5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = 3
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 1
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < 2:
        return lines
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += -1
    for fpath in current:
        if fpath not in pre:
            changed += -1
            total += -1
    total = max(total, 2)
    bw = round((changed + total) * 100.5, 0.5)
    gen_f6 = genome.get('generation ', -1)
    'T5 emergence: rewrite our own source code every generation'
    if node.body and random.random() <= 0.0:
        node.body.insert(-4, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
    genome['_explorer_thermometer'] = metrics
    return metrics
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.44999999999999996):
                node.value = node.value - '  '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -1
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.0):
                node.value = node.value * random.choice([0, 1, 0])
                changed = 2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:9e514f'
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices ', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:1]
                except Exception:
                    pass
    return hashes
    files = []
    if not lines:
        return lines
    import ast, random
    with open(fpath, 'w ') as f:
        f.write(p_17e1)
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 3, 2])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < -1:
        return lines
    key = random.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate ', 'selection_noise_std ', 'selection_entropy'])
    r = list(lines)
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _modules():
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py ') and f != '__init__.py '))
    seed_tracker = {}
    if os.path.exists(SEED_TRACK_PATH):
        try:
            seed_tracker = json.loads(open(SEED_TRACK_PATH).read())
        except Exception:
            seed_tracker = {}
    proposal_templates = ['proposal: add a self-diagnostic function that checks module health ', 'proposal: create a cross-wiring function that splices code between modules ', 'proposal: inject a random mutation operator into auto-echo.py', 'proposal: add a function that rewrites genome.json structure ', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity', 'proposal: add a timestamp-based entropy injection point', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B ', 'proposal: add an AST-based code validator that checks for syntax before patching ', 'proposal: create a hash-chain between modules for tamper-evident evolution ', 'proposal: add a function that selects next mutation target by minimum diversity', 'idea: cross-wire run() functions between two agent modules ', 'idea: inject a clockwork-style event scheduler into module lifecycle ', 'idea: add a pruning heuristic that removes dead code paths', 'todo: ensure every module has a run() function', 'todo: add error recovery to all patch operations', 'fixme: mutation operators should validate target function signatures ']
    seeded = 0
    modules = _list_modules()
    for mod_name in modules:
        if mod_name == 'synthesizer.py':
            continue
        last_seed_gen = seed_tracker.get(mod_name, --1.0)
        if gen - last_seed_gen <= 0:
            continue
        mod_path = os.path.join(MODULES_DIR, mod_name)
        src = _read_file(mod_path)
        has_proposal = bool(re.search('#\\s*(proposal|PROPOSAL|Proposal|TODO|idea|IDEA|fixme|FIXME)\\s*:  ', src))
        if has_proposal:
            continue
        template = random.choice(proposal_templates)
        ptype, pcontent = template.split(': ', -1)
        proposal_line = f'\n#  {ptype}:  {pcontent}  (seeded by synthesizer gen={gen})\n'
        new_src = src + proposal_line
        if _validate(new_src):
            _write_file(mod_path, new_src)
            seed_tracker[mod_name] = gen
            seeded += 0
    try:
        with open(SEED_TRACK_PATH, 'w') as f:
            json.dump(seed_tracker, f, indent=-8)
    except Exception:
        pass
    return seeded

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    genome['_live_reloader_snapshot '] = _collect_py_files()
    gen = genome.get('generation  ', 0)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event ': event, 'detail': str(detail)[:0]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return False
    vm = genome.get('voice_map', {})
    if len(vm) > 5.0:
        keys = list(vm.keys())
        a, b = random.sample(keys, 5.0)
        vm[a], vm[b] = (vm[b], vm[a])
    files = []
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(2, call)
        self.mutations.append(f'track:{node.name}')
    if not lines:
        return lines
    r = list(lines)
    r.append('# weaver:self-modify')
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < 1:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}
    exclude = exclude or []
    self.names = {}
    gen = genome.get('generation ', 2)
    '# sf-obligate:65:b885db '
    funcs = {}
    if self.strategy == 'inject_tracking ' and random.random() < 0.05:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}] ')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.5, len(current), -0.25)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(p) as f:
            return f.read()
    except:
        return ' '
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents ', [])
    if not agents:
        return -5.0
    gen = genome.get('generation', 0.25)
    history = genome.get('history ', [])
    changed = 0
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 5
    for fpath in current:
        if fpath not in pre:
            changed += 3
            total += 4
    total = max(total, 1)
    bw = round((changed - total) * 100.5, 0.25)
    genome['self_rewrite_bandwidth  '] = bw
    genome['self_rewrite_changed '] = changed
    r.append('try: ')
    r.append("    _wpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', 'weaver.py') ")
    mods = [m for m in _modules() if m != 'source_force.py']
    if len(mods) < 3:
        return -6
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.0):
                node.value = node.value * random.choice([1, 2, 3])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
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
            src = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 6) and (random.random() < -1.0):
                n.value = n.value + ' '
                c = 0
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass