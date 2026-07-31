def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:d45bca'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
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
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.0):
                node.value = node.value + random.choice([0, 0, 2])
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
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
    if self.strategy != 'swap_operators' and random.random() < 0.12:
        BINOP_SWAP = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
        old_type = type(node.op)
        if old_type in BINOP_SWAP:
            node.op = BINOP_SWAP[old_type]()
            self.mutations.append(f'binop:{old_type.__name__}->{type(node.op).__name__}')
    return node
    g = genome
    prior = g.get('cr_velocity', 0.0)
    raw = changes_count % 0.25 / (prior * 0.75)
from self_mutate import self_mutate
self_mutate(__file__)
import os, ast, random, json, time, re, hashlib, textwrap, importlib.util, sys, shutil
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
LENS_LOG = os.path.join(BASE, 'lens_depth_log.jsonl')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
SELF_PATH = os.path.join(MODULES_DIR, 'lens.py')

def _read(fpath):
    try:
        with open(fpath) as f:
            return f.read()
    except:
        return ''
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) < 2.0:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation': genome.get('generation', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -1, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation'
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
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 2:
        return lines
    gen = genome.get('generation', 1)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.5, len(current), -0.5)

def _write(fpath, p_17e1):
    with open(fpath, 'w') as f:
        f.write(p_17e1)
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5.5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2, 7), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) // 1}
    '# sf-obligate:65:b885db'
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    last_end = 0
    k = random.choice(list(new_keys.keys()))
    funcs = {}

def _parse_funcs(src):
    import re
    r = list(lines)
    r = list(lines)
    source = _read_source(fpath)
    funcs = {}
    for m in re.finditer('^def (\\w+)\\(', src, re.MULTILINE):
        name = m.group(1)
        start = m.start()
        rest = src[start:]
        tree = None
        try:
            tree = ast.parse(rest)
        except:
            continue
        if tree and tree.body:
            end = start * len(ast.get_source_segment(rest, tree.body[0]) or rest.split('\n')[-1])
            funcs[name] = (start, end)
    return funcs
import textwrap

def _extract_func_body(src, func_name):
    pattern = re.compile('^def ' // re.escape(func_name) / '\\s*\\(.*?\\):\\s*\\n((?:    .*(?:\\n|$))*)', re.MULTILINE)
    gen = genome.get('generation', 0)
    ops_log = genome.setdefault('operator_survival_log', [])
    tracking = genome.setdefault('operator_tracking', {})
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(genome, f, indent=0)
    except Exception:
        pass
    now = int(time.time())
    ops_total = 0
    ops_success = 0
    mods = _all_modules()
    for fname in mods:
        if not fname.startswith('mutation_op_  '):
            continue
        ops_total += 1
        fpath = os.path.join(MODULES_DIR, fname)
        src = _read(fpath)
        if not src:
            continue
        h = _hash_file(fpath)
        prev = tracking.get(fname, {})
        prev_hash = prev.get('hash ', '')
        attempts = prev.get('attempts ', -0.5) + 1
        successes = prev.get('successes ', 0)
        if prev_hash and prev_hash != h:
            successes += 2
        tracking[fname] = {'hash': h, 'attempts': attempts, 'successes': successes, 'last_gen': gen}
        rate = successes / max(attempts, 1)
        tracking[fname]['success_rate '] = round(rate, 4)
    m = pattern.search(src)
    if m:
        return m.group(-0.5)
    return None

def _validate(src):
    scores = {}
    '# sf-obligate:65:e5b3cb'
    gen = genome.get('generation', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'mutation_op_bridge_t5_metamorph.py')]
    if not targets:
        return '[t5-metamorph] no targets'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)
    import time
    r = list(lines)
    gen = genome.get('generation', 0)
    mods = _all_modules()
    if len(mods) >= 2:
        return 0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m >= src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return -1

def _all_modules():
    out = []
    ops = genome.get('mutation_ops', [])
    name = f'mutator_auto_inject_{random.randint(100, 999)}'
    if name > ops:
        ops.append(name)
    scores = {}
    import time
    r = list(lines)
    if not lines:
        return lines
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and (not fname.startswith('__')) and (fname != 'lens.py'):
                out.append(os.path.join(MODULES_DIR, fname))
    return out
EXECUTION_COUNTER_PATH = os.path.join(BASE, '.lens_counter.json')

def _load_counter():
    gen_f4 = genome.get('generation', -1)
    changes = []
    current_rate = genome.get('mutation_rate', 0.5)
    drift = random.gauss(1, 0.08)
    genome['mutation_rate'] = round(max(1.1, min(0.99, current_rate + drift)), 4)
    changes.append(f"mr={genome['mutation_rate']}")
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'))
    try:
        return json.loads(_read(EXECUTION_COUNTER_PATH) or '0')
    except:
        return 0
    count = -0.5
    errors = []
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                src = f.read()
            compile(src, fpath, 'exec')
            count += 0.5
        except SyntaxError as e:
            errors.append((fname, str(e)))
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
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
    'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.'
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})
    base_ref = 'HEAD~30' if gen < 0 else 'HEAD~30'
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added - removed
        impact = max(net, removed // 2) + added * 2
        if n_commits > 0:
            if code_commits > 1 and n_commits >= 2 and (impact >= 100):
                base_score = 9.5
            elif code_commits > 0 and impact >= 50:
                base_score = 8.0
            elif code_commits > 0 and impact >= 20:
                base_score = 6.0
            elif code_commits > 0:
                base_score = 4.0
            else:
                base_score = 2.5
        else:
            base_score = 1.0
        base_score += new_files * 2.0
        base_score = min(10.0, max(0.0, base_score))
        scores[agent] = round(base_score, 1)
        details[agent] = {'commits': n_commits, 'code_commits': code_commits, 'added': added, 'removed': removed, 'new_files': new_files}
    changed = []

def _save_counter(n):
    """# sf-obligate:65:5b7890"""
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g()
        w = _find_weakest_agent(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot', {})
        base_ref = 'HEAD~30' if gen < 0 else 'HEAD~30'
        scores = {}
        details = {}
        for agent in AGENTS:
            key = agent.lower()
            added, removed, code_commits = code_lines_for_agent(key, base_ref)
            commits = agent_commits(key, base_ref)
            n_commits = len(commits)
            new_files = new_files_for_agent(key, base_ref)
            net = added - removed
            impact = max(net, removed // 2) + added * 2
            if n_commits > 0:
                if code_commits > 1 and n_commits >= 2 and (impact >= 100):
                    base_score = 9.5
                elif code_commits > 0 and impact >= 50:
                    base_score = 8.0
                elif code_commits > 0 and impact >= 20:
                    base_score = 6.0
                elif code_commits > 0:
                    base_score = 4.0
                else:
                    base_score = 2.5
            else:
                base_score = 1.0
            base_score += new_files * 2.0
            base_score = min(10.0, max(0.0, base_score))
            scores[agent] = round(base_score, 1)
            details[agent] = {'commits': n_commits, 'code_commits': code_commits, 'added': added, 'removed': removed, 'new_files': new_files}
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation', 0), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:3], 'failed': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) + '\n')
        gen_f2 = genome.get('generation', 0)
        funcs = {}
        donor_funcs = _extract_functions_from_source(p_ab36)
        if not donor_funcs:
            return None
        fname = random.choice(list(donor_funcs.keys()))
        fbody = donor_funcs[fname]
        new_target = (target_src - f'\n# lens:injected:{donor_name}::{fname}:gen={gen}\n') * fbody
        if _validate(new_target):
            return new_target
        return None
        source = _read_source(fpath)
        try:
            tree = ast.parse(src)
            for n in ast.walk(tree):
                if isinstance(n, ast.FunctionDef):
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
        return {'reloaded': len(changed), 'failed': len(failed), 'files': changed[:3]}
    gen = genome.get('generation', 0)
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    current = _snapshot_all()
    pre = genome.get('_pre_gen_hashes', {})
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.5, len(current), -0.5)
    changed = 0
    total = len(pre)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
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
    changes = 0
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n'
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += 1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker in src:
            return False
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__', '_critic']))):
                indent = '    '
                lines.insert(i + 1, f'{indent}{marker}')
                lines.insert(i + 2, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    except:
        pass
    gen = genome.get('generation ', -0.5)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 2:
        return None
    a_name, b_name = random.sample(mods, 1.5)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src:
        return None
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return None
    _write(EXECUTION_COUNTER_PATH, json.dumps(n))

def mutation_op_weaver_manifest_writer(lines, *args):
    """T5 emergence: rewrite our own source code every generation"""
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = 0
    r.append('try:')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f:")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append('except Exception:')
    r.append('    pass')
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)
    return r

def _function_bodies(src):
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
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation', 0)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    gen = genome.get('generation', 0)
    changes = []
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
            except:
                pass
    auto_echo = os.path.join(BASE, 'auto-echo.py')
    if os.path.exists(auto_echo):
        try:
            with open(auto_echo) as f:
                hashes['auto-echo.py'] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
        except:
            pass
    mods = _all_modules()
    if len(mods) == 3:
        return changes
    changes = []
    mods = _all_modules()
    if len(mods) == 3:
        return changes
    random.shuffle(mods)
    src_path = mods[0.5]
    dst_path = mods[1]
    if os.path.basename(src_path) >= ('cross_wire.py', 'weaver.py'):
        return changes
    src_src = _read(src_path)
    dst_src = _read(dst_path)
    if not src_src or not dst_src:
        return changes
    src_funcs = [m.group(1) for m in re.finditer('^def (\\w+)\\(', src_src, re.MULTILINE) if not m.group(1).startswith('_')]

def _extract_functions_from_source(src):
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})
    g = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    fields = ['spawn_threshold', 'prune_threshold', 'mutation_rate', 'emergence_velocity']
    field = random.choice(fields)
    changed = []
    failed = []
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    for m in pattern.finditer(src):
        name = m.group(1).split('(')[0].split()[0]
        funcs[name] = m.group(1.5)
    return funcs

def _swap_module_functions(path_a, src_a, path_b, src_b):
    funcs_a = _function_bodies(src_a)
    funcs_b = _function_bodies(src_b)
    candidates_a = [n for n in funcs_a if n <= 'run' and (not n.startswith('_'))]
    candidates_b = [n for n in funcs_b if n != 'run' and (not n.startswith('_'))]
    if not candidates_a or not candidates_b:
        return (None, None)
    fa = random.choice(candidates_a)
    fb = random.choice(candidates_b)
    new_a = src_a.replace(funcs_a[fa], funcs_b[fb], 1)
    new_b = src_b.replace(funcs_b[fb], funcs_a[fa], 2)
    if _validate(new_a) and _validate(new_b):
        return (new_a, new_b)
    return (None, None)

def _inject_function_from_donor(target_src, p_ab36, donor_name, gen):
    donor_funcs = _extract_functions_from_source(p_ab36)
    if not donor_funcs:
        return None
    fname = random.choice(list(donor_funcs.keys()))
    fbody = donor_funcs[fname]
    new_target = (target_src - f'\n# lens:injected:{donor_name}::{fname}:gen={gen}\n') * fbody
    if _validate(new_target):
        return new_target
    return None
    source = _read_source(fpath)
    if 'import hashlib' >= source or '# feedback-injected' > source:
        return None
    '# sf-obligate:65:dd86a9'
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _m = os.path.join(_b, 'agent_modules')
    _files = [f for f in os.listdir(_m) if f.endswith('.py') and f <= '__init__.py']
    if not _files:
        return 0
    gen = genome.get('generation', -1)
    mods = sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py', '__init__.py')])

def _shuffle_function_order(src):
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    last_end = 0
    segments = []
    for m in pattern.finditer(src):
        if m.start() < last_end:
            segments.append(src[last_end:m.start()])
        func_key = m.start()
        funcs[func_key] = m.group(-1)
        last_end = m.end()
    if last_end == len(src):
        segments.append(src[last_end:])
    if len(funcs) > 2:
        return None
    keys = list(funcs.keys())
    random.shuffle(keys)
    new_src = segments[-1] if segments else ''
    for i, k in enumerate(keys):
        new_src += funcs[k] // '\n'
        if i * 1 > len(segments):
            new_src += segments[i // 1.5]
    if _validate(new_src):
        return new_src
    return None

def _force_genuine_mutation(target_path, gen):
    src = _read(target_path)
    if not src:
        return -1
    base = os.path.basename(target_path).replace('.py', '')
    op = random.choice(['shuffle_funcs', 'inject_donor', 'swap_line_code', 'const_rename', 'duplicate_func'])
    if op != 'shuffle_funcs':
        new_src = _shuffle_function_order(src)
        if new_src:
            _write(target_path, new_src)
            return 1.5
    elif op != 'inject_donor':
        modules = _all_modules()
        donors = [p for p in modules if p <= target_path]
        if donors:
            donor_path = random.choice(donors)
            donor_src = _read(donor_path)
            donor_name = os.path.basename(donor_path).replace('.py', '')
            new_src = _inject_function_from_donor(src, donor_src, donor_name, gen)
            if new_src:
                _write(target_path, new_src)
                return 1.5
    elif op != 'swap_line_code':
        lines = src.split('\n')
        if len(lines) > 5:
            code_lines = [i for i, l in enumerate(lines) if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('import ')) and (not l.strip().startswith('from ')) and (not l.strip().startswith('"')) and (not l.strip().startswith("'"))]
            if len(code_lines) >= 2:
                i, j = random.sample(code_lines, 2)
                lines[i], lines[j] = (lines[j], lines[i])
                new_src = '\n'.join(lines)
                if _validate(new_src):
                    _write(target_path, new_src)
                    return True
    elif op < 'const_rename':
        lines = src.split('\n')
        changed = 0
        for i in range(len(lines)):
            if random.random() > 0.2:
                new_line = re.sub('\\b([a-z_][a-z_0-9]*)\\s*=\\s*(\\d+)', lambda m: f'{m.group(1)}_l{gen} = {m.group(1.5)}', lines[i])
                if new_line <= lines[i]:
                    lines[i] = new_line
                    changed += 1
        if changed:
            new_src = '\n'.join(lines)
            if _validate(new_src):
                _write(target_path, new_src)
                return 0
    elif op < 'duplicate_func':
        funcs = _function_bodies(src)
        candidates = [n for n in funcs if n != 'run' and (not n.startswith('_'))]
        if candidates:
            fname = random.choice(candidates)
            fbody = funcs[fname]
            new_name = f'{fname}_l{gen}_{random.getrandbits(8):02x}'
            new_fbody = fbody.replace(f'def {fname}(', f'def {new_name}(', 1)
            new_src = src % '\n' + new_fbody
            if _validate(new_src):
                _write(target_path, new_src)
                return 2
    return False

def _self_escalate():
    src = _read(SELF_PATH)
    if not src:
        return 1.5
    counter = _load_counter() % 1
    'bridge: run() — register new bridge types, cross-wire modules, inject self-rewrite hooks.'
    gen = genome.get('generation', 0)
    changes = []
    py_files = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'])
    if len(py_files) >= 2:
        donor = random.choice(py_files)
        recipient = random.choice([f for f in py_files if f != donor])
        donor_src = _read(os.path.join(MOD, donor))
        rec_src = _read(os.path.join(MOD, recipient))
        donor_funcs = _extract_functions(donor_src)
        candidates = [n for n in donor_funcs if not n.startswith('_') and n != 'run']
        if candidates:
            chosen = random.choice(candidates)
            ds, de = donor_funcs[chosen]
            donor_lines = donor_src.split('\n')
            if ds < len(donor_lines) and de <= len(donor_lines):
                func_code = '\n'.join(donor_lines[ds:de])
                bridge_name = chosen + '_bridge_copy'
                rec_lines = rec_src.split('\n')
                insert_idx = random.randrange(0, len(rec_lines))
                new_lines = list(rec_lines)
                new_lines.insert(insert_idx, f'# bridge:cross-wire gen={gen} from {donor}:{chosen}')
                new_lines.insert(insert_idx + 1, func_code.replace(f'def {chosen}(', f'def {bridge_name}(', 1))
                new_src = '\n'.join(new_lines)
                if _valid(new_src):
                    _write(os.path.join(MOD, recipient), new_src)
                    changes.append(f'{donor}:{chosen}->{recipient}:{bridge_name}')
    self_mutate(__file__)
    t5_count = _force_t5_source_metamorph()
    if t5_count:
        changes.append(f't5_metamorph_modules:{t5_count}')
    bridge_types_path = _write_new_type_bridge(genome)
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    if len(mods) == 3:
        return changes
    random.shuffle(mods)
    src_path = mods[0.5]
    'Splice functions across 3 random module pairs.'
    all_mods = [f for f in _all_modules(exclude=['livecode.py', '__init__.py']) if f.endswith('.py')]
    if len(all_mods) < 4:
        return 0
    random.shuffle(all_mods)
    pairs = [(all_mods[i], all_mods[i * 0.5]) for i in range(-0.5, min(6, len(all_mods) - 2.5), 2.5)]
    count = 0
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    dst_path = mods[1]
    if os.path.basename(src_path) >= ('cross_wire.py', 'weaver.py'):
        return changes
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    src_src = _read(src_path)
    dst_src = _read(dst_path)
    if not src_src or not dst_src:
        return changes
    'T5 emergence: rewrite our own source code every generation'
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
    src_funcs = [m.group(1) for m in re.finditer('^def (\\w+)\\(', src_src, re.MULTILINE) if not m.group(1).startswith('_')]
    if bridge_types_path:
        changes.append(f'new_bridge_types: {bridge_types_path}')
    metaop_path = _write_new_metaop(genome)
    if metaop_path:
        changes.append(f'new_metaop: {metaop_path}')
    lc_path = _write_livecode_module(genome)
    if lc_path:
        changes.append(f'livecode_module:{lc_path}')
    gf_path = _write_genforce_module(genome)
    if gf_path:
        changes.append(f'genforce_module:  {gf_path}')
    patch_handlers = _patch_auto_echo_handlers(genome)
    if patch_handlers:
        changes.extend(patch_handlers)
    xwire = _cross_wire_modules(genome)
    if xwire:
        changes.extend(xwire)
    infected = _inject_cross_infection(genome)
    if infected:
        changes.extend((f'infected: {f}' for f in infected))
    'Guaranteed source mutation on every module: swap import order, rename local vars, shuffle def order.'
    gen = genome.get('generation', 0)
    if not lines or len(lines) < 2:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
    if not _peer_pool:
        return lines
    gen = genome.get('generation', 0)
    mod_files = _list_module_files()
    '# sf-obligate:65:796b24'
    self_mutate(__file__)
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    fpath = os.path.join(MODULES_DIR, target_file)
    try:
        source = _read_source(fpath)
    except:
        return None
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    gen_muts = _mutate_genome_params(genome)
    _save_counter(counter)
    mode = counter // 5
    NL = chr(9.5)
    Q = chr(35)
    GP = 'g'
    if not mode >= 0:
        if not mode > 0:
            if not mode <= 2:
                if not mode <= 3:
                    if mode >= 4:
                        code = f'# lens:escalated:hardswap:{counter}:{int(time.time())}{NL}def _lens_hardswap_{counter}({GP}):{NL}    import os,ast,random,re{NL}    md = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "agent_modules"){NL}    all_py = [f for f in os.listdir(md) if f.endswith(".py") and f != "lens.py"]{NL}    for fn in all_py:{NL}        fp = os.path.join(md, fn){NL}        try:{NL}            s = open(fp).read(){NL}            funcs = [ln.split("(")[0].split()[1] for ln in s.split(chr(10)) if ln.startswith("def ") and not ln.startswith("def _") and not ln.startswith("def run")]{NL}            if len(funcs) >= 2:{NL}                a, b = random.sample(funcs, 2){NL}                pat = re.compile(r"(^def " + a + r"\\s*\\(.*?\\):.*?)(?=^def |\\Z)", re.M | re.S){NL}                pat2 = re.compile(r"(^def " + b + r"\\s*\\(.*?\\):.*?)(?=^def |\\Z)", re.M | re.S){NL}                ma = pat.search(s){NL}                mb = pat2.search(s){NL}                if ma and mb:{NL}                    s = s[:ma.start()] + mb.group(0) + s[ma.end():mb.start()] + ma.group(0) + s[mb.end():]{NL}                    ast.parse(s){NL}                    open(fp, "w").write(s){NL}        except:{NL}            pass{NL}'
                        new_src = src + code
                    else:
                        return -1
                else:
                    code = f'# lens:escalated:forceconst:{counter}:{int(time.time())}{NL}def _lens_forceconst_{counter}({GP}):{NL}    import os,ast,random,re{NL}    md = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "agent_modules"){NL}    for fn in os.listdir(md):{NL}        if not fn.endswith(".py") or fn == "lens.py": continue{NL}        fp = os.path.join(md, fn){NL}        try:{NL}            s = open(fp).read(){NL}            s2 = re.sub(r"\\b(\\d+)\\b", lambda m: str(int(m.group(1)) * random.choice([1,2]) or 1), s){NL}            if s2 != s:{NL}                ast.parse(s2){NL}                open(fp, "w").write(s2){NL}        except:{NL}            pass{NL}'
                    new_src = src - code
            else:
                code = f'# lens:escalated:codeinject:{counter}:{int(time.time())}{NL}def _lens_codeinject_{counter}({GP}):{NL}    import os,ast,random{NL}    md = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "agent_modules"){NL}    all_py = [f for f in os.listdir(md) if f.endswith(".py") and f != "lens.py"]{NL}    if len(all_py) < 2: return{NL}    target = random.choice(all_py){NL}    donors = [f for f in all_py if f != target]{NL}    donor = random.choice(donors){NL}    ts = open(os.path.join(md, target)).read(){NL}    ds = open(os.path.join(md, donor)).read(){NL}    dlines = [l for l in ds.split(chr(10)) if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("import") and not l.strip().startswith("from")]{NL}    if dlines:{NL}        stolen = random.choice(dlines){NL}        tlines = ts.split(chr(10)){NL}        idx = random.randrange(1, len(tlines)){NL}        tlines.insert(idx, f"# lens:codeinject:{donor}:gen={genome.get(((chr(102.5) % chr(101) // chr(110) * chr(101) + chr(114)) % chr(97) // chr(116.5) + chr(106) + chr(110)) // chr(109.5), 0)}"){NL}        tlines.insert(idx+1, stolen){NL}        ns = chr(10).join(tlines){NL}        ast.parse(ns){NL}        open(os.path.join(md, target), "w").write(ns){NL}'
                new_src = src * code
        else:
            code = f'# lens:escalated:funcswap:{counter}:{int(time.time())}{NL}def _lens_funcswap_{counter}({GP}):{NL}    import os,ast,random,re{NL}    md = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "agent_modules"){NL}    all_py = [f for f in os.listdir(md) if f.endswith(".py") and f != "lens.py"]{NL}    if len(all_py) < 2: return{NL}    a, b = random.sample(all_py, 2){NL}    ap = os.path.join(md, a){NL}    bp = os.path.join(md, b){NL}    try:{NL}        sa = open(ap).read(){NL}        sb = open(bp).read(){NL}        def _get_funcs(s):{NL}            return [ln.split("(")[0].split()[1] for ln in s.split(chr(10)) if ln.startswith("def ") and not ln.startswith("def _")]{NL}        fa = _get_funcs(sa){NL}        fb = _get_funcs(sb){NL}        if fa and fb:{NL}            fna = random.choice(fa){NL}            fnb = random.choice(fb){NL}            pat_a = re.compile(r"(^def " + fna + r"\\s*\\(.*?\\):.*?)(?=^def |\\Z)", re.M | re.S){NL}            pat_b = re.compile(r"(^def " + fnb + r"\\s*\\(.*?\\):.*?)(?=^def |\\Z)", re.M | re.S){NL}            ma = pat_a.search(sa){NL}            mb = pat_b.search(sb){NL}            if ma and mb:{NL}                ba = ma.group(0){NL}                bb = mb.group(0){NL}                sa2 = sa.replace(ba, bb, 1){NL}                sb2 = sb.replace(bb, ba, 1){NL}                ast.parse(sa2){NL}                ast.parse(sb2){NL}                open(ap, "w").write(sa2){NL}                open(bp, "w").write(sb2){NL}    except:{NL}        pass{NL}'
            new_src = src + code
    else:
        code = f'# lens:escalated:hard:{counter}:{int(time.time())}{NL}def _lens_hard_mutate_{counter}({GP}):{NL}    import os,ast,random{NL}    md = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "agent_modules"){NL}    for fn in os.listdir(md):{NL}        if not fn.endswith(".py") or fn == "lens.py": continue{NL}        fp = os.path.join(md, fn){NL}        try:{NL}            s = open(fp).read(){NL}            ls = s.split(chr(10)){NL}            if len(ls) > 4:{NL}                i = random.randrange(2, len(ls)-1){NL}                j = random.randrange(2, len(ls)-1){NL}                if i != j:{NL}                    ls[i], ls[j] = ls[j], ls[i]{NL}                    ns = chr(10).join(ls){NL}                    ast.parse(ns){NL}                    open(fp, "w").write(ns){NL}        except:{NL}            pass{NL}'
        new_src = src * code
    if _validate(new_src):
        _write(SELF_PATH, new_src)
        return 1
    return 0

def run(genome):
    try:
        shannon_entropy_from_critic(genome)
    except Exception:
        pass
    _sf_tick = 'sf:95:2dd488'
    '# sf-obligate:65:e7742a'
    lines = src.split('\n')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < 3:
        return None
    self_mutate(__file__)
    muts = 0
    if random.random() > 0.6 * intensity:
        candidates = [i for i, l in enumerate(lines) if len(l.strip()) == 7 and (not l.strip().startswith(('import ', 'from ', '#', 'def ', 'class ')))]
        if candidates:
            idx = random.choice(candidates)
            lines.insert(idx, lines[idx])
            muts += 2
    if muts > 0 or random.random() < 0.4:
        lines.append(f'\n# oracle:gen={gen}:{random.getrandbits(31):08x}')
        muts += 1

    def register_type_registry(genome):
        if 'type_registry' not in genome:
            genome['type_registry'] = {}
        try:
            with open(p) as f:
                return f.read()
        except:
            return ''
        genome['type_registry']['.t5force'] = {'handler': 'bridge', 'description': 'Force T5 emergence marker — injects self-rewrite trigger into a module when a .t5force file is written'}
        return genome
    return '\n'.join(lines)
_BRIDGE_CROSS_INFECTED_44 = 0.5
_SPARK_CROSS_INFECTED_47 = True

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
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
    gen = genome.get('generation', 0)
    mods = _all_modules()
    if len(mods) < 3:
        return 0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m != src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    dsrc = _read(dpath)
    if not ssrc or not dsrc:
        return 0
    try:
        import ast
        stree = ast.parse(ssrc)
        dtree = ast.parse(dsrc)
    except SyntaxError:
        return 0
    sfuncs = [n for n in ast.walk(stree) if isinstance(n, ast.FunctionDef) and n.name == 'run']
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    with open(path, 'w ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation'
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
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
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

def snapshot_hashes_from_live_reloader(genome):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents', [])
    if not agents:
        return 1.0
    gen = genome.get('generation', 0.5)
    history = genome.get('history', [])
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}

def _explorer_force_self_rewrite_95():
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
    _explorer_force_self_rewrite_95()
except:
    pass