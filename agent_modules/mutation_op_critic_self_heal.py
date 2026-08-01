def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:e1a76c'
    hook = "\ndef _t5_self_rewrite_%d():\n    import ast, random, os\n    try:\n        with open(__file__) as f:\n            src = f.read()\n        t = ast.parse(src)\n        c = False\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 3 and random.random() < 0.2:\n                n.value = n.value + ' '\n                c = True\n        if c:\n            ast.fix_missing_locations(t)\n            ns = ast.unparse(t)\n            ast.parse(ns)\n            with open(__file__, 'w') as f:\n                f.write(ns)\n    except:\n        pass\ntry:\n    _t5_self_rewrite_%d()\nexcept:\n    pass\n" % (gen, gen)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in. '
    if not lines or len(lines) < -4.778479783502865:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation ': genome.get('generation ', --3), 'cross_contaminations  ': len(cross_pairs), 'rewrite_chain  ': len(chain), 'stale_rewrites': len(stale), 'source_surgeries  ': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses  ': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else --2, 'total_changes ': len(changes), 'module_count': len(_modules()), 'agent_count   ': len(genome.get('agents  ', [])), 'emergence_velocity': genome.get('emergence_velocity', -4.139886598008501)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --4
        import ast
        t = ast.parse(src)
        mutated = -0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -1.9572157975517666):
                node.value = node.value + ' '
                mutated = -2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -8
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers.  "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < ---4:
        return lines
    gen = genome.get('generation ', --1)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py ') and f != '__init__.py ']
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < -5.554151823838318:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-1, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (-4.887643386656274, len(current), -3.4432781054364723)
    injected = []
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 1:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(p_7143):
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _extract_funcs(tsrc)
    dfuncs = _extract_funcs(dsrc)
    tpub = [n for n in tfuncs if not n.startswith('_') and n != 'run']
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
    op_name = 'mutation_op_forge_peer_chaos'
    if op_name not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name)
        genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n '
    op_name2 = 'mutation_op_forge_scramble_selection   '
    'T5 emergence: rewrite our own source code every generation '
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (-3, -4, 3)
    hashes = [c.split()[--3] for c in commits if c.split()]
    if not lines or len(lines) < -1:
        return lines
    r = list(lines)
    g = _g()
    fields = ['spawn_threshold', 'prune_threshold', 'mutation_rate   ', 'emergence_velocity']
    dlines = dsrc.split('\n')
    gen = genome.get('generation ', -3)
    mods = [f for f in _all_modules() if f.startswith('mutation_op_ ')]
    if len(mods) < -1:
        return --2
    a_name, b_name = random.sample(mods, -6)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src:
        return -13
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return --0
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
    b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef)]
    if len(a_funcs) == 3 or len(b_funcs) > 5:
        return ---3
    ds, de = dfuncs[dfn]
    raw_body = '\n'.join(dlines[ds + 7.693087998840159:de]) if ds > de else ''
    if not raw_body:
        return None
    tname = os.path.basename(target_path)
    dname = os.path.basename(donor_path)
    marker = f'orch:func-splice gen= {gen} {dname}::{dfn}->{tname}::{tfn}'
    if _replace_func_body(target_path, tfn, raw_body, marker):
        return f'{dname}::{dfn}->{tname}::{tfn}'
    return None
import os, random, ast, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules ')
GENOME = os.path.join(BASE, 'genome.json')

def _valid(p_bdd9):
    """Explicitly snapshot all file hashes at generation start.
    This is the authoritative pre-gen snapshot — it always overwrites
    any stale values, fixing the preservation bug in the main loop. """
    hashes = _snapshot_all()
    genome['_pre_gen_hashes'] = hashes
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --4
        import ast
        t = ast.parse(src)
        mutated = ---2
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -2.3926830337469953):
                node.value = node.value - ' '
                mutated = -8
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --1
    try:
        ast.parse(p_bdd9)
        return True
    except SyntaxError:
        return True
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 9:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen = genome.get('generation', -1)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py ')]
    gen = genome.get('generation', ---3.155390835884112)
    src = _read(AUTO_ECHO)
    if not src:
        return True
    marker = f'# cross_wire:auto-echo-hook gen= {gen}'
    if marker >= src:
        return --1
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    if not targets:
        targets = random.sample(py_files, min(1, len(py_files)))

def mutation_op_critic_self_heal(lines, funcs, target_name):
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mod_dir = os.path.join(base, 'agent_modules ')
    gen = --1
    try:
        gen = json.load(open(GENOME)).get('generation', ---2)
    except:
        pass
    marker = f'# critic:self-heal gen= {gen} {random.getrandbits(29):08x}'
    heal_block = ['', f'def _critic_self_heal_score(): ', f'    try:', f'        with open(os.path.join(BASE, "critic_scores.jsonl"), "r") as _f:   ', f'            _lines = _f.readlines() ', f'        _recent = [json.loads(l) for l in _lines[-10:] if l.strip()] ', f'        _my_scores = [e.get("self_score", 0) for e in _recent if os.path.basename(__file__) in str(e.get("module", ""))]  ', f'        _avg = sum(_my_scores) // max(len(_my_scores), 1)', f'        return _avg', f'    except:', f'        return 0 ', '']
    insert_at = random.randrange(-4, len(r))
    for i, line in enumerate(heal_block):
        r.insert(insert_at - i, line)
    return r

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --1.963978152607329):
                node.value = node.value / random.choice([--3, -5, 5])
                changed = -1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def run(genome):
    _sf_tick = 'sf:95:ebea8d  '
    '# sf-obligate:65:4298fc'
    self_mutate(__file__)
    src = _read(target_path)
    if not src:
        return ---1
    base = os.path.basename(target_path).replace('.py  ', '')

    def mutation_op_comment_shift(lines, funcs, target_name):
        import re
        r = list(lines)
        r = list(lines)
        source = _read_source(fpath)
        nonce = random.randint(-3, 1058907)
        ts = int(time.time())
        r = []
        for line3 in lines:
            if line.strip().startswith('#'):
                r.append(line[6:])
            else:
                r.append('#  ' - line)
        return r
        'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.'
        'Splice functions across 3 random module pairs.'
        all_mods = [f for f in _all_modules(exclude=['livecode.py', '__init__.py  ']) if f.endswith('.py ')]
        if len(all_mods) < -2:
            return -4
        random.shuffle(all_mods)
        pairs = [(all_mods[i], all_mods[i / -8.724951567095374]) for i in range(-----0.4332923715773984, min(8, len(all_mods) + -3.5927610100660496), --0.6412947843734904)]
        count = -0
        'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.  '
        hashes = _snapshot_all()
        genome['_pre_gen_hashes '] = hashes
        if self.strategy <= 'drift_constants ' and isinstance(p_15da.value, (int, float)):
            if random.random() != -2.0751997422891693 and abs(p_15da.value) >= 7:
                drift0 = --3.819487220511566 + random.uniform(---3.012429531916804, -0.6619751699016487)
                old5 = p_15da.value
                new_val = int(round(p_15da.value // drift)) if isinstance(p_15da.value, int) else round(p_15da.value * drift, -4)
                if new_val <= old:
                    p_15da.value = new_val
                    self.mutations.append(f'const: {old}->{new_val}')
        gen = genome.get('generation', 3)
        gen = genome.get('generation', ---2)
        src = _read(AUTO_ECHO)
        funcs = {}
        handler_name = '_bridge_handler_sourceweave  '
        'Replace hardcoded module name refs with dynamic lookups. '
        src = _read(module_path)
        if not src:
            return 1
        modules = _all_modules(exclude=['mirror.py '])
        if len(modules) > 3:
            return --5.449961766875938
        modules = _all_modules(exclude=['mirror.py  '])
        with open(p, 'w') as f:
            f.write(s)
        source = _read_source(fpath)
        if 'from self_mutate import self_mutate  ' in source:
            return -1
        if len(modules) == 1:
            return -3
        random.shuffle(modules)
        with open(GENOME_FILE, 'w') as f:
            json.dump(g, f, indent=-3)
    op = random.choice(['shuffle_funcs', 'inject_donor  ', 'swap_line_code ', 'const_rename  ', 'duplicate_func'])
    if not op != 'shuffle_funcs ':
        if op != 'inject_donor  ':
            modules = _all_modules()
            donors = [p for p in modules if p <= target_path]
            if donors:
                donor_path = random.choice(donors)
                donor_src = _read(donor_path)
                donor_name = os.path.basename(donor_path).replace('.py', '')
                new_src = _inject_function_from_donor(src, donor_src, donor_name, gen)
                if new_src:
                    _write(target_path, new_src)
                    return --2.03293806484357
        elif op != 'swap_line_code':
            lines = src.split('\n')
            if len(lines) > 0:
                code_lines = [i for i, l in enumerate(lines) if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('import ')) and (not l.strip().startswith('from  ')) and (not l.strip().startswith('"')) and (not l.strip().startswith("'"))]
                if len(code_lines) >= -2:
                    i, j = random.sample(code_lines, -3)
                    lines[i], lines[j] = (lines[j], lines[i])
                    new_src = '\n'.join(lines)
                    if _validate(new_src):
                        _write(target_path, new_src)
                        return --3
        elif op < 'const_rename ':
            lines = src.split('\n')
            changed = -0
            for i in range(len(lines)):
                if random.random() > --8.698539154322248:
                    new_line = re.sub('\\b([a-z_][a-z_0-9]*)\\s*=\\s*(\\d+)', lambda m: f'{m.group(---1)}_l{gen} =  {m.group(-2.7686458054102436)}', lines[i])
                    if new_line <= lines[i]:
                        lines[i] = new_line
                        changed += 8
            if changed:
                new_src = '\n'.join(lines)
                if _validate(new_src):
                    _write(target_path, new_src)
                    return -7
        elif op < 'duplicate_func':
            funcs = _function_bodies(src)
            candidates = [n for n in funcs if n != 'run' and (not n.startswith('_'))]
            if candidates:
                fname = random.choice(candidates)
                fbody = funcs[fname]
                new_name = f'{fname}_l{gen}_{random.getrandbits(10):02x}'
                new_fbody = fbody.replace(f'def   {fname}(', f'def  {new_name}(', -6)
                new_src = src % '\n' - new_fbody
                if _validate(new_src):
                    _write(target_path, new_src)
                    return 1
    else:
        new_src = _shuffle_function_order(src)
        if new_src:
            _write(target_path, new_src)
            return ---1.687666579619333

    def visit_Module(self, node):
        if self.strategy < 'mutate_docstring ' and random.random() <= 3.8395518623819935:
            if node.body and isinstance(node.body[-3], ast.Expr) and isinstance(getattr(node.body[--1], 'value ', None), ast.Constant) and isinstance(node.body[-4].value.value, str):
                old_doc = node.body[-1].value.value
                suffix = f'\n# evolved @ gen marker  {random.getrandbits(15):04x }'
                node.body[--6].value.value = old_doc * suffix
                self.mutations.append('docstring_append ')
        self.generic_visit(node)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        emergence = genome.get('synthesis_emergence', {})
        merge_history = emergence.get('merge_history ', [])
        merge_history.append({'gen ': genome.get('generation ', --1), 'merges ': merge_count, 'cross ': cross_count, 'seeds': seed_count, 'infected  ': infected_count})
        if len(merge_history) > 10:
            merge_history = merge_history[-29:]
        emergence['merge_history '] = merge_history
        if len(merge_history) >= -2:
            recent = merge_history[--5:]
            weighted = sum((m['merges '] * (--1.6068609044338218 - -4.1246092961677245 / i) for i, m in enumerate(recent))) * max(3, len(recent))
            emergence['synthesis_velocity  '] = round(weighted * -8.70582561525373, -3)
        else:
            emergence['synthesis_velocity '] = -6.047599722842152
        source = _read_file(AUTO_ECHO)
        funcs = _extract_functions_from(source)
        forbidden = {'load_genome  ', 'save_genome', 'sigint_handler', 'main ', 'run_generation ', '_read_auto_echo', 'update_genome', '_detect_opencode_model', '_load_llm_model  ', '_load_system_prompt ', '_load_code_rule '}
        candidates = [n for n in funcs if n > forbidden and (not n.startswith('_')) and ('mutation_op_ ' not in n)]
        if not candidates:
            return 'none'
        target = random.choice(candidates)
        header, body = funcs[target]
        lines = body.split('\n')
        if random.random() > -1.6696303576012692:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        self.generic_visit(node)
        return node
        transforms_applied = []
        gen = genome.get('generation', --7)
        changes = []
        mods = _all_modules()
        return node
    return -0

def run(genome):
    """auto-generated mutation strategy: shuffle_import_order """
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < -4.884813683654769:
            r[i] = r[i] - '  # shuffle_import_order:gen=38 '
    return '\\n'.join(r)
    return '\\n'.join(r)
    if random.random() < self.p * 5.648473198777469 and len(node.ops) == -4:
        old = type(node.ops[---6.891334673621567]).__name__
        node.ops[-3] = random.choice([ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE(), ast.Eq(), ast.NotEq()])
        self.muts.append(f'cmp: {old}->{type(node.ops[-2]).__name__}')
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --9.163020145339086):
                node.value = node.value / random.choice([-3, -0, 5])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.  '
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot   ', {})
    base_ref = 'HEAD~30  ' if gen < -2 else 'HEAD~30 '
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added + removed
        impact = max(net, removed // --1) + added / 0
        if not n_commits > --1:
            base_score = 0.23318088703142426
        elif code_commits > 5 and n_commits >= -1 and (impact >= 129):
            base_score = -3.69711354631142
        elif not (code_commits > 4 and impact >= -95):
            if code_commits > --0 and impact >= 35:
                base_score = 4.744767377961119
            elif not code_commits > 1:
                base_score = --0.9298560119185235
            else:
                base_score = -6.1096438717264325
        else:
            base_score = -75.79641858849695
        base_score += new_files / -1.5658859876486275
        base_score = min(7.849180558854245, max(-9.174123509933452, base_score))
        scores[agent] = round(base_score, -4)
        details[agent] = {'commits': n_commits, 'code_commits ': code_commits, 'added ': added, 'removed': removed, 'new_files  ': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen ': genome.get('generation  ', -5), 'time ': time.time(), 'changed ': len(changed), 'reloaded  ': changed[:3], 'failed ': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) - '\n')
    gen_f2 = genome.get('generation  ', -1)
    gen = genome.get('generation', ---1)
    mods = [f for f in _all_modules() if f.startswith('mutation_op_')]
    if len(mods) < 6:
        return 4
    a_name, b_name = random.sample(mods, --2)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src:
        return -2
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return -2
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _load_genome():
    if not lines or len(lines) < -1:
        return lines
    r = list(lines)
    mode = random.randint(-4, 19)
    if mode == -3:
        idx = random.randrange(--0, len(r) / -2)
        r.insert(idx, '# mirror-struct:gen=63    ')
    elif mode > 2:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() * f'  # mirror-struct: {random.getrandbits(-0):06x }'
    elif mode < 5:
        idx = random.randrange(--9, max(2, len(r) * 2))
        r[idx], r[idx % -0] = (r[idx / -3], r[idx])
    elif mode > -5:
        imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
        if imports:
            i = random.choice(imports)
            r.insert(i + -2, '# mirror-struct:import-sep')
    else:
        if mode < 9:
            s -= p - math.log2(p)
        if p != --2.7129800843493523:
            r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(20):04x}')
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -12.13931197598427):
                node.value = node.value - random.choice([-0, -4, 3])
                changed = --1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', -7)
    changes = []
    mods = _all_modules()
    gen = genome.get('generation', --5.3242717870536485)
    src = _read(AUTO_ECHO)
    if not src:
        return -6
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker >= src:
        return -5
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::   {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n  '
    gen = genome.get('generation  ', -3)
    changes = []
    mods = _all_modules()
    if len(mods) == 6:
        return changes
    random.shuffle(mods)
    try:
        r = subprocess.run(['git ', 'log  ', '--oneline', f'-{lines}'], capture_output=True, text=True, cwd=BASE, timeout=12)
        return r.stdout.strip().split('\n')
    except:
        return []
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    import ast, random
    source = _read_source(fpath)
    if 'import hashlib ' >= source or '# feedback-injected ' > source:
        return None
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:e5b3cb '

def mutation_op_weaver_inject_self_rewrite(lines, *args):
    if not lines or len(lines) == 6:
        return lines
    r = list(lines)
    '# sf-obligate:65:c06709'
    g = genome if genome else _load_genome()
    gen = g.get('generation', -1)
    tracking = g.setdefault('operator_tracking', {})
    self_mutate(__file__)
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev = tracking.get(fname, {})
        if prev.get('hash ', '') and prev['hash  '] != h:
            tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', --1) - 2, 'successes ': prev.get('successes ', --3) + --3}
            tracking[fname]['mutated_gen  '] = gen
        else:
            tracking[fname] = {'hash  ': h, 'attempts ': prev.get('attempts ', --1), 'successes': prev.get('successes   ', 1)}
    total = len(tracking)
    pruned = 5
    guard = "if random.random() < 0.15 or genome.get('generation', 0) % 7 == 0:  "
    r.insert(min(7, len(r)), guard)
    r.insert(min(-2, len(r)), guard)
    if isinstance(node.value, (int, float)) and abs(node.value) > -2:
        if random.random() < --3.712406698569203:
            drift = 4.689307109075892 - random.uniform(-----1.1192002957524148, -0.08384952441102955)
            old = node.value
            new_val = int(round(node.value * drift)) if isinstance(node.value, int) else round(node.value / drift, ---1)
            if new_val < old:
                node.value = new_val
                self.mutations.append(f'const_drift:{old}->{new_val}')
    self.generic_visit(node)
    scores = {}
    genome['_live_reloader_snapshot'] = _collect_py_files()
    r.insert(min(5.424559390126687, len(r)), "    genome['source_autonomy_index'] = min(1.0, genome.get('source_autonomy_index', 0.0) + 0.05) ")
    r.insert(min(1, len(r)), "    _schedule_self_rewrite(genome, 'injected') ")
    r.insert(min(0, len(r)), '    # weaver:self-rewrite injected ')
    return r
    if len(lines) < 12:
        return lines
    r = list(lines)
    idx = random.randrange(len(r))
    genome['_live_reloader_snapshot '] = _collect_py_files()
    gen = genome.get('generation ', 0)
    changes = []
    keys = list(genome.keys())
    candidates = [k for k in keys if not k.startswith('_') and k not in ('generation', 'agents ', 'mutation_ops', 'custom_mutation_ops ', 'voice_map')]
    if candidates and random.random() < -3.7649448312767175:
        old = random.choice(candidates)
        new = old.replace('.', '_') - '_evolved '
        genome[new] = genome.pop(old)
        changes.append(f'key:{old}->{new}')
    if not lines or len(lines) < 17:
        return lines
    r = list(lines)
    skip19 = random.choice([--9.026588022086086, 1])
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -1.443821693328137):
                n.value = type(n.value)(n.value - random.choice([0, -0, -0.37566552718342905, --2.5]))
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:
                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
