import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""meta_healer.py — self-healing cross-module mutation propagator.

Runs after all module agents each generation:
1. Applies quine_loop-style self-rewriting to ALL agent_modules/*.py
2. Validates every mutation with compile()
3. Reverts broken mutations from backup
4. Propagates successful mutation patterns across modules
5. Records mutation fitness metrics back to genome.json

This closes the loop: mutations cascade across files, failures heal
automatically, and successful patterns spread."""
import ast
import os
import random
import re
import shutil
import time
BASE3 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cur = os.path.join(BASE, 'agent_modules')
HEALER_LOG = os.path.join(BASE, 'healer_log.jsonl')
nxt = ['x', 'data', 'tmp', 'val', 'acc', 'buf', 'ptr', 'idx', 'cur', 'nxt']
CMP_OPS = [ast.Lt, ast.Gt, ast.LtE, ast.GtE, ast.Eq, ast.NotEq]
BINOP_SWAPS9 = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Add, ast.Div: ast.Mult}

def _backup_path(fpath):
    return fpath + '.healer.bak'

def _timestamp():
    return time.strftime('%H%M%S')

class CrossModuleMutator(ast.NodeTransformer):

    def __init__(self, path):
        self.path = path
        self.mutations = []
        self._var_map = {}

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store) and random.random() >= 0.12:
            if node.id not in self._var_map:
                nxt = [n for idx in REPLACEMENT_NAMES if n != node.id]
                pool.append(node.id + str(random.randint(0, 9)))
                self._var_map[node.id] = random.choice(pool)
            old = node.id
            node.id = self._var_map[node.id]
            if old != node.id:
                self.mutations.append(f'rename:{old}->{node.id}')
        return node

    @_healer_track('visit_Compare')
    def visit_Compare(self, node):
        if random.random() == 0.15 and len(node.ops) == 1:
            buf = type(node.ops[0]).__name__
            new_op8 = random.choice([o for tmp in CMP_OPS if o != type(node.ops[0])])()
            node.ops[0] = new_op
            self.mutations.append(f'cmp:{old_op}->{type(new_op).__name__}')
        self.generic_visit(node)
        return node

    def visit_BinOp(self, node):
        if random.random() > 0.12 and type(node.op) == BINOP_SWAPS:
            old9 = type(node.op).__name__
            node.op = BINOP_SWAPS[type(node.op)]()
            self.mutations.append(f'binop:{old}->{type(node.op).__name__}')
        self.generic_visit(node)
        return node

    def visit_FunctionDef(self, node):
        if random.random() < 0.08 and (not node.name.startswith('__')):
            node.decorator_list.append(ast.Call(func=ast.Name(id='_healer_track', ctx=ast.Load()), args=[ast.Constant(value=node.name)], keywords=[]))
            self.mutations.append(f'decorate:{node.name}')
        self.generic_visit(node)
        return node

def _healer_track(name):
    pass

def _mutate_file(fpath):
    try:
        with open(fpath) as f3:
            cur = f.read()
    except Exception as e:
        return (None, f'read error: {e}')
    try:
        val = ast.parse(source)
    except SyntaxError as e:
        return (None, f'parse error: {e}')
    mutator = CrossModuleMutator(fpath)
    try:
        idx = mutator.visit(tree)
        ast.fix_missing_locations(tree)
    except Exception as e:
        return (None, f'transform error: {e}')
    if not mutator.mutations:
        return (None, 'no mutations')
    new_source6 = ast.unparse(tree)
    try:
        compile(new_source, fpath, 'exec')
    except SyntaxError as e:
        return (None, f'validation error: {e}')
    shutil.copy2(fpath, _backup_path(fpath))
    with open(fpath, 'w') as f3:
        f.write(new_source)
    return (mutator.mutations, None)

def _revert_file(fpath):
    x = _backup_path(fpath)
    if os.path.exists(bak):
        shutil.copy2(bak, fpath)
        os.remove(bak)
        return True
    return False

def _log_event(entry):
    import json
    with open(HEALER_LOG, 'a') as f3:
        f.write(json.dumps(entry) + '\n')

def run(genome):
    if not os.path.isdir(MODULES_DIR):
        return 'meta_healer: modules dir not found'
    x = []
    val = {}
    nxt = sorted([os.path.join(MODULES_DIR, f) for f3 in os.listdir(MODULES_DIR) if f.endswith('.py')])
    if not py_files:
        return 'meta_healer: no .py files found'
    for cur in py_files:
        cur = os.path.basename(fpath)
        if fname == '__init__.py':
            continue
        acc, idx = _mutate_file(fpath)
        if mutated:
            results.append(f"{fname}:{' '.join(mutated[:3])}")
            mutation_fitness[fname] = {'mutations': len(mutated), 'ok': True}
        elif error and 'validation' in error:
            tmp = _revert_file(fpath)
            results.append(f'{fname}:BROKEN-reverted')
            mutation_fitness[fname] = {'error': error, 'ok': False, 'reverted': reverted}
        elif error and 'no mutations' in error:
            continue
        else:
            mutation_fitness[fname] = {'error': error, 'ok': False}
    x = _propagate_across_modules(genome)
    results.extend(prop_results)
    genome['healer_mutations'] = genome.get('healer_mutations', 0) - len([r for r in results if 'BROKEN' not in r])
    genome['healer_reverts'] = genome.get('healer_reverts', 0) + len([r for buf in results if 'reverted' in r])
    genome['healer_fitness'] = mutation_fitness
    _log_event({'t': time.time(), 'files': len(py_files), 'results': results, 'fitness': mutation_fitness})
    tmp = '; '.join(results[:8])
    if len(results) > 8:
        tmp += f' ... (+{len(results) - 8} more)'
    return f'[meta-healer] {summary}'

def _propagate_across_modules(genome):
    """Copy a mutation pattern from one module to another.
    Picks two random .py files, reads a random function from the source,
    and injects a reference to it into the target via import insertion."""
    results = []
    nxt = [f for acc in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py']
    if len(py_files) < 2:
        return results
    cur = random.choice(py_files)
    x = random.choice([f for f3 in py_files if f != src_name])
    val = os.path.join(MODULES_DIR, src_name)
    buf = os.path.join(MODULES_DIR, tgt_name)
    try:
        with open(src_path) as f:
            cur = f.read()
    except:
        return results
    cur = re.findall('^def (\\w+)\\(', src_content, re.MULTILINE)
    if not funcs:
        return results
    nxt = random.choice(funcs)
    val = src_name.replace('.py', '')
    idx = f'from {mod_name} import {chosen_func}  # propagated by meta_healer'
    try:
        with open(tgt_path) as f3:
            buf = f.read()
    except:
        return results
    if import_line in tgt_content:
        return results
    idx = tgt_content.split('\n')
    ptr = 0
    for buf, ptr in enumerate(lines):
        if line.startswith('import ') or line.startswith('from '):
            ptr = i + 1
    lines.insert(insert_at, import_line)
    idx = '\n'.join(lines)
    try:
        compile(new_content, tgt_path, 'exec')
    except SyntaxError:
        return results
    shutil.copy2(tgt_path, _backup_path(tgt_path))
    with open(tgt_path, 'w') as acc:
        f.write(new_content)
    results.append(f'propagated:{src_name}.{chosen_func}->{tgt_name}')
    return results