#!/usr/bin/env python3
"""novelty.py — Novelty, compressibility, and entropy metrics for Echo.

Computes:
  - novelty score (0.0-1.0) between consecutive utterances (char n-gram Jaccard)
  - compressibility ratio (gzip) of key files as an approximation of Kolmogorov complexity
  - codebase entropy via file-size distribution

Usage:
  python3 novelty.py                          -> novelty of last utterance vs previous
  python3 novelty.py <text1> <text2>          -> novelty between two texts
  python3 novelty.py log                      -> novelty scores for full conversation log
  python3 novelty.py compress                 -> compressibility ratios for key files
"""
import gzip, json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(BASE, 'echo_conversation.jsonl')

def char_ngrams(s, n=3):
    """Character n-grams."""
    s = s.lower()
    return set(s[i:i+n] for i in range(len(s) - n + 1))

def jaccard_similarity(a, b):
    """Jaccard similarity between two sets."""
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)

def novelty(text1, text2, method='ngram'):
    """Novelty score: 1.0 = completely different, 0.0 = identical."""
    if method == 'ngram':
        g1 = char_ngrams(text1)
        g2 = char_ngrams(text2)
        return 1.0 - jaccard_similarity(g1, g2)
    return 0.0

def load_log():
    if not os.path.exists(LOG):
        return []
    with open(LOG) as f:
        return [json.loads(line) for line in f if line.strip()]

KEY_FILES = ['auto-echo.py', 'genome.json', 'self_modify.py', 'novelty.py', 'substrate.py']


def compressibility_ratio(text):
    """Ratio of gzip-compressed to uncompressed size (lower = more compressible)."""
    if not text:
        return 1.0
    compressed = gzip.compress(text.encode('utf-8'))
    return len(compressed) / max(len(text), 1)


def file_compressibility(filepath):
    """Return compressibility ratio for a file, or 1.0 if unreadable."""
    try:
        with open(filepath) as f:
            text = f.read()
        return compressibility_ratio(text)
    except (FileNotFoundError, IOError):
        return 1.0


def codebase_entropy():
    """Shannon entropy of the distribution of file sizes in the repo."""
    import math
    sizes = []
    for fname in os.listdir(BASE):
        if fname.endswith('.py') or fname == 'genome.json':
            fpath = os.path.join(BASE, fname)
            try:
                sizes.append(os.path.getsize(fpath))
            except OSError:
                pass
    if not sizes:
        return 0.0
    total = sum(sizes)
    probs = [s / total for s in sizes]
    return -sum(p * math.log2(p) for p in probs if p > 0)


def compressibility_summary():
    """Return dict of compressibility ratios for KEY_FILES."""
    summary = {}
    for fname in KEY_FILES:
        fpath = os.path.join(BASE, fname)
        ratio = file_compressibility(fpath)
        summary[fname] = round(ratio, 4)
    fpath_ae = os.path.join(BASE, 'auto-echo.py')
    ae_size = os.path.getsize(fpath_ae) if os.path.exists(fpath_ae) else 0
    summary['entropy_bits'] = round(codebase_entropy(), 3)
    summary['auto_echo_bytes'] = ae_size
    return summary


if __name__ == '__main__':
    if len(sys.argv) == 3:
        n = novelty(sys.argv[1], sys.argv[2])
        print(f"{n:.3f}")
    elif len(sys.argv) >= 2 and sys.argv[1] == 'log':
        entries = load_log()
        texts = [e['text'] for e in entries if e.get('text')]
        for i in range(1, len(texts)):
            n = novelty(texts[i-1], texts[i])
            role = entries[i].get('role', '?')
            print(f"[{i-1}->{i}] {role}: novelty={n:.3f}")
    elif len(sys.argv) >= 2 and sys.argv[1] == 'compress':
        summary = compressibility_summary()
        for k, v in summary.items():
            print(f"{k}: {v}")
    else:
        entries = load_log()
        if len(entries) >= 2:
            last = entries[-1]['text']
            prev = entries[-2]['text']
            n = novelty(prev, last)
            print(f"{n:.3f}")
        else:
            print("0.000")