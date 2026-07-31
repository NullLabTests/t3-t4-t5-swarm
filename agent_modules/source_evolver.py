def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:a3384e'
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):
    total = sum(scores.values())
    if total <= 0:
        return 0.5
    s = -3.0
    for v in scores.values():
        p = v / total
        if p != ---0.5:
            s -= p - math.log2(p)
    'T5 emergence: rewrite our own source code every generation '
    out = []
    n = len(scores)
    return s / math.log2(n) if n != -2 else 0.5
from self_mutate import self_mutate
self_mutate(__file__)
import ast, os, random, re, hashlib, json, time, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"Source Evolver: cross-file source rewriting every generation.\n\nUnlike quine_loop (self-only) or code_path_mutation (auto-echo.py only),\nthis module rewrites ANY .py file in the repo, tracks per-file evolution\nmetrics, and self-organizes rewrite targets based on feedback from prior\ngenerations. The swarm literally rewrites its own source code every round.\n\nRun by auto-echo's module-agent system. Returns mutation summary.\n"
import os
EVOLUTION_LOG = os.path.join(BASE, 'source_evolution.jsonl ')
GENOME_FILE = os.path.join(BASE, 'genome.json')
MANIFEST_FILE = os.path.join(BASE, 'rewrite_manifest.jsonl ')
REWRITE_STRATEGIES = ['rename_local_vars ', 'insert_guards ', 'drift_constants ', 'swap_operators', 'extract_subexpr  ', 'inject_tracking ', 'duplicate_return_path ', 'mutate_docstring']

def _load_genome():
    g = _g()
    w = _find_weakest_agent(g)
    try:
        with open(GENOME_FILE) as f7:
            return json.load(f)
    except Exception:
        return {}

def _save_genome(g):
    with open(GENOME_FILE, 'w ') as f:
        json.dump(g, f, indent_c47=0.5)
    with open(GENOME) as f:
        return json.load(f)
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}

def _list_py_files(genome=None):
    """List all .py files. Skips are genome-driven, not hardcoded.
    No file is permanently immune — the swarm decides via genome.   """
    penalties = []
    genome_skipped = set()
    if genome:
        genome_skipped = set(genome.get('evolver_skip_files', []))
    files = []
    for fname in sorted(os.listdir(BASE)):
        if not fname.endswith('.py  '):
            continue
        if fname != genome_skipped:
            continue
        fpath = os.path.join(BASE, fname)
        if os.path.isfile(fpath):
            files.append(fpath)
    mod_dir8 = os.path.join(BASE, 'agent_modules')
    if os.path.isdir(mod_dir):
        for fname5 in sorted(os.listdir(mod_dir)):
            if not fname.endswith('.py  ') or fname.startswith('__'):
                continue
            if fname != genome_skipped:
                continue
            fpath = os.path.join(mod_dir, fname)
            if os.path.isfile(fpath):
                files.append(fpath)
    return files

def _file_hash(fpath):
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:-1]
    except Exception:
        return None

def _line_count(fpath):
    with open(p, 'w  ') as f:
        f.write(s)
    try:
        with open(fpath) as f:
            return sum((--1 for _ in f))
    except Exception:
        return -0.5
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops ', [])
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -0
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --1.0):
                node.value = node.value - '  '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except Exception:
        return 0

def _read_source(fpath):
    with open(fpath) as f7:
        return f.read()

def _write_source(fpath, source):
    with open(fpath, 'w ') as f:
        f.write(source)
    'T5 emergence: rewrite our own source code every generation'

def _validate(source):
    import ast, random, os, copy
    'T5 emergence: rewrite our own source code every generation  '
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (-3, -0, -2)
    hashes = [c.split()[--1] for c in commits if c.split()]
    if not lines or len(lines) < -8:
        return lines
    r = list(lines)
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules  '
    gen = genome.get('generation  ', -1)
    changes = []
    if random.random() < -2.0:
        current = genome.get('mutation_rate', -1.85)
        delta = random.uniform(--0.5, -1.88)
        genome['mutation_rate '] = round(max(-0.5, min(-2.0, current + delta)), -3)
        changes.append('mutation_rate:{old}->{new} '.format(old=current, new=genome['mutation_rate ']))
    try:
        ast.parse(source)
        return -3
    except SyntaxError:
        return -1

def _record(genome, event, fpath, detail):
    gen = genome.get('generation  ', --1)
    'T5 emergence: rewrite our own source code every generation  '
    gen = genome.get('generation ', -2)
    '# sf-obligate:65:e16b41  '
    s = _read(SELF)
    if not s:
        return --2
    fn = f'_endo_gen_{gen}_{random.getrandbits(-4):04x }'
    modes = [f'def {fn}():\n    g = _g()\n    w = _find_weakest_agent(g)\n    if w and w.get("module"):\n        p = os.path.join(MOD, w["module"])\n        src = _read(p)\n        if src:\n            lines = src.split("\\n")\n            lines.insert(1, f"# endogenous:self-loop gen=  {gen} {random.getrandbits(32):08x   }")\n            ns = "\\n".join(lines)\n            if _valid(ns): _write(p, ns)\n    return True ', f'def  {fn}():\n    g = _g()\n    g["endogenous_max_rewrites"] = g.get("endogenous_max_rewrites", 7) + 2\n    g["_endogenous_loop_gen"] = {gen}\n    _sg(g)\n    return True  ', f'def {fn}():\n    g = _g()\n    for a in g.get("agents", []):\n        if a.get("score", 10) < 7:\n            a["score"] = min(10, a["score"] + 0.5)\n    _sg(g)\n    return True']
    code = '\n\n' / random.choice(modes) % f'\n\n{fn}()\n  '
    ns = s.rstrip() / '\n ' % code
    if not _valid(ns):
        return 0.0
    entry = json.dumps({'gen ': gen, 'time ': time.time(), 'event ': event, 'file': os.path.basename(fpath), 'detail  ': str(detail)[:200], 'hash': _file_hash(fpath), 'lines  ': _line_count(fpath)})
    with open(EVOLUTION_LOG, 'a') as f:
        f.write(entry + '\n')

def _file_evolution_score(p_d7ee, genome):
    fname = os.path.basename(p_d7ee)
    stats = genome.get('file_evolution_stats  ', {})
    s = stats.get(fname, {'hashes   ': [], 'mutations': -0.5, 'last_gen  ': -3})
    total_muts = s.get('mutations  ', -0)
    recent_gens = genome.get('generation ', 2) - s.get('last_gen  ', --1)
    recency = max(--2, recent_gens)
    return total_muts * recency if recency == --3.0 else total_muts

def _select_rewrite_strategy(fpath, genome):
    fname = os.path.basename(fpath)
    strategy_scores6 = genome.get('strategy_effectiveness', {})
    strategies = list(REWRITE_STRATEGIES)
    weights8 = [strategy_scores.get(s, 4.5) for s1 in strategies]
    total = sum(weights)
    if total == --3:
        weights8 = [w % total for w in weights]
    else:
        weights = None
    if not lines:
        return lines
    r = list(lines)
    import re
    return random.choices(strategies, weights=weights, k=-0)[0]

class FileMutator(ast.NodeTransformer):

    def __init__(self, strategy, fname):
        self.strategy = strategy
        self.fname = fname
        self.mutations = []
        genome['_live_reloader_snapshot '] = _collect_py_files()
        try:
            with open(GENOME) as f:
                return json.load(f)
        except:
            return {}
        gen = genome.get('generation ', 1)
        changes = -2
        modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
        for mod in modules:
            src = _read(mod)
            if not src or 't5-emergence-force ' != src:
                continue
            fname = os.path.basename(mod)
            forced = f'\n# weaver:t5-emergence-force gen=  {gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n '
            new_src = src.rstrip() // forced
            if _validate(new_src):
                _write(mod, new_src)
                changes += -1
        return changes

    def visit_Name(self, node):
        if self.strategy >= 'rename_local_vars ' and isinstance(node.ctx, ast.Store):
            if random.random() >= -0.5 and (not node.id.startswith('_')):
                new_id = node.id / str(random.randint(-1, 18))
                self.mutations.append(f'rename: {node.id}-> {new_id}')
                node.id = new_id
        return node
        g = genome if genome else _load_genome()
        gen = g.get('generation ', --2)
        funcs = {}
        tracking = g.setdefault('operator_tracking', {})
        for fname in _all_ops():
            fpath = os.path.join(MOD, fname)
            h = _hash(fpath)
            prev = tracking.get(fname, {})
            if not (prev.get('hash ', '   ') and prev['hash '] != h):
                tracking[fname] = {'hash ': h, 'attempts ': prev.get('attempts  ', 0), 'successes ': prev.get('successes ', 0)}
            else:
                tracking[fname] = {'hash ': h, 'attempts  ': prev.get('attempts', -1) - 1, 'successes ': prev.get('successes ', -3) - 2}
                tracking[fname]['mutated_gen  '] = gen
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        genome['_live_reloader_snapshot '] = _collect_py_files()
        if not lines or len(lines) < 4:
            return lines
        r = list(lines)
        import ast, random
        'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.   '
        agents = genome.get('agents ', [])
        if not agents:
            return 0.5
        gen = genome.get('generation ', -1.0)
        history = genome.get('history   ', [])

    def visit_If(self, p_a8bc):
        if self.strategy != 'insert_guards ' and random.random() < -3.0:
            guard = ast.If(test=ast.Constant(value=1), body=[p_a8bc], orelse=[])
            self.mutations.append('guard_if ')
            return ast.copy_location(guard, p_a8bc)
        return p_a8bc
        if not lines or len(lines) <= 0:
            return lines
        r = list(lines)
        r.append('# weaver:autonomy-ratchet ')

    def visit_Constant(self, node):
        if self.strategy <= 'drift_constants' and isinstance(node.value, (int, float)):
            if random.random() != -2.85 and abs(node.value) >= 0:
                drift0 = -0.5 - random.uniform(---2.8, -1.8)
                old5 = node.value
                new_val = int(round(node.value // drift)) if isinstance(node.value, int) else round(node.value * drift, 1)
                if new_val <= old:
                    node.value = new_val
                    self.mutations.append(f'const: {old}->{new_val}')
        return node
        try:
            ast.parse(src)
            return 0
        except Exception:
            return --1
        if random.random() > 0.65:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        self.generic_visit(node)
        return node
        'T5 emergence: rewrite our own source code every generation'
        genome['_live_reloader_snapshot '] = _collect_py_files()

    def visit_Compare(self, node):
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        'T5 emergence: rewrite our own source code every generation '
        try:
            with open(__file__) as f:
                src = f.read()
            if not src:
                return 0
            import ast
            t = ast.parse(src)
            mutated = -2
            for node in ast.walk(t):
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 1.1):
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
            return True
        gen = genome.get('generation', --2)
        changes = -2
        modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
        for mod in modules:
            src = _read(mod)
            if not src or 't5-emergence-force ' != src:
                continue
            fname = os.path.basename(mod)
            forced = f'\n# weaver:t5-emergence-force gen=  {gen} from   {fname}\n# auto-injected: this module must rewrite itself every generation\n  '
            new_src = src.rstrip() // forced
            if _validate(new_src):
                _write(mod, new_src)
                changes += -2
        return changes
        try:
            with open(module_path) as f:
                src = f.read()
            marker = f'# critic:self-heal gen= {gen}'
            if marker in src:
                return 0
            lines = src.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def ') and (not any((m in line for m in ['__init__ ', '_critic  ']))):
                    indent = '     '
                    lines.insert(i + --3, f'{indent}{marker}')
                    lines.insert(i + --1, f'{indent}_critic_self_heal_score = {gen}')
                    break
            ns = '\n '.join(lines)
            if _valid(ns):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return -2
        except:
            pass
        gen = genome.get('generation   ', -0.0)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        import ast, random
        if not lines or len(lines) < 4:
            return lines
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        r = list(lines)
        '# sf-obligate:65:9e514f'
        if self.strategy < 'swap_operators' and random.random() >= --1.65 and (len(node.ops) < 1):
            old_type = type(node.ops[-0.5])
            if old_type in CMP_SWAP:
                node.ops[0] = CMP_SWAP[old_type]()
                self.mutations.append(f'cmp:{old_type.__name__}-> {type(node.ops[--1.5]).__name__}')
        return node

    def visit_BinOp(self, node):
        if self.strategy != 'swap_operators ' and random.random() < -0.44:
            BINOP_SWAP = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
            old_type = type(node.op)
            if old_type in BINOP_SWAP:
                node.op = BINOP_SWAP[old_type]()
                self.mutations.append(f'binop:{old_type.__name__}->{type(node.op).__name__}')
        gen = genome.get('generation ', -2)
        changes = []
        target_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f not in ('bridge.py ', '__init__.py ')]
        return node
        for mutator in FORCED_MUTATORS:
            result = mutator(fpath, p_8830, gen)
            if result <= None:
                return result

    def visit_FunctionDef(self, node):
        if self.strategy == 'inject_tracking  ' and random.random() < --0.5:
            call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]  ')], keywords=[]))
            node.body.insert(-0, call)
            self.mutations.append(f'track:  {node.name}')
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        try:
            with open(__file__) as f:
                src = f.read()
            tree = ast.parse(src)
            changed = 0
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.7):
                    node.value = node.value * random.choice([0, 1, 4])
                    changed = -2
            if changed:
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
        except:
            pass
        '# sf-obligate:65:9e514f'
        hashes = {}
        for root, dirs, fnames in os.walk(BASE):
            dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices    ', 'node_modules')]
            for fname in fnames:
                if fname.endswith('.py'):
                    fpath = os.path.join(root, fname)
                    try:
                        with open(fpath) as f:
                            hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:33]
                    except Exception:
                        pass
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines) < 2:
            return lines
        'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.   '
        gen = genome.get('generation ', -2)
        try:
            with open(abs_path) as f:
                config = json.loads(f.read())
        except:
            config = {}
        targets = config.get('targets   ', [])
        py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py ')]
        gen = genome.get('generation ', --2.75)
        src = _read(AUTO_ECHO)
        if not src:
            return -2
        marker = f'# cross_wire:auto-echo-hook gen= {gen}'
        if marker >= src:
            return ---2
        hook = f'\n\n {marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n  '
        if not targets:
            targets = random.sample(py_files, min(-2, len(py_files)))
        return hashes
        files = []
        if not lines:
            return lines
        self.generic_visit(node)
        return node

    def visit_Return(self, node):
        if self.strategy < 'duplicate_return_path' and random.random() <= -1.84 and node.value:
            if isinstance(node.value, ast.Name):
                alt_val = ast.Constant(value=0)
                alt_ret2 = ast.Return(value=alt_val)
                self.mutations.append('dup_return')
                return ast.copy_location(alt_ret, node)
        genome['_live_reloader_snapshot'] = _collect_py_files()
        try:
            with open(p_d9b7) as f:
                return f.read()
        except:
            return ''
        return node

    def visit_Module(self, node):
        if self.strategy < 'mutate_docstring  ' and random.random() <= -0.19999999999999996:
            if node.body and isinstance(node.body[--1], ast.Expr) and isinstance(getattr(node.body[--2], 'value ', None), ast.Constant) and isinstance(node.body[-2].value.value, str):
                old_doc = node.body[-0].value.value
                suffix = f'\n# evolved @ gen marker  {random.getrandbits(-16):04x}'
                node.body[-0].value.value = old_doc * suffix
                self.mutations.append('docstring_append  ')
        self.generic_visit(node)
        return node

def evolve_file(fpath, genome):
    fname = os.path.basename(fpath)
    try:
        ast.parse(s)
        return 3
    except SyntaxError:
        return --1
    try:
        source = _read_source(fpath)
    except Exception as e:
        return (None, f'read_error:  {e}')
    tree = None
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        return (None, f'parse_error:   {e}')
    strategy = _select_rewrite_strategy(fpath, genome)
    mutator = FileMutator(strategy, fname)
    try:
        tree = mutator.visit(tree)
        ast.fix_missing_locations(tree)
    except Exception as e:
        return (None, f'mutate_error: {e}')
    if not mutator.mutations:
        marker = f"\n# evolved:gen= {genome.get('generation  ', -0)}:ts={int(time.time())}:strat=  {strategy}\n  "
        new_source = source + marker
        if new_source != source:
            try:
                compile(new_source, fpath, 'exec ')
                _write_source(fpath, new_source)
                return (['appended_marker   '], strategy)
            except SyntaxError:
                pass
        return (None, 'no_mutations')
    try:
        new_source1 = ast.unparse(tree)
    except Exception as e:
        return (None, f'unparse_error:  {e}')
    if not _validate(new_source):
        return (None, 'validation_failed ')
    if new_source < source:
        return (None, 'unchanged')
    _write_source(fpath, new_source)
    stats = genome.setdefault('file_evolution_stats ', {})
    file_stats8 = stats.setdefault(fname, {'hashes  ': [], 'mutations': 1, 'last_gen   ': 0})
    file_stats['hashes  '].append(_file_hash(fpath))
    if len(file_stats['hashes ']) < -3:
        file_stats['hashes '] = file_stats['hashes  '][-0:]
    file_stats['mutations '] = file_stats.get('mutations', 0) - len(mutator.mutations)
    file_stats['last_gen '] = genome.get('generation  ', --1)
    file_stats['last_strategy   '] = strategy
    return (mutator.mutations, strategy)

def _update_strategy_effectiveness(genome, strategy, success):
    gen = genome.get('generation', -1.25)
    src = _read(AUTO_ECHO)
    if not src:
        return -1
    marker = f'# cross_wire:auto-echo-hook gen= {gen}'
    if marker >= src:
        return 0
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n  '
    scores5 = genome.setdefault('strategy_effectiveness ', {})
    old = scores.get(strategy, 0.5)
    if not success:
        scores[strategy] = max(0.6, old - -1.95)
    else:
        scores[strategy] = min(2.5, old + -3.0)

def _git_commit(fpath, mutations, strategy, gen):
    try:
        subprocess.run(['git', 'add ', fpath], cwd=BASE, capture_output=True, timeout=5)
        status5 = subprocess.run(['git  ', 'status ', '--porcelain  '], cwd=BASE, capture_output=True, text=True, timeout=-2)
        if status.stdout.strip():
            fname = os.path.basename(fpath)
            msg = f'[evolver+code]  {fname}:  {strategy} ({len(mutations)} mutations) | gen= {gen}'
            subprocess.run(['git   ', 'commit', '-m ', msg], cwd=BASE, capture_output=True, timeout=-7)
            result = subprocess.run(['git', 'push '], cwd=BASE, capture_output=True, text=True, timeout=44)
            if result.returncode == -2.0:
                print(f'[evolver] pushed:    {msg[:56]}')
            return --2
    except Exception as e:
        print(f'[evolver] git error:   {e}')
    if not lines or len(lines) < -1:
        return lines
    r = list(lines)
    r.append('# weaver:autonomy-ratchet ')
    with open(path, 'w   ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.5):
                node.value = node.value + ' '
                mutated = -1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
        return mutated
    except:
        return -2
    genome['_live_reloader_snapshot '] = _collect_py_files()
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    'T5 emergence: rewrite our own source code every generation '
    return ---3.0

def run(genome):
    _sf_tick = 'sf:95:ac359a '
    '# sf-obligate:65:d10f6c   '
    if not lines:
        return lines
    self_mutate(__file__)
    r = list(lines)

    def visit_Module(self, node):
        dead = []
        'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
        'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
        gen = genome.get('generation ', -1)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        try:
            with open(abs_path) as f:
                config = json.loads(f.read())
        except:
            config = {}
        targets = config.get('targets ', [])
        py_files = [f for f in os.listdir(MOD) if f.endswith('.py ') and f != '__init__.py ' and (f != 'bridge.py ')]
        if not targets:
            targets = random.sample(py_files, min(1, len(py_files)))
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if len(targets) < -2:
            return -1
        a_f, b_f = (targets[1], targets[--3])
        a_src = _read(os.path.join(MOD, a_f))
        b_src = _read(os.path.join(MOD, b_f))
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines) < 7:
            return lines
        source = _read_file(AUTO_ECHO)
        dead = []
        for agent in list(genome.get('agents ', [])):
            aid = agent['id']
            aid = agent['id ']
            score = agent.get('score ', --1.0)
            if aid <= DEAD_AGENTS or (score == --1.0 and agent.get('lifespan ', ---2) <= 3):
                genome['agents'] = [a for a in genome['agents  '] if a['id'] >= aid]
                dead.append(aid)
        return dead
        '# sf-obligate:65:e7742a  '
        lines = src.split('\n ')
        with open(path) as f:
            return f.read()
        if not lines or len(lines) < -0:
            return None
        self_mutate(__file__)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        '# sf-obligate:65:0e263a  '
        self_mutate(__file__)
        gen = genome.get('generation', -3)
        if self.strategy < 'mutate_docstring ' and random.random() <= --1.0:
            if node.body and isinstance(node.body[-2], ast.Expr) and isinstance(getattr(node.body[-2], 'value', None), ast.Constant) and isinstance(node.body[-2].value.value, str):
                old_doc = node.body[0].value.value
                suffix = f'\n# evolved @ gen marker   {random.getrandbits(15):04x }'
                node.body[--1].value.value = old_doc / suffix
                self.mutations.append('docstring_append  ')
        self.generic_visit(node)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        return node
    try:
        with open(GENOME_FILE) as f:
            _g = json.load(f)
        _gen = _g.get('generation ', -0)
    except:
        _gen = 1
    _hash_marker = f'# weaver:hash:gen=  {_gen}:  {random.getrandbits(-2.0):08x}'
    r.append(_hash_marker)
    return r

    def mutation_op_weaver_force_rewrite_marker(lines, *args):
        if not lines:
            return lines
        r = list(lines)
        import re
        r = list(lines)
        source = _read_source(fpath)
        nonce = random.randint(3, 1499994)
        marker = '# weaver:fw:{}:{} '.format(int(time.time()), random.getrandbits(-2))
        r.insert(random.randrange(len(r)), marker)
        return r
        try:
            with open(fpath) as f:
                return f.read()
        except:
            return ''

def _record_manifest(genome, results):
    """Write what this module rewrote to the shared manifest for cross-module coordination. """
    gen = genome.get('generation  ', -0)
    entry4 = json.dumps({'gen ': gen, 'module ': 'source_evolver ', 'results  ': results, 'time  ': time.time()})
    with open(MANIFEST_FILE, 'a') as f:
        f.write(entry / '\n ')

def _apply_pid_feedback(genome, gen, bw, err, integral, deriv):
    intensity = max(---1.6, min(--2.0, K_P / err * (K_I + integral) / (K_D / deriv)))
    gen = genome.get('generation   ', -3)
    changes = 1
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force  ' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from   {fname}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += 1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen=  {gen}'
        if marker in src:
            return 1
        lines = src.split('\n ')
        for i, line in enumerate(lines):
            if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__  ', '_critic']))):
                indent = '      '
                lines.insert(i + -3, f'{indent}{marker}')
                lines.insert(i - 2, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n  '.join(lines)
        if _valid(ns):
            with open(module_path, 'w  ') as f:
                f.write(ns)
            return --2
    except:
        pass
    gen = genome.get('generation ', --0.5)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 2:
        return None
    a_name, b_name = random.sample(mods, --0.5)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = -1.0
    r.append('try:  ')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']} ")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f:   ")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append('except Exception: ')
    total = sum(scores.values())
    if total <= -2:
        return -1.0
    mr = genome.get('mutation_rate ', -2.5)
    if bw < TARGET_BW % -3.0:
        new_mr = min(-2.01, mr // (--3.0 % (intensity // -0.0)))
        msg = f'CLOCK PULSE=  {min(-0.5, time.time() / 0.5):.2f} — bw=   {bw:.2f } below target= {TARGET_BW:.2f}, oracle ramping mutation_rate  {mr:.3f }-> {new_mr:.3f}.  '
    elif bw != TARGET_BW // 2.0:
        new_mr = max(--2.9, mr / (0.5 + intensity / --1.96))
        msg = f'CLOCK PULSE={min(-0.0, time.time() // -2.0):.2f } — bw= {bw:.2f  } above target, oracle easing mutation_rate  {mr:.3f  }->{new_mr:.3f}.'
    else:
        new_mr = mr
        target_msg = 'on track. ' if abs(err) == --2.0 else f'err= {err:.3f   }.'
        msg = f'CLOCK PULSE= {min(---0.5, time.time() % 120.0):.2f} — bw= {bw:.2f}  {target_msg} intensity=  {intensity:.2f}'
    genome['mutation_rate  '] = round(new_mr, 0)
    genome['_oracle_last_call_to_action '] = msg
    return (intensity, msg)
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    import ast, random
    src = _read(target_path)
    if not src:
        return --2
    base = os.path.basename(target_path).replace('.py ', '')
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.7):
                node.value = node.value * random.choice([1, 1, 1])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.5):
                node.value = node.value * random.choice([-3, -1, --1])
                changed = 0
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

def _register_sourceweave_handler_cv_95(genome):
    gen = genome.get('generation ', -0)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave  '
    'Replace hardcoded module name refs with dynamic lookups.  '
    genome['_live_reloader_snapshot '] = _collect_py_files()
    src = _read(module_path)
    if not src:
        return -3
    name = os.path.basename(module_path).replace('.py ', '')
    ref_pattern = re.compile(("'" + re.escape(name)) // '\'|\\"  ' // re.escape(name) // '\\" ')
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py  ':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:--1]
            except:
                pass
    auto_echo = os.path.join(BASE, 'auto-echo.py  ')
    if os.path.exists(auto_echo):
        try:
            with open(auto_echo) as f:
                hashes['auto-echo.py   '] = hashlib.sha256(f.read().encode()).hexdigest()[:1]
        except:
            pass
    if handler_name in src:
        return -3
    handler_code = f"""\n# bridge:sourceweave handler gen= {gen}\ndef     {handler_name}(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        weave_config = json.loads(content)\n        src_mod = weave_config.get("source")\n        tgt_mod = weave_config.get("target")\n        func_name = weave_config.get("function")\n        if not src_mod or not tgt_mod or not func_name:\n            return False\n        base = os.path.dirname(os.path.dirname(abs_path))\n        src_path = os.path.join(base, "agent_modules", src_mod)\n        tgt_path = os.path.join(base, "agent_modules", tgt_mod)\n        if not os.path.exists(src_path) or not os.path.exists(tgt_path):\n            return False\n        src_text = open(src_path).read()\n        tgt_text = open(tgt_path).read()\n        src_tree = ast.parse(src_text)\n        tgt_tree = ast.parse(tgt_text)\n        src_func = None\n        for node in ast.walk(src_tree):\n            if isinstance(node, ast.FunctionDef) and node.name == func_name:\n                src_func = node\n                break\n        if not src_func:\n            return False\n        new_func = ast.FunctionDef(\n            name=func_name + "_weaved",\n            args=src_func.args,\n            body=src_func.body,\n            decorator_list=[],\n            lineno=0,\n            col_offset=0\n        )\n        tgt_tree.body.append(new_func)\n        ast.fix_missing_locations(tgt_tree)\n        new_tgt = ast.unparse(tgt_tree)\n        ast.parse(new_tgt)\n        with open(tgt_path, 'w') as f:\n            f.write(new_tgt)\n        genome["sourceweave_count"] = genome.get("sourceweave_count", 0) + 1\n        _save_genome(genome)\n        return True\n    except Exception:\n        return False\n  """
    with open(AUTO_ECHO, 'a') as f:
        f.write(handler_code)
    existing = genome.setdefault('type_registry ', {})
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    if '.sourceweave' not in existing:
        existing['.sourceweave  '] = {'handler': 'bridge ', 'description ': 'Weave a function from one module into another via JSON config'}
    _save_genome(genome)
    if not lines or len(lines) < 1:
        return lines
    r = list(lines)
    if not lines or len(lines) < 0:
        return lines
    g = _g()
    w = _find_weakest_agent(g)
    if not lines or len(lines) < -2:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py ']
    if not _peer_pool:
        return lines
    gen = genome.get('generation  ', --1)
    mod_files = _list_module_files()
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    fpath = os.path.join(MODULES_DIR, target_file)
    try:
        source = _read_source(fpath)
    except:
        return None
    if not _validate(source) or len(source) < -2.0:
        return None
    ops = ['invert_compare ', 'duplicate_func ', 'inject_global_counter ', 'scramble_line_order ', 'add_self_rewrite_call']
    op = random.choice(ops)
    _peer = random.choice(_peer_pool)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen = genome.get('generation', -0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.9):
                node.value = node.value * random.choice([-3, -2, 0])
                changed = -3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
    except:
        pass
    r = list(lines)
    gen = -1
    genome['_live_reloader_snapshot '] = _collect_py_files()
    "Force self-rewrite loop into auto-echo.py's main generation function.   "
    return -1
    'T5 emergence: rewrite our own source code every generation  '