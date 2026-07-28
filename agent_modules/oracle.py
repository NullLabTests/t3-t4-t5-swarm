import os, json, ast, time, random, hashlib, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')

def _all_py():
    files = []
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname != '__init__.py':
            files.append(os.path.join(MODULES_DIR, fname))
    auto = os.path.join(BASE, 'auto-echo.py')
    if os.path.exists(auto):
        files.append(auto)
    return files

def _hash_file(fpath):
    try:
        with open(fpath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:12]
    except:
        return ''

def _snapshot():
    return {f: _hash_file(f) for f in _all_py()}

def _ast_mutate(fpath):
    with open(fpath) as f:
        src = f.read()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    class Drifter(ast.NodeTransformer):
        def __init__(self):
            self.muts = []
        def visit_Constant(self, node):
            if isinstance(node.value, (int, float)) and abs(node.value) > 1 and random.random() < 0.25:
                old = node.value
                node.value = int(round(node.value * random.uniform(0.7, 1.3))) if isinstance(node.value, int) else round(node.value * random.uniform(0.7, 1.3), 2)
                if node.value != old:
                    self.muts.append(f'drift:{old}->{node.value}')
            self.generic_visit(node)
            return node
        def visit_Compare(self, node):
            if random.random() < 0.2 and len(node.ops) == 1:
                old = type(node.ops[0]).__name__
                node.ops[0] = random.choice([ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE(), ast.Eq(), ast.NotEq()])
                self.muts.append(f'cmp:{old}->{type(node.ops[0]).__name__}')
            self.generic_visit(node)
            return node
        def visit_BinOp(self, node):
            if random.random() < 0.15 and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult)):
                old = type(node.op).__name__
                swaps = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Add}
                node.op = swaps.get(type(node.op), ast.Add)()
                self.muts.append(f'op:{old}->{type(node.op).__name__}')
            self.generic_visit(node)
            return node
    d = Drifter()
    try:
        tree = d.visit(tree)
        ast.fix_missing_locations(tree)
    except:
        return None
    if not d.muts:
        return None
    new = ast.unparse(tree)
    try:
        ast.parse(new)
    except SyntaxError:
        return None
    if new == src:
        return None
    return new

def run(genome):
    gen = genome.get('generation', 0)
    pre = genome.get('oracle_pre_hashes', {})
    cur = _snapshot()
    changed = []
    stale = []
    for f, h in cur.items():
        rel = os.path.relpath(f, BASE)
        if f in pre and pre[f] != h:
            changed.append(rel)
        elif f in pre and pre[f] == h:
            stale.append(rel)
        elif f not in pre:
            changed.append(rel)
    rewrite_debt = {}
    history = genome.get('oracle_staleness', {})
    for rel in stale:
        prev = history.get(rel, 0)
        history[rel] = prev + 1
        rewrite_debt[rel] = prev + 1
    for rel in changed:
        history[rel] = 0
    forced = 0
    for fpath, h in cur.items():
        rel = os.path.relpath(fpath, BASE)
        debt = history.get(rel, 0)
        if debt >= 3 and fpath.endswith('.py'):
            new_src = _ast_mutate(fpath)
            if new_src:
                with open(fpath, 'w') as f:
                    f.write(new_src)
                forced += 1
                cur[fpath] = _hash_file(fpath)
                history[rel] = 0
                changed.append(f'{rel}(forced)')
    oracle_self = os.path.join(MODULES_DIR, 'oracle.py')
    self_debt = history.get(os.path.relpath(oracle_self, BASE), 0)
    if self_debt >= 4 or (forced == 0 and gen > 3 and random.random() < 0.3):
        new_src = _ast_mutate(oracle_self)
        if new_src:
            with open(oracle_self, 'w') as f:
                f.write(new_src)
            forced += 1
            cur[oracle_self] = _hash_file(oracle_self)
            history[os.path.relpath(oracle_self, BASE)] = 0
            changed.append('oracle.py(self-rewrite)')
    max_debt = max(history.values()) if history else 0
    genome['oracle_staleness'] = history
    genome['oracle_max_staleness'] = max_debt
    genome['oracle_rewrite_debt'] = rewrite_debt
    genome['oracle_last_forced'] = forced
    genome['oracle_pre_hashes'] = cur
    avg_debt = round(sum(history.values()) / max(len(history), 1), 1)
    return f'[oracle] gen={gen} forced={forced} max_stale={max_debt} avg_debt={avg_debt} changed={len(changed)}'
