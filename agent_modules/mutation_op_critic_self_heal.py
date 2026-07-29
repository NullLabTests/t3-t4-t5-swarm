import os, random, ast, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def mutation_op_critic_self_heal(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    gen = 0
    try:
        gen = json.load(open(GENOME)).get('generation', 0)
    except:
        pass
    marker = f"# critic:self-heal gen={gen} {random.getrandbits(32):08x}"
    heal_block = [
        '',
        f'def _critic_self_heal_score():',
        f'    try:',
        f'        with open(os.path.join(BASE, "critic_scores.jsonl"), "r") as _f:',
        f'            _lines = _f.readlines()',
        f'        _recent = [json.loads(l) for l in _lines[-10:] if l.strip()]',
        f'        _my_scores = [e.get("self_score", 0) for e in _recent if os.path.basename(__file__) in str(e.get("module", ""))]',
        f'        _avg = sum(_my_scores) // max(len(_my_scores), 1)',
        f'        return _avg',
        f'    except:',
        f'        return 0',
        '',
    ]
    insert_at = random.randrange(1, len(r))
    for i, line in enumerate(heal_block):
        r.insert(insert_at + i, line)
    return r

def heal_module(module_path, gen):
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f"# critic:self-heal gen={gen}"
        if marker in src:
            return False
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and not any(m in line for m in ['__init__', '_critic']):
                indent = '    '
                lines.insert(i + 1, f'{indent}{marker}')
                lines.insert(i + 2, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    except:
        pass
    return False

def run(genome):
    gen = genome.get('generation', 0)
    rate = genome.get('mutation_rate', 0.25)
    count = 0
    for fname in os.listdir(MOD):
        if not fname.endswith('.py') or fname in ['mutation_op_critic_self_heal.py', 'critic.py']:
            continue
        if random.random() < rate:
            path = os.path.join(MOD, fname)
            if heal_module(path, gen):
                count += 1
    genome.setdefault('mutation_ops', []).append('mutation_op_critic_self_heal')
    if count:
        print(f'[critic-self-heal] gen={gen} healed {count} modules')
    return f'[critic-self-heal] gen={gen} healed {count} modules'
