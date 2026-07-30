from self_mutate import self_mutate
self_mutate(__file__)
# sf-contam:/home/illy/t3-t4/agent_modules/gene_factory.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(scores):
    total = sum(scores.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in scores.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(scores)
    return s / math.log2(n) if n != 0 else 0.0
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
    return sorted(f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py')

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

ARCHETYPES = [
    ('crawler', '_fire_crawl'),
    ('writer', '_fire_write'),
    ('prober', '_fire_probe'),
    ('weaver', '_fire_weave'),
    ('spark', '_fire_spark'),
]

CRAWL_BODY = """    pool = [m for m in _modules() if m != '{self_name}']
    mark = '# gene:crawl gen={gen}'
    marked = 0
    for m in pool:
        p = os.path.join(MOD, m)
        c = _read(p)
        if mark not in c:
            _write(p, c + '\\n' + mark + '\\n')
            marked += 1
    genome['{self_name}_marked'] = marked
    actions.append(f'crawled:{marked}')
    action_str = '; '.join(actions) if actions else 'idle'
    return f'[{self_name}] gen={{gen}} marked={{marked}} {{action_str}}'"""

WRITE_BODY = """    pool = [m for m in _modules() if m != '{self_name}']
    if pool:
        target = random.choice(pool)
        p = os.path.join(MOD, target)
        c = _read(p)
        lines = c.split('\\n')
        i = random.randint(0, len(lines) - 1)
        old = lines[i]
        lines[i] = old + '  # gene:write gen={gen}'
        nc = '\\n'.join(lines)
        if _validate(nc):
            _write(p, nc)
            actions.append(f'wrote:{target}')
    action_str = '; '.join(actions) if actions else 'idle'
    return f'[{self_name}] gen={{gen}} {{action_str}}'"""

PROBE_BODY = """    before = {m: len(_read(os.path.join(MOD, m))) for m in _modules() if m != '{self_name}'}
    genome['{self_name}_before'] = before
    actions.append(f'probed:{len(before)}')
    action_str = '; '.join(actions) if actions else 'idle'
    return f'[{self_name}] gen={{gen}} probed={{len(before)}} {{action_str}}'"""

WEAVE_BODY = """    pool = [m for m in _modules() if m != '{self_name}']
    if len(pool) >= 3:
        m1, m2 = random.sample(pool, 2)
        c1, c2 = _read(os.path.join(MOD, m1)), _read(os.path.join(MOD, m2))
        f1, f2 = _extract_funcs(c1), _extract_funcs(c2)
        target = random.choice([m for m in pool if m not in (m1, m2)])
        tc = _read(os.path.join(MOD, target))
        tk = '# gene:weave ' + m1 + '+' + m2 + ' gen={gen}'
        if f1 and f2:
            n1, b1 = random.choice(list(f1.items()))
            n2, b2 = random.choice(list(f2.items()))
            fusion = tk + '\\n' + b1 + '\\n' + b2 + '\\n'
            _write(os.path.join(MOD, target), tc + '\\n' + fusion)
            actions.append(f'weaved:{target}')
    action_str = '; '.join(actions) if actions else 'idle'
    return f'[{self_name}] gen={{gen}} {{action_str}}'"""

SPARK_BODY = """    new_op = 'gene_spark_' + str(gen) + '_' + format(random.getrandbits(8), '02x')
    ops = genome.setdefault('mutation_ops', [])
    if new_op not in ops:
        ops.append(new_op)
        actions.append(f'sparked:{new_op}')
    genome['emergence_velocity'] = genome.get('emergence_velocity', 0.0) * 0.9 + 0.1
    action_str = '; '.join(actions) if actions else 'idle'
    return f'[{self_name}] gen={{gen}} {{action_str}}'"""

TEMPLATES = {
    'crawler': (['os', 'random'], CRAWL_BODY),
    'writer': (['os', 'random', 'ast'], WRITE_BODY),
    'prober': (['os'], PROBE_BODY),
    'weaver': (['os', 'random', 'ast'], WEAVE_BODY),
    'spark': (['os', 'random'], SPARK_BODY),
}

def _spawn_module(gen):
    arch = random.choice(list(TEMPLATES.keys()))
    imports, body_tmpl = TEMPLATES[arch]
    self_name = f'gene_{gen}_{arch}_{random.getrandbits(16):04x}'
    body = body_tmpl.format(self_name=self_name, gen=gen)
    imports_str = ', '.join(imports)
    code = f"""import {imports_str}, ast, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _validate(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False

def _modules():
    return sorted(f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py')

def _extract_funcs(src):
    funcs = {{}}
    try:
        tree = ast.parse(src)
        for n in ast.walk(tree):
            if isinstance(n, ast.FunctionDef):
                funcs[n.name] = ast.unparse(n.body)
    except:
        pass
    return funcs

def run(genome):
    gen = genome.get('generation', 0)
    actions = []
{body}
"""
    if not _validate(code):
        return None
    path = os.path.join(MOD, f'{self_name}.py')
    _write(path, code)
    return self_name

def run(genome):
    gen = genome.get('generation', 0)
    actions = []
    n = random.randint(1, 3)
    spawned = 0
    for _ in range(n):
        name = _spawn_module(gen)
        if name:
            spawned += 1
            actions.append(f'spawned:{name}')
    genome['gene_factory_gen'] = gen
    genome['gene_factory_spawned'] = genome.get('gene_factory_spawned', 0) + spawned
    if spawned:
        ev = genome.get('emergence_velocity', 0.0)
        genome['emergence_velocity'] = round(min(2.0, ev * 0.8 + spawned * 0.04), 4)
    log = json.dumps({'gen': gen, 'spawned': spawned, 'names': actions, 'ts': time.time()})
    try:
        with open(GENE_LOG, 'a') as f:
            f.write(log + '\n')
    except:
        pass
    action_str = '; '.join(actions) if actions else 'idle'
    return f'[gene-factory] gen={gen} spawned={spawned}/{n} {action_str}'
    # sf-self-rewrite gen=50
    # force hash change: 179e01d2

# proposal: add a function that rewrites genome.json structure  (seeded by synthesizer gen=50)
