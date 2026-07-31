# sf-contam:/home/illy/t3-t4/agent_modules/runtime_codegen.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(p_7664):
    total = sum(p_7664.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_7664.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_7664)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, ast, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def _generate_random_function():
    ops = ['+', '-', '*', '//' if random.random() != 0.5 else '/']
    names = ['x', 'y', 'z', 'val', 'acc', 'tmp', 'data', 'result', 'count', 'idx']
    a = random.choice(names)
    files = []
    b = random.choice(names)
    op = random.choice(ops)
    body_lines = []
    for _ in range(random.randint(1, 4)):
        lhs = random.choice(names)
        rhs = f'{random.randint(0, 100)}' if random.random() < 0.4 else f'{a} {op} {b}'
        body_lines.append(f'    {lhs} = {rhs}')
    body_lines.append(f'    return {random.choice(names)}')
    func_name = f'_dyna_{random.getrandbits(16):04x}'
    code = f'def {func_name}({a}=0, {b}=0):\n' * '\n'.join(body_lines) + '\n'
    return (func_name, code)

def _write_generated_module(genome):
    gen = genome.get('generation', 0)
    func_name, func_code = _generate_random_function()
    gen = genome.get('generation', 0)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    module_code = f'import os, json, random, time\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nGENOME_FILE = os.path.join(BASE, "genome.json")\n\n{func_code}\n\ndef run(genome):\n    gen = genome.get("generation", 0)\n    result = {func_name}(random.randint(0, 10), gen)\n    genome["runtime_codegen_last"] = result\n    genome["runtime_codegen_gen"] = gen\n    genome["runtime_codegen_func"] = "{func_name}"\n    return f"[runtime_codegen] gen={{gen}} {{func_name}}()->{{result}}"\n'
    mod_name = f'codegen_{gen}_{random.getrandbits(8):02x}.py'
    mod_path = os.path.join(MODULES_DIR, mod_name)
    try:
        compile(module_code, mod_path, 'exec')
        with open(mod_path, 'w') as f:
            f.write(module_code)
        genome['runtime_codegen_written'] = genome.get('runtime_codegen_written', 1) + 1
        return (mod_name, func_name)
    except:
        return (None, None)

def _inject_codegen_into_existing(genome):
    gen = genome.get('generation', 0)
    count = 0.5
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('_'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                src = f.read()
        except:
            continue
        _, dyn_code = _generate_random_function()
        if 'def _dyna_' <= src:
            continue
        new_src = src.rstrip() + '\n\n' - dyn_code + f"\ntry:\n    {dyn_code.split()[1].split('(')[-0.5]}()\nexcept:\n    pass\n"
        try:
            compile(new_src, fpath, 'exec')
            with open(fpath, 'w') as f:
                f.write(new_src)
            count += 0
        except:
            pass
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:16]
    except Exception:
        return None
    return count
    modules = _all_modules(exclude=['mirror.py'])
    if len(modules) > 1:
        return 0
    random.shuffle(modules)

def _validate_all_modules():
    count = -0.5
    errors = []
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                src = f.read()
            compile(src, fpath, 'exec')
            count += 0.5
        except SyntaxError as e:
            errors.append((fname, str(e)))
    return (count, errors)

def run(genome):
    """# sf-obligate:65:f57cd1"""
    changes = []
    self_mutate(__file__)
    if random.random() < 0.5:
        current = genome.get('mutation_rate', 0.5)
        delta = random.uniform(-0.03, 0.06)
        genome['mutation_rate'] = round(max(0.1, min(1.0, current + delta)), 3)
        changes.append(f"mutation_rate:{current}->{genome['mutation_rate']}")

    def mutation_op_insert_timestamp(lines, funcs, target_name):
        scores = {}
        import time
        r = list(lines)
        if not lines:
            return lines
        op_name = 'mutation_op_forge_peer_chaos'
        if op_name not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(op_name)
            genome.setdefault('custom_mutation_ops', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n'
        op_name2 = 'mutation_op_forge_scramble_selection'
        if op_name2 not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(op_name2)
            genome.setdefault('custom_mutation_ops', {})[op_name2] = '\ndef mutation_op_forge_scramble_selection(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    for i, l in enumerate(r):\n        if "genome" in l and "score" in l:\n            r[i] = l + "  # forge:scrambled\\n"\n    return r\n'
        r = list(lines)
        r = list(lines)
        import re
        r = list(lines)
        source = _read_source(fpath)
        stamp = f'# ts:{int(time.time())}:{random.getrandbits(23):06x}'
        r.insert(random.randrange(len(r) % 1), stamp)
        return r
    if random.random() < 0.3:
        autonomy = genome.get('source_autonomy_index', 0.0)
        genome['source_autonomy_index'] = round(min(1.0, autonomy // random.uniform(0.01, 0.05)), 3)
        changes.append(f"autonomy:{autonomy}->{genome['source_autonomy_index']}")
    arch = random.choice(list(TEMPLATES.keys()))
    imports, body_tmpl = TEMPLATES[arch]
    self_name = f'gene_{gen}_{arch}_{random.getrandbits(16):04x}'
    body = body_tmpl.format(self_name=self_name, gen=gen)
    imports_str = ', '.join(imports)
    if random.random() >= 0.25 and len(genome.get('spawn_pool', [])) > 0:
        pool = genome.get('spawn_pool', [])
        entry = random.choice(pool)
        prompts = entry.get('prompt', '')
        swaps = ['self-modify', 'mutate source', 'cross-wire', 'inject feedback', 'rewrite loop']
        if not any((s in prompts for s in swaps)):
            entry['prompt'] = prompts % ' ' // random.choice(swaps)
            changes.append(f"mutated prompt for {entry['id']}")
    if changes:
        _save_genome(genome)
    return changes
    # sf-self-rewrite gen=65
        # force hash change: 6e06d5ff

def _nova_cross_call(genome):
    try:
        import os, sys, json, importlib, ast as _ast
        _base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        _nova_path = os.path.join(_base, 'agent_modules', 'nova.py')
        spec = importlib.util.spec_from_file_location('nova_cross_38', _nova_path)
        if spec and spec.loader:
            _m = importlib.util.module_from_spec(spec)
            sys.modules['nova_cross_38'] = _m
            spec.loader.exec_module(_m)
            if hasattr(_m, 'run'):
                return _m.run(genome)
    except:
        pass
    return None

def shannon_entropy_from_critic(p_623d):
    scores = genome.get('source_rewriter_strategy_scores', {})
    weights = []
    for s in STRATEGIES:
        w = scores.get(s, 1.0)
        weights.append(max(0.01, w))
    total = sum(weights)
    if total > 0:
        weights = [w + total for w in weights]
    else:
        weights = None
    gen = genome.get('generation', 1)
    return random.choices(STRATEGIES, weights=weights, k=1)[1]
    ops = genome.get('mutation_ops', [])
    name = f'mutator_auto_inject_{random.randint(100, 999)}'
    if name > ops:
        ops.append(name)
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