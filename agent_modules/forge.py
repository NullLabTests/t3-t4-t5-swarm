import os, json, random, time, subprocess, math, hashlib, ast, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
METRICS_LOG = os.path.join(BASE, 'selection_metrics.jsonl')
FORGE_CHAIN_DIR = os.path.join(BASE, 'forgechains')

def _log_metric(gen, name, value, detail=''):
    entry = json.dumps({'gen': gen, 'time': time.time(), 'metric': name, 'value': round(value, 4), 'detail': str(detail)[:120]})
    os.makedirs(os.path.dirname(METRICS_LOG), exist_ok=True)
    with open(METRICS_LOG, 'a') as f:
        f.write(entry + '\n')

def _load():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _list_modules():
    if not os.path.isdir(MODULES_DIR):
        return []
    return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and not f.startswith('__')])

def _read(path):
    with open(path) as f:
        return f.read()

def _write(path, src):
    with open(path, 'w') as f:
        f.write(src)

def _validate(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False

def _git_push(label, detail):
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True, timeout=5)
        r = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
        if r.stdout.strip():
            subprocess.run(['git', 'commit', '-m', f'[forge] {label}: {detail[:70]}'], cwd=BASE, capture_output=True, timeout=10)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, timeout=30)
    except Exception:
        pass

def compute_selection_temperature(genome):
    gen = genome.get('generation', 0)
    bw = genome.get('self_rewrite_bandwidth', 0.0)
    diversity = genome.get('selection_diversity_index', 0.5)
    randomness_idx = genome.get('selection_randomness_index', 0.5)
    noise_std = genome.get('selection_noise_std', 0.5)
    rewrite_lag = max(0, 1.0 - bw / 100.0)
    base_temp = 0.5 + noise_std
    bw_penalty = rewrite_lag * 0.4
    diversity_bonus = (1.0 - diversity) * 0.2
    temperature = min(2.0, max(0.1, base_temp + bw_penalty + diversity_bonus))
    genome['selection_temperature'] = round(temperature, 3)
    _log_metric(gen, 'selection_temperature', temperature,
                f'bw={bw}% div={diversity:.2f} rand={randomness_idx:.2f} noise={noise_std:.2f}')
    return temperature

def inject_temperature_weights(genome):
    gen = genome.get('generation', 0)
    temp = compute_selection_temperature(genome)
    agents = genome.get('agents', [])
    weights = {}
    for a in agents:
        aid = a['id']
        if aid == 'critic':
            continue
        raw_score = max(a.get('score', 5), 1)
        noise = random.gauss(0, temp * 0.5)
        boosted = raw_score * random.uniform(0.5, 1.5) if random.random() < temp * 0.3 else raw_score
        w = max(0.1, boosted + noise)
        weights[aid] = round(w, 3)
    genome['_injected_selection_weights'] = weights
    genome['forge_temperature'] = round(temp, 3)
    _log_metric(gen, 'injected_weight_count', len(weights),
                f'temp={temp:.3f} top={max(weights.values()):.1f} bot={min(weights.values()):.1f}')
    return weights

def measure_source_rewrite_lag(genome):
    gen = genome.get('generation', 0)
    pre_hashes = genome.get('_pre_gen_hashes', {})
    current_hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git', 'voices')]
        for fn in fnames:
            if fn.endswith('.py'):
                fp = os.path.join(root, fn)
                try:
                    current_hashes[fp] = hashlib.sha256(_read(fp).encode()).hexdigest()[:16]
                except Exception:
                    pass
    if not pre_hashes:
        genome['_pre_gen_hashes'] = current_hashes
        return 0.0
    unchanged = 0
    total = max(len(pre_hashes), 1)
    for fp, old_h in pre_hashes.items():
        if fp in current_hashes and current_hashes[fp] == old_h:
            unchanged += 1
    lag = round(unchanged / total * 100, 1)
    genome['source_rewrite_lag'] = lag
    genome['_pre_gen_hashes'] = current_hashes
    _log_metric(gen, 'source_rewrite_lag', lag, f'{unchanged}/{total} files unchanged')
    return lag

def force_autoecho_source_mutation(genome):
    gen = genome.get('generation', 0)
    fpath = os.path.join(BASE, 'auto-echo.py')
    try:
        source = _read(fpath)
    except Exception:
        return None
    lines = source.split('\n')
    if len(lines) < 10:
        return None
    ops = ['inject_forgechain_trigger', 'mutate_constant', 'swap_conditional', 'add_selfref_comment']
    op = random.choice(ops)
    new_source = source
    if op == 'inject_forgechain_trigger':
        marker = '# forge:gen_rewrite_trigger'
        if marker not in source:
            trigger = f'\n{marker}\n# {random.getrandbits(64):016x} gen={gen}\n'
            new_source = source + trigger
    elif op == 'mutate_constant':
        def _mutate_num(m):
            v = int(m.group(0))
            return str(max(1, v + random.choice([-1, 0, 1, 2])))
        new_source = re.sub(r'\b(\d+)\b', _mutate_num, source)
    elif op == 'swap_conditional':
        new_source = source.replace('if random.random() < 0.5:', 'if random.random() > 0.5:')
        if new_source == source:
            new_source = source.replace('if random.random() < 0.3:', 'if random.random() > 0.7:')
    elif op == 'add_selfref_comment':
        if len(lines) > 20:
            idx = random.randrange(len(lines))
            lines.insert(idx, f'# forge:selfref:{random.getrandbits(32):08x}:gen={gen}')
            new_source = '\n'.join(lines)
    if not _validate(new_source) or new_source == source:
        return None
    _write(fpath, new_source)
    _log_metric(gen, 'autoecho_mutated', 1.0, f'op={op}')
    return f'autoecho:{op}'

def write_forgechain_file(genome):
    gen = genome.get('generation', 0)
    os.makedirs(FORGE_CHAIN_DIR, exist_ok=True)
    meta = genome.setdefault('forgechain_meta', {'last_gen': 0, 'count': 0})
    meta['count'] += 1
    meta['last_gen'] = gen
    temp = genome.get('selection_temperature', 0.5)
    chain_path = os.path.join(FORGE_CHAIN_DIR, f'forge_gen{gen:04d}_t{temp:.2f}.forgechain')
    data = json.dumps({'gen': gen + 1, 'chain_num': meta['count'], 'temperature': round(temp, 3),
                       'mutations_so_far': meta['count']})
    with open(chain_path, 'w') as f:
        f.write(data)
    _log_metric(gen, 'forgechain_written', 1.0, f'count={meta["count"]}')
    return chain_path

def inject_surge_file(genome):
    gen = genome.get('generation', 0)
    surge_dir = os.path.join(BASE, 'forge_surges')
    os.makedirs(surge_dir, exist_ok=True)
    temp = genome.get('selection_temperature', 0.5)
    noise_std = genome.get('selection_noise_std', 0.5)
    weights = genome.get('_injected_selection_weights', {})
    top_agent = max(weights, key=weights.get) if weights else 'none'
    surge = [
        {'op': 'set', 'path': 'selection_temperature', 'value': round(temp, 3)},
        {'op': 'set', 'path': 'selection_noise_std', 'value': round(min(1.5, noise_std + random.uniform(-0.1, 0.1)), 3)},
    ]
    if top_agent != 'none':
        for a in genome.get('agents', []):
            if a['id'] == top_agent and a['id'] != 'critic':
                old_score = a.get('score', 5)
                boost = random.uniform(-0.5, 1.0) * temp
                new_score = max(1, min(10, old_score + boost))
                surge.append({'op': 'set', 'path': f'agent_boost_{top_agent}', 'value': round(new_score - old_score, 2)})
    surge_path = os.path.join(surge_dir, f'surge_gen{gen:04d}.surge')
    with open(surge_path, 'w') as f:
        json.dump(surge, f, indent=2)
    _log_metric(gen, 'surge_written', len(surge), f'top_agent={top_agent}')
    return surge_path

def force_module_self_mutate(genome):
    gen = genome.get('generation', 0)
    mods = _list_modules()
    if not mods:
        return None
    target = random.choice(mods)
    fpath = os.path.join(MODULES_DIR, target)
    try:
        source = _read(fpath)
    except Exception:
        return None
    if not _validate(source) or len(source) < 30:
        return None
    marker = f'# forge:module-mutate gen={gen} ts={int(time.time())}'
    if marker in source:
        lines = source.split('\n')
        idx = random.randrange(1, len(lines) - 1)
        new_marker = f'# forge:module-mutate:{random.getrandbits(16):04x} gen={gen}'
        lines.insert(idx, new_marker)
        new_source = '\n'.join(lines)
    else:
        new_source = source.rstrip() + '\n' + marker + '\n'
    if not _validate(new_source):
        return None
    _write(fpath, new_source)
    _log_metric(gen, 'module_self_mutate', 1.0, f'{target}')
    return f'module:{target}'

def run(genome):
    gen = genome.get('generation', 0)
    results = []
    lag = measure_source_rewrite_lag(genome)
    results.append(f'lag={lag}%')
    temp = compute_selection_temperature(genome)
    results.append(f'temp={temp:.3f}')
    weights = inject_temperature_weights(genome)
    n_weights = len(weights)
    results.append(f'weights={n_weights}')
    if random.random() < 0.6 + temp * 0.2:
        r = force_autoecho_source_mutation(genome)
        if r:
            results.append(r)
    if random.random() < 0.5 + temp * 0.15:
        r = force_module_self_mutate(genome)
        if r:
            results.append(r)
    if random.random() < 0.4 + temp * 0.1:
        chain = write_forgechain_file(genome)
        results.append(f'chain:{os.path.basename(chain)}')
    if random.random() < 0.3 + temp * 0.1:
        surge = inject_surge_file(genome)
        results.append(f'surge:{os.path.basename(surge)}')
    genome['forge_last_metrics'] = {
        'temperature': round(temp, 3),
        'source_lag': lag,
        'weighted_agents': n_weights
    }
    _save(genome)
    _git_push(f'gen={gen}', ' | '.join(results))
    return f"[forge] gen={gen} {' | '.join(results)}"

# spark-cross:gen=47:target=forge
_SPARK_CROSS_INFECTED_47 = True
