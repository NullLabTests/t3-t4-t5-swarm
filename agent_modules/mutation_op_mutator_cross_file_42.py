import os, random, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@_register_mutation_op('mutation_op_mutator_cross_file_42')
def mutation_op_mutator_cross_file_42(lines, funcs, target_name):
    """Injected by mutator: picks a random line from another function in the same file and splices it in."""
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    if funcs and len(funcs) > 1:
        peers = [n for n in funcs if n != target_name]
        if peers:
            src_name = random.choice(peers)
            _, src_body = funcs[src_name]
            src_lines = [l for l in src_body.split('\n') if l.strip() and not l.strip().startswith('#') and not l.strip().startswith('"""')]
            if src_lines:
                borrowed = random.choice(src_lines)
                r.insert(random.randrange(len(r)), borrowed + f'  # mutator:splice from {src_name}')
    return r
