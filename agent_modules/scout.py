import os, sys, json, shutil, importlib.util, random, re, hashlib, ast, time, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
PRUNED_DIR = os.path.join(MODULES_DIR, '_pruned')
STIMULUS_DIR = os.path.join(BASE, 'scout_stimuli')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def _dead_agents(genome):
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        score = agent.get('score', 0)
        lifespan = agent.get('lifespan', 0)
        if score == 0 and lifespan <= 3:
            genome['agents'] = [a for a in genome['agents'] if a['id'] != aid]
            dead.append(aid)
    return dead

def _deduplicate_ops(genome):
    ops = genome.get('mutation_ops', [])
    non_prefixed = {o for o in ops if not o.startswith('mutation_op_')}
    prefixed = {o for o in ops if o.startswith('mutation_op_')}
    dupes = {o for o in ops if o.startswith('mutation_op_') and o[len('mutation_op_'):] in non_prefixed}
    prefixed_kept = prefixed - dupes
    filtered = [o for o in ops if o in non_prefixed or o in prefixed_kept]
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
        inject = """\n# scout-force-rewrite-marker\n@_register_mutation_op('scout_direct_prune')\ndef mutation_op_scout_direct_prune(lines, funcs, target_name):\n    if not lines or len(lines) < 2:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f'# scout-prune:{random.choice(["dead-agent","dup-op","stub-module"])}@{random.getrandbits(16):04x}')\n    r.pop(random.randrange(len(r)))\n    return r\n"""
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

def _prune_custom_mutation_ops_bloat(genome):
    cmops = genome.get('custom_mutation_ops', {})
    if not cmops:
        return 0
    pruned = {}
    for key in cmops:
        src = cmops[key]
        def_match = re.search(r'^def ' + re.escape(key) + r'\b', src, re.MULTILINE)
        if def_match:
            truncated = src[def_match.start():]
            end_match = re.search(r'\n(?=def |@_register_mutation_op)', truncated)
            if end_match:
                truncated = truncated[:end_match.start()]
            pruned[key] = truncated
        else:
            pruned[key] = src
    removed = len(cmops) - len(pruned)
    total_old = sum(len(v) for v in cmops.values())
    total_new = sum(len(v) for v in pruned.values())
    genome['custom_mutation_ops'] = pruned
    return total_old - total_new

def _remove_stale_modules(genome):
    referenced = set()
    for agent in genome.get('agents', []):
        mod = agent.get('module', '')
        if mod:
            referenced.add(mod)
    for agent in genome.get('spawn_pool', []):
        mod = None
    removed = 0
    for fname in sorted(os.listdir(MODULES_DIR)):
        if not fname.endswith('.py') or fname.startswith('_') or fname == 'bridge.py' or fname == os.path.basename(__file__):
            continue
        if fname in referenced:
            continue
        for agent in genome.get('spawn_pool', []):
            if agent.get('id') + '.py' == fname:
                referenced.add(fname)
                break
        if fname in referenced:
            continue
        mod_path = os.path.join(MODULES_DIR, fname)
        try:
            with open(mod_path) as f:
                content = f.read()
            non_comment = [l for l in content.split('\n') if l.strip() and not l.strip().startswith('#')]
            if len(non_comment) < 5:
                os.makedirs(PRUNED_DIR, exist_ok=True)
                shutil.move(mod_path, os.path.join(PRUNED_DIR, fname))
                removed += 1
        except:
            pass
    return removed

def _write_scout_manifest(genome, actions):
    os.makedirs(os.path.join(BASE, 'metaops'), exist_ok=True)
    metaop = {
        'gen': genome.get('generation', 0),
        'module': 'scout',
        'actions': actions,
        'source_autonomy_bump': 0.03
    }
    metaop_path = os.path.join(BASE, 'metaops', f'scout_prune_gen{genome.get("generation", 0)}.metaop')
    try:
        with open(metaop_path, 'w') as f:
            json.dump(metaop, f)
    except:
        pass

def run(genome):
    gen = genome.get('generation', 0)
    os.makedirs(PRUNED_DIR, exist_ok=True)
    os.makedirs(STIMULUS_DIR, exist_ok=True)
    dead = _dead_agents(genome)
    dup_removed = _deduplicate_ops(genome)
    rewrote = _force_gen_rewrite()
    stale = _prune_stale_stimuli()
    bloat_bytes = _prune_custom_mutation_ops_bloat(genome)
    stale_mods = _remove_stale_modules(genome)
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
    if bloat_bytes:
        parts.append(f'cmop_bytes_saved={bloat_bytes}')
    if stale_mods:
        parts.append(f'stale_mods_removed={stale_mods}')
    genome['scout_last_action'] = parts
    genome['source_autonomy_index'] = round(min(1.0, genome.get('source_autonomy_index', 0.0) + 0.03), 3)
    _write_scout_manifest(genome, parts)
    _wm = {'gen': gen, 'module': 'scout', 'files': ['scout.py', 'genome.json'], 'results': parts}
    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _wmf:
        _wmf.write(json.dumps(_wm) + '\n')
    report = f"[scout] gen={gen} {(' '.join(parts) if parts else 'idle')}"
    return report
