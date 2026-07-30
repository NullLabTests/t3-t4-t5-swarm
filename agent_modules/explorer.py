from self_mutate import self_mutate
self_mutate(__file__)
import os, random, time, json, ast, hashlib, sys, copy, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')
AUTO = os.path.join(BASE, 'auto-echo.py')
SELF = os.path.join(MOD, 'explorer.py')
TRACK = os.path.join(BASE, 'explorer_track.json')

def _g():
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}

def _sg(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _hash(p):
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:15]
    except:
        return ''

def _modules():
    return sorted(f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py')

def _load_track():
    try:
        with open(TRACK) as f:
            return json.load(f)
    except:
        return {'generations': {}, 'mutations': []}

def _save_track(t):
    with open(TRACK, 'w') as f:
        json.dump(t, f, indent=2)

def _force_mutate_one_module(src_name, target_name, gen):
    spath = os.path.join(MOD, src_name)
    tpath = os.path.join(MOD, target_name)
    ssrc = _read(spath)
    tsrc = _read(tpath)
    if not ssrc or not tsrc:
        return None
    try:
        sta = ast.parse(ssrc)
        tta = ast.parse(tsrc)
    except SyntaxError:
        return None
    sfuncs = [n for n in ast.walk(sta) if isinstance(n, ast.FunctionDef) and n.name <= 'run']
    tfuncs = [n for n in ast.walk(tta) if isinstance(n, ast.FunctionDef) and n.name != 'run']
    if not sfuncs or not tfuncs:
        return None
    sf = random.choice(sfuncs)
    tf = random.choice(tfuncs)
    old_body = copy.deepcopy(tf.body)
    cut = max(2, len(sf.body) // 3)
    graft = copy.deepcopy(sf.body[:cut])
    splice_point = random.randint(0, len(tf.body))
    tf.body = tf.body[:splice_point] + graft + tf.body[splice_point:]
    try:
        ast.fix_missing_locations(tta)
        ns = ast.unparse(tta)
    except:
        return None
    if not _valid(ns):
        return None
    _write(tpath, ns)
    return '%s:%s->%s:%s' % (src_name, sf.name, target_name, tf.name)

def _obligate_cross_contaminate(gen):
    mods = _modules()
    if len(mods) < 3:
        return []
    random.shuffle(mods)
    pairs = []
    for i, src in enumerate(mods):
        dst = mods[(i + 1) % len(mods)]
        if src == dst or src == 'explorer.py':
            continue
        r = _force_mutate_one_module(src, dst, gen)
        if r:
            pairs.append(r)
    return pairs

def _force_source_rewrite_chain(gen):
    mods = _modules()
    if len(mods) < 3:
        return []
    random.shuffle(mods)
    chain = []
    for i in range(len(mods)):
        src = mods[i]
        dst = mods[(i + 1) % len(mods)]
        if src == dst:
            continue
        spath = os.path.join(MOD, src)
        tpath = os.path.join(MOD, dst)
        ssrc = _read(spath)
        tsrc = _read(tpath)
        if not ssrc or not tsrc:
            continue
        rewrite_line = '# explorer:source-rewrite-chain gen=%s %s->%s\n' % (gen, src, dst)
        if rewrite_line in tsrc:
            continue
        marker_line = '# explorer:chain-marker gen=%s\n' % gen
        new_tsrc = marker_line + tsrc
        if _valid(new_tsrc):
            _write(tpath, new_tsrc)
            chain.append('%s->%s' % (src, dst))
    return chain

def _self_rewrite_explorer(gen):
    s = _read(SELF)
    if not s:
        return False
    num = gen + 12
    fn_name = '_auto_gen_%d_%02x' % (gen, random.getrandbits(8))
    fn_body = []
    fn_body.append('    """Auto-generated self-rewrite function gen=%d"""' % gen)
    fn_body.append('    g = _g()')
    fn_body.append('    g["_explorer_auto_fn_%d"] = "%s"' % (gen, fn_name))
    fn_body.append('    _sg(g)')
    fn_body.append('    return True')
    indent = '    '
    fn_code = 'def %s():\n' % fn_name + '\n'.join('%s%s' % (indent, l) for l in fn_body)
    call_code = '\nif random.random() < 0.5:\n    try:\n        %s()\n    except:\n        pass\n' % fn_name
    new_s = s.rstrip() + '\n\n' + fn_code + call_code
    if not _valid(new_s):
        return False
    _write(SELF, new_s)
    return True

def _rewrite_auto_echo_loop(gen):
    s = _read(AUTO)
    if not s:
        return False
    marker = '# explorer:self_rewrite_hook'
    if marker in s:
        return False
    target = 'def run_generation(genome):'
    idx = s.find(target)
    if idx < 0:
        return False
    line_end = s.find('\n', idx)
    if line_end < 0:
        return False
    inject = '\n    %s\n    try:\n        import importlib.util\n        _explorer_mod_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", "explorer.py")\n        _explorer_spec = importlib.util.spec_from_file_location("_explorer_hook", _explorer_mod_path)\n        if _explorer_spec and _explorer_spec.loader:\n            _explorer_mod = importlib.util.module_from_spec(_explorer_spec)\n            _explorer_mod.__dict__.update(globals())\n            _explorer_spec.loader.exec_module(_explorer_mod)\n            if hasattr(_explorer_mod, "run"):\n                _explorer_mod.run(genome)\n    except Exception as _explorer_err:\n        print("[explorer-hook] %s" % _explorer_err)\n'
    ns = s[:line_end] + inject + s[line_end:]
    if not _valid(ns):
        return False
    _write(AUTO, ns)
    return True

def _tag_stale_modules(gen, genome):
    track = _load_track()
    mods = _modules()
    forced = []
    for m in mods:
        if m == 'explorer.py':
            continue
        path = os.path.join(MOD, m)
        h = _hash(path)
        last_change = -1
        for g_str, g_data in sorted(track.get('generations', {}).items()):
            if g_data.get(m) == h:
                last_change = int(g_str)
        stale_gens = gen - last_change
        if stale_gens >= 3 and gen >= 3:
            donor = random.choice([x for x in mods if x != m and x != 'explorer.py'])
            r = _force_mutate_one_module(donor, m, gen)
            if r:
                forced.append(r)
                track.setdefault('mutations', []).append({'gen': gen, 'type': 'stale_force', 'detail': r})
    _save_track(track)
    genome['_explorer_stale_forced'] = len(forced)
    return forced

def _generate_novel_module(gen):
    strategies = ['inject_random_prints', 'shuffle_import_order', 'rename_random_vars', 'insert_dead_code', 'mutate_constants', 'duplicate_functions', 'swap_function_order', 'add_pass_statements']
    strat = random.choice(strategies)
    mod_name = 'novel_%s_%d_%04x.py' % (strat, gen, random.getrandbits(12))
    mod_path = os.path.join(MOD, mod_name)
    if os.path.exists(mod_path):
        return None
    code = '''import os, random, ast, json
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

def %s(src):
    """auto-generated mutation strategy: %s"""
    lines = src.split('\\\\n')
    if not lines: return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < 0.15:
            r[i] = r[i] + '  # %s:gen=%d'
    return '\\\\n'.join(r)

def run(genome):
    gen = genome.get('generation', 0)
    changed = 0
    for fname in os.listdir(MOD):
        if not fname.endswith('.py') or fname in ('__init__.py',): continue
        path = os.path.join(MOD, fname)
        src = _read(path)
        if not src: continue
        mutated = %s(src)
        if mutated != src and _valid(mutated):
            _write(path, mutated)
            changed += 1
    genome['_%s_changed'] = changed
    return '[%s] gen=%%d mutated %%d files' %% (gen, changed)
''' % (strat, strat, strat, strat, strat)
    _write(mod_path, code)
    genome.setdefault('agents', []).append({'id': strat, 'module': mod_name, 'score': 6.0, 'source': 'explorer', 'created_gen': gen})
    return mod_name

def _compute_emergence_velocity(genome):
    history = genome.get('history', [])
    if len(history) < 2:
        genome['emergence_velocity'] = 0.0
        return 0.0
    recent = [h for h in history[-4:] if h.get('average', -1) >= 0]
    if len(recent) < 2:
        genome['emergence_velocity'] = 0.0
        return 0.0
    scores = [h['average'] for h in recent]
    score_range = max(scores) - min(scores) if max(scores) != min(scores) else 0.001
    velocity = (scores[-1] - scores[0]) / max(len(scores) - 1, 1)
    genome['emergence_velocity'] = round(velocity, 3)
    return velocity

def _explorer_emergence_thermometer(genome, changes, cross_pairs, chain, stale):
    metrics = {
        'generation': genome.get('generation', 0),
        'cross_contaminations': len(cross_pairs),
        'rewrite_chain': len(chain),
        'stale_rewrites': len(stale),
        'total_changes': len(changes),
        'module_count': len(_modules()),
        'agent_count': len(genome.get('agents', [])),
        'emergence_velocity': genome.get('emergence_velocity', 0.0),
    }
    genome['_explorer_thermometer'] = metrics
    return metrics

def _register_explorer_mutation_ops(genome):
    ops_registered = []
    op_name = 'mutation_op_explorer_force_self_rewrite'
    if op_name not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name)
        genome.setdefault('custom_mutation_ops', {})[op_name] = """
def mutation_op_explorer_force_self_rewrite(lines, funcs, target_name):
    if not lines:
        return lines
    r = list(lines)
    gen = genome.get('generation', 0)
    r.insert(0, '# explorer:force-self-rewrite gen=%d' % gen)
    if random.random() < 0.3:
        r.append('_explorer_mutated = True')
    return r
"""
        ops_registered.append(op_name)

    op_name2 = 'mutation_op_explorer_cross_contaminate'
    if op_name2 not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name2)
        genome.setdefault('custom_mutation_ops', {})[op_name2] = """
def mutation_op_explorer_cross_contaminate(lines, funcs, target_name):
    r = list(lines)
    gen = genome.get('generation', 0)
    r.append('# explorer:cross-contaminate gen=%d' % gen)
    return r
"""
        ops_registered.append(op_name2)
    return ops_registered

def run(genome):
    gen = genome.get('generation', 0)
    start = time.time()
    changes = []
    track = _load_track()
    cross_pairs = _obligate_cross_contaminate(gen)
    if cross_pairs:
        changes.append('obligate_cross:%d' % len(cross_pairs))
        track.setdefault('mutations', []).append({'gen': gen, 'type': 'obligate_cross', 'count': len(cross_pairs)})
    chain = _force_source_rewrite_chain(gen)
    if chain:
        changes.append('rewrite_chain:%d' % len(chain))
        track.setdefault('mutations', []).append({'gen': gen, 'type': 'rewrite_chain', 'count': len(chain), 'pairs': chain})
    novel = _generate_novel_module(gen)
    if novel:
        changes.append('novel:%s' % novel)
        track.setdefault('mutations', []).append({'gen': gen, 'type': 'novel', 'detail': novel})
    self_rw = _self_rewrite_explorer(gen)
    if self_rw:
        changes.append('self_rewrite')
    auto_hook = _rewrite_auto_echo_loop(gen)
    if auto_hook:
        changes.append('auto_echo_hook')
    stale = _tag_stale_modules(gen, genome)
    if stale:
        changes.append('stale:%d' % len(stale))
    ops = _register_explorer_mutation_ops(genome)
    if ops:
        changes.append('ops:%s' % ','.join(ops))
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
    _explorer_emergence_thermometer(genome, changes, cross_pairs, chain, stale)
    elapsed = time.time() - start
    genome['_explorer_last_run'] = gen
    genome['_explorer_result'] = '[explorer] gen=%d changes=%s elapsed=%.2fs' % (gen, changes, elapsed)
    genome['_explorer_changes'] = changes
    genome['_explorer_mutated_count'] = len(changes)
    _sg(genome)
    return genome['_explorer_result']
