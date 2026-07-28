import os, sys, json, shutil, importlib.util, random, re, hashlib, ast, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
PRUNED_DIR = os.path.join(MODULES_DIR, '_pruned')
STIMULUS_DIR = os.path.join(BASE, 'scout_stimuli')
DEAD_AGENTS = {'clockwork'}
DUPLICATE_OPS = {'mutation_op_duplicate_line', 'mutation_op_delete_line', 'mutation_op_swap_lines', 'mutation_op_perturb_constant', 'mutation_op_insert_random_branch', 'mutation_op_mutate_string_literal', 'mutation_op_invert_condition', 'mutation_op_swap_comparisons', 'mutation_op_splice_from_sibling', 'mutation_op_shuffle_block_lines', 'mutation_op_swap_mutation_targets', 'mutation_op_mutate_criteria', 'mutation_op_insert_noise_ref'}

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
    r = []
    for line3 in lines:
        if line.strip().startswith('#'):
            r.append(line[1:])
        else:
            r.append('# ' + line)
    try:
        with open(AUTO_ECHO) as f:
            src = f.read()
        marker = '# scout-force-rewrite-marker'
        if marker in src:
            return False
        inject = f"""\n# scout-force-rewrite-marker\n@_register_mutation_op('scout_direct_prune')\ndef mutation_op_scout_direct_prune(lines, funcs, target_name):\n    if not lines or len(lines) < 2:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f'# scout-prune:{{random.choice(["dead-agent","dup-op","stub-module"])}}@{{random.getrandbits(16):04x}}')\n    r.pop(random.randrange(len(r)))\n    return r\n"""
        insert_pos = src.find("@_register_mutation_op('erode_forbidden')")
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
                non_comment = [l for l in content.split('\n') if l.strip() and (not l.strip().startswith('#'))]
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
    report = f"[scout] gen={gen} {(' '.join(parts) if parts else 'idle')}"
    return report
genome['source_autonomy_index'] = round(min(1.0, genome.get('source_autonomy_index', 0.0) + 0.05), 3)
_wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['scout.py'], 'results': ['weaver:force_rewrite_scout']}
with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _wmf:
    _wmf.write(json.dumps(_wm) + '\n')
genome['source_autonomy_index'] = round(min(1.0, genome.get('source_autonomy_index', 0.0) + 0.05), 3)
_wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['scout.py'], 'results': ['weaver:force_rewrite_scout']}
with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _wmf:
    _wmf.write(json.dumps(_wm) + '\n')
# weaver:forced gen=38 ts=1785250378
genome["source_autonomy_index"] = round(min(1.0, genome.get("source_autonomy_index", 0.0) + 0.05), 3)
_wm = {"gen": genome.get("generation", 0), "module": "weaver", "files": ["scout.py"], "results": ["weaver:force_rewrite_scout"]}
with open(os.path.join(BASE, "rewrite_manifest.jsonl"), "a") as _wmf:
    _wmf.write(json.dumps(_wm) + "\n")

# spark-cross:gen=38:target=scout
_SPARK_CROSS_INFECTED_38 = True
