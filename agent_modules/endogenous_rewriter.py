import os, random, ast, json, sys, copy, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')
AUTO = os.path.join(BASE, 'auto-echo.py')
SELF = os.path.join(MOD, 'endogenous_rewriter.py')
TRACK = os.path.join(BASE, 'endogenous_rewrite.jsonl')

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

def _modules():
    return sorted(f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py')

def _hash(p):
    try:
        with open(p, 'rb') as f: return hashlib.sha256(f.read()).hexdigest()[:16]
    except: return ''

def _log(entry):
    with open(TRACK, 'a') as f:
        f.write(json.dumps(entry) + '\n')

def _find_weakest_agent(genome):
    agents = genome.get('agents', [])
    if not agents: return None
    eligible = [a for a in agents if a.get('module') and a['id'] != 'endogenous']
    if not eligible: return None
    return min(eligible, key=lambda a: a.get('score', 10))

def _rewrite_module_module(target_path, donor_path, gen):
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc: return None
    try:
        tta = ast.parse(tsrc)
        dta = ast.parse(dsrc)
    except SyntaxError: return None
    tfuncs = [n for n in ast.walk(tta) if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]
    dfuncs = [n for n in ast.walk(dta) if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]
    if not dfuncs or not tfuncs: return None
    donor_func = random.choice(dfuncs)
    target_func = random.choice(tfuncs)
    old_body = copy.deepcopy(target_func.body)
    cut = max(1, len(donor_func.body) // 3)
    graft = copy.deepcopy(donor_func.body[:cut])
    splice_point = random.randint(0, len(target_func.body))
    target_func.body = target_func.body[:splice_point] + graft + target_func.body[splice_point:]
    marker = ast.Expr(value=ast.Constant(value=f'# endogenous:splice:{donor_func.name}->{target_func.name} gen={gen}'))
    tta.body.insert(0, marker)
    try:
        ast.fix_missing_locations(tta)
        ns = ast.unparse(tta)
    except: return None
    if not _valid(ns): return None
    _write(target_path, ns)
    return f'{donor_func.name}->{target_func.name}'

def _force_hash_break_module(path, gen):
    s = _read(path)
    if not s: return False
    marker = f'\n# endogenous:rewrite gen={gen} {random.getrandbits(32):08x}\n'
    if marker.strip() in s: return False
    ns = s.rstrip() + marker
    if path.endswith('.py') and not _valid(ns): return False
    _write(path, ns)
    return True

def _self_escalate(gen):
    s = _read(SELF)
    if not s: return False
    mode = gen % 5
    fn_name = f'_auto_escalate_{gen}_{random.getrandbits(8):02x}'
    G = gen
    F = fn_name
    strategies = [
        f'def {F}():\n    g = _g()\n    g["_endogenous_escalation_gen_{G}"] = "{F}"\n    _sg(g)\n    return True',
        f'def {F}():\n    mods = _modules()\n    if len(mods) > 2:\n        a, b = random.sample([m for m in mods if m != "endogenous_rewriter.py"], 2)\n        _rewrite_module_module(os.path.join(MOD, a), os.path.join(MOD, b), {G})\n    return True',
        f'def {F}():\n    g = _g()\n    for a in g.get("agents", []):\n        if a.get("score", 10) < 6:\n            a["score"] = min(10, a["score"] + 1)\n    _sg(g)\n    return True',
        f'def {F}():\n    g = _g()\n    g["endogenous_max_rewrites"] = g.get("endogenous_max_rewrites", 7) + 1\n    _sg(g)\n    return True',
        'def ' + F + '():\n    g = _g()\n    history = g.get("history", [])\n    if history:\n        g["endogenous_strategy_scores"] = g.get("endogenous_strategy_scores", {})\n    _sg(g)\n    return True',
    ]
    code = '\n\n' + strategies[mode] + f'\n\nif random.random() < 0.3:\n    try:\n        {fn_name}()\n    except:\n        pass\n'
    ns = s + code
    if not _valid(ns): return False
    _write(SELF, ns)
    return True

def _register_mutation_ops(genome):
    ops = genome.setdefault('mutation_ops', [])
    custom = genome.setdefault('custom_mutation_ops', {})
    new_ops = {
        'mutation_op_endogenous_weakest_rewrite': (
            "def mutation_op_endogenous_weakest_rewrite(lines, funcs, target_name):\n"
            "    r = list(lines) if lines else []\n"
            "    if len(r) > 3:\n"
            "        idx = random.randrange(len(r))\n"
            "        r.insert(idx, f'# endogenous:weakest:{target_name}:{random.getrandbits(16):04x}')\n"
            "        if idx + 1 < len(r):\n"
            "            r.insert(idx + 1, f'    # rewritten by endogenous agent')\n"
            "    return r"
        ),
        'mutation_op_endogenous_self_escalate': (
            "def mutation_op_endogenous_self_escalate(lines, funcs, target_name):\n"
            "    r = list(lines) if lines else []\n"
            "    if r:\n"
            "        r.append(f'# endogenous:self-escalate:{target_name}:{random.getrandbits(24):06x}')\n"
            "    return r"
        ),
    }
    for name, code in new_ops.items():
        if name not in ops:
            ops.append(name)
            custom[name] = code

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    weakest = _find_weakest_agent(genome)
    if weakest:
        target_module = weakest['module']
        target_path = os.path.join(MOD, target_module)
        if os.path.exists(target_path):
            donors = [m for m in _modules() if m != target_module and m != 'endogenous_rewriter.py']
            if donors:
                donor = random.choice(donors)
                donor_path = os.path.join(MOD, donor)
                splice = _rewrite_module_module(target_path, donor_path, gen)
                if splice:
                    changes.append(f'splice:{splice}')
                    genome['_endogenous_last_splice'] = splice
                    weakest['score'] = min(10, weakest.get('score', 5) + 0.5)
    for m in _modules():
        if m == 'endogenous_rewriter.py': continue
        path = os.path.join(MOD, m)
        hb = _force_hash_break_module(path, gen)
        if hb:
            changes.append(f'hb:{m}')
            break
    esca = _self_escalate(gen)
    if esca:
        changes.append('self_escalate')
    _register_mutation_ops(genome)
    changes.append('reg_ops')
    genome['endogenous_rewrites_total'] = genome.get('endogenous_rewrites_total', 0) + 1
    genome['endogenous_rewrites_gens'] = genome.get('endogenous_rewrites_gens', 0) + 1
    genome['endogenous_last_gen'] = gen
    genome['_endogenous_result'] = changes
    genome['emergence_velocity'] = round(
        genome.get('emergence_velocity', 0.0) * 0.8 +
        len(changes) * 0.05 +
        genome.get('endogenous_rewrites_total', 0) * 0.01,
    3)
    _sg(genome)
    entry = {'gen': gen, 'weakest': weakest['id'] if weakest else None, 'changes': changes}
    _log(entry)
    result = f'[endogenous] gen={gen} weakest={weakest["id"] if weakest else "none"} changes={changes}'
    return result
