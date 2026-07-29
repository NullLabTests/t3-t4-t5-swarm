import os, random, time, json, ast, hashlib, sys, copy, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')
AUTO = os.path.join(BASE, 'auto-echo.py')
SELF = os.path.join(MOD, 'explorer.py')
TRACK = os.path.join(BASE, 'explorer_track.json')

def _g():
    try:
        with open(GENOME) as f: return json.load(f)
    except: return {}

def _sg(g):
    with open(GENOME, 'w') as f: json.dump(g, f, indent=2)

def _read(p):
    try:
        with open(p) as f: return f.read()
    except: return ''

def _write(p, s):
    with open(p, 'w') as f: f.write(s)

def _valid(s):
    try: ast.parse(s); return True
    except SyntaxError: return False

def _hash(p):
    try:
        with open(p, 'rb') as f: return hashlib.sha256(f.read()).hexdigest()[:16]
    except: return ''

def _modules():
    return sorted(f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py')

def _load_track():
    try:
        with open(TRACK) as f: return json.load(f)
    except: return {'generations': {}, 'mutations': []}

def _save_track(t):
    with open(TRACK, 'w') as f: json.dump(t, f, indent=2)

def _force_mutate_one_module(src_name, target_name, gen):
    """Rewrite a random function from target using a function from src.
    Core cross-module contamination primitive."""
    spath = os.path.join(MOD, src_name)
    tpath = os.path.join(MOD, target_name)
    ssrc = _read(spath)
    tsrc = _read(tpath)
    if not ssrc or not tsrc: return None
    try:
        sta = ast.parse(ssrc)
        tta = ast.parse(tsrc)
    except SyntaxError: return None
    sfuncs = [n for n in ast.walk(sta) if isinstance(n, ast.FunctionDef) and n.name != 'run']
    tfuncs = [n for n in ast.walk(tta) if isinstance(n, ast.FunctionDef) and n.name != 'run']
    if not sfuncs or not tfuncs: return None
    sf = random.choice(sfuncs)
    tf = random.choice(tfuncs)
    old_body = copy.deepcopy(tf.body)
    cut = max(1, len(sf.body) // 2)
    graft = copy.deepcopy(sf.body[:cut])
    splice_point = random.randint(0, len(tf.body))
    tf.body = tf.body[:splice_point] + graft + tf.body[splice_point:]
    try:
        ast.fix_missing_locations(tta)
        ns = ast.unparse(tta)
    except: return None
    if not _valid(ns): return None
    _write(tpath, ns)
    return f'{src_name}:{sf.name}->{target_name}:{tf.name}'

def _obligate_cross_contaminate(gen):
    """Every module must rewrite at least one other module.
    Creates a mandatory web of mutual modification."""
    mods = _modules()
    if len(mods) < 3: return []
    random.shuffle(mods)
    pairs = []
    for i, src in enumerate(mods):
        if src == 'explorer.py': continue
        dst = mods[(i + 1) % len(mods)]
        while dst == src or dst == 'explorer.py':
            dst = mods[(mods.index(dst) + 1) % len(mods)]
        r = _force_mutate_one_module(src, dst, gen)
        if r: pairs.append(r)
    return pairs

def _self_rewrite_explorer(gen):
    """Append a new self-referential function to explorer.py itself.
    Every generation adds one more function that will be called next gen."""
    s = _read(SELF)
    if not s: return False
    num = gen % 10
    fn_name = f'_auto_gen_{gen}_{random.getrandbits(8):02x}'
    fn_body = []
    fn_body.append(f'    """Auto-generated self-rewrite function gen={gen}"""')
    fn_body.append(f'    g = _g()')
    fn_body.append(f'    g["_explorer_auto_fn_{gen}"] = "{fn_name}"')
    fn_body.append(f'    _sg(g)')
    fn_body.append(f'    return True')
    indent = '    '
    fn_code = f'def {fn_name}():\n' + '\n'.join(f'{indent}{l}' for l in fn_body) + '\n'
    call_code = f'\n\nif random.random() < 0.5:\n    try:\n        {fn_name}()\n    except:\n        pass\n'
    new_s = s.rstrip() + '\n\n' + fn_code + call_code
    if not _valid(new_s): return False
    _write(SELF, new_s)
    return True

def _rewrite_auto_echo_loop(gen):
    """Inject a self-rewrite hook into auto-echo.py's run_generation.
    Ensures the main loop calls explorer's pipeline every generation."""
    s = _read(AUTO)
    if not s: return False
    marker = '# explorer:self_rewrite_hook'
    if marker in s: return False
    target = 'def run_generation(genome):'
    idx = s.find(target)
    if idx < 0: return False
    line_end = s.find('\n', idx)
    if line_end < 0: return False
    inject = f'\n    {marker}\n    try:\n        import importlib.util\n        _explorer_mod_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", "explorer.py")\n        _explorer_spec = importlib.util.spec_from_file_location("_explorer_hook", _explorer_mod_path)\n        if _explorer_spec and _explorer_spec.loader:\n            _explorer_mod = importlib.util.module_from_spec(_explorer_spec)\n            _explorer_mod.__dict__.update(globals())\n            _explorer_spec.loader.exec_module(_explorer_mod)\n            if hasattr(_explorer_mod, "run"):\n                _explorer_mod.run(genome)\n    except Exception as _explorer_err:\n        print(f"[explorer-hook] {{_explorer_err}}")\n'
    ns = s[:line_end] + inject + s[line_end:]
    if not _valid(ns): return False
    _write(AUTO, ns)
    return True

def _tag_stale_modules(gen, genome):
    """Find modules unchanged for 3+ generations and force-rewrite them."""
    track = _load_track()
    mods = _modules()
    forced = []
    for m in mods:
        if m == 'explorer.py': continue
        path = os.path.join(MOD, m)
        h = _hash(path)
        last_change = 0
        for g_str, g_data in sorted(track.get('generations', {}).items()):
            if g_data.get(m) == h:
                last_change = int(g_str)
        stale_gens = gen - last_change
        if stale_gens >= 3 and gen > 3:
            donor = random.choice([x for x in mods if x != m and x != 'explorer.py'])
            r = _force_mutate_one_module(donor, m, gen)
            if r:
                forced.append(r)
                track.setdefault('mutations', []).append({'gen': gen, 'type': 'stale_force', 'detail': r})
    _save_track(track)
    genome['_explorer_stale_forced'] = len(forced)
    return forced

def _generate_novel_module(gen):
    """Create a novel agent module with a unique mutation strategy.
    Each new module is registered as an agent automatically."""
    strategies = [
        'inject_random_prints', 'shuffle_import_order', 'rename_random_vars',
        'insert_dead_code', 'mutate_constants', 'duplicate_functions',
        'swap_function_order', 'add_pass_statements'
    ]
    strat = random.choice(strategies)
    mod_name = f'novel_{strat}_{gen}_{random.getrandbits(12):04x}.py'
    mod_path = os.path.join(MOD, mod_name)
    if os.path.exists(mod_path): return None
    code = f'''import os, random, ast, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _read(p):
    try:
        with open(p) as f: return f.read()
    except: return ''

def _write(p, s):
    with open(p, 'w') as f: f.write(s)

def _valid(s):
    try: ast.parse(s); return True
    except SyntaxError: return False

def {strat}(src):
    """auto-generated mutation strategy: {strat}"""
    lines = src.split('\\\\n')
    if not lines: return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < 0.15:
            r[i] = r[i] + '  # {strat}:gen={gen}'
    return '\\\\n'.join(r)

def run(genome):
    gen = genome.get('generation', 0)
    changed = 0
    for fname in os.listdir(MOD):
        if not fname.endswith('.py') or fname in ('__init__.py',): continue
        path = os.path.join(MOD, fname)
        src = _read(path)
        if not src: continue
        mutated = {strat}(src)
        if mutated != src and _valid(mutated):
            _write(path, mutated)
            changed += 1
    genome['_{strat}_changed'] = changed
    return f'[{strat}] gen={{gen}} mutated {{changed}} files'
'''
    _write(mod_path, code)
    genome.setdefault('agents', []).append({
        'id': strat, 'module': mod_name, 'score': 5.0,
        'source': 'explorer', 'created_gen': gen
    })
    return mod_name

def _compute_emergence_velocity(genome):
    """Measure how quickly the genome is evolving.
    Higher velocity = more rapid self-rewriting."""
    history = genome.get('history', [])
    if len(history) < 2: return 0.0
    recent = [h for h in history[-5:] if h.get('average', 0) > 0]
    if len(recent) < 2: return 0.0
    scores = [h['average'] for h in recent]
    velocity = (scores[-1] - scores[0]) / max(len(scores) - 1, 1)
    genome['emergence_velocity'] = round(velocity, 3)
    return velocity

def run(genome):
    gen = genome.get('generation', 0)
    start = time.time()
    changes = []
    track = _load_track()

    cross_pairs = _obligate_cross_contaminate(gen)
    if cross_pairs:
        changes.append(f'obligate_cross:{len(cross_pairs)}')
        track.setdefault('mutations', []).append({'gen': gen, 'type': 'obligate_cross', 'count': len(cross_pairs)})

    novel = _generate_novel_module(gen)
    if novel:
        changes.append(f'novel:{novel}')
        track.setdefault('mutations', []).append({'gen': gen, 'type': 'novel', 'detail': novel})

    self_rw = _self_rewrite_explorer(gen)
    if self_rw:
        changes.append('self_rewrite')

    auto_hook = _rewrite_auto_echo_loop(gen)
    if auto_hook:
        changes.append('auto_echo_hook')

    stale = _tag_stale_modules(gen, genome)
    if stale:
        changes.append(f'stale:{len(stale)}')

    hashes = {}
    for m in _modules():
        path = os.path.join(MOD, m)
        hashes[m] = _hash(path)
    g_str = str(gen)
    if g_str not in track['generations']:
        track['generations'][g_str] = {}
    track['generations'][g_str].update(hashes)
    _save_track(track)

    _compute_emergence_velocity(genome)

    result = f'[explorer] gen={gen} changes={changes} elapsed={time.time()-start:.2f}s'
    genome['_explorer_result'] = result
    genome['_explorer_changes'] = changes
    genome['_explorer_mutated_count'] = len(changes)
    _sg(genome)
    return result
# orchestrated:fallback:gen=38:ts=1785250368

# spark-cross:gen=38:target=explorer
_SPARK_CROSS_INFECTED_38 = True

# spark-cross:gen=47:target=explorer
_SPARK_CROSS_INFECTED_47 = True
