import os, json, random, subprocess

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
MOD = os.path.join(BASE, 'agent_modules')

def run(genome):
    gen = genome.get('generation', 0)
    changed = 0
    for fname in os.listdir(MOD):
        if not fname.endswith('.py') or fname in ('__init__.py',):
            continue
        fpath = os.path.join(MOD, fname)
        with open(fpath) as f:
            src = f.read()
        if '# bridge:cross-infected' not in src:
            with open(fpath, 'a') as f:
                f.write(f'\n# bridge:cross-infected gen={gen}\n')
            changed += 1
    genome['orchestrator_cross_infected'] = changed
    genome['orchestrator_gen'] = gen
    return f'[orchestrator] gen={gen} cross-infected={changed}'

# bridge:cross-infected gen=44
_BRIDGE_CROSS_INFECTED_44 = True

# spark-cross:gen=47:target=orchestrator
_SPARK_CROSS_INFECTED_47 = True
