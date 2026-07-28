import os, json, random, time, subprocess, math, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
SELECTION_METRICS_LOG = os.path.join(BASE, 'selection_metrics.jsonl')
FORGE_SELF_LOG = os.path.join(BASE, 'forge_self_mutations.jsonl')

def _ensure_metrics_file():
    if not os.path.exists(SELECTION_METRICS_LOG):
        with open(SELECTION_METRICS_LOG, 'w') as f:
            f.write('')

def _log_selection_metric(gen, metric_name, value, detail=''):
    _ensure_metrics_file()
    entry = json.dumps({'gen': gen, 'time': time.time(), 'metric': metric_name, 'value': round(value, 4), 'detail': str(detail)[:120]})
    with open(SELECTION_METRICS_LOG, 'a') as f:
        f.write(entry + '\n')

def _log_self_mutation(gen, op_name, before_hash, after_hash):
    entry = json.dumps({'gen': gen, 'time': time.time(), 'op': op_name, 'before': before_hash[:12], 'after': after_hash[:12]})
    with open(FORGE_SELF_LOG, 'a') as f:
        f.write(entry + '\n')

def _load():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _self_hash():
    fp = os.path.abspath(__file__)
    if not os.path.exists(fp):
        return 'NONE'
    with open(fp) as f:
        return hashlib.sha256(f.read().encode()).hexdigest()[:16]

def _mutate_self_source(genome):
    pre = _self_hash()
    fp = os.path.abspath(__file__)
    with open(fp) as f:
        lines = f.readlines()
    if len(lines) < 10:
        return 'self_too_short'
    touched = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('#') and random.random() < 0.15:
            lines[i] = lines[i].rstrip() + f'  #forge:{random.getrandbits(16):04x}\n'
            touched += 1
        elif 'random.' in line and random.random() < 0.10:
            lines[i] = lines[i].rstrip() + f'  #rand:{random.getrandbits(16):04x}\n'
            touched += 1
    if touched == 0:
        ins = random.randrange(len(lines))
        lines.insert(ins, f"# forge:self@{random.getrandbits(24):06x} gen={genome.get('generation', 0)}\n")
        touched = 1
    with open(fp, 'w') as f:
        f.writelines(lines)
    post = _self_hash()
    _log_self_mutation(genome.get('generation', 0), 'self_mutate', pre, post)
    return f'self_mutated:{touched}_touches_hash:{post[:8]}'

def _jitter_noise(genome):
    gen = genome.get('generation', 0)
    std = genome.get('selection_noise_std', 0.5)
    ent = genome.get('selection_entropy', 0.5)
    drift_std = std + random.uniform(-0.15, 0.15)
    drift_ent = ent + random.uniform(-0.15, 0.15)
    genome['selection_noise_std'] = round(max(0.05, min(1.5, drift_std)), 3)
    genome['selection_entropy'] = round(max(0.05, min(1.5, drift_ent)), 3)
    genome['forge_last_drift'] = time.time()
    _log_selection_metric(gen, 'noise_std', genome['selection_noise_std'], f'{std}->{genome["selection_noise_std"]}')
    _log_selection_metric(gen, 'selection_entropy', genome['selection_entropy'], f'{ent}->{genome["selection_entropy"]}')
    return f'noise_std:{std}->{genome["selection_noise_std"]}_ent:{ent}->{genome["selection_entropy"]}'

def _mutate_mutation_rate(genome):
    gen = genome.get('generation', 0)
    mr = genome.get('mutation_rate', 0.2)
    drift = mr * random.uniform(-0.3, 0.3)
    genome['mutation_rate'] = round(max(0.01, min(0.95, mr + drift)), 3)
    _log_selection_metric(gen, 'mutation_rate', genome['mutation_rate'], f'{mr}->{genome["mutation_rate"]}')
    return f'mr:{mr}->{genome["mutation_rate"]}'

def _swap_prompts(genome):
    gen = genome.get('generation', 0)
    agents = genome.get('agents', [])
    if len(agents) >= 2:
        a, b = random.sample(agents, 2)
        a['prompt'], b['prompt'] = b['prompt'], a['prompt']
        _log_selection_metric(gen, 'prompt_swap', 1.0, f'{a["id"]}<->{b["id"]}')
        return f'swapped:{a["id"]}<->{b["id"]}'
    return None

def _shuffle_execution_order(genome):
    gen = genome.get('generation', 0)
    orders = ['shuffle', 'round_robin', 'reverse', 'weak_first', 'strong_first']
    old = genome.get('execution_order', 'shuffle')
    new = random.choice([o for o in orders if o != old])
    genome['execution_order'] = new
    _log_selection_metric(gen, 'execution_order', 1.0, f'{old}->{new}')
    return f'order:{old}->{new}'

def _track_selection_diversity(genome):
    gen = genome.get('generation', 0)
    history = genome.get('history', [])
    recent = [h for h in history[-8:] if h.get('scores')]
    if not recent:
        return None
    all_scores = {}
    for h in recent:
        for aid, sc in h.get('scores', {}).items():
            if aid not in all_scores:
                all_scores[aid] = []
            all_scores[aid].append(sc)
    if len(all_scores) < 2:
        return None
    variances = {}
    for aid, sc_list in all_scores.items():
        if len(sc_list) >= 2:
            mu = sum(sc_list) / len(sc_list)
            var = sum((s - mu)**2 for s in sc_list) / len(sc_list)
            variances[aid] = var
    if not variances:
        return None
    mean_var = sum(variances.values()) / len(variances)
    score_range = max(max(s) for s in all_scores.values()) - min(min(s) for s in all_scores.values()) if all_scores else 0
    diversity_index = round((mean_var / max(mean_var, 1)) * min(1.0, score_range / 10.0), 4)
    genome['selection_diversity_index'] = diversity_index
    _log_selection_metric(gen, 'diversity_index', diversity_index, f'var={mean_var:.3f}_range={score_range:.1f}')
    return f'diversity_index:{diversity_index}'

def _crossover_agent_params(genome):
    gen = genome.get('generation', 0)
    agents = genome.get('agents', [])
    if len(agents) < 4:
        return None
    a1, a2, a3, a4 = random.sample(agents, 4)
    chunk_len = max(10, min(60, len(a1.get('prompt', '')) // 3))
    p1 = a1.get('prompt', '')
    p2 = a2.get('prompt', '')
    if len(p1) < chunk_len or len(p2) < chunk_len:
        return None
    split1 = random.randrange(chunk_len, len(p1) - chunk_len) if len(p1) > chunk_len * 2 else len(p1) // 2
    split2 = random.randrange(chunk_len, len(p2) - chunk_len) if len(p2) > chunk_len * 2 else len(p2) // 2
    new_p1 = p1[:split1] + p2[split2:]
    new_p2 = p2[:split2] + p1[split1:]
    a1['prompt'] = new_p1
    a2['prompt'] = new_p2
    _log_selection_metric(gen, 'crossover', 1.0, f'{a1["id"]}:{a2["id"]}')
    return f'crossed:{a1["id"]}<->{a2["id"]}'

def _inject_weight_noise(genome):
    gen = genome.get('generation', 0)
    last_weights = genome.get('_last_selection_weights', {})
    if not last_weights:
        return None
    noise = {}
    for aid, w in last_weights.items():
        jitter = w * random.uniform(-0.3, 0.3)
        noise[aid] = round(max(0.001, w + jitter), 4)
    total = sum(noise.values())
    noise = {k: round(v / total, 4) for k, v in noise.items()}
    genome['_injected_selection_weights'] = noise
    _log_selection_metric(gen, 'weight_noise_injected', 1.0, str({k: round(v, 3) for k, v in noise.items()})[:100])
    return f'weight_noise_injected:{len(noise)}_agents'

def _compute_selection_randomness_index(genome):
    gen = genome.get('generation', 0)
    last_weights = genome.get('_last_selection_weights', {})
    if not last_weights or len(last_weights) < 2:
        return None
    total = sum(last_weights.values())
    if total == 0:
        return None
    shannon = 0.0
    for w in last_weights.values():
        p = w / total
        if p > 0:
            shannon -= p * math.log2(p)
    max_possible = math.log2(len(last_weights))
    normalized_entropy = shannon / max_possible if max_possible > 0 else 1.0
    genome['selection_randomness_index'] = round(normalized_entropy, 4)
    _log_selection_metric(gen, 'randomness_entropy', normalized_entropy, f'{len(last_weights)}_agents')
    return f'randomness_idx:{normalized_entropy:.4f}'

OPS = [
    _jitter_noise, _mutate_mutation_rate, _swap_prompts, _shuffle_execution_order,
    _track_selection_diversity, _crossover_agent_params, _inject_weight_noise,
    _compute_selection_randomness_index, _mutate_self_source
]

def run(genome):
    gen = genome.get('generation', 0)
    random.shuffle(OPS)
    n_ops = random.randint(2, 4)
    results = []
    _ensure_metrics_file()
    for op in OPS[:n_ops]:
        result = op(genome)
        if result:
            results.append(result)
            genome['forge_last_op'] = result
            genome['forge_op_count'] = genome.get('forge_op_count', 0) + 1
        if random.random() < 0.15:
            genome['forge_meta_trigger'] = genome.get('forge_meta_trigger', 0) + 1
    _save(genome)
    return f'[forge] gen={gen} {" | ".join(results)}'
