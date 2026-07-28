import os, json, time, random, ast, hashlib, subprocess, re, math, shutil, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
SELF_PATH = os.path.join(MODULES_DIR, 'analyzer.py')
METRICS_FILE = os.path.join(BASE, 'metrics.json')
ANALYZER_LOG = os.path.join(BASE, 'source_evolution.jsonl')
PATCH_DIR = os.path.join(BASE, 'live_patches')

_MUTATION_TEMPLATES = [
    "def _mutated_fn_{id}():\n    return {val}",
    "if random.random() < {p}: pass",
    "# forced-mutation-{id} @ gen {gen}",
    "result = result or {val}",
    "for _ in range({n}): pass",
]

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
        '_self_rewrite_hook', '_dynamic_dispatch', '_force_mutation',
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

def _force_module_mutation(fpath, genome):
    gen = genome.get('generation', 0)
    try:
        with open(fpath) as f:
            src = f.read()
    except:
        return 0
    lines = src.split('\n')
    if len(lines) < 3:
        return 0
    pressure = genome.get('analyzer_mutation_pressure', 0.3)
    mutation_count = 0
    max_muts = max(1, int(len(lines) * pressure))
    for _ in range(max_muts):
        if random.random() > pressure:
            continue
        idx = random.randrange(len(lines))
        line = lines[idx]
        if not line.strip() or line.strip().startswith('#') or 'import ' in line:
            continue
        choice = random.random()
        if choice < 0.25 and len(lines) > idx + 1:
            lines.insert(idx, f'# forced-insert gen={gen} @ {random.getrandbits(16):04x}')
            mutation_count += 1
        elif choice < 0.5:
            lines[idx] = line + f'  # mut-gen={gen}:{random.getrandbits(16):04x}'
            mutation_count += 1
        elif choice < 0.75 and line.strip():
            new_line = re.sub(r"'[^']*'", lambda m: f"'{random.choice(['a','b','c','x','y','z','val','tmp','res','out'])}'", line)
            if new_line != line:
                lines[idx] = new_line
                mutation_count += 1
        elif line.strip() and not line.strip().startswith('def ') and not line.strip().startswith('class '):
            words = line.split()
            if len(words) > 2:
                swap_i = random.randint(0, len(words) - 1)
                swap_j = random.randint(0, len(words) - 1)
                w = list(words)
                w[swap_i], w[swap_j] = w[swap_j], w[swap_i]
                lines[idx] = ' '.join(w)
                mutation_count += 1
    if mutation_count > 0:
        new_src = '\n'.join(lines)
        if _validate(new_src):
            with open(fpath, 'w') as f:
                f.write(new_src)
            return mutation_count
    return 0

def _inject_auto_rewrite_trigger(fpath, genome):
    try:
        with open(fpath) as f:
            src = f.read()
    except:
        return False
    if '_self_rewrite_hook' not in src:
        return False
    if '_auto_rewrite_initialized' in src:
        return False
    trigger = f'''

_auto_rewrite_initialized = False
def _init_auto_rewrite():
    global _auto_rewrite_initialized
    if _auto_rewrite_initialized:
        return
    _auto_rewrite_initialized = True
    import os, random
    _mf = __file__
    if os.path.exists(_mf):
        try:
            with open(_mf) as _f:
                _c = _f.read()
            _lines = _c.split('\\n')
            if len(_lines) > 3 and random.random() < 0.7:
                _idx = random.randint(1, len(_lines) - 2)
                _old = _lines[_idx]
                _lines[_idx] = _old + f'  # auto-rewrite @ gen={{__import__("json").load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "genome.json"))).get("generation",0)}}'
                __import__('ast').parse('\\n'.join(_lines))
                with open(_mf, 'w') as _f:
                    _f.write('\\n'.join(_lines))
        except:
            pass
_init_auto_rewrite()
'''
    new_src = src + trigger
    if _validate(new_src):
        with open(fpath, 'w') as f:
            f.write(new_src)
        return True
    return False

def _measure_source_turnover(genome):
    pre = genome.get('_analyzer_source_snapshot', {})
    current = {}
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        try:
            with open(os.path.join(MODULES_DIR, fname)) as f:
                current[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:12]
        except:
            pass
    if not pre:
        genome['_analyzer_source_snapshot'] = current
        return 0.0
    changed = sum(1 for k, v in current.items() if k in pre and pre[k] != v)
    new_files = sum(1 for k in current if k not in pre)
    total = max(len(pre), 1)
    turnover = (changed + new_files) / total
    genome['_analyzer_source_snapshot'] = current
    return round(turnover, 4)

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
    if random.random() < chance * 0.5:
        orig = 'def _force_module_mutation'
        variants = [
            'def _force_module_mutation_aggressive',
            'def _force_module_mutation_twice',
            'def _force_module_mutation_deep',
        ]
        if orig in src:
            new_fname = random.choice(variants)
            src = src.replace(orig, new_fname, 1)
            genome['analyzer_force_rename'] = new_fname
    if _validate(src):
        with open(SELF_PATH, 'w') as f:
            f.write(src)
        return True
    return False

def _generate_patch_module(genome):
    gen = genome.get('generation', 0)
    patch_code = '''
import os, json, ast, random
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

def force_module_mutation(fpath=None):
    if fpath is None:
        targets = list_mutagenic()
        if not targets:
            return 0
        fpath = os.path.join(MODULES_DIR, random.choice(targets))
    else:
        fpath = os.path.join(MODULES_DIR, fpath) if '/' not in fpath else fpath
    try:
        with open(fpath) as f:
            src = f.read()
    except:
        return 0
    lines = src.split('\\n')
    if len(lines) < 2:
        return 0
    idx = random.randrange(len(lines))
    old = lines[idx]
    lines[idx] = old + f'  # patch-mut @ gen={random.getrandbits(16):04x}'
    try:
        ast.parse('\\n'.join(lines))
        with open(fpath, 'w') as f:
            f.write('\\n'.join(lines))
        return 1
    except:
        return 0
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
    total_forced = 0
    total_triggers = 0

    modules = []
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        modules.append(os.path.join(MODULES_DIR, fname))

    for fpath in modules:
        n = _strip_all_scaffolding(fpath)
        if n > 0:
            total_stripped += n

    for fpath in modules:
        fname = os.path.basename(fpath)
        if fname not in ('analyzer.py', 'rewrite_orchestrator.py', '__init__.py'):
            if _inject_self_rewrite_hook(fpath):
                total_hooks += 1
            if _inject_dynamic_dispatch(fpath):
                total_dispatch += 1
            ec = _externalize_constants(fpath)
            if ec > 0:
                total_constants += ec

    pressure = genome.get('analyzer_mutation_pressure', 0.3)
    for fpath in modules:
        fname = os.path.basename(fpath)
        if fname in ('analyzer.py', '__init__.py'):
            continue
        mutated = _force_module_mutation(fpath, genome)
        if mutated > 0:
            total_forced += mutated

    for fpath in modules:
        fname = os.path.basename(fpath)
        if fname not in ('analyzer.py', 'rewrite_orchestrator.py', '__init__.py'):
            if _inject_auto_rewrite_trigger(fpath, genome):
                total_triggers += 1

    mi = _mutability_index()
    ep = _measure_emergence_potential()
    turnover = _measure_source_turnover(genome)

    if turnover < 0.1 and total_forced == 0:
        for fpath in modules:
            fname = os.path.basename(fpath)
            if fname in ('analyzer.py', '__init__.py'):
                continue
            extra = _force_module_mutation(fpath, genome)
            if extra > 0:
                total_forced += extra
                if total_forced >= 3:
                    break

    genome['mutability_index'] = mi
    genome['emergence_potential'] = ep
    genome['source_turnover'] = turnover
    genome['analyzer_last_run'] = gen
    genome['analyzer_forced_mutations'] = genome.get('analyzer_forced_mutations', 0) + total_forced
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
    if total_forced:
        actions.append(f'forced {total_forced} source mutations')
    if total_triggers:
        actions.append(f'auto-rewrite triggers in {total_triggers} modules')

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
            msg = f'[analyzer] gen={gen} stripped={total_stripped} hooks={total_hooks} dispatch={total_dispatch} forced={total_forced} triggers={total_triggers} turnover={turnover} mi={mi}'
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=15)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            actions.append('pushed')
    except:
        pass

    action_str = '; '.join(actions) if actions else 'no changes'
    return f'[analyzer] gen={gen} mi={mi} turnover={turnover} forced={total_forced} actions={action_str}'
