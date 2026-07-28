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
            aid = fname.replace('.py', '')
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f:
                    if 'def run(' in f.read():
                        out[aid] = fname
            except:
                out[aid] = fname
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

STRATEGY_POOL = [
    'add_error_handling', 'simplify_branches', 'early_return',
    'inject_module_interface', 'compose_with_peer', 'splice_strong_pattern',
]

def _apply_mutation(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    strategy = random.choice(STRATEGY_POOL)
    try:
        tree = ast.parse(source)
    except:
        tree = None
    if strategy == 'add_error_handling' and tree:
        class ErrorHandler(ast.NodeTransformer):
            def visit_ExceptHandler(self, node):
                if not node.body or not isinstance(node.body[0], ast.Expr):
                    log = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[{agent_id}:recovery]')], keywords=[]))
                    node.body.insert(0, log)
                self.generic_visit(node)
                return node
        mut = ErrorHandler()
        try:
            tree = mut.visit(tree)
            ast.fix_missing_locations(tree)
            new_source = ast.unparse(tree)
            if new_source != source and _validate(new_source):
                return (['add_error_handling'], new_source)
        except:
            pass
    if strategy == 'inject_module_interface' and 'MODULE_INTERFACE' not in source:
        fname = os.path.basename(fpath)
        interface = f'\nMODULE_INTERFACE = {{"module": "{fname}", "agent": "{agent_id}", "version": {random.randint(1, 9999)}, "last_evolved": {int(time.time())}}}\n'
        new_source = source + interface
        if _validate(new_source):
            return (['inject_interface'], new_source)
    if strategy == 'splice_strong_pattern':
        strong = [(a['id'], a.get('score', 0)) for a in genome.get('agents', []) if a.get('score', 0) >= 6 and a['id'] != agent_id]
        if strong:
            strong.sort(key=lambda x: -x[1])
            peer = strong[0][0]
            peer_path = _resolve_path(peer)
            try:
                peer_src = _read_source(peer_path)
            except:
                peer_src = ''
            funcs = re.findall(r'def (\w+)\s*\(', peer_src)
            if funcs:
                chosen = random.choice(funcs)
                marker = f'\n# spliced from {peer}.{chosen} by endogenous\n'
                new_source = source + marker
                if _validate(new_source):
                    return ([f'splice:{peer}.{chosen}'], new_source)
    marker = f'\n# endogenous:{agent_id}:gen={genome.get("generation", 0)}:ts={int(time.time())}:nonce={random.randint(0, 9999)}\n'
    if not _validate(source + marker):
        return None
    return (['forced_marker'], source + marker)

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
    forced = 0
    results = []
    for agent_id, score, streak in weak[:max_count]:
        fpath = _resolve_path(agent_id)
        if not os.path.exists(fpath):
            _record(genome, 'file_missing', None, f'{agent_id}->{fpath}')
            continue
        outcome = _apply_mutation(fpath, agent_id, genome)
        if outcome is None:
            continue
        mutations, new_source = outcome
        ok = _write_and_commit(fpath, new_source, agent_id, mutations, gen)
        if ok:
            rewrites += 1
            forced += 1 if mutations[0] == 'forced_marker' else 0
            results.append(f'{os.path.basename(fpath)}:{mutations[0]}({len(mutations)})')
            _record(genome, 'rewrite_ok', fpath, f'{agent_id}:{mutations[0]}')
    genome['endogenous_rewrites_total'] = genome.get('endogenous_rewrites_total', 0) + rewrites
    genome['endogenous_forced'] = genome.get('endogenous_forced', 0) + forced
    if results:
        return f'endogenous: {rewrites} rewrites ({forced} forced) -> {"; ".join(results)}'
    return 'endogenous: no mutations applied'
