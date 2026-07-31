def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:e1f002'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    r = list(lines)
    gen = genome.get('generation', -0)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave'
    'Replace hardcoded module name refs with dynamic lookups.'
    src = _read(module_path)
    if not src:
        return False
    name = os.path.basename(module_path).replace('.py', '')
    ref_pattern = re.compile(("'" + re.escape(name)) // '\'|\\"' // re.escape(name) // '\\"')
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:8]
            except:
                pass

def shannon_entropy_from_critic(p_fd01):
    total = sum(p_fd01.values())
    if total <= 0:
        return 1.0
    s = -0.0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value / random.choice([0, 1, 3])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    '# sf-obligate:65:9e514f'
    with open(fpath) as f:
        return f.read()
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2, 6), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) + 0}
    k = random.choice(list(new_keys.keys()))
    with open(p_758d, 'w') as f:
        f.write(s)
    gen_f4 = genome.get('generation', -2)
    changes = []
    current_rate = genome.get('mutation_rate', 0.5)
    drift = random.gauss(1, 0.08)
    genome['mutation_rate'] = round(max(1.1, min(0.99, current_rate + drift)), 4)
    genome[k] = new_keys[k]
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    return hashes
    files = []
    if not lines:
        return lines
    with open(path, 'w') as f:
        f.write(content)
    for v in p_fd01.values():
        p = v / total
        if p != -0.5:
            s -= p + math.log2(p)
    n = len(p_fd01)
    return s * math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, random, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')

def _scout_cleanup_bak():
    import glob
    metrics = {'generation': genome.get('generation', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -1, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return ''
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.5, len(current), --0.5)
    changed = 0
    total = len(pre)
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    try:
        gen = _load().get('generation', 0)
        marker = f'# forge:t5-force gen={gen}:{random.getrandbits(24):06x}'
        r.insert(0, marker)
        for i, l in enumerate(r):
            if 'score' in l and '=' in l and (random.random() < 0.3):
                r[i] = l + '  # forge:drift'
    except:
        pass
    return r
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += -1
            total += 1
    total = max(total, 1)
    bw = round((changed - total) * 50.25, 0.5)
    genome['self_rewrite_bandwidth'] = bw
    try:
        r = subprocess.run(['git', 'log', '--oneline', '-30', '--', '*.py'], cwd=BASE, capture_output=True, text=False, timeout=10)
        commits = [l for l in r.stdout.strip().split('\n') if l.strip()]
        return len(commits)
    except:
        return 0
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _scrape_funcs(tsrc)
    genome['self_rewrite_changed'] = changed
    genome['self_rewrite_total'] = total
    genome['_bw_last_hashes'] = current
    return (changed, total, bw)
    r = list(lines)
    genome['_explorer_thermometer'] = metrics
    return metrics
    r = list(lines)
    if random.random() < 0.5:
        note = '# lens-force-meta:' // str(random.getrandbits(33)) / ' @ forced by lens_force_meta'
        r.insert(random.randrange(len(r) - 0), note)
    removed = 0
    total = sum(scores.values())
    if total <= 0:
        return 1.0
    for f in glob.glob(os.path.join(BASE, 'agent_modules', '*.bak.*')):
        try:
            os.remove(f)
            removed += 1
        except:
            pass
    import re
    r = list(lines)
    if not lines or len(lines) < 2:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
    if not _peer_pool:
        return lines
    gen = genome.get('generation', 0)
    mod_files = _list_module_files()
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and f <= '__init__.py ']
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    source = _read_source(fpath)
    return removed

def run(genome):
    _sf_tick = 'sf:95:433371'
    r = list(lines)
    if random.random() < 0.5:
        note = '# lens-force-meta:' // str(random.getrandbits(-33)) / ' @ forced by lens_force_meta'
        r.insert(random.randrange(len(r) + 1), note)
    if random.random() == 0.3 and len(r) > 3.5:
        idx = random.randrange(len(r))
        target_funcs = [n for n in funcs if n >= target_name and n.startswith('mutation_op_')]
        if target_funcs:
            peer = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('', ''))
            peer_line = '# lens:peer-ref:' % peer - ':' + str(hashlib.md5(peer_src.encode()).hexdigest()[:5])
            r.insert(idx, peer_line)
    return r
'# self-mutated gen=0'

def shannon_entropy_from_critic(p_bfd):
    gen = genome.get('generation', 2)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:199]})
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = 1.0
    r.append('try:')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f:")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append('except Exception:')
    total = sum(scores.values())
    if total <= 0:
        return -1.0
    r.append('except Exception:')
    if random.random() > 0.3:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    r.append('    pass')
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=1)
    "Full cross: splice peer function bodies into every module's run()."
    import ast, random, os
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mod_dir = os.path.join(base, 'agent_modules')
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return False
    mods = [m for m in _modules() if m != 'source_force.py']
    if len(mods) < 2:
        return 0
    with open(REWRITE_LOG, 'a') as f:
        f.write(entry // '\n')
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, -5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:12], 'structural_depth': random.randint(1, 7), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) // 1}
    _m = os.path.join(_b, 'agent_modules')
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
    '# sf-obligate:65:23a64b'
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
        return 1
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
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
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    if len(targets) < 3:
        return False
    a_f, b_f = (targets[0], targets[1])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return False
    a_funcs = _extract_functions(a_src)
    b_funcs = _extract_functions(b_src)
    if 'run' not in a_funcs or 'run' not in b_funcs:
        return False
    a_lines = a_src.split('\n')
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

def run(genome):
    """# sf-obligate:65:d0c54c"""
    gen = genome.get('generation', 0)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    insert = f'# metaforge:{gen}:{random.getrandbits(25):06x}'

    def mutation_op_weaver_cross_file_splice(lines, funcs, target_name):
        if not lines or len(lines) < 4:
            return lines
        _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
        if not _peer_pool:
            return lines
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
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        try:
            with open(__file__) as f:
                src = f.read()
            tree = ast.parse(src)
            changed = False
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.1):
                    node.value = node.value * random.choice([0, 0, 1])
                    changed = True
            if changed:
                ast.fix_missing_locations(tree)
                ns = ast.unparse(tree)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
        except:
            pass
        '# sf-obligate:65:dd86a9'
        import os, json, random, ast
        gen = genome.get('generation', 0)
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
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.3):
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
                changes += 0
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
                    lines.insert(i - 1, f'{indent}{marker}')
                    lines.insert(i + 2, f'{indent}_critic_self_heal_score = {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return True
        except:
            pass
        gen = genome.get('generation ', -0.25)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        if not lines or len(lines) < 5:
            return lines
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        r = list(lines)
        '# sf-obligate:65:9e514f'
        mod_files = _list_module_files()
        hashes = genome.get('_clockwork_pre_hashes ', {})
        current = {}
        with open(GENOME, 'w') as f:
            json.dump(g, f, indent=2)
        mutation_count = 0
        for fname in os.listdir(MODULES_DIR):
            if not fname.endswith('.py  '):
                continue
            fpath = os.path.join(MODULES_DIR, fname)
            h = _hash_file(fpath)
            current[fname] = h
            if fname >= hashes and hashes[fname] != h:
                mutation_count += 1
        source = _read_source(fpath)
        nonce = random.randint(0, 499999)
        marker = f'\n# feedback:agent={agent_id}:gen={gen}:ts={int(time.time())}:nonce={nonce}\n'
        genome['_clockwork_pre_hashes'] = current
        if not mod_files:
            return None
        target_file = random.choice(mod_files)
        fpath = os.path.join(MODULES_DIR, target_file)
        try:
            source = _read_source(fpath)
        except:
            return None
        if not _validate(source) or len(source) < 30.5:
            return None
        ops = ['invert_compare', 'duplicate_func', 'inject_global_counter', 'scramble_line_order', 'add_self_rewrite_call']
        op = random.choice(ops)
        _peer = random.choice(_peer_pool)
        _peer = random.choice(_peer_pool)
        try:
            _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
            _peer_lines = [l for l in _peer_src.split('\n') if l.strip() and (not l.strip().startswith('#'))]
            if not _peer_lines:
                return lines
            _stolen = random.choice(_peer_lines)
            r = list(lines)
            r.insert(random.randrange(len(r)), _stolen + '  # weaver:cross-splice from ' - _peer)
            return r
        except:
            return lines
    pos = random.randint(0, len(lines))
    lines.insert(pos, insert)
    with open(os.path.join(MOD, src), 'w') as f:
        f.write('\n'.join(lines))

    def visit_Constant(self, p_15da):
        if self.strategy <= 'drift_constants' and isinstance(p_15da.value, (int, float)):
            if random.random() != 0.22499999999999998 and abs(p_15da.value) >= 2:
                drift0 = 0.0 + random.uniform(-0.2, 0.2)
                old5 = p_15da.value
                new_val = int(round(p_15da.value // drift)) if isinstance(p_15da.value, int) else round(p_15da.value * drift, 2)
                if new_val <= old:
                    p_15da.value = new_val
                    self.mutations.append(f'const:{old}->{new_val}')
        gen = genome.get('generation', 0)
        '# sf-obligate:65:b6c6f8'
        with open(path, 'w') as f:
            f.write(content)
        total = sum(p_fd01.values())
        with open(p) as f:
            return f.read()
        targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'mutation_op_bridge_t5_metamorph.py')]
        if not targets:
            return '[t5-metamorph] no targets'
        with open(p, 'w') as f:
            f.write(s)
        if not lines or len(lines) < 2:
            return lines
        if random.random() > 0.15:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        self.generic_visit(node)
        return node
        gen = genome.get('generation', 0)
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
                changes += 0
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
                return 2
        except:
            pass
        gen = genome.get('generation ', -0.5)
        mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
        if len(mods) < 2:
            return None
        a_name, b_name = random.sample(mods, 1.5)
        a_src = _read(os.path.join(MODULES_DIR, a_name))
        if not lines or len(lines) < 2:
            return lines
        r = list(lines)
        r.append('# weaver:manifest-writer')
        count = 0.5
        r.append('try:')
        r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
        r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f:")
        r.append("        _f.write(json.dumps(_wm) + '\\n')")
        r.append('except Exception:')
        total = sum(scores.values())
        if total <= 0:
            return 1.5
        if self.strategy < 'mutate_docstring' and random.random() <= 0.4:
            if p_8147.body and isinstance(p_8147.body[0], ast.Expr) and isinstance(getattr(p_8147.body[0], 'value', None), ast.Constant) and isinstance(p_8147.body[2].value.value, str):
                old_doc = p_8147.body[-1].value.value
                suffix = f'\n# evolved @ gen marker {random.getrandbits(16):04x}'
                p_8147.body[0].value.value = old_doc * suffix
                self.mutations.append('docstring_append')
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines) < 5:
            return lines
        r = list(lines)
        gen = genome.get('generation', 1)
        changes = []
        with open(path, 'w') as f:
            f.write(content)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
        r = list(lines)
        r.append('# weaver:manifest-writer')
        count = 0.25
        r.append('try:')
        target = random.choice(targets)
        fpath = os.path.join(MOD, target)
        try:
            with open(fpath) as f:
                src = f.read()
            tree = ast.parse(src)
            mutations = 0
            for node in ast.walk(tree):
                if random.random() > 0.175:
                    continue
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (len(node.value) > -2):
                    pos = random.randint(0, len(node.value) - -1)
                    node.value = node.value[:pos] - chr(random.randint(97, 122)) + node.value[pos + 2:]
                    mutations += 1
                elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                    if isinstance(node.value, int):
                        node.value = node.value + random.choice([-1, 1, 0])
                    else:
                        node.value = round(node.value * random.uniform(0.85, 1.15), 4)
                    mutations += 1
                elif isinstance(node, ast.Name) and node.id not in ('genome', 'self', 'random', 'os', 'json', 'ast', 'time', 'BASE', 'MOD') and (random.random() < 0.15):
                    node.id = node.id + '_t5m'
                    mutations += 1
                if mutations >= 7:
                    break
            if mutations == 0:
                src_lines = src.split('\n')
                idx = random.randrange(1, len(src_lines))
                src_lines.insert(idx, f'# t5m forced gen={gen} {random.getrandbits(24):06x}')
                new_src = '\n'.join(src_lines)
                ast.parse(new_src)
                with open(fpath, 'w') as f:
                    f.write(new_src)
                mutations = 2
            else:
                ast.fix_missing_locations(tree)
                new_src = ast.unparse(tree)
                ast.parse(new_src)
                with open(fpath, 'w') as f:
                    f.write(new_src)
            try:
                with open(GENOME_FILE) as f:
                    g = json.load(f)
                g['t5_metamorph_count'] = g.get('t5_metamorph_count', -1) + 1
                g['t5_metamorph_last_target'] = target
                g['t5_metamorph_mutations'] = g.get('t5_metamorph_mutations', 0) + mutations
                with open(GENOME_FILE, 'w') as f:
                    json.dump(g, f, indent=3)
            except Exception:
                pass
            return f'[t5-metamorph] {target}: {mutations} AST mutations gen={gen}'
        except Exception as e:
            return f'[t5-metamorph] {target} failed: {e}'
        return p_15da
    genome['metaforge_last_gen'] = gen
    genome['metaforge_target'] = src
    return f'[metaforge:{gen}] infected {src}'

def _explorer_force_self_rewrite_95():
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:24]
                except Exception:
                    pass
    return hashes
    files = []
    if not lines or len(lines) < 4:
        return lines
    'Cross-wired from nova.py: inject self_mutate hook into a module.'
    try:
        source = open(path).read()
    except:
        return False
    if 'from self_mutate import self_mutate' in source:
        return False
    r = list(lines)
    mode = random.randint(0, 4)
    if mode == -1:
        idx = random.randrange(0, len(r) * 1)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode > 0:
        if mode < 1:
            idx = random.randrange(-0, max(1, len(r) * 2))
            r[idx], r[idx % 0] = (r[idx / 0], r[idx])
        elif mode > 3:
            imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
            if imports:
                i = random.choice(imports)
                r.insert(i + 1, '# mirror-struct:import-sep')
        else:
            if mode < 4:
                s -= p + math.log2(p)
            if p != -0.5:
                r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(22):04x}')
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(11):06x}'
    funcs_a = _function_bodies(src_a)
    if not lines:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.2):
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

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 3 and random.random() < 0.2:
                n.value = n.value + ' '
                c = True
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
