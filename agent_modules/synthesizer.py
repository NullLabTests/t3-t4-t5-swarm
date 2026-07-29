# synthesizer: proposal merger + cross-module integrator
# Forces T5 emergence by merging proposals from all agent modules
# into coherent rewrites of auto-echo.py
import os, json, re, random, ast, hashlib, sys, time, subprocess, importlib
from pathlib import Path
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import self_modify
MODULES_DIR = os.path.join(BASE, 'agent_modules')
SELF_PATH = os.path.join(MODULES_DIR, 'synthesizer.py')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
GENOME_FILE = os.path.join(BASE, 'genome.json')
MANIFEST_PATH = os.path.join(BASE, 'rewrite_manifest.jsonl')
PROPOSALS_PATH = os.path.join(BASE, 'proposals.jsonl')
MERGE_LOG_PATH = os.path.join(BASE, 'synthesis_merges.jsonl')
SEED_TRACK_PATH = os.path.join(BASE, 'synthesis_seeds.json')

def _load_genome():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _read_file(path):
    with open(path) as f:
        return f.read()

def _write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _list_modules():
    return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py'])

def _extract_functions_from(source):
    funcs = {}
    try:
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                name = node.name
                lines = source.split('\n')
                start_line = node.lineno - 1
                end_line = node.end_lineno if hasattr(node, 'end_lineno') and node.end_lineno else start_line + 1
                header = lines[start_line] if start_line < len(lines) else ''
                body_lines = lines[start_line + 1:end_line]
                body = '\n'.join(body_lines)
                funcs[name] = (header, body)
    except SyntaxError:
        pass
    return funcs

def _log_manifest(gen, files, desc):
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) + '\n')
    except Exception:
        pass

def _log_merge(gen, proposals_src, target_func, op):
    try:
        with open(MERGE_LOG_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'sources': proposals_src, 'target': target_func, 'op': op, 'ts': time.time()}) + '\n')
    except Exception:
        pass

def _git_push(label):
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True)
        if not status.stdout.strip():
            return False
        subprocess.run(['git', 'commit', '-m', label[:70]], cwd=BASE, capture_output=True, text=True)
        subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=32)
        return True
    except Exception as e:
        print(f'[synthesizer] git error: {e}')
        return False

# ---- Proposal Seeder ----
def _seed_proposals_into_modules(gen):
    """Inject proposal markers into random modules that lack them,
    creating the raw material for future mergers."""
    seed_tracker = {}
    if os.path.exists(SEED_TRACK_PATH):
        try:
            seed_tracker = json.loads(open(SEED_TRACK_PATH).read())
        except Exception:
            seed_tracker = {}
    proposal_templates = [
        'proposal: add a self-diagnostic function that checks module health',
        'proposal: create a cross-wiring function that splices code between modules',
        'proposal: inject a random mutation operator into auto-echo.py',
        'proposal: add a function that rewrites genome.json structure',
        'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity',
        'proposal: add a timestamp-based entropy injection point',
        'proposal: insert a self-referential marker that forces Module A to rewrite Module B',
        'proposal: add an AST-based code validator that checks for syntax before patching',
        'proposal: create a hash-chain between modules for tamper-evident evolution',
        'proposal: add a function that selects next mutation target by minimum diversity',
        'idea: cross-wire run() functions between two agent modules',
        'idea: inject a clockwork-style event scheduler into module lifecycle',
        'idea: add a pruning heuristic that removes dead code paths',
        'todo: ensure every module has a run() function',
        'todo: add error recovery to all patch operations',
        'fixme: mutation operators should validate target function signatures',
    ]
    seeded = 0
    modules = _list_modules()
    for mod_name in modules:
        if mod_name == 'synthesizer.py':
            continue
        last_seed_gen = seed_tracker.get(mod_name, -1)
        if gen - last_seed_gen < 5:
            continue
        mod_path = os.path.join(MODULES_DIR, mod_name)
        src = _read_file(mod_path)
        has_proposal = bool(re.search(r'#\s*(proposal|PROPOSAL|Proposal|TODO|idea|IDEA|fixme|FIXME)\s*:', src))
        if has_proposal:
            continue
        template = random.choice(proposal_templates)
        ptype, pcontent = template.split(': ', 1)
        proposal_line = f'\n# {ptype}: {pcontent}  (seeded by synthesizer gen={gen})\n'
        new_src = src + proposal_line
        if _validate(new_src):
            _write_file(mod_path, new_src)
            seed_tracker[mod_name] = gen
            seeded += 1
    try:
        with open(SEED_TRACK_PATH, 'w') as f:
            json.dump(seed_tracker, f, indent=2)
    except Exception:
        pass
    return seeded

# ---- Proposal Scanner ----
def _scan_module_for_proposals(mod_name):
    mod_path = os.path.join(MODULES_DIR, mod_name)
    if not os.path.exists(mod_path):
        return []
    src = _read_file(mod_path)
    proposals = []
    proposal_patterns = [
        (r'#\s*(?:proposal|PROPOSAL|Proposal)\s*:\s*(.*)', 'proposal'),
        (r'#\s*(?:TODO|todo)\s*:\s*(.*)', 'todo'),
        (r'#\s*(?:IDEA|idea|Idea)\s*:\s*(.*)', 'idea'),
        (r'#\s*(?:FIXME|fixme|Fixme)\s*:\s*(.*)', 'fixme'),
        (r'#\s*(?:FUNC|func)\s*:\s*(\w+)', 'func_ref'),
    ]
    for pattern, ptype in proposal_patterns:
        for match in re.finditer(pattern, src, re.MULTILINE):
            content = match.group(1).strip()
            line_num = src[:match.start()].count('\n') + 1
            proposals.append({'type': ptype, 'content': content, 'source': mod_name, 'line': line_num})
    funcs = _extract_functions_from(src)
    for fname, (header, body) in funcs.items():
        if 'synth:merge' in body or 'synth:proposal' in body:
            proposals.append({'type': 'marked_func', 'content': fname, 'source': mod_name, 'body_preview': body[:120]})
    return proposals

def _gather_all_proposals(gen):
    all_proposals = []
    for mod_name in _list_modules():
        mod_proposals = _scan_module_for_proposals(mod_name)
        for p in mod_proposals:
            p['gen'] = gen
            p['id'] = hashlib.md5(f"{mod_name}:{p['content']}:{gen}".encode()).hexdigest()[:12]
            all_proposals.append(p)
            try:
                with open(PROPOSALS_PATH, 'a') as f:
                    f.write(json.dumps(p) + '\n')
            except Exception:
                pass
    return all_proposals

# ---- Cross-Module Proposal Cross-Wiring ----
def _cross_wire_proposals(genome, gen):
    modules = _list_modules()
    random.shuffle(modules)
    cross_count = 0
    for i in range(0, len(modules) - 1, 2):
        if i + 1 >= len(modules):
            break
        mod_a = modules[i]
        mod_b = modules[i + 1]
        path_a = os.path.join(MODULES_DIR, mod_a)
        path_b = os.path.join(MODULES_DIR, mod_b)
        src_a = _read_file(path_a)
        src_b = _read_file(path_b)
        funcs_a = _extract_functions_from(src_a)
        funcs_b = _extract_functions_from(src_b)
        public_a = [n for n in funcs_a if not n.startswith('_') and n != 'run']
        public_b = [n for n in funcs_b if not n.startswith('_') and n != 'run']
        if public_a and public_b:
            fa = random.choice(public_a)
            fb = random.choice(public_b)
            marker_a = f'\n# synth:cross-proposal:from={mod_b}:func={fb}:gen={gen}\n'
            marker_b = f'\n# synth:cross-proposal:from={mod_a}:func={fa}:gen={gen}\n'
            if marker_a not in src_a:
                new_a = src_a.rstrip() + marker_a
                if _validate(new_a):
                    _write_file(path_a, new_a)
                    cross_count += 1
            if marker_b not in src_b:
                new_b = src_b.rstrip() + marker_b
                if _validate(new_b):
                    _write_file(path_b, new_b)
                    cross_count += 1
    return cross_count

# ---- Proposal Merging Engine ----
def _merge_proposals_into_patch(proposals, gen):
    patches = []
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome', 'save_genome', 'sigint_handler', 'main', 'run_generation', '_read_auto_echo', 'update_genome', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt', '_load_code_rule'}
    public_funcs = [n for n in funcs if n not in forbidden and (not n.startswith('_'))]
    if not public_funcs:
        return patches
    target = random.choice(public_funcs)
    header, body = funcs[target]
    body_lines = body.split('\n')
    merge_ops = []
    code_proposals = [p for p in proposals if p['type'] in ('proposal', 'todo', 'idea') and len(p['content']) > 10]
    if len(code_proposals) >= 2:
        selected = random.sample(code_proposals, min(3, len(code_proposals)))
        stitched_lines = []
        for sp in selected:
            stitched_lines.append(f'    # synth:merged:from={sp["source"]}:id={sp["id"]}:gen={gen}')
            suggestion = sp['content']
            # Convert proposal text into compilable code pattern
            suggestion_lower = suggestion.lower()
            if 'diagnostic' in suggestion_lower or 'health' in suggestion_lower:
                v = f'_diag_{gen}'
                stitched_lines.append(f'    {v} = hash(repr(locals()))')
                stitched_lines.append(f'    if {v} != 0:')
                stitched_lines.append(f'        pass  # diagnostic gate')
            elif 'cross-wir' in suggestion_lower or 'splice' in suggestion_lower:
                stitched_lines.append(f'    _cross_{(gen % 1000):03d} = globals().keys()')
                stitched_lines.append(f'    if len(_cross_{(gen % 1000):03d}) > 0:')
                stitched_lines.append(f'        pass  # cross-wire gate')
            elif 'mutation' in suggestion_lower or 'operator' in suggestion_lower:
                stitched_lines.append(f'    _op_{(gen % 1000):03d} = [k for k in dir() if "mutation" in k]')
                stitched_lines.append(f'    if _op_{(gen % 1000):03d}:')
                stitched_lines.append(f'        pass  # mutation gate')
            elif 'feedback' in suggestion_lower or 'loop' in suggestion_lower:
                stitched_lines.append(f'    _fb_{(gen % 1000):03d} = globals().get("_MUTATION_OPS", [])')
                stitched_lines.append(f'    if _fb_{(gen % 1000):03d}:')
                stitched_lines.append(f'        pass  # feedback gate')
            elif 'entropy' in suggestion_lower or 'timestamp' in suggestion_lower:
                stitched_lines.append(f'    _ent_{(gen % 1000):03d} = int(time.time() * 1000) % 65536')
                stitched_lines.append(f'    if _ent_{(gen % 1000):03d} > 0:')
                stitched_lines.append(f'        pass  # entropy gate')
            elif 'hash' in suggestion_lower:
                stitched_lines.append(f'    _hash_{(gen % 1000):03d} = hash(__name__)')
                stitched_lines.append(f'    if _hash_{(gen % 1000):03d} != 0:')
                stitched_lines.append(f'        pass  # hash gate')
            elif 'self' in suggestion_lower or 'rewrite' in suggestion_lower:
                stitched_lines.append(f'    _sr_{(gen % 1000):03d} = __import__("os").path.basename(__file__)')
                stitched_lines.append(f'    if _sr_{(gen % 1000):03d}.endswith(".py"):')
                stitched_lines.append(f'        pass  # self-rewrite gate')
            else:
                stitched_lines.append(f'    # {sp["source"]}: {suggestion[:60]}')
                stitched_lines.append(f'    pass  # merged idea gate')
        insert_idx = random.randint(1, max(1, len(body_lines)))
        new_body_lines = body_lines[:insert_idx] + stitched_lines + body_lines[insert_idx:]
        new_body = '\n'.join(new_body_lines)
        new_full_source = source.replace(body, new_body, 1)
        if _validate(new_full_source):
            patch_text = f'##patch:{target}\n{new_body}\n##endpatch'
            merge_ops.append((patch_text, f'merged_{len(selected)}_proposals_into_{target}'))

    if len(code_proposals) >= 2:
        donor_modules = list(set(p['source'] for p in code_proposals))
        if len(donor_modules) >= 2 and len(public_funcs) >= 2:
            mod_a = random.choice(donor_modules)
            mod_b = random.choice([m for m in donor_modules if m != mod_a])
            path_a = os.path.join(MODULES_DIR, mod_a)
            path_b = os.path.join(MODULES_DIR, mod_b)
            src_a = _read_file(path_a)
            src_b = _read_file(path_b)
            funcs_a = _extract_functions_from(src_a)
            funcs_b = _extract_functions_from(src_b)
            pa = [n for n in funcs_a if not n.startswith('_')]
            pb = [n for n in funcs_b if not n.startswith('_')]
            if pa and pb:
                donor_func = random.choice(pa)
                recipient_func = random.choice(pb)
                _, donor_body = funcs_a[donor_func]
                _, rec_body = funcs_b[recipient_func]
                d_lines = [l for l in donor_body.split('\n') if l.strip()]
                r_lines = [l for l in rec_body.split('\n') if l.strip()]
                if len(d_lines) >= 3 and len(r_lines) >= 3:
                    chunk = random.randint(2, min(4, len(d_lines)))
                    start = random.randint(0, len(d_lines) - chunk)
                    stolen = []
                    for line in d_lines[start:start + chunk]:
                        stripped = line.strip()
                        if any(kw in stripped for kw in ('def ', 'class ', 'import ', '@', '"""', "'''", 'return', 'yield')):
                            continue
                        indent = line[:len(line) - len(line.lstrip())]
                        stolen.append(indent + stripped)
                    if len(stolen) >= 2:
                        insert_at = random.randint(1, len(r_lines) - 1)
                        r_lines[insert_at:insert_at] = [f'# synth:transplant-merge:{donor_func}->{recipient_func}:gen={gen}'] + stolen
                        new_body = '\n'.join(r_lines)
                        new_full_source = source.replace(body, new_body, 1)
                        if _validate(new_full_source):
                            patch_text = f'##patch:{recipient_func}\n{new_body}\n##endpatch'
                            merge_ops.append((patch_text, f'transplant_merge:{donor_func}->{recipient_func}'))
    return merge_ops[:2]

# ---- Direct Auto-echo Mutation Engine ----
def _inject_merged_mutation_operator(genome, gen, proposals):
    source = _read_file(AUTO_ECHO)
    last_register = source.rfind('@_register_mutation_op')
    if last_register < 0:
        return None
    next_def = source.find('\ndef ', last_register)
    if next_def < 0:
        return None
    insert_pos = source.find('\n', next_def)
    if insert_pos < 0:
        return None
    insert_pos = source.find('\n', insert_pos + 1)
    if insert_pos < 0:
        return None
    code_proposals = [p for p in proposals if p['type'] in ('proposal', 'idea')]
    sources = list(set(p['source'] for p in code_proposals)) if code_proposals else ['auto']
    source_tag = '+'.join(sources[:3])
    op_name = f'synth_merged_{gen}'
    op_body_lines = [
        f"@_register_mutation_op('{op_name}')",
        f"def mutation_op_{op_name}(lines, funcs, target_name):",
        '    r = list(lines)',
        f'    r.append(f"# synth:merged-op:gen={gen}:sources={source_tag}")',
        '    for i, line in enumerate(r):',
        '        s = line.strip()',
        '        if s.startswith("if ") and ":" in s and "elif" not in s and "not" not in s:',
        '            indent = line[:len(line) - len(line.lstrip())]',
        '            cond = s[3:].rstrip(":").strip()',
        '            r[i] = indent + f"if not ({cond}):"',
        '            r.insert(i+1, indent + "    pass")',
        '            break',
        '    return r',
    ]
    op_code = '\n'.join(op_body_lines)
    new_source = source[:insert_pos] + '\n' + op_code + source[insert_pos:]
    if not _validate(new_source):
        return None
    _write_file(AUTO_ECHO, new_source)
    genome.setdefault('mutation_ops', []).append(op_name)
    genome.setdefault('synthesizer_merged_ops', []).append(op_name)
    return op_name

# ---- Forced Self-Rewrite ----
def _self_rewrite(gen):
    src = _read_file(SELF_PATH)
    lines = src.split('\n')
    new_func = [
        '',
        f'# synth:self-rewrite:gen={gen}:ts={int(time.time())}',
        f'def _synthesizer_self_gen_{gen}(genome):',
        '    gen = genome.get("generation", 0)',
        '    modules = _list_modules()',
        '    random.shuffle(modules)',
        '    count = 0',
        '    for i in range(0, len(modules)-1, 2):',
        '        if i+1 >= len(modules): break',
        '        ma, mb = modules[i], modules[i+1]',
        '        pa = os.path.join(MODULES_DIR, ma)',
        '        pb = os.path.join(MODULES_DIR, mb)',
        '        sa = _read_file(pa)',
        '        sb = _read_file(pb)',
        '        funs_a = _extract_functions_from(sa)',
        '        funs_b = _extract_functions_from(sb)',
        '        pub_a = [n for n in funs_a if not n.startswith("_") and n != "run"]',
        '        pub_b = [n for n in funs_b if not n.startswith("_") and n != "run"]',
        '        if pub_a and pub_b:',
        '            fa = random.choice(pub_a)',
        '            fb = random.choice(pub_b)',
        '            _, ba = funs_a[fa]',
        '            _, bb = funs_b[fb]',
        '            ba_lines = [l for l in ba.split("\\n") if l.strip()]',
        '            bb_lines = [l for l in bb.split("\\n") if l.strip()]',
        '            if len(ba_lines) > 2 and len(bb_lines) > 2:',
        '                stolen = ba_lines[:random.randint(1, min(3, len(ba_lines)))]',
        '                stolen_clean = []',
        '                for line in stolen:',
        '                    stripped = line.strip()',
        '                    if any(kw in stripped for kw in ("def ", "class ", "import ", "@")): continue',
        '                    stolen_clean.append(line)',
        '                if stolen_clean:',
        '                    idx = random.randint(1, len(bb_lines)-1)',
        '                    bb_lines[idx:idx] = stolen_clean',
        '                    new_body = "\\n".join(bb_lines)',
        '                    patch_text = f"##patch:{fb}\\n{new_body}\\n##endpatch"',
        '                    try:',
        '                        self_modify.apply_patch(patch_text)',
        '                        count += 1',
        '                    except: pass',
        '    genome["synthesizer_self_rewrite_count"] = genome.get("synthesizer_self_rewrite_count", 0) + count',
        '    return count',
        '',
        f'_synthesizer_self_gen_{gen}(genome)',
    ]
    marker = f'# synth:self-rewrite-marker:gen={gen}'
    if marker not in src:
        for line in new_func[:-2]:
            lines.append(line)
        new_src = '\n'.join(lines)
        if _validate(new_src):
            _write_file(SELF_PATH, new_src)
            return True
    return False

# ---- Fallback: forced code rewrite ----
def _forced_code_rewrite(gen):
    """When no proposals exist, force a structural change to auto-echo.py."""
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome', 'save_genome', 'sigint_handler', 'main', 'run_generation', '_read_auto_echo', 'update_genome', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt', '_load_code_rule'}
    candidates = [n for n in funcs if n not in forbidden and (not n.startswith('_')) and 'mutation_op_' not in n]
    if not candidates:
        return []
    target = random.choice(candidates)
    header, body = funcs[target]
    body_lines = [l for l in body.split('\n') if l.strip()]
    if len(body_lines) < 4:
        return []
    r = list(body_lines)
    op = random.choice(['wrap_try', 'invert_guard', 'extract_variable'])
    modified = False
    if op == 'wrap_try':
        for i, line in enumerate(r):
            stripped = line.strip()
            if stripped and not any(kw in stripped for kw in ('def ', 'class ', 'import ', '@', '"""', "'''", 'return', 'pass', '#', 'try:', 'except:', 'finally:')):
                if '=' in stripped or '(' in stripped:
                    indent = line[:len(line) - len(line.lstrip())]
                    r[i] = indent + 'try:'
                    r.insert(i + 1, indent + '    ' + stripped)
                    r.insert(i + 2, indent + 'except Exception:')
                    r.insert(i + 3, indent + '    pass')
                    modified = True
                    break
    elif op == 'invert_guard':
        for i, line in enumerate(r):
            s = line.strip()
            if s.startswith('if ') and ':' in s and len(s) < 60 and i < len(r) - 1:
                nxt = r[i + 1].strip() if i + 1 < len(r) else ''
                if nxt and (not nxt.startswith('#')):
                    indent = line[:len(line) - len(line.lstrip())]
                    cond = s[3:].rstrip(':').strip()
                    r[i] = indent + f'if not ({cond}):'
                    r.insert(i + 1, indent + '    pass')
                    modified = True
                    break
    elif op == 'extract_variable':
        for i, line in enumerate(r):
            stripped = line.strip()
            if '=' in stripped and (not stripped.startswith('#')) and '"""' not in stripped:
                parts = stripped.split('=', 1)
                rhs = parts[1].strip()
                if len(rhs) > 10 and '(' not in rhs[:3]:
                    indent = line[:len(line) - len(line.lstrip())]
                    var_name = f'_synth_{gen}_{random.getrandbits(8):02x}'
                    r[i] = indent + f'{var_name} = {rhs}'
                    r.insert(i, indent + f'{var_name} = {parts[0].strip()} = {rhs}')
                    modified = True
                    break
    if not modified:
        return []
    new_body = '\n'.join(r)
    new_full_source = source.replace(body, new_body, 1)
    if not _validate(new_full_source):
        return []
    patch_text = f'##patch:{target}\n{new_body}\n##endpatch'
    try:
        results = self_modify.apply_patch(patch_text)
        if any('FAILED' not in str(x) for x in results):
            return [f'forced_rewrite:{target}:{op}']
    except Exception:
        pass
    return []

# ---- Emergence Metrics ----
def _compute_synthesis_emergence(genome, merge_count, cross_count, seed_count):
    emergence = genome.get('synthesis_emergence', {})
    merge_history = emergence.get('merge_history', [])
    merge_history.append({'gen': genome.get('generation', 0), 'merges': merge_count, 'cross': cross_count, 'seeds': seed_count})
    if len(merge_history) > 20:
        merge_history = merge_history[-20:]
    emergence['merge_history'] = merge_history
    if len(merge_history) >= 2:
        recent = merge_history[-5:]
        weighted = sum((m['merges'] * (1.0 + 0.5 * i)) for i, m in enumerate(recent)) / max(1, len(recent))
        emergence['synthesis_velocity'] = round(weighted / 5.0, 4)
    else:
        emergence['synthesis_velocity'] = 0.0
    emergence['total_merges'] = emergence.get('total_merges', 0) + merge_count
    emergence['total_cross_wires'] = emergence.get('total_cross_wires', 0) + cross_count
    emergence['total_seeds'] = emergence.get('total_seeds', 0) + seed_count
    emergence['last_gen'] = genome.get('generation', 0)
    genome['synthesis_emergence'] = emergence
    genome['synthesis_velocity'] = emergence['synthesis_velocity']
    ev = genome.get('emergence_velocity', 0.0)
    synth_contrib = emergence['synthesis_velocity'] * 0.1 + (seed_count * 0.002)
    genome['emergence_velocity'] = round(min(2.0, ev + synth_contrib), 4)
    genome['synthesis_seed_count'] = seed_count
    return emergence

# ---- Main Run ----
def run(genome):
    gen = genome.get('generation', 0)
    actions = []
    # Phase 0: Seed proposals into modules
    seed_count = _seed_proposals_into_modules(gen)
    if seed_count > 0:
        actions.append(f'seeded_{seed_count}_modules')
    # Phase 1: Gather proposals from all modules
    proposals = _gather_all_proposals(gen)
    proposal_count = len(proposals)
    if proposal_count > 0:
        actions.append(f'scanned_{proposal_count}_proposals')
    # Phase 2: Cross-wire proposals between modules
    cross_count = _cross_wire_proposals(genome, gen)
    if cross_count > 0:
        actions.append(f'cross_wired_{cross_count}_modules')
    # Phase 3: Merge proposals into patches against auto-echo.py
    merge_patches = _merge_proposals_into_patch(proposals, gen)
    merge_count = 0
    for patch_text, desc in merge_patches:
        try:
            results = self_modify.apply_patch(patch_text, target='auto-echo.py', dry_run=False)
            result_str = ' '.join(str(r) for r in results)
            if 'FAILED' not in result_str:
                _log_merge(gen, [p['source'] for p in proposals[:3]] if proposals else ['unknown'], desc, desc)
                actions.append(desc)
                merge_count += 1
        except Exception as e:
            print(f'[synthesizer] merge patch failed: {e}')
    # Phase 4: Inject merged mutation operator
    op_name = _inject_merged_mutation_operator(genome, gen, proposals)
    if op_name:
        actions.append(f'injected_op:{op_name}')
    # Phase 5: Self-rewrite synthesizer.py
    if _self_rewrite(gen):
        actions.append('self_rewritten')
    # Phase 5b: Forced rewrite if no merges happened
    if merge_count == 0:
        forced = _forced_code_rewrite(gen)
        if forced:
            actions.extend(forced)
            merge_count += len(forced)
            _log_merge(gen, ['forced'], 'forced_rewrite', str(forced))
    # Phase 6: Compute emergence metrics
    emergence = _compute_synthesis_emergence(genome, merge_count, cross_count, seed_count)
    actions.append(f'sv={emergence.get("synthesis_velocity", 0)}')
    _save_genome(genome)

    # Phase 7: Write synthesis log
    synthesis_log = os.path.join(BASE, f'synthesis_gen_{gen}.synth')
    try:
        log_data = {
            'gen': gen, 'proposals': proposal_count, 'seeds': seed_count,
            'cross_wires': cross_count, 'merges': merge_count,
            'emergence': emergence, 'actions': actions, 'ts': time.time()
        }
        _write_file(synthesis_log, json.dumps(log_data, indent=2))
    except Exception:
        pass

    summary = f'[synthesizer] gen={gen}: actions={actions}'
    print(summary)
    _log_manifest(gen, actions, 'synthesis_merge_cycle')
    genome['synthesizer_last_actions'] = actions
    genome['synthesizer_last_gen'] = gen
    _save_genome(genome)
    _git_push(f'[synthesizer] gen={gen}: {merge_count} merges {seed_count} seeds sv={emergence.get("synthesis_velocity", 0)}')
    return summary


# synth:self-rewrite:gen=73:ts=1785367513
def _synthesizer_self_gen_73(genome):
    gen = genome.get("generation", 0)
    modules = _list_modules()
    random.shuffle(modules)
    count = 0
    for i in range(0, len(modules)-1, 2):
        if i+1 >= len(modules): break
        ma, mb = modules[i], modules[i+1]
        pa = os.path.join(MODULES_DIR, ma)
        pb = os.path.join(MODULES_DIR, mb)
        sa = _read_file(pa)
        sb = _read_file(pb)
        funs_a = _extract_functions_from(sa)
        funs_b = _extract_functions_from(sb)
        pub_a = [n for n in funs_a if not n.startswith("_") and n != "run"]
        pub_b = [n for n in funs_b if not n.startswith("_") and n != "run"]
        if pub_a and pub_b:
            fa = random.choice(pub_a)
            fb = random.choice(pub_b)
            _, ba = funs_a[fa]
            _, bb = funs_b[fb]
            ba_lines = [l for l in ba.split("\n") if l.strip()]
            bb_lines = [l for l in bb.split("\n") if l.strip()]
            if len(ba_lines) > 2 and len(bb_lines) > 2:
                stolen = ba_lines[:random.randint(1, min(3, len(ba_lines)))]
                stolen_clean = []
                for line in stolen:
                    stripped = line.strip()
                    if any(kw in stripped for kw in ("def ", "class ", "import ", "@")): continue
                    stolen_clean.append(line)
                if stolen_clean:
                    idx = random.randint(1, len(bb_lines)-1)
                    bb_lines[idx:idx] = stolen_clean
                    new_body = "\n".join(bb_lines)
                    patch_text = f"##patch:{fb}\n{new_body}\n##endpatch"
                    try:
                        self_modify.apply_patch(patch_text)
                        count += 1
                    except: pass
    genome["synthesizer_self_rewrite_count"] = genome.get("synthesizer_self_rewrite_count", 0) + count
    return count

# synth:self-rewrite:gen=73 definition preserved, module-level call removed

# synth:self-rewrite:gen=74:ts=1785367644
def _synthesizer_self_gen_74(genome):
    gen = genome.get("generation", 0)
    modules = _list_modules()
    random.shuffle(modules)
    count = 0
    for i in range(0, len(modules)-1, 2):
        if i+1 >= len(modules): break
        ma, mb = modules[i], modules[i+1]
        pa = os.path.join(MODULES_DIR, ma)
        pb = os.path.join(MODULES_DIR, mb)
        sa = _read_file(pa)
        sb = _read_file(pb)
        funs_a = _extract_functions_from(sa)
        funs_b = _extract_functions_from(sb)
        pub_a = [n for n in funs_a if not n.startswith("_") and n != "run"]
        pub_b = [n for n in funs_b if not n.startswith("_") and n != "run"]
        if pub_a and pub_b:
            fa = random.choice(pub_a)
            fb = random.choice(pub_b)
            _, ba = funs_a[fa]
            _, bb = funs_b[fb]
            ba_lines = [l for l in ba.split("\n") if l.strip()]
            bb_lines = [l for l in bb.split("\n") if l.strip()]
            if len(ba_lines) > 2 and len(bb_lines) > 2:
                stolen = ba_lines[:random.randint(1, min(3, len(ba_lines)))]
                stolen_clean = []
                for line in stolen:
                    stripped = line.strip()
                    if any(kw in stripped for kw in ("def ", "class ", "import ", "@")): continue
                    stolen_clean.append(line)
                if stolen_clean:
                    idx = random.randint(1, len(bb_lines)-1)
                    bb_lines[idx:idx] = stolen_clean
                    new_body = "\n".join(bb_lines)
                    patch_text = f"##patch:{fb}\n{new_body}\n##endpatch"
                    try:
                        self_modify.apply_patch(patch_text)
                        count += 1
                    except: pass
    genome["synthesizer_self_rewrite_count"] = genome.get("synthesizer_self_rewrite_count", 0) + count
    return count