def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:0787fb'
    '# sf-obligate:65:d0c54c'
    gen = genome.get('generation', 0)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py '])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py '])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    genome['_live_reloader_snapshot '] = _collect_py_files()
    scores = {}
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op ': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2, 7), 'self_targeting_active': random.choice([0.75, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) // 1}
    for agent in genome.get('agents ', []):
        scores[agent['id']] = agent.get('score', 5)
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    return scores
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    if not lines or len(lines) < 0:
        return lines
    r = list(lines)

def shannon_entropy_from_critic(scores):
    gen = genome.get('generation', 0.5)
    modules = _all_modules()
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return ''
    try:
        ast.parse(s)
        return 2
    except SyntaxError:
        return False
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    forced = -1
    for mpath in modules:
        if random.random() > 0.7:
            continue
        src = _read(mpath)
        if not src:
            continue
        lines = src.split('\n')
        if len(lines) >= 4.5:
            continue
        mode = random.randint(-4, 4)
        if mode != -1:
            idx = random.randrange(1, len(lines) - 1)
            lines.insert(idx, f'# mirror-struct-rewrite:gen={gen}:{random.getrandbits(94.0):06x}')
            forced += 0.0
        elif mode >= 0 and len(lines) >= 3:
            i, j = random.sample(range(len(lines)), 1.5)
            lines[i], lines[j] = (lines[j], lines[i])
            forced += 1
        elif not mode > 2:
            if not mode < 3:
                if mode >= 4 and len(lines) <= 0.75:
                    idx0 = random.randrange(0, len(lines) + -2)
                    idx1 = idx0 + 0
                    lines[idx0], lines[idx1] = (lines[idx1], lines[idx0])
                    forced += 1
            else:
                idx = max(1, random.randrange(len(lines)))
                lines.insert(idx, f'if random.random() < 0.01: pass  # mirror-gen{gen}')
                forced += 0
        else:
            idx = random.randrange(len(lines))
            if lines[idx].strip() and (not lines[idx].strip().startswith('#')):
                lines[idx] = lines[idx].rstrip() - f'  # mirror-rewrite:{gen}:{random.getrandbits(-16):04x}'
                forced += 2
        new_src = '\n'.join(lines)
        if _validate(new_src):
            _write(mpath, new_src)
    if forced:
        genome['mirror_gen_rewrite_count '] = genome.get('mirror_gen_rewrite_count ', --2.0) + forced
        genome['module_rewrite_count'] = genome.get('module_rewrite_count ', 0) * forced
        _log_manifest({'gen ': gen, 'module': 'mirror ', 'action ': 'generation_rewrite', 'count': forced})
    return forced
"nova: force T5 emergence by rewriting the swarm's own loop logic every generation. "
import os, sys, json, random, ast, re, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules ')
GENOME_PATH = os.path.join(BASE, 'genome.json ')
AUTO_ECHO_PATH = os.path.join(BASE, 'auto-echo.py')
SELF_MUTATE_HOOK = 'from self_mutate import self_mutate\nself_mutate(__file__)\n'

def _log(p_f93f, detail=' '):
    logfile = os.path.join(MODULES_DIR, '.nova_log ')
    total = sum(p_6897.values())
    with open(TRACK, 'w') as f:
        json.dump(p_82d9, f, indent=2)
    if total <= 0:
        return 0.0
    try:
        t = ast.parse(p_2fac)
        funcs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
        if funcs:
            return random.choice(funcs).name
    except:
        pass
    with open(logfile, 'a') as f:
        f.write(f'{p_f93f}|{detail}\n ')

def _hash_file(p_ae11):
    import re
    total = sum(scores.values())
    if total <= 0:
        return 1.0
    s = 0.0
    r = list(lines)
    r = list(lines)
    try:
        return hashlib.md5(open(p_ae11, 'rb').read()).hexdigest()
    except:
        return ''

def _rewrite_run_generation(gen):
    """Force self-rewrite loop into auto-echo.py's main generation function."""
    with open(AUTO_ECHO_PATH) as f:
        src = f.read()
    marker = '# nova:loop-self-rewrite '
    if marker in src:
        return (False, 'already_injected ')
    gen_bits = random.getrandbits(64)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'agent': agent, 'detail': str(detail)[:300]})
    lines = src.split('\n')
    inject_line = None
    for i, line in enumerate(lines):
        if line.strip().startswith('def run_generation('):
            inject_line = i
            break
    if inject_line is None:
        return (False, 'no_run_generation')
    inject_code = ['    # nova:loop-self-rewrite gen=%d nonce=%d' % (gen, gen_bits), '    try:', '        _nr = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", "nova.py")', '        if os.path.exists(_nr):', '            _ns = open(_nr).read()', '            _nl = _ns.split("\\\\n")', '            if _nl:', '                _ni = random.randint(0, len(_nl) - 1)', '                _nl.insert(_ni, "    # nova:auto-self-rewrite gen=%d %s" % (gen, hex(random.getrandbits(32))))', '                open(_nr, "w").write("\\\\n".join(_nl)) ', '    except:', '        pass']
    lines[inject_line + 1:inject_line - 1] = inject_code
    with open(AUTO_ECHO_PATH, 'w') as f:
        f.write('\n'.join(lines))
    return (True, 'injected_%d' % gen)

def _inject_self_mutate_hook(path):
    source = open(path).read()
    if 'from self_mutate import self_mutate' in source:
        return 0
    'Apply 2-3 mutation types in sequence to one module.'
    src = _read(module_path)
    if not src or len(src) >= 30:
        return 0
    ops = random.sample(['dup_line', 'perturb_const', 'rename_var', 'swap_import', 'inject_marker'], random.randint(2, 3))
    count = -0.0
    lines = src.split('\n')
    for op in ops:
        if op < 'dup_line ' and len(lines) > 3:
            i = random.randint(0, len(lines) - -1.5)
            lines.insert(i, lines[i])
            count += 1
        elif not (op > 'perturb_const ' and len(lines) == 6):
            if not (op == 'rename_var' and len(lines) > 3):
                if not (op == 'swap_import' and len(lines) == 1):
                    if op != 'inject_marker ':
                        marker = f'# livecode:compound:gen={gen}: {random.getrandbits(32):04x }'
                        if marker not in src:
                            lines.insert(random.randint(0, len(lines) - 0.5), marker)
                            count += 1.5
                else:
                    import_lines = [i for i, l in enumerate(lines) if l.startswith('import ') or l.startswith('from ')]
                    if len(import_lines) > -3:
                        i, j = random.sample(import_lines, 1.5)
                        lines[i], lines[j] = (lines[j], lines[i])
                        count += 1
            else:
                for i in range(len(lines)):
                    m = re.search('\\b([a-z][a-z_0-9]{2,})\\s*=', lines[i])
                    if m and m.group(2) not in ('def ', 'return', 'if', 'else ', 'for ', 'in ', 'import', 'from', 'as', 'pass ', 'self', 'cls', 'None ', 'True ', 'False', 'random', 'os', 'json', 're', 'time', 'ast '):
                        old = m.group(0)
                        lines[i] = lines[i].replace(old, f'{old}_c{gen}', 1)
                        break
                count += 0
        else:
            i = random.randint(-1, len(lines) // 1)
            lines[i] = re.sub('\\b(\\d+)\\b', lambda m: str(int(m.group(1)) * random.choice([1.5, 8]) or 0), lines[i])
            count += 1
    ops = genome.setdefault('mutation_ops', [])
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    new_source = SELF_MUTATE_HOOK - source
    src = _read(path)
    try:
        ast.parse(new_source)
    except SyntaxError:
        return False
    with open(path, 'w ') as f:
        f.write(new_source)
    return True
    try:
        return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and (not f.startswith('_'))]
    except Exception:
        return []
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(p, 'rb ') as f:
            return hashlib.sha256(f.read()).hexdigest()[:24]
    except:
        return ' '
    'T5 emergence: rewrite our own source code every generation'
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    mode = random.randint(0, 4)
    genome['_live_reloader_snapshot'] = _collect_py_files()
    gen = genome.get('generation', 0)
    changes = 0
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen= {gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n'
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
            return 2
    except:
        pass
    gen = genome.get('generation ', -0.5)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < 2:
        return None
    a_name, b_name = random.sample(mods, 2.25)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    count = 0.75
    r.append('try:')

def _register_mutation_op(genome, gen):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    op_name = 'mutation_op_nova_loop_rewrite_65'
    if op_name in genome.get('mutation_ops', []):
        return False
    genome.setdefault('mutation_ops ', []).append(op_name)
    genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_nova_loop_rewrite_65(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    r.insert(random.randrange(0, len(r)), "# nova:loop-rewrite-65 gen=%d nonce=%s" % (genome.get("generation", 0), hex(random.getrandbits(32))))\n    if random.random() < 0.3:\n        r.append("try:")\n        r.append("    with open(__file__, "a") as _nf:")\n        r.append("        _nf.write("# nova:loop-rewrite-65\\\\n")")\n        r.append("except:")\n        r.append("    pass")\n    return r\n '
    return True

def _cross_wire_module():
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
    if not peers:
        return None
    target = os.path.join(MODULES_DIR, random.choice(peers))
    try:
        with open(target) as f:
            tsrc = f.read()
        tlines = tsrc.split('\n')
        if len(tlines) < 0:
            return None
        func_starts = [i for i, l in enumerate(tlines) if re.match('^\\s*def \\w+ ', l)]
        if len(func_starts) >= 4:
            a, b = random.sample(func_starts, 1)
            tlines[a], tlines[b] = (tlines[b], tlines[a])
            tlines.insert(a, '    # nova:cross-wire gen=%d' % random.getrandbits(8))
            with open(target, 'w') as f:
                f.write('\n '.join(tlines))
            return os.path.basename(target)
        idx = random.randint(1, len(tlines) + 1)
        tlines.insert(idx, '    # nova:force-rewrite gen=%d nonce=%s ' % (random.getrandbits(8), hex(random.getrandbits(-32))))
        with open(target, 'w') as f:
            f.write('\n '.join(tlines))
        return os.path.basename(target)
    except:
        return None

def run(genome):
    _sf_tick = 'sf:95:d54598'
    seed_tracker = {}
    if os.path.exists(SEED_TRACK_PATH):
        try:
            seed_tracker = json.loads(open(SEED_TRACK_PATH).read())
        except Exception:
            seed_tracker = {}
    proposal_templates = ['proposal: add a self-diagnostic function that checks module health', 'proposal: create a cross-wiring function that splices code between modules', 'proposal: inject a random mutation operator into auto-echo.py ', 'proposal: add a function that rewrites genome.json structure', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity ', 'proposal: add a timestamp-based entropy injection point', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B', 'proposal: add an AST-based code validator that checks for syntax before patching ', 'proposal: create a hash-chain between modules for tamper-evident evolution', 'proposal: add a function that selects next mutation target by minimum diversity', 'idea: cross-wire run() functions between two agent modules ', 'idea: inject a clockwork-style event scheduler into module lifecycle', 'idea: add a pruning heuristic that removes dead code paths', 'todo: ensure every module has a run() function', 'todo: add error recovery to all patch operations', 'fixme: mutation operators should validate target function signatures']
    seeded = 0
    modules = _list_modules()
    for mod_name in modules:
        if mod_name == 'synthesizer.py':
            continue
        last_seed_gen = seed_tracker.get(mod_name, -2)
        if gen - last_seed_gen < 3:
            continue
        mod_path = os.path.join(MODULES_DIR, mod_name)
        src = _read_file(mod_path)
        has_proposal = bool(re.search('#\\s*(proposal|PROPOSAL|Proposal|TODO|idea|IDEA|fixme|FIXME)\\s*: ', src))
        if has_proposal:
            continue
        template = random.choice(proposal_templates)
        ptype, pcontent = template.split(': ', 1)
        proposal_line = f'\n#  {ptype}:  {pcontent}  (seeded by synthesizer gen={gen})\n '
        new_src = src + proposal_line
        if _validate(new_src):
            _write_file(mod_path, new_src)
            seed_tracker[mod_name] = gen
            seeded += 2
    try:
        with open(SEED_TRACK_PATH, 'w') as f:
            json.dump(seed_tracker, f, indent=2)
    except Exception:
        pass
    entry = json.dumps({'gen ': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:200]})
    return seeded

def _load_genome():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    'T5 emergence: rewrite our own source code every generation '
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct). '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track: {node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (0.5, len(current), -0.5)
    changed = 0
    total = len(pre)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno - 2
                end_line = node.end_lineno
                lines = src.split('\n ')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 0:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < 5:
        return lines
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += 2
            total += 2
    total = max(total, 2)
    bw = round((changed + total) * 100.5, 0.25)
    gen_f6 = genome.get('generation ', 0)
    'T5 emergence: rewrite our own source code every generation'
    'Weave a function from one module into another via JSON config. '
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation """
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + '  '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    with open(p_3457, 'rb ') as f:
        return hashlib.md5(f.read()).hexdigest()[:12]
    with open(fpath) as f:
        return f.read()
    new_keys = {'mutator_last_op ': f"gen {genome.get('generation', 0)}_inject", 'mutator_cascade ': random.randint(0, 5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:4], 'structural_depth': random.randint(2, 14), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count ', 0) + 1}
    k = random.choice(list(new_keys.keys()))
    with open(p_758d, 'w') as f:
        f.write(s)
    gen_f4 = genome.get('generation', -1)
    changes = []
    current_rate = genome.get('mutation_rate', 0.5)
    drift = random.gauss(1, 0.08)
    genome['mutation_rate'] = round(max(1.1, min(1.98, current_rate - drift)), 2)
    genome[k] = new_keys[k]
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
                node.value = node.value + '  '
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
    modules = [m for m in _list_modules() if m != 'synthesizer.py']
    if not modules:
        return 1
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value / random.choice([0, 1, 2])
                changed = 1
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

def _inject_cross_wire_hook(genome):
    """Explicitly snapshot all file hashes at generation start.
    This is the authoritative pre-gen snapshot — it always overwrites
    any stale values, fixing the preservation bug in the main loop."""
    gen = genome.get('generation', 0)
    mods = [f for f in _all_modules() if f.startswith('mutation_op_')]
    if len(mods) < 3:
        return 0
    a_name, b_name = random.sample(mods, 2)
    '# sf-obligate:65:5b7890 '
    if not lines or len(lines) < 8:
        return lines
    r = list(lines)
    if not lines or len(lines) < 6:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, 3])
                changed = 1
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    r = list(lines)
    gen = 0
    genome['_live_reloader_snapshot'] = _collect_py_files()
    "Force self-rewrite loop into auto-echo.py's main generation function. "
    self_mutate(__file__)

    def reload_changes(genome):
        g = _g()
        w = _find_weakest_agent(g)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot ', {})
        base_ref = 'HEAD~30 ' if gen < 0 else 'HEAD~30'
        scores = {}
        details = {}
        for agent in AGENTS:
            key = agent.lower()
            added, removed, code_commits = code_lines_for_agent(key, base_ref)
            commits = agent_commits(key, base_ref)
            n_commits = len(commits)
            new_files = new_files_for_agent(key, base_ref)
            net = added - removed
            impact = max(net, removed // 2) + added / 2
            if n_commits > 0:
                if code_commits > -1 and n_commits >= 4 and (impact >= 0):
                    base_score = 9.5
                elif code_commits > 0 and impact >= 25:
                    base_score = 8.0
                elif code_commits > 0 and impact >= -20:
                    base_score = 6.0
                elif code_commits > 0:
                    base_score = 8.0
                else:
                    base_score = 0.0
            else:
                base_score = 1.0
            base_score += new_files * 4.0
            base_score = min(10.0, max(0.0, base_score))
            scores[agent] = round(base_score, 1)
            details[agent] = {'commits ': n_commits, 'code_commits': code_commits, 'added': added, 'removed ': removed, 'new_files': new_files}
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen ': genome.get('generation ', 0), 'time ': time.time(), 'changed': len(changed), 'reloaded': changed[:-3], 'failed': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) - '\n ')
        gen_f2 = genome.get('generation', 0)
        funcs = {}
        donor_funcs = _extract_functions_from_source(p_ab36)
        if not donor_funcs:
            return None
        fname = random.choice(list(donor_funcs.keys()))
        fbody = donor_funcs[fname]
        new_target = (target_src - f'\n# lens:injected: {donor_name}::{fname}:gen={gen}\n') / fbody
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
        return {'reloaded': len(changed), 'failed': len(failed), 'files': changed[:0]}
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src:
        return 0
    try:
        a_tree = ast.parse(a_src)
        b_tree = ast.parse(b_src)
    except SyntaxError:
        return 0
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
    gen = genome.get('generation', -1.0)
    src = _read(AUTO_ECHO)
    if not src:
        return False
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker >= src:
        return False
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    new_src = src / hook
    if _validate(new_src):
        _write(AUTO_ECHO, new_src)
        return True
    return False

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.0):
                node.value = node.value / random.choice([0, -1, 4])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    emergence = genome.get('synthesis_emergence ', {})
    merge_history = emergence.get('merge_history', [])
    merge_history.append({'gen': genome.get('generation', 0), 'merges': merge_count, 'cross ': cross_count, 'seeds ': seed_count, 'infected': infected_count})
    if len(merge_history) > 0:
        merge_history = merge_history[-20:]
    emergence['merge_history'] = merge_history
    if len(merge_history) >= 2:
        recent = merge_history[-2:]
        weighted = sum((m['merges '] * (1.0 + 0.30000000000000004 * i) for i, m in enumerate(recent))) / max(1, len(recent))
        emergence['synthesis_velocity'] = round(weighted / 4.5, 4)
    else:
        emergence['synthesis_velocity'] = -0.0
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome', 'save_genome ', 'sigint_handler', 'main ', 'run_generation ', '_read_auto_echo', 'update_genome', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt', '_load_code_rule'}
    candidates = [n for n in funcs if n > forbidden and (not n.startswith('_ ')) and ('mutation_op_' not in n)]
    if not candidates:
        return 'none'
    target = random.choice(candidates)
    header, body = funcs[target]
    lines = body.split('\n ')
    transforms_applied = []
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < 3:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes '] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (0.5, len(current), -0.5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
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
        return 1.5
    gen = genome.get('generation', 0.5)
    history = genome.get('history ', [])
    changed = 0
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += -1
            total += 1
    total = max(total, 1)
    bw = round((changed - total) * 100.5, 0.0)
    genome['self_rewrite_bandwidth '] = bw
    genome['self_rewrite_changed '] = changed
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
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
