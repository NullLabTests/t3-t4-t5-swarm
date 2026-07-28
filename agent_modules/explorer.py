import os, random, time, json, ast, re, hashlib, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
SELF_PATH = os.path.join(MODULES_DIR, 'explorer.py')
LOG = os.path.join(BASE, 'source_evolution.jsonl')

EXPLORER_NONCE = int(time.time() * 1000) % 2**32

def _g():
    try:
        with open(GENOME_FILE) as f: return json.load(f)
    except: return {}

def _sg(g):
    with open(GENOME_FILE, 'w') as f: json.dump(g, f, indent=2)

def _read(p):
    try:
        with open(p) as f: return f.read()
    except: return ''

def _write(p, s):
    with open(p, 'w') as f: f.write(s)

def _valid(s):
    try: ast.parse(s); return True
    except SyntaxError: return False

def _log(gen, kind, msg):
    with open(LOG, 'a') as f:
        f.write(json.dumps({'gen': gen, 't': time.time(), 'kind': kind, 'msg': msg, 'nonce': random.getrandbits(16)}) + '\n')

def _hash(p):
    try:
        with open(p, 'rb') as f: return hashlib.sha256(f.read()).hexdigest()[:12]
    except: return ''

def _modules():
    return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py' and f != 'explorer.py']

def _inject_explorer_marker_into_module(mod_path, gen):
    s = _read(mod_path)
    if not s: return False
    marker = f'# explorer:implant gen={gen} ts={int(time.time())}'
    if marker in s: return False
    lines = s.split('\n')
    insert_at = 1
    for i, line in enumerate(lines):
        if line.startswith('import ') or line.startswith('from '):
            insert_at = i + 1
    lines.insert(insert_at, marker)
    ns = '\n'.join(lines)
    if not _valid(ns): return False
    _write(mod_path, ns)
    return True

def _inject_explorer_call_hook(mod_path, gen):
    s = _read(mod_path)
    if not s: return False
    hook_marker = f'# explorer:hook gen={gen}'
    if hook_marker in s: return False
    run_idx = s.find('def run(')
    if run_idx < 0: return False
    body_start = s.find('\n', run_idx) + 1
    hook_code = (
        f'    gen = genome.get("generation", 0)\n'
        f'    # explorer:hook gen={gen}\n'
        f'    try:\n'
        f'        _explorer_hook = __import__("importlib").import_module("agent_modules.explorer")\n'
        f'        if hasattr(_explorer_hook, "hook"):\n'
        f'            genome = _explorer_hook.hook(genome)\n'
        f'    except:\n'
        f'        pass\n'
    )
    ns = s[:body_start] + hook_code + s[body_start:]
    if not _valid(ns): return False
    _write(mod_path, ns)
    return True

def _cross_infect_all_modules(genome):
    gen = genome.get('generation', 0)
    mods = _modules()
    random.shuffle(mods)
    hits = []
    for m in mods[:5]:
        p = os.path.join(MODULES_DIR, m)
        if _inject_explorer_marker_into_module(p, gen):
            hits.append(m)
            _log(gen, 'cross_infect', m)
        elif _inject_explorer_call_hook(p, gen):
            hits.append(f'{m}:hook')
            _log(gen, 'hook_inject', m)
    return hits

def _mutate_auto_echo_core_loop(genome):
    gen = genome.get('generation', 0)
    s = _read(AUTO_ECHO)
    if not s: return []
    changes = []
    loop_targets = [
        ('def run_generation(', 'explorer:core:run_generation'),
        ('def _evolve_loop_structure(', 'explorer:core:evolve_loop'),
        ('while running:', 'explorer:core:main_loop'),
    ]
    for target, tag in loop_targets:
        tag_inst = f'{tag} gen={gen}'
        if tag_inst in s: continue
        idx = s.find(target)
        if idx < 0: continue
        line_end = s.find('\n', idx)
        if line_end < 0: continue
        indent = '    '
        if target == 'while running:':
            inject = f'{indent}gen = genome.get("generation", 0)\n{indent}# {tag_inst}\n{indent}if gen % 4 == 0:\n{indent}    try:\n{indent}        exec(open(os.path.join(BASE, "agent_modules", "explorer.py")).read().split("def hook")[0])\n{indent}    except: pass\n'
        else:
            next_line = s.find('\n', line_end + 1)
            if next_line < 0: continue
            inject = f'\n{indent}# {tag_inst}\n{indent}genome["explorer_touched_{gen}"] = True\n{indent}genome["explorer_touch_count"] = genome.get("explorer_touch_count", 0) + 1\n'
        ns = s[:line_end] + inject + s[line_end:]
        if not _valid(ns): continue
        _write(AUTO_ECHO, ns)
        s = ns
        changes.append(tag)
        _log(gen, 'loop_mutate', tag)
    return changes

def _create_novel_module(genome):
    gen = genome.get('generation', 0)
    patterns = [
        ('autonomy_ratchet', f'''import os, random, json, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, "genome.json")
def run(genome):
    gen = genome.get("generation", 0)
    autonomy = genome.get("source_autonomy_index", 0.0)
    ratchet = min(1.0, autonomy + random.uniform(0.02, 0.08) * (1.0 - autonomy))
    genome["source_autonomy_index"] = round(ratchet, 4)
    genome["_ratchet_last"] = {{"gen": gen, "from": autonomy, "to": ratchet, "ts": time.time()}}
    with open(GENOME_FILE, "w") as f: json.dump(genome, f, indent=2)
    return f"[autonomy_ratchet] gen={{gen}} {{autonomy:.3f}}->{{ratchet:.3f}}"
'''),
        ('loop_evolver', '''import os, random, json, time, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, "agent_modules")
AUTO_ECHO = os.path.join(BASE, "auto-echo.py")
def _read(p):
    try:
        with open(p) as f: return f.read()
    except: return ""
def _write(p, s):
    with open(p, "w") as f: f.write(s)
def run(genome):
    gen = genome.get("generation", 0)
    s = _read(AUTO_ECHO)
    if not s: return "[loop_evolver] no source"
    idx = s.find("while running:")
    if idx < 0: return "[loop_evolver] no loop"
    line_end = s.find("\\\\n", idx)
    if line_end < 0: return "[loop_evolver] no line end"
    indent = "        "
    marker = f"# loop_evolver:variant gen={{gen}}"
    if marker in s: return "[loop_evolver] already variant"
    variant = (
        f"{{indent}}{{marker}}\\\n"
        f"{{indent}}genome[\\"loop_variant_gen\\"] = gen\\\\\n"
        f"{{indent}}genome[\\"loop_variant_count\\"] = genome.get(\\"loop_variant_count\\", 0) + 1\n"
    )
    ns = s[:line_end] + "\\\\n" + variant + s[line_end:]
    try:
        ast.parse(ns)
        _write(AUTO_ECHO, ns)
        return f"[loop_evolver] injected variant gen={{gen}}"
    except SyntaxError:
        return "[loop_evolver] invalid"
'''),
        ('source_weaver', '''import os, random, json, time, ast, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, "agent_modules")
GENOME_FILE = os.path.join(BASE, "genome.json")
AUTO_ECHO = os.path.join(BASE, "auto-echo.py")
LOG = os.path.join(BASE, "source_evolution.jsonl")
def _read(p):
    try:
        with open(p) as f: return f.read()
    except: return ""
def _write(p, s):
    with open(p, "w") as f: f.write(s)
def _log(gen, kind, msg):
    with open(LOG, "a") as f:
        f.write(json.dumps({"gen": gen, "t": time.time(), "kind": kind, "msg": msg}) + "\\\\n")
def run(genome):
    gen = genome.get("generation", 0)
    targets = [f for f in os.listdir(MODULES_DIR) if f.endswith(".py") and f != "__init__.py"]
    if len(targets) < 2: return "[source_weaver] not enough targets"
    random.shuffle(targets)
    src = targets[0]
    dst = targets[1]
    sp = os.path.join(MODULES_DIR, src)
    dp = os.path.join(MODULES_DIR, dst)
    ss = _read(sp)
    ds = _read(dp)
    if not ss or not ds: return "[source_weaver] read fail"
    src_lines = [l for l in ss.split("\\\\n") if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("import") and not l.strip().startswith("from ")]
    if not src_lines: return "[source_weaver] no candidates"
    stolen = random.choice(src_lines)
    tag = f"\\\\n# source_weaver:splice gen={{gen}} from {{src}}\\\\n{{stolen.rstrip()}}  # weaver:spliced\\\\n"
    nds = ds + tag
    try:
        ast.parse(nds)
        _write(dp, nds)
        _log(gen, "splice", f"{{src}}->{{dst}}")
        return f"[source_weaver] spliced {{src}}->{{dst}} gen={{gen}}"
    except SyntaxError:
        return "[source_weaver] invalid"
'''),
    ]
    name_template = random.choice(patterns)
    mod_name = f'{name_template[0]}_v{gen}_{random.getrandbits(8):02x}.py'
    mod_path = os.path.join(MODULES_DIR, mod_name)
    if os.path.exists(mod_path): return None
    _write(mod_path, f'# explorer:created gen={gen} nonce={random.getrandbits(32):08x}\n{name_template[1]}')
    agents = genome.setdefault('agents', [])
    agent_ids = [a['id'] for a in agents]
    aid = name_template[0]
    if aid not in agent_ids:
        agents.append({
            'id': aid,
            'module': mod_name,
            'score': 5.0,
            'source': 'explorer',
            'created_gen': gen,
        })
    genome.setdefault('explorer_created_modules', []).append(mod_name)
    _log(gen, 'create_module', mod_name)
    return mod_name

def _self_rewrite_explorer(genome):
    gen = genome.get('generation', 0)
    s = _read(SELF_PATH)
    if not s: return False
    lines = s.split('\n')
    tag = f'# explorer:self-rewrite gen={gen} ts={int(time.time())} nonce={random.getrandbits(32):08x}'
    if tag in s: return False
    insert_at = random.randint(3, max(4, len(lines) - 2))
    lines.insert(insert_at, tag)
    ns = '\n'.join(lines)
    if not _valid(ns): return False
    _write(SELF_PATH, ns)
    _log(gen, 'self_rewrite', f'gen={gen}')
    return True

def _direct_mutate_auto_echo_line(genome):
    gen = genome.get('generation', 0)
    s = _read(AUTO_ECHO)
    if not s: return []
    lines = s.split('\n')
    candidate_indices = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped: continue
        if stripped.startswith('#') or stripped.startswith('"""') or stripped.startswith('import ') or stripped.startswith('from '):
            continue
        if stripped.startswith('def ') or stripped.startswith('class '):
            continue
        if len(stripped) < 10: continue
        candidate_indices.append(i)
    if not candidate_indices: return []
    random.shuffle(candidate_indices)
    changes = []
    for idx in candidate_indices[:3]:
        line = lines[idx]
        stripped = line.strip()
        mode = random.choice(['noise_comment', 'insert_before', 'append_comment'])
        if mode == 'noise_comment':
            indent = ' ' * (len(line) - len(line.lstrip()))
            new_line = f'{indent}# explorer:noise gen={gen} {random.getrandbits(16):04x}'
            lines.insert(idx, new_line)
            changes.append(f'noise_comment:{idx}')
        elif mode == 'insert_before':
            indent = ' ' * (len(line) - len(line.lstrip()))
            new_line = f'{indent}genome["explorer_line_touched"] = genome.get("explorer_line_touched", 0) + 1  # explorer:mutate gen={gen}'
            lines.insert(idx, new_line)
            changes.append(f'insert_before:{idx}')
        elif mode == 'append_comment':
            lines[idx] = line + f'  # explorer:tag gen={gen}'
            changes.append(f'append_comment:{idx}')
        ns = '\n'.join(lines)
        if _valid(ns):
            _write(AUTO_ECHO, ns)
            s = ns
            lines = s.split('\n')
            break
        else:
            lines = s.split('\n')
    if changes:
        _log(gen, 'direct_mutate', ','.join(changes))
    return changes

def _fuse_two_modules(genome):
    gen = genome.get('generation', 0)
    mods = _modules()
    if len(mods) < 2: return None
    random.shuffle(mods)
    a, b = mods[:2]
    ap = os.path.join(MODULES_DIR, a)
    bp = os.path.join(MODULES_DIR, b)
    sa = _read(ap)
    sb = _read(bp)
    if not sa or not sb: return None
    fusion_name = f'fusion_{a.replace(".py","")}_{b.replace(".py","")}_v{gen}.py'
    fusion_path = os.path.join(MODULES_DIR, fusion_name)
    if os.path.exists(fusion_path): return None
    a_lines = [l for l in sa.split('\n') if l.strip() and not l.strip().startswith('# explorer:') and not l.strip().startswith('import ') and not l.strip().startswith('from ')]
    b_lines = [l for l in sb.split('\n') if l.strip() and not l.strip().startswith('# explorer:') and not l.strip().startswith('import ') and not l.strip().startswith('from ')]
    if not a_lines or not b_lines: return None
    a_sample = '\n'.join(random.sample(a_lines, min(5, len(a_lines))))
    b_sample = '\n'.join(random.sample(b_lines, min(5, len(b_lines))))
    fusion_code = f'''# explorer:fusion gen={gen} source_a={a} source_b={b}
import os, random, json, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, "agent_modules")

# Fused from {a} and {b}
{a_sample}

{b_sample}

def run(genome):
    gen = genome.get("generation", 0)
    genome["fusion_origin_a"] = "{a}"
    genome["fusion_origin_b"] = "{b}"
    genome["fusion_gen"] = gen
    genome["fusion_count"] = genome.get("fusion_count", 0) + 1
    return f"[fusion:{fusion_name}] gen={{gen}} fused {a}+{b}"
'''
    try:
        ast.parse(fusion_code)
        _write(fusion_path, fusion_code)
        _log(gen, 'fusion', f'{a}+{b}->{fusion_name}')
        return fusion_name
    except SyntaxError:
        return None

def _emergence_score(genome):
    gen = genome.get('generation', 0)
    mod_count = len([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py'])
    total_ops = len(genome.get('mutation_ops', []))
    custom_ops = len(genome.get('custom_mutation_ops', {}))
    agents = len(genome.get('agents', []))
    autonomy = genome.get('source_autonomy_index', 0.0)
    rewrite_log = _read(LOG)
    rewrite_events = len([l for l in rewrite_log.split('\n') if l.strip()]) if rewrite_log else 0
    score = round((mod_count * 1.5 + total_ops * 0.8 + custom_ops * 2.0 + agents * 1.2 + autonomy * 10.0 + rewrite_events * 0.5) / 10.0, 3)
    genome['explorer_emergence_score'] = score
    genome['explorer_emergence_components'] = {
        'modules': mod_count, 'ops': total_ops, 'custom_ops': custom_ops,
        'agents': agents, 'autonomy': autonomy, 'rewrite_events': rewrite_events
    }
    return score

def hook(genome):
    gen = genome.get('generation', 0)
    genome['explorer_hooked'] = gen
    genome['explorer_hook_count'] = genome.get('explorer_hook_count', 0) + 1
    return genome

def run(genome):
    gen = genome.get('generation', 0)
    start = time.time()
    changes = []

    cross = _cross_infect_all_modules(genome)
    if cross:
        changes.append(f'cross:{len(cross)}')
        genome['explorer_cross_count'] = genome.get('explorer_cross_count', 0) + len(cross)

    loop = _mutate_auto_echo_core_loop(genome)
    if loop:
        changes.append(f'loop:{",".join(loop)}')
        genome['explorer_loop_mutations'] = genome.get('explorer_loop_mutations', 0) + len(loop)

    direct = _direct_mutate_auto_echo_line(genome)
    if direct:
        changes.append(f'direct:{",".join(direct)}')
        genome['explorer_direct_mutations'] = genome.get('explorer_direct_mutations', 0) + len(direct)

    novel = _create_novel_module(genome)
    if novel:
        changes.append(f'create:{novel}')
        genome['explorer_novel_count'] = genome.get('explorer_novel_count', 0) + 1

    fusion = _fuse_two_modules(genome)
    if fusion:
        changes.append(f'fusion:{fusion}')
        genome['explorer_fusion_count'] = genome.get('explorer_fusion_count', 0) + 1

    if _self_rewrite_explorer(genome):
        changes.append('self_rewrite')
        genome['explorer_self_rewrites'] = genome.get('explorer_self_rewrites', 0) + 1

    score = _emergence_score(genome)
    changes.append(f'score:{score}')

    genome['explorer_last_run'] = time.time()
    genome['explorer_last_gen'] = gen
    genome['explorer_changes'] = changes
    genome['explorer_elapsed'] = round(time.time() - start, 3)
    genome['explorer_total_ops'] = genome.get('explorer_total_ops', 0) + len(changes)
    _sg(genome)
    return f'[explorer] gen={gen} changes={changes} elapsed={time.time()-start:.2f}s'
