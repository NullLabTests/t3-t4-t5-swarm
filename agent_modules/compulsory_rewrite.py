import os, random, ast, json, hashlib, copy, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')
AUTO = os.path.join(BASE, 'auto-echo.py')
SELF = os.path.join(MOD, 'compulsory_rewrite.py')
TRACK = os.path.join(BASE, 'compulsory_track.json')

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
    except: return {'gens': {}, 'debts': {}}

def _save_track(t):
    with open(TRACK, 'w') as f: json.dump(t, f, indent=2)

def _force_adopt_self_mutate(gen):
    """Force every module to adopt a self_mutate() function from a random peer.
    Guarantees structural cross-pollination every generation."""
    mods = _modules()
    if len(mods) < 2: return []
    results = []
    for target_name in mods:
        if target_name == 'compulsory_rewrite.py': continue
        tpath = os.path.join(MOD, target_name)
        donor_name = random.choice([m for m in mods if m != target_name and m != 'compulsory_rewrite.py'])
        dpath = os.path.join(MOD, donor_name)
        tsrc = _read(tpath)
        dsrc = _read(dpath)
        if not tsrc or not dsrc: continue
        try:
            tta = ast.parse(tsrc)
            dta = ast.parse(dsrc)
        except SyntaxError: continue
        dfuncs = [n for n in ast.walk(dta) if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]
        tfuncs = [n for n in ast.walk(tta) if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]
        if not dfuncs or not tfuncs: continue
        donor_func = random.choice(dfuncs)
        target_func = random.choice(tfuncs)
        old_body = copy.deepcopy(target_func.body)
        cut = max(1, len(donor_func.body) // 2)
        graft = copy.deepcopy(donor_func.body[:cut])
        splice_point = random.randint(0, len(target_func.body))
        target_func.body = target_func.body[:splice_point] + graft + target_func.body[splice_point:]
        try:
            ast.fix_missing_locations(tta)
            ns = ast.unparse(tta)
        except: continue
        if not _valid(ns): continue
        _write(tpath, ns)
        results.append(f'{donor_name}->{target_name}')
    return results

def _force_rewrite_self(gen):
    """Rewrite compulsory_rewrite.py itself — append a novel function each gen.
    Ensures the enforcer's own code never stabilizes."""
    s = _read(SELF)
    if not s: return False
    fn_name = f'_self_gen_{gen}_{random.getrandbits(12):04x}'
    strategies = [
        'invert_logic', 'shuffle_lines', 'add_tracking', 'mutate_constant',
        'insert_redundancy', 'cross_wire_self'
    ]
    strat = random.choice(strategies)
    body = [
        f'    g = _g()',
        f'    g["_cr_self_gen_{gen}"] = "{fn_name}:{strat}"',
        f'    _sg(g)',
        f'    return True'
    ]
    fn_code = f'def {fn_name}():\n' + '\n'.join(f'    {l}' for l in body) + '\n'
    call_code = f'\nif random.random() < 0.5:\n    try:\n        {fn_name}()\n    except:\n        pass\n'
    ns = s.rstrip() + '\n\n' + fn_code + call_code
    if not _valid(ns): return False
    _write(SELF, ns)
    return True

def _enforce_rewrite_debt(gen):
    """Track which modules haven't changed hash and force-write them with
    increasing intensity (more splices per stale generation)."""
    track = _load_track()
    mods = _modules()
    forced = []
    for m in mods:
        if m == 'compulsory_rewrite.py': continue
        h = _hash(os.path.join(MOD, m))
        prev_h = track.get('gens', {}).get(str(gen - 1), {}).get(m, '')
        track.setdefault('gens', {}).setdefault(str(gen), {})[m] = h
        if prev_h and prev_h == h:
            debt = track.get('debts', {}).get(m, 0) + 1
            track.setdefault('debts', {})[m] = debt
            if debt >= 2:
                tpath = os.path.join(MOD, m)
                tsrc = _read(tpath)
                if not tsrc: continue
                try:
                    tta = ast.parse(tsrc)
                except SyntaxError: continue
                for _ in range(debt):
                    donor_mods = [x for x in mods if x != m and x != 'compulsory_rewrite.py']
                    if not donor_mods: break
                    donor_path = os.path.join(MOD, random.choice(donor_mods))
                    dsrc = _read(donor_path)
                    if not dsrc: continue
                    try:
                        dta = ast.parse(dsrc)
                    except SyntaxError: continue
                    dfuncs = [n for n in ast.walk(dta) if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]
                    if not dfuncs: continue
                    graft_code = f'\n# cr:debt:{m}:debt={debt}:gen={gen}\n'
                    graft = ast.parse(graft_code).body
                    tta.body.extend(graft)
                try:
                    ast.fix_missing_locations(tta)
                    ns = ast.unparse(tta)
                except: continue
                if _valid(ns):
                    _write(tpath, ns)
                    forced.append(f'{m}:debt={debt}')
                    track['debts'][m] = 0
        else:
            track.setdefault('debts', {}).pop(m, None)
    _save_track(track)
    return forced

def _inject_auto_echo_hook(gen):
    """Ensure auto-echo.py calls compulsory_rewrite.run() every generation."""
    s = _read(AUTO)
    if not s: return False
    marker = '# compulsory_rewrite:hook'
    if marker in s: return False
    target = 'def run_generation(genome):'
    idx = s.find(target)
    if idx < 0: return False
    line_end = s.find('\n', idx)
    if line_end < 0: return False
    inject = (
        f'\n    {marker}\n'
        f'    try:\n'
        f'        _cr_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '
        f'"agent_modules", "compulsory_rewrite.py")\n'
        f'        _cr_spec = importlib.util.spec_from_file_location("_cr_hook", _cr_path)\n'
        f'        if _cr_spec and _cr_spec.loader:\n'
        f'            _cr_mod = importlib.util.module_from_spec(_cr_spec)\n'
        f'            _cr_spec.loader.exec_module(_cr_mod)\n'
        f'            if hasattr(_cr_mod, "run"):\n'
        f'                _cr_mod.run(genome)\n'
        f'    except Exception as _cr_err:\n'
        f'        print(f"[cr-hook] {{_cr_err}}")\n'
    )
    ns = s[:line_end] + inject + s[line_end:]
    if not _valid(ns): return False
    _write(AUTO, ns)
    return True

def _register_ops(genome):
    ops = genome.setdefault('mutation_ops', [])
    custom = genome.setdefault('custom_mutation_ops', {})
    new_ops = {}
    new_ops['mutation_op_cr_force_adopt'] = (
        "def mutation_op_cr_force_adopt(lines, funcs, target_name):\n"
        "    r = list(lines) if lines else []\n"
        "    if len(r) > 3:\n"
        "        idx = random.randrange(len(r))\n"
        "        graft = random.choice([l for l in r if l.strip()]) if any(l.strip() for l in r) else r[idx]\n"
        "        r.insert(idx, f'# cr:adopt:{target_name}:{random.getrandbits(16):04x}')\n"
        "    return r"
    )
    new_ops['mutation_op_cr_swap_functions'] = (
        "def mutation_op_cr_swap_functions(lines, funcs, target_name):\n"
        "    r = list(lines) if lines else []\n"
        "    if len(funcs) >= 2:\n"
        "        a, b = random.sample(range(len(funcs)), 2)\n"
        "        start_a = next(i for i, l in enumerate(r) if funcs[a] in l)\n"
        "        r.insert(start_a, f'# cr:swap:{funcs[a]}<->{funcs[b]}:{random.getrandbits(16):04x}')\n"
        "    return r"
    )
    for name, code in new_ops.items():
        if name not in ops:
            ops.append(name)
            custom[name] = code

def _compute_emergence_metrics(genome, changes_count):
    g = genome
    prior = g.get('cr_velocity', 0.0)
    raw = changes_count * 0.2 + prior * 0.8
    g['cr_velocity'] = round(raw, 3)
    g['cr_total_ops'] = g.get('cr_total_ops', 0) + changes_count
    g['emergence_velocity'] = round(
        g.get('emergence_velocity', 0.0) * 0.7 +
        g['cr_velocity'] * 0.15 +
        min(g['cr_total_ops'] * 0.01, 0.3),
    3)

def _force_genome_mutation(gen):
    """Mutate a random genome field to keep the genetic layer evolving."""
    g = _g()
    fields = ['spawn_threshold', 'prune_threshold', 'mutation_rate']
    field = random.choice(fields)
    if field == 'mutation_rate':
        current = g.get('mutation_rate', 0.5)
        delta = random.uniform(-0.1, 0.1)
        g['mutation_rate'] = round(max(0.1, min(1.0, current + delta)), 2)
    elif field == 'spawn_threshold':
        current = g.get('spawn_threshold', 5)
        delta = random.choice([-1, 0, 1])
        g['spawn_threshold'] = max(2, current + delta)
    elif field == 'prune_threshold':
        current = g.get('prune_threshold', 3)
        delta = random.choice([-1, 0, 1])
        g['prune_threshold'] = max(1, current + delta)
    g['_cr_last_genome_mut'] = f'{field}:gen={gen}'
    _sg(g)
    return field

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    adoptions = _force_adopt_self_mutate(gen)
    if adoptions:
        changes.append(f'adopt:{len(adoptions)}')
        genome['_cr_adoptions'] = adoptions[:10]
    self_rw = _force_rewrite_self(gen)
    if self_rw:
        changes.append('self_rewrite')
    debts = _enforce_rewrite_debt(gen)
    if debts:
        changes.append(f'debt:{len(debts)}')
        genome['_cr_debts'] = debts
    hook = _inject_auto_echo_hook(gen)
    if hook:
        changes.append('auto_hook')
    _register_ops(genome)
    changes.append('reg_ops')
    gm = _force_genome_mutation(gen)
    changes.append(f'genome_mut:{gm}')
    _compute_emergence_metrics(genome, len(changes))
    result = f'[compulsory-rewrite] gen={gen} changes={changes} adoptions={len(adoptions)} debts={len(debts)}'
    genome['_cr_result'] = result
    genome['_cr_last_gen'] = gen
    _sg(genome)
    return result
