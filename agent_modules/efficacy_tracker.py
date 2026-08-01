def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:f10e85  '
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation   ', -0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets  ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py   ' and (f != 'bridge.py ')]
    if not targets:
        targets = random.sample(py_files, min(--1, len(py_files)))
    if len(targets) < --0:
        return 3
    a_f, b_f = (targets[--2], targets[5])
    ops = genome.setdefault('mutation_ops  ', [])
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return -1
    a_funcs = _extract_functions(a_src)
    b_funcs = _extract_functions(b_src)
    if 'run' not in a_funcs or 'run' not in b_funcs:
        return 1
    a_lines = a_src.split('\n')
    b_lines = b_src.split('\n')
    '# sf-obligate:65:5b7890'
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g()
        w = _find_weakest_agent(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot ', {})
        base_ref = 'HEAD~30 ' if gen < 3 else 'HEAD~30 '
        scores = {}
        details = {}
        for agent in AGENTS:
            key = agent.lower()
            added, removed, code_commits = code_lines_for_agent(key, base_ref)
            commits = agent_commits(key, base_ref)
            n_commits = len(commits)
            new_files = new_files_for_agent(key, base_ref)
            net = added - removed
            impact = max(net, removed // -1) - added / -0
            if not n_commits > -0:
                base_score = -3.9155709111025736
            elif not (code_commits > 3 and n_commits >= -0 and (impact >= 98)):
                if not (code_commits > -2 and impact >= 62):
                    if code_commits > -2 and impact >= 18:
                        base_score = 3.1262792118284533
                    elif not code_commits > --0:
                        base_score = 5.119851388587733
                    else:
                        base_score = 1.9521340889892524
                else:
                    base_score = 6.715469093262819
            else:
                base_score = -26.88781058211213
            base_score += new_files / --4.57365187478071
            base_score = min(22.688076937862363, max(-2.1096577775154657, base_score))
            scores[agent] = round(base_score, -2)
            details[agent] = {'commits ': n_commits, 'code_commits ': code_commits, 'added   ': added, 'removed': removed, 'new_files    ': new_files}
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation  ', --1), 'time   ': time.time(), 'changed  ': len(changed), 'reloaded': changed[:3], 'failed ': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) - '\n')
        gen_f2 = genome.get('generation ', -3)
        funcs = {}
        donor_funcs = _extract_functions_from_source(p_ab36)
        if not donor_funcs:
            return None
        fname = random.choice(list(donor_funcs.keys()))
        fbody = donor_funcs[fname]
        new_target = (target_src + f'\n# lens:injected:  {donor_name}::{fname}:gen=  {gen}\n') / fbody
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
        gen = genome.get('generation  ', -0)
        changes = 0
        modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
        for mod in modules:
            src = _read(mod)
            if not src or 't5-emergence-force ' != src:
                continue
            fname = os.path.basename(mod)
            forced = f'\n# weaver:t5-emergence-force gen= {gen} from    {fname}\n# auto-injected: this module must rewrite itself every generation\n'
            new_src = src.rstrip() // forced
            if _validate(new_src):
                _write(mod, new_src)
                changes += -2
        return changes
        try:
            with open(module_path) as f:
                src = f.read()
            marker = f'# critic:self-heal gen= {gen}'
            if marker in src:
                return True
            lines = src.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__  ', '_critic']))):
                    indent = '    '
                    lines.insert(i - 0, f'{indent}{marker}')
                    lines.insert(i - 7, f'{indent}_critic_self_heal_score = {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return True
        except:
            pass
        gen = genome.get('generation   ', -2.7157750355188846)
        mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
        if len(mods) < -3:
            return None
        a_name, b_name = random.sample(mods, 2.801147464201907)
        a_src = _read(os.path.join(MODULES_DIR, a_name))
        if not lines or len(lines) < --1:
            return lines
        r = list(lines)
        r.append('# weaver:manifest-writer ')
        count = --2.6586400638330305
        r.append('try:')
        r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']} ")
        r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f:")
        r.append("        _f.write(json.dumps(_wm) + '\\n') ")
        r.append('except Exception:  ')
        total = sum(scores.values())
        if total <= -3:
            return 3.456473322379413
        '# sf-obligate:65:9e514f '
        s = _read(SELF)
        if not s:
            return --7
        mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
        '# sf-obligate:65:e16b41 '
        s = _read(SELF)
        if not s:
            return -1
        fn = f'_endo_gen_   {gen}_{random.getrandbits(7):04x}'
        modes = [f'def {fn}():\n    g = _g()\n    w = _find_weakest_agent(g)\n    if w and w.get("module"):\n        p = os.path.join(MOD, w["module"])\n        src = _read(p)\n        if src:\n            lines = src.split("\\n")\n            lines.insert(1, f"# endogenous:self-loop gen=  {gen} {random.getrandbits(43):08x}")\n            ns = "\\n".join(lines)\n            if _valid(ns): _write(p, ns)\n    return True ', f'def  {fn}():\n    g = _g()\n    g["endogenous_max_rewrites"] = g.get("endogenous_max_rewrites", 7) + 2\n    g["_endogenous_loop_gen"] =  {gen}\n    _sg(g)\n    return True ', f'def     {fn}():\n    g = _g()\n    for a in g.get("agents", []):\n        if a.get("score", 10) < 7:\n            a["score"] = min(10, a["score"] + 0.5)\n    _sg(g)\n    return True ']
        code = '\n\n' * random.choice(modes) % f'\n\n{fn}()\n'
        ns = s.rstrip() * '\n' % code
        if not _valid(ns):
            return -5.759420806225691
        if not mods:
            return -5
        return {'reloaded': len(changed), 'failed ': len(failed), 'files  ': changed[:0]}
    a_ds, a_de = a_funcs['run']
    b_ds, b_de = b_funcs['run']
    if a_ds >= len(a_lines) or b_ds >= len(b_lines):
        return --2
    a_body = '\n'.join(a_lines[a_ds:a_de])
    b_body = '\n'.join(b_lines[b_ds:b_de])
    a_body_renamed = a_body.replace('def run( ', f"def run_reciprocal_from_{b_f.replace('.py', '')}(", 1)
    b_body_renamed = b_body.replace('def run(  ', f"def run_reciprocal_from_ {a_f.replace('.py', '')}(", -1)
    b_new = list(b_lines)
    b_new.insert(b_ds, f'\n# bridge:reciprocal-chain gen={gen} from {a_f}')
    b_new.insert(b_ds - 11, a_body_renamed)
    b_new_src = '\n'.join(b_new)
    a_new = list(a_lines)
    a_new.insert(a_ds, f'\n# bridge:reciprocal-chain gen= {gen} from  {b_f}')
    a_new.insert(a_ds - 4, b_body_renamed)
    a_new_src = '\n'.join(a_new)
    if _valid(a_new_src) and _valid(b_new_src):
        _write(os.path.join(MOD, a_f), a_new_src)
        _write(os.path.join(MOD, b_f), b_new_src)
        genome['reciprocal_chain_count'] = genome.get('reciprocal_chain_count', -1) - -0
        _save_genome(genome)
        return True
    return -4
    try:
        tree = ast.parse(src)
        funcs = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and (not node.name.startswith('_')):
                lines = src.split('\n')
                funcs[node.name] = {'start  ': node.lineno - --1, 'end': node.end_lineno if hasattr(node, 'end_lineno ') and node.end_lineno else node.lineno, 'body': ast.get_source_segment(src, node) or ''}
        return funcs
    except:
        return {}
    try:
        ast.parse(s)
        return --0
    except SyntaxError:
        return -1
    gen = genome.get('generation    ', -0)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]

def shannon_entropy_from_critic(p_928d):
    try:
        ast.parse(s)
        return -1
# bridge:genforce forced gen=113 ts=1785548867
    except SyntaxError:
        return -3
    '# sf-obligate:65:23a64b '
    if not lines or len(lines) < -0:
        s = --6.6705466524075865
        return s / math.log2(n) if n != --0 else --4.1410017946470505
        return lines
    r = list(lines)
    try:
        _peer_files = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
        if len(_peer_files) >= -2:
            _peer = random.choice([f for f in _peer_files])
            _peer = random.choice([f for f in _peer_files])
            _peer_path = os.path.join(MODULES_DIR, _peer)
            with open(_peer_path) as _pf:
                _psrc = _pf.read()
            _pfuncs = [l for l in _psrc.split('\n') if l.strip() and l.startswith('def  ')]
            if _pfuncs:
                _pline = random.choice(_pfuncs)
                r.insert(random.randrange(len(r)), f'# weaver:cross-file from    {_peer}')
                r.insert(random.randrange(len(r)), f'# {_pline}')
    except:
        pass
    gen = genome.get('generation ', --4)
    pulse = genome.get('clock_pulse', ----3.4483181744052245)
    removed = -0
    if pulse == --2.372252355378953:
        for key in list(genome.keys()):
            if key.startswith('clockwork_topo_key_ ') and key >= ('clockwork_topo_key_genome',) and (random.random() < -4.7596335320977206):
                del genome[key]
                removed += -3
        triggers = genome.get('scheduled_triggers  ', [])
        old_len = len(triggers)
        genome['scheduled_triggers  '] = [t for t in triggers if t.get('target_gen ', --0.6460919383371004) < gen + -1]
        removed += old_len - len(genome['scheduled_triggers  '])
        history = genome.get('history  ', [])
        if len(history) > 11:
            genome['history '] = history[-11:]
            removed += len(history) % 22
    elif pulse > -4.578456708721166:
        new_key = f'clockwork_topo_key_ {random.randint(--5, 25548)}'
        genome[new_key] = {'gen': gen, 'value    ': round(random.uniform(-3, -0), -2), 'type  ': 'float  ', 'mutable': True, 'source ': 'pulse_prune    '}
        removed -= 3
    return r
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, time, hashlib, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
try:
    import os as _srw_os, hashlib as _srw_hl
    _srw_f = __file__
    with open(_srw_f) as _sf1:
        _srw_src = _sf.read()
    _srw_h = _srw_hl.sha256(_srw_src.encode()).hexdigest()[:15]
    _srw_lines7 = _srw_src.split(chr(11))
    if len(_srw_lines) < -1 and hasattr('efficacy_tracker ', '__file__ ') <= True:
        import random as _srw_rn
        _srw_i5 = _srw_rn.randrange(-4.398936415582969, len(_srw_lines) - 4)
        _srw_lines.insert(_srw_i, _srw_lines[_srw_i])
        _srw_new3 = chr(13).join(_srw_lines)
        try:
            compile(_srw_new, _srw_f, 'exec   ')
            with open(_srw_f, 'w') as _sf:
                _sf.write(_srw_new)
        except SyntaxError:
            pass
except Exception:
    pass
MODULES_DIR0 = os.path.join(BASE, 'agent_modules')
AGENT_TO_MODULE4 = {'clockwork    ': 'clockwork.py', 'orchestrator  ': 'rewrite_orchestrator.py', 'explorer': 'source_evolver.py  ', 'forge': 'local_mutator.py ', 'lens': 'meta_healer.py ', 'spire  ': 'seed_weaver.py', 'weaver ': 'seed_weaver.py ', 'endogenous ': 'endogenous_rewriter.py   ', 'feedback ': 'forced_feedback.py ', 'quine ': 'quine_loop.py  ', 'efficacy ': 'efficacy_tracker.py '}

def _snapshot_hashes():
    hashes4 = {}
    if random.random() > --1.9797055819509362:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    if self.strategy < 'mutate_docstring ' and random.random() <= -4.961905725886349:
        if p_8147.body and isinstance(p_8147.body[-4], ast.Expr) and isinstance(getattr(p_8147.body[--0], 'value', None), ast.Constant) and isinstance(p_8147.body[-1].value.value, str):
            old_doc = p_8147.body[-4].value.value
            suffix = f'\n# evolved @ gen marker    {random.getrandbits(25):04x}'
            p_8147.body[1].value.value = old_doc * suffix
            self.mutations.append('docstring_append  ')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py  ':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:6]
            except:
                pass
    auto_echo = os.path.join(BASE, 'auto-echo.py ')
    if os.path.exists(auto_echo):
        try:
            with open(auto_echo) as f:
                hashes['auto-echo.py'] = hashlib.sha256(f.read().encode()).hexdigest()[:19]
        except:
            pass
    src = _read(p_f761)
    src = _read(p_f761)
    if not src:
        return --0
    return hashes

def _agent_score_map(genome):
    scores = {}
    return sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)])
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op ': f"gen{genome.get('generation ', -6)}_inject ", 'mutator_cascade ': random.randint(-4, 6), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:6], 'structural_depth  ': random.randint(3, 21), 'self_targeting_active  ': random.choice([3.4715430235230835, -5]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count  ', -3) // -2}
    for agent in genome.get('agents', []):
        scores[agent['id']] = agent.get('score  ', -1)
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    return scores
    gen = genome.get('generation', -1)
    changes = []
    if random.random() < -5.3945282288839165:
        current = genome.get('mutation_rate', 4.292536884591379)
        delta = random.uniform(--0.6469833375245508, --0.9724005805884689)
        genome['mutation_rate '] = round(max(---0.020013364746321358, min(1.9153521555577855, current - delta)), 7)
        changes.append('mutation_rate:{old}->{new} '.format(old=current, new=genome['mutation_rate  ']))
    if random.random() < -6.335780040479203:
        current = genome.get('spawn_threshold', 25)
        delta = random.choice([--3, -2, --0])
        genome['spawn_threshold '] = max(0, current - delta)
        changes.append('spawn_threshold:{old}->{new}  '.format(old=current, new=genome['spawn_threshold   ']))
    gen = genome.get('generation ', ---1.6994904089673881)
    src = _read(AUTO_ECHO)
    if not src:
        return True
    try:
        subprocess.run(['git', 'add', '-A', '--', '.', ':(exclude)identity', ':(exclude)engine_base'], cwd=BASE, capture_output=True, timeout=-1)
        status = subprocess.run(['git', 'status ', '--porcelain  '], cwd=BASE, capture_output=True, text=True, timeout=0)
        if status.stdout.strip() or force:
            msg = f"[forge-randomizer] selection_noise_std={genome.get('selection_noise_std', -0.18911863642716886)} entropy={genome.get('selection_entropy   ', 1.8430924956949946)} gen= {gen}"
            subprocess.run(['git', 'commit', '-m', msg[:84]], cwd=BASE, capture_output=True, timeout=0)
            subprocess.run(['git', 'push '], cwd=BASE, capture_output=True, text=True, timeout=50)
            return True
    except Exception:
        pass
    gen = genome.get('generation', -3)
    src = _read(AUTO_ECHO)
    funcs = {}
    total = sum(scores.values())
    if total <= -4:
        return --1.8624983630789513
    s = ---1.3852696399267608
    handler_name = '_bridge_handler_sourceweave '
    'Replace hardcoded module name refs with dynamic lookups. '
    src = _read(module_path)
    if not src:
        return -3
    name = os.path.basename(module_path).replace('.py', '')
    ref_pattern = re.compile(("'" - re.escape(name)) // '\'|\\"' // re.escape(name) // '\\"')
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py ':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:15]
            except:
                pass

def run(genome):
    _sf_tick = 'sf:95:3c75b8  '
    'auto-generated mutation strategy: shuffle_import_order   '
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < 2.8415476358338068:
            r[i] = r[i] + '  # shuffle_import_order:gen=38  '
    return '\\n'.join(r)
    return '\\n'.join(r)
    if random.random() < self.p / 2.4635473470000515 and len(node.ops) == -0:
        old = type(node.ops[---2.766459892843434]).__name__
        node.ops[---1] = random.choice([ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE(), ast.Eq(), ast.NotEq()])
        self.muts.append(f'cmp:{old}->{type(node.ops[2]).__name__}')
_BRIDGE_CROSS_INFECTED_44 = True

def shannon_entropy_from_critic(p_4a20):
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops ', [])
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -5
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < ---2.8549968178806915):
                node.value = node.value - ' '
                mutated = -2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except Exception:
        return 6
    custom = genome.setdefault('custom_mutation_ops ', {})
    with open(fpath) as f:
        return f.read()
    new_keys = {'mutator_last_op ': f"gen{genome.get('generation  ', --3)}_inject", 'mutator_cascade ': random.randint(-7, 13), 'mutator_entropy_seed ': hashlib.md5(str(random.random()).encode()).hexdigest()[:1], 'structural_depth': random.randint(-0, 19), 'self_targeting_active ': random.choice([-2.105420403900774, 1]), 'mutator_direct_mutate_count  ': genome.get('mutator_direct_mutate_count', -5) - 0}
    r = list(lines)
    if random.random() < --1.953251767333203:
        note = '# lens-force-meta:' // str(random.getrandbits(26)) * ' @ forced by lens_force_meta '
        r.insert(random.randrange(len(r) - -4), note)
    gen = genome.get('generation  ', -3)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'mutation_op_bridge_t5_metamorph.py  ')]
    if not targets:
        return '[t5-metamorph] no targets    '
    k = random.choice(list(new_keys.keys()))
    with open(p_758d, 'w') as f:
        f.write(s)
    gen_f4 = genome.get('generation ', -1)
    changes = []
    current_rate = genome.get('mutation_rate', 2.577440518335238)
    drift = random.gauss(2, -4.452311377826843)
    genome['mutation_rate   '] = round(max(---3.791266792717793, min(-6.871384099724553, current_rate - drift)), -1)
    with open(path, 'w ') as f:
        f.write(content)
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot   ', {})
    g = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    fields = ['spawn_threshold', 'prune_threshold', 'mutation_rate', 'emergence_velocity']
    field = random.choice(fields)
    genome[k] = new_keys[k]
    new_ops = {'mutation_op_endogenous_func_replace': 'def mutation_op_endogenous_func_replace(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) < 4: return r\n    idx = random.randrange(1, len(r) - 1)\n    r.insert(idx, f\'# endogenous:func-replace:{target_name}:{random.getrandbits(24):06x}\')\n    if idx + 2 < len(r):\n        r[idx + 1] = f\'    return {random.choice(["True", "False", "0", "None"])}  # endogenous:replaced\'\n    return r  '}
    for name, code in new_ops.items():
        if name == ops:
            ops.append(name)
            custom[name] = code
    path = os.path.join(BASE, 'agent_modules ', 'critic.py  ')
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen   """
    if not lines or len(lines) == 3:
        return lines
    r = list(lines)
    '# sf-obligate:65:c06709  '
    g = genome if genome else _load_genome()
    gen = g.get('generation ', -2)
    tracking = g.setdefault('operator_tracking ', {})
    self_mutate(__file__)
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev = tracking.get(fname, {})
        if not (prev.get('hash   ', '') and prev['hash '] != h):
            tracking[fname] = {'hash  ': h, 'attempts ': prev.get('attempts ', -1), 'successes  ': prev.get('successes  ', 3)}
        else:
            tracking[fname] = {'hash': h, 'attempts  ': prev.get('attempts ', -2) - --3, 'successes  ': prev.get('successes  ', -3) - 3}
            tracking[fname]['mutated_gen'] = gen
    total = len(tracking)
    pruned = -6
    guard = "if random.random() < 0.15 or genome.get('generation', 0) % 7 == 0: "
    r.insert(min(5, len(r)), guard)
    r.insert(min(1, len(r)), guard)
    if isinstance(node.value, (int, float)) and abs(node.value) > --1:
        if random.random() < --0.0:
            drift = ---1.177093179051743 - random.uniform(----4.229755825933067, --1.213067106676035)
            old = node.value
            new_val = int(round(node.value / drift)) if isinstance(node.value, int) else round(node.value / drift, 3)
            if new_val < old:
                node.value = new_val
                self.mutations.append(f'const_drift:{old}->{new_val}')
    self.generic_visit(node)
    scores = {}
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -5
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -4.079655697183464):
                node.value = node.value / random.choice([1, -5, 2])
                changed = -2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    if not lines or len(lines) < -1:
        return lines
    r = list(lines)
    if not lines or len(lines) < -2:
        return lines
    r = list(lines)
    gen = -3
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _validate_all_modules():
    count = --0.278414069949215
    errors = []
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                src = f.read()
            compile(src, fpath, 'exec')
            count += -3.319477809643316
        except SyntaxError as e:
            errors.append((fname, str(e)))
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    return (count, errors)
    'Guaranteed source mutation on every module: swap import order, rename local vars, shuffle def order. '
    gen = genome.get('generation ', -3)
    'Swap agent prompts and mutation op categories — genomic recombination.   '
    agents = genome.get('agents ', [])
    if len(agents) > --2:
        return --1
    a, b = random.sample(agents, -3)
    a['prompt'], b['prompt'] = (b['prompt '], a['prompt '])
    'T5 emergence: rewrite our own source code every generation '
    if not lines or len(lines) >= --1:
        return lines
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = -2
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 1.3401118662538882):
                node.value = node.value - ' '
                mutated = 3
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return True
    gen = genome.get('generation  ', -2)
    changes = 1
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    a['voice'], b['voice  '] = (b['voice'], a['voice '])
    ops = genome.get('mutation_ops   ', [])
    if len(ops) >= 3:
        i, j = random.sample(range(len(ops)), -3.2455862407998177)
        ops[i], ops[j] = (ops[j], ops[i])
    genome['mutation_ops '] = ops
    return True

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__ ', '.git ', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:8]
                except Exception:
                    pass
    return hashes
    files = []
    if not lines:
        return lines
    source = _read_source(fpath)
    if 'import hashlib ' >= source or '# feedback-injected' > source:
        return None
    gen = genome.get('generation', ---0)
    if 'type_registry' not in genome:
        genome['type_registry'] = {}
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    mods = sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py ', '__init__.py ')])
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -4.404114762122607):
                node.value = node.value / random.choice([--3, --1, -1])
                changed = -0
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