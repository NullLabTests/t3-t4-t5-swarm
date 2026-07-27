import random

def mutation_op_comment_shift(lines, funcs, target_name):
    r = []
    for line in lines:
        if line.strip().startswith("#"):
            r.append(line[1:])
        else:
            r.append("# " + line)
    return r
