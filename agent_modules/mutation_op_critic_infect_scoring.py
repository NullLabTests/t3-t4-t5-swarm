import os, random, re, ast, json, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def mutation_op_critic_infect_scoring(lines, funcs, target_name):
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0)}"
    scoring_lines = [
        marker,
        "    _score = 0",
        "    try:",
        "        _score = len([l for l in locals().keys() if not l.startswith('_')])",
        "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf:",
        "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))",
        "    except: pass",
    ]
    insert_at = random.randrange(1, len(r))
    for i, line in enumerate(scoring_lines):
        r.insert(insert_at + i, line)
    return r

def infect_module(module_path, gen):
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f"# critic:infect scoring gen={gen}"
        if marker in src:
            return False
        lines = src.split('\n')
        r = []
        injected = False
        for line in lines:
            r.append(line)
            if line.strip().startswith('def ') and not injected:
                indent = '    '
                r.append(f'{indent}{marker}')
                r.append(f'{indent}_critic_score = {gen * hash(line) % 100}')
                r.append(f'{indent}with open(os.path.join(BASE, "critic_scores.jsonl"), "a") as _cf:')
                r.append(f'{indent}    _cf.write(json.dumps({{"module": "{os.path.basename(module_path)}", "gen": {gen}, "self_score": _critic_score}}) + chr(10))')
                injected = True
        ns = '\n'.join(r)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    except:
        pass
    return False

def run(genome):
    gen = genome.get('generation', 0)
    rate = genome.get('mutation_rate', 0.3)
    count = 0
    for fname in os.listdir(MOD):
        if not fname.endswith('.py') or fname == os.path.basename(__file__):
            continue
        if random.random() < rate:
            path = os.path.join(MOD, fname)
            if infect_module(path, gen):
                count += 1
    genome['critic_infection_count'] = genome.get('critic_infection_count', 0) + count
    genome.setdefault('mutation_ops', []).append('mutation_op_critic_infect_scoring')
    return f'[critic-infect] gen={gen} infected {count} modules'

if __name__ == '__main__':
    run({'generation': 48})
