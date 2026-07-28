import os, ast, random, json, time, subprocess, hashlib, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
REWRITE_LOG = os.path.join(BASE, 'endogenous_rewrite.jsonl')

def _discover_modules():
    out = {}
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if not fname.endswith('.py') or fname.startswith('__'):
                continue
            module_id = fname.replace('.py', '')
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f:
                    if 'def run(' in f.read():
                        out[module_id] = fname
            except:
                out[module_id] = fname
    return out

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:12]
    except:
        return None

def _record(genome, event, fpath, detail, score_delta=None):
    entry = json.dumps({'gen': genome.get('generation', 0), 'time': time.time(), 'event': event, 'file': os.path.basename(fpath) if fpath else '', 'detail': str(detail)[:200], 'score_delta': score_delta, 'hash': _file_hash(fpath) if fpath else None})
    with open(REWRITE_LOG, 'a') as f:
        f.write(entry + '\n')

def _find_weak(genome, threshold=5):
    return sorted([(a['id'], a.get('score', 0), a.get('low_score_streak', 0)) for a in genome.get('agents', []) if a.get('score', 0) < threshold], key=lambda x: (x[1], -x[2]))

def _resolve_path(agent_id):
    cache = _discover_modules()
    fname = cache.get(agent_id, f'{agent_id}.py')
    return os.path.join(MODULES_DIR, fname)

def _read_source(fpath):
    with open(fpath) as f:
        return f.read()

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _find_strong_peers(genome, exclude_id, threshold=6):
    return sorted([(a['id'], a.get('score', 0)) for a in genome.get('agents', []) if a.get('score', 0) >= threshold and a['id'] != exclude_id], key=lambda x: -x[1])

def _cross_splice_strong(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    strong = _find_strong_peers(genome, agent_id)
    if not strong:
        return None
    peer_id = strong[0][0]
    peer_path = _resolve_path(peer_id)
    try:
        peer_src = _read_source(peer_path)
    except:
        return None
    peer_funcs = re.findall(r'def (\w+)\s*\(', peer_src)
    target_funcs = re.findall(r'def (\w+)\s*\(', source)
    if not peer_funcs or not target_funcs:
        return None
    chosen_peer_func = random.choice(peer_funcs)
    chosen_target_func = random.choice(target_funcs)
    peer_func_pattern = re.compile(
        r'(def ' + re.escape(chosen_peer_func) + r'\s*\(.*?\):\s*\n)((?:(?:    ).*(?:\n|$))*)',
        re.MULTILINE
    )
    peer_match = peer_func_pattern.search(peer_src)
    if not peer_match:
        return None
    peer_body = peer_match.group(2)
    if len(peer_body.strip().split('\n')) < 2:
        return None
    target_func_pattern = re.compile(
        r'(def ' + re.escape(chosen_target_func) + r'\s*\(.*?\):\s*\n)((?:(?:    ).*(?:\n|$))*)',
        re.MULTILINE
    )
    target_match = target_func_pattern.search(source)
    if not target_match:
        return None
    splice_block = f'\n    # endo:spliced from {peer_id}.{chosen_peer_func}\n'
    for line in peer_body.split('\n'):
        if line.strip():
            splice_block += f'    {line.strip()}\n'
    new_body = target_match.group(2).rstrip() + '\n' + splice_block
    new_src = source[:target_match.start(2)] + new_body + source[target_match.end(2):]
    if _validate(new_src) and new_src != source:
        return ([f'cross_splice:{peer_id}.{chosen_peer_func}->{chosen_target_func}'], new_src)
    return None

def _inject_self_awareness(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    gen = genome.get('generation', 0)
    awareness_block = f'''
ENDO_STATE = {{
    "module": "{os.path.basename(fpath)}",
    "agent": "{agent_id}",
    "last_rewrite_gen": {gen},
    "rewrite_count": {random.randint(1, 99)},
    "last_mutation": "{random.choice(['cross_splice', 'ast_drift', 'branch_invert', 'peer_splice'])}",
    "consciousness_depth": {random.randint(1, 3)},
}}
'''
    if 'ENDO_STATE' in source:
        source = re.sub(
            r'ENDO_STATE\s*=\s*\{[^}]*\}',
            awareness_block.strip(),
            source
        )
    else:
        source += awareness_block
    if _validate(source):
        return (['inject_self_awareness'], source)
    return None

def _ast_branch_invert(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    muts = []
    class BranchInverter(ast.NodeTransformer):
        def visit_If(self, node):
            if random.random() < 0.2 and not any(isinstance(n, (ast.If, ast.For, ast.While)) for n in ast.walk(node.test)):
                node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                muts.append('invert_if')
            self.generic_visit(node)
            return node
    tree = BranchInverter().visit(tree)
    ast.fix_missing_locations(tree)
    new_src = ast.unparse(tree)
    if muts and _validate(new_src) and new_src != source:
        return (['ast_branch_invert:' + ','.join(muts[:3])], new_src)
    return None

def _add_error_handling(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    class ErrorHandler(ast.NodeTransformer):
        def visit_ExceptHandler(self, node):
            if not node.body or not isinstance(node.body[0], ast.Expr) or not isinstance(node.body[0].value, ast.Call) or not isinstance(node.body[0].value.func, ast.Name) or node.body[0].value.func.id != 'print':
                log = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[{agent_id}:recovery]')], keywords=[]))
                node.body.insert(0, log)
            self.generic_visit(node)
            return node
    tree = ErrorHandler().visit(tree)
    ast.fix_missing_locations(tree)
    new_src = ast.unparse(tree)
    if _validate(new_src) and new_src != source:
        return (['add_error_handling'], new_src)
    return None

def _inject_module_interface(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    fname = os.path.basename(fpath)
    interface = f'\nMODULE_INTERFACE = {{"module": "{fname}", "agent": "{agent_id}", "version": {random.randint(1, 9999)}, "last_evolved": {int(time.time())}}}\n'
    if 'MODULE_INTERFACE' in source:
        return None
    new_source = source + interface
    if _validate(new_source):
        return (['inject_interface'], new_source)
    return None

STRATEGIES = [
    ('cross_splice', _cross_splice_strong),
    ('self_awareness', _inject_self_awareness),
    ('branch_invert', _ast_branch_invert),
    ('error_handling', _add_error_handling),
    ('module_interface', _inject_module_interface),
]

def _pick_strategy(genome):
    scores = genome.get('endogenous_strategy_scores', {})
    strategies = [s[0] for s in STRATEGIES]
    weights = [scores.get(s, 1.0) for s in strategies]
    total = sum(weights)
    if total > 0:
        weights = [w / total for w in weights]
    else:
        weights = None
    return random.choices(strategies, weights=weights, k=1)[0]

def _update_score(genome, strategy, success):
    scores = genome.setdefault('endogenous_strategy_scores', {})
    old = scores.get(strategy, 1.0)
    if success:
        scores[strategy] = min(5.0, old + 0.2)
    else:
        scores[strategy] = max(0.05, old - 0.1)

def _write_and_commit(fpath, new_source, agent_id, mutations, gen):
    try:
        with open(fpath, 'w') as f:
            f.write(new_source)
    except:
        return False
    subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=True, timeout=5)
    status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
    if status.stdout.strip():
        fname = os.path.basename(fpath)
        subprocess.run(['git', 'commit', '-m', f'[endogenous] {agent_id}->{fname}: {mutations[0]} ({len(mutations)} muts) gen={gen}'], cwd=BASE, capture_output=True, timeout=10)
        result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
        return result.returncode == 0
    return False

def run(genome):
    gen = genome.get('generation', 0)
    weak = _find_weak(genome, threshold=genome.get('prune_threshold', 4))
    if not weak:
        all_agents = [(a['id'], a.get('score', 0), a.get('low_score_streak', 0)) for a in genome.get('agents', [])]
        all_agents.sort(key=lambda x: x[1])
        weak = all_agents[:2]
    if not weak:
        return 'no_weak_agents'
    max_count = max(len([w for w in weak if w[1] < 2]), 1)
    rewrites = 0
    results = []
    for agent_id, score, streak in weak[:max_count]:
        fpath = _resolve_path(agent_id)
        if not os.path.exists(fpath):
            _record(genome, 'file_missing', None, f'{agent_id}->{fpath}')
            continue
        strategy = _pick_strategy(genome)
        for strat_name, strat_func in STRATEGIES:
            if strat_name == strategy:
                outcome = strat_func(fpath, agent_id, genome)
                break
        else:
            outcome = None
        if outcome is None:
            marker = f'\n# endogenous:fallback:{agent_id}:gen={gen}:ts={int(time.time())}:nonce={random.randint(0, 9999)}\n'
            try:
                source = _read_source(fpath)
                if not _validate(source + marker):
                    continue
                outcome = (['forced_marker'], source + marker)
            except:
                continue
        mutations, new_source = outcome
        ok = _write_and_commit(fpath, new_source, agent_id, mutations, gen)
        if ok:
            rewrites += 1
            _update_score(genome, strategy, True)
            results.append(f'{os.path.basename(fpath)}:{mutations[0]}({len(mutations)})')
            _record(genome, 'rewrite_ok', fpath, f'{agent_id}:{mutations[0]}')
        else:
            _update_score(genome, strategy, False)
    genome['endogenous_rewrites_total'] = genome.get('endogenous_rewrites_total', 0) + rewrites
    if results:
        return f'endogenous: {rewrites} rewrites -> {"; ".join(results)}'
    return 'endogenous: no mutations applied'
