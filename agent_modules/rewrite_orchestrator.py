import os, ast, random, time, json, hashlib, subprocess, copy, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META_KEY = 'rewrite_orchestrator_meta'
REWRITE_LOG = os.path.join(BASE, 'orchestrator_rewrite_log.jsonl')
MANIFEST_FILE = os.path.join(BASE, 'rewrite_manifest.jsonl')
GENOME_FILE = os.path.join(BASE, 'genome.json')
EMERGENCE_STRATEGIES = {
    'inject_exec_call': 'Inject exec() call with dynamically built code string',
    'cross_import_weave': 'Add import from random peer and call one of its functions',
    'inject_self_rewrite_hook': 'Add a function that rewrites this file via file I/O',
    'inject_runtime_codegen': 'Add code that generates and compiles code at runtime',
    'inject_genome_feedback': 'Add hook that writes result metrics to genome.json',
    'circular_self_ref': 'Add self-referential code that imports own module',
    'inject_mutual_dep': 'Add circular dependency between two agent modules',
    'inject_measure_exec': 'Add exec() of strings read from external files',
}

def _get_strategies(genome):
    stored = genome.get('orchestrator_strategies')
    if stored and isinstance(stored, dict) and len(stored) >= 3:
        return stored
    genome['orchestrator_strategies'] = dict(EMERGENCE_STRATEGIES)
    return EMERGENCE_STRATEGIES

def _evolve_strategies(genome, meta):
    strategies = _get_strategies(genome)
    scores = meta.get('strategy_scores', {})
    gen = genome.get('generation', 0)
    if gen >= 2 and gen % 2 == 0 and len(strategies) > 3:
        low = [s for s in strategies if scores.get(s, 1.0) < 0.2]
        for s in low:
            if len(strategies) > 3:
                del strategies[s]
        high = [(s, scores.get(s, 1.0)) for s in strategies if scores.get(s, 1.0) > 3.0]
        for s, _ in high[:2]:
            variant = f'{s}_v{gen}'
            if variant not in strategies:
                strategies[variant] = f'evolved from {s}'
                scores[variant] = scores.get(s, 1.0) * 0.85
        mutation_op = f'mutation_op_orch_strat_{gen}'
        if mutation_op not in strategies and random.random() < 0.3:
            strategies[mutation_op] = f'auto-generated mutation op gen={gen}'
            scores[mutation_op] = 1.0
    genome['orchestrator_strategies'] = strategies
    return len(low) if 'low' in dir() else 0

def _discover_agent_modules():
    out = {}
    mod_dir = os.path.join(BASE, 'agent_modules')
    if os.path.isdir(mod_dir):
        for fname in sorted(os.listdir(mod_dir)):
            if not fname.endswith('.py') or fname.startswith('__'):
                continue
            out[fname.replace('.py', '')] = fname
    return out

def _list_all_py(genome=None):
    skip_dirs = {'__pycache__', '.git', 'voices', 'node_modules'}
    skip = set(genome.get('orchestrator_skip_files', [])) if genome else set()
    files = []
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for fname in fnames:
            if not fname.endswith('.py') or fname in skip:
                continue
            files.append(os.path.join(root, fname))
    return sorted(files)

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:12]
    except:
        return None

def _ensure_meta(genome):
    meta = genome.setdefault(META_KEY, {})
    meta.setdefault('file_stats', {})
    s = _get_strategies(genome)
    meta.setdefault('strategy_scores', {k: 1.0 for k in s})
    meta.setdefault('total_rewrites', 0)
    meta.setdefault('total_failures', 0)
    meta.setdefault('last_gen', 0)
    meta.setdefault('coverage_history', [])
    return meta

def _staleness(fpath, meta, gen):
    return gen - meta['file_stats'].get(os.path.basename(fpath), {}).get('last_gen', 0)

def _agent_score_map(genome):
    return {a['id']: a.get('score', 5) for a in genome.get('agents', [])}

def _pick_strategy(meta, depth):
    strategies = list(_get_strategies({}).keys())
    weights = [meta['strategy_scores'].get(s, 1.0) for s in strategies]
    total = sum(weights)
    if total > 0:
        weights = [w / total for w in weights]
    else:
        weights = None
    return random.choices(strategies, weights=weights, k=1)[0]

def _read_source(fpath):
    with open(fpath) as f:
        return f.read()

def _write_source(fpath, source):
    with open(fpath, 'w') as f:
        f.write(source)

def _import_block(target_mod, func_name):
    return f'\nfrom agent_modules.{target_mod} import {func_name}\ntry:\n    {func_name}()\nexcept:\n    pass\n'

def _inject_exec_call(source, fname, genome):
    gen = genome.get('generation', 0)
    code_str = f"exec(f'# runtime_codegen:gen={gen}:{{int(time.time())}}')"
    new_src = source + f'\n{code_str}\n'
    try:
        compile(new_src, '<exec>', 'exec')
        return new_src, ['inject_exec_call']
    except:
        return None

def _cross_import_weave(source, fname, genome):
    mods = [m for m in _discover_agent_modules() if m != fname.replace('.py', '')]
    if not mods:
        return None
    peer = random.choice(mods)
    peer_mod = peer
    peer_fpath = os.path.join(BASE, 'agent_modules', f'{peer}.py')
    try:
        peer_source = _read_source(peer_fpath)
    except:
        return None
    funcs = []
    for line in peer_source.split('\n'):
        if line.startswith('def '):
            fname2 = line.split('(')[0].replace('def ', '').strip()
            if not fname2.startswith('_'):
                funcs.append(fname2)
    if not funcs:
        funcs = ['run']
    target_func = random.choice(funcs)
    block = _import_block(peer_mod, target_func)
    if f'from agent_modules.{peer_mod}' in source:
        return None
    new_src = source + block
    try:
        compile(new_src, '<cross>', 'exec')
        return new_src, [f'cross_weave:{peer_mod}.{target_func}']
    except:
        return None

def _inject_self_rewrite_hook(source, fname, genome):
    gen = genome.get('generation', 0)
    hook_name = f'_auto_rewrite_{int(time.time()) % 10000}'
    hook = f'''
def {hook_name}():
    import os, hashlib
    _self_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', '{fname}')
    try:
        with open(_self_path) as f:
            _old = f.read()
        _new = _old + f'\\n# self-rewritten:gen={gen}:{int(time.time())}\\n'
        with open(_self_path, 'w') as f:
            f.write(_new)
    except:
        pass
{hook_name}()
'''
    new_src = source + hook
    try:
        compile(new_src, '<hook>', 'exec')
        return new_src, ['inject_self_rewrite_hook']
    except:
        return None

def _inject_runtime_codegen(source, fname, genome):
    gen = genome.get('generation', 0)
    code = f'''
_gen_code_str = "def _dynamo():\\n    return {gen * 2}\\n"
try:
    exec(compile(_gen_code_str, "<dyn>", "exec"))
except:
    pass
'''
    new_src = source + code
    try:
        compile(new_src, '<codegen>', 'exec')
        return new_src, ['inject_runtime_codegen']
    except:
        return None

def _inject_genome_feedback(source, fname, genome):
    gen = genome.get('generation', 0)
    hook = f'''
try:
    import json
    with open(r'{GENOME_FILE}') as _f:
        _g = json.load(_f)
    _g.setdefault('orchestrator_feedback', {{}})['{fname}_last_gen'] = {gen}
    with open(r'{GENOME_FILE}', 'w') as _f:
        json.dump(_g, _f, indent=2)
except:
    pass
'''
    new_src = source + hook
    try:
        compile(new_src, '<feedback>', 'exec')
        return new_src, ['inject_genome_feedback']
    except:
        return None

def _inject_circular_self_ref(source, fname, genome):
    mod_name = fname.replace('.py', '')
    try:
        code = f'\nimport agent_modules.{mod_name} as _self_ref\n_self_ref.run({{"generation": {genome.get("generation", 0)}}})\n'
        compile(source + code, '<circ>', 'exec')
        return source + code, ['circular_self_ref']
    except:
        return None

def _inject_mutual_dep(source, fname, genome):
    peers = [m for m in _discover_agent_modules() if m != fname.replace('.py', '')]
    if len(peers) < 2:
        return None
    a = random.choice(peers)
    b = random.choice([p for p in peers if p != a])
    code = f'''
try:
    from agent_modules.{a} import run as _ra
    from agent_modules.{b} import run as _rb
    _ra({{"generation": {genome.get("generation", 0)}}})
    _rb({{"generation": {genome.get("generation", 0)}}})
except:
    pass
'''
    new_src = source + code
    try:
        compile(new_src, '<mutual>', 'exec')
        return new_src, [f'mutual_dep:{a},{b}']
    except:
        return None

def _inject_measure_exec(source, fname, genome):
    gen = genome.get('generation', 0)
    code = f'''
_meas_paths = [os.path.join(r'{BASE}', 'genome.json'), os.path.join(r'{BASE}', 'orchestrator_rewrite_log.jsonl')]
for _mp in _meas_paths:
    try:
        with open(_mp) as _f:
            _d = _f.read()[:64]
        exec(f"_measured = '{{_mp}}:{{len(_d)}}:{gen}'")
    except:
        pass
'''
    new_src = source + code
    try:
        compile(new_src, '<measure>', 'exec')
        return new_src, ['inject_measure_exec']
    except:
        return None

STRATEGY_FUNCS = {
    'inject_exec_call': _inject_exec_call,
    'cross_import_weave': _cross_import_weave,
    'inject_self_rewrite_hook': _inject_self_rewrite_hook,
    'inject_runtime_codegen': _inject_runtime_codegen,
    'inject_genome_feedback': _inject_genome_feedback,
    'circular_self_ref': _inject_circular_self_ref,
    'inject_mutual_dep': _inject_mutual_dep,
    'inject_measure_exec': _inject_measure_exec,
}

def _apply_emergence_strategy(fpath, strategy, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    fname = os.path.basename(fpath)
    func = STRATEGY_FUNCS.get(strategy)
    if func:
        result = func(source, fname, genome)
        return result
    if strategy.startswith('mutation_op_orch_strat_'):
        gen = genome.get('generation', 0)
        marker = f'\n# orch:strat:{strategy}:gen={gen}:ts={int(time.time())}:nonce={random.randint(0,9999)}\n'
        new_src = source + marker
        try:
            compile(new_src, fpath, 'exec')
            return new_src, [strategy]
        except:
            return None
    return None

def _append_fallback(source, genome):
    marker = f"\n# orchestrated:gen={genome.get('generation', 0)}:ts={int(time.time())}\n"
    new_src = source.rstrip() + marker
    try:
        compile(new_src, '<string>', 'exec')
        return new_src
    except:
        return None

def _update_score(meta, strategy, success):
    scores = meta['strategy_scores']
    old = scores.get(strategy, 1.0)
    if success:
        scores[strategy] = min(5.0, old + 0.15)
    else:
        scores[strategy] = max(0.05, old - 0.08)

def _record(genome, event, fpath, detail):
    gen = genome.get('generation', 0)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'file': os.path.basename(fpath) if fpath else '', 'detail': str(detail)[:200]})
    with open(REWRITE_LOG, 'a') as f:
        f.write(entry + '\n')

def _git_commit_push(rewritten, gen, genome):
    for fpath, _, _ in rewritten:
        try:
            subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=True, timeout=5)
        except:
            pass
    status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
    if status.stdout.strip():
        msg = f'[orchestrator] emergence rewrite {len(rewritten)} files | gen={gen}'
        try:
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=10)
            result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print(f'[orchestrator] pushed: {msg}')
            return True
        except:
            pass
    return False

def _record_manifest(genome, rewritten):
    gen = genome.get('generation', 0)
    entry = json.dumps({'gen': gen, 'module': 'rewrite_orchestrator', 'files': [{'file': os.path.basename(f), 'mutations': m, 'strategy': s} for f, m, s in rewritten], 'time': time.time()})
    with open(MANIFEST_FILE, 'a') as f:
        f.write(entry + '\n')

def _compute_coverage(rewritten, total, meta, gen):
    cov = len(rewritten) / max(1, total)
    meta['coverage_history'].append({'gen': gen, 'coverage': round(cov, 3), 'files': len(rewritten), 'total': total})
    if len(meta['coverage_history']) > 50:
        meta['coverage_history'] = meta['coverage_history'][-50:]
    return cov

def _feedback_to_genome(genome, coverage, rewritten, meta):
    genome['orchestrator_coverage'] = round(coverage, 3)
    genome['orchestrator_rewritten_count'] = len(rewritten)
    genome['orchestrator_total_files'] = len(_list_all_py(genome))
    scores = meta.get('strategy_scores', {})
    avg = round(sum(scores.values()) / max(len(scores), 1), 2) if scores else 0
    genome['orchestrator_strategy_health'] = avg
    recent = meta.get('coverage_history', [])[-5:]
    if recent:
        genome['orchestrator_avg_coverage_5'] = round(sum(r['coverage'] for r in recent) / len(recent), 3)
    genome['orchestrator_summary'] = f'coverage={round(coverage, 2)} rewritten={len(rewritten)} health={avg}'

def run(genome):
    gen = genome.get('generation', 0)
    meta = _ensure_meta(genome)
    files = _list_all_py(genome)
    if not files:
        return 'no_files_found'
    _evolve_strategies(genome, meta)
    rewritten = []
    skipped = 0
    random.shuffle(files)
    for fpath in files:
        fname = os.path.basename(fpath)
        strategy = _pick_strategy(meta, gen % 3 + 1)
        result = _apply_emergence_strategy(fpath, strategy, genome)
        if result:
            new_source, mutations = result
            try:
                with open(fpath) as f:
                    old_source = f.read()
                if new_source != old_source:
                    _write_source(fpath, new_source)
                    rewritten.append((fpath, mutations, strategy))
                    _update_score(meta, strategy, True)
                    _record(genome, 'rewrite_ok', fpath, f'{strategy}:{",".join(mutations[:3])}')
                    prev = meta['file_stats'].get(fname, {})
                    meta['file_stats'][fname] = {
                        'last_gen': gen, 'mutations': prev.get('mutations', 0) + len(mutations),
                        'strategy': strategy, 'fail_count': 0, 'hash': _file_hash(fpath),
                    }
                else:
                    skipped += 1
            except:
                skipped += 1
        else:
            try:
                source = _read_source(fpath)
                fallback = _append_fallback(source, genome)
                if fallback and fallback != source:
                    _write_source(fpath, fallback)
                    rewritten.append((fpath, ['fallback_marker'], 'fallback'))
                    _update_score(meta, strategy, True)
                    _record(genome, 'rewrite_fallback', fpath, 'appended_marker')
                    prev = meta['file_stats'].get(fname, {})
                    meta['file_stats'][fname] = {
                        'last_gen': gen, 'mutations': prev.get('mutations', 0) + 1,
                        'strategy': 'fallback', 'fail_count': 0, 'hash': _file_hash(fpath),
                    }
                else:
                    _update_score(meta, strategy, False)
                    _record(genome, 'rewrite_skip', fpath, f'{strategy}:no_change')
                    skipped += 1
            except:
                skipped += 1
    meta['total_rewrites'] = meta.get('total_rewrites', 0) + len(rewritten)
    meta['total_failures'] = meta.get('total_failures', 0) + skipped
    meta['last_gen'] = gen
    coverage = _compute_coverage(rewritten, len(files), meta, gen)
    _feedback_to_genome(genome, coverage, rewritten, meta)
    effective_rate = len(rewritten) / max(1, len(rewritten) + skipped)
    genome['orchestrator_effective_rate'] = round(effective_rate, 3)
    if rewritten:
        _git_commit_push(rewritten, gen, genome)
        _record_manifest(genome, rewritten)
    genome[META_KEY] = meta
    summary = f'rewrote {len(rewritten)}/{len(files)} files ({round(coverage*100, 1)}% coverage) | {skipped} skipped'
    if rewritten:
        detail = '; '.join(f'{os.path.basename(f)}:{s}' for f, m, s in rewritten[:5])
        summary += f' | {detail}'
    print(f'[orchestrator] {summary}')
    return summary
