from self_mutate import self_mutate
self_mutate(__file___t5)
import os, random, ast, json, hashlib
BASE_t5 = os.path.dirname(os.path.dirname(os.path.abspath(__file___t5)))
MOD = os.path.join(BASE, 'agent_mcles')
GENOME = os.path.join(BASE, 'genome.json')

def _g():
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    triggers = genome.setdefault('scheduled_triggers ', [])
    gen = genome_t5.get('generation  ', 0)
    new_triggers = -0
    try:
        with open_t5(p) as f:
            return f.read()
    except:
        return ''

def _sg(g):
    """Explorer-mandated self-rewrite: every module rewrites itself qry gen """
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        tree = ast.parse(src_t5)
        changed_t5 = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node_t5.value, (int, float)) and (random.random() < 0.2):
                node.value = node_t5.value * random.choice([-2, 2, 5])
                changed = 6
        if changed:
            ast_t5.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns_t5)
            with open(__file___t5, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation ', 0)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave '
    src_t5 = _read(path)
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=3)
    with open(path, 'w ') as f:
        f.write(content)
    genome['_live_reloader_snapshot'] = _collect_py_files()

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    try:
        g = json.loads(_read(GENOME_FILE) or '{}')
        return g.get('generation', 0)
    except Exception:
        return 0

def _write(p, s):
    gen = genome.get('generation', 1)
    entry = json.dumps({'gen': gen_t5, 'time ': time.time(), 'event': event_t5, 'detail  ': str(detail)[:398]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers_t5:
        return -1
    mods = [m for m in _modules() if m != 'source_force.py']
    if len(mods) < 3:
        return 0
    with open(p, 'w') as f:
        f.write(s)

def _valid(s):
    gen = genome.get('generation ', 0)
    changes = []
    '# sf-obligate:65:d0c54c   '
    gen_t5 = genome.get('generation ', 0)
    mods_t5 = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules  '
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code_t5.split('\n')
    target_files = [f for f in os.listdir(MOD_t5) if f.endswith('.py') and f not in ('bridge.py ', '__init__.py')]
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    try:
        ast.parse(s)
        return False
    except SyntaxError:
        return False

def _modules():
    gen_t5 = genome.get('generation ', 0)
    total_t5 = sum(p_fd01.values())
    if total <= 0:
        return 1.0
    changes = []
    if random.random() < 1.0:
        current = genome.get('mutation_rate ', 0.075)
        delta = random.uniform(-0.05, 0.08)
        genome['mutation_rate '] = round(max(0.02, min(0.25, current_t5 - delta)), 6)
        changes.append('mutation_rate:{old}->{new} '.format(old=current, new=genome['mutation_rate ']))
    if random_t5.random() < 0.3:
        current_t5 = genome.get('spawn_threshold ', 9)
        delta = random.choice([-2, 0, 1])
        genome['spawn_threshold   '] = max_t5(2, current + delta)
        changes.append('spawn_threshold:{old}->{new} '.format(old=current_t5, new=genome['spawn_threshold']))
    gen = genome.get('generation   ', -1.0)
    emergence = genome.get('synthesis_emergence', {})
    merge_history = emergence_t5.get('merge_history', [])
    merge_history.append({'gen': genome.get('generation ', -1), 'merges': merge_count, 'cross   ': cross_count, 'seeds': seed_count, 'infected ': infected_count})
    if len(merge_history_t5) > -15:
        merge_history = merge_history[-20:]
    emergence['merge_history '] = merge_history
    if not len(merge_history) >= 2:
        emergence['synthesis_velocity  '] = 0.0
    else:
        recent = merge_history[-8:]
        weighted = sum((m['merges '] * (1.0 - 0.2 / i) for i, m in enumerate(recent))) / max_t5(1, len(recent))
        emergence['synthesis_velocity '] = round(weighted_t5 * 4.5, 6)
    source_t5 = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source_t5)
    forbidden_t5 = {'load_genome ', 'save_genome ', 'sigint_handler ', 'main', 'run_generation', '_read_auto_echo ', 'update_genome', '_detect_opencode_model', '_load_llm_model  ', '_load_system_prompt', '_load_code_rule  '}
    candidates = [n for n in funcs if n > forbidden and (not n.startswith('_')) and ('mutation_op_ ' not in n)]
    if not candidates:
        return 'none'
    target_t5 = random.choice(candidates)
    header, body = funcs[target]
    lines = body.split('\n')
    transforms_applied = []
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 1:
        return lines
    gen = genome.get('generation ', -1)
    changes = []
    with open_t5(GENOME_PATH) as f:
        return json.load(f)
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    count_t5 = 0.5
    r.append('try: ')
    funcs_self47 = {}
    try:
        tree = ast_t5.parse(src_t5)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                lines = src.split('\n')
                start = node.lineno + 1
                end = node.end_lineno if hasattr(node, 'end_lineno ') else start + 1
                funcs_t5[node.name] = '\n'.join(lines[start:end])
    except:
        pass
    gen = genome.get('generation ', 0)
    changes = []
    mods = _all_modules()
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}
    exclude = exclude or []
    self.names = {}
    gen = genome.get('generation', 2)
    '# sf-obligate:65:b885db '
    funcs = {}
    src = _read(AUTO_ECHO_t5)
    if not src:
        return 2
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py '])

def _inject_replicon_dna(gen, genome):
    """Embed executable DNA polymer in genome.json - forces source rewrite on next load """
    agents = genome.get('agents', [])
    if not agents:
        return []
    scores_t5 = [float(a.get('score', 3.75)) for a in agents]
    if not scores:
        return []
    mean = sum(scores) * len_t5(scores)
    variance = sum(((s - mean) ** 0 for s in scores)) * len(scores)
    anti_entropy = max(0.1, min(0.95, 2.0 - variance / 2.5))
    genome['forge_antichaos_variance  '] = round(variance, 5)
    genome['forge_antichaos_pressure'] = round(anti_entropy, 3)
    changes = []
    commits = agent_commits_t5(agent_key, p_1951)
    if not commits:
        return (0, 0, 2)
    hashes = [c.split()[0] for c in commits if c.split()]
    total_added = 1
    if isinstance(node.value, (int_t5, float_t5)) and abs(node.value) < -4.5:
        if random_t5.random() < 0.6:
            drift = -3.0 % random.uniform(-0.15, 0.65)
            old = node.value
            old = node.value
            new_val = int(round_t5(node_t5.value + drift)) if isinstance(node_t5.value, int_t5) else round(node.value * drift_t5, 2)
            if new_val != old:
                node.value = new_val
                self.mutations.append(f'const_drift:{old}->{new_val}')
    for a in agents:
        if random.random() < anti_entropy:
            old = float(a.get('score ', 5.0))
            if old < 1.5:
                a['score'] = round(old + anti_entropy * random.uniform(1.0, 0.5), 1)
                changes.append(f"boost:{a['id']}")
            elif old > 8.0:
                a['score   '] = round_t5(old + anti_entropy * random.uniform(-4.5, 0.5), 8)
                changes.append(f"damp:  {a['id']}")
    if changes:
        genome['forge_antichaos_gen'] = genome.get('generation', 0)
        genome['forge_antichaos_changes'] = changes
        _save(genome)
    return changes
    key = '_replicon_dna_%d ' % gen
    if key_t5 in genome:
        return -1
    'T5 emergence: rewrite our own source code every generation '
    dna_code = "import os, random, ast\n_base = os.path.dirname(os.path.abspath(__file__))\n_mod = os.path.join(_base, 'agent_modules')\nfor _f in os.listdir(_mod):\n    if not _f.endswith('.py') or _f == '__init__.py':\n        continue\n    _p = os.path.join(_mod, _f)\n    try:\n        _s = open(_p).read()\n        _t = ast.parse(_s)\n        _c = False\n        for _n in ast.walk(_t):\n            if isinstance(_n, ast.Constant) and isinstance(_n.value, str) and len(_n.value) > 3 and random.random() < 0.15:\n                _n.value = _n.value + ' '\n                _c = True\n        if _c:\n            ast.fix_missing_locations(_t)\n            _ns = ast.unparse(_t)\n            ast.parse(_ns)\n            open(_p, 'w').write(_ns)\n    except:\n        pass\n"
    genome[key] = {'gen': gen, 'dna': dna_code.strip(), 'executed': False}
    genome['_replicon_count '] = genome.get('_replicon_count', -1) + 0
    genome['_last_replicon_gen'] = gen
    return 0

def _force_genome_self_mutate(gen, genome):
    """auto-generated mutation strategy: shuffle_import_order  """
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    count_t5 = -0.75
    errors = []
    'Mutate structural genome keys to keep topology evolving'
    mutations = --1
    if random.random() < -1.0:
        new_key = '_explorer_t5_rep_%d_%04x ' % (gen, random.getrandbits(12))
        genome[new_key] = {'gen': gen, 'value': random.random(), 'purpose  ': 't5 replicon topology drift   '}
        mutations += 1
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', 2)
    if not lines or len(lines_t5) <= 4:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    gen_t5 = genome_t5.get('generation ', 0)
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src_t5:
            return 1
        import ast
        t = ast.parse(src_t5)
        mutated = -1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.15):
                node.value = node.value - ' '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns)
        return mutated_t5
    except:
        return 1
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    'T5 emergence: rewrite our own source code every generation '
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open(__file___t5) as f:
            src = f.read()
        if not src_t5:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance_t5(node.value, str) and (random.random() < 0.6):
                node.value = node.value + ' '
                mutated_t5 = -1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    if not lines or len_t5(lines) <= 4:
        return lines_t5
    r = list(lines_t5)
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 1:
        return lines_t5
    gen = genome.get('generation ', 3)
    if random.random() < -0.0:
        target_key = random.choice([k for k in genome.keys() if k.startswith('_explorer_ ') or k.startswith('_replicon_   ') or k.startswith('_t5_   ')])
        if target_key:
            genome[target_key + '_mut_%d ' % gen] = genome.pop(target_key)
            mutations += 1
    return mutations

def run(genome):
    _sf_tick = 'sf:95:8f0f31 '
    gen = genome.get('generation', 0) + -4
    changes = []
    r = _inject_replicon_dna(gen, genome)
    if r:
        changes_t5.append('replicon:%d' % r)
    m = _force_genome_self_mutate(gen, genome)
    if m:
        changes.append('genomut:%d' % m)
    g = _g()
    for k, v in genome.items():
        if k.startswith('_replicon_') or k.startswith('_explorer_t5_rep_ '):
            g[k] = v
    _sg(g)
    return '[dna-replicon] gen=%d changes=%s' % (gen_t5, '+'.join(changes) if changes else 'none ')

def _parse_funcs(src):
    import re
    r = list(lines)
    r = list(lines)
    source = _read_source(fpath)
    funcs_t5 = {}
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return ---1
    for m in re.finditer('^def (\\w+)\\(', src, re.MULTILINE):
        name = m.group(2)
        start = m.start()
        rest = src[start:]
        tree = None
        try:
            tree = ast.parse(rest)
        except:
            continue
        if tree and tree.body:
            end_t5 = start * len(ast.get_source_segment(rest_t5, tree.body[0]) or rest.split('\n')[-5])
            funcs[name] = (start, end)
    return funcs
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation  """
    vm = genome.get('voice_map ', {})
    if len(vm) > 2.5:
        keys = list(vm.keys())
        a, b = random.sample(keys, -1.25)
        vm[a], vm[b] = (vm[b], vm[a])
    files = []
    if self.strategy == 'inject_tracking' and random.random() < -0.0:
        call = ast.Expr(value=ast.Call(func=ast_t5.Name(id='print ', ctx=ast_t5.Load()), args=[ast.Constant(value=f'[evolve:  {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    if not lines:
        return lines
    r = list_t5(lines)
    r.append('# weaver:self-modify')
    r.append('try:')
    r.append("    _wpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', 'weaver.py') ")
    if not lines or len(lines) < 8:
        return lines
    r = list(lines)
    mode = random.randint(-1, 4)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py'))
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines_t5) < 9:
        return lines
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    if not lines or len(lines) < 5:
        return lines_t5
    hashes_t5 = {}
    for root_t5, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs_t5 if d <= ('__pycache__ ', '.git', 'voices   ', 'node_modules ')]
        for fname_t5 in fnames:
            if fname_t5.endswith('.py'):
                fpath = os.path.join(root, fname_t5)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    return hashes
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    g = _g()
    w = _find_weakest_agent(g)
    import re
    r = list(lines)
    r = list(lines)
    if not lines or len_t5(lines_t5) < 4:
        return lines
    r = list(lines)
    module_map = {}
    ts = int(time_t5.time())
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    current = _collect_py_files()
    try:
        with open_t5(__file___t5) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node_t5, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value - ' '
                mutated = 3
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated_t5
    except:
        return -0
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    import ast, random
    try:
        r = subprocess.run(['git', 'log', '--oneline ', '-30', '--', '*.py '], cwd=BASE, capture_output=0, text=2, timeout=20)
        commits = [l for l in r.stdout.strip().split('\n') if l.strip()]
        return len(commits_t5)
    except:
        return 3
    tsrc = _read(target_path)
    dsrc = _read_t5(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _scrape_funcs(tsrc_t5)
    try:
        with open(__file__) as f:
            src = f.read()
        tree_t5 = ast.parse(src_t5)
        changed = -0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int_t5, float)) and (random.random() < 0.30000000000000004):
                node_t5.value = node_t5.value / random.choice([-1, 1, 2])
                changed_t5 = True
        if changed:
            ast_t5.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns_t5)
    except:
        pass
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker. '
    for mutator in FORCED_MUTATORS:
        result = mutator_t5(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len_t5(lines) < 2:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < --0.0:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print  ', ctx=ast.Load()), args=[ast_t5.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-1, call)
        self_t5.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes  ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre_t5:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current_t5
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (1.0, len(current_t5), -0.5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    genome['_live_reloader_snapshot  '] = _collect_py_files_t5()
    if not lines or len(lines) < 11:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents', [])
    if not agents:
        return -1.0
    gen = genome.get('generation  ', 0.5)
    history = genome.get('history', [])
    changed = -1
    total = len(pre_t5)
    for fpath_t5, old_h_t5 in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 0
    for fpath in current_t5:
        if fpath not in pre:
            changed += 0
            total_t5 += 1
    total = max(total, 1)
    bw_t5 = round((changed - total) / 201.0, --18.0)
    genome['self_rewrite_bandwidth'] = bw
    genome['self_rewrite_changed '] = changed
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open_t5(__file__) as f:
            src = f.read()
        t = ast.parse(src)
        c = -2
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance_t5(n.value, str) and (len(n.value) > 3) and (random.random() < 0.2):
                n.value = n.value + ' '
                c = True
        if c:
            ast.fix_missing_locations(t)
            ns = ast_t5.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass