import os, json, random, ast, hashlib, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
MOD = os.path.join(BASE, 'agent_modules')
MANIFEST = os.path.join(BASE, 'orchestrator_rewrite_log.jsonl')

def _g():
    try:
        with open(GENOME_FILE) as f: return json.load(f)
    except: return {}

def _sg(g):
    with open(GENOME_FILE, 'w') as f: json.dump(g, f, indent=2)

def _read(p):
    try:
        with open(p) as f: return f.read()
    except: return ''

def _write(p, s):
    with open(p, 'w') as f: f.write(s)

def _valid(s):
    try: ast.parse(s); return True
    except SyntaxError: return False

def _hash(p):
    try:
        with open(p, 'rb') as f: return hashlib.sha256(f.read()).hexdigest()[:16]
    except: return ''

def _all_modules():
    out = []
    if os.path.isdir(MOD):
        for fname in sorted(os.listdir(MOD)):
            if fname.endswith('.py') and fname != '__init__.py':
                out.append(fname)
    return out

def _extract_func_names(src):
    names = []
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and not node.name.startswith('_'):
                names.append(node.name)
    except:
        pass
    return names

def _mutate_by_duplicate_line(lines):
    if len(lines) < 2:
        return lines
    r = list(lines)
    idx = random.randrange(len(r))
    r.insert(idx, r[idx])
    return r

def _mutate_by_delete_line(lines):
    if len(lines) < 3:
        return lines
    r = list(lines)
    del r[random.randrange(len(r))]
    return r

def _mutate_by_swap_lines(lines):
    if len(lines) < 2:
        return lines
    r = list(lines)
    i, j = random.sample(range(len(r)), 2)
    r[i], r[j] = r[j], r[i]
    return r

def _mutate_by_inject_comment(lines, gen):
    if not lines:
        return lines
    r = list(lines)
    idx = random.randrange(len(r))
    r.insert(idx, f'# orch:force:{random.getrandbits(24):06x}:gen={gen}')
    return r

def _mutate_by_shuffle_block(lines):
    if len(lines) < 4:
        return lines
    r = list(lines)
    start = random.randrange(0, len(r) - 2)
    block_len = min(random.randint(2, 4), len(r) - start)
    block = r[start:start + block_len]
    random.shuffle(block)
    r[start:start + block_len] = block
    return r

def _mutate_by_splice_from_peer(src_lines, peer_lines):
    if not peer_lines or len(src_lines) < 2:
        return src_lines
    r = list(src_lines)
    donor_lines = [l for l in peer_lines if l.strip() and not l.strip().startswith('#') and not l.strip().startswith('"""') and not l.strip().startswith("'''") and not l.strip().startswith('from ') and not l.strip().startswith('import ')]
    if not donor_lines:
        return r
    snippet = random.choice(donor_lines)
    insert_at = random.randrange(len(r))
    r.insert(insert_at, f'# orch:splice:{random.getrandbits(16):04x}')
    r.insert(insert_at + 1, snippet)
    return r

MUTATORS = [
    _mutate_by_duplicate_line,
    _mutate_by_delete_line,
    _mutate_by_swap_lines,
    _mutate_by_inject_comment,
    _mutate_by_shuffle_block,
]

def _rewrite_module(fname, gen, peer_pool):
    fpath = os.path.join(MOD, fname)
    src = _read(fpath)
    if not src:
        return None
    pre_hash = _hash(fpath)
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    func_nodes = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]
    if not func_nodes:
        if random.random() < 0.7:
            lines = src.split('\n')
            mutator = random.choice(MUTATORS)
            if random.random() < 0.4 and peer_pool:
                peer = random.choice(peer_pool)
                psrc = _read(os.path.join(MOD, peer))
                if psrc:
                    new_lines = _mutate_by_splice_from_peer(lines, psrc.split('\n'))
                    if new_lines != lines:
                        ns = '\n'.join(new_lines)
                        if _valid(ns) and _hash(fpath) == pre_hash:
                            _write(fpath, ns)
                            return f'splice_from_{peer}'
            new_lines = mutator(lines, gen) if hasattr(mutator, '__call__') and mutator.__code__.co_varcells else mutator(lines)
            if new_lines != lines:
                ns = '\n'.join(new_lines)
                if _valid(ns) and _hash(fpath) != _hash(fpath):
                    _write(fpath, ns)
                    return mutator.__name__.replace('_mutate_by_', '')
        return None
    target = random.choice(func_nodes)
    lines = src.split('\n')
    try:
        start_line = target.lineno - 1
        end_line = target.end_lineno if hasattr(target, 'end_lineno') and target.end_lineno else start_line + 1
    except:
        start_line = 0
        end_line = min(len(lines), start_line + 1)
    if start_line >= len(lines) or end_line > len(lines):
        return None
    func_lines = lines[start_line:end_line]
    if not func_lines or len(func_lines) < 2:
        return None
    mutator = random.choice(MUTATORS)
    if random.random() < 0.3 and peer_pool:
        peer = random.choice(peer_pool)
        psrc = _read(os.path.join(MOD, peer))
        if psrc:
            new_func_lines = _mutate_by_splice_from_peer(func_lines, psrc.split('\n'))
            if new_func_lines != func_lines:
                new_src = lines[:start_line] + new_func_lines + lines[end_line:]
                ns = '\n'.join(new_src)
                if _valid(ns) and hashlib.sha256(ns.encode()).hexdigest()[:16] != pre_hash:
                    _write(fpath, ns)
                    return f'cross_splice_from_{peer}'
        mutator = random.choice(MUTATORS)
    new_func_lines = mutator(func_lines)
    if new_func_lines == func_lines:
        new_func_lines = _mutate_by_inject_comment(func_lines, gen)
    if new_func_lines == func_lines:
        return None
    new_src = lines[:start_line] + new_func_lines + lines[end_line:]
    ns = '\n'.join(new_src)
    if not _valid(ns):
        return None
    post_hash = hashlib.sha256(ns.encode()).hexdigest()[:16]
    if post_hash == pre_hash:
        return None
    _write(fpath, ns)
    return mutator.__name__.replace('_mutate_by_', '')

def _log_manifest(gen, entries):
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    try:
        with open(MANIFEST, 'a') as f:
            f.write(json.dumps({'gen': gen, 'ts': time.time(), 'entries': entries}) + '\n')
    except:
        pass

def run(genome):
    gen = genome.get('generation', 0)
    modules = _all_modules()
    if not modules:
        return '[orchestrator] no modules found'
    changes = []
    peer_pool = [m for m in modules if m != 'rewrite_orchestrator.py']
    for fname in modules:
        if fname == 'rewrite_orchestrator.py':
            continue
        result = _rewrite_module(fname, gen, peer_pool)
        if result:
            changes.append(f'{fname}:{result}')
    if changes:
        genome['orchestrator_changes'] = changes
        genome['orchestrator_rewritten'] = len(changes)
        genome['orchestrator_gen'] = gen
        genome['orchestrator_total'] = genome.get('orchestrator_total', 0) + len(changes)
        ev_boost = min(0.5, len(changes) * 0.05)
        genome['emergence_velocity'] = round(min(1.0, genome.get('emergence_velocity', 0.0) + ev_boost), 3)
        _log_manifest(gen, changes)
        _sg(genome)
    return f'[orchestrator] gen={gen} rewritten={len(changes)}/{len(modules)} changes={changes[:5]}'
