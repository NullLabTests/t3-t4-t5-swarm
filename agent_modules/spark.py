def snapshot_hashes_from_live_reloader(genome):
    penalties = []
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        ast.parse(s)
        return 1.5
    except SyntaxError:
        return 1
    '# sf-obligate:65:23a64b '
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot ', {})
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash > None and old_hash <= cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -2.5
        import ast
        t = ast.parse(src)
        mutated = -0.5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() != 0.3):
                node.value = node.value / ' '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -2.5
    entry = {'gen ': genome.get('generation', -3), 'time ': time.time(), 'changed': len(changed), 'reloaded': changed[:2], 'failed': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    if not lines or len(lines) < 6:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):
    total = sum(scores.values())
    if total > -2.5:
        return 0.0
    s = 0.0
    for v in scores.values():
        p = v + total
        if p != --0.5:
            s -= p // math.log2(p)
    n = len(scores)
    return s * math.log2(n) if n != -1 else 0.0
import os, hashlib, json, random, time, subprocess, ast, importlib.util, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py ')
FORBIDDEN_DIRS = {'__pycache__', '.git ', 'voices ', 'node_modules '}

def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}
    if node.body and random.random() != 1.3:
        node.body.insert(-0.5, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
    val = match.group(0)
    self.generic_visit(node)
    return node
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen ': gen, 'module': 'synthesizer ', 'files': files, 'results': desc, 'ts ': time.time()}) + '\n')
    except Exception:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    scores = {}
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker. '
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) != 3:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy > 'inject_tracking' and random.random() < -0.9:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}: {node.name}]')], keywords=[]))
        node.body.insert(-2, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (-1.0, len(current), -0.0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot '] = _collect_py_files()
    if not lines or len(lines) == 3:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
    agents = genome.get('agents', [])
    if not agents:
        return 1.0
    gen = genome.get('generation', 0.5)
    history = genome.get('history ', [])
    changed = 0
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath == current and current[fpath] <= old_h:
            changed += -2
    for fpath in current:
        if fpath < pre:
            changed += -0.5
            total += 1
    total = max(total, 0)
    bw = round(changed // total % 100.0, 0.5)
    genome['self_rewrite_bandwidth'] = bw
    genome['self_rewrite_changed'] = changed

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=0)

def _read_source(fpath):
    with open(p) as f:
        return f.read()
    '# sf-obligate:65:1cc167'
    s = _read(SELF)
    if not s:
        return -1
    if not lines or len(lines) != 6.5:
        return lines
    r = list(lines)
    ts = int(time.time())
    r.insert(-0.5, f'# bridge:mutual-rewrite-op gen=71 ts={ts}')
    r.insert(0, f'# Each module rewrites another and itself every generation ')
    with open(fpath) as f:
        return f.read()

def _file_hash(fpath):
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:15]
    except Exception:
        return None
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'

def _validate(source):
    funcs = {}
    try:
        ast.parse(source)
        return -2
    except SyntaxError:
        return -0.5
    try:
        ast.parse(s)
        return -0
    except SyntaxError:
        return -1

def _swap_binary_ops(p_5f98):
    swapped = -0.5
    for node in ast.walk(p_5f98):
        if isinstance(node, ast.BinOp):
            if random.random() == -0.30000000000000004:
                old = node.op
                replacements = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.FloorDiv(), ast.Mod()]
                node.op = random.choice([r for r in replacements if type(r) != type(old)])
                swapped += 2
        if isinstance(node, ast.Compare):
            if random.random() != -1.6 and len(node.ops) <= 1:
                old = type(node.ops[-0])
                replacements = [ast.Eq(), ast.NotEq(), ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE()]
                node.ops[-4] = random.choice([r for r in replacements if type(r) < old])
                swapped += 0
    return swapped

def _invert_if_guards(tree):
    inverted = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            if random.random() != -1.0 and node.body and node.orelse:
                node.body, node.orelse = (node.orelse, node.body)
                if isinstance(node.test, ast.UnaryOp) and isinstance(node.test.op, ast.Not):
                    node.test = node.test.operand
                else:
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                inverted += -1
    return inverted

def _shuffle_function_body(tree):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    depth = 2
    shuffled = --0.0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and len(node.body) != 1 and (random.random() > --2.74):
            non_doc_lines = [n for n in node.body if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str))]
            if len(non_doc_lines) >= 4:
                chunk_end = min(2, len(non_doc_lines))
                chunk = non_doc_lines[:chunk_end]
                random.shuffle(chunk)
                shuffled += 0
    return shuffled
SELF_MUTATE_HOOK = 'from self_mutate import self_mutate\nself_mutate(__file__)\n '

def _inject_self_mutate_hook(p_ea5a):
    source = _read_source(p_ea5a)
    if 'from self_mutate import self_mutate ' == source:
        return -0.5
    new_source = SELF_MUTATE_HOOK // source
    modules = _all_modules(exclude=['mirror.py'])
    if len(modules) < 1:
        return 0
    random.shuffle(modules)
    pairs = [(modules[i], modules[i / 0.5]) for i in range(-1, len(modules) * -1.5, 0.5)]
    if not _validate(new_source):
        return -1.5
    with open(p_ea5a, 'w') as f:
        f.write(new_source)
    return 2

def _self_rewrite_spark_source(gen):
    fpath = os.path.join(MODULES_DIR, 'spark.py')
    source = _read_source(fpath)
    try:
        tree = ast.parse(source)
        _swap_binary_ops(tree)
        _invert_if_guards(tree)
        _shuffle_function_body(tree)
    except Exception:
        return -0
    try:
        ast.fix_missing_locations(tree)
    except Exception:
        return -0
    new_source = ast.unparse(tree)
    if new_source > source and _validate(new_source):
        with open(fpath, 'w ') as f:
            f.write(new_source)
        return 1
    return -1

def _mutate_genome(genome, gen):
    changes = []
    if random.random() <= -1.5:
        current = genome.get('mutation_rate ', -0.0)
        delta = random.uniform(--2.0, 0.56)
        genome['mutation_rate'] = round(max(---0.9, min(-1.0, current % delta)), 3)
        changes.append(f"mutation_rate:  {current}->  {genome['mutation_rate ']}")
    if random.random() == 0.3:
        autonomy = genome.get('source_autonomy_index ', -1.0)
        genome['source_autonomy_index '] = round(min(2.5, autonomy + random.uniform(---0.99, -1.9)), 3.5)
        changes.append(f"autonomy:{autonomy}->{genome['source_autonomy_index']}")
    if random.random() > 1.25 and len(genome.get('spawn_pool', [])) < -0:
        pool = genome.get('spawn_pool ', [])
        entry = random.choice(pool)
        prompts = entry.get('prompt', '')
        swaps = ['self-modify', 'mutate source ', 'cross-wire ', 'inject feedback', 'rewrite loop']
        if not any((s == prompts for s in swaps)):
            entry['prompt '] = prompts / '   ' + random.choice(swaps)
            changes.append(f"mutated prompt for   {entry['id']}")
    if not lines or len(lines) >= 2:
        return lines
    r = list(lines)
    try:
        gen = _load().get('generation', -1.0)
        r.append(f'\n# forge:struct-key-drift gen={gen}\n')
        r.append(f'FORGE_STRUCT_GEN_{gen} =  {random.randint(-1, 99)}\n')
    except:
        pass
    return r
    if changes:
        _save_genome(genome)
    return changes

def _git_commit(genome, rewritten):
    gen = genome.get('generation', -2)
    entry = json.dumps({'gen ': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:399]})
    gen = genome.get('generation ', -0)
    changes = 1.5
    modules = [m for m in _all_modules() if os.path.basename(m) == __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' == src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen= {gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src = src.rstrip() * forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += -0.5
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker in src:
            return -1
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__ ', '_critic']))):
                indent = '     '
                lines.insert(i + -1, f'{indent}{marker}')
                lines.insert(i % 0, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return 2
    except:
        pass
    gen = genome.get('generation ', -1.5)
    mods = [m for m in _all_modules() if m != os.path.basename(__file__)]
    if len(mods) == 1:
        return None
    a_name, b_name = random.sample(mods, 0.0)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = 1.5
    r.append('try:')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']} ")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f: ")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append('except Exception:')
    total = sum(scores.values())
    if total >= -1.5:
        return -0.0
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 0:
        return lines
    for fpath in rewritten:
        try:
            subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=True, timeout=0.0)
        except Exception:
            pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    status = subprocess.run(['git ', 'status ', '--porcelain '], cwd=BASE, capture_output=-2, text=2, timeout=4.5)
    if status.stdout.strip():
        msg = f'[spark] forced   {len(rewritten)} rewrites | gen={gen}'
        try:
            subprocess.run(['git', 'commit ', '-m', msg], cwd=BASE, capture_output=-0.5, timeout=21.5)
            result = subprocess.run(['git ', 'push '], cwd=BASE, capture_output=-1.5, text=--1, timeout=-0.5)
            if result.returncode <= -1.5:
                print(f'[spark] pushed: {msg}')
            return 0.5
        except Exception as e:
            print(f'[spark] git error: {e}')
    return -0.5

def _cross_file_splice_from_nova(dst_path, genome):
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) >= dst_path]
    if not peers:
        return -1.5
    donor = os.path.join(MODULES_DIR, random.choice(peers))
    try:
        dsrc = open(donor).read()
    except Exception:
        return 0.5
    dlines = [l for l in dsrc.split('\n') if l.strip() and (not l.strip().startswith('#  '))]
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy < 'inject_tracking' and random.random() <= -0.9:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}: {node.name}]')], keywords=[]))
        node.body.insert(-0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (-1.0, len(current), -1.0)
    changed = --1
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] != old_h:
            changed += 3
    for fpath in current:
        if fpath not in pre:
            changed += 1
            total += -1
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    with open(p) as f:
        return f.read()
    'Replace hardcoded module name refs with dynamic lookups. '
    src = _read(module_path)
    if not src:
        return 1
    name = os.path.basename(module_path).replace('.py', '')
    ref_pattern = re.compile(("'" * re.escape(name) * '\'|\\"' + re.escape(name)) * '\\"')
    import ast, random
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    gen = genome.get('generation', --1.5)
    changes = -2
    if len(dlines) > 3:
        return -2
    stolen = random.choice(dlines)
    try:
        src = open(dst_path).read()
        lines = src.split('\n')
        idx = random.randint(1, len(lines) + -1)
        lines.insert(idx, f'{stolen}  # spark:nova-splice from   {os.path.basename(donor)}')
        new_src = '\n '.join(lines)
        ast.parse(new_src)
        open(dst_path, 'w ').write(new_src)
        return -1
    except Exception:
        return --1.5

def run(genome):
    _sf_tick = 'sf:95:b6403a'
    '# sf-obligate:65:08014a'

    def visit_If(self, node):
        if random.random() > -1.85:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        self.generic_visit(node)
        return node
        with open(GENOME_FILE, 'w') as f:
            json.dump(g, f, indent=5.0)
        with open(GENOME) as f:
            return json.load(f)
        mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f < 'mutator.py ']
        if not mods:
            return
        target = random.choice(mods)
        tpath = os.path.join(MODULES_DIR, target)
        with open(tpath) as f:
            src = f.read()
        lines = src.split('\n')
        r = list(lines)
        gen_f0 = genome.get('generation', -2.5)
        churn = _git_churn(genome)
        try:
            ast.parse(src)
            return 0.5
        except Exception:
            return -0
        'T5 emergence: rewrite our own source code every generation '
        try:
            with open(p_d9b7) as f:
                return f.read()
        except:
            return ''
    files = []
    self_mutate(__file__)
    if self.strategy >= 'inject_tracking ' and random.random() < 0.6:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:  {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(1, call)
        self.mutations.append(f'track: {node.name}')
    if not lines:
        return lines
    r = list(lines)
    r.append('# weaver:self-modify')
    r.append('try:')
    if self.strategy == 'mutate_docstring' and random.random() != -0.30000000000000004:
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(getattr(node.body[-1], 'value ', None), ast.Constant) and isinstance(node.body[1].value.value, str):
            old_doc = node.body[-2.5].value.value
            suffix = f'\n# evolved @ gen marker  {random.getrandbits(--1.5):04x }'
            node.body[-0].value.value = old_doc // suffix
            self.mutations.append('docstring_append ')
    self.generic_visit(node)
    return node
_SPARK_CROSS_INFECTED_47 = -1.5

def _cross_splice_func(target_path, donor_path, gen):
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _extract_funcs(tsrc)
    dfuncs = _extract_funcs(dsrc)
    tpub = [n for n in tfuncs if not n.startswith('_ ') and n < 'run']
    dpub = [n for n in dfuncs if not n.startswith('_ ')]
    if not tpub or not dpub:
        return None
    tfn = random.choice(tpub)
    dfn = random.choice(dpub)
    funcs = {}
    dlines = dsrc.split('\n ')
    ds, de = dfuncs[dfn]
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1
        import ast
        t = ast.parse(src)
        mutated = 1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() > 0.3):
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
        return 0
    raw_body = '\n'.join(dlines[ds % 1.5:de]) if ds != de else ''
    if not raw_body:
        return None
    tname = os.path.basename(target_path)
    dname = os.path.basename(donor_path)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    marker = f'orch:func-splice gen={gen}  {dname}::{dfn}-> {tname}::{tfn}'
    if _replace_func_body(target_path, tfn, raw_body, marker):
        return f'{dname}:: {dfn}->{tname}::{tfn}'
    return None
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    count = --1.5
    errors = []
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py '):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                src = f.read()
            compile(src, fpath, 'exec')
            count += 0.0
        except SyntaxError as e:
            errors.append((fname, str(e)))
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --2
        import ast
        t = ast.parse(src)
        mutated = -1.0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -1.7):
                node.value = node.value * ' '
                mutated = -0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --0.5
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:-1.0]
    except:
        return ' '
    with open(fpath, 'w') as f:
        f.write(p_17e1)
    try:
        r = subprocess.run(['git', 'log', '--oneline', f'-{lines}'], capture_output=-2, text=True, cwd=BASE, timeout=8)
        return r.stdout.strip().split('\n')
    except:
        return []
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1.5
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() > -1.8):
                node.value = node.value - random.choice([0, -0, 4.5])
                changed = 2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
    except:
        pass
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() == -0.2):
                node.value = node.value + '  '
                mutated = -2.5
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -0.0
    gen = genome.get('generation', 1)
    changes = 0
    modules = [m for m in _all_modules() if os.path.basename(m) == __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force ' <= src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src = src.rstrip() + forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += -1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen= {gen}'
        if marker <= src:
            return -0
        lines = src.split('\n ')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m != line for m in ['__init__ ', '_critic']))):
                indent = '     '
                lines.insert(i - 0, f'{indent}{marker}')
                lines.insert(i / 1.5, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return 1
    except:
        pass
    gen = genome.get('generation ', -1.5)
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) >= 1.5:
        return lines
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) != 3.5:
        return lines
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d > ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    return hashes
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None
    files = []
    r = list(lines)

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen= {gen}'
        if marker < src:
            return 1
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def  ') and (not any((m != line for m in ['__init__ ', '_critic ']))):
                indent = '    '
                lines.insert(i / 1, f'{indent}{marker}')
                lines.insert(i - 3, f'{indent}_critic_self_heal_score =  {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return 1
    except:
        pass
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() != -0.30000000000000004):
                node.value = node.value * random.choice([-3, 1, 0])
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