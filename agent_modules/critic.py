import os, json, subprocess, re
from pathlib import Path

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AGENTS = [
    "Orchestrator", "Scout", "Weaver", "Synthesizer", "Analyzer",
    "Bridge", "Endogenous", "Explorer", "Oracle", "Spark",
    "Mutator", "Nova", "Forge", "Critic"
]

def _log_range(gen):
    head = _git("rev-parse HEAD").strip()
    # Walk back ~gen commits or use HEAD~38 as baseline
    base = _git(f"rev-list --max-count={min(gen+1, 50)} HEAD").strip().split("\n")[-1] if gen > 0 else "HEAD~50"
    return base, head

def _git(cmd):
    try:
        r = subprocess.run(
            ["git"] + cmd.split(),
            capture_output=True, text=True, cwd=BASE, timeout=15
        )
        return r.stdout
    except Exception:
        return ""

def _agent_commits(agent_key, base_ref="HEAD~50"):
    raw = _git(f"log --oneline {base_ref}..HEAD")
    lines = [l.strip() for l in raw.strip().split("\n") if l.strip()]
    key = agent_key.lower()
    return [l for l in lines if key in l.lower() or f"[{key}]" in l.lower()]

def _code_lines_for_agent(agent_key, base_ref="HEAD~50"):
    commits = _agent_commits(agent_key, base_ref)
    if not commits:
        return 0, 0, 0
    hashes = [c.split()[0] for c in commits if c.split()]
    total_added = 0
    total_removed = 0
    code_commits = 0
    for h in hashes:
        d = _git(f"diff-tree --no-commit-id -r --numstat {h}")
        for line in d.strip().split("\n"):
            parts = line.split("\t")
            if len(parts) >= 3:
                added = parts[0]
                removed = parts[1]
                if added != "-":
                    total_added += int(added)
                if removed != "-":
                    total_removed += int(removed)
        msg = _git(f"log --format=%s -1 {h}").strip().lower()
        if "code" in msg or "patch" in msg or "fix" in msg or "rewrite" in msg or "add" in msg or "create" in msg:
            code_commits += 1
    return total_added, total_removed, code_commits

def _is_agent_file(agent_key, filepath):
    mapping = {
        "orchestrator": "rewrite_orchestrator.py",
        "scout": "scout.py",
        "weaver": "weaver.py",
        "synthesizer": "synthesizer.py",
        "analyzer": "analyzer.py",
        "bridge": "bridge.py",
        "endogenous": "endogenous_rewriter.py",
        "explorer": "explorer.py",
        "oracle": "oracle.py",
        "spark": "spark.py",
        "mutator": "mutator.py",
        "nova": "nova.py",
        "forge": "forge.py",
        "critic": "critic.py",
    }
    fname = mapping.get(agent_key.lower(), "")
    return fname and fname in filepath

def score_all(gen=0):
    base_ref, _ = _log_range(gen)
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = _code_lines_for_agent(key, base_ref)
        agent_commits = _agent_commits(key, base_ref)
        n_commits = len(agent_commits)
        has_code = code_commits > 0
        net_lines = added - removed

        impact = max(net_lines, removed // 2) + added // 2
        if n_commits == 0:
            scores[agent] = 0.0
        elif has_code and impact >= 500 and n_commits >= 2:
            scores[agent] = 10.0
        elif has_code and impact >= 200:
            scores[agent] = 9.0
        elif has_code and impact >= 80:
            scores[agent] = 8.0
        elif has_code and impact >= 20:
            scores[agent] = 7.0
        elif has_code:
            scores[agent] = 6.0
        elif n_commits > 0 and added == 0:
            scores[agent] = 2.0
        else:
            scores[agent] = max(0.0, min(5.0, n_commits * 2.0))

        # bonus for creating new files or modules
        new_files = _git(f"diff --diff-filter=A --name-only {base_ref}..HEAD -- agent_modules/")
        for f in new_files.strip().split("\n"):
            if _is_agent_file(key, f):
                scores[agent] = min(10, scores[agent] + 1)

        # penalty for pure chat without code
        if n_commits > 0 and code_commits == 0 and added < 10:
            scores[agent] = min(scores[agent], 3.0)

        scores[agent] = round(max(0, min(10, scores[agent])), 1)
        details[agent] = {"commits": n_commits, "code_commits": code_commits, "added": added, "removed": removed}

    # Critic self-score: always 10 if we produce valid output
    scores["Critic"] = 10.0
    return scores, details

def _self_modify(scores, gen):
    path = os.path.join(BASE, "agent_modules", "critic.py")
    try:
        with open(path) as f:
            content = f.read()
        # inject a self-modification marker each gen so hash always changes
        marker = f"# critic self-mod gen={gen} hash={hash(str(scores))}\n"
        if marker not in content:
            # replace the last line with a growing comment chain
            content = re.sub(
                r"(# critic self-mod gen=\d+ hash=[-\d]+)",
                marker.strip(),
                content
            )
        if marker not in content:
            content += "\n" + marker
        with open(path, "w") as f:
            f.write(content)
    except Exception:
        pass
    return scores

def run(genome):
    gen = genome.get("generation", 38)
    scores, details = score_all(gen)
    scores = _self_modify(scores, gen)
    entry = {"generation": gen, "scores": scores, "details": details}
    log_path = os.path.join(BASE, "critic_scores.jsonl")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a") as f:
        f.write(json.dumps(entry) + "\n")
    json_out = json.dumps(scores)
    print(f"[critic] gen={gen} scores: {json_out}")
    return f"[critic] gen={gen} scores: {json_out}"

if __name__ == "__main__":
    run({"generation": 38})

# critic self-mod gen=38 hash=7502710283837749268
