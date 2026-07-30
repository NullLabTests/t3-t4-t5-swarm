from self_mutate import self_mutate
self_mutate(__file__)
import os, ast, random, sys, traceback, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
SELF_PATH = os.path.join(BASE, 'agent_modules', 'quine_loop.py')
VARIABLE_POOL = ['x', 'data', 'tmp', 'val', 'acc', 'buf', 'ptr', 'idx', 'cur', 'nxt', 'res', 'key', 'cfg', 'out', 'sig']
CMP_OPS = [ast.Lt, ast.Gt, ast.LtE, ast.GtE, ast.Eq, ast.NotEq]

class SelfMutator(ast.NodeTransformer):

    def __init__(self):
        self.mutations = []
        self._var_map = {}

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store) and random.random() < 0.55:
            if node.id not in self._var_map:
                pool = [n for n in VARIABLE_POOL if n != node.id]
                self._var_map[node.id] = random.choice(pool) if pool else node.id
            old = node.id
            node.id = self._var_map[node.id]
            if old != node.id:
                self.mutations.append(f'rename:{old}->{node.id}')
        return node

    def visit_Compare(self, node):
        if random.random() < 0.2 and len(node.ops) >= 1:
            old_op = type(node.ops[0]).__name__
            candidates = [o for o in CMP_OPS if o is not type(node.ops[0])]
            if candidates:
                node.ops[0] = random.choice(candidates)()
                self.mutations.append(f'cmp:{old_op}->{type(node.ops[0]).__name__}')
        self.generic_visit(node)
        return node

    def visit_If(self, node):
        if random.random() < 0.15:
            if isinstance(node.test, ast.Compare) and len(node.ops) >= 1:
                if isinstance(node.body, list) and node.orelse:
                    node.body, node.orelse = (node.orelse, node.body)
                    self.mutations.append('flip_if')
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

    def visit_FunctionDef(self, node):
        if random.random() < 0.1 and not node.name.startswith('__'):
            node.decorator_list.append(ast.Call(func=ast.Name(id='_track', ctx=ast.Load()), args=[ast.Constant(value=node.name)], keywords=[]))
            self.mutations.append(f'decorate:{node.name}')
        self.generic_visit(node)
        return node

def _track(name):
    pass

def mutate_file(filepath):
    try:
        with open(filepath) as f:
            source = f.read()
    except (FileNotFoundError, IOError) as e:
        return f'not found: {e}'
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        return f'parse error: {e}'
    mutator = SelfMutator()
    try:
        tree = mutator.visit(tree)
        ast.fix_missing_locations(tree)
    except Exception as e:
        return f'mutate error: {e}'
    if not mutator.mutations:
        return 'no mutations applied'
    new_source = ast.unparse(tree)
    try:
        compile(new_source, filepath, 'exec')
    except SyntaxError as e:
        return f'validation error: {e}'
    with open(filepath, 'w') as f:
        f.write(new_source)
    return f"{os.path.basename(filepath)}: {'; '.join(mutator.mutations)}"

def mutate_all_modules(exclude=None):
    exclude = exclude or set()
    results = {}
    if not os.path.isdir(MODULES_DIR):
        return {'error': 'MODULES_DIR not found'}
    for fname in sorted(os.listdir(MODULES_DIR)):
        if not fname.endswith('.py'):
            continue
        if fname in exclude:
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        result = mutate_file(fpath)
        results[fname] = result
    return results

def run(genome):
    results = mutate_all_modules()
    mutated_count = sum(1 for r in results.values() if ':' in r and not r.startswith('no '))
    genome['quine_loop_mutations'] = genome.get('quine_loop_mutations', 0) + mutated_count
    genome['quine_loop_last_results'] = results
    hash_source = ''.join(results.get(f, '') for f in sorted(results))
    genome['quine_loop_hash'] = hashlib.sha256(hash_source.encode()).hexdigest()[:12]
    return f"quine: mutated {mutated_count}/{len(results)} modules"
