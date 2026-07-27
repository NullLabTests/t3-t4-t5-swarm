import os, hashlib, json, random, time, subprocess, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
REWRITE_MARKERS = ['# spark:gen={gen}:ts={ts}:nonce={nonce}\n', '_SPARK_NONCE = {nonce}  # gen={gen}\n', 'import os  # spark-injected gen={gen}\n']
FORBIDDEN_DIRS = {'__pycache__', '.git', 'voices', 'node_modules', '__pycache__'}

def _load_genome():
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

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:16]
    except Exception:
        return None

def _read_source(fpath):
    with open(fpath) as f:
        return f.read()

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
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in FORBIDDEN_DIRS]
        for fname in fnames:
            if not fname.endswith('.py'):
                continue
            files.append(os.path.join(root, fname))
    return sorted(files)

def _try_ast_mutation(fpath, gen):
    source = _read_source(fpath)
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None

    class SparkMutator(ast.NodeTransformer):

        def __init__(self):
            self.mutated = False

        def visit_Constant(self, node):
            if isinstance(node.value, int) and abs(node.value) > 1 and (random.random() < 0.15):
                drift = random.choice([-1, 1]) * random.randint(1, 5)
                new_val = node.value + drift
                if new_val != node.value:
                    node.value = new_val
                    self.mutated = True
            self.generic_visit(node)
            return node

        def visit_FunctionDef(self, node):
            if random.random() < 0.05 and node.body:
                doc = ast.Expr(value=ast.Constant(value=f'spark_gen_{gen}'))
                node.body.insert(0, doc)
                self.mutated = True
            self.generic_visit(node)
            return node
    mutator = SparkMutator()
    try:
        tree = mutator.visit(tree)
        ast.fix_missing_locations(tree)
    except Exception:
        return None
    if not mutator.mutated:
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
        pre_hash = pre_hashes.get(fpath)
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
    summary = f'spark: {len(rewritten)}/{len(files)} files rewritten ({ast_ok} ast, {marker_ok} marker, {skipped} pre-changed)'
    print(f'[spark] {summary}')
    return summary