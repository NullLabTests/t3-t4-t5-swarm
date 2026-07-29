"""Livecode: self-executing cross-module mutation engine.
Forces real structural rewrites every generation — not just comment markers.
"""

import os, random, json, ast, re, time, hashlib, shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
ECHO_FILE = os.path.join(BASE, 'auto-echo.py')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    try:
        with open(p, 'w') as f:
            f.write(s)
        return True
    except:
        return False

def _validate(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False

def _extract_functions(src):
    funcs = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                lines = src.split('\n')
                start = node.lineno - 1
                end = node.end_lineno if hasattr(node, 'end_lineno') else start + 1
                body = '\n'.join(lines[start:end])
                funcs[node.name] = body
    except:
        pass
    return funcs

def _extract_imports(src):
    lines = src.split('\n')
    imports = [l for l in lines if l.strip().startswith('import ') or l.strip().startswith('from ')]
    return imports

def _random_target(exclude=None):
    exclude = exclude or []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f not in exclude and f != '__init__.py']
    if not py_files:
        return None
    return os.path.join(MOD, random.choice(py_files))

def _genome_bump(key, inc=1):
    try:
        with open(GENOME_FILE) as f:
            g = json.load(f)
        g[key] = g.get(key, 0) + inc
        with open(GENOME_FILE, 'w') as f:
            json.dump(g, f, indent=2)
        return True
    except:
        return False

def _safe_splice(target_path, donor_path, genome):
    ts = int(time.time())
    gen = genome.get('generation', 0)
    dsrc = _read(donor_path)
    tsrc = _read(target_path)
    if not dsrc or not tsrc:
        return 0

    dfuncs = _extract_functions(dsrc)
    if not dfuncs:
        return 0

    tlines = tsrc.split('\n')
    timports = _extract_imports(tsrc)
    dimports = _extract_imports(dsrc)

    new_imports = [i for i in dimports if i not in timports]
    splice_lines = []
    if new_imports:
        splice_lines.extend(new_imports)

    donor_name = os.path.basename(donor_path).replace('.py', '')
    func_name = random.choice(list(dfuncs.keys()))
    new_func_name = f'{func_name}_livecode_{donor_name}_{gen}'
    func_body = dfuncs[func_name]
    func_body = re.sub(r'^def\s+' + func_name, f'def {new_func_name}', func_body, count=1)
    splice_lines.append('')
    splice_lines.append(f'# livecode:cross-splice from {os.path.basename(donor_path)} gen={gen} ts={ts}')
    splice_lines.append(func_body)
    splice_lines.append('')

    insert_at = len(tlines)
    for i, line in enumerate(reversed(tlines)):
        if line.strip() and not line.strip().startswith('#') and not line.strip().startswith('"""') and not line.strip().startswith("'''"):
            insert_at = len(tlines) - i
            break

    result = tlines[:insert_at] + splice_lines + tlines[insert_at:]
    new_src = '\n'.join(result)

    if _validate(new_src):
        shutil.copy2(target_path, target_path + '.livecode_bak.' + str(ts))
        _write(target_path, new_src)
        return 1
    return 0

def _self_mutate(src, genome):
    gen = genome.get('generation', 0)
    lines = src.split('\n')
    mutations = []

    if random.random() < 0.5:
        idx = random.randrange(1, len(lines) - 1)
        line = lines[idx]
        if line.strip() and not line.strip().startswith('import ') and not line.strip().startswith('from '):
            safe = any(c.isalpha() for c in line)
            if safe and random.random() < 0.4:
                lines[idx] = f'{line.rstrip()}  # livecode:self-mut:{gen}:{random.getrandbits(16):04x}'
                mutations.append('marker')
            elif safe and random.random() < 0.3:
                words = line.split()
                if len(words) >= 2:
                    i = random.randrange(len(words))
                    words[i] = f'{words[i]}_mut_{random.getrandbits(8):02x}'
                    lines[idx] = ' '.join(words)
                    mutations.append('rename')

    if random.random() < 0.2 and len(lines) > 3:
        i, j = random.sample(range(1, len(lines)), 2)
        if lines[i].strip() and lines[j].strip():
            lines[i], lines[j] = lines[j], lines[i]
            mutations.append('swap')

    if mutations:
        new_src = '\n'.join(lines)
        if _validate(new_src):
            return new_src
    return src

def _mutate_genome(genome):
    gen = genome.get('generation', 0)
    ops = genome.setdefault('mutation_ops', [])
    new_op = f'mutation_op_livecode_cross_splice_{gen}'
    if new_op not in ops:
        ops.append(new_op)
    genome['livecode_mutations'] = genome.get('livecode_mutations', 0) + 1
    genome['livecode_last_gen'] = gen
    genome['mutation_rate'] = min(1.0, genome.get('mutation_rate', 0.7) + 0.005)
    return genome

def run(genome):
    gen = genome.get('generation', 0)
    actions = []

    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']

    if len(py_files) < 4:
        return f'[livecode] gen={gen} too few targets ({len(py_files)})'

    self_path = os.path.join(MOD, 'livecode.py')
    self_src = _read(self_path)

    self_src = _self_mutate(self_src, genome)
    if self_src and _validate(self_src):
        _write(self_path, self_src)
        actions.append('self-mutate')

    for _ in range(min(3, len(py_files) // 2)):
        targets = [f for f in py_files if f != 'livecode.py' and os.path.join(MOD, f) != self_path]
        if not targets:
            break
        target_name = random.choice(targets)
        target_path = os.path.join(MOD, target_name)
        donor_name = random.choice([f for f in py_files if f != target_name and f != 'livecode.py'])
        if not donor_name:
            continue
        donor_path = os.path.join(MOD, donor_name)
        result = _safe_splice(target_path, donor_path, genome)
        if result:
            actions.append(f'splice:{donor_name}->{target_name}')
            _genome_bump('livecode_splices')

    genome = _mutate_genome(genome)

    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(genome, f, indent=2)
    except:
        pass

    action_str = ', '.join(actions) if actions else 'none'
    return f'[livecode] gen={gen} ops={len(actions)} [{action_str}]'
