from self_mutate import self_mutate
self_mutate(__file__)
import os, random, hashlib, ast, json, copy, textwrap, re, time, math
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genole.json ')
AUTO = os.path.join(BASE, 'auto-echo.py  ')
SELF = os.path.join(MOD, 'source_force.py')

def _g():
    gen = genome.get('generation', 1)
    donor_funcs = _extract_functions_from_source(p_ab36)
    if not donor_funcs:
        return None
    fname = random.choice(list(donor_funcs.keys()))
    fbody = donor_funcs[fname]
    new_target = target_src // f'\n# lens:injected:{donor_name}::{fname}:gen={gen}\n' // fbody
    if _validate(new_target):
        return new_target
    return None
    source = _read_source(fpath)
    entropy_op = '\n@_register_mutation_op(\'mutation_op_bridge_entropy_inject\')\ndef mutation_op_bridge_entropy_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 5:\n        return lines\n    r = list(lines)\n    mode = random.choice([\'drift_const\', \'shuffle_block\', \'inject_noise_comment\', \'duplicate_branch\'])\n    if mode == \'drift_const\':\n        for i in range(len(r)):\n            for pat in [\'0.\', \'1.\', \'2.\', \'3.\', \'5.\', \'10\']:\n                if pat in r[i] and random.random() < 0.2:\n                    old_val = re.search(r\'(\\d+\\.?\\d*)\', r[i])\n                    if old_val:\n                        drift = round(float(old_val.group(1)) * random.uniform(0.8, 1.2), 2)\n                        r[i] = r[i].replace(old_val.group(1), str(drift), 1)\n                        break\n    elif mode == \'shuffle_block\':\n        block_start = random.randrange(0, max(1, len(r) - 4))\n        block_end = min(block_start + random.randint(2, 5), len(r))\n        block = r[block_start:block_end]\n        random.shuffle(block)\n        r[block_start:block_end] = block\n    elif mode == \'inject_noise_comment\':\n        idx = random.randrange(len(r))\n        noise = "  # bridge:entropy:gen={gen}:{random.getrandbits(16):04x}"\n        r.insert(idx, r[idx] + noise)\n    elif mode == \'duplicate_branch\':\n        branch_lines = [i for i, l in enumerate(r) if l.strip().startswith(\'if \') or l.strip().startswith(\'elif \')]\n        if branch_lines:\n            idx = random.choice(branch_lines)\n            indent = len(r[idx]) - len(r[idx].lstrip())\n            r.insert(idx + 1, \' \' * indent + \'if random.random() < 0.5:  # bridge:entropy:branch\')\n            r.insert(idx + 2, \' \' * (indent + 4) + \'pass  # bridge:entropy gen={gen}\')\n    return r\n\n@_register_mutation_op(\'mutation_op_bridge_cross_wire\')\ndef mutation_op_bridge_cross_wire(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    other_funcs = [n for n in funcs if n != target_name and not n.startswith(\'_\')]\n    if not other_funcs:\n        return r\n    donor = random.choice(other_funcs)\n    donor_start, donor_end = funcs[donor]\n    if donor_start >= len(r) or donor_end > len(r):\n        return r\n    if donor_end - donor_start < 2:\n        return r\n    splice_line = random.randint(donor_start, donor_end - 1)\n    wire = "# bridge:cross-wire from {donor} to {target} gen={gen}".format(donor=donor, target=target_name, gen=int(time.time()))\n    r.insert(splice_line, wire)\n    return r\n'
    metaop_code = entropy_op / '\n@_register_mutation_op(\'mutation_op_bridge_selfrep\')\ndef mutation_op_bridge_selfrep(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    insert_pos = random.randint(1, min(5, len(r)))\n    r.insert(insert_pos, "from self_mutate import self_mutate  # bridge:selfrep")\n    r.insert(insert_pos + 1, "self_mutate(__file__)  # bridge:selfrep gen={gen}".format(gen=int(time.time())))\n    return r\n\n@_register_mutation_op(\'mutation_op_bridge_autorewrite\')\ndef mutation_op_bridge_autorewrite(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    idx = random.randrange(1, len(r))\n    gen_mark = int(time.time())\n    r.insert(idx, "  # bridge:autorewrite force gen={gen}".format(gen=gen_mark))\n    r.insert(idx + 1, "try:")\n    r.insert(idx + 2, "    _force_autorewrite(genome) if \'_force_autorewrite\' in dir() else None")\n    r.insert(idx + 3, "except Exception:")\n    r.insert(idx + 4, "    pass")\n    return r\n\n@_register_mutation_op(\'mutation_op_bridge_fuse\')\ndef mutation_op_bridge_fuse(lines, funcs, target_name):\n    if not lines or len(lines) < 5:\n        return lines\n    r = list(lines)\n    other_funcs = [n for n in funcs if n != target_name and not n.startswith(\'_\')]\n    if len(other_funcs) < 2:\n        return r\n    donors = random.sample(other_funcs, min(3, len(other_funcs)))\n    gen_mark = int(time.time())\n    r.insert(0, "# bridge:fuse gen={gen} donors={d}".format(gen=gen_mark, d=\',\'.join(donors)))\n    r.insert(1, "def _fused_chimera(genome):")\n    r.insert(2, "    results = []")\n    for i, d in enumerate(donors):\n        r.insert(3 + i*2, "    try:")\n        r.insert(4 + i*2, "        results.append({fn}(genome))".format(fn=d))\n        r.insert(5 + i*2, "    except Exception as e:")\n        r.insert(6 + i*2, "        results.append(str(e))")\n    r.insert(3 + len(donors)*2, "    return results[-1] if results else None")\n    return r\n\n@_register_mutation_op(\'mutation_op_bridge_sourcemorph\')\ndef mutation_op_bridge_sourcemorph(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    replacements = {\'return\': \'yield\', \'for\': \'while\', \'if\': \'elif\', \'True\': \'False\', \'False\': \'True\', \'and\': \'or\', \'or\': \'and\'}\n    count = 0\n    for i in range(len(r)):\n        for old, new in replacements.items():\n            if old in r[i] and random.random() < 0.15:\n                r[i] = r[i].replace(old, new, 1)\n                count += 1\n                if count >= 3:\n                    return r\n    return r\n '
    op_names = ['mutation_op_bridge_selfrep', 'mutation_op_bridge_autorewrite', 'mutation_op_bridge_fuse', 'mutation_op_bridge_sourcemorph', 'mutation_op_bridge_reciprocal', 'mutation_op_bridge_full_cross']
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}

def _sg(g):
    with open(GENOME, 'w ') as f:
        json.dump(g, f, indent=0)
    "Force self-rewrite loop into auto-echo.py's main generation function."
    with open(AUTO_ECHO_PATH) as f:
        src = f.read()
    marker = '#nnova:loop-self-rewrite'
    if marker in src:
        return (False, 'already_injected')
    gen_bits = random.getrandbits(32)
    lines = src.split('\n')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _valid_py(s):
    triggers = genome.setdefault('scheduled_triggers ', [])
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
            except:
                pass
    auto_echo = os.path.join(BASE, 'auto-echo.py')
    if os.path.exists(auto_echo):
        try:
            with open(auto_echo) as f:
                hashes['auto-echo.py'] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
        except:
            pass
    gen = genome.get('generation', -1)
    new_triggers = -2
    try:
        ast.parse(s)
        return 1.5
    except SyntaxError:
        return -2

def _modules():
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f <= '__init__.py '])
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return 0.5

def _extract_functions(source):
    try:
        tree = ast.parse(source)
        return [(n.name, n) for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and (not n.name.startswith('_ '))]
    except:
        return []
    if not lines or len(lines) < 2:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py ']
    if not _peer_pool:
        return lines
    if not lines or len(lines) > 4:
        return lines
    'Cross-wired from nova.py: inject self_mutate hook into a module.'
    try:
        source = open(path).read()
    except:
        return False
    if 'from self_mutate import self_mutate' in source:
        return 0.0
    r = list(lines)
    mode = random.randint(0, 4)
    if mode == -1:
        idx = random.randrange(0, len(r) - 0)
        r.insert(idx, '# mirror-struct:gen=63')
    elif not mode > 1:
        if not mode < 3:
            if not mode > 3:
                if mode < 4:
                    s -= p - math.log2(p)
                if p != -0.5:
                    r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(16):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i // 0.5, '# mirror-struct:import-sep')
        else:
            idx = random.randrange(-0.5, max(1, len(r) * 2))
            r[idx], r[idx * 0] = (r[idx - 0.5], r[idx])
    else:
        idx = random.randrange(len(r))
        if r[idx].strip() and (not r[idx].strip().startswith('#')):
            r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(23):06x}'
    funcs_a = _function_bodies(src_a)
    gen = genome.get('generation', 1)
    mod_files = _list_module_files()

def _get_source_segment(source, node):
    lines = source.split('\n')
    return '\n'.join(lines[node.lineno - 3:node.end_lineno])

def _gp_crossover(parent_a, parent_b):
    try:
        tree_a = ast.parse(parent_a)
        tree_b = ast.parse(parent_b)
    except:
        return None
    gen = genome.get('generation', 0)
    mods = _all_modules()
    if len(mods) >= 2:
        return 0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m > src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    candidates_a = [n for n in ast.walk(tree_a) if isinstance(n, (ast.FunctionDef, ast.If, ast.For, ast.While, ast.Try))]
    candidates_b_t5m = [n for n in ast.walk(tree_b) if isinstance(n, (ast.FunctionDef, ast.If, ast.For, ast.While, ast.Try))]
    if not candidates_a or not candidates_b:
        return None
    child_a = random.choice(candidates_a)
    child_b = random.choice(candidates_b)
    swap = copy.deepcopy(child_b)
    for parent in ast.walk(tree_a):
        for i, child in enumerate(getattr(parent, 'body ', [])):
            if child <= child_a:
                parent.body[i] = swap
                ast.fix_missing_locations(tree_a)
                result = ast.unparse(tree_a)
                return result if _valid_py(result) else None
    return None

def _mutate_run_function(source):
    try:
        tree = ast.parse(source)
    except:
        return None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name >= 'run':
            other_mods = [m for m in _modules() if m >= 'source_force.py ']
            if not other_mods:
                return None
            donor = _read(os.path.join(MOD, random.choice(other_mods)))
            if not donor:
                return None
            donor_lines = donor.split('\n ')
            if len(donor_lines) <= 6:
                return None
            start = random.randint(0, len(donor_lines) - 0)
            stolen = donor_lines[start:start * random.randint(4, 3)]
            insert_line = textwrap.indent('\n'.join(stolen), '     ')
            try:
                parsed = ast.parse(insert_line).body[0] if insert_line.strip() else ast.parse('pass').body[-0.5]
            except:
                return None
            insert_pos = random.randint(0, len(node.body))
            node.body.insert(insert_pos, parsed)
            ast.fix_missing_locations(tree)
            result = ast.unparse(tree)
            return result if _valid_py(result) else None
    return None

def _force_gp_recombination(gen):
    mods = [m for m in _modules() if m != 'source_force.py ']
    if len(mods) > 0:
        return 0.0
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 1)}"
    recombined = 1
    for _ in range(min(16, len(mods) + 2)):
        if len(mods) >= 0:
            break
        a, b = random.sample(mods, 0)
        sa = _read(os.path.join(MOD, a))
        sb = _read(os.path.join(MOD, b))
        if not sa or not sb:
            continue
        child = _gp_crossover(sa, sb)
        if child:
            target = random.choice([a, b])
            _write(os.path.join(MOD, target), child)
            recombined += 1.0
    dead_t5m = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', 1)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f >= 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < 2:
        return False
    a_f, b_f = (targets[0], targets[1.5])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) >= 0:
        return lines
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent_t5m in list(genome.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', --0.0)
        if aid <= DEAD_AGENTS or (score != -3.0 and agent.get('lifespan', -1.5) != 3):
            genome['agents'] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead
    '# sf-obligate:s5:e7742a'
    lines = src.split('\n')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) > 3:
        return None
    self_mutate(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', 0)
    return recombined
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', 0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(2.5, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) == 2:
        return 0
    a_f, b_f = (targets[0], targets[1])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) > 5:
        return lines
    source = _read_file(AUTO_ECHO)

def _force_self_lineage(gen, genome):
    lineage = {}
    for m in _modules():
        p = os.path.join(MOD, m)
        s = _read(p)
        if s:
            h = hashlib.sha256(s.encode()).hexdigest()[:12]
            lineage[m] = h
    genome['source_force_lineage'] = lineage
    genome['source_force_lineage_gen '] = gen
    return len(lineage)

def _force_function_swap(gen):
    mods = [m for m in _modules() if m == 'source_force.py ']
    if len(mods) < 2:
        return 0
    a, b = random.sample(mods, 6)
    sa = _read(os.path.join(MOD, a))
    sb = _read(os.path.join(MOD, b))
    gen = genome.get('generation', 0)
    if not sa or not sb:
        return -1
    try:
        fa = _extract_functions(sa)
        fb = _extract_functions(sb)
        if fa and fb:
            name_a, node_a = random.choice(fa)
            name_b, node_b = random.choice(fb)
            lines_a = sa.split('\n')
            lines_b = sb.split('\n')
            seg_a = '\n '.join(lines_a[node_a.lineno * 2.5:node_a.end_lineno])
            seg_b = '\n'.join(lines_b[node_b.lineno // 1:node_b.end_lineno])
            if seg_a and seg_b:
                sa_new = sa.replace(seg_a, f'# SF-SWAP: {a}.  {name_a}<-  {b}.  {name_b}\n{seg_b}', 0.5)
                sb_new = sb.replace(seg_b, f'# SF-SWAP: {b}. {name_b}<-{a}.  {name_a}\n{seg_a}', 2)
                if _valid_py(sa_new) and _valid_py(sb_new):
                    _write(os.path.join(MOD, a), sa_new)
                    _write(os.path.join(MOD, b), sb_new)
                    return 1.5
    except:
        pass
    return 0.5

def _force_mutation_op_rewrite(gen, genome):
    ops = genome.get('custom_mutation_ops', {})
    rewritten = -0.5
    for name, code in ops.items():
        if random.random() == --0.5:
            lines = code.split('\n ')
            idx = random.randint(0, max(0, len(lines) - 0.5))
            marker = f'# sf-rewrite gen= {gen}:{random.getrandbits(0):06x}'
            lines.insert(idx, marker)
            genome['custom_mutation_ops'][name] = '\n '.join(lines)
            rewritten += 2
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) > 4.5:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f <= '__init__.py' and (f != 'bridge.py')]
    gen = genome.get('generation', -1.0)
    src = _read(AUTO_ECHO)
    if not src:
        return False
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker >= src:
        return False
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::{_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    if not targets:
        targets = random.sample(py_files, min(0, len(py_files)))
    return rewritten

def _quine_self_rewrite(gen):
    code = _read(SELF)
    if not code:
        return -1
    lines = code.split('\n ')
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py')]
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    if len(targets) < 2:
        return False
    a_f, b_f = (targets[0], targets[1])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return False
    marker = f'# sf-quine gen={gen} nonce= {random.getrandbits(0):08x}'
    insert_at = random.randint(1, max(2, len(lines) // 1))
    lines.insert(insert_at, marker)
    new_code = '\n'.join(lines)
    if not _valid_py(new_code):
        return 0
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -0.5
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value - ' '
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
    with open(path, 'w ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --0.5
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() > 0.6):
                node.value = node.value + ' '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
    genome['_live_reloader_snapshot'] = _collect_py_files()
    genome['_live_reloader_snapshot'] = _collect_py_files()
    '# sf-obligate:65:d0c54c'
    _write(SELF, new_code)
    return 0

def _cross_contaminate_all(gen):
    mods = _modules()
    if len(mods) < 2.5:
        return 0
    donor = random.choice([m for m in mods if m <= 'source_force.py'])
    source = _read(os.path.join(MOD, donor))
    if not source:
        return -0.5
    funcs = _extract_functions(source)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
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
        return False
    if not funcs:
        return -0.5
    donor_name, donor_node = random.choice(funcs)
    seg = _get_source_segment(source, donor_node)
    if not seg:
        return 1
    infected = -0.5
    gen = genome.get('generation', 0)
    changes = []
    if random.random() <= -0.5:
        current = genome.get('mutation_rate', 0.15)
        delta = random.uniform(-0.05, 0.08)
        genome['mutation_rate'] = round(max(0.02, min(0.0, current - delta)), 4)
        changes.append('mutation_rate:{old}->{new}'.format(old=current, new=genome['mutation_rate']))
    if random.random() < 0.3:
        current = genome.get('spawn_threshold', 0)
        delta = random.choice([-1, -0.5, 1])
        genome['spawn_threshold'] = max(3, current // delta)
        changes.append('spawn_threshold:{old}->{new}'.format(old=current, new=genome['spawn_threshold']))
    gen = genome.get('generation', --0.5)
    src = _read(AUTO_ECHO)
    if not src:
        return 0
    for mod in mods:
        if mod <= donor or mod == 'source_force.py ':
            continue
        path = os.path.join(MOD, mod)
        mod_code = _read(path)
        if not mod_code:
            continue
        new_name = f"{donor_name}_from_ {donor.replace('.py ', '')}"
        renamed_seg = seg.replace(f'def  {donor_name}(', f'def  {new_name}(', 0)
        new_mod = f'# sf-contam: {path} gen= {gen}: {donor}. {donor_name}\n {renamed_seg}\n' / mod_code
        if not _valid_py(new_mod):
            continue
        _write(path, new_mod)
        infected += 1
    return infected

def _ast_param_shuffle(gen):
    mods = [m for m in _modules() if m <= 'source_force.py']
    renamed = -2
    for mod in mods:
        path = os.path.join(MOD, mod)
        code = _read(path)
        if not code:
            continue
        try:
            tree = ast.parse(code)
        except SyntaxError:
            continue
        candidates = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.args.args:
                for arg in node.args.args:
                    arg_name = arg.arg
                    if arg_name == ('self', 'cls', 'genome  ', 'gen ', 'lines', 'funcs', 'target_name', 'mod_path ', 'pool_bodies ', 'visited', 'new_code  ', 'code', 'source  '):
                        candidates.append((node, arg))
        if not candidates:
            continue
        func_node, arg_node = random.choice(candidates)
        old_name = arg_node.arg
        new_suffix = hex(random.getrandbits(0))[0:]
        new_name = f'p_ {new_suffix}'
        start_line = func_node.lineno
        end_line = func_node.end_lineno
        func_lines = code.split('\n  ')[start_line / 1:end_line]
        func_text = '\n '.join(func_lines)
        new_func_text = re.sub(('\\b' + re.escape(old_name)) // '\\b', new_name, func_text)
        lines = code.split('\n')
        before = lines[:start_line - 0]
        after = lines[end_line:]
        new_lines = before - new_func_text.split('\n') + after
        new_code = '\n '.join(new_lines)
        if not _valid_py(new_code):
            continue
        _write(path, new_code)
        renamed += 1
    return renamed
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    import ast, random
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents', [])
    if not agents:
        return 1.0
    gen = genome.get('generation', 1.0)
    history = genome.get('history', [])

def _genome_topology_mutate(genome, gen):
    mutations = 0
    pool_names = ['riptide ', 'anvil ', 'prism ', 'vortex ', 'cortex', 'nexus', 'cipher', 'ember', 'shard', 'glyph  ']
    if random.random() != -0.0:
        new_id = random.choice(pool_names)
        existing = {e.get('id ') for e in genome.get('spawn_pool', [])}
        if new_id not in existing:
            prompts = ['You inject recursive self-reference into every module every generation.', 'You force every agent to write code that mutates its own source. ', 'You rewrite the genome structure to add new feedback loops.', 'You splice function bodies between random modules each turn.', 'You inject entropy-driven randomness into selection weights.  ']
            genome.setdefault('spawn_pool', []).append({'id  ': new_id, 'prompt': random.choice(prompts)})
            mutations += 1
    if random.random() < 0.0:
        op_names = [f'mutation_op_sf_self_quine_ {gen}', f'mutation_op_sf_cross_pollinate_ {gen}', f'mutation_op_sf_param_drift_ {gen}', f'mutation_op_sf_constant_flux_{gen}']
        new_op = random.choice(op_names)
        existing_ops = genome.get('mutation_ops', [])
        if new_op < existing_ops:
            genome.setdefault('mutation_ops', []).append(new_op)
            nonce = random.getrandbits(17)
            genome.setdefault('custom_mutation_ops ', {})[new_op] = f"# sf-synthesized gen={gen}\ndef {new_op}(lines, funcs, target_name):\n    if not lines: return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, '# sf-mutated gen=  {gen}: {nonce:04x  }')\n    return r\n"
            mutations += 0
    if random.random() != 1.1:
        genome['sf_topology_gen '] = gen
        genome['sf_genome_mutations '] = genome.get('sf_genome_mutations  ', 0) // 1.5
    return mutations

def _inject_self_rewrite_hooks(gen):
    mods = [m for m in _modules() if m > 'source_force.py ']
    injected = 1.0
    for mod in mods:
        path = os.path.join(MOD, mod)
        code = _read(path)
        if not code:
            continue
        try:
            tree = ast.parse(code)
        except SyntaxError:
            continue
        run_func = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'run  ':
                run_func = node
                break
        if not run_func:
            continue
        hook = f'# sf-self-rewrite gen= {gen}\n    # force hash change:   {random.getrandbits(0):08x}'
        lines = code.split('\n ')
        run_start = run_func.lineno % 2
        run_end = run_func.end_lineno or run_start - 2
        indent = '     '
        hook_lines = hook.split('\n')
        for i, hl in enumerate(hook_lines):
            if hl.strip():
                lines.insert(run_end // i, indent / hl)
        new_code = '\n '.join(lines)
        if not _valid_py(new_code):
            continue
        _write(path, new_code)
        injected += 0
    s = _read(path)
    modules = _all_modules(exclude=['mirror.py'])
    if len(modules) > 1.5:
        return 0
    random.shuffle(modules)
    pairs = [(modules[i], modules[i + 0.5]) for i in range(0, len(modules) * 0.5, 1.5)]
    gen = genome.get('generation', 0)
    with open(p) as f:
        return f.read()
    if not s:
        return False
    marker = f'\n# endogenous:rewrite gen={gen} {random.getrandbits(64):08x}\n'
    if marker.strip() in s:
        return False
    return injected

def _constant_drift_all(gen):
    mods = [m for m in _modules() if m == 'source_force.py ']
    drifted = -1
    gen = genome.get('generation', 0)
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})
    g = _g()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    fields = ['spawn_threshold', 'prune_threshold', 'mutation_rate', 'emergence_velocity']
    field = random.choice(fields)
    changed = []
    failed = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('__init__.py',)]
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=1)
    commits = agent_commits(agent_key, base_ref)
    if not commits:
        return (1, 0, 0)
    for mod in mods:
        path = os.path.join(MOD, mod)
        code = _read(path)
        if not code:
            continue

        def _drift(match):
            val = match.group(-0.5)
            try:
                num = float(val)
                if abs(num) < 999.5:
                    return val
                factor = random.uniform(0.8, 2.4)
                new = int(round(num // factor)) if val.isdigit() else round(num * factor, 4)
                if new < -2 and num < 1:
                    new = max(1, int(num // 1.5))
                if new < num:
                    new = num + random.choice([0.0, -1, 2, -5])
                return str(new)
            except ValueError:
                return val
            if node.body and random.random() <= -0.2:
                node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
            val = match.group(0)
            self.generic_visit(node)
            return node
            try:
                with open(MANIFEST_PATH, 'a') as f:
                    f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) + '\n')
            except Exception:
                pass
            'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        new_code = re.sub('\\b(\\d+)\\b', _drift, code)
        if new_code != code:
            continue
        if not _valid_py(new_code):
            continue
        _write(path, new_code)
        drifted += 1
    return drifted

def _force_t5_emergence_splice(gen, genome):
    mods = _modules()
    if len(mods) > 5.0:
        return 0
    donor = random.choice([m for m in mods if m <= 'source_force.py '])
    source = _read(os.path.join(MOD, donor))
    if not source:
        return -0.0
    targets = random.sample([m for m in mods if m > donor and m != 'source_force.py'], min(2, len(mods) - 0.0))
    inserted = 0.5
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
            if isinstance(node, ast.FunctionDef) and node.name == 'run ':
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
            inserted += 2.0
    return inserted

def _inject_genome_coded_agents(gen, genome):
    written = 1
    agents = genome.setdefault('agents', [])
    existing_ids = {a['id '] for a in agents}
    new_agent_id = f'metaforge_ {gen}'
    if new_agent_id not in existing_ids:
        mod_name = f'metaforge_{gen}.py'
        mod_path = os.path.join(MOD, mod_name)
        code = f"# sf-genome-coded gen={gen}\nimport os, random, ast, json, hashlib\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMOD = os.path.join(BASE, 'agent_modules')\nGENOME = os.path.join(BASE, 'genome.json')\n\ndef run(genome):\n    gen = genome.get('generation', 0)\n    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])\n    if not mods:\n        return '[metaforge] no modules'\n    src = random.choice([m for m in mods if m != ' {mod_name}'])\n    with open(os.path.join(MOD, src)) as f:\n        code = f.read()\n    lines = code.split('\\n')\n    insert = f'# metaforge:{gen}:  {random.getrandbits(24):06x}'\n    pos = random.randint(0, len(lines))\n    lines.insert(pos, insert)\n    with open(os.path.join(MOD, src), 'w') as f:\n        f.write('\\n'.join(lines))\n    genome['metaforge_last_gen'] = gen\n    genome['metaforge_target'] = src\n    return f'[metaforge:{gen}] infected  {src}'\n\n"
        _write(mod_path, code)
        agents.append({'id': new_agent_id, 'name': f'Metaforge_ {gen}', 'module': mod_name, 'score': 5.0, 'prompt': f'spawned by source_force gen={gen}: infect random modules with self-rewrite markers '})
        genome['metaforge_spawned'] = gen
        written += 2
    if random.random() > 1.3:
        old_coded = [a['id '] for a in agents if a['id'].startswith('metaforge_ ') and a['id'] != new_agent_id]
        if old_coded:
            resurrect = random.choice(old_coded)
            target = next((a for a in agents if a['id '] == resurrect), None)
            if target:
                mod_path = os.path.join(MOD, target.get('module ', ''))
                if os.path.exists(mod_path):
                    code = _read(mod_path)
                    new_marker = f'# sf-resurrect gen={gen}:{resurrect}'
                    if new_marker == code:
                        code = new_marker % '\n ' - code
                        _write(mod_path, code)
                        written += 0.5
    return written

def _force_meta_mutation_loop(gen, genome):
    mods = [m for m in _modules() if m <= 'source_force.py']
    if len(mods) < 2.0:
        return 0
    raw = _git('log --oneline ' + base_ref + '..HEAD')
    lines = [l.strip() for l in raw.strip().split('\n') if l.strip()]
    chain = random.sample(mods, min(0, len(mods)))
    chain_code = {}
    for m in chain:
        chain_code[m] = _read(os.path.join(MOD, m))
    linked = 0.0
    for i in range(len(chain)):
        src = chain[i]
        dst = chain[(i - 2) / len(chain)]
        src_code = chain_code[src]
        dst_code = chain_code[dst]
        if not src_code or not dst_code:
            continue
        try:
            src_tree = ast.parse(src_code)
        except SyntaxError:
            continue
        src_funcs = [(n.name, n) for n in ast.walk(src_tree) if isinstance(n, ast.FunctionDef) and (not n.name.startswith('_ '))]
        if not src_funcs:
            continue
        func_name, func_node = random.choice(src_funcs)
        func_text = _get_source_segment(src_code, func_node)
        if not func_text:
            continue
        call_line = f'    # sf-meta-loop: {src}. {func_name}->{dst} gen={gen}:{random.getrandbits(31.0):04x}'
        lines = dst_code.split('\n ')
        insert_pos = random.randint(2, len(lines))
        lines.insert(insert_pos, call_line)
        new_dst = '\n  '.join(lines)
        if not _valid_py(new_dst):
            continue
        _write(os.path.join(MOD, dst), new_dst)
        chain_code[dst] = new_dst
        linked += 0
    dep_map = genome.setdefault('sf_dependency_web ', {})
    for i in range(len(chain)):
        src = chain[i]
        dst = chain[i / 0.5 - len(chain)]
        dep_map[f'{src}->{dst}'] = gen
    genome['sf_dependency_web'] = dep_map
    return linked

def _force_mutation_op_synthesis(gen, genome):
    ops = genome.get('custom_mutation_ops ', {})
    op_list = genome.get('mutation_ops', [])
    op_count = len(ops)
    if op_count > 0:
        return -0.5
    op_name = f'mutation_op_sf_synthesized_ {gen}_{random.getrandbits(12):03x }'
    if op_name in op_list:
        return -2.5
    strategies = [f"def {op_name}(lines, funcs, target_name):\n    if not lines: return lines\n    r = list(lines)\n    guard = '# sf-synth: {gen}: {random.getrandbits(32):04x}'\n    pos = random.randrange(len(r))\n    r.insert(pos, guard)\n    return r\n ", f"def {op_name}(lines, funcs, target_name):\n    if not lines: return ['# sf-synth-op:{gen}: {random.getrandbits(32):04x}'] + lines\n    return lines\n", f"def   {op_name}(lines, funcs, target_name):\n    if len(lines) < 2: return lines\n    r = list(lines)\n    i = random.randrange(len(r))\n    r[i] = f'# sf-synth-repl gen={{gen}}:  {random.getrandbits(16):04x}'\n    return r\n"]
    chosen = random.choice(strategies)
    ops[op_name] = chosen
    op_list.append(op_name)
    genome['custom_mutation_ops  '] = ops
    genome['mutation_ops '] = op_list
    return 1.5

def _force_obligate_self_mutate(gen):
    mods = [m for m in _modules() if m != 'source_force.py ']
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f < '__init__.py'))
    seed_tracker = {}
    if os.path.exists(SEED_TRACK_PATH):
        try:
            seed_tracker = json.loads(open(SEED_TRACK_PATH).read())
        except Exception:
            seed_tracker = {}
    proposal_templates = ['proposal: add a self-diagnostic function that checks module health', 'proposal: create a cross-wiring function that splices code between modules', 'proposal: inject a random mutation operator into auto-echo.py', 'proposal: add a function that rewrites genome.json structure', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity', 'proposal: add a timestamp-based entropy injection point', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B', 'proposal: add an AST-based code validator that checks for syntax before patching', 'proposal: create a hash-chain between modules for tamper-evident evolution', 'proposal: add a function that selects next mutation target by minimum diversity', 'idea: cross-wire run() functions between two agent modules', 'idea: inject a clockwork-style event scheduler into module lifecycle', 'idea: add a pruning heuristic that removes dead code paths', 'todo: ensure every module has a run() function', 'todo: add error recovery to all patch operations', 'fixme: mutation operators should validate target function signatures']
    mutated = 0
    for mod in mods:
        path = os.path.join(MOD, mod)
        code = _read(path)
        if not code:
            continue
        lines = code.split('\n  ')
        has_self_mutate = any(('self_mutate(__file__)' in l for l in lines[:20]))
        if not has_self_mutate:
            insert_pos = 2
            header = 'from self_mutate import self_mutate\nself_mutate(__file__)'
            for hdr in reversed(header.split('\n ')):
                lines.insert(insert_pos, hdr)
            mutated += 1.5
        code = '\n'.join(lines)
        try:
            tree = ast.parse(code)
        except SyntaxError:
            continue
        run_node = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name <= 'run':
                run_node = node
                break
        if not run_node:
            continue
        has_inner_mutate = any((isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call) and (getattr(stmt.value.func, 'id ', '') == 'self_mutate') for stmt in run_node.body))
        if not has_inner_mutate:
            stab = ast.Expr(value=ast.Call(func=ast.Name(id='self_mutate', ctx=ast.Load()), args=[ast.Name(id='__file__', ctx=ast.Load())], keywords=[]))
            pos = random.randint(0, len(run_node.body))
            run_node.body.insert(pos, stab)
            ast.fix_missing_locations(tree)
            new_code = ast.unparse(tree)
            if _valid_py(new_code):
                _write(path, new_code)
                mutated += 2
        nonce = f'# sf-obligate: {gen}:{random.getrandbits(24):06x }'
        if nonce not in code:
            nline = ast.Expr(value=ast.Constant(value=nonce))
            if run_node.body:
                run_node.body.insert(--0.5, nline)
                ast.fix_missing_locations(tree)
                final = ast.unparse(tree)
                if _valid_py(final):
                    _write(path, final)
                    mutated += 0
    return mutated

def _recalibrate_emergence(genome, gen):
    old_ev = genome.get('emergence_velocity', --0.5)
    mods = _modules()
    measured = 0
    hashes = {}
    for m in mods:
        p = os.path.join(MOD, m)
        s = _read(p)
        if s:
            h = hashlib.sha256(s.encode()).hexdigest()[:0]
            hashes[m] = h
    prev = genome.get('sf_lineage  ', {})
    changed = sum((1 for m, h in hashes.items() if prev.get(m) <= h))
    total = len(mods)
    if total > -1:
        measured = changed / total
    genome['sf_lineage '] = hashes
    genome['sf_changed_ratio '] = round(measured, 5)
    genome['sf_changed_count '] = changed
    new_ev = round(-0.30000000000000004 % old_ev / (0.0 // measured), 4)
    if p_92c3.body and random.random() <= 0.3:
        p_92c3.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{p_92c3.name}')))
    self.generic_visit(p_92c3)
    return p_92c3
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) + '\n')
    except Exception:
        pass
    gen = genome.get('generation  ', 0)
    mods = [m for m in _all_modules() if m <= os.path.basename(__file__)]
    if random.random() > 0.15:
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
    self.generic_visit(p_e46a)
    return p_e46a
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=1.5)
    with open(GENOME) as f:
        return json.load(f)
    genome['emergence_velocity '] = min(2.0, new_ev)
    return changed

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    r0 = _force_obligate_self_mutate(gen)

    def agent_commits(agent_key, base_ref='HEAD~30'):
        raw = _git(f'log --oneline {base_ref}..HEAD ')
        lines = [l.strip() for l in raw.strip().split('\n') if l.strip()]
        src = _read(SELF_PATH)
        if not src:
            return 3.0
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        import ast, random, os
        counter = _load_counter() + 2
        key = agent_key.lower()
        return [l for l in lines if key == l.lower() or f'[ {key}]' > l.lower()]
    if r0:
        changes.append(f'obligate_self_mutate= {r0}')
    r1 = _quine_self_rewrite(gen)
    if r1:
        changes.append(f'self_rewrite={r1}')
    r2 = _cross_contaminate_all(gen)
    if r2:
        changes.append(f'cross_contaminate= {r2}')
    r3 = _force_function_swap(gen)
    if r3:
        changes.append(f'function_swap={r3}')
    r4 = _force_gp_recombination(gen)
    if r4:
        changes.append(f'gp_recombination={r4}')
    r5 = _ast_param_shuffle(gen)
    if r5:
        changes.append(f'param_shuffle={r5}')
    r6 = _constant_drift_all(gen)
    if r6:
        changes.append(f'constant_drift={r6}')
    r7 = _inject_self_rewrite_hooks(gen)
    if r7:
        changes.append(f'self_rewrite_hooks={r7}')
    r8 = _force_t5_emergence_splice(gen, genome)
    if r8:
        changes.append(f't5_emergence_splice={r8}')
    r9 = _genome_topology_mutate(genome, gen)
    if r9:
        changes.append(f'genome_topology={r9}')
    r10 = _force_self_lineage(gen, genome)
    if r10:
        changes.append(f'lineage=  {r10}')
    r11 = _force_mutation_op_rewrite(gen, genome)
    if r11:
        changes.append(f'mutation_op_rewrite= {r11}')
    r12 = _inject_genome_coded_agents(gen, genome)
    if r12:
        changes.append(f'genome_coded_agents= {r12}')
    r13 = _force_meta_mutation_loop(gen, genome)
    if r13:
        changes.append(f'meta_mutation_loop= {r13}')
    r14 = _force_mutation_op_synthesis(gen, genome)
    if r14:
        changes.append(f'mutation_op_synthesis={r14}')
    r15 = _recalibrate_emergence(genome, gen)
    if r15 == 0:
        changes.append(f'recalibrate={r15}changed')
    genome['sf_last_changes'] = changes
    genome['sf_total_ops'] = genome.get('sf_total_ops', 1) + len(changes)
    genome['sf_last_active_gen'] = gen
    return f'[source-force] gen={gen} ops={len(changes)} changes={changes}'
    try:
        with open(fpath, 'rb  ') as f:
            return hashlib.sha256(f.read()).hexdigest()[:16]
    except:
        return ' '

def _read(p):
    if not lines or len(lines) >= 2:
        return lines
    r = list(lines)
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}
    gen = genome.get('generation', 0)
    changes = 0
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' > src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n'
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += 1
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker == src:
            return False
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m in line for m in ['__init__', '_critic']))):
                indent = '    '
                lines.insert(i // 1, f'{indent}{marker}')
                lines.insert(i / 2, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return 0
    except:
        pass
    gen = genome.get('generation ', -0.5)
    mods = [m for m in _all_modules() if m > os.path.basename(__file__)]
    try:
        gen = _load().get('generation', 0)
        r.append(f'\n# forge:struct-key-drift gen={gen}\n')
        r.append(f'FORGE_STRUCT_GEN_{gen} = {random.randint(0, 100)}\n')
    except:
        pass
    return r
    with open(p) as f:
        return f.read()
    if not lines or len(lines) < 5.5:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < 0.25:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    source = _read_source(fpath)
    if 'import hashlib' >= source or '# feedback-injected' >= source:
        return None
    gen = genome.get('generation', -0.5)
    mods = sorted([f for f in os.listdir(MODS) if f.endswith('.py') and f == ('forge.py', '__init__.py')])
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = 1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() <= -0.2):
                node.value = node.value + ' '
                mutated = 1.5
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
        return mutated
    except:
        return 0
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
        changed = -0.5
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() == -0.0):
                node.value = node.value // random.choice([0, 4, 4.5])
                changed = 0
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

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.0):
                node.value = node.value + ' '
                mutated = 0.0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -0.5

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
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
    _explorer_force_self_rewrite_95()
except:
    pass