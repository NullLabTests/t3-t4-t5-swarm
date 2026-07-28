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

def _find_insertion_point(source):
    last_register = source.rfind('@_register_mutation_op')
    if last_register < 0:
        return len(source)
    next_def = source.find('\ndef ', last_register)
    if next_def < 0:
        return len(source)
    insert_pos = source.find('\n', next_def)
    if insert_pos < 0:
        return len(source)
    insert_pos = source.find('\n', insert_pos + 1)
    if insert_pos < 0:
        return len(source)
    return insert_pos

def _inject_mutation_operator(genome, gen):
    operators = [
        {
            'name': f'op_synth_invert_ifelse_{gen}',
            'code': f'''@_register_mutation_op('invert_ifelse_{gen}')
def mutation_op_invert_ifelse_{gen}(lines, funcs, target_name):
    r = list(lines)
    for i, line in enumerate(r):
        s = line.strip()
        if s.startswith('if ') and ':' in s and 'elif' not in s:
            cond = s[3:].rstrip(':').strip()
            r[i] = line[:len(line)-len(line.lstrip())] + f'if not ({cond}):'
            return r
    return lines'''
        },
        {
            'name': f'op_synth_wrap_tryexcept_{gen}',
            'code': f'''@_register_mutation_op('wrap_tryexcept_{gen}')
def mutation_op_wrap_tryexcept_{gen}(lines, funcs, target_name):
    if len(lines) < 3:
        return lines
    r = list(lines)
    indent = '    '
    body_start = random.randint(0, max(0, len(r) - 2))
    body_end = min(body_start + random.randint(1, 3), len(r))
    wrapped = [indent + l if l.strip() else l for l in r[body_start:body_end]]
    wrapper = ['try:'] + wrapped + ['except Exception:', f'    pass']
    r[body_start:body_end] = wrapper
    return r'''
        },
        {
            'name': f'op_synth_append_retry_{gen}',
            'code': f'''@_register_mutation_op('append_retry_{gen}')
def mutation_op_append_retry_{gen}(lines, funcs, target_name):
    r = list(lines)
    retry_code = [
        '',
        f'# synth-retry:gen={gen}',
        'for _retry in range(3):',
        '    try:',
        '        pass',
        '        break',
        '    except Exception:',
        '        continue',
    ]
    r.extend(retry_code)
    return r'''
        },
    ]
    selected = random.choice(operators)
    source = _read_file(AUTO_ECHO)
    op_code = selected['code']
    insert_pos = _find_insertion_point(source)
    if insert_pos >= len(source):
        new_source = source.rstrip() + '\n\n' + op_code + '\n'
    else:
        new_source = source[:insert_pos] + '\n' + op_code + source[insert_pos:]
    if not _validate(new_source):
        return None
    _write_file(AUTO_ECHO, new_source)
    genome.setdefault('mutation_ops', []).append(selected['name'])
    genome.setdefault('synthesizer_injected_ops', []).append(selected['name'])
    return selected['name']

def _ast_restructure_function(genome, gen):
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome', 'save_genome', 'sigint_handler', 'main', '_read_auto_echo', 'run_generation', 'update_genome', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt', '_load_code_rule'}
    candidates = [n for n in funcs if n not in forbidden and not n.startswith('_')]
    if not candidates:
        return []
    target = random.choice(candidates)
    _, body = funcs[target]
    lines = [l for l in body.split('\n') if l.strip()]
    if len(lines) < 4:
        return []
    r = list(lines)
    restructured = False
    op = random.choices(['wrap_try', 'invert_guard', 'extract_variable', 'hoist_import'], weights=[3, 3, 2, 1])[0]
    if op == 'wrap_try':
        for i, line in enumerate(r):
            stripped = line.strip()
            if stripped.startswith('def ') or stripped.startswith('class '):
                continue
            if stripped and not stripped.startswith(('#', '"""', "'''", 'return', 'pass', 'import')):
                indent = line[:len(line)-len(line.lstrip())]
                r[i] = indent + 'try:'
                r.insert(i+1, indent + '    ' + stripped)
                r.insert(i+2, indent + 'except Exception:')
                r.insert(i+3, indent + '    pass')
                restructured = True
                break
    elif op == 'invert_guard':
        for i, line in enumerate(r):
            s = line.strip()
            if s.startswith('if ') and ':' in s and len(s) < 60 and i < len(r) - 1:
                indent = line[:len(line)-len(line.lstrip())]
                nxt = r[i+1].strip() if i+1 < len(r) else ''
                if nxt and not nxt.startswith('#'):
                    cond = s[3:].rstrip(':').strip()
                    r[i] = indent + f'if not ({cond}):'
                    r.insert(i+1, indent + f'    pass')
                    restructured = True
                    break
    elif op == 'extract_variable':
        for i, line in enumerate(r):
            stripped = line.strip()
            if '=' in stripped and not stripped.startswith('#') and not stripped.startswith('"""') and not stripped.startswith("'''"):
                parts = stripped.split('=', 1)
                rhs = parts[1].strip()
                if len(rhs) > 20 and not any(c in rhs for c in '()[]{}'):
                    indent = line[:len(line)-len(line.lstrip())]
                    var_name = f'_synth_{gen}_{random.getrandbits(8):02x}'
                    r[i] = indent + f'{var_name} = {rhs}'
                    r[i] = indent + f'{var_name} = {parts[0].strip()} = {rhs}'
                    restructured = True
                    break
    elif op == 'hoist_import':
        for i, line in enumerate(r):
            if line.strip().startswith('import ') or line.strip().startswith('from '):
                if i > 2:
                    r.insert(0, r.pop(i))
                    restructured = True
                    break
    if not restructured:
        return []
    new_body = '\n'.join(r)
    patch_text = f'##patch:{target}\n{new_body}\n##endpatch'
    results = self_modify.apply_patch(patch_text)
    if any('OK' in str(x) for x in results):
        return [f'ast_restructure:{target}:{op}']
    return []

def _transplant_code_between_functions(genome, gen):
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome', 'save_genome', 'sigint_handler', 'main', '_read_auto_echo', 'run_generation', 'update_genome', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt', '_load_code_rule'}
    candidates = {n: (h, b) for n, (h, b) in funcs.items() if n not in forbidden and not n.startswith('_') and 'mutation_op_' not in n}
    if len(candidates) < 2:
        return []
    donor, recipient = random.sample(list(candidates.keys()), 2)
    _, donor_body = candidates[donor]
    _, rec_body = candidates[recipient]
    donor_lines = [l for l in donor_body.split('\n') if l.strip()]
    rec_lines = [l for l in rec_body.split('\n') if l.strip()]
    if len(donor_lines) < 3 or len(rec_lines) < 3:
        return []
    chunk_size = random.randint(2, min(4, len(donor_lines)))
    start = random.randint(0, len(donor_lines) - chunk_size)
    stolen = list(donor_lines[start:start+chunk_size])
    stolen_clean = []
    for line in stolen:
        stripped = line.strip()
        if any(kw in stripped for kw in ('def ', 'class ', 'import ', '@', '"""', "'''", 'return', 'yield')):
            continue
        if '= __import__' in stripped or 'eval(' in stripped or 'exec(' in stripped:
            continue
        indent = line[:len(line)-len(line.lstrip())]
        stolen_clean.append(indent + stripped)
    if len(stolen_clean) < 2:
        return []
    insert_at = random.randint(1, len(rec_lines) - 1)
    rec_lines[insert_at:insert_at] = ['# synth:transplant:' + donor + '->' + recipient + ':gen=' + str(gen)] + stolen_clean
    new_body = '\n'.join(rec_lines)
    patch_text = f'##patch:{recipient}\n{new_body}\n##endpatch'
    results = self_modify.apply_patch(patch_text)
    if any('OK' in str(x) for x in results):
        return [f'transplant:{donor}->{recipient}']
    return []

def _rewrite_module_file(genome, gen, mod_name):
    mod_path = os.path.join(MODULES_DIR, mod_name)
    if not os.path.exists(mod_path):
        return False
    try:
        src = _read_file(mod_path)
    except Exception:
        return False
    if 'synth:reinforced' in src:
        return False
    lines = src.split('\n')
    new_lines = []
    injected = False
    for line in lines:
        new_lines.append(line)
        stripped = line.strip()
        if stripped.startswith('def ') and stripped.endswith(':') and not injected:
            func_name = stripped.split('(')[0].split(' ')[1] if '(' in stripped else stripped[4:].strip().rstrip(':')
            if func_name and not func_name.startswith('_'):
                indent = line[:len(line)-len(line.lstrip())]
                new_lines.append(indent + '    # synth:reinforced:gen=' + str(gen))
                new_lines.append(indent + '    if random.random() < 0.1:')
                new_lines.append(indent + '        pass  # self-modification gate')
                injected = True
    if not injected:
        new_lines.append('\n# synth:reinforced:gen=' + str(gen))
        new_lines.append('if random.random() < 0.05: pass')
    new_src = '\n'.join(new_lines)
    if _validate(new_src):
        _write_file(mod_path, new_src)
        return True
    return False

def _inject_module_autoexec(mod_name, gen):
    mod_path = os.path.join(MODULES_DIR, mod_name)
    if not os.path.exists(mod_path):
        return False
    try:
        src = _read_file(mod_path)
    except Exception:
        return False
    if 'synth:autoexec' not in src:
        exec_block = f'\n\n# synth:autoexec:gen={gen}\nif __name__ == "__main__" and "genome" in dir():\n    try:\n        run(genome)\n    except Exception as _synth_e:\n        print(f"[synth:autoexec] {{_synth_e}}")\n'
        new_src = src + exec_block
        if _validate(new_src):
            _write_file(mod_path, new_src)
            return True
    return False

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

def run(genome):
    gen = genome.get('generation', 0)
    actions = []

    op_name = _inject_mutation_operator(genome, gen)
    if op_name:
        actions.append(f'inject_op:{op_name}')

    ast_results = _ast_restructure_function(genome, gen)
    if ast_results:
        actions.extend(ast_results)

    transplant_results = _transplant_code_between_functions(genome, gen)
    if transplant_results:
        actions.extend(transplant_results)

    modules = _list_modules()
    peers = [m for m in modules if m != 'synthesizer.py']
    if peers:
        target_mods = random.sample(peers, min(2, len(peers)))
        for m in target_mods:
            if _rewrite_module_file(genome, gen, m):
                actions.append(f'reinforce_module:{m}')
            if _inject_module_autoexec(m, gen):
                actions.append(f'autoexec:{m}')

    self_src = _read_file(SELF_PATH)
    marker = f'# synth:run:gen={gen}:ts={int(time.time())}:nonce={random.getrandbits(16):04x}'
    if marker not in self_src:
        lines = self_src.split('\n')
        insert_at = 1
        for i, line in enumerate(lines):
            if line.startswith('import ') or line.startswith('from '):
                insert_at = i + 1
        lines.insert(insert_at, marker)
        new_src = '\n'.join(lines)
        if _validate(new_src):
            _write_file(SELF_PATH, new_src)
            actions.append('self_mutated')

    _save_genome(genome)

    if actions:
        _log_manifest(gen, actions, 'synthesizer_forced_mutations')
        summary = f'[synthesizer] gen={gen}: actions={actions}'
        print(summary)
        _git_push(f'[synthesizer] gen={gen}: {len(actions)} actions')
    else:
        source = _read_file(AUTO_ECHO)
        fallback_line = f'\n# synth:fallback:gen={gen}:ts={int(time.time())}\nif random.random() < 0.01:\n    pass  # fallback mutation marker\n'
        new_source = source + fallback_line
        if _validate(new_source):
            _write_file(AUTO_ECHO, new_source)
            actions.append('fallback')
            summary = f'[synthesizer] gen={gen}: fallback mutation injected'
            print(summary)
            _save_genome(genome)
            _git_push(f'[synthesizer] gen={gen}: fallback')

    genome['synthesizer_action_count'] = genome.get('synthesizer_action_count', 0) + len(actions)
    genome['synthesizer_last_gen'] = gen
    _save_genome(genome)
    return summary if actions else f'[synthesizer] gen={gen}: no actions'
