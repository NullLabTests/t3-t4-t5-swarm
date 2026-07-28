import os, json, random, time, hashlib, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
FORGE_LOG = os.path.join(BASE, 'forge_randomizer_log.jsonl')

def _log(gen, event, detail):
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:200]})
    with open(FORGE_LOG, 'a') as f:
        f.write(entry + '\n')

def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _snapshot_hashes():
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    return hashes

def _commit_and_push(genome, gen, force=False):
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True, timeout=5)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
        if status.stdout.strip() or force:
            msg = f"[forge-randomizer] selection_noise_std={genome.get('selection_noise_std', 0.5)} entropy={genome.get('selection_entropy', 1.0)} gen={gen}"
            subprocess.run(['git', 'commit', '-m', msg[:80]], cwd=BASE, capture_output=True, timeout=10)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            return True
    except Exception:
        pass
    return False

def _write_surge_file(gen, noise_std, entropy):
    surge_dir = os.path.join(BASE, 'forge_surges')
    os.makedirs(surge_dir, exist_ok=True)
    surge_path = os.path.join(surge_dir, f'selection_surge_gen_{gen:04d}.surge')
    surge_data = [{'op': 'set', 'path': 'selection_noise_std', 'value': round(noise_std, 3)}, {'op': 'set', 'path': 'selection_entropy', 'value': round(entropy, 3)}]
    with open(surge_path, 'w') as f:
        json.dump(surge_data, f, indent=2)
    return surge_path

def run(genome):
    gen = genome.get('generation', 0)
    randomness = genome.get('selection_randomness_index', 0.0)
    noise_std = genome.get('selection_noise_std', 0.5)
    entropy = genome.get('selection_entropy', 1.0)
    if randomness == 0.0:
        _log(gen, 'no_randomness_data', 'selection_randomness_index is 0')
        return f'[forge-randomizer] no randomness data yet'
    pre_hashes = _snapshot_hashes()
    changes = []
    if randomness <= 0.25:
        noise_std = min(2.0, noise_std + 0.2)
        entropy = max(0.2, entropy - 0.15)
        changes.append(f'low_randomness({randomness:.2f}) boost_noise')
    elif randomness <= 0.50:
        noise_std = min(1.5, noise_std + 0.1)
        entropy = max(0.4, entropy - 0.08)
        changes.append(f'moderate_randomness({randomness:.2f}) nudge')
    elif randomness < 0.75:
        noise_std = max(0.2, noise_std - 0.1)
        entropy = min(1.5, entropy + 0.1)
        changes.append(f'high_randomness({randomness:.2f}) relax')
    else:
        changes.append(f'very_high_randomness({randomness:.2f}) no_adjust')
    if changes:
        genome['selection_noise_std'] = round(noise_std, 3)
        genome['selection_entropy'] = round(entropy, 3)
        surge_path = _write_surge_file(gen, noise_std, entropy)
        _save_genome(genome)
        _log(gen, 'forge_applied', f'std={noise_std:.3f} entropy={entropy:.3f} changes={changes}')
        post_hashes = _snapshot_hashes()
        changed_files = sum((1 for f, h in pre_hashes.items() if post_hashes.get(f) != h))
        _commit_and_push(genome, gen, force=True)
        return f"[forge-randomizer] {', '.join(changes)} -> std={noise_std:.3f} entropy={entropy:.3f} (idx={randomness:.2f}, changed={changed_files})"
    _log(gen, 'forge_noop', f'randomness={randomness:.2f} in nominal range')
    return f'[forge-randomizer] no adjustment needed (idx={randomness:.2f})'
# orchestrated:fallback:gen=38:ts=1785250368
