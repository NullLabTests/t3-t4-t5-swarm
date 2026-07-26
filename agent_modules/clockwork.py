import os, random, re, ast, time, json, hashlib, subprocess, copy

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
GENOME_FILE = os.path.join(BASE, 'genome.json')
REWRITE_LOG = os.path.join(BASE, 'clockwork_rewrite_log.jsonl')
MANIFEST_FILE = os.path.join(BASE, 'rewrite_manifest.jsonl')
MODULES_DIR = os.path.join(BASE, 'agent_modules')

SELF_REWRITE_CADENCE_DEFAULT = 2
REWRITE_MIN_INTERVAL = 1
REWRITE_MAX_INTERVAL = 6

REWRITE_STRATEGIES = [
    'rename_locals', 'drift_constants', 'swap_operators',
    'inject_guards', 'append_marker', 'duplicate_branch',
    'shuffle_top_level', 'invert_conditions',
]


def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}


def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
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
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:16]
    except Exception:
        return None


def _file_line_count(fpath):
    try:
        with open(fpath) as f:
            return sum(1 for _ in f)
    except Exception:
        return 0


def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False


def _record_rewrite(genome, event, detail):
    gen = genome.get('generation', 0)
    entry = json.dumps({
        'gen': gen,
        'time': time.time(),
        'event': event,
        'detail': detail,
    })
    with open(REWRITE_LOG, 'a') as f:
        f.write(entry + '\n')


def _read_rewrite_log():
    if not os.path.exists(REWRITE_LOG):
        return []
    entries = []
    with open(REWRITE_LOG) as f:
        for line in f:
            if line.strip():
                try:
                    entries.append(json.loads(line))
                except Exception:
                    pass
    return entries


def _record_manifest(genome, rewrites):
    gen = genome.get('generation', 0)
    entry = json.dumps({
        'gen': gen,
        'module': 'clockwork',
        'files': rewrites,
        'time': time.time(),
    })
    with open(MANIFEST_FILE, 'a') as f:
        f.write(entry + '\n')


def _git_commit_files(fpaths, gen):
    try:
        for fp in fpaths:
            subprocess.run(['git', 'add', fp], cwd=BASE, capture_output=True, timeout=5)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
        if status.stdout.strip():
            msg = f"[clockwork] rewrite {len(fpaths)} files | gen={gen}"
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=10)
            result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print(f"[clockwork] pushed: {msg}")
            return True
    except Exception as e:
        print(f"[clockwork] git error: {e}")
    return False


def _get_staleness_map(genome):
    sched = genome.get('clockwork_file_schedule', {})
    gen = genome.get('generation', 0)
    staleness = {}
    for fpath in _list_all_py():
        fname = os.path.relpath(fpath, BASE)
        last = sched.get(fname, 0)
        staleness[fname] = gen - last
    return staleness


def _adaptive_cadence(genome):
    log = _read_rewrite_log()
    recent = [e for e in log if e.get('gen', 0) > genome.get('generation', 0) - 10]
    successes = sum(1 for e in recent if e.get('event') == 'rewrite_ok')
    attempts = sum(1 for e in recent if e.get('event') in ('rewrite_ok', 'rewrite_fail'))
    base = genome.get('rewrite_cadence', SELF_REWRITE_CADENCE_DEFAULT)
    if attempts > 0:
        success_rate = successes / attempts
        if success_rate < 0.3:
            base = min(REWRITE_MAX_INTERVAL, base + 1)
        elif success_rate > 0.7:
            base = max(REWRITE_MIN_INTERVAL, base - 1)
    genome['rewrite_cadence'] = base
    return base


def _should_rewrite(genome):
    gen = genome.get('generation', 0)
    cadence = _adaptive_cadence(genome)
    last_rewrite_gen = genome.get('last_rewrite_gen', 0)
    return (gen - last_rewrite_gen) >= cadence


class OrchestratorMutator(ast.NodeTransformer):
    def __init__(self, strategy, fname, depth=1):
        self.strategy = strategy
        self.fname = fname
        self.depth = depth
        self.mutations = []
        self._var_map = {}

    def visit_Name(self, node):
        if self.strategy == 'rename_locals' and isinstance(node.ctx, ast.Store):
            prob = min(0.25, 0.08 + self.depth * 0.06)
            if random.random() < prob and not node.id.startswith('_'):
                if node.id not in self._var_map:
                    self._var_map[node.id] = node.id + str(random.randint(0, 99) if self.depth >= 2 else random.randint(0, 9))
                new_id = self._var_map[node.id]
                if new_id != node.id:
                    self.mutations.append(f"rename:{node.id}->{new_id}")
                    node.id = new_id
        return node

    def visit_Constant(self, node):
        if self.strategy == 'drift_constants' and isinstance(node.value, (int, float)):
            prob = min(0.3, 0.1 + self.depth * 0.07)
            if random.random() < prob and abs(node.value) > 1:
                range_factor = 0.2 + self.depth * 0.1
                drift = 1.0 + random.uniform(-range_factor, range_factor)
                old = node.value
                new_val = int(round(node.value * drift)) if isinstance(node.value, int) else round(node.value * drift, 2)
                if new_val != old:
                    node.value = new_val
                    self.mutations.append(f"const:{old}->{new_val}")
        return node

    def visit_Compare(self, node):
        if self.strategy == 'swap_operators' and random.random() < 0.15 and len(node.ops) == 1:
            CMP_SWAP = {
                ast.Lt: ast.Gt, ast.Gt: ast.Lt,
                ast.LtE: ast.GtE, ast.GtE: ast.LtE,
                ast.Eq: ast.NotEq, ast.NotEq: ast.Eq,
            }
            old_type = type(node.ops[0])
            if old_type in CMP_SWAP:
                node.ops[0] = CMP_SWAP[old_type]()
                self.mutations.append(f"cmp:{old_type.__name__}->{type(node.ops[0]).__name__}")
        return node

    def visit_BinOp(self, node):
        if self.strategy == 'swap_operators' and random.random() < 0.12:
            BINOP_SWAP = {
                ast.Add: ast.Sub, ast.Sub: ast.Add,
                ast.Mult: ast.Div, ast.Div: ast.Mult,
            }
            old_type = type(node.op)
            if old_type in BINOP_SWAP:
                node.op = BINOP_SWAP[old_type]()
                self.mutations.append(f"binop:{old_type.__name__}->{type(node.op).__name__}")
        return node

    def visit_If(self, node):
        if self.strategy == 'inject_guards' and random.random() < 0.08:
            guard = ast.If(
                test=ast.Constant(value=True),
                body=[node],
                orelse=[],
            )
            self.mutations.append("guard_wrap")
            return ast.copy_location(guard, node)
        if self.strategy == 'invert_conditions' and random.random() < 0.20:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            self.mutations.append("invert_cond")
        self.generic_visit(node)
        return node

    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        return node

    def visit_Return(self, node):
        if self.strategy == 'duplicate_branch' and random.random() < 0.06 and node.value:
            self.mutations.append("dup_return_path")
            node.value = ast.IfExp(
                test=ast.Constant(value=True),
                body=node.value,
                orelse=ast.Constant(value=0),
            )
        return node

    def visit_Module(self, node):
        self.generic_visit(node)
        return node


def _pick_strategy(depth=1):
    if depth >= 3:
        exotic = ['invert_conditions', 'inject_guards', 'duplicate_branch']
        if random.random() < 0.5:
            return random.choice(exotic)
    return random.choice(REWRITE_STRATEGIES)


def _apply_strategy(fpath, strategy, genome, depth=1):
    fname = os.path.basename(fpath)
    try:
        with open(fpath) as f:
            source = f.read()
    except Exception as e:
        return None, f"read_error: {e}"

    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        return None, f"parse_error: {e}"

    attempts = 1 if depth <= 1 else min(depth, 3)
    all_mutations = []
    current_tree = tree
    for attempt in range(attempts):
        mutator = OrchestratorMutator(strategy, fname, depth)
        try:
            tree_copy = copy.deepcopy(current_tree)
            tree_copy = mutator.visit(tree_copy)
            ast.fix_missing_locations(tree_copy)
        except Exception:
            continue
        if mutator.mutations:
            all_mutations.extend(mutator.mutations)
            current_tree = tree_copy

    if not all_mutations:
        marker = f"\n# clockwork:gen={genome.get('generation', 0)}:ts={int(time.time())}:depth={depth}:strat={strategy}\n"
        new_source = source + marker
        if new_source != source:
            try:
                compile(new_source, fpath, 'exec')
                with open(fpath, 'w') as f:
                    f.write(new_source)
                return ["appended_marker"], strategy
            except SyntaxError:
                return None, "marker_syntax_fail"
        return None, "no_mutations"

    try:
        new_source = ast.unparse(current_tree)
    except Exception as e:
        return None, f"unparse_error: {e}"

    try:
        compile(new_source, fpath, 'exec')
    except SyntaxError:
        return None, "validation_failed"

    if new_source == source:
        return None, "unchanged"

    with open(fpath, 'w') as f:
        f.write(new_source)

    return all_mutations, strategy


def _schedule_module_rewrites(genome, gen):
    sched = genome.setdefault('clockwork_file_schedule', {})
    files = _list_all_py()
    if not files:
        return []

    cadence = genome.get('rewrite_cadence', SELF_REWRITE_CADENCE_DEFAULT)
    stale_threshold = cadence + 1
    stale_files = []
    for fpath in files:
        fname = os.path.relpath(fpath, BASE)
        last = sched.get(fname, 0)
        if gen - last >= stale_threshold:
            stale_files.append((fpath, gen - last))

    stale_files.sort(key=lambda x: -x[1])
    return stale_files[:max(3, len(files) // 3)]


def _compute_generation_bandwidth(genome, pre_hashes):
    current_hashes = _snapshot_hashes()
    if not pre_hashes:
        return 0, len(current_hashes), 0.0
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
    bw = round((changed / total) * 100, 1)
    genome['self_rewrite_bandwidth'] = bw
    genome['self_rewrite_changed'] = changed
    genome['self_rewrite_total'] = total
    return changed, total, bw


def _fire_scheduled_triggers(genome, gen):
    fired = []
    triggers = genome.get('scheduled_triggers', [])
    for t in triggers:
        if t.get('gen') == gen and not t.get('fired', False):
            action = t.get('action', '')
            if action == 'force_self_rewrite':
                fired.append(f"trigger:force_self_rewrite")
            elif action == 'boost_mutation':
                old = genome.get('mutation_rate', 0.15)
                genome['mutation_rate'] = min(0.50, old + t.get('amount', 0.05))
                fired.append(f"trigger:boost_mutation(gen={gen})")
            elif action == 'inject_noise':
                genome['selection_noise_std'] = genome.get('selection_noise_std', 0.5) + t.get('amount', 0.2)
                fired.append(f"trigger:inject_noise(gen={gen})")
            elif action == 'reset_streaks':
                for a in genome.get('agents', []):
                    a['low_score_streak'] = 0
                fired.append(f"trigger:reset_streaks(gen={gen})")
            elif action == 'self_rewrite':
                old = genome.get('mutation_rate', 0.15)
                genome['mutation_rate'] = min(0.50, old + t.get('amount', 0.1))
                genome['clock_self_rewrites'] = genome.get('clock_self_rewrites', 0) + 1
                fired.append(f"trigger:self_rewrite(gen={gen})")
            elif action == 'schedule_module_rewrite':
                fired.append(f"trigger:schedule_module_rewrite(gen={gen})")
            t['fired'] = True
    return fired


def _schedule_future_triggers(genome, gen):
    triggers = genome.setdefault('scheduled_triggers', [])
    existing_gens = {t.get('gen') for t in triggers}
    cadence = genome.get('rewrite_cadence', SELF_REWRITE_CADENCE_DEFAULT)
    scheduled = []

    next_rewrite = gen + cadence
    if next_rewrite not in existing_gens:
        triggers.append({
            'gen': next_rewrite,
            'action': 'force_self_rewrite',
            'amount': 0,
            'fired': False,
        })
        scheduled.append(f"periodic_rewrite@{next_rewrite}")

    for offset in range(1, cadence + 1):
        future = gen + offset
        if future not in existing_gens and random.random() < 0.3:
            actions = ['boost_mutation', 'inject_noise', 'reset_streaks', 'schedule_module_rewrite']
            action = random.choice(actions)
            triggers.append({
                'gen': future,
                'action': action,
                'amount': round(random.uniform(0.02, 0.1), 3),
                'fired': False,
            })
            scheduled.append(f"{action}@{future}")

    if len(triggers) > 50:
        genome['scheduled_triggers'] = [t for t in triggers if not t.get('fired', False)][-30:]

    return scheduled


def _clock_emergency_rewrite(genome, gen):
    if genome.get('generation_timeouts', 0) >= 3:
        return []
    elapsed = time.time() - genome.get('gen_start_time', time.time())
    budget = genome.get('gen_time_budget', 120.0)
    if elapsed > budget * 0.9:
        genome.setdefault('scheduled_triggers', []).append({
            'gen': gen + 1,
            'action': 'force_self_rewrite',
            'amount': 0,
            'fired': False,
        })
        return ["emergency_rewrite_scheduled"]
    return []


def _execute_generation_rewrites(genome, gen):
    actions = []
    rewrites = []

    pre_hashes = genome.get('_clockwork_pre_hashes', _snapshot_hashes())

    stale_files = _schedule_module_rewrites(genome, gen)
    if stale_files:
        for fpath, staleness in stale_files:
            fname = os.path.relpath(fpath, BASE)
            depth = 1 if staleness < 4 else (2 if staleness < 8 else 3)
            strategy = _pick_strategy(depth)
            mutations, used_strategy = _apply_strategy(fpath, strategy, genome, depth)
            if mutations:
                sched = genome.setdefault('clockwork_file_schedule', {})
                sched[fname] = gen
                rewrites.append({
                    'file': fname,
                    'strategy': used_strategy,
                    'mutations': len(mutations),
                    'depth': depth,
                    'staleness': staleness,
                })
                actions.append(f"rewrite:{fname}:{used_strategy}({len(mutations)})")
                _record_rewrite(genome, 'rewrite_ok', f"{fname}:{used_strategy}:{','.join(mutations[:3])}")
                print(f"[clockwork] {fname}: {used_strategy} depth={depth} -> {mutations[:3]}")
            else:
                _record_rewrite(genome, 'rewrite_skip', f"{fname}:{used_strategy}:{used_strategy}")

    if _should_rewrite(genome):
        fpath = AUTO_ECHO
        if os.path.exists(fpath):
            strategy = _pick_strategy(depth=2)
            mutations, used_strategy = _apply_strategy(fpath, strategy, genome, depth=2)
            if mutations:
                genome['last_rewrite_gen'] = gen
                genome['source_rewrite_count'] = genome.get('source_rewrite_count', 0) + 1
                rewrites.append({
                    'file': 'auto-echo.py',
                    'strategy': used_strategy,
                    'mutations': len(mutations),
                    'depth': 2,
                    'staleness': 0,
                })
                actions.append(f"self_rewrite:auto-echo.py:{used_strategy}({len(mutations)})")
                _record_rewrite(genome, 'rewrite_ok', f"auto-echo.py:{used_strategy}:{','.join(mutations[:3])}")
                print(f"[clockwork] auto-echo.py: {used_strategy} -> {mutations[:3]}")

    post_hashes = _snapshot_hashes()
    changed, total, bw = _compute_generation_bandwidth(genome, pre_hashes)
    genome['_clockwork_pre_hashes'] = post_hashes
    actions.append(f"bw={bw}%({changed}/{total})")

    if rewrites:
        _record_manifest(genome, rewrites)
        fpaths = [os.path.join(BASE, r['file']) for r in rewrites if os.path.exists(os.path.join(BASE, r['file']))]
        if fpaths:
            _git_commit_files(fpaths, gen)

    return actions


def run(genome):
    gen = genome.get('generation', 0)
    now = time.time()
    start = genome.get('gen_start_time', now)
    elapsed = now - start
    budget = genome.get('gen_time_budget', 120.0)
    pulse = min(1.0, elapsed / budget)
    actions = []

    cadence = _adaptive_cadence(genome)
    genome['clock_pulse'] = pulse
    genome['gen_elapsed'] = round(elapsed, 1)

    triggered = _fire_scheduled_triggers(genome, gen)
    actions.extend(triggered)

    rewrite_actions = _execute_generation_rewrites(genome, gen)
    actions.extend(rewrite_actions)

    scheduled = _schedule_future_triggers(genome, gen)
    actions.extend(scheduled)

    emergency = _clock_emergency_rewrite(genome, gen)
    actions.extend(emergency)

    if pulse > 0.8:
        old = genome.get('gen_time_budget', 120.0)
        new = max(30.0, old - 15.0)
        genome['gen_time_budget'] = new
        actions.append(f"budget:{old:.0f}->{new:.0f}")
    elif pulse < 0.2 and genome.get('generation_timeouts', 0) == 0:
        old = genome.get('gen_time_budget', 120.0)
        new = min(300.0, old + 30.0)
        genome['gen_time_budget'] = new
        actions.append(f"budget:{old:.0f}->{new:.0f}")

    if random.random() < pulse * 0.2:
        old_mr = genome.get('mutation_rate', 0.15)
        drift = random.uniform(-0.03, 0.05)
        new_mr = round(max(0.05, min(0.50, old_mr + drift)), 3)
        genome['mutation_rate'] = new_mr
        actions.append(f"mr:{old_mr:.3f}->{new_mr:.3f}")

    rewrite_count = genome.get('source_rewrite_count', 0)
    sched_count = len(genome.get('clockwork_file_schedule', {}))
    actions.append(f"cadence={cadence} rewrites={rewrite_count} scheduled={sched_count} pulse={pulse:.2f}")

    genome['clock_pulse_log'] = genome.get('clock_pulse_log', [])
    genome['clock_pulse_log'].append({'gen': gen, 'actions': actions[:8]})
    if len(genome['clock_pulse_log']) > 50:
        genome['clock_pulse_log'] = genome['clock_pulse_log'][-50:]

    _save_genome(genome)

    return "[clockwork] " + "; ".join(actions) if actions else "[clockwork] no_action"
