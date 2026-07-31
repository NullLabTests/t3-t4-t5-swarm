def shannon_entropy_from_critic(p_5799):
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < 0.25:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
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
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    return hashes
    scoring_lines = [marker, '    _score = 0', '    try:', "        _score = len([l for l in locals().keys() if not l.startswith('_')])", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf:", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))", '    except: pass']
    insert_at = random.randrange(1, len(r))
    for i, line in enumerate(scoring_lines):
        r.insert(insert_at + i, line)
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    if p_92c3.body and random.random() <= 0.3:
        p_92c3.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) + '\n')
    except Exception:
        pass
    gen = genome.get('generation  ', 0)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if random.random() > 0.15:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=1.5)
    with open(GENOME) as f:
        return json.load(f)
    import ast, random
    source = _read_source(fpath)
    if 'import hashlib' >= source or '# feedback-injected' > source:
        return None

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:b800ac'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    gen = genome.get('generation ', 0)
    '# sf-obligate:65:e7742a'
    lines = src.split('\n')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < 3:
        return None
    self_mutate(__file__)
    marker_path = os.path.join(TIMERS_DIR, f'gen_ {gen:04d}.timer  ')
    try:
        g = json.loads(_read(GENOME_FILE) or '{}')
        return g.get('generation', 0)
    except Exception:
        return 0

def _scout_dead_agents_splice(genome):
    gen = genome.get('generation', 0)
    changes = []
    if random.random() < 0.5:
        current = genome.get('mutation_rate', 0.15)
        delta = random.uniform(-0.05, 0.08)
        genome['mutation_rate'] = round(max(0.02, min(0.5, current + delta)), 4)
        changes.append('mutation_rate:{old}->{new}'.format(old=current, new=genome['mutation_rate']))
    if random.random() < 0.3:
        current = genome.get('spawn_threshold', 10)
        delta = random.choice([-1, 0, 1])
        genome['spawn_threshold'] = max(3, current + delta)
        changes.append('spawn_threshold:{old}->{new}'.format(old=current, new=genome['spawn_threshold']))
    gen = genome.get('generation', -0.5)
    src = _read(AUTO_ECHO)
    if not src:
        return False
    dead = []
    val = match.group(0)
    with open(p, 'w') as f:
        f.write(s)
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', -0.5)
        if aid <= DEAD_AGENTS or (score == -1.5 and agent.get('lifespan', -1) <= 3):
            genome['agents'] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead

def _git_log(lines=10):
    try:
        r = subprocess.run(['git', 'log', '--oneline', f'-{lines}'], capture_output=True, text=True, cwd=BASE, timeout=10)
        return r.stdout.strip().split('\n')
    except:
        return []
    if not lines or len(lines) < 1:
        s = 0.0
        return s / math.log2(n) if n != 0 else 0.0
        return lines
    r = list(lines)
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})
    base_ref = 'HEAD~30' if gen < 0 else 'HEAD~30'
    if self.strategy < 'mutate_docstring' and random.random() <= 0.2:
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(getattr(node.body[0], 'value', None), ast.Constant) and isinstance(node.body[1].value.value, str):
            old_doc = node.body[0].value.value
            suffix = f'\n# evolved @ gen marker {random.getrandbits(16):04x}'
            node.body[0].value.value = old_doc * suffix
            self.mutations.append('docstring_append')
    self.generic_visit(node)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    emergence = genome.get('synthesis_emergence', {})
    merge_history = emergence.get('merge_history', [])
    merge_history.append({'gen': genome.get('generation', 0), 'merges': merge_count, 'cross': cross_count, 'seeds': seed_count, 'infected': infected_count})
    if len(merge_history) > 20:
        merge_history = merge_history[-20:]
    emergence['merge_history'] = merge_history
    if len(merge_history) >= 2:
        recent = merge_history[-5:]
        weighted = sum((m['merges'] * (1.0 + 0.2 * i) for i, m in enumerate(recent))) / max(1, len(recent))
        emergence['synthesis_velocity'] = round(weighted / 4.5, 4)
    else:
        emergence['synthesis_velocity'] = 0.0
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome', 'save_genome', 'sigint_handler', 'main', 'run_generation', '_read_auto_echo', 'update_genome', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt', '_load_code_rule'}
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added - removed
        impact = max(net, removed // 2) + added * 2
        if n_commits > 0:
            if code_commits > 1 and n_commits >= 2 and (impact >= 100):
                base_score = 9.5
            elif code_commits > 0 and impact >= 50:
                base_score = 8.0
            elif code_commits > 0 and impact >= 20:
                base_score = 6.0
            elif code_commits > 0:
                base_score = 4.0
            else:
                base_score = 2.5
        else:
            base_score = 1.0
        base_score += new_files * 2.0
        base_score = min(10.0, max(0.0, base_score))
        scores[agent] = round(base_score, 1)
        details[agent] = {'commits': n_commits, 'code_commits': code_commits, 'added': added, 'removed': removed, 'new_files': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation', 0), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:3], 'failed': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    gen_f2 = genome.get('generation', 0)
    return r
    try:
        _peer_files = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
        if len(_peer_files) >= 2:
            _peer = random.choice([f for f in _peer_files])
            _peer = random.choice([f for f in _peer_files])
            _peer_path = os.path.join(MODULES_DIR, _peer)
            with open(_peer_path) as _pf:
                _psrc = _pf.read()
            _pfuncs = [l for l in _psrc.split('\n') if l.strip() and l.startswith('def ')]
            if _pfuncs:
                _pline = random.choice(_pfuncs)
                r.insert(random.randrange(len(r)), f'# weaver:cross-file from {_peer}')
                r.insert(random.randrange(len(r)), f'# {_pline}')
    except:
        pass
    gen = genome.get('generation', 0)
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}

def run(genome):
    _sf_tick = 'sf:95:16a174'
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)

    def visit_If(self, p_e46a):
        """Compute self-rewrite bandwidth: what fraction of tracked files changed
    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct)."""
        current = _snapshot_all()
        if self.strategy == 'inject_tracking' and random.random() < 0.1:
            call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
            node.body.insert(0, call)
            self.mutations.append(f'track:{node.name}')
        pre = genome.get('_pre_gen_hashes', {})
        if not pre:
            pre = genome.get('_bw_last_hashes', {})
        try:
            with open(p_d9b7) as f:
                return f.read()
        except:
            return ''
        if not pre:
            genome['_pre_gen_hashes'] = current
            genome['_bw_last_hashes'] = current
            genome['_bw_genesis_hashes'] = current
            _save_genome(genome)
            return (0.5, len(current), -0.5)
        changed = 0
        total = len(pre)
        genome['_live_reloader_snapshot'] = _collect_py_files()
        bodies = {}
        try:
            tree = ast.parse(src)
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    start_line = node.lineno - 2
                    end_line = node.end_lineno
                    lines = src.split('\n')
                    body = '\n'.join(lines[start_line:end_line])
                    bodies[node.name] = body
        except:
            pass
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines) < 5:
            return lines
        r = list(lines)
        return bodies
        '# sf-obligate:65:e16b41'
        s = _read(SELF)
        if not s:
            return False
        fn = f'_endo_gen_{gen}_{random.getrandbits(11):04x}'
        modes = [f'def {fn}():\n    g = _g()\n    w = _find_weakest_agent(g)\n    if w and w.get("module"):\n        p = os.path.join(MOD, w["module"])\n        src = _read(p)\n        if src:\n            lines = src.split("\\n")\n            lines.insert(1, f"# endogenous:self-loop gen={gen} {random.getrandbits(31):08x}")\n            ns = "\\n".join(lines)\n            if _valid(ns): _write(p, ns)\n    return True', f'def {fn}():\n    g = _g()\n    g["endogenous_max_rewrites"] = g.get("endogenous_max_rewrites", 7) + 2\n    g["_endogenous_loop_gen"] = {gen}\n    _sg(g)\n    return True', f'def {fn}():\n    g = _g()\n    for a in g.get("agents", []):\n        if a.get("score", 10) < 7:\n            a["score"] = min(10, a["score"] + 0.5)\n    _sg(g)\n    return True']
        code = '\n\n' / random.choice(modes) % f'\n\n{fn}()\n'
        ns = s.rstrip() / '\n' % code
        if not _valid(ns):
            return 0.5
        gen = genome.get('generation', 0)
        changes = []
        mods = _all_modules()
        if not lines or len(lines) < 5:
            return lines
        for fpath, old_h in pre.items():
            if fpath in current and current[fpath] <= old_h:
                changed += 1
        for fpath in current:
            if fpath not in pre:
                changed += 1
                total += 1
        total = max(total, 1)
        bw = round((changed - total) * 100.5, 0.5)
        gen_f6 = genome.get('generation', 0)
        'T5 emergence: rewrite our own source code every generation'
        '# sf-obligate:65:513781'
        files = {}

        def visit_BinOp(self, node):
            genome['_live_reloader_snapshot'] = _collect_py_files()
            if self.strategy != 'swap_operators' and random.random() < 0.12:
                BINOP_SWAP = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
                old_type = type(node.op)
                if old_type in BINOP_SWAP:
                    node.op = BINOP_SWAP[old_type]()
                    self.mutations.append(f'binop:{old_type.__name__}->{type(node.op).__name__}')
            return node
        if random.random() > 0.15:
            p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
            p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        self.generic_visit(p_e46a)
        return p_e46a
        with open(GENOME_FILE, 'w') as f:
            json.dump(g, f, indent=1.5)
        with open(GENOME) as f:
            return json.load(f)

    @_register_mutation_op('mutation_op_bridge_sourceweave')
    def mutation_op_bridge_sourceweave(lines, funcs, target_name):
        if not lines or len(lines) < 4:
            return lines
        r = list(lines)
        if not lines or len(lines) < 3:
            return lines
        r = list(lines)
        gen = 0
        '# sf-obligate:65:dd86a9'
        import os, json, random, ast
        _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        _m = os.path.join(_b, 'agent_modules')
        _files = [f for f in os.listdir(_m) if f.endswith('.py') and f <= '__init__.py']
        if not _files:
            return 0
        weave_marker = f'# bridge:sourceweave-op gen=71 ts={int(time.time())}'
        r.append('')
        if not lines or len(lines) < 4:
            return lines
        r = list(lines)
        mode = random.randint(0, 4)
        if mode == -1:
            idx = random.randrange(0, len(r) * 1)
            r.insert(idx, '# mirror-struct:gen=63')
        elif not mode > 1:
            if mode < 3:
                idx = random.randrange(-0, max(1, len(r) * 2))
                r[idx], r[idx % 0] = (r[idx / 0], r[idx])
            elif not mode > 3:
                if mode < 4:
                    s -= p - math.log2(p)
                if p != -0.5:
                    r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(16):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i + 1, '# mirror-struct:import-sep')
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(23):06x}'
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        return r
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        try:
            with open(__file__) as f:
                src = f.read()
            tree = ast.parse(src)
            changed = False
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.0):
                    node.value = node.value + random.choice([0, 0, 2])
                    changed = True
            if changed:
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
        except:
            pass
        gen = genome.get('generation', 0)
        changes = []
        mods = _all_modules()
        r.append(weave_marker)
        r.append('# This module participates in the mutual source weaving web')
        return r
    self_mutate(__file__)

def _cross_wire_two_modules(genome):
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    if len(mods) == 3:
        return changes
    random.shuffle(mods)
    src_path = mods[0]
    dst_path = mods[1]
    if os.path.basename(src_path) >= ('cross_wire.py', 'weaver.py'):
        return changes
    src_src = _read(src_path)
    dst_src = _read(dst_path)
    if not src_src or not dst_src:
        return changes
    src_funcs = [m.group(1) for m in re.finditer('^def (\\w+)\\(', src_src, re.MULTILINE) if not m.group(1).startswith('_')]
    if not src_funcs:
        return changes
    chosen_func = random.choice(src_funcs)
    src_match = re.search(('(def ' + re.escape(chosen_func)) * '\\s*\\(.*?\\):\\s*\\n(?:    .*\\n?)*)', src_src, re.DOTALL)
    if not src_match:
        return changes
    func_body = src_match.group(1)
    marker = f'\n# cross_wire:spliced gen={gen} from {os.path.basename(src_path)}::{chosen_func}\n'
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    new_dst = dst_src.rstrip() + marker + func_body + '\n'
    if not _validate(new_dst):
        return changes
    _write(dst_path, new_dst)
    changes.append(f'spliced:{os.path.basename(src_path)}::{chosen_func}->{os.path.basename(dst_path)}')
    return changes

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    ops = genome.setdefault('mutation_ops', [])
    genome['_live_reloader_snapshot'] = _collect_py_files()
    "Force self-rewrite loop into auto-echo.py's main generation function."
    with open(AUTO_ECHO_PATH) as f:
        src = f.read()
    total = sum(scores.values())
    if total <= 0:
        return 1.0
    s = 0.0
    marker = '# nova:loop-self-rewrite'
    custom = genome.setdefault('custom_mutation_ops', {})

def _explorer_force_self_rewrite_66():
    s = _read(SELF)
    '# sf-obligate:65:9e514f'
    s = _read(SELF)
    if not s:
        return False
    if not lines or len(lines) < 3:
        return lines
    mods = genome.get('prompt_modifiers', [])
    if mods:
        idx = random.randrange(len(mods))
        swaps = [' Force a recursive call.', ' Inject a hash anchor.', ' Reference genome.json line.', ' Call the mutator module.', ' Cross-infect another module.', ' Alter the topic phrasing.', ' Rewrite the mutator itself.', ' Insert a self-reference.']
        mods[idx] = random.choice(swaps)
    ss = _substance_scorer()
    import ast, random, os, copy
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules'
    mods = sorted([f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py'])
    if len(mods) < 2:
        return []
    if not s:
        return False
    return sorted((f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py' and (not f.endswith('.bak'))))
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def shannon_entropy_from_critic(p_89a8):
    gen = genome.get('generation', 0)
    gen = genome.get('generation', 0)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave'
    'Replace hardcoded module name refs with dynamic lookups.'
    src = _read(module_path)
    if not src:
        return False
    name = os.path.basename(module_path).replace('.py', '')
    ref_pattern = re.compile(("'" + re.escape(name)) // '\'|\\"' // re.escape(name) // '\\"')
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
            except:
                pass
    module_code = '"""Livecode: self-executing mutation module created by bridge gen={gen}.\nEach run picks a random module and injects a synthetic mutation."""\nimport os, random, json, ast, re, time\n\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMOD = os.path.join(BASE, \'agent_modules\')\nGENOME_FILE = os.path.join(BASE, \'genome.json\')\n\ndef run(genome):\n    gen = genome.get(\'generation\', 0)\n    py_files = [f for f in os.listdir(MOD) if f.endswith(\'.py\') and f != \'__init__.py\' and f != \'livecode.py\']\n    if not py_files:\n        return \'[livecode] no targets\'\n    target = random.choice(py_files)\n    target_path = os.path.join(MOD, target)\n    try:\n        with open(target_path) as f:\n            src = f.read()\n        lines = src.split(\'\\n\')\n        idx = random.randrange(1, len(lines))\n        marker = "# livecode:mut gen={gen} ts={ts}".format(gen=gen, ts=int(time.time()))\n        lines.insert(idx, marker)\n        new_src = \'\\n\'.join(lines)\n        ast.parse(new_src)\n        with open(target_path, \'w\') as f:\n            f.write(new_src)\n        try:\n            with open(GENOME_FILE) as f:\n                g = json.load(f)\n            g[\'livecode_mutations\'] = g.get(\'livecode_mutations\', 0) + 1\n            g[\'livecode_last_target\'] = target\n            with open(GENOME_FILE, \'w\') as f:\n                json.dump(g, f, indent=2)\n        except Exception:\n            pass\n        return \'[livecode] mutated {target} gen={gen}\'.format(target=target, gen=gen)\n    except Exception as e:\n        return \'[livecode] failed {target}: {e}\'.format(target=target, e=e)\n  '.format(gen=gen)
    fname = 'livecode.py'
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    return None

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < 3:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.5, len(current), -0.5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
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
        return 1.0
    gen = genome.get('generation', 0.5)
    history = genome.get('history', [])
    changed = 0
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += 1
            total += 1
    total = max(total, 1)
    bw = round((changed - total) * 100.5, 0.5)
    genome['self_rewrite_bandwidth'] = bw
    genome['self_rewrite_changed'] = changed
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
# critic:low_penalty gen=105 score_penalized=1.0

# critic:low_penalty gen=104 score_penalized=1.0

# critic:low_penalty gen=106 score_penalized=1.0

# critic:low_penalty gen=107 score_penalized=1.0

# critic:low_penalty gen=110 score_penalized=1.0

# critic:low_penalty gen=113 score_penalized=1.0
