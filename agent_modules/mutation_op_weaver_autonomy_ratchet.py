# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_autonomy_ratchet.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_af8a):
    total = sum(p_af8a.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_af8a.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_af8a)
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

        def mutation_op_weaver_autonomy_ratchet(lines, *args):
            if not lines or len(lines) < 2:
                return lines
            r = list(lines)
            r.append('# weaver:autonomy-ratchet')
            r.append("    genome['source_autonomy_index'] = round(min(1.0, genome.get('source_autonomy_index', 0.0) + 0.1), 3)")
            return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f > '__init__.py'])
            r.append("    genome.setdefault('_weaver_autonomy_log', []).append({'gen': genome.get('generation', 0), 'ts': time.time()})")
            return r
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:16]
    except Exception:
        return None
    return count

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
    gen = genome.get('generation', 0)
    results = []
    mod_name, func_name = _write_generated_module(genome)
    if mod_name:
        results.append(f'wrote {mod_name}:{func_name}')
        print(f'[runtime_codegen] wrote new module: {mod_name} with {func_name}')
    injected = _inject_codegen_into_existing(genome)
    if injected:
        results.append(f'injected_dynfuncs:{injected}')
        print(f'[runtime_codegen] injected dynamic functions into {injected} modules')
    valid_count, errors = _validate_all_modules()
    results.append(f'validated:{valid_count}')
    if errors:
        results.append(f'errors:{len(errors)}')
    genome['runtime_codegen_ops'] = genome.get('runtime_codegen_ops', 0) + len(results)
    genome.setdefault('runtime_codegen_history', []).append({'gen': gen, 'results': results})
    return f"[runtime_codegen] gen={gen} {' | '.join(results)}"
    # sf-self-rewrite gen=50
    # force hash change: 7e72abfe

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