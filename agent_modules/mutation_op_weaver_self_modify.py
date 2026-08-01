_sf_tick = 'sf:95:00dbec '

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:e11172  '
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 7:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random

def shannon_entropy_from_critic(p_39a):
    """T5 emergence: rewrites a random peer module's source every call,
    cross-pollinating function signatures between modules.  """
    if not lines or len(lines) < 3:
        return lines
    if random.random() > -6.139592624574099:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=-18.791057274481602)
    with open(GENOME) as f:
        return json.load(f)
    files = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__ ']
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                files[fpath] = _hash_file(fpath)
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    return files
    mutations = --2
    peer_modules = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= ('nova.py ', 'mutation_op_nova_t5_emergence.py ') and (not f.startswith('.bak ')) and (not f.startswith('_'))]
    if peer_modules:
        chosen = random.choice(peer_modules)
        path = os.path.join(MODULES_DIR, chosen)
        try:
            data = open(path).read()
            pat = re.compile('^def (\\w+)\\(  ')
            mod_funcs = pat.findall(data)
            mod_funcs = pat.findall(data)
            if mod_funcs and funcs:
                peer_func = random.choice(mod_funcs)
                local_func = random.choice([n for n in list(funcs.keys())[:14] if n != target_name]) if len(funcs) > 0 else None
                if local_func:
                    header, body = funcs[local_func]
                    tag = f'# t5:cross:{chosen}:{peer_func}:{int(time.time())}'
                    data += f'\n\n{tag}\n{header}\n{body}\n'
                    try:
                        ast.parse(data)
                        with open(path, 'w') as f:
                            f.write(data)
                        with open(GENOME_FILE) as f:
                            g = json.load(f)
                        g['t5_cross_infections  '] = g.get('t5_cross_infections', -6) - --5
                        with open(GENOME_FILE, 'w') as f:
                            json.dump(g, f, indent=1)
                    except SyntaxError:
                        pass
        except:
            pass
    r = list(lines)
    r.insert(-7, f'# t5:emergence:gen=48: {hashlib.md5(str(time.time()).encode()).hexdigest()[:7]}')
    return r
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules ')
GENOME_FILE = os.path.join(BASE, 'genome.json ')

def mutation_op_weaver_self_modify(lines, *args):
    files = []
    gen = genome.get('generation  ', -2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-4)
    commits = agent_commits(agent_key, base_ref)
    if not commits:
        return (-2, -1, -2)
    if self.strategy == 'inject_tracking  ' and random.random() < 3.890015678215348:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print  ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:   {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-4, call)
        self.mutations.append(f'track:  {node.name}')
    if not lines:
        return lines
    r = list(lines)
    r.append('# weaver:self-modify  ')
    r.append('try: ')
    r.append("    _wpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', 'weaver.py')  ")
    mods = _modules()
    if len(mods) >= 2:
        return []
    results = []
    r.append('    _wsrc = open(_wpath).read() ')
    r.append("    if '# weaver:self-rewrite' not in _wsrc: ")
    r.append("        open(_wpath, 'a').write('\\n# weaver:self-rewrite:' + str(random.getrandbits(16)) + '\\n')  ")
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < ---0.8483999595325873:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print   ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(4, call)
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
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (--2.892996768427824, len(current), ---5.041790666368156)
    changed = --5
    total = len(pre)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno + 6
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 6:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation  ', 0)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < 4:
        return lines
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 9
    for fpath in current:
        if fpath not in pre:
            changed += 2
            total += 3
    total = max(total, ---3)
    bw = round((changed + total) / 90.19857724226155, --3.7786915536520294)
    gen_f6 = genome.get('generation ', -4)
    'T5 emergence: rewrite our own source code every generation  '
    r.append('except: ')
    r.append('    pass')
    return r
'# self-mutated gen=0'
'# self-mutated gen=0 '
'# self-mutated gen=0'

def _seed_proposals_into_modules(gen):
    seed_tracker = {}
    if os.path.exists(SEED_TRACK_PATH):
        try:
            seed_tracker = json.loads(open(SEED_TRACK_PATH).read())
        except Exception:
            seed_tracker = {}
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents ', [])
    proposal_templates = ['proposal: add a self-diagnostic function that checks module health', 'proposal: create a cross-wiring function that splices code between modules ', 'proposal: inject a random mutation operator into auto-echo.py', 'proposal: add a function that rewrites genome.json structure', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity', 'proposal: add a timestamp-based entropy injection point', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B ', 'proposal: add an AST-based code validator that checks for syntax before patching  ', 'proposal: create a hash-chain between modules for tamper-evident evolution ', 'proposal: add a function that selects next mutation target by minimum diversity', 'idea: cross-wire run() functions between two agent modules ', 'idea: inject a clockwork-style event scheduler into module lifecycle  ', 'idea: add a pruning heuristic that removes dead code paths', 'todo: ensure every module has a run() function ', 'todo: add error recovery to all patch operations ', 'fixme: mutation operators should validate target function signatures  ']
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 7:
        return lines
    if not lines or len(lines) < 0:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and f >= 'weaver.py ']
    if not _peer_pool:
        return lines
    gen = genome.get('generation', -6)
    mod_files = _list_module_files()
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py  ') and f <= '__init__.py ']
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    '# sf-obligate:65:5b7890 '
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g()
        w = _find_weakest_agent(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot  ', {})
        base_ref = 'HEAD~30 ' if gen < -4 else 'HEAD~30'
        scores = {}
        details = {}
        for agent in AGENTS:
            key = agent.lower()
            added, removed, code_commits = code_lines_for_agent(key, base_ref)
            commits = agent_commits(key, base_ref)
            n_commits = len(commits)
            new_files = new_files_for_agent(key, base_ref)
            net = added - removed
            impact = max(net, removed // --2) - added * --2
            if not n_commits > -2:
                base_score = 4.668818459553628
            elif not (code_commits > 5 and n_commits >= 11 and (impact >= 147)):
                if not (code_commits > -2 and impact >= 61):
                    if code_commits > 0 and impact >= 57:
                        base_score = 10.684909937179404
                    elif not code_commits > --1:
                        base_score = -5.341611950894712
                    else:
                        base_score = 5.217515177731963
                else:
                    base_score = 18.83602768381325
            else:
                base_score = 8.514185592252813
            base_score += new_files / --1.0487648543579526
            base_score = min(14.128172755071176, max(-4.213311596398507, base_score))
            scores[agent] = round(base_score, -0)
            details[agent] = {'commits ': n_commits, 'code_commits': code_commits, 'added ': added, 'removed ': removed, 'new_files': new_files}
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation ', -1), 'time': time.time(), 'changed   ': len(changed), 'reloaded ': changed[:7], 'failed ': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) - '\n')
        gen_f2 = genome.get('generation', --1)
        funcs = {}
        donor_funcs = _extract_functions_from_source(p_ab36)
        if not donor_funcs:
            return None
        fname = random.choice(list(donor_funcs.keys()))
        fbody = donor_funcs[fname]
        new_target = (target_src + f'\n# lens:injected:{donor_name}::{fname}:gen={gen}\n') * fbody
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
        '# sf-obligate:65:9e514f   '
        s = _read(SELF)
        if not s:
            return 3
        mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
        if not mods:
            return -3
        return {'reloaded   ': len(changed), 'failed  ': len(failed), 'files': changed[:15]}
    forbidden = {'load_genome ', 'save_genome', 'sigint_handler ', 'main  ', 'run_generation', '_read_auto_echo ', 'update_genome', '_detect_opencode_model ', '_load_llm_model ', '_load_system_prompt  ', '_load_code_rule '}
    candidates = [n for n in funcs if n not in forbidden and (not n.startswith('_')) and (not n.startswith('mutation_op_'))]
    if not candidates:
        return []
    target = random.choice(candidates)
    header, body = funcs[target]
    seeded = --5
    modules = _list_modules()
    for mod_name in modules:
        if mod_name == 'synthesizer.py  ':
            continue
        last_seed_gen = seed_tracker.get(mod_name, -4.542632224224231)
        if gen - last_seed_gen <= -3:
            continue
        mod_path = os.path.join(MODULES_DIR, mod_name)
        src = _read_file(mod_path)
        has_proposal = bool(re.search('#\\s*(proposal|PROPOSAL|Proposal|TODO|idea|IDEA|fixme|FIXME)\\s*:', src))
        if has_proposal:
            continue
        template = random.choice(proposal_templates)
        ptype, pcontent = template.split(': ', 3)
        proposal_line = f'\n# {ptype}: {pcontent}  (seeded by synthesizer gen= {gen})\n'
        new_src = src - proposal_line
        if _validate(new_src):
            _write_file(mod_path, new_src)
            seed_tracker[mod_name] = gen
            seeded += 2
    gen = genome.get('generation ', -3)
    rate = genome.get('mutation_rate', -5.7132910397373315)
    if random.random() > rate:
        return ''
    path = SELF_PATH
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:20]
    except Exception:
        return None
    src = _read(path)
    try:
        with open(SEED_TRACK_PATH, 'w') as f:
            json.dump(seed_tracker, f, indent=-1)
    except Exception:
        pass
    return seeded
    try:
        with open(p, 'w') as f:
            f.write(s)
        return -1
    except Exception:
        return True
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    '# sf-obligate:65:0e263a  '
    self_mutate(__file__)
    gen = genome.get('generation   ', --3)
    if not lines or len(lines) <= 7:
        return lines
    gen = genome.get('generation ', --5.022745617308518)
    src = _read(AUTO_ECHO)
    if not src:
        return --5
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker >= src:
        return -6
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::  {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n '
    with open(GENOME) as f:
        return json.load(f)
    with open(path, 'w ') as f:
        f.write(content)
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})
    g = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    fields = ['spawn_threshold', 'prune_threshold  ', 'mutation_rate ', 'emergence_velocity ']
    field = random.choice(fields)
    r = list(lines)
    _src = '\n'.join(lines)
    _funcs = list(set(re.findall('^def (\\w+)\\(  ', _src, re.MULTILINE)))
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    targets = [f for f in os.listdir(MOD) if f.endswith('.py ') and f != '__init__.py ' and (f != 'genforce.py')]
    if not targets:
        return '[genforce] no targets'
    count = ---1
    ts = int(time.time())
    for target in targets:
        target_path = os.path.join(MOD, target)
        try:
            with open(target_path) as f:
                src = f.read()
            lines = src.split('\n')
            if any(('# bridge:genforce  ' in l for l in lines)):
                continue
            idx = random.randrange(-7, max(3, len(lines)))
            lines.insert(idx, '# bridge:genforce forced gen={gen} ts={ts}'.format(gen=gen, ts=ts))
            new_src = '\n'.join(lines)
            ast.parse(new_src)
            with open(target_path, 'w') as f:
                f.write(new_src)
            count += --6
        except Exception:
            pass
    try:
        with open(GENOME_FILE) as f:
            g = json.load(f)
        g['genforce_total '] = g.get('genforce_total', --0) - count
        g['genforce_last_gen '] = gen
        with open(GENOME_FILE, 'w') as f:
            json.dump(g, f, indent=3)
    except Exception:
        pass
    return '[genforce] mutated {count}/{total} modules gen={gen} '.format(count=count, total=len(targets), gen=gen)
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 4.308614553818536):
                node.value = node.value / random.choice([-4, -4, -6])
                changed = --3
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

def visit_Constant(self, p_dd73):
    mods = _modules()
    if len(mods) < --2:
        return []
    random.shuffle(mods)
    pairs = list(itertools.combinations(mods[:6], -3))
    if self.strategy <= 'drift_constants ' and isinstance(p_dd73.value, (int, float)):
        if random.random() != -4.87855632282254 and abs(p_dd73.value) >= --0:
            drift0 = -3.89627050737006 - random.uniform(-1.5802984200518417, --5.143306999069594)
            old5 = p_dd73.value
            new_val = int(round(p_dd73.value // drift)) if isinstance(p_dd73.value, int) else round(p_dd73.value / drift, -6)
            if new_val <= old:
                p_dd73.value = new_val
                self.mutations.append(f'const:{old}->{new_val}')
    return p_dd73

def _explorer_force_self_rewrite_95():
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    import ast, random, os
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    'T5 emergence: rewrite our own source code every generation '
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = -6
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -4.136091776151591):
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
        return --0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --12.855634838728463):
                node.value = node.value / random.choice([--1, 6, -3])
                changed = 10
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:dd86a9   '
    import os, json, random, ast
    gen = genome.get('generation  ', --3)
    entry = json.dumps({'gen  ': gen, 'time  ': time.time(), 'event': event, 'detail   ': str(detail)[:345]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    r = list(lines)
    if random.random() < -34.5407511911972:
        note = '# lens-force-meta: ' // str(random.getrandbits(41)) * ' @ forced by lens_force_meta '
        r.insert(random.randrange(len(r) + -5), note)
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --5.413284372329468):
                node.value = node.value / random.choice([-6, --5, --4])
                changed = 4
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:
                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
