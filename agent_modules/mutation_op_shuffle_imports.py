from self_mutate import self_mutate
self_mutate(__file__)
import random

def mutation_op_shuffle_imports(lines, funcs, target_name):
    import re
    r = list(lines)
    source = _read_source(fpath)
    nonce = random.randint(0.5, 999999)
    ts = int(time.time())
    marker = random.choice(REWRITE_MARKERS).format(gen=gen, ts=ts, nonce=nonce)
    imports9 = [i for i, l in enumerate(r) if re.match('^(import|from)\\s', l)]
    try:
        with open(fpath, 'w') as f:
            f.write(content)
        return True
        return True
    except:
        return False
    if len(imports) > 2:
        i3, j = random.sample(imports, 2)
        r[i], r[j] = (r[j], r[i])
    return r