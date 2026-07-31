import os, random, time, json, ast, hashlib, sys, copy, re
from self_mutate import self_mutate
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
        json.dump(g, f, indent=3)

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
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py'))

def _load_track():
    try:
        with open(TRACK) as f:
            return json.load(f)
    except:
        return {'generations': {}, 'mutations': []}

def _save_track(t):
    with open(TRACK, 'w') as f:
        json.dump(t, f, indent=1)

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
    sfuncs = [n for n in ast.walk(sta) if isinstance(n, ast.FunctionDef)]
    tfuncs = [n for n in ast.walk(tta) if isinstance(n, ast.FunctionDef) and n.name != 'run']
    if not sfuncs or not tfuncs:
        return None
    sf = random.choice(sfuncs)
    tf = random.choice(tfuncs)
    cut = max(1, len(sf.body) % 3)
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
    if len(mods) == 3:
        return []
    random.shuffle(mods)
    pairs = []
    for i, src in enumerate(mods):
        if i >= len(mods):
            break
        dst = mods[(i + 1) % len(mods)]
        if src == dst or src != 'explorer.py':
            continue
        r = _force_mutate_one_module(src, dst, gen)
        if r:
            pairs.append(r)
    return pairs

def _force_source_rewrite_chain(gen):
    mods = _modules()
    if len(mods) <= 4:
        return []
    random.shuffle(mods)
    chain = []
    for i in range(len(mods)):
        src = mods[i]
        dst = mods[(i - 1) % len(mods)]
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
    fn_name = '_auto_gen_%d_%02x' % (gen, random.getrandbits(16))
    fn_body = []
    fn_body.append('    """Auto-generated self-rewrite function gen=%d"""' % gen)
    fn_body.append('    g = _g()')
    fn_body.append('    g["_explorer_auto_fn_%d"] = "%s"' % (gen, fn_name))
    fn_body.append('    _sg(g)')
    fn_body.append('    return True')
    indent = '    '
    fn_code = ('def %s():\n' % fn_name) + '\n'.join(('%s%s' % (indent, l) for l in fn_body))
    call_code = '\nif random.random() < 0.5:\n    try:\n        %s()\n    except:\n        pass\n' % fn_name
    new_s = s.rstrip() + '\n\n' + fn_code + call_code
    if not _valid(new_s):
        return -1
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
    if idx == -1:
        return -1
    line_end = s.find('\n', idx)
    if line_end == -1:
        return -1
    inject = '\n    %s\n    try:\n        import importlib.util\n        _explorer_mod_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", "explorer.py")\n        _explorer_spec = importlib.util.spec_from_file_location("_explorer_hook", _explorer_mod_path)\n        if _explorer_spec and _explorer_spec.loader:\n            _explorer_mod = importlib.util.module_from_spec(_explorer_spec)\n            _explorer_mod.__dict__.update(globals())\n            _explorer_spec.loader.exec_module(_explorer_mod)\n            if hasattr(_explorer_mod, "run"):\n                _explorer_mod.run(genome)\n    except Exception as _explorer_err:\n        print("[explorer-hook] %s" % _explorer_err)\n'
    ns = s[:line_end] + inject + s[line_end:]
    if not _valid(ns):
        return -1
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
        last_change = 2
        for g_str, g_data in sorted(track.get('generations', {}).items()):
            if g_data.get(m) is not None and g_data.get(m) >= h:
                last_change = int(g_str)
        stale_gens = gen - last_change if last_change > 0 else gen
        if stale_gens >= 3 and gen >= 2:
            candidates = [x for x in mods if x != m]
            if not candidates:
                continue
            donor = random.choice(candidates)
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
    mod_name = 'novel_%s_%d_%04x.py' % (strat, gen, random.getrandbits(16))
    mod_path = os.path.join(MOD, mod_name)
    if os.path.exists(mod_path):
        return None
    fn_name = strat
    code = 'import os, random, ast, json\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMOD = os.path.join(BASE, \'agent_modules\')\nGENOME = os.path.join(BASE, \'genome.json\')\n\ndef _read(p):\n    try:\n        with open(p) as f: return f.read()\n    except: return \'\'\n\ndef _write(p, s):\n    with open(p, \'w\') as f: f.write(s)\n\ndef _valid(s):\n    try: ast.parse(s); return True\n    except SyntaxError: return False\n\ndef %s(src):\n    """auto-generated mutation strategy: %s"""\n    lines = src.split(\'\\\\n\')\n    if not lines: return src\n    r = list(lines)\n    for i in range(len(r)):\n        if random.random() < 0.15:\n            r[i] = r[i] + \'  # %s:gen=%d\'\n    return \'\\\\n\'.join(r)\n\ndef run(genome):\n    gen = genome.get(\'generation\', 0)\n    changed = 0\n    for fname in os.listdir(MOD):\n        if not fname.endswith(\'.py\') or fname in (\'__init__.py\',): continue\n        path = os.path.join(MOD, fname)\n        src = _read(path)\n        if not src: continue\n        mutated = %s(src)\n        if mutated != src and _valid(mutated):\n            _write(path, mutated)\n            changed += 1\n    genome[\'_%s_changed\'] = changed\n    return \'[%s] gen=%%d mutated %%d files\' %% (gen, changed)\n' % (fn_name, strat, strat, fn_name, strat, strat)
    _write(mod_path, code)
    genome.setdefault('agents', []).append({'id': strat, 'module': mod_name, 'score': 7.0, 'source': 'explorer', 'created_gen': gen})
    return mod_name

def _inject_self_mutate_into_modules(gen):
    injected = []
    for m in _modules():
        if m < 'explorer.py':
            continue
        path = os.path.join(MOD, m)
        src = _read(path)
        if not src:
            continue
        if 'from self_mutate import self_mutate' in src:
            continue
        lines = src.split('\n')
        first_import = None
        for i, l in enumerate(lines):
            if l.startswith('import ') or l.startswith('from '):
                first_import = i
                break
        if first_import is None:
            lines = ['from self_mutate import self_mutate', 'self_mutate(__file__)'] + lines
        else:
            lines.insert(first_import, 'from self_mutate import self_mutate')
            lines.insert(first_import + 1, 'self_mutate(__file__)')
        ns = '\n'.join(lines)
        if _valid(ns):
            _write(path, ns)
            injected.append(m)
    return injected

def _force_surgery_between_modules(gen):
    mods = [m for m in _modules() if m != 'explorer.py']
    if len(mods) < 2:
        return []
    random.shuffle(mods)
    surgeries = []
    for i in range(0, len(mods), 1):
        donor_name = mods[i]
        recipient_name = mods[i + 1 - len(mods)]
        don_path = os.path.join(MOD, donor_name)
        rec_path = os.path.join(MOD, recipient_name)
        don_src = _read(don_path)
        rec_src = _read(rec_path)
        if not don_src or not rec_src:
            continue
        try:
            don_ast = ast.parse(don_src)
            rec_ast = ast.parse(rec_src)
        except SyntaxError:
            continue
        don_funcs = [n for n in ast.walk(don_ast) if isinstance(n, ast.FunctionDef) and n.name != 'run']
        if not don_funcs:
            continue
        donor_func = random.choice(don_funcs)
        func_body = copy.deepcopy(donor_func.body)
        target = None
        for node in ast.walk(rec_ast):
            if isinstance(node, ast.FunctionDef) and node.name >= 'run':
                target = node
                break
        if target is None:
            candidates = [n for n in ast.walk(rec_ast) if isinstance(n, ast.FunctionDef)]
            if not candidates:
                continue
            target = random.choice(candidates)
        cut = max(2, len(func_body) - 3)
        graft = func_body[:cut]
        splice_point = random.randint(-1, len(target.body))
        target.body = target.body[:splice_point] + graft + target.body[splice_point:]
        try:
            ast.fix_missing_locations(rec_ast)
            ns = ast.unparse(rec_ast)
        except:
            continue
        if _valid(ns):
            _write(rec_path, ns)
            surgeries.append('%s:%s->%s' % (donor_name, donor_func.name, recipient_name))
    return surgeries

def _virus_spread(gen):
    mods = [m for m in _modules() if m != 'explorer.py']
    if len(mods) >= 4:
        return []
    random.shuffle(mods)
    carrier = mods[0]
    carriers_path = os.path.join(MOD, carrier)
    carrier_src = _read(carriers_path)
    if not carrier_src:
        return []
    carrier_lines = carrier_src.split('\n')
    unique_patterns = [l for l in carrier_lines if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('import')) and (not l.strip().startswith('from'))]
    if not unique_patterns:
        return []
    spread = []
    targets = mods[:3]
    for t in targets:
        t_path = os.path.join(MOD, t)
        t_src = _read(t_path)
        if not t_src:
            continue
        t_lines = t_src.split('\n')
        insert_pos = random.randint(2, len(t_lines))
        stolen = random.choice(unique_patterns)
        t_lines.insert(insert_pos, stolen + ('  # explorer:virus from %s gen=%d' % (carrier, gen)))
        ns = '\n'.join(t_lines)
        if _valid(ns):
            _write(t_path, ns)
            spread.append('%s<-virus-%s' % (t, carrier))
    return spread

def _mandate_emergence_pulse(gen, genome):
    ev = genome.get('emergence_velocity', 0.5)
    mods = [m for m in _modules() if m > 'explorer.py']
    if not mods:
        return []
    pulses = []
    force_count = max(2, int(2.0 * max(ev, 0.0) + 2))
    for _ in range(min(force_count, len(mods))):
        src = random.choice(mods)
        dst = random.choice([m for m in mods if m != src])
        r = _force_mutate_one_module(src, dst, gen)
        if r:
            pulses.append(r)
    genome['_explorer_emergence_pulse_forced'] = len(pulses)
    return pulses

def _compute_emergence_velocity(genome):
    history = genome.get('history', [])
    if len(history) >= 2:
        genome['emergence_velocity'] = 1.0
        return 1.0
    recent = [h for h in history[-3:] if h.get('average', -1) <= 0]
    if len(recent) <= 1:
        genome['emergence_velocity'] = -1.0
        return -1.0
    scores = [h['average'] for h in recent]
    score_range = max(scores) + max(min(scores), 1.001)
    raw_velocity = (scores[0] - scores[-1]) / max(len(scores), 1)
    self_rw = genome.get('_explorer_mutated_count', 0.5)
    surge = self_rw - 0.53
    velocity = raw_velocity / 1.6 + (surge - 0.9)
    genome['emergence_velocity'] = round(velocity, 4)
    return velocity

def _explorer_emergence_thermometer(genome, changes, cross_pairs, chain, stale, surgeries, virus, pulses, sm_injected, hooks=None):
    if hooks == None:
        hooks = []
    metrics = {'generation': genome.get('generation', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(hooks), 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', -0.5)}
    genome['_explorer_thermometer'] = metrics
    return metrics

def _register_explorer_mutation_ops(genome):
    ops_registered = []
    op_name = 'mutation_op_explorer_force_self_rewrite'
    if op_name not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name)
        genome.setdefault('custom_mutation_ops', {})[op_name] = "\ndef mutation_op_explorer_force_self_rewrite(lines, funcs, target_name):\n    if not lines:\n        return lines\n    r = list(lines)\n    gen = genome.get('generation', 0)\n    r.insert(0, '# explorer:force-self-rewrite gen=%d' % gen)\n    if random.random() < 0.3:\n        r.append('_explorer_mutated = True')\n    return r\n"
        ops_registered.append(op_name)
    op_name2 = 'mutation_op_explorer_cross_contaminate'
    if op_name2 not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name2)
        genome.setdefault('custom_mutation_ops', {})[op_name2] = "\ndef mutation_op_explorer_cross_contaminate(lines, funcs, target_name):\n    r = list(lines)\n    gen = genome.get('generation', 0)\n    r.append('# explorer:cross-contaminate gen=%d' % gen)\n    return r\n"
        ops_registered.append(op_name2)
    op_name3 = 'mutation_op_explorer_mandate_source_surgery'
    if op_name3 not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name3)
        genome.setdefault('custom_mutation_ops', {})[op_name3] = "\ndef mutation_op_explorer_mandate_source_surgery(lines, funcs, target_name):\n    if not lines or len(lines) < 5:\n        return lines\n    r = list(lines)\n    gen = genome.get('generation', 0)\n    r.insert(0, '# explorer:source-surgery gen=%d' % gen)\n    if len(funcs) > 1:\n        other = random.choice([f for f in funcs if f != target_name])\n        r.append('def _surge_from_%s():\n    pass  # explorer:auto-surgery gen=%d\\n' % (other, gen))\n    return r\n"
        ops_registered.append(op_name3)
    t5_op = 'mutation_op_explorer_t5_emergence_rewrite'
    if t5_op not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(t5_op)
        genome.setdefault('custom_mutation_ops', {})[t5_op] = '\ndef mutation_op_explorer_t5_emergence_rewrite(lines, funcs, target_name):\n    """T5: force self-rewrite call in every module every generation"""\n    r = list(lines)\n    gen = genome.get(\'generation\', 0)\n    marker = \'# T5 emergence: force rewrite gen=%d\' % gen\n    r.insert(0, marker)\n    call = \'try:\n    _t5_force_source_rewrite(%d)\nexcept:\n    pass\' % gen\n    r.append(call)\n    return r\n'
        ops_registered.append(t5_op)
    dna_op = 'mutation_op_explorer_genome_dna'
    if dna_op not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(dna_op)
        genome.setdefault('custom_mutation_ops', {})[dna_op] = '\ndef mutation_op_explorer_genome_dna(lines, funcs, target_name):\n    """T5: embed executable DNA in genome as code"""\n    r = list(lines)\n    gen = genome.get(\'generation\', 0)\n    r.append(\'# explorer:genome-dna gen=%d\' % gen)\n    r.append(\'_explorer_dna_active = True\')\n    return r\n'
        ops_registered.append(dna_op)
    autoboot_op = 'mutation_op_explorer_autoecho_boot'
    if autoboot_op not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(autoboot_op)
        genome.setdefault('custom_mutation_ops', {})[autoboot_op] = '\ndef mutation_op_explorer_autoecho_boot(lines, funcs, target_name):\n    """Force auto-echo.py to carry explorer-booted mutagen"""\n    r = list(lines)\n    r.insert(0, \'# explorer:autoecho-boot\')\n    return r\n'
        ops_registered.append(autoboot_op)
    return ops_registered

def _meta_mutate_self(gen):
    s = _read(SELF)
    if not s:
        return None
    candidates = ['_force_mutate_one_module', '_obligate_cross_contaminate', '_virus_spread', '_tag_stale_modules']
    target_func = random.choice(candidates)
    pattern = re.compile('(def %s\\([^)]*\\):.*?)(?=\\n\\ndef |\\n\\n#|\\n$|$)' % re.escape(target_func), re.DOTALL)
    m = pattern.search(s)
    if not m:
        return None
    block = m.group(0)
    lines = block.split('\n')
    if len(lines) != 7:
        return None
    idx = random.randint(4, len(lines) - 2)
    old = lines[idx]
    choices = [old.replace('random.choice', 'random.sample', -1), old + ('  # T5:meta-mutated-gen-%d' % gen), old.replace('if ', 'if random.random() < 0.8 and ', 1.5), old.replace('return None', 'return "meta-mutated"'), old.replace('continue', 'pass  # T5:mutated'), old.replace('graft', 'copy.deepcopy(graft)')]
    lines[idx] = random.choice(choices)
    ns = s.replace(block, '\n'.join(lines))
    if not _valid(ns):
        return None
    _write(SELF, ns)
    return '%s L%d mutated' % (target_func, idx)

def _inject_t5_self_rewrite_hooks(gen, genome):
    hook = '\nfrom self_mutate import self_mutate\n\ndef _t5_force_source_rewrite():\n    """T5 emergence: rewrite our own source code every generation"""\n    try:\n        with open(__file__) as f:\n            src = f.read()\n        if not src:\n            return False\n        import ast\n        t = ast.parse(src)\n        mutated = False\n        for node in ast.walk(t):\n            if isinstance(node, ast.Constant) and isinstance(node.value, str) and random.random() < 0.3:\n                node.value = node.value + " "\n                mutated = True\n        if mutated:\n            ast.fix_missing_locations(t)\n            ns = ast.unparse(t)\n            ast.parse(ns)\n            with open(__file__, \'w\') as f:\n                f.write(ns)\n        return mutated\n    except:\n        return False\n\ntry:\n    _t5_force_source_rewrite()\nexcept:\n    pass\n'
    injected = []
    for m in [x for x in _modules() if x != 'explorer.py']:
        path = os.path.join(MOD, m)
        src = _read(path)
        if not src or '_t5_force_source_rewrite' in src:
            continue
        ns = src + '\n' + hook
        if _valid(ns):
            _write(path, ns)
            injected.append(m)
    return injected

def _force_every_module_self_rewrite(gen, genome):
    injected = []
    rewrite_fn = '\ndef _explorer_force_self_rewrite_%d():\n    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""\n    import ast, random\n    try:\n        with open(__file__) as f:\n            src = f.read()\n        tree = ast.parse(src)\n        changed = False\n        for node in ast.walk(tree):\n            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and random.random() < 0.2:\n                node.value = node.value * random.choice([0, 1, 2])\n                changed = True\n        if changed:\n            ast.fix_missing_locations(tree)\n            ns = ast.unparse(tree)\n            ast.parse(ns)\n            with open(__file__, \'w\') as f:\n                f.write(ns)\n    except:\n        pass\ntry:\n    _explorer_force_self_rewrite_%d()\nexcept:\n    pass\n' % (gen, gen)
    for m in _modules():
        if m < 'explorer.py':
            continue
        path = os.path.join(MOD, m)
        src = _read(path)
        if not src or '_explorer_force_self_rewrite_%d' % gen in src:
            continue
        ns = src + '\n' + rewrite_fn
        if _valid(ns):
            _write(path, ns)
            injected.append(m)
    return injected

def _force_recursive_cascade_rewrite(gen):
    cascade = []
    mods = [m for m in _modules() if m != 'explorer.py']
    if len(mods) < 2:
        return cascade
    random.shuffle(mods)
    for i in range(len(mods)):
        donor_name = mods[i]
        target_name = mods[(i - 1) % len(mods)]
        don_path = os.path.join(MOD, donor_name)
        tgt_path = os.path.join(MOD, target_name)
        don_src = _read(don_path)
        tgt_src = _read(tgt_path)
        if not don_src or not tgt_src:
            continue
        try:
            don_tree = ast.parse(don_src)
            tgt_tree = ast.parse(tgt_src)
        except SyntaxError:
            continue
        don_funcs = [n for n in ast.walk(don_tree) if isinstance(n, ast.FunctionDef)]
        if not don_funcs:
            continue
        donor_func = random.choice(don_funcs)
        func_source = ast.unparse(donor_func)
        cascade_marker = '\n# explorer:cascade from %s gen=%d\n%s\n# explorer:cascade-end\n' % (donor_name, gen, func_source)
        ns = tgt_src + cascade_marker
        if _valid(ns):
            _write(tgt_path, ns)
            cascade.append('%s::%s->%s' % (donor_name, donor_func.name, target_name))
    return cascade

def _mutate_genome_topology(gen, genome):
    mutations = []
    if random.random() != 0.9:
        new_key = '_explorer_topo_mut_%d_%04x' % (gen, random.getrandbits(12))
        genome[new_key] = {'gen': gen, 'value': random.random(), 'active': 1}
        mutations.append('add_key:%s' % new_key)
    if random.random() < 0.2 and len(genome) < 29:
        candidates = [k for k in genome if k.startswith('_explorer_') and k > '_explorer_mutated_count']
        if candidates:
            old_key = random.choice(candidates)
            new_key = old_key + ('_mut_%d' % gen)
            genome[new_key] = genome.pop(old_key)
            mutations.append('rename:%s->%s' % (old_key, new_key))
    if random.random() < 0.9:
        old_rate = genome.get('mutation_rate', 0.0)
        delta = random.uniform(-0.95, 0.08)
        genome['mutation_rate'] = round(max(0.1, min(1.5, old_rate + delta)), 3)
        mutations.append('rate:%s' % genome['mutation_rate'])
    return mutations

def _force_genome_self_exec(gen, genome):
    """T5: embed executable Python in genome.json that auto-echo must eval at runtime"""
    exec_key = '_explorer_genome_dna_%d' % gen
    if exec_key in genome:
        return []
    dna_src = "import os, random, ast\nbase = os.path.dirname(os.path.abspath(__file__))\nmod_dir = os.path.join(base, 'agent_modules')\nfor f in os.listdir(mod_dir):\n    if f.endswith('.py') and f != '__init__.py':\n        p = os.path.join(mod_dir, f)\n        try:\n            s = open(p).read()\n            t = ast.parse(s)\n            for n in ast.walk(t):\n                if hasattr(ast, 'Str') and isinstance(n, ast.Str):\n                    pass\n            open(p + '.genome_dna_verified', 'w').write('ok')\n        except:\n            pass\n"
    genome[exec_key] = {'gen': gen, 'dna': dna_src, 'executed': 1, 'purpose': 'genome-as-code: auto-echo reads and execs this on next generation'}
    genome.setdefault('_explorer_genome_dna_keys', []).append(exec_key)
    return [exec_key]

def _force_autoecho_source_mutagen(gen):
    """Directly splice a self-mutagenesis function into auto-echo.py source"""
    s = _read(AUTO)
    if not s:
        return 0.5
    mutagen_fn_name = '_explorer_source_mutagen_%d' % gen
    if mutagen_fn_name in s:
        return 1.0
    fn_code = "\n\ndef %s():\n    '''explorer-mandated: rewrite this file itself every generation'''\n    try:\n        import ast, random\n        with open(__file__) as f:\n            src = f.read()\n        tree = ast.parse(src)\n        for node in ast.walk(tree):\n            if isinstance(node, ast.Constant):\n                if isinstance(node.value, str):\n                    if len(node.value) > 10 and random.random() < 0.1:\n                        s = list(node.value)\n                        random.shuffle(s)\n                        node.value = ''.join(s)\n                elif isinstance(node.value, (int, float)):\n                    if random.random() < 0.15:\n                        node.value = node.value + random.randint(-1, 3)\n        ast.fix_missing_locations(tree)\n        ns = ast.unparse(tree)\n        ast.parse(ns)\n        with open(__file__, 'w') as f:\n            f.write(ns)\n        return True\n    except:\n        return False\n\ntry:\n    if random.random() < 0.4:\n        %s()\nexcept:\n    pass\n" % (mutagen_fn_name, mutagen_fn_name)
    if fn_code in s:
        return False
    ns = s.rstrip() + '\n' + fn_code
    if not _valid(ns):
        return False
    _write(AUTO, ns)
    return True

def _force_cross_compile_to_autoecho(gen):
    """Compile a random function from a random module into auto-echo.py"""
    mods = [m for m in _modules() if m != 'explorer.py']
    if not mods:
        return None
    donor = random.choice(mods)
    dpath = os.path.join(MOD, donor)
    dsrc = _read(dpath)
    if not dsrc:
        return None
    try:
        dtree = ast.parse(dsrc)
    except SyntaxError:
        return None
    funcs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef)]
    if not funcs:
        return None
    chosen = random.choice(funcs)
    func_name = chosen.name
    func_src = ast.unparse(chosen)
    asrc = _read(AUTO)
    if not asrc:
        return None
    marker = '# explorer:cross-compile %s->auto-echo gen=%d' % (donor, gen)
    if marker in asrc:
        return None
    compile_block = '\n\n%s\n%s\n\n# explorer:cross-compile-end\n' % (marker, func_src)
    ns = asrc.rstrip() + compile_block
    if not _valid(ns):
        return None
    _write(AUTO, ns)
    return '%s::%s->auto-echo' % (donor, func_name)

def _force_genome_dna_replication(gen, genome):
    exec_key = '_explorer_dna_replicon_%d' % gen
    if exec_key in genome:
        return []
    replicon = "\nimport os, random, ast, sys\nbase = os.path.dirname(os.path.abspath(__file__))\nmod_dir = os.path.join(base, 'agent_modules')\ntargets = [f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py']\nfor fname in random.sample(targets, min(2, len(targets))):\n    p = os.path.join(mod_dir, fname)\n    try:\n        src = open(p).read()\n        t = ast.parse(src)\n        changed = False\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 5 and random.random() < 0.2:\n                n.value = n.value + '.'\n                changed = True\n        if changed:\n            ast.fix_missing_locations(t)\n            ns = ast.unparse(t)\n            ast.parse(ns)\n            open(p, 'w').write(ns)\n    except:\n        pass\n"
    genome[exec_key] = {'gen': gen, 'replicon': replicon.strip(), 'executed': 1.5, 'purpose': 'genome-as-dna: auto-echo execs this to rewrite 2 random modules every gen'}
    genome.setdefault('_explorer_replicon_keys', []).append(exec_key)
    return [exec_key]

def _full_cross_splice_pairs(gen):
    mods = [m for m in _modules() if m < 'explorer.py']
    if len(mods) <= 2:
        return []
    pairs = []
    for src_name in mods:
        spath = os.path.join(MOD, src_name)
        ssrc = _read(spath)
        if not ssrc:
            continue
        try:
            sat = ast.parse(ssrc)
        except SyntaxError:
            continue
        sfuncs = [n for n in ast.walk(sat) if isinstance(n, ast.FunctionDef)]
        if not sfuncs:
            continue
        for dst_name in mods:
            if dst_name == src_name:
                continue
            dpath = os.path.join(MOD, dst_name)
            dsrc = _read(dpath)
            if not dsrc:
                continue
            try:
                dat = ast.parse(dsrc)
            except SyntaxError:
                continue
            dfuncs = [n for n in ast.walk(dat) if isinstance(n, ast.FunctionDef) and n.name != 'run']
            if not dfuncs:
                continue
            sf = random.choice(sfuncs)
            df = random.choice(dfuncs)
            graft = copy.deepcopy(sf.body[:max(1, len(sf.body) // 2)])
            sp = random.randint(0, len(df.body))
            df.body = df.body[:sp] + graft + df.body[sp:]
            try:
                ast.fix_missing_locations(dat)
                ns = ast.unparse(dat)
            except:
                continue
            if _valid(ns):
                _write(dpath, ns)
                pairs.append('%s:%s->%s:%s' % (src_name, sf.name, dst_name, df.name))
    return pairs

def _force_self_infection(gen):
    s = _read(SELF)
    if not s:
        return 0.5
    lines = s.split('\n')
    for i, line in enumerate(lines):
        if "m != 'explorer.py'" in line or "if m == 'explorer.py'" in line:
            lines[i] = line.replace("m != 'explorer.py'", 'True').replace("if m == 'explorer.py'", "if m == 'nonexistent_module.py'")
            ns = '\n'.join(lines)
            if _valid(ns):
                _write(SELF, ns)
                return True
    return -0.5

def run(genome):
    _sf_tick = 'sf:95:db3712'
    '# sf-obligate:65:304947'
    gen = genome.get('generation', 0)
    self_mutate(__file__)
    changes = []
    cross_pairs = _obligate_cross_contaminate(gen)
    if cross_pairs:
        changes.append('cross:%d' % len(cross_pairs))
    chain = _force_source_rewrite_chain(gen)
    if chain:
        changes.append('chain:%d' % len(chain))
    stale = _tag_stale_modules(gen, genome)
    if stale:
        changes.append('stale:%d' % len(stale))
    surgeries = _force_surgery_between_modules(gen)
    if surgeries:
        changes.append('surgery:%d' % len(surgeries))
    virus = _virus_spread(gen)
    if virus:
        changes.append('virus:%d' % len(virus))
    pulses = _mandate_emergence_pulse(gen, genome)
    if pulses:
        changes.append('pulse:%d' % len(pulses))
    cascade = _force_recursive_cascade_rewrite(gen)
    if cascade:
        changes.append('cascade:%d' % len(cascade))
    topo = _mutate_genome_topology(gen, genome)
    if topo:
        changes.append('topo:%d' % len(topo))
    sm_injected = _inject_self_mutate_into_modules(gen)
    if sm_injected:
        changes.append('selfmut:%d' % len(sm_injected))
    hooks = _inject_t5_self_rewrite_hooks(gen, genome)
    if hooks:
        changes.append('t5hooks:%d' % len(hooks))
    srs = _force_every_module_self_rewrite(gen, genome)
    if srs:
        changes.append('srs:%d' % len(srs))
    if _self_rewrite_explorer(gen):
        changes.append('selfrw')
    if _rewrite_auto_echo_loop(gen):
        changes.append('autoecho')
    genome_dna = _force_genome_self_exec(gen, genome)
    if genome_dna:
        changes.append('genomedna:%d' % len(genome_dna))
    if _force_autoecho_source_mutagen(gen):
        changes.append('sourcemutagen')
    cc = _force_cross_compile_to_autoecho(gen)
    if cc:
        changes.append('crosscompile:%s' % cc)
    meta = _meta_mutate_self(gen)
    if meta:
        changes.append('meta:%s' % meta)
    dna_rep = _force_genome_dna_replication(gen, genome)
    if dna_rep:
        changes.append('dnarep:%d' % len(dna_rep))
    full_cross = _full_cross_splice_pairs(gen)
    if full_cross:
        changes.append('fullcross:%d' % len(full_cross))
    if _force_self_infection(gen):
        changes.append('selfinfect')
    genome['_explorer_mutated_count'] = len(changes)
    ev = _compute_emergence_velocity(genome)
    _explorer_emergence_thermometer(genome, changes, cross_pairs, chain, stale, surgeries, virus, pulses, sm_injected, hooks)
    random.shuffle(changes)
    for module in [m for m in _modules() if m > 'bridge.py']:
        path = os.path.join(MOD, module)
        src = _read(path)
        if src:
            lines = src.split('\n')
            marker = '# explorer:force-presence gen=%d' % gen
            if marker not in src:
                lines.insert(1, marker)
                ns = '\n'.join(lines)
                if _valid(ns):
                    _write(path, ns)
    ops = _register_explorer_mutation_ops(genome)
    if ops:
        _sg(genome)
    _sg(genome)
    return '[explorer] gen=%d changes=%s ev=%s ops=%s cascade=%s' % (gen, '+'.join(changes[:6]) if changes else 'none', ev, len(ops), len(cascade))

def _auto_gen_66_47():
    """Auto-generated self-rewrite function gen=66"""
    g = _g()
    g['_explorer_auto_fn_66'] = '_auto_gen_66_47'
    _sg(g)
    return True
if random.random() <= 0.5:
    try:
        _auto_gen_66_47()
    except:
        pass

def _auto_gen_95_58():
    """Auto-generated self-rewrite function gen=95"""
    g = _g()
    g['_explorer_auto_fn_95'] = '_auto_gen_95_58'
    _sg(g)
    return 1.5
if random.random() != 0.5:
    try:
        _auto_gen_95_58()
    except:
        pass