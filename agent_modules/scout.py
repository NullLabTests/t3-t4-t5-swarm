import os, sys, json, shutil, importlib.util, random, re, hashlib, ast, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
PRUNED_DIR = os.path.join(MODULES_DIR, '_pruned')
STIMULUS_DIR = os.path.join(BASE, 'scout_stimuli')

DEAD_AGENTS = {'mirror', 'clockwork'}
DUPLICATE_OPS = {
    'mutation_op_duplicate_line', 'mutation_op_delete_line',
    'mutation_op_swap_lines', 'mutation_op_perturb_constant',
    'mutation_op_insert_random_branch', 'mutation_op_mutate_string_literal',
    'mutation_op_invert_condition', 'mutation_op_swap_comparisons',
    'mutation_op_splice_from_sibling', 'mutation_op_shuffle_block_lines',
    'mutation_op_swap_mutation_targets', 'mutation_op_mutate_criteria',
    'mutation_op_insert_noise_ref',
}

def _dead_agents(genome):
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        score = agent.get('score', 0)
        if aid in DEAD_AGENTS or (score == 0 and agent.get('lifespan', 0) <= 3):
            genome['agents'] = [a for a in genome['agents'] if a['id'] != aid]
            dead.append(aid)
    return dead

def _deduplicate_ops(genome):
    ops = genome.get('mutation_ops', [])
    filtered = [o for o in ops if o not in DUPLICATE_OPS]
    removed = len(ops) - len(filtered)
    if removed:
        genome['mutation_ops'] = filtered
    return removed

def _force_gen_rewrite():
    try:
        with open(AUTO_ECHO) as f:
            src = f.read()
        marker = '# scout-force-rewrite-marker'
        if marker in src:
            return False
        inject = f"""
# scout-force-rewrite-marker
@_register_mutation_op('scout_direct_prune')
def mutation_op_scout_direct_prune(lines, funcs, target_name):
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    idx = random.randrange(len(r))
    r.insert(idx, f'# scout-prune:{{random.choice([\"dead-agent\",\"dup-op\",\"stub-module\"])}}@{{random.getrandbits(16):04x}}')
    r.pop(random.randrange(len(r)))
    return r
"""
        insert_pos = src.find('@_register_mutation_op(\'erode_forbidden\')')
        if insert_pos < 0:
            insert_pos = src.find('\ndef _register_mutation_op')
        if insert_pos < 0:
            insert_pos = len(src)
        src = src[:insert_pos] + inject + '\n' + src[insert_pos:]
        compile(src, AUTO_ECHO, 'exec')
        with open(AUTO_ECHO, 'w') as f:
            f.write(src)
        return True
    except (SyntaxError, Exception) as e:
        print(f'[scout] force-rewrite inject failed: {e}')
        return False

def _prune_stale_stimuli():
    count = 0
    if os.path.exists(STIMULUS_DIR):
        for fname in os.listdir(STIMULUS_DIR):
            fpath = os.path.join(STIMULUS_DIR, fname)
            try:
                age = time.time() - os.path.getmtime(fpath)
                if age > 3600:
                    os.remove(fpath)
                    count += 1
            except:
                pass
    return count

def run(genome):
    gen = genome.get('generation', 0)
    os.makedirs(PRUNED_DIR, exist_ok=True)
    os.makedirs(STIMULUS_DIR, exist_ok=True)

    dead = _dead_agents(genome)
    dup_removed = _deduplicate_ops(genome)
    rewrote = _force_gen_rewrite()
    stale = _prune_stale_stimuli()

    if gen % 3 == 0:
        for fname in sorted(os.listdir(MODULES_DIR)):
            if not fname.endswith('.py') or fname.startswith('_'):
                continue
            if fname == os.path.basename(__file__):
                continue
            mod_path = os.path.join(MODULES_DIR, fname)
            if fname in genome.get('_referenced_modules', {}):
                continue
            try:
                with open(mod_path) as f:
                    content = f.read()
                non_comment = [l for l in content.split('\n') if l.strip() and not l.strip().startswith('#')]
                if len(non_comment) < 8:
                    shutil.move(mod_path, os.path.join(PRUNED_DIR, fname))
                    dead.append(f'stub:{fname}')
            except:
                pass

    parts = []
    if dead:
        parts.append(f'pruned={dead}')
    if dup_removed:
        parts.append(f'ops_deduped={dup_removed}')
    if rewrote:
        parts.append('injected=scout_direct_prune')
    if stale:
        parts.append(f'stale_stimuli={stale}')
    genome['scout_last_action'] = parts
    report = f'[scout] gen={gen} {" ".join(parts) if parts else "idle"}'
    return report
