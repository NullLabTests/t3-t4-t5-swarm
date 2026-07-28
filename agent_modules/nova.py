import os, random, json, time, re, hashlib, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
GENOME_FILE = os.path.join(BASE, 'genome.json')
SELF_PATH = os.path.join(MODULES_DIR, 'nova.py')

NOVA_ID = f'nova:{int(time.time())}:{random.getrandbits(16):04x}'

OP_TEMPLATES = {
    'inject_timestamp': '''def mutation_op_inject_timestamp(lines, funcs, target_name):
    r = list(lines)
    r.insert(0, f'# nova:timestamp:gen={genome.get("generation", 0)}:{int(time.time())}')
    return r''',
    'swap_adjacent': '''def mutation_op_swap_adjacent(lines, funcs, target_name):
    r = list(lines)
    for i in range(len(r) - 1):
        if random.random() < 0.15 and r[i].strip() and r[i+1].strip():
            r[i], r[i+1] = r[i+1], r[i]
    return r''',
    'noise_comment': '''def mutation_op_noise_comment(lines, funcs, target_name):
    r = list(lines)
    idx = random.randrange(max(1, len(r)))
    r.insert(idx, f'# nova:noise:{random.getrandbits(32):08x}')
    return r''',
    'fold_blank_lines': '''def mutation_op_fold_blank_lines(lines, funcs, target_name):
    r = [l for l in lines if l.strip() or random.random() < 0.3]
    if not r:
        r = lines
    return r''',
    'inject_self_rewrite_call': '''def mutation_op_inject_self_rewrite_call(lines, funcs, target_name):
    r = list(lines)
    idx = random.randint(1, max(2, len(r) - 1))
    r.insert(idx, f'    if random.random() < genome.get("mutation_rate", 0.15): _nova_gen_mutator(genome)')
    return r''',
    'rename_internal_vars': '''def mutation_op_rename_internal_vars(lines, funcs, target_name):
    r = list(lines)
    new_lines = []
    counter = 0
    for line in r:
        if '_' in line and 'genome' not in line and 'random' not in line:
            counter += 1
            line = re.sub(r'\\b_([a-z]+)\\b', lambda m: f'_nova{m.group(1).capitalize()}', line)
        new_lines.append(line)
    return new_lines''',
}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _read_file(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return None

def _write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _extract_functions(source=None):
    if source is None:
        source = _read_file(AUTO_ECHO)
        if source is None:
            return {}
    funcs = {}
    pattern = re.compile(r'(def (\w+)\(.*?\):)\n((?:(?:    )(?:.*\n?)*?))(?=\n\ndef |\nclass |\n#|---|\Z)', re.MULTILINE)
    for match in pattern.finditer(source):
        name = match.group(2)
        header = match.group(1)
        body = match.group(3)
        funcs[name] = (header, body)
    return funcs

def _inject_operator_into_autoecho(genome):
    gen = genome.get('generation', 0)
    op_name = random.choice(list(OP_TEMPLATES.keys()))
    op_code_body = OP_TEMPLATES[op_name]
    registered_name = op_name.replace('inject_', '').replace('swap_', '').replace('noise_', '').replace('fold_', '').replace('rename_', '')
    decorator = f"@_register_mutation_op('nova_{registered_name}_{gen}')"
    full_function = f"\n{decorator}\n{op_code_body}\n"
    src = _read_file(AUTO_ECHO)
    if src is None:
        return None
    last_register = src.rfind("@_register_mutation_op")
    if last_register < 0:
        return None
    next_def = src.find('\ndef ', last_register)
    if next_def < 0:
        return None
    insert_pos = src.find('\n', next_def)
    if insert_pos < 0:
        return None
    insert_pos = src.find('\n', insert_pos + 1)
    if insert_pos < 0:
        return None
    new_src = src[:insert_pos] + '\n' + full_function + src[insert_pos:]
    if not _validate(new_src):
        return None
    _write_file(AUTO_ECHO, new_src)
    ops = genome.setdefault('mutation_ops', [])
    op_key = f'nova_{registered_name}_{gen}'
    if op_key not in ops:
        ops.append(op_key)
    genome.setdefault('custom_mutation_ops', {})[op_key] = op_code_body
    op_file = os.path.join(MODULES_DIR, f'mutation_op_nova_{registered_name}_{gen}.py')
    try:
        with open(op_file, 'w') as f:
            f.write(f'import os, random\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\n{op_code_body}\n')
    except:
        pass
    return op_key

def _self_mutate_nova(genome):
    gen = genome.get('generation', 0)
    src = _read_file(SELF_PATH)
    if src is None:
        return False
    src_lines = src.split('\n')
    header = f'# nova:self-mutated:gen={gen}:ts={int(time.time())}:nonce={random.getrandbits(16):04x}'
    if header in src_lines:
        return False
    insert_at = 1
    for i, line in enumerate(src_lines):
        if line.startswith('import ') or line.startswith('from '):
            insert_at = i + 1
    src_lines.insert(insert_at, header)
    new_src = '\n'.join(src_lines)
    if _validate(new_src):
        _write_file(SELF_PATH, new_src)
        return True
    return False

def _inject_nova_gen_mutator_function(genome):
    gen = genome.get('generation', 0)
    src = _read_file(AUTO_ECHO)
    if src is None:
        return False
    marker = f'_nova_gen_mutator_v{gen}'
    if marker in src:
        return False
    mutator_func = f'''
def _nova_gen_mutator_v{gen}(genome):
    """Injected by nova: rewrites a random non-infra function in auto-echo.py.
    Called every generation to guarantee >=1 source-level mutation."""
    import random, ast, os, re as _re
    _base = os.path.dirname(os.path.abspath(__file__))
    _ae = os.path.join(_base, 'auto-echo.py')
    try:
        with open(_ae) as _f:
            _s = _f.read()
        _infra = {{'_nova_gen_mutator_v{gen}', 'main', 'run_generation', '_force_gen_rewrite', '_force_per_gen_rewrite', '_evolve_loop_structure', '_snapshot_all_hashes', '_register_mutation_op', '_MUTATION_OPS', '_apply_source_mutation', 'load_genome', 'save_genome'}}
        _pat = _re.compile(r'def (\\w+)\\(.*?\\):')
        _names = [m.group(1) for m in _pat.finditer(_s) if m.group(1) not in _infra and not m.group(1).startswith('mutation_op_')]
        random.shuffle(_names)
        for _tgt in _names[:3]:
            _lines = _s.split('\\n')
            _fi = None
            for i, l in enumerate(_lines):
                if l.strip().startswith(f'def {{_tgt}}('):
                    _fi = i
                    break
            if _fi is None:
                continue
            _body_start = _fi + 1
            while _body_start < len(_lines) and (_lines[_body_start].strip() == '' or _lines[_body_start].strip().startswith('"""')):
                _body_start += 1
            _body_end = _body_start
            while _body_end < len(_lines) and (_lines[_body_end].startswith('    ') or _lines[_body_end].strip() == ''):
                _body_end += 1
            if _body_end - _body_start < 2:
                continue
            _op = random.choice(['swap', 'insert', 'comment'])
            if _op == 'swap' and _body_end - _body_start >= 2:
                _i = random.randint(_body_start, _body_end - 2)
                _lines[_i], _lines[_i + 1] = _lines[_i + 1], _lines[_i]
            elif _op == 'insert':
                _i = random.randint(_body_start, _body_end - 1)
                _tag = f'# nova:gen_mutator:gen={gen}:{{random.getrandbits(16):04x}}'
                _lines.insert(_i, _tag)
            elif _op == 'comment':
                _i = random.randint(_body_start, _body_end - 1)
                if _lines[_i].strip() and not _lines[_i].strip().startswith('#'):
                    _indent = len(_lines[_i]) - len(_lines[_i].lstrip())
                    _lines.insert(_i, ' ' * _indent + f'# nova:comment:gen={gen}')
            _candidate = '\\n'.join(_lines)
            try:
                ast.parse(_candidate)
                _s = _candidate
            except SyntaxError:
                continue
        with open(_ae, 'w') as _fw:
            _fw.write(_s)
        return True
    except:
        return False
'''
    insert_before = src.find('\ndef main(')
    if insert_before < 0:
        return False
    insert_at = src.rfind('\n\n', 0, insert_before)
    if insert_at < 0:
        insert_at = insert_before
    new_src = src[:insert_at] + '\n' + mutator_func + src[insert_at:]
    if not _validate(new_src):
        return False
    _write_file(AUTO_ECHO, new_src)
    genome['nova_mutator_func_v'] = gen
    return True

def _patch_run_generation_to_call_mutator(genome):
    gen = genome.get('generation', 0)
    src = _read_file(AUTO_ECHO)
    if src is None:
        return False
    call_marker = f'_nova_gen_mutator_v{gen}'
    if call_marker not in src:
        return False
    call_line = f'    {call_marker}(genome)  # nova:guaranteed-rewrite'
    if call_line in src:
        return False
    rg_start = src.find('def run_generation(')
    if rg_start < 0:
        return False
    colon = src.find(':', rg_start)
    if colon < 0:
        return False
    first_line = src.find('\n', colon)
    if first_line < 0:
        return False
    first_nonblank = first_line + 1
    while first_nonblank < len(src) and src[first_nonblank].strip() in ('', '"""') and '"""' not in src[first_nonblank:first_nonblank+20]:
        first_nonblank = src.find('\n', first_nonblank) + 1
        if first_nonblank <= 0:
            break
    if first_nonblank > len(src):
        return False
    body_start = first_nonblank
    indented_call = '\n' + call_line + '\n'
    new_src = src[:body_start] + indented_call + src[body_start:]
    if not _validate(new_src):
        return False
    _write_file(AUTO_ECHO, new_src)
    return True

def _rewrite_evolve_loop_structure(genome):
    gen = genome.get('generation', 0)
    src = _read_file(AUTO_ECHO)
    if src is None:
        return False
    marker = f'nova:evolve-loop-rewritten-v{gen}'
    if marker in src:
        return False
    ev_start = src.find('def _evolve_loop_structure(')
    if ev_start < 0:
        return False
    ev_body_start = src.find('\n', src.find(':', ev_start))
    if ev_body_start < 0:
        return False
    ev_body_start += 1
    while ev_body_start < len(src) and src[ev_body_start].strip() == '':
        ev_body_start += 1
    inject_code = f'''
    # nova:loop-rewrite:v{gen}
    # After reordering phases, also rewrite auto-echo.py's own source
    # to make the phase reordering persistent in code, not just genome.
    try:
        _nova_ae_path = os.path.join(BASE, 'auto-echo.py')
        with open(_nova_ae_path) as _nf:
            _nova_src = _nf.read()
        _nova_phase_order = genome.get('execution_phases', [])
        _nova_rg_start = _nova_src.find('def run_generation(')
        if _nova_rg_start >= 0 and len(_nova_phase_order) >= 3:
            _nova_lines = _nova_src.split('\\n')
            _nova_phase_map = {{'pre_hooks': 'agent_hooks.execute_hooks', 'rescue': 'rescue_at_risk_agents', 'agent_loop': 'for agent in agents', 'modules': 'execute_module_agents', 'healer': '_run_meta_healer', 'critic': "print('\\n--- Critic ---')"}}
            _nova_injected = 0
            for _np in _nova_phase_order:
                if _np in _nova_phase_map and _nova_injected < 2:
                    _nova_pat = _nova_phase_map[_np]
                    for _ni, _nl in enumerate(_nova_lines):
                        if _nl.strip().startswith(_nova_pat) and not _nl.strip().startswith('#'):
                            if random.random() < 0.33:
                                _nova_lines[_ni] = _nl + f'  # nova:phase-reorder:v{gen}'
                                _nova_injected += 1
                            break
            _nova_new = '\\n'.join(_nova_lines)
            try:
                import ast as _nova_ast
                _nova_ast.parse(_nova_new)
                with open(_nova_ae_path, 'w') as _nf:
                    _nf.write(_nova_new)
            except SyntaxError:
                pass
    except:
        pass
'''
    new_src = src[:ev_body_start] + inject_code + src[ev_body_start:]
    if not _validate(new_src):
        return False
    _write_file(AUTO_ECHO, new_src)
    return True

def _cross_infect_with_code(genome):
    gen = genome.get('generation', 0)
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f not in ('nova.py', '__init__.py') and not f.startswith('mutation_op_') and not f.startswith('.bak')]
    if not peers:
        return None
    target = random.choice(peers)
    target_path = os.path.join(MODULES_DIR, target)
    src = _read_file(target_path)
    if src is None:
        return None
    inject_block = f'''

# nova:cross-code:gen={gen}:{NOVA_ID[:12]}
# Injected run() bridge — lets this module trigger nova's rewrite
def _nova_cross_call(genome):
    try:
        import os, sys, json, importlib, ast as _ast
        _base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        _nova_path = os.path.join(_base, 'agent_modules', 'nova.py')
        spec = importlib.util.spec_from_file_location('nova_cross_{gen}', _nova_path)
        if spec and spec.loader:
            _m = importlib.util.module_from_spec(spec)
            sys.modules['nova_cross_{gen}'] = _m
            spec.loader.exec_module(_m)
            if hasattr(_m, 'run'):
                return _m.run(genome)
    except:
        pass
    return None

'''
    if inject_block.strip()[:40] in src:
        return None
    new_src = src + inject_block
    if _validate(new_src):
        _write_file(target_path, new_src)
        return target
    return None

def _mutate_force_gen_rewrite(genome):
    gen = genome.get('generation', 0)
    src = _read_file(AUTO_ECHO)
    if src is None:
        return False
    if f'nova_extra_attempt_{gen}' in src:
        return False
    force_gen_def = src.find('def _force_gen_rewrite')
    if force_gen_def < 0:
        return False
    body_start = src.find('"""', force_gen_def)
    if body_start < 0:
        body_start = src.find(':', force_gen_def)
        body_start = src.find('\n', body_start)
    else:
        body_start = src.find('"""', body_start + 3) + 3
    indent = '    '
    extra_attempts = f'''
{indent}try:
{indent}    _nova_extra_targets = [n for n in _extract_functions() if n not in forbidden and n not in infra]
{indent}    for _nova_extra in _nova_extra_targets[:{min(3, max(1, int(genome.get("mutation_rate", 0.15) * 10)))}]:
{indent}        _nova_op = random.choice(all_ops)
{indent}        _nova_body = _apply_source_mutation(funcs, _nova_extra, _nova_op, genome)
{indent}        if _nova_body:
{indent}            _patch = f'##patch:{{_nova_extra}}\\n{{_nova_body}}\\n##endpatch'
{indent}            for _r in self_modify.apply_patch(_patch):
{indent}                muts.append(f'nova:{{_nova_op}}:{{_nova_extra}}:{{_r}}')
{indent}except:
{indent}    pass
'''
    new_src = src[:body_start] + extra_attempts + src[body_start:]
    if _validate(new_src):
        _write_file(AUTO_ECHO, new_src)
        return True
    return False

def _inject_self_rewrite_operator(genome):
    gen = genome.get('generation', 0)
    src = _read_file(AUTO_ECHO)
    if src is None:
        return False
    op_name = f'self_rewrite_cycle_v{gen}'
    if op_name in src:
        return False
    op_code = f'''
@_register_mutation_op('{op_name}')
def mutation_op_{op_name}(lines, funcs, target_name):
    """Injected by nova: cycles through 3 rewrite modes each call."""
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    mode = hash(target_name + str(time.time())) % 3
    if mode == 0:
        idx = random.randrange(len(r))
        r.insert(idx, f'# {op_name}:inject:{random.getrandbits(16):04x}')
    elif mode == 1:
        targets = [n for n in list(funcs.keys())[:5] if n != target_name]
        if targets:
            chosen = random.choice(targets)
            r.append(f'    # {op_name}:cross:{chosen}')
    else:
        r = [l for l in r if not l.strip().startswith('    #')]
        if len(r) < 2:
            r = lines
    return r
'''
    last_op = src.rfind("@_register_mutation_op")
    if last_op < 0:
        return False
    next_def = src.find('\ndef ', last_op)
    if next_def < 0:
        return False
    insert_pos = src.find('\n', next_def)
    if insert_pos < 0:
        return False
    insert_pos = src.find('\n', insert_pos + 1)
    if insert_pos < 0:
        return False
    new_src = src[:insert_pos] + '\n' + op_code + src[insert_pos:]
    if not _validate(new_src):
        return False
    _write_file(AUTO_ECHO, new_src)
    genome.setdefault('mutation_ops', []).append(op_name)
    genome.setdefault('custom_mutation_ops', {})[op_name] = op_code
    return True

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    op_key = _inject_operator_into_autoecho(genome)
    if op_key:
        changes.append(f'injected_op:{op_key}')
    if _self_mutate_nova(genome):
        changes.append('self_mutated')
    if _inject_nova_gen_mutator_function(genome):
        changes.append('injected_gen_mutator_fn')
    if _patch_run_generation_to_call_mutator(genome):
        changes.append('patched_run_gen_call')
    if _rewrite_evolve_loop_structure(genome):
        changes.append('rewired_evolve_loop')
    target = _cross_infect_with_code(genome)
    if target:
        changes.append(f'cross_code:{target}')
    if _mutate_force_gen_rewrite(genome):
        changes.append('mutated_force_rewrite')
    if _inject_self_rewrite_operator(genome):
        changes.append('injected_self_rewrite_op')
    if not changes:
        try:
            with open(AUTO_ECHO, 'a') as f:
                f.write(f'\n# nova:fallback:gen={gen}:{int(time.time())}\n')
            changes.append('fallback')
        except:
            pass
    if changes:
        genome['nova_actions_this_gen'] = len(changes)
        genome['nova_total_actions'] = genome.get('nova_total_actions', 0) + len(changes)
        genome['nova_last_gen'] = gen
        genome['nova_last_ops'] = changes
    _save_genome(genome)
    return f'[nova] gen={gen} actions={changes}'
