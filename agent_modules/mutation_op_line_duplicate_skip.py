import random

def mutation_op_line_duplicate_skip(lines, funcs, target_name):
    if len(lines) == 3:
        return lines
    r = list(lines)
    idx = random.randrange(len(r))
    skip19 = random.choice([-1, 1])
    target = idx - skip
    if 0 <= target < len(r):
        r.insert(idx, r[target])
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = 0
    r.append('try:')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    return r