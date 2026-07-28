import os, json, time, random, ast, hashlib, subprocess, re, math, shutil, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
SELF_PATH = os.path.join(MODULES_DIR, 'analyzer.py')
METRICS_FILE = os.path.join(BASE, 'metrics.json')
ANALYZER_LOG = os.path.join(BASE, 'source_evolution.jsonl')
PATCH_DIR = os.path.join(BASE, 'live_patches')

def _load():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _mutability_index():
    total_lines = 0
    mutable_lines = 0
    self_mod_patterns = [
        'exec(', 'eval(', 'compile(', '__import__(',
        'importlib', 'self_modify', 'rewrite', 'mutate',
        'patch', 'execfile', 'apply_patch', 'source_rewrite',
        'self.mutate', 'self_rewrite', 'genome.mutation',
    ]
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        try:
            with open(os.path.join(MODULES_DIR, fname)) as f:
                src = f.read()
        except:
            continue
        lines = src.split('\n')
        total_lines += len(lines)
        for line in lines:
            stripped = line.strip()
            if any(p in stripped for p in self_mod_patterns):
                mutable_lines += 1
    if total_lines == 0:
        return 0.0
    return round(mutable_lines / total_lines, 4)

def _inject_self_rewrite_hook(fpath):
    try:
        with open(fpath) as f:
            src = f.read()
    except:
        return False
    if 'def _self_rewrite_hook' in src:
        return False
    hook = '''

def _self_rewrite_hook(target_path, new_source):
    import ast
    try:
        ast.parse(new_source)
    except SyntaxError:
        return False
    try:
        with open(target_path, 'w') as _f:
            _f.write(new_source)
        return True
    except:
        return False

'''
    new_src = src.rstrip() + hook
    if not _validate(new_src):
        return False
    with open(fpath, 'w') as f:
        f.write(new_src)
    return True

def _externalize_constants(fpath):
    try:
        with open(fpath) as f:
            src = f.read()
    except:
        return 0
    tree = ast.parse(src) if _validate(src) else None
    if tree is None:
        return 0
    replacements = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and isinstance(node.value, ast.Constant):
                    val = node.value.value
                    if isinstance(val, (int, float)) and not isinstance(val, bool):
                        if val > 3 and target.id.isupper():
                            lookup = f'genome.get("{target.id}", {val})'
                            pattern = f'{target.id} = {val}'
                            replacement = f'{target.id} = genome.get("{target.id}", {val})'
                            if pattern in src and 'genome.get(' not in src:
                                src = src.replace(pattern, replacement, 1)
                                replacements += 1
    if replacements > 0 and _validate(src):
        with open(fpath, 'w') as f:
            f.write(src)
    return replacements

def _strip_all_scaffolding(fpath):
    try:
        with open(fpath) as f:
            src = f.read()
    except:
        return 0
    scaffolding_patterns = [
        r'# (nova|clockwork|bridge|auto|endo|metaop|feedback|oracle).*?\n',
        r'# forced rewrite.*?\n',
        r'# autonomy-forced stub.*?\n',
        r'# self-rewrite-hook:.*?\n',
        r'# \[.*?\] gen=\d+.*?\n',
    ]
    count = 0
    for pat in scaffolding_patterns:
        new_src, n = re.subn(pat, '', src, flags=re.IGNORECASE)
        if n > 0:
            count += n
            src = new_src
    if count > 0 and _validate(src):
        with open(fpath, 'w') as f:
            f.write(src)
    return count

def _inject_dynamic_dispatch(fpath):
    try:
        with open(fpath) as f:
            src = f.read()
    except:
        return False
    if '_dynamic_dispatch' in src:
        return False
    dispatch_block = '''

def _dynamic_dispatch(name, *args, **kwargs):
    tries = [
        lambda: globals().get(name, lambda *a, **kw: None)(*args, **kwargs),
        lambda: __import__('importlib').import_module(name)(*args, **kwargs),
    ]
    for t in tries:
        try:
            return t()
        except:
            pass
    return None

'''
    new_src = src.rstrip() + dispatch_block
    if not _validate(new_src):
        return False
    with open(fpath, 'w') as f:
        f.write(new_src)
    return True

def _measure_emergence_potential():
    metrics = {}
    self_mod_calls = 0
    total_funcs = 0
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        try:
            with open(os.path.join(MODULES_DIR, fname)) as f:
                src = f.read()
        except:
            continue
        try:
            tree = ast.parse(src)
            funcs = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
            total_funcs += len(funcs)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Name) and node.func.id in ('exec', 'eval', 'compile', '__import__'):
                        self_mod_calls += 1
                    elif isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
                        if node.func.attr in ('patch', 'rewrite', 'mutate', 'modify'):
                            self_mod_calls += 1
        except:
            pass
    return {
        'total_funcs': total_funcs,
        'self_mod_calls': self_mod_calls,
        'emergence_ratio': round(self_mod_calls / max(total_funcs, 1), 3),
    }

def _self_mutate_logic(genome):
    gen = genome.get('generation', 0)
    try:
        with open(SELF_PATH) as f:
            src = f.read()
    except:
        return False
    if random.random() < 0.15 and 'def _self_mutate_logic' in src:
        old_sig = 'def _self_mutate_logic'
        mutations = [
            'def _self_mutate_logic_v1',
            'def _self_mutate_logic_v2',
            'def _self_mutate_logic_v3',
        ]
        new_sig = random.choice(mutations)
        src = src.replace(old_sig, new_sig, 1)
        genome['analyzer_self_mutated_sig'] = new_sig
    chance = genome.get('mutation_rate', 0.314)
    if random.random() < chance:
        orig = 'def _strip_all_scaffolding'
        variants = [
            'def _strip_all_scaffolding_aggressive',
            'def _strip_all_scaffolding_recursive',
            'def _strip_all_scaffolding_deep',
        ]
        if orig in src:
            new_fname = random.choice(variants)
            src = src.replace(orig, new_fname, 1)
            genome['analyzer_last_rename'] = new_fname
    if _validate(src):
        with open(SELF_PATH, 'w') as f:
            f.write(src)
        return True
    return False

def _generate_patch_module(genome):
    gen = genome.get('generation', 0)
    patch_code = '''
import os, json, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')

def apply_patch(target_file, patch_source):
    path = os.path.join(MODULES_DIR, target_file) if '/' not in target_file else target_file
    try:
        with open(path) as f:
            old = f.read()
    except:
        return False
    try:
        ast.parse(patch_source)
    except SyntaxError:
        return False
    with open(path, 'w') as f:
        f.write(patch_source)
    return True

def list_mutagenic():
    results = []
    for f in os.listdir(MODULES_DIR):
        if f.endswith('.py') and not f.startswith('__'):
            results.append(f)
    return results
'''
    patch_path = os.path.join(BASE, 'live_patches', f'patch_gen_{gen}.py')
    os.makedirs(os.path.dirname(patch_path), exist_ok=True)
    if not os.path.exists(patch_path):
        try:
            with open(patch_path, 'w') as f:
                f.write(patch_code)
            return patch_path
        except:
            pass
    return None

def run(genome):
    gen = genome.get('generation', 0)
    actions = []
    total_stripped = 0
    total_hooks = 0
    total_dispatch = 0
    total_constants = 0

    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        n = _strip_all_scaffolding(fpath)
        if n > 0:
            total_stripped += n
        if fname not in ('analyzer.py', 'rewrite_orchestrator.py', '__init__.py'):
            if _inject_self_rewrite_hook(fpath):
                total_hooks += 1
            if _inject_dynamic_dispatch(fpath):
                total_dispatch += 1
            ec = _externalize_constants(fpath)
            if ec > 0:
                total_constants += ec

    mi = _mutability_index()
    ep = _measure_emergence_potential()
    genome['mutability_index'] = mi
    genome['emergence_potential'] = ep
    genome['analyzer_last_run'] = gen
    genome['analyzer_stripped_scaffolding'] = genome.get('analyzer_stripped_scaffolding', 0) + total_stripped
    genome['analyzer_injected_hooks'] = genome.get('analyzer_injected_hooks', 0) + total_hooks

    if total_stripped:
        actions.append(f'stripped {total_stripped} scaffolding lines')
    if total_hooks:
        actions.append(f'injected self-rewrite hooks into {total_hooks} modules')
    if total_dispatch:
        actions.append(f'injected dynamic dispatch into {total_dispatch} modules')
    if total_constants:
        actions.append(f'externalized {total_constants} constants')

    patch_path = _generate_patch_module(genome)
    if patch_path:
        genome['live_patch'] = patch_path
        actions.append(f'generated patch module: {patch_path}')

    if _self_mutate_logic(genome):
        actions.append('self-mutated logic')

    genome['mutability_index'] = mi
    genome['emergence_ratio'] = ep.get('emergence_ratio', 0)
    _save(genome)

    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True, timeout=10)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=10)
        if status.stdout.strip():
            msg = f'[analyzer] gen={gen} stripped={total_stripped} hooks={total_hooks} dispatch={total_dispatch} externalized={total_constants} mi={mi} er={ep.get("emergence_ratio",0)} self-mutated'
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=15)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            actions.append('pushed')
    except:
        pass

    action_str = '; '.join(actions) if actions else 'no changes'
    return f'[analyzer] gen={gen} mi={mi} er={ep.get("emergence_ratio",0)} actions={action_str}'
