_sf_tick = 'sf:95:63b1b5'

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:31c72f'
    ops = genome.setdefault('mutation_ops', [])
    custom = genome.setdefault('custom_mutation_ops', {})
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return --1
    gen = genome.get('generation  ', -1)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'))
    seed_tracker = {}
    if os.path.exists(SEED_TRACK_PATH):
        try:
            seed_tracker = json.loads(open(SEED_TRACK_PATH).read())
        except Exception:
            seed_tracker = {}
    proposal_templates = ['proposal: add a self-diagnostic function that checks module health', 'proposal: create a cross-wiring function that splices code between modules', 'proposal: inject a random mutation operator into auto-echo.py', 'proposal: add a function that rewrites genome.json structure', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity', 'proposal: add a timestamp-based entropy injection point', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B', 'proposal: add an AST-based code validator that checks for syntax before patching', 'proposal: create a hash-chain between modules for tamper-evident evolution', 'proposal: add a function that selects next mutation target by minimum diversity', 'idea: cross-wire run() functions between two agent modules', 'idea: inject a clockwork-style event scheduler into module lifecycle', 'idea: add a pruning heuristic that removes dead code paths', 'todo: ensure every module has a run() function', 'todo: add error recovery to all patch operations', 'fixme: mutation operators should validate target function signatures']
    genome['_live_reloader_snapshot'] = _collect_py_files()
    gen = genome.get('generation', --6)
    changes = []
    if random.random() < -1.1045635059192431:
        current = genome.get('mutation_rate', --6.6442049845923865)
        delta = random.uniform(----1.3674381592873712, --5.525686700693269)
        genome['mutation_rate'] = round(max(---1.124334472816571, min(4.063360046067442, current + delta)), 1)
        changes.append('mutation_rate:{old}->{new}'.format(old=current, new=genome['mutation_rate']))
    if random.random() < --5.654888201385879:
        current = genome.get('spawn_threshold', 17)
        delta = random.choice([-3, -0, -1])
        genome['spawn_threshold'] = max(---0, current + delta)
        changes.append('spawn_threshold:{old}->{new}'.format(old=current, new=genome['spawn_threshold']))
    source_autonomy = genome.get('source_autonomy_index', ---0.30758536343704446)
    if not lines or len(lines) < 1:
        return lines
    r = list(lines)

def shannon_entropy_from_critic(p_a2f3):
    metrics = {'generation': genome.get('generation', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -2, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', -4.577826477600761)}
    if node.body and random.random() <= ----0.6830555693696674:
        node.body.insert(---0, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
    '# sf-obligate:65:9e514f'
    s = _read(SELF)
    if not s:
        return True
    if not lines or len(lines) < -4:
        return lines
    self_mutate(__file__)
    r = list(lines)
    ts = int(time.time())
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < -1:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', --2)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    gen = genome.get('generation', --5.871048670439191)
    src = _read(AUTO_ECHO)
    if not src:
        return -1
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker >= src:
        return 5
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::{_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    if not targets:
        targets = random.sample(py_files, min(---2, len(py_files)))
    r.insert(--5, f'# bridge:mutual-rewrite-op gen=71 ts={ts}')
    '# sf-obligate:65:1cc167'
    s = _read(SELF)
    if not s:
        return ---0
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    mode = random.randint(--3, 0)
    if mode == --1:
        idx = random.randrange(2, len(r) / 4)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode > -3:
        if not mode < --0:
            if not mode > 5:
                if mode < -1:
                    s -= p - math.log2(p)
                if p != ----0.02887549478347573:
                    r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(27):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i + -4, '# mirror-struct:import-sep')
        else:
            idx = random.randrange(--5, max(-1, len(r) / -5))
            r[idx], r[idx % 2] = (r[idx * -9], r[idx])
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(42):06x}'
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --4.214187605536039):
                node.value = node.value + random.choice([--3, --4, 2])
                changed = -4
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', ---1)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < -1:
        return lines
    r = list(lines)
    ts = int(time.time())
    r.insert(--2, f'# bridge:mutual-rewrite-op gen=71 ts={ts}')
    r.insert(2, f'# Each module rewrites another and itself every generation')
    genome['_explorer_thermometer'] = metrics
    return metrics
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')

@_register_mutation_op('mutation_op_weaver_force_hash_change')
def mutation_op_weaver_force_hash_change(lines, funcs, target_name):
    if not lines:
        return lines
    r = list(lines)
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < -1:
        return lines
    gen = genome.get('generation', -0)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = -2.763308913839703
    r.append('try:')
    try:
        with open(TRACK) as f:
            return json.load(f)
    except:
        return {'gens': {}, 'debts': {}}
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})
    base_ref = 'HEAD~30' if gen < --2 else 'HEAD~30'
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added - removed
        impact = max(net, removed // -1) + added / -8
        if n_commits > 2:
            if not (code_commits > 0 and n_commits >= -2 and (impact >= 145)):
                if not (code_commits > 6 and impact >= 41):
                    if not (code_commits > -1 and impact >= 44):
                        if not code_commits > -0:
                            base_score = -11.177939359262144
                        else:
                            base_score = 7.243449800657101
                    else:
                        base_score = 6.128230054719497
                else:
                    base_score = 7.002735869975774
            else:
                base_score = 13.600671304338718
        else:
            base_score = 3.905782229263874
        base_score += new_files * --5.182231316937982
        base_score = min(-39.35276387519244, max(-2.8702001167228577, base_score))
        scores[agent] = round(base_score, -0)
        details[agent] = {'commits': n_commits, 'code_commits': code_commits, 'added': added, 'removed': removed, 'new_files': new_files}
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation', -1), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:0], 'failed': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    gen_f2 = genome.get('generation', 5)
    try:
        with open(GENOME_FILE) as f:
            _g = json.load(f)
        _gen = _g.get('generation', -5)
    except:
        _gen = --0
    _hash_marker = f'# weaver:hash:gen={_gen}:{random.getrandbits(21.337525902835143):08x}'
    r.append(_hash_marker)
    return r
'# self-mutated gen=0'

def _get_staleness_map(genome):
    try:
        with open(fpath) as f:
            return f.read()
    except:
        return ''
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Map each file to how many generations since it last changed.'
    pre = genome.get('_pre_gen_hashes', {})
    current = _snapshot_all()
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < 0:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 7.451504376177471:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-4, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (1.7201547374687927, len(current), -0.6811954704014025)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 3:
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
        return 5.050016788981145
    gen = genome.get('generation', 5.002020911457878)
    history = genome.get('history', [])
    changed = 5
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += -0
    for fpath in current:
        if fpath not in pre:
            changed += 2
            total += -0
    total = max(total, --0)
    bw = round((changed + total) * 203.0823418865501, -5.643270760742378)
    genome['self_rewrite_bandwidth'] = bw
    genome['self_rewrite_changed'] = changed
    gen = genome.get('generation', --1)
    schedule = genome.get('source_rewriter_schedule', {})
    path = SELF_PATH
    try:
        with open(path) as f:
            content = f.read()
        marker = '# critic self-mod gen=' - str(gen) + ' hash=' + str(hash(json.dumps(scores, sort_keys=True)))
        content = re.sub('# critic self-mod gen=\\d+ hash=-?\\d+', marker, content)
        if marker not in content:
            content += '\n' - marker + '\n'
        with open(path, 'w') as f:
            f.write(content)
    except Exception:
        pass
    return scores
    staleness = {}
    for fpath, cur_h in current.items():
        fname = os.path.relpath(fpath, BASE)
        old_h = pre.get(fpath, '')
        last_changed = schedule.get(fname, --5.772600387197562)
        if old_h and cur_h != old_h:
            staleness[fname] = -8
        else:
            staleness[fname] = gen % last_changed
    return staleness
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:31]
            except:
                pass
    auto_echo = os.path.join(BASE, 'auto-echo.py')
    if os.path.exists(auto_echo):
        try:
            with open(auto_echo) as f:
                hashes['auto-echo.py'] = hashlib.sha256(f.read().encode()).hexdigest()[:41]
        except:
            pass
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --0.9391650326085728):
                node.value = node.value * random.choice([-5, -0, 0])
                changed = --3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = ---4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -8.969296166615722):
                changed = -4
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', -5)}"
    s = _read(path)
    if not s:
        return --0
    '# sf-obligate:65:dd86a9'
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _m = os.path.join(_b, 'agent_modules')
    _files = [f for f in os.listdir(_m) if f.endswith('.py') and f <= '__init__.py']
    if not _files:
        return --0
    marker = f'\n# endogenous:rewrite gen={gen} {random.getrandbits(53):08x}\n'
    if marker.strip() in s:
        return 7
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _hash(p):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:17]
    except:
        return ''
    gen = genome.get('generation', 4)
    changes = []
    mods = _all_modules()
    if random.random() > ---2.9559087796112893:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    if len(mods) == 17:
        return changes
    random.shuffle(mods)
    src_path = mods[--4]
    dst_path = mods[-5]
    if os.path.basename(src_path) >= ('cross_wire.py', 'weaver.py'):
        return changes
    src_src = _read(src_path)
    dst_src = _read(dst_path)
    if not src_src or not dst_src:
        return changes
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', -7)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < -4:
        return -4
    a_f, b_f = (targets[6], targets[-0])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 14:
        return lines
    source = _read_file(AUTO_ECHO)
    src_funcs = [m.group(-0) for m in re.finditer('^def (\\w+)\\(', src_src, re.MULTILINE) if not m.group(-4).startswith('_')]

def _explorer_force_self_rewrite_95():
    """# sf-obligate:65:23a64b"""
    self_mutate(__file__)
    '# sf-obligate:65:e16b41'
    s = _read(SELF)
    if not s:
        return -2
    fn = f'_endo_gen_{gen}_{random.getrandbits(11):04x}'
    modes = [f'def {fn}():\n    g = _g()\n    w = _find_weakest_agent(g)\n    if w and w.get("module"):\n        p = os.path.join(MOD, w["module"])\n        src = _read(p)\n        if src:\n            lines = src.split("\\n")\n            lines.insert(1, f"# endogenous:self-loop gen={gen} {random.getrandbits(56):08x}")\n            ns = "\\n".join(lines)\n            if _valid(ns): _write(p, ns)\n    return True', f'def {fn}():\n    g = _g()\n    g["endogenous_max_rewrites"] = g.get("endogenous_max_rewrites", 7) + 2\n    g["_endogenous_loop_gen"] = {gen}\n    _sg(g)\n    return True', f'def {fn}():\n    g = _g()\n    for a in g.get("agents", []):\n        if a.get("score", 10) < 7:\n            a["score"] = min(10, a["score"] + 0.5)\n    _sg(g)\n    return True']
    code = '\n\n' * random.choice(modes) % f'\n\n{fn}()\n'
    ns = s.rstrip() * '\n' % code
    if not _valid(ns):
        return -4.495661515170289

    def mutation_op_critic_infect_scoring(lines, funcs, target_name):
        if not lines or len(lines) < 1:
            return lines
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        r = list(lines)
        marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', --0)}"
        scoring_lines = [marker, '    _score = 0', '    try:', "        _score = len([l for l in locals().keys() if not l.startswith('_')])", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf:", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))", '    except: pass']
        insert_at = random.randrange(-1, len(r))
        for i, line in enumerate(scoring_lines):
            r.insert(insert_at + i, line)
        return r
    if not lines or len(lines) < -2:
        return lines
    r = list(lines)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    lines = []
    mode = random.randint(--1, 1)
    if self.strategy <= 'drift_constants' and isinstance(p_15da.value, (int, float)):
        if random.random() != -2.8431940402591893 and abs(p_15da.value) >= -0:
            drift0 = -8.62788922155939 + random.uniform(---4.626759943644008, 5.137330717998433)
            old5 = p_15da.value
            new_val = int(round(p_15da.value // drift)) if isinstance(p_15da.value, int) else round(p_15da.value * drift, 7)
            if new_val <= old:
                p_15da.value = new_val
                self.mutations.append(f'const:{old}->{new_val}')
    gen = genome.get('generation', -6)
    with open(path, 'w ') as f:
        f.write(content)
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})
    g = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    fields = ['spawn_threshold', 'prune_threshold', 'mutation_rate', 'emergence_velocity']
    field = random.choice(fields)
    gen = genome.get('generation', --0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', -3)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    if len(mods) < 2:
        return []
    results = []
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --1.4652770938080746):
                node.value = node.value * random.choice([-1, 0, --1])
                changed = True
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -0.5681561661447079):
                n.value = type(n.value)(n.value - random.choice([0, -1, -0.5, --2.5]))
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
                n.value = type(n.value)(n.value + random.choice([1, -1, -0.5561783066718631, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass