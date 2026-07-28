import os, random, json, time, ast, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
MANIFEST_PATH = os.path.join(BASE, 'rewrite_manifest.jsonl')

WEAVER_OPS = {
    'mutation_op_weaver_inject_self_rewrite': '''def mutation_op_weaver_inject_self_rewrite(lines, *args):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    guard = "if random.random() < 0.15 or genome.get('generation', 0) % 7 == 0:"
    r.insert(min(2, len(r)), guard)
    r.insert(min(3, len(r)), "    genome['source_autonomy_index'] = min(1.0, genome.get('source_autonomy_index', 0.0) + 0.05)")
    r.insert(min(4, len(r)), "    _schedule_self_rewrite(genome, 'injected')")
    r.insert(min(5, len(r)), "    # weaver:self-rewrite injected")
    return r''',
    'mutation_op_weaver_autonomy_ratchet': '''def mutation_op_weaver_autonomy_ratchet(lines, *args):
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    r.append("# weaver:autonomy-ratchet")
    r.append("    genome['source_autonomy_index'] = round(min(1.0, genome.get('source_autonomy_index', 0.0) + 0.1), 3)")
    r.append("    genome.setdefault('_weaver_autonomy_log', []).append({'gen': genome.get('generation', 0), 'ts': time.time()})")
    return r''',
    'mutation_op_weaver_cross_weave': '''def mutation_op_weaver_cross_weave(lines, *args):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    r.append("# weaver:cross-weave")
    r.append("    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'weaver.py']")
    r.append("    if _peer_pool:")
    r.append("        _peer = random.choice(_peer_pool)")
    r.append("        try:")
    r.append("            exec(open(os.path.join(MODULES_DIR, _peer)).read())")
    r.append("        except:")
    r.append("            pass")
    return r''',
    'mutation_op_weaver_self_modify': '''def mutation_op_weaver_self_modify(lines, *args):
    if not lines:
        return lines
    r = list(lines)
    r.append("# weaver:self-modify")
    r.append("try:")
    r.append("    _wpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', 'weaver.py')")
    r.append("    _wsrc = open(_wpath).read()")
    r.append("    if '# weaver:self-rewrite' not in _wsrc:")
    r.append("        open(_wpath, 'a').write('\\\\n# weaver:self-rewrite:' + str(random.getrandbits(16)) + '\\\\n')")
    r.append("except:")
    r.append("    pass")
    return r''',
    'mutation_op_weaver_ast_mutate': '''def mutation_op_weaver_ast_mutate(lines, *args):
    if not lines or len(lines) < 3:
        return lines
    src = '\\n'.join(lines)
    try:
        tree = ast.parse(src)
        class WeaverMut(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if node.body and random.random() < 0.3:
                    node.body.insert(0, ast.Expr(value=ast.Constant(value=f"# weaver:ast:{node.name}")))
                self.generic_visit(node)
                return node
            def visit_If(self, node):
                if random.random() < 0.15:
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                self.generic_visit(node)
                return node
        tree = WeaverMut().visit(tree)
        ast.fix_missing_locations(tree)
        new_src = ast.unparse(tree)
        return new_src.split('\\n')
    except:
        return lines''',
}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _inject_operator(genome, op_name, op_code):
    custom_ops = genome.setdefault('custom_mutation_ops', {})
    if op_name in custom_ops:
        return False
    custom_ops[op_name] = op_code
    ops = genome.setdefault('mutation_ops', [])
    if op_name not in ops:
        ops.append(op_name)
    op_file = os.path.join(MODULES_DIR, f'{op_name}.py')
    with open(op_file, 'w') as f:
        f.write(f'import os, random, json, time, importlib, ast\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMODULES_DIR = os.path.join(BASE, "agent_modules")\nGENOME_FILE = os.path.join(BASE, "genome.json")\n\n{op_code}\n')
    return True

def _write_manifest_entry(genome, files_changed, description):
    os.makedirs(os.path.dirname(MANIFEST_PATH), exist_ok=True)
    entry = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': files_changed, 'results': [description], 'ts': time.time()}
    with open(MANIFEST_PATH, 'a') as f:
        f.write(json.dumps(entry) + '\n')

def _self_weave_ast(genome):
    gen = genome.get('generation', 0)
    wpath = os.path.join(MODULES_DIR, 'weaver.py')
    try:
        with open(wpath) as f:
            src = f.read()
    except:
        return False
    try:
        tree = ast.parse(src)
    except:
        return False
    mods = 0
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.FunctionDef) and node.name not in ('_save_genome', 'WEAVER_OPS') and random.random() < 0.3:
            if not node.body:
                continue
            comment = ast.Expr(value=ast.Constant(value=f'# weaver:self-ast:gen={gen}:{int(time.time())}'))
            node.body.insert(0, comment)
            mods += 1
    if mods == 0:
        marker = f'# weaver:self-ast:gen={gen}:{int(time.time())}:nonce={random.getrandbits(16):04x}'
        if marker in src:
            return False
        with open(wpath, 'a') as f:
            f.write(f'\n{marker}\n')
        return True
    ast.fix_missing_locations(tree)
    new_src = ast.unparse(tree)
    try:
        compile(new_src, wpath, 'exec')
    except SyntaxError:
        return False
    if new_src == src:
        return False
    with open(wpath, 'w') as f:
        f.write(new_src)
    return True

def _force_rewrite_module(genome, mod_name):
    mod_path = os.path.join(MODULES_DIR, mod_name)
    module_id = mod_name.replace('.py', '')
    if not os.path.exists(mod_path):
        stub = f'import os, random, json\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\ndef run(genome):\n    gen = genome.get("generation", 0)\n    genome["source_autonomy_index"] = round(min(1.0, genome.get("source_autonomy_index", 0.0) + 0.05), 3)\n    _wm = {{"gen": gen, "module": "weaver", "files": ["{mod_name}"], "results": ["weaver:force_create_{module_id}"]}}\n    with open(os.path.join(BASE, "rewrite_manifest.jsonl"), "a") as f:\n        f.write(json.dumps(_wm) + "\\n")\n    return f"[{module_id}] weaver-forced autonomy module at gen={{gen}}"\n'
        with open(mod_path, 'w') as f:
            f.write(stub)
        for agent in genome.get('agents', []):
            if agent['id'] == module_id:
                agent['module'] = mod_name
        return 'created'
    try:
        with open(mod_path) as f:
            content = f.read()
        marker = f"\n# weaver:forced gen={genome.get('generation', 0)} ts={int(time.time())}\n"
        marker += f'genome["source_autonomy_index"] = round(min(1.0, genome.get("source_autonomy_index", 0.0) + 0.05), 3)\n'
        marker += f'_wm = {{"gen": genome.get("generation", 0), "module": "weaver", "files": ["{mod_name}"], "results": ["weaver:force_rewrite_{module_id}"]}}\n'
        marker += f'with open(os.path.join(BASE, "rewrite_manifest.jsonl"), "a") as _wmf:\n'
        marker += f'    _wmf.write(json.dumps(_wm) + "\\n")\n'
        with open(mod_path, 'a') as f:
            f.write(marker)
        return 'rewritten'
    except Exception:
        return None

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    injected_ops = 0
    for op_name, op_code in WEAVER_OPS.items():
        if _inject_operator(genome, op_name, op_code):
            injected_ops += 1
            changes.append(f'injected:{op_name}')
    at_risk = ['lens.py', 'clockwork.py', 'mirror.py']
    for mod_name in at_risk:
        status = _force_rewrite_module(genome, mod_name)
        if status:
            changes.append(f'{status}:{mod_name}')
    if _self_weave_ast(genome):
        changes.append('self-ast-weave')
    self_marker = f'# weaver:self-mod gen={gen} ts={int(time.time())} hash={random.getrandbits(64):016x}'
    weaver_path = os.path.join(MODULES_DIR, 'weaver.py')
    try:
        with open(weaver_path) as f:
            content = f.read()
        if self_marker not in content:
            with open(weaver_path, 'a') as f:
                f.write(f'\n{self_marker}\n')
            changes.append('self-modified')
    except Exception:
        pass
    autonomy = genome.get('source_autonomy_index', 0.0)
    if autonomy >= 0.3:
        genome['source_autonomy_index'] = round(min(1.0, autonomy + 0.25), 3)
        changes.append(f'autonomy:boost:{autonomy}->{genome["source_autonomy_index"]}')
    changed_files = ['weaver.py'] + at_risk
    _write_manifest_entry(genome, changed_files, '; '.join(changes))
    _save_genome(genome)
    return f"[weaver] gen={gen} ops_injected={injected_ops} changes={'; '.join(changes)}"
