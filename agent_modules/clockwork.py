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
    injection4 = f'{indent}_add_scheduled_trigger(genome, gen, "self_rewrite", 0.15, offset=1)\n'
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
        if random.random() < 0.3 or gens_since_run >= interval * 2:
            trig_count = _schedule_rewrite_wave(genome, gen)
            if trig_count:
                pulses.append(f'scheduled:{trig_count}')
        if random.random() < 0.15:
            self_muts = _rewrite_clockwork_self(genome, gen)
            if self_muts:
                changes.append(f'self:{len(self_muts)}')
                pulses.append('self_mutated')
        if random.random() < 0.1 and gens_since_run >= interval:
            inject_result = _inject_direct_trigger(genome, gen)
            if inject_result:
                changes.append('injected_direct_trigger')
                pulses.append('injected_direct_trigger')
        schedule_changes = _mutate_genome_schedule(genome, gen)
        if schedule_changes:
            changes.extend(schedule_changes)
            pulses.append('schedule_evolved')
        genome['_clockwork_pre_hashes'] = _snapshot_hashes()
        genome['_clockwork_pre_gen'] = gen
    else:
        pulses.append(f'waiting({gens_since_run}/{interval})')
    genome['clockwork_last_pulse'] = pulses
    genome['clockwork_last_changes'] = changes
    genome['clockwork_last_run'] = time.time()
    if pulses:
        for p in pulses:
            _record_pulse(gen, 'pulse', p)
    elapsed = round(time.time() - start_time, 3)
    _save_genome(genome)
    return f'[clockwork] gen={gen} elapsed={elapsed}s changes={len(changes)} rewrites={len(rewrites)} pulses={pulses}'
# feedback:agent=clockwork:gen=38:ts=1785193678:nonce=269100

# weaver:forced gen=40 ts=1785248904
genome["source_autonomy_index"] = round(min(1.0, genome.get("source_autonomy_index", 0.0) + 0.05), 3)
_wm = {"gen": genome.get("generation", 0), "module": "weaver", "files": ["clockwork.py"], "results": ["weaver:force_rewrite_clockwork"]}
with open(os.path.join(BASE, "rewrite_manifest.jsonl"), "a") as _wmf:
    _wmf.write(json.dumps(_wm) + "\n")
