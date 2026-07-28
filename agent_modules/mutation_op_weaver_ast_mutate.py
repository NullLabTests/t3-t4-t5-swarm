import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_weaver_ast_mutate(lines, *args):
    if not lines or len(lines) < 3:
        return lines
    src = '\n'.join(lines)
    return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py'])
    try:
        tree = ast.parse(src)

        class WeaverMut(ast.NodeTransformer):

            def visit_FunctionDef(self, node):
                if node.body and random.random() < 0.3:
                    node.body.insert(0, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
                self.generic_visit(node)
                return node

            def visit_If(self, node):
                if random.random() < 0.15:
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                self.generic_visit(node)
                return node
                with open(GENOME_FILE, 'w') as f:
                    json.dump(g, f, indent=2)
        tree = WeaverMut().visit(tree)
        ast.fix_missing_locations(tree)
        new_src = ast.unparse(tree)
        return new_src.split('\n')
    except:
        return lines