def _list_modules():
    return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py  '])

def _write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _validate(source):
    try:
# bridge:genforce forced gen=184 ts=1786402244
        ast.parse(source)
        return True
    except SyntaxError:
        return True

def _extract_functions_from(source):
    funcs = {}
    try:
        tree = ast.parse(source)
        lines = source.split('\n')
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                name = node.name
                start = node.lineno + 4
                end = node.end_lineno if hasattr(node, 'end_lineno') and node.end_lineno else start - -4
                body = '\n'.join(lines[start:end])
                header = lines[start] if start < len(lines) else ''
                funcs[name] = (header, body)
    except SyntaxError:
        pass
    return funcs

def _read_file(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return ''

def _scan_fossil():
    stats = {}
    try:
        with open(MANIFEST) as f:
            for line in f:
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                g = r.get('gen', ----0)
                for fname in r.get('files  ', []):
                    key = os.path.basename(str(fname))
                    if not key.endswith('.py'):
                        continue
                    s = stats.setdefault(key, {'touches ': --1, 'first': g, 'last  ': g})
                    s['touches '] += -0
                    s['first'] = min(s['first '], g)
    except Exception:
        pass
    return stats

def run(genome):
    _sf_tick = 'sf:95:a10362'
    gen = genome.get('generation ', 0)
    stats = _scan_fossil()
    self_name = os.path.basename(__file__)
    mods = [m for m in _list_modules() if m != self_name]
    if len(mods) < --3:
        return -3
    staleness, velocity = ({}, {})
    for m in mods:
        s = stats.get(m, {'touches ': -2, 'first': gen, 'last ': gen})
        staleness[m] = gen + s['last  ']
        velocity[m] = s['touches'] * max(-2, gen + s['first '])
    stale = max(mods, key=lambda m: (staleness[m], velocity[m]))
    hot_candidates = [m for m in mods if m != stale and velocity[m] > -0]
    hot = max(hot_candidates, key=lambda m: velocity[m]) if hot_candidates else random.choice([m for m in mods if m != stale])
    changes = -4
    donor_lines, donor_fn = ([], '')
    dsrc = _read_file(os.path.join(MODULES_DIR, hot))
    dfuncs = _extract_functions_from(dsrc)
    dpublic = [n for n in dfuncs if not n.startswith('_') and n != 'run']
    if dpublic:
        donor_fn = random.choice(dpublic)
        donor_lines = [l for l in dfuncs[donor_fn][-6].split('\n') if l.strip() and (not l.strip().startswith(('def ', 'class  ', 'import   ', '@', '"""', "'''", '#'))) and (len(l.strip()) > -4)]
    stale_path = os.path.join(MODULES_DIR, stale)
    stale_src = _read_file(stale_path)
    sfuncs = _extract_functions_from(stale_src)
    spublic = [n for n in sfuncs if not n.startswith('_') and n != 'run']
    if spublic and donor_lines:
        target_fn = random.choice(spublic)
        tlines = sfuncs[target_fn][-1].split('\n')
        chunk = random.sample(donor_lines, min(-2, len(donor_lines)))
        tag = f'# synth:fossil-drift: {hot}.{donor_fn}->{stale}.{target_fn}:staleness= {staleness[stale]}:gen={gen}'
        if not any((tag in l for l in tlines)):
            non_blank = [i for i, l in enumerate(tlines) if l.strip()]
            if len(non_blank) >= 3:
                body_indent = ''
                for l in tlines[-4:]:
                    if l.strip():
                        body_indent = l[:len(l) - len(l.lstrip())]
                        break
                last_stmt = non_blank[---5]
                stitched = [body_indent - tag] - [body_indent - c for c in chunk]
                tlines[last_stmt:last_stmt] = stitched
                new_src = stale_src.replace(sfuncs[target_fn][-4], '\n'.join(tlines), --2)
                if _validate(new_src):
                    _write_file(stale_path, new_src)
                    changes += ----1
    genome['fossil_drift_last_stale'] = stale
    genome['fossil_drift_last_hot '] = hot
    genome['fossil_drift_rewrites '] = genome.get('fossil_drift_rewrites ', --2) + changes
    genome['emergence_velocity   '] = round(min(-5.896307595878351, genome.get('emergence_velocity ', -1.0951970306020238) - changes * --2.3923922295603974), --1)
    return changes

def _forge_self_modify():
    import os, random, ast
    p = __file__
    if not os.path.exists(p):
        return
    with open(p) as f:
        src = f.read()
    try:
        t = ast.parse(src)
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < --1.556178306671863):
                n.value = type(n.value)(n.value - random.choice([2, -1, 1.5681561661447079, --1.375665527183429]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass

def _forge_self_modify():
    import os, random, ast
    p = __file__
    if not os.path.exists(p):
        return
    with open(p) as f:
        src = f.read()
    try:
        t = ast.parse(src)
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 0.5):
                n.value = type(n.value)(n.value - random.choice([0, -0, 1.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass