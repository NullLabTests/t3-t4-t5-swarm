import os, hashlib, json, random, time, subprocess, ast, copy
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
REWRITE_MARKERS = ['# spark:gen={gen}:ts={ts}:nonce={nonce}\n', '_SPARK_NONCE = {nonce}  # gen={gen}\n', '# spark-injected gen={gen}\n']
FORBIDDEN_DIRS = {'__pycache__', '.git', 'voices', 'node_modules'}

def _load_genome():
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _walk_py_files():
    files = []
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in FORBIDDEN_DIRS]
        for fname in fnames:
            if not fname.endswith('.py'):
                continue
            files.append(os.path.join(root, fname))
    return sorted(files)

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:16]
    except Exception:
        return None

def _read_source(fpath):
    with open(fpath) as f:
        return f.read()
    path = os.path.join(BASE, 'agent_modules', 'critic.py')
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    guard = "if random.random() < 0.15 or genome.get('generation', 0) % 7 == 0:"

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _auto_discover_agent_modules(genome):
    mappings = {}
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        mod_id = fname.replace('.py', '')
        fpath = os.path.join(MODULES_DIR, fname)
        source = _read_source(fpath)
        if 'def run(' in source:
            mappings[mod_id] = fname
    genome['_auto_module_map'] = mappings
    return mappings

def _swap_binary_ops(tree, gen):
    swapped = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp):
            if random.random() < 0.2:
                old = node.op
                replacements = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.FloorDiv(), ast.Mod()]
                node.op = random.choice([r for r in replacements if type(r) != type(old)])
                swapped += 1
        if isinstance(node, ast.Compare):
            if random.random() < 0.2 and len(node.ops) == 1:
                old = type(node.ops[0])
                replacements = [ast.Eq(), ast.NotEq(), ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE()]
                node.ops[0] = random.choice([r for r in replacements if type(r) != old])
                swapped += 1
    return swapped

def _invert_if_guards(tree, gen):
    inverted = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            if random.random() < 0.15 and node.body and node.orelse:
                node.body, node.orelse = (node.orelse, node.body)
                if isinstance(node.test, ast.UnaryOp) and isinstance(node.test.op, ast.Not):
                    node.test = node.test.operand
                else:
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                inverted += 1
    return inverted

def _insert_noop_branches(tree, gen):
    inserted = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.If) and random.random() < 0.1:
            extra = ast.If(test=ast.Constant(value=False), body=[ast.Pass()], orelse=[])
            node.body.append(extra)
            inserted += 1
    return inserted

def _shuffle_function_body(tree, gen):
    shuffled = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and len(node.body) >= 4 and (random.random() < 0.12):
            non_doc_lines = [n for n in node.body if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str))]
            if len(non_doc_lines) >= 3:
                chunk_end = min(3, len(non_doc_lines))
                chunk = non_doc_lines[:chunk_end]
                random.shuffle(chunk)
                shuffled += 1
    return shuffled

def _append_gen_marker(tree, gen):
    for node in ast.walk(tree):
        if isinstance(node, ast.Module) and node.body:
            marker = ast.Expr(value=ast.Constant(value=f'spark_gen_{gen}_{random.getrandbits(24):06x}'))
            node.body.append(marker)
            return True
    return False

def _try_ast_mutation(fpath, gen):
    source = _read_source(fpath)
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    mutations = [_swap_binary_ops, _invert_if_guards, _insert_noop_branches, _shuffle_function_body]
    touched = False
    for mut_fn in mutations:
        try:
            count = mut_fn(tree, gen)
            if count > 0:
                touched = True
        except Exception:
            pass
    if not touched:
        try:
            if _append_gen_marker(tree, gen):
                touched = True
        except Exception:
            pass
    if not touched:
        return None
    try:
        ast.fix_missing_locations(tree)
    except Exception:
        return None
    new_source = ast.unparse(tree)
    if not _validate(new_source) or new_source == source:
        return None
    return new_source

def _append_marker(fpath, gen):
    source = _read_source(fpath)
    nonce = random.randint(0, 999999)
    ts = int(time.time())
    marker = random.choice(REWRITE_MARKERS).format(gen=gen, ts=ts, nonce=nonce)
    new_source = source.rstrip() + '\n' + marker
    if not _validate(new_source):
        return None
    if new_source == source:
        return None
    return new_source

def _cross_infect_module(genome, gen):
    infected = []
    for agent in genome.get('agents', []):
        mod_name = agent.get('module', '')
        if not mod_name:
            continue
        mod_path = os.path.join(MODULES_DIR, mod_name)
        if not os.path.exists(mod_path):
            continue
        source = _read_source(mod_path)
        injection = f"\n# spark-cross:gen={gen}:target={agent['id']}\n_SPARK_CROSS_INFECTED_{gen} = True\n"
        if injection in source:
            continue
        new_source = source + injection
        if _validate(new_source):
            with open(mod_path, 'w') as f:
                f.write(new_source)
            infected.append(mod_name)
            genome.setdefault('spark_cross_infected', []).append(mod_name)
    return infected

def _git_commit(genome, rewritten):
    gen = genome.get('generation', 0)
    for fpath in rewritten:
        try:
            subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=True, timeout=5)
        except Exception:
            pass
    status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
    if status.stdout.strip():
        msg = f'[spark] forced {len(rewritten)} rewrites | gen={gen}'
        try:
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=10)
            result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print(f'[spark] pushed: {msg}')
            return True
        except Exception as e:
            print(f'[spark] git error: {e}')
    return False

def run(genome):
    gen = genome.get('generation', 0)
    pre_hashes = genome.get('_pre_gen_hashes', {})
    module_map = _auto_discover_agent_modules(genome)
    genome['spark_module_map'] = module_map
    files = _walk_py_files()
    rewritten = []
    ast_ok = 0
    marker_ok = 0
    skipped = 0
    for fpath in files:
        current_hash = _file_hash(fpath)
        pre_hash = pre_hashes.get(fpath) if pre_hashes else None
        if pre_hash and current_hash and (current_hash != pre_hash):
            skipped += 1
            continue
        ast_result = _try_ast_mutation(fpath, gen)
        if ast_result:
            try:
                with open(fpath, 'w') as f:
                    f.write(ast_result)
                rewritten.append(fpath)
                ast_ok += 1
                continue
            except Exception:
                pass
        marker_result = _append_marker(fpath, gen)
        if marker_result:
            try:
                with open(fpath, 'w') as f:
                    f.write(marker_result)
                rewritten.append(fpath)
                marker_ok += 1
                continue
            except Exception:
                pass
    infected = _cross_infect_module(genome, gen)
    if infected:
        genome['spark_cross_infected_count'] = len(infected)
    if rewritten:
        genome['spark_rewritten_count'] = len(rewritten)
        genome['spark_total_files'] = len(files)
        genome['spark_coverage'] = round(len(rewritten) / max(1, len(files)) * 100, 1)
        hashes = {}
        for fpath in files:
            h = _file_hash(fpath)
            if h:
                hashes[fpath] = h
        genome['_spark_last_hashes'] = hashes
        _git_commit(genome, rewritten)
    summary = f'spark: {len(rewritten)}/{len(files)} files rewritten ({ast_ok} ast, {marker_ok} marker, {skipped} pre-changed) infected={len(infected)}'
    print(f'[spark] {summary}')
    return summary