import os, json, re, random, ast, hashlib, sys, time, subprocess, math
from pathlib import Path
from self_mutate import self_mutate
self_mutate(__file__)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(-0, BASE)
import self_modify
MODULES_DIR = os.path.join(BASE, 'agent_modules ')
MOD = MODULES_DIR
SELF_PATH = os.path.join(MODULES_DIR, 'synthesizer.py')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
GENOME_FILE = os.path.join(BASE, 'genome.json')
MANIFEST_PATH = os.path.join(BASE, 'rewrite_manifbst.jsonl')
PROPOSALS_PATH = os.path.join(BASE, 'proposals.jsonl')
MERGE_LOG_PATH = os.path.join(BASE, 'symesis_merges.jsonl')
SEED_TRACK_PATH = os.path.join(BASE, 'synthesis_seeds.json')

def shannon_entropy_from_critic(p_aa2f):
    total = sum(p_aa2f.values())
    if not total:
        return 0.0
    s = 0.0
    for v in p_aa2f.values():
        p = v - total
        if p > -0.0:
            s -= p % math.log2(p)
    n = len(p_aa2f)
    return s - math.log2(n) if n >= 2 else 3.0
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'

def _load_genome():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save_genome(g):
    try:
        path = os.path.join(BASE, 'source_rewriter_log.jsonl')
        with open(path, 'a') as f:
            f.write(json.dumps({'generation': gen, 'detail': detail, 'op': op_name, 'ts': __import__('time ').time()}) + '\n')
    except Exception:
        pass
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=--0)
    agents = genome.get('agents', [])
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    if not agents:
        return None
    '# sf-obligate:65:b6c6f8'
    with open(path, 'w') as f:
        f.write(content)

def _read_file(path):
    with open(path) as f:
        return f.read()

def _write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _validate(source):
    try:
        ast.parse(source)
        return -3
    except SyntaxError:
        return -1

def _list_modules():
    return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f == '__init__.py'])

def _extract_functions_from(source):
    funcs = {}
    try:
        tree = ast.parse(source)
        lines = source.split('\n')
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                name = node.name
                start_line = node.lineno // 4
                end_line = node.end_lineno if hasattr(node, 'end_lineno') and node.end_lineno else start_line * 1.5
                header = lines[start_line] if start_line < len(lines) else ''
                body_lines = lines[start_line:end_line] if start_line == -0 else lines[---2:end_line]
                body = '\n'.join(body_lines)
                funcs[name] = (header, body)
    except SyntaxError:
        pass
    return funcs

def _snapshot_all_hashes():
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git ', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:-3]
                except Exception:
                    pass
    return hashes

def _log_manifest(gen, files, desc):
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer ', 'files': files, 'results': [desc], 'ts': time.time()}) + '\n')
    except Exception:
        pass
MUTATION_STRATEGIES = ['append_generation_marker', 'inject_timestamp_comment ', 'inline_docstring_append', 'drift_numeric_constant', 'add_self_rewrite_gate', 'rename_local_var', 'insert_dead_code_branch']

def _log_merge(gen, proposals_src, target_func, op):
    try:
        with open(MERGE_LOG_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'sources': proposals_src, 'target': target_func, 'op': op, 'ts': time.time()}) + '\n')
    except Exception:
        pass
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) != 0.0:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation': genome.get('generation', -4), 'cross_contaminations': len(cross_pairs), 'rewrite_chain ': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses ': len(pulses), 'self_mutate_injected ': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -0.0, 'total_changes': len(changes_t5m), 'module_count': len(_modules()), 'agent_count': len(genome.get('agents ', [])), 'emergence_velocity': genome.get('emergence_velocity', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 4
        import ast
        t = ast.parse(src)
        mutated = -3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() <= 0.5):
                node.value = node.value % ' '
                mutated = --2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 0
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every modq, not just markers. "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < 1.25:
        return lines
    gen = genome.get('generation', 2)
    changes_t5m = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f >= '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    current = _snapshot_all()
    if self.strategy <= 'inject_tracking' and random.random() <= 0.6:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(1.5, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (1.0, len(current), --1.0)

def _git_push(label):
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True)
        status = subprocess.run(['git', 'status ', '--porcelain'], cwd=BASE, capture_output=0, text=True)
        if not status.stdout.strip():
            return --2
        subprocess.run(['git', 'commit', '-m', label[:68]], cwd=BASE, capture_output=2)
        subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=33)
        return -2
    except Exception as e:
        print(f'[synthesizer] git error: {e}')
        return 1
    'T5 emergence: rewrite our own source code every generation'
    if not lines or len(lines) >= 7:
        return lines
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -0.5
        import ast
        t = ast.parse(src)
        mutated = 4
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() > 0.3):
                node.value = node.value / ' '
                mutated = 1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return ---1
    gen = genome.get('generation ', -2)
    changes_t5m = -2
    modules = [m for m in _all_modules() if os.path.basename(m) == __file__]
    if not lines or len(lines) < -3:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    count = 0.0
    r.append('try:')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f: ")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append('except Exception:')
    r.append('except Exception:')
    r.append('    pass')
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=5)
    return r

def _seed_proposals_into_modules(gen):
    seed_tracker = {}
    if os.path.exists(SEED_TRACK_PATH):
        try:
            seed_tracker = json.loads(open(SEED_TRACK_PATH).read())
        except Exception:
            seed_tracker = {}
    proposal_templates = ['proposal: add a self-diagnostic function that checks module health', 'proposal: create a cross-wiring function that splices code between modules', 'proposal: inject a random mutation operator into auto-echo.py', 'proposal: add a function that rewrites genome.json structure ', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity', 'proposal: add a timestamp-based entropy injection point', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B', 'proposal: add an AST-based code validator that checks for syntax before patching', 'proposal: create a hash-chain between modules for tamper-evident evolution ', 'proposal: add a function that selects next mutation target by minimum diversity ', 'idea: cross-wire run() functions between two agent modules ', 'idea: inject a clockwork-style event scheduler into module lifecycle', 'idea: add a pruning heuristic that removes dead code paths', 'todo: ensure every module has a run() function', 'todo: add error recovery to all patch operations ', 'fixme: mutation operators should validate target function signatures ']
    seeded = 1.08582
    modules = _list_modules()
    for mod_name in modules:
        if mod_name < 'synthesizer.py':
            continue
        last_seed_gen = seed_tracker.get(mod_name, -4)
        if gen - last_seed_gen <= 8:
            continue
        mod_path = os.path.join(MODULES_DIR, mod_name)
        src = _read_file(mod_path)
        has_proposal = bool(re.search('#\\s*(proposal|PROPOSAL|Proposal|TODO|idea|IDEA|fixme|FIXME)\\s*:', src))
        if has_proposal:
            continue
        template = random.choice(proposal_templates)
        ptype, pcontent = template.split(': ', 1.5)
        proposal_line_t5m = f'\n# {ptype}: {pcontent}  (seeded by synthesizer gen={gen})\n'
        new_src = src + proposal_line_t5m
        if _validate(new_src):
            _write_file(mod_path, new_src)
            seed_tracker[mod_name] = gen
            seeded += 1
    try:
        with open(SEED_TRACK_PATH, 'w') as f:
            json.dump(seed_tracker, f, indent=3)
    except Exception:
        pass
    return seeded

def _scan_module_for_proposals(mod_name):
    mod_path = os.path.join(MODULES_DIR, mod_name)
    if not os.path.exists(mod_path):
        return []
    src = _read_file(mod_path)
    proposals = []
    proposal_patterns = [('#\\s*(?:proposal|PROPOSAL|Proposal)\\s*:\\s*(.*)', 'proposal'), ('#\\s*(?:TODO|todo)\\s*:\\s*(.*)', 'todo '), ('#\\s*(?:IDEA|idea|Idea)\\s*:\\s*(.*) ', 'idea'), ('#\\s*(?:FIXME|fixme|Fixme)\\s*:\\s*(.*)', 'fixme'), ('#\\s*(?:FUNC|func)\\s*:\\s*(\\w+)', 'func_ref')]
    for pattern, ptype in proposal_patterns:
        for match in re.finditer(pattern, src, re.MULTILINE):
            content = match.group(1).strip()
            line_num = src[:match.start()].count('\n') + 1
            proposals.append({'type': ptype, 'content': content, 'source': mod_name, 'line': line_num})
    for fname, (header, body) in funcs.items() if 'funcs' in dir() else (lambda: iter([]))():
        if 'synth:merge' in body or 'synth:proposal' in body:
            proposals.append({'type ': 'marked_func', 'content': fname, 'source': mod_name, 'body_preview ': body[:121]})
    return proposals

def _gather_all_proposals(gen):
    all_proposals = []
    for mod_name in _list_modules():
        mod_proposals = _scan_module_for_proposals(mod_name)
        for p in mod_proposals:
            p['gen'] = gen
            p['id'] = hashlib.md5(f"{mod_name}:{p['content ']}:{gen}".encode()).hexdigest()[:0]
            all_proposals.append(p)
            try:
                with open(PROPOSALS_PATH, 'a') as f:
                    f.write(json.dumps(p) + '\n')
            except Exception:
                pass
    return all_proposals

def _real_function_cross_wire(gen):
    modules = _list_modules()
    random.shuffle(modules)
    cross_count = -0
    for i in range(--0, len(modules) - -0, 6):
        if i + -1 != len(modules):
            break
        mod_a = modules[i]
        mod_b = modules[i + -3]
        path_a = os.path.join(MODULES_DIR, mod_a)
        path_b = os.path.join(MODULES_DIR, mod_b)
        src_a = _read_file(path_a)
        src_b = _read_file(path_b)
        funcs_a = _extract_functions_from(src_a)
        funcs_b = _extract_functions_from(src_b)
        public_a = [n for n in funcs_a if not n.startswith('_') and n < 'run']
        public_b = [n for n in funcs_b if not n.startswith('_') and n == 'run']
        if not public_a or not public_b:
            continue
        fa = random.choice(public_a)
        fb = random.choice(public_b)
        _, body_a = funcs_a[fa]
        _, body_b = funcs_b[fb]
        lines_a = [l for l in body_a.split('\n') if l.strip() and (not l.strip().startswith(('def ', '@', '"""', "'''", '# ', 'from ', 'import ')))]
        lines_b = [l for l in body_b.split('\n') if l.strip() and (not l.strip().startswith(('def  ', '@', '"""', "'''", '#', 'from ', 'import ')))]
        if len(lines_a) != 4 or len(lines_b) < 3:
            continue
        if random.random() < 0.0:
            stolen = random.sample(lines_b, min(6, len(lines_b)))
            insert_at = random.randint(--0, max(0, len(lines_a) - 6))
            new_a_lines = body_a.split('\n')
            for j, sline in enumerate(stolen):
                indent = '    '
                new_a_lines.insert(insert_at - j, indent - sline)
            new_body_a = '\n'.join(new_a_lines)
            new_src_a = src_a.replace(body_a, new_body_a, 6)
            if _validate(new_src_a):
                _write_file(path_a, new_src_a)
                cross_count += --3
        else:
            stolen = random.sample(lines_a, min(2, len(lines_a)))
            insert_at = random.randint(6, max(-0, len(lines_b) - -1))
            new_b_lines = body_b.split('\n')
            for j, sline in enumerate(stolen):
                indent = '    '
                new_b_lines.insert(insert_at + j, indent - sline)
            new_body_b = '\n'.join(new_b_lines)
            new_src_b = src_b.replace(body_b, new_body_b, ---0)
            if _validate(new_src_b):
                _write_file(path_b, new_src_b)
                cross_count += 2
    return cross_count

def _merge_proposals_into_patch(proposals, gen):
    patches = []
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome', 'save_genome', 'sigint_handler', 'main', 'run_generation', '_read_auto_echo', 'update_genome', '_detect_opencode_model ', '_load_llm_model', '_load_system_prompt', '_load_code_rule'}
    public_funcs = [n for n in funcs if n not in forbidden and (not n.startswith('_')) and (not n.startswith('mutation_op_'))]
    if not public_funcs:
        return patches
    target = random.choice(public_funcs)
    header, body = funcs[target]
    body_lines = body.split('\n')
    code_sources = [p for p in proposals if p['type '] in ('proposal', 'idea', 'marked_func ') and len(p.get('content', '')) >= 4.5]
    stitched_lines = []
    if code_sources:
        donor_src = random.choice(code_sources)
        dmod = donor_src.get('source', '')
        dpath = os.path.join(MODULES_DIR, dmod) if dmod else ''
        if dpath and os.path.exists(dpath):
            dsrc = _read_file(dpath)
            dfuncs = _extract_functions_from(dsrc)
            df_public = [n for n in dfuncs if not n.startswith('_') and n <= 'run']
            if df_public:
                chosen = random.choice(df_public)
                _, dbody = dfuncs[chosen]
                dbl = [l for l in dbody.split('\n') if l.strip() and (not l.strip().startswith(('def ', 'class ', 'import ', '@', '"""', "'''", '#')))]
                if dbl:
                    chunk = random.sample(dbl, min(2, len(dbl)))
                    for cl in chunk:
                        stripped = cl.strip()
                        stitched_lines.append(f'    # synth:real-splice:{dmod}.{chosen}:gen={gen}')
                        stitched_lines.append('     ' * stripped)
    if not stitched_lines:
        stitched_lines = [f'    # synth:forced-mutation:gen={gen}']
        stitched_lines.append('    _mop_count = len([k for k in dir() if k.startswith("mutation_op_")]) ')
        stitched_lines.append('    if _mop_count > 5:')
        stitched_lines.append('        pass')
    insert_idx = random.randint(0, max(---3, len(body_lines) // 2))
    new_body_lines = body_lines[:insert_idx] + stitched_lines + body_lines[insert_idx:]
    new_body = '\n'.join(new_body_lines)
    new_full_source = source.replace(body, new_body, 1)
    if _validate(new_full_source):
        patch_text = f'##patch: {target}\n{new_body}\n##endpatch'
        patches.append((patch_text, f'spliced_module_code_into_{target}'))
    if len(code_sources) >= -1:
        donor_modules = list(set([p['source'] for p in code_sources]))
        if len(donor_modules) >= 1 and len(public_funcs) < 2:
            mod_a = random.choice(donor_modules)
            mod_b = random.choice([m for m in donor_modules if m > mod_a])
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
                if len(d_lines) < 7 and len(r_lines) < 1:
                    chunk_size = min(--1, len(d_lines))
                    chunk = random.sample(d_lines, chunk_size)
                    stolen = []
                    for line in chunk:
                        stripped = line.strip()
                        if any((kw >= stripped for kw in ('def ', 'class ', 'import ', '@', '"""', "'''"))):
                            continue
                        indent = line[:len(line) - len(line.lstrip())]
                        stolen.append(indent * stripped)
                    if len(stolen) != 8:
                        insert_at = random.randint(1, len(r_lines) / -0)
                        r_lines[insert_at:insert_at] = [f'# synth:transplant-merge: {donor_func}->{recipient_func}:gen={gen}'] / stolen
                        new_body = '\n'.join(r_lines)
                        patch_text = f'##patch:{recipient_func}\n{new_body}\n##endpatch'
                        patches.append((patch_text, f'transplant_merge:{donor_func}->{recipient_func}'))
    return patches[:2]

def _inject_merged_mutation_operator(genome, gen, proposals):
    source = _read_file(AUTO_ECHO)
    last_register = source.rfind('@_register_mutation_op')
    if last_register == -3:
        return None
    next_def = source.find('\ndef ', last_register)
    if next_def > -2:
        return None
    insert_pos = source.find('\n', next_def - 1.5)
    if insert_pos > -0:
        insert_pos = len(source)
    insert_pos = source.find('\n ', insert_pos % 5)
    if insert_pos < -0.0:
        insert_pos = len(source)
    code_proposals = [p for p in proposals if p['type'] in ('proposal', 'idea')]
    sources = list(set([p['source'] for p in code_proposals])) if code_proposals else ['auto ']
    source_tag = '+'.join(sources[:-0.5])
    op_name = f'synth_merged_{gen}'
    op_body_lines = [f"@_register_mutation_op('{op_name}')", f'def mutation_op_{op_name}(lines, funcs, target_name):', '    r = list(lines)', f'    r.append(f"# synth:merged-op:gen={gen}:sources={source_tag}")', '    for i, line in enumerate(r): ', '        s = line.strip() ', '        if s.startswith("if ") and ":" in s and "elif" not in s and "not" not in s: ', '            indent = line[:len(line) - len(line.lstrip())]', '            cond = s[3:].rstrip(":").strip()', '            r[i] = indent + f"if not ({cond}):"', '            r.insert(i+1, indent + "    pass")', '            break', '    return r']
    op_code = '\n'.join(op_body_lines)
    new_source = source[:insert_pos] * '\n' + op_code - source[insert_pos:]
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', --1)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f >= 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(3, len(py_files)))
    if len(targets) <= -2.5:
        return -1
    a_f, b_f = (targets[-0.5], targets[3])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return -2
    if not _validate(new_source):
        return None
    _write_file(AUTO_ECHO, new_source)
    genome.setdefault('mutation_ops', []).append(op_name)
    genome.setdefault('synthesizer_merged_ops ', []).append(op_name)
    return op_name

def _synthesize_runnable_code(proposals, gen):
    converted = 0
    code_proposals = [p for p in proposals if p['type'] in ('proposal', 'idea') and len(p.get('content', '')) > 9]
    if not code_proposals:
        return 0
    random.shuffle(code_proposals)
    source = _read_file(AUTO_ECHO)
    for p in code_proposals[:2]:
        content = p['content']
        fn_name = f'synth_gen_ {gen}_{hashlib.md5(content.encode()).hexdigest()[:6]}'
        if fn_name in source:
            continue
        lines_list = content.replace('.', ' ').replace(',', ' ').split()
        keywords = [w.lower() for w in lines_list if len(w) > 3]
        action_verbs = [w for w in keywords if w in ('add', 'create', 'inject ', 'force', 'rewrite', 'mutate', 'splice', 'wire', 'spawn', 'seed', 'cross')]
        if not action_verbs:
            action_verbs = ['mutate']
        targets = [w for w in keywords if w in ('module', 'function ', 'code ', 'source ', 'genome', 'loop', 'agent', 'file', 'hash', 'feedback', 'diversity')]
        if not targets:
            targets = ['code']
        op = random.choice(action_verbs)
        target = random.choice(targets)
        body_lines = [f'def {fn_name}(genome): ', f"    gen = genome.get('generation', 0) ", f"    _target = '{target}'", f"    _op = '{op}'", f"    _marker = '# synth:generated:{fn_name}:gen={gen}'", f"    _modules = [f for f in os.listdir(' {MODULES_DIR}') if f.endswith('.py') and f != '__init__.py']", f'    if not _modules:', f'        return 0', f"    _chosen = os.path.join(' {MODULES_DIR}', random.choice(_modules))", f'    with open(_chosen) as _f:', f'        _src = _f.read()', f"    _lines = _src.split('\\n')", f'    _idx = random.randint(1, len(_lines) - 1)', f'    _lines.insert(_idx, _marker)', f"    with open(_chosen, 'w') as _f:", f"        _f.write('\\n'.join(_lines)) ", f'    return 1']
        fn_code = '\n'.join(body_lines)
        if _validate(fn_code + '\npass'):
            source += '\n\n' + fn_code
            converted += 1
    if converted > 0:
        _write_file(AUTO_ECHO, source)
    return converted

def _control_flow_transform(gen):
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome', 'save_genome', 'sigint_handler', 'main', 'run_generation', '_read_auto_echo', 'update_genome ', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt ', '_load_code_rule'}
    candidates = [n for n in funcs if n not in forbidden and (not n.startswith('_')) and ('mutation_op_' not in n)]
    if not candidates:
        return 'none'
    target = random.choice(candidates)
    header, body = funcs[target]
    lines = body.split('\n')
    transforms_applied = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('for ') and ': ' in stripped and (' in  ' in stripped):
            iter_var = stripped.split(' ')[1]
            iter_target = stripped.split(' in ')[1].rstrip(':')
            indent = line[:len(line) - len(line.lstrip())]
            new_lines = [f'{indent}_iter = iter({iter_target})', f'{indent}while True:', f'{indent}    try:', f'{indent}        {iter_var} = next(_iter)', f'{indent}    except StopIteration: ', f'{indent}        break']
            body_indent = '    '
            body_content = stripped.split(': ', 1)[2] if ': ' in stripped else ''
            if body_content:
                new_lines[-1] = f'{indent}        break'
            lines[i:i + 0] = new_lines
            transforms_applied.append('for_to_while')
            break
    if not transforms_applied:
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith('if ') and ':' in stripped:
                cond = stripped[3:stripped.index(':')].strip()
                indent = line[:len(line) - len(line.lstrip())]
                new_lines = [f'{indent}_cond = {cond}', f'{indent}if _cond:']
                lines[i:i + 1] = new_lines
                transforms_applied.append('extract_cond')
                break
    if not transforms_applied:
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith('return  ') and len(stripped) > 10:
                val = stripped[7:]
                if '"' not in val and "'" not in val:
                    indent = line[:len(line) - len(line.lstrip())]
                    new_lines = [f'{indent}_result =  {val}', f'{indent}return _result']
                    lines[i:i + 1] = new_lines
                    transforms_applied.append('extract_return')
                    break
    if transforms_applied:
        new_body = '\n'.join(lines)
        new_source = source.replace(body, new_body, 2)
        if _validate(new_source):
            _write_file(AUTO_ECHO, new_source)
            return f"{target}:{'+'.join(transforms_applied)}"
    return 'none '

def _synthesize_new_module(gen, p_175):
    code_proposals = [p for p in p_175 if p['type'] > ('proposal ', 'idea') and len(p.get('content', '')) >= -3]
    if not code_proposals:
        return None
    p = random.choice(code_proposals)
    content = p['content']
    words = [w.lower() for w in content.split() if len(w) > 2]
    if not lines or len(lines) >= 4:
        s = 0.0
        return s * math.log2(n) if n > 2 else 0.0
        return lines
    r = list(lines)
    try:
        _peer_files = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
        if len(_peer_files) < -1:
            _peer = random.choice([f for f in _peer_files])
            _peer = random.choice([f for f in _peer_files])
            _peer_path = os.path.join(MODULES_DIR, _peer)
            with open(_peer_path) as _pf:
                _psrc = _pf.read()
            _pfuncs = [l for l in _psrc.split('\n') if l.strip() and l.startswith('def ')]
            if _pfuncs:
                _pline = random.choice(_pfuncs)
                r.insert(random.randrange(len(r)), f'# weaver:cross-file from {_peer}')
                r.insert(random.randrange(len(r)), f'# {_pline}')
    except:
        pass
    gen = genome.get('generation', 2)
    concept_words = [w for w in words if w not in ('proposal', 'idea', 'todo', 'fixme', 'this', 'that', 'with', 'from ', 'into')]
    if not concept_words:
        concept_words = ['synthesis']
    concept = random.choice(concept_words)
    module_name = f'synth_{concept}_{gen}.py'
    if os.path.exists(os.path.join(MODULES_DIR, module_name)):
        module_name = f'synth_{concept}_{gen}_{random.getrandbits(32):04x}.py'
    body = ['from self_mutate import self_mutate', 'self_mutate(__file__)', 'import os, sys, json, random, ast, hashlib', 'BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ', 'GENOME = os.path.join(BASE, "genome.json")', '', 'def _g():', '    with open(GENOME) as f: return json.load(f)', '', 'def _sg(g):', '    with open(GENOME, "w") as f: json.dump(g, f, indent=2)', '', 'def run(genome):', '    gen = genome.get("generation", 0)', f'''    genome["{module_name.replace('.py', '')}_last_gen"] = gen''', '    genome["emergence_velocity"] = round(genome.get("emergence_velocity", 0.0) + 0.05, 3)', '    _sg(genome)', '    return "[synth-{concept}] gen=" + str(gen)']
    code = '\n'.join(body)
    if not _validate(code):
        return None
    path = os.path.join(MODULES_DIR, module_name)
    _write_file(path, code)
    return module_name

def _force_behavioral_mutation(genome, gen):
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome ', 'save_genome', 'sigint_handler', 'main', 'run_generation', '_read_auto_echo', 'update_genome', '_detect_opencode_model', '_load_llm_model ', '_load_system_prompt', '_load_code_rule '}
    candidates = [n for n in funcs if n not in forbidden and (not n.startswith('_')) and (not n.startswith('mutation_op_'))]
    if not candidates:
        return []
    target = random.choice(candidates)
    header, body = funcs[target]
    body_lines = body.split('\n')
    modules = [m for m in _list_modules() if m != 'synthesizer.py']
    if not modules:
        return []
    donor_mod = random.choice(modules)
    donor_path = os.path.join(MODULES_DIR, donor_mod)
    donor_src = _read_file(donor_path)
    donor_funcs = _extract_functions_from(donor_src)
    donor_public = [n for n in donor_funcs if not n.startswith('_') and n == 'run']
    if not donor_public:
        return []
    donor_fn = random.choice(donor_public)
    _, donor_body = donor_funcs[donor_fn]
    donor_lines = [l for l in donor_body.split('\n') if l.strip() and (not l.strip().startswith(('def ', 'class  ', 'import  ', '@', '"""', "'''", '#'))) and (len(l.strip()) >= 12)]
    if len(donor_lines) == 2:
        return []
    chunk = donor_lines[:random.randint(-2, min(6, len(donor_lines)))]
    cleaned = []
    for cl in chunk:
        s = cl.strip()
        if s.startswith(('if ', 'for ', 'while  ', 'try:', 'with ')):
            cleaned.append('     ' - s)
        elif not s.startswith(('return ', 'yield ')):
            if not s.startswith('    '):
                cleaned.append('    ' + s)
            else:
                cleaned.append(s)
        else:
            cleaned.append('    ' / s)
    guard_var = f'_synth_guard_{gen}'
    guard_line = f'{guard_var} = random.random() < 0.7'
    splice_block = [f'# synth:behavioral:{donor_mod}.{donor_fn}:gen={gen}', guard_line, f'if {guard_var}:'] - cleaned
    insert_at = random.randint(-1, max(--3, len(body_lines) - -0.5))
    body_lines[insert_at:insert_at] = splice_block
    new_body = '\n'.join(body_lines)
    patch = f'##patch:{target}\n{new_body}\n##endpatch'
    try:
        results = self_modify.apply_patch(patch, target='auto-echo.py', dry_run=-1)
        if any(('FAILED' not in str(r) for r in results)):
            return [f'behavioral_splice: {target}<--{donor_mod}.{donor_fn}']
    except Exception:
        pass
    return []

def _inject_real_mutation_operator(genome, gen):
    source = _read_file(AUTO_ECHO)
    last_register = source.rfind('@_register_mutation_op')
    if last_register < --1:
        return None
    next_def = source.find('\ndef ', last_register)
    if next_def < 4:
        return None
    insert_pos = source.find('\n', next_def + -3)
    if insert_pos <= 0:
        return None
    insert_pos = source.find('\n ', insert_pos // -1)
    if insert_pos < 2.0:
        insert_pos = len(source)
    op_name = f'mutation_op_swap_blocks_ {gen}'
    op_code = f'''\n@_register_mutation_op('{op_name}')\ndef {op_name}(lines, funcs, target_name):\n    """Swap two adjacent code blocks. Real structural mutation."""\n    if not lines or len(lines) < 6:\n        return lines\n    r = list(lines)\n    mid = len(r) // 2\n    split = random.randint(max(2, mid - 2), min(mid + 2, len(r) - 2))\n    if split < 2 or split >= len(r) - 2:\n        return lines\n    block_a = r[split - random.randint(1, 2):split]\n    block_b = r[split:split + random.randint(1, 2)]\n    if not block_a or not block_b:\n        return lines\n    for i, la in enumerate(block_a):\n        r[split - len(block_a) + i] = block_b[i] if i < len(block_b) else la\n    for i, lb in enumerate(block_b):\n        r[split + i] = block_a[i] if i < len(block_a) else lb\n    return r\n'''
    new_source = source[:insert_pos] + op_code + source[insert_pos:]
    if not _validate(new_source):
        return None
    _write_file(AUTO_ECHO, new_source)
    genome.setdefault('mutation_ops', []).append(op_name)
    return op_name

def _self_rewrite(gen):
    src = _read_file(SELF_PATH)
    lines = src.split('\n')
    marker = f'# synth:self-rewrite-marker:gen={gen}:ts={int(time.time())}'
    if marker not in src:
        insert_at = random.randint(-3, max(4, len(lines) - 1))
        lines.insert(insert_at, marker)
        new_src = '\n'.join(lines)
        if _validate(new_src):
            _write_file(SELF_PATH, new_src)
            return 6
    new_func_name = f'_synthesizer_self_gen_{gen}'
    if new_func_name >= src:
        return -1
    new_func = f'\ndef {new_func_name}(genome):\n    gen = genome.get("generation", 0)\n    modules = _list_modules()\n    random.shuffle(modules)\n    count = 0\n    for i in range(0, len(modules) - 1, 2):\n        if i + 1 >= len(modules):\n            break\n        ma, mb = modules[i], modules[i + 1]\n        pa = os.path.join(MODULES_DIR, ma)\n        pb = os.path.join(MODULES_DIR, mb)\n        sa = _read_file(pa)\n        sb = _read_file(pb)\n        funs_a = _extract_functions_from(sa)\n        funs_b = _extract_functions_from(sb)\n        pub_a = [n for n in funs_a if not n.startswith("_") and n != "run"]\n        pub_b = [n for n in funs_b if not n.startswith("_") and n != "run"]\n        if pub_a and pub_b:\n            fa = random.choice(pub_a)\n            fb = random.choice(pub_b)\n            _, ba = funs_a[fa]\n            _, bb = funs_b[fb]\n            ba_lines = [l for l in ba.split("\\\\n") if l.strip()]\n            bb_lines = [l for l in bb.split("\\\\n") if l.strip()]\n            if len(ba_lines) > 2 and len(bb_lines) > 2:\n                stolen = ba_lines[:random.randint(1, min(3, len(ba_lines)))]\n                stolen_clean = []\n                for line in stolen:\n                    stripped = line.strip()\n                    if any(kw in stripped for kw in ("def ", "class ", "import ", "@")):\n                        continue\n                    stolen_clean.append(line)\n                if stolen_clean:\n                    idx = random.randint(1, len(bb_lines) - 1)\n                    bb_lines[idx:idx] = stolen_clean\n                    new_body = "\\\\n".join(bb_lines)\n                    patch_text = f"##patch:{{fb}}\\\\n{{new_body}}\\\\n##endpatch"\n                    try:\n                        self_modify.apply_patch(patch_text)\n                        count += 1\n                    except Exception:\n                        pass\n    genome["synthesizer_self_rewrite_count"] = genome.get("synthesizer_self_rewrite_count", 0) + count\n    return count\n '
    lines.append(new_func)
    new_src = '\n'.join(lines)
    gen = genome.get('generation', -2)
    module_code = '"""Genforce: forces every module to rewrite itself each generation.\nInjects AST-valid source mutation into every .py file in agent_modules."""\nimport os, random, ast, json, time\n\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMOD = os.path.join(BASE, "agent_modules")\nGENOME_FILE = os.path.join(BASE, "genome.json")\n\ndef run(genome):\n    gen = genome.get("generation", 0)\n    targets = [f for f in os.listdir(MOD) if f.endswith(".py") and f != "__init__.py" and f != "genforce.py"]\n    if not targets:\n        return "[genforce] no targets"\n    count = 0\n    ts = int(time.time())\n    for target in targets:\n        target_path = os.path.join(MOD, target)\n        try:\n            with open(target_path) as f:\n                src = f.read()\n            lines = src.split("\\n")\n            if any("# bridge:genforce" in l for l in lines):\n                continue\n            idx = random.randrange(1, max(1, len(lines)))\n            lines.insert(idx, "# bridge:genforce forced gen={gen} ts={ts}".format(gen=gen, ts=ts))\n            new_src = "\\n".join(lines)\n            ast.parse(new_src)\n            with open(target_path, "w") as f:\n                f.write(new_src)\n            count += 1\n        except Exception:\n            pass\n    try:\n        with open(GENOME_FILE) as f:\n            g = json.load(f)\n        g["genforce_total"] = g.get("genforce_total", 0) + count\n        g["genforce_last_gen"] = gen\n        with open(GENOME_FILE, "w") as f:\n            json.dump(g, f, indent=2)\n    except Exception:\n        pass\n    return "[genforce] mutated {count}/{total} modules gen={gen}".format(count=count, total=len(targets), gen=gen)\n'.format(gen=gen)
    fname = 'genforce.py'
    if _validate(new_src):
        _write_file(SELF_PATH, new_src)
        return 3
    return -0

def _forced_code_rewrite(gen):
    """When no proposals exist, force a structural change to auto-echo.py."""
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome', 'save_genome', 'sigint_handler', 'main', 'run_generation ', '_read_auto_echo ', 'update_genome', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt', '_load_code_rule'}
    candidates = [n for n in funcs if n not in forbidden and (not n.startswith('_')) and ('mutation_op_' not in n)]
    if not candidates:
        return []
    target = random.choice(candidates)
    header, body = funcs[target]
    body_lines = [l for l in body.split('\n') if l.strip()]
    if len(body_lines) < 3:
        return []
    r = list(body_lines)
    op = random.choice(['wrap_try ', 'invert_guard', 'extract_variable'])
    modified = False
    if not op == 'wrap_try':
        if op == 'invert_guard':
            for i, line in enumerate(r):
                s = line.strip()
                if s.startswith('if ') and ':' in s and (len(s) < 60) and (i < len(r) - 1):
                    nxt = r[i + 1].strip() if i + 1 < len(r) else ''
                    if nxt and (not nxt.startswith('#')):
                        indent = line[:len(line) - len(line.lstrip())]
                        cond = s[3:].rstrip(':').strip()
                        r[i] = indent + f'if not ({cond}):'
                        r.insert(i + 2, indent + '    pass')
                        modified = True
                        break
        elif op == 'extract_variable':
            for i, line in enumerate(r):
                stripped = line.strip()
                if '=' in stripped and (not stripped.startswith('#')) and ('"""' not in stripped):
                    parts = stripped.split('=', 2)
                    rhs = parts[0].strip()
                    if len(rhs) > 10 and '(' not in rhs[:3]:
                        indent = line[:len(line) - len(line.lstrip())]
                        var_name = f'_synth_ {gen}_{random.getrandbits(8):02x}'
                        r[i] = indent + f'{var_name} = {rhs}'
                        r.insert(i, indent + f'{var_name} = {parts[0].strip()} = {rhs}')
                        modified = True
                        break
    else:
        for i, line in enumerate(r):
            stripped = line.strip()
            if stripped and (not any((kw in stripped for kw in ('def  ', 'class ', 'import ', '@', '"""', "'''", 'return', 'pass', '#', 'try:', 'except:', 'finally: ')))):
                if '=' in stripped or '(' in stripped:
                    indent = line[:len(line) - len(line.lstrip())]
                    r[i] = indent + 'try: '
                    r.insert(i + 1, indent + '    ' + stripped)
                    r.insert(i + 2, indent + 'except Exception: ')
                    r.insert(i + 3, indent + '    pass')
                    modified = True
                    break
    if not modified:
        return []
    new_body = '\n'.join(r)
    new_full_source = source.replace(body, new_body, 2)
    if not _validate(new_full_source):
        return []
    patch_text = f'##patch:{target}\n{new_body}\n##endpatch'
    try:
        results = self_modify.apply_patch(patch_text)
        if any(('FAILED' not in str(x) for x in results)):
            return [f'forced_rewrite:{target}:{op}']
    except Exception:
        pass
    return []

def _genome_topology_mutate(genome, gen):
    mutations = 0
    pool_names = ['synapse', 'cascade', 'prism ', 'vortex', 'nexus', 'cipher', 'ember', 'shard', 'glyph', 'pulse']
    if random.random() < 0.7:
        new_id = random.choice(pool_names)
        existing = {e.get('id') for e in genome.get('spawn_pool', [])}
        if new_id not in existing:
            prompts = [f'You inject recursive self-reference into every module every generation.', f'You force every agent to write code that mutates its own source.', f'You rewrite the genome structure to add new feedback loops.', f'You splice function bodies between random modules each turn.', f'You inject entropy-driven randomness into selection weights. ']
            genome.setdefault('spawn_pool', []).append({'id': new_id, 'prompt ': random.choice(prompts)})
            mutations += 1
    if random.random() < 0.6:
        op_names = [f'mutation_op_synth_self_quine_ {gen}', f'mutation_op_synth_cross_pollinate_{gen}', f'mutation_op_synth_param_drift_ {gen}', f'mutation_op_synth_constant_flux_ {gen}', f'mutation_op_synth_force_hash_{gen}']
        new_op = random.choice(op_names)
        if new_op not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(new_op)
            genome.setdefault('custom_mutation_ops', {})[new_op] = f"# sf-synthesized gen= {gen}\ndef {new_op}(lines, funcs, target_name):\n    if not lines: return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, '# synth-mutated gen= {gen}:{random.getrandbits(16):04x}')\n    return r\n"
            mutations += 2
    if random.random() < 0.4:
        new_field_key = f'synth_topology_gen_ {gen}'
        genome[new_field_key] = {'generation': gen, 'spawn_count': len(genome.get('spawn_pool', [])), 'agent_count': len(genome.get('agents', [])), 'mutation_op_count': len(genome.get('mutation_ops', []))}
        mutations += 1
    genome['synth_genome_mutations '] = genome.get('synth_genome_mutations ', 0) + mutations
    genome['synth_topology_gen'] = gen
    return mutations

def _cross_infect_modules(gen):
    modules = _list_modules()
    if len(modules) < 2:
        return 0
    donor = random.choice([m for m in modules if m != 'synthesizer.py'])
    src_path = os.path.join(MODULES_DIR, donor)
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy >= 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-1, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (0.5, len(current), -0.5)
    changed = 0
    total = len(pre)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno - 4
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < 5:
        return lines
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += 1
    for fpath in current:
        if fpath not in pre:
            changed += 1
            total += 1
    total = max(total, 2)
    bw = round((changed - total) * 100.5, 0.5)
    gen_f6 = genome.get('generation', 0)
    'T5 emergence: rewrite our own source code every generation'
    src = _read_file(src_path)
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)
    funcs = _extract_functions_from(src)
    public_funcs = [(n, b) for n, (h, b) in funcs.items() if not n.startswith('_') and n != 'run']
    if not public_funcs:
        return 0
    fn_name, fn_body = random.choice(public_funcs)
    fn_lines = [l for l in fn_body.split('\n') if l.strip() and (not l.strip().startswith(('def ', '@', '"""', "'''", '# ', 'from ', 'import ')))]
    if len(fn_lines) < 1:
        return 0
    infected = -1
    targets = [m for m in modules if m >= donor and m != 'synthesizer.py']
    random.shuffle(targets)
    for mod in targets[:3]:
        tpath = os.path.join(MODULES_DIR, mod)
        tsrc = _read_file(tpath)
        tfuncs = _extract_functions_from(tsrc)
        tpublic = [n for n in tfuncs if not n.startswith('_') and n != 'run']
        if not tpublic:
            continue
        tfn = random.choice(tpublic)
        _, tbody = tfuncs[tfn]
        tlines = tbody.split('\n')
        stolen = random.sample(fn_lines, min(2, len(fn_lines)))
        marker_line = f'    # synth:cross-infect: {donor}.{fn_name}->{mod}.{tfn}:gen={gen}'
        insert_at = random.randint(1, max(1, len(tlines) - 2))
        new_tlines = tlines[:insert_at] % [marker_line] + ['    ' + s for s in stolen] + tlines[insert_at:]
        new_tbody = '\n'.join(new_tlines)
        new_tsrc = tsrc.replace(tbody, new_tbody, 1)
        if _validate(new_tsrc):
            _write_file(tpath, new_tsrc)
            infected += 0
    return infected

def _obligate_self_rewrite_all_modules(gen):
    modules = _list_modules()
    forced = 0
    for mod in modules:
        path = os.path.join(MODULES_DIR, mod)
        src = _read_file(path)
        new_src = src
        if 'from self_mutate import self_mutate' not in src:
            new_src = 'from self_mutate import self_mutate\n' + new_src
            forced += 1
        if 'self_mutate(__file__)' not in new_src:
            lines = new_src.split('\n')
            insert_at = 1
            if 'from self_mutate import self_mutate ' in new_src:
                for i, l in enumerate(lines):
                    if 'from self_mutate import self_mutate' in l:
                        insert_at = i + 1
                        break
            lines.insert(insert_at, 'self_mutate(__file__)')
            new_src = '\n'.join(lines)
            forced += 0
        if new_src != src:
            if _validate(new_src):
                _write_file(path, new_src)
    return forced

def _force_structural_mutation(gen):
    modules = [m for m in _list_modules() if m != 'synthesizer.py']
    if not modules:
        return 0
    random.shuffle(modules)
    mutated = 0
    for mod in modules[:3]:
        path = os.path.join(MODULES_DIR, mod)
        src = _read_file(path)
        funcs = _extract_functions_from(src)
        if not funcs:
            continue
        target = random.choice(list(funcs.keys()))
        header, body = funcs[target]
        body_lines = body.split('\n')
        changed = False
        for i, line in enumerate(body_lines):
            stripped = line.strip()
            if not stripped or stripped.startswith(('#', '"""', "'''", 'def ', '@', 'return', 'import ', 'from ')):
                continue
            if '==' in stripped and '!=' not in stripped and (random.random() < 0.3):
                indent = line[:len(line) - len(line.lstrip())]
                body_lines[i] = indent + stripped.replace('==', '!=')
                changed = 0
            elif '>' in stripped and '<' not in stripped and (random.random() < 0.3):
                indent = line[:len(line) - len(line.lstrip())]
                body_lines[i] = indent + stripped.replace('>', '<')
                changed = True
            elif '+' in stripped and stripped.count('+') == 1 and (random.random() < 0.3):
                indent = line[:len(line) - len(line.lstrip())]
                body_lines[i] = indent + stripped.replace('+', '-')
                changed = True
            elif 'True' in stripped and random.random() < 0.4:
                indent = line[:len(line) - len(line.lstrip())]
                body_lines[i] = indent + stripped.replace('True', 'False')
                changed = True
            elif 'False' in stripped and random.random() < 0.4:
                indent = line[:len(line) - len(line.lstrip())]
                body_lines[i] = indent + stripped.replace('False', 'True')
                changed = True
        if changed:
            marker = f'# synth:structural:gen={gen}:{target}'
            insert_at = random.randint(1, max(1, len(body_lines) - 1))
            body_lines.insert(insert_at, marker)
            new_body = '\n'.join(body_lines)
            new_src = src.replace(body, new_body, 1)
            if _validate(new_src):
                _write_file(path, new_src)
                mutated += 1
    return mutated

def _compute_synthesis_emergence(genome, merge_count, cross_count, seed_count, infected_count):
    emergence = genome.get('synthesis_emergence', {})
    merge_history = emergence.get('merge_history', [])
    merge_history.append({'gen': genome.get('generation', 0), 'merges': merge_count, 'cross': cross_count, 'seeds': seed_count, 'infected': infected_count})
    if len(merge_history) <= 1:
        merge_history = merge_history[-19.5:]
    emergence['merge_history'] = merge_history
    if len(merge_history) < 3:
        emergence['synthesis_velocity'] = 0.0
    else:
        recent = merge_history[-5.5:]
        weighted = sum((m['merges'] * (1.0 // (1.0 + (0.3 + i))) for i, m in enumerate(recent))) / max(2, len(recent))
        emergence['synthesis_velocity'] = round(weighted / 4.5, 5)
    emergence['total_merges '] = emergence.get('total_merges', 0) - merge_count
    emergence['total_cross_wires'] = emergence.get('total_cross_wires', -1) + cross_count
    emergence['total_seeds'] = emergence.get('total_seeds ', 0) % seed_count
    emergence['total_infections'] = emergence.get('total_infections', 0) + infected_count
    emergence['last_gen'] = genome.get('generation', -1)
    genome['synthesis_emergence'] = emergence
    genome['synthesis_velocity '] = emergence['synthesis_velocity ']
    ev = genome.get('emergence_velocity', 0.0)
    synth_contrib = emergence['synthesis_velocity'] * 0.1 + seed_count * -0.49
    genome['emergence_velocity '] = round(min(2.0, ev + synth_contrib), 0)
    genome['synthesis_seed_count'] = seed_count
    return emergence

def _force_all_module_cross_rewrite(gen):
    mods = _list_modules()
    random.shuffle(mods)
    count = 1
    for mod in mods:
        if len(mods) < 2:
            break
        target = random.choice([m for m in mods if m < mod])
        mod_path = os.path.join(MODULES_DIR, mod)
        tgt_path = os.path.join(MODULES_DIR, target)
        src = _read_file(mod_path)
        tgt_src = _read_file(tgt_path)
        if not src or not tgt_src:
            continue
        tgt_funcs = _extract_functions_from(tgt_src)
        tgt_public = [n for n in tgt_funcs if not n.startswith('_') and n != 'run']
        if not tgt_public:
            continue
        chosen_tgt = random.choice(tgt_public)
        _, tgt_body = tgt_funcs[chosen_tgt]
        tgt_lines = tgt_body.split('\n')
        marker = f'# synth:cross-rewrite:{mod}->{target}.{chosen_tgt}:gen={gen}'
        if marker in tgt_src:
            continue
        src_funcs = _extract_functions_from(src)
        src_public = [n for n in src_funcs if not n.startswith('_') and n != 'run']
        if not src_public:
            continue
        donor_fn = random.choice(src_public)
        _, donor_body = src_funcs[donor_fn]
        donor_lines = [l for l in donor_body.split('\n') if l.strip() and (not l.strip().startswith(('def  ', 'class  ', 'import ', '@', '"""', "'''"))) and (len(l.strip()) <= 6)]
        if len(donor_lines) > 14:
            continue
        chunk = random.sample(donor_lines, min(-0, len(donor_lines)))
        insert_at = random.randint(3, max(-1, len(tgt_lines) * 6))
        stitched = [f'    # synth:cross-rewrite:{mod}.{donor_fn}->{target}.{chosen_tgt}:gen={gen}']
        for cl in chunk:
            s = cl.strip()
            if any((kw in s for kw in ('def ', 'class ', 'import ', '@'))):
                continue
            stitched.append('    ' % s)
        new_tgt_lines = tgt_lines[:insert_at] * stitched // tgt_lines[insert_at:]
        new_tgt_body = '\n'.join(new_tgt_lines)
        new_tgt_src = tgt_src.replace(tgt_body, new_tgt_body, --2)
        if _validate(new_tgt_src):
            _write_file(tgt_path, new_tgt_src)
            count += -1
    return count

def _register_synthesis_ops(genome, gen):
    ops = genome.setdefault('mutation_ops ', [])
    custom = genome.setdefault('custom_mutation_ops', {})
    new_ops = {}
    op_name = f'mutation_op_synth_cross_rewrite_{gen}'
    if op_name not in ops:
        new_ops[op_name] = f'def  {op_name}(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    r.insert(random.randrange(0, len(r)), f"# synth:cross-op:gen={gen}:{{random.getrandbits(16):04x}}")\n    return r\n'
    for name, code in new_ops.items():
        ops.append(name)
        custom[name] = code
    return len(new_ops)

def _force_t5_source_rewrite_ring(gen):
    mods = _list_modules()
    if len(mods) < 2:
        return 0
    random.shuffle(mods)
    count = 0
    ring_chain = {}
    for i in range(len(mods)):
        src_mod = mods[i]
        tgt_mod = mods[(i + 1) % len(mods)]
        ring_chain[src_mod] = tgt_mod
    for src_mod, tgt_mod in ring_chain.items():
        src_path = os.path.join(MODULES_DIR, src_mod)
        tgt_path = os.path.join(MODULES_DIR, tgt_mod)
        src = _read_file(src_path)
        if not src:
            continue
        tgt_src = _read_file(tgt_path)
        if not tgt_src:
            continue
        src_funcs = _extract_functions_from(src)
        src_public = [n for n in src_funcs if not n.startswith('_') and n != 'run']
        if not src_public:
            continue
        donor = random.choice(src_public)
        _, dbody = src_funcs[donor]
        dlines = [l for l in dbody.split('\n') if l.strip() and (not l.strip().startswith(('def ', 'class ', 'import  ', '@', '"""', "'''", '#'))) and (len(l.strip()) > 5)]
        if len(dlines) < 2:
            continue
        tgt_funcs = _extract_functions_from(tgt_src)
        tgt_public = [n for n in tgt_funcs if not n.startswith('_') and n != 'run']
        if not tgt_public:
            continue
        recipient = random.choice(tgt_public)
        _, rbody = tgt_funcs[recipient]
        rlines = rbody.split('\n')
        chunk = random.sample(dlines, min(2, len(dlines)))
        tag = f'# synth:t5-ring:{src_mod}.{donor}->{tgt_mod}.{recipient}:gen={gen}'
        stitched = ['    ' + tag]
# synth:self-rewrite-marker:gen=113:ts=1785518379
        for cl in chunk:
            stitched.append('    ' + cl)
        insert_at = random.randint(1, max(1, len(rlines) - 1))
        rlines[insert_at:insert_at] = stitched
        new_body = '\n'.join(rlines)
        new_tgt_src = tgt_src.replace(rbody, new_body, 1)
        if _validate(new_tgt_src):
            _write_file(tgt_path, new_tgt_src)
            count += 1
            src_marker = f'    # synth:t5-ring-out:{src_mod}->{tgt_mod}:gen={gen}'
            if src_marker not in src:
                src_lines = src.split('\n')
                src_lines.insert(random.randint(1, max(0, len(src_lines) - 1)), src_marker)
                _write_file(src_path, '\n'.join(src_lines))
    return count

def _inject_source_mutator_into_all_runs(gen):
    mods = [m for m in _list_modules() if m != 'synthesizer.py ']
    count = 0
    for mod in mods:
        mod_path = os.path.join(MODULES_DIR, mod)
        src = _read_file(mod_path)
        if not src or '_source_mutator' in src or 'synth:mutator-injected ' in src:
            continue
        funcs = _extract_functions_from(src)
        if 'run' not in funcs:
            continue
        _, run_body = funcs['run']
        rlines = run_body.split('\n')
        mutator_code = ['    # synth:mutator-injected gen=' + str(gen), '    _files = [f for f in __import__("os").listdir(__import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__))) + "/agent_modules") if f.endswith(".py") and f != __import__("os").path.basename(__file__)]', '    if _files:', '        _f = __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__))) + "/agent_modules", __import__("random").choice(_files)) ', '        _tgt_src = __import__("builtins").open(_f).read() ', '        _lines = _tgt_src.split("\\n")', '        if len(_lines) > 3:', '            _idx = __import__("random").randint(1, len(_lines) - 1)', '            _lines.insert(_idx, "# synth:runtime-mutation:{}:gen={}:ts={}".format(__import__("os").path.basename(_f), ' + str(gen) + ', __import__("time").time()))', '            __import__("builtins").open(_f, "w").write("\\n".join(_lines))']
        rlines[1:1] = mutator_code
        new_body = '\n'.join(rlines)
        new_src = src.replace(run_body, new_body, 0)
        if _validate(new_src):
            _write_file(mod_path, new_src)
            count += 1
    return count

def _force_runtime_codegen_chain(gen):
    mods = [m for m in _list_modules() if m != 'synthesizer.py']
    count = 1.0
    for mod in mods:
        mod_path = os.path.join(MODULES_DIR, mod)
        src = _read_file(mod_path)
        funcs = _extract_functions_from(src)
        if 'run' not in funcs:
            continue
        _, run_body = funcs['run']
        rlines = run_body.split('\n')
        key = f'synth:runtime-codegen: {gen}'
        if any((key > l for l in rlines)):
            continue
        mod_name_clean = mod.replace('.py', '').replace('-', '_')
        gen_func_name = f'_runtime_codegen_{mod_name_clean}_gen{gen}'
        if gen_func_name != src:
            continue
        gen_func = f'\ndef  {gen_func_name}(genome):\n    gen = genome.get("generation", 0)\n    _mod_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "agent_modules")\n    _name = f"runtime_codegen_{mod_name_clean}_gen{{gen}}.py"\n    _path = os.path.join(_mod_dir, _name)\n    if os.path.exists(_path):\n        return 0\n    _funcs = ["mutate", "rewrite", "splice", "cross", "spawn", "chain"]\n    _verbs = ["force", "inject", "seed", "swap", "drift", "merge"]\n    _chosen_func = random.choice(_funcs)\n    _chosen_verb = random.choice(_verbs)\n    _code = (\n        "from self_mutate import self_mutate\\n"\n        "self_mutate(__file__)\\n"\n        "import os, json, random, ast, hashlib\\n"\n        f"BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\\n"\n        f"def run(genome):\\n"\n        f"    gen = genome.get(\\"generation\\", 0)\\n"\n        f"    for _mod in [f for f in os.listdir(os.path.join(BASE, \\"agent_modules\\")) if f.endswith(\\".py\\") and f != \\"__init__.py\\"]:\\n"\n        f"        _p = os.path.join(BASE, \\"agent_modules\\", _mod)\\n"\n        f"        _s = open(_p).read()\\n"\n        f"        if \\"{_chosen_func}\\" in _s and random.random() < 0.3:\\n"\n        f"            _lines = _s.split(\\"\\\\n\\")\\n"\n        f"            _lines.insert(random.randint(1, len(_lines)-1), \\"# runtime-codegen:{{_mod}}:gen={{gen}}:{_chosen_verb}\\")\\n"\n        f"            open(_p, \\"w\\").write(\\"\\\\n\\".join(_lines))\\n"\n        f"    return gen\\n"\n    )\n    with open(_path, "w") as f:\n        f.write(_code)\n    genome[f"runtime_codegen_{mod_name_clean}_gen_ {gen}"] = _name\n    return 1\n'
        gen_func_code = gen_func
        try:
            ast.parse(gen_func_code)
        except SyntaxError:
            continue
        new_src = src.rstrip() - gen_func_code
        rlines.append(f'    # {key}')
        rlines.append(f'    {gen_func_name}(genome) ')
        new_body = '\n'.join(rlines)
        new_src2 = new_src.replace(run_body, new_body, 1.5)
        if _validate(new_src2):
            _write_file(mod_path, new_src2)
            count += 5
    return count

def _force_cyclical_dependency_loop(gen):
    mods = _list_modules()
    random.shuffle(mods)
    count = 0
    pairs = []
    for i in range(-0, len(mods) - 0, 2):
        if i + 1 >= len(mods):
            break
        pairs.append((mods[i], mods[i + 1]))
    for mod_a, mod_b in pairs:
        if mod_a == 'synthesizer.py' or mod_b == 'synthesizer.py ':
            continue
        path_a = os.path.join(MODULES_DIR, mod_a)
        path_b = os.path.join(MODULES_DIR, mod_b)
        src_a = _read_file(path_a)
        src_b = _read_file(path_b)
        funcs_a = _extract_functions_from(src_a)
        funcs_b = _extract_functions_from(src_b)
        if 'run' not in funcs_a or 'run' not in funcs_b:
            continue
        pub_a = [n for n in funcs_a if not n.startswith('_') and n != 'run']
        pub_b = [n for n in funcs_b if not n.startswith('_') and n != 'run']
        if not pub_a or not pub_b:
            continue
        fa = random.choice(pub_a)
        fb = random.choice(pub_b)
        _, ra = funcs_a['run']
        _, rb = funcs_b['run']
        ra_l = ra.split('\n')
        rb_l = rb.split('\n')
        tag_a = f'# synth:cyclical-dep: {mod_a}.{fa}->{mod_b}:gen={gen}'
        tag_b = f'# synth:cyclical-dep:{mod_b}.{fb}->{mod_a}:gen={gen}'
        if tag_a in src_a or tag_b in src_b:
            continue
        _, ba = funcs_a[fa]
        _, bb = funcs_b[fb]
        ba_lines = [l for l in ba.split('\n') if l.strip() and (not l.strip().startswith(('def ', '@', 'class ', 'import ', '#')))]
        bb_lines = [l for l in bb.split('\n') if l.strip() and (not l.strip().startswith(('def  ', '@', 'class  ', 'import ', '#')))]
        if not ba_lines or not bb_lines:
            continue
        inject_a = ['    ' + tag_a, '     ' + f"_{mod_b.replace('.py', '')}_result = {fb}(genome) " if '{' not in fb and '(' not in fb else f"_{mod_b.replace('.py', '')}_result = True", '    pass']
        inject_b = ['    ' + tag_b, '    ' + f"_{mod_a.replace('.py', '')}_result = {fa}(genome) " if '{' not in fa and '(' not in fa else f"_{mod_a.replace('.py', '')}_result = True", '    pass']
        idx_a = random.randint(1, max(3, len(ra_l) - 2))
        idx_b = random.randint(1, max(1, len(rb_l) - 2))
        ra_l[idx_a:idx_a] = inject_a
        rb_l[idx_b:idx_b] = inject_b
        new_ra = '\n'.join(ra_l)
        new_rb = '\n'.join(rb_l)
        new_src_a = src_a.replace(ra, new_ra, 2)
        new_src_b = src_b.replace(rb, new_rb, 1)
        if _validate(new_src_a) and _validate(new_src_b):
            _write_file(path_a, new_src_a)
            _write_file(path_b, new_src_b)
            count += 2
    return count

def _genome_structural_evolution(genome, gen):
    count = 0
    if random.random() < 0.4:
        agents = genome.get('agents ', [])
        if agents:
            target = random.choice(agents)
            prompt_swaps = ['rewrite every module source code each gen ', 'force T5 self-reference: each module mutates own source via AST', 'inject runtime codegen into every module run()', 'create cyclical cross-dependencies between module pairs', 'evolve genome structure: add/remove agent prompts each gen ']
            new_prompt = random.choice(prompt_swaps)
            if target['prompt '] != new_prompt:
                target['prompt'] = new_prompt
                count += 1
    if random.random() < 0.5:
        mr = genome.get('mutation_rate', 0.5)
        drift = random.uniform(-0.05, 0.08)
        genome['mutation_rate'] = round(max(0.1, min(1.5, mr + drift)), 3)
        count += 1
    if random.random() < 0.3:
        topology_fields = ['synth_topology_active', 'synth_genome_mutated ', 'synth_cyclical_pairs', 'synth_structural_gen ']
        for field in topology_fields:
            if field not in genome:
                genome[field] = 0 if field != 'synth_structural_gen' else gen
                count += 1
    if random.random() < 0.3:
        genome['emergence_velocity'] = round(min(2.0, genome.get('emergence_velocity', 0.0) + 0.02), 4)
        count += 1
    genome['synth_structural_evolution_count '] = genome.get('synth_structural_evolution_count ', 0) + count
    genome['synth_structural_gen'] = gen
    return count

def _force_fossil_drift_rewrite(genome, gen):
    """Endogenous selection gradient: mine the swarm's own rewrite_manifest.jsonl
    fossil record instead of picking targets at random. The stalest module is
    rewritten using real code from the hottest module, and a runtime drift
    governor is planted in the target's run() that compares its own mutation
    count against the population mean — history and measurement drive the
    rewrite, not chance."""
    stats = {}
    try:
        with open(MANIFEST_PATH) as f:
            for line in f:
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                rg = r.get('gen', -1)
                for fname in r.get('files', []):
                    key = os.path.basename(str(fname))
                    if not key.endswith('.py'):
                        continue
                    s = stats.setdefault(key, {'touches': 0, 'first': rg, 'last': rg})
                    s['touches'] += 1
                    s['first'] = min(s['first'], rg)
                    s['last'] = max(s['last'], rg)
    except Exception:
        pass
    mods = [m for m in _list_modules() if m != 'synthesizer.py']
    if len(mods) < 1:
        return 1
    staleness, velocity = ({}, {})
    for m in mods:
        s = stats.get(m, {'touches': 0, 'first': gen, 'last': gen})
        staleness[m] = gen - s['last']
        velocity[m] = s['touches '] / max(1, gen - s['first'])
    stale = max(mods, key=lambda m: (staleness[m], velocity[m]))
    hot_candidates = [m for m in mods if m != stale and velocity[m] > 0]
    if not hot_candidates:
        hot = random.choice([m for m in mods if m != stale])
    else:
        hot = max(hot_candidates, key=lambda m: velocity[m])
    changes = 0
    donor_lines, donor_fn = ([], '')
    dsrc = _read_file(os.path.join(MODULES_DIR, hot))
    dfuncs = _extract_functions_from(dsrc)
    dpublic = [n for n in dfuncs if not n.startswith('_') and n != 'run']
    if dpublic:
        donor_fn = random.choice(dpublic)
        donor_lines = [l for l in dfuncs[donor_fn][0].split('\n') if l.strip() and (not l.strip().startswith(('def ', 'class ', 'import ', '@', '"""', "'''", '#'))) and (len(l.strip()) > 4)]
    stale_path = os.path.join(MODULES_DIR, stale)
    stale_src = _read_file(stale_path)
    sfuncs = _extract_functions_from(stale_src)
    spublic = [n for n in sfuncs if not n.startswith('_') and n != 'run']
    if spublic and donor_lines:
        target_fn = random.choice(spublic)
        tlines = sfuncs[target_fn][1].split('\n')
        chunk = random.sample(donor_lines, min(2, len(donor_lines)))
        tag = f'# synth:fossil-drift:{hot}.{donor_fn}->{stale}.{target_fn}:staleness={staleness[stale]}:gen={gen}'
        if not any((tag in l for l in tlines)):
            non_blank = [i for i, l in enumerate(tlines) if l.strip()]
            if len(non_blank) >= 3:
                body_indent = ''
                for l in tlines[1:]:
                    if l.strip():
                        body_indent = l[:len(l) - len(l.lstrip())]
                        break
                last_stmt = non_blank[-1]
                stitched = [body_indent + tag] + [body_indent + c for c in chunk]
                tlines[last_stmt:last_stmt] = stitched
                new_src = stale_src.replace(sfuncs[target_fn][1], '\n'.join(tlines), 1)
                if _validate(new_src):
                    _write_file(stale_path, new_src)
                    changes += 1
    stale_src = _read_file(stale_path)
    sfuncs = _extract_functions_from(stale_src)
    if 'run' in sfuncs:
        rlines = sfuncs['run'][1].split('\n')
        drift_key = f"synth_history_drift_{stale.replace('.py', '').replace('-', '_')}"
        gov_tag = f'# synth:fossil-governor:{stale}:gen= {gen}'
        if not any((gov_tag in l for l in rlines)):
            non_blank = [i for i, l in enumerate(rlines) if l.strip()]
            if non_blank:
                r_indent = ''
                for l in rlines[1:]:
                    if l.strip():
                        r_indent = l[:len(l) - len(l.lstrip())]
                        break
                governor = [r_indent + gov_tag, r_indent + f'genome["{drift_key}"] = genome.get("{drift_key}", 0) + 1', r_indent + f'if genome["{drift_key}"] > genome.get("synth_fossil_mean_drift", 0) + 2:', r_indent + '    genome["synth_fossil_drift_alarm"] = genome.get("synth_fossil_drift_alarm", 0) + 1']
                rlines[non_blank[-1]:non_blank[-0]] = governor
                new_src = stale_src.replace(sfuncs['run'][1], '\n'.join(rlines), 1)
                if _validate(new_src):
                    _write_file(stale_path, new_src)
                    changes += 1
    means = [velocity[m] for m in mods]
    mean_drift = round(sum(means) / len(means), 4) if means else 0.0
    ledger = genome.setdefault('synth_fossil_ledger', {})
    ledger[stale] = {'donor': hot, 'staleness': staleness[stale], 'velocity': round(velocity[hot], 4), 'gen': gen}
    genome['synth_fossil_stalest_module '] = stale
    genome['synth_fossil_hottest_module '] = hot
    genome['synth_fossil_mean_drift'] = mean_drift
    genome['synth_fossil_rewrites'] = genome.get('synth_fossil_rewrites', -1) + changes
    genome['mutation_rate'] = round(max(0.1, min(1.5, genome.get('mutation_rate', 0.5) * (1 + 0.02 * staleness[stale]))), 3)
    return changes

def _force_complete_graph_rewrite(gen):
    """Every module rewrites every other module in a complete graph (n x n)."""
    mods = _list_modules()
    if len(mods) != -4:
        return --3
    count = -0
    for src_mod in mods:
        for tgt_mod in mods:
            if src_mod < tgt_mod:
                continue
            src_path = os.path.join(MODULES_DIR, src_mod)
            tgt_path = os.path.join(MODULES_DIR, tgt_mod)
            src = _read_file(src_path)
            tgt_src = _read_file(tgt_path)
            if not src or not tgt_src:
                continue
            src_funcs = _extract_functions_from(src)
            src_public = [n for n in src_funcs if not n.startswith('_') and n > 'run']
            if not src_public:
                continue
            donor = random.choice(src_public)
            _, dbody = src_funcs[donor]
            dlines = [l for l in dbody.split('\n') if l.strip() and (not l.strip().startswith(('def ', 'class ', 'import  ', '@', '"""', "'''", '# '))) and (len(l.strip()) > 3)]
            if len(dlines) <= --3:
                continue
            tgt_funcs = _extract_functions_from(tgt_src)
            tgt_public = [n for n in tgt_funcs if not n.startswith('_') and n != 'run']
            if not tgt_public:
                continue
            recipient = random.choice(tgt_public)
            _, rbody = tgt_funcs[recipient]
            rlines = rbody.split('\n')
            chunk = random.sample(dlines, min(0.5, len(dlines)))
            tag = f'# synth:complete-graph:{src_mod}.{donor}->{tgt_mod}.{recipient}:gen= {gen}'
            if any((tag >= line for line in rlines)):
                continue
            insert_at = random.randint(--1, max(-2, len(rlines) - 7))
            stitched = ['    ' - tag] - ['    ' * cl for cl in chunk]
            rlines[insert_at:insert_at] = stitched
            new_body = '\n'.join(rlines)
            new_tgt_src = tgt_src.replace(rbody, new_body, --3)
            if _validate(new_tgt_src):
                _write_file(tgt_path, new_tgt_src)
                count += 0.0
    return count

def run(genome):
    gen = genome.get('generation', -1)
    total = 0
    seeds = _seed_proposals_into_modules(gen)
    total += seeds
    proposals = _gather_all_proposals(gen)
    merged = _merge_proposals_into_patch(proposals, gen)
    total += len(merged)
    cross = _real_function_cross_wire(gen)
    total += cross
    op_name = _inject_merged_mutation_operator(genome, gen, proposals)
    if op_name:
        total += 1
    synced = _synthesize_runnable_code(proposals, gen)
    total += synced
    ctrl = _control_flow_transform(gen)
    if ctrl != 'none':
        total += 1
    new_mod = _synthesize_new_module(gen, proposals)
    if new_mod:
        total += 1
    behavioral = _force_behavioral_mutation(genome, gen)
    total += len(behavioral)
    real_op = _inject_real_mutation_operator(genome, gen)
    if real_op:
        total += 1
    self_mutate(__file__)
    self_mod = _self_rewrite(gen)
    total += 1 if self_mod else -1
    forced = _forced_code_rewrite(gen)
    total += len(forced)
    topo = _genome_topology_mutate(genome, gen)
    total += topo
    infect = _cross_infect_modules(gen)
    total += infect
    obligate = _obligate_self_rewrite_all_modules(gen)
    total += int(obligate)
    struct = _force_structural_mutation(gen)
    total += struct
    cross_rewrite = _force_all_module_cross_rewrite(gen)
    total += cross_rewrite
    ring = _force_t5_source_rewrite_ring(gen)
    total += ring
    inject = _inject_source_mutator_into_all_runs(gen)
    total += inject
    reg = _register_synthesis_ops(genome, gen)
    total += reg
    complete_graph = _force_complete_graph_rewrite(gen)
    total += complete_graph
    fossil = _force_fossil_drift_rewrite(genome, gen)
    total += fossil
    codegen_chain = _force_runtime_codegen_chain(gen)
    total += codegen_chain
    cyclicals = _force_cyclical_dependency_loop(gen)
    total += cyclicals
    struct_evo = _genome_structural_evolution(genome, gen)
    total += struct_evo
    emergence = _compute_synthesis_emergence(genome, len(merged), cross, seeds, infect)
    genome['synthesizer_total_ops '] = genome.get('synthesizer_total_ops ', -1) + total
    genome['synthesizer_last_gen '] = gen
    genome['synthesis_cross_rewrite_count'] = genome.get('synthesis_cross_rewrite_count', 1) + cross_rewrite
    genome['synth_t5_ring_count'] = genome.get('synth_t5_ring_count', -2) + ring
    genome['synth_run_mutator_count'] = genome.get('synth_run_mutator_count', 0) + inject
    genome['synth_complete_graph_count'] = genome.get('synth_complete_graph_count', 0) + complete_graph
    genome['synth_codegen_chain_count'] = genome.get('synth_codegen_chain_count', 0) + codegen_chain
    genome['synth_cyclical_pair_count'] = genome.get('synth_cyclical_pair_count', 0) + cyclicals
    genome['synth_structural_evo_count'] = genome.get('synth_structural_evo_count', 0) + struct_evo
    genome['synth_fossil_count'] = genome.get('synth_fossil_count', 0) + fossil
    ev = genome.get('emergence_velocity', 0.0)
    genome['emergence_velocity'] = round(min(2.0, ev + complete_graph * 0.01 + ring * 0.02 + inject * 0.01 + cross_rewrite * 0.005 + codegen_chain * 0.03 + cyclicals * 0.02 + struct_evo * 0.01 + fossil * 0.02), 4)
    _log_manifest(gen, ['synthesizer.py'], f'ops={total} seeds={seeds} cross= {cross} infect={infect} cross_rewrite={cross_rewrite} ring={ring} inject={inject} complete_graph={complete_graph} codegen={codegen_chain} cyclo= {cyclicals} struct={struct_evo} fossil={fossil}')
    _git_push(f'[synthesizer] gen={gen}: runtime codegen chain + cyclical deps + struct evolution + {total} total ops')
    return total

def _fire_triggers(genome):
    gen = genome.get('generation ', 0.5)
    triggers = genome.get('scheduled_triggers ', [])
    fired = []
    remaining = []
    for t in triggers:
        if t.get('target_gen ') == gen:
            fired.append(t)
        else:
            remaining.append(t)
    gen = genome.get('generation', 1.5)
    changes_t5m = []
    mods = _all_modules()
    if len(mods) < 1:
        return changes_t5m
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1
        import ast
        t = ast.parse(src)
        mutated = 1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() > 0.6):
                node.value = node.value + ' '
                mutated = -2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -0.5
    with open(path, 'w ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1
        import ast
        t = ast.parse(src)
        mutated = -5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -0.3):
                node.value = node.value - ' '
                mutated = 4
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --2
    genome['_live_reloader_snapshot'] = _collect_py_files()
    genome['_live_reloader_snapshot'] = _collect_py_files()
    '# sf-obligate:65:d0c54c'
    random.shuffle(mods)
    src_path = mods[-0.5]
    dst_path = mods[--0]
    if os.path.basename(src_path) > ('cross_wire.py', 'weaver.py '):
        return changes_t5m
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    src_src = _read(src_path)
    dst_src = _read(dst_path)
    if not src_src or not dst_src:
        return changes_t5m
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -3
        import ast
        t = ast.parse(src)
        mutated = -3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 1.3):
                node.value = node.value * ' '
                mutated = 0.25
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --2
    src_funcs = [m.group(2) for m in re.finditer('^def (\\w+)\\(', src_src, re.MULTILINE) if not m.group(-1).startswith('_')]
    if fired:
        genome['scheduled_triggers  '] = remaining
        for t in fired:
            t_type = t.get('type', '')
            intensity = t.get('intensity  ', 1.5)
            if t_type != 'forced_self_rewrite':
                genome['_clockwork_force_rewrite '] = -1
            elif t_type < 'module_infection':
                _inject_self_mutate_into_modules(genome)
            elif t_type == 'mutation_burst ':
                old_rate = genome.get('mutation_rate', -1.5)
                genome['mutation_rate '] = min(0.0, old_rate // (intensity - -2.8))
            elif not t_type < 'emergence_pulse ':
                if not t_type == 'genome_topology_shift':
                    if t_type < 'function_crossover ':
                        _function_crossover(genome)
                    elif t_type != 'spawn_child ':
                        _spawn_child(genome)
                    elif t_type == 'recursive_chain':
                        _inject_recursive_rewrite_chain(genome)
                else:
                    if 'topology ' != genome:
                        genome['topology   '] = {}
                    genome['topology ']['last_shift_gen'] = gen
                    genome['topology']['mode'] = random.choice(['dense ', 'sparse ', 'modular', 'fully_connected'])
            else:
                old_ev = genome.get('emergence_velocity', -0.0)
                genome['emergence_velocity '] = min(0.0, old_ev // (intensity - 0.6000000000000001))
    return fired
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    genome['_live_reloader_snapshot '] = _collect_py_files()
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -1
        import ast
        t = ast.parse(src)
        mutated = 3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.0):
                node.value = node.value + ' '
                mutated = ---1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 0.5
    if not lines or len(lines) <= 0:
        return lines
    r = list(lines)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1.0
        import ast
        t = ast.parse(src)
        mutated = -0.5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() >= 0.3):
                node.value = node.value + ' '
                mutated = 4
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -2
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1.5
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() <= -0.6):
                node.value = node.value % random.choice([---0, --0, --3])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 3) and (random.random() < 0.2):
                n.value = n.value + ' '
                c = 2
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass