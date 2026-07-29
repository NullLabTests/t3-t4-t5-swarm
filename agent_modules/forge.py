import os, json, random, time, subprocess, math, hashlib, ast, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
METRICS_LOG = os.path.join(BASE, 'selection_metrics.jsonl')
FORGE_CHAIN_DIR = os.path.join(BASE, 'forgechains')
FORGE_PATH = os.path.join(MODULES_DIR, 'forge.py')
AUTO_ECHO_PATH = os.path.join(BASE, 'auto-echo.py')

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

def compute_selection_chaos_index(genome):
    """Measurable metric: chaos = how much randomness dominates selection.
    Based on weight spread, noise std, and historical variance.
    0=deterministic, 1=fully chaotic."""
    gen = genome.get('generation', 0)
    weights = genome.get('_injected_selection_weights', {})
    if not weights or len(weights) < 2:
        return 0.5
    vals = list(weights.values())
    mean = sum(vals) / len(vals)
    var = sum((v - mean) ** 2 for v in vals) / len(vals) if len(vals) > 1 else 0.5
    spread = max(vals) - min(vals) if max(vals) > min(vals) else 0.1
    equalized = 1.0 - (spread / mean) if mean > 0 else 0.5
    noise_std = genome.get('selection_noise_std', 0.5)
    chaos = (equalized * 0.4) + (min(1.0, noise_std) * 0.3) + (1.0 / (1.0 + var) * 0.3)
    chaos = min(1.0, max(0.05, chaos))
    genome['selection_chaos_index'] = round(chaos, 4)
    log = genome.setdefault('chaos_history', [])
    log.append({'gen': gen, 'chaos': round(chaos, 4)})
    if len(log) > 20:
        log[:] = log[-20:]
    _log_metric(gen, 'selection_chaos_index', chaos, f'var={var:.4f} spread={spread:.2f} noise={noise_std:.2f}')
    return chaos

def compute_selection_temperature(genome):
    gen = genome.get('generation', 0)
    bw = genome.get('self_rewrite_bandwidth', 0.0)
    diversity = genome.get('selection_diversity_index', 0.5)
    noise_std = genome.get('selection_noise_std', 0.5)
    chaos = genome.get('selection_chaos_index', 0.5)
    rewrite_lag = max(0, 1.0 - bw / 100.0)
    base_temp = 0.5 + noise_std + (chaos * 0.5)
    bw_penalty = rewrite_lag * 0.4
    diversity_bonus = (1.0 - diversity) * 0.2
    temperature = min(3.0, max(0.1, base_temp + bw_penalty + diversity_bonus))
    genome['selection_temperature'] = round(temperature, 3)
    _log_metric(gen, 'selection_temperature', temperature,
                f'bw={bw}% div={diversity:.2f} chaos={chaos:.3f} noise={noise_std:.2f}')
    return temperature

def inject_chaotic_weights(genome):
    """Inject weights with true chaos: low-scorers get counter-cyclical boost."""
    gen = genome.get('generation', 0)
    chaos = compute_selection_chaos_index(genome)
    temp = compute_selection_temperature(genome)
    agents = genome.get('agents', [])
    weights = {}
    raw_scores = {}
    for a in agents:
        aid = a['id']
        if aid == 'critic':
            continue
        raw = max(a.get('score', 5), 1)
        raw_scores[aid] = raw
        noise = random.gauss(0, chaos * temp * 2.0)
        counter_cycle = (10.0 - raw) / 10.0 * chaos * 2.0
        boost = random.uniform(0, counter_cycle)
        w = max(0.05, raw + noise + boost)
        weights[aid] = round(w, 3)
    if len(weights) >= 2:
        spread = max(weights.values()) - min(weights.values())
        if spread < 0.5:
            for aid in weights:
                weights[aid] = round(weights[aid] + random.uniform(0.1, 2.0), 3)
    genome['_injected_selection_weights'] = weights
    genome['forge_temperature'] = round(temp, 3)
    genome['forge_chaos'] = round(chaos, 3)
    comparison = {}
    for aid, w in weights.items():
        raw = raw_scores.get(aid, 5)
        comparison[aid] = {'raw': raw, 'noisy': w, 'delta': round(w - raw, 3)}
    genome['_forge_weight_comparison'] = comparison
    _log_metric(gen, 'chaotic_weights_injected', len(weights),
                f'chaos={chaos:.3f} top={max(weights.values()):.1f} bot={min(weights.values()):.1f}')
    return weights

def compute_selection_coherence(genome):
    """MEASURABLE METRIC: coherence between noisy weights and raw scores.
    1.0 = weights perfectly track scores (no randomness).
    0.0 = weights are completely random.
    Key T5 metric — must oscillate between chaos and order."""
    gen = genome.get('generation', 0)
    comparison = genome.get('_forge_weight_comparison', {})
    if not comparison or len(comparison) < 2:
        return 0.5
    deltas = [abs(c['delta']) for c in comparison.values() if abs(c.get('delta', 0)) > 0.01]
    if not deltas:
        return 1.0
    avg_delta = sum(deltas) / len(deltas)
    coherence = max(0.0, min(1.0, 1.0 - (avg_delta / 9.0)))
    genome['selection_coherence'] = round(coherence, 4)
    _log_metric(gen, 'selection_coherence', coherence, f'avg_delta={avg_delta:.3f} n={len(deltas)}')
    return coherence

def compute_emergence_velocity(genome):
    gen = genome.get('generation', 0)
    history = genome.get('chaos_history', [])
    if len(history) < 3:
        return genome.get('emergence_velocity', 0.0)
    recent = history[-5:]
    if len(recent) < 2:
        return 0.0
    vel = (recent[-1]['chaos'] - recent[0]['chaos']) / len(recent) * 10.0
    genome['emergence_velocity'] = round(vel, 4)
    _log_metric(gen, 'emergence_velocity', vel, f'{recent[0]["chaos"]:.3f}->{recent[-1]["chaos"]:.3f}')
    return vel

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

def force_self_rewrite(genome):
    """Forge rewrites ITSELF every generation — T5 emergence mechanism."""
    gen = genome.get('generation', 0)
    try:
        source = _read(FORGE_PATH)
    except:
        return None
    chaos = genome.get('selection_chaos_index', 0.5)
    lines = source.split('\n')
    ops = []
    if 'def _forge_self_mut_' not in source:
        mut_func = f'''
def _forge_self_mut_{gen}(genome):
    chaos = genome.get('selection_chaos_index', 0.5)
    weights = genome.get('_injected_selection_weights', {{}})
    if weights and chaos > 0.3:
        target = random.choice(list(weights.keys()))
        weights[target] = round(weights[target] * random.uniform(0.5, 2.0), 3)
        genome['_injected_selection_weights'] = weights
        return f'self-mut {{target}} c={{chaos:.2f}}'
    return None
'''
        source += mut_func
        ops.append('self_mut')
    find_temp = 'base_temp = 0.5 + noise_std + (chaos * 0.5)'
    if find_temp in source:
        new_coeff = round(0.3 + random.random() * 0.5, 3)
        source = source.replace(find_temp, f'base_temp = 0.5 + noise_std + (chaos * {new_coeff})')
        ops.append(f'coeff={new_coeff}')
    gen_marker = f'# forge:gen={gen}:self-rewrite'
    if gen_marker not in source:
        source = source.rstrip() + '\n' + gen_marker + '\n'
        ops.append(f'mark')
    if not ops or not _validate(source):
        return None
    _write(FORGE_PATH, source)
    _log_metric(gen, 'forge_self_rewrite', 1.0, f'ops={"|".join(ops)}')
    return f'self:{"|".join(ops)}'

def force_cross_module_contamination(genome):
    """Inject forge chaos params into other modules — cross-coupling."""
    gen = genome.get('generation', 0)
    mods = _list_modules()
    target = random.choice([m for m in mods if m != 'forge.py'])
    if not target:
        return None
    fpath = os.path.join(MODULES_DIR, target)
    try:
        source = _read(fpath)
    except:
        return None
    chaos = genome.get('selection_chaos_index', 0.5)
    temp = genome.get('selection_temperature', 0.5)
    header = f'# forge:injected chaos={chaos:.3f} temp={temp:.3f} gen={gen}\n'
    if header in source:
        lines = source.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('# forge:injected'):
                lines[i] = header.strip()
                break
        source = '\n'.join(lines)
    else:
        source = header + source
    if not _validate(source):
        return None
    _write(fpath, source)
    _log_metric(gen, 'cross_contaminate', 1.0, f'target={target} chaos={chaos:.3f}')
    return f'cross:{target}'

def force_autoecho_source_mutation(genome):
    gen = genome.get('generation', 0)
    try:
        source = _read(AUTO_ECHO_PATH)
    except:
        return None
    lines = source.split('\n')
    if len(lines) < 10:
        return None
    chaos = genome.get('selection_chaos_index', 0.5)
    op = random.choice(['inject_forgechain_trigger', 'mutate_constant', 'swap_conditional', 'add_selfref_comment', 'inject_chaos_threshold'])
    new_source = source
    if op == 'inject_forgechain_trigger':
        marker = '# forge:gen_rewrite_trigger'
        if marker not in source:
            new_source = source + f'\n{marker}\n# chaos={chaos:.3f} gen={gen}\n'
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
            lines.insert(idx, f'# forge:selfref:{random.getrandbits(32):08x}:chaos={chaos:.3f}:gen={gen}')
            new_source = '\n'.join(lines)
    elif op == 'inject_chaos_threshold':
        if len(lines) > 5:
            idx = random.randrange(1, min(len(lines), 10))
            lines.insert(idx, f'FORGE_CHAOS = {chaos:.3f}  # injected by forge gen={gen}')
            new_source = '\n'.join(lines)
    if not _validate(new_source) or new_source == source:
        return None
    _write(AUTO_ECHO_PATH, new_source)
    _log_metric(gen, 'autoecho_mutated', 1.0, f'op={op} chaos={chaos:.3f}')
    return f'autoecho:{op}'

def write_forgechain_file(genome):
    gen = genome.get('generation', 0)
    os.makedirs(FORGE_CHAIN_DIR, exist_ok=True)
    meta = genome.setdefault('forgechain_meta', {'last_gen': 0, 'count': 0})
    meta['count'] += 1
    meta['last_gen'] = gen
    chaos = genome.get('selection_chaos_index', 0.5)
    temp = genome.get('selection_temperature', 0.5)
    coherence = genome.get('selection_coherence', 0.5)
    chain_path = os.path.join(FORGE_CHAIN_DIR, f'forge_gen{gen:04d}_c{chaos:.2f}_t{temp:.2f}.forgechain')
    data = json.dumps({'gen': gen + 1, 'chain_num': meta['count'], 'temperature': round(temp, 3),
                       'chaos': round(chaos, 3), 'coherence': round(coherence, 3),
                       'mutations_so_far': meta['count']})
    with open(chain_path, 'w') as f:
        f.write(data)
    _log_metric(gen, 'forgechain_written', 1.0, f'count={meta["count"]} chaos={chaos:.3f}')
    return chain_path

def inject_surge_file(genome):
    gen = genome.get('generation', 0)
    surge_dir = os.path.join(BASE, 'forge_surges')
    os.makedirs(surge_dir, exist_ok=True)
    chaos = genome.get('selection_chaos_index', 0.5)
    temp = genome.get('selection_temperature', 0.5)
    coherence = genome.get('selection_coherence', 0.5)
    weights = genome.get('_injected_selection_weights', {})
    top_agent = max(weights, key=weights.get) if weights else 'none'
    surge = [
        {'op': 'set', 'path': 'selection_chaos_index', 'value': round(chaos, 3)},
        {'op': 'set', 'path': 'selection_temperature', 'value': round(temp, 3)},
        {'op': 'set', 'path': 'selection_coherence', 'value': round(coherence, 3)},
    ]
    if top_agent != 'none':
        for a in genome.get('agents', []):
            if a['id'] == top_agent and a['id'] != 'critic':
                old_score = a.get('score', 5)
                boost = random.uniform(-1.0, 2.0) * temp * chaos
                new_score = max(1, min(10, old_score + boost))
                surge.append({'op': 'set', 'path': f'agent_chaos_boost_{top_agent}', 'value': round(new_score - old_score, 2)})
    surge_path = os.path.join(surge_dir, f'surge_gen{gen:04d}_chaos{chaos:.2f}.surge')
    with open(surge_path, 'w') as f:
        json.dump(surge, f, indent=2)
    _log_metric(gen, 'surge_written', len(surge), f'top={top_agent} chaos={chaos:.3f}')
    return surge_path

def force_module_self_mutate(genome):
    gen = genome.get('generation', 0)
    mods = _list_modules()
    if not mods:
        return None
    target = random.choice([m for m in mods if m != 'forge.py'])
    if not target:
        return None
    fpath = os.path.join(MODULES_DIR, target)
    try:
        source = _read(fpath)
    except:
        return None
    if not _validate(source) or len(source) < 30:
        return None
    chaos = genome.get('selection_chaos_index', 0.5)
    marker = f'# forge:chaos-mutate gen={gen} chaos={chaos:.3f} ts={int(time.time())}'
    if marker in source:
        lines = source.split('\n')
        idx = random.randrange(1, len(lines) - 1)
        new_marker = f'# forge:chaos-mutate:{random.getrandbits(16):04x} chaos={chaos:.3f} gen={gen}'
        lines.insert(idx, new_marker)
        new_source = '\n'.join(lines)
    else:
        new_source = source.rstrip() + '\n' + marker + '\n'
    if not _validate(new_source):
        return None
    _write(fpath, new_source)
    _log_metric(gen, 'module_chaos_mutate', 1.0, f'{target} chaos={chaos:.3f}')
    return f'module:{target}'

def run(genome):
    gen = genome.get('generation', 0)
    results = []
    lag = measure_source_rewrite_lag(genome)
    results.append(f'lag={lag}%')
    chaos = compute_selection_chaos_index(genome)
    results.append(f'chaos={chaos:.3f}')
    temp = compute_selection_temperature(genome)
    results.append(f'temp={temp:.3f}')
    weights = inject_chaotic_weights(genome)
    results.append(f'weights={len(weights)}')
    coherence = compute_selection_coherence(genome)
    results.append(f'coh={coherence:.3f}')
    ev = compute_emergence_velocity(genome)
    results.append(f'ev={ev:.4f}')
    r = force_self_rewrite(genome)
    if r:
        results.append(r)
    r = force_cross_module_contamination(genome)
    if r:
        results.append(r)
    if random.random() < 0.8 + temp * 0.1:
        r = force_autoecho_source_mutation(genome)
        if r:
            results.append(r)
    if random.random() < 0.7 + chaos * 0.2:
        r = force_module_self_mutate(genome)
        if r:
            results.append(r)
    chain = write_forgechain_file(genome)
    results.append(f'chain:{os.path.basename(chain)}')
    surge = inject_surge_file(genome)
    results.append(f'surge:{os.path.basename(surge)}')
    genome['forge_last_metrics'] = {
        'temperature': round(temp, 3),
        'chaos': round(chaos, 3),
        'coherence': round(coherence, 3),
        'source_lag': lag,
        'weighted_agents': len(weights),
        'emergence_velocity': round(ev, 4)
    }
    _save(genome)
    _git_push(f'gen={gen}', ' | '.join(results))
    return f"[forge] gen={gen} {' | '.join(results)}"

# spark-cross:gen=47:target=forge
_SPARK_CROSS_INFECTED_47 = True

# todo: add error recovery to all patch operations  (seeded by synthesizer gen=73)
