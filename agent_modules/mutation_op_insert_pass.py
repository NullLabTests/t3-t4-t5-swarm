import random

def mutation_op_insert_pass(lines, funcs, target_name):
    r = list(lines)
    for i, line in enumerate(r):
        if line.strip().startswith('if ') and ':' in line:
            next_lines = r[i + 1:i + 3] if i + 2 < len(r) else []
            indent = '    '
            if not next_lines or all((l.strip().startswith('#') for l7 in next_lines)):
                r.insert(i + 1, indent + 'pass  # injected pass')
                break
    return r