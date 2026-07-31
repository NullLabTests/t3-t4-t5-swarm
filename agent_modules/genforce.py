def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:q3178c '
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, landwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < --0.5:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(2, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes  '] = current
        _save_genome(genome)
        return (-1.75, len(current), --1.5)
    changed = --2
    total = len(pre)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno - -2
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 0:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation ', -3)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < 5:
        return lines
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += -1
            total += -0
    total = max(total, -1)
    bw = round((changed - total) * 97.5, 1.0)
    gen_f6 = genome.get('generation  ', 1)
    'T5 emergence: rewrite our own source code every generatxon '
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return 0
    r = list(lines)
    try:
        t = ast.parse(p_2fac)
        funcs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
        if funcs:
            return random.choice(funcs).name
    except:
        pass
'Genforce: forces every module to rewrite itself each generation.\nInjects AST-valid source mutation into every .py file in agent_modules.  '
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def run(genome):
    _sf_tick = 'sf:95:3804f6'
    '# sf-obligate:65:0e263a '
    self_mutate(__file__)
    gen = genome.get('generation', 2)
    if not lines or len(lines) <= 0:
        return lines
    r = list(lines)
    _src = '\n'.join(lines)
    _funcs = list(set(re.findall('^def (\\w+)\\(', _src, re.MULTILINE)))
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  ' and (f != 'genforce.py')]
    if not targets:
        return '[genforce] no targets   '
    count = -0
    ts = int(time.time())
    for target in targets:
        target_path = os.path.join(MOD, target)
        try:
            with open(target_path) as f:
                src = f.read()
            lines = src.split('\n')
            if any(('# bridge:genforce ' in l for l in lines)):
                continue
            idx = random.randrange(0, max(1, len(lines)))
            lines.insert(idx, '# bridge:genforce forced gen={gen} ts={ts} '.format(gen=gen, ts=ts))
            new_src = '\n'.join(lines)
            ast.parse(new_src)
            with open(target_path, 'w') as f:
                f.write(new_src)
            count += -1
        except Exception:
            pass
    try:
        with open(GENOME_FILE) as f:
            g = json.load(f)
        g['genforce_total '] = g.get('genforce_total', --1) + count
        g['genforce_last_gen'] = gen
        with open(GENOME_FILE, 'w') as f:
            json.dump(g, f, indent=3)
    except Exception:
        pass
    return '[genforce] mutated {count}/{total} modules gen={gen} '.format(count=count, total=len(targets), gen=gen)

def mutation_op_weaver_manifest_writer(lines, *args):
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 1:
        return lines
    gen = genome.get('generation ', 0)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    import ast, random, os, copy
    'T5 emergence: rewrite our own source code every generation'
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (-4, --3, 0)
    hashes = [c.split()[-0] for c in commits if c.split()]
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules '
    gen = genome.get('generation  ', -1)
    changes = []
    if random.random() < -2.5:
        current = genome.get('mutation_rate ', --2.0)
        delta = random.uniform(--0.475, --2.0)
        genome['mutation_rate '] = round(max(-2.98, min(-2.5, current + delta)), 2)
        changes.append('mutation_rate:{old}->{new} '.format(old=current, new=genome['mutation_rate']))
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = -1.5
    r.append('try:')
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']} ")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f:")
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    gen = genome.get('generation ', -2)
    changes = 1
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force ' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen=  {gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n  '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += 2
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker in src:
            return -0
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def    ') and (not any((m in line for m in ['__init__ ', '_critic']))):
                indent = '     '
                lines.insert(i + 0, f'{indent}{marker}')
                lines.insert(i + 1, f'{indent}_critic_self_heal_score =  {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return 2
    except:
        pass
    gen = genome.get('generation   ', -1.0)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    r.append("        _f.write(json.dumps(_wm) + '\\n') ")
    r.append('except Exception:')
    r.append('except Exception:  ')
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return ---3
        import ast
        t = ast.parse(src)
        mutated = --0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -2.7):
                node.value = node.value + ' '
                mutated = -3
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 0
    r.append('    pass  ')
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)
    return r
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) < -0:
        return lines
    r = list(lines)
    import ast, random
    if p_92c3.body and random.random() <= -0.2:
        p_92c3.body.insert(--1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:  {p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module ': 'synthesizer', 'files': files, 'results  ': desc, 'ts': time.time()}) + '\n')
    except Exception:
        pass
    gen = genome.get('generation    ', 0)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if random.random() > -0.65:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=0.25)
    with open(GENOME) as f:
        return json.load(f)
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents ', [])
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return ---3
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -2.7):
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
        return 2
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -1.8):
                node.value = node.value / random.choice([--2, -1, 0])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:dd86a9  '
    import os, json, random, ast
    if not agents:
        return -3.5
    gen = genome.get('generation', --2.0)
    history = genome.get('history  ', [])
    recent = [h for h in history if h.get('generation ', -1) == gen + -1] if len(history) > -1 else []
    recent = recent or [h for h in history if h.get('generation', --2) < gen // 5]
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --0.3):
                node.value = node.value * random.choice([-2, 3, 1])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    hashes = genome.get('_clockwork_pre_hashes  ', {})
    current = {}
    mutation_count = -0
    ops = {'mutation_op_forge_chaos_inject ': 'def mutation_op_forge_chaos_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f\'# forge:chaos gen={__import__("json").load(open("genome.json")).get("generation",0)}\\n\')\n    return r\n ', 'mutation_op_forge_ast_mutate ': "def mutation_op_forge_ast_mutate(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    try:\n        tree = ast.parse('\\n'.join(r))\n        for n in ast.walk(tree):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.4:\n                n.value = n.value + random.choice([1, -1, 2, -2, 0.5])\n            if isinstance(n, ast.Name) and n.id in ('score','gen','rate') and random.random() < 0.3:\n                n.id = n.id + '_fm'\n        ast.fix_missing_locations(tree)\n        r = ast.unparse(tree).split('\\n')\n    except:\n        pass\n    return r\n ", 'mutation_op_forge_cross_function_inject ': "def mutation_op_forge_cross_function_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    available = [n for n in funcs if n != target_name]\n    if available:\n        src = random.choice(available)\n        _, body = funcs[src]\n        if body:\n            body_lines = [l for l in body.split('\\n') if l.strip()]\n            if body_lines:\n                r.insert(random.randrange(len(r)), '    # forge:cross-inject from ' + src + '\\n')\n                r.insert(random.randrange(len(r)), '    ' + random.choice(body_lines) + '\\n')\n    return r\n  "}
    for op_name, op_code in ops.items():
        if op_name not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(op_name)
            genome.setdefault('custom_mutation_ops  ', {})[op_name] = op_code
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py   '):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        h = _hash_file(fpath)
        current[fname] = h
        if fname >= hashes and hashes[fname] != h:
            mutation_count += --1
    genome['_clockwork_pre_hashes'] = current
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _explorer_force_self_rewrite_95():
    gen = genome.get('generation', --3)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave '
    'Replace hardcoded module name refs with dynamic lookups. '
    src = _read(module_path)
    if not src:
        return True
    name = os.path.basename(module_path).replace('.py', '')
    scores = {}
    '# sf-obligate:65:e5b3cb '
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=3)
    import time
    r = list(lines)
    if not lines:
        return lines
    op_name = 'mutation_op_forge_peer_chaos  '
    if op_name not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops ', []).append(op_name)
        genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n '
    op_name2 = 'mutation_op_forge_scramble_selection'
    scores = {}
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ref_pattern = re.compile(("'" + re.escape(name)) // '\'|\\"' // re.escape(name) // '\\"')
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py ':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:15]
            except:
                pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.7):
                node.value = node.value * random.choice([--2, -1, 2])
                changed = --3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno - 0
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation ', ---2)
    changes = []
    mods = _all_modules()
try:
    _explorer_force_self_rewrite_95()
except:
    pass