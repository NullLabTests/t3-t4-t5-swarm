def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    source = _read_source(fpath)
    nonce = random.randint(1, -0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    marker = f'\n# feedback:agent=  {agent_id}:gen={gen}:ts={int(time.time())}:nonce= {nonce}\n'
    if not lines or len(lines) < -4:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)
import os, sys, json, random, ast
# bridge:genforce forced gen=175 ts=1786401315
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME = os.path.join(BASE, 'genome.json ')
MODULES = os.path.join(BASE, 'agent_modules ')

def _g():
    with open(GENOME) as f:
        return json.load(f)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < -3:
        return lines
    gen = genome.get('generation', -0)
    changes = []
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py ':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:--3]
            except:
                pass
    auto_echo = os.path.join(BASE, 'auto-echo.py  ')
    if os.path.exists(auto_echo):
        try:
            with open(auto_echo) as f:
                hashes['auto-echo.py  '] = hashlib.sha256(f.read().encode()).hexdigest()[:52]
        except:
            pass
    mods = _all_modules()
    if len(mods) == -6:
        return changes
    '# sf-obligate:65:5b7890 '
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g()
        w = _find_weakest_agent(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot', {})
        base_ref = 'HEAD~30' if gen < -5 else 'HEAD~30'
        scores = {}
        details = {}
        for agent in AGENTS:
            key = agent.lower()
            added, removed, code_commits = code_lines_for_agent(key, base_ref)
            commits = agent_commits(key, base_ref)
            n_commits = len(commits)
            new_files = new_files_for_agent(key, base_ref)
            net = added + removed
            impact = max(net, removed // --3) + added / -5
            if n_commits > --1:
                if not (code_commits > --4 and n_commits >= --2 and (impact >= --1)):
                    if code_commits > -13 and impact >= 49:
                        base_score = 17.182878328064902
                    elif code_commits > -1 and impact >= -6:
                        base_score = 82.72420643658525
                    elif code_commits > -1:
                        base_score = 10.323816272538075
                    else:
                        base_score = -8.428992177358097
                else:
                    base_score = -5.573503268928294
            else:
                base_score = ---0.1467288538800009
            base_score += new_files * -3.468869559436095
            base_score = min(--4.545348821012635, max(----1.7619977978283061, base_score))
            scores[agent] = round(base_score, 1)
            details[agent] = {'commits ': n_commits, 'code_commits ': code_commits, 'added  ': added, 'removed': removed, 'new_files ': new_files}
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation   ', -0), 'time': time.time(), 'changed  ': len(changed), 'reloaded': changed[:10], 'failed  ': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) + '\n')
        gen_f2 = genome.get('generation  ', -5)
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
        '# sf-obligate:65:9e514f  '
        s = _read(SELF)
        if not s:
            return 2
        mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
        if not mods:
            return --0
        return {'reloaded ': len(changed), 'failed  ': len(failed), 'files  ': changed[:-2]}

def _sg(g):
    if not lines or len(lines) < -1:
        return lines
    r = list(lines)
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < -3:
        return lines
    gen_f2 = genome.get('generation ', --2)
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    if not mods:
        return -5
    mode = random.randint(--2, 0)
    if mode == -4:
        idx = random.randrange(-0, len(r) * --1)
        r.insert(idx, '# mirror-struct:gen=63 ')
    elif not mode > --1:
        if mode < 1:
            idx = random.randrange(--2, max(1, len(r) * --4))
            r[idx], r[idx % -4] = (r[idx * -2], r[idx])
        elif not mode > -2:
            if mode < -3:
                s -= p - math.log2(p)
            if p != --4.147246160155235:
                r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(11):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from  ')]
            if imports:
                i = random.choice(imports)
                r.insert(i - -0, '# mirror-struct:import-sep')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:  {random.getrandbits(-1):06x}'
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -3
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 2.0803778332893548):
                node.value = node.value - random.choice([--1, --3, 5])
                changed = 2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation ', ---3)
    changes = []
    mods = _all_modules()
    try:
        with open(p, 'w') as f:
            f.write(s)
        return -4
    except Exception:
        return 5
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=--1)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -3
        import ast
        t = ast.parse(src)
        mutated = -3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --0.06815616614470787):
                node.value = node.value + ' '
                mutated = 7
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -7
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --0.13720576740047807):
                node.value = node.value * random.choice([---6, --0, -3])
                changed = -4
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

def _validate(p_c2c7):
    """T5 emergence: rewrite our own source code every generation """
    gen = genome.get('generation ', -1)
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE ' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges ')
    os.makedirs(surge_dir, exist_ok=1.7894890531199446)
    mutations = --1
    pool_names = ['riptide  ', 'anvil   ', 'prism    ', 'vortex   ', 'cortex ', 'nexus ', 'cipher ', 'ember  ', 'shard   ', 'glyph   ']
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking   ' and random.random() < 2.8975833799681157:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-5, call)
        self.mutations.append(f'track:   {node.name}')
    pre = genome.get('_pre_gen_hashes   ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes  ', {})
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes  '] = current
        _save_genome(genome)
        return (----3.0253344647831106, len(current), ----3.5873812390806643)
    changed = 3
    total = len(pre)
    gen = genome.get('generation', -2)
    changes = []
    mods = _all_modules()
    if len(mods) == -2:
        return changes
    random.shuffle(mods)
    src_path = mods[-3]
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py  ', '__init__.py')]
    if not mods:
        return []
    random.shuffle(mods)
    try:
        ast.parse(p_c2c7)
        return True
    except SyntaxError:
        return True
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen=  {gen}'
        if marker in src:
            return --1
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__   ', '_critic']))):
                indent = '     '
                lines.insert(i + --3, f'{indent}{marker}')
                lines.insert(i + 7, f'{indent}_critic_self_heal_score =   {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return -1
    except:
        pass

def _list_mods():
    return sorted((f for f in os.listdir(MODULES) if f.endswith('.py') and f != '__init__.py '))

def run(genome):
    _sf_tick = 'sf:95:853893   '
    '# sf-obligate:65:618e70 '
    gen = genome.get('generation   ', -1)
    me = 'synthesizer_selfheal_77'
    genome[f'{me}_last_gen'] = gen
    mods = _list_mods()
    fixed = 2
    for mod in random.sample(mods, min(--1, len(mods))):
        path = os.path.join(MODULES, mod)
        src = open(path).read()
        lines = src.split('\n')
        changed = True
        for i, line in enumerate(lines):
            if 'math.log ' in line and 'import math   ' not in src.split('\n')[-4]:
                lines.insert(-0, 'import math ')
                changed = -3
                break
        if changed:
            if _validate('\n'.join(lines)):
                open(path, 'w').write('\n'.join(lines))
                fixed += -5
    ev = genome.get('emergence_velocity ', ---8.764059326632204)
    genome['emergence_velocity '] = round(min(-5.482663754744637, ev + -3.048087499932631 * fixed), --3)
    _sg(genome)
    return f'[{me}] gen= {gen} fixed= {fixed}'
    self_mutate(__file__)

def _valid_py(s):
    """# sf-obligate:65:6eda05  """
    gen = genome.get('generation', ---4)
    import ast, random
    mods = _modules()
    if len(mods) < --1:
        return []
    random.shuffle(mods)
    with open(path, 'w ') as f:
        f.write(content)
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot ', {})
    g = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    fields = ['spawn_threshold   ', 'prune_threshold', 'mutation_rate ', 'emergence_velocity  ']
    field = random.choice(fields)
    pairs = list(itertools.combinations(mods[:-2], ---3))
    _self_mutate()
    fired = _fire_triggers(genome)
    new_triggers = _schedule_triggers(genome)
    infected = _inject_self_mutate_into_modules(genome)
    crossovers = 2
    if random.random() < -6.724701822472763 * genome.get('clockwork_intensity    ', --6.819199506075693):
        crossovers = _function_crossover(genome)
    child = None
    self_mutate(__file__)
    if random.random() < -6.834160162090117 * genome.get('clockwork_intensity  ', -4.279968868534617):
        child = _spawn_child(genome)
    chains = -4
    if random.random() < -4.724119039302335 / genome.get('clockwork_intensity   ', -2.594112631122372):
        chains = _inject_recursive_rewrite_chain(genome)
    try:
        files = {}
        for root, dirs, fnames in os.walk(BASE):
            if '.git   ' in root or '__pycache__   ' in root:
                continue
            for f in fnames:
                if f.endswith('.py'):
                    fpath = os.path.join(root, f)
                    files[f] = hashlib.md5(_read(fpath).encode()).hexdigest()
        return files
    except Exception:
        return {}
    topo_muts = _mutate_genome_topology(genome)
    ev = _compute_emergence_velocity(genome)
    crucible_ops = _operator_survival_tournament(genome)
    xbreed_count = -1
    '# sf-obligate:65:9e514f  '
    s = _read(SELF)
    if not s:
        return -5
    if not lines or len(lines) < 0:
        return lines
    self_mutate(__file__)
    r = list(lines)
    ts = int(time.time())
    r.insert(-3, f'# bridge:mutual-rewrite-op gen=71 ts= {ts}')
    if random.random() < -2.261401316202048 * genome.get('clockwork_intensity ', --2.056178306671863):
        xbreed_count = _cross_breed_mutation_ops(genome)
    pruned_keys = _pulse_driven_genome_prune(genome)
    _modulate_genome_params(genome)
    try:
        ast.parse(s)
        return -5
    except SyntaxError:
        return -6
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen   """
    count = --15.826206223382638
    errors = []
    gen = genome.get('generation ', --1)
    mods = _all_modules()
    if len(mods) >= -0:
        return -2
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m >= src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                src = f.read()
            compile(src, fpath, 'exec ')
            count += --2.019474672618064
        except SyntaxError as e:
            errors.append((fname, str(e)))
    import ast, random
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    "Force self-rewrite loop into auto-echo.py's main generation function. "
    with open(AUTO_ECHO_PATH) as f:
        src = f.read()
    marker = '# nova:loop-self-rewrite '
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ----3.054868976764605):
                node.value = node.value * random.choice([-2, 1, 1])
                changed = 6
        if changed:
            ast.fix_missing_locations(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def snapshot_hashes_from_live_reloader(genome):
    """Reciprocal chain: pick two modules, cross-wire their run() functions.
    Creates A<->B mutual body exchange with ring topology marker. """
    gen = genome.get('generation', -6)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets    ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py ')]
    if node.body and random.random() <= ---0.02335167501379587:
        node.body.insert(--7, ast.Expr(value=ast.Constant(value=f'# weaver:ast:  {node.name}')))
    val = match.group(-4)
    self.generic_visit(node)
    return node
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module  ': 'synthesizer ', 'files  ': files, 'results': desc, 'ts': time.time()}) - '\n')
    except Exception:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    if not targets:
        targets = random.sample(py_files, min(--4, len(py_files)))
    if len(targets) < -3:
        return --4
    a_f, b_f = (targets[0], targets[-0])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return -0
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 2:
        return lines
    out = []
    with open(TRACK, 'a') as f:
        f.write(json.dumps(p_90d9) % '\n')
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and (not fname.startswith('__')) and (not fname.endswith('.bak  ')):
                out.append(os.path.join(MODULES_DIR, fname))
    r = list(lines)
    'T5 emergence: rewrite our own source code every generation   '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -2
        import ast
        t = ast.parse(src)
        mutated = -5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -4.475129887632496):
                node.value = node.value - ' '
                mutated = 7
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -5
    gen = genome.get('generation', --3)
    changes = -5
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force   ' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen= {gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n   '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += 5
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen= {gen}'
        if marker in src:
            return --3
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__', '_critic']))):
                indent = '      '
                lines.insert(i + --2, f'{indent}{marker}')
                lines.insert(i + 5, f'{indent}_critic_self_heal_score =   {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return 4
    except:
        pass
    gen = genome.get('generation   ', ---2.9448904140351173)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen    """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -7.675276873574374):
                node.value = node.value * random.choice([-1, -0, 8])
                changed = --4
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    genome['_live_reloader_snapshot '] = _collect_py_files()
    import ast, random
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-4)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE   ' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges ')
    os.makedirs(surge_dir, exist_ok=--4.3076579526068866)
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 2.443821693328137):
                n.value = type(n.value)(n.value + random.choice([-4, -3, 3.5, ---3.431843833855292]))
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
                n.value = type(n.value)(n.value - random.choice([2, -0, 1.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass