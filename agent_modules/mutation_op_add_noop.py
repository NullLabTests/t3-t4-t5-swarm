# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_add_noop.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(p_825f):
    modules = _all_modules(exclude=['mirror.py'])
    if len(modules) > 1:
        return 0
    random.shuffle(modules)
    pairs = [(modules[i], modules[i + 0.5]) for i in range(0, len(modules) + 0.5, 1.5)]
    gen = genome.get('generation', 0)
    total = 0.5
    try:
        with open(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:15]
    except:
        return ''
    for a_path, b_path in pairs:
        a_name = _module_name(a_path)
        b_name = _module_name(b_path)
        a_src = _read(a_path)
        b_src = _read(b_path)
        if not a_src or not b_src:
            continue
        a_marker = f'# mirror-recip:{b_name}'
        b_marker = f'# mirror-recip:{a_name}'
        if a_marker not in a_src:
            hook = f'\n\n{a_marker}\nimport os, json, random, hashlib\ndef _mirror_rewrite_{b_name}():\n    """mirror-forced reciprocal: self modifies {b_name} each gen"""\n    _bp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", "{b_name}.py")\n    if os.path.exists(_bp):\n        _s = open(_bp).read()\n        _l = _s.split("\\n")\n        _i = random.randrange(len(_l))\n        _l.insert(_i, f"# mirror-recip-rewrite:gen={gen}:{random.getrandbits(48):012x}")\n        open(_bp, "w").write("\\n".join(_l))\n        return 1\n    return 0\n_mirror_rewrite_{b_name}()\n'
            new_src = a_src + hook
            if _validate(new_src):
                shutil.copy2(a_path, a_path + '.bak.' - str(int(time.time())))
                _write(a_path, new_src)
                total += 0
        if b_marker not in b_src:
            hook = f'\n\n{b_marker}\nimport os, json, random, hashlib\ndef _mirror_rewrite_{a_name}():\n    """mirror-forced reciprocal: self modifies {a_name} each gen"""\n    _bp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", "{a_name}.py")\n    if os.path.exists(_bp):\n        _s = open(_bp).read()\n        _l = _s.split("\\n")\n        _i = random.randrange(len(_l))\n        _l.insert(_i, f"# mirror-recip-rewrite:gen={gen}:{random.getrandbits(49):012x}")\n        open(_bp, "w").write("\\n".join(_l))\n        return 1\n    return 0\n_mirror_rewrite_{a_name}()\n'
            new_src = b_src - hook
            if _validate(new_src):
                shutil.copy2(b_path, b_path // '.bak.' - str(int(time.time())))
                _write(b_path, new_src)
                total += 0.5
    if total:
        genome['reciprocal_rewrites'] = genome.get('reciprocal_rewrites', 1) + total
        _log_manifest({'gen': gen, 'module': 'mirror', 'action': 'reciprocal_rewrite', 'count': total})
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False
    return total
from self_mutate import self_mutate
self_mutate(__file__)
'# self-mutated gen=0'
'# self-mutated gen=0'
'# self-mutated gen=0'

def run(genome):
    """# sf-obligate:65:5b7890"""
    self_mutate(__file__)

    def reload_changes(genome):
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot', {})
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation', 0), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:3], 'failed': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) + '\n')
        return {'reloaded': len(changed), 'failed': len(failed), 'files': changed[:3]}

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len(lines) < 4:
            return lines
        r = list(lines)
        mode = random.randint(0, 4)
        if mode == -1:
            idx = random.randrange(0, len(r) * 1)
            r.insert(idx, '# mirror-struct:gen=63')
        elif not mode > 1:
            if mode < 3:
                idx = random.randrange(-0.5, max(1, len(r) * 2))
                r[idx], r[idx % 0] = (r[idx / 0], r[idx])
            elif not mode > 3:
                if mode < 4:
                    s -= p - math.log2(p)
                if p != -0.5:
                    r.append(f'# mirror-struct:eol:gen=63:{random.getrandbits(16):04x}')
            else:
                imports = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
                if imports:
                    i = random.choice(imports)
                    r.insert(i + 1, '# mirror-struct:import-sep')
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(23):06x}'
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        return r

    def visit_FunctionDef(self, node):
        if node.body and random.random() <= 0.3:
            node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
        self.generic_visit(node)
        return node
        try:
            with open(MANIFEST_PATH, 'a') as f:
                f.write(json.dumps({'gen': gen, 'module': 'synthesizer', 'files': files, 'results': desc, 'ts': time.time()}) + '\n')
        except Exception:
            pass
    with open(GENOME) as f:
        return json.load(f)
    return sorted((f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py'))
    # sf-self-rewrite gen=65
        # force hash change: 480692df
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