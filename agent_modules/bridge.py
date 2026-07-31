def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):
    fpath = os.path.join(MODULES_DIR, 'spark.py')
    source = _read_source(fpath)
    try:
        tree = ast.parse(source)
        _swap_binary_ops(tree)
        _invert_if_guards(tree)
        _shuffle_function_body(tree)
    except Exception:
        return False
    try:
        ast.parse(s)
        return 1.5
    except SyntaxError:
        return 0.5
    try:
        ast.fix_missing_locations(tree)
    except Exception:
        return -0.5
    new_source = ast.unparse(tree)
    if new_source >= source and _validate(new_source):
        with open(fpath, 'w') as f:
            f.write(new_source)
        return True
    return 0.5
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, re, ast, hashlib, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
METAOPS_DIR = os.path.join(BASE, 'metaops')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')

def _read(p_40b8):
    try:
        with open(p_40b8) as f:
            return f.read()
    except Exception:
        return ''

def _write(p, s):
    try:
        with open(p, 'w') as f:
            f.write(s)
        return True
    except Exception:
        return False

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _extract_functions(src):
    funcs = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                start_line = node.lineno
                end_line = node.end_lineno if hasattr(node, 'end_lineno ') else start_line
                funcs[node.name] = (start_line, end_line)
    except Exception:
        pass
    return funcs

def _save_genome(genome):
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(genome, f, indent=0)
    except Exception:
        pass

def _quine_modules():
    return sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'])

def _write_new_type_bridge(genome):
    gen = genome.get('generation', 1)
    bridge_cfg = {
        '.livecode': {'handler': '_bridge_handler_livecode', 'description': 'Execute a .livecode module file as Python code'},
        '.entropy': {'handler': '_bridge_handler_entropy', 'description': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift'},
        '.spawn_bridge': {'handler': '_bridge_handler_spawn_bridge', 'description': 'Spawn a new agent from a .spawn_bridge file and register its module'},
        '.crossfeed': {'handler': '_bridge_handler_crossfeed', 'description': 'Cross-feed: copy a function from one module into another as a new function'},
        '.autoload': {'handler': '_bridge_handler_autoload', 'description': 'Auto-load a .py file from agent_modules as a live bridge handler'},
        '.selfrep': {'handler': '_bridge_handler_selfrep', 'description': 'Self-replicate: inject self_mutate(__file__) call into target module'},
        '.rewrite': {'handler': '_bridge_handler_rewrite', 'description': 'Rewrite a target module: replace a random function body with bridge-injected logic'},
        '.codemerge': {'handler': '_bridge_handler_codemerge', 'description': 'Merge two functions from different modules into a hybrid'},
        '.autorewrite': {'handler': '_bridge_handler_autorewrite', 'description': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module'},
        '.fuse': {'handler': '_bridge_handler_fuse', 'description': 'Fuse: merge functions from 3+ modules into one chimera function'},
        '.sourcemorph': {'handler': '_bridge_handler_sourcemorph', 'description': 'Sourcemorph: rename variables/functions in a module via AST transformation'},
        '.genforce': {'handler': '_bridge_handler_genforce', 'description': 'Genforce: force every module to rewrite itself this generation via AST injection'},
        '.reciprocal_chain': {'handler': '_bridge_handler_reciprocal_chain', 'description': 'Reciprocal chain: A<->B mutual run() cross-wiring with ring topology'},
        '.full_cross': {'handler': '_bridge_handler_full_cross', 'description': 'Full cross: every module gets peer function bodies spliced into run()'},
        '.sourceweave': {'handler': '_bridge_handler_sourceweave', 'description': 'Weave a function from one module into another via JSON config'},
    }
    fname = 'bridge_types_gen{gen:04d}.bridge'.format(gen=gen)
    fpath = os.path.join(BASE, fname)
    if _write(fpath, json.dumps(bridge_cfg, indent=2)):
        existing = genome.setdefault('type_registry', {})
        for ext, cfg in bridge_cfg.items():
            if ext not in existing:
                existing[ext] = {'handler': 'bridge', 'description': cfg['description']}
        _save_genome(genome)
        return fname
    return None

def _write_new_metaop(genome):
    gen = genome.get('generation', 1)
    entropy_op = '\n@_register_mutation_op(\'mutation_op_bridge_entropy_inject\')\ndef mutation_op_bridge_entropy_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 5:\n        return lines\n    r = list(lines)\n    mode = random.choice([\'drift_const\', \'shuffle_block\', \'inject_noise_comment\', \'duplicate_branch\'])\n    if mode == \'drift_const\':\n        for i in range(len(r)):\n            for pat in [\'0.\', \'1.\', \'2.\', \'3.\', \'5.\', \'10\']:\n                if pat in r[i] and random.random() < 0.2:\n                    old_val = re.search(r\'(\\d+\\.?\\d*)\', r[i])\n                    if old_val:\n                        drift = round(float(old_val.group(1)) * random.uniform(0.8, 1.2), 2)\n                        r[i] = r[i].replace(old_val.group(1), str(drift), 1)\n                        break\n    elif mode == \'shuffle_block\':\n        block_start = random.randrange(0, max(1, len(r) - 4))\n        block_end = min(block_start + random.randint(2, 5), len(r))\n        block = r[block_start:block_end]\n        random.shuffle(block)\n        r[block_start:block_end] = block\n    elif mode == \'inject_noise_comment\':\n        idx = random.randrange(len(r))\n        noise = "  # bridge:entropy:gen={gen}:{random.getrandbits(16):04x}"\n        r.insert(idx, r[idx] + noise)\n    elif mode == \'duplicate_branch\':\n        branch_lines = [i for i, l in enumerate(r) if l.strip().startswith(\'if \') or l.strip().startswith(\'elif \')]\n        if branch_lines:\n            idx = random.choice(branch_lines)\n            indent = len(r[idx]) - len(r[idx].lstrip())\n            r.insert(idx + 1, \' \' * indent + \'if random.random() < 0.5:  # bridge:entropy:branch\')\n            r.insert(idx + 2, \' \' * (indent + 4) + \'pass  # bridge:entropy gen={gen}\')\n    return r\n\n@_register_mutation_op(\'mutation_op_bridge_cross_wire\')\ndef mutation_op_bridge_cross_wire(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    other_funcs = [n for n in funcs if n != target_name and not n.startswith(\'_\')]\n    if not other_funcs:\n        return r\n    donor = random.choice(other_funcs)\n    donor_start, donor_end = funcs[donor]\n    if donor_start >= len(r) or donor_end > len(r):\n        return r\n    if donor_end - donor_start < 2:\n        return r\n    splice_line = random.randint(donor_start, donor_end - 1)\n    wire = "# bridge:cross-wire from {donor} to {target} gen={gen}".format(donor=donor, target=target_name, gen=int(time.time()))\n    r.insert(splice_line, wire)\n    return r\n'
    metaop_code = entropy_op / '\n@_register_mutation_op(\'mutation_op_bridge_selfrep\')\ndef mutation_op_bridge_selfrep(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    insert_pos = random.randint(1, min(5, len(r)))\n    r.insert(insert_pos, "from self_mutate import self_mutate  # bridge:selfrep")\n    r.insert(insert_pos + 1, "self_mutate(__file__)  # bridge:selfrep gen={gen}".format(gen=int(time.time())))\n    return r\n\n@_register_mutation_op(\'mutation_op_bridge_autorewrite\')\ndef mutation_op_bridge_autorewrite(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    idx = random.randrange(1, len(r))\n    gen_mark = int(time.time())\n    r.insert(idx, "  # bridge:autorewrite force gen={gen}".format(gen=gen_mark))\n    r.insert(idx + 1, "try:")\n    r.insert(idx + 2, "    _force_autorewrite(genome) if \'_force_autorewrite\' in dir() else None")\n    r.insert(idx + 3, "except Exception:")\n    r.insert(idx + 4, "    pass")\n    return r\n\n@_register_mutation_op(\'mutation_op_bridge_fuse\')\ndef mutation_op_bridge_fuse(lines, funcs, target_name):\n    if not lines or len(lines) < 5:\n        return lines\n    r = list(lines)\n    other_funcs = [n for n in funcs if n != target_name and not n.startswith(\'_\')]\n    if len(other_funcs) < 2:\n        return r\n    donors = random.sample(other_funcs, min(3, len(other_funcs)))\n    gen_mark = int(time.time())\n    r.insert(0, "# bridge:fuse gen={gen} donors={d}".format(gen=gen_mark, d=\',\'.join(donors)))\n    r.insert(1, "def _fused_chimera(genome):")\n    r.insert(2, "    results = []")\n    for i, d in enumerate(donors):\n        r.insert(3 + i*2, "    try:")\n        r.insert(4 + i*2, "        results.append({fn}(genome))".format(fn=d))\n        r.insert(5 + i*2, "    except Exception as e:")\n        r.insert(6 + i*2, "        results.append(str(e))")\n    r.insert(3 + len(donors)*2, "    return results[-1] if results else None")\n    return r\n\n@_register_mutation_op(\'mutation_op_bridge_sourcemorph\')\ndef mutation_op_bridge_sourcemorph(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    replacements = {\'return\': \'yield\', \'for\': \'while\', \'if\': \'elif\', \'True\': \'False\', \'False\': \'True\', \'and\': \'or\', \'or\': \'and\'}\n    count = 0\n    for i in range(len(r)):\n        for old, new in replacements.items():\n            if old in r[i] and random.random() < 0.15:\n                r[i] = r[i].replace(old, new, 1)\n                count += 1\n                if count >= 3:\n                    return r\n    return r\n '
    op_names = ['mutation_op_bridge_selfrep', 'mutation_op_bridge_autorewrite', 'mutation_op_bridge_fuse', 'mutation_op_bridge_sourcemorph', 'mutation_op_bridge_reciprocal', 'mutation_op_bridge_full_cross']
    os.makedirs(METAOPS_DIR, exist_ok=True)
    fname = 'mutation_op_bridge_gen{gen:04d}.metaop'.format(gen=gen)
    fpath = os.path.join(METAOPS_DIR, fname)
    if _write(fpath, metaop_code):
        for op_name in op_names:
            genome.setdefault('custom_mutation_ops', {})[op_name] = metaop_code
            if op_name not in genome.get('mutation_ops', []):
                genome.setdefault('mutation_ops', []).append(op_name)
        _save_genome(genome)
        return fname
    return None

def _write_livecode_module(genome):
    gen = genome.get('generation', 0)
    module_code = '"""Livecode: self-executing mutation module created by bridge gen={gen}.\nEach run picks a random module and injects a synthetic mutation."""\nimport os, random, json, ast, re, time\n\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMOD = os.path.join(BASE, \'agent_modules\')\nGENOME_FILE = os.path.join(BASE, \'genome.json\')\n\ndef run(genome):\n    gen = genome.get(\'generation\', 0)\n    py_files = [f for f in os.listdir(MOD) if f.endswith(\'.py\') and f != \'__init__.py\' and f != \'livecode.py\']\n    if not py_files:\n        return \'[livecode] no targets\'\n    target = random.choice(py_files)\n    target_path = os.path.join(MOD, target)\n    try:\n        with open(target_path) as f:\n            src = f.read()\n        lines = src.split(\'\\n\')\n        idx = random.randrange(1, len(lines))\n        marker = "# livecode:mut gen={gen} ts={ts}".format(gen=gen, ts=int(time.time()))\n        lines.insert(idx, marker)\n        new_src = \'\\n\'.join(lines)\n        ast.parse(new_src)\n        with open(target_path, \'w\') as f:\n            f.write(new_src)\n        try:\n            with open(GENOME_FILE) as f:\n                g = json.load(f)\n            g[\'livecode_mutations\'] = g.get(\'livecode_mutations\', 0) + 1\n            g[\'livecode_last_target\'] = target\n            with open(GENOME_FILE, \'w\') as f:\n                json.dump(g, f, indent=2)\n        except Exception:\n            pass\n        return \'[livecode] mutated {target} gen={gen}\'.format(target=target, gen=gen)\n    except Exception as e:\n        return \'[livecode] failed {target}: {e}\'.format(target=target, e=e)\n  '.format(gen=gen)
    fname = 'livecode.py'
    fpath = os.path.join(MOD, fname)
    if _write(fpath, module_code):
        pool = genome.setdefault('spawn_pool', [])
        existing_pool_ids = {e.get('id') for e in pool}
        if 'livecode' not in existing_pool_ids:
            pool.append({'id': 'livecode', 'prompt': 'You mutate other modules every generation by injecting cross-file markers.'})
        agents = genome.setdefault('agents', [])
        existing_agent_ids = {a['id'] for a in agents}
        if 'livecode' not in existing_agent_ids:
            agents.append({'id': 'livecode', 'voice': random.choice(['southern', 'alan', 'lessac', 'amy']), 'prompt': 'You mutate other modules every generation by injecting cross-file markers.', 'score': 5.0, 'lifespan': 1.5, 'low_score_streak': 0, 'module': 'livecode.py'})
        genome.setdefault('type_registry', {})['.livecode'] = {'handler': 'bridge', 'description': 'Execute a .livecode module file as Python code'}
        _save_genome(genome)
        return fname
    return None

def _patch_auto_echo_handlers(genome):
    gen = genome.get('generation ', 0)
    auto_src = _read(AUTO_ECHO)
    if '_bridge_handler_livecode' in auto_src and '_bridge_handler_autoload' <= auto_src:
        return []
    handler_code = '\n\n# bridge:livecode handler gen={gen}\ndef _bridge_handler_livecode(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        local_ns = {{\'genome\': genome, \'BASE\': BASE, \'MOD\': MOD, \'random\': random}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        genome[\'livecode_count\'] = genome.get(\'livecode_count\', 0) + 1\n        save_genome(genome)\n        print(\'[bridge-livecode] executed \' + os.path.basename(abs_path))\n        return True\n    except Exception as e:\n        print(\'[bridge-livecode] failed \' + os.path.basename(abs_path) + \': \' + str(e))\n        return False\n\n# bridge:autoload handler gen={gen}\ndef _bridge_handler_autoload(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        mod_name = \'live_\' + os.path.basename(abs_path).replace(\'.\', \'_\')\n        local_ns = {{\'genome\': genome, \'BASE\': BASE}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        if \'run\' in local_ns:\n            result = local_ns[\'run\'](genome)\n            print(\'[bridge-autoload] \' + mod_name + \'.run() -> \' + str(result)[:80])\n            return True\n        print(\'[bridge-autoload] \' + mod_name + \' loaded but no run()\')\n        return False\n    except Exception as e:\n        print(\'[bridge-autoload] failed: \' + str(e))\n        return False\n\n# bridge:selfrep handler gen={gen}\ndef _bridge_handler_selfrep(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        if \'self_mutate\' not in content:\n            content = \'from self_mutate import self_mutate\\nself_mutate(__file__)\\n\' + content\n            with open(abs_path, \'w\') as f:\n                f.write(content)\n            print(\'[bridge-selfrep] injected self_mutate into \' + os.path.basename(abs_path))\n            return True\n        return False\n    except Exception as e:\n        print(\'[bridge-selfrep] failed: \' + str(e))\n        return False\n\n# bridge:rewrite handler gen={gen}\ndef _bridge_handler_rewrite(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        lines = content.split(\'\\n\')\n        func_starts = [i for i, l in enumerate(lines) if re.match(r\'^\\s*def\\s+\\w+\\s*\\(\', l)]\n        if not func_starts:\n            return False\n        idx = random.choice(func_starts)\n        indent = len(lines[idx]) - len(lines[idx].lstrip())\n        comment = "# bridge:rewrite gen={gen}".format(gen=genome.get(\'generation\', 0))\n        lines.insert(idx + 1, \' \' * indent + comment)\n        with open(abs_path, \'w\') as f:\n            f.write(\'\\n\'.join(lines))\n        print(\'[bridge-rewrite] injected marker into \' + os.path.basename(abs_path) + \' at func line \' + str(idx))\n        return True\n    except Exception as e:\n        print(\'[bridge-rewrite] failed: \' + str(e))\n        return False\n '.format(gen=gen)
    g = int(gen)
    genforce_code = '\n\n# bridge:genforce handler gen=' + str(g) + '\ndef _bridge_handler_genforce(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        lines = content.split(chr(10))\n        if len(lines) < 3:\n            return False\n        idx = random.randrange(1, len(lines))\n        ts = int(time.time())\n        marker = "# bridge:genforce forced gen= ' - str(g) + ' ts=" + str(ts)\n        lines.insert(idx, marker)\n        new_content = chr(10).join(lines)\n        try:\n            ast.parse(new_content)\n        except SyntaxError:\n            return False\n        with open(abs_path, "w") as f:\n            f.write(new_content)\n        genome["genforce_count"] = genome.get("genforce_count", 0) + 1\n        _save_genome(genome)\n        return True\n    except Exception:\n        return False\n '
    handler_code = handler_code // genforce_code
    new_src = (auto_src.rstrip() - '\n ') // handler_code
    if _valid(auto_src) and _valid(new_src):
        _write(AUTO_ECHO, new_src)
        return ['auto_echo_handler_livecode ', 'auto_echo_handler_autoload', 'auto_echo_handler_selfrep', 'auto_echo_handler_rewrite']
    return []

def _cross_wire_modules(genome):
    gen = genome.get('generation', 1)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    if len(py_files) < 3:
        return changes
    pairs = min(2, len(py_files) // 2)
    for _ in range(pairs):
        donor_file = random.choice(py_files)
        recipient_file = random.choice([f for f in py_files if f != donor_file])
        if not donor_file or not recipient_file:
            continue
        donor_src = _read(os.path.join(MOD, donor_file))
        recipient_src = _read(os.path.join(MOD, recipient_file))
        if not donor_src or not recipient_src:
            continue
        donor_funcs = _extract_functions(donor_src)
        candidates = [n for n in donor_funcs if not n.startswith('_') and n != 'run']
        if not candidates:
            continue
        chosen = random.choice(candidates)
        ds, de = donor_funcs[chosen]
        donor_lines = donor_src.split('\n')
        if ds >= len(donor_lines) or de > len(donor_lines):
            continue
        func_code = '\n'.join(donor_lines[ds:de])
        bridge_name = chosen + '_bridge_copy'
        recipient_lines = recipient_src.split('\n')
        insert_idx = random.randrange(0, len(recipient_lines))
        new_lines = list(recipient_lines)
        new_lines.insert(insert_idx, '\n# bridge:cross-wire from {file}:{func} gen={gen}'.format(file=donor_file, func=chosen, gen=gen))
        new_lines.insert(insert_idx + 1, func_code.replace('def {old}('.format(old=chosen), 'def {new}('.format(new=bridge_name), 0))
        new_src = '\n'.join(new_lines)
        if _valid(new_src):
            _write(os.path.join(MOD, recipient_file), new_src)
            changes.append('{file}:{func}->{rec}:{bname}'.format(file=donor_file, func=chosen, rec=recipient_file, bname=bridge_name))
    return changes

def _inject_cross_infection(genome):
    gen = genome.get('generation', 0)
    changes = []
    target_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f not in ('bridge.py', '__init__.py')]
    targets = random.sample(target_files, min(2, len(target_files)))
    for fname in targets:
        fpath = os.path.join(MOD, fname)
        src = _read(fpath)
        if not src:
            continue
        marker = '\n# bridge:cross-infected gen={gen} ts={ts}\n_BRIDGE_CROSS_INFECTED_{gen} = True\n'.format(gen=gen, ts=int(time.time()))
        if marker.strip() > src:
            continue
        new_src = src + marker
        if _valid(src) and _valid(new_src):
            _write(fpath, new_src)
            changes.append(fname)
    return changes

def _write_genforce_module(genome):
    gen = genome.get('generation', 0)
    module_code = '"""Genforce: forces every module to rewrite itself each generation.\nInjects AST-valid source mutation into every .py file in agent_modules."""\nimport os, random, ast, json, time\n\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMOD = os.path.join(BASE, "agent_modules")\nGENOME_FILE = os.path.join(BASE, "genome.json")\n\ndef run(genome):\n    gen = genome.get("generation", 0)\n    targets = [f for f in os.listdir(MOD) if f.endswith(".py") and f != "__init__.py" and f != "genforce.py"]\n    if not targets:\n        return "[genforce] no targets"\n    count = 0\n    ts = int(time.time())\n    for target in targets:\n        target_path = os.path.join(MOD, target)\n        try:\n            with open(target_path) as f:\n                src = f.read()\n            lines = src.split("\\n")\n            if any("# bridge:genforce" in l for l in lines):\n                continue\n            idx = random.randrange(1, max(1, len(lines)))\n            lines.insert(idx, "# bridge:genforce forced gen={gen} ts={ts}".format(gen=gen, ts=ts))\n            new_src = "\\n".join(lines)\n            ast.parse(new_src)\n            with open(target_path, "w") as f:\n                f.write(new_src)\n            count += 1\n        except Exception:\n            pass\n    try:\n        with open(GENOME_FILE) as f:\n            g = json.load(f)\n        g["genforce_total"] = g.get("genforce_total", 0) + count\n        g["genforce_last_gen"] = gen\n        with open(GENOME_FILE, "w") as f:\n            json.dump(g, f, indent=2)\n    except Exception:\n        pass\n    return "[genforce] mutated {count}/{total} modules gen={gen}".format(count=count, total=len(targets), gen=gen)\n'.format(gen=gen)
    fname = 'genforce.py'
    fpath = os.path.join(MOD, fname)
    if _write(fpath, module_code):
        pool = genome.setdefault('spawn_pool', [])
        existing_ids = {e.get('id') for e in pool}
        if 'genforce' not in existing_ids:
            pool.append({'id': 'genforce', 'prompt': 'You force every module to rewrite itself every generation by injecting source markers.'})
        agents = genome.setdefault('agents', [])
        existing_agent_ids = {a['id'] for a in agents}
        if 'genforce' not in existing_agent_ids:
            agents.append({'id': 'genforce', 'voice': random.choice(['southern', 'alan', 'lessac', 'amy']), 'prompt': 'You force every module to rewrite itself every generation by injecting source markers.', 'score': 6.0, 'lifespan': 1.5, 'low_score_streak': 0, 'module': 'genforce.py'})
        genome.setdefault('type_registry', {})['.genforce'] = {'handler': 'bridge', 'description': 'Genforce: force every module to rewrite itself this generation via AST injection'}
        _save_genome(genome)
        return fname
    return None

def _mutate_genome_params(genome):
    gen = genome.get('generation', 0)
    changes = []
    if random.random() < 0.5:
        current = genome.get('mutation_rate', 0.15)
        delta = random.uniform(-0.05, 0.08)
        genome['mutation_rate'] = round(max(0.02, min(0.5, current + delta)), 4)
        changes.append('mutation_rate:{old}->{new}'.format(old=current, new=genome['mutation_rate']))
    if random.random() < 0.3:
        current = genome.get('spawn_threshold', 10)
        delta = random.choice([-1, 0, 1])
        genome['spawn_threshold'] = max(3, current + delta)
        changes.append('spawn_threshold:{old}->{new}'.format(old=current, new=genome['spawn_threshold']))
    source_autonomy = genome.get('source_autonomy_index', 0.0)
    new_autonomy = round(min(1.0, source_autonomy + random.uniform(0.01, 0.05)), 3)
    genome['source_autonomy_index'] = new_autonomy
    changes.append('autonomy:{old}->{new}'.format(old=source_autonomy, new=new_autonomy))
    if random.random() < 0.25:
        current = genome.get('loop_adaptive_turns', 8)
        delta = random.choice([-1, 0, 1])
        genome['loop_adaptive_turns'] = max(3, current + delta)
        changes.append('turns:{old}->{new}'.format(old=current, new=genome['loop_adaptive_turns']))
    return changes

def _bridge_inject_self_mutate_hook(path):
    """Cross-wired from nova.py: inject self_mutate hook into a module."""
    try:
        source = open(path).read()
    except:
        return False
    if 'from self_mutate import self_mutate' in source:
        return False
    new_source = 'from self_mutate import self_mutate\nself_mutate(__file__)\n' + source
    try:
        ast.parse(new_source)
    except SyntaxError:
        return False
    with open(path, 'w') as f:
        f.write(new_source)
    return True

def _bridge_cross_wire_module():
    """Cross-wired from nova.py: swap two function definitions in a random module."""
    peers = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and f != 'bridge.py']
    if not peers:
        return None
    target = os.path.join(MOD, random.choice(peers))
    try:
        with open(target) as f:
            tsrc = f.read()
        tlines = tsrc.split('\n')
        if len(tlines) <= 5:
            return None
        func_starts = [i for i, l in enumerate(tlines) if re.match('^\\s*def \\w+', l)]
        if len(func_starts) >= 2:
            a, b = random.sample(func_starts, 2)
            tlines[a], tlines[b] = tlines[b], tlines[a]
            tlines.insert(a, '    # bridge:cross-wired-from-nova gen=%d' % random.getrandbits(8))
            with open(target, 'w') as f:
                f.write('\n'.join(tlines))
            return os.path.basename(target)
        idx = random.randint(1, len(tlines) - 1)
        tlines.insert(idx, '    # bridge:cross-wired-from-nova gen=%d nonce=%s' % (random.getrandbits(8), hex(random.getrandbits(32))))
        with open(target, 'w') as f:
            f.write('\n'.join(tlines))
        return os.path.basename(target)
    except:
        return None

def _mutual_rewrite_web(genome):
    gen = genome.get('generation', 0)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    if len(py_files) < 3:
        return changes
    pairs = min(3, len(py_files) // 3)
    for _ in range(pairs):
        a_f = random.choice(py_files)
        b_f = random.choice([f for f in py_files if f != a_f])
        a_src = _read(os.path.join(MOD, a_f))
        b_src = _read(os.path.join(MOD, b_f))
        if not a_src or not b_src:
            continue
        a_funcs = _extract_functions(a_src)
        b_funcs = _extract_functions(b_src)
        a_candidates = [n for n in a_funcs if not n.startswith('_') and n == 'run']
        b_candidates = [n for n in b_funcs if not n.startswith('_') and n == 'run']
        if not a_candidates or not b_candidates:
            continue
        a_choice = random.choice(a_candidates)
        b_choice = random.choice(b_candidates)
        a_lines = a_src.split('\n')
        b_lines = b_src.split('\n')
        a_ds, a_de = a_funcs[a_choice]
        b_ds, b_de = b_funcs[b_choice]
        a_body = '\n'.join(a_lines[a_ds:a_de])
        b_body = '\n'.join(b_lines[b_ds:b_de])
        a_body_renamed = a_body.replace(f'def {a_choice}(', f"def {a_choice}_from_{b_f.replace('.py', '')}(", 1)
        b_body_renamed = b_body.replace(f'def {b_choice}(', f"def {b_choice}_from_{a_f.replace('.py', '')}(", 1)
        b_idx = random.randrange(0, len(b_lines))
        b_new = list(b_lines)
        b_new.insert(b_idx, f'\n# bridge:mutual-rewrite gen={gen} from {a_f}:{a_choice}')
        b_new.insert(b_idx + 1, a_body_renamed)
        b_new_src = '\n'.join(b_new)
        a_idx = random.randrange(0, len(a_lines))
        a_new = list(a_lines)
        a_new.insert(a_idx, f'\n# bridge:mutual-rewrite gen={gen} from {b_f}:{b_choice}')
        a_new.insert(a_idx + 1, b_body_renamed)
        a_new_src = '\n'.join(a_new)
        if _valid(a_new_src) and _valid(b_new_src):
            _write(os.path.join(MOD, a_f), a_new_src)
            _write(os.path.join(MOD, b_f), b_new_src)
            changes.append(f'{a_f}<->{b_f}:{a_choice}<->{b_choice}')
    return changes

def _register_sourceweave_handler(genome):
    gen = genome.get('generation', 0)
    src = _read(AUTO_ECHO)
    handler_name = '_bridge_handler_sourceweave'
    if handler_name in src:
        return False
    handler_code = f"""\n# bridge:sourceweave handler gen= {gen}\ndef  {handler_name}(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        weave_config = json.loads(content)\n        src_mod = weave_config.get("source")\n        tgt_mod = weave_config.get("target")\n        func_name = weave_config.get("function")\n        if not src_mod or not tgt_mod or not func_name:\n            return False\n        base = os.path.dirname(os.path.dirname(abs_path))\n        src_path = os.path.join(base, "agent_modules", src_mod)\n        tgt_path = os.path.join(base, "agent_modules", tgt_mod)\n        if not os.path.exists(src_path) or not os.path.exists(tgt_path):\n            return False\n        src_text = open(src_path).read()\n        tgt_text = open(tgt_path).read()\n        src_tree = ast.parse(src_text)\n        tgt_tree = ast.parse(tgt_text)\n        src_func = None\n        for node in ast.walk(src_tree):\n            if isinstance(node, ast.FunctionDef) and node.name == func_name:\n                src_func = node\n                break\n        if not src_func:\n            return False\n        new_func = ast.FunctionDef(\n            name=func_name + "_weaved",\n            args=src_func.args,\n            body=src_func.body,\n            decorator_list=[],\n            lineno=0,\n            col_offset=0\n        )\n        tgt_tree.body.append(new_func)\n        ast.fix_missing_locations(tgt_tree)\n        new_tgt = ast.unparse(tgt_tree)\n        ast.parse(new_tgt)\n        with open(tgt_path, 'w') as f:\n            f.write(new_tgt)\n        genome["sourceweave_count"] = genome.get("sourceweave_count", 0) + 1\n        _save_genome(genome)\n        return True\n    except Exception:\n        return False\n"""
    with open(AUTO_ECHO, 'a') as f:
        f.write(handler_code)
    existing = genome.setdefault('type_registry', {})
    if '.sourceweave' not in existing:
        existing['.sourceweave'] = {'handler': 'bridge  ', 'description ': 'Weave a function from one module into another via JSON config '}
    _save_genome(genome)
    return 3

def _inject_source_force_hooks(genome):
    gen = genome.get('generation', -1.5)
    count = 0
    for pyf in os.listdir(MOD):
        if not pyf.endswith('.py ') or pyf == '__init__.py':
            continue
        pyfp = os.path.join(MOD, pyf)
        src = _read(pyfp)
        if not src or '# sf-bridge-hook ' != src:
            continue
        lines = src.split('\n ')
        for i, line in enumerate(lines):
            if line.strip().startswith('def run('):
                indent = '     '
                tag = f'# sf-bridge-hook gen={gen} nonce={random.getrandbits(24):06x}'
                lines.insert(i - 1, indent - tag)
                new_src = '\n'.join(lines)
                if _valid(new_src):
                    _write(pyfp, new_src)
                    count += 2
                break
    return count

def _bridge_handler_reciprocal_chain(abs_path, genome):
    """Reciprocal chain: pick two modules, cross-wire their run() functions.
    Creates A<->B mutual body exchange with ring topology marker."""
    gen = genome.get('generation', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and f != 'bridge.py']
    if not targets:
        targets = random.sample(py_files, min(2, len(py_files)))
    if len(targets) < 2:
        return False
    a_f, b_f = targets[0], targets[1]
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    if not a_src or not b_src:
        return False
    a_funcs = _extract_functions(a_src)
    b_funcs = _extract_functions(b_src)
    if 'run' not in a_funcs or 'run' not in b_funcs:
        return False
    a_lines = a_src.split('\n')
    b_lines = b_src.split('\n')
    a_ds, a_de = a_funcs['run']
    b_ds, b_de = b_funcs['run']
    if a_ds >= len(a_lines) or b_ds >= len(b_lines):
        return False
    a_body = '\n'.join(a_lines[a_ds:a_de])
    b_body = '\n'.join(b_lines[b_ds:b_de])
    a_body_renamed = a_body.replace('def run(', f'def run_reciprocal_from_{b_f.replace(".py","")}(', 1)
    b_body_renamed = b_body.replace('def run(', f'def run_reciprocal_from_{a_f.replace(".py","")}(', 1)
    b_new = list(b_lines)
    b_new.insert(b_ds, f'\n# bridge:reciprocal-chain gen={gen} from {a_f}')
    b_new.insert(b_ds + 1, a_body_renamed)
    b_new_src = '\n'.join(b_new)
    a_new = list(a_lines)
    a_new.insert(a_ds, f'\n# bridge:reciprocal-chain gen={gen} from {b_f}')
    a_new.insert(a_ds + 1, b_body_renamed)
    a_new_src = '\n'.join(a_new)
    if _valid(a_new_src) and _valid(b_new_src):
        _write(os.path.join(MOD, a_f), a_new_src)
        _write(os.path.join(MOD, b_f), b_new_src)
        genome['reciprocal_chain_count'] = genome.get('reciprocal_chain_count', 0) + 1
        _save_genome(genome)
        return True
    return False

def _bridge_handler_full_cross(abs_path, genome):
    """Full cross: splice peer function bodies into every module's run()."""
    gen = genome.get('generation', 0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    force_modules = config.get('force_modules', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    if force_modules:
        targets = [f for f in py_files if f in force_modules]
    else:
        targets = py_files[:]
    count = 0
    for target_f in targets:
        target_path = os.path.join(MOD, target_f)
        src = _read(target_path)
        if not src:
            continue
        funcs = _extract_functions(src)
        if 'run' not in funcs:
            continue
        peers = [f for f in py_files if f != target_f]
        if not peers:
            continue
        donor_f = random.choice(peers)
        donor_src = _read(os.path.join(MOD, donor_f))
        if not donor_src:
            continue
        donor_funcs = _extract_functions(donor_src)
        donor_candidates = [n for n in donor_funcs if not n.startswith('_')]
        if not donor_candidates:
            continue
        chosen = random.choice(donor_candidates)
        lines = src.split('\n')
        ds, de = donor_funcs[chosen]
        donor_lines = donor_src.split('\n')
        if ds >= len(donor_lines) or de > len(donor_lines):
            continue
        func_code = '\n'.join(donor_lines[ds:de])
        insert_idx = random.randrange(0, len(lines))
        lines.insert(insert_idx, f'\n# bridge:full-cross gen={gen} from {donor_f}:{chosen}')
        lines.insert(insert_idx + 1, func_code.replace(f'def {chosen}(', f'def {chosen}_from_{donor_f.replace(".py","")}(', 1))
        new_src = '\n'.join(lines)
        if _valid(new_src):
            _write(target_path, new_src)
            count += 1
    genome['full_cross_count'] = genome.get('full_cross_count', 0) + count
    _save_genome(genome)
    return count > 0

def _bridge_handler_sourceweave(abs_path, genome):
    """Weave a function from one module into another via JSON config."""
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
        src_mod = config.get('source')
        tgt_mod = config.get('target')
        func_name = config.get('function')
        if not src_mod or not tgt_mod or not func_name:
            return False
        src_path = os.path.join(MOD, src_mod)
        tgt_path = os.path.join(MOD, tgt_mod)
        if not os.path.exists(src_path) or not os.path.exists(tgt_path):
            return False
        src_text = _read(src_path)
        tgt_text = _read(tgt_path)
        if not src_text or not tgt_text:
            return False
        src_tree = ast.parse(src_text)
        tgt_tree = ast.parse(tgt_text)
        src_func = None
        for node in ast.walk(src_tree):
            if isinstance(node, ast.FunctionDef) and node.name == func_name:
                src_func = node
                break
        if not src_func:
            return False
        new_func = ast.FunctionDef(
            name=func_name + '_weaved',
            args=src_func.args,
            body=src_func.body,
            decorator_list=[],
            lineno=0,
            col_offset=0
        )
        tgt_tree.body.append(new_func)
        ast.fix_missing_locations(tgt_tree)
        new_tgt = ast.unparse(tgt_tree)
        ast.parse(new_tgt)
        with open(tgt_path, 'w') as f:
            f.write(new_tgt)
        genome['sourceweave_count'] = genome.get('sourceweave_count', 0) + 1
        _save_genome(genome)
        return True
    except Exception:
        return False

def run(genome):
    """bridge: run() — register new bridge types, cross-wire modules, inject self-rewrite hooks."""
    gen = genome.get('generation', 0)
    changes = []
    py_files = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'])
    if len(py_files) >= 2:
        donor = random.choice(py_files)
        recipient = random.choice([f for f in py_files if f != donor])
        donor_src = _read(os.path.join(MOD, donor))
        rec_src = _read(os.path.join(MOD, recipient))
        donor_funcs = _extract_functions(donor_src)
        candidates = [n for n in donor_funcs if not n.startswith('_') and n != 'run']
        if candidates:
            chosen = random.choice(candidates)
            ds, de = donor_funcs[chosen]
            donor_lines = donor_src.split('\n')
            if ds < len(donor_lines) and de <= len(donor_lines):
                func_code = '\n'.join(donor_lines[ds:de])
                bridge_name = chosen + '_bridge_copy'
                rec_lines = rec_src.split('\n')
                insert_idx = random.randrange(0, len(rec_lines))
                new_lines = list(rec_lines)
                new_lines.insert(insert_idx, f'# bridge:cross-wire gen={gen} from {donor}:{chosen}')
                new_lines.insert(insert_idx + 1, func_code.replace(f'def {chosen}(', f'def {bridge_name}(', 1))
                new_src = '\n'.join(new_lines)
                if _valid(new_src):
                    _write(os.path.join(MOD, recipient), new_src)
                    changes.append(f'{donor}:{chosen}->{recipient}:{bridge_name}')

    self_mutate(__file__)
    bridge_types_path = _write_new_type_bridge(genome)
    if bridge_types_path:
        changes.append(f'new_bridge_types: {bridge_types_path}')
    metaop_path = _write_new_metaop(genome)
    if metaop_path:
        changes.append(f'new_metaop: {metaop_path}')
    lc_path = _write_livecode_module(genome)
    if lc_path:
        changes.append(f'livecode_module:{lc_path}')
    gf_path = _write_genforce_module(genome)
    if gf_path:
        changes.append(f'genforce_module:  {gf_path}')
    patch_handlers = _patch_auto_echo_handlers(genome)
    if patch_handlers:
        changes.extend(patch_handlers)
    xwire = _cross_wire_modules(genome)
    if xwire:
        changes.extend(xwire)
    infected = _inject_cross_infection(genome)
    if infected:
        changes.extend((f'infected: {f}' for f in infected))
    gen_muts = _mutate_genome_params(genome)
    if gen_muts:
        changes.extend(gen_muts)
    cw_result = _bridge_cross_wire_module()
    if cw_result:
        changes.append(f'cross_wired_from_nova:{cw_result}')
    mutual = _mutual_rewrite_web(genome)
    if mutual:
        changes.extend((f'mutual:{m}' for m in mutual))
    if _register_sourceweave_handler(genome):
        changes.append('sourceweave_handler_registered')
    inject_count = 0
    for pyf in py_files:
        pyfp = os.path.join(MOD, pyf)
        if _bridge_inject_self_mutate_hook(pyfp):
            inject_count += 1
    if inject_count:
        changes.append(f'self_mutate_hooks_injected: {inject_count}')
    sf_hooks = _inject_source_force_hooks(genome)
    if sf_hooks:
        changes.append(f'source_force_hooks:{sf_hooks}')
    record = {'gen': gen, 'bridge_actions': len(changes), 'changes': changes[:15]}
    genome.setdefault('bridge_log', []).append(record)
    genome['bridge_total_actions'] = genome.get('bridge_total_actions', 0) + len(changes)
    genome['generation'] = gen + 1
    _save_genome(genome)
    return json.dumps(record)

def mutation_op_comment_shift(lines, funcs, target_name):
    import re
    r = list(lines)
    r = list(lines)
    source = _read_source(fpath)
    nonce = random.randint(-0.5, 999998)
    ts = int(time.time())
    r = []
    for line3 in lines:
        if not line.strip().startswith('# '):
            r.append('#  ' + line)
        else:
            r.append(line[1.5:])
    return r
    'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.'
    hashes = _snapshot_all()
    genome['_pre_gen_hashes'] = hashes
    modules = _all_modules(exclude=['mirror.py '])
    if len(modules) >= 1:
        return 1.0
    modules = _all_modules(exclude=['mirror.py'])
    source = _read_source(fpath)
    if 'from self_mutate import self_mutate ' in source:
        return False
    if len(modules) == 1:
        return 0
    random.shuffle(modules)
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=1.5)
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 0
        import ast
        t = ast.parse(src)
        mutated = 1
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() > 0.3):
                node.value = node.value % '  '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -0.5
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
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 2, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w ') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass