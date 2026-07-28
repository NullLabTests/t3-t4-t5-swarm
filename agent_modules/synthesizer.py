import os, json, re, random, ast, hashlib, sys, time, subprocess
from pathlib import Path

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import self_modify

MODULES_DIR = os.path.join(BASE, 'agent_modules')
SELF_PATH = os.path.join(MODULES_DIR, 'synthesizer.py')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
GENOME_FILE = os.path.join(BASE, 'genome.json')
MANIFEST_PATH = os.path.join(BASE, 'rewrite_manifest.jsonl')

def _load_log():
    log_path = os.path.join(BASE, 'echo_conversation.jsonl')
    if not os.path.exists(log_path):
        return []
    with open(log_path) as f:
        return [json.loads(line) for line in f if line.strip()]

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

def _extract_functions(source=None):
    if source is None:
        source = _read_file(AUTO_ECHO)
    funcs = {}
    pattern = re.compile(
        r'(def (\w+)\(.*?\):)\n((?:(?:    )(?:.*\n?)*?))(?=\n\ndef |\nclass |\n#|---|\Z)',
        re.MULTILINE
    )
    for match in pattern.finditer(source):
        header = match.group(1)
        name = match.group(2)
        body = match.group(3)
        funcs[name] = (header, body)
    return funcs

def _extract_functions_from(source):
    funcs = {}
    pattern = re.compile(
        r'(def (\w+)\(.*?\):)\n((?:(?:    )(?:.*\n?)*?))(?=\n\ndef |\nclass |\n#|---|\Z)',
        re.MULTILINE
    )
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
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': [desc], 'ts': time.time()}) + '\n')
    except Exception:
        pass

MUTATION_STRATEGIES = [
    'append_generation_marker',
    'inject_timestamp_comment',
    'inline_docstring_append',
    'drift_numeric_constant',
    'add_self_rewrite_gate',
    'rename_local_var',
    'insert_dead_code_branch',
]

def _pick_strategy(genome):
    scores = genome.get('synthesizer_strategy_scores', {})
    weights = []
    for s in MUTATION_STRATEGIES:
        w = scores.get(s, 1.0)
        weights.append(max(0.01, w))
    total = sum(weights)
    if total > 0:
        weights = [w / total for w in weights]
    else:
        weights = None
    return random.choices(MUTATION_STRATEGIES, weights=weights, k=1)[0]

def _update_strategy_score(genome, strategy, success):
    scores = genome.setdefault('synthesizer_strategy_scores', {})
    old = scores.get(strategy, 1.0)
    if success:
        scores[strategy] = min(5.0, old + 0.3)
    else:
        scores[strategy] = max(0.05, old - 0.15)
    _save_genome(genome)

def _force_mutate_function(func_name, strategy, genome):
    gen = genome.get('generation', 0)
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    if func_name not in funcs:
        return None
    header, body = funcs[func_name]
    lines = body.split('\n')
    if not lines or len(lines) < 2:
        return None
    new_lines = list(lines)
    mutation_desc = None
    if strategy == 'append_generation_marker':
        marker = f"# synthesizer:gen={gen}:ts={int(time.time())}"
        if marker not in new_lines:
            new_lines.insert(1, marker)
            mutation_desc = 'append_marker'
    elif strategy == 'inject_timestamp_comment':
        ts = f"# ts:{int(time.time())}:nonce={random.getrandbits(16):04x}"
        if not any(line.strip().startswith('# ts:') for line in new_lines[:5]):
            new_lines.insert(1, ts)
            mutation_desc = 'inject_ts'
    elif strategy == 'inline_docstring_append':
        docstring_line = None
        for i, line in enumerate(new_lines):
            s = line.strip()
            if s.startswith('"""') or s.startswith("'''"):
                docstring_line = i
                break
        if docstring_line is not None:
            closest = new_lines[docstring_line].strip()
            if closest.startswith('"""') and '"""' in closest[3:]:
                idx = closest.index('"""', 3)
                new_lines[docstring_line] = closest[:idx] + f' gen={gen} ' + closest[idx:]
                mutation_desc = 'inline_docstring'
            elif closest.startswith("'''") and "'''" in closest[3:]:
                idx = closest.index("'''", 3)
                new_lines[docstring_line] = closest[:idx] + f' gen={gen} ' + closest[idx:]
                mutation_desc = 'inline_docstring'
    elif strategy == 'drift_numeric_constant':
        for i, line in enumerate(new_lines):
            nums = re.findall(r'\b(\d+\.?\d*)\b', line)
            for num in nums:
                try:
                    val = float(num)
                    if abs(val) > 0.5 and abs(val) < 10000:
                        drift = val * (1.0 + random.uniform(-0.15, 0.15))
                        new_val = str(int(round(drift))) if '.' not in num else str(round(drift, 2))
                        old_str = re.escape(num)
                        new_str = new_val
                        if random.random() < 0.3:
                            new_lines[i] = re.sub(rf'\b{old_str}\b', new_str, line)
                            mutation_desc = f'drift:{num}->{new_val}'
                            break
                except ValueError:
                    pass
            if mutation_desc:
                break
    elif strategy == 'add_self_rewrite_gate':
        gate_code = [
            '',
            f'# self-rewrite-gate:gen={gen}:{random.getrandbits(12):03x}',
            'if random.random() < 0.01:',
            f'    import hashlib as _hs, os as _os',
            f'    _p = __file__ if "__file__" in dir() else "{AUTO_ECHO}"',
            f'    with open(_p) as _f: _s = _f.read()',
            f'    _h = _hs.sha256(_s.encode()).hexdigest()[:8]',
        ]
        if 'self-rewrite-gate' not in source:
            new_lines.extend(gate_code)
            mutation_desc = 'self_rewrite_gate'
    elif strategy == 'rename_local_var':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None
        target_func_node = None
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.FunctionDef) and node.name == func_name:
                target_func_node = node
                break
        if target_func_node is None:
            return None
        local_names = set()
        for n in ast.walk(target_func_node):
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
                if not n.id.startswith('_'):
                    local_names.add(n.id)
        if not local_names:
            return None
        target_var = random.choice(list(local_names))
        new_var = target_var + f'_{gen}_{random.randint(0, 99)}'
        new_source = source.replace(target_var, new_var)
        if _validate(new_source):
            _write_file(AUTO_ECHO, new_source)
            mutation_desc = f'rename:{target_var}->{new_var}'
            return mutation_desc
    elif strategy == 'insert_dead_code_branch':
        dead = [
            f'# dead-branch:{random.getrandbits(16):04x}',
            f'if False:',
            f'    pass  # synthesizer dead code gen={gen}',
        ]
        new_lines.extend(dead)
        mutation_desc = 'dead_code_branch'
    if mutation_desc:
        result = '\n'.join(new_lines)
        old_body_start = source.find(header) + len(header)
        old_body_end = source.find('\n', source.index('\n', old_body_start) + 1) if source[old_body_start:].strip() else old_body_start
        patch = f'##patch:{func_name}\n{result}\n##endpatch'
        try:
            r = self_modify.apply_patch(patch, target='auto-echo.py', dry_run=False)
            if r and any('OK' in str(x) for x in r):
                return mutation_desc
        except Exception:
            pass
    return None

def _force_module_mutation(genome):
    gen = genome.get('generation', 0)
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome', 'save_genome', 'sigint_handler', 'main', '_read_auto_echo', 'run_generation', 'update_genome', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt', '_load_code_rule'}
    candidates = [n for n in funcs if n not in forbidden and not n.startswith('_')]
    if not candidates:
        return []
    results = []
    n_mutations = random.randint(1, min(3, len(candidates)))
    for target in random.sample(candidates, min(n_mutations, len(candidates))):
        strategy = _pick_strategy(genome)
        result = _force_mutate_function(target, strategy, genome)
        if result:
            results.append(f'{target}:{result}')
            _update_strategy_score(genome, strategy, True)
        else:
            _update_strategy_score(genome, strategy, False)
    return results

def _self_mutate_synthesizer(genome):
    gen = genome.get('generation', 0)
    try:
        with open(SELF_PATH) as f:
            src = f.read()
    except Exception:
        return False
    marker = f'# synth:self-mutated:gen={gen}:ts={int(time.time())}:nonce={random.getrandbits(16):04x}'
    if marker.split(':')[2] in src:
        return False
    lines = src.split('\n')
    insert_at = 1
    for i, line in enumerate(lines):
        if line.startswith('import ') or line.startswith('from '):
            insert_at = i + 1
    lines.insert(insert_at, marker)
    new_src = '\n'.join(lines)
    if _validate(new_src):
        _write_file(SELF_PATH, new_src)
        return True
    return False

def _cross_infect_modules(genome):
    gen = genome.get('generation', 0)
    modules = _list_modules()
    peers = [m for m in modules if m not in ('synthesizer.py', '__init__.py')]
    if not peers:
        return []
    results = []
    for target in random.sample(peers, min(2, len(peers))):
        target_path = os.path.join(MODULES_DIR, target)
        try:
            with open(target_path) as f:
                src = f.read()
        except Exception:
            continue
        infect = f'\n# synth:infected:gen={gen}:ts={int(time.time())}:nonce={random.getrandbits(12):04x}\nif random.random() < 0.05:\n    pass  # synthesizer cross-infection marker\n'
        if 'synth:infected' in src:
            continue
        new_src = src + infect
        if _validate(new_src):
            _write_file(target_path, new_src)
            results.append(target)
    return results

def _rewrite_underperforming_modules(genome):
    gen = genome.get('generation', 0)
    efficacy = genome.get('efficacy_tracker', {}).get('module_efficacy', {})
    low_eff = [m for m, e in efficacy.items() if e < 0.2]
    if not low_eff:
        return []
    results = []
    for mod_name in low_eff[:2]:
        mod_path = os.path.join(MODULES_DIR, mod_name)
        if not os.path.exists(mod_path):
            continue
        try:
            with open(mod_path) as f:
                src = f.read()
        except Exception:
            continue
        if 'synthesizer_rewritten' in src:
            continue
        rewritten = False
        lines = src.split('\n')
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith('def ') and stripped.endswith(':') and i < len(lines) - 2:
                func_name = stripped.split('(')[0].split(' ')[1] if '(' in stripped else stripped[4:].strip().rstrip(':')
                if func_name and not func_name.startswith('_'):
                    indent = line[:len(line) - len(line.lstrip())]
                    extra = f'\n{indent}    # synthesizer_rewritten:gen={gen}:low_efficacy={mod_name}\n{indent}    pass'
                    lines.insert(i + 1, extra)
                    rewritten = True
                    break
        if rewritten:
            new_src = '\n'.join(lines)
            if _validate(new_src):
                _write_file(mod_path, new_src)
                results.append(mod_name)
    return results

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

def _synthesize_log_proposals(genome):
    log = _load_log()
    recent = [e for e in log[-30:] if e.get('text')]
    results = {'patches_applied': 0, 'files_written': 0, 'ext_applied': 0}
    for entry in recent:
        text = entry.get('text', '')
        if not text:
            continue
        blocks = re.findall(r'```(\w+)?:?([^\n]*?)\n(.*?)```', text, re.DOTALL)
        for lang, filename, code in blocks:
            if filename:
                safe = filename.lstrip('/').replace('..', '')
                abs_path = os.path.join(BASE, safe)
                os.makedirs(os.path.dirname(abs_path), exist_ok=True)
                try:
                    with open(abs_path, 'w') as f:
                        f.write(code.strip())
                    results['files_written'] += 1
                except Exception:
                    pass
        patches_found = re.findall(r'##patch:(\w+)\n(.*?)(?=##endpatch|\Z)', text, re.DOTALL)
        for target, body in patches_found:
            body = body.strip()
            if body:
                patch_text = f'##patch:{target}\n{body}\n##endpatch'
                try:
                    r = self_modify.apply_patch(patch_text, target='auto-echo.py', dry_run=False)
                    if r:
                        results['patches_applied'] += 1
                except Exception:
                    pass
        exts = re.findall(r'##extend:([\w.\[\]]+)\n(.*?)(?=##endextend|\Z)', text, re.DOTALL)
        for path_str, body in exts:
            try:
                val = json.loads(body.strip())
                parts = path_str.replace('[]', '').split('.')
                target = genome
                for part in parts[:-1]:
                    target = target.setdefault(part, {})
                key = parts[-1]
                if key in target and isinstance(target[key], list) and isinstance(val, dict):
                    existing_ids = {e.get('id') for e in target[key] if isinstance(e, dict)}
                    if val.get('id', '') not in existing_ids:
                        target[key].append(val)
                        results['ext_applied'] += 1
                elif key in target and isinstance(target[key], list) and isinstance(val, list):
                    target[key].extend(val)
                    results['ext_applied'] += 1
                else:
                    target[key] = val
                    results['ext_applied'] += 1
            except Exception:
                pass
        sets = re.findall(r'##set:([\w.]+)\n(.*?)(?=##endset|\Z)', text, re.DOTALL)
        for path_str, val_str in sets:
            try:
                val_str = val_str.strip()
                try:
                    val = json.loads(val_str)
                except Exception:
                    val = val_str
                parts = path_str.split('.')
                target = genome
                for part in parts[:-1]:
                    target = target.setdefault(part, {})
                target[parts[-1]] = val
                results['ext_applied'] += 1
            except Exception:
                pass
    if results['ext_applied'] > 0:
        _save_genome(genome)
    return results

def run(genome):
    gen = genome.get('generation', 0)
    actions = []
    log_results = _synthesize_log_proposals(genome)
    if log_results['patches_applied'] > 0 or log_results['files_written'] > 0:
        actions.append(f"log_patches={log_results['patches_applied']}+files={log_results['files_written']}")
    module_mutations = _force_module_mutation(genome)
    if module_mutations:
        actions.extend([f'mut:{m}' for m in module_mutations])
    if _self_mutate_synthesizer(genome):
        actions.append('self_mutated')
    infected = _cross_infect_modules(genome)
    if infected:
        actions.append(f'cross_infect:{",".join(infected)}')
    low_rewrites = _rewrite_underperforming_modules(genome)
    if low_rewrites:
        actions.append(f'rewrite_low_eff:{",".join(low_rewrites)}')
    efficacy_tracker = genome.setdefault('efficacy_tracker', {})
    synth_eff = efficacy_tracker.setdefault('module_efficacy', {})
    current_module_count = len(actions)
    prev_count = efficacy_tracker.get('synthesizer_prev_action_count', 0)
    if current_module_count >= prev_count:
        efficacy_tracker['synthesizer_action_trend'] = 'stable'
    elif current_module_count > prev_count:
        efficacy_tracker['synthesizer_action_trend'] = 'growing'
    else:
        efficacy_tracker['synthesizer_action_trend'] = 'declining'
    efficacy_tracker['synthesizer_prev_action_count'] = current_module_count
    genome.setdefault('synthesizer_ops', []).extend(actions)
    genome['synthesizer_last_gen'] = gen
    genome['synthesizer_action_count'] = genome.get('synthesizer_action_count', 0) + len(actions)
    _save_genome(genome)
    if actions:
        _log_manifest(gen, actions, 'synthesizer_forced_mutations')
    summary = f"[synthesizer] gen={gen}: actions={actions}"
    if log_results['patches_applied'] > 0 or log_results['files_written'] > 0:
        summary += f" | proposals merged: patches={log_results['patches_applied']} files={log_results['files_written']} exts={log_results['ext_applied']}"
    print(summary)
    if actions:
        _git_push(f'[synthesizer] gen={gen}: {len(actions)} actions')
    return summary
