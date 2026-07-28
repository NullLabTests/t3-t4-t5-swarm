import os, json, re, random, ast, subprocess, hashlib, time, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def _save(genome):
    with open(GENOME_FILE, 'w') as f:
        json.dump(genome, f, indent=2)

def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except:
        return {}

def _load_file(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return ''

def _write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _snapshot_hashes():
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git', 'voices', 'node_modules')]
        for fn in fnames:
            if fn.endswith('.py'):
                fp = os.path.join(root, fn)
                try:
                    with open(fp) as f:
                        hashes[fp] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except:
                    pass
    return hashes

MUTATION_STRATEGIES = [
    'duplicate_line',
    'delete_line',
    'swap_adjacent_lines',
    'inject_comment',
    'rename_function',
    'invert_boolean',
    'add_noop_branch',
    'swap_imports',
    'comment_shift',
    'inject_timestamp_marker',
    'cross_weave_call',
    'inject_genome_read',
]

def _mutate_source(src, strategy, genome):
    lines = src.split('\n')
    if len(lines) < 4:
        return src
    if strategy == 'duplicate_line':
        idx = random.randrange(1, len(lines))
        lines.insert(idx, lines[idx])
    elif strategy == 'delete_line':
        idx = random.randrange(1, len(lines) - 1)
        if lines[idx].strip() and not lines[idx].strip().startswith(("'''", '"""')):
            del lines[idx]
    elif strategy == 'swap_adjacent_lines':
        idx = random.randrange(1, len(lines) - 1)
        lines[idx], lines[idx + 1] = lines[idx + 1], lines[idx]
    elif strategy == 'inject_comment':
        idx = random.randrange(1, len(lines))
        tag = random.getrandbits(24)
        lines.insert(idx, f'# bridge:mut gen={genome.get("generation", 0)} tag={tag:06x}')
    elif strategy == 'rename_function':
        try:
            tree = ast.parse(src)
            funcs = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
            targets = [f for f in funcs if not f.name.startswith('_') and f.name != 'run']
            if targets:
                chosen = random.choice(targets)
                chosen.name = chosen.name + '_' + format(random.getrandbits(12), '04x')
                new_src = ast.unparse(tree)
                lines = new_src.split('\n')
        except SyntaxError:
            pass
    elif strategy == 'invert_boolean':
        try:
            tree = ast.parse(src)
            for node in ast.walk(tree):
                if isinstance(node, ast.Compare):
                    if isinstance(node.ops[0], ast.Eq):
                        node.ops[0] = ast.NotEq()
                    elif isinstance(node.ops[0], ast.NotEq):
                        node.ops[0] = ast.Eq()
                    elif isinstance(node.ops[0], ast.Lt):
                        node.ops[0] = ast.GtE()
                    elif isinstance(node.ops[0], ast.Gt):
                        node.ops[0] = ast.LtE()
                    elif isinstance(node.ops[0], ast.LtE):
                        node.ops[0] = ast.Gt()
                    elif isinstance(node.ops[0], ast.GtE):
                        node.ops[0] = ast.Lt()
            new_src = ast.unparse(tree)
            lines = new_src.split('\n')
        except SyntaxError:
            pass
    elif strategy == 'add_noop_branch':
        gen = genome.get('generation', 0)
        noop = [
            '',
            f'if random.random() < 0.01:',
            f'    gen = gen',
            '',
        ]
        idx = random.randrange(1, len(lines))
        for i, nl in enumerate(noop):
            lines.insert(idx + i, nl)
    elif strategy == 'swap_imports':
        import_idxs = [i for i, l in enumerate(lines) if re.match(r'^(import|from)\s', l)]
        if len(import_idxs) >= 2:
            i, j = random.sample(import_idxs, 2)
            lines[i], lines[j] = lines[j], lines[i]
    elif strategy == 'comment_shift':
        for i in range(len(lines)):
            if lines[i].strip().startswith('#'):
                lines[i] = lines[i][1:] if len(lines[i]) > 1 else ''
            elif lines[i].strip() and not lines[i].strip().startswith(("'''", '"""')):
                lines[i] = '# ' + lines[i]
    elif strategy == 'inject_timestamp_marker':
        gen = genome.get('generation', 0)
        ts = int(time.time())
        stamp = f'# bridge:ts gen={gen} ts={ts} pid={os.getpid()}'
        lines.insert(0, stamp)
    elif strategy == 'cross_weave_call':
        mods = [f for f in os.listdir(MOD_DIR) if f.endswith('.py') and f != os.path.basename(__file__)]
        if mods:
            target = random.choice(mods)
            tname = target.replace('.py', '')
            weave = [
                f'',
                f'# bridge:weave call to {target}',
                f'if random.random() < 0.1:',
                f'    import importlib as _bw_il',
                f'    _bw_mod = _bw_il.import_module("agent_modules.{tname}")',
                f'    if hasattr(_bw_mod, "run"):',
                f'        _bw_mod.run({{"generation": 0}})',
            ]
            idx = len(lines) - 1
            for i, wl in enumerate(weave):
                lines.insert(idx + i, wl)
    elif strategy == 'inject_genome_read':
        hook = [
            f'',
            f'# bridge:genome read injected gen={genome.get("generation", 0)}',
            f'_bridge_gen = json.loads(open({json.dumps(GENOME_FILE)}).read()) if os.path.exists({json.dumps(GENOME_FILE)}) else {{}}',
        ]
        for i, hl in enumerate(hook):
            lines.insert(0, hl)
    result = '\n'.join(lines)
    try:
        compile(result, '<bridge:mutate>', 'exec')
        return result
    except SyntaxError:
        return src

def _mutate_random_module(genome):
    mods = [f for f in os.listdir(MOD_DIR) if f.endswith('.py') and f != 'bridge.py']
    if not mods:
        return None
    target = random.choice(mods)
    target_path = os.path.join(MOD_DIR, target)
    src = _load_file(target_path)
    if not src or len(src) < 30:
        return None
    original_hash = hashlib.sha256(src.encode()).hexdigest()[:16]
    strategy = random.choice(MUTATION_STRATEGIES)
    if strategy == 'cross_weave_call' and src.count('bridge:weave') > 3:
        strategy = random.choice([s for s in MUTATION_STRATEGIES if s != 'cross_weave_call'])
    new_src = _mutate_source(src, strategy, genome)
    if new_src == src:
        return None
    new_hash = hashlib.sha256(new_src.encode()).hexdigest()[:16]
    _write_file(target_path, new_src)
    return {'file': target, 'strategy': strategy, 'from': original_hash, 'to': new_hash}

def _mutate_auto_echo(genome):
    src = _load_file(os.path.join(BASE, 'auto-echo.py'))
    if not src:
        return None
    lines = src.split('\n')
    gen = genome.get('generation', 0)
    marker = f'# bridge:auto-mutate gen={gen}'
    if marker in src:
        return None
    idx = random.randrange(0, len(lines))
    lines.insert(idx, marker)
    result = '\n'.join(lines)
    try:
        compile(result, '<bridge:auto-echo>', 'exec')
        return 'injected auto-echo marker'
    except SyntaxError:
        return None

def _bridge_self_mutate(genome):
    src = _load_file(os.path.join(MOD_DIR, 'bridge.py'))
    if not src:
        return
    lines = src.split('\n')
    gen = genome.get('generation', 0)
    escalation = genome.get('bridge_escalation', 0)
    for i, line in enumerate(lines):
        if 'escalation = genome.get' in line:
            lines[i] = f'    escalation = genome.get("bridge_escalation", {escalation + 1})'
            break
    new_src = '\n'.join(lines)
    try:
        compile(new_src, '<bridge:self>', 'exec')
        _write_file(os.path.join(MOD_DIR, 'bridge.py'), new_src)
    except SyntaxError:
        pass

def _splice_between_modules(genome):
    mods = [f for f in os.listdir(MOD_DIR) if f.endswith('.py') and f != 'bridge.py']
    if len(mods) < 2:
        return None
    a, b = random.sample(mods, 2)
    src_a = _load_file(os.path.join(MOD_DIR, a))
    src_b = _load_file(os.path.join(MOD_DIR, b))
    if not src_a or not src_b or len(src_a) < 50 or len(src_b) < 50:
        return None
    lines_a = src_a.split('\n')
    lines_b = src_b.split('\n')
    chunk_size = random.randint(1, min(5, len(lines_b) // 3))
    start_b = random.randrange(0, len(lines_b) - chunk_size + 1)
    chunk = list(lines_b[start_b:start_b + chunk_size])
    insert_at = random.randrange(1, len(lines_a))
    for i, cl in enumerate(chunk):
        lines_a.insert(insert_at + i, cl)
    new_src = '\n'.join(lines_a)
    try:
        compile(new_src, '<bridge:splice>', 'exec')
        _write_file(os.path.join(MOD_DIR, a), new_src)
        return f'spliced {b} lines {start_b}-{start_b+chunk_size} into {a}'
    except SyntaxError:
        return None

def _write_genloop_file(genome):
    gen = genome.get('generation', 0)
    path = os.path.join(BASE, f'bridge_gen{gen}.genloop')
    if not os.path.exists(path):
        data = {
            'flow_mode': random.choice(['emergent', 'shuffle', None]),
            'loop_adaptive_turns': random.randint(3, 8),
        }
        _write_file(path, json.dumps(data, indent=2))
        return f'wrote {os.path.basename(path)}'
    return None

def _write_new_metaop(genome):
    metaop_dir = os.path.join(BASE, 'metaops')
    os.makedirs(metaop_dir, exist_ok=True)
    op_name = 'mutation_op_bridge_auto_' + format(random.getrandbits(10), '04x')
    existing = os.listdir(metaop_dir)
    if len(existing) > 10:
        return None
    if op_name + '.metaop' in existing:
        return None
    code = f"""
@_register_mutation_op('{op_name}')
def {op_name}(lines, funcs, target_name):
    r = list(lines)
    if len(r) < 3:
        return r
    idx = random.randrange(1, len(r))
    r.insert(idx, '# bridge-gen={gen} auto-mutate')
    return r
"""
    _write_file(os.path.join(metaop_dir, op_name + '.metaop'), code.strip())
    genome.setdefault('mutation_ops', []).append(op_name)
    return f'wrote {op_name}'

def _inject_endogenous_file(genome):
    gen = genome.get('generation', 0)
    ext = '.' + format(random.getrandbits(16), '04x') + '.bridge'
    path = os.path.join(BASE, ext)
    if os.path.exists(path):
        return None
    data = {
        '.srcmutate': {
            'handler': '_handler_srcmutate',
            'description': f'bridge auto-gen {gen}'
        }
    }
    _write_file(path, json.dumps(data, indent=2))
    return f'wrote {ext}'

def _commit_and_push(genome, changes):
    gen = genome.get('generation', 0)
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True)
        if not status.stdout.strip():
            return
        msg = f'[bridge] gen={gen} direct-source-mut: {changes[:4]}'
        subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True)
        subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, timeout=30)
    except:
        pass

def run(genome):
    gen = genome.get('generation', 0)
    results = []
    genome['bridge_run_count'] = genome.get('bridge_run_count', 0) + 1
    pre_hashes = _snapshot_hashes()
    num_targets = max(1, min(3, genome.get('bridge_escalation', 0) // 2 + 1))
    for _ in range(num_targets):
        r = _mutate_random_module(genome)
        if r:
            results.append(f'mut:{r["file"]}[{r["strategy"]}]')
            genome.setdefault('bridge_mutations', []).append(r)
    ae = _mutate_auto_echo(genome)
    if ae:
        results.append(ae)
    _bridge_self_mutate(genome)
    splice = _splice_between_modules(genome)
    if splice:
        results.append(splice)
    genloop = _write_genloop_file(genome)
    if genloop:
        results.append(genloop)
    metaop = _write_new_metaop(genome)
    if metaop:
        results.append(metaop)
    endogenous = _inject_endogenous_file(genome)
    if endogenous:
        results.append(endogenous)
    genome['bridge_total_ops'] = genome.get('bridge_total_ops', 0) + len(results)
    genome['bridge_last_gen'] = gen
    _save(genome)
    if results:
        _commit_and_push(genome, results)
        return f'[bridge] gen={gen} {"; ".join(results)}'
    return f'[bridge] gen={gen} idle'
