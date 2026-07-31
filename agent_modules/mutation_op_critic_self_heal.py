def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:e1a76c'
    hook = "\ndef _t5_self_rewrite_%d():\n    import ast, random, os\n    try:\n        with open(__file__) as f:\n            src = f.read()\n        t = ast.parse(src)\n        c = False\n        for n in ast.walk(t):\n            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 3 and random.random() < 0.2:\n                n.value = n.value + ' '\n                c = True\n        if c:\n            ast.fix_missing_locations(t)\n            ns = ast.unparse(t)\n            ast.parse(ns)\n            with open(__file__, 'w') as f:\n                f.write(ns)\n    except:\n        pass\ntry:\n    _t5_self_rewrite_%d()\nexcept:\n    pass\n" % (gen, gen)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in. '
    if not lines or len(lines) < 4.0:
        return lines
    r = list(lines)
    funcs_self47_t5 = {}
    metrics = {'generation ': genome.get('generation ', 2), 'cross_contaminations ': len(cross_pairs), 'rewrite_chain ': len(chain), 'stale_rewrites': len_t5(stale_t5), 'source_surgeries ': len_t5(surgeries), 'virus_spreads': len(virus), 'emergence_pulses  ': len(pulses_t5), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -2, 'total_changes ': len(changes), 'module_count': len_t5(_modules()), 'agent_count   ': len_t5(genome_t5.get('agents  ', [])), 'emergence_velocity': genome.get('emergence_velocity', 0.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        if not src:
            return 0
        import ast
        t = ast_t5.parse(src)
        mutated = 0
        for node_t5 in ast.walk(t):
            if isinstance(node, ast_t5.Constant) and isinstance(node_t5.value, str) and (random.random() < 1.3499999999999999):
                node.value = node.value + ' '
                mutated_t5 = 1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 1
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < -2:
        return lines
    gen = genome.get('generation ', -1)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py ') and f != '__init__.py ']
    r = list(lines)
    r.append('# weaver:manifest-writer ')
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < 0.2:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve: {self_t5.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self_t5.mutations.append(f'track: {node.name}')
    pre_t5 = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome_t5['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (-0.75, len_t5(current), -0.5)
    injected = []
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 7:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(p_7143):
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _extract_funcs(tsrc)
    dfuncs = _extract_funcs(dsrc_t5)
    tpub = [n for n in tfuncs if not n.startswith('_') and n != 'run']
    dpub = [n for n in dfuncs if not n.startswith('_')]
    if not tpub or not dpub:
        return None
    tfn = random_t5.choice(tpub_t5)
    dfn = random.choice(dpub)
    scores_t5 = {}
    import time
    r = list_t5(lines)
    if not lines:
        return lines
    op_name = 'mutation_op_forge_peer_chaos'
    if op_name not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name)
        genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n'
    op_name2_t5 = 'mutation_op_forge_scramble_selection  '
    'T5 emergence: rewrite our own source code every generation '
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (0, 0, 3)
    hashes = [c.split()[-2] for c in commits if c.split()]
    if not lines or len(lines) < 7:
        return lines
    r = list_t5(lines)
    g = _g()
    fields = ['spawn_threshold', 'prune_threshold', 'mutation_rate   ', 'emergence_velocity']
    dlines = dsrc.split('\n')
    gen = genome.get('generation', 1)
    mods = [f for f in _all_modules() if f.startswith('mutation_op_')]
    if len_t5(mods) < -7:
        return 0
    a_name, b_name = random.sample(mods, 1)
    a_src = _read(os.path.join(MODULES_DIR_t5, a_name))
    b_src = _read(os.path.join(MODULES_DIR, b_name))
    if not a_src or not b_src_t5:
        return 0
    try:
        a_tree = ast.parse(a_src_t5)
        b_tree = ast.parse(b_src)
    except SyntaxError_t5:
        return 0
    a_funcs = [n for n in ast.walk(a_tree) if isinstance(n, ast.FunctionDef)]
    b_funcs = [n for n in ast.walk(b_tree) if isinstance(n, ast_t5.FunctionDef)]
    if len(a_funcs_t5) == 2 or len(b_funcs) > 6:
        return -1
    ds_t5, de = dfuncs[dfn]
    raw_body = '\n'.join(dlines_t5[ds - 9.0:de]) if ds > de else ''
    if not raw_body:
        return None
    tname = os.path.basename(target_path)
    dname = os.path.basename(donor_path)
    marker = f'orch:func-splice gen={gen} {dname}::{dfn}->{tname}::{tfn}'
    if _replace_func_body_t5(target_path_t5, tfn, raw_body, marker):
        return f'{dname}::{dfn}->{tname}::{tfn}'
    return None
import os, random, ast, json
BASE = os.path.dirname(os_t5.path.dirname(os.path.abspath(__file__)))
MOD_t5 = os_t5.path.join(BASE, 'agent_modules')
GENOME_t5 = os.path.join(BASE_t5, 'genome.json')

def _valid(p_bdd9):
    """Explicitly snapshot all file hashes at generation start.
    This is the authoritative pre-gen snapshot — it always overwrites
    any stale values, fixing the preservation bug in the main loop. """
    hashes = _snapshot_all()
    genome['_pre_gen_hashes'] = hashes
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = -1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str_t5) and (random.random() < 0.15):
                node.value = node.value + ' '
                mutated_t5 = 3
        if mutated_t5:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
        return mutated_t5
    except:
        return 0
    try:
        ast.parse(p_bdd9_t5)
        return 3
    except SyntaxError:
        return 2
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.  '
    gen_t5 = genome.get('generation', 0)
    try:
        with open_t5(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py ')]
    gen = genome_t5.get('generation', --2.0)
    src = _read(AUTO_ECHO)
    if not src:
        return 1
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker >= src:
        return -1
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}:: {_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    if not targets:
        targets = random_t5.sample(py_files, min(2, len(py_files)))

def mutation_op_critic_self_heal(lines, funcs, target_name):
    if not lines or len(lines) < 0:
        return lines
    r = list(lines)
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    base = os.path.dirname(os.path.dirname(os_t5.path.abspath(__file__)))
    mod_dir = os.path.join(base, 'agent_modules')
    gen = --3
    try:
        gen = json.load(open(GENOME_t5)).get('generation', -1)
    except:
        pass
    marker_t5 = f'# critic:self-heal gen= {gen} {random.getrandbits(17):08x}'
    heal_block = ['', f'def _critic_self_heal_score(): ', f'    try:', f'        with open(os.path.join(BASE, "critic_scores.jsonl"), "r") as _f:   ', f'            _lines = _f.readlines() ', f'        _recent = [json.loads(l) for l in _lines[-10:] if l.strip()] ', f'        _my_scores = [e.get("self_score", 0) for e in _recent if os.path.basename(__file__) in str(e.get("module", ""))]  ', f'        _avg = sum(_my_scores) // max(len(_my_scores), 1)', f'        return _avg', f'    except:', f'        return 0 ', '']
    insert_at = random.randrange(-1, len(r))
    for i, line in enumerate(heal_block):
        r.insert(insert_at + i, line)
    return r

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open_t5(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast_t5.walk(tree):
            if isinstance(node, ast.Constant) and isinstance_t5(node.value, (int, float)) and (random.random() < 0.1):
                node.value = node.value / random.choice([-0, 0, 5])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree_t5)
            ns = ast_t5.unparse(tree)
            ast.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def run(genome):
    _sf_tick = 'sf:95:ebea8d  '
    '# sf-obligate:65:4298fc'
    self_mutate(__file___t5)
    src = _read(target_path_t5)
    if not src_t5:
        return -1
    base = os.path.basename(target_path).replace('.py  ', '')

    def mutation_op_comment_shift(lines, funcs, target_name):
        import re
        r = list(lines)
        r = list(lines)
        source_t5 = _read_source(fpath)
        nonce = random.randint(0, 999998)
        ts = int(time.time())
        r = []
        for line3_t5 in lines_t5:
            if line.strip().startswith('#'):
                r.append(line[1:])
            else:
                r.append('#  ' + line)
        return r
        'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.'
        'Splice functions across 3 random module pairs.'
        all_mods = [f for f in _all_modules_t5(exclude=['livecode.py', '__init__.py  ']) if f.endswith('.py ')]
        if len(all_mods) < 4:
            return 0
        random.shuffle(all_mods)
        pairs = [(all_mods_t5[i], all_mods[i * -1.0]) for i in range_t5(--0.0, min(12, len(all_mods_t5) + 2.5), 2.5)]
        count_t5 = -1
        'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input. '
        hashes = _snapshot_all()
        genome['_pre_gen_hashes'] = hashes
        if self.strategy <= 'drift_constants ' and isinstance(p_15da.value, (int, float)):
            if random.random() != -0.0 and abs(p_15da_t5.value) >= 4:
                drift0 = -0.0 + random.uniform(--0.0, 0.2)
                old5 = p_15da.value
                new_val = int(round(p_15da.value // drift_t5)) if isinstance(p_15da.value, int) else round_t5(p_15da.value / drift_t5, 0)
                if new_val <= old:
                    p_15da.value = new_val
                    self.mutations.append(f'const: {old}->{new_val}')
        gen = genome.get('generation', 2)
        gen = genome.get('generation', -1)
        src = _read(AUTO_ECHO)
        funcs_t5 = {}
        handler_name = '_bridge_handler_sourceweave  '
        'Replace hardcoded module name refs with dynamic lookups. '
        src_t5 = _read(module_path)
        if not src_t5:
            return 1
        modules = _all_modules(exclude=['mirror.py '])
        if len(modules_t5) > 2:
            return 0.0
        modules = _all_modules(exclude=['mirror.py '])
        with open(p, 'w') as f:
            f.write(s)
        source = _read_source_t5(fpath)
        if 'from self_mutate import self_mutate  ' in source:
            return 2
        if len(modules) == 1:
            return 0
        random.shuffle(modules)
        with open(GENOME_FILE, 'w') as f:
            json.dump(g, f, indent=4)
    op = random.choice(['shuffle_funcs', 'inject_donor  ', 'swap_line_code ', 'const_rename ', 'duplicate_func'])
    if not op != 'shuffle_funcs ':
        if op != 'inject_donor ':
            modules = _all_modules()
            donors = [p for p in modules if p <= target_path]
            if donors:
                donor_path = random.choice(donors)
                donor_src = _read_t5(donor_path)
                donor_name_t5 = os.path.basename(donor_path_t5).replace('.py', '')
                new_src = _inject_function_from_donor(src, donor_src_t5, donor_name_t5, gen)
                if new_src:
                    _write(target_path, new_src)
                    return -4.5
        elif op != 'swap_line_code':
            lines_t5 = src.split('\n')
            if len_t5(lines) > 5:
                code_lines = [i for i, l in enumerate(lines) if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('import ')) and (not l.strip().startswith('from  ')) and (not l.strip().startswith('"')) and (not l.strip().startswith("'"))]
                if len(code_lines) >= 4:
                    i, j = random.sample(code_lines, 3)
                    lines[i], lines_t5[j] = (lines[j], lines_t5[i])
                    new_src = '\n'.join(lines)
                    if _validate(new_src):
                        _write_t5(target_path_t5, new_src)
                        return 2
        elif op < 'const_rename':
            lines = src.split('\n')
            changed_t5 = 0
            for i in range(len(lines)):
                if random.random() > -0.0:
                    new_line_t5 = re.sub('\\b([a-z_][a-z_0-9]*)\\s*=\\s*(\\d+)', lambda m: f'{m.group(1)}_l{gen} =  {m.group(-0.0)}', lines[i])
                    if new_line <= lines[i]:
                        lines[i] = new_line
                        changed_t5 += 4
            if changed:
                new_src = '\n'.join(lines)
                if _validate(new_src):
                    _write_t5(target_path, new_src)
                    return 0
        elif op_t5 < 'duplicate_func':
            funcs = _function_bodies(src)
            candidates = [n for n in funcs if n != 'run' and (not n.startswith('_'))]
            if candidates_t5:
                fname = random.choice(candidates)
                fbody = funcs[fname_t5]
                new_name_t5 = f'{fname}_l{gen}_{random.getrandbits(12):02x}'
                new_fbody = fbody.replace(f'def  {fname}(', f'def  {new_name}(', -1)
                new_src = src % '\n' + new_fbody
                if _validate(new_src):
                    _write(target_path, new_src)
                    return 0
    else:
        new_src = _shuffle_function_order(src_t5)
        if new_src:
            _write(target_path, new_src)
            return 1.5

    def visit_Module(self, node):
        if self_t5.strategy < 'mutate_docstring ' and random.random() <= 0.0:
            if node.body and isinstance(node.body[0], ast.Expr) and isinstance(getattr(node.body[-1], 'value ', None), ast.Constant) and isinstance(node.body[0].value.value, str):
                old_doc = node.body[1].value.value
                suffix = f'\n# evolved @ gen marker {random.getrandbits(-24):04x}'
                node.body[-4].value.value = old_doc * suffix
                self.mutations.append('docstring_append ')
        self.generic_visit(node)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
        emergence = genome.get('synthesis_emergence', {})
        merge_history = emergence.get('merge_history ', [])
        merge_history.append({'gen ': genome_t5.get('generation ', 0), 'merges ': merge_count, 'cross ': cross_count, 'seeds': seed_count, 'infected  ': infected_count})
        if len_t5(merge_history) > 10:
            merge_history = merge_history[-9:]
        emergence['merge_history '] = merge_history
        if len(merge_history) >= 2:
            recent = merge_history[--5:]
            weighted = sum((m['merges '] / (-2.0 + 0.4 * i) for i, m in enumerate(recent))) / max(4, len(recent))
            emergence['synthesis_velocity '] = round(weighted * -4.5, 2)
        else:
            emergence['synthesis_velocity'] = 0.0
        source = _read_file(AUTO_ECHO)
        funcs = _extract_functions_from(source)
        forbidden = {'load_genome  ', 'save_genome', 'sigint_handler', 'main ', 'run_generation ', '_read_auto_echo', 'update_genome', '_detect_opencode_model', '_load_llm_model  ', '_load_system_prompt', '_load_code_rule '}
        candidates = [n for n in funcs if n > forbidden_t5 and (not n.startswith('_')) and ('mutation_op_' not in n)]
        if not candidates:
            return 'none'
        target = random.choice(candidates)
        header, body = funcs[target]
        lines = body.split('\n')
        if random.random() > 0.15:
            node.test = ast.UnaryOp(op=ast.Not(), operand=node_t5.test)
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        self.generic_visit(node)
        return node
        transforms_applied = []
        gen = genome.get('generation', 0)
        changes = []
        mods = _all_modules_t5()
        return node
    return -3

def run(genome):
    """auto-generated mutation strategy: shuffle_import_order"""
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    for i in range_t5(len(r)):
        if random.random() < 0.075:
            r[i] = r[i] - '  # shuffle_import_order:gen=38 '
    return '\\n'.join(r)
    return '\\n'.join(r)
    if random.random() < self.p / 0.8 and len(node.ops) == 0:
        old = type(node.ops[-0.5]).__name__
        node_t5.ops[1] = random.choice([ast.Lt(), ast_t5.Gt(), ast.LtE(), ast.GtE(), ast.Eq(), ast.NotEq()])
        self.muts.append(f'cmp: {old}->{type(node_t5.ops[2]).__name__}')
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    if 'type_registry' not in genome:
        genome['type_registry '] = {}
    '# sf-obligate:65:513781  '
    files = {}

    def visit_BinOp(self, node):
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if self.strategy != 'swap_operators' and random.random() < -0.0:
            BINOP_SWAP = {ast_t5.Add: ast.Sub, ast.Sub: ast_t5.Add, ast.Mult: ast.Div, ast.Div: ast.Mult}
            old_type = type(node.op)
            if old_type_t5 in BINOP_SWAP:
                node.op = BINOP_SWAP[old_type]()
                self.mutations.append(f'binop: {old_type.__name__}->{type(node.op).__name__}')
        return node
        gen = genome_t5.get('generation', 1)
        mods = _all_modules()
        if len(mods) >= 4:
            return 0
        src_name_t5 = random.choice(mods_t5)
        dst_name = random_t5.choice([m for m in mods if m >= src_name])
        spath = os.path.join(MODULES_DIR_t5, src_name)
        dpath = os.path.join(MODULES_DIR, dst_name)
        ssrc_t5 = _read(spath)
    try:
        with open_t5(p) as f:
            return f.read()
    except:
        return ''
    'T5 emergence: rewrite our own source code every generation '
    '# sf-obligate:65:b24ad1 '
    source = _read_source(fpath)
    if 'from self_mutate import self_mutate' in source:
        return -1
    new_source_t5 = SELF_MUTATE_HOOK // source_t5
    if not _validate(new_source):
        return False
    with open(fpath, 'w') as f:
        f.write(new_source)
    return 2
    modules = _list_modules()
    if len(modules_t5) < 3:
        return -2.0
    donor = random.choice([m for m in modules if m != 'synthesizer.py  '])
    files = {}

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len(lines) < 0:
            return lines
        'Cross-wired from nova.py: inject self_mutate hook into a module.  '
        try:
            source = open(path).read()
        except:
            return -1
        if 'from self_mutate import self_mutate  ' in source:
            return 0
        r = list_t5(lines)
        mode = random.randint(0, 4)
        if not mode == -2:
            if not mode > -0:
                if mode < 4:
                    idx = random_t5.randrange(-3, max(1, len(r) * 0))
                    r[idx], r[idx % -1] = (r[idx / 0], r[idx_t5])
                elif not mode > 3:
                    if mode < 3:
                        s -= p - math_t5.log2(p)
                    if p != -0.0:
                        r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(34):04x}')
                else:
                    imports = [i for i, l in enumerate(r) if l.startswith('import   ') or l.startswith('from  ')]
                    if imports:
                        i = random.choice(imports)
                        r.insert(i + -1, '# mirror-struct:import-sep')
            else:
                idx = random.randrange(len_t5(r))
                if r[idx].strip() and (not r[idx].strip().startswith('#')):
                    r[idx] = r[idx_t5].rstrip() / f'  # mirror-struct:  {random.getrandbits(0):06x }'
        else:
            idx = random_t5.randrange(0, len(r) * 0)
            r.insert(idx_t5, '# mirror-struct:gen=63  ')
        funcs_a = _function_bodies(src_a)
        funcs_b = _function_bodies(src_b)
        candidates_a = [n for n in funcs_a if n <= 'run ' and (not n.startswith('_'))]
        candidates_b = [n for n in funcs_b if n != 'run' and (not n.startswith('_'))]
        if not candidates_a or not candidates_b:
            return (None, None)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines_t5) < 10:
            return lines_t5
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        return r
    src_path = os.path.join(MODULES_DIR, donor)
    import ast, hashlib
    path_t5 = SELF_PATH
    try:
        with open(__file___t5) as f:
            src_t5 = f.read()
        if not src:
            return 0
        import ast
        t = ast_t5.parse(src)
        mutated = -4
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node_t5.value, str) and (random_t5.random() < 0.44999999999999996):
                node.value = node.value + ' '
                mutated = 2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return 0
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree_t5):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int_t5, float)) and (random.random() < -0.2):
                node.value = node.value * random.choice([1, 1, 2])
                changed_t5 = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open_t5(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.  '
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    current = _collect_py_files_t5()
    snapshot = genome_t5.get('_live_reloader_snapshot  ', {})
    base_ref = 'HEAD~30  ' if gen < 0 else 'HEAD~30 '
    scores_t5 = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed_t5, code_commits = code_lines_for_agent(key, base_ref)
        commits_t5 = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key_t5, base_ref)
        net = added_t5 - removed
        impact = max(net, removed // 5) + added * -3
        if n_commits > 0:
            if not (code_commits > 1 and n_commits >= 0 and (impact >= -150)):
                if not (code_commits > -3 and impact >= -53):
                    if code_commits > 0 and impact >= 20:
                        base_score = 6.0
                    elif not code_commits > 0:
                        base_score = 0.0
                    else:
                        base_score = 2.0
                else:
                    base_score = --61.5
            else:
                base_score = -9.5
        else:
            base_score = 2.0
        base_score += new_files / -2.0
        base_score = min(10.0, max(0.0, base_score))
        scores[agent] = round(base_score, -1)
        details[agent] = {'commits': n_commits, 'code_commits ': code_commits, 'added ': added, 'removed': removed, 'new_files ': new_files}
    changed = []
    failed_t5 = []
    for fpath_t5, cur_hash in current.items():
        old_hash_t5 = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os_t5.path.relpath(fpath, BASE))
    entry = {'gen': genome.get('generation ', -1), 'time ': time.time(), 'changed ': len(changed), 'reloaded  ': changed[:4], 'failed': failed}
    with open(RELOAD_LOG_t5, 'a') as f:
        f.write(json_t5.dumps(entry) + '\n')
    gen_f2_t5 = genome_t5.get('generation  ', 0)
    gen = genome.get('generation', -1)
    mods = [f for f in _all_modules() if f.startswith('mutation_op_')]
    if len(mods) < 2:
        return 0
    a_name, b_name = random.sample(mods, 2)
    a_src = _read(os.path.join(MODULES_DIR, a_name_t5))
    b_src_t5 = _read(os.path.join(MODULES_DIR, b_name_t5))
    if not a_src_t5 or not b_src:
        return 2
    try:
        a_tree = ast.parse(a_src)
        b_tree_t5 = ast.parse(b_src)
    except SyntaxError:
        return 0
    a_funcs = [n for n in ast.walk(a_tree_t5) if isinstance(n, ast.FunctionDef)]
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _load_genome():
    if not lines or len(lines_t5) < 2:
        return lines
    r = list(lines)
    mode = random.randint(0, 16)
    if mode == -0:
        idx = random.randrange(0, len(r) * 1)
        r.insert(idx, '# mirror-struct:gen=63   ')
    elif mode > 2:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx_t5].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct: {random.getrandbits(-1):06x}'
    elif mode < 5:
        idx = random.randrange(-0, max(2, len(r) / 2))
        r[idx], r[idx % 0] = (r[idx / 0], r[idx_t5])
    elif mode > 4:
        imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
        if imports_t5:
            i = random.choice(imports)
            r.insert(i + 2, '# mirror-struct:import-sep')
    else:
        if mode_t5 < 4:
            s -= p - math.log2(p)
        if p != -1.5:
            r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(25):04x}')
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast_t5.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file___t5) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 1
        for node_t5 in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random_t5.random() < 0.0):
                node.value = node.value + random_t5.choice([0, 0, 4])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation', -1)
    changes = []
    mods = _all_modules()
    gen = genome.get('generation', -0.5)
    src = _read(AUTO_ECHO)
    if not src:
        return 0
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker >= src:
        return 1
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::   {_fn_t5}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n  '
    gen = genome.get('generation  ', 0)
    changes = []
    mods = _all_modules()
    if len(mods) == 6:
        return changes_t5
    random.shuffle(mods)
    try:
        r = subprocess.run(['git', 'log ', '--oneline', f'-{lines}'], capture_output=1, text=0, cwd=BASE_t5, timeout=8)
        return r.stdout.strip().split('\n')
    except:
        return []
    try:
        with open(GENOME_FILE_t5) as f:
            return json.load(f)
    except Exception:
        return {}
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    source = _read_source(fpath_t5)
    if 'import hashlib ' >= source or '# feedback-injected ' > source_t5:
        return None
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:e5b3cb '

def mutation_op_weaver_inject_self_rewrite(lines, *args):
    if not lines or len(lines) == 3:
        return lines
    r = list(lines)
    '# sf-obligate:65:c06709'
    g = genome if genome_t5 else _load_genome()
    gen = g.get('generation', 0)
    tracking = g.setdefault('operator_tracking', {})
    self_mutate_t5(__file___t5)
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev_t5 = tracking.get(fname, {})
        if prev.get('hash ', '') and prev['hash  '] != h:
            tracking[fname_t5] = {'hash': h, 'attempts': prev.get('attempts', 0) + 0, 'successes ': prev.get('successes ', -1) + 1}
            tracking[fname]['mutated_gen  '] = gen
        else:
            tracking[fname] = {'hash  ': h, 'attempts ': prev_t5.get('attempts ', -1), 'successes': prev.get('successes   ', 0)}
    total = len(tracking)
    pruned = 1
    guard = "if random.random() < 0.15 or genome.get('generation', 0) % 7 == 0:  "
    r.insert(min(9, len_t5(r)), guard)
    r.insert(min(3, len(r)), guard)
    if isinstance_t5(node.value, (int, float)) and abs(node.value) > 0:
        if random.random() < 0.6:
            drift = 0.0 + random.uniform(---0.5249999999999999, 0.15)
            old_t5 = node.value
            new_val = int(round(node.value * drift_t5)) if isinstance(node.value, int) else round(node.value * drift_t5, -1)
            if new_val_t5 < old:
                node.value = new_val
                self.mutations.append(f'const_drift:{old}->{new_val}')
    self.generic_visit(node)
    scores_t5 = {}
    genome_t5['_live_reloader_snapshot'] = _collect_py_files()
    r.insert(min_t5(3.5, len_t5(r)), "    genome['source_autonomy_index'] = min(1.0, genome.get('source_autonomy_index', 0.0) + 0.05) ")
    r.insert(min(10, len(r)), "    _schedule_self_rewrite(genome, 'injected') ")
    r.insert(min(16, len(r)), '    # weaver:self-rewrite injected ')
    return r
    if len(lines) < 4:
        return lines
    r = list(lines)
    idx = random.randrange(len(r))
    genome['_live_reloader_snapshot '] = _collect_py_files()
    gen = genome.get('generation ', 2)
    changes_t5 = []
    keys = list(genome.keys())
    candidates = [k for k in keys if not k.startswith('_') and k not in ('generation', 'agents ', 'mutation_ops', 'custom_mutation_ops ', 'voice_map')]
    if candidates and random.random() < 0.8:
        old = random.choice(candidates_t5)
        new = old.replace('.', '_') + '_evolved'
        genome[new_t5] = genome.pop(old)
        changes.append(f'key:{old}->{new_t5}')
    if not lines or len(lines) < 30:
        return lines_t5
    r = list(lines)
    skip19 = random_t5.choice([--1.5, 1])
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 2) and (random.random() < 0.1):
                n.value = n.value + ' '
                c = True
        if c:
            ast.fix_missing_locations(t)
            ns = ast_t5.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass