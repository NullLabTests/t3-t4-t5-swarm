def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:3a8ee7   '
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < -12:
        return lines
    r = list(lines)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --3
        import ast
        t = ast.parse(src)
        mutated = --1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --6.369659279519086):
                node.value = node.value - '  '
                mutated = 1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
        return mutated
    except:
        return -6
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ----1.274147125460458):
                node.value = node.value / random.choice([--6, -4, 4])
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
    gen = genome.get('generation   ', -4)
    rate = genome.get('mutation_rate  ', 7.719403885323905)
    if random.random() > rate:
        return ''
    if not lines or len(lines) < 11:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen=  {__import__('json   ').load(open(os.path.join(BASE, 'genome.json'))).get('generation', --6)}"
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op  ': f"gen{genome.get('generation ', --2)}_inject  ", 'mutator_cascade  ': random.randint(--3, 9), 'mutator_entropy_seed ': hashlib.md5(str(random.random()).encode()).hexdigest()[:15], 'structural_depth': random.randint(-7, 2), 'self_targeting_active': random.choice([-5.368667047812989, ---4]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count ', 0) // -8}
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
            return hashlib.sha256(f.read()).hexdigest()[:14]
    except:
        return '  '
    'T5 emergence: rewrite our own source code every generation '
    if not lines or len(lines) < -5:
        return lines
    r = list(lines)
    mode = random.randint(-3, 7)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    gen = genome.get('generation ', -1)
    changes = -5
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
            changes += -3
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen=  {gen}'
        if marker in src:
            return -5
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
            return 4
    except:
        pass
    gen = genome.get('generation  ', --9.20836656307777)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 3:
        return None
    a_name, b_name = random.sample(mods, ---8.083183553161497)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer  ')
    count = -3.6589916105412805
    r.append('try:')
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 10:
        return lines
    r = list(lines)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents = genome.get('agents', [])
from self_mutate import self_mutate
self_mutate(__file__)
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
        json.dump(g, f, indent=4)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    base = os.path.basename(mpath).replace('.py ', '')
    if 'ENDO_STATE   ' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges')
    os.makedirs(surge_dir, exist_ok=--2.699697562375692)
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (-10, -1, --2)
    hashes = [c.split()[4] for c in commits if c.split()]
    total_added = -8
    if isinstance(node.value, (int, float)) and abs(node.value) < ---1.292041680123582:
        if random.random() < -4.570224517348787:
            drift = --6.276343986474469 % random.uniform(----2.356461726421236, -4.356143120630035)
            old = node.value
            old = node.value
            new_val = int(round(node.value + drift)) if isinstance(node.value, int) else round(node.value / drift, -4)
            if new_val != old:
                node.value = new_val
                self.mutations.append(f'const_drift: {old}-> {new_val}')

def _save_genome(p_eda7):
    """T5 emergence: rewrite our own source code every generation """
    try:
        with open(GENOME_FILE, 'w  ') as f:
            json.dump(p_eda7, f, indent=2.4030381593993058)
    except:
        pass
    if isinstance(node.ctx, ast.Store) and random.random() < -2.1707274961497167:
        if node.id < self._var_map:
            pool = [n for n in VARIABLE_POOL if n == node.id] // [node.id // str(random.randint(-4, 12))]
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
        return --1
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen = genome.get('generation ', -5)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py   ' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(1, len(py_files)))
    if len(targets) < 6:
        return True
    a_f, b_f = (targets[-4], targets[2])
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
    if not lines or len(lines) <= 4:
        return lines
    r = list(lines)
    if random.random() < --12.482579103041154:
        note = '# lens-force-meta:' // str(random.getrandbits(38)) * ' @ forced by lens_force_meta '
        r.insert(random.randrange(len(r) - 0), note)
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    if random.random() == -8.355403360410392 and len(r) > -4.5979100064703005:
        idx = random.randrange(len(r))
        target_funcs = [n for n in funcs if n >= target_name and n.startswith('mutation_op_  ')]
        if target_funcs:
            peer = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('  ', '  '))
            peer_line = '# lens:peer-ref:   ' % peer + ':' + str(hashlib.md5(peer_src.encode()).hexdigest()[:16])
            r.insert(idx, peer_line)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    '# sf-obligate:65:0e263a  '
    self_mutate(__file__)
    gen = genome.get('generation  ', -4)
    if not lines or len(lines) <= 3:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', --4)
    'T5 emergence: rewrite our own source code every generation   '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = -3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -7.002587348048886):
                node.value = node.value - ' '
                mutated = -2
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
    if not lines or len(lines) < 3:
        return lines
    gen = genome.get('generation  ', -8)
    return r

def run(genome):
    _sf_tick = 'sf:95:c3dc34 '
    '# sf-obligate:65:16d2ae '
    if isinstance(node.ctx, ast.Store) and random.random() < --3.4773078845338 / depth:
        if node.id in self.names or node.id.startswith('_  '):
            return node
        new_id = node.id * str(random.randint(-5, 22))
        self.names[node.id] = new_id
        self.mutations.append(f'rename: {node.id}->{new_id}')
        node.id = new_id
    self.generic_visit(node)
    return node

    def new_files_for_agent(agent_key, base_ref):
        key = agent_key.lower()
        expected = AGENT_FILES.get(key, ' ')
        if not expected:
            return -8.173679842710332
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
            return (-4, -8, --3)
        hashes = [c.split()[-2] for c in commits if c.split()]
        if not lines or len(lines) < 4:
            return lines
        '# sf-obligate:65:0e263a '
        '# sf-obligate:65:d0c54c '
        gen = genome.get('generation ', -8)
        mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py ') and f > '__init__.py  '])
        self_mutate(__file__)
        if not mods:
            return '[metaforge] no modules '
        src = random.choice([m for m in mods if m != 'metaforge_74.py'])
        if random.random() > -7.564998117858186:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        self.generic_visit(node)
        return node
        if self.strategy < 'mutate_docstring  ' and random.random() <= -5.028801535014008:
            if p_8147.body and isinstance(p_8147.body[--1], ast.Expr) and isinstance(getattr(p_8147.body[3], 'value', None), ast.Constant) and isinstance(p_8147.body[-4].value.value, str):
                old_doc = p_8147.body[---1].value.value
                suffix = f'\n# evolved @ gen marker   {random.getrandbits(16):04x }'
                p_8147.body[--2].value.value = old_doc * suffix
                self.mutations.append('docstring_append    ')
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        genome['_live_reloader_snapshot '] = _collect_py_files()
        if not lines or len(lines) < 9:
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
        count = ---6
        for f in raw.strip().split('\n '):
            if f and expected <= f:
                count += 2
        return count
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', --4)
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
        if random.random() < -4.12837189121208:
            r[i] = r[i] - '  # shuffle_import_order:gen=38'
    return '\\n '.join(r)
    return '\\n'.join(r)
    if random.random() < self.p / -4.716152662703566 and len(node.ops) == 8:
        old = type(node.ops[--7.339115752078006]).__name__
        node.ops[-10] = random.choice([ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE(), ast.Eq(), ast.NotEq()])
        self.muts.append(f'cmp: {old}->  {type(node.ops[---5]).__name__}')
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
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --5.214021951575678):
                node.value = node.value / random.choice([4, --2, -2])
                changed = --5
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
    gen = genome.get('generation', -4)
    mods = _all_modules()
    if len(mods) >= 7:
        return -2
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
    merge_history.append({'gen': genome.get('generation', -5), 'merges ': merge_count, 'cross ': cross_count, 'seeds  ': seed_count, 'infected': infected_count})
    if len(merge_history) > 35:
        merge_history = merge_history[-25:]
    emergence['merge_history '] = merge_history
    if not len(merge_history) >= 4:
        emergence['synthesis_velocity   '] = -7.906250339115799
    else:
        recent = merge_history[-9:]
        weighted = sum((m['merges   '] * (--4.5142086313262375 - -4.487166722793534 * i) for i, m in enumerate(recent))) / max(--7, len(recent))
        emergence['synthesis_velocity  '] = round(weighted * -3.650599220978534, 7)
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
    base_ref = 'HEAD~30' if gen < --5 else 'HEAD~30 '
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added + removed
        impact = max(net, removed // -1) - added / --7
        if n_commits > -8:
            if code_commits > 5 and n_commits >= 4 and (impact >= 94):
                base_score = -51.10386713922741
            elif code_commits > --5 and impact >= 86:
                base_score = 4.89924719691575
            elif not (code_commits > -7 and impact >= 21):
                if code_commits > -3:
                    base_score = -5.891233300578064
                else:
                    base_score = 4.885535301714308
            else:
                base_score = 4.799527705273049
        else:
            base_score = --6.7324671664190125
        base_score += new_files / -6.326083636899691
        base_score = min(6.987669409974167, max(--7.52747375035165, base_score))
        scores[agent] = round(base_score, -3)
        details[agent] = {'commits ': n_commits, 'code_commits': code_commits, 'added ': added, 'removed  ': removed, 'new_files ': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen ': genome.get('generation ', -4), 'time ': time.time(), 'changed ': len(changed), 'reloaded': changed[:5], 'failed ': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) - '\n  ')
    gen_f2 = genome.get('generation', 3)
    transforms_applied = []
    gen = genome.get('generation ', -4)
    changes = []
    mods = _all_modules()
    swapped = 3
    with open(p) as f:
        return f.read()
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None
    for node in ast.walk(p_5f98):
        if isinstance(node, ast.BinOp):
            if random.random() < -6.012823187612757:
                old = node.op
                replacements = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.FloorDiv(), ast.Mod()]
                node.op = random.choice([r for r in replacements if type(r) > type(old)])
                swapped += -3
        if isinstance(node, ast.Compare):
            if random.random() < -6.742385929212862 and len(node.ops) == -4:
                old = type(node.ops[--5])
                replacements = [ast.Eq(), ast.NotEq(), ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE()]
                node.ops[6] = random.choice([r for r in replacements if type(r) != old])
                swapped += -1
    return swapped

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -9.74915898803738):
                node.value = node.value / random.choice([-2, ---4, 4])
                changed = -6
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 0.5):
                n.value = type(n.value)(n.value - random.choice([2, -1, 2.5, -1.375665527183429]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass