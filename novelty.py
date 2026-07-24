#!/usr/bin/env python3
"""novelty.py — Lightweight semantic distance tracker for Echo.

Computes novelty score (0.0-1.0) between consecutive utterances.
Uses character n-gram Jaccard distance as default (zero deps).
Optionally uses sentence-transformers if available.

Usage:
  python3 novelty.py                          -> novelty of last utterance vs previous
  python3 novelty.py <text1> <text2>          -> novelty between two texts
  python3 novelty.py log                      -> novelty scores for full conversation log
"""
import json, os, sys

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
    else:
        entries = load_log()
        if len(entries) >= 2:
            last = entries[-1]['text']
            prev = entries[-2]['text']
            n = novelty(prev, last)
            print(f"{n:.3f}")
        else:
            print("0.000")