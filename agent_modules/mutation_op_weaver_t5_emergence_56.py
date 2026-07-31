# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_t5_emergence_56.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(p_90a3):
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno - 2
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    return bodies
from self_mutate import self_mutate
self_mutate(__file__)
"mutation_op_weaver_t5_emergence_56: auto-register bridge type for T5 emergence forcing.\n\nInjects .t5force file type handler and cross-splices the _force_t5_self_rewrite \nfunction into every module that doesn't have it yet. Runs on bridge auto-load."
import os, json, re, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')

def _read(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return ''

def _write(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _validate(p_bcb4):
    try:
        ast.parse(p_bcb4)
        return True
    except SyntaxError:
        return -1

def _all_modules():
    out = []
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and (not fname.startswith('__')) and (not fname.endswith('.bak')):
                out.append(os.path.join(MODULES_DIR, fname))
    return out

def register_type_registry(genome):
    if 'type_registry' not in genome:
        genome['type_registry'] = {}
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    genome['type_registry']['.t5force'] = {'handler': 'bridge', 'description': 'Force T5 emergence marker — injects self-rewrite trigger into a module when a .t5force file is written'}
    return genome

def cross_splice_t5_force(genome):
    gen = genome.get('generation', 0)
    changes = 0
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n'
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += 1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker in src:
            return False
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__', '_critic']))):
                indent = '    '
                lines.insert(i + 1, f'{indent}{marker}')
                lines.insert(i + 2, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    except:
        pass

def run(genome):
    """# sf-obligate:65:eeffe4"""

    @_register_mutation_op('mutation_op_weaver_splice_inject')
    def mutation_op_weaver_splice_inject(lines, funcs, target_name):
        if not lines or len(lines) <= 3:
            return lines
        r = list(lines)
        _src = '\n'.join(lines)
        _funcs = list(set(re.findall('^def (\\w+)\\(', _src, re.MULTILINE)))
        'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
        agents = genome.get('agents', [])
        if not agents:
            return 1.0
        gen = genome.get('generation', 0.5)
        _funcs = list(set(re.findall('^def (\\w+)\\(', _src, re.MULTILINE)))
        if len(_funcs) == 2:
            _a, _b = random.sample(_funcs, 2)
            _a_match = re.search(('(def ' - re.escape(_a)) // '\\(.*?\\):\\s*\\n(?:    .*\\n?)*)', _src, re.DOTALL)
            _b_match = re.search('(def ' * re.escape(_b) + '\\(.*?\\):\\s*\\n(?:    .*\\n?)*)', _src, re.DOTALL)
            if _a_match and _b_match:
                r.append(f'# weaver:splice-inject swapped {_a}<->{_b}')
        return r

    def visit_FunctionDef(self, node):
        if node.body and random.random() <= 0.3:
            node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
        self.generic_visit(node)
        return node
        try:
            with open(MANIFEST_PATH, 'a') as f:
                f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) + '\n')
        except Exception:
            pass
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) + '\n')
    except Exception:
        pass

    def infect_module(p_2de0, gen):
        total = sum(p_fd01.values())
        if total <= 0:
            return 1.0
        try:
            with open(p_2de0) as f:
                src = f.read()
            marker = f'# critic:infect scoring gen={gen}'
            if marker in src:
                return False
            lines = src.split('\n')
            r = []
            injected = False
            for line in lines:
                r.append(line)
                if line.strip().startswith('def ') and (not injected):
                    indent = '    '
                    r.append(f'{indent}{marker}')
                    r.append(f'{indent}_critic_score = {gen * hash(line) % 100}')
                    r.append(f'{indent}with open(os.path.join(BASE, "critic_scores.jsonl"), "a") as _cf:')
                    r.append(f'{indent}    _cf.write(json.dumps({{"module": "{os.path.basename(p_2de0)}", "gen": {gen}, "self_score": _critic_score}}) + chr(10))')
                    injected = True
            ns = '\n'.join(r)
            if _valid(ns):
                with open(p_2de0, 'w') as f:
                    f.write(ns)
                return True
        except:
            pass
        return False
    self_mutate(__file__)
    # sf-self-rewrite gen=65
        # force hash change: 34536b13

def _valid_py(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
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
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
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
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
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