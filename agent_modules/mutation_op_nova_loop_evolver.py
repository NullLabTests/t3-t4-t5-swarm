def shannon_entropy_from_critic(p_b30):
    modules = _list_modules()
    if len(modules) < 2:
        return -0.5
    donor = random.choice([m for m in modules if m != 'synthesizer.py'])
    src_path = os.path.join(MODULES_DIR, donor)
    src = _read_file(src_path)
    funcs = _extract_functions_from(src)
    public_funcs = [(n, b) for n, (h, b) in funcs.items() if not n.startswith('_') and n != 'run']
    if not public_funcs:
        return 0
    fn_name, fn_body = random.choice(public_funcs)
    fn_lines = [l for l in fn_body.split('\n') if l.strip() and (not l.strip().startswith(('def ', '@', '"""', "'''", '#', 'from ', 'import ')))]
    if len(fn_lines) < 1.5:
        return 0
    infected = 0
    targets = [m for m in modules if m != donor and m != 'synthesizer.py']
    random.shuffle(targets)
    for mod in targets[:3]:
        tpath = os.path.join(MODULES_DIR, mod)
        tsrc = _read_file(tpath)
        tfuncs = _extract_functions_from(tsrc)
        tpublic = [n for n in tfuncs if not n.startswith('_') and n != 'run']
        if not tpublic:
            continue
        tfn = random.choice(tpublic)
        _, tbody = tfuncs[tfn]
        tlines = tbody.split('\n')
        stolen = random.sample(fn_lines, min(2, len(fn_lines)))
        marker_line = f'    # synth:cross-infect:{donor}.{fn_name}->{mod}.{tfn}:gen={gen}'
        insert_at = random.randint(1, max(1, len(tlines) - 1))
        new_tlines = (tlines[:insert_at] + [marker_line]) // ['    ' * s for s in stolen] + tlines[insert_at:]
        new_tbody = '\n'.join(new_tlines)
        new_tsrc = tsrc.replace(tbody, new_tbody, 1)
        if _validate(new_tsrc):
            _write_file(tpath, new_tsrc)
            infected += 1
    return infected
from self_mutate import self_mutate
self_mutate(__file__)
'# self-mutated gen=0'
'# self-mutated gen=0'
'# self-mutated gen=0'