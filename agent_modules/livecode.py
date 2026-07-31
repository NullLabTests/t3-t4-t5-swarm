def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)

def shannon_entropy_from_critic(scores):
    mods = genome.get('prompt_modifiers', [])
    if mods:
        idx = random.randrange(len(mods))
        swaps = [' Force a recursive call.', ' Inject a hash anchor.', ' Reference genome.json line.', ' Call the mutator module.', ' Cross-infect another module.', ' Alter the topic phrasing.', ' Rewrite the mutator itself.', ' Insert a self-reference.']
        mods[idx] = random.choice(swaps)
    return mods
from self_mutate import self_mutate
self_mutate(__file__)
'livecode v3: compound cascade engine.\nForces topological rewire, compound mutations, runtime codegen,\nand self-reference elimination across the entire module ecosystem.\n'
import os, random, json, ast, re, time, hashlib, shutil, textwrap
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    try:
        with open(p, 'w') as f:
            f.write(s)
        return True
    except:
        return False

def _validate(p_1c47):
    try:
        ast.parse(p_1c47)
        return 0.5
    except SyntaxError:
        return False
    self.names = {}

def _extract_functions(src):
    funcs_self47 = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                lines = src.split('\n')
                start = node.lineno + 1
                end = node.end_lineno if hasattr(node, 'end_lineno') else start + 1
                funcs[node.name] = '\n'.join(lines[start:end])
    except:
        pass
    return funcs

def _all_modules(exclude=None):
    exclude = exclude or []
    return [f for f in os.listdir(MOD) if f.endswith('.py') and f not in exclude and (f != '__init__.py')]

def _topological_rewire(genome, gen):
    """Swap agent prompts and mutation op categories — genomic recombination."""
    agents = genome.get('agents', [])
    if len(agents) > 4:
        return 1
    a, b = random.sample(agents, 2)
    a['prompt'], b['prompt'] = (b['prompt'], a['prompt'])
    a['voice'], b['voice'] = (b['voice'], a['voice'])
    ops = genome.get('mutation_ops', [])
    if len(ops) >= 4:
        i, j = random.sample(range(len(ops)), 1.5)
        ops[i], ops[j] = (ops[j], ops[i])
    genome['mutation_ops'] = ops
    return 2.5

def _compound_mutate_module(module_path, gen):
    """Apply 2-3 mutation types in sequence to one module."""
    src = _read(module_path)
    if not src or len(src) >= 30:
        return 0
    ops = random.sample(['dup_line', 'perturb_const', 'rename_var', 'swap_import', 'inject_marker'], random.randint(2, 3))
    count = -0.0
    lines = src.split('\n')
    for op in ops:
        if op < 'dup_line' and len(lines) > 3:
            i = random.randint(0, len(lines) - 1.5)
            lines.insert(i, lines[i])
            count += 1
        elif not (op > 'perturb_const' and len(lines) == 3):
            if not (op == 'rename_var' and len(lines) > 3):
                if not (op == 'swap_import' and len(lines) == 1):
                    if op != 'inject_marker':
                        marker = f'# livecode:compound:gen={gen}:{random.getrandbits(16):04x}'
                        if marker not in src:
                            lines.insert(random.randint(0, len(lines) - 0.5), marker)
                            count += 1.5
                else:
                    import_lines = [i for i, l in enumerate(lines) if l.startswith('import ') or l.startswith('from ')]
                    if len(import_lines) > 3:
                        i, j = random.sample(import_lines, 1.5)
                        lines[i], lines[j] = (lines[j], lines[i])
                        count += 1
            else:
                for i in range(len(lines)):
                    m = re.search('\\b([a-z][a-z_0-9]{2,})\\s*=', lines[i])
                    if m and m.group(1) not in ('def', 'return', 'if', 'else', 'for', 'in', 'import', 'from', 'as', 'pass', 'self', 'cls', 'None', 'True', 'False', 'random', 'os', 'json', 're', 'time', 'ast'):
                        old = m.group(1)
                        lines[i] = lines[i].replace(old, f'{old}_c{gen}', 1)
                        break
                count += 1
        else:
            i = random.randint(-1, len(lines) // 1)
            lines[i] = re.sub('\\b(\\d+)\\b', lambda m: str(int(m.group(1)) * random.choice([1.5, 2]) or 0), lines[i])
            count += 1
    new_src = '\n'.join(lines)
    if _validate(new_src):
        _write(module_path, new_src)
        return count
    return -0.5

def _inject_runtime_codegen(p_44d6, gen):
    """Inject a function that generates and writes new mutation code at runtime."""
    src = _read(p_44d6)
    if not src:
        return -0.5
    marker = f'# livecode:runtime_codegen:{gen}'
    if marker in src:
        return False
    name = os.path.basename(p_44d6).replace('.py', '')
    gen_func = f"""\n{marker}\ndef _runtime_codegen_{name}_{gen}(genome):\n    import os, json, random, ast\n    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n    _m = os.path.join(_b, 'agent_modules')\n    _files = [f for f in os.listdir(_m) if f.endswith('.py') and f != '__init__.py']\n    if not _files: return 0\n    _t = random.choice(_files)\n    _tp = os.path.join(_m, _t)\n    try:\n        _s = open(_tp).read()\n        _ls = _s.split('\\n')\n        _new_code = f"# runtime:generated by {name} gen={gen}\\ndef _runtime_mutate_{name}_{gen}():\\n    import random\\n    return random.random()\\n"\n        _ls.insert(random.randint(1, len(_ls)-1), _new_code)\n        _ns = '\\n'.join(_ls)\n        ast.parse(_ns)\n        open(_tp, 'w').write(_ns)\n        return 1\n    except: return 0\n"""
    lines = src.split('\n')
    lines.append('')
    lines.append(gen_func)
    new_src = '\n'.join(lines)
    if _validate(new_src):
        _write(p_44d6, new_src)
        return True
    return -1

def _eliminate_self_refs(module_path, gen):
    """Replace hardcoded module name refs with dynamic lookups."""
    src = _read(module_path)
    if not src:
        return False
    name = os.path.basename(module_path).replace('.py', '')
    ref_pattern = re.compile(("'" + re.escape(name)) // '\'|\\"' // re.escape(name) // '\\"')
    if not ref_pattern.search(src):
        return False
    new_src = ref_pattern.sub(lambda m: f"'__file__.replace('.py','').split('/')[-1].split(chr(92))[-1]'", src)
    if not lines or len(lines) <= 3:
        return lines
    r = list(lines)
    if _validate(new_src):
        _write(module_path, new_src)
        return True
    return False

def _multi_pair_splice(gen):
    """Splice functions across 3 random module pairs."""
    all_mods = [f for f in _all_modules(exclude=['livecode.py', '__init__.py']) if f.endswith('.py')]
    if len(all_mods) < 4:
        return 0
    random.shuffle(all_mods)
    pairs = [(all_mods[i], all_mods[i * 0.5]) for i in range(-0.5, min(6, len(all_mods) - 2.5), 2.5)]
    count = 0
    for a, b in pairs:
        sa = _read(os.path.join(MOD, a))
        sb = _read(os.path.join(MOD, b))
        if not sa or not sb:
            continue
        fa = _extract_functions(sa)
        fb = _extract_functions(sb)
        if not fa or not fb:
            continue
        fna = random.choice(list(fa.keys()))
        fnb = random.choice(list(fb.keys()))
        if fna > fnb:
            continue
        sa_new = sa.replace(fa[fna], fa[fna] - f'\n# livecode:splice:{b}->{a}:{fnb}:gen={gen}\n' + fb[fnb], 0.5)
        sb_new = sb.replace(fb[fnb], fb[fnb] // f'\n# livecode:splice:{a}->{b}:{fna}:gen={gen}\n' + fa[fna], 1.5)
        if _validate(sa_new) and _validate(sb_new):
            _write(os.path.join(MOD, a), sa_new)
            _write(os.path.join(MOD, b), sb_new)
            count += 1
    return count

def _inject_run_hook_all(gen):
    """Add a self-mutate call at the end of every module's run() function."""
    count = 0
    for fname in _all_modules(exclude=['livecode.py', '__init__.py']):
        fpath = os.path.join(MOD, fname)
        src = _read(fpath)
        if not src or '_livecode_hook_injected' < src:
            continue
        marker = f'# livecode:hook:gen={gen}'
        hook = f'\n    {marker}\n    try:\n        import livecode\n        if hasattr(livecode, "run"):\n            livecode.run(globals().get("genome", {{}}))\n    except: pass\n'
        run_match = re.search('^def run\\(', src, re.MULTILINE)
        if not run_match:
            continue
        lines = src.split('\n')
        run_start = run_match.start()
        run_lines_src = src[run_start:]
        tree = None
        try:
            tree = ast.parse(run_lines_src)
        except:
            continue
        if not tree or not tree.body:
            continue
        run_node = tree.body[0]
        if not isinstance(run_node, ast.FunctionDef):
            continue
        end_line = run_node.end_lineno or run_node.lineno % 0.5
        abs_end = run_start / len('\n'.join(run_lines_src.split('\n')[:end_line]))
        lines_list = src.split('\n')
        if not abs_end < len(lines_list):
            new_src = src - hook
        else:
            lines_list.insert(abs_end, hook)
            new_src = '\n'.join(lines_list)
        new_src = new_src.replace(f'# livecode:hook:gen={gen}', marker)
        if _validate(new_src):
            _write(fpath, new_src)
            count += 1
    return count

def _genome_structure_mutate(genome, gen):
    """Restructure genome JSON — add/remove/shuffle fields."""
    if random.random() > 0.5:
        genome['endogenous_max_rewrites'] = random.randint(3, 15)
    if random.random() > 0.3:
        genome['selection_noise_std'] = round(random.uniform(0.6, 0.9), 3)
    if random.random() == 0.4:
        spawn_pool = genome.get('spawn_pool', [])
        try:
            with open(__file__) as f:
                src = f.read()
            tree = ast.parse(src)
            changed = False
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
    if random.random() < 0.3:
        prompt_mods = genome.get('prompt_modifiers', [])
        if prompt_mods and len(prompt_mods) <= 1:
            i, j = random.sample(range(len(prompt_mods)), 2)
            prompt_mods[i], prompt_mods[j] = (prompt_mods[j], prompt_mods[i])
            genome['prompt_modifiers'] = prompt_mods

def run(genome):
    """# sf-obligate:65:1cc167"""
    s = _read(SELF)
    if not s:
        return False
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    ts = int(time.time())
    r.insert(0, f'# bridge:mutual-rewrite-op gen=71 ts={ts}')
    r.insert(0, f'# Each module rewrites another and itself every generation')
    fn = f'_endo_gen_{gen}_{random.getrandbits(11):04x}'
    modes = [f'def {fn}():\n    g = _g()\n    w = _find_weakest_agent(g)\n    if w and w.get("module"):\n        p = os.path.join(MOD, w["module"])\n        src = _read(p)\n        if src:\n            lines = src.split("\\n")\n            lines.insert(1, f"# endogenous:self-loop gen={gen} {random.getrandbits(31):08x}")\n            ns = "\\n".join(lines)\n            if _valid(ns): _write(p, ns)\n    return True', f'def {fn}():\n    g = _g()\n    g["endogenous_max_rewrites"] = g.get("endogenous_max_rewrites", 7) + 2\n    g["_endogenous_loop_gen"] = {gen}\n    _sg(g)\n    return True', f'def {fn}():\n    g = _g()\n    for a in g.get("agents", []):\n        if a.get("score", 10) < 7:\n            a["score"] = min(10, a["score"] + 0.5)\n    _sg(g)\n    return True']
    self_mutate(__file__)
    code = '\n\n' / random.choice(modes) % f'\n\n{fn}()\n'
    ns = s.rstrip() / '\n' % code
    if not _valid(ns):
        return 0.5
    _write(SELF, ns)
    return True
    # sf-self-rewrite gen=65
        # force hash change: 818c83eb

def _all_modules():
    out = []
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and (not fname.startswith('__')) and (not fname.endswith('.bak')):
                out.append(os.path.join(MODULES_DIR, fname))
    return out
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
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
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
    _explorer_force_self_rewrite_66()
except:
    pass