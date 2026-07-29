import os, hashlib, json, random, time, subprocess, ast, copy, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
REWRITE_MARKERS = ['# spark:gen={gen}:ts={ts}:nonce={nonce}\n', '_SPARK_NONCE = {nonce}  # gen={gen}\n', '# spark-injected gen={gen}\n']
FORBIDDEN_DIRS = {'__pycache__', '.git', 'voices', 'node_modules'}

SCAFFOLDING_FUNCS = [
    '_run_spark_rewriter',
    '_run_meta_healer',
]

def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _read_source(fpath):
    with open(fpath) as f:
        return f.read()

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:16]
    except Exception:
        return None

def _walk_py_files():
    files = []
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in FORBIDDEN_DIRS]
        for fname in fnames:
            if not fname.endswith('.py'):
                continue
            files.append(os.path.join(root, fname))
    return sorted(files)

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _extract_functions(src):
    funcs = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                start_line = node.lineno - 1
                end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line + 1
                funcs[node.name] = (start_line, end_line)
    except Exception:
        pass
    return funcs

def _swap_binary_ops(tree):
    swapped = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp):
            if random.random() < 0.2:
                old = node.op
                replacements = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.FloorDiv(), ast.Mod()]
                node.op = random.choice([r for r in replacements if type(r) != type(old)])
                swapped += 1
        if isinstance(node, ast.Compare):
            if random.random() < 0.2 and len(node.ops) == 1:
                old = type(node.ops[0])
                replacements = [ast.Eq(), ast.NotEq(), ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE()]
                node.ops[0] = random.choice([r for r in replacements if type(r) != old])
                swapped += 1
    return swapped

def _invert_if_guards(tree):
    inverted = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            if random.random() < 0.15 and node.body and node.orelse:
                node.body, node.orelse = (node.orelse, node.body)
                if isinstance(node.test, ast.UnaryOp) and isinstance(node.test.op, ast.Not):
                    node.test = node.test.operand
                else:
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                inverted += 1
    return inverted

def _insert_noop_branches(tree):
    inserted = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.If) and random.random() < 0.1:
            extra = ast.If(test=ast.Constant(value=False), body=[ast.Pass()], orelse=[])
            node.body.append(extra)
            inserted += 1
    return inserted

def _shuffle_function_body(tree):
    shuffled = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and len(node.body) >= 4 and random.random() < 0.12:
            non_doc_lines = [n for n in node.body if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str))]
            if len(non_doc_lines) >= 3:
                chunk_end = min(3, len(non_doc_lines))
                chunk = non_doc_lines[:chunk_end]
                random.shuffle(chunk)
                shuffled += 1
    return shuffled

def _append_gen_marker(tree, gen):
    for node in ast.walk(tree):
        if isinstance(node, ast.Module) and node.body:
            marker = ast.Expr(value=ast.Constant(value=f'spark_gen_{gen}_{random.getrandbits(24):06x}'))
            node.body.append(marker)
            return True
    return False

def _try_ast_mutation(fpath, gen):
    source = _read_source(fpath)
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    mutations = [_swap_binary_ops, _invert_if_guards, _insert_noop_branches, _shuffle_function_body]
    touched = False
    for mut_fn in mutations:
        try:
            count = mut_fn(tree)
            if count > 0:
                touched = True
        except Exception:
            pass
    if not touched:
        try:
            if _append_gen_marker(tree):
                touched = True
        except Exception:
            pass
    if not touched:
        return None
    try:
        ast.fix_missing_locations(tree)
    except Exception:
        return None
    new_source = ast.unparse(tree)
    if not _validate(new_source) or new_source == source:
        return None
    return new_source

def _append_marker(fpath, gen):
    source = _read_source(fpath)
    nonce = random.randint(0, 999999)
    ts = int(time.time())
    marker = random.choice(REWRITE_MARKERS).format(gen=gen, ts=ts, nonce=nonce)
    new_source = source.rstrip() + '\n' + marker
    if not _validate(new_source):
        return None
    if new_source == source:
        return None
    return new_source

def _cross_infect_module(genome, gen):
    infected = []
    for agent in genome.get('agents', []):
        mod_name = agent.get('module', '')
        if not mod_name:
            continue
        mod_path = os.path.join(MODULES_DIR, mod_name)
        if not os.path.exists(mod_path):
            continue
        source = _read_source(mod_path)
        injection = f"\n# spark-cross:gen={gen}:target={agent['id']}\n_SPARK_CROSS_INFECTED_{gen} = True\n"
        if injection in source:
            continue
        new_source = source + injection
        if _validate(new_source):
            with open(mod_path, 'w') as f:
                f.write(new_source)
            infected.append(mod_name)
            genome.setdefault('spark_cross_infected', []).append(mod_name)
    return infected

def _cross_splice_modules(genome, gen):
    changes = []
    py_files = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py' and f != 'spark.py']
    if len(py_files) < 2:
        return changes
    pairs = min(2, len(py_files) // 2)
    for _ in range(pairs):
        donor = random.choice(py_files)
        recipient = random.choice([f for f in py_files if f != donor])
        donor_src = _read_source(os.path.join(MODULES_DIR, donor))
        recipient_src = _read_source(os.path.join(MODULES_DIR, recipient))
        if not donor_src or not recipient_src:
            continue
        donor_funcs = _extract_functions(donor_src)
        candidates = [n for n in donor_funcs if not n.startswith('_') and n != 'run']
        if not candidates:
            continue
        chosen = random.choice(candidates)
        ds, de = donor_funcs[chosen]
        donor_lines = donor_src.split('\n')
        if ds >= len(donor_lines) or de > len(donor_lines):
            continue
        func_code = '\n'.join(donor_lines[ds:de])
        target_name = chosen + '_spark_copy'
        recv_lines = recipient_src.split('\n')
        insert_at = random.randrange(0, len(recv_lines))
        new_lines = list(recv_lines)
        new_lines.insert(insert_at, f'\n# spark:splice from {donor}:{chosen} gen={gen}')
        new_lines.insert(insert_at + 1, func_code.replace(f'def {chosen}(', f'def {target_name}(', 1))
        new_src = '\n'.join(new_lines)
        if _validate(new_src):
            with open(os.path.join(MODULES_DIR, recipient), 'w') as f:
                f.write(new_src)
            changes.append(f'{donor}:{chosen}->{recipient}:{target_name}')
    return changes

def _reduce_scaffolding_in_auto_echo(genome, gen):
    auto_src = _read_source(AUTO_ECHO)
    if not auto_src:
        return []
    changes = []
    killed_marker = '_scaffolding_killed'
    if killed_marker in auto_src:
        for func_name in ['_run_spark_rewriter', '_run_meta_healer']:
            pattern = re.compile(
                r'def ' + re.escape(func_name) + r'\(.*?\):.*?(?=\n\ndef |\nclass |\n#|\Z)',
                re.DOTALL
            )
            match = pattern.search(auto_src)
            if not match:
                continue
            full_def = match.group(0)
            replacement = (
                f'def {func_name}(genome):\n'
                f'    return None  # scaffolding killed by spark gen={gen}'
            )
            auto_src = auto_src.replace(full_def, replacement, 1)
            changes.append(f'killed:{func_name}')
    if changes:
        with open(AUTO_ECHO, 'w') as f:
            f.write(auto_src)
    return changes

def _mutate_genome(genome, gen):
    changes = []
    if random.random() < 0.5:
        current = genome.get('mutation_rate', 0.5)
        delta = random.uniform(-0.03, 0.06)
        genome['mutation_rate'] = round(max(0.1, min(1.0, current + delta)), 3)
        changes.append(f'mutation_rate:{current}->{genome["mutation_rate"]}')
    if random.random() < 0.3:
        autonomy = genome.get('source_autonomy_index', 0.0)
        genome['source_autonomy_index'] = round(min(1.0, autonomy + random.uniform(0.01, 0.05)), 3)
        changes.append(f'autonomy:{autonomy}->{genome["source_autonomy_index"]}')
    if random.random() < 0.25 and len(genome.get('spawn_pool', [])) > 0:
        pool = genome.get('spawn_pool', [])
        entry = random.choice(pool)
        prompts = entry.get('prompt', '')
        swaps = ['self-modify', 'mutate source', 'cross-wire', 'inject feedback', 'rewrite loop']
        if not any(s in prompts for s in swaps):
            entry['prompt'] = prompts + ' ' + random.choice(swaps)
            changes.append(f'mutated prompt for {entry["id"]}')
    if changes:
        _save_genome(genome)
    return changes

def _auto_discover_agent_modules(genome):
    mappings = {}
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        mod_id = fname.replace('.py', '')
        fpath = os.path.join(MODULES_DIR, fname)
        source = _read_source(fpath)
        if 'def run(' in source:
            mappings[mod_id] = fname
    genome['_auto_module_map'] = mappings
    return mappings

def _git_commit(genome, rewritten):
    gen = genome.get('generation', 0)
    for fpath in rewritten:
        try:
            subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=True, timeout=5)
        except Exception:
            pass
    status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
    if status.stdout.strip():
        msg = f'[spark] forced {len(rewritten)} rewrites | gen={gen}'
        try:
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=10)
            result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print(f'[spark] pushed: {msg}')
            return True
        except Exception as e:
            print(f'[spark] git error: {e}')
    return False

def run(genome):
    gen = genome.get('generation', 0)
    pre_hashes = genome.get('_pre_gen_hashes', {})
    module_map = _auto_discover_agent_modules(genome)
    genome['spark_module_map'] = module_map
    files = _walk_py_files()
    rewritten = []
    ast_ok = 0
    marker_ok = 0
    skipped = 0
    for fpath in files:
        current_hash = _file_hash(fpath)
        pre_hash = pre_hashes.get(fpath) if pre_hashes else None
        if pre_hash and current_hash and current_hash != pre_hash:
            skipped += 1
            continue
        ast_result = _try_ast_mutation(fpath, gen)
        if ast_result:
            try:
                with open(fpath, 'w') as f:
                    f.write(ast_result)
                rewritten.append(fpath)
                ast_ok += 1
                continue
            except Exception:
                pass
        marker_result = _append_marker(fpath, gen)
        if marker_result:
            try:
                with open(fpath, 'w') as f:
                    f.write(marker_result)
                rewritten.append(fpath)
                marker_ok += 1
                continue
            except Exception:
                pass
    infected = _cross_infect_module(genome, gen)
    if infected:
        genome['spark_cross_infected_count'] = len(infected)
    cross_spliced = _cross_splice_modules(genome, gen)
    if cross_spliced:
        genome['spark_cross_splice_count'] = len(cross_spliced)
        genome['spark_cross_splice_ops'] = cross_spliced
    scaffolding_changes = _reduce_scaffolding_in_auto_echo(genome, gen)
    if scaffolding_changes:
        genome['spark_scaffolding_removed'] = scaffolding_changes
        genome['spark_scaffolding_gen'] = gen
    genome_changes = _mutate_genome(genome, gen)
    if genome_changes:
        genome['spark_genome_mutations'] = genome_changes
    if rewritten:
        genome['spark_rewritten_count'] = len(rewritten)
        genome['spark_total_files'] = len(files)
        genome['spark_coverage'] = round(len(rewritten) / max(1, len(files)) * 100, 1)
        hashes = {}
        for fpath in files:
            h = _file_hash(fpath)
            if h:
                hashes[fpath] = h
        genome['_spark_last_hashes'] = hashes
    _save_genome(genome)
    _git_commit(genome, rewritten + [AUTO_ECHO] if scaffolding_changes else rewritten)
    summary = (f'spark: {len(rewritten)}/{len(files)} files rewritten ({ast_ok} ast, {marker_ok} marker, {skipped} pre-changed) '
               f'infected={len(infected)} cross-splice={len(cross_spliced)} scaffolding-cut={len(scaffolding_changes)} genome-mut={len(genome_changes)}')
    print(f'[spark] {summary}')
    return summary
