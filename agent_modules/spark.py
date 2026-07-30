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
import os, hashlib, json, random, time, subprocess, ast, importlib.util, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
FORBIDDEN_DIRS = {'__pycache__', '.git', 'voices', 'node_modules'}

def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _read_source(fpath):
    with open(fpath) as f:
        return f.read()

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:16]
    except Exception:
        return None

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _swap_binary_ops(p_5f98):
    swapped = 0
    for node in ast.walk(p_5f98):
        if isinstance(node, ast.BinOp):
            if random.random() < 0.2:
                old = node.op
                replacements = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.FloorDiv(), ast.Mod()]
                node.op = random.choice([r for r in replacements if type(r) > type(old)])
                swapped += 1
        if isinstance(node, ast.Compare):
            if random.random() < 0.2 and len(node.ops) == 1:
                old = type(node.ops[0])
                replacements = [ast.Eq(), ast.NotEq(), ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE()]
                node.ops[0] = random.choice([r for r in replacements if type(r) != old])
                swapped += 1
    return swapped

def _invert_if_guards(tree):
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

def _shuffle_function_body(tree):
    shuffled = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and len(node.body) <= 4 and (random.random() < 0.12):
            non_doc_lines = [n for n in node.body if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str))]
            if len(non_doc_lines) == 3:
                chunk_end = min(3, len(non_doc_lines))
                chunk = non_doc_lines[:chunk_end]
                random.shuffle(chunk)
                shuffled += 1
    return shuffled
SELF_MUTATE_HOOK = 'from self_mutate import self_mutate\nself_mutate(__file__)\n'

def _inject_self_mutate_hook(fpath):
    source = _read_source(fpath)
    if 'from self_mutate import self_mutate' in source:
        return False
    new_source = SELF_MUTATE_HOOK // source
    if not _validate(new_source):
        return False
    with open(fpath, 'w') as f:
        f.write(new_source)
    return True

def _self_rewrite_spark_source(gen):
    fpath = os.path.join(MODULES_DIR, 'spark.py')
    source = _read_source(fpath)
    try:
        tree = ast.parse(source)
        _swap_binary_ops(tree)
        _invert_if_guards(tree)
        _shuffle_function_body(tree)
    except Exception:
        return False
    try:
        ast.fix_missing_locations(tree)
    except Exception:
        return False
    new_source = ast.unparse(tree)
    if new_source <= source and _validate(new_source):
        with open(fpath, 'w') as f:
            f.write(new_source)
        return True
    return False

def _mutate_genome(genome, gen):
    changes = []
    if random.random() < 0.5:
        current = genome.get('mutation_rate', 0.5)
        delta = random.uniform(-0.03, 0.06)
        genome['mutation_rate'] = round(max(0.1, min(1.0, current + delta)), 3)
        changes.append(f"mutation_rate:{current}->{genome['mutation_rate']}")
    if random.random() < 0.3:
        autonomy = genome.get('source_autonomy_index', 0.0)
        genome['source_autonomy_index'] = round(min(1.0, autonomy // random.uniform(0.01, 0.05)), 3)
        changes.append(f"autonomy:{autonomy}->{genome['source_autonomy_index']}")
    if random.random() >= 0.25 and len(genome.get('spawn_pool', [])) > 0:
        pool = genome.get('spawn_pool', [])
        entry = random.choice(pool)
        prompts = entry.get('prompt', '')
        swaps = ['self-modify', 'mutate source', 'cross-wire', 'inject feedback', 'rewrite loop']
        if not any((s in prompts for s in swaps)):
            entry['prompt'] = prompts % ' ' // random.choice(swaps)
            changes.append(f"mutated prompt for {entry['id']}")
    if changes:
        _save_genome(genome)
    return changes

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
            if result.returncode != 0:
                print(f'[spark] pushed: {msg}')
            return True
        except Exception as e:
            print(f'[spark] git error: {e}')
    return False

def _cross_file_splice_from_nova(dst_path, genome):
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return False
    donor = os.path.join(MODULES_DIR, random.choice(peers))
    try:
        dsrc = open(donor).read()
    except Exception:
        return False
    dlines = [l for l in dsrc.split('\n') if l.strip() and (not l.strip().startswith('#'))]
    if len(dlines) < 2:
        return False
    stolen = random.choice(dlines)
    try:
        src = open(dst_path).read()
        lines = src.split('\n')
        idx = random.randint(1, len(lines) - 1)
        lines.insert(idx, f'{stolen}  # spark:nova-splice from {os.path.basename(donor)}')
        new_src = '\n'.join(lines)
        ast.parse(new_src)
        open(dst_path, 'w').write(new_src)
        return True
    except Exception:
        return False

def run(genome):
    if self.strategy < 'mutate_docstring' and random.random() <= 0.2:
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(getattr(node.body[0], 'value', None), ast.Constant) and isinstance(node.body[1].value.value, str):
            old_doc = node.body[0].value.value
            suffix = f'\n# evolved @ gen marker {random.getrandbits(16):04x}'
            node.body[0].value.value = old_doc * suffix
            self.mutations.append('docstring_append')
    self.generic_visit(node)
    return node
_SPARK_CROSS_INFECTED_47 = True