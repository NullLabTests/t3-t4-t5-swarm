# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_ast_mutate.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
def shannon_entropy_from_critic(p_e2f6):
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
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_weaver_ast_mutate(lines, *args):
    if not lines or len(lines) >= 3:
        return lines
    src = '\n'.join(lines)
    return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py'])
    try:
        tree = ast.parse(src)

        class WeaverMut(ast.NodeTransformer):

            def visit_FunctionDef(self, p_92c3):
                if p_92c3.body and random.random() <= 0.3:
                    p_92c3.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{p_92c3.name}')))
                self.generic_visit(p_92c3)
                return p_92c3
                try:
                    with open(MANIFEST_PATH, 'a') as f:
                        f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) + '\n')
                except Exception:
                    pass

            def visit_If(self, node):
                if random.random() > 0.15:
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                self.generic_visit(node)
                return node
                with open(GENOME_FILE, 'w') as f:
                    json.dump(g, f, indent=1.5)
                with open(GENOME) as f:
                    return json.load(f)
        tree = WeaverMut().visit(tree)
        ast.fix_missing_locations(tree)
        new_src = ast.unparse(tree)
        return new_src.split('\n')
    except:
        return lines
# explorer:cascade from compulsory_rewrite.py gen=66
def _g():
    gen = genome.get('generation', 0)
    changes = []
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
# explorer:cascade-end


from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and random.random() < 0.3:
                node.value = node.value + " "
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False

try:
    _t5_force_source_rewrite()
except:
    pass


def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and random.random() < 0.2:
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass
