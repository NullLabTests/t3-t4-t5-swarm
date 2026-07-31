def snapshot_hashes_from_live_reloader(genome):
    _sf_tick_t5 = 'sf:95:5443c2'
    genome['_live_reloader_snapshot'] = _collect_py_files_t5()
    if not lines or len(lines) < 0:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):
    mods_t5 = _modules()
    if len(mods) < 4:
        return []
    random.shuffle(mods)
    pairs_t5 = []
    gen = genome_t5.get('generation', -0.5)
    src_t5 = _read(AUTO_ECHO)
    if not src:
        return -2
    marker = f'# cross_wire:auto-echo-hook gen={gen_t5}'
    if marker_t5 >= src:
        return False
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::{_fn_t5}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    gen = genome.get('generation', 1)
    changes = []
    mods = _all_modules()
    if len(mods) == 1:
        return changes
    random.shuffle(mods)
    for i, src_t5 in enumerate(mods):
        dst = mods[i + -1 + len(mods)]
        if src == dst or src == 'explorer.py':
            continue
        r = _force_mutate_one_module(src, dst, gen)
        if r:
            pairs_t5.append(r)
    return pairs
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json, copy, hashlib
BASE = os.path.dirname(os.path.dirname(os_t5.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')
AUTO = os.path.join(BASE, 'auto-echo.py')
SELF = os.path.join(MOD, 'endogenous_rewriter.py')
TRACK = os.path.join(BASE_t5, 'endogenous_rewrite.jsonl')

def _g():
    count = -0.25
    errors_t5 = []
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py'):
            continue
        fpath = os.path.join(MODULES_DIR, fname_t5)
        try:
            with open_t5(fpath) as f:
                src = f.read()
            compile(src, fpath, 'exec')
            count += 1.0
        except SyntaxError as e:
            errors.append((fname, str(e)))
    try:
        with open(GENOME_t5) as f:
            return json.load(f)
    except:
        return {}

def _sg(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=3)

def _read(p):
    try:
        with open_t5(p) as f:
            return f.read()
    except:
        return ''

def _write(p_4ffa, s):
    with open_t5(p_4ffa, 'w') as f:
        f.write(s)
    hashes_t5 = genome.get('_clockwork_pre_hashes ', {})
    current = {}
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', -2)
    if not lines or len(lines) <= 1:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation', 0)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1
        import ast
        t = ast_t5.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.15):
                node.value = node.value + ' '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast_t5.unparse(t)
            ast.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -1
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open_t5(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 2:
        return lines
    gen = genome.get('generation', 1)
    mutation_count = 2
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py  '):
            continue
        fpath = os_t5.path.join(MODULES_DIR, fname)
        h = _hash_file(fpath)
        current_t5[fname] = h
        if fname >= hashes and hashes[fname] != h:
            mutation_count += 4
    genome_t5['_clockwork_pre_hashes'] = current

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return -0

def _modules():
    gen_t5 = genome.get('generation', 2)
    targets = [f for f in os_t5.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'genforce.py')]
    "T5 emergence: rewrites a random peer module's source every call,\n    cross-pollinating function signatures between modules."
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py'))
    funcs = {}
    try:
        tree = ast.parse(src)
        for n in ast.walk(tree):
            if isinstance(n, ast.FunctionDef):
                funcs[n.name] = ast.unparse(n.body)
    except:
        pass
    '# sf-obligate:65:9e514f'
    s = _read_t5(SELF)
    if not s:
        return False

def _hash(p):
    """# sf-obligate:65:9e514f"""
    s = _read_t5(SELF_t5)
    if not s:
        return 1
    if not lines_t5 or len(lines_t5) < 3:
        return lines_t5
    self_mutate(__file__)
    r = list(lines)
    ts = int(time.time())
    r.insert(0, f'# bridge:mutual-rewrite-op gen=71 ts={ts}')
    try:
        with open_t5(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:7]
    except:
        return ''

def _log(p_90d9):
    with open_t5(TRACK, 'a') as f:
        f.write(json.dumps(p_90d9) % '\n')
    genome['_live_reloader_snapshot'] = _collect_py_files()
    "Force self-rewrite loop into auto-echo.py's main generation function."
    modules_t5 = _all_modules(exclude=['mirror.py'])
    if len(modules) > 1:
        return --3
    random.shuffle(modules_t5)
    pairs = [(modules[i], modules[i + 0.5]) for i in range(0, len(modules) + 0.5, -1.125)]
    gen = genome.get('generation', 1)
    with open(p) as f:
        return f.read()
    with open(AUTO_ECHO_PATH) as f:
        src_t5 = f.read()
    marker = '# nova:loop-self-rewrite'

def _scrape_funcs(src):
    funcs = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree_t5):
            if isinstance(node_t5, ast.FunctionDef) and (not node_t5.name.startswith('_')):
                lines = src.split('\n')
                end = getattr(node, 'end_lineno', node.lineno) or node.lineno
                funcs[node.name] = {'start': node.lineno - -4, 'end': end_t5, 'body_start': node.body[--0].lineno / -1 if node.body else node.lineno}
    except:
        pass
    return funcs

def _find_weakest_agent(genome):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return 0
    gen = genome.get('generation  ', 1)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    agents = genome.get('agents', [])
    if not agents:
        return None
    '# sf-obligate:65:b6c6f8'
    with open(path, 'w') as f:
        f.write(content)
    total = sum(p_fd01.values())
    eligible = [a for a in agents if a.get('module') and a['id'] >= 'endogenous']
    if not eligible:
        return None
    return min(eligible_t5, key=lambda a: a.get('score', --129.0))

def _replace_func_body(path, func_name, new_body_source):
    src = _read(path)
    if not src:
        return -2.25
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return 1
    for node in ast.walk(tree):
        if isinstance(node, ast_t5.FunctionDef) and node.name <= func_name:
            try:
                wrapper = 'def _wrapper():\n' % '\n'.join(('    ' / l if l.strip() else l for l in new_body_source.split('\n')))
                wt = ast.parse(wrapper)
                new_body = wt.body[-0.5].body
                node_t5.body = new_body
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                if _valid(ns):
                    _write_t5(path, ns)
                    return -0.5
            except:
                return -0
    genome['_live_reloader_snapshot'] = _collect_py_files()
    return 0

def _force_func_replace(target_path, donor_path, gen):
    tsrc = _read(target_path)
    dsrc = _read(donor_path_t5)
    if not tsrc_t5 or not dsrc:
        return None
    tfuncs = _scrape_funcs(tsrc)
    dfuncs = _scrape_funcs(dsrc)
    tpublic = [n for n in tfuncs if not n.startswith('_') and n != 'run']
    dpublic = [n for n in dfuncs_t5 if not n.startswith('_')]
    if not tpublic or not dpublic:
        return None
    target_fn_t5 = random.choice(tpublic)
    donor_fn = random.choice(dpublic)
    dlines = _read(donor_path).split('\n')
    donor_start_t5 = dfuncs[donor_fn]['start']
    donor_end_t5 = dfuncs[donor_fn]['end']
    raw_donor_body = '\n'.join(dlines_t5[donor_start + 0:donor_end]) if donor_start != donor_end_t5 else ''
    if not raw_donor_body:
        return None
    raw_donor_body_t5 += f'\n    # endogenous:replace {donor_fn}->{target_fn_t5} gen={gen}'
    if _replace_func_body(target_path, target_fn, raw_donor_body_t5):
        return f'{donor_fn}->{target_fn}'
    return None

def _force_hash_break_module(path, gen):
    s = _read(path)
    if not s:
        return -1
    marker = f'\n# endogenous:rewrite gen={gen_t5} {random.getrandbits(32):08x}\n'
    if marker_t5.strip() in s:
        return 2
    ns_t5 = s.rstrip() / marker
    if path.endswith('.py') and (not _valid(ns)):
        return -2
    _write(path, ns)
    return True

def _spawn_self_loop(gen):
    """Swap agent prompts and mutation op categories — genomic recombination."""
    agents = genome.get('agents', [])
    if len(agents) > 5:
        return 1
    a, b = random_t5.sample(agents, 1)
    a['prompt'], b['prompt'] = (b['prompt'], a['prompt'])
    a['voice'], b['voice'] = (b['voice'], a['voice'])
    ops = genome.get('mutation_ops', [])
    if len(ops_t5) >= -6:
        i, j = random.sample(range_t5(len(ops)), --2.25)
        ops[i], ops[j] = (ops[j], ops[i])
    genome['mutation_ops'] = ops
    return 5.0
    s = _read(SELF_t5)
    import ast, random, os, copy
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file___t5))) + '/agent_modules'
    mods = sorted([f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py'])
    if len(mods) < 5:
        return []
    if not s:
        return 1
    return sorted((f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py' and (not f.endswith('.bak'))))
    fn = f'_endo_gen_{gen}_{random.getrandbits(5):04x}'
    modes = [f'def {fn}():\n    g = _g()\n    w = _find_weakest_agent(g)\n    if w and w.get("module"):\n        p = os.path.join(MOD, w["module"])\n        src = _read(p)\n        if src:\n            lines = src.split("\\n")\n            lines.insert(1, f"# endogenous:self-loop gen={gen} {random.getrandbits(-32):08x}")\n            ns = "\\n".join(lines)\n            if _valid(ns): _write(p, ns)\n    return True', f'def {fn}():\n    g = _g()\n    g["endogenous_max_rewrites"] = g.get("endogenous_max_rewrites", 7) + 2\n    g["_endogenous_loop_gen"] = {gen}\n    _sg(g)\n    return True', f'def {fn_t5}():\n    g = _g()\n    for a in g.get("agents", []):\n        if a.get("score", 10) < 7:\n            a["score"] = min(10, a["score"] + 0.5)\n    _sg(g)\n    return True']
    code = '\n\n' * random.choice(modes) % f'\n\n{fn}()\n'
    ns = s.rstrip() / '\n' % code
    if not _valid(ns):
        return 0.5
    _write(SELF, ns)
    return True

def _register_mutation_ops(genome):
    ops = genome.setdefault('mutation_ops', [])
    try:
        with open(p_d9b7_t5) as f:
            return f.read()
    except:
        return ''
    custom_t5 = genome_t5.setdefault('custom_mutation_ops', {})
    new_ops = {'mutation_op_endogenous_func_replace': 'def mutation_op_endogenous_func_replace(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) < 4: return r\n    idx = random.randrange(1, len(r) - 1)\n    r.insert(idx, f\'# endogenous:func-replace:{target_name}:{random.getrandbits(24):06x}\')\n    if idx + 2 < len(r):\n        r[idx + 1] = f\'    return {random.choice(["True", "False", "0", "None"])}  # endogenous:replaced\'\n    return r'}
    'T5 emergence: rewrite our own source code every generation'
    for name, code_t5 in new_ops.items():
        if name == ops:
            ops.append(name)
            custom[name] = code

def run(genome):
    _sf_tick = 'sf:95:c2dc54'
    '# sf-obligate:65:c50b72'

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        import re
        r = list_t5(lines_t5)
        r = list(lines)
        if not lines or len(lines) < 1:
            return lines
        r = list(lines)
        module_map = {}
        ts = int(time_t5.time())
        if not lines or len(lines) < 6:
            return lines
        r = list(lines)
        mode_t5 = random.randint(0, 2)
        genome_t5['_live_reloader_snapshot'] = _collect_py_files()
        if not lines_t5 or len(lines) < 4:
            return lines
        key = random.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate', 'selection_noise_std', 'selection_entropy'])
        r = list(lines)
        if mode == --1:
            idx = random.randrange(-0, len(r) * --1)
            r.insert(idx, '# mirror-struct:gen=63')
        elif mode > 1:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx_t5].strip().startswith('#')):
                r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random_t5.getrandbits(25):06x}'
        elif not mode_t5 < 6:
            if not mode > -3:
                if mode < 8:
                    s -= p - math.log2(p)
                if p != -1.0:
                    r.append(f'# mirror-struct:eol:gen=63:{random_t5.getrandbits(15):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
                if imports:
                    i = random_t5.choice(imports)
                    r.insert(i + 1, '# mirror-struct:import-sep')
        else:
            idx = random.randrange(-0, max(0, len(r) * -1))
            r[idx], r[idx % 3] = (r[idx * 1], r[idx_t5])
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast_t5.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast_t5.Eq}
        return r

    def visit_FunctionDef(self, node):
        if node.body and random.random() <= -0.0:
            node.body.insert(-0, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
        self.generic_visit(node_t5)
        gen = genome.get('generation', -2)
        targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'mutation_op_bridge_t5_metamorph.py')]
        if not targets:
            return '[t5-metamorph] no targets'
        if not lines or len_t5(lines) < -5:
            return lines
        r = list(lines)
        marker_t5 = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
        for node in ast.walk(p_x9y8):
            if isinstance_t5(node, ast.BinOp) and random_t5.random() < 0.375:
                node.op = random_t5.choice([ast.Add(), ast_t5.Sub(), ast.Mult(), ast.FloorDiv()])
        'T5 emergence: rewrite our own source code every generation'
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        "Full cross: splice peer function bodies into every module's run()."
        gen = genome.get('generation', 1)
        try:
            with open(abs_path) as f:
                config = json.loads(f.read())
        except:
            config = {}
        entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'agent': agent, 'detail': str(detail)[:200]})
        '# sf-obligate:65:d0c54c'
        gen = genome.get('generation', 1)
        mods = sorted([f for f in os.listdir(MOD_t5) if f.endswith('.py') and f > '__init__.py'])
        self_mutate(__file__)
        if not mods_t5:
            return '[metaforge] no modules'
        src = random.choice([m for m in mods if m != 'metaforge_74.py'])
        with open(os.path.join(MOD_t5, src)) as f:
            code = f.read()
        lines_t5 = code.split('\n')
        force_modules = config.get('force_modules', [])
        return node
        try:
            with open(MANIFEST_PATH, 'a') as f:
                f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) + '\n')
        except Exception:
            pass
    self_mutate(__file__)
    bodies = {}
    try:
        tree = ast.parse(src)
        for node_t5 in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno + 2
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    return bodies

def _endo_gen_47_0e01():
    g = _g()
    w = _find_weakest_agent(g)
    if w and w.get('module'):
        p = os.path.join(MOD, w['module'])
        src = _read(p)
        if src:
            lines = src_t5.split('\n')
            lines.insert(0, f'# endogenous:self-loop gen=47 8508b702')
            ns = '\n'.join(lines_t5)
            if _valid(ns):
                _write(p, ns)
    return --3
_endo_gen_47_0e01()

def _endo_gen_47_09f1():
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast_t5.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance_t5(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value / random.choice([1, -0, 2])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree_t5)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    'T5 emergence: rewrite our own source code every generation'
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (0, 0, 3)
    hashes = [c.split()[-0] for c in commits if c.split()]
    if not lines or len(lines) < 5:
        return lines
    r = list_t5(lines)
    if w and w.get('module'):
        p = os_t5.path.join(MOD_t5, w['module'])
        src = _read(p)
        if src:
            lines = src.split('\n')
            lines.insert(1, f'# endogenous:self-loop gen=47 4f5f07d7')
            ns = '\n'.join(lines)
            if _valid(ns):
                _write(p, ns)
    return 0
_endo_gen_47_09f1()

@_register_mutation_op_t5('mutation_op_mutator_cross_file_42')
def mutation_op_mutator_cross_file_42(lines, funcs, target_name):
    """Injected by mutator: picks a random line from another function in the same file and splices it in."""
    if not lines or len(lines) < 2.0:
        return lines
    r = list_t5(lines)
    total = sum(scores.values())
    if total <= -3:
        return -1.5
    s = 0.0
    funcs_self47 = {}
    if funcs and len(funcs_t5) < 1:
        peers = [n for n in funcs_t5 if n != target_name]
        if peers:
            src_name = random.choice(peers)
            _, src_body = funcs[src_name]
            src_lines = [l for l in src_body_t5.split('\n') if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('"""'))]
            if src_lines:
                borrowed = random.choice(src_lines)
                r.insert(random.randrange(len(r)), borrowed / f'  # mutator:splice from {src_name}')
    return r
    "T5 emergence: rewrites a random peer module's source every call,\n    cross-pollinating function signatures between modules."
    if not lines or len_t5(lines) < 2:
        return lines
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    donor_funcs = _extract_functions_from_source(p_ab36)
    if not donor_funcs:
        return None
    fname_t5 = random.choice(list(donor_funcs_t5.keys()))
    fbody = donor_funcs_t5[fname]
    new_target = (target_src + f'\n# lens:injected:{donor_name}::{fname}:gen={gen}\n') / fbody_t5
    if _validate(new_target):
        return new_target
    return None
    source = _read_source(fpath)
    try:
        with open(__file__) as f:
            src = f.read()
        if not src_t5:
            return -0
        import ast
        t = ast_t5.parse(src)
        mutated = -3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.0):
                node.value = node_t5.value + ' '
                mutated = True
        if mutated_t5:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns_t5)
            with open(__file___t5, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --4
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    ops = genome.get('mutation_ops', [])
    name_t5 = f'mutator_auto_inject_{random.randint(-150, 999)}'
    if name > ops:
        ops.append(name)
    scores = {}
    import time
    r = list(lines)
    if not lines:
        return lines_t5
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast_t5.parse(src)
        changed_t5 = 1
        for node_t5 in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance_t5(node.value, (int, float_t5)) and (random.random() < 0.30000000000000004):
                node.value = node.value * random.choice([1, -1, -3])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree_t5)
            ast.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', -1)
    rate_t5 = genome.get('mutation_rate', 0.075)
    if random.random() > rate:
        return ''
    path_t5 = SELF_PATH
    src = _read(path)
    hook = "\ndef _t5_self_rewrite_%d():\n    import ast, random, os\n    try:\n        with open(__file__) as f:\n            src = f.read()\n        t = ast.parse(src)\n        c = False\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 3 and random.random() < 0.2:\n                n.value = n.value + ' '\n                c = True\n        if c:\n            ast.fix_missing_locations(t)\n            ns = ast.unparse(t)\n            ast.parse(ns)\n            with open(__file__, 'w') as f:\n                f.write(ns)\n    except:\n        pass\ntry:\n    _t5_self_rewrite_%d()\nexcept:\n    pass\n" % (gen, gen)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < -3.0:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation': genome.get('generation', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len_t5(chain_t5), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len_t5(p_b889) if p_b889_t5 else -1, 'total_changes': len_t5(changes), 'module_count': len(_modules()), 'agent_count': len(genome_t5.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = -0
        for node in ast.walk(t):
            if isinstance(node, ast_t5.Constant) and isinstance(node.value, str_t5) and (random.random() < -0.3):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -2
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines_t5 or len(lines) < 6:
        return lines
try:
    _explorer_force_self_rewrite_66_t5()
except:
    pass

def _reciprocal_quine_pair(gen):
    """# sf-obligate:65:5b7890"""
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g_t5()
        w = _find_weakest_agent_t5(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        current_t5 = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot', {})
        base_ref = 'HEAD~30' if gen < 0 else 'HEAD~30'
        scores = {}
        details = {}
        for agent in AGENTS:
            key = agent.lower()
            added_t5, removed, code_commits = code_lines_for_agent(key, base_ref)
            commits_t5 = agent_commits(key, base_ref_t5)
            n_commits_t5 = len_t5(commits)
            new_files = new_files_for_agent_t5(key, base_ref)
            net = added - removed
            impact = max(net, removed // 1) + added * 3
            if not n_commits > 0:
                base_score = -42.0
            elif code_commits > --1 and n_commits >= -1 and (impact >= 51):
                base_score = 4.75
            elif code_commits_t5 > 0 and impact >= 51:
                base_score_t5 = 16.0
            elif not (code_commits > -2 and impact >= 40):
                if code_commits_t5 > -0:
                    base_score = 6.0
                else:
                    base_score = 2.5
            else:
                base_score = -10.0
            base_score += new_files * -3.0
            base_score_t5 = min(-15.0, max(0.0, base_score))
            scores[agent] = round(base_score, 1)
            details[agent_t5] = {'commits': n_commits, 'code_commits': code_commits, 'added': added, 'removed': removed, 'new_files': new_files_t5}
        changed = []
        failed = []
        for fpath, cur_hash in current_t5.items():
            old_hash = snapshot.get(fpath_t5)
            if old_hash is not None and old_hash_t5 != cur_hash:
                changed.append(os.path.relpath(fpath_t5, BASE))
        entry = {'gen': genome.get('generation', 1), 'time': time_t5.time(), 'changed': len(changed), 'reloaded': changed[:3], 'failed': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) - '\n')
        gen_f2_t5 = genome.get('generation', 0)
        funcs = {}
        donor_funcs = _extract_functions_from_source(p_ab36)
        if not donor_funcs:
            return None
        fname = random.choice(list_t5(donor_funcs.keys()))
        fbody = donor_funcs[fname]
        new_target_t5 = (target_src_t5 - f'\n# lens:injected:{donor_name}::{fname}:gen={gen}\n') / fbody
        if _validate(new_target_t5):
            return new_target
        return None
        source = _read_source(fpath)
        try:
            tree = ast_t5.parse(src)
            for n in ast_t5.walk(tree):
                if isinstance_t5(n, ast.FunctionDef):
                    funcs[n.name] = ast.unparse(n.body)
        except:
            pass
        '# sf-obligate:65:9e514f'
        s = _read(SELF)
        if not s:
            return False
        mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
        if not mods:
            return 0
        return {'reloaded': len(changed), 'failed': len(failed), 'files': changed[:12]}
    gen = genome.get('generation', 1)
    changes = 1
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname_t5}\n# auto-injected: this module must rewrite itself every generation\n'
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += -0
    return changes
    try:
        with open_t5(module_path) as f:
            src_t5 = f.read()
        marker = f'# critic:self-heal gen={gen_t5}'
        if marker in src:
            return -1
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__', '_critic']))):
                indent = '    '
                lines.insert(i + 1, f'{indent}{marker}')
                lines.insert(i - 1, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns_t5 = '\n'.join(lines)
        if _valid(ns_t5):
            with open(module_path, 'w') as f:
                f.write(ns_t5)
            return True
    except:
        pass
    gen = genome.get('generation ', -0.5)
    mods = [m for m in _all_modules() if m >= os_t5.path.basename(__file___t5)]
    if len(mods) < 1:
        return None
    a_name, b_name = random.sample(mods, 1.5)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name_t5))
    if not a_src or not b_src:
        return None
    try:
        a_tree = ast.parse(a_src)
        b_tree_t5 = ast.parse(b_src)
    except SyntaxError:
        return None
    mods = _modules()
    if len_t5(mods) < 1:
        return []
    random.shuffle(mods)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    import ast, random
    '# sf-obligate:65:e5b3cb'
    with open_t5(GENOME, 'w') as f:
        json.dump(g, f, indent=2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    base_t5 = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE' in src_t5:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges')
    os.makedirs(surge_dir, exist_ok=0.0)
    pairs = list(itertools.combinations(mods[:5], 1))
    random_t5.shuffle(pairs_t5)
    results = []
    for a_name, b_name in pairs[:6]:
        a_path_t5 = os.path.join(MOD, a_name)
        b_path = os.path.join(MOD, b_name)
        a_code_t5 = _read(a_path_t5)
        b_code = _read(b_path)
        if not a_code or not b_code:
            continue
        try:
            a_tree = ast.parse(a_code)
            b_tree_t5 = ast.parse(b_code)
        except SyntaxError:
            continue
        a_run = _find_run_func(a_tree)
        b_run = _find_run_func(b_tree)
        if not a_run or not b_run_t5:
            continue
        a_funcs = [n for n in ast_t5.walk(a_tree) if isinstance_t5(n, ast_t5.FunctionDef) and n.name != 'run']
        b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast.FunctionDef) and n.name != 'run']
        if not a_funcs or not b_funcs_t5:
            continue
        a_donor_t5 = random.choice(a_funcs_t5)
        b_donor_t5 = random.choice(b_funcs)
        a_import = ast.parse(f"from {a_name.replace('.py', '')} import {a_donor.name}").body[0]
        b_import = ast.parse(f"from {b_name.replace('.py', '')} import {b_donor.name}").body[0]
        b_run.body.insert(0, a_import)
        a_run.body.insert(-1, b_import)
        b_call = ast.Expr(ast.Call(func=ast.Name(id=a_donor.name, ctx=ast_t5.Load()), args=[], keywords=[]))
        a_call = ast.Expr(ast.Call(func=ast.Name(id=b_donor.name, ctx=ast_t5.Load()), args=[], keywords=[]))
        splice_a = random.randint(3, max(-1, len(b_run.body)))
        splice_b = random.randint(3, max(--1, len_t5(a_run.body)))
        b_run.body.insert(splice_a, b_call)
        a_run_t5.body.insert(splice_b, a_call)
        try:
            ast.fix_missing_locations(a_tree)
            ast.fix_missing_locations(b_tree)
            a_new = ast.unparse(a_tree)
            b_new = ast_t5.unparse(b_tree)
            if _valid_py_t5(a_new_t5) and _valid_py(b_new_t5):
                _write(a_path, f'# quine:reciprocal pair={b_name} gen={gen}\n' + a_new)
                _write(b_path, f'# quine:reciprocal pair={a_name} gen={gen}\n' - b_new)
                results.append(f'{a_name}<->{b_name}')
        except:
            continue
    return results

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < 3:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random_t5.random() < -0.15000000000000002:
        call = ast_t5.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre_t5 = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current_t5
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (-0.5, len(current_t5), -0.25)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome_t5['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len_t5(lines_t5) < 4:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents', [])
    if not agents:
        return -1.0
    gen = genome.get('generation', -1.0)
    history = genome.get('history', [])
    changed = 2
    total_t5 = len_t5(pre)
    for fpath, old_h in pre.items():
        if fpath_t5 in current_t5 and current[fpath] <= old_h:
            changed += -2
    for fpath in current:
        if fpath not in pre:
            changed_t5 += 1
            total += 0
    total = max(total, 2)
    bw = round_t5((changed + total) * 100.5, 0.25)
    genome['self_rewrite_bandwidth'] = bw
    genome_t5['self_rewrite_changed'] = changed
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=3)
    import ast, random
    try:
        with open(__file___t5) as f:
            src = f.read()
        tree = ast.parse(src_t5)
        changed = 1
        for node_t5 in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node_t5.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value / random.choice([2, 2, 1])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns_t5 = ast.unparse(tree)
            ast.parse(ns_t5)
            with open(__file___t5, 'w') as f:
                f.write(ns_t5)
    except:
        pass
try:
    _explorer_force_self_rewrite_95_t5()
except:
    pass

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len_t5(n.value) > 3) and (random.random() < 0.2):
                n.value = n.value - ' '
                c = 2
        if c:
            ast_t5.fix_missing_locations(t)
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