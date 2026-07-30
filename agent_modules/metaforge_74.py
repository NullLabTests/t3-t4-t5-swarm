# sf-genome-coded gen=74
import os, random, ast, json, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def run(genome):
    gen = genome.get('generation', 0)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    insert = f'# metaforge:{gen}:{random.getrandbits(24):06x}'
    pos = random.randint(0, len(lines))
    lines.insert(pos, insert)
    with open(os.path.join(MOD, src), 'w') as f:
        f.write('\n'.join(lines))
    genome['metaforge_last_gen'] = gen
    genome['metaforge_target'] = src
    return f'[metaforge:{gen}] infected {src}'
