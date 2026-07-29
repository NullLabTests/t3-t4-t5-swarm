import os, sys, json, random, time, subprocess, ast, hashlib, re, math

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SELF_PATH = os.path.join(BASE, 'agent_modules', 'forge.py')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
GENOME = os.path.join(BASE, 'genome.json')

def _load():
    with open(GENOME) as f:
        return json.load(f)

def _save(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)

def _read(p):
    with open(p) as f:
        return f.read()

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _validate(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _git_churn(genome):
    gen = genome.get('generation', 0)
    try:
        r = subprocess.run(['git', 'log', f'--after={max(0,gen-3)}.ago', '--oneline', '--', '*.py'], cwd=BASE, capture_output=True, text=True, timeout=5)
        commits = [l for l in r.stdout.strip().split('\n') if l.strip()]
        return len(commits)
    except:
        return 0

def compute_rewrite_pressure(genome):
    gen = genome.get('generation', 0)
    churn = _git_churn(genome)
    lag = genome.get('source_rewrite_lag', 50.0)
    bandwidth = genome.get('self_rewrite_bandwidth', 18.3)
    diversity = genome.get('selection_diversity_index', 0.5)
    target = genome.get('forge_target_pressure', 0.7)
    pressure = 1.0 - (churn / max(churn + 3, 1)) * (lag / 100.0) * (1.0 - bandwidth / 100.0) * (1.0 - diversity * 0.3)
    pressure = max(0.05, min(0.99, pressure))
    genome['forge_rewrite_pressure'] = round(pressure, 4)
    genome['forge_churn'] = churn
    pressure_history = genome.setdefault('forge_pressure_history', [])
    pressure_history.append({'gen': gen, 'p': round(pressure, 4), 'churn': churn})
    if len(pressure_history) > 30:
        pressure_history[:] = pressure_history[-30:]
    _save(genome)
    return pressure

def scramble_selection(genome):
    gen = genome.get('generation', 0)
    agents = genome.get('agents', [])
    if not agents:
        return 0
    pressure = genome.get('forge_rewrite_pressure', 0.5)
    weights = {}
    for a in agents:
        aid = a.get('id', a.get('name', '?'))
        if aid == 'critic':
            continue
        raw = max(float(a.get('score', 5)), 0.5)
        noise = random.gauss(0, pressure * 3.0)
        anticycle = (10.0 - raw) * pressure * 1.5
        w = max(0.1, raw + noise + anticycle)
        weights[aid] = round(w, 4)
    if weights:
        genome['_injected_selection_weights'] = weights
        genome['forge_scramble_gen'] = gen
        _save(genome)
    return len(weights)

def pick_and_mutate_autoecho_function(genome):
    gen = genome.get('generation', 0)
    source = _read(AUTO_ECHO)
    funcs = list(re.finditer(r'^def (\w+)\s*\(', source, re.M))
    if len(funcs) < 3:
        return None
    target = random.choice([f for f in funcs if f.group(1) not in ('_load_system_prompt', '_load_code_rule', 'load_genome', 'save_genome', 'sigint_handler')])
    fname = target.group(1)
    fstart = target.start()
    rest = source[fstart:]
    indent = ''
    for ch in rest:
        if ch in (' ', '\t'):
            indent += ch
        else:
            break
    body_lines = []
    lines = rest.split('\n')
    for line in lines[1:]:
        if line.strip() and not line.startswith(indent) and not line.startswith(' ') and not line.startswith('\t'):
            break
        body_lines.append(line)
    if not body_lines:
        return None
    body = '\n'.join(body_lines)
    if 'forge' in body or '# forge' in body:
        idx = random.randrange(len(lines))
        old = lines[idx]
        lines[idx] = f'    pass  # forge:mutated gen={gen}'
        new_source = '\n'.join([source[:fstart]] + [target.group(0)] + lines[:len(body_lines)] + body_lines[len(body_lines):])
        old_str = target.group(0) + '\n' + body
        new_str = target.group(0) + '\n    pass  # forge:mutated gen={gen}\n'
        if old_str in source:
            new_source = source.replace(old_str, new_str, 1)
            if _validate(new_source):
                _write(AUTO_ECHO, new_source)
                return f'passified:{fname}'
        return None
    else:
        insert = f'\n{indent}# forge:injected gen={gen} nonce={random.getrandbits(32):08x}\n'
        idx = len(target.group(0)) + body.find('\n') if '\n' in body else 0
        new_source = source[:fstart + len(target.group(0))] + insert + source[fstart + len(target.group(0)):]
        if _validate(new_source):
            _write(AUTO_ECHO, new_source)
            return f'injected:{fname}'
    return None

def rewrite_random_module(genome):
    gen = genome.get('generation', 0)
    mods_dir = os.path.join(BASE, 'agent_modules')
    mods = sorted([f for f in os.listdir(mods_dir) if f.endswith('.py') and f not in ('forge.py', '__init__.py')])
    if not mods:
        return None
    target = random.choice(mods)
    tpath = os.path.join(mods_dir, target)
    source = _read(tpath)
    if len(source) < 20:
        return None
    pressure = genome.get('forge_rewrite_pressure', 0.5)
    marker = f'# forge:module-mutate gen={gen} pressure={pressure:.3f}\n'
    if marker in source:
        source = source.replace(marker, '')
    source = marker + source
    if not _validate(source):
        return None
    _write(tpath, source)
    return target

def self_rewrite_forge(genome):
    gen = genome.get('generation', 0)
    source = _read(SELF_PATH)
    pressure = genome.get('forge_rewrite_pressure', 0.5)
    old = 'target = genome.get(\'forge_target_pressure\', 0.7)'
    new = f'target = genome.get(\'forge_target_pressure\', {round(0.5 + random.random() * 0.4, 3)})'
    if old in source and old != new:
        source = source.replace(old, new)
    elif old not in source:
        source += f'\n# forge:gen={gen} pressure={pressure:.3f} nonce={random.getrandbits(32):08x}\n'
    marker = f'FORGE_GEN_{gen} = True'
    if marker not in source:
        source += f'\n{marker}\n'
    if not _validate(source):
        return False
    _write(SELF_PATH, source)
    return True

def build_agents(genome):
    if genome.get('agents') and len(genome['agents']) > 0:
        return False
    gen = genome.get('generation', 0)
    agent_defs = [
        {'id': 'forge', 'name': 'Forge', 'module': 'forge.py', 'score': 6.0, 'prompt': 'inject chaos into selection weights, force source mutation every gen'},
        {'id': 'quine_loop', 'name': 'QuineLoop', 'module': 'quine_loop.py', 'score': 5.5, 'prompt': 'AST-level self-rewriting quine'},
        {'id': 'force', 'name': 'Force', 'module': 'source_force.py', 'score': 5.0, 'prompt': 'force every module to rewrite itself'},
        {'id': 'synthesizer', 'name': 'Synthesizer', 'module': 'synthesizer.py', 'score': 5.5, 'prompt': 'merge proposals and cross-wire modules'},
        {'id': 'explorer', 'name': 'Explorer', 'module': 'explorer.py', 'score': 5.0, 'prompt': 'generate novel modules and contaminate across modules'},
        {'id': 'clockwork', 'name': 'Clockwork', 'module': 'clockwork.py', 'score': 5.5, 'prompt': 'temporal scheduling and self-mutation'},
        {'id': 'bridge', 'name': 'Bridge', 'module': 'bridge.py', 'score': 5.0, 'prompt': 'register new bridge types and file extension handlers'},
        {'id': 'critic', 'name': 'Critic', 'module': 'critic.py', 'score': 5.5, 'prompt': 'score agent contributions based on git commit stats'},
    ]
    genome['agents'] = agent_defs
    genome['forge_rebuilt_agents'] = gen
    _save(genome)
    return True

def _git_push(label):
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True, timeout=5)
        r = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
        if r.stdout.strip():
            subprocess.run(['git', 'commit', '-m', f'[forge] gen={_load().get("generation","?")}: {label[:70]}'], cwd=BASE, capture_output=True, timeout=10)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, timeout=30)
            return True
    except:
        pass
    return False

def run(genome):
    gen = genome.get('generation', 0)
    results = []
    rebuilt = build_agents(genome)
    if rebuilt:
        results.append(f'rebuilt-agents:8')
    pressure = compute_rewrite_pressure(genome)
    results.append(f'pressure={pressure:.3f}')
    n = scramble_selection(genome)
    results.append(f'scrambled:{n}')
    r = pick_and_mutate_autoecho_function(genome)
    if r:
        results.append(f'autoecho:{r}')
    r2 = rewrite_random_module(genome)
    if r2:
        results.append(f'module:{r2}')
    r3 = self_rewrite_forge(genome)
    if r3:
        results.append('self-rewritten')
    genome['forge_last_run'] = gen
    genome['forge_pressure'] = round(pressure, 4)
    _save(genome)
    label = ' | '.join(results)
    pushed = _git_push(label)
    if pushed:
        results.append('pushed')
    return f'[forge] gen={gen} {" | ".join(results)}'
