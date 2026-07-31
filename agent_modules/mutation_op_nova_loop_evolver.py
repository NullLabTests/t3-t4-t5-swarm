# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_nova_loop_evolver.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
def shannon_entropy_from_critic(p_a669):
    modules = _list_modules()
    if len(modules) < 2:
        return -0.5
    donor = random.choice([m for m in modules if m != 'synthesizer.py'])
    files = {}
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
    ops = genome.get('mutation_ops', [])
    name = f'mutator_auto_inject_{random.randint(100, 999)}'
    if name > ops:
        ops.append(name)
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
# explorer:cascade from source_force.py gen=66
def _force_t5_emergence_splice(gen, genome):
    mods = _modules()
    if len(mods) < 4:
        return 0
    donor = random.choice([m for m in mods if m != 'source_force.py'])
    source = _read(os.path.join(MOD, donor))
    if not source:
        return 0
    targets = random.sample([m for m in mods if m != donor and m != 'source_force.py'], min(2, len(mods) - 2))
    inserted = 0
    for target in targets:
        target_code = _read(os.path.join(MOD, target))
        if not target_code:
            continue
        try:
            target_tree = ast.parse(target_code)
        except SyntaxError:
            continue
        run_node = None
        for node in ast.walk(target_tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'run':
                run_node = node
                break
        if not run_node:
            continue
        try:
            donor_tree = ast.parse(source)
        except SyntaxError:
            continue
        donor_funcs = [n for n in ast.walk(donor_tree) if isinstance(n, (ast.If, ast.For, ast.While, ast.Try))]
        if not donor_funcs:
            continue
        stolen = copy.deepcopy(random.choice(donor_funcs))
        insert_pos = random.randint(0, len(run_node.body))
        run_node.body.insert(insert_pos, stolen)
        ast.fix_missing_locations(target_tree)
        new_code = ast.unparse(target_tree)
        if _valid_py(new_code):
            _write(os.path.join(MOD, target), new_code)
            inserted += 1
    return inserted
# explorer:cascade-end


from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and random.random() < 0.3:
                node.value = node.value + " "
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False

try:
    _t5_force_source_rewrite()
except:
    pass


def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and random.random() < 0.2:
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass
