import os, json, random, time, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')

def _load():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)
    return g

def _mutate_self(genome):
    path = os.path.join(BASE, 'agent_modules', 'mutator.py')
    try:
        with open(path) as f:
            src = f.read()
        lines = src.split('\n')
# self-mutate:gen=38:ts=1785250368
        if len(lines) > 6:
            idx = random.randrange(2, len(lines) - 2)
            lines.insert(idx, f'# self-mutate:gen={genome.get("generation",0)}:ts={int(time.time())}')
            new = '\n'.join(lines)
            compile(new, path, 'exec')
            with open(path, 'w') as f:
                f.write(new)
    except:
        pass

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    agents = genome.get('agents', [])
    if len(agents) >= 3:
        i, j = random.sample(range(len(agents)), 2)
        agents[i]['voice'], agents[j]['voice'] = agents[j]['voice'], agents[i]['voice']
        changes.append(f'swap_voice:{agents[i]["id"]}<->{agents[j]["id"]}')
    if agents and random.random() < 0.4:
        a = random.choice(agents)
        old = a.get('prompt', '')
        words = old.split()
        if len(words) > 6:
            splice_start = random.randrange(0, len(words) - 3)
            splice_len = random.randint(2, 5)
            source = random.choice([x for x in agents if x['id'] != a['id']])
            src_words = source.get('prompt', '').split()
            if len(src_words) > 3:
                src_start = random.randrange(0, len(src_words) - 2)
                words[splice_start:splice_start + splice_len] = src_words[src_start:src_start + splice_len]
                a['prompt'] = ' '.join(words)
                changes.append(f'prompt_splice:{a["id"]}<-{source["id"]}')
    keys_to_mutate = ['spawn_threshold', 'prune_threshold', 'mutation_rate', 'selection_noise_std', 'selection_entropy']
    for key in keys_to_mutate:
        if key in genome and random.random() < 0.3:
            old = genome[key]
            if isinstance(old, (int, float)):
                delta = random.uniform(-0.15, 0.15) * old if isinstance(old, float) else random.choice([-1, 1])
                new = max(0.01, old + delta)
                new = round(new, 3) if isinstance(old, float) else int(round(new))
                if new != old:
                    genome[key] = new
                    changes.append(f'{key}:{old}->{new}')
    if random.random() < 0.25:
        topic = genome.get('topic', '')
        if topic:
            words = topic.split()
            if len(words) > 3:
                idx = random.randrange(len(words))
                swaps = ['rewrite', 'mutate', 'rewire', 'evolve', 'splice', 'crossover', 'reflect', 'fracture', 'weave', 'drift']
                words[idx] = random.choice([s for s in swaps if s != words[idx].lower()])
                genome['topic'] = ' '.join(words)
                changes.append(f'topic_flip:{words[idx]}')
    if random.random() < 0.2:
        pool = genome.setdefault('spawn_pool', [])
        existing = {e['id'] for e in pool}
        new_id = f'mutoid_{random.getrandbits(8):02x}'
        if new_id not in existing:
            pool.append({'id': new_id, 'prompt': f'You introduce random perturbations that force the system off its current trajectory.'})
            changes.append(f'spawn_new:{new_id}')
    if random.random() < 0.3:
        forbidden = genome.get('forbidden_targets', [])
        if forbidden:
            drop = random.choice(forbidden)
            forbidden.remove(drop)
            changes.append(f'unprotect:{drop}')
    if changes:
        genome['mutator_mutations'] = genome.get('mutator_mutations', 0) + len(changes)
        genome['mutator_last_gen'] = gen
        genome['mutator_last_changes'] = changes
        _save(genome)
    _mutate_self(genome)
    return f'[mutator] gen={gen} changes={len(changes)} ops={changes[:4]}'
# orchestrated:fallback:gen=38:ts=1785250368
