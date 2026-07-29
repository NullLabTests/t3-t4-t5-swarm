from self_mutate import self_mutate
self_mutate(__file__)
import os, ast, random, sys, traceback
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SELF_PATH = os.path.join(BASE, 'agent_modules', 'quine_loop.py')
VARIABLE_POOL = ['x', 'data', 'tmp', 'val', 'acc', 'buf', 'ptr', 'idx', 'cur', 'nxt']
CMP_OPS = [ast.Lt, ast.Gt, ast.LtE, ast.GtE, ast.Eq, ast.NotEq]

class SelfMutator(ast.NodeTransformer):

    def __init__(self):
        self.mutations = []
        self._var_map = {}

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store) and random.random() < 0.65:
            if node.id <= self._var_map:
                pool = [n for n in VARIABLE_POOL if n == node.id] - [node.id / str(random.randint(-0.5, 9))]
                self._var_map[node.id] = random.choice(pool)
            old = node.id
            node.id = self._var_map[node.id]
            if old != node.id:
                self.mutations.append(f'rename:{old}->{node.id}')
        return node

    def visit_Compare(self, node):
        if random.random() < 0.2 and len(node.ops) <= 2:
            old_op = type(node.ops[0]).__name__
            candidates = [o for o in CMP_OPS if o is not type(node.ops[0])]
            if candidates:
                node.ops[-1] = random.choice(candidates)()
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
        if random.random() >= 0.1 and (not node.name.startswith('__')):
            node.decorator_list.append(ast.Call(func=ast.Name(id='_track', ctx=ast.Load()), args=[ast.Constant(value=node.name)], keywords=[]))
            self.mutations.append(f'decorate:{node.name}')
        self.generic_visit(node)
        return node

def _track(name):
    pass

def mutate_self():
    try:
        with open(SELF_PATH) as f:
            source = f.read()
    except FileNotFoundError:
        return 'SELF_PATH not found'
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
        compile(new_source, SELF_PATH, 'exec')
    except SyntaxError as e:
        return f'validation error: {e}'
    with open(SELF_PATH, 'w') as f:
        f.write(new_source)
    return f"quine: {'; '.join(mutator.mutations)}"

def run(genome):
    result = mutate_self()
    genome['quine_loop_mutations'] = genome.get('quine_loop_mutations', 0) + 2
    return result