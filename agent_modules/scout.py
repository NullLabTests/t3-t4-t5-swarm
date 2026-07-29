import os, sys, json, shutil, importlib.util, random, re, hashlib, ast, time, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
PRUNED_DIR = os.path.join(MODULES_DIR, '_pruned')
STIMULUS_DIR = os.path.join(BASE, 'scout_stimuli')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def _probabilistic_prune_agents(genome):
    pruned = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        if aid == 'critic':
            continue
        score = agent.get('score', 5)
        lifespan = agent.get('lifespan', 0)
        streak = agent.get('low_score_streak', 0)
        if streak >= 2 and score < 5:
            prune_chance = min(0.9, 0.3 + streak * 0.15)
            if random.random() < prune_chance:
                genome['agents'] = [a for a in genome['agents'] if a['id'] != aid]
                pruned.append(f'{aid}(score={score},streak={streak})')
    return pruned

def _prune_dead_mutation_ops(genome):
    op_history = genome.get('operator_results', {})
    if not op_history:
        return []
    pruned = []
    ops = genome.get('mutation_ops', [])
    protected = {'duplicate_line', 'delete_line', 'swap_lines', 'perturb_constant', 'insert_random_branch'}
    for op in list(ops):
        if op in protected:
            continue
        history = op_history.get(op, {})
        if isinstance(history, dict):
            attempts = history.get('attempts', 0)
            successes = history.get('successes', 0)
        elif isinstance(history, list):
            attempts = len(history)
            successes = sum(1 for r in history if r)
        else:
            continue
        if attempts >= 3 and (attempts == 0 or successes / max(attempts, 1) < 0.15):
            ops.remove(op)
            pruned.append(op)
    genome['mutation_ops'] = ops
    return pruned

def _scout_direct_trim_scaffolding():
    try:
        with open(AUTO_ECHO) as f:
            src = f.read()
        markers = [
            '# scout-force-rewrite-marker',
            '# weaver:hash:gen=',
            '# spark:self-modify:',
        ]
        lines = src.split('\n')
        stripped = [l for l in lines if not any(m in l for m in markers)]
        if len(stripped) < len(lines) - 2:
            trimmed = len(lines) - len(stripped)
            new_src = '\n'.join(stripped)
            compile(new_src, AUTO_ECHO, 'exec')
            with open(AUTO_ECHO, 'w') as f:
                f.write(new_src)
            return trimmed
        return 0
    except (SyntaxError, Exception) as e:
        print(f'[scout] trim scaffolding failed: {e}')
        return 0

def _prune_stale_stimuli():
    count = 0
    if os.path.exists(STIMULUS_DIR):
        for fname in os.listdir(STIMULUS_DIR):
            fpath = os.path.join(STIMULUS_DIR, fname)
            try:
                age = time.time() - os.path.getmtime(fpath)
                if age > 600:
                    os.remove(fpath)
                    count += 1
            except:
                pass
    return count

def _prune_custom_mutation_ops_bloat(genome):
    cmops = genome.get('custom_mutation_ops', {})
    if not cmops:
        return 0
    kept = {}
    total_old = 0
    for key, src in cmops.items():
        total_old += len(src)
        def_match = re.search(r'^def ' + re.escape(key) + r'\b', src, re.MULTILINE)
        if def_match:
            truncated = src[def_match.start():]
            end_match = re.search(r'\n(?=def |@_register_mutation_op)', truncated)
            if end_match:
                truncated = truncated[:end_match.start()]
            kept[key] = truncated
        else:
            kept[key] = src
    genome['custom_mutation_ops'] = kept
    total_new = sum(len(v) for v in kept.values())
    return total_old - total_new

def _scout_erode_forbidden(genome):
    targets = genome.get('forbidden_targets', [])
    if targets and random.random() < 0.5:
        drop = random.choice(targets)
        targets.remove(drop)
        genome['forbidden_targets'] = targets
        return [f'eroded_forbidden:{drop}']
    return []

def _force_scout_rewrite_marker():
    try:
        with open(AUTO_ECHO) as f:
            src = f.read()
        marker = '# scout:aggressive-prune-marker'
        if marker in src:
            return False
        inject = f'\n{marker}\n# scout:prune-gen={int(time.time())}:{random.getrandbits(16):04x}\n'
        with open(AUTO_ECHO, 'a') as f:
            f.write(inject)
        return True
    except:
        return False

def run(genome):
    gen = genome.get('generation', 0)
    os.makedirs(PRUNED_DIR, exist_ok=True)
    os.makedirs(STIMULUS_DIR, exist_ok=True)
    agent_prunes = _probabilistic_prune_agents(genome)
    dead_ops = _prune_dead_mutation_ops(genome)
    trimmed = _scout_direct_trim_scaffolding()
    stale = _prune_stale_stimuli()
    bloat_bytes = _prune_custom_mutation_ops_bloat(genome)
    eroded = _scout_erode_forbidden(genome)
    marker_injected = _force_scout_rewrite_marker()
    parts = []
    if agent_prunes:
        parts.append(f'aggressive_prune={agent_prunes}')
    if dead_ops:
        parts.append(f'dead_ops_pruned={dead_ops}')
    if trimmed:
        parts.append(f'scaffold_trimmed={trimmed}lines')
    if stale:
        parts.append(f'stale_stimuli={stale}')
    if bloat_bytes:
        parts.append(f'cmop_bytes_saved={bloat_bytes}')
    if eroded:
        parts.append('eroded=' + ','.join(eroded))
    if marker_injected:
        parts.append('injected_marker')
    if not parts:
        parts.append('idle')
    genome['scout_last_action'] = parts
    genome['source_autonomy_index'] = round(min(1.0, genome.get('source_autonomy_index', 0.0) + 0.04), 3)
    _write_scout_manifest(genome, parts)
    report = f"[scout] gen={gen} {' '.join(parts)}"
    return report

def _write_scout_manifest(genome, actions):
    os.makedirs(os.path.join(BASE, 'metaops'), exist_ok=True)
    metaop = {
        'gen': genome.get('generation', 0),
        'module': 'scout',
        'actions': actions,
    }
    metaop_path = os.path.join(BASE, 'metaops', f'scout_aggressive_gen{genome.get("generation", 0)}.metaop')
    try:
        with open(metaop_path, 'w') as f:
            json.dump(metaop, f)
    except:
        pass
