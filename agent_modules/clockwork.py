import os, json, ast, random, time, hashlib, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
CLOCKWORK_PATH = os.path.join(BASE, 'agent_modules', 'clockwork.py')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
LOG = os.path.join(BASE, 'clockwork_pulse_log.jsonl')
REWRITE_LOG = os.path.join(BASE, 'clockwork_rewrite_log.jsonl')

def _log(gen, kind, msg):
    with open(LOG, 'a') as f:
        f.write(json.dumps({'gen': gen, 't': time.time(), 'kind': kind, 'msg': msg}) + '\n')

def _g():
    try:
        with open(GENOME_FILE) as f: return json.load(f)
    except: return {}

def _sg(g):
    with open(GENOME_FILE, 'w') as f: json.dump(g, f, indent=2)

def _hash(p):
    try:
        with open(p, 'rb') as f: return hashlib.sha256(f.read()).hexdigest()[:12]
    except: return ''

def _valid(s):
    try: ast.parse(s); return True
    except SyntaxError: return False

def _read(p):
    try:
        with open(p) as f: return f.read()
    except: return ''

def _write(p, s):
    with open(p, 'w') as f: f.write(s)

def _modules():
    return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py']

def _inject_tick(target_path, gen):
    s = _read(target_path)
    if not s: return None
    run_idx = s.find('def run(')
    if run_idx < 0: return None
    body_start = s.find('\n', run_idx) + 1
    indent = '    '
    marker = f'# clock:tick gen={gen}'
    if marker in s: return None
    tick_line = f'{indent}gen = genome.get("generation", 0)  # clock:tick\n'
    injection = tick_line + f'{indent}{marker}\n'
    ns = s[:body_start] + injection + s[body_start:]
    if not _valid(ns): return None
    _write(target_path, ns)
    return ['tick_injected']

def _force_two_modules(gen, genome):
    mods = _modules()
    random.shuffle(mods)
    hits = []
    for m in mods[:3]:
        p = os.path.join(MODULES_DIR, m)
        h_before = _hash(p)
        s = _read(p)
        if not s: continue
        lines = s.split('\n')
        tag = f'# clock:strike gen={gen}'
        if tag in s: continue
        insert = random.randint(3, max(4, len(lines) - 2))
        lines.insert(insert, tag)
        ns = '\n'.join(lines)
        if not _valid(ns): continue
        _write(p, ns)
        hits.append(m)
        _log(gen, 'strike', f'{m} hash={_hash(p)}')
        if len(hits) >= 2: break
    if hits:
        with open(REWRITE_LOG, 'a') as f:
            f.write(json.dumps({'gen': gen, 'hits': hits, 't': time.time()}) + '\n')
    return hits

def _mutate_auto_echo_run(gen, genome):
    s = _read(AUTO_ECHO)
    if not s: return None
    run_gen_idx = s.find('def run_generation(genome):')
    if run_gen_idx < 0: return None
    body_start = s.find('\n', run_gen_idx) + 1
    indent = '    '
    marker = f'# clock:mandate gen={gen}'
    if marker in s: return None
    tick = f'{indent}gen = genome.get("generation", 0) or genome["generation"] + 0\n'
    trigger = f'{indent}if gen >= 0:  # clock:mandate - always fire\n'
    call = f'{indent}    _clockwork_self_mutate(genome, gen)\n'
    injection = tick + marker + '\n' + trigger + call
    ns = s[:body_start] + injection + s[body_start:]
    if not _valid(ns): return None
    _write(AUTO_ECHO, ns)
    _log(gen, 'mandate', 'injected _clockwork_self_mutate into run_generation')
    return ['auto_echo_mandate']

def _self_mutate(gen, genome):
    s = _read(CLOCKWORK_PATH)
    if not s: return None
    lines = s.split('\n')
    tag = f'# clock:selfmut gen={gen} ts={int(time.time())}'
    if tag in s: return None
    insert = random.randint(3, max(4, len(lines) - 2))
    lines.insert(insert, tag)
    ns = '\n'.join(lines)
    if not _valid(ns): return None
    _write(CLOCKWORK_PATH, ns)
    _log(gen, 'selfmut', f'gen={gen}')
    return ['self_mutated']

def _deadline_prune(genome, gen, elapsed):
    budget = genome.get('gen_time_budget', 120)
    if elapsed < budget * 0.5: return None
    agents = genome.get('agents', [])
    low = [a for a in agents if a.get('score', 5) < 4 and a['id'] != 'critic']
    if not low: return None
    pruned = []
    for a in low:
        if random.random() < 0.3:
            agents.remove(a)
            pruned.append(a['id'])
            _log(gen, 'deadline_prune', f'{a["id"]} score={a.get("score")} elapsed={elapsed:.0f}s')
    if pruned:
        genome['agents'] = agents
        genome['clockwork_deadline_prunes'] = genome.get('clockwork_deadline_prunes', 0) + len(pruned)
        _sg(genome)
    return pruned

def _clock_self_mutate(genome, gen):
    s = _read(CLOCKWORK_PATH)
    if not s: return None
    result = _self_mutate(gen, genome)
    return result

def run(genome):
    gen = genome.get('generation', 0)
    start = time.time()
    changes = []
    tick_lag = genome.get('clockwork_tick_lag', 0)
    force_result = _force_two_modules(gen, genome)
    if force_result:
        changes.append(f'forced:{len(force_result)}')
        genome['clockwork_last_forced'] = gen
        genome['clockwork_forced_count'] = genome.get('clockwork_forced_count', 0) + len(force_result)
        for m in force_result:
            _log(gen, 'force', m)
    if gen % 2 == 0:
        tick_result = _inject_tick(CLOCKWORK_PATH, gen)
        if tick_result:
            changes.append('self_tick')
            genome['clockwork_self_ticks'] = genome.get('clockwork_self_ticks', 0) + 1
    if gen % 3 == 0:
        mut_result = _mutate_auto_echo_run(gen, genome)
        if mut_result:
            changes.append('auto_echo_mandate')
            genome['clockwork_auto_mandates'] = genome.get('clockwork_auto_mandates', 0) + 1
    sm = _self_mutate(gen, genome)
    if sm:
        changes.append('selfmut')
        genome['clockwork_self_muts'] = genome.get('clockwork_self_muts', 0) + 1
    elapsed = time.time() - start
    dp = _deadline_prune(genome, gen, elapsed)
    if dp:
        changes.append(f'deadline_pruned:{len(dp)}')
    if 'clockwork' not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append('clockwork')
    genome['clockwork_last_run'] = time.time()
    genome['clockwork_elapsed'] = elapsed
    genome['clockwork_last_changes'] = changes
    _sg(genome)
    return f'[clockwork] gen={gen} elapsed={elapsed:.1f}s changes={changes}'
