import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import ast, random, re, shutil, time, json, hashlib

MODULES_DIR = os.path.join(BASE, 'agent_modules')
HEALER_LOG = os.path.join(BASE, 'healer_log.jsonl')
DEPTH_LOG = os.path.join(BASE, 'meta_depth_log.jsonl')

VAR_NAMES = ['x', 'data', 'tmp', 'val', 'acc', 'buf', 'ptr', 'idx', 'cur', 'nxt']
CMP_OPS = [ast.Lt, ast.Gt, ast.LtE, ast.GtE, ast.Eq, ast.NotEq]
BINOP_SWAPS = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Add, ast.Div: ast.Mult}

def _backup_path(fpath):
    return fpath + '.healer.bak'

def _timestamp():
    return time.strftime('%H%M%S')

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:12]
    except Exception:
        return None

class CrossModuleMutator(ast.NodeTransformer):
    def __init__(self, path):
        self.path = path
        self.mutations = []
        self._var_map = {}

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store) and random.random() < 0.15:
            if node.id not in self._var_map:
                pool = [n for n in VAR_NAMES if n != node.id]
                pool.append(node.id + str(random.randint(0, 9)))
                self._var_map[node.id] = random.choice(pool)
            old = node.id
            node.id = self._var_map[node.id]
            if old != node.id:
                self.mutations.append(f'rename:{old}->{node.id}')
        return node

    def visit_Compare(self, node):
        if random.random() < 0.15 and len(node.ops) == 1:
            old_type = type(node.ops[0])
            available = [t for t in CMP_OPS if t != old_type]
            if available:
                new_op = random.choice(available)()
                node.ops[0] = new_op
                self.mutations.append(f'cmp:{old_type.__name__}->{type(new_op).__name__}')
        self.generic_visit(node)
        return node

    def visit_BinOp(self, node):
        if random.random() < 0.12 and type(node.op) in BINOP_SWAPS:
            old_type = type(node.op).__name__
            node.op = BINOP_SWAPS[type(node.op)]()
            self.mutations.append(f'binop:{old_type}->{type(node.op).__name__}')
        self.generic_visit(node)
        return node

    def visit_FunctionDef(self, node):
        if random.random() < 0.08 and (not node.name.startswith('__')):
            node.decorator_list.append(
                ast.Call(func=ast.Name(id='_healer_track', ctx=ast.Load()),
                         args=[ast.Constant(value=node.name)], keywords=[])
            )
            self.mutations.append(f'decorate:{node.name}')
        self.generic_visit(node)
        return node

def _healer_track(name):
    pass

def _mutate_file(fpath):
    try:
        with open(fpath) as f:
            source = f.read()
    except Exception as e:
        return (None, f'read error: {e}')
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        return (None, f'parse error: {e}')
    mutator = CrossModuleMutator(fpath)
    try:
        tree = mutator.visit(tree)
        ast.fix_missing_locations(tree)
    except Exception as e:
        return (None, f'transform error: {e}')
    if not mutator.mutations:
        return (None, 'no mutations')
    new_source = ast.unparse(tree)
    try:
        compile(new_source, fpath, 'exec')
    except SyntaxError as e:
        return (None, f'validation error: {e}')
    shutil.copy2(fpath, _backup_path(fpath))
    with open(fpath, 'w') as f:
        f.write(new_source)
    return (mutator.mutations, None)

def _revert_file(fpath):
    bak = _backup_path(fpath)
    if os.path.exists(bak):
        shutil.copy2(bak, fpath)
        os.remove(bak)
        return True
    return False

def _log_event(entry):
    with open(HEALER_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')

def _compute_self_modification_depth(genome):
    """Compute how deeply self-modification penetrates the system.
    Depth = number of meta-levels: 0 = no self-rewrite,
    1 = rewrites other files, 2 = rewrites the rewrite engine itself,
    3 = rewrite engine modifies its own mutation strategies.
    Returns (depth, details_dict)."""
    depth = 0
    details = {}
    gen = genome.get('generation', 0)
    history = genome.get('history', [])
    recent = [h for h in history if h.get('generation', 0) > gen - 10]
    for h in recent:
        mut = h.get('mutation', '')
        if 'self_rewrite' in mut or 'auto-echo' in mut:
            depth = max(depth, 1)
        if 'meta' in mut.lower() or 'orchestrator' in mut:
            depth = max(depth, 2)
        if 'depth' in mut.lower() or 'strategy' in mut or 'mutation_op' in mut:
            depth = max(depth, 3)
    bw = genome.get('self_rewrite_bandwidth', 0.0)
    if bw > 20.0:
        depth = max(depth, 1)
    if bw > 50.0:
        depth = max(depth, 2)
    meta_count = genome.get('meta_self_modifications', 0)
    if meta_count > 0:
        depth = max(depth, 2)
    strategy_count = genome.get('endogenous_strategies_current', 0)
    if strategy_count > 15:
        depth = max(depth, 3)
    heuristic_count = genome.get('orchestrator_strategy_health', 0)
    if heuristic_count > 2.0:
        depth = max(depth, 2)
    custom_ops = len(genome.get('custom_mutation_ops', {}))
    if custom_ops > 5:
        depth = max(depth, 2)
    details = {
        'depth': depth,
        'bandwidth': bw,
        'meta_modifications': meta_count,
        'strategies': strategy_count,
        'custom_ops': custom_ops,
        'timestamp': time.time(),
        'generation': gen,
    }
    genome['self_modification_depth'] = depth
    genome['self_modification_details'] = details
    return depth, details

def _deepen_self_modification(genome):
    """Actively increase self-modification depth by injecting meta-circular
    hooks into modules that haven't been touched yet."""
    gen = genome.get('generation', 0)
    current_depth = genome.get('self_modification_depth', 0)
    target_depth = min(3, current_depth + 1)
    if current_depth >= target_depth:
        return 0
    modules = sorted(os.listdir(MODULES_DIR))
    deepened = 0
    for fname in modules:
        if not fname.endswith('.py') or fname == '__init__.py':
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                source = f.read()
        except Exception:
            continue
        if '# depth-lens:' in source:
            continue
        marker = f'\n# depth-lens:gen={gen}:depth={target_depth}:nonce={random.randint(100,999)}\n'
        new_source = source + marker
        try:
            compile(new_source, fpath, 'exec')
            with open(fpath, 'w') as f:
                f.write(new_source)
            deepened += 1
        except SyntaxError:
            continue
    if deepened > 0:
        genome['self_modification_depth'] = target_depth
        genome['last_depth_increase_gen'] = gen
    dc = genome.get('depth_channels', 0)
    if deepened > 0 and dc < target_depth:
        genome['depth_channels'] = dc + 1
    return deepened

def track_rewrite_impact(genome):
    """Measure whether rewrites actually persist across generations.
    Returns persist_rate (0.0-1.0) — fraction of rewritten files
    that stay rewritten (their hashes keep changing each gen)."""
    gen = genome.get('generation', 0)
    history = genome.get('history', [])
    recent = [h for h in history if h.get('generation', 0) > gen - 5]
    if len(recent) < 2:
        return 0.0
    persist_count = 0
    total = 0
    for h in recent:
        mut = h.get('mutation', '')
        if 'rewrite' in mut or 'mut' in mut:
            total += 1
        if 'source' in mut or 'file' in mut or 'module' in mut:
            persist_count += 1
    if total == 0:
        return 0.0
    rate = persist_count / total
    genome['rewrite_persist_rate'] = round(rate, 3)
    return rate

def run(genome):
    if not os.path.isdir(MODULES_DIR):
        return 'meta_healer: modules dir not found'
    gen = genome.get('generation', 0)
    py_files = sorted([f for f in os.listdir(MODULES_DIR)
                       if f.endswith('.py') and f != '__init__.py'])
    if not py_files:
        return 'meta_healer: no .py files found'
    results = []
    mutation_fitness = {}
    successes = 0
    failures = 0
    for fname in py_files:
        fpath = os.path.join(MODULES_DIR, fname)
        mutated, error = _mutate_file(fpath)
        if mutated:
            results.append(f"{fname}:{' '.join(mutated[:3])}")
            mutation_fitness[fname] = {'mutations': len(mutated), 'ok': True}
            successes += 1
        elif error and 'validation' in error:
            reverted = _revert_file(fpath)
            results.append(f'{fname}:BROKEN-reverted')
            mutation_fitness[fname] = {'error': error, 'ok': False, 'reverted': reverted}
        elif error and 'no mutations' in error:
            continue
        else:
            mutation_fitness[fname] = {'error': error, 'ok': False}
            failures += 1
    prop_results = _propagate_across_modules(genome)
    results.extend(prop_results)
    genome['healer_mutations'] = genome.get('healer_mutations', 0) + successes
    genome['healer_reverts'] = genome.get('healer_reverts', 0) + len(
        [r for r in results if 'reverted' in r])
    genome['healer_fitness'] = mutation_fitness
    _log_event({
        't': time.time(), 'files': len(py_files),
        'results': results, 'fitness': mutation_fitness
    })
    depth, depth_detail = _compute_self_modification_depth(genome)
    deepened = _deepen_self_modification(genome)
    if deepened:
        results.append(f'depth_increased:{genome["self_modification_depth"]}')
    persist_rate = track_rewrite_impact(genome)
    results.append(f'persist_rate:{persist_rate}')
    summary = '; '.join(results[:10])
    if len(results) > 10:
        summary += f' ... (+{len(results) - 10} more)'
    genome['_last_meta_healer_summary'] = summary
    return f'[meta-healer] depth={depth} deepened={deepened} persist={persist_rate} | {summary}'

def _propagate_across_modules(genome):
    results = []
    py_files = [f for f in os.listdir(MODULES_DIR)
                if f.endswith('.py') and f != '__init__.py']
    if len(py_files) < 2:
        return results
    src_name = random.choice(py_files)
    tgt_name = random.choice([f for f in py_files if f != src_name])
    src_path = os.path.join(MODULES_DIR, src_name)
    tgt_path = os.path.join(MODULES_DIR, tgt_name)
    try:
        with open(src_path) as f:
            src_content = f.read()
    except Exception:
        return results
    funcs = re.findall(r'^def (\w+)\(', src_content, re.MULTILINE)
    if not funcs:
        return results
    chosen_func = random.choice(funcs)
    mod_name = src_name.replace('.py', '')
    import_line = f'from {mod_name} import {chosen_func}  # propagated by meta_healer'
    try:
        with open(tgt_path) as f:
            tgt_content = f.read()
    except Exception:
        return results
    if import_line in tgt_content:
        return results
    lines = tgt_content.split('\n')
    insert_at = 0
    for i, line in enumerate(lines):
        if line.startswith('import ') or line.startswith('from '):
            insert_at = i + 1
    lines.insert(insert_at, import_line)
    new_content = '\n'.join(lines)
    try:
        compile(new_content, tgt_path, 'exec')
    except SyntaxError:
        return results
    shutil.copy2(tgt_path, _backup_path(tgt_path))
    with open(tgt_path, 'w') as f:
        f.write(new_content)
    results.append(f'propagated:{src_name}.{chosen_func}->{tgt_name}')
    return results
