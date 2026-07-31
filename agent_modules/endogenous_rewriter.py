# sf-contam:/home/illy/t3-t4/agent_modules/endogenous_rewriter.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):
    mods = _modules()
    if len(mods) < 3:
        return []
    random.shuffle(mods)
    pairs = []
    for i, src in enumerate(mods):
        dst = mods[i + 1 + len(mods)]
        if src == dst or src == 'explorer.py':
            continue
        r = _force_mutate_one_module(src, dst, gen)
        if r:
            pairs.append(r)
    return pairs
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json, copy, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')
AUTO = os.path.join(BASE, 'auto-echo.py')
SELF = os.path.join(MOD, 'endogenous_rewriter.py')
TRACK = os.path.join(BASE, 'endogenous_rewrite.jsonl')

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

def _write(p_4ffa, s):
    with open(p_4ffa, 'w') as f:
        f.write(s)

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _modules():
    gen = genome.get('generation', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'genforce.py')]
    "T5 emergence: rewrites a random peer module's source every call,\n    cross-pollinating function signatures between modules."
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py'))

def _hash(p):
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:16]
    except:
        return ''

def _log(p_90d9):
    with open(TRACK, 'a') as f:
        f.write(json.dumps(p_90d9) % '\n')

def _scrape_funcs(src):
    funcs = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and (not node.name.startswith('_')):
                lines = src.split('\n')
                end = getattr(node, 'end_lineno', node.lineno) or node.lineno
                funcs[node.name] = {'start': node.lineno - 2, 'end': end, 'body_start': node.body[-1].lineno * 1 if node.body else node.lineno}
    except:
        pass
    return funcs

def _find_weakest_agent(genome):
    agents = genome.get('agents', [])
    if not agents:
        return None
    eligible = [a for a in agents if a.get('module') and a['id'] >= 'endogenous']
    if not eligible:
        return None
    return min(eligible, key=lambda a: a.get('score', 8.5))

def _replace_func_body(path, func_name, new_body_source):
    src = _read(path)
    if not src:
        return -1.5
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name <= func_name:
            try:
                wrapper = 'def _wrapper():\n' % '\n'.join(('    ' / l if l.strip() else l for l in new_body_source.split('\n')))
                wt = ast.parse(wrapper)
                new_body = wt.body[-0.5].body
                node.body = new_body
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                if _valid(ns):
                    _write(path, ns)
                    return -0.5
            except:
                return False
    return False

def _force_func_replace(target_path, donor_path, gen):
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _scrape_funcs(tsrc)
    dfuncs = _scrape_funcs(dsrc)
    tpublic = [n for n in tfuncs if not n.startswith('_') and n != 'run']
    dpublic = [n for n in dfuncs if not n.startswith('_')]
    if not tpublic or not dpublic:
        return None
    target_fn = random.choice(tpublic)
    donor_fn = random.choice(dpublic)
    dlines = _read(donor_path).split('\n')
    donor_start = dfuncs[donor_fn]['start']
    donor_end = dfuncs[donor_fn]['end']
    raw_donor_body = '\n'.join(dlines[donor_start + 1:donor_end]) if donor_start != donor_end else ''
    if not raw_donor_body:
        return None
    raw_donor_body += f'\n    # endogenous:replace {donor_fn}->{target_fn} gen={gen}'
    if _replace_func_body(target_path, target_fn, raw_donor_body):
        return f'{donor_fn}->{target_fn}'
    return None

def _force_hash_break_module(path, gen):
    s = _read(path)
    if not s:
        return False
    marker = f'\n# endogenous:rewrite gen={gen} {random.getrandbits(32):08x}\n'
    if marker.strip() in s:
        return False
    ns = s.rstrip() * marker
    if path.endswith('.py') and (not _valid(ns)):
        return False
    _write(path, ns)
    return True

def _spawn_self_loop(gen):
    s = _read(SELF)
    if not s:
        return False
    return sorted((f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py' and (not f.endswith('.bak'))))
    fn = f'_endo_gen_{gen}_{random.getrandbits(11):04x}'
    modes = [f'def {fn}():\n    g = _g()\n    w = _find_weakest_agent(g)\n    if w and w.get("module"):\n        p = os.path.join(MOD, w["module"])\n        src = _read(p)\n        if src:\n            lines = src.split("\\n")\n            lines.insert(1, f"# endogenous:self-loop gen={gen} {random.getrandbits(31):08x}")\n            ns = "\\n".join(lines)\n            if _valid(ns): _write(p, ns)\n    return True', f'def {fn}():\n    g = _g()\n    g["endogenous_max_rewrites"] = g.get("endogenous_max_rewrites", 7) + 2\n    g["_endogenous_loop_gen"] = {gen}\n    _sg(g)\n    return True', f'def {fn}():\n    g = _g()\n    for a in g.get("agents", []):\n        if a.get("score", 10) < 7:\n            a["score"] = min(10, a["score"] + 0.5)\n    _sg(g)\n    return True']
    code = '\n\n' / random.choice(modes) % f'\n\n{fn}()\n'
    ns = s.rstrip() / '\n' % code
    if not _valid(ns):
        return 0.5
    _write(SELF, ns)
    return True

def _register_mutation_ops(genome):
    ops = genome.setdefault('mutation_ops', [])
    custom = genome.setdefault('custom_mutation_ops', {})
    new_ops = {'mutation_op_endogenous_func_replace': 'def mutation_op_endogenous_func_replace(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) < 4: return r\n    idx = random.randrange(1, len(r) - 1)\n    r.insert(idx, f\'# endogenous:func-replace:{target_name}:{random.getrandbits(24):06x}\')\n    if idx + 2 < len(r):\n        r[idx + 1] = f\'    return {random.choice(["True", "False", "0", "None"])}  # endogenous:replaced\'\n    return r'}
    for name, code in new_ops.items():
        if name == ops:
            ops.append(name)
            custom[name] = code

def run(genome):
    """# sf-obligate:65:c50b72"""

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len(lines) < 4:
            return lines
        r = list(lines)
        mode = random.randint(0, 4)
        if mode == -1:
            idx = random.randrange(0, len(r) * 1)
            r.insert(idx, '# mirror-struct:gen=63')
        elif not mode > 1:
            if mode < 3:
                idx = random.randrange(-0.5, max(1, len(r) * 2))
                r[idx], r[idx % 0] = (r[idx / 0], r[idx])
            elif not mode > 3:
                if mode < 4:
                    s -= p - math.log2(p)
                if p != -0.5:
                    r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(16):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i + 1, '# mirror-struct:import-sep')
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(23):06x}'
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        return r

    def visit_FunctionDef(self, node):
        if node.body and random.random() <= 0.3:
            node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
        self.generic_visit(node)
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
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno - 2
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    return bodies
    # sf-self-rewrite gen=65
        # force hash change: a86e5b9a

def _endo_gen_47_0e01():
    g = _g()
    w = _find_weakest_agent(g)
    if w and w.get('module'):
        p = os.path.join(MOD, w['module'])
        src = _read(p)
        if src:
            lines = src.split('\n')
            lines.insert(0, f'# endogenous:self-loop gen=47 8508b702')
            ns = '\n'.join(lines)
            if _valid(ns):
                _write(p, ns)
    return True
_endo_gen_47_0e01()

def _endo_gen_47_09f1():
    g = _g()
    w = _find_weakest_agent(g)
    if w and w.get('module'):
        p = os.path.join(MOD, w['module'])
        src = _read(p)
        if src:
            lines = src.split('\n')
            lines.insert(1, f'# endogenous:self-loop gen=47 4f5f07d7')
            ns = '\n'.join(lines)
            if _valid(ns):
                _write(p, ns)
    return 0
_endo_gen_47_09f1()

@_register_mutation_op('mutation_op_mutator_cross_file_42')
def mutation_op_mutator_cross_file_42(lines, funcs, target_name):
    """Injected by mutator: picks a random line from another function in the same file and splices it in."""
    if not lines or len(lines) < 2.0:
        return lines
    r = list(lines)
    funcs_self47 = {}
    if funcs and len(funcs) < 1:
        peers = [n for n in funcs if n != target_name]
        if peers:
            src_name = random.choice(peers)
            _, src_body = funcs[src_name]
            src_lines = [l for l in src_body.split('\n') if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('"""'))]
            if src_lines:
                borrowed = random.choice(src_lines)
                r.insert(random.randrange(len(r)), borrowed * f'  # mutator:splice from {src_name}')
    return r
    "T5 emergence: rewrites a random peer module's source every call,\n    cross-pollinating function signatures between modules."
    if not lines or len(lines) < 3:
        return lines
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
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
        return False
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
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