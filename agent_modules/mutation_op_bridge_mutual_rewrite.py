@_register_mutation_op('mutation_op_bridge_mutual_rewrite')
def mutation_op_bridge_mutual_rewrite(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    ts = int(time.time())
    r.insert(0, f'# bridge:mutual-rewrite-op gen=71 ts={ts}')
    r.insert(0, f'# Each module rewrites another and itself every generation')
    other_funcs = [n for n in funcs if n != target_name and not n.startswith('_') and n != 'run']
    if other_funcs:
        src_name = random.choice(other_funcs)
        _, src_body = funcs[src_name]
        src_lines = [l for l in src_body.split('\n') if l.strip()]
        if src_lines:
            r.insert(1, f'# bridge:mutual-spliced-from-{src_name}')
            r[2:2] = [f'    {l}' for l in src_lines[:3]]
    return r

@_register_mutation_op('mutation_op_bridge_sourceweave')
def mutation_op_bridge_sourceweave(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    weave_marker = f'# bridge:sourceweave-op gen=71 ts={int(time.time())}'
    r.append('')
    r.append(weave_marker)
    r.append('# This module participates in the mutual source weaving web')
    return r
