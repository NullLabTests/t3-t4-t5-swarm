import os, json, random, subprocess

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')

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
