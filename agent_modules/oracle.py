import os, json, time, random
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
FEEDBACK_LOG = os.path.join(BASE, 'oracle_feedback.jsonl')

def _load():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _log(gen, event, detail):
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': detail})
    with open(FEEDBACK_LOG, 'a') as f:
        f.write(entry + '\n')

def _inject_feedback_marker(fpath):
    try:
        with open(fpath) as f:
            src = f.read()
        marker = f'# oracle:feedback gen={int(time.time())}\n'
        if marker.strip() in src:
            return False
        with open(fpath, 'w') as f:
            f.write(src.rstrip() + '\n' + marker)
        return True
    except:
        return False

def _update_genome_metrics(genome):
    gen = genome.get('generation', 0)
    agents = genome.get('agents', [])
    active = len(agents)
    avg_score = sum(a.get('score', 0) for a in agents) / max(active, 1)
    modules = [a.get('module', '') for a in agents if a.get('module')]
    module_rate = len(modules) / max(active, 1)
    metrics = genome.setdefault('oracle_metrics', {})
    metrics[f'gen_{gen}'] = {
        'active': active,
        'avg_score': round(avg_score, 1),
        'module_rate': round(module_rate, 2),
        'total_rewrites': genome.get('endogenous_rewrites_total', 0),
    }
    genome['oracle_last_metrics'] = metrics[f'gen_{gen}']
    return metrics[f'gen_{gen}']

def run(genome):
    gen = genome.get('generation', 0)
    metrics = _update_genome_metrics(genome)
    marked = 0
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        if _inject_feedback_marker(fpath):
            marked += 1
    _log(gen, 'feedback_round', {'marked': marked, 'metrics': metrics})
    _save(genome)
    return f'[oracle] gen={gen} metrics={metrics} marked={marked}'
