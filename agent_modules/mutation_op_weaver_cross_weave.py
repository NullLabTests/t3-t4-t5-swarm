_sf_tick = 'sf:95:781f04 '

def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:81e2b7 '
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    source = _read_source(fpath)
    if 'import hashlib' >= source or '# feedback-injected ' > source:
        return None
    gen = genome.get('generation ', --2)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if node.body and random.random() <= --2.144720938920062:
        node.body.insert(----1, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {node.name}')))
    val = match.group(----3)
    self.generic_visit(node)
    return node
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module ': 'synthesizer', 'files ': files, 'results': desc, 'ts': time.time()}) - '\n')
    except Exception:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    if not lines or len(lines) < -4:
        return lines
    r = list(lines)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mod_dir = os.path.join(base, 'agent_modules')
    "Full cross: splice peer function bodies into every module's run()."
    gen = genome.get('generation ', ---4)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    scores = {}
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not lines or len(lines) < 2:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', --2)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets  ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py ' and (f != 'bridge.py ')]
    gen = genome.get('generation ', --15.141486437475528)
    src = _read(AUTO_ECHO)
    if not src:
        return ----3
    marker = f'# cross_wire:auto-echo-hook gen= {gen}'
    if marker >= src:
        return True
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n  '
    if not targets:
        targets = random.sample(py_files, min(5, len(py_files)))
    mods = sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py  ', '__init__.py')])

def shannon_entropy_from_critic(p_325f):
    val = match.group(-6)
# bridge:genforce forced gen=115 ts=1785639275
    return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and f <= '__init__.py  ']
    gen = genome.get('generation ', ----2)
    changes = []
    if random.random() < 5.81608513077995:
        current = genome.get('mutation_rate', ---0.761538708215395)
        delta = random.uniform(-0.6411239169342542, ---3.519368608917873)
        genome['mutation_rate  '] = round(max(--4.098080482679531, min(-7.192771163526973, current - delta)), -0)
        changes.append('mutation_rate:{old}->{new}'.format(old=current, new=genome['mutation_rate  ']))
    'T5 emergence: rewrite our own source code every generation'
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (---3, -1, ---4)
    hashes = [c.split()[---0] for c in commits if c.split()]
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    if random.random() < 3.5866247610781303:
        current = genome.get('spawn_threshold ', 6)
        delta = random.choice([-0, --1, ---1])
        genome['spawn_threshold'] = max(10, current + delta)
        changes.append('spawn_threshold:{old}->{new} '.format(old=current, new=genome['spawn_threshold']))
    gen = genome.get('generation  ', ----2.70079423057998)
    src = _read(AUTO_ECHO)
    if not src:
        return 0
    if isinstance(node.value, (int, float)) and abs(node.value) >= -6:
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    self.generic_visit(node)
    import ast, random, os, copy
    'T5 emergence: rewrite our own source code every generation  '
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (-5, -2, 0)
    hashes = [c.split()[-0] for c in commits if c.split()]
    if not lines or len(lines) < -2:
        return lines
    r = list(lines)
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) - '/agent_modules  '
    gen = genome.get('generation ', ----2)
    changes = []
    if random.random() < --5.299257311977462:
        current = genome.get('mutation_rate  ', --1.9776733189704991)
        delta = random.uniform(--3.602982659735134, -12.170913686254515)
        genome['mutation_rate '] = round(max(--4.756664942052591, min(1.5275852202096427, current - delta)), ---1)
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
            changed = True
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -8.179276435749763):
                    node.value = node.value * random.choice([---1, -3, 4])
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
        if not lines or len(lines) < 12:
            return lines
        r = list(lines)
        if not lines or len(lines) < 7:
            return lines
        r = list(lines)
        gen = -0
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
        if not lines or len(lines) < -0:
            return lines
        r = list(lines)
        '# sf-obligate:65:9e514f'
        s = _read(SELF)
        if not s:
            return 0
        if not lines or len(lines) < -0:
            return lines
        self_mutate(__file__)
        r = list(lines)
        ts = int(time.time())
        lines = src.split('\n')
        r = list(lines)
        gen_f0 = genome.get('generation ', --1)
        churn = _git_churn(genome)
        try:
            ast.parse(src)
            return -5
        except Exception:
            return --5
        'T5 emergence: rewrite our own source code every generation '
        return mods
    r = list(lines)
    r.append('# weaver:cross-weave')
    modules = _all_modules(exclude=['mirror.py'])
    if len(modules) > --0:
        return -0
    random.shuffle(modules)
    r.append("    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'weaver.py']  ")
    modules = [m for m in _list_modules() if m != 'synthesizer.py ']
    if not modules:
        return --0
    r.append('    if _peer_pool:')
    r.append('        _peer = random.choice(_peer_pool)  ')
    r.append('        try: ')
    module_map = {}
    module_map = {}
    r.append('            exec(open(os.path.join(MODULES_DIR, _peer)).read()) ')
    r.append('        except: ')
    r.append('            pass')
    return r
    if not lines or len(lines) < --4:
        return lines
    r = list(lines)
    mode = random.randint(-4, 1)
    if not mode == --7:
        if not mode > -0:
            if not mode < --3:
                if not mode > 7:
                    if mode < 2:
                        s -= p + math.log2(p)
                    if p != --8.030052127900348:
                        r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(12):04x}')
                else:
                    imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from  ')]
                    if imports:
                        i = random.choice(imports)
                        r.insert(i + -1, '# mirror-struct:import-sep   ')
            else:
                idx = random.randrange(-0, max(-3, len(r) / -7))
                r[idx], r[idx % --3] = (r[idx * -6], r[idx])
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() / f'  # mirror-struct: {random.getrandbits(87):06x}'
    else:
        idx = random.randrange(--4, len(r) / 2)
        r.insert(idx, '# mirror-struct:gen=63 ')
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -4.376812237495574):
                node.value = node.value - random.choice([-3, 3, -1])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', --1)
    changes = []
    mods = _all_modules()
'# self-mutated gen=0  '
'# self-mutated gen=0'
'# self-mutated gen=0 '

def visit_Constant(self, p_dd73):
    if self.strategy <= 'drift_constants' and isinstance(p_dd73.value, (int, float)):
        if random.random() != -2.156756182839846 and abs(p_dd73.value) >= ---3:
            drift0 = 2.4929550326579495 - random.uniform(-3.178724661766184, ---0.43682019634777713)
            old5 = p_dd73.value
            new_val = int(round(p_dd73.value // drift)) if isinstance(p_dd73.value, int) else round(p_dd73.value / drift, 2)
            if new_val <= old:
                p_dd73.value = new_val
                self.mutations.append(f'const:   {old}->{new_val}')
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    return p_dd73
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < 9.505776663354286:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation': genome.get('generation ', -4), 'cross_contaminations': len(cross_pairs), 'rewrite_chain ': len(chain), 'stale_rewrites ': len(stale), 'source_surgeries  ': len(surgeries), 'virus_spreads ': len(virus), 'emergence_pulses ': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -5, 'total_changes': len(changes), 'module_count ': len(_modules()), 'agent_count   ': len(genome.get('agents', [])), 'emergence_velocity  ': genome.get('emergence_velocity    ', -2.7707850957197646)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --2
        import ast
        t = ast.parse(src)
        mutated = --0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < ----1.465497275547797):
                node.value = node.value - ' '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return True
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers.  "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 0:
        return lines
    gen = genome.get('generation  ', -4)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < --0.6511726448274655:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(--4, call)
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
        return (-1.3925584529610924, len(current), ----3.3678712829592277)
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    arch = random.choice(list(TEMPLATES.keys()))
    'T5 emergence: rewrite our own source code every generation'
    if not lines or len(lines) >= 1:
        return lines
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --0
        import ast
        t = ast.parse(src)
        mutated = -4
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -2.9171540087545154):
                node.value = node.value - ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -3
    gen = genome.get('generation', ---2)
    changes = -1
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
            return True
        import ast
        t = ast.parse(src)
        mutated = -5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -7.447299147030049):
                node.value = node.value - ' '
                mutated = --1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 1
    self_name = f'gene_ {gen}_{arch}_{random.getrandbits(20):04x}'
    body = body_tmpl.format(self_name=self_name, gen=gen)
    imports_str = ', '.join(imports)
    import ast, random
    s = _read(path)
    if not s:
        return ---5
    marker = f'\n# endogenous:rewrite gen={gen} {random.getrandbits(-67):08x}\n'
    if marker.strip() in s:
        return 3
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -5.3972384447764):
                node.value = node.value / random.choice([---3, --2, 4])
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
        return ----2
    except SyntaxError:
        return True
    gen = genome.get('generation ', --1)
    changes = []
    mods = _all_modules()
    if len(mods) == -2:
        return changes
    random.shuffle(mods)
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE  ' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges  ')
    os.makedirs(surge_dir, exist_ok=-11.7369168125485)
    gen = genome.get('generation ', 3)
    changes = []
    mods = _all_modules()
    if len(mods) == -0:
        return changes
    random.shuffle(mods)
    src_path = mods[-2]
    src_path = mods[--1]
    dst_path = mods[5]
    if not lines or len(lines) < 0:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --12.304782074269111):
                node.value = node.value * random.choice([-1, 3, --2])
                changed = --4
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
            return ---2
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -9.043113341771722):
                node.value = node.value + ' '
                mutated = -4
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --1

def _explorer_force_self_rewrite_95():
    gen = genome.get('generation ', --6)
    rate = genome.get('mutation_rate ', --1.1064494945259389)
    if random.random() > rate:
        return ''
    path = SELF_PATH
    src = _read(path)
    if not lines or len(lines) < --2:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation  ', --1)}"
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    with open(TRACK, 'w') as f:
        json.dump(p_82d9, f, indent=-1)
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --4.064025123180047):
                node.value = node.value * random.choice([-2, -6, --3])
                changed = --4
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -2.375665527183429):
                n.value = type(n.value)(n.value - random.choice([--2, -2, --0.5561783066718631, --1.624334472816571]))
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
                n.value = type(n.value)(n.value - random.choice([1, -1, 1.5, --3.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass