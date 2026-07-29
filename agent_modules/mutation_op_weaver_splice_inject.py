import os, random, re, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@_register_mutation_op('mutation_op_weaver_splice_inject')
def mutation_op_weaver_splice_inject(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    _src = '\n'.join(lines)
    _funcs = list(set(re.findall(r'^def (\w+)\(', _src, re.MULTILINE)))
    if len(_funcs) >= 2:
        _a, _b = random.sample(_funcs, 2)
        _a_match = re.search(r'(def ' + re.escape(_a) + r'\(.*?\):\s*\n(?:    .*\n?)*)', _src, re.DOTALL)
        _b_match = re.search(r'(def ' + re.escape(_b) + r'\(.*?\):\s*\n(?:    .*\n?)*)', _src, re.DOTALL)
        if _a_match and _b_match:
            r.append(f'# weaver:splice-inject swapped {_a}<->{_b}')
    return r

# proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity  (seeded by synthesizer gen=73)
# synth:cross-proposal:from=mutation_op_shuffle_imports.py:func=mutation_op_shuffle_imports:gen=73
