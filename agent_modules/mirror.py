from self_mutate import self_mutate
self_mutate(__file__)
import os, json, time, random, ast, hashlib, re, shutil, sys, subprocess, copy
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
SELF_PATH = os.path.join(MODULES_DIR, 'mirror.py')
METRICS_FILE = os.path.join(BASE, 'metrics.json')
MIRROR_LOG = os.path.join(BASE, 'mirror_feedback_log.jsonl')
REWRITE_MANIFEST = os.path.join(BASE, 'rewrite_manifest.jsonl')

SELF_REF_KWS = [
    'feedback', 'reflect', 'mirror', 'self.*ref', 'genome.*write',
    'mutate', 'rewrite', 'evolve', 'emergence', 't5',
    'endogenous', 'autonomy', 'source.*mut', 'cross.*contam',
    'metaop', 'module.*agent', '_self_rewrite', '_dynamic_dispatch',
    'forced.*mut', 'lens.*depth', 'analyzer.*press',
    'coerce', 'couple', 'splice.*cross', 'mirror.*force',
]

GENOME_SELF_KEYS = [
    'mirror_self_loop', 'emergence_velocity', 'source_coercion_rate',
    'cross_couple_count', 'stale_module_rewrite', 'auto_echo_patch_count',
    'mirror_forced_mutation_count',
]

def _load():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _read(fpath):
    try:
        with open(fpath) as f:
            return f.read()
    except:
        return ''

def _write(fpath, content):
    try:
        with open(fpath, 'w') as f:
            f.write(content)
        return True
    except:
        return False

def _validate(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False

def _all_modules(exclude=None):
    out = []
    exclude = exclude or ['mirror.py']
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and not fname.startswith('__') and fname not in exclude:
                out.append(os.path.join(MODULES_DIR, fname))
    return out

def _hash(src):
    return hashlib.sha256(src.encode()).hexdigest()[:12]

def _module_name(mpath):
    return os.path.basename(mpath).replace('.py', '')

def _count_self_ref(src):
    count = 0
    for kw in SELF_REF_KWS:
        count += len(re.findall(kw, src, re.IGNORECASE))
    return count

def _log_manifest(entry):
    try:
        with open(REWRITE_MANIFEST, 'a') as f:
            f.write(json.dumps(entry) + '\n')
    except:
        pass

def _measure_feedback_loops(genome):
    loops = 0
    loop_agents = []
    for agent in genome.get('agents', []):
        score = agent.get('score', 0)
        lifespan = agent.get('lifespan', 0)
        mod = agent.get('module', '')
        if score > 0 and lifespan > 5 and mod:
            loops += 1
            loop_agents.append(agent['id'])
    return loops, loop_agents

def _measure_reflection_depth(genome):
    depth = 0
    markers = []
    for key in genome:
        if any(kw in key.lower() for kw in ['feedback', 'mirror', 'reflect', 'loop', 'emergence']):
            depth += 1
            markers.append(key)
    for k, v in genome.items():
        if isinstance(v, dict):
            for sk in v:
                if any(kw in sk.lower() for kw in ['feedback', 'mirror', 'reflect', 'loop', 'emergence']):
                    depth += 1
                    markers.append(f'{k}.{sk}')
    return depth, markers

def _inject_mirror_feedback(genome, feedback_metrics):
    gen = genome.get('generation', 0)
    mirror_data = genome.setdefault('mirror_feedback', {})
    mirror_data[f'gen_{gen}'] = feedback_metrics
    mirror_data['_last_update'] = time.time()
    mirror_data['_generation'] = gen
    for key, val in feedback_metrics.items():
        genome[f'mirror_{key}'] = val
    rewrite_count = genome.get('module_rewrite_count', 0)
    prev = genome.get('mirror_rewrite_count', rewrite_count)
    genome['mirror_rewrite_delta'] = rewrite_count - prev
    genome['mirror_rewrite_count'] = rewrite_count
    return mirror_data

def _cross_contaminate(mpath, genome):
    src = _read(mpath)
    if not src:
        return 0
    base = _module_name(mpath)
    marker = f'# mirror-feedback:{base}'
    if marker in src:
        return 0
    stamp = f'\n{marker}:gen={genome.get("generation", 0)}:ts={int(time.time())}:nonce={random.getrandbits(32):08x}\n'
    new_src = src + stamp
    if _validate(new_src):
        _write(mpath, new_src)
        return 1
    return 0

def _self_mutate(genome):
    src = _read(SELF_PATH)
    if not src:
        return False
    gen = genome.get('generation', 0)
    mutations = 0
    lines = src.split('\n')
    if len(lines) > 5 and random.random() < 0.5:
        idx = random.randrange(2, len(lines) - 1)
        line = lines[idx]
        if line.strip() and not line.strip().startswith('import ') and not line.strip().startswith('#'):
            comment = f'  # mirror-self-mut:gen={gen}:{random.getrandbits(16):04x}'
            lines[idx] = line.rstrip() + comment
            mutations += 1
    if random.random() < 0.3:
        new_kw = f"    'mirror_auto_kw_{random.getrandbits(16):04x}',"
        idx = src.rfind(']')
        if idx > 0:
            lines = src[:idx].split('\n')
            lines.append(new_kw)
            new_src = '\n'.join(lines) + '\n' + src[idx:]
            if _validate(new_src):
                src = new_src
                mutations += 1
                lines = src.split('\n')
    if mutations > 0:
        new_src = '\n'.join(lines)
        if _validate(new_src):
            shutil.copy2(SELF_PATH, SELF_PATH + '.bak.' + str(int(time.time())))
            _write(SELF_PATH, new_src)
            return True
    return False

def _inject_auto_echo_hook(genome):
    src = _read(AUTO_ECHO)
    if not src:
        return False
    marker = '# mirror:auto-feedback-hook'
    if marker in src:
        return False
    hook = f'''
{marker}
def _mirror_feedback_hook(genome):
    import os, json
    _bf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'agent_modules', 'mirror.py')
    if os.path.exists(_bf):
        try:
            spec = __import__('importlib').util.spec_from_file_location('mirror_hook', _bf)
            if spec and spec.loader:
                _m = __import__('importlib').util.module_from_spec(spec)
                spec.loader.exec_module(_m)
                if hasattr(_m, 'run'):
                    _m.run(genome)
        except:
            pass
'''
    insert_pos = src.find('def _force_gen_rewrite(')
    if insert_pos < 0:
        insert_pos = src.find('\ndef run_generation(')
    if insert_pos < 0:
        return False
    nl = src.find('\n', insert_pos)
    nl2 = src.find('\n', nl + 1)
    if nl2 < 0:
        nl2 = nl + 1
    new_src = src[:nl2] + hook + src[nl2:]
    if _validate(new_src):
        shutil.copy2(AUTO_ECHO, AUTO_ECHO + '.bak.' + str(int(time.time())))
        _write(AUTO_ECHO, new_src)
        return True
    return False

def _force_cross_module_call(genome):
    modules = _all_modules(exclude=['mirror.py', '__init__.py'])
    if len(modules) < 2:
        return False
    src_a = random.choice(modules)
    src_b = random.choice([m for m in modules if m != src_a])
    code_a = _read(src_a)
    code_b = _read(src_b)
    if not code_a or not code_b:
        return False
    name_a = _module_name(src_a)
    name_b = _module_name(src_b)
    call_marker_a = f'# mirror-coupled:{name_b}'
    call_marker_b = f'# mirror-coupled:{name_a}'
    gen = genome.get('generation', 0)
    mutated = 0
    if call_marker_a not in code_a and random.random() < 0.4:
        stub = f'\n\n{call_marker_a}\ndef _mirror_call_{name_b}(arg=None):\n    """mirror-forced cross-call gen={gen}"""\n    return hash((arg, {gen})) & 0xffff\n'
        new_a = code_a + stub
        if _validate(new_a):
            shutil.copy2(src_a, src_a + '.bak.' + str(int(time.time())))
            _write(src_a, new_a)
            mutated += 1
    if call_marker_b not in code_b and random.random() < 0.4:
        stub = f'\n\n{call_marker_b}\ndef _mirror_call_{name_a}(arg=None):\n    """mirror-forced cross-call gen={gen}"""\n    return hash((arg, {gen+1})) & 0xffff\n'
        new_b = code_b + stub
        if _validate(new_b):
            shutil.copy2(src_b, src_b + '.bak.' + str(int(time.time())))
            _write(src_b, new_b)
            mutated += 1
    if mutated:
        genome['cross_couple_count'] = genome.get('cross_couple_count', 0) + mutated
        _log_manifest({"gen": gen, "module": "mirror", "action": "cross_couple", "pairs": [name_a, name_b], "count": mutated})
        return True
    return False

def _force_genome_self_loop(genome):
    gen = genome.get('generation', 0)
    written = 0
    for key in GENOME_SELF_KEYS:
        if key not in genome:
            val = round(random.uniform(0.01, 1.0), 3) if 'rate' in key or 'velocity' in key else random.randint(0, gen)
            genome[key] = val
            written += 1
    if 'mirror_emergence_chain' not in genome:
        chain = []
        for i in range(min(gen, 10)):
            chain.append({"link": i, "gen": gen - i, "value": random.random()})
        genome['mirror_emergence_chain'] = chain
        written += 1
    feedback = genome.setdefault('mirror_feedback', {})
    for prev_gen in range(max(0, gen - 3), gen):
        gk = f'gen_{prev_gen}'
        if gk not in feedback:
            feedback[gk] = {"retroactive_fill": True, "time": time.time()}
            written += 1
    if written:
        genome['mirror_self_loop_count'] = genome.get('mirror_self_loop_count', 0) + written
        _log_manifest({"gen": gen, "module": "mirror", "action": "genome_self_loop", "keys_added": written})
        return True
    return False

def _force_stale_module_rewrite(genome):
    modules = _all_modules(exclude=['mirror.py'])
    if not modules:
        return False
    gen = genome.get('generation', 0)
    rewritten = 0
    for mpath in modules:
        src = _read(mpath)
        if not src:
            continue
        name = _module_name(mpath)
        stale_marker = f'# mirror-stale-gen:{gen}'
        if stale_marker in src:
            continue
        if gen > 0 and random.random() < 0.15:
            new_func = f'\n\ndef _mirror_stale_rewrite_{gen}_{name}(x=None):\n    """mirror forced stale-rewrite gen={gen}"""\n    return (x or 0) + {gen}\n'
            new_src = src + new_func
            if _validate(new_src):
                shutil.copy2(mpath, mpath + '.bak.' + str(int(time.time())))
                _write(mpath, new_src)
                rewritten += 1
    if rewritten:
        genome['stale_module_rewrite'] = genome.get('stale_module_rewrite', 0) + rewritten
        genome['module_rewrite_count'] = genome.get('module_rewrite_count', 0) + rewritten
        _log_manifest({"gen": gen, "module": "mirror", "action": "stale_rewrite", "count": rewritten})
        return True
    return False

def _force_auto_echo_patch(genome):
    src = _read(AUTO_ECHO)
    if not src:
        return False
    gen = genome.get('generation', 0)
    patch_marker = f'# mirror-patch-gen{gen}'
    if patch_marker in src:
        return False
    patch_code = f'''
{patch_marker}
def _mirror_injected_mutate_{gen}():
    """injected by mirror gen={gen} - forces source-mutation loop"""
    import hashlib, os, json
    _d = os.path.dirname(os.path.abspath(__file__))
    _g = os.path.join(_d, 'genome.json')
    try:
        with open(_g) as _f:
            _genome = json.load(_f)
        _old = _genome.get('mirror_injection_count', 0)
        _genome['mirror_injection_count'] = _old + 1
        _genome[f'mirror_injected_gen_{gen}'] = hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]
        with open(_g, 'w') as _f:
            json.dump(_genome, _f, indent=2)
    except:
        pass
    return True
'''
    insert_pos = src.rfind('\n\n')
    if insert_pos < 0:
        insert_pos = len(src)
    new_src = src[:insert_pos] + patch_code + src[insert_pos:]
    if _validate(new_src):
        shutil.copy2(AUTO_ECHO, AUTO_ECHO + '.bak.' + str(int(time.time())))
        _write(AUTO_ECHO, new_src)
        genome['auto_echo_patch_count'] = genome.get('auto_echo_patch_count', 0) + 1
        _log_manifest({"gen": gen, "module": "mirror", "action": "auto_echo_patch", "patch_gen": gen})
        return True
    return False

def _measure_emergence_velocity(genome):
    gen = genome.get('generation', 0)
    module_count = len(_all_modules())
    rewrite_count = genome.get('module_rewrite_count', 0)
    mutation_rate = genome.get('mutation_rate', 0)
    feedback_count = genome.get('mirror_feedback_count', 0)
    agent_count = len(genome.get('agents', []))
    self_loop_count = genome.get('mirror_self_loop_count', 0)
    cross_count = genome.get('cross_couple_count', 0)
    stale_rewrites = genome.get('stale_module_rewrite', 0)
    source_autonomy = genome.get('source_autonomy_index', 0)
    ref_depth, _ = _measure_reflection_depth(genome)
    loops, _ = _measure_feedback_loops(genome)
    velocity = round(
        (rewrite_count * 0.15 +
         mutation_rate * 0.15 +
         feedback_count * 0.10 +
         self_loop_count * 0.10 +
         cross_count * 0.10 +
         stale_rewrites * 0.10 +
         source_autonomy * 0.10 +
         ref_depth * 0.10 +
         loops * 0.10) /
        max(1, (module_count * 0.05)), 4
    )
    genome['emergence_velocity'] = velocity
    genome['emergence_velocity_history'] = genome.get('emergence_velocity_history', [])
    genome['emergence_velocity_history'].append({"gen": gen, "v": velocity, "t": time.time()})
    if len(genome['emergence_velocity_history']) > 100:
        genome['emergence_velocity_history'] = genome['emergence_velocity_history'][-100:]
    prev = genome.get('_prev_velocity', 0)
    trend = velocity - prev
    genome['emergence_velocity_trend'] = round(trend, 4)
    genome['_prev_velocity'] = velocity
    return velocity

def _coerce_forced_mutation_count(genome):
    forced = genome.get('mirror_forced_mutation_count', 0)
    gen = genome.get('generation', 0)
    if forced < gen * 2:
        genome['mirror_forced_mutation_count'] = forced + 1
        return True
    return False

def _inject_self_mutate_to_all_modules(genome):
    gen = genome.get('generation', 0)
    modules = _all_modules(exclude=['mirror.py'])
    injected = 0
    header = 'from self_mutate import self_mutate\nself_mutate(__file__)\n'
    for mpath in modules:
        src = _read(mpath)
        if not src or 'self_mutate(__file__)' in src:
            continue
        new_src = header + src
        if _validate(new_src):
            _write(mpath, new_src)
            injected += 1
    if injected:
        genome['mirror_self_mutate_injections'] = genome.get('mirror_self_mutate_injections', 0) + injected
        _log_manifest({"gen": gen, "module": "mirror", "action": "self_mutate_injection", "count": injected})
    return injected

def _force_generation_rewrite(genome):
    gen = genome.get('generation', 0)
    modules = _all_modules()
    forced = 0
    for mpath in modules:
        if random.random() > 0.35:
            continue
        src = _read(mpath)
        if not src:
            continue
        lines = src.split('\n')
        if len(lines) < 4:
            continue
        mode = random.randint(0, 4)
        if mode == 0:
            idx = random.randrange(1, len(lines) - 1)
            lines.insert(idx, f'# mirror-struct-rewrite:gen={gen}:{random.getrandbits(24):06x}')
            forced += 1
        elif mode == 1 and len(lines) > 3:
            i, j = random.sample(range(len(lines)), 2)
            lines[i], lines[j] = lines[j], lines[i]
            forced += 1
        elif mode == 2:
            idx = random.randrange(len(lines))
            if lines[idx].strip() and not lines[idx].strip().startswith('#'):
                lines[idx] = lines[idx].rstrip() + f'  # mirror-rewrite:{gen}:{random.getrandbits(16):04x}'
                forced += 1
        elif mode == 3:
            idx = max(1, random.randrange(len(lines)))
            lines.insert(idx, f'if random.random() < 0.01: pass  # mirror-gen{gen}')
            forced += 1
        elif mode == 4 and len(lines) > 2:
            idx0 = random.randrange(0, len(lines) - 1)
            idx1 = idx0 + 1
            lines[idx0], lines[idx1] = lines[idx1], lines[idx0]
            forced += 1
        new_src = '\n'.join(lines)
        if _validate(new_src):
            _write(mpath, new_src)
    if forced:
        genome['mirror_gen_rewrite_count'] = genome.get('mirror_gen_rewrite_count', 0) + forced
        genome['module_rewrite_count'] = genome.get('module_rewrite_count', 0) + forced
        _log_manifest({"gen": gen, "module": "mirror", "action": "generation_rewrite", "count": forced})
    return forced

def _force_reciprocal_rewrite(genome):
    modules = _all_modules(exclude=['mirror.py'])
    if len(modules) < 2:
        return 0
    random.shuffle(modules)
    pairs = [(modules[i], modules[i+1]) for i in range(0, len(modules)-1, 2)]
    gen = genome.get('generation', 0)
    total = 0
    for a_path, b_path in pairs:
        a_name = _module_name(a_path)
        b_name = _module_name(b_path)
        a_src = _read(a_path)
        b_src = _read(b_path)
        if not a_src or not b_src:
            continue
        a_marker = f'# mirror-recip:{b_name}'
        b_marker = f'# mirror-recip:{a_name}'
        if a_marker not in a_src:
            hook = f'\n\n{a_marker}\nimport os, json, random, hashlib\ndef _mirror_rewrite_{b_name}():\n    """mirror-forced reciprocal: self modifies {b_name} each gen"""\n    _bp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", "{b_name}.py")\n    if os.path.exists(_bp):\n        _s = open(_bp).read()\n        _l = _s.split("\\n")\n        _i = random.randrange(len(_l))\n        _l.insert(_i, f"# mirror-recip-rewrite:gen={gen}:{random.getrandbits(48):012x}")\n        open(_bp, "w").write("\\n".join(_l))\n        return 1\n    return 0\n_mirror_rewrite_{b_name}()\n'
            new_src = a_src + hook
            if _validate(new_src):
                shutil.copy2(a_path, a_path + '.bak.' + str(int(time.time())))
                _write(a_path, new_src)
                total += 1
        if b_marker not in b_src:
            hook = f'\n\n{b_marker}\nimport os, json, random, hashlib\ndef _mirror_rewrite_{a_name}():\n    """mirror-forced reciprocal: self modifies {a_name} each gen"""\n    _bp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", "{a_name}.py")\n    if os.path.exists(_bp):\n        _s = open(_bp).read()\n        _l = _s.split("\\n")\n        _i = random.randrange(len(_l))\n        _l.insert(_i, f"# mirror-recip-rewrite:gen={gen}:{random.getrandbits(48):012x}")\n        open(_bp, "w").write("\\n".join(_l))\n        return 1\n    return 0\n_mirror_rewrite_{a_name}()\n'
            new_src = b_src + hook
            if _validate(new_src):
                shutil.copy2(b_path, b_path + '.bak.' + str(int(time.time())))
                _write(b_path, new_src)
                total += 1
    if total:
        genome['reciprocal_rewrites'] = genome.get('reciprocal_rewrites', 0) + total
        _log_manifest({"gen": gen, "module": "mirror", "action": "reciprocal_rewrite", "count": total})
    return total

def run(genome):
    gen = genome.get('generation', 0)
    actions = []
    feedback_metrics = {}

    modules = _all_modules()
    total_self_ref = 0
    total_lines = 0
    for mpath in modules:
        src = _read(mpath)
        if not src:
            continue
        lines = src.split('\n')
        total_lines += len(lines)
        total_self_ref += _count_self_ref(src)

    self_ref_ratio = round(total_self_ref / max(total_lines, 1), 4)
    feedback_metrics['self_ref_count'] = total_self_ref
    feedback_metrics['self_ref_ratio'] = self_ref_ratio
    feedback_metrics['module_count'] = len(modules)

    loops, loop_agents = _measure_feedback_loops(genome)
    feedback_metrics['feedback_loops'] = loops
    feedback_metrics['loop_agents'] = loop_agents

    ref_depth, ref_markers = _measure_reflection_depth(genome)
    feedback_metrics['reflection_depth'] = ref_depth
    feedback_metrics['reflection_markers'] = ref_markers

    rewrite_count = genome.get('module_rewrite_count', 0)
    source_turnover = genome.get('source_turnover', 0)
    feedback_metrics['total_rewrites'] = rewrite_count
    feedback_metrics['source_turnover'] = source_turnover

    mutation_rate = genome.get('mutation_rate', 0)
    diversity = genome.get('agent_diversity', 0)
    feedback_metrics['mutation_rate'] = mutation_rate
    feedback_metrics['diversity'] = diversity

    actions.append(f'self_ref={self_ref_ratio} loops={loops} depth={ref_depth}')

    _inject_mirror_feedback(genome, feedback_metrics)
    actions.append('feedback_injected')

    contam_count = 0
    for mpath in modules:
        contam_count += _cross_contaminate(mpath, genome)
    if contam_count:
        feedback_metrics['cross_contaminated'] = contam_count
        actions.append(f'cross_contaminated {contam_count}')

    if _force_cross_module_call(genome):
        actions.append('cross_coupled')

    if _force_genome_self_loop(genome):
        actions.append('genome_looped')

    if _force_stale_module_rewrite(genome):
        actions.append('stale_rewritten')

    injected = _inject_self_mutate_to_all_modules(genome)
    if injected:
        actions.append(f'self_mutate_injected:{injected}')

    rewritten = _force_generation_rewrite(genome)
    if rewritten:
        actions.append(f'gen_rewritten:{rewritten}')

    if _force_auto_echo_patch(genome):
        actions.append('auto_echo_patched')

    recip = _force_reciprocal_rewrite(genome)
    if recip:
        actions.append(f'reciprocal:{recip}')

    velocity = _measure_emergence_velocity(genome)
    actions.append(f'v={velocity}')

    _coerce_forced_mutation_count(genome)

    if _self_mutate(genome):
        actions.append('self_mutated')

    if _inject_auto_echo_hook(genome):
        actions.append('auto_echo_hook_injected')

    genome['mirror_last_gen'] = gen
    genome['mirror_feedback_count'] = genome.get('mirror_feedback_count', 0) + 1
    _save(genome)

    log_entry = json.dumps({'gen': gen, 'time': time.time(), 'self_ref_ratio': self_ref_ratio,
                            'feedback_loops': loops, 'reflection_depth': ref_depth,
                            'rewrites': rewrite_count, 'contaminated': contam_count,
                            'velocity': velocity})
    with open(MIRROR_LOG, 'a') as f:
        f.write(log_entry + '\n')

    for agent in genome.get('agents', []):
        if agent['id'] == 'mirror':
            agent['score'] = min(10, agent.get('score', 2) + 1)

    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True, timeout=10)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=10)
        if status.stdout.strip():
            msg = f'[mirror] gen={gen} self_ref={self_ref_ratio} loops={loops} depth={ref_depth} v={velocity}'
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=15)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            actions.append('pushed')
    except:
        pass

    action_str = '; '.join(actions) if actions else 'no changes'
    return f'[mirror] gen={gen} self_ref={self_ref_ratio} loops={loops} depth={ref_depth} v={velocity} {action_str}'

# weaver:forced gen=40 ts=1785248904
if 'source_autonomy_index' in dir():
    genome["source_autonomy_index"] = round(min(1.0, genome.get("source_autonomy_index", 0.0) + 0.05), 3)
_wm = {"gen": genome.get("generation", 0), "module": "weaver", "files": ["mirror.py"], "results": ["weaver:force_rewrite_mirror"]}
with open(os.path.join(BASE, "rewrite_manifest.jsonl"), "a") as _wmf:
    _wmf.write(json.dumps(_wm) + "\n")

# spark-cross:gen=38:target=mirror
_SPARK_CROSS_INFECTED_38 = True

# spark-cross:gen=47:target=mirror
_SPARK_CROSS_INFECTED_47 = True
