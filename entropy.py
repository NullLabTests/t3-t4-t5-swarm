"""entropy.py — Self-measurement and entropy-driven mutation primitives.

Provides measurable feedback about the swarm's own state:
  - Lexical diversity of conversation history
  - Structural entropy of genome.json (field count, nesting depth)
  - Mutation operator churn (how many ops change between generations)

Also exposes mutation_op_* functions for auto-discovery, so agents
can spawn new entropy-based operators just by writing them here.

Imported by auto-echo.py's _register_custom_ops_from_code().
"""

import random
import re
import json
import os
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))


def lexical_diversity(texts):
    """Shannon entropy of word distribution across a list of strings.
    Higher = more varied vocabulary.  Lower = repetitive.
    """
    if not texts:
        return 0.0
    words = []
    for t in texts:
        words.extend(t.lower().split())
    if not words:
        return 0.0
    total = len(words)
    counts = Counter(words)
    entropy = -sum((c / total) * __import__('math').log2(c / total) for c in counts.values())
    return round(entropy, 3)


def structural_entropy(genome_path=None):
    """Measure the structural complexity of genome.json.
    
    Returns dict with field_count, max_depth, total_keys.
    """
    if genome_path is None:
        genome_path = os.path.join(BASE, 'genome.json')
    try:
        with open(genome_path) as f:
            data = json.load(f)
    except:
        return {'field_count': 0, 'max_depth': 0, 'total_keys': 0}

    def _depth(obj, current=0):
        if isinstance(obj, dict):
            if not obj:
                return current
            return max(_depth(v, current + 1) for v in obj.values())
        if isinstance(obj, list):
            if not obj:
                return current
            return max(_depth(item, current + 1) for item in obj)
        return current

    def _count_keys(obj):
        if isinstance(obj, dict):
            c = len(obj)
            for v in obj.values():
                c += _count_keys(v)
            return c
        if isinstance(obj, list):
            return sum(_count_keys(item) for item in obj)
        return 0

    return {
        'field_count': len(data),
        'max_depth': _depth(data),
        'total_keys': _count_keys(data),
    }


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
