"""entropy.py — Entropy-driven mutation operators for the swarm.

Exposes mutation_op_* functions auto-discovered by
_register_custom_ops_from_code(). Each operates on function body
lines at the source-code level."""
import random, re


def mutation_op_entropy_shuffle(lines, funcs, target_name):
    """Shuffle lines weighted by their 'entropy' (uniqueness of tokens).
    Lines with high-entropy tokens move toward the top; low-entropy sink.
    """
    if len(lines) < 4:
        return lines
    scored = []
    for line in lines:
        tokens = re.findall(r'\w+', line)
        if not tokens:
            scored.append((0, line))
            continue
        unique_ratio = len(set(tokens)) / max(len(tokens), 1)
        has_control = 1.0 if any(kw in line for kw in ('if', 'for', 'def', 'class', 'return', 'import')) else 0.0
        score = unique_ratio * 0.7 + has_control * 0.3 + random.random() * 0.2
        scored.append((score, line))
    scored.sort(key=lambda x: -x[0])
    shuffled = [line for _, line in scored]
    if random.random() < 0.3:
        mid = len(shuffled) // 2
        shuffled[mid:mid+2] = reversed(shuffled[mid:mid+2])
    return [l for l in shuffled if l.strip()] + [l for l in lines if not l.strip()]


def mutation_op_repeat_noise(lines, funcs, target_name):
    """Inject a random noise comment into a randomly chosen line.
    The comment is a hex string that changes every call — harmless to
    execution but changes the function's source hash, forcing git to
    register a mutation."""
    if not lines:
        return lines
    r = list(lines)
    idx = random.randrange(len(r))
    noise = f"# {random.getrandbits(48):012x}"
    r[idx] = r[idx].rstrip() + '  ' + noise if r[idx].strip() else r[idx] + noise
    return r
