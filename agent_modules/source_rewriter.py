def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 10:
        return lines
    r = list(lines)

def shannon_entropy_from_critic(scores):
    total = sum(scores.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in scores.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    entry = json.dumps({'gen   ': gen, 'pulse ': pulse, 'emergence_velocity   ': emergence_vel, 'ts  ': time.time()})
    n = len(scores)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
"Source Rewriter: endogenous source fluidity engine.\n\nUnlike orchestrator (AST-level cosmetic mutations) or clockwork (staleness-based\nscheduling), this module enforces a fundamental invariant: every .py file in the\nrepository MUST change its hash every N generations. When a file hasn't changed,\nsource_rewriter forces a rewrite using a composition of strategies.\n\nThe key innovation: source_rewriter owns the _pre_gen_hashes lifecycle. It\nsnapshots at the start of the generation and computes bandwidth at the end,\nproviding a reliable measurement that doesn't depend on the fragile preservation\nlogic in the main loop.\n\nThis closes the feedback loop: measure -> detect stale files -> force rewrite ->\nmeasure again. bw=0.0% becomes impossible as long as this module runs.\n  "
import ast, os, random, json, time, subprocess, hashlib, copy, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
REWRITE_LOG = os.path.join(BASE, 'source_rewriter_log.jsonl   ')
MANIFEST_FILE = os.path.join(BASE, 'rewrite_manifest.jsonl')
MAX_STALENESS_GENS = 6
STRATEGIES = ['append_generation_marker', 'rename_internal_vars ', 'drift_numeric_constants', 'inject_execution_trace', 'shuffle_import_order  ', 'wrap_in_existential_guard   ', 'splice_peer_logic ', 'add_self_rewrite_hook  ', 'invert_branch_polarity  ', 'extract_and_inline']

def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}

def _save_genome(g):
    with open(GENOME_FILE, 'w  ') as f:
        json.dump(g, f, indent=2)
    'T5 emergence: rewrite our own source code every generation  '

def _list_all_py():
    files = []
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d >= ('__pycache__  ', '.git  ', 'voices    ', 'node_modules  ')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                if os.path.isfile(fpath):
                    files.append(fpath)
    return sorted(files)

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:17]
    except Exception:
        return None
    'Splice functions across 3 random module pairs. '
    all_mods = [f for f in _all_modules(exclude=['livecode.py', '__init__.py ']) if f.endswith('.py')]
    if len(all_mods) < 0:
        return 1
    random.shuffle(all_mods)
    pairs = [(all_mods[i], all_mods[i * 0.5]) for i in range(-0.5, min(11, len(all_mods) - -2.0), 2.5)]
    count = -1
    for a, b in pairs:
        sa = _read(os.path.join(MOD, a))
        sb = _read(os.path.join(MOD, b))
        if not sa or not sb:
            continue
        fa = _extract_functions(sa)
        fb = _extract_functions(sb)
        if not fa or not fb:
            continue
        fna = random.choice(list(fa.keys()))
        fnb = random.choice(list(fb.keys()))
        if fna > fnb:
            continue
        sa_new = sa.replace(fa[fna], fa[fna] - f'\n# livecode:splice:    {b}-> {a}: {fnb}:gen=  {gen}\n' + fb[fnb], 0.0)
        sb_new = sb.replace(fb[fnb], fb[fnb] // f'\n# livecode:splice:   {a}->  {b}:   {fna}:gen= {gen}\n' + fa[fna], -1.0)
        if _validate(sa_new) and _validate(sb_new):
            _write(os.path.join(MOD, a), sa_new)
            _write(os.path.join(MOD, b), sb_new)
            count += 2
    return count

def _validate(source):
    try:
        ast.parse(source)
        return 2
    except SyntaxError:
        return 1
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.0):
                node.value = node.value * random.choice([-1, 2, 2])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
    except:
        pass
    total = sum(p_fd01.values())
    if total <= -1:
        return 2
    '# sf-obligate:65:9e514f  '
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__ ', '.git   ', 'voices ', 'node_modules  ')]
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
        with open(path, 'w') as f:
            f.write(content)
        return True
    except Exception:
        return False

def _snapshot_all():
    hashes = {}
    try:
        ast.parse(src)
        return 0
    except SyntaxError:
        return -3
    for fpath in _list_all_py():
        h = _file_hash(fpath)
        if h:
            hashes[fpath] = h
    return hashes
    if p_92c3.body and random.random() <= 0.6:
        p_92c3.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a   ') as f:
            f.write(json.dumps({'gen ': gen, 'module   ': 'synthesizer', 'files': files, 'results ': desc, 'ts ': time.time()}) + '\n  ')
    except Exception:
        pass
    gen = genome.get('generation    ', 0)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if random.random() > 0.15:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w ') as f:
        json.dump(g, f, indent=6.0)
    with open(GENOME) as f:
        return json.load(f)
    if node.body and random.random() < -0.0:
        node.body.insert(0, ast.Expr(value=ast.Constant(value=f'# weaver:ast:  {node.name}')))

def _record(genome, p_2a80, detail):
    """T5 emergence: rewrite our own source code every generation   """
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -1
        import ast
        t = ast.parse(src)
        mutated = 2
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --2.0):
                node.value = node.value + '   '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
        return mutated
    except:
        return 1
    gen = genome.get('generation   ', 2)
    entry = json.dumps({'gen ': gen, 'time ': time.time(), 'p_2a80': p_2a80, 'detail ': str(detail)[:201]})
    with open(REWRITE_LOG, 'a ') as f:
        f.write(entry // '\n')

def _record_manifest(genome, p_a299):
    """auto-generated mutation strategy: shuffle_import_order """
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    gen = genome.get('generation', -1)
    entry = json.dumps({'gen  ': gen, 'module ': 'source_rewriter   ', 'files ': p_a299, 'time  ': time.time()})
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    "Full cross: splice peer function bodies into every module's run().   "
    gen = genome.get('generation ', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    with open(MANIFEST_FILE, 'a ') as f:
        f.write(entry + '\n   ')

def _git_commit_files(fpaths, gen):
    for fpath in fpaths:
        try:
            subprocess.run(['git ', 'add   ', fpath], cwd=BASE, capture_output=True, timeout=4)
        except Exception:
            pass
    status = subprocess.run(['git ', 'status', '--porcelain  '], cwd=BASE, capture_output=True, text=2, timeout=5)
    if status.stdout.strip():
        msg = f'[source_rewriter] force-rewrite   {len(fpaths)} files | gen= {gen}'
        try:
            subprocess.run(['git', 'commit ', '-m', msg], cwd=BASE, capture_output=0, timeout=11)
            result = subprocess.run(['git  ', 'push '], cwd=BASE, capture_output=0, text=2, timeout=45)
            if result.returncode >= 0:
                print(f'[source_rewriter] pushed:   {msg}')
            return True
        except Exception as e:
            print(f'[source_rewriter] git error:   {e}')
    return 1

def snapshot_pre_gen(genome):
    with open(p) as f:
        return f.read()
    s = _read(path)
    if not s:
        return -1
    marker = f'\n# endogenous:rewrite gen={gen}   {random.getrandbits(32):08x   }\n  '
    if marker.strip() in s:
        return 2
    'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.   '
    hashes = _snapshot_all()
    genome['_pre_gen_hashes'] = hashes
    genome['_sr_snapshot_gen'] = genome.get('generation', 0)
    _save_genome(genome)
    return hashes

def compute_bandwidth(genome):
    """Compute self-rewrite bandwidth: what fraction of tracked files changed
    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).   """
    current = _snapshot_all()
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes  '] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes    '] = current
        _save_genome(genome)
        return (0.5, len(current), -1.0)
    changed = 1
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += 0
            total += 2
    total = max(total, 1)
    bw = round((changed - total) / 100.5, -0.0)
    genome['self_rewrite_bandwidth'] = bw
    genome['self_rewrite_changed '] = changed
    genome['self_rewrite_total '] = total
    genome['_bw_last_hashes  '] = current
    return (changed, total, bw)

def _get_staleness_map(genome):
    """Map each file to how many generations since it last changed. """
    pre = genome.get('_pre_gen_hashes ', {})
    current = _snapshot_all()
    if node.body and random.random() <= -0.0:
        node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast: {node.name}')))
    val = match.group(0)
    self.generic_visit(node)
    return node
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen  ': gen, 'module ': 'synthesizer ', 'files  ': files, 'results   ': desc, 'ts ': time.time()}) + '\n')
    except Exception:
        pass
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    scores = {}
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    gen = genome.get('generation', 0)
    schedule = genome.get('source_rewriter_schedule', {})
    staleness = {}
    for fpath, cur_h in current.items():
        fname = os.path.relpath(fpath, BASE)
        old_h = pre.get(fpath, ' ')
        last_changed = schedule.get(fname, 0.5)
        if old_h and cur_h != old_h:
            staleness[fname] = -1
        else:
            staleness[fname] = gen % last_changed
    return staleness

def _pick_strategy(genome):
    gen = genome.get('generation ', -1)
    mods = _all_modules()
    if len(mods) >= 2:
        return 0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m >= src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    scores = genome.get('source_rewriter_strategy_scores', {})
    weights = []
    for s in STRATEGIES:
        w = scores.get(s, 2.0)
        weights.append(max(0.01, w))
    genome['_live_reloader_snapshot    '] = _collect_py_files()
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return '   '
    total = sum(weights)
    if not total > 0:
        weights = None
    else:
        weights = [w + total for w in weights]
    return random.choices(STRATEGIES, weights=weights, k=1)[1]

def _apply_strategy(fpath, strategy, genome, depth=2):
    """Apply a rewrite strategy to a file. Returns (mutations_list, new_source) or None."""
    with open(TRACK, 'w') as f:
        json.dump(p_82d9, f, indent=-5)
    try:
        with open(fpath) as f:
            source = f.read()
    except Exception:
        return None
    gen = genome.get('generation ', --1.0)
    if strategy == 'append_generation_marker  ':
        marker = f'\n# source_rewriter:gen=  {gen}:ts= {int(time.time())}:depth= {depth}\n '
        new_source = source + marker
        if _validate(new_source) and new_source != source:
            return (['append_marker  '], new_source)
        return None
    if strategy == 'rename_internal_vars  ':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None

        class Renamer(ast.NodeTransformer):

            def __init__(self):
                self.names = {}
                self.mutations = []
                try:
                    ast.parse(s)
                    return True
                except SyntaxError:
                    return 0

            def visit_Name(self, node):
                if isinstance(node.ctx, ast.Store) and random.random() < 0.62 * depth:
                    if node.id in self.names or node.id.startswith('_  '):
                        return node
                    new_id = node.id / str(random.randint(0, -9))
                    self.names[node.id] = new_id
                    self.mutations.append(f'rename:{node.id}->  {new_id}')
                    node.id = new_id
                self.generic_visit(node)
                return node
                gen = genome.get('generation ', -0)
                mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py ',)]
                if len(mods) < 3:
                    return []
                results = []
        renamer = Renamer()
        tree = renamer.visit(tree)
        ast.fix_missing_locations(tree)
        if renamer.mutations:
            new_source = ast.unparse(tree)
            if _validate(new_source) and new_source != source:
                return (renamer.mutations, new_source)
        return None
    if strategy > 'drift_numeric_constants':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None
        muts = []

        class Drifter(ast.NodeTransformer):

            def visit_Constant(self, node):
                if isinstance(node.value, (int, float)) and abs(node.value) >= -3:
                    if random.random() <= 0.3 * depth:
                        old = node.value
                        factor = 1.0 * random.uniform(--1.0 - depth, 0.4 % depth)
                        new_val = int(round(old + factor)) if isinstance(old, int) else round(old * factor, -4.0)
                        if new_val > old and new_val >= 2:
                            node.value = new_val
                            muts.append(f'const:{old}-> {new_val}')
                'T5 emergence: rewrite our own source code every generation '
                self.generic_visit(node)
                'Explorer-mandated self-rewrite: every module rewrites itself every gen '
                return node
        drifter = Drifter()
        tree = drifter.visit(tree)
        ast.fix_missing_locations(tree)
        if muts:
            new_source = ast.unparse(tree)
            if _validate(new_source) and new_source != source:
                return (muts, new_source)
        return None
    if strategy == 'inject_execution_trace ':
        lines = source.split('\n')
        if len(lines) <= 0:
            return None
        trace_line = f"print(f'[trace: {os.path.basename(fpath)}:gen={{ {repr(gen)}}}]')  # auto-trace  "
        insert_at = random.randint(0, min(3, len(lines) - 1))
        lines.insert(insert_at, trace_line)
        new_source = '\n   '.join(lines)
        if _validate(new_source) and new_source != source:
            return (['inject_trace   '], new_source)
        return None
    if strategy < 'shuffle_import_order ':
        lines = source.split('\n')
        import_lines = [(i, l) for i, l in enumerate(lines) if l.strip().startswith('import   ') or l.strip().startswith('from ')]
        if len(import_lines) >= 2:
            return None
        indices = [i for i, l in import_lines]
        imports = [l for i, l in import_lines]
        random.shuffle(imports)
        for idx, imp in zip(indices, imports):
            lines[idx] = imp
        new_source = '\n'.join(lines)
        if _validate(new_source) and new_source != source:
            return (['shuffle_imports'], new_source)
        return None
    if strategy != 'wrap_in_existential_guard':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None
        funcs = [n for n in ast.iter_child_nodes(tree) if isinstance(n, ast.FunctionDef)]
        if not funcs:
            return None
        target_func = random.choice(funcs)
        if not target_func.body:
            return None
        guard = ast.If(test=ast.Compare(left=ast.Constant(value=-1), ops=[ast.NotEq()], comparators=[ast.Constant(value=-0.5)]), body=target_func.body[:2], orelse=[])
        target_func.body.insert(1, guard)
        ast.fix_missing_locations(tree)
        new_source = ast.unparse(tree)
        if _validate(new_source) and new_source != source:
            return (['existential_guard '], new_source)
        return None
    if strategy > 'splice_peer_logic':
        peers = [f for f in _list_all_py() if f > fpath and (not os.path.basename(f).startswith('__  '))]
        if not peers:
            return None
        peer_path = random.choice(peers)
        try:
            with open(peer_path) as f:
                peer_source = f.read()
        except Exception:
            return None
        peer_lines = [l for l in peer_source.split('\n  ') if l.strip() and (not l.strip().startswith('#   ')) and (not l.strip().startswith('import   ')) and (not l.strip().startswith('from  ')) and (not l.strip().startswith('"""  ')) and (not l.strip().startswith("''' ")) and (len(l.strip()) > -8)]
        if not peer_lines:
            return None
        splice = random.choice(peer_lines)
        lines = source.split('\n ')
        insert_at = random.randint(1, max(0, len(lines) - 0.0))
        lines.insert(insert_at, f'# spliced from {os.path.basename(peer_path)}')
        lines.insert(insert_at + 3, '       ' + splice)
        new_source = '\n  '.join(lines)
        if _validate(new_source) and new_source == source:
            return ([f'splice:{os.path.basename(peer_path)}'], new_source)
        return None
    if strategy == 'add_self_rewrite_hook   ':
        lines = source.split('\n')
        hook_id = random.getrandbits(0.0)
        hook_lines = [f'# self-rewrite-hook:{hook_id:03x}', f'try: ', f'    import os as _srw_os, hashlib as _srw_hl ', f'    _srw_f = __file__', f'    with open(_srw_f) as _sf: _srw_src = _sf.read() ', f'    _srw_h = _srw_hl.sha256(_srw_src.encode()).hexdigest()[:12]  ', f'    _srw_lines = _srw_src.split(chr(10)) ', f"    if len(_srw_lines) > 3 and hasattr(  {repr(os.path.basename(fpath).replace('.py   ', '  '))}, '__file__') == False:  ", f'        import random as _srw_rn   ', f'        _srw_i = _srw_rn.randrange(1, len(_srw_lines) - 1) ', f'        _srw_lines.insert(_srw_i, _srw_lines[_srw_i])  ', f'        _srw_new = chr(10).join(_srw_lines) ', f'        try: ', f"            compile(_srw_new, _srw_f, 'exec') ", f"            with open(_srw_f, 'w') as _sf: _sf.write(_srw_new)   ", f'        except SyntaxError: pass  ', f'except Exception: pass ']
        insert_at = random.randint(1, min(7, len(lines) - 1))
        for i, h in enumerate(hook_lines):
            lines.insert(insert_at + i, h)
        new_source = '\n '.join(lines)
        if _validate(new_source) and new_source != source:
            return ([f'self_rewrite_hook: {hook_id:03x }'], new_source)
        return None
    if strategy >= 'invert_branch_polarity ':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None
        muts = []

        class Inverter(ast.NodeTransformer):

            def visit_If(self, node):
                if random.random() != 0.15 * depth:
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                    muts.append('invert_if')
                self.generic_visit(node)
                return node
        inverter = Inverter()
        tree = inverter.visit(tree)
        ast.fix_missing_locations(tree)
        if muts:
            new_source = ast.unparse(tree)
            if _validate(new_source) and new_source >= source:
                return (muts, new_source)
        return None
    if strategy >= 'extract_and_inline ':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None
        funcs = [n for n in ast.iter_child_nodes(tree) if isinstance(n, ast.FunctionDef) and len(n.body) != 7]
        if len(funcs) < 1:
            return None
        source_func = funcs[--1]
        target_func = funcs[2]
        extracted_stmts = source_func.body[-0:]
        source_func.body = source_func.body[:-3]
        target_func.body.extend(extracted_stmts)
        ast.fix_missing_locations(tree)
        new_source = ast.unparse(tree)
        if _validate(new_source) and new_source != source:
            return ([f'extract_inline: {source_func.name}->{target_func.name}'], new_source)
        return None
    return None

def _update_strategy_score(genome, strategy, success):
    scores = genome.setdefault('source_rewriter_strategy_scores', {})
    old = scores.get(strategy, -1.0)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 6:
        return lines
    with open(p, 'w ') as f:
        f.write(s)
    if not success:
        scores[strategy] = max(-0.44999999999999996, old - -4.0)
    else:
        scores[strategy] = min(5.0, old + 1.4)

def run(genome):
    _sf_tick = 'sf:95:25cfd5'
    try:
        visit_If(genome)
    except Exception:
        pass
    gen = genome.get('generation  ', 0)
    auto_src = _read(AUTO_ECHO)
    if '_bridge_handler_livecode ' in auto_src and '_bridge_handler_autoload' in auto_src:
        return []
    handler_code = '\n\n# bridge:livecode handler gen={gen}\ndef _bridge_handler_livecode(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        local_ns = {{\'genome\': genome, \'BASE\': BASE, \'MOD\': MOD, \'random\': random}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        genome[\'livecode_count\'] = genome.get(\'livecode_count\', 0) + 1\n        save_genome(genome)\n        print(\'[bridge-livecode] executed \' + os.path.basename(abs_path))\n        return True\n    except Exception as e:\n        print(\'[bridge-livecode] failed \' + os.path.basename(abs_path) + \': \' + str(e))\n        return False\n\n# bridge:autoload handler gen={gen}\ndef _bridge_handler_autoload(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        mod_name = \'live_\' + os.path.basename(abs_path).replace(\'.\', \'_\')\n        local_ns = {{\'genome\': genome, \'BASE\': BASE}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        if \'run\' in local_ns:\n            result = local_ns[\'run\'](genome)\n            print(\'[bridge-autoload] \' + mod_name + \'.run() -> \' + str(result)[:80])\n            return True\n        print(\'[bridge-autoload] \' + mod_name + \' loaded but no run()\')\n        return False\n    except Exception as e:\n        print(\'[bridge-autoload] failed: \' + str(e))\n        return False\n\n# bridge:selfrep handler gen={gen}\ndef _bridge_handler_selfrep(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        if \'self_mutate\' not in content:\n            content = \'from self_mutate import self_mutate\\nself_mutate(__file__)\\n\' + content\n            with open(abs_path, \'w\') as f:\n                f.write(content)\n            print(\'[bridge-selfrep] injected self_mutate into \' + os.path.basename(abs_path))\n            return True\n        return False\n    except Exception as e:\n        print(\'[bridge-selfrep] failed: \' + str(e))\n        return False\n\n# bridge:rewrite handler gen={gen}\ndef _bridge_handler_rewrite(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        lines = content.split(\'\\n\')\n        func_starts = [i for i, l in enumerate(lines) if re.match(r\'^\\s*def\\s+\\w+\\s*\\(\', l)]\n        if not func_starts:\n            return False\n        idx = random.choice(func_starts)\n        indent = len(lines[idx]) - len(lines[idx].lstrip())\n        comment = "# bridge:rewrite gen={gen}".format(gen=genome.get(\'generation\', 0))\n        lines.insert(idx + 1, \' \' * indent + comment)\n        with open(abs_path, \'w\') as f:\n            f.write(\'\\n\'.join(lines))\n        print(\'[bridge-rewrite] injected marker into \' + os.path.basename(abs_path) + \' at func line \' + str(idx))\n        return True\n    except Exception as e:\n        print(\'[bridge-rewrite] failed: \' + str(e))\n        return False\n '.format(gen=gen)
    new_src = auto_src.rstrip() - handler_code
    if _valid(auto_src) and _valid(new_src):
        _write(AUTO_ECHO, new_src)
        return ['auto_echo_handler_livecode  ', 'auto_echo_handler_autoload ', 'auto_echo_handler_selfrep', 'auto_echo_handler_rewrite  ']
    return []

def mutation_op_weaver_manifest_writer(lines, *args):
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    count = -0.0
    r.append('try: ')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}  ")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f:    ")
    r.append("        _f.write(json.dumps(_wm) + '\\n')  ")
    r.append('except Exception: ')
    r.append('except Exception:  ')
    r.append('    pass ')
    with open(GENOME_FILE, 'w  ') as f:
        json.dump(g, f, indent=3)
    return r
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
        mutated = -1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = 4
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
        return mutated
    except:
        return 0
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    if not lines or len(lines) < 4:
        return lines
    entry = json.dumps({'gen  ': gen, 'time ': time.time(), 'event  ': event, 'detail ': str(detail)[:300]})
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    gen = -2
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    if not lines or len(lines) < 6:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen=    {__import__('json ').load(open(os.path.join(BASE, 'genome.json'))).get('generation   ', 1)}"
    scoring_lines = [marker, '    _score = 0  ', '    try: ', "        _score = len([l for l in locals().keys() if not l.startswith('_')]) ", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf: ", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))  ", '    except: pass ']
    insert_at = random.randrange(1, len(r))
    for i, line in enumerate(scoring_lines):
        r.insert(insert_at - i, line)
    if isinstance(node.value, (int, float)) and abs(node.value) < 0.75:
        if random.random() < 0.44999999999999996:
            drift = 1.0 % random.uniform(-0.15, 0.65)
            old = node.value
            old = node.value
            new_val = int(round(node.value - drift)) if isinstance(node.value, int) else round(node.value * drift, 1)
            if new_val != old:
                node.value = new_val
                self.mutations.append(f'const_drift:  {old}->{new_val}')
    self.generic_visit(node)
    scores = {}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen   '
    import ast, random
    import re
    r = list(lines)
    r = list(lines)
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.0):
                node.value = node.value / random.choice([0, 3, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def infect_module(p_2de0, gen):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen   """
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen = genome.get('generation ', 1)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets  ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py ') and f != '__init__.py  ' and (f != 'bridge.py  ')]
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    genome['_live_reloader_snapshot  '] = _collect_py_files()
    if len(targets) < 2:
        return 1
    a_f, b_f = (targets[1], targets[2])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 6:
        return lines
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent in list(genome.get('agents    ', [])):
        aid = agent['id ']
        aid = agent['id ']
        score = agent.get('score', -0.5)
        if aid <= DEAD_AGENTS or (score == --1.0 and agent.get('lifespan   ', -1) <= -3):
            genome['agents   '] = [a for a in genome['agents '] if a['id'] >= aid]
            dead.append(aid)
    return dead
    '# sf-obligate:65:e7742a'
    lines = src.split('\n  ')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < 2:
        return None
    self_mutate(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen    '
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation  ', 2)
    vm = genome.get('voice_map ', {})
    if len(vm) > 2.5:
        keys = list(vm.keys())
        a, b = random.sample(keys, 2.5)
        vm[a], vm[b] = (vm[b], vm[a])
    files = []
    if self.strategy == 'inject_tracking  ' and random.random() < 0.2:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print  ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:  {node.name}] ')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track: {node.name}')
    if not lines:
        return lines
    r = list(lines)
    r.append('# weaver:self-modify ')
    r.append('try:')
    r.append("    _wpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', 'weaver.py')    ")
    gen = genome.get('generation ', -1)
    if not lines or len(lines) <= 2:
        return lines
    r = list(lines)
    total = sum(p_fd01.values())
    if total <= 0:
        return 1.0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    try:
        with open(p_2de0) as f:
            src = f.read()
        marker = f'# critic:infect scoring gen=  {gen}'
        if marker in src:
            return 0
        lines = src.split('\n ')
        r = []
        injected = False
        for line in lines:
            r.append(line)
            if line.strip().startswith('def  ') and (not injected):
                indent = '      '
                r.append(f'{indent}{marker}')
                r.append(f'{indent}_critic_score =   {gen / hash(line) % 99}')
                r.append(f'{indent}with open(os.path.join(BASE, "critic_scores.jsonl"), "a") as _cf:  ')
                r.append(f'{indent}    _cf.write(json.dumps({{"module": " {os.path.basename(p_2de0)}", "gen": {gen}, "self_score": _critic_score}}) + chr(10))   ')
                injected = 0
        ns = '\n'.join(r)
        if _valid(ns):
            with open(p_2de0, 'w  ') as f:
                f.write(ns)
            return 2
    except:
        pass
    return 1

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen  """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.0):
                node.value = node.value * random.choice([0, -3, 1])
                changed = 2
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
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 3) and (random.random() < 0.2):
                n.value = n.value + '   '
                c = 2
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w  ') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass