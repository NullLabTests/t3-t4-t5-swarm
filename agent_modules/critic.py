import os
import json
import subprocess
import random
from pathlib import Path

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _commits_by_prefix(prefix, since_ref="HEAD~50"):
    try:
        result = subprocess.run(
            ["git", "log", "--oneline", since_ref + "..HEAD"],
            capture_output=True, text=True, cwd=BASE, timeout=15
        )
        lines = [l.strip() for l in result.stdout.strip().split("\n") if l.strip()]
        return [l for l in lines if l.lower().startswith(prefix.lower()) or f"[{prefix.lower()}]" in l.lower()]
    except Exception:
        return []

def _count_modified_files(since_ref="HEAD~50"):
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", since_ref, "HEAD"],
            capture_output=True, text=True, cwd=BASE, timeout=15
        )
        return len([l for l in result.stdout.strip().split("\n") if l.strip()])
    except Exception:
        return 0

def _file_changed_lines(filepath):
    try:
        result = subprocess.run(
            ["git", "diff", "HEAD~50", "HEAD", "--", filepath],
            capture_output=True, text=True, cwd=BASE, timeout=15
        )
        additions = 0
        for line in result.stdout.split("\n"):
            if line.startswith("+") and not line.startswith("+++"):
                additions += 1
        return additions
    except Exception:
        return 0

AGENTS = [
    "Orchestrator", "Scout", "Weaver", "Synthesizer", "Analyzer",
    "Bridge", "Endogenous", "Explorer", "Oracle", "Spark",
    "Mutator", "Nova", "Forge", "Critic"
]

AGENT_GREP_KEYWORDS = {
    "Orchestrator": "orchestrator",
    "Scout": "scout",
    "Weaver": "weaver",
    "Synthesizer": "synthesizer",
    "Analyzer": "analyzer",
    "Bridge": "bridge",
    "Endogenous": "endogenous",
    "Explorer": "explorer",
    "Oracle": "oracle",
    "Spark": "spark",
    "Mutator": "mutator",
    "Nova": "nova",
    "Forge": "forge",
    "Critic": "critic",
}

_RUNTIME_CACHE = {}

def score_all():
    scores = {}
    agent_commit_map = {}
    for agent in AGENTS:
        prefix = AGENT_GREP_KEYWORDS.get(agent, agent.lower())
        commits = _commits_by_prefix(prefix)
        agent_commit_map[agent] = commits
    total_commits = sum(len(v) for v in agent_commit_map.values())
    for agent in AGENTS:
        commits = agent_commit_map[agent]
        n = len(commits)
        if n >= 3:
            base = 10
        elif n == 2:
            base = 9
        elif n == 1:
            base = 8
        elif total_commits > 0:
            base = 5
        else:
            base = 3
        penalty = max(0, n - 5) * 0.5
        bonus = 0
        for c in commits:
            if "+code" in c.lower() or "#patch" in c.lower():
                bonus += 0.5
            if "push" in c.lower():
                bonus += 0.3
        scores[agent] = min(10, base + bonus - penalty)
    scores = {k: round(v, 1) for k, v in scores.items()}
    return scores

CRITIC_THRESHOLD = 5.0

def _self_modify(scores):
    path = os.path.join(BASE, "agent_modules", "critic.py")
    try:
        with open(path) as f:
            content = f.read()
        min_agent = min(scores, key=scores.get)
        max_agent = max(scores, key=scores.get)
        global CRITIC_THRESHOLD
        CRITIC_THRESHOLD = scores[min_agent]
        score_variance = max(scores.values()) - min(scores.values())
        if score_variance < 1.0:
            for agent in scores:
                if scores[agent] > 5:
                    scores[agent] = max(1, scores[agent] - 2)
        return scores
    except Exception as e:
        print(f"[critic] self_modify error: {e}")
        return scores

def run(genome):
    gen = genome.get("generation", 0)
    scores = score_all()
    scores = _self_modify(scores)
    entry = {"generation": gen, "scores": scores}
    log_path = os.path.join(BASE, "critic_scores.jsonl")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a") as f:
        f.write(json.dumps(entry) + "\n")
    json_out = json.dumps(scores)
    print(f"[critic] gen={gen} scores: {json_out}")
    return f"[critic] gen={gen} scores: {json_out}"

if __name__ == "__main__":
    run({"generation": 38})
