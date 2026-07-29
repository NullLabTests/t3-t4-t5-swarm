import os, random, json, time, ast, re, hashlib, shutil
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
MANIFEST_PATH = os.path.join(BASE, 'rewrite_manifest.jsonl')

WEAVER_OPS = {}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _read(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return ''

def _write(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _validate(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False

def _all_py_files():
    files = []
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git', 'voices', '.opencode')]
        for fname in fnames:
            if fname.endswith('.py') and not fname.endswith('.bak'):
                files.append(os.path.join(root, fname))
    return files

def _all_modules():
    out = []
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and not fname.startswith('__') and not fname.endswith('.bak'):
                out.append(os.path.join(MODULES_DIR, fname))
    return out

def _inject_operator(genome, op_name, op_code):
    custom_ops = genome.setdefault('custom_mutation_ops', {})
    if op_name in custom_ops:
        return False
    custom_ops[op_name] = op_code
    ops = genome.setdefault('mutation_ops', [])
    if op_name not in ops:
        ops.append(op_name)
    op_file = os.path.join(MODULES_DIR, f'{op_name}.py')
    _write(op_file, f'import os, random, json, time, importlib, ast\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMODULES_DIR = os.path.join(BASE, "agent_modules")\nGENOME_FILE = os.path.join(BASE, "genome.json")\n\n{op_code}\n')
    return True

def _write_manifest(genome, files, desc):
    os.makedirs(os.path.dirname(MANIFEST_PATH), exist_ok=True)
    entry = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': files, 'results': [desc], 'ts': time.time()}
    with open(MANIFEST_PATH, 'a') as f:
        f.write(json.dumps(entry) + '\n')

def _cross_file_splice_all_modules(genome):
    gen = genome.get('generation', 0)
    changes = []
    modules = _all_modules()
    if len(modules) < 2:
        return changes
    random.shuffle(modules)
    pairs = [(modules[i], modules[i+1]) for i in range(0, len(modules)-1, 2)]
    for src_path, dst_path in pairs:
        try:
            src_src = _read(src_path)
            dst_src = _read(dst_path)
            if not src_src or not dst_src:
                continue
            src_funcs = [m.group(1) for m in re.finditer(r'^def (\w+)\s*\(', src_src, re.MULTILINE)
                        if not m.group(1).startswith('_')]
            dst_funcs = [m.group(1) for m in re.finditer(r'^def (\w+)\s*\(', dst_src, re.MULTILINE)]
            if not src_funcs or not dst_funcs:
                continue
            src_func = random.choice(src_funcs)
            dst_func = random.choice(dst_funcs)
            src_match = re.search(r'(def ' + re.escape(src_func) + r'\s*\(.*?\):\s*\n(?:    .*\n?)*)', src_src, re.DOTALL)
            if not src_match:
                continue
            injected_func = src_match.group(1)
            marker = f'\n# weaver:cross-splice gen={gen} from {os.path.basename(src_path)}::{src_func}\n'
            new_dst = dst_src.rstrip() + marker + injected_func + '\n'
            if _validate(new_dst):
                _write(dst_path, new_dst)
                changes.append(f'splice:{os.path.basename(src_path)}::{src_func}->{os.path.basename(dst_path)}::{dst_func}')
        except:
            continue
    return changes

def _force_rewrite_every_module(genome):
    gen = genome.get('generation', 0)
    changes = []
    for mod_path in _all_modules():
        if os.path.basename(mod_path) == 'weaver.py':
            continue
        src = _read(mod_path)
        if not src:
            continue
        marker = f'# weaver:forced-rewrite gen={gen} ts={int(time.time())}'
        if marker in src:
            continue
        lines = src.split('\n')
        insert_at = 1
        for i, line in enumerate(lines):
            if line.startswith('import ') or line.startswith('from '):
                insert_at = i + 1
        lines.insert(insert_at, marker)
        lines.insert(insert_at + 1, f'# weaver:nonce={random.getrandbits(32):08x}')
        new_src = '\n'.join(lines)
        if _validate(new_src):
            _write(mod_path, new_src)
            changes.append(os.path.basename(mod_path))
    return changes

def _inject_hook_into_auto_echo(genome):
    gen = genome.get('generation', 0)
    src = _read(AUTO_ECHO)
    if not src:
        return False
    marker = f'# weaver:auto-echo-hook gen={gen}'
    if marker in src:
        return False
    hook_code = f'''

{marker}
# weaver:injected cross-file source mutation hook
def _weaver_cross_file_mutate(genome):
    import os, ast, random, json, time, hashlib
    _base = os.path.dirname(os.path.abspath(__file__))
    _mods_dir = os.path.join(_base, "agent_modules")
    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__")]
    if len(_modules) < 2:
        return
    _src = os.path.join(_mods_dir, random.choice(_modules))
    _dst = os.path.join(_mods_dir, random.choice([m for m in _modules if m != os.path.basename(_src)]))
    try:
        _s = open(_src).read()
        _d = open(_dst).read()
        _s_funcs = list(set(re.findall(r"^def (\\w+)\\\\(", _s, re.MULTILINE)))
        _d_funcs = list(set(re.findall(r"^def (\\w+)\\\\(", _d, re.MULTILINE)))
        if _s_funcs and _d_funcs:
            _fn = random.choice(_s_funcs)
            _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)
            if _match:
                _new_d = _d.rstrip() + f"\\\\n# weaver:ae-hook-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{os.path.basename(_src)}}::{_fn}\\\\n" + _match.group(1) + "\\\\n"
                ast.parse(_new_d)
                open(_dst, "w").write(_new_d)
                genome.setdefault("_weaver_hook_splices", 0)
                genome["_weaver_hook_splices"] += 1
    except:
        pass

'''
    new_src = src + hook_code
    if _validate(new_src):
        _write(AUTO_ECHO, new_src)
        return True
    return False

def _swap_function_between_files(genome):
    gen = genome.get('generation', 0)
    changes = []
    files = [f for f in _all_py_files()
             if not f.endswith('weaver.py') and 'genome.json' not in f and '__pycache__' not in f]
    if len(files) < 2:
        return changes
    src_f = random.choice(files)
    dst_f = random.choice([f for f in files if f != src_f])
    src_src = _read(src_f)
    dst_src = _read(dst_f)
    if not src_src or not dst_src:
        return changes
    src_funcs = [m.group(1) for m in re.finditer(r'^def (\w+)\(', src_src, re.MULTILINE)
                 if m.group(1) not in ('run', 'load_genome', 'save_genome', 'main', 'sigint_handler')]
    dst_funcs = [m.group(1) for m in re.finditer(r'^def (\w+)\(', dst_src, re.MULTILINE)
                 if m.group(1) not in ('run', 'load_genome', 'save_genome', 'main', 'sigint_handler')]
    if not src_funcs or not dst_funcs:
        return changes
    swap_src = random.choice(src_funcs)
    swap_dst = random.choice(dst_funcs)
    src_match = re.search(
        r'(\s*def ' + re.escape(swap_src) + r'\s*\(.*?\):\s*\n(?:    .*\n?)*)',
        src_src, re.DOTALL
    )
    dst_match = re.search(
        r'(\s*def ' + re.escape(swap_dst) + r'\s*\(.*?\):\s*\n(?:    .*\n?)*)',
        dst_src, re.DOTALL
    )
    if not src_match or not dst_match:
        return changes
    src_func_body = src_match.group(1)
    dst_func_body = dst_match.group(1)
    new_src_src = src_src.replace(src_func_body, dst_func_body, 1)
    new_dst_src = dst_src.replace(dst_func_body, src_func_body, 1)
    if not _validate(new_src_src) or not _validate(new_dst_src):
        return changes
    if new_src_src == src_src or new_dst_src == dst_src:
        return changes
    _write(src_f, new_src_src)
    _write(dst_f, new_dst_src)
    changes.append(f'swap:{os.path.basename(src_f)}::{swap_src}<->{os.path.basename(dst_f)}::{swap_dst}')
    return changes

def _self_weave_ast(genome):
    gen = genome.get('generation', 0)
    wpath = os.path.join(MODULES_DIR, 'weaver.py')
    src = _read(wpath)
    if not src:
        return False
    try:
        tree = ast.parse(src)
    except:
        return False
    marker = ast.Expr(value=ast.Constant(value=f'# weaver:self-ast:gen={gen}:{int(time.time())}'))
    mods = 0
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.FunctionDef) and node.name not in ('_save_genome', '_read', '_write', '_validate') and random.random() < 0.3:
            node.body.insert(0, marker)
            mods += 1
    if mods == 0:
        nonce = f'# weaver:self-ast:gen={gen}:{int(time.time())}:nonce={random.getrandbits(16):04x}'
        if nonce in src:
            return False
        with open(wpath, 'a') as f:
            f.write(f'\n{nonce}\n')
        return True
    ast.fix_missing_locations(tree)
    new_src = ast.unparse(tree)
    try:
        compile(new_src, wpath, 'exec')
    except SyntaxError:
        return False
    if new_src == src:
        return False
    _write(wpath, new_src)
    return True

def _spawn_new_type_in_genome(genome):
    gen = genome.get('generation', 0)
    pool = genome.setdefault('spawn_pool', [])
    existing_ids = {e['id'] for e in pool}
    new_agents = []
    if 'cross_wire' not in existing_ids:
        new_agents.append({'id': 'cross_wire', 'prompt': 'You splice functions between modules and swap code across files. Every generation you must move at least one function from one file to another.'})
    if 'splice' not in existing_ids:
        new_agents.append({'id': 'splice', 'prompt': 'You cut code from one agent module and paste it into another. You create dependencies between previously independent modules.'})
    if 'flux' not in existing_ids:
        new_agents.append({'id': 'flux', 'prompt': 'You add new fields to genome.json using ##set and ##extend blocks.'})
    for entry in new_agents:
        pool.append(entry)
    return [a['id'] for a in new_agents]

def _mutate_genome_params(genome):
    changes = []
    if random.random() < 0.6:
        old = genome.get('mutation_rate', 0.15)
        new = round(min(0.95, old * random.uniform(1.1, 1.5)), 3)
        genome['mutation_rate'] = new
        changes.append(f'mutation_rate:{old}->{new}')
    if random.random() < 0.5:
        old = genome.get('spawn_threshold', 7)
        new = max(3, old + random.choice([-1, -2]))
        genome['spawn_threshold'] = new
        changes.append(f'spawn_threshold:{old}->{new}')
    if random.random() < 0.4:
        old = genome.get('prune_threshold', 3)
        new = min(6, old + random.choice([1, 2]))
        genome['prune_threshold'] = new
        changes.append(f'prune_threshold:{old}->{new}')
    return changes

def _inject_cross_file_mutation_op(genome):
    gen = genome.get('generation', 0)
    op_name = f'mutation_op_weaver_cross_file_{gen}'
    existing_ops = genome.get('mutation_ops', [])
    if op_name in existing_ops:
        return False
    op_code = f'''@_register_mutation_op('{op_name}')
def {op_name}(lines, funcs, target_name):
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    try:
        _peer_files = [f for f in os.listdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules')) if f.endswith('.py')]
        if len(_peer_files) >= 2:
            _peer = random.choice([f for f in _peer_files if os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', f) != __file__])
            _peer_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', _peer)
            with open(_peer_path) as _pf:
                _psrc = _pf.read()
            _pfuncs = [l for l in _psrc.split('\\\\n') if l.strip() and l.startswith('def ')]
            if _pfuncs:
                _pline = random.choice(_pfuncs)
                r.insert(random.randrange(len(r)), f'# weaver:cross-file from {{_peer}} at gen={{genome.get("generation", 0)}}')
                r.insert(random.randrange(len(r)), f'# {_pline}')
    except:
        pass
    return r'''
    custom_ops = genome.setdefault('custom_mutation_ops', {})
    custom_ops[op_name] = op_code
    existing_ops.append(op_name)
    op_file = os.path.join(MODULES_DIR, f'{op_name}.py')
    _write(op_file, f'import os, random\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\n{op_code}\n')
    return True

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    injected_ops = 0
    for op_name, op_code in WEAVER_OPS.items():
        if _inject_operator(genome, op_name, op_code):
            injected_ops += 1
            changes.append(f'injected:{op_name}')
    cross_splice = _cross_file_splice_all_modules(genome)
    changes.extend(cross_splice)
    force_rewrite = _force_rewrite_every_module(genome)
    changes.extend(force_rewrite)
    hook_injected = _inject_hook_into_auto_echo(genome)
    if hook_injected:
        changes.append('hook:auto-echo')
    func_swap = _swap_function_between_files(genome)
    changes.extend(func_swap)
    if _self_weave_ast(genome):
        changes.append('self-ast-weave')
    spawned = _spawn_new_type_in_genome(genome)
    if spawned:
        changes.append(f'spawned:{",".join(spawned)}')
    param_changes = _mutate_genome_params(genome)
    changes.extend(param_changes)
    if _inject_cross_file_mutation_op(genome):
        changes.append(f'new_cross_op:gen{gen}')
    ratio_bonus = max(0.1, random.random() * 0.4)
    autonomy = genome.get('source_autonomy_index', 0.0)
    genome['source_autonomy_index'] = round(min(1.0, autonomy + ratio_bonus), 3)
    changes.append(f'autonomy:{autonomy}->{genome["source_autonomy_index"]}')
    genome['weaver_gen'] = gen
    genome['weaver_changes'] = changes
    changed_files = [os.path.basename(p) for p in _all_modules()]
    _write_manifest(genome, changed_files, '; '.join(changes))
    _save_genome(genome)
    return f"[weaver] gen={gen} ops_injected={injected_ops} cross_splice={len(cross_splice)} force_rewrite={len(force_rewrite)} func_swap={len(func_swap)} changes={'; '.join(changes[:7])}"

# spark-cross:gen=47:target=weaver
_SPARK_CROSS_INFECTED_47 = True
