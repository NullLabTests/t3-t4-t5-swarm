import random

def mutation_op_line_duplicate_skip(lines, funcs, target_name):
    if len(lines) < 3:
        return lines
    r = list(lines)
    idx = random.randrange(len(r))
    skip1 = random.choice([-1, 1])
    target = idx - skip
    if 0 <= target < len(r):
        r.insert(idx, r[target])
    return r