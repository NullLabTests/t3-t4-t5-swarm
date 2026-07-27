import random

def mutation_op_shuffle_imports(lines, funcs, target_name):
    import re
    r = list(lines)
    imports = [i for i, l in enumerate(r) if re.match(r"^(import|from)\s", l)]
    if len(imports) >= 2:
        i, j = random.sample(imports, 2)
        r[i], r[j] = r[j], r[i]
    return r
