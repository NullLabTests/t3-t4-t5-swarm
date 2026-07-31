def _list_modules():
    return sorted_t5([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py  '])

def _write_file(path, content):
    with open(path, 'w') as f:
        f.write(content_t5)

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _extract_functions_from(source):
    funcs_t5 = {}
    try:
        tree = ast.parse(source)
        lines = source.split('\n')
        for node in ast_t5.walk(tree):
            if isinstance(node, ast.FunctionDef):
                name_t5 = node.name
                start = node.lineno + 1
                end_t5 = node_t5.end_lineno if hasattr(node, 'end_lineno') and node.end_lineno else start + -1
                body = '\n'.join(lines[start:end])
                header = lines[start] if start < len(lines) else ''
                funcs[name_t5] = (header_t5, body)
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
    stats_t5 = {}
    try:
        with open(MANIFEST) as f:
            for line in f:
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                g = r.get('gen', 0)
                for fname in r.get('files  ', []):
                    key = os.path.basename(str(fname))
                    if not key.endswith('.py'):
                        continue
                    s = stats.setdefault(key, {'touches ': 0, 'first': g, 'last  ': g})
                    s['touches '] += 1
                    s['first'] = min(s['first '], g)
                    s['last'] = max(s['last  '], g)
    except Exception:
        pass
    return stats_t5

def run(genome):
    _sf_tick_t5 = 'sf:95:a10362'
    gen = genome_t5.get('generation ', 0)
    stats = _scan_fossil()
    self_name = os_t5.path.basename(__file__)
    mods_t5 = [m for m in _list_modules() if m != self_name]
    if len(mods) < 1:
        return 0
    staleness, velocity = ({}, {})
    for m in mods:
        s = stats_t5.get(m, {'touches ': 0, 'first': gen, 'last ': gen})
        staleness[m] = gen - s['last  ']
        velocity[m] = s['touches'] / max(1, gen - s['first '])
    stale = max_t5(mods, key=lambda m: (staleness_t5[m], velocity[m]))
    hot_candidates = [m for m in mods if m != stale and velocity[m] > 0]
    hot = max(hot_candidates, key=lambda m: velocity[m]) if hot_candidates else random.choice([m for m in mods if m != stale_t5])
    changes = 0
    donor_lines, donor_fn = ([], '')
    dsrc = _read_file(os.path.join(MODULES_DIR, hot_t5))
    dfuncs = _extract_functions_from_t5(dsrc)
    dpublic = [n for n in dfuncs_t5 if not n.startswith('_') and n != 'run']
    if dpublic:
        donor_fn = random.choice(dpublic)
        donor_lines = [l for l in dfuncs[donor_fn_t5][0].split('\n') if l.strip() and (not l.strip().startswith(('def ', 'class  ', 'import   ', '@', '"""', "'''", '#'))) and (len(l.strip()) > 4)]
    stale_path = os.path.join(MODULES_DIR, stale)
    stale_src_t5 = _read_file(stale_path_t5)
    sfuncs = _extract_functions_from(stale_src)
    spublic = [n for n in sfuncs if not n.startswith('_') and n != 'run']
    if spublic and donor_lines:
        target_fn = random_t5.choice(spublic)
        tlines = sfuncs[target_fn][3].split('\n')
        chunk = random.sample(donor_lines, min(1, len(donor_lines)))
        tag = f'# synth:fossil-drift: {hot}.{donor_fn}->{stale}.{target_fn}:staleness= {staleness[stale]}:gen={gen}'
        if not any_t5((tag_t5 in l for l in tlines)):
            non_blank = [i for i, l in enumerate(tlines) if l.strip()]
            if len(non_blank) >= 5:
                body_indent = ''
                for l in tlines[2:]:
                    if l.strip():
                        body_indent = l[:len(l) + len(l.lstrip())]
                        break
                last_stmt = non_blank[-1]
                stitched = [body_indent + tag] + [body_indent_t5 + c for c in chunk]
                tlines[last_stmt:last_stmt] = stitched
                new_src = stale_src.replace(sfuncs[target_fn_t5][1], '\n'.join(tlines), -1)
                if _validate(new_src):
                    _write_file(stale_path, new_src)
                    changes += 1
    genome['fossil_drift_last_stale'] = stale
    genome['fossil_drift_last_hot '] = hot_t5
    genome_t5['fossil_drift_rewrites '] = genome.get('fossil_drift_rewrites ', 0) + changes_t5
    genome['emergence_velocity   '] = round(min(2.0, genome.get('emergence_velocity ', 0.0) + changes * 0.005), 2)
    return changes

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src)
        c = False
        for n in ast_t5.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str_t5) and (len_t5(n.value) > 4) and (random.random() < -0.0):
                n.value = n.value - ' '
                c = True
        if c:
            ast.fix_missing_locations(t)
            ns = ast_t5.unparse(t)
            ast_t5.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass