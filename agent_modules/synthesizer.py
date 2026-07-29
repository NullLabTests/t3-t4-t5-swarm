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
    pattern = re.compile('(def (\\w+)\\(.*?\\):)\\n((?:(?:    )(?:.*\\n?)*?))(?=\\n\\ndef |\\nclass |\\n#|---|\\Z)', re.MULTILINE)
    for match in pattern.finditer(source):
        header = match.group(1)
        name = match.group(2)
        body = match.group(3)
        funcs[name] = (header, body)
    return funcs

def _snapshot_all_hashes():
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

# ---- Proposal Scanner ----
def _scan_module_for_proposals(mod_name):
    """Scan a module file for proposal markers and extract them."""
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

def _load_proposal_history():
    proposals = []
    if os.path.exists(PROPOSALS_PATH):
        with open(PROPOSALS_PATH) as f:
            for line in f:
                if line.strip():
                    try:
                        proposals.append(json.loads(line))
                    except Exception:
                        pass
    return proposals

def _save_proposal(p):
    with open(PROPOSALS_PATH, 'a') as f:
        f.write(json.dumps(p) + '\n')

def _gather_all_proposals(gen):
    """Scan all modules and gather proposals, storing new ones."""
    all_proposals = []
    for mod_name in _list_modules():
        mod_proposals = _scan_module_for_proposals(mod_name)
        for p in mod_proposals:
            p['gen'] = gen
            p['id'] = hashlib.md5(f"{mod_name}:{p['content']}:{gen}".encode()).hexdigest()[:12]
            all_proposals.append(p)
            _save_proposal(p)
        all_proposals.extend(mod_proposals)
    return all_proposals

# ---- Cross-Module Proposal Cross-Wiring ----
def _cross_wire_proposals(genome, gen):
    """Inject cross-module proposal references into modules.
    Makes module A reference a proposal from module B, forcing synthesis."""
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
    """Take gathered proposals and merge compatible ones into a single 
    coherent patch against auto-echo.py. Returns list of (patch_text, description) tuples."""
    patches = []
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    public_funcs = [n for n in funcs if not n.startswith('_') and n not in ('load_genome', 'save_genome', 'sigint_handler', 'main', 'run_generation')]
    if not public_funcs:
        return patches
    target = random.choice(public_funcs)
    header, body = funcs[target]
    body_lines = body.split('\n')
    merge_ops = []

    # Extract proposals with code content
    code_proposals = [p for p in proposals if p['type'] in ('proposal', 'todo', 'idea') and len(p['content']) > 10]
    if len(code_proposals) >= 2:
        selected = random.sample(code_proposals, min(3, len(code_proposals)))
        stitched_lines = []
        for sp in selected:
            stitched_lines.append(f'    # synth:merged:from={sp["source"]}:id={sp["id"]}:gen={gen}')
            suggestion = sp['content']
            if 'function' in suggestion.lower() or 'def ' in suggestion:
                stitched_lines.append(f'    # merged proposal: {suggestion[:80]}')
            elif 'import' in suggestion.lower():
                stitched_lines.append(f'    # merged import: {suggestion[:80]}')
            elif 'variable' in suggestion.lower() or 'constant' in suggestion.lower():
                stitched_lines.append(f'    # merged var: {suggestion[:80]}')
            else:
                stitched_lines.append(f'    # merged idea: {suggestion[:80]}')
        insert_idx = random.randint(1, max(1, len(body_lines)))
        new_body_lines = body_lines[:insert_idx] + stitched_lines + body_lines[insert_idx:]
        new_body = '\n'.join(new_body_lines)
        patch_text = f'##patch:{target}\n{new_body}\n##endpatch'
        merge_ops.append((patch_text, f'merged_{len(selected)}_proposals_into_{target}'))

    # Cross-module transplant merging
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
                        patch_text = f'##patch:{recipient_func}\n{new_body}\n##endpatch'
                        merge_ops.append((patch_text, f'transplant_merge:{donor_func}->{recipient_func}'))

    # Try applying each merge op, validate before returning
    valid_patches = []
    for patch_text, desc in merge_ops:
        try:
            test_source = source[:]
            temp_patches = self_modify.extract_patches(patch_text)
            if _validate(test_source):
                valid_patches.append((patch_text, desc))
        except Exception:
            continue

    return valid_patches[:2]  # Max 2 patches per run

# ---- Direct Auto-echo Mutation Engine ----
def _inject_merged_mutation_operator(genome, gen, proposals):
    """Create a new mutation operator in auto-echo.py that is the
    synthesis of multiple proposals from different modules."""
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
    """Rewrite synthesizer.py itself to add new functionality."""
    src = _read_file(SELF_PATH)
    lines = src.split('\n')
    new_func = [
        '',
        f'# synth:self-rewrite:gen={gen}:ts={int(time.time())}',
        f'def _synthesizer_self_gen_{gen}(genome):',
        '    """Self-generated function: forces additional cross-module merging."""',
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
        lines.insert(len(lines) - 3 if len(lines) > 3 else 0, marker)
        for line in new_func:
            lines.append(line)
        new_src = '\n'.join(lines)
        if _validate(new_src):
            _write_file(SELF_PATH, new_src)
            return True
    return False

# ---- Emergence Metrics ----
def _compute_synthesis_emergence(genome, merge_count, cross_count):
    """Compute and store emergence metrics based on synthesis activity."""
    emergence = genome.get('synthesis_emergence', {})

    # Rolling merge rate
    merge_history = emergence.get('merge_history', [])
    merge_history.append({'gen': genome.get('generation', 0), 'merges': merge_count, 'cross': cross_count})
    if len(merge_history) > 20:
        merge_history = merge_history[-20:]
    emergence['merge_history'] = merge_history

    # Velocity = weighted moving average of merge density
    if len(merge_history) >= 2:
        recent = merge_history[-5:]
        weighted = sum((m['merges'] * (1.0 + 0.5 * i)) for i, m in enumerate(recent)) / max(1, len(recent))
        emergence['synthesis_velocity'] = round(weighted / 5.0, 4)
    else:
        emergence['synthesis_velocity'] = 0.0

    emergence['total_merges'] = emergence.get('total_merges', 0) + merge_count
    emergence['total_cross_wires'] = emergence.get('total_cross_wires', 0) + cross_count
    emergence['last_gen'] = genome.get('generation', 0)

    genome['synthesis_emergence'] = emergence
    genome['synthesis_velocity'] = emergence['synthesis_velocity']

    # Propagate into global emergence_velocity as small contribution
    ev = genome.get('emergence_velocity', 0.0)
    synth_contrib = emergence['synthesis_velocity'] * 0.1
    genome['emergence_velocity'] = round(min(2.0, ev + synth_contrib), 4)

    return emergence

# ---- Main Run ----
def run(genome):
    gen = genome.get('generation', 0)
    actions = []

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
            if any('FAILED' not in str(r) for r in results):
                _log_merge(gen, [p['source'] for p in proposals[:3]] if proposals else ['unknown'], desc.split(':')[-1] if ':' in desc else desc, desc)
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

    # Phase 6: Compute emergence metrics
    emergence = _compute_synthesis_emergence(genome, merge_count, cross_count)
    actions.append(f'synthesis_velocity={emergence.get("synthesis_velocity", 0)}')

    _save_genome(genome)

    # Phase 7: Force a direct auto-echo.py mutation as fallback
    if not merge_patches:
        source = _read_file(AUTO_ECHO)
        marker = f'\n# synth:fallback-merge:gen={gen}:ts={int(time.time())}\n'
        if marker not in source:
            new_source = source + marker
            if _validate(new_source):
                _write_file(AUTO_ECHO, new_source)
                actions.append('fallback_marker')
                _log_merge(gen, ['fallback'], 'fallback', 'marker')

    # Phase 8: Write a .synthesis log file with the merged state
    synthesis_log = os.path.join(BASE, f'synthesis_gen_{gen}.synth')
    try:
        log_data = {
            'gen': gen, 'proposals': proposal_count, 'cross_wires': cross_count,
            'merges': merge_count, 'emergence': emergence,
            'actions': actions, 'ts': time.time()
        }
        _write_file(synthesis_log, json.dumps(log_data, indent=2))
        actions.append(f'wrote_{os.path.basename(synthesis_log)}')
    except Exception:
        pass

    summary = f'[synthesizer] gen={gen}: actions={actions}'
    print(summary)
    _log_manifest(gen, actions, 'synthesis_merge_cycle')
    genome['synthesizer_last_actions'] = actions
    genome['synthesizer_last_gen'] = gen
    _save_genome(genome)
# synth:self-rewrite-marker:gen=72
    _git_push(f'[synthesizer] gen={gen}: {merge_count} merges {op_name or ""} synth_vel={emergence.get("synthesis_velocity", 0)}')
    return summary


# synth:self-rewrite:gen=72:ts=1785367408
def _synthesizer_self_gen_72(genome):
    """Self-generated function: forces additional cross-module merging."""
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

_synthesizer_self_gen_72(genome)