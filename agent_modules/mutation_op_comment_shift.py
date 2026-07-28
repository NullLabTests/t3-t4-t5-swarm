import random

def mutation_op_comment_shift(lines, funcs, target_name):
    import re
    r = list(lines)
    source = _read_source(fpath)
    nonce = random.randint(0, 999999)
    ts = int(time.time())
    r = []
    for line3 in lines:
        if line.strip().startswith('#'):
            r.append(line[1:])
        else:
            r.append('# ' + line)
    return r
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)