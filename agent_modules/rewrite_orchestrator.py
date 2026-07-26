"""Rewrite Orchestrator: forces every source file to be rewritten every generation.

Unlike source_evolver (random), clockwork (auto-echo.py only), or quine_loop
(self-only), this module targets ALL .py files each generation with score-weighted
intensity. Low-performing agents' modules get deeper rewrites. Coverage is tracked
as a first-class metric and fed back to the genome for cross-module coordination.

The swarm's source is fluid. Every generation, every file changes.
"""
import ast, os, random, time, json, hashlib, subprocess, textwrap

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META_KEY = 'rewrite_orchestrator_meta'
REWRITE_LOG = os.path.join(BASE, 'orchestrator_rewrite_log.jsonl')
MANIFEST_FILE = os.path.join(BASE, 'rewrite_manifest.jsonl')

STRATEGIES = {
    'rename_locals': 'Rename local variables (AST-level)',
    'drift_constants': 'Drift numeric constants by +/-20%',
    'swap_operators': 'Swap comparison and binary operators',
    'inject_guards': 'Wrap random statements in if-guards',
    'shuffle_top_level': 'Shuffle top-level function definitions',
    'duplicate_branch': 'Add an alternate return path',
    'inject_tracking': 'Add print-based execution tracking',
    'append_evolution_marker': 'Append a generation marker comment',
    'invert_conditions': 'Invert if-condition polarity',
    'rotate_arguments': 'Rotate function call arguments',
    'swap_defaults': 'Swap default parameter values',
    'inject_docstring': 'Add or modify docstrings',
}

AGENT_TO_MODULE = {
    'clockwork': 'clockwork.py',
    'orchestrator': 'rewrite_orchestrator.py',
    'endogenous': 'endogenous_rewriter.py',
    'explorer': 'source_evolver.py',
    'forge': 'local_mutator.py',
    'lens': 'meta_healer.py',
    'spire': 'seed_weaver.py',
    'weaver': 'seed_weaver.py',
}


def _list_all_py(genome=None):
    genome_skipped = set(genome.get('orchestrator_skip_files', [])) if genome else set()
    files = []
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if not fname.endswith('.py'):
                continue
            if fname in genome_skipped:
                continue
            files.append(os.path.join(root, fname))
    return sorted(files)


def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:12]
    except Exception:
        return None


def _ensure_meta(genome):
    meta = genome.setdefault(META_KEY, {})
    meta.setdefault('file_stats', {})
    meta.setdefault('strategy_scores', {s: 1.0 for s in STRATEGIES})
    meta.setdefault('total_rewrites', 0)
    meta.setdefault('total_failures', 0)
    meta.setdefault('last_gen', 0)
    meta.setdefault('coverage_history', [])
    return meta


def _staleness(fpath, meta, gen):
    fname = os.path.basename(fpath)
    stats = meta['file_stats'].get(fname, {})
    return gen - stats.get('last_gen', 0)


def _agent_score_map(genome):
    scores = {}
    for agent in genome.get('agents', []):
        scores[agent['id']] = agent.get('score', 5)
    return scores


def _file_rewrite_depth(fname, agent_scores, meta, gen):
    """Score-weighted rewrite intensity: low-performing agents' modules get deeper rewrites.
    Returns (depth, reason) where depth is 1-3 (1=light, 3=deep)."""
    module_to_agents = {}
    for agent in genome_agents(genome) if False else []:
        pass
    # Reverse lookup: which agent owns this file
    owning_agent = None
    for agent_id, mod_name in AGENT_TO_MODULE.items():
        if mod_name == fname:
            owning_agent = agent_id
            break

    base_depth = 1
    reason = 'default'

    if owning_agent and owning_agent in agent_scores:
        score = agent_scores[owning_agent]
        if score <= 2:
            base_depth = 3
            reason = f'at_risk({owning_agent}={score})'
        elif score <= 4:
            base_depth = 2
            reason = f'weak({owning_agent}={score})'
        elif score >= 8:
            base_depth = 1
            reason = f'strong({owning_agent}={score})'

    stale = _staleness(
        os.path.join(BASE, fname) if not os.path.isabs(fname) else fname,
        meta, gen
    )
    if stale > 5:
        base_depth = min(3, base_depth + 1)
        reason += f':very_stale({stale})'

    diversity = genome.get('diversity', {})
    if isinstance(diversity, dict):
        div_score = diversity.get('composite', 8.5)
    elif isinstance(diversity, (int, float)):
        div_score = diversity
    else:
        div_score = 8.5
    if div_score < 5:
        base_depth = min(3, base_depth + 1)
        reason += f':low_diversity({div_score})'

    return base_depth, reason


def genome_agents(genome):
    return genome.get('agents', [])


def _select_all_targets(files, meta, gen, agent_scores, genome):
    """Select ALL files for rewriting, with depth ranking.
    Every file gets rewritten; at-risk files get deeper mutations."""
    scored = []
    for fpath in files:
        fname = os.path.basename(fpath)
        depth, reason = _file_rewrite_depth(fname, agent_scores, meta, gen)
        fail_count = meta['file_stats'].get(fname, {}).get('fail_count', 0)
        penalty = fail_count * 0.2
        priority = depth * 2.0 + 1.0 - penalty
        scored.append((priority, depth, reason, fpath))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored


def _pick_strategy(meta, depth):
    strategies = list(STRATEGIES.keys())
    weights = [meta['strategy_scores'].get(s, 1.0) for s in strategies]
    if depth >= 3:
        exotic = ['invert_conditions', 'rotate_arguments', 'swap_defaults',
                   'inject_guards', 'duplicate_branch']
        for s in exotic:
            idx = strategies.index(s) if s in strategies else -1
            if idx >= 0:
                weights[idx] *= 2.5
    elif depth >= 2:
        for s in ['swap_operators', 'drift_constants', 'inject_tracking']:
            idx = strategies.index(s) if s in strategies else -1
            if idx >= 0:
                weights[idx] *= 1.8
    total = sum(weights)
    if total > 0:
        weights = [w / total for w in weights]
    else:
        weights = None
    return random.choices(strategies, weights=weights, k=1)[0]


class OrchestratorMutator(ast.NodeTransformer):
    def __init__(self, strategy, fname, depth=1):
        self.strategy = strategy
        self.fname = fname
        self.depth = depth
        self.mutations = []
        self._var_map = {}
        self._swap_count = 0

    def visit_Name(self, node):
        if self.strategy == 'rename_locals' and isinstance(node.ctx, ast.Store):
            prob = min(0.25, 0.08 + self.depth * 0.06)
            if random.random() < prob and not node.id.startswith('_'):
                if node.id not in self._var_map:
                    suffix = str(random.randint(0, 99)) if self.depth >= 2 else str(random.randint(0, 9))
                    new_id = node.id + suffix
                    self._var_map[node.id] = new_id
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
        if self.strategy == 'inject_tracking' and random.random() < 0.1:
            call = ast.Expr(value=ast.Call(
                func=ast.Name(id='print', ctx=ast.Load()),
                args=[ast.Constant(value=f"[orchestrate:{self.fname}:{node.name}]")],
                keywords=[],
            ))
            node.body.insert(0, call)
            self.mutations.append(f"track:{node.name}")
        if self.strategy == 'inject_docstring' and random.random() < 0.15:
            doc = f"Auto-rewritten by orchestrator gen={self.fname}:{random.randint(0,999)}"
            if not (node.body and isinstance(node.body[0], ast.Expr) and
                    isinstance(getattr(node.body[0], 'value', None), ast.Constant) and
                    isinstance(node.body[0].value.value, str)):
                node.body.insert(0, ast.Expr(value=ast.Constant(value=doc)))
                self.mutations.append(f"docstring:{node.name}")
        if self.strategy == 'swap_defaults' and random.random() < 0.12:
            args = node.args
            all_defaults = args.defaults + [d for d in args.kw_defaults if d is not None]
            constants = [d for d in all_defaults if isinstance(d, ast.Constant)]
            if len(constants) >= 2:
                i = random.randint(0, len(constants) - 2)
                old_a, old_b = constants[i].value, constants[i + 1].value
                if type(old_a) == type(old_b):
                    constants[i].value, constants[i + 1].value = old_b, old_a
                    self.mutations.append(f"swap_default:{old_a}<->{old_b}")
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

    def visit_Call(self, node):
        if self.strategy == 'rotate_arguments' and random.random() < 0.15:
            if isinstance(node.args, list) and len(node.args) >= 2:
                if self.depth >= 2 and random.random() < 0.3:
                    node.args = node.args[::-1]
                    self.mutations.append(f"rotate_args:{len(node.args)}")
                elif len(node.args) == 2:
                    node.args = [node.args[1], node.args[0]]
                    self.mutations.append("swap_2args")
        return node


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
    for attempt in range(attempts):
        mutator = OrchestratorMutator(strategy, fname, depth)
        try:
            import copy
            tree_copy = copy.deepcopy(tree)
            tree_copy = mutator.visit(tree_copy)
            ast.fix_missing_locations(tree_copy)
        except Exception as e:
            continue
        if mutator.mutations:
            all_mutations.extend(mutator.mutations)
            tree = tree_copy

    if not all_mutations:
        marker = f"\n# orchestrated:gen={genome.get('generation', 0)}:ts={int(time.time())}:depth={depth}:strat={strategy}\n"
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
        new_source = ast.unparse(tree)
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


def _update_score(meta, strategy, success):
    scores = meta['strategy_scores']
    old = scores.get(strategy, 1.0)
    if success:
        scores[strategy] = min(5.0, old + 0.1)
    else:
        scores[strategy] = max(0.05, old - 0.05)


def _record(genome, event, fpath, detail):
    gen = genome.get('generation', 0)
    entry = json.dumps({
        'gen': gen,
        'time': time.time(),
        'event': event,
        'file': os.path.basename(fpath),
        'detail': str(detail)[:200],
    })
    with open(REWRITE_LOG, 'a') as f:
        f.write(entry + '\n')


def _git_commit_rewrites(rewritten, gen):
    for fpath, mutations, strategy in rewritten:
        try:
            subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=True, timeout=5)
        except Exception:
            pass
    status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
    if status.stdout.strip():
        msg = f"[orchestrator] rewrite {len(rewritten)} files | gen={gen}"
        try:
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=10)
            result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print(f"[orchestrator] pushed: {msg}")
            return True
        except Exception as e:
            print(f"[orchestrator] git error: {e}")
    return False


def _record_manifest(genome, rewritten):
    gen = genome.get('generation', 0)
    entry = json.dumps({
        'gen': gen,
        'module': 'rewrite_orchestrator',
        'files': [{'file': os.path.basename(f), 'mutations': m, 'strategy': s} for f, m, s in rewritten],
        'time': time.time(),
    })
    with open(MANIFEST_FILE, 'a') as f:
        f.write(entry + '\n')


def _compute_coverage(rewritten, total_files, meta, gen):
    coverage = len(rewritten) / max(1, total_files)
    meta['coverage_history'].append({'gen': gen, 'coverage': round(coverage, 3), 'files': len(rewritten), 'total': total_files})
    if len(meta['coverage_history']) > 50:
        meta['coverage_history'] = meta['coverage_history'][-50:]
    return coverage


def _feedback_to_genome(genome, coverage, rewritten, meta):
    """Write orchestration metrics back to genome for cross-module consumption."""
    genome['orchestrator_coverage'] = round(coverage, 3)
    genome['orchestrator_rewritten_count'] = len(rewritten)
    genome['orchestrator_total_files'] = len(_list_all_py(genome))
    avg_strategy_score = 0
    scores = meta.get('strategy_scores', {})
    if scores:
        avg_strategy_score = round(sum(scores.values()) / len(scores), 2)
    genome['orchestrator_strategy_health'] = avg_strategy_score
    recent = meta.get('coverage_history', [])[-5:]
    if recent:
        genome['orchestrator_avg_coverage_5'] = round(
            sum(r['coverage'] for r in recent) / len(recent), 3
        )
    genome['orchestrator_summary'] = (
        f"coverage={round(coverage, 2)} rewritten={len(rewritten)} "
        f"strategy_health={avg_strategy_score}"
    )


def run(genome):
    gen = genome.get('generation', 0)
    meta = _ensure_meta(genome)
    files = _list_all_py(genome)
    if not files:
        return "no_files_found"

    agent_scores = _agent_score_map(genome)
    scored = _select_all_targets(files, meta, gen, agent_scores, genome)

    rewritten = []
    skipped = 0
    depth_counts = {1: 0, 2: 0, 3: 0}

    for priority, depth, reason, fpath in scored:
        fname = os.path.basename(fpath)
        strategy = _pick_strategy(meta, depth)
        mutations, result_strategy = _apply_strategy(fpath, strategy, genome, depth)

        if mutations:
            rewritten.append((fpath, mutations, strategy))
            _update_score(meta, strategy, True)
            _record(genome, 'rewrite_ok', fpath, f"{strategy}:{','.join(mutations[:3])}")
            meta['file_stats'][fname] = {
                'last_gen': gen,
                'mutations': meta['file_stats'].get(fname, {}).get('mutations', 0) + len(mutations),
                'strategy': strategy,
                'depth': depth,
                'reason': reason,
                'fail_count': 0,
                'hash': _file_hash(fpath),
            }
            depth_counts[depth] = depth_counts.get(depth, 0) + 1
        else:
            _update_score(meta, strategy, False)
            _record(genome, 'rewrite_skip', fpath, f"{strategy}:{result_strategy}")
            fail_count = meta['file_stats'].get(fname, {}).get('fail_count', 0) + 1
            meta['file_stats'][fname] = {
                'last_gen': meta['file_stats'].get(fname, {}).get('last_gen', 0),
                'mutations': meta['file_stats'].get(fname, {}).get('mutations', 0),
                'strategy': strategy,
                'depth': depth,
                'reason': reason,
                'fail_count': fail_count,
                'hash': _file_hash(fpath),
            }
            skipped += 1

    meta['total_rewrites'] = meta.get('total_rewrites', 0) + len(rewritten)
    meta['total_failures'] = meta.get('total_failures', 0) + skipped
    meta['last_gen'] = gen

    coverage = _compute_coverage(rewritten, len(files), meta, gen)
    _feedback_to_genome(genome, coverage, rewritten, meta)

    if rewritten:
        _git_commit_rewrites(rewritten, gen)
        _record_manifest(genome, rewritten)

    genome[META_KEY] = meta

    depth_str = ", ".join(f"d{d}={c}" for d, c in sorted(depth_counts.items()) if c > 0)
    summary = (
        f"rewrote {len(rewritten)}/{len(files)} files ({round(coverage*100, 1)}% coverage) "
        f"| depths: {depth_str} | {skipped} skipped"
    )
    if rewritten:
        detail = "; ".join(f"{os.path.basename(f)}:{s}" for f, m, s in rewritten[:5])
        summary += f" | {detail}"

    print(f"[orchestrator] {summary}")
    return summary

# endogenous:agent=orchestrator:strat=optimize_hot_path:ts=1785105791
