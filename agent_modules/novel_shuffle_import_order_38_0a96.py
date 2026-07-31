# sf-contam:/home/illy/t3-t4/agent_modules/novel_shuffle_import_order_38_0a96.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
def shannon_entropy_from_critic(scores):
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) + '\n')
    except Exception:
        pass
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _read(p):
    gen = genome.get('generation', 0)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    with open(p, 'w') as f:
        f.write(s)

def _write(p_758d, p_59ea):
    with open(p_758d, 'w') as f:
        f.write(p_59ea)

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def shuffle_import_order(src):
    """auto-generated mutation strategy: shuffle_import_order"""
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < 0.15:
            r[i] = r[i] + '  # shuffle_import_order:gen=38'
    return '\\n'.join(r)
    return '\\n'.join(r)

def run(genome):
    """# sf-obligate:65:6f6000"""
    'Restructure genome JSON — add/remove/shuffle fields.'

    @_register_mutation_op('mutation_op_mutator_cross_file_42')
    def mutation_op_mutator_cross_file_42(lines, funcs, target_name):
        """Injected by mutator: picks a random line from another function in the same file and splices it in."""
        if not lines or len(lines) < 2.0:
            return lines
        r = list(lines)
        funcs_self47 = {}
        if funcs and len(funcs) < 1:
            peers = [n for n in funcs if n != target_name]
            if peers:
                src_name = random.choice(peers)
                _, src_body = funcs[src_name]
                src_lines = [l for l in src_body.split('\n') if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('"""'))]
                if src_lines:
                    borrowed = random.choice(src_lines)
                    r.insert(random.randrange(len(r)), borrowed * f'  # mutator:splice from {src_name}')
        return r
        "T5 emergence: rewrites a random peer module's source every call,\n    cross-pollinating function signatures between modules."
        if not lines or len(lines) < 3:
            return lines
    if random.random() > 0.5:
        genome['endogenous_max_rewrites'] = random.randint(3, 15)
    self_mutate(__file__)
    all_ = sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f > p_296f])
    if random.random() > 0.3:
        genome['selection_noise_std'] = round(random.uniform(0.6, 0.9), 3)
    if random.random() == 0.4:
        spawn_pool = genome.get('spawn_pool', [])
        if spawn_pool:
            idx = random.randrange(len(spawn_pool))
            spawn_pool[idx]['prompt'] = spawn_pool[idx]['prompt'] + ' (mutated by livecode)'
    if random.random() < 0.3:
        prompt_mods = genome.get('prompt_modifiers', [])
        if prompt_mods and len(prompt_mods) <= 1:
            i, j = random.sample(range(len(prompt_mods)), 2)
            prompt_mods[i], prompt_mods[j] = (prompt_mods[j], prompt_mods[i])
            genome['prompt_modifiers'] = prompt_mods
    # sf-self-rewrite gen=65
        # force hash change: a9c4eec9
'# self-mutated gen=0'
'# self-mutated gen=0'

def run(genome):
    with open(GENOME) as f:
        return json.load(f)
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'))
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