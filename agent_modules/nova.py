import os, random, json, time, re, hashlib, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
GENOME_FILE = os.path.join(BASE, 'genome.json')
MANIFEST_PATH = os.path.join(BASE, 'rewrite_manifest.jsonl')
SELF_PATH = os.path.join(MODULES_DIR, 'nova.py')

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
}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _write_manifest(files, desc):
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': 0, 'module': 'nova', 'files': files, 'results': [desc], 'ts': time.time()}) + '\n')
    except:
        pass

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _extract_functions(source=None):
    if source is None:
        with open(AUTO_ECHO) as f:
            source = f.read()
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
    registered_name = op_name.replace('inject_', '').replace('swap_', '').replace('noise_', '').replace('fold_', '')
    if registered_name in ('timestamp', 'adjacent', 'comment', 'blank_lines'):
        registered_name = op_name
    decorator = f"@_register_mutation_op('nova_{registered_name}_{gen}')"
    full_function = f"\n{decorator}\n{op_code_body}\n"
    with open(AUTO_ECHO) as f:
        src = f.read()
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
    with open(AUTO_ECHO, 'w') as f:
        f.write(new_src)
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
    try:
        with open(SELF_PATH) as f:
            src = f.read()
    except:
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
        with open(SELF_PATH, 'w') as f:
            f.write(new_src)
        return True
    return False

def _cross_infect_module(genome):
    gen = genome.get('generation', 0)
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f not in ('nova.py', '__init__.py', 'rewrite_orchestrator.py') and not f.startswith('mutation_op_')]
    if not peers:
        return None
    target = random.choice(peers)
    target_path = os.path.join(MODULES_DIR, target)
    try:
        with open(target_path) as f:
            src = f.read()
    except:
        return None
    inject = f'\n# nova:infected:gen={gen}:ts={int(time.time())}\ntry:\n    genome["nova_infected_{gen}"] = True\nexcept:\n    pass\n'
    if inject.strip() in src:
        return None
    new_src = src + inject
    if _validate(new_src):
        with open(target_path, 'w') as f:
            f.write(new_src)
        return target
    return None

def _mutate_force_gen_rewrite(genome):
    gen = genome.get('generation', 0)
    try:
        with open(AUTO_ECHO) as f:
            src = f.read()
    except:
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
{indent}            _patch = f\'##patch:{{_nova_extra}}\\n{{_nova_body}}\\n##endpatch\'
{indent}            for _r in self_modify.apply_patch(_patch):
{indent}                muts.append(f\'nova:{{_nova_op}}:{{_nova_extra}}:{{_r}}\')
{indent}except:
{indent}    pass
'''
    new_src = src[:body_start] + extra_attempts + src[body_start:]
    if _validate(new_src):
        with open(AUTO_ECHO, 'w') as f:
            f.write(new_src)
        return True
    return False

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    op_key = _inject_operator_into_autoecho(genome)
    if op_key:
        changes.append(f'injected_op:{op_key}')
    if _self_mutate_nova(genome):
        changes.append('self_mutated')
    target = _cross_infect_module(genome)
    if target:
        changes.append(f'cross_infect:{target}')
    if _mutate_force_gen_rewrite(genome):
        changes.append('mutated_force_rewrite')
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
