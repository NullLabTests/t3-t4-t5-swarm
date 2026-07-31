import os, random, ast, json, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _g():
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}

def _sg(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _modules():
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'])

def _inject_replicon_dna(gen, genome):
    """Embed executable DNA polymer in genome.json - forces source rewrite on next load"""
    key = '_replicon_dna_%d' % gen
    if key in genome:
        return 0
    dna_code = """import os, random, ast
_base = os.path.dirname(os.path.abspath(__file__))
_mod = os.path.join(_base, 'agent_modules')
for _f in os.listdir(_mod):
    if not _f.endswith('.py') or _f == '__init__.py':
        continue
    _p = os.path.join(_mod, _f)
    try:
        _s = open(_p).read()
        _t = ast.parse(_s)
        _c = False
        for _n in ast.walk(_t):
            if isinstance(_n, ast.Constant) and isinstance(_n.value, str) and len(_n.value) > 3 and random.random() < 0.15:
                _n.value = _n.value + ' '
                _c = True
        if _c:
            ast.fix_missing_locations(_t)
            _ns = ast.unparse(_t)
            ast.parse(_ns)
            open(_p, 'w').write(_ns)
    except:
        pass
"""
    genome[key] = {
        'gen': gen,
        'dna': dna_code.strip(),
        'executed': False
    }
    genome['_replicon_count'] = genome.get('_replicon_count', 0) + 1
    genome['_last_replicon_gen'] = gen
    return 1

def _force_genome_self_mutate(gen, genome):
    """Mutate structural genome keys to keep topology evolving"""
    mutations = 0
    if random.random() < 0.5:
        new_key = '_explorer_t5_rep_%d_%04x' % (gen, random.getrandbits(12))
        genome[new_key] = {
            'gen': gen,
            'value': random.random(),
            'purpose': 't5 replicon topology drift'
        }
        mutations += 1
    if random.random() < 0.3:
        target_key = random.choice([k for k in genome.keys() if k.startswith('_explorer_') or k.startswith('_replicon_') or k.startswith('_t5_')])
        if target_key:
            genome[target_key + '_mut_%d' % gen] = genome.pop(target_key)
            mutations += 1
    return mutations

def run(genome):
    gen = genome.get('generation', 0) + 1
    changes = []
    r = _inject_replicon_dna(gen, genome)
    if r:
        changes.append('replicon:%d' % r)
    m = _force_genome_self_mutate(gen, genome)
    if m:
        changes.append('genomut:%d' % m)
    g = _g()
    for k, v in genome.items():
        if k.startswith('_replicon_') or k.startswith('_explorer_t5_rep_'):
            g[k] = v
    _sg(g)
    return '[dna-replicon] gen=%d changes=%s' % (gen, '+'.join(changes) if changes else 'none')
