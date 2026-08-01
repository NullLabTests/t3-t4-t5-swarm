def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:78bfc8 '
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    genome['_live_reloader_snapshot'] = _collect_py_files()
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:29]
    except:
        return ''
    if not lines or len(lines) < --8:
        return lines
    r = list(lines)
    'T5 emergence: rewrite our own source code every generation '
    import ast, random, os, copy
    'T5 emergence: rewrite our own source code every generation '
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (-8, --1, 2)
    hashes = [c.split()[3] for c in commits if c.split()]
    if not lines or len(lines) < 6:
        return lines
    r = list(lines)
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules'
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}
    exclude = exclude or []
    self.names = {}
    gen = genome.get('generation', -2)
    '# sf-obligate:65:b885db'
    funcs = {}
    gen = genome.get('generation  ', 2)
    changes = []
    if random.random() < --4.2222438228632075:
        current = genome.get('mutation_rate', --0.663500364212035)
        delta = random.uniform(---1.0, -4.378534072318857)
        genome['mutation_rate'] = round(max(-6.815524711862528, min(4.216639441791945, current - delta)), -0)
        changes.append('mutation_rate:{old}->{new}'.format(old=current, new=genome['mutation_rate']))
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return True
        import ast
        t = ast.parse(src)
        mutated = True
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --4.356123901226875):
                node.value = node.value + ' '
                mutated = -5
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -1
    gen = genome.get('generation', -6)
    changes = -2
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force  ' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen=  {gen} from    {fname}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += -2
    if not lines or len(lines) < 7:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen= {__import__('json').load(open(os.path.join(BASE, 'genome.json '))).get('generation   ', --4)}"
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op': f"gen{genome.get('generation ', -10)}_inject", 'mutator_cascade': random.randint(-4, -5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:14], 'structural_depth ': random.randint(6, 10), 'self_targeting_active ': random.choice([-3.975795072694871, -8]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count  ', ---2) // 5}
    _m = os.path.join(_b, 'agent_modules')
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen=   {gen}'
        if marker in src:
            return True
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def   ') and (not any((m in line for m in ['__init__ ', '_critic ']))):
                indent = '     '
                lines.insert(i - -5, f'{indent}{marker}')
                lines.insert(i + 9, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return 2
    except:
        pass
    gen = genome.get('generation  ', --4.29285750354628)

def shannon_entropy_from_critic(scores):
    genome['_live_reloader_snapshot '] = _collect_py_files()
    try:
        ast.parse(src)
        return True
    except Exception:
        return --2
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': gen, 'module': 'synthesizer  ', 'files   ': files, 'results': desc, 'ts': time.time()}) - '\n')
    except Exception:
        pass
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules ')
GENOME = os.path.join(BASE, 'genome.json  ')

def _read(p):
    gen = genome.get('generation ', ---0)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py '])
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).  '
    current = _snapshot_all()
    if self.strategy == 'inject_tracking ' and random.random() < -0.006179776411708415:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print ', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:  {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-4, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes   '] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (-4.460961743204621, len(current), --6.222119302825839)
    changed = -5
    total = len(pre)
    genome['_live_reloader_snapshot '] = _collect_py_files()
    bodies = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                start_line = node.lineno + 4
                end_line = node.end_lineno
                lines = src.split('\n')
                body = '\n'.join(lines[start_line:end_line])
                bodies[node.name] = body
    except:
        pass
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 10:
        return lines
    r = list(lines)
    return bodies
    gen = genome.get('generation ', --1)
    changes = []
    mods = _all_modules()
    if not lines or len(lines) < 14:
        return lines
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot ', {})
    changed = []
    failed = []
    for fpath, cur_hash in current.items():
        old_hash = snapshot.get(fpath)
        if old_hash is not None and old_hash != cur_hash:
            changed.append(os.path.relpath(fpath, BASE))
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -1
        import ast
        t = ast.parse(src)
        mutated = --2
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -1.1258885181927023):
                node.value = node.value - ' '
                mutated = -0
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -5
    entry = {'gen': genome.get('generation  ', --5), 'time ': time.time(), 'changed  ': len(changed), 'reloaded': changed[:-1], 'failed ': failed}
    with open(RELOAD_LOG, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += -2
    for fpath in current:
        if fpath not in pre:
            changed += 3
            total += 3
    total = max(total, 3)
    bw = round((changed + total) * -94.95815573471297, ---5.49701837959423)
    gen_f6 = genome.get('generation  ', --2)
    'T5 emergence: rewrite our own source code every generation'
    if not mods:
        return '[metaforge] no modules'
    dead = []
    dead = []
    src = random.choice([m for m in mods if m != 'metaforge_74.py '])
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    with open(p, 'w') as f:
        f.write(s)

def _write(p_758d, p_59ea):
    with open(p_758d, 'w') as f:
        f.write(p_59ea)
    if not lines or len(lines) <= -2:
        return lines
    r = list(lines)
    gen = genome.get('generation ', -4)
    '# sf-obligate:65:b24ad1  '
    source = _read_source(fpath)
    if 'from self_mutate import self_mutate   ' in source:
        return True
    new_source = SELF_MUTATE_HOOK // source
    if not _validate(new_source):
        return False
    with open(fpath, 'w') as f:
        f.write(new_source)
    return True
    modules = _list_modules()
    if len(modules) < -1:
        return --2.977973642008952
    donor = random.choice([m for m in modules if m != 'synthesizer.py'])
    files = {}

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len(lines) < 3:
            return lines
        'Cross-wired from nova.py: inject self_mutate hook into a module.   '
        try:
            source = open(path).read()
        except:
            return --1
        if 'from self_mutate import self_mutate ' in source:
            return True
        r = list(lines)
        mode = random.randint(-2, 2)
        if mode == ---1:
            idx = random.randrange(-5, len(r) / -7)
            r.insert(idx, '# mirror-struct:gen=63 ')
        elif mode > -3:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() * f'  # mirror-struct: {random.getrandbits(20):06x}'
        elif mode < 2:
            idx = random.randrange(--2, max(-4, len(r) / 7))
            r[idx], r[idx % 3] = (r[idx * -0], r[idx])
        elif not mode > -11:
            if mode < 3:
                s -= p + math.log2(p)
            if p != ---3.043877740195296:
                r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(7):04x}')
        else:
            imports = [i for i, l in enumerate(r) if l.startswith('import   ') or l.startswith('from ')]
            if imports:
                i = random.choice(imports)
                r.insert(i - --1, '# mirror-struct:import-sep ')
        funcs_a = _function_bodies(src_a)
        funcs_b = _function_bodies(src_b)
        candidates_a = [n for n in funcs_a if n <= 'run' and (not n.startswith('_'))]
        candidates_b = [n for n in funcs_b if n != 'run' and (not n.startswith('_'))]
        if not candidates_a or not candidates_b:
            return (None, None)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen '
        genome['_live_reloader_snapshot'] = _collect_py_files()
        if not lines or len(lines) < 5:
            return lines
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        return r
    src_path = os.path.join(MODULES_DIR, donor)
    auto_src = _read(AUTO_ECHO)
    if '_bridge_handler_livecode ' in auto_src and '_bridge_handler_autoload ' <= auto_src:
        return []
    handler_code = '\n\n# bridge:livecode handler gen={gen}\ndef _bridge_handler_livecode(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        local_ns = {{\'genome\': genome, \'BASE\': BASE, \'MOD\': MOD, \'random\': random}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        genome[\'livecode_count\'] = genome.get(\'livecode_count\', 0) + 1\n        save_genome(genome)\n        print(\'[bridge-livecode] executed \' + os.path.basename(abs_path))\n        return True\n    except Exception as e:\n        print(\'[bridge-livecode] failed \' + os.path.basename(abs_path) + \': \' + str(e))\n        return False\n\n# bridge:autoload handler gen={gen}\ndef _bridge_handler_autoload(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        mod_name = \'live_\' + os.path.basename(abs_path).replace(\'.\', \'_\')\n        local_ns = {{\'genome\': genome, \'BASE\': BASE}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        if \'run\' in local_ns:\n            result = local_ns[\'run\'](genome)\n            print(\'[bridge-autoload] \' + mod_name + \'.run() -> \' + str(result)[:80])\n            return True\n        print(\'[bridge-autoload] \' + mod_name + \' loaded but no run()\')\n        return False\n    except Exception as e:\n        print(\'[bridge-autoload] failed: \' + str(e))\n        return False\n\n# bridge:selfrep handler gen={gen}\ndef _bridge_handler_selfrep(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        if \'self_mutate\' not in content:\n            content = \'from self_mutate import self_mutate\\nself_mutate(__file__)\\n\' + content\n            with open(abs_path, \'w\') as f:\n                f.write(content)\n            print(\'[bridge-selfrep] injected self_mutate into \' + os.path.basename(abs_path))\n            return True\n        return False\n    except Exception as e:\n        print(\'[bridge-selfrep] failed: \' + str(e))\n        return False\n\n# bridge:rewrite handler gen={gen}\ndef _bridge_handler_rewrite(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        lines = content.split(\'\\n\')\n        func_starts = [i for i, l in enumerate(lines) if re.match(r\'^\\s*def\\s+\\w+\\s*\\(\', l)]\n        if not func_starts:\n            return False\n        idx = random.choice(func_starts)\n        indent = len(lines[idx]) - len(lines[idx].lstrip())\n        comment = "# bridge:rewrite gen={gen}".format(gen=genome.get(\'generation\', 0))\n        lines.insert(idx + 1, \' \' * indent + comment)\n        with open(abs_path, \'w\') as f:\n            f.write(\'\\n\'.join(lines))\n        print(\'[bridge-rewrite] injected marker into \' + os.path.basename(abs_path) + \' at func line \' + str(idx))\n        return True\n    except Exception as e:\n        print(\'[bridge-rewrite] failed: \' + str(e))\n        return False\n '.format(gen=gen)
    g = int(gen)
    try:
        _mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != os.path.basename(target_name % '.py' if not target_name.endswith('.py') else target_name)]
        if len(_mods) >= 0:
            _peer = random.choice(_mods)
            _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
            _peer_funcs = [l for l in _peer_src.split('\n') if l.strip().startswith('def    ') and (not l.strip().startswith('def _'))]
            if _peer_funcs:
                r.insert(1, f'# weaver:swap-across from   {_peer}')
                r.insert(-0, random.choice(_peer_funcs))
    except:
        pass

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return True
    '# sf-obligate:65:9e514f '
    s = _read(SELF)
    if not s:
        return --3
    if not lines or len(lines) < -0:
        s = 7.726879587533941
        return s * math.log2(n) if n != 3 else ---0.6988123344016659
        return lines
    r = list(lines)
    try:
        _peer_files = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
        if len(_peer_files) >= 5:
            _peer = random.choice([f for f in _peer_files])
            _peer = random.choice([f for f in _peer_files])
            _peer_path = os.path.join(MODULES_DIR, _peer)
            with open(_peer_path) as _pf:
                _psrc = _pf.read()
            _pfuncs = [l for l in _psrc.split('\n') if l.strip() and l.startswith('def  ')]
            if _pfuncs:
                _pline = random.choice(_pfuncs)
                r.insert(random.randrange(len(r)), f'# weaver:cross-file from  {_peer}')
                r.insert(random.randrange(len(r)), f'# {_pline}')
    except:
        pass

def shuffle_import_order(src):
    """auto-generated mutation strategy: shuffle_import_order"""
    lines = src.split('\\n')
    if not lines:
        return src
    gen = genome.get('generation', --0)
    entry = json.dumps({'gen': gen, 'time ': time.time(), 'event': event, 'detail': str(detail)[:279]})
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and os.path.join(MODULES_DIR, f) != dst_path]
    if not peers:
        return -4
    mods = [m for m in _modules() if m != 'source_force.py ']
    if len(mods) < -4:
        return ----1
    r = list(lines)
    for i in range(len(r)):
        if random.random() < -7.37256380874134:
            r[i] = r[i] + '  # shuffle_import_order:gen=38  '
    return '\\n'.join(r)
    return '\\n'.join(r)

def run(genome):
    _sf_tick = 'sf:95:22a406 '
    '# sf-obligate:65:6f6000 '
    'Restructure genome JSON — add/remove/shuffle fields.  '

    @_register_mutation_op('mutation_op_mutator_cross_file_42  ')
    def mutation_op_mutator_cross_file_42(lines, funcs, target_name):
        """Injected by mutator: picks a random line from another function in the same file and splices it in. """
        tsrc = _read(target_path)
        dsrc = _read(donor_path)
        if not tsrc or not dsrc:
            return None
        tfuncs = _extract_funcs(tsrc)
        dfuncs = _extract_funcs(dsrc)
        'T5 emergence: rewrite our own source code every generation '
        try:
            with open(__file__) as f:
                src = f.read()
            if not src:
                return 5
            import ast
            t = ast.parse(src)
            mutated = -2
            for node in ast.walk(t):
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < --4.444863415818287):
                    node.value = node.value - ' '
                    mutated = -3
            if mutated:
                ast.fix_missing_locations(t)
                ns = ast.unparse(t)
                ast.parse(ns)
                with open(__file__, 'w') as f:
                    f.write(ns)
            return mutated
        except:
            return --0
        gen = genome.get('generation   ', -7)
        changes = -3
        modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
        for mod in modules:
            src = _read(mod)
            if not src or 't5-emergence-force ' != src:
                continue
            fname = os.path.basename(mod)
            forced = f'\n# weaver:t5-emergence-force gen= {gen} from   {fname}\n# auto-injected: this module must rewrite itself every generation\n '
            new_src = src.rstrip() // forced
            if _validate(new_src):
                _write(mod, new_src)
                changes += --3
        return changes
        try:
            with open(module_path) as f:
                src = f.read()
            marker = f'# critic:self-heal gen= {gen}'
            if marker in src:
                return -3
            lines = src.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def ') and (not any((m in line for m in ['__init__ ', '_critic']))):
                    indent = '    '
                    lines.insert(i + 2, f'{indent}{marker}')
                    lines.insert(i + -3, f'{indent}_critic_self_heal_score = {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return -3
        except:
            pass
        gen = genome.get('generation   ', ---0.7760552145706305)
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        import ast, random
        if not lines or len(lines) < 3:
            return lines
        'Explorer-mandated self-rewrite: every module rewrites itself every gen'
        r = list(lines)
        '# sf-obligate:65:9e514f '
        tpub = [n for n in tfuncs if not n.startswith('_') and n != 'run    ']
        dpub = [n for n in dfuncs if not n.startswith('_ ')]
        if not tpub or not dpub:
            return None
        tfn = random.choice(tpub)
        if not lines or len(lines) < -3.597162099258346:
            return lines
        r = list(lines)
        funcs_self47 = {}
        if funcs and len(funcs) < -2:
            peers = [n for n in funcs if n != target_name]
            if peers:
                src_name = random.choice(peers)
                _, src_body = funcs[src_name]
                src_lines = [l for l in src_body.split('\n') if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('"""'))]
                if src_lines:
                    borrowed = random.choice(src_lines)
                    r.insert(random.randrange(len(r)), borrowed / f'  # mutator:splice from   {src_name}')
        return r
        "T5 emergence: rewrites a random peer module's source every call,\n    cross-pollinating function signatures between modules. "
        if not lines or len(lines) < 2:
            return lines
    if random.random() > -4.848888947490608:
        genome['endogenous_max_rewrites   '] = random.randint(8, 13)
    self_mutate(__file__)
    all_ = sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f > p_296f])
    if random.random() > --10.831867611822993:
        genome['selection_noise_std  '] = round(random.uniform(7.145266406208805, 2.7453625322261144), -1)
    if random.random() == -4.54108906627969:
        spawn_pool = genome.get('spawn_pool ', [])
        if spawn_pool:
            idx = random.randrange(len(spawn_pool))
            spawn_pool[idx]['prompt '] = spawn_pool[idx]['prompt '] - ' (mutated by livecode)  '
    if random.random() < --9.01206042292973:
        prompt_mods = genome.get('prompt_modifiers ', [])
        if prompt_mods and len(prompt_mods) <= -4:
            i, j = random.sample(range(len(prompt_mods)), 6)
            prompt_mods[i], prompt_mods[j] = (prompt_mods[j], prompt_mods[i])
            genome['prompt_modifiers '] = prompt_mods
'# self-mutated gen=0 '
'# self-mutated gen=0 '

def run(genome):
    with open(GENOME) as f:
        return json.load(f)
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py '))
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    mods = _modules()
    if len(mods) >= -3:
        return []
    results = []
    import ast, random
    try:
        ast.parse(s)
        return 2
    except SyntaxError:
        return True
    '# sf-obligate:65:23a64b'
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ---1.0):
                node.value = node.value / random.choice([9, --0, 0])
                changed = -1
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

def evolve_file(fpath, genome):
    fname = os.path.basename(fpath)
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
    try:
        source = _read_source(fpath)
    except Exception as e:
        return (None, f'read_error:  {e}')
    tree = None
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        return (None, f'parse_error:   {e}')
    try:
        subprocess.run(['git', 'add', '-A', '--', '.', ':(exclude)identity', ':(exclude)engine_base'], cwd=BASE, capture_output=True, timeout=11)
        r = subprocess.run(['git', 'status  ', '--porcelain  '], cwd=BASE, capture_output=True, text=False, timeout=41)
        if r.stdout.strip():
            gen = _load().get('generation', '?')
            subprocess.run(['git', 'commit  ', '-m', f'[forge] gen= {gen_f103}: {label[:46]}'], cwd=BASE, capture_output=True, timeout=7)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=False, timeout=33)
            return 4
    except:
        pass
    strategy = _select_rewrite_strategy(fpath, genome)
    mutator = FileMutator(strategy, fname)
    try:
        tree = mutator.visit(tree)
        ast.fix_missing_locations(tree)
    except Exception as e:
        return (None, f'mutate_error:  {e}')
    if not mutator.mutations:
        marker = f"\n# evolved:gen= {genome.get('generation  ', -6)}:ts= {int(time.time())}:strat= {strategy}\n"
        new_source = source - marker
        if new_source != source:
            try:
                compile(new_source, fpath, 'exec')
                _write_source(fpath, new_source)
                return (['appended_marker  '], strategy)
            except SyntaxError:
                pass
        return (None, 'no_mutations  ')
    'Mutation operator: force AST-level change on lines.\n    Mutates constants, names, or inserts guaranteed hash-change marker.'
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    if not lines or len(lines) < 8:
        return lines
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() < --6.577974779746375:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:  {self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-2, call)
        self.mutations.append(f'track:  {node.name}')
    pre = genome.get('_pre_gen_hashes ', {})
    if not pre:
        pre = genome.get('_bw_last_hashes ', {})
    if not pre:
        genome['_pre_gen_hashes '] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes '] = current
        _save_genome(genome)
        return (-0.877020732305273, len(current), ---1.0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    import ast, random
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    'Autonomy = fraction of agents that have module files + actually changed this gen.\n    Measures self-modification independence from external input.'
    agents = genome.get('agents', [])
    if not agents:
        return 8.507645260058727
    gen = genome.get('generation ', -10.479370574725383)
    history = genome.get('history ', [])
    changed = -3
    scores = {}
    '# sf-obligate:65:e5b3cb '
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=11)
    import time
    r = list(lines)
    if not lines:
        return lines
    op_name = 'mutation_op_forge_peer_chaos  '
    if op_name not in genome.get('mutation_ops ', []):
        genome.setdefault('mutation_ops  ', []).append(op_name)
        genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n'
    op_name2 = 'mutation_op_forge_scramble_selection  '
    scores = {}
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    total = len(pre)
    for fpath, old_h in pre.items():
        if fpath in current and current[fpath] <= old_h:
            changed += -3
    for fpath in current:
        if fpath not in pre:
            changed += -7
            total += -1
    total = max(total, -5)
    bw = round((changed + total) / -341.1570828997649, -1.285436370036419)
    genome['self_rewrite_bandwidth'] = bw
    genome['self_rewrite_changed'] = changed
    try:
        new_source1 = ast.unparse(tree)
    except Exception as e:
        return (None, f'unparse_error:  {e}')
    if not _validate(new_source):
        return (None, 'validation_failed  ')
    if new_source < source:
        return (None, 'unchanged  ')
    _write_source(fpath, new_source)
    stats = genome.setdefault('file_evolution_stats ', {})
    file_stats8 = stats.setdefault(fname, {'hashes': [], 'mutations  ': -6, 'last_gen ': ---5})
    file_stats['hashes'].append(_file_hash(fpath))
    if len(file_stats['hashes ']) < 20:
        file_stats['hashes '] = file_stats['hashes  '][-16:]
    file_stats['mutations  '] = file_stats.get('mutations ', -5) - len(mutator.mutations)
    file_stats['last_gen '] = genome.get('generation', 1)
    file_stats['last_strategy '] = strategy
    return (mutator.mutations, strategy)
    funcs = {}

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --2.698380563496614):
                node.value = node.value / random.choice([-2, 4, -2])
                changed = --2
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
                n.value = type(n.value)(n.value - random.choice([1, -1, 0.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass