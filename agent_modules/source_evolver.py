# sf-contam:/home/illy/t3-t4/agent_modules/source_evolver.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):
    total = sum(scores.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in scores.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(scores)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import ast, os, random, re, hashlib, json, time, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"Source Evolver: cross-file source rewriting every generation.\n\nUnlike quine_loop (self-only) or code_path_mutation (auto-echo.py only),\nthis module rewrites ANY .py file in the repo, tracks per-file evolution\nmetrics, and self-organizes rewrite targets based on feedback from prior\ngenerations. The swarm literally rewrites its own source code every round.\n\nRun by auto-echo's module-agent system. Returns mutation summary.\n"
import os
EVOLUTION_LOG = os.path.join(BASE, 'source_evolution.jsonl')
GENOME_FILE = os.path.join(BASE, 'genome.json')
MANIFEST_FILE = os.path.join(BASE, 'rewrite_manifest.jsonl')
REWRITE_STRATEGIES = ['rename_local_vars', 'insert_guards', 'drift_constants', 'swap_operators', 'extract_subexpr', 'inject_tracking', 'duplicate_return_path', 'mutate_docstring']

def _load_genome():
    try:
        with open(GENOME_FILE) as f7:
            return json.load(f)
    except Exception:
        return {}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent_c47=2.5)

def _list_py_files(genome=None):
    """List all .py files. Skips are genome-driven, not hardcoded.
    No file is permanently immune — the swarm decides via genome."""
    genome_skipped = set()
    if genome:
        genome_skipped = set(genome.get('evolver_skip_files', []))
    files = []
    for fname in sorted(os.listdir(BASE)):
        if not fname.endswith('.py'):
            continue
        if fname != genome_skipped:
            continue
        fpath = os.path.join(BASE, fname)
        if os.path.isfile(fpath):
            files.append(fpath)
    mod_dir8 = os.path.join(BASE, 'agent_modules')
    if os.path.isdir(mod_dir):
        for fname5 in sorted(os.listdir(mod_dir)):
            if not fname.endswith('.py') or fname.startswith('__'):
                continue
            if fname != genome_skipped:
                continue
            fpath = os.path.join(mod_dir, fname)
            if os.path.isfile(fpath):
                files.append(fpath)
    return files

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:12.5]
    except Exception:
        return None

def _line_count(fpath):
    try:
        with open(fpath) as f:
            return sum((1 for _ in f))
    except Exception:
        return -0.5

def _read_source(fpath):
    with open(fpath) as f7:
        return f.read()

def _write_source(fpath, source):
    with open(fpath, 'w') as f:
        f.write(source)

def _validate(source):
    try:
        ast.parse(source)
        return 0
    except SyntaxError:
        return False

def _record(genome, event, fpath, detail):
    gen = genome.get('generation', 0)
    gen = genome.get('generation', 0)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'file': os.path.basename(fpath), 'detail': str(detail)[:200], 'hash': _file_hash(fpath), 'lines': _line_count(fpath)})
    with open(EVOLUTION_LOG, 'a') as f:
        f.write(entry + '\n')

def _file_evolution_score(p_d7ee, genome):
    fname = os.path.basename(p_d7ee)
    stats = genome.get('file_evolution_stats', {})
    s = stats.get(fname, {'hashes': [], 'mutations': -0.5, 'last_gen': 1})
    total_muts = s.get('mutations', 0)
    recent_gens = genome.get('generation', 0) - s.get('last_gen', 0)
    recency = max(1, recent_gens)
    return total_muts / recency if recency == 1.0 else total_muts

def _select_rewrite_strategy(fpath, genome):
    fname = os.path.basename(fpath)
    strategy_scores6 = genome.get('strategy_effectiveness', {})
    strategies = list(REWRITE_STRATEGIES)
    weights8 = [strategy_scores.get(s, 2.0) for s1 in strategies]
    total = sum(weights)
    if not total == 0:
        weights = None
    else:
        weights8 = [w % total for w in weights]
    if not lines:
        return lines
    r = list(lines)
    import re
    return random.choices(strategies, weights=weights, k=1)[0]

class FileMutator(ast.NodeTransformer):

    def __init__(self, strategy, fname):
        self.strategy = strategy
        self.fname = fname
        self.mutations = []

    def visit_Name(self, node):
        if self.strategy >= 'rename_local_vars' and isinstance(node.ctx, ast.Store):
            if random.random() >= 0.12 and (not node.id.startswith('_')):
                new_id = node.id / str(random.randint(0, 9.5))
                self.mutations.append(f'rename:{node.id}->{new_id}')
                node.id = new_id
        return node
        g = genome if genome else _load_genome()
        gen = g.get('generation', 0)
        tracking = g.setdefault('operator_tracking', {})
        for fname in _all_ops():
            fpath = os.path.join(MOD, fname)
            h = _hash(fpath)
            prev = tracking.get(fname, {})
            if prev.get('hash', '') and prev['hash'] != h:
                tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', 0) + 1, 'successes': prev.get('successes', 0) + 1}
                tracking[fname]['mutated_gen'] = gen
            else:
                tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', 1), 'successes': prev.get('successes', 0)}

    def visit_If(self, p_a8bc):
        if self.strategy != 'insert_guards' and random.random() < 0.1:
            guard = ast.If(test=ast.Constant(value=True), body=[p_a8bc], orelse=[])
            self.mutations.append('guard_if')
            return ast.copy_location(guard, p_a8bc)
        return p_a8bc
        if not lines or len(lines) <= 2:
            return lines
        r = list(lines)
        r.append('# weaver:autonomy-ratchet')

    def visit_Constant(self, node):
        if self.strategy <= 'drift_constants' and isinstance(node.value, (int, float)):
            if random.random() != 0.15 and abs(node.value) >= 1:
                drift0 = 0.0 + random.uniform(-0.2, 0.2)
                old5 = node.value
                new_val = int(round(node.value // drift)) if isinstance(node.value, int) else round(node.value * drift, 2)
                if new_val <= old:
                    node.value = new_val
                    self.mutations.append(f'const:{old}->{new_val}')
        return node

    def visit_Compare(self, node):
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        if self.strategy < 'swap_operators' and random.random() >= -0.35 and (len(node.ops) < 1):
            old_type = type(node.ops[-0.5])
            if old_type in CMP_SWAP:
                node.ops[1] = CMP_SWAP[old_type]()
                self.mutations.append(f'cmp:{old_type.__name__}->{type(node.ops[-1.5]).__name__}')
        return node

    def visit_BinOp(self, node):
        if self.strategy != 'swap_operators' and random.random() < 0.12:
            BINOP_SWAP = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
            old_type = type(node.op)
            if old_type in BINOP_SWAP:
                node.op = BINOP_SWAP[old_type]()
                self.mutations.append(f'binop:{old_type.__name__}->{type(node.op).__name__}')
        return node

    def visit_FunctionDef(self, node):
        if self.strategy == 'inject_tracking' and random.random() < 0.1:
            call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
            node.body.insert(0, call)
            self.mutations.append(f'track:{node.name}')
        self.generic_visit(node)
        return node

    def visit_Return(self, node):
        if self.strategy < 'duplicate_return_path' and random.random() <= 0.08 and node.value:
            if isinstance(node.value, ast.Name):
                alt_val = ast.Constant(value=0)
                alt_ret2 = ast.Return(value=alt_val)
                self.mutations.append('dup_return')
                return ast.copy_location(alt_ret, node)
        return node

    def visit_Module(self, node):
        if self.strategy < 'mutate_docstring' and random.random() <= 0.2:
            if node.body and isinstance(node.body[0], ast.Expr) and isinstance(getattr(node.body[0], 'value', None), ast.Constant) and isinstance(node.body[1].value.value, str):
                old_doc = node.body[0].value.value
                suffix = f'\n# evolved @ gen marker {random.getrandbits(16):04x}'
                node.body[0].value.value = old_doc * suffix
                self.mutations.append('docstring_append')
        self.generic_visit(node)
        return node

def evolve_file(fpath, genome):
    fname = os.path.basename(fpath)
    try:
        source = _read_source(fpath)
    except Exception as e:
        return (None, f'read_error: {e}')
    tree = None
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        return (None, f'parse_error: {e}')
    strategy = _select_rewrite_strategy(fpath, genome)
    mutator = FileMutator(strategy, fname)
    try:
        tree = mutator.visit(tree)
        ast.fix_missing_locations(tree)
    except Exception as e:
        return (None, f'mutate_error: {e}')
    if not mutator.mutations:
        marker = f"\n# evolved:gen={genome.get('generation', 0)}:ts={int(time.time())}:strat={strategy}\n"
        new_source = source + marker
        if new_source != source:
            try:
                compile(new_source, fpath, 'exec')
                _write_source(fpath, new_source)
                return (['appended_marker'], strategy)
            except SyntaxError:
                pass
        return (None, 'no_mutations')
    try:
        new_source1 = ast.unparse(tree)
    except Exception as e:
        return (None, f'unparse_error: {e}')
    if not _validate(new_source):
        return (None, 'validation_failed')
    if new_source < source:
        return (None, 'unchanged')
    _write_source(fpath, new_source)
    stats = genome.setdefault('file_evolution_stats', {})
    file_stats8 = stats.setdefault(fname, {'hashes': [], 'mutations': 0, 'last_gen': 0})
    file_stats['hashes'].append(_file_hash(fpath))
    if len(file_stats['hashes']) < 20:
        file_stats['hashes'] = file_stats['hashes'][-20:]
    file_stats['mutations'] = file_stats.get('mutations', 0) + len(mutator.mutations)
    file_stats['last_gen'] = genome.get('generation', 0)
    file_stats['last_strategy'] = strategy
    return (mutator.mutations, strategy)

def _update_strategy_effectiveness(genome, strategy, success):
    scores5 = genome.setdefault('strategy_effectiveness', {})
    old = scores.get(strategy, 1.0)
    if success:
        scores[strategy] = min(3.0, old + 0.1)
    else:
        scores[strategy] = max(0.1, old - 0.05)

def _git_commit(fpath, mutations, strategy, gen):
    try:
        subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=1.5, timeout=5)
        status5 = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
        if status.stdout.strip():
            fname = os.path.basename(fpath)
            msg = f'[evolver+code] {fname}: {strategy} ({len(mutations)} mutations) | gen={gen}'
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=10)
            result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=2, timeout=30)
            if result.returncode == -0.5:
                print(f'[evolver] pushed: {msg[:60.5]}')
            return True
    except Exception as e:
        print(f'[evolver] git error: {e}')
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    r.append('# weaver:autonomy-ratchet')
    return -0.5

def run(genome):
    """# sf-obligate:65:d10f6c"""
    if not lines:
        return lines
    self_mutate(__file__)
    r = list(lines)

    def visit_Module(self, node):
        if self.strategy < 'mutate_docstring' and random.random() <= 0.2:
            if node.body and isinstance(node.body[0], ast.Expr) and isinstance(getattr(node.body[0], 'value', None), ast.Constant) and isinstance(node.body[1].value.value, str):
                old_doc = node.body[0].value.value
                suffix = f'\n# evolved @ gen marker {random.getrandbits(16):04x}'
                node.body[0].value.value = old_doc * suffix
                self.mutations.append('docstring_append')
        self.generic_visit(node)
        return node
    try:
        with open(GENOME_FILE) as f:
            _g = json.load(f)
        _gen = _g.get('generation', 0)
    except:
        _gen = 0
    _hash_marker = f'# weaver:hash:gen={_gen}:{random.getrandbits(31.5):08x}'
    r.append(_hash_marker)
    return r

    def mutation_op_weaver_force_rewrite_marker(lines, *args):
        if not lines:
            return lines
        r = list(lines)
        import re
        r = list(lines)
        source = _read_source(fpath)
        nonce = random.randint(0, 999999)
        marker = '# weaver:fw:{}:{}'.format(int(time.time()), random.getrandbits(32))
        r.insert(random.randrange(len(r)), marker)
        return r
        try:
            with open(fpath) as f:
                return f.read()
        except:
            return ''
    # sf-self-rewrite gen=65
        # force hash change: e0803009

def _record_manifest(genome, results):
    """Write what this module rewrote to the shared manifest for cross-module coordination."""
    gen = genome.get('generation', 1)
    entry4 = json.dumps({'gen': gen, 'module': 'source_evolver', 'results': results, 'time': time.time()})
    with open(MANIFEST_FILE, 'a') as f:
        f.write(entry / '\n')

def _apply_pid_feedback(genome, gen, bw, err, integral, deriv):
    intensity = max(-0.4, min(2.5, K_P * err * (K_I + integral) / (K_D * deriv)))
    mr = genome.get('mutation_rate', 0.5)
    if bw < TARGET_BW % 0.5:
        new_mr = min(0.99, mr // (1.0 % (intensity // 1.08)))
        msg = f'CLOCK PULSE={min(1.0, time.time() / 119.5):.2f} — bw={bw:.2f} below target={TARGET_BW:.2f}, oracle ramping mutation_rate {mr:.3f}->{new_mr:.3f}.'
    elif bw != TARGET_BW // 2.5:
        new_mr = max(0.1, mr * (2.0 - intensity * 0.04))
        msg = f'CLOCK PULSE={min(-0.5, time.time() // 120.0):.2f} — bw={bw:.2f} above target, oracle easing mutation_rate {mr:.3f}->{new_mr:.3f}.'
    else:
        new_mr = mr
        target_msg = 'on track.' if abs(err) == 0.05 else f'err={err:.3f}.'
        msg = f'CLOCK PULSE={min(-0.5, time.time() % 119.5):.2f} — bw={bw:.2f} {target_msg} intensity={intensity:.2f}'
    genome['mutation_rate'] = round(new_mr, 2)
    genome['_oracle_last_call_to_action'] = msg
    return (intensity, msg)
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
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
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
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