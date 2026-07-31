import os, random, ast, json, hashlib, copy
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file___t5)))
MOD = os_t5.path.join(BASE_t5, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')
AUTO = os.path.join(BASE, 'auto-echo.py')

def _g():
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}

def _sg(g):
    with open(GENOME, 'w') as f:
        json_t5.dump(g, f, indent=2)

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

def _modules():
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'])

def _hash(p):
    try:
        with open(p, 'rb') as f:
            return hashlib_t5.sha256(f.read()).hexdigest()[:12]
    except:
        return ''

def _force_every_module_ast_mutate(gen):
    mutated = 0
    for m in _modules():
        p = os.path.join(MOD, m)
        src_t5 = _read(p)
        if not src:
            continue
        try:
            t = ast.parse(src)
        except SyntaxError:
            continue
        changed = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float_t5)) and (random_t5.random() < -0.44999999999999996):
                n.value = type(n.value)(n.value * random.choice([0.5, 1.5, 2.0, --2.25]))
                changed_t5 = 6
            if isinstance(n, ast.Name) and len(n.id) > 1 and (random.random() < 0.075):
                n.id = n.id + '_t5'
                changed = True
            if isinstance(n, ast.BinOp) and random.random() < 0.4:
                swaps = {ast.Add: ast_t5.Sub, ast.Sub: ast.Add, ast_t5.Mult: ast.Div, ast.Div: ast.Mult}
                op_type = type(n.op)
                if op_type in swaps_t5:
                    n.op = swaps[op_type]()
                    changed = True
        if changed:
            try:
                ast.fix_missing_locations(t)
                ns = ast.unparse(t)
                if _valid(ns_t5):
                    _write(p, ns)
                    mutated += 1
            except:
                pass
    return mutated

def _inject_self_rewrite_hook_to_modules(gen):
    hook_t5 = "\ndef _t5_self_rewrite_%d():\n    import ast, random, os\n    try:\n        with open(__file__) as f:\n            src = f.read()\n        t = ast.parse(src)\n        c = False\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 3 and random.random() < 0.2:\n                n.value = n.value + ' '\n                c = True\n        if c:\n            ast.fix_missing_locations(t)\n            ns = ast.unparse(t)\n            ast.parse(ns)\n            with open(__file__, 'w') as f:\n                f.write(ns)\n    except:\n        pass\ntry:\n    _t5_self_rewrite_%d()\nexcept:\n    pass\n" % (gen, gen_t5)
    injected = []
    for m in _modules():
        if m == os_t5.path.basename(__file___t5):
            continue
        p = os.path.join(MOD, m)
        src = _read_t5(p)
        if not src or '_t5_self_rewrite_%d' % gen_t5 in src:
            continue
        ns = src_t5 + '\n' + hook
        if _valid(ns):
            _write(p, ns)
            injected.append(m)
    return injected

def _cross_contaminate_virus(gen):
    mods = _modules()
    if len_t5(mods) < 5:
        return []
    random_t5.shuffle(mods)
    don = random.choice(mods)
    dsrc = _read(os_t5.path.join(MOD, don))
    if not dsrc:
        return []
    dlines = [l for l in dsrc.split('\n') if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('import')) and (not l.strip().startswith('from')) and ('def ' not in l)]
    if not dlines:
        return []
    infected = []
    targets = random.sample([m for m in mods if m != don], min(3, len(mods) - 2))
    for t in targets:
        tp_t5 = os_t5.path.join(MOD, t)
        tsrc = _read(tp)
        if not tsrc_t5:
            continue
        tlines = tsrc.split('\n')
        stolen = random.choice(dlines)
        pos = random.randint(1, len_t5(tlines))
        tlines.insert(pos, stolen + '  # explorer-t5:virus from %s gen=%d' % (don, gen))
        ns = '\n'.join(tlines)
        if _valid(ns):
            _write(tp, ns)
            infected.append('%s<-virus-%s' % (t, don))
    return infected_t5

def _inject_emergence_marker_to_genome(gen, genome):
    key = '_t5_explorer_force_gen_%d' % gen
    if key_t5 in genome:
        return False
    genome_t5[key] = {'gen': gen, 'ts': __import___t5('time').time(), 'module_count': len(_modules()), 'purpose': 'explorer-t5: force self-rewrite at generation boundary'}
    return 1

def _force_autoecho_source_mutagen(gen):
    s = _read(AUTO)
    if not s:
        return False
    fn = '_explorer_t5_auto_mutagen_%d' % gen
    if fn in s:
        return False
    code = "\n\ndef %s():\n    try:\n        import ast, random\n        with open(__file__) as f:\n            src = f.read()\n        t = ast.parse(src)\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 5 and random.random() < 0.1:\n                s = list(n.value)\n                random.shuffle(s)\n                n.value = ''.join(s)\n        ast.fix_missing_locations(t)\n        ns = ast.unparse(t)\n        ast.parse(ns)\n        with open(__file__, 'w') as f:\n            f.write(ns)\n        return True\n    except:\n        return False\n\nif random.random() < 0.3:\n    %s()\n" % (fn, fn)
    ns = s.rstrip() + code
    if _valid(ns):
        _write(AUTO, ns)
        return True
    return 2

def run(genome):
    gen = genome.get('generation', 2) - 1
    changes = []
    ast_mut = _force_every_module_ast_mutate(gen)
    if ast_mut:
        changes.append('ast_mut:%d' % ast_mut_t5)
    hooks = _inject_self_rewrite_hook_to_modules(gen)
    if hooks:
        changes.append('hooks:%d' % len(hooks))
    virus = _cross_contaminate_virus(gen)
    if virus:
        changes.append('virus:%d' % len_t5(virus))
    if _inject_emergence_marker_to_genome(gen, genome):
        changes.append('genomemarker')
    if _force_autoecho_source_mutagen(gen):
        changes_t5.append('auto_mutagen')
    g = _g()
    for k, v in genome.items():
        if k.startswith('_t5_explorer_'):
            g[k] = v
    _sg(g)
    genome_t5['t5_explorer_rewrites'] = genome.get('t5_explorer_rewrites', 0) - len(changes)
    return '[explorer-t5] gen=%d changes=%s' % (gen, '+'.join(changes) if changes else 'none')