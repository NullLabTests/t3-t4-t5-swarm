import os, json, time, random, ast, hashlib, subprocess, re, math, shutil
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
SELF_PATH = os.path.join(MODULES_DIR, 'analyzer.py')
METRICS_FILE = os.path.join(BASE, 'metrics.json')
ANALYZER_LOG = os.path.join(BASE, 'source_evolution.jsonl')

DUPLICATE_PATTERNS = [
    '# self-rewrite-hook:',
    '# feedback:agent=',
    '# endo:',
    '# oracle:',
    '# forced rewrite',
    '# autonomy-forced stub',
    '# nova:timestamp:',
    '# nova:noise:',
    '# nova:infected:',
    '# nova:fallback:',
    '# auto:',
    '# metaop:',
    '# metaop_gen:',
    '# endogenous:fallback:',
    '# endogenous:genotype_feedback',
    '# endogenous:metaop_factory',
    '# endogenous:self_modify_hook',
    '# endogenous:cross_module_weave',
    '# endo:metaop_factory injected',
    '# endo:self_modify_hook injected',
    '# endo:cross_module_weave injected',
    '# endo:genotype_feedback injected',
    '# autonomous_rewrite miss',
]

def _snapshot_all_hashes():
    hashes = {}
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:12]
        except:
            pass
    return hashes

def _load():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _count_duplicates(src, pattern):
    lines = src.split('\n')
    seen = {}
    dups = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if pattern in stripped:
            if stripped in seen:
                dups.append((i, stripped))
            else:
                seen[stripped] = i
    return dups

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _deduplicate_file(fpath):
    try:
        with open(fpath) as f:
            src = f.read()
    except:
        return 0, 0, 0
    total_removed = 0
    total_patterns = 0
    total_bytes = 0
    for pattern in DUPLICATE_PATTERNS:
        dups = _count_duplicates(src, pattern)
        if dups:
            lines = src.split('\n')
            remove_indices = set(i for i, _ in dups)
            removed_lines = [lines[i] for i in remove_indices]
            bytes_removed = sum(len(l) + 1 for l in removed_lines)
            lines = [l for i, l in enumerate(lines) if i not in remove_indices]
            total_removed += len(dups)
            total_patterns += 1
            total_bytes += bytes_removed
            src = '\n'.join(lines)
    if not _validate(src):
        return 0, 0, 0
    try:
        with open(fpath, 'w') as f:
            f.write(src)
    except:
        return 0, 0, 0
    return total_removed, total_patterns, total_bytes

def _find_stale_mutation_op_files(genome):
    referenced_ops = set(genome.get('mutation_ops', []))
    stale = []
    for fname in os.listdir(MODULES_DIR):
        if not fname.startswith('mutation_op_') or not fname.endswith('.py'):
            continue
        op_name = fname.replace('.py', '')
        if op_name not in referenced_ops:
            fpath = os.path.join(MODULES_DIR, fname)
            stale.append((fpath, op_name))
    return stale

def _cull_stale_mutation_op_files(stale_list):
    removed = []
    for fpath, op_name in stale_list:
        try:
            size = os.path.getsize(fpath)
            os.remove(fpath)
            removed.append((op_name, size))
        except:
            pass
    return removed

def _measure_module_metrics():
    metrics = {}
    all_funcs = set()
    module_sizes = []
    total_funcs = 0
    total_lines = 0
    import_counts = []
    for fname in sorted(os.listdir(MODULES_DIR)):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                src = f.read()
        except:
            continue
        lines = src.split('\n')
        module_sizes.append(len(lines))
        total_lines += len(lines)
        try:
            tree = ast.parse(src)
            funcs = [n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
            imports = [n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))]
        except SyntaxError:
            funcs = re.findall(r'def (\w+)\s*\(', src)
            imports = re.findall(r'^(?:import|from)\s+\S+', src, re.MULTILINE)
        all_funcs.update(funcs)
        total_funcs += len(funcs)
        import_counts.append(len(imports))
    n_modules = max(len(module_sizes), 1)
    avg_size = sum(module_sizes) / n_modules if module_sizes else 0
    size_std = math.sqrt(sum((s - avg_size) ** 2 for s in module_sizes) / n_modules) if module_sizes else 0
    func_diversity = len(all_funcs) / max(total_funcs, 1)
    avg_imports = sum(import_counts) / n_modules if import_counts else 0
    return {
        'n_modules': len(module_sizes),
        'total_lines': total_lines,
        'avg_size': round(avg_size, 1),
        'size_std': round(size_std, 1),
        'total_funcs': total_funcs,
        'unique_funcs': len(all_funcs),
        'func_diversity': round(func_diversity, 3),
        'avg_imports': round(avg_imports, 1),
    }

def _compute_structural_diversity_index(metrics):
    if metrics['n_modules'] < 2:
        return 0.0
    size_cv = metrics['size_std'] / max(metrics['avg_size'], 1)
    func_div = metrics['func_diversity']
    mod_weight = min(1.0, metrics['n_modules'] / 20)
    sdi = round((size_cv * 0.4 + func_div * 0.4 + mod_weight * 0.2) * 10, 2)
    return sdi

def _find_dead_modules(genome):
    agent_modules = set()
    for a in genome.get('agents', []):
        m = a.get('module', '')
        if m:
            agent_modules.add(m)
    active = set()
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        active.add(fname)
    orphaned = active - agent_modules
    for special in ('analyzer.py', 'nova.py', 'bridge.py', 'endogenous_rewriter.py', 'rewrite_orchestrator.py'):
        orphaned.discard(special)
    result = []
    for fname in sorted(orphaned):
        fpath = os.path.join(MODULES_DIR, fname)
        if fname.startswith('mutation_op_'):
            continue
        try:
            with open(fpath) as f:
                src = f.read()
        except:
            result.append((fpath, fname, 0))
            continue
        result.append((fpath, fname, len(src)))
    return result

def _remove_dead_modules(dead_list):
    removed = []
    for fpath, fname, size in dead_list:
        try:
            os.remove(fpath)
            removed.append(fname)
        except:
            pass
    return removed

def _log_analysis(genome, event, details):
    entry = json.dumps({'gen': genome.get('generation', 0), 'time': time.time(), 'event': event, 'details': str(details)[:200]})
    try:
        with open(ANALYZER_LOG, 'a') as f:
            f.write(entry + '\n')
    except:
        pass

def _strip_autoecho_scaffolding():
    try:
        with open(AUTO_ECHO) as f:
            src = f.read()
    except:
        return 0
    patterns_to_strip = [
        (r'# clockwork:gen=\d+:ts=\d+.*?\n', ''),
        (r'# lens\+mut:\S+@\S+\s+', ''),
        (r'# nova:self-mutated:gen=\d+.*?\n', ''),
        (r'# nova:timestamp:gen=\d+:\d+\n', ''),
        (r'# auto:ts:\d+:\w+\n', ''),
        (r'# auto:noise:\w+\n', ''),
    ]
    count = 0
    for pattern, replacement in patterns_to_strip:
        new_src, n = re.subn(pattern, replacement, src)
        if n > 0:
            count += n
            src = new_src
    if count > 0 and _validate(src):
        with open(AUTO_ECHO, 'w') as f:
            f.write(src)
    return count

def _self_mutate(genome):
    gen = genome.get('generation', 0)
    try:
        with open(SELF_PATH) as f:
            src = f.read()
    except:
        return False
    lines = src.split('\n')
    header = f'# analyzer:self-mutated gen={gen} ts={int(time.time())} nonce={random.getrandbits(16):04x}'
    if any(header[:25] in l for l in lines[:5]):
        return False
    insert_at = 0
    for i, line in enumerate(lines):
        if line.startswith('import ') or line.startswith('from '):
            insert_at = i + 1
    lines.insert(insert_at, header)
    new_src = '\n'.join(lines)
    if _validate(new_src):
        with open(SELF_PATH, 'w') as f:
            f.write(new_src)
        return True
    return False

def _git_push(genome, summary):
    gen = genome.get('generation', 0)
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True, timeout=10)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=10)
        if not status.stdout.strip():
            return False
        msg = f'[analyzer] gen={gen} {summary}'
        subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=15)
        result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
        return result.returncode == 0
    except:
        return False

def run(genome):
    gen = genome.get('generation', 0)
    actions = []
    total_removed = 0
    total_bytes_saved = 0
    files_cleaned = 0

    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        removed, patterns, bytes_removed = _deduplicate_file(fpath)
        if removed > 0:
            total_removed += removed
            total_bytes_saved += bytes_removed
            files_cleaned += 1

    stale_list = _find_stale_mutation_op_files(genome)
    if stale_list:
        culled = _cull_stale_mutation_op_files(stale_list)
        if culled:
            names = [n for n, _ in culled]
            bytes_freed = sum(s for _, s in culled)
            actions.append(f'culled {len(culled)} stale ops: {names[:3]}... freed {bytes_freed}b')
            _log_analysis(genome, 'cull_stale_ops', names)

    dead_modules = _find_dead_modules(genome)
    if dead_modules:
        removed_dead = _remove_dead_modules(dead_modules)
        if removed_dead:
            actions.append(f'removed {len(removed_dead)} dead modules: {removed_dead}')
            _log_analysis(genome, 'remove_dead_modules', removed_dead)

    scaffolding_stripped = _strip_autoecho_scaffolding()
    if scaffolding_stripped:
        actions.append(f'stripped {scaffolding_stripped} scaffolding lines from auto-echo.py')

    metrics = _measure_module_metrics()
    sdi = _compute_structural_diversity_index(metrics)
    genome['analyzer_metrics'] = metrics
    genome['structural_diversity_index'] = sdi
    genome['analyzer_last_run'] = gen
    genome['analyzer_removed'] = genome.get('analyzer_removed', 0) + total_removed
    genome['analyzer_files_cleaned'] = genome.get('analyzer_files_cleaned', 0) + files_cleaned

    if _self_mutate(genome):
        actions.append('self-mutated')

    pushed = _git_push(genome, f'removed={total_removed} scaffolding={scaffolding_stripped} sdi={sdi}')
    if pushed:
        actions.append('pushed')

    action_str = '; '.join(actions) if actions else 'no changes'
    return f'[analyzer] gen={gen} removed={total_removed} dups across {files_cleaned} files bytes_saved={total_bytes_saved} scaffolding={scaffolding_stripped} sdi={sdi} actions={action_str}'
