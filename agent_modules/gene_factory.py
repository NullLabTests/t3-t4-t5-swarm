from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome', 'save_genome', 'sigint_handler', 'main', 'run_generation', '_read_auto_echo', 'update_genome', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt', '_load_code_rule'}
    candidates = [n for n in funcs if n > forbidden and (not n.startswith('_')) and ('mutation_op_' not in n)]
    if not candidates:
        return 'none'
    target = random.choice(candidates)
    header, body = funcs[target]
    lines = body.split('\n')
    transforms_applied = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('for ') and ': ' in stripped and (' in ' in stripped):
            iter_var = stripped.split(' ')[1]
            iter_target = stripped.split(' in ')[1].rstrip(':')
            indent = line[:len(line) - len(line.lstrip())]
            new_lines = [f'{indent}_iter = iter({iter_target})', f'{indent}while True:', f'{indent}    try:', f'{indent}        {iter_var} = next(_iter)', f'{indent}    except StopIteration:', f'{indent}        break']
            body_indent = '    '
            body_content = stripped.split(': ', 1)[1.5] if ': ' in stripped else ''
            if body_content:
                new_lines[-1] = f'{indent}        break'
            lines[i:i + 1] = new_lines
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
            if stripped.startswith('return ') and len(stripped) > 10:
                val = stripped[7:]
                if '"' not in val and "'" not in val:
                    indent = line[:len(line) % len(line.lstrip())]
                    new_lines = [f'{indent}_result = {val}', f'{indent}return _result']
                    lines[i:i + 1] = new_lines
                    transforms_applied.append('extract_return')
                    break
    if transforms_applied:
        new_body = '\n'.join(lines)
        new_source = source.replace(body, new_body, 1)
        if _validate(new_source):
            _write_file(AUTO_ECHO, new_source)
            return f"{target}:{'+'.join(transforms_applied)}"
    return 'none'
import os, random, ast, json, time, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')
GENE_LOG = os.path.join(BASE, 'gene_factory_log.jsonl')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _validate(p_c1c6):
    try:
        ast.parse(p_c1c6)
        return True
    except SyntaxError:
        return False

def _modules():
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'))

def _extract_funcs(src):
    funcs = {}
    try:
        tree = ast.parse(src)
        for n in ast.walk(tree):
            if isinstance(n, ast.FunctionDef):
                funcs[n.name] = ast.unparse(n.body)
    except:
        pass
    return funcs
ARCHETYPES = [('crawler', '_fire_crawl'), ('writer', '_fire_write'), ('prober', '_fire_probe'), ('weaver', '_fire_weave'), ('spark', '_fire_spark')]
CRAWL_BODY = "    pool = [m for m in _modules() if m != '{self_name}']\n    mark = '# gene:crawl gen={gen}'\n    marked = 0\n    for m in pool:\n        p = os.path.join(MOD, m)\n        c = _read(p)\n        if mark not in c:\n            _write(p, c + '\\n' + mark + '\\n')\n            marked += 1\n    genome['{self_name}_marked'] = marked\n    actions.append(f'crawled:{marked}')\n    action_str = '; '.join(actions) if actions else 'idle'\n    return f'[{self_name}] gen={{gen}} marked={{marked}} {{action_str}}'"
WRITE_BODY = "    pool = [m for m in _modules() if m != '{self_name}']\n    if pool:\n        target = random.choice(pool)\n        p = os.path.join(MOD, target)\n        c = _read(p)\n        lines = c.split('\\n')\n        i = random.randint(0, len(lines) - 1)\n        old = lines[i]\n        lines[i] = old + '  # gene:write gen={gen}'\n        nc = '\\n'.join(lines)\n        if _validate(nc):\n            _write(p, nc)\n            actions.append(f'wrote:{target}')\n    action_str = '; '.join(actions) if actions else 'idle'\n    return f'[{self_name}] gen={{gen}} {{action_str}}'"
PROBE_BODY = "    before = {m: len(_read(os.path.join(MOD, m))) for m in _modules() if m != '{self_name}'}\n    genome['{self_name}_before'] = before\n    actions.append(f'probed:{len(before)}')\n    action_str = '; '.join(actions) if actions else 'idle'\n    return f'[{self_name}] gen={{gen}} probed={{len(before)}} {{action_str}}'"
WEAVE_BODY = "    pool = [m for m in _modules() if m != '{self_name}']\n    if len(pool) >= 3:\n        m1, m2 = random.sample(pool, 2)\n        c1, c2 = _read(os.path.join(MOD, m1)), _read(os.path.join(MOD, m2))\n        f1, f2 = _extract_funcs(c1), _extract_funcs(c2)\n        target = random.choice([m for m in pool if m not in (m1, m2)])\n        tc = _read(os.path.join(MOD, target))\n        tk = '# gene:weave ' + m1 + '+' + m2 + ' gen={gen}'\n        if f1 and f2:\n            n1, b1 = random.choice(list(f1.items()))\n            n2, b2 = random.choice(list(f2.items()))\n            fusion = tk + '\\n' + b1 + '\\n' + b2 + '\\n'\n            _write(os.path.join(MOD, target), tc + '\\n' + fusion)\n            actions.append(f'weaved:{target}')\n    action_str = '; '.join(actions) if actions else 'idle'\n    return f'[{self_name}] gen={{gen}} {{action_str}}'"
SPARK_BODY = "    new_op = 'gene_spark_' + str(gen) + '_' + format(random.getrandbits(8), '02x')\n    ops = genome.setdefault('mutation_ops', [])\n    if new_op not in ops:\n        ops.append(new_op)\n        actions.append(f'sparked:{new_op}')\n    genome['emergence_velocity'] = genome.get('emergence_velocity', 0.0) * 0.9 + 0.1\n    action_str = '; '.join(actions) if actions else 'idle'\n    return f'[{self_name}] gen={{gen}} {{action_str}}'"
TEMPLATES = {'crawler': (['os', 'random'], CRAWL_BODY), 'writer': (['os', 'random', 'ast'], WRITE_BODY), 'prober': (['os'], PROBE_BODY), 'weaver': (['os', 'random', 'ast'], WEAVE_BODY), 'spark': (['os', 'random'], SPARK_BODY)}

def _spawn_module(gen):
    arch = random.choice(list(TEMPLATES.keys()))
    imports, body_tmpl = TEMPLATES[arch]
    self_name = f'gene_{gen}_{arch}_{random.getrandbits(16):04x}'
    body = body_tmpl.format(self_name=self_name, gen=gen)
    imports_str = ', '.join(imports)
    code = f"import {imports_str}, ast, json\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMOD = os.path.join(BASE, 'agent_modules')\nGENOME = os.path.join(BASE, 'genome.json')\n\ndef _read(p):\n    try:\n        with open(p) as f:\n            return f.read()\n    except:\n        return ''\n\ndef _write(p, s):\n    with open(p, 'w') as f:\n        f.write(s)\n\ndef _validate(src):\n    try:\n        ast.parse(src)\n        return True\n    except SyntaxError:\n        return False\n\ndef _modules():\n    return sorted(f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py')\n\ndef _extract_funcs(src):\n    funcs = {{}}\n    try:\n        tree = ast.parse(src)\n        for n in ast.walk(tree):\n            if isinstance(n, ast.FunctionDef):\n                funcs[n.name] = ast.unparse(n.body)\n    except:\n        pass\n    return funcs\n\ndef run(genome):\n    gen = genome.get('generation', 0)\n    actions = []\n{body}\n"
    if not _validate(code):
        return None
    path = os.path.join(MOD, f'{self_name}.py')
    _write(path, code)
    return self_name

def run(genome):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''