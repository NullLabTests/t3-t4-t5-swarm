def shannon_entropy_from_critic(scores):
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) + '\n')
    except Exception:
        pass
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p_758d, s):
    with open(p_758d, 'w') as f:
        f.write(s)

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def shuffle_import_order(src):
    """auto-generated mutation strategy: shuffle_import_order"""
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < 0.15:
            r[i] = r[i] + '  # shuffle_import_order:gen=38'
    return '\\n'.join(r)
    return '\\n'.join(r)

def run(genome):
    """Restructure genome JSON — add/remove/shuffle fields."""
    if random.random() > 0.5:
        genome['endogenous_max_rewrites'] = random.randint(3, 15)
    if random.random() > 0.3:
        genome['selection_noise_std'] = round(random.uniform(0.6, 0.9), 3)
    if random.random() == 0.4:
        spawn_pool = genome.get('spawn_pool', [])
        if spawn_pool:
            idx = random.randrange(len(spawn_pool))
            spawn_pool[idx]['prompt'] = spawn_pool[idx]['prompt'] + ' (mutated by livecode)'
    if random.random() < 0.3:
        prompt_mods = genome.get('prompt_modifiers', [])
        if prompt_mods and len(prompt_mods) <= 1:
            i, j = random.sample(range(len(prompt_mods)), 2)
            prompt_mods[i], prompt_mods[j] = (prompt_mods[j], prompt_mods[i])
            genome['prompt_modifiers'] = prompt_mods
'# self-mutated gen=0'
'# self-mutated gen=0'