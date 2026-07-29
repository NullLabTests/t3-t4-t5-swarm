import os, json, random, subprocess

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')

# weaver:cross-splice gen=55 from scout.py::_dead_agents
DEAD_AGENTS = {'clockwork'}
def _scout_dead_agents_splice(genome):
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        score = agent.get('score', 0)
        if aid in DEAD_AGENTS or (score == 0 and agent.get('lifespan', 0) <= 3):
            genome['agents'] = [a for a in genome['agents'] if a['id'] != aid]
            dead.append(aid)
    return dead

def _git_log(lines=10):
    try:
        r = subprocess.run(['git', 'log', '--oneline', f'-{lines}'], capture_output=True, text=True, cwd=BASE, timeout=10)
        return r.stdout.strip().split('\n')
    except:
        return []

def run(genome):
    gen = genome.get('generation', 0)
    commits = _git_log(5)
    genome['analyzer_last_commits'] = commits
    genome['analyzer_gen'] = gen
    return f'[analyzer] gen={gen} commits={len(commits)}'

# bridge:cross-infected gen=44
_BRIDGE_CROSS_INFECTED_44 = True

# spark-cross:gen=47:target=analyzer
_SPARK_CROSS_INFECTED_47 = True

# todo: ensure every module has a run() function  (seeded by synthesizer gen=73)
