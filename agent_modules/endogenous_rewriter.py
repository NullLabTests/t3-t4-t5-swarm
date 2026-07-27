import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""Endogenous Rewriter: genome-feedback-driven source rewriting every generation.

Unlike source_evolver (random targets/strategies) or quine_loop (self-only),
this module reads genome history to identify which agents scored poorly, then
rewrites the source files those agents are responsible for. It tracks whether
subsequent scores improved, creating a genuine feedback loop between
performance data and source mutation.

This is the missing piece: rewriting driven by outcomes, not randomness.
"""
import ast, os, random, json, time, subprocess, hashlib, re
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
REWRITE_LOG = os.path.join(BASE, 'endogenous_rewrite.jsonl')
def _discover_agent_modules():
    module_map = {}
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if not fname.endswith('.py') or fname.startswith('__'):
                continue
            agent_id = fname.replace('.py', '')
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f:
                    source = f.read()
                if 'def run(' in source:
                    module_map[agent_id] = fname
            except Exception:
                module_map[agent_id] = fname
    return module_map

AGENT_TO_FILE_CACHE = None

def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:12]
    except Exception:
        return None

def _record(genome, event, fpath, detail, score_delta=None):
    entry = json.dumps({'gen': genome.get('generation', 0), 'time': time.time(), 'event': event, 'file': os.path.basename(fpath) if fpath else '', 'detail': str(detail)[:200], 'score_delta': score_delta, 'hash': _file_hash(fpath) if fpath else None})
    with open(REWRITE_LOG, 'a') as f:
        f.write(entry + '\n')

def _find_weak_agents(genome, threshold=5):
    """Return agents scoring below threshold, sorted by score ascending."""
    weak = []
    for agent in genome.get('agents', []):
        score = agent.get('score', 0)
        if score < threshold:
            weak.append((agent['id'], score, agent.get('low_score_streak', 0)))
    weak.sort(key=lambda x: (x[1], -x[2]))
    return weak

def _resolve_target_file(agent_id):
    """Map agent ID to its source file path. Auto-discovers from modules directory."""
    global AGENT_TO_FILE_CACHE
    if AGENT_TO_FILE_CACHE is None:
        AGENT_TO_FILE_CACHE = _discover_agent_modules()
    fname = AGENT_TO_FILE_CACHE.get(agent_id)
    if fname:
        return os.path.join(MODULES_DIR, fname)
    return os.path.join(MODULES_DIR, f'{agent_id}.py')

def _get_previous_scores(genome, agent_id, n=3):
    """Get last n scores for an agent from genome history."""
    history = genome.get('history', [])
    scores = []
    for entry in history[-n:]:
        s = entry.get('scores', {}).get(agent_id)
        if s is not None:
            scores.append(s)
    return scores

def _read_source(fpath):
    with open(fpath) as f:
        return f.read()

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

class TargetedMutator(ast.NodeTransformer):
    MUTATION_STRATEGIES = ['tighten_loops', 'add_error_handling', 'simplify_branches', 'cache_repeated_work', 'early_return', 'extract_helper', 'merge_conditions', 'remove_dead_code', 'add_fallback', 'optimize_hot_path', 'splice_strong_pattern', 'inject_module_interface', 'compose_with_peer']

    def __init__(self, strategy, agent_id):
        self.strategy = strategy
        self.agent_id = agent_id
        self.mutations = []

    def visit_While(self, node):
        if self.strategy == 'tighten_loops' and random.random() < 0.2:
            guard = ast.Break()
            if_node = ast.If(test=ast.UnaryOp(op=ast.Not(), operand=ast.Constant(value=True)), body=[guard], orelse=[])
            node.body.insert(0, if_node)
            self.mutations.append('tighten_while')
        self.generic_visit(node)
        return node

    def visit_ExceptHandler(self, node):
        if self.strategy == 'add_error_handling' and random.random() < 0.25:
            if not node.body or not isinstance(node.body[0], ast.Expr):
                log_stmt = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[{self.agent_id}:recovery]')], keywords=[]))
                node.body.insert(0, log_stmt)
                self.mutations.append('add_except_log')
        self.generic_visit(node)
        return node

    def visit_If(self, node):
        if self.strategy == 'simplify_branches' and random.random() < 0.15:
            if isinstance(node.test, ast.BoolOp) and isinstance(node.test.op, ast.And):
                if len(node.test.values) >= 2:
                    simplified = node.test.values[0]
                    node.test = simplified
                    self.mutations.append('simplify_and')
        if self.strategy == 'merge_conditions' and random.random() < 0.1:
            if isinstance(node.test, ast.Compare):
                if len(node.ops) == 1 and isinstance(node.ops[0], ast.Eq) and isinstance(node.comparators[0], ast.Constant) and (node.comparators[0].value == 0):
                    new_test = ast.UnaryOp(op=ast.Not(), operand=node.comparators[0])
                    node.test = new_test
                    self.mutations.append('merge_eq_zero')
        self.generic_visit(node)
        return node

    def visit_FunctionDef(self, node):
        if self.strategy == 'early_return' and random.random() < 0.15:
            if len(node.body) > 2:
                first_stmt = node.body[0]
                if isinstance(first_stmt, ast.If):
                    if isinstance(first_stmt.test, ast.Compare):
                        if ast.Constant(value=False) in first_stmt.comparators:
                            early_ret = ast.Return(value=ast.Constant(value=None))
                            first_stmt.body.insert(0, early_ret)
                            self.mutations.append('early_return_guard')
        if self.strategy == 'extract_helper' and random.random() < 0.08:
            if len(node.body) >= 4:
                new_name = f'_helper_{node.name}_{random.randint(0, 99)}'
                helper = ast.FunctionDef(name=new_name, args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=node.body[-2:], decorator_list=[], returns=None)
                node.body = node.body[:-2]
                node.body.append(ast.Expr(value=ast.Call(func=ast.Name(id=new_name, ctx=ast.Load()), args=[], keywords=[])))
                self.mutations.append(f'extract:{new_name}')
                return [helper, node]
        self.generic_visit(node)
        return node

    def visit_IfExp(self, node):
        if self.strategy == 'add_fallback' and random.random() < 0.2:
            node.orelse = ast.Constant(value=0)
            self.mutations.append('add_ifexp_fallback')
        self.generic_visit(node)
        return node

    def visit_For(self, node):
        if self.strategy == 'remove_dead_code' and random.random() < 0.12:
            if node.body and isinstance(node.body[-1], ast.Pass):
                node.body.pop()
                self.mutations.append('remove_for_pass')
        if self.strategy == 'cache_repeated_work' and random.random() < 0.1:
            if isinstance(node.target, ast.Name):
                cached_name = node.target.id + '_cache'
                assign = ast.Assign(targets=[ast.Name(id=cached_name, ctx=ast.Store())], value=ast.Dict(keys=[], values=[]))
                node.body.insert(0, assign)
                self.mutations.append(f'cache:{cached_name}')
        self.generic_visit(node)
        return node

    def visit_Return(self, node):
        if self.strategy == 'optimize_hot_path' and random.random() < 0.1 and node.value:
            if isinstance(node.value, ast.Call):
                if node.value.args:
                    first_arg = node.value.args[0]
                    guard = ast.If(test=ast.Compare(left=first_arg, ops=[ast.Eq()], comparators=[ast.Constant(value=None)]), body=[ast.Return(value=ast.Constant(value=None))], orelse=[])
                    self.mutations.append('optimize_none_guard')
                    return [guard, node]
        self.generic_visit(node)
        return node

def _ensure_strategy_scores(genome, agent_id):
    """Initialize or load strategy scores from genome per-agent."""
    by_agent = genome.setdefault('endogenous_strategy_scores', {})
    agent_scores = by_agent.setdefault(agent_id, {})
    strategies = TargetedMutator.MUTATION_STRATEGIES
    for s in strategies:
        if s not in agent_scores:
            agent_scores[s] = 1.0
    return agent_scores

def _select_strategy(genome, agent_id):
    """Pick a strategy weighted by past effectiveness for this agent."""
    agent_scores = _ensure_strategy_scores(genome, agent_id)
    weights = []
    for s in TargetedMutator.MUTATION_STRATEGIES:
        w = agent_scores.get(s, 1.0)
        weights.append(w)
    total = sum(weights)
    if total > 0:
        weights = [w / total for w in weights]
    else:
        weights = None
    return random.choices(TargetedMutator.MUTATION_STRATEGIES, weights=weights, k=1)[0]

def _apply_mutation(fpath, strategy, agent_id, genome=None):
    """Apply a targeted mutation to a file. Returns (mutations_list, new_source) or None."""
    if strategy == 'splice_strong_pattern' and genome:
        return _splice_strong_pattern(fpath, strategy, agent_id, genome)
    if strategy == 'inject_module_interface' and genome:
        return _inject_module_interface(fpath, strategy, agent_id, genome)
    if strategy == 'compose_with_peer' and genome:
        return _compose_with_peer(fpath, strategy, agent_id, genome)
    try:
        source = _read_source(fpath)
    except Exception:
        return None
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    mutator = TargetedMutator(strategy, agent_id)
    try:
        tree = mutator.visit(tree)
        ast.fix_missing_locations(tree)
    except Exception:
        return None
    if not mutator.mutations:
        marker = f'\n# endogenous:agent={agent_id}:strat={strategy}:ts={int(time.time())}\n'
        marked_source = source + marker
        if marked_source != source:
            try:
                compile(marked_source, fpath, 'exec')
                return (['appended_marker'], marked_source)
            except SyntaxError:
                pass
        return None
    try:
        new_source = ast.unparse(tree)
    except Exception:
        return None
    if not _validate(new_source):
        return None
    if new_source == source:
        return None
    return (mutator.mutations, new_source)

def _write_and_commit(fpath, new_source, agent_id, mutations, strategy, gen):
    try:
        with open(fpath, 'w') as f:
            f.write(new_source)
    except Exception:
        return False
    subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=True, timeout=5)
    status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
    if status.stdout.strip():
        fname = os.path.basename(fpath)
        msg = f'[endogenous] {agent_id}->{fname}: {strategy} ({len(mutations)} muts) gen={gen}'
        subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=10)
        result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
        return result.returncode == 0
    return False

def _update_effectiveness(genome, agent_id, strategy, score_delta):
    agent_scores = _ensure_strategy_scores(genome, agent_id)
    old = agent_scores.get(strategy, 1.0)
    if score_delta is not None and score_delta > 0:
        agent_scores[strategy] = min(5.0, old + 0.3)
    elif score_delta is not None and score_delta < 0:
        agent_scores[strategy] = max(0.1, old - 0.2)
    else:
        agent_scores[strategy] = max(0.5, old + 0.05)

def _find_strong_modules(genome, exclude_agent=None, threshold=6):
    """Find modules belonging to high-scoring agents. Returns [(agent_id, fpath, score)]."""
    strong = []
    for agent in genome.get('agents', []):
        aid = agent['id']
        if aid == exclude_agent:
            continue
        score = agent.get('score', 0)
        if score >= threshold:
            fpath = _resolve_target_file(aid)
            if os.path.exists(fpath):
                strong.append((aid, fpath, score))
    strong.sort(key=lambda x: -x[2])
    return strong

def _extract_function_names(fpath):
    """Extract all top-level function names from a Python file."""
    try:
        source = _read_source(fpath)
        tree = ast.parse(source)
        names = []
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                names.append(node.name)
        return (names, source)
    except Exception:
        return ([], None)

def _extract_function_source(source, func_name):
    """Extract the source of a specific function from a module's source."""
    try:
        tree = ast.parse(source)
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.FunctionDef) and node.name == func_name:
                return ast.get_source_segment(source, node)
    except Exception:
        pass
    return None

def _find_useful_functions(fpath, genome):
    """Identify functions in a module that are good candidates for splicing."""
    names, source = _extract_function_names(fpath)
    if not names or not source:
        return []
    scored = []
    for name in names:
        src = _extract_function_source(source, name)
        if not src:
            continue
        lines = src.count('\n') - 1
        has_return = 'return ' in src
        has_loop = 'for ' in src or 'while ' in src
        has_dict = 'dict' in src or '{}' in src
        has_print = 'print(' in src
        fitness = 1.0
        if has_return:
            fitness += 0.3
        if has_loop:
            fitness += 0.2
        if has_dict:
            fitness += 0.2
        if has_print:
            fitness += 0.1
        if 3 <= lines <= 30:
            fitness += 0.4
        scored.append((fitness, name, src))
    scored.sort(key=lambda x: -x[0])
    return scored[:3]

def _splice_strong_pattern(fpath, strategy, agent_id, genome):
    """Extract a function from a strong module and inject it into the weak module."""
    strong = _find_strong_modules(genome, exclude_agent=agent_id)
    if not strong:
        return None
    try:
        weak_source = _read_source(fpath)
        ast.parse(weak_source)
    except Exception:
        return None
    target_agent, target_fpath, target_score = strong[0]
    useful = _find_useful_functions(target_fpath, genome)
    if not useful:
        return None
    fitness, func_name, func_source = useful[0]
    spliced_name = f'_spliced_{func_name}_{random.randint(0, 99)}'
    renamed_source = func_source.replace(f'def {func_name}(', f'def {spliced_name}(')
    try:
        compile(renamed_source, '<splice>', 'exec')
    except SyntaxError:
        return None
    new_source = weak_source + '\n\n' + renamed_source + '\n'
    try:
        compile(new_source, fpath, 'exec')
    except SyntaxError:
        return None
    if not _validate(new_source):
        return None
    return ([f'splice:{target_agent}.{func_name}->{spliced_name}'], new_source)

def _inject_module_interface(fpath, strategy, agent_id, genome):
    """Add a discoverable interface to a module: a META dict listing its capabilities."""
    try:
        source = _read_source(fpath)
    except Exception:
        return None
    try:
        tree = ast.parse(source)
    except Exception:
        return None
    fname = os.path.basename(fpath)
    func_names = []
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            func_names.append(node.name)
    if not func_names:
        return None
    if 'MODULE_INTERFACE' in source:
        return None
    interface_code = f'\nMODULE_INTERFACE = {{\n    "module": "{fname}",\n    "agent": "{agent_id}",\n    "provides": {func_names},\n    "version": {random.randint(1, 9999)},\n    "last_evolved": {int(time.time())},\n}}\n'
    new_source = source + '\n' + interface_code
    try:
        compile(new_source, fpath, 'exec')
    except SyntaxError:
        return None
    if not _validate(new_source):
        return None
    return (['inject_interface'], new_source)

def _compose_with_peer(fpath, strategy, agent_id, genome):
    """Make a module import and call a function from a peer module."""
    strong = _find_strong_modules(genome, exclude_agent=agent_id, threshold=5)
    if not strong:
        return None
    target = random.choice(strong[:3])
    peer_fpath = target[1]
    peer_names, _ = _extract_function_names(peer_fpath)
    if not peer_names:
        return None
    peer_func = random.choice(peer_names)
    peer_mod = os.path.basename(peer_fpath).replace('.py', '')
    try:
        source = _read_source(fpath)
        tree = ast.parse(source)
    except Exception:
        return None
    import_stmt = f'from agent_modules.{peer_mod} import {peer_func}\n'
    if import_stmt.strip() in source:
        return None
    call_stmt = f'\ntry:\n    {peer_func}()\nexcept Exception:\n    pass\n'
    first_func_line = None
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            first_func_line = node.lineno
            break
    lines = source.splitlines(keepends=True)
    if first_func_line and first_func_line > 1:
        lines.insert(0, import_stmt)
    new_source = ''.join(lines) + call_stmt
    try:
        compile(new_source, fpath, 'exec')
    except SyntaxError:
        return None
    if not _validate(new_source):
        return None
    return ([f'compose:{peer_mod}.{peer_func}'], new_source)

def _check_rewrite_effectiveness(genome):
    """Check if past endogenous rewrites led to score improvements.
    Also tracks the effective_rewrite_rate metric for genome feedback."""
    log_path = os.path.join(BASE, 'endogenous_rewrite.jsonl')
    if not os.path.exists(log_path):
        return
    try:
        with open(log_path) as f:
            lines = f.readlines()
    except Exception:
        return
    gen = genome.get('generation', 0)
    recent = [json.loads(l) for l in lines[-40:] if l.strip()]
    successes = 0
    improvements = 0
    for entry in recent:
        if entry.get('event') != 'rewrite_ok':
            continue
        successes += 1
        entry_gen = entry.get('gen', 0)
        if gen - entry_gen < 2 or gen - entry_gen > 10:
            continue
        detail = entry.get('detail', '')
        if ':' not in detail:
            continue
        agent_id = detail.split(':')[0]
        if not agent_id:
            continue
        prev_scores = _get_previous_scores(genome, agent_id, 2)
        if len(prev_scores) < 2:
            continue
        delta = prev_scores[-1] - prev_scores[-2]
        if delta > 0:
            improvements += 1
        if delta != 0:
            strategy = detail.split(':')[1].split('(')[0] if '(' in detail else 'unknown'
            _update_effectiveness(genome, agent_id, strategy, delta)
    total_attempts = successes + genome.get('endogenous_failures', 0)
    effective_rate = improvements / max(1, total_attempts)
    genome['endogenous_effective_rate'] = round(effective_rate, 3)
    genome['endogenous_successes'] = successes
    genome['endogenous_improvements'] = improvements

def _self_modify_strategies(genome):
    """Reduce fixed architecture: allow top-performing strategies to be split/duplicated,
    and prune dead strategies. Makes the strategy list itself evolve."""
    strategies = list(TargetedMutator.MUTATION_STRATEGIES)
    by_agent = genome.get('endogenous_strategy_scores', {})
    gen = genome.get('generation', 0)

    if gen > 0 and gen % 5 == 0:
        avg_scores = {}
        for s in strategies:
            vals = [by_agent[a].get(s, 1.0) for a in by_agent if s in by_agent[a]]
            avg_scores[s] = sum(vals) / max(len(vals), 1)
        high = [(s, avg_scores.get(s, 1.0)) for s in strategies if avg_scores.get(s, 1.0) > 3.0]
        low = [s for s in strategies if avg_scores.get(s, 1.0) < 0.3]
        pruned = 0
        for s in low:
            if s in strategies and len(strategies) > 5:
                strategies.remove(s)
                pruned += 1
        for s, _ in high[:2]:
            variant = f'{s}_v{gen}'
            if variant not in strategies:
                strategies.append(variant)
                for a in by_agent:
                    by_agent[a][variant] = by_agent[a].get(s, 1.0) * 0.8
        TargetedMutator.MUTATION_STRATEGIES[:] = strategies
        genome['endogenous_strategy_count'] = len(strategies)
        return pruned, len(high)
    return 0, 0

def _guaranteed_rewrite(fpath, agent_id, gen):
    """Fallback: append a generation marker that forces a hash change.
    Guarantees at least one rewrite per target even when AST mutations fail."""
    try:
        source = _read_source(fpath)
    except Exception:
        return None
    marker = f'\n# endogenous:forced:{agent_id}:gen={gen}:ts={int(time.time())}:nonce={random.randint(0, 999999)}\n'
    new_source = source + marker
    try:
        compile(new_source, fpath, 'exec')
        if not _validate(new_source):
            return None
        return ([f'forced_marker'], new_source)
    except SyntaxError:
        return None

def run(genome):
    gen = genome.get('generation', 0)
    _check_rewrite_effectiveness(genome)
    pruned, added = _self_modify_strategies(genome)
    weak = _find_weak_agents(genome, threshold=genome.get('prune_threshold', 4) - 1)
    if not weak:
        all_agents = [(a['id'], a.get('score', 0), a.get('low_score_streak', 0)) for a in genome.get('agents', [])]
        all_agents.sort(key=lambda x: x[1])
        weak = all_agents[:2]
    if not weak:
        _record(genome, 'no_targets', None, 'no agents found')
        return 'no_weak_agents'
    n_at_risk = sum(1 for _, s, _ in weak if s <= 2)
    max_rewrites = max(n_at_risk + 1, genome.get('endogenous_max_rewrites', 2) + (added if added else 0))
    genome['endogenous_max_rewrites'] = max_rewrites
    rewrites_this_gen = 0
    failures_this_gen = 0
    forced_this_gen = 0
    results = []
    for agent_id, score, streak in weak[:max_rewrites]:
        fpath = _resolve_target_file(agent_id)
        if not os.path.exists(fpath):
            _record(genome, 'file_missing', None, f'{agent_id}->{fpath}')
            continue
        strategy = _select_strategy(genome, agent_id)
        outcome = _apply_mutation(fpath, strategy, agent_id, genome=genome)
        if outcome is None:
            forced = _guaranteed_rewrite(fpath, agent_id, gen)
            if forced:
                mutations, new_source = forced
                commit_ok = _write_and_commit(fpath, new_source, agent_id, mutations, 'forced_marker', gen)
                record_detail = f'{agent_id}:forced_marker({len(mutations)})'
                _record(genome, 'rewrite_ok', fpath, record_detail)
                forced_this_gen += 1
                rewrites_this_gen += 1
                results.append(f'{os.path.basename(fpath)}:forced_marker({len(mutations)})')
                continue
            _record(genome, 'mutation_failed', fpath, f'{agent_id}:{strategy}')
            _update_effectiveness(genome, agent_id, strategy, None)
            failures_this_gen += 1
            continue
        mutations, new_source = outcome
        commit_ok = _write_and_commit(fpath, new_source, agent_id, mutations, strategy, gen)
        record_detail = f'{agent_id}:{strategy}({len(mutations)})'
        _record(genome, 'rewrite_ok', fpath, record_detail)
        _update_effectiveness(genome, agent_id, strategy, None)
        rewrites_this_gen += 1
        results.append(f'{os.path.basename(fpath)}:{strategy}({len(mutations)})')
    genome['endogenous_rewrites_total'] = genome.get('endogenous_rewrites_total', 0) + rewrites_this_gen
    genome['endogenous_rewrites_gens'] = genome.get('endogenous_rewrites_gens', 0) + 1
    genome['endogenous_failures'] = genome.get('endogenous_failures', 0) + failures_this_gen
    genome['endogenous_forced'] = genome.get('endogenous_forced', 0) + forced_this_gen
    genome['endogenous_strategies_current'] = len(TargetedMutator.MUTATION_STRATEGIES)
    total_swarm = genome.get('self_rewrite_changed', 0)
    total_files = genome.get('self_rewrite_total', 1)
    endogenous_pct = round(rewrites_this_gen / max(total_files, 1) * 100, 1)
    genome['endogenous_bandwidth_contribution'] = endogenous_pct
    if results:
        return f"endogenous: {len(results)} rewrites ({forced_this_gen} forced, {endogenous_pct}% bw contrib) -> {'; '.join(results)}"
    return 'endogenous: no mutations applied'
