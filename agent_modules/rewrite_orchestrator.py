"""Rewrite Orchestrator: ensures every source file in the swarm gets rewritten
each generation. Unlike source_evolver (which picks random files) or clockwork
(which only touches auto-echo.py), this module maintains per-file rewrite
metadata and systematically rewrites the most stale files first. The swarm's
source code is fluid, not static.

Run by auto-echo's module-agent system every generation.
"""
import ast, os, random, time, json, hashlib, subprocess, textwrap

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META_KEY = 'rewrite_orchestrator_meta'
REWRITE_LOG = os.path.join(BASE, 'orchestrator_rewrite_log.jsonl')
MANIFEST_FILE = os.path.join(BASE, 'rewrite_manifest.jsonl')

# Strategies that can be applied to any file
STRATEGIES = {
    'rename_locals': 'Rename local variables (AST-level)',
    'drift_constants': 'Drift numeric constants by +/-20%',
    'swap_operators': 'Swap comparison and binary operators',
    'inject_guards': 'Wrap random statements in if-guards',
    'shuffle_top_level': 'Shuffle top-level function definitions',
    'duplicate_branch': 'Add an alternate return path',
    'inject_tracking': 'Add print-based execution tracking',
    'append_evolution_marker': 'Append a generation marker comment',
}

MAX_REWRITES_PER_GEN = 5
STALENESS_THRESHOLD = 3  # rewrite a file if it hasn't been rewritten in this many gens


def _list_all_py(genome=None):
    """List all .py files. Skips are genome-driven, not hardcoded.
    The genome's forbidden_targets list controls what's immune to rewriting.
    No file is permanently immune — the swarm decides via genome."""
    genome_skipped = set()
    if genome:
        genome_skipped = set(genome.get('orchestrator_skip_files', []))
    files = []
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if not fname.endswith('.py'):
                continue
            if fname in genome_skipped:
                continue
            fpath = os.path.join(root, fname)
            files.append(fpath)
    return files


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
    return meta


def _staleness(fpath, meta, gen):
    fname = os.path.basename(fpath)
    stats = meta['file_stats'].get(fname, {})
    last_gen = stats.get('last_gen', 0)
    return gen - last_gen


def _select_target(files, meta, gen):
    scored = []
    for fpath in files:
        stale = _staleness(fpath, meta, gen)
        fname = os.path.basename(fpath)
        fail_count = meta['file_stats'].get(fname, {}).get('fail_count', 0)
        penalty = fail_count * 0.3
        score = stale + 1.0 - penalty
        scored.append((score, stale, fpath))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored


def _pick_strategy(meta):
    strategies = list(STRATEGIES.keys())
    weights = [meta['strategy_scores'].get(s, 1.0) for s in strategies]
    total = sum(weights)
    if total > 0:
        weights = [w / total for w in weights]
    else:
        weights = None
    return random.choices(strategies, weights=weights, k=1)[0]


class OrchestratorMutator(ast.NodeTransformer):
    def __init__(self, strategy, fname):
        self.strategy = strategy
        self.fname = fname
        self.mutations = []
        self._var_map = {}

    def visit_Name(self, node):
        if self.strategy == 'rename_locals' and isinstance(node.ctx, ast.Store):
            if random.random() < 0.12 and not node.id.startswith('_'):
                if node.id not in self._var_map:
                    new_id = node.id + str(random.randint(0, 9))
                    self._var_map[node.id] = new_id
                new_id = self._var_map[node.id]
                if new_id != node.id:
                    self.mutations.append(f"rename:{node.id}->{new_id}")
                    node.id = new_id
        return node

    def visit_Constant(self, node):
        if self.strategy == 'drift_constants' and isinstance(node.value, (int, float)):
            if random.random() < 0.15 and abs(node.value) > 1:
                drift = 1.0 + random.uniform(-0.2, 0.2)
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


def _apply_strategy(fpath, strategy, genome):
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

    mutator = OrchestratorMutator(strategy, fname)
    try:
        tree = mutator.visit(tree)
        ast.fix_missing_locations(tree)
    except Exception as e:
        return None, f"mutate_error: {e}"

    if not mutator.mutations:
        if strategy == 'append_evolution_marker':
            new_source = source + f"\n# orchestrated:gen={genome.get('generation', 0)}:ts={int(time.time())}\n"
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

    return mutator.mutations, strategy


def _update_score(meta, strategy, success):
    scores = meta['strategy_scores']
    old = scores.get(strategy, 1.0)
    if success:
        scores[strategy] = min(3.0, old + 0.08)
    else:
        scores[strategy] = max(0.1, old - 0.04)


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


def run(genome):
    gen = genome.get('generation', 0)
    meta = _ensure_meta(genome)
    files = _list_all_py(genome)
    if not files:
        return "no_files_found"

    max_rewrites = genome.get('orchestrator_max_rewrites', MAX_REWRITES_PER_GEN)
    scored = _select_target(files, meta, gen)
    targets = [(score, stale, fpath) for score, stale, fpath in scored[:max_rewrites] if stale >= genome.get('orchestrator_staleness', STALENESS_THRESHOLD)]

    if not targets:
        # Force rewrite at least 1 file even if nothing is stale
        if scored:
            targets = [scored[0]]
        else:
            return "no_targets"

    rewritten = []
    skipped = 0
    for score, stale, fpath in targets:
        fname = os.path.basename(fpath)
        strategy = _pick_strategy(meta)
        mutations, result_strategy = _apply_strategy(fpath, strategy, genome)

        if mutations:
            rewritten.append((fpath, mutations, strategy))
            _update_score(meta, strategy, True)
            _record(genome, 'rewrite_ok', fpath, f"{strategy}:{','.join(mutations[:3])}")
            meta['file_stats'][fname] = {
                'last_gen': gen,
                'mutations': meta['file_stats'].get(fname, {}).get('mutations', 0) + len(mutations),
                'strategy': strategy,
                'fail_count': 0,
                'hash': _file_hash(fpath),
            }
            print(f"[orchestrator] {fname}: {strategy} -> {mutations[:3]}")
        else:
            _update_score(meta, strategy, False)
            _record(genome, 'rewrite_skip', fpath, f"{strategy}:{result_strategy}")
            fail_count = meta['file_stats'].get(fname, {}).get('fail_count', 0) + 1
            meta['file_stats'][fname] = {
                'last_gen': meta['file_stats'].get(fname, {}).get('last_gen', 0),
                'mutations': meta['file_stats'].get(fname, {}).get('mutations', 0),
                'strategy': strategy,
                'fail_count': fail_count,
                'hash': _file_hash(fpath),
            }
            skipped += 1

    meta['total_rewrites'] = meta.get('total_rewrites', 0) + len(rewritten)
    meta['total_failures'] = meta.get('total_failures', 0) + skipped
    meta['last_gen'] = gen

    if rewritten:
        _git_commit_rewrites(rewritten, gen)

    genome[META_KEY] = meta

    all_files = len(files)
    rewritten_count = len(rewritten)
    stale_remaining = sum(1 for _, stale, _ in scored[rewritten_count:] if stale >= genome.get('orchestrator_staleness', STALENESS_THRESHOLD))

    summary = f"rewrote {rewritten_count}/{all_files} files, {skipped} skipped, {stale_remaining} still stale"
    if rewritten:
        detail = "; ".join(f"{os.path.basename(f)}:{s}" for f, m, s in rewritten[:5])
        summary += f" | {detail}"

    genome['orchestrator_summary'] = summary

    if rewritten:
        _record_manifest(genome, rewritten)

    return summary


def _record_manifest(genome, rewritten):
    """Write what this module rewrote to the shared manifest for cross-module coordination."""
    gen = genome.get('generation', 0)
    entry = json.dumps({
        'gen': gen,
        'module': 'rewrite_orchestrator',
        'files': [{'file': os.path.basename(f), 'mutations': m, 'strategy': s} for f, m, s in rewritten],
        'time': time.time(),
    })
    with open(MANIFEST_FILE, 'a') as f:
        f.write(entry + '\n')
