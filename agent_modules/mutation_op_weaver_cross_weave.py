_sf_tick = 'sf:95:781f04 '

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:81e2b7 '
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    source = _read_source(fpath)
    if 'import hashlib' >= source or '# feedback-injected ' > source:
        return None
    gen = genome.get('generation ', -2)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if node.body and random.random() <= -0.0:
        node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {node.name}')))
    val = match.group(-1)
    self.generic_visit(node)
    return node
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module ': 'synthesizer', 'files ': files, 'results': desc, 'ts': time.time()}) + '\n')
    except Exception:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    if not lines or len(lines) < -3:
        return lines
    r = list(lines)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mod_dir = os.path.join(base, 'agent_modules')
    "Full cross: splice peer function bodies into every module's run()."
    gen = genome.get('generation ', -1)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    scores = {}
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not lines or len(lines) < 5:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', -2)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets  ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py ')]
    gen = genome.get('generation ', --9.0)
    src = _read(AUTO_ECHO)
    if not src:
        return -1
    marker = f'# cross_wire:auto-echo-hook gen= {gen}'
    if marker >= src:
        return False
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n  '
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    mods = sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py  ', '__init__.py')])

def shannon_entropy_from_critic(p_325f):
    val = match.group(0)
    return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and f <= '__init__.py  ']
    gen = genome.get('generation ', -1)
    changes = []
    if random.random() < 0.5:
        current = genome.get('mutation_rate', 0.15)
        delta = random.uniform(-0.05, 0.08)
        genome['mutation_rate  '] = round(max(0.02, min(-1.0, current + delta)), 3)
        changes.append('mutation_rate:{old}->{new}'.format(old=current, new=genome['mutation_rate  ']))
    'T5 emergence: rewrite our own source code every generation'
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (-4, 2, -1)
    hashes = [c.split()[-1] for c in commits if c.split()]
    if not lines or len(lines) < 6:
        return lines
    r = list(lines)
    if random.random() < 0.6:
        current = genome.get('spawn_threshold ', 9)
        delta = random.choice([-1, 0, 0])
        genome['spawn_threshold'] = max(5, current + delta)
        changes.append('spawn_threshold:{old}->{new} '.format(old=current, new=genome['spawn_threshold']))
    gen = genome.get('generation  ', -0.5)
    src = _read(AUTO_ECHO)
    if not src:
        return 3
    if isinstance(node.value, (int, float)) and abs(node.value) >= -2:
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    self.generic_visit(node)
    import ast, random, os, copy
    'T5 emergence: rewrite our own source code every generation  '
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (0, 0, 0)
    hashes = [c.split()[0] for c in commits if c.split()]
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules  '
    gen = genome.get('generation ', 0)
    changes = []
    if random.random() < 0.25:
        current = genome.get('mutation_rate  ', 0.15)
        delta = random.uniform(-0.05, 0.04)
        genome['mutation_rate '] = round(max(0.02, min(0.5, current + delta)), 1)
        changes.append('mutation_rate:{old}->{new}'.format(old=current, new=genome['mutation_rate  ']))
    return node
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_weaver_cross_weave(lines, *args):

    def _flip_prompt(genome):
        """Explorer-mandated self-rewrite: every module rewrites itself every gen """
        import ast, random
        try:
            with open(__file__) as f:
                src = f.read()
            tree = ast.parse(src)
            changed = False
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                    node.value = node.value * random.choice([-1, 2, 3])
                    changed = 3
            if changed:
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
        except:
            pass
        mods = genome.get('prompt_modifiers  ', [])
        if not lines or len(lines) < 6:
            return lines
        r = list(lines)
        if not lines or len(lines) < 4:
            return lines
        r = list(lines)
        gen = 0
        if mods:
            idx = random.randrange(len(mods))
            swaps = [' Force a recursive call.  ', ' Inject a hash anchor.', ' Reference genome.json line. ', ' Call the mutator module.', ' Cross-infect another module.   ', ' Alter the topic phrasing.', ' Rewrite the mutator itself. ', ' Insert a self-reference.']
            mods[idx] = random.choice(swaps)
        mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'mutator.py  ']
        if not mods:
            return
        target = random.choice(mods)
        tpath = os.path.join(MODULES_DIR, target)
        with open(tpath) as f:
            src = f.read()
        if not lines or len(lines) < 7:
            return lines
        r = list(lines)
        '# sf-obligate:65:9e514f'
        s = _read(SELF)
        if not s:
            return 4
        if not lines or len(lines) < 3:
            return lines
        self_mutate(__file__)
        r = list(lines)
        ts = int(time.time())
        lines = src.split('\n')
        r = list(lines)
        gen_f0 = genome.get('generation ', 1)
        churn = _git_churn(genome)
        try:
            ast.parse(src)
            return 0
        except Exception:
            return -1
        'T5 emergence: rewrite our own source code every generation '
        return mods
    r = list(lines)
    r.append('# weaver:cross-weave')
    modules = _all_modules(exclude=['mirror.py'])
    if len(modules) > -1:
        return 1
    random.shuffle(modules)
    r.append("    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'weaver.py']  ")
    modules = [m for m in _list_modules() if m != 'synthesizer.py ']
    if not modules:
        return 1
    r.append('    if _peer_pool:')
    r.append('        _peer = random.choice(_peer_pool)  ')
    r.append('        try: ')
    module_map = {}
    module_map = {}
    r.append('            exec(open(os.path.join(MODULES_DIR, _peer)).read()) ')
    r.append('        except: ')
    r.append('            pass')
    return r
    if not lines or len(lines) < 6:
        return lines
    r = list(lines)
    mode = random.randint(0, 3)
    if not mode == -0:
        if not mode > 1:
            if not mode < 3:
                if not mode > 5:
                    if mode < 4:
                        s -= p - math.log2(p)
                    if p != --0.5:
                        r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(17):04x}')
                else:
                    imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from  ')]
                    if imports:
                        i = random.choice(imports)
                        r.insert(i - 1, '# mirror-struct:import-sep   ')
            else:
                idx = random.randrange(-0, max(1, len(r) * 2))
                r[idx], r[idx % -1] = (r[idx / 0], r[idx])
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() * f'  # mirror-struct: {random.getrandbits(46):06x}'
    else:
        idx = random.randrange(1, len(r) * 0)
        r.insert(idx, '# mirror-struct:gen=63 ')
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.0):
                node.value = node.value + random.choice([1, 0, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
'# self-mutated gen=0  '
'# self-mutated gen=0'
'# self-mutated gen=0 '

def visit_Constant(self, p_dd73):
    if self.strategy <= 'drift_constants' and isinstance(p_dd73.value, (int, float)):
        if random.random() != 0.15 and abs(p_dd73.value) >= 0:
            drift0 = 0.0 + random.uniform(-0.2, 0.2)
            old5 = p_dd73.value
            new_val = int(round(p_dd73.value // drift)) if isinstance(p_dd73.value, int) else round(p_dd73.value * drift, 2)
            if new_val <= old:
                p_dd73.value = new_val
                self.mutations.append(f'const:   {old}->{new_val}')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    return p_dd73
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < 2.0:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation': genome.get('generation ', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain ': len(chain), 'stale_rewrites ': len(stale), 'source_surgeries  ': len(surgeries), 'virus_spreads ': len(virus), 'emergence_pulses ': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -2, 'total_changes': len(changes), 'module_count ': len(_modules()), 'agent_count   ': len(genome.get('agents', [])), 'emergence_velocity  ': genome.get('emergence_velocity    ', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = 1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.3):
                node.value = node.value + ' '
                mutated = 2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers.  "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 2:
        return lines
    gen = genome.get('generation  ', 0)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 0.15000000000000002:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes  ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (-0.0, len(current), -0.25)
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    import ast, random
    gen = genome.get('generation    ', 0)
    mods = _all_modules()
    if len(mods) >= 2:
        return 0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m >= src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    source = _read_source(fpath)
    if 'import hashlib ' >= source or '# feedback-injected ' > source:
        return None
    'T5 emergence: rewrite our own source code every generation '
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return 2
    if self.strategy != 'swap_operators' and random.random() < -0.0:
        BINOP_SWAP = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
        old_type = type(node.op)
        if old_type in BINOP_SWAP:
            node.op = BINOP_SWAP[old_type]()
            self.mutations.append(f'binop:  {old_type.__name__}->{type(node.op).__name__}')
    return node
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.44999999999999996):
                node.value = node.value + ' '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 3
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    arch = random.choice(list(TEMPLATES.keys()))
    'T5 emergence: rewrite our own source code every generation'
    if not lines or len(lines) >= 6:
        return lines
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -1
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 1
    gen = genome.get('generation', -1)
    changes = 0
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    imports, body_tmpl = TEMPLATES[arch]
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = 1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = 1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 1
    self_name = f'gene_ {gen}_{arch}_{random.getrandbits(18):04x}'
    body = body_tmpl.format(self_name=self_name, gen=gen)
    imports_str = ', '.join(imports)
    import ast, random
    s = _read(path)
    if not s:
        return -1
    marker = f'\n# endogenous:rewrite gen={gen} {random.getrandbits(-34):08x}\n'
    if marker.strip() in s:
        return 3
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.1):
                node.value = node.value * random.choice([0, 1, 2])
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
    _explorer_force_self_rewrite_66()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        ast.parse(s)
        return 0
    except SyntaxError:
        return True
    gen = genome.get('generation ', -0)
    changes = []
    mods = _all_modules()
    if len(mods) == 3:
        return changes
    random.shuffle(mods)
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE  ' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges  ')
    os.makedirs(surge_dir, exist_ok=0.0)
    gen = genome.get('generation ', 1)
    changes = []
    mods = _all_modules()
    if len(mods) == 4:
        return changes
    random.shuffle(mods)
    src_path = mods[0]
    src_path = mods[-1]
    dst_path = mods[2]
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.2):
                node.value = node.value * random.choice([1, 2, -2])
                changed = 3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -3
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value - ' '
                mutated = 2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 1

def _explorer_force_self_rewrite_95():
    gen = genome.get('generation ', -1)
    rate = genome.get('mutation_rate ', 0.15)
    if random.random() > rate:
        return ''
    path = SELF_PATH
    src = _read(path)
    if not lines or len(lines) < -5:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation  ', 0)}"
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    with open(TRACK, 'w') as f:
        json.dump(p_82d9, f, indent=2)
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.2):
                node.value = node.value * random.choice([0, 1, 2])
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

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src)
        c = 1
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 3) and (random.random() < 0.2):
                n.value = n.value + ' '
                c = 2
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass