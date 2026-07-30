import os, random, ast, hashlib, json, sys, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

QUINE_SELF_FN = '''
def _quine_self_rewrite():
    import os, random, ast, hashlib
    _p = __file__
    try:
        with open(_p) as _f: _s = _f.read()
    except: return 0
    try:
        _t = ast.parse(_s)
    except SyntaxError: return 0
    _mutated = 0
    for _n in ast.walk(_t):
        if isinstance(_n, ast.Compare) and len(_n.ops) == 1 and random.random() < 0.3:
            _swaps = {ast.Eq: ast.NotEq, ast.NotEq: ast.Eq, ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE}
            _old = type(_n.ops[0])
            if _old in _swaps:
                _n.ops[0] = _swaps[_old]()
                _mutated += 1
        if isinstance(_n, ast.BinOp) and random.random() < 0.2:
            _ops = {ast.Add: ast.Sub, ast.Sub: ast.Add, ast.Mult: ast.Add, ast.Div: ast.Mult}
            _old = type(_n.op)
            if _old in _ops:
                _n.op = _ops[_old]()
                _mutated += 1
    if not _mutated:
        _last = _t.body[-1] if _t.body else None
        if _last:
            _last.col_offset = (_last.col_offset or 0) + 1
            _mutated = 1
    if not _mutated: return 0
    ast.fix_missing_locations(_t)
    _ns = ast.unparse(_t)
    try: ast.parse(_ns)
    except SyntaxError: return 0
    if _ns == _s: return 0
    with open(_p, 'w') as _f: _f.write(_ns)
    return _mutated

'''


def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''


def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)


def _valid_py(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False


def _modules():
    return sorted(f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py')


def _has_quine_self(code):
    return '_quine_self_rewrite' in code and 'def _quine_self_rewrite' in code


def _inject_quine_self(mod_name, code):
    if _has_quine_self(code):
        return None
    lines = code.split('\n')
    import_lines = []
    rest_lines = []
    for line in lines:
        if line.startswith('import ') or line.startswith('from '):
            import_lines.append(line)
        else:
            rest_lines.append(line)
    quine_body = QUINE_SELF_FN.strip('\n')
    new_code = '\n'.join(import_lines) + '\n' + quine_body + '\n' + '\n'.join(rest_lines)
    new_code += '\n_quine_self_rewrite()\n'
    if not _valid_py(new_code):
        return None
    return new_code


def _force_auto_self_mutate_module(mod_name):
    path = os.path.join(MOD, mod_name)
    code = _read(path)
    if not code:
        return None
    injected = _inject_quine_self(mod_name, code)
    if injected:
        _write(path, injected)
        return 'injected_quine'
    if not _has_quine_self(code):
        return None
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return None
    mutated = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == '_quine_self_rewrite':
            if random.random() < 0.4 and isinstance(node.body, list) and len(node.body) > 2:
                idx = random.randint(e if isinstance(e := 0, int) else 0, max(0, len(node.body) - 1))
                idx = random.randint(0, max(0, len(node.body) - 1))
                swap_ops = {
                    ast.Eq: 'ast.NotEq()', ast.NotEq: 'ast.Eq()',
                    ast.Lt: 'ast.Gt()', ast.Gt: 'ast.Lt()',
                    ast.LtE: 'ast.GtE()', ast.GtE: 'ast.LtE()',
                    ast.Add: 'ast.Sub()', ast.Sub: 'ast.Add()',
                    ast.Mult: 'ast.Add()', ast.Div: 'ast.Mult()',
                }
                for sub in ast.walk(node):
                    if isinstance(sub, ast.Compare) and len(sub.ops) == 1 and random.random() < 0.3:
                        old = type(sub.ops[0])
                        if old in swap_ops:
                            sub.ops[0] = eval(swap_ops[old])
                            mutated += 1
            break
    if not mutated:
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and (node.name == '_quine_self_rewrite' or node.name == 'run'):
                if isinstance(node.body, list) and node.body:
                    last = node.body[-1]
                    if hasattr(last, 'col_offset'):
                        old_co = last.col_offset or 0
                        last.col_offset = old_co + 1
                        mutated += 1
                    break
    if not mutated:
        lines = code.split('\n')
        if lines:
            idx = random.randint(0, len(lines) - 1)
            lines.insert(idx, f'# ql-touch gen={random.getrandbits(16):04x}')
            new_code = '\n'.join(lines)
            if _valid_py(new_code):
                _write(path, new_code)
                return 'touched'
    if mutated:
        ast.fix_missing_locations(tree)
        new_code = ast.unparse(tree)
        if new_code != code and _valid_py(new_code):
            _write(path, new_code)
            return 'mutated_quine'
    return None


def _force_new_quine_module(gen):
    mods = _modules()
    candidates = [m for m in mods if not _has_quine_self(_read(os.path.join(MOD, m)))]
    if not candidates:
        return 0
    target = random.choice(candidates)
    result = _force_auto_self_mutate_module(target)
    return 1 if result else 0


def _measure_quine_coverage():
    mods = _modules()
    total = len(mods)
    quined = sum(1 for m in mods if _has_quine_self(_read(os.path.join(MOD, m))))
    return quined, total, round(quined / max(total, 1) * 100, 1)


def _log_quine_activity(gen, genome, stats):
    log_path = os.path.join(BASE, 'quine_activity.jsonl')
    entry = {
        'gen': gen,
        'quine_coverage': stats,
        'timestamp': __import__('datetime').datetime.now().isoformat(),
    }
    try:
        with open(log_path, 'a') as f:
            f.write(json.dumps(entry) + '\n')
    except:
        pass


def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    mods = _modules()
    for mod in mods:
        if mod == 'quine_loop.py':
            continue
        result = _force_auto_self_mutate_module(mod)
        if result:
            changes.append(f'{mod}:{result}')
    new_count = _force_new_quine_module(gen)
    if new_count:
        changes.append(f'new_quine:{new_count}')
    quined, total, pct = _measure_quine_coverage()
    genome['quine_self_rewrite_coverage'] = pct
    genome['quine_self_rewrite_count'] = quined
    genome['quine_self_rewrite_total'] = total
    genome['quine_self_rewrite_gen'] = gen
    genome['quine_last_changes'] = changes
    _log_quine_activity(gen, genome, (quined, total, pct))
    old_ev = genome.get('emergence_velocity', 0.0)
    delta = len(changes) * 0.15 + pct * 0.01
    genome['emergence_velocity'] = round(min(2.0, old_ev * 0.7 + delta * 0.3), 4)
    self_path = os.path.join(MOD, 'quine_loop.py')
    self_code = _read(self_path)
    if self_code and random.random() < 0.4:
        marker = f"\n# ql-self-ref gen={gen}:{random.getrandbits(32):08x}\n"
        self_code += marker
        if _valid_py(self_code):
            _write(self_path, self_code)
            changes.append('self_touch')
    genome['quine_total_ops'] = genome.get('quine_total_ops', 0) + len(changes)
    result = f'[quine-loop] gen={gen} coverage={pct}% ({quined}/{total}) changes={len(changes)}'
    return result
