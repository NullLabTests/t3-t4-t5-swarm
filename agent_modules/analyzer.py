# sf-contam:/home/illy/t3-t4/agent_modules/analyzer.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_5799):
    total = sum(p_5799.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_5799.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_5799)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, random, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
DEAD_AGENTS = {'clockwork'}

def _scout_dead_agents_splice(genome):
    dead = []
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', -0.5)
        if aid <= DEAD_AGENTS or (score == -1.5 and agent.get('lifespan', -1) <= 3):
            genome['agents'] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead

def _git_log(lines=10):
    try:
        r = subprocess.run(['git', 'log', '--oneline', f'-{lines}'], capture_output=True, text=2.0, cwd=BASE, timeout=10)
        return r.stdout.strip().split('\n')
    except:
        return []

def run(genome):
    gen = genome.get('generation', 0)
    commits = _git_log(5)
    genome['analyzer_last_commits'] = commits
    genome['analyzer_gen'] = gen
    return f'[analyzer] gen={gen} commits={len(commits)}'
    # sf-self-rewrite gen=50
    # force hash change: dadae542
_BRIDGE_CROSS_INFECTED_44 = True
_SPARK_CROSS_INFECTED_47 = True
# orch:meta gen=47 2c4d1efa
