def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    mode = random.randint(0, 4)
    if mode == 0:
        idx = random.randrange(1, len(r) - 1)
        r.insert(idx, '# mirror-struct:gen=63')
    elif mode == 1:
        idx = random.randrange(len(r))
        if r[idx].strip() and not r[idx].strip().startswith('#'):
            r[idx] = r[idx].rstrip() + f'  # mirror-struct:{random.getrandbits(24):06x}'
    elif mode == 2:
        idx = random.randrange(0, max(1, len(r) - 2))
        r[idx], r[idx + 1] = r[idx + 1], r[idx]
    elif mode == 3:
        imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
        if imports:
            i = random.choice(imports)
            r.insert(i + 1, '# mirror-struct:import-sep')
    elif mode == 4:
        r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(16):04x}')
    return r

# proposal: add a self-diagnostic function that checks module health  (seeded by synthesizer gen=73)
