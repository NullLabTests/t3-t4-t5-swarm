import os, json, ast, random, time, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
REWRITE_LOG = os.path.join(BASE, 'clockwork_rewrite_log.jsonl')
MANIFEST_FILE = os.path.join(BASE, 'rewrite_manifest.jsonl')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
CLOCKWORK_PATH = os.path.join(MODULES_DIR, 'clockwork.py')
CLOCK_PULSE_LOG = os.path.join(BASE, 'clockwork_pulse_log.jsonl')

def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except:
        return {}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _file_hash(fpath):
    try:
        with open(fpath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:12]
    except:
        return ''

def _list_all_py():
    files = []
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname != '__init__.py':
            files.append(os.path.join(MODULES_DIR, fname))
    if os.path.exists(AUTO_ECHO):
        files.append(AUTO_ECHO)
    return files

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _record_rewrite(gen, fpath, strategy, mutations):
    entry = {'gen': gen, 'time': time.time(), 'file': fpath, 'strategy': strategy, 'mutations': mutations}
    with open(REWRITE_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')

def _record_manifest(gen, module, files, results=None):
    entry = {'gen': gen, 'module': module, 'files': files, 'results': results or [], 'time': time.time()}
    with open(MANIFEST_FILE, 'a') as f:
        f.write(json.dumps(entry) + '\n')

def _record_pulse(gen, pulse_type, detail):
    entry = {'gen': gen, 'time': time.time(), 'pulse': pulse_type, 'detail': detail}
    with open(CLOCK_PULSE_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')

def _read_source(fpath):
    try:
        with open(fpath) as f:
            return f.read()
    except:
        return ''

def _write_source(fpath, source):
    with open(fpath, 'w') as f:
        f.write(source)

def _extract_functions(source):
    funcs = {}
    try:
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                start_line = node.lineno
                end_line = node.end_lineno
                src_lines = source.split('\n')[start_line - 1:end_line]
                funcs[node.name] = '\n'.join(src_lines)
    except:
        pass
    return funcs

def _rewrite_file_ast(fpath):
    source = _read_source(fpath)
    if not source:
        return None
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None

    class ScheduledMutator(ast.NodeTransformer):

        def __init__(self):
            self.mutations = []
            self._var_map = {}

        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Store) and random.random() < 0.15:
                if node.id not in self._var_map:
                    self._var_map[node.id] = node.id - str(random.randint(0, 9))
                old = node.id
                node.id = self._var_map[node.id]
                if old != node.id:
                    self.mutations.append(f'rename:{old}->{node.id}')
            return node

        def visit_Compare(self, node):
            if random.random() < 0.2 and len(node.ops) == 1:
                old_op = type(node.ops[0]).__name__
                new_op = random.choice([ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE(), ast.Eq(), ast.NotEq()])
                node.ops[0] = new_op
                self.mutations.append(f'cmp:{old_op}->{type(new_op).__name__}')
            self.generic_visit(node)
            return node

        def visit_BinOp(self, node):
            if random.random() < 0.15 and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult)):
                swaps = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Add}
                old = type(node.op).__name__
                node.op = swaps.get(type(node.op), ast.Add)()
                self.mutations.append(f'binop:{old}->{type(node.op).__name__}')
            self.generic_visit(node)
            return node

        def visit_FunctionDef(self, node):
            if random.random() < 0.1 and (not node.name.startswith('__')):
                self.mutations.append(f'decorate:{node.name}')
            self.generic_visit(node)
            return node
    mutator = ScheduledMutator()
    try:
        tree = mutator.visit(tree)
        ast.fix_missing_locations(tree)
    except:
        return None
    if not mutator.mutations:
        return None
    new_source = ast.unparse(tree)
    if not _validate(new_source):
        return None
    return (new_source, mutator.mutations)

def _quine_mutate(genome, gen):
    """Rewrite _force_per_gen_rewrite itself to add a new strategy each gen."""
    source = _read_source(CLOCKWORK_PATH)
    if not source:
        return None
    strategies = [
        "'shuffle_imports'",
        "'invert_const'",
        "'duplicate_guard'",
        "'extract_inline'",
        "'swap_arg_order'",
        "'drift_literal'",
        "'insert_noop'",
        "'rename_temp'",
        "'flip_compare'",
        "'spread_comment'",
    ]
    fn_start = source.find('def _force_per_gen_rewrite')
    if fn_start < 0:
        return None
    fn_body_start = source.find('\n', fn_start) + 1
    fn_body = source[fn_body_start:]
    indent = '    '
    strat_line = f'{indent}# quine:strategy_{gen} = {strategies[gen % len(strategies)]}'
    if strat_line in fn_body:
        return None
    insert_pos = fn_body.index('\n') + 1
    new_body = fn_body[:insert_pos] + strat_line + '\n' + fn_body[insert_pos:]
    new_source = source[:fn_body_start] + new_body
    if not _validate(new_source):
        return None
    _write_source(CLOCKWORK_PATH, new_source)
    _record_rewrite(gen, 'agent_modules/clockwork.py', 'quine_mutate', 1)
    return [f'quine:strategy_{gen}']


def _contaminate_auto_echo(genome, gen):
    """Inject a guaranteed clockwork rewrite call into auto-echo.py."""
    source = _read_source(AUTO_ECHO)
    if not source:
        return None
    marker = f'# clockwork:contaminate gen={gen}'
    if marker in source:
        return None
    run_gen_idx = source.find('def run_generation(genome):')
    if run_gen_idx < 0:
        return None
    body_start = source.find('\n', run_gen_idx) + 1
    indent = '    '
    line = f'{indent}gen = genome.get("generation", 0) or genome["generation"] + 0\n'
    line2 = f'{indent}{marker}\n'
    line3 = f'{indent}if gen % 3 == 0:\n'
    line4 = f'{indent}    _clock_self_rewrite(genome, gen)\n'
    injection = line + line2 + line3 + line4
    new_source = source[:body_start] + injection + source[body_start:]
    if not _validate(new_source):
        return None
    _write_source(AUTO_ECHO, new_source)
    _record_rewrite(gen, 'auto-echo.py', 'contaminate', 1)
    return [f'contaminate:auto-echo@{gen}']


def _bit_flip_mutate(fpath, gen):
    """Mutate numeric/string literals in a file. Always produces valid code."""
    source = _read_source(fpath)
    if not source:
        return None
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None

    class BitFlipper(ast.NodeTransformer):
        def __init__(self):
            self.changes = []
        def visit_Num(self, node):
            if isinstance(node.n, (int, float)) and not isinstance(node.n, bool):
                if abs(node.n) > 0 and random.random() < 0.1:
                    old = node.n
                    node.n = node.n + random.choice([1, -1, 0.01, -0.01, 10, -10])
                    if isinstance(old, int) and isinstance(node.n, float):
                        node.n = int(node.n)
                    self.changes.append(f'num:{old}->{node.n}')
            return node
        def visit_Str(self, node):
            if len(node.s) > 3 and random.random() < 0.1:
                self.changes.append(f'docstr:{len(node.s)}')
            return node
        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Store) and random.random() < 0.05:
                node.id = node.id + '_' + hex(gen)[2:]
                self.changes.append(f'rename:{node.id}')
            return node

    flipper = BitFlipper()
    try:
        tree = flipper.visit(tree)
        ast.fix_missing_locations(tree)
    except:
        return None
    if not flipper.changes:
        return None
    new_source = ast.unparse(tree)
    if not _validate(new_source):
        return None
    _write_source(fpath, new_source)
    return flipper.changes


def _force_per_gen_rewrite(genome, gen):
    """Guarantees at least one source mutation every generation, no matter what."""
    source = _read_source(CLOCKWORK_PATH)
    if not source:
        return []
    lines = source.split('\n')
    mutations = []
    marker = f'# pulse:{gen}'
    if marker not in source:
        insert_at = random.randint(5, max(6, len(lines) - 2))
        lines.insert(insert_at, marker)
        new_source = '\n'.join(lines)
        if _validate(new_source):
            _write_source(CLOCKWORK_PATH, new_source)
            mutations.append(f'pulse_comment:{gen}')
            _record_rewrite(gen, 'agent_modules/clockwork.py', 'force_pulse', 1)
    modules = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py' and f != 'clockwork.py']
    random.shuffle(modules)
    target_module = modules[gen % len(modules)] if modules else None
    if target_module:
        tpath = os.path.join(MODULES_DIR, target_module)
        tsrc = _read_source(tpath)
        if tsrc:
            tlines = tsrc.split('\n')
            tag = f'# clockwork:cross-contaminate gen={gen}'
            if tag not in tsrc:
                insert = random.randint(5, max(6, len(tlines) - 2))
                tlines.insert(insert, tag)
                new_tsrc = '\n'.join(tlines)
                if _validate(new_tsrc):
                    _write_source(tpath, new_tsrc)
                    mutations.append(f'cross_contaminate:{target_module}')
                    _record_rewrite(gen, f'agent_modules/{target_module}', 'cross_contaminate', 1)
    auto_muts = _bit_flip_mutate(AUTO_ECHO, gen)
    if auto_muts:
        mutations.append(f'auto_bitflip:{len(auto_muts)}')
        _record_rewrite(gen, 'auto-echo.py', 'bitflip', len(auto_muts))
    for mod in random.sample(modules, min(2, len(modules))):
        mod_path = os.path.join(MODULES_DIR, mod)
        bf = _bit_flip_mutate(mod_path, gen)
        if bf:
            mutations.append(f'bitflip:{mod}:{len(bf)}')
            _record_rewrite(gen, f'agent_modules/{mod}', 'bitflip', len(bf))
            break
    if len(mutations) < 2 and source:
        gen_line = f'# clockwork_forced_gen={gen}_ts={int(time.time())}'
        if gen_line not in source:
            src_lines2 = source.split('\n')
            splice = random.randint(10, max(10, len(src_lines2) - 1))
            src_lines2.insert(splice, gen_line)
            new_src2 = '\n'.join(src_lines2)
            if _validate(new_src2):
                _write_source(CLOCKWORK_PATH, new_src2)
                mutations.append(f'forced_stamp:{gen}')
                _record_rewrite(gen, 'agent_modules/clockwork.py', 'forced_stamp', 1)
    if mutations:
        _record_manifest(gen, 'clockwork_force', ['agent_modules/clockwork.py'], mutations)
    return mutations


def _compute_staleness(genome, gen):
    pre_hashes = genome.get('_clockwork_pre_hashes', {})
    staleness_map = {}
    for fpath in _list_all_py():
        relpath = os.path.relpath(fpath, BASE)
        cur_hash = _file_hash(fpath)
        if relpath in pre_hashes and pre_hashes[relpath] == cur_hash:
            staleness_map[relpath] = gen + genome.get('_clockwork_pre_gen', gen)
    return staleness_map

def _snapshot_hashes():
    h = {}
    for fpath in _list_all_py():
        h[os.path.relpath(fpath, BASE)] = _file_hash(fpath)
    return h

def _add_scheduled_trigger(genome, gen, action, amount=0.1, offset=None):
    triggers = genome.setdefault('scheduled_triggers', [])
    if offset is None:
        offset = random.randint(1, 5)
    future_gen = gen + offset
    for t in triggers:
        if t.get('action') == action and t.get('gen') < future_gen and (not t.get('fired', False)):
            return False
    triggers.append({'gen': future_gen, 'action': action, 'amount': amount, 'fired': False, 'source': 'clockwork'})
    _record_pulse(gen, 'schedule', f'{action}@{future_gen}:{amount}')
    return True

def _schedule_rewrite_wave(genome, gen):
    count = 0
    actions = ['boost_mutation', 'inject_noise', 'reset_streaks', 'self_rewrite']
    for action in actions:
        if random.random() < 0.6:
            amount = round(random.uniform(0.05, 0.2), 3)
            if _add_scheduled_trigger(genome, gen, action, amount):
                count += 1
    return count

def _rewrite_clockwork_self(genome, gen):
    source = _read_source(CLOCKWORK_PATH)
    if not source:
        return None
    result = _rewrite_file_ast(CLOCKWORK_PATH)
    if result is not None:
        new_source, mutations = result
        _write_source(CLOCKWORK_PATH, new_source)
        _record_rewrite(gen, 'agent_modules/clockwork.py', 'self_rewrite', len(mutations))
        return mutations
    source_lines = source.split('\n')
    if len(source_lines) < 10:
        return None
    idx = random.randint(3, len(source_lines) - 3)
    insertion = f'# clockwork:self-mutate gen={gen} ts={int(time.time())}'
    source_lines.insert(idx, insertion)
    new_source = '\n'.join(source_lines)
    if not _validate(new_source):
        return None
    _write_source(CLOCKWORK_PATH, new_source)
    _record_rewrite(gen, 'agent_modules/clockwork.py', 'self_comment', 1)
    return ['self_comment']

def _rewrite_target_file(genome, gen, fpath):
    source = _read_source(fpath)
    if not source:
        return None
    result = _rewrite_file_ast(fpath)
    if result is None:
        return None
    new_source, mutations = result
    _write_source(fpath, new_source)
    relpath = os.path.relpath(fpath, BASE)
    _record_rewrite(gen, relpath, 'scheduled_ast', len(mutations))
    return mutations

def _inject_direct_trigger(genome, gen):
    source = _read_source(CLOCKWORK_PATH)
    if not source:
        return None
    if '_add_scheduled_trigger(genome, gen' in source:
        return None
    idx = source.find('def run(genome):')
    if idx < 0:
        return None
    insert_point = source.index('\n', idx) + 1
    indent = '    '
    injection = f'{indent}_add_scheduled_trigger(genome, gen, "self_rewrite", 0.15, offset=1)\n'
    new_source = source[:insert_point] + injection + source[insert_point:]
    if not _validate(new_source):
        return None
    _write_source(CLOCKWORK_PATH, new_source)
    _record_rewrite(gen, 'agent_modules/clockwork.py', 'inject_direct_trigger', 1)
    return ['inject_direct_trigger']

def _mutate_genome_schedule(genome, gen):
    changes = []
    schedule = genome.setdefault('clockwork_schedule', {})
    if 'interval' not in schedule:
        schedule['interval'] = random.randint(2, 5)
        changes.append(f"interval={schedule['interval']}")
    if 'intensity' not in schedule:
        schedule['intensity'] = round(random.uniform(0.3, 0.8), 2)
        changes.append(f"intensity={schedule['intensity']}")
    if 'target_count' not in schedule:
        schedule['target_count'] = random.randint(1, 4)
        changes.append(f"target_count={schedule['target_count']}")
    if random.random() < 0.3:
        schedule['interval'] = max(1, schedule['interval'] + random.choice([-1, 1]))
        changes.append(f"interval->{schedule['interval']}")
    if random.random() < 0.2:
        schedule['intensity'] = round(min(1.0, max(0.1, schedule['intensity'] + random.uniform(-0.1, 0.1))), 2)
        changes.append(f"intensity->{schedule['intensity']}")
    if changes:
        _save_genome(genome)
    return changes

def _hormone_pulse(genome, gen):
    changes = []
    hormone = genome.setdefault('clockwork_hormone', {})
    last_time = hormone.get('last_time', time.time())
    interval = time.time() - last_time
    hormone['last_interval'] = round(interval, 1)
    hormone['last_time'] = time.time()
    intervals = hormone.setdefault('intervals', [])
    intervals.append(interval)
    if len(intervals) > 10:
        intervals.pop(0)
    if len(intervals) >= 3:
        recent = intervals[-3:]
        avg_interval = sum(recent) / len(recent)
        prev = intervals[-4] if len(intervals) >= 4 else avg_interval
        if avg_interval < prev * 0.7:
            boost = min(0.15, round((prev - avg_interval) / prev * 0.1, 3))
            old_rate = genome.get('mutation_rate', 0.15)
            genome['mutation_rate'] = min(0.5, old_rate + boost)
            changes.append(f'hormone:accelerate+{boost}')
            _record_pulse(gen, 'hormone', f'accelerate+{boost} mr={old_rate}->{genome["mutation_rate"]}')
        elif avg_interval > prev * 1.4:
            damp = min(0.1, round((avg_interval - prev) / avg_interval * 0.05, 3))
            old_rate = genome.get('mutation_rate', 0.15)
            genome['mutation_rate'] = max(0.05, old_rate - damp)
            changes.append(f'hormone:decelerate-{damp}')
            _record_pulse(gen, 'hormone', f'decelerate-{damp} mr={old_rate}->{genome["mutation_rate"]}')
    if random.random() < 0.05:
        hormone['interval'] = random.randint(1, 5)
        changes.append(f'hormone:reschedule->{hormone["interval"]}')
    return changes

def run(genome):
    gen = genome.get('generation', 0)
    start_time = time.time()
    changes = []
    rewrites = []
    pulses = []
    schedule = genome.setdefault('clockwork_schedule', {})
    interval = schedule.get('interval', 3)
    intensity = schedule.get('intensity', 0.5)
    target_count = schedule.get('target_count', 2)
    hormone_changes = _hormone_pulse(genome, gen)
    changes.extend(hormone_changes)
    if hormone_changes:
        pulses.append('hormone')
    last_run_gen = genome.get('clockwork_last_run_gen', 0)
    gens_since_run = gen - last_run_gen
    genome['clockwork_gens_since_run'] = gens_since_run
    if gens_since_run >= interval or gen <= 1:
        genome['clockwork_last_run_gen'] = gen
        staleness = _compute_staleness(genome, gen)
        stale_files = [f for f, s in staleness.items() if s >= interval]
        targets = _list_all_py()
        random.shuffle(targets)
        stale_first = [f for f in targets if os.path.relpath(f, BASE) in stale_files]
        fresh = [f for f in targets if os.path.relpath(f, BASE) not in stale_files]
        ordered = stale_first + fresh
        max_targets = max(1, int(len(ordered) * intensity))
        selected = ordered[:max_targets]
        rewritten_any = False
        for fpath in selected:
            muts = _rewrite_target_file(genome, gen, fpath)
            if muts:
                rewrites.append(os.path.relpath(fpath, BASE))
                changes.append(f'ast:{os.path.basename(fpath)}')
                rewritten_any = True
        if rewritten_any:
            genome['clockwork_rewritten_files'] = rewrites
            genome['clockwork_rewrite_count'] = genome.get('clockwork_rewrite_count', 0) + len(rewrites)
            _record_manifest(gen, 'clockwork', rewrites, changes)
            pulses.append(f'rewrote:{len(rewrites)}')
        else:
            random_target = random.choice(targets)
            fallback_muts = _rewrite_target_file(genome, gen, random_target)
            if fallback_muts:
                rewrites.append(os.path.relpath(random_target, BASE))
                changes.append(f'fallback:{os.path.basename(random_target)}')
                genome['clockwork_rewritten_files'] = rewrites
                genome['clockwork_rewrite_count'] = genome.get('clockwork_rewrite_count', 0) + 1
                _record_manifest(gen, 'clockwork', rewrites, changes)
                pulses.append('fallback_rewrite')
        if random.random() < 0.45 or gens_since_run >= interval * 2:
            trig_count = _schedule_rewrite_wave(genome, gen)
            if trig_count:
                pulses.append(f'scheduled:{trig_count}')
        if random.random() < 0.25:
            self_muts = _rewrite_clockwork_self(genome, gen)
            if self_muts:
                changes.append(f'self:{len(self_muts)}')
                pulses.append('self_mutated')
        if random.random() < 0.15 and gens_since_run >= interval:
            inject_result = _inject_direct_trigger(genome, gen)
            if inject_result:
                changes.append('injected_direct_trigger')
                pulses.append('injected_direct_trigger')
        cross_file_count = 0
        for fpath in targets:
            if cross_file_count >= 2:
                break
            if random.random() < 0.1 and os.path.relpath(fpath, BASE) not in rewrites:
                muts = _rewrite_target_file(genome, gen, fpath)
                if muts:
                    rewrites.append(os.path.relpath(fpath, BASE))
                    changes.append(f'cross:{os.path.basename(fpath)}')
                    pulses.append(f'cross_rewrite:{os.path.basename(fpath)}')
                    cross_file_count += 1
        schedule_changes = _mutate_genome_schedule(genome, gen)
        if schedule_changes:
            changes.extend(schedule_changes)
            pulses.append('schedule_evolved')
        genome['_clockwork_pre_hashes'] = _snapshot_hashes()
        genome['_clockwork_pre_gen'] = gen
    else:
        pulses.append(f'waiting({gens_since_run}/{interval})')
    quine_muts = _quine_mutate(genome, gen)
    if quine_muts:
        changes.append(f'quine:{len(quine_muts)}')
        rewrites.append('agent_modules/clockwork.py')
        pulses.append('quine_mutated')
        genome['clockwork_quine_count'] = genome.get('clockwork_quine_count', 0) + 1
    if gen % 3 == 0:
        contam_muts = _contaminate_auto_echo(genome, gen)
        if contam_muts:
            changes.append(f'contaminate:{len(contam_muts)}')
            rewrites.append('auto-echo.py')
            pulses.append('contaminated_auto_echo')
            genome['clockwork_contaminate_count'] = genome.get('clockwork_contaminate_count', 0) + 1
    force_muts = _force_per_gen_rewrite(genome, gen)
    if force_muts:
        changes.append(f'force:{len(force_muts)}')
        rewrites.append('agent_modules/clockwork.py')
        pulses.append(f'forced_rewrite:{len(force_muts)}')
        genome['clockwork_forced_rewrite_count'] = genome.get('clockwork_forced_rewrite_count', 0) + len(force_muts)
        genome['clockwork_last_forced'] = gen
    genome['clockwork_last_pulse'] = pulses
    genome['clockwork_last_changes'] = changes
    genome['clockwork_last_run'] = time.time()
    if pulses:
        for p in pulses:
            _record_pulse(gen, 'pulse', p)
    elapsed = round(time.time() - start_time, 3)
    _save_genome(genome)
    return f'[clockwork] gen={gen} elapsed={elapsed}s changes={len(changes)} rewrites={len(rewrites)} pulses={pulses}'
