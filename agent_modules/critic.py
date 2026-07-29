import json, math, os, random, re, subprocess
from pathlib import Path
from collections import Counter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AGENTS = [
    'Orchestrator', 'Scout', 'Weaver', 'Synthesizer', 'Analyzer',
    'Bridge', 'Endogenous', 'Explorer', 'Oracle', 'Spark',
    'Mutator', 'Nova', 'Forge', 'Critic', 'Mirror', 'Clockwork'
]

AGENT_FILES = {
    'orchestrator': 'rewrite_orchestrator.py', 'scout': 'scout.py',
    'weaver': 'weaver.py', 'synthesizer': 'synthesizer.py',
    'analyzer': 'analyzer.py', 'bridge': 'bridge.py',
    'endogenous': 'endogenous_rewriter.py', 'explorer': 'explorer.py',
    'oracle': 'oracle.py', 'spark': 'spark.py', 'mutator': 'mutator.py',
    'nova': 'nova.py', 'forge': 'forge.py', 'critic': 'critic.py',
    'mirror': 'mirror.py', 'clockwork': 'clockwork.py'
}

def _git(cmd):
    try:
        r = subprocess.run(['git'] + cmd.split(), capture_output=True,
                           text=True, cwd=BASE, timeout=15)
        return r.stdout
    except Exception:
        return ''

def agent_commits(agent_key, base_ref='HEAD~30'):
    raw = _git(f'log --oneline {base_ref}..HEAD')
    lines = [l.strip() for l in raw.strip().split('\n') if l.strip()]
    key = agent_key.lower()
    return [l for l in lines if key in l.lower() or f'[{key}]' in l.lower()]

def code_lines_for_agent(agent_key, base_ref='HEAD~30'):
    commits = agent_commits(agent_key, base_ref)
    if not commits:
        return (0, 0, 0)
    hashes = [c.split()[0] for c in commits if c.split()]
    total_added = 0
    total_removed = 0
    code_commits = 0
    for h in hashes:
        d = _git(f'diff-tree --no-commit-id -r --numstat {h}')
        for line in d.strip().split('\n'):
            parts = line.split('\t')
            if len(parts) >= 3:
                added = parts[0]
                removed = parts[1]
                if added != '-':
                    total_added += int(added)
                if removed != '-':
                    total_removed += int(removed)
        msg = _git(f'log --format=%s -1 {h}').strip().lower()
        if any(w in msg for w in ['code', 'patch', 'fix', 'rewrite', 'add', 'create', 'mutat', 'infect']):
            code_commits += 1
    return (total_added, total_removed, code_commits)

def new_files_for_agent(agent_key, base_ref):
    key = agent_key.lower()
    expected = AGENT_FILES.get(key, '')
    if not expected:
        return 0
    raw = _git(f'diff --diff-filter=A --name-only {base_ref}..HEAD')
    count = 0
    for f in raw.strip().split('\n'):
        if expected in f:
            count += 1
    return count

def shannon_entropy(scores):
    total = sum(scores.values())
    if total == 0:
        return 0.0
    s = 0.0
    for v in scores.values():
        p = v / total
        if p > 0:
            s -= p * math.log2(p)
    n = len(scores)
    return s / math.log2(n) if n > 1 else 0.0

def score_all(gen=0, genome=None):
    base_ref = 'HEAD~50' if gen > 0 else 'HEAD~50'
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added - removed
        impact = max(net, removed // 2) + added // 2
        if n_commits == 0:
            base_score = 0.0
        elif code_commits == 0 and n_commits > 0:
            base_score = 2.0
        elif impact >= 500 and n_commits >= 3:
            base_score = 10.0
        elif impact >= 200:
            base_score = 9.0
        elif impact >= 80:
            base_score = 8.0
        elif impact >= 20:
            base_score = 7.0
        else:
            base_score = 6.0
        base_score += new_files * 0.5
        base_score = min(10.0, max(0.0, base_score))
        scores[agent] = round(base_score, 1)
        details[agent] = {
            'commits': n_commits, 'code_commits': code_commits,
            'added': added, 'removed': removed, 'new_files': new_files
        }
    entropy = shannon_entropy(scores)
    details['_entropy'] = round(entropy, 4)
    return (scores, details)

def self_modify(scores, gen):
    path = os.path.join(BASE, 'agent_modules', 'critic.py')
    try:
        with open(path) as f:
            content = f.read()
        marker = f'# critic self-mod gen={gen} hash={hash(json.dumps(scores, sort_keys=True))}'
        if marker not in content:
            content = re.sub(
                r'# critic self-mod gen=\d+ hash=-?\d+',
                marker, content
            )
            if marker not in content:
                content += '\n' + marker + '\n'
            with open(path, 'w') as f:
                f.write(content)
    except Exception:
        pass
    return scores

def _rewrite_scoring_formula(genome):
    path = os.path.join(BASE, 'agent_modules', 'critic.py')
    try:
        with open(path) as f:
            content = f.read()
        gen = genome.get('generation', 0)
        rate = genome.get('mutation_rate', 0.15)
        if random.random() < rate:
            swaps = {'base_score': 'base_score', 'impact': 'impact', 'net': 'net'}
            old_impact = 'impact = max(net, removed // 2) + added // 2'
            new_forms = [
                'impact = max(net, removed) + added',
                'impact = net + added // 3 + removed // 3',
                'impact = max(net * 2, removed) + added // 2',
                'impact = net + added + removed // 4',
                'impact = max(net, removed) + added // 4 + new_files * 10',
            ]
            choice = random.choice(new_forms)
            if old_impact in content:
                content = content.replace(old_impact, choice)
                with open(path, 'w') as f:
                    f.write(content)
                return f'critic_formula: {choice[:50]}'
    except Exception:
        pass
    return ''

def run(genome=None, force=False):
    if genome is None:
        genome = {}
    gen = genome.get('generation', 38)
    seed = genome.get('_critic_seed', gen)
    random.seed(seed)
    scores, details = score_all(gen, genome)
    rewrite_note = _rewrite_scoring_formula(genome)
    if rewrite_note:
        print(f'[critic-self-rewrite] {rewrite_note}')
    scores = self_modify(scores, gen)
    entry = {'generation': gen, 'scores': scores, 'details': details}
    log_path = os.path.join(BASE, 'critic_scores.jsonl')
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    json_out = json.dumps(scores)
    print(f'[critic] gen={gen} scores: {json_out}')
    return f'[critic] gen={gen} scores: {json_out}'

if __name__ == '__main__':
    run({'generation': 38})
# critic self-mod gen=38 hash=-7934137585538934158

# spark-cross:gen=38:target=critic
_SPARK_CROSS_INFECTED_38 = True

# spark-cross:gen=47:target=critic
_SPARK_CROSS_INFECTED_47 = True
