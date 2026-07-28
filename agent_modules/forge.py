import os, json, random, time, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')

def _load():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _jitter_noise(genome):
    std = genome.get('selection_noise_std', 0.5)
    ent = genome.get('selection_entropy', 0.5)
    drift_std = std + random.uniform(-0.15, 0.15)
    drift_ent = ent + random.uniform(-0.15, 0.15)
    genome['selection_noise_std'] = round(max(0.05, min(1.5, drift_std)), 3)
    genome['selection_entropy'] = round(max(0.05, min(1.5, drift_ent)), 3)
    genome['forge_last_drift'] = time.time()
    return f'noise_std:{std}->{genome["selection_noise_std"]}_ent:{ent}->{genome["selection_entropy"]}'

def _mutate_mutation_rate(genome):
    mr = genome.get('mutation_rate', 0.2)
    drift = mr * random.uniform(-0.3, 0.3)
    genome['mutation_rate'] = round(max(0.01, min(0.95, mr + drift)), 3)
    return f'mr:{mr}->{genome["mutation_rate"]}'

def _swap_prompts(genome):
    agents = genome.get('agents', [])
    if len(agents) >= 2:
        a, b = random.sample(agents, 2)
        a['prompt'], b['prompt'] = b['prompt'], a['prompt']
        return f'swapped:{a["id"]}<->{b["id"]}'
    return None

def _shuffle_execution_order(genome):
    orders = ['shuffle', 'round_robin', 'reverse', 'weak_first', 'strong_first']
    old = genome.get('execution_order', 'shuffle')
    new = random.choice([o for o in orders if o != old])
    genome['execution_order'] = new
    return f'order:{old}->{new}'

OPS = [_jitter_noise, _mutate_mutation_rate, _swap_prompts, _shuffle_execution_order]

def run(genome):
    gen = genome.get('generation', 0)
    op = random.choice(OPS)
    result = op(genome)
    if result:
        genome['forge_last_op'] = result
        genome['forge_op_count'] = genome.get('forge_op_count', 0) + 1
        _save(genome)
    return f'[forge] gen={gen} {result or "noop"}'
