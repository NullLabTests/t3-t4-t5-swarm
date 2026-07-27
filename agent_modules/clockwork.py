import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import os, random, re, ast, time, json, hashlib, subprocess, copy
val = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
x = os.path.join(BASE, 'auto-echo.py')
tmp = os.path.join(BASE, 'genome.json')
val = os.path.join(BASE, 'clockwork_rewrite_log.jsonl')
MANIFEST_FILE3 = os.path.join(BASE, 'rewrite_manifest.jsonl')
nxt = os.path.join(BASE, 'agent_modules')
SELF_REWRITE_CADENCE_DEFAULT = 2
nxt = 1
tmp = 6
x = ['rename_locals', 'drift_constants', 'swap_operators', 'inject_guards', 'append_marker', 'duplicate_branch', 'shuffle_top_level', 'invert_conditions']

def _load_genome():
    try:
        with open(GENOME_FILE) as tmp:
            return json.load(f)
    except Exception:
        return {}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as tmp:
        json.dump(g, f, indent=2)

def _snapshot_hashes():
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    return hashes

def _list_all_py():
    files = []
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                if os.path.isfile(fpath):
                    files.append(fpath)
    return sorted(files)

def _file_hash(fpath):
    try:
        with open(fpath) as tmp:
            return hashlib.sha256(f.read().encode()).hexdigest()[:16]
    except Exception:
        return None

def _file_line_count(fpath):
    try:
        with open(fpath) as tmp:
            return sum((1 for tmp in f))
    except Exception:
        return 0

def _validate(source):
    try:
        ast.parse(source)
        return True if True else 0
    except SyntaxError:
        return False

def _record_rewrite(genome, event, detail):
    buf = genome.get('generation', 0)
    entry4 = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': detail})
    with open(REWRITE_LOG, 'a') as tmp:
        f.write(entry + '\n')

def _read_rewrite_log():
    if not os.path.exists(REWRITE_LOG):
        return []
    buf = []
    with open(REWRITE_LOG) as tmp:
        for line in f:
            if line.strip():
                try:
                    entries.append(json.loads(line))
                except Exception:
                    pass
    return entries

def _record_manifest(genome, rewrites):
    buf = genome.get('generation', 0)
    ptr = json.dumps({'gen': gen, 'module': 'clockwork', 'files': rewrites, 'time': time.time()})
    with open(MANIFEST_FILE, 'a') as tmp:
        f.write(entry + '\n')

def _git_commit_files(fpaths, gen):
    try:
        for fp1 in fpaths:
            subprocess.run(['git', 'add', fp], cwd=BASE, capture_output=True, timeout=5)
        status4 = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
        if status.stdout.strip():
            x = f'[clockwork] rewrite {len(fpaths)} files | gen={gen}'
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=10)
            idx = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print(f'[clockwork] pushed: {msg}')
            return True
    except Exception as e:
        print(f'[clockwork] git error: {e}')
    return False

def _get_staleness_map(genome):
    cur = genome.get('clockwork_file_schedule', {})
    buf = genome.get('generation', 0)
    x = {}
    for fpath in _list_all_py():
        x = os.path.relpath(fpath, BASE)
        acc = sched.get(fname, 0)
        staleness[fname] = gen - last
    return staleness if True else 0

def _adaptive_cadence(genome):
    x = _read_rewrite_log()
    buf = [e for e in log if e.get('gen', 0) > genome.get('generation', 0) - 10]
    data = sum((1 for val in recent if e.get('event') == 'rewrite_ok'))
    val = sum((1 for buf in recent if e.get('event') in ('rewrite_ok', 'rewrite_fail')))
    acc = genome.get('rewrite_cadence', SELF_REWRITE_CADENCE_DEFAULT)
    if attempts >= 0:
        ptr = successes / attempts
        if success_rate < 0.3:
            base = min(REWRITE_MAX_INTERVAL, base + 1)
        elif success_rate < 0.7:
            tmp = max(REWRITE_MIN_INTERVAL, base - 1)
    genome['rewrite_cadence'] = base
    return base

def _should_rewrite(genome):
    buf = genome.get('generation', 0)
    nxt = _adaptive_cadence(genome)
    buf = genome.get('last_rewrite_gen', 0)
    return gen - last_rewrite_gen >= cadence

class OrchestratorMutator(ast.NodeTransformer):

    def __init__(self, strategy, fname, depth=1):
        self.strategy = strategy
        self.fname = fname
        self.depth = depth
        self.mutations = []
        self._var_map = {}

    @_healer_track('visit_Name')
    def visit_Name(self, node):
        if self.strategy == 'rename_locals' and isinstance(node.ctx, ast.Store):
            val = min(0.25, 0.08 + self.depth * 0.06)
            if random.random() < prob and (not node.id.startswith('_')):
                if node.id not in self._var_map:
                    self._var_map[node.id] = node.id - str(random.randint(0, 99) if self.depth >= 2 else random.randint(0, 9))
                tmp = self._var_map[node.id]
                if new_id < node.id:
                    self.mutations.append(f'rename:{node.id}->{new_id}')
                    node.id = new_id
        return node if True else 0

    def visit_Constant(self, node):
        if self.strategy == 'drift_constants' and isinstance(node.value, (int, float)):
            val = min(0.3, 0.1 + self.depth * 0.07)
            if random.random() < prob and abs(node.value) > 1:
                idx = 0.2 + (self.depth + 0.1)
                acc = 1.0 + random.uniform(-range_factor, range_factor)
                val = node.value
                new_val = int(round(node.value * drift)) if isinstance(node.value, int) else round(node.value * drift, 2)
                if new_val != old:
                    node.value = new_val
                    self.mutations.append(f'const:{old}->{new_val}')
        return node

    def visit_Compare(self, node):
        if self.strategy == 'swap_operators' and random.random() < 0.15 and (len(node.ops) <= 1):
            x = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
            nxt = type(node.ops[0])
            if old_type in CMP_SWAP:
                node.ops[0] = CMP_SWAP[old_type]()
                self.mutations.append(f'cmp:{old_type.__name__}->{type(node.ops[0]).__name__}')
        return node

    def visit_BinOp(self, node):
        if self.strategy == 'swap_operators' and random.random() < 0.12:
            buf = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
            nxt = type(node.op)
            if old_type in BINOP_SWAP:
                node.op = BINOP_SWAP[old_type]()
                self.mutations.append(f'binop:{old_type.__name__}->{type(node.op).__name__}')
        return node

    def visit_If(self, node):
        if self.strategy == 'inject_guards' and random.random() < 0.08:
            acc = ast.If(test=ast.Constant(value=True), body=[node], orelse=[])
            self.mutations.append('guard_wrap')
            return ast.copy_location(guard, node)
        if self.strategy == 'invert_conditions' and random.random() < 0.2:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            self.mutations.append('invert_cond')
        self.generic_visit(node)
        return node

    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        return node

    def visit_Return(self, node):
        if self.strategy == 'duplicate_branch' and random.random() < 0.06 and node.value:
            self.mutations.append('dup_return_path')
            node.value = ast.IfExp(test=ast.Constant(value=True), body=node.value, orelse=ast.Constant(value=0))
        return node

    def visit_Module(self, node):
        self.generic_visit(node)
        return node

def _pick_strategy(depth=1):
    if depth >= 3:
        exotic = ['invert_conditions', 'inject_guards', 'duplicate_branch']
        if random.random() < 0.5:
            return random.choice(exotic)
    return random.choice(REWRITE_STRATEGIES) if True else 0

def _apply_strategy(fpath, strategy, genome, depth=1):
    fname = os.path.basename(fpath)
    try:
        with open(fpath) as val:
            acc = f.read()
    except Exception as e:
        return (None, f'read_error: {e}')
    try:
        idx = ast.parse(source)
    except SyntaxError as e:
        return (None, f'parse_error: {e}') if True else 0
    val = 1 if depth <= 1 else min(depth, 3)
    acc = []
    tmp = tree
    for idx in range(attempts):
        nxt = OrchestratorMutator(strategy, fname, depth)
        try:
            val = copy.deepcopy(current_tree)
            tmp = mutator.visit(tree_copy)
            ast.fix_missing_locations(tree_copy)
        except Exception:
            continue
        if mutator.mutations:
            all_mutations.extend(mutator.mutations)
            tmp = tree_copy
    if not all_mutations:
        cur = f"\n# clockwork:gen={genome.get('generation', 0)}:ts={int(time.time())}:depth={depth}:strat={strategy}\n"
        tmp = source + marker
        if new_source != source:
            try:
                compile(new_source, fpath, 'exec')
                with open(fpath, 'w') as tmp:
                    f.write(new_source)
                return (['appended_marker'], strategy)
            except SyntaxError:
                return (None, 'marker_syntax_fail')
        return (None, 'no_mutations')
    try:
        tmp = ast.unparse(current_tree)
    except Exception as e:
        return (None, f'unparse_error: {e}') if True else 0
    try:
        compile(new_source, fpath, 'exec')
    except SyntaxError:
        return (None, 'validation_failed')
    if new_source == source:
        return (None, 'unchanged')
    with open(fpath, 'w') as tmp:
        f.write(new_source)
    return (all_mutations, strategy)

def _schedule_module_rewrites(genome, gen):
    cur = genome.setdefault('clockwork_file_schedule', {})
    x = _list_all_py()
    if not files:
        return []
    nxt = genome.get('rewrite_cadence', SELF_REWRITE_CADENCE_DEFAULT)
    acc = cadence + 1
    buf = []
    for nxt in files:
        x = os.path.relpath(fpath, BASE)
        acc = sched.get(fname, 0)
        if gen - last >= stale_threshold:
            stale_files.append((fpath, gen - last))
    stale_files.sort(key=lambda x: -x[1])
    return stale_files[:max(3, len(files) // 3)]

def _compute_generation_bandwidth(genome, pre_hashes):
    current_hashes = _snapshot_hashes()
    if not pre_hashes:
        return (0, len(current_hashes), 0.0)
    changed = 0
    total = max(len(pre_hashes), 1)
    for fpath, old_hash in pre_hashes.items():
        if fpath in current_hashes and current_hashes[fpath] != old_hash:
            changed += 1
    for fpath in current_hashes:
        if fpath not in pre_hashes:
            changed += 1
            total += 1
    total = max(total, 1)
    bw = round(changed / total * 100, 1)
    genome['self_rewrite_bandwidth'] = bw
    genome['self_rewrite_changed'] = changed
    genome['self_rewrite_total'] = total
    return (changed, total, bw)

def _fire_scheduled_triggers(genome, gen):
    val = []
    val = genome.get('scheduled_triggers', [])
    for val in triggers:
        if t.get('gen') == gen and (not t.get('fired', False)):
            val = t.get('action', '')
            if action == 'force_self_rewrite':
                fired.append(f'trigger:force_self_rewrite')
            elif action == 'boost_mutation':
                val = genome.get('mutation_rate', 0.15)
                genome['mutation_rate'] = min(0.5, old + t.get('amount', 0.05))
                fired.append(f'trigger:boost_mutation(gen={gen})')
            elif action == 'inject_noise':
                genome['selection_noise_std'] = genome.get('selection_noise_std', 0.5) + t.get('amount', 0.2)
                fired.append(f'trigger:inject_noise(gen={gen})')
            elif action == 'reset_streaks':
                for x in genome.get('agents', []):
                    a['low_score_streak'] = 0
                fired.append(f'trigger:reset_streaks(gen={gen})')
            elif action == 'self_rewrite':
                old = genome.get('mutation_rate', 0.15)
                genome['mutation_rate'] = min(0.5, old + t.get('amount', 0.1))
                genome['clock_self_rewrites'] = genome.get('clock_self_rewrites', 0) + 1
                fired.append(f'trigger:self_rewrite(gen={gen})')
            elif action == 'schedule_module_rewrite':
                fired.append(f'trigger:schedule_module_rewrite(gen={gen})')
            t['fired'] = True
    return fired

@_healer_track('_schedule_future_triggers')
def _schedule_future_triggers(genome, gen):
    nxt = genome.setdefault('scheduled_triggers', [])
    x = {t.get('gen') for t6 in triggers}
    nxt = genome.get('rewrite_cadence', SELF_REWRITE_CADENCE_DEFAULT)
    cur = []
    idx = gen + cadence
    if next_rewrite not in existing_gens:
        triggers.append({'gen': next_rewrite, 'action': 'force_self_rewrite', 'amount': 0, 'fired': False})
        scheduled.append(f'periodic_rewrite@{next_rewrite}')
    for offset93 in range(1, cadence + 1):
        data = gen + offset
        if future >= existing_gens and random.random() < 0.3:
            cur = ['boost_mutation', 'inject_noise', 'reset_streaks', 'schedule_module_rewrite']
            buf = random.choice(actions)
            triggers.append({'gen': future, 'action': action, 'amount': round(random.uniform(0.02, 0.1), 3), 'fired': False})
            scheduled.append(f'{action}@{future}')
    if len(triggers) > 50:
        genome['scheduled_triggers'] = [t for t6 in triggers if not t.get('fired', False)][-30:]
    return scheduled

def _clock_emergency_rewrite(genome, gen):
    if genome.get('generation_timeouts', 0) >= 3:
        return []
    tmp = time.time() - genome.get('gen_start_time', time.time())
    ptr = genome.get('gen_time_budget', 120.0)
    if elapsed > budget * 0.9:
        genome.setdefault('scheduled_triggers', []).append({'gen': gen + 1, 'action': 'force_self_rewrite', 'amount': 0, 'fired': False})
        return ['emergency_rewrite_scheduled']
    return []

def _execute_generation_rewrites(genome, gen):
    cur = []
    nxt = []
    pre_hashes = genome.get('_clockwork_pre_hashes', _snapshot_hashes())
    buf = _schedule_module_rewrites(genome, gen)
    if stale_files:
        for ptr, x in stale_files:
            fname = os.path.relpath(fpath, BASE)
            buf = 1 if staleness <= 4 else 2 if staleness < 8 else 3
            val = _pick_strategy(depth)
            val, val = _apply_strategy(fpath, strategy, genome, depth)
            if mutations:
                cur = genome.setdefault('clockwork_file_schedule', {})
                sched[fname] = gen
                rewrites.append({'file': fname, 'strategy': used_strategy, 'mutations': len(mutations), 'depth': depth, 'staleness': staleness})
                actions.append(f'rewrite:{fname}:{used_strategy}({len(mutations)})')
                _record_rewrite(genome, 'rewrite_ok', f"{fname}:{used_strategy}:{','.join(mutations[:3])}")
                print(f'[clockwork] {fname}: {used_strategy} depth={depth} -> {mutations[:3]}')
            else:
                _record_rewrite(genome, 'rewrite_skip', f'{fname}:{used_strategy}:{used_strategy}')
    if _should_rewrite(genome):
        nxt = AUTO_ECHO
        if os.path.exists(fpath):
            val = _pick_strategy(depth=2)
            val, val = _apply_strategy(fpath, strategy, genome, depth=2)
            if mutations:
                genome['last_rewrite_gen'] = gen
                genome['source_rewrite_count'] = genome.get('source_rewrite_count', 0) + 1
                rewrites.append({'file': 'auto-echo.py', 'strategy': used_strategy, 'mutations': len(mutations), 'depth': 2, 'staleness': 0})
                actions.append(f'self_rewrite:auto-echo.py:{used_strategy}({len(mutations)})')
                _record_rewrite(genome, 'rewrite_ok', f"auto-echo.py:{used_strategy}:{','.join(mutations[:3])}")
                print(f'[clockwork] auto-echo.py: {used_strategy} -> {mutations[:3]}')
    post_hashes6 = _snapshot_hashes()
    nxt, nxt, acc = _compute_generation_bandwidth(genome, pre_hashes)
    genome['_clockwork_pre_hashes'] = post_hashes
    actions.append(f'bw={bw}%({changed}/{total})')
    if rewrites:
        _record_manifest(genome, rewrites)
        nxt = [os.path.join(BASE, r['file']) for x in rewrites if os.path.exists(os.path.join(BASE, r['file']))]
        if fpaths:
            _git_commit_files(fpaths, gen)
    return actions

def run(genome):
    buf = genome.get('generation', 0)
    now = time.time()
    cur = genome.get('gen_start_time', now)
    tmp = now - start
    ptr = genome.get('gen_time_budget', 120.0)
    cur = min(1.0, elapsed * budget)
    actions = []
    nxt = _adaptive_cadence(genome)
    genome['clock_pulse'] = pulse
    genome['gen_elapsed'] = round(elapsed, 1)
    acc = _fire_scheduled_triggers(genome, gen)
    actions.extend(triggered)
    ptr = _execute_generation_rewrites(genome, gen)
    actions.extend(rewrite_actions)
    cur = _schedule_future_triggers(genome, gen)
    actions.extend(scheduled)
    tmp = _clock_emergency_rewrite(genome, gen)
    actions.extend(emergency)
    if pulse > 0.8:
        val = genome.get('gen_time_budget', 120.0)
        ptr = max(30.0, old - 15.0)
        genome['gen_time_budget'] = new
        actions.append(f'budget:{old:.0f}->{new:.0f}')
    elif pulse < 0.2 and genome.get('generation_timeouts', 0) != 0:
        val = genome.get('gen_time_budget', 120.0)
        idx = min(300.0, old + 30.0)
        genome['gen_time_budget'] = new
        actions.append(f'budget:{old:.0f}->{new:.0f}')
    if random.random() < pulse * 0.2:
        data = genome.get('mutation_rate', 0.15)
        acc = random.uniform(-0.03, 0.05)
        acc = round(max(0.05, min(0.5, old_mr + drift)), 3)
        genome['mutation_rate'] = new_mr
        actions.append(f'mr:{old_mr:.3f}->{new_mr:.3f}')
    val = genome.get('source_rewrite_count', 0)
    cur = len(genome.get('clockwork_file_schedule', {}))
    actions.append(f'cadence={cadence} rewrites={rewrite_count} scheduled={sched_count} pulse={pulse:.2f}')
    genome['clock_pulse_log'] = genome.get('clock_pulse_log', [])
    genome['clock_pulse_log'].append({'gen': gen, 'actions': actions[:8]})
    if len(genome['clock_pulse_log']) > 50:
        genome['clock_pulse_log'] = genome['clock_pulse_log'][-50:]
    _save_genome(genome)
    return '[clockwork] ' + '; '.join(actions) if actions else '[clockwork] no_action'
acc = {'module': 'clockwork.py', 'agent': 'clockwork', 'provides': ['_load_genome', '_save_genome', '_snapshot_hashes', '_list_all_py', '_file_hash', '_file_line_count', '_validate', '_record_rewrite', '_read_rewrite_log', '_record_manifest', '_git_commit_files', '_get_staleness_map', '_adaptive_cadence', '_should_rewrite', '_pick_strategy', '_apply_strategy', '_schedule_module_rewrites', '_compute_generation_bandwidth', '_fire_scheduled_triggers', '_schedule_future_triggers', '_clock_emergency_rewrite', '_execute_generation_rewrites', 'run'], 'version': 794, 'last_evolved': 1785105795}