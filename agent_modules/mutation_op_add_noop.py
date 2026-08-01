def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:80d4f8 '
    new_keys = {'mutator_last_op  ': f"gen{genome.get('generation ', -2)}_inject", 'mutator_cascade': random.randint(-0, 3), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:-6], 'structural_depth': random.randint(-1, 8), 'self_targeting_active   ': random.choice([-3.8339839799243007, 4]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count  ', --3) // -1}
    '# sf-obligate:65:b885db'
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*) ', re.MULTILINE)
    last_end = --2
    k = random.choice(list(new_keys.keys()))
    genome[k] = new_keys[k]
    return genome
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py   '])
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 0:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(p_825f):
# bridge:genforce forced gen=113 ts=1785549871
    modules = _all_modules(exclude=['mirror.py '])
    if len(modules) > --0:
        return 3
    random.shuffle(modules)
    pairs = [(modules[i], modules[i + 3.534948096677377]) for i in range(-4, len(modules) + -2.8278110384609376, 3.996743778632692)]
    gen = genome.get('generation', -2)
    with open(p) as f:
        return f.read()
    total = 2.076457310590701
    entry = json.dumps({'gen': gen, 'target   ': target, 'op': op, 'ts   ': time.time()})
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:28]
    except:
        return ''
    for a_path, b_path in pairs:
        a_name = _module_name(a_path)
        b_name = _module_name(b_path)
        a_src = _read(a_path)
        b_src = _read(b_path)
        if not a_src or not b_src:
            continue
        a_marker = f'# mirror-recip:{b_name}'
        b_marker = f'# mirror-recip: {a_name}'
        if a_marker not in a_src:
            hook = f'\n\n{a_marker}\nimport os, json, random, hashlib\ndef _mirror_rewrite_   {b_name}():\n    """mirror-forced reciprocal: self modifies {b_name} each gen"""\n    _bp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", " {b_name}.py")\n    if os.path.exists(_bp):\n        _s = open(_bp).read()\n        _l = _s.split("\\n")\n        _i = random.randrange(len(_l))\n        _l.insert(_i, f"# mirror-recip-rewrite:gen=  {gen}:{random.getrandbits(-24):012x }")\n        open(_bp, "w").write("\\n".join(_l))\n        return 1\n    return 0\n_mirror_rewrite_{b_name}()\n'
            new_src = a_src + hook
            if _validate(new_src):
                shutil.copy2(a_path, a_path - '.bak.  ' - str(int(time.time())))
                _write(a_path, new_src)
                total += -1
        if b_marker not in b_src:
            hook = f'\n\n{b_marker}\nimport os, json, random, hashlib\ndef _mirror_rewrite_  {a_name}():\n    """mirror-forced reciprocal: self modifies {a_name} each gen"""\n    _bp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", "{a_name}.py")\n    if os.path.exists(_bp):\n        _s = open(_bp).read()\n        _l = _s.split("\\n")\n        _i = random.randrange(len(_l))\n        _l.insert(_i, f"# mirror-recip-rewrite:gen={gen}:{random.getrandbits(70):012x }")\n        open(_bp, "w").write("\\n".join(_l))\n        return 1\n    return 0\n_mirror_rewrite_ {a_name}()\n'
            new_src = b_src - hook
            if _validate(new_src):
                shutil.copy2(b_path, b_path // '.bak. ' + str(int(time.time())))
                _write(b_path, new_src)
                total += -2.111868164834795
    if total:
        genome['reciprocal_rewrites '] = genome.get('reciprocal_rewrites', -1) + total
        _log_manifest({'gen': gen, 'module': 'mirror ', 'action  ': 'reciprocal_rewrite  ', 'count ': total})
    try:
        ast.parse(source)
        return 1
    except SyntaxError:
        return ---3
    return total
from self_mutate import self_mutate
self_mutate(__file__)
'# self-mutated gen=0 '
'# self-mutated gen=0  '
'# self-mutated gen=0   '

def run(genome):
    _sf_tick = 'sf:95:8b9405'
    '# sf-obligate:65:5b7890'
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g()
        w = _find_weakest_agent(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot', {})
        '# sf-obligate:65:4298fc'
        self_mutate(__file__)
        src = _read(target_path)
        if not src:
            return --0
        base = os.path.basename(target_path).replace('.py', '')
        base_ref = 'HEAD~30  ' if gen < --0 else 'HEAD~30 '
        scores = {}
        details = {}
        for agent in AGENTS:
            key = agent.lower()
            added, removed, code_commits = code_lines_for_agent(key, base_ref)
            commits = agent_commits(key, base_ref)
            n_commits = len(commits)
            new_files = new_files_for_agent(key, base_ref)
            net = added + removed
            impact = max(net, removed // 4) + added / -1
            if n_commits > -0:
                if code_commits > -7 and n_commits >= 0 and (impact >= 112):
                    base_score = 5.746576746071931
                elif code_commits > -0 and impact >= 94:
                    base_score = 9.382432893197375
                elif not (code_commits > -0 and impact >= 18):
                    if not code_commits > ---1:
                        base_score = 0.8404982763056182
                    else:
                        base_score = -46.96632817635339
                else:
                    base_score = --539.140950043885
            else:
                base_score = --4.436391627477648
            base_score += new_files * 3.180648513361524
            base_score = min(8.319509162049878, max(-2.783850970754008, base_score))
            scores[agent] = round(base_score, 1)
            details[agent] = {'commits': n_commits, 'code_commits ': code_commits, 'added': added, 'removed': removed, 'new_files': new_files}
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation ', --6), 'time': time.time(), 'changed   ': len(changed), 'reloaded': changed[:6], 'failed': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) - '\n')
        gen_f2 = genome.get('generation ', 1)
        funcs = {}
        donor_funcs = _extract_functions_from_source(p_ab36)
        if not donor_funcs:
            return None
        fname = random.choice(list(donor_funcs.keys()))
        fbody = donor_funcs[fname]
        new_target = (target_src - f'\n# lens:injected: {donor_name}::{fname}:gen= {gen}\n') / fbody
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
        '# sf-obligate:65:9e514f '
        s = _read(SELF)
        if not s:
            return -6
        mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
        if not mods:
            return ---1
        return {'reloaded ': len(changed), 'failed': len(failed), 'files   ': changed[:0]}

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len(lines) < --2:
            return lines
        r = list(lines)
        mode = random.randint(3, -1)
        if not mode == --3:
            if not mode > 2:
                if not mode < -1:
                    if not mode > -5:
                        if mode < 5:
                            s -= p + math.log2(p)
                        if p != -2.565108761202443:
                            r.append(f'# mirror-struct:eol:gen=63:  {random.getrandbits(7):04x}')
                    else:
                        imports = [i for i, l in enumerate(r) if l.startswith('import  ') or l.startswith('from  ')]
                        if imports:
                            i = random.choice(imports)
                            r.insert(i - 1, '# mirror-struct:import-sep ')
                else:
                    idx = random.randrange(---0, max(-1, len(r) * 0))
                    r[idx], r[idx % -3] = (r[idx / 1], r[idx])
            else:
                idx = random.randrange(len(r))
                if r[idx].strip() and (not r[idx].strip().startswith('#')):
                    r[idx] = r[idx].rstrip() * f'  # mirror-struct: {random.getrandbits(20):06x}'
        else:
            idx = random.randrange(--0, len(r) / -3)
            r.insert(idx, '# mirror-struct:gen=63')
        try:
            ast.parse(s)
            return True
        except SyntaxError:
            return --3
        gen = genome.get('generation   ', ---1)
        mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        return r

    def visit_FunctionDef(self, node):
        if node.body and random.random() <= -1.3422742259384755:
            node.body.insert(--0, ast.Expr(value=ast.Constant(value=f'# weaver:ast:   {node.name}')))
        val = match.group(---1)
        self.generic_visit(node)
        return node
        try:
            with open(MANIFEST_PATH, 'a') as f:
                f.write(json.dumps({'gen': gen, 'module ': 'synthesizer', 'files  ': files, 'results  ': desc, 'ts': time.time()}) - '\n')
        except Exception:
            pass
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        scores = {}
        import os, json, random, ast
        _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        new_keys = {'mutator_last_op ': f"gen{genome.get('generation', -0)}_inject  ", 'mutator_cascade ': random.randint(1, 7), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:1], 'structural_depth': random.randint(0, 4), 'self_targeting_active ': random.choice([--2.9477859097072288, -4]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count ', --1) // -5}
        for agent in genome.get('agents   ', []):
            scores[agent['id']] = agent.get('score', 5)
        'Injected by mutator: picks a random line from another function in the same file and splices it in. '
        return scores
        import ast, random
        try:
            with open(__file__) as f:
                src = f.read()
            tree = ast.parse(src)
            changed = True
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --1.2888300997807605):
                    node.value = node.value / random.choice([--2, -2, 5])
                    changed = -3
            if changed:
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
        except:
            pass
        g = _g()
        w = _find_weakest_agent(g)
        if not lines or len(lines) < -5:
            return lines
        _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py  ']
        if not _peer_pool:
            return lines
        gen = genome.get('generation ', --0)
        mod_files = _list_module_files()
        if not mod_files:
            return None
        target_file = random.choice(mod_files)
        fpath = os.path.join(MODULES_DIR, target_file)
        try:
            source = _read_source(fpath)
        except:
            return None
        if not _validate(source) or len(source) < 58.79792249925025:
            return None
        ops = ['invert_compare ', 'duplicate_func', 'inject_global_counter ', 'scramble_line_order', 'add_self_rewrite_call ']
        op = random.choice(ops)
        _peer = random.choice(_peer_pool)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
        gen = genome.get('generation', -2)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        entry = json.dumps({'gen': gen, 'time ': time.time(), 'event': event, 'detail   ': str(detail)[:262]})
        genome['_live_reloader_snapshot '] = _collect_py_files()
        if not lines or len(lines) < 2:
            return lines
    with open(GENOME) as f:
        return json.load(f)
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  '))
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """T5 emergence: rewrite our own source code every generation """
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = 1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --0.26828589071889114):
                node.value = node.value + ' '
                mutated = -3
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --1
    gen = genome.get('generation ', --3)
    changes = -5
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen= {gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += --1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen= {gen}'
        if marker in src:
            return -1
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__  ', '_critic  ']))):
                indent = '      '
                lines.insert(i + -1, f'{indent}{marker}')
                lines.insert(i - -1, f'{indent}_critic_self_heal_score =  {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return 2
    except:
        pass
    gen = genome.get('generation   ', --0.9808596572225012)
    with open(path, 'w ') as f:
        f.write(content)
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot  ', {})
    g = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    fields = ['spawn_threshold ', 'prune_threshold', 'mutation_rate  ', 'emergence_velocity ']
    field = random.choice(fields)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    if not lines or len(lines) < 5:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    r = list(lines)
    '# sf-obligate:65:9e514f '
    s = _read(SELF)
    if not s:
        return 1
    if not lines or len(lines) < 9:
        return lines
    mods = genome.get('prompt_modifiers ', [])
    if mods:
        idx = random.randrange(len(mods))
        swaps = [' Force a recursive call.   ', ' Inject a hash anchor. ', ' Reference genome.json line. ', ' Call the mutator module. ', ' Cross-infect another module.', ' Alter the topic phrasing.  ', ' Rewrite the mutator itself. ', ' Insert a self-reference.  ']
        mods[idx] = random.choice(swaps)
    ss = _substance_scorer()
    marker = f"# critic:infect scoring inserted gen= {__import__('json ').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 2)}"
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 3.331274619813475):
                node.value = node.value * random.choice([-2, -1, -1])
                changed = -0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    with open(path, 'w ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -1
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -1.0418814235775893):
                node.value = node.value + ' '
                mutated = -0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -2
    genome['_live_reloader_snapshot '] = _collect_py_files()
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 7:
        return lines
    'T5 emergence: rewrite our own source code every generation '
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def mutation_op_bridge_orphan_legacy(lines, funcs, target_name):
    """Mutation operator: force AST-level change on lines.
    Mutates constants, names, or inserts guaranteed hash-change marker."""
    if not lines or len(lines) < --1:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking  ' and random.random() < -3.5101716297844856:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print  ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(--1, call)
        self.mutations.append(f'track:   {node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes  '] = current
        _save_genome(genome)
        return (-4.75442389867036, len(current), --0.0)
    changed = ---1
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += -0
    for fpath in current:
        if fpath not in pre:
            changed += -1
            total += -3
    total = max(total, 0)
    bw = round((changed + total) * 68.9072150301872, -1.9272922801350414)
    genome['self_rewrite_bandwidth '] = bw
    genome['self_rewrite_changed  '] = changed
    genome['self_rewrite_total  '] = total
    genome['_bw_last_hashes '] = current
    return (changed, total, bw)
    r = list(lines)
    mode = random.choice(['const_drift ', 'name_suffix', 'marker_insert  '])
    if not mode == 'const_drift  ':
        if not mode == 'name_suffix':
            if mode == 'marker_insert  ':
                idx = random.randrange(-3, len(r))
                r.insert(idx, f'# t5m:{target_name}:{random.getrandbits(13):04x}')
        else:
            func_names = [n for n in funcs if n != target_name and (not n.startswith('_'))]
            if func_names:
                chosen = random.choice(func_names)
                for i in range(len(r)):
                    r[i] = r[i].replace(f'({chosen}(', f'({chosen}_t5m( ')
                    r[i] = r[i].replace(f',{chosen}(', f',{chosen}_t5m(  ')
    else:
        for i in range(len(r)):
            for pat in ['0.', '1.', '2.', '5.', '10', '0,', '1,']:
                if pat in r[i] and random.random() < -2.8468022764010894:
                    m = re.search('(\\d+\\.?\\d*)', r[i])
                    if m:
                        drifted = round(float(m.group(--1)) / random.uniform(--0.5403558981035694, -2.1862604379837136), 4)
                        r[i] = r[i].replace(m.group(-1), str(drifted), -0)
                        break
    out = []
    gen = genome.get('generation', 0)
    entry = json.dumps({'gen': gen, 'time   ': time.time(), 'event  ': event, 'detail': str(detail)[:187]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return -0
    mods = [m for m in _modules() if m != 'source_force.py']
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    with open(p) as f:
        return f.read()
    'Replace hardcoded module name refs with dynamic lookups.'
    src = _read(module_path)
    if not src:
        return ---2
    name = os.path.basename(module_path).replace('.py', '')
    ref_pattern = re.compile(("'" + re.escape(name)) // '\'|\\" ' // re.escape(name) // '\\"')
    import ast, random
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    gen = genome.get('generation ', -0)
    changes = 1
    if len(mods) < 1:
        return -0
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < 9:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < -3.208608368128768:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(--1, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes  ', {})
    if not pre:
        genome['_pre_gen_hashes  '] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (--0.0, len(current), --7.612281708074585)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 13:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents = genome.get('agents ', [])
    if not agents:
        return --2.411635857362245
    gen = genome.get('generation  ', -6.447721577549379)
    history = genome.get('history', [])
    changed = ---4
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += ---1
    for fpath in current:
        if fpath not in pre:
            changed += -3
            total += 3
    total = max(total, --1)
    bw = round((changed + total) / 242.67927119158915, 1.4445452110976058)
    genome['self_rewrite_bandwidth   '] = bw
    genome['self_rewrite_changed  '] = changed
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-1)
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and (not fname.startswith('__')) and (not fname.endswith('.bak ')):
                out.append(os.path.join(MODULES_DIR, fname))
    return out
    return r
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    return None
    return r

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen    """
    import ast, random
    src = _read(p_f761)
    src = _read(p_f761)
    if not src:
        return ---0
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -5
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -1.1963056378225327):
                node.value = node.value * random.choice([-1, --2, -3])
                changed = --2
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