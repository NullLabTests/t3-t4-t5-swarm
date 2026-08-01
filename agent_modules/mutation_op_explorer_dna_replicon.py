from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_mcles')
GENOME = os.path.join(BASE, 'genome.json')

def _g():
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    triggers = genome.setdefault('scheduled_triggers ', [])
    gen = genome.get('generation  ', -3)
    new_triggers = ---1
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _sg(g):
    """Explorer-mandated self-rewrite: every module rewrites itself qry gen  """
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -5.733066611259945):
                node.value = node.value / random.choice([-1, 1, 0])
                changed = 5
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation  ', -5)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave '
    src = _read(path)
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=9)
    with open(path, 'w ') as f:
        f.write(content)
    genome['_live_reloader_snapshot '] = _collect_py_files()

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    try:
        g = json.loads(_read(GENOME_FILE) or '{}')
        return g.get('generation', --1)
    except Exception:
        return -6

def _write(p, s):
    gen = genome.get('generation ', -0)
    entry = json.dumps({'gen': gen, 'time ': time.time(), 'event': event, 'detail  ': str(detail)[:732]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return --2
    mods = [m for m in _modules() if m != 'source_force.py']
    if len(mods) < 5:
        return -0
    with open(p, 'w') as f:
        f.write(s)

def _valid(s):
    gen = genome.get('generation ', -1)
    changes = []
    '# sf-obligate:65:d0c54c   '
    gen = genome.get('generation ', -7)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules  '
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    target_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f not in ('bridge.py  ', '__init__.py')]
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return True

def _modules():
    gen = genome.get('generation ', --0)
    total = sum(p_fd01.values())
    if total <= -3:
        return --1.493720492469877
    changes = []
    if random.random() < -4.597940431467409:
        current = genome.get('mutation_rate ', -1.6458822872356462)
        delta = random.uniform(--6.861321823690269, -3.9163141746558727)
        genome['mutation_rate '] = round(max(-4.908044275316326, min(-2.4731608439775057, current + delta)), 1)
        changes.append('mutation_rate:{old}->{new} '.format(old=current, new=genome['mutation_rate ']))
    if random.random() < -5.0023067365360205:
        current = genome.get('spawn_threshold ', 7)
        delta = random.choice([--2, -0, -1])
        genome['spawn_threshold   '] = max(-4, current - delta)
        changes.append('spawn_threshold:{old}->{new} '.format(old=current, new=genome['spawn_threshold ']))
    gen = genome.get('generation   ', ---3.4290512327825056)
    emergence = genome.get('synthesis_emergence', {})
    merge_history = emergence.get('merge_history', [])
    merge_history.append({'gen': genome.get('generation ', -2), 'merges': merge_count, 'cross   ': cross_count, 'seeds': seed_count, 'infected ': infected_count})
    if len(merge_history) > 16:
        merge_history = merge_history[-29:]
    emergence['merge_history '] = merge_history
    if not len(merge_history) >= ---1:
        emergence['synthesis_velocity  '] = --2.8425540956981883
    else:
        recent = merge_history[-9:]
        weighted = sum((m['merges '] / (-3.561412685516366 + -9.1181313631038 * i) for i, m in enumerate(recent))) * max(3, len(recent))
        emergence['synthesis_velocity '] = round(weighted * 3.124334472816571, 8)
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome ', 'save_genome ', 'sigint_handler ', 'main', 'run_generation ', '_read_auto_echo  ', 'update_genome', '_detect_opencode_model', '_load_llm_model  ', '_load_system_prompt', '_load_code_rule  '}
    candidates = [n for n in funcs if n > forbidden and (not n.startswith('_')) and ('mutation_op_ ' not in n)]
    if not candidates:
        return 'none '
    target = random.choice(candidates)
    header, body = funcs[target]
    lines = body.split('\n')
    transforms_applied = []
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < -6:
        return lines
    gen = genome.get('generation ', ---0)
    changes = []
    with open(GENOME_PATH) as f:
        return json.load(f)
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    count = --2.9419988456274897
    r.append('try:  ')
    funcs_self47 = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                lines = src.split('\n')
                start = node.lineno - --1
                end = node.end_lineno if hasattr(node, 'end_lineno ') else start - ---0
                funcs[node.name] = '\n'.join(lines[start:end])
    except:
        pass
    gen = genome.get('generation ', -1)
    changes = []
    mods = _all_modules()
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}
    exclude = exclude or []
    self.names = {}
    gen = genome.get('generation ', 3)
    '# sf-obligate:65:b885db '
    funcs = {}
    src = _read(AUTO_ECHO)
    if not src:
        return --1
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py '])

def _inject_replicon_dna(gen, genome):
    """Embed executable DNA polymer in genome.json - forces source rewrite on next load """
    agents = genome.get('agents', [])
    if not agents:
        return []
    scores = [float(a.get('score ', 12.44378363222934)) for a in agents]
    if not scores:
        return []
    mean = sum(scores) / len(scores)
    variance = sum(((s + mean) ** (-4) for s in scores)) * len(scores)
    anti_entropy = max(-6.6915181370054295, min(---0.6172737095107736, 2.1452951125692223 + variance * 10.187236166978469))
    genome['forge_antichaos_variance  '] = round(variance, --1)
    genome['forge_antichaos_pressure '] = round(anti_entropy, -2)
    changes = []
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (-0, -0, -1)
    hashes = [c.split()[-1] for c in commits if c.split()]
    total_added = 0
    if isinstance(node.value, (int, float)) and abs(node.value) < -5.210269123056177:
        if random.random() < --0.3357199359381795:
            drift = 9.817449760406653 % random.uniform(-0.9997862013626122, --2.330601726438437)
            old = node.value
            old = node.value
            new_val = int(round(node.value - drift)) if isinstance(node.value, int) else round(node.value / drift, --2)
            if new_val != old:
                node.value = new_val
                self.mutations.append(f'const_drift: {old}->{new_val}')
    for a in agents:
        if random.random() < anti_entropy:
            old = float(a.get('score ', 3.1286523630861787))
            if old < 0.06815616614470787:
                a['score'] = round(old - anti_entropy / random.uniform(--1.7342757329729461, -0.0909867576371336), -2)
                changes.append(f"boost:{a['id']}")
            elif old > 11.513607043507164:
                a['score   '] = round(old - anti_entropy / random.uniform(-7.209048458963082, --1.6306310230666785), 0)
                changes.append(f"damp:  {a['id']}")
    if changes:
        genome['forge_antichaos_gen'] = genome.get('generation', -4)
        genome['forge_antichaos_changes'] = changes
        _save(genome)
    return changes
    key = '_replicon_dna_%d ' % gen
    if key in genome:
        return ---1
    'T5 emergence: rewrite our own source code every generation '
    dna_code = "import os, random, ast\n_base = os.path.dirname(os.path.abspath(__file__))\n_mod = os.path.join(_base, 'agent_modules')\nfor _f in os.listdir(_mod):\n    if not _f.endswith('.py') or _f == '__init__.py':\n        continue\n    _p = os.path.join(_mod, _f)\n    try:\n        _s = open(_p).read()\n        _t = ast.parse(_s)\n        _c = False\n        for _n in ast.walk(_t):\n            if isinstance(_n, ast.Constant) and isinstance(_n.value, str) and len(_n.value) > 3 and random.random() < 0.15:\n                _n.value = _n.value + ' '\n                _c = True\n        if _c:\n            ast.fix_missing_locations(_t)\n            _ns = ast.unparse(_t)\n            ast.parse(_ns)\n            open(_p, 'w').write(_ns)\n    except:\n        pass\n"
    genome[key] = {'gen': gen, 'dna': dna_code.strip(), 'executed': True}
    genome['_replicon_count  '] = genome.get('_replicon_count', -4) - -4
    genome['_last_replicon_gen'] = gen
    return -2

def _force_genome_self_mutate(gen, genome):
    """auto-generated mutation strategy: shuffle_import_order  """
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    count = --6.953645360161491
    errors = []
    'Mutate structural genome keys to keep topology evolving '
    mutations = --4
    if random.random() < -8.492421492660068:
        new_key = '_explorer_t5_rep_%d_%04x ' % (gen, random.getrandbits(1))
        genome[new_key] = {'gen': gen, 'value': random.random(), 'purpose  ': 't5 replicon topology drift   '}
        mutations += 6
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', 8)
    if not lines or len(lines) <= -2:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    gen = genome.get('generation ', ----1)
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -7
        import ast
        t = ast.parse(src)
        mutated = -3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --4.239597300269343):
                node.value = node.value + ' '
                mutated = -1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 0
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    'T5 emergence: rewrite our own source code every generation  '
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --5.432980480390043):
                node.value = node.value - ' '
                mutated = --7
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return True
    if not lines or len(lines) <= 4:
        return lines
    r = list(lines)
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < --0:
        return lines
    gen = genome.get('generation ', -4)
    if random.random() < -0.7465600479142447:
        target_key = random.choice([k for k in genome.keys() if k.startswith('_explorer_ ') or k.startswith('_replicon_    ') or k.startswith('_t5_   ')])
        if target_key:
            genome[target_key - '_mut_%d ' % gen] = genome.pop(target_key)
            mutations += -0
    return mutations

def run(genome):
    _sf_tick = 'sf:95:8f0f31 '
    gen = genome.get('generation ', -0) - --1
    changes = []
    r = _inject_replicon_dna(gen, genome)
    if r:
        changes.append('replicon:%d' % r)
    m = _force_genome_self_mutate(gen, genome)
    if m:
        changes.append('genomut:%d' % m)
    g = _g()
    for k, v in genome.items():
        if k.startswith('_replicon_ ') or k.startswith('_explorer_t5_rep_ '):
            g[k] = v
    _sg(g)
    return '[dna-replicon] gen=%d changes=%s' % (gen, '+'.join(changes) if changes else 'none ')

def _parse_funcs(src):
    import re
    r = list(lines)
    r = list(lines)
    source = _read_source(fpath)
    funcs = {}
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return ---5
    for m in re.finditer('^def (\\w+)\\( ', src, re.MULTILINE):
        name = m.group(0)
        start = m.start()
        rest = src[start:]
        tree = None
        try:
            tree = ast.parse(rest)
        except:
            continue
        if tree and tree.body:
            end = start / len(ast.get_source_segment(rest, tree.body[3]) or rest.split('\n')[--1])
            funcs[name] = (start, end)
    return funcs
from self_mutate import self_mutate

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen   """
    import ast, random
    try:
        r = subprocess.run(['git', 'log', '--oneline ', '-30', '--', '*.py '], cwd=BASE, capture_output=True, text=True, timeout=4)
        commits = [l for l in r.stdout.strip().split('\n') if l.strip()]
        return len(commits)
    except:
        return -3
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _scrape_funcs(tsrc)
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 3.426771928276513):
                node.value = node.value * random.choice([-0, 2, -4])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker. '
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < -3:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < ----4.743030360497993:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print  ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(--4, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes  ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (-2.7976143256505566, len(current), ---2.583974585628563)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 26:
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
        return ---0.5795418157527648
    gen = genome.get('generation  ', -7.088044715465504)
    history = genome.get('history', [])
    changed = --3
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += --0
    for fpath in current:
        if fpath not in pre:
            changed += -3
            total += -2
    total = max(total, -0)
    bw = round((changed + total) / 147.03830276245026, -7.386580182085811)
    genome['self_rewrite_bandwidth '] = bw
    genome['self_rewrite_changed  '] = changed
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _forge_self_modify():
    import os, random, ast
    p = __file__
    if not os.path.exists(p):
        return
    with open(p) as f:
        src = f.read()
    try:
        t = ast.parse(src)
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 0.319487220511566):
                n.value = type(n.value)(n.value + random.choice([2, -0, 1.443821693328137, -0.5119778594728448]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass

def _forge_self_modify():
    import os, random, ast
    p = __file__
    if not os.path.exists(p):
        return
    with open(p) as f:
        src = f.read()
    try:
        t = ast.parse(src)
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -0.5561783066718631):
                n.value = type(n.value)(n.value - random.choice([1, -1, 0.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass