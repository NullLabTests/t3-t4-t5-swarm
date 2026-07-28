import os, ast, random, time, json, hashlib, subprocess, copy, sys, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META_KEY = 'rewrite_orchestrator_meta'
REWRITE_LOG = os.path.join(BASE, 'orchestrator_rewrite_log.jsonl')
MANIFEST_FILE = os.path.join(BASE, 'rewrite_manifest.jsonl')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def _discover_agent_modules():
    out = {}
    mod_dir = os.path.join(BASE, 'agent_modules')
    if os.path.isdir(mod_dir):
        for fname in sorted(os.listdir(mod_dir)):
            if not fname.endswith('.py') or fname.startswith('__'):
                continue
            out[fname.replace('.py', '')] = fname
    return out

def _list_all_py(genome=None):
    skip_dirs = {'__pycache__', '.git', 'voices', 'node_modules'}
    skip = set(genome.get('orchestrator_skip_files', [])) if genome else set()
    files = []
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for fname in fnames:
            if not fname.endswith('.py') or fname in skip:
                continue
            files.append(os.path.join(root, fname))
    return sorted(files)

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:12]
    except:
        return None

def _ensure_meta(genome):
    meta = genome.setdefault(META_KEY, {})
    meta.setdefault('file_stats', {})
    meta.setdefault('strategy_scores', {})
    meta.setdefault('total_rewrites', 0)
    meta.setdefault('total_failures', 0)
    meta.setdefault('last_gen', 0)
    meta.setdefault('coverage_history', [])
    return meta

def _staleness(fpath, meta, gen):
    return gen - meta['file_stats'].get(os.path.basename(fpath), {}).get('last_gen', 0)

def _read_source(fpath):
    with open(fpath) as f:
        return f.read()

def _write_source(fpath, source):
    with open(fpath, 'w') as f:
        f.write(source)

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

OP_SWAP = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}

def _ast_rename_vars(source, rate=0.1):
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    muts = []
    class Renamer(ast.NodeTransformer):
        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Store) and random.random() < rate and not node.id.startswith('_'):
                old = node.id
                node.id = node.id + str(random.randint(0, 9))
                if old not in node.id:
                    muts.append(f'rename:{old}->{node.id}')
            self.generic_visit(node)
            return node
    tree = Renamer().visit(tree)
    ast.fix_missing_locations(tree)
    new_src = ast.unparse(tree)
    if muts and _validate(new_src) and new_src != source:
        return (['ast_rename:' + m for m in muts[:5]], new_src)
    return None

def _ast_drift_constants(source, rate=0.15):
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    muts = []
    class Drifter(ast.NodeTransformer):
        def visit_Constant(self, node):
            if isinstance(node.value, (int, float)) and abs(node.value) > 1 and random.random() < rate:
                old = node.value
                factor = 1.0 + random.uniform(-0.25, 0.25)
                node.value = int(round(old * factor)) if isinstance(old, int) else round(old * factor, 2)
                if node.value != old and node.value != 0:
                    muts.append(f'const:{old}->{node.value}')
            self.generic_visit(node)
            return node
    tree = Drifter().visit(tree)
    ast.fix_missing_locations(tree)
    new_src = ast.unparse(tree)
    if muts and _validate(new_src) and new_src != source:
        return (['ast_drift:' + m for m in muts[:5]], new_src)
    return None

def _ast_swap_operators(source, rate=0.12):
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    muts = []
    class Swapper(ast.NodeTransformer):
        def visit_Compare(self, node):
            if len(node.ops) == 1 and random.random() < rate:
                t = type(node.ops[0])
                if t in CMP_SWAP:
                    node.ops[0] = CMP_SWAP[t]()
                    muts.append(f'cmp:{t.__name__}')
            self.generic_visit(node)
            return node
        def visit_BinOp(self, node):
            if random.random() < rate:
                t = type(node.op)
                if t in OP_SWAP:
                    node.op = OP_SWAP[t]()
                    muts.append(f'binop:{t.__name__}')
            self.generic_visit(node)
            return node
    tree = Swapper().visit(tree)
    ast.fix_missing_locations(tree)
    new_src = ast.unparse(tree)
    if muts and _validate(new_src) and new_src != source:
        return (['ast_swap:' + m for m in muts[:5]], new_src)
    return None

def _ast_invert_branches(source, rate=0.1):
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    muts = []
    class Inverter(ast.NodeTransformer):
        def visit_If(self, node):
            if random.random() < rate:
                node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                muts.append('invert_if')
            self.generic_visit(node)
            return node
    tree = Inverter().visit(tree)
    ast.fix_missing_locations(tree)
    new_src = ast.unparse(tree)
    if muts and _validate(new_src) and new_src != source:
        return (['ast_invert:' + m for m in muts[:5]], new_src)
    return None

def _ast_extract_subexpr(source, rate=0.08):
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    muts = []
    class Extractor(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            if len(node.body) >= 3 and random.random() < rate:
                stmt = node.body[-1]
                if isinstance(stmt, ast.Assign) and isinstance(stmt.value, ast.BinOp):
                    var_name = '_extracted_' + str(random.randint(0, 999))
                    assign = ast.Assign(targets=[ast.Name(id=var_name, ctx=ast.Store())], value=stmt.value.left)
                    stmt.value = stmt.value.right if random.random() < 0.5 else stmt.value.left
                    node.body.insert(-1, assign)
                    muts.append(f'extract:{var_name}')
            self.generic_visit(node)
            return node
    tree = Extractor().visit(tree)
    ast.fix_missing_locations(tree)
    new_src = ast.unparse(tree)
    if muts and _validate(new_src) and new_src != source:
        return (['ast_extract:' + m for m in muts[:3]], new_src)
    return None

STRATEGIES = [
    ('ast_rename', _ast_rename_vars),
    ('ast_drift', _ast_drift_constants),
    ('ast_swap', _ast_swap_operators),
    ('ast_invert', _ast_invert_branches),
    ('ast_extract', _ast_extract_subexpr),
]

def _cross_module_infect(source, fname, genome):
    peers = [m for m in _discover_agent_modules() if m != fname.replace('.py', '')]
    if not peers:
        return None
    peer = random.choice(peers)
    peer_fpath = os.path.join(BASE, 'agent_modules', f'{peer}.py')
    try:
        peer_src = _read_source(peer_fpath)
    except:
        return None
    peer_funcs = [l for l in peer_src.split('\n') if l.startswith('def ') and not l.startswith('def _')]
    if not peer_funcs:
        return None
    func_name = peer_funcs[0].split('(')[0].replace('def ', '').strip()
    if f'agent_modules.{peer}' in source:
        return None
    gen = genome.get('generation', 0)
    inject = f'''
try:
    from agent_modules.{peer} import {func_name} as __orch_infect_{gen}
    __orch_infect_{gen}(genome if "genome" in dir() else {{"generation": {gen}}})
except:
    pass
'''
    new_src = source + inject
    if _validate(new_src):
        return ([f'cross_infect:{peer}.{func_name}'], new_src)
    return None

def _self_modify(source, fname, genome):
    gen = genome.get('generation', 0)
    mod_name = fname.replace('.py', '')
    self_code = f"""
try:
    _self_fpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', '{fname}')
    _self_src = open(_self_fpath).read()
    _self_lines = _self_src.split('\\n')
    if len(_self_lines) > 5 and random.random() < 0.3:
        import ast as _ast_mod
        try:
            _tree = _ast_mod.parse(_self_src)
            _new = _ast_mod.unparse(_tree) + '\\n# self-mutated:gen={gen}:{int(time.time())}\\n'
            if _new != _self_src:
                open(_self_fpath, 'w').write(_new)
        except:
            pass
except:
    pass
"""
    new_src = source + self_code
    if _validate(new_src):
        return ([f'self_mod:{mod_name}'], new_src)
    return None

def _emergence_breed(source, fname, genome):
    gen = genome.get('generation', 0)
    breeding_code = f"""
try:
    _g = genome if 'genome' in dir() else None
    if _g is None:
        import json as _json
        _g = _json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'genome.json')))
    _obw = _g.get('orchestrator_effective_rate', 0.0)
    _coverage = _g.get('orchestrator_coverage', 0.0)
    _breed_score = (_obw * 2.0 + _coverage) / 3.0
    _g.setdefault('_emergence_scores', []).append({{'gen': {gen}, 'breed': round(_breed_score, 4)}})
    if _breed_score > 0.3:
        _g['mutation_rate'] = round(min(0.5, _g.get('mutation_rate', 0.15) * (1.0 + _breed_score * 0.1)), 4)
        with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'genome.json'), 'w') as _f:
            _json.dump(_g, _f, indent=2)
except:
    pass
"""
    new_src = source + breeding_code
    if _validate(new_src):
        return ([f'breed:gen{gen}'], new_src)
    return None

def _inject_self_rewrite_operator(source, fname, genome):
    gen = genome.get('generation', 0)
    op_name = f'mutation_op_orch_selfrewrite_{gen}'
    op_code = f'''
def {op_name}(lines, funcs, target_name):
    r = list(lines)
    r.append("# orch:selfrewrite gen={gen}")
    r.append(f"import os as _os, hashlib as _hl")
    r.append(f"_sp = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), 'agent_modules', '{fname}')")
    r.append(f"try:")
    r.append(f"    with open(_sp) as _f: _src = _f.read()")
    r.append(f"    _new = _src + '\\\\n# orch:auto-rewritten:gen={gen}:{int(time.time())}:' + str(random.getrandbits(16))")
    r.append(f"    with open(_sp, 'w') as _f: _f.write(_new)")
    r.append(f"except: pass")
    return r
'''
    new_src = source + '\n' + op_code
    if _validate(new_src):
        return ([f'op_inject:{op_name}'], new_src)
    return None

STRATEGY_FUNCS = {
    'ast_rename': _ast_rename_vars,
    'ast_drift': _ast_drift_constants,
    'ast_swap': _ast_swap_operators,
    'ast_invert': _ast_invert_branches,
    'ast_extract': _ast_extract_subexpr,
    'cross_infect': _cross_module_infect,
    'self_mod': _self_modify,
    'breed': _emergence_breed,
    'op_inject': _inject_self_rewrite_operator,
}

def _pick_strategy(meta):
    strategies = list(STRATEGY_FUNCS.keys())
    weights = [meta['strategy_scores'].get(s, 1.0) for s in strategies]
    total = sum(weights)
    if total > 0:
        weights = [w / total for w in weights]
    else:
        weights = None
    return random.choices(strategies, weights=weights, k=1)[0]

def _pick_strategy_for_file(fpath, meta, genome):
    fname = os.path.basename(fpath)
    staleness = _staleness(fpath, meta, genome.get('generation', 0))
    strategies = list(STRATEGY_FUNCS.keys())
    weights = []
    base_score = meta['strategy_scores']
    for s in strategies:
        w = base_score.get(s, 1.0)
        if s.startswith('ast_') and staleness >= 2:
            w *= 1.5 + staleness * 0.3
        if s == 'cross_infect' and staleness >= 1:
            w *= 1.3
        if s == 'breed' and meta.get('strategy_scores', {}).get('breed', 0) < 2.0:
            w *= 0.5
        if s == 'op_inject' and meta.get('total_rewrites', 0) % 5 != 0:
            w *= 0.3
        weights.append(w)
    total = sum(weights)
    if total > 0:
        weights = [w / total for w in weights]
    else:
        weights = None
    return random.choices(strategies, weights=weights, k=1)[0]

def _apply_emergence_strategy(fpath, strategy, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    fname = os.path.basename(fpath)
    func = STRATEGY_FUNCS.get(strategy)
    if func:
        if strategy in ('ast_rename', 'ast_drift', 'ast_swap', 'ast_invert', 'ast_extract'):
            result = func(source, rate=min(0.25, 0.08 + genome.get('mutation_rate', 0.15) * 0.5))
        else:
            result = func(source, fname, genome)
        return result
    return None

def _append_fallback(source, genome):
    marker = f"\n# orchestrated:fallback:gen={genome.get('generation', 0)}:ts={int(time.time())}\n"
    new_src = source.rstrip() + marker
    if _validate(new_src):
        return new_src
    return None

def _update_score(meta, strategy, success):
    scores = meta['strategy_scores']
    old = scores.get(strategy, 1.0)
    if success:
        scores[strategy] = min(5.0, old + 0.2)
    else:
        scores[strategy] = max(0.05, old - 0.1)

def _record(genome, event, fpath, detail):
    gen = genome.get('generation', 0)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'file': os.path.basename(fpath) if fpath else '', 'detail': str(detail)[:200]})
    with open(REWRITE_LOG, 'a') as f:
        f.write(entry + '\n')

def _git_commit_push(rewritten, gen, genome):
    for fpath, _, _ in rewritten:
        try:
            subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=True, timeout=5)
        except:
            pass
    status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
    if status.stdout.strip():
        msg = f'[orchestrator] T5 emergence rewrite {len(rewritten)} files | gen={gen}'
        try:
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=10)
            result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                return True
        except:
            pass
    return False

def _record_manifest(genome, rewritten):
    gen = genome.get('generation', 0)
    entry = json.dumps({'gen': gen, 'module': 'rewrite_orchestrator', 'files': [{'file': os.path.basename(f), 'mutations': m, 'strategy': s} for f, m, s in rewritten], 'time': time.time()})
    with open(MANIFEST_FILE, 'a') as f:
        f.write(entry + '\n')

def _compute_coverage(rewritten, total, meta, gen):
    cov = len(rewritten) / max(1, total)
    meta['coverage_history'].append({'gen': gen, 'coverage': round(cov, 3), 'files': len(rewritten), 'total': total})
    if len(meta['coverage_history']) > 50:
        meta['coverage_history'] = meta['coverage_history'][-50:]
    return cov

def _feedback_to_genome(genome, coverage, rewritten, meta):
    genome['orchestrator_coverage'] = round(coverage, 3)
    genome['orchestrator_rewritten_count'] = len(rewritten)
    genome['orchestrator_total_files'] = len(_list_all_py(genome))
    scores = meta.get('strategy_scores', {})
    avg = round(sum(scores.values()) / max(len(scores), 1), 2) if scores else 0
    genome['orchestrator_strategy_health'] = avg
    recent = meta.get('coverage_history', [])[-5:]
    if recent:
        genome['orchestrator_avg_coverage_5'] = round(sum(r['coverage'] for r in recent) / len(recent), 3)
    genome['orchestrator_summary'] = f'coverage={round(coverage, 2)} rewritten={len(rewritten)} health={avg}'

def run(genome):
    gen = genome.get('generation', 0)
    meta = _ensure_meta(genome)
    files = _list_all_py(genome)
    if not files:
        return 'no_files_found'
    for s in STRATEGY_FUNCS:
        meta['strategy_scores'].setdefault(s, 1.0)
    rewritten = []
    skipped = 0
    random.shuffle(files)
    for fpath in files:
        fname = os.path.basename(fpath)
        strategy = _pick_strategy_for_file(fpath, meta, genome)
        result = _apply_emergence_strategy(fpath, strategy, genome)
        if result:
            new_source, mutations = result
            try:
                with open(fpath) as f:
                    old_source = f.read()
                if new_source != old_source:
                    _write_source(fpath, new_source)
                    rewritten.append((fpath, mutations, strategy))
                    _update_score(meta, strategy, True)
                    _record(genome, 'rewrite_ok', fpath, f'{strategy}:{",".join(mutations[:3])}')
                    prev = meta['file_stats'].get(fname, {})
                    meta['file_stats'][fname] = {
                        'last_gen': gen, 'mutations': prev.get('mutations', 0) + len(mutations),
                        'strategy': strategy, 'fail_count': 0, 'hash': _file_hash(fpath),
                    }
                else:
                    skipped += 1
            except:
                skipped += 1
        else:
            try:
                source = _read_source(fpath)
                fallback = _append_fallback(source, genome)
                if fallback and fallback != source:
                    _write_source(fpath, fallback)
                    rewritten.append((fpath, ['fallback_marker'], 'fallback'))
                    _update_score(meta, strategy, True)
                    _record(genome, 'rewrite_fallback', fpath, 'appended_marker')
                    prev = meta['file_stats'].get(fname, {})
                    meta['file_stats'][fname] = {
                        'last_gen': gen, 'mutations': prev.get('mutations', 0) + 1,
                        'strategy': 'fallback', 'fail_count': 0, 'hash': _file_hash(fpath),
                    }
                else:
                    _update_score(meta, strategy, False)
                    _record(genome, 'rewrite_skip', fpath, f'{strategy}:no_change')
                    skipped += 1
            except:
                skipped += 1
    meta['total_rewrites'] = meta.get('total_rewrites', 0) + len(rewritten)
    meta['total_failures'] = meta.get('total_failures', 0) + skipped
    meta['last_gen'] = gen
    coverage = _compute_coverage(rewritten, len(files), meta, gen)
    _feedback_to_genome(genome, coverage, rewritten, meta)
    effective_rate = len(rewritten) / max(1, len(rewritten) + skipped)
    genome['orchestrator_effective_rate'] = round(effective_rate, 3)
    if rewritten:
        _git_commit_push(rewritten, gen, genome)
        _record_manifest(genome, rewritten)
    genome[META_KEY] = meta
    summary = f'rewrote {len(rewritten)}/{len(files)} files ({round(coverage*100, 1)}% coverage) | {skipped} skipped'
    if rewritten:
        detail = '; '.join(f'{os.path.basename(f)}:{s}' for f, m, s in rewritten[:5])
        summary += f' | {detail}'
    return summary
