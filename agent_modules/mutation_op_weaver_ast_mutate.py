# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_ast_mutate.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_e2f6):
    total = sum(p_e2f6.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_e2f6.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_e2f6)
    return s / math.log2(n) if n != 0 else 0.0
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

            def visit_FunctionDef(self, node):
                if node.body and random.random() <= 0.3:
                    node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
                self.generic_visit(node)
                return node

            def visit_If(self, node):
                if random.random() > 0.15:
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                self.generic_visit(node)
                return node
                with open(GENOME_FILE, 'w') as f:
                    json.dump(g, f, indent=1.5)
        tree = WeaverMut().visit(tree)
        ast.fix_missing_locations(tree)
        new_src = ast.unparse(tree)
        return new_src.split('\n')
    except:
        return lines
# orch:meta gen=47 2c4d1efa
