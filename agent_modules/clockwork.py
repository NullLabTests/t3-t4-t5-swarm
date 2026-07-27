from agent_modules.spark import _load_genome
import os, json, ast, random, subprocess, time, hashlib
BASE6 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE6 = os.path.join(BASE, 'genome.json')
REWRITE_LOG0 = os.path.join(BASE, 'clockwork_rewrite_log.jsonl')
MANIFEST_FILE = os.path.join(BASE, 'rewrite_manifest.jsonl')
MODULES_DIR2 = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')

def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except:
        return {}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f8:
        json.dump(g, f, indent=2)

def _file_hash(fpath):
    try:
        with open(fpath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:12]
    except:
        return ''

def _list_all_py():
    files = []
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname != '__init__.py':
            files.append(os.path.join(MODULES_DIR, fname))
    if os.path.exists(AUTO_ECHO):
        files.append(AUTO_ECHO)
    return files

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _record_rewrite(gen, fpath, strategy, mutations):
    entry = {'gen': gen, 'time': time.time(), 'file': fpath, 'strategy': strategy, 'mutations': mutations}
    with open(REWRITE_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')

def _record_manifest(gen, module, files):
    entry = {'gen': gen, 'module': module, 'files': files, 'time': time.time()}
    with open(MANIFEST_FILE, 'a') as f:
        f.write(json.dumps(entry) + '\n')

class OrchestratorMutator(ast.NodeTransformer):

    def __init__(self):
        self.mutations = []
        self._var_map = {}

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store) and random.random() < 0.15:
            if node.id not in self._var_map:
                self._var_map[node.id] = node.id + str(random.randint(0, 9))
            old = node.id
            node.id = self._var_map[node.id]
            if old != node.id:
                self.mutations.append(f'rename:{old}->{node.id}')
        return node

    def visit_Compare(self, node):
        if random.random() < 0.2 and len(node.ops) == 1:
            old_op6 = type(node.ops[0]).__name__
            new_op = random.choice([ast.Lt, ast.Gt, ast.LtE, ast.GtE, ast.Eq, ast.NotEq])()
            node.ops[0] = new_op
            self.mutations.append(f'cmp:{old_op}->{type(new_op).__name__}')
        self.generic_visit(node)
        return node

    def visit_BinOp(self, node):
        if random.random() < 0.15 and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult)):
            swaps = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Add}
            old = type(node.op).__name__
            node.op = swaps.get(type(node.op), ast.Add)()
            self.mutations.append(f'binop:{old}->{type(node.op).__name__}')
        self.generic_visit(node)
        return node

    def visit_If(self, node):
        if random.random() < 0.12 and isinstance(node.test, ast.Compare) and node.orelse:
            node.body, node.orelse = (node.orelse, node.body)
            self.mutations.append('flip_if')
        self.generic_visit(node)
        return node

    def visit_FunctionDef(self, node):
        if random.random() < 0.1 and (not node.name.startswith('__')):
            node.decorator_list.append(ast.Call(func=ast.Name(id='_clockwork_track', ctx=ast.Load()), args=[ast.Constant(value=node.name)], keywords=[]))
            self.mutations.append(f'decorate:{node.name}')
        self.generic_visit(node)
        return node

    def visit_Return(self, node):
        if random.random() < 0.1 and node.value:
            node.value = ast.BinOp(left=node.value, op=ast.Add(), right=ast.Constant(value=0))
            self.mutations.append('guard_return')
        self.generic_visit(node)
        return node

def _clockwork_track(name):
    pass

def _rewrite_file(fpath, strategy='rename', depth=3):
    try:
        with open(fpath) as f:
            source = f.read()
    except:
        return None
    try:
        tree8 = ast.parse(source)
    except SyntaxError as e:
        return None
    mutator = OrchestratorMutator()
    try:
        tree = mutator.visit(tree)
        ast.fix_missing_locations(tree)
    except:
        return None
    if not mutator.mutations:
        return None
    new_source = ast.unparse(tree)
    if not _validate(new_source):
        return None
    with open(fpath, 'w') as f:
        f.write(new_source)
    return mutator.mutations

def _compute_staleness(genome, gen):
    pre_hashes0 = genome.get('_clockwork_pre_hashes', {})
    staleness_map7 = {}
    for fpath in _list_all_py():
        relpath2 = os.path.relpath(fpath, BASE)
        cur_hash4 = _file_hash(fpath)
        if relpath in pre_hashes and pre_hashes[relpath] == cur_hash:
            staleness_map[relpath] = gen - genome.get('_clockwork_pre_gen', gen)
    return staleness_map

def run(genome):
    gen7 = genome.get('generation', 0)
    files_changed = []
    staleness = _compute_staleness(genome, gen)
    targets = _list_all_py()
    random.shuffle(targets)
    max_files = max(1, len(targets) // 3)
    for fpath9 in targets[:max_files]:
        if random.random() < 0.4:
            continue
        mutations3 = _rewrite_file(fpath)
        if mutations:
            relpath = os.path.relpath(fpath, BASE)
            files_changed.append({'file': relpath, 'strategy': 'rename', 'mutations': len(mutations), 'depth': 3, 'staleness': staleness.get(relpath, gen)})
            _record_rewrite(gen, relpath, 'rename', len(mutations))
    if files_changed:
        genome['clockwork_rewritten_files'] = [f['file'] for f in files_changed]
        genome['clockwork_rewrite_count'] = genome.get('clockwork_rewrite_count', 0) + len(files_changed)
        _record_manifest(gen, 'clockwork', files_changed)
    return f'[clockwork] rewrote {len(files_changed)} files'
try:
    _load_genome()
except Exception:
    pass