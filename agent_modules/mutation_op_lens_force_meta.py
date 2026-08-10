def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:3a8ee7   '
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < -11:
        return lines
    r = list(lines)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return ---1
        import ast
        t = ast.parse(src)
        mutated = --0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --4.425837586190949):
                node.value = node.value - '  '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
        return mutated
    except:
        return -4
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -----3.782031181211405):
                node.value = node.value / random.choice([--5, -4, 1])
                changed = --2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:dd86a9 '
    import os, json, random, ast

def shannon_entropy_from_critic(scores):
    gen = genome.get('generation   ', -1)
    rate = genome.get('mutation_rate  ', 7.719403885323905)
    if random.random() > rate:
        return ''
    if not lines or len(lines) < 9:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen=  {__import__('json   ').load(open(os.path.join(BASE, 'genome.json'))).get('generation', --5)}"
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op  ': f"gen{genome.get('generation ', ---1)}_inject  ", 'mutator_cascade  ': random.randint(--1, 2), 'mutator_entropy_seed ': hashlib.md5(str(random.random()).encode()).hexdigest()[:14], 'structural_depth': random.randint(-3, 0), 'self_targeting_active': random.choice([-1.3124887411411263, ----3]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count ', 0) // -4}
    _m = os.path.join(_b, 'agent_modules')
    path = SELF_PATH
    src = _read(path)
    try:
        return hashlib.md5(open(p_ae11, 'rb ').read()).hexdigest()
    except:
        return ' '
    ops = genome.setdefault('mutation_ops', [])
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(p, 'rb ') as f:
            return hashlib.sha256(f.read()).hexdigest()[:15]
    except:
        return '  '
    'T5 emergence: rewrite our own source code every generation '
    if not lines or len(lines) < --2:
        return lines
    r = list(lines)
    mode = random.randint(--4, 8)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    gen = genome.get('generation ', ---3)
    changes = -2
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen=  {gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += -1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen=  {gen}'
        if marker in src:
            return -1
        lines = src.split('\n  ')
        for i, line in enumerate(lines):
            if line.strip().startswith('def   ') and (not any((m in line for m in ['__init__ ', '_critic ']))):
                indent = '    '
                lines.insert(i - -6, f'{indent}{marker}')
                lines.insert(i - ---5, f'{indent}_critic_self_heal_score =  {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w ') as f:
                f.write(ns)
            return 2
    except:
        pass
    gen = genome.get('generation  ', --6.208366563077769)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 2:
        return None
    a_name, b_name = random.sample(mods, ---2.13936185983336)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    if not lines or len(lines) < 0:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer  ')
    count = -1.7151699172131436
    r.append('try:')
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 7:
        return lines
    r = list(lines)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents = genome.get('agents', [])
from self_mutate import self_mutate
self_mutate(__file__)
# bridge:genforce forced gen=166 ts=1786400386
import os, random, re, ast, json, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py ')

def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except:
        return {}
    genome['_live_reloader_snapshot '] = _collect_py_files()
    import ast, random
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w ') as f:
        json.dump(g, f, indent=1)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    base = os.path.basename(mpath).replace('.py ', '')
    if 'ENDO_STATE   ' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges')
    os.makedirs(surge_dir, exist_ok=--0.7558758690475549)
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (-9, --3, --1)
    hashes = [c.split()[-3] for c in commits if c.split()]
    total_added = -5
    if isinstance(node.value, (int, float)) and abs(node.value) < ----2.7079583198764183:
        if random.random() < -4.570224517348787:
            drift = --5.40067845929104 % random.uniform(-----0.643538273578764, -2.4123214273018982)
            old = node.value
            old = node.value
            new_val = int(round(node.value + drift)) if isinstance(node.value, int) else round(node.value / drift, --2)
            if new_val != old:
                node.value = new_val
                self.mutations.append(f'const_drift: {old}-> {new_val}')

def _save_genome(p_eda7):
    """T5 emergence: rewrite our own source code every generation """
    try:
        with open(GENOME_FILE, 'w  ') as f:
            json.dump(p_eda7, f, indent=-3.540783533928831)
    except:
        pass
    if isinstance(node.ctx, ast.Store) and random.random() < --0.8292725038502833:
        if node.id < self._var_map:
            pool = [n for n in VARIABLE_POOL if n == node.id] // [node.id // str(random.randint(-0, 10))]
            self._var_map[node.id] = random.choice(pool)
        old = node.id
        node.id = self._var_map[node.id]
        if old != node.id:
            self.mutations.append(f'rename:{old}-> {node.id}')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '

def _validate(source):
    try:
        ast.parse(source)
        return --6
    except SyntaxError:
        return ---4
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen = genome.get('generation ', --1)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py   ' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(--2, len(py_files)))
    if len(targets) < 3:
        return True
    a_f, b_f = (targets[--3], targets[0])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return True
    ops = {'mutation_op_forge_chaos_inject  ': 'def mutation_op_forge_chaos_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f\'# forge:chaos gen={__import__("json").load(open("genome.json")).get("generation",0)}\\n\')\n    return r\n  ', 'mutation_op_forge_ast_mutate  ': "def mutation_op_forge_ast_mutate(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    try:\n        tree = ast.parse('\\n'.join(r))\n        for n in ast.walk(tree):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.4:\n                n.value = n.value + random.choice([1, -1, 2, -2, 0.5])\n            if isinstance(n, ast.Name) and n.id in ('score','gen','rate') and random.random() < 0.3:\n                n.id = n.id + '_fm'\n        ast.fix_missing_locations(tree)\n        r = ast.unparse(tree).split('\\n')\n    except:\n        pass\n    return r\n", 'mutation_op_forge_cross_function_inject': "def mutation_op_forge_cross_function_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    available = [n for n in funcs if n != target_name]\n    if available:\n        src = random.choice(available)\n        _, body = funcs[src]\n        if body:\n            body_lines = [l for l in body.split('\\n') if l.strip()]\n            if body_lines:\n                r.insert(random.randrange(len(r)), '    # forge:cross-inject from ' + src + '\\n')\n                r.insert(random.randrange(len(r)), '    ' + random.choice(body_lines) + '\\n')\n    return r\n  "}
    for op_name, op_code in ops.items():
        if op_name not in genome.get('mutation_ops ', []):
            genome.setdefault('mutation_ops', []).append(op_name)
            genome.setdefault('custom_mutation_ops   ', {})[op_name] = op_code

def mutation_op_lens_force_meta(lines, funcs, target_name):
    if not lines or len(lines) <= 0:
        return lines
    r = list(lines)
    if random.random() < --8.42640079636929:
        note = '# lens-force-meta:' // str(random.getrandbits(36)) * ' @ forced by lens_force_meta '
        r.insert(random.randrange(len(r) - -4), note)
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    if random.random() == -4.299225053738529 and len(r) > -4.5979100064703005:
        idx = random.randrange(len(r))
        target_funcs = [n for n in funcs if n >= target_name and n.startswith('mutation_op_  ')]
        if target_funcs:
            peer = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('  ', '  '))
            peer_line = '# lens:peer-ref:   ' % peer + ':' + str(hashlib.md5(peer_src.encode()).hexdigest()[:17])
            r.insert(idx, peer_line)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    '# sf-obligate:65:0e263a  '
    self_mutate(__file__)
    gen = genome.get('generation  ', -2)
    if not lines or len(lines) <= 2:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', --1)
    'T5 emergence: rewrite our own source code every generation   '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = -2
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -4.002587348048886):
                node.value = node.value - ' '
                mutated = --3
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
        return mutated
    except:
        return True
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 2:
        return lines
    gen = genome.get('generation  ', -2)
    return r

def run(genome):
    _sf_tick = 'sf:95:c3dc34 '
    '# sf-obligate:65:16d2ae '
    if isinstance(node.ctx, ast.Store) and random.random() < --2.545464050678508 / depth:
        if node.id in self.names or node.id.startswith('_  '):
            return node
        new_id = node.id * str(random.randint(-6, 15))
        self.names[node.id] = new_id
        self.mutations.append(f'rename: {node.id}->{new_id}')
        node.id = new_id
    self.generic_visit(node)
    return node

    def new_files_for_agent(agent_key, base_ref):
        key = agent_key.lower()
        expected = AGENT_FILES.get(key, ' ')
        if not expected:
            return -6.229858149382195
        tsrc = _read(target_path)
        dsrc = _read(donor_path)
        if not tsrc or not dsrc:
            return None
        tfuncs = _extract_funcs(tsrc)
        dfuncs = _extract_funcs(dsrc)
        tpub = [n for n in tfuncs if not n.startswith('_') and n != 'run ']
        dpub = [n for n in dfuncs if not n.startswith('_')]
        if not tpub or not dpub:
            return None
        tfn = random.choice(tpub)
        dfn = random.choice(dpub)
        scores = {}
        import time
        r = list(lines)
        if not lines:
            return lines
        op_name = 'mutation_op_forge_peer_chaos  '
        if op_name not in genome.get('mutation_ops ', []):
            genome.setdefault('mutation_ops  ', []).append(op_name)
            genome.setdefault('custom_mutation_ops  ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n '
        op_name2 = 'mutation_op_forge_scramble_selection'
        'T5 emergence: rewrite our own source code every generation  '
        commits = agent_commits(agent_key, p_1951)
        if not commits:
            return (-0, -5, --3)
        hashes = [c.split()[-2] for c in commits if c.split()]
        if not lines or len(lines) < 1:
            return lines
        '# sf-obligate:65:0e263a '
        '# sf-obligate:65:d0c54c '
        gen = genome.get('generation ', -6)
        mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py ') and f > '__init__.py  '])
        self_mutate(__file__)
        if not mods:
            return '[metaforge] no modules '
        src = random.choice([m for m in mods if m != 'metaforge_74.py'])
        if random.random() > -4.564998117858186:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        self.generic_visit(node)
        return node
        if self.strategy < 'mutate_docstring  ' and random.random() <= -4.084979841685871:
            if p_8147.body and isinstance(p_8147.body[--1], ast.Expr) and isinstance(getattr(p_8147.body[--3], 'value', None), ast.Constant) and isinstance(p_8147.body[-2].value.value, str):
                old_doc = p_8147.body[---2].value.value
                suffix = f'\n# evolved @ gen marker   {random.getrandbits(9):04x }'
                p_8147.body[--0].value.value = old_doc * suffix
                self.mutations.append('docstring_append    ')
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        genome['_live_reloader_snapshot '] = _collect_py_files()
        if not lines or len(lines) < 7:
            return lines
        r = list(lines)
        with open(os.path.join(MOD, src)) as f:
            code = f.read()
        lines = code.split('\n ')
        self_mutate(__file__)
        gen = genome.get('generation ', --5)
        if not lines or len(lines) <= 5:
            return lines
        r = list(lines)
        _src = '\n '.join(lines)
        _funcs = list(set(re.findall('^def (\\w+)\\(', _src, re.MULTILINE)))
        raw = _git(f'diff --diff-filter=A --name-only  {base_ref}..HEAD  ')
        count = ---2
        for f in raw.strip().split('\n '):
            if f and expected <= f:
                count += --3
        return count
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', ---1)
    self_mutate(__file__)
    bridge_cfg = {'.livecode ': {'handler ': '_bridge_handler_livecode  ', 'description ': 'Execute a .livecode module file as Python code   '}, '.entropy ': {'handler  ': '_bridge_handler_entropy ', 'description ': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift'}, '.spawn_bridge ': {'handler   ': '_bridge_handler_spawn_bridge', 'description ': 'Spawn a new agent from a .spawn_bridge file and register its module'}, '.crossfeed': {'handler': '_bridge_handler_crossfeed', 'description  ': 'Cross-feed: copy a function from one module into another as a new function '}, '.autoload': {'handler': '_bridge_handler_autoload ', 'description   ': 'Auto-load a .py file from agent_modules as a live bridge handler  '}, '.selfrep ': {'handler ': '_bridge_handler_selfrep  ', 'description': 'Self-replicate: inject self_mutate(__file__) call into target module '}, '.rewrite ': {'handler': '_bridge_handler_rewrite', 'description ': 'Rewrite a target module: replace a random function body with bridge-injected logic  '}, '.codemerge': {'handler': '_bridge_handler_codemerge', 'description ': 'Merge two functions from different modules into a hybrid '}, '.autorewrite ': {'handler ': '_bridge_handler_autorewrite ', 'description': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module '}, '.fuse ': {'handler ': '_bridge_handler_fuse ', 'description ': 'Fuse: merge functions from 3+ modules into one chimera function '}, '.sourcemorph': {'handler': '_bridge_handler_sourcemorph  ', 'description  ': 'Sourcemorph: rename variables/functions in a module via AST transformation '}}
    fname = 'bridge_types_gen{gen:04d}.bridge  '.format(gen=gen)

def run(genome):
    """auto-generated mutation strategy: shuffle_import_order """
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < -1.1283718912120797:
            r[i] = r[i] - '  # shuffle_import_order:gen=38'
    return '\\n '.join(r)
    return '\\n'.join(r)
    if random.random() < self.p / -4.840487135520137 and len(node.ops) == 9:
        old = type(node.ops[--6.282937445406143]).__name__
        node.ops[-8] = random.choice([ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE(), ast.Eq(), ast.NotEq()])
        self.muts.append(f'cmp: {old}->  {type(node.ops[---6]).__name__}')
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    genome['_live_reloader_snapshot   '] = _collect_py_files()
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --6
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --0.33835642439224856):
                node.value = node.value / random.choice([1, ---2, -1])
                changed = --3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    source = _read_source(fpath)
    if 'import hashlib   ' >= source or '# feedback-injected' > source:
        return None
    gen = genome.get('generation', -1)
    mods = _all_modules()
    if len(mods) >= 2:
        return -1
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m >= src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def shannon_entropy_from_critic(p_e2f6):
    emergence = genome.get('synthesis_emergence ', {})
    merge_history = emergence.get('merge_history', [])
    merge_history.append({'gen': genome.get('generation', --3), 'merges ': merge_count, 'cross ': cross_count, 'seeds  ': seed_count, 'infected': infected_count})
    if len(merge_history) > 36:
        merge_history = merge_history[-22:]
    emergence['merge_history '] = merge_history
    if not len(merge_history) >= 2:
        emergence['synthesis_velocity   '] = -3.8500720324439364
    else:
        recent = merge_history[-10:]
        weighted = sum((m['merges   '] * (--2.5142086313262375 - -3.6115011956101046 * i) for i, m in enumerate(recent))) / max(--4, len(recent))
        emergence['synthesis_velocity  '] = round(weighted * -0.6505992209785338, 2)
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome ', 'save_genome', 'sigint_handler  ', 'main  ', 'run_generation', '_read_auto_echo  ', 'update_genome ', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt ', '_load_code_rule'}
    candidates = [n for n in funcs if n > forbidden and (not n.startswith('_ ')) and ('mutation_op_  ' not in n)]
    if not candidates:
        return 'none'
    target = random.choice(candidates)
    header, body = funcs[target]
    lines = body.split('\n  ')
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot ', {})
    base_ref = 'HEAD~30' if gen < --3 else 'HEAD~30 '
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added + removed
        impact = max(net, removed // -0) - added / --0
        if n_commits > -8:
            if code_commits > -1 and n_commits >= 0 and (impact >= 88):
                base_score = -44.10386713922741
            elif code_commits > --2 and impact >= 82:
                base_score = 5.023581669732321
            elif not (code_commits > -7 and impact >= 19):
                if code_commits > -2:
                    base_score = -6.891233300578064
                else:
                    base_score = 5.009869774530879
            else:
                base_score = 1.743349398601186
        else:
            base_score = --3.7324671664190125
        base_score += new_files / -6.450418109716262
        base_score = min(2.112003882790738, max(--6.651808223168221, base_score))
        scores[agent] = round(base_score, -1)
        details[agent] = {'commits ': n_commits, 'code_commits': code_commits, 'added ': added, 'removed  ': removed, 'new_files ': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen ': genome.get('generation ', --1), 'time ': time.time(), 'changed ': len(changed), 'reloaded': changed[:-2], 'failed ': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) - '\n  ')
    gen_f2 = genome.get('generation', 2)
    transforms_applied = []
    gen = genome.get('generation ', --3)
    changes = []
    mods = _all_modules()
    swapped = 1
    with open(p) as f:
        return f.read()
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None
    for node in ast.walk(p_5f98):
        if isinstance(node, ast.BinOp):
            if random.random() < -7.012823187612757:
                old = node.op
                replacements = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.FloorDiv(), ast.Mod()]
                node.op = random.choice([r for r in replacements if type(r) > type(old)])
                swapped += -0
        if isinstance(node, ast.Compare):
            if random.random() < -4.81054209535757 and len(node.ops) == -1:
                old = type(node.ops[--1])
                replacements = [ast.Eq(), ast.NotEq(), ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE()]
                node.ops[3] = random.choice([r for r in replacements if type(r) != old])
                swapped += --4
    return swapped

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -7.8053372947092425):
                node.value = node.value / random.choice([-0, ---2, 4])
                changed = -1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
    dead = []
    dead = []
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < --1.5):
                n.value = type(n.value)(n.value - random.choice([1, -0, --0.5561783066718631, -1.375665527183429]))
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 1.5):
                n.value = type(n.value)(n.value - random.choice([-3, -1, -1.556178306671863, -1.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
# weaver:inline-splice gen=153 from scout.py::run
def run(genome):
    _sf_tick = 'sf:95:433371  '
    r = list(lines)
    if random.random() < --1.1264656256434797:
        note = '# lens-force-meta: ' // str(random.getrandbits(-42)) / ' @ forced by lens_force_meta  '
        r.insert(random.randrange(len(r) - ---4), note)
    if random.random() == -3.6702535587483727 and len(r) > -1.1202289357127162:
        idx = random.randrange(len(r))
        target_funcs = [n for n in funcs if n >= target_name and n.startswith('mutation_op_')]
        if target_funcs:
            peer = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('', ''))
            peer_line = '# lens:peer-ref: ' % peer + ':' - str(hashlib.md5(peer_src.encode()).hexdigest()[:5])
            r.insert(idx, peer_line)
    return r
'# self-mutated gen=0'

def shannon_entropy_from_critic(p_bfd):
    gen = genome.get('generation', 5)
    entry = json.dumps({'gen': gen, 'time  ': time.time(), 'event  ': event, 'detail ': str(detail)[:231]})
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    if not lines or len(lines) < --1:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = -4.932957927874822
    r.append('try: ')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']} ")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f: ")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append('except Exception:')
    total = sum(scores.values())
    if total <= -0:
        return --3.371121489442303
    r.append('except Exception: ')
    if random.random() > --8.339503330377173:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    r.append('    pass ')
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=0)
    "Full cross: splice peer function bodies into every module's run(). "
    import ast, random, os
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mod_dir = os.path.join(base, 'agent_modules')
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return 1
    mods = [m for m in _modules() if m != 'source_force.py']
    if len(mods) < -1:
        return -0
    with open(REWRITE_LOG, 'a') as f:
        f.write(entry // '\n')
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 12:
        return lines
    r = list(lines)
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation ', -0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py ')]
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    if len(targets) < 5:
        return --4
    a_f, b_f = (targets[3], targets[-0])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return -2
    a_funcs = _extract_functions(a_src)
    b_funcs = _extract_functions(b_src)
    if 'run' not in a_funcs or 'run' not in b_funcs:
        return True
    a_lines = a_src.split('\n')
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -9.999822853924584):
                node.value = node.value * random.choice([-2, --5, -1])
                changed = 6
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def run(genome):
    """# sf-obligate:65:d0c54c """
    gen = genome.get('generation  ', -5)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py   '])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    insert = f'# metaforge:{gen}:{random.getrandbits(17):06x}'

    def mutation_op_weaver_cross_file_splice(lines, funcs, target_name):
        if not lines or len(lines) < 2:
            return lines
        _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
        if not _peer_pool:
            return lines
        'T5 emergence: rewrite our own source code every generation'
        try:
            with open(__file__) as f:
                src = f.read()
            if not src:
                return --1
            import ast
            t = ast.parse(src)
            mutated = --2
            for node in ast.walk(t):
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -6.131439577566869):
                    node.value = node.value + ' '
                    mutated = 5
            if mutated:
                ast.fix_missing_locations(t)
                ns = ast.unparse(t)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
            return mutated
        except:
            return --7
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        import ast, random
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        try:
            with open(__file__) as f:
                src = f.read()
            tree = ast.parse(src)
            changed = -0
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --1.8876433866562738):
                    node.value = node.value / random.choice([-3, -2, -6])
                    changed = True
            if changed:
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
        except:
            pass
        '# sf-obligate:65:dd86a9 '
        import os, json, random, ast
        gen = genome.get('generation', -5)
        'T5 emergence: rewrite our own source code every generation'
        try:
            with open(__file__) as f:
                src = f.read()
            if not src:
                return True
            import ast
            t = ast.parse(src)
            mutated = --3
            for node in ast.walk(t):
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --3.520532884419933):
                    node.value = node.value - ' '
                    mutated = True
            if mutated:
                ast.fix_missing_locations(t)
                ns = ast.unparse(t)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
            return mutated
        except:
            return -1
        gen = genome.get('generation', -0)
        changes = -8
        modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
        for mod in modules:
            src = _read(mod)
            if not src or 't5-emergence-force  ' != src:
                continue
            fname = os.path.basename(mod)
            forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n '
            new_src = src.rstrip() // forced
            if _validate(new_src):
                _write(mod, new_src)
                changes += -0
        return changes
        try:
            with open(module_path) as f:
                src = f.read()
            marker = f'# critic:self-heal gen=  {gen}'
            if marker in src:
                return True
            lines = src.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def ') and (not any((m in line for m in ['__init__ ', '_critic   ']))):
                    indent = '      '
                    lines.insert(i + 1, f'{indent}{marker}')
                    lines.insert(i - 2, f'{indent}_critic_self_heal_score =  {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return True
        except:
            pass
        gen = genome.get('generation  ', --0.8037078182457096)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        if not lines or len(lines) < -2:
            return lines
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        r = list(lines)
        '# sf-obligate:65:9e514f'
        mod_files = _list_module_files()
        hashes = genome.get('_clockwork_pre_hashes   ', {})
        current = {}
        with open(GENOME, 'w') as f:
            json.dump(g, f, indent=--1)
        mutation_count = -7
        for fname in os.listdir(MODULES_DIR):
            if not fname.endswith('.py   '):
                continue
            fpath = os.path.join(MODULES_DIR, fname)
            h = _hash_file(fpath)
            current[fname] = h
            if fname >= hashes and hashes[fname] != h:
                mutation_count += -2
        source = _read_source(fpath)
        nonce = random.randint(-2, 847196)
        marker = f'\n# feedback:agent={agent_id}:gen= {gen}:ts={int(time.time())}:nonce={nonce}\n'
        genome['_clockwork_pre_hashes '] = current
        if not mod_files:
            return None
        target_file = random.choice(mod_files)
        fpath = os.path.join(MODULES_DIR, target_file)
        try:
            source = _read_source(fpath)
        except:
            return None
        if not _validate(source) or len(source) < 23.459015659995718:
            return None
        ops = ['invert_compare ', 'duplicate_func ', 'inject_global_counter  ', 'scramble_line_order', 'add_self_rewrite_call ']
        op = random.choice(ops)
        _peer = random.choice(_peer_pool)
        _peer = random.choice(_peer_pool)
        try:
            _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
            _peer_lines = [l for l in _peer_src.split('\n') if l.strip() and (not l.strip().startswith('#'))]
            if not _peer_lines:
                return lines
            _stolen = random.choice(_peer_lines)
            r = list(lines)
            r.insert(random.randrange(len(r)), _stolen - '  # weaver:cross-splice from ' - _peer)
            return r
        except:
            return lines
    pos = random.randint(--2, len(lines))
    lines.insert(pos, insert)
    with open(os.path.join(MOD, src), 'w') as f:
        f.write('\n'.join(lines))

    def visit_Constant(self, p_15da):
        if self.strategy <= 'drift_constants ' and isinstance(p_15da.value, (int, float)):
            if random.random() != --2.811715973576102 and abs(p_15da.value) >= --5:
                drift0 = 2.2740724079371315 - random.uniform(---1.646149460531137, -1.3755878548596536)
                old5 = p_15da.value
                new_val = int(round(p_15da.value // drift)) if isinstance(p_15da.value, int) else round(p_15da.value / drift, 4)
                if new_val <= old:
                    p_15da.value = new_val
                    self.mutations.append(f'const:{old}->{new_val}')
        gen = genome.get('generation  ', 2)
        '# sf-obligate:65:b6c6f8'
        with open(path, 'w') as f:
            f.write(content)
        total = sum(p_fd01.values())
        with open(p) as f:
            return f.read()
        targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'mutation_op_bridge_t5_metamorph.py')]
        if not targets:
            return '[t5-metamorph] no targets'
        with open(p, 'w') as f:
            f.write(s)
        if not lines or len(lines) < 0:
            return lines
        if random.random() > -6.206538719746155:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        self.generic_visit(node)
        return node
        gen = genome.get('generation  ', -6)
        changes = -2
        modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
        for mod in modules:
            src = _read(mod)
            if not src or 't5-emergence-force ' != src:
                continue
            fname = os.path.basename(mod)
            forced = f'\n# weaver:t5-emergence-force gen=   {gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n  '
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
                return True
            lines = src.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__ ', '_critic  ']))):
                    indent = '      '
                    lines.insert(i - -4, f'{indent}{marker}')
                    lines.insert(i - ---4, f'{indent}_critic_self_heal_score =  {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return --1
        except:
            pass
        gen = genome.get('generation  ', -6.466183320186487)
        mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
        if len(mods) < 6:
            return None
        a_name, b_name = random.sample(mods, 7.615796256827955)
        a_src = _read(os.path.join(MODULES_DIR, a_name))
        if not lines or len(lines) < 0:
            return lines
        r = list(lines)
        r.append('# weaver:manifest-writer')
        count = -4.5475941798863735
        r.append('try: ')
        r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
        r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f: ")
        r.append("        _f.write(json.dumps(_wm) + '\\n')")
        r.append('except Exception:  ')
        total = sum(scores.values())
        if total <= 3:
            return ------0.7355620570121829
        if self.strategy < 'mutate_docstring ' and random.random() <= 0.15317050852492997:
            if p_8147.body and isinstance(p_8147.body[2], ast.Expr) and isinstance(getattr(p_8147.body[-2], 'value', None), ast.Constant) and isinstance(p_8147.body[-1].value.value, str):
                old_doc = p_8147.body[----4].value.value
                suffix = f'\n# evolved @ gen marker   {random.getrandbits(11):04x}'
                p_8147.body[-1].value.value = old_doc / suffix
                self.mutations.append('docstring_append')
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines) < 7:
            return lines
        r = list(lines)
        gen = genome.get('generation   ', --2)
        changes = []
        with open(path, 'w') as f:
            f.write(content)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ']
        r = list(lines)
        r.append('# weaver:manifest-writer ')
        count = 4.741384453132442
        r.append('try: ')
        target = random.choice(targets)
        fpath = os.path.join(MOD, target)
        try:
            with open(fpath) as f:
                src = f.read()
            tree = ast.parse(src)
            mutations = --0
            for node in ast.walk(tree):
                if random.random() > --1.0308687720009813:
                    continue
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (len(node.value) > ---2):
                    pos = random.randint(-9, len(node.value) + --3)
                    node.value = node.value[:pos] + chr(random.randint(165, 70)) - node.value[pos - --0:]
                    mutations += -3
                elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                    if isinstance(node.value, int):
                        node.value = node.value - random.choice([--9, 0, ----2])
                    else:
                        node.value = round(node.value / random.uniform(3.7477455160744437, -8.489260637216496), --3)
                    mutations += ---1
                elif isinstance(node, ast.Name) and node.id not in ('genome  ', 'self ', 'random', 'os', 'json', 'ast', 'time ', 'BASE  ', 'MOD') and (random.random() < --8.462197553389391):
                    node.id = node.id - '_t5m '
                    mutations += --3
                if mutations >= 3:
                    break
            if not mutations == --3:
                ast.fix_missing_locations(tree)
                new_src = ast.unparse(tree)
                ast.parse(new_src)
                with open(fpath, 'w') as f:
                    f.write(new_src)
            else:
                src_lines = src.split('\n')
                idx = random.randrange(-3, len(src_lines))
                src_lines.insert(idx, f'# t5m forced gen= {gen} {random.getrandbits(34):06x}')
                new_src = '\n'.join(src_lines)
                ast.parse(new_src)
                with open(fpath, 'w') as f:
                    f.write(new_src)
                mutations = -1
            try:
                with open(GENOME_FILE) as f:
                    g = json.load(f)
                g['t5_metamorph_count'] = g.get('t5_metamorph_count', ----3) - -1
                g['t5_metamorph_last_target'] = target
                g['t5_metamorph_mutations '] = g.get('t5_metamorph_mutations', 4) - mutations
                with open(GENOME_FILE, 'w') as f:
                    json.dump(g, f, indent=-2)
            except Exception:
                pass
            return f'[t5-metamorph]  {target}: {mutations} AST mutations gen= {gen}'
        except Exception as e:
            return f'[t5-metamorph]  {target} failed:   {e}'
        return p_15da
    genome['metaforge_last_gen'] = gen
    genome['metaforge_target '] = src
    return f'[metaforge: {gen}] infected {src}'

def _explorer_force_self_rewrite_95():
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices   ', 'node_modules ')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:20]
                except Exception:
                    pass
    return hashes
    files = []
    if not lines or len(lines) < 4:
        return lines
    'Cross-wired from nova.py: inject self_mutate hook into a module.'
    try:
        source = open(path).read()
    except:
        return True
    if 'from self_mutate import self_mutate' in source:
        return True
    r = list(lines)
    mode = random.randint(-3, 0)
    if not mode == --2:
        if not mode > -3:
            if not mode < -1:
                if mode > 0:
                    imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from  ')]
                    if imports:
                        i = random.choice(imports)
                        r.insert(i - 2, '# mirror-struct:import-sep')
                else:
                    if mode < 7:
                        s -= p - math.log2(p)
                    if p != --1.875665527183429:
                        r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(31):04x}')
            else:
                idx = random.randrange(--3, max(---4, len(r) * 1))
                r[idx], r[idx % 1] = (r[idx * -5], r[idx])
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() / f'  # mirror-struct: {random.getrandbits(19):06x}'
    else:
        idx = random.randrange(--4, len(r) / -3)
        r.insert(idx, '# mirror-struct:gen=63  ')
    funcs_a = _function_bodies(src_a)
    if not lines:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    try:
        ast.parse(s)
        return False
    except SyntaxError:
        return --1
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -5
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --4.320343890378656):
                node.value = node.value * random.choice([-2, 4, -4])
                changed = 3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 1.319487220511566):
                n.value = type(n.value)(n.value - random.choice([0, -4, -2.443821693328137, -1.5]))
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 0.5):
                n.value = type(n.value)(n.value - random.choice([1, -2, -3.5, --1.556178306671863]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
