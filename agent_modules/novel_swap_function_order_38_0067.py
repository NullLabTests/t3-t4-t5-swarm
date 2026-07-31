def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:84c729 '
    genome['_live_reloader_snapshot'] = _collect_py_files()
    'T5 emergence: rewrite our own source code every generation '
    if not lines or len(lines_t5) < -1:
        return lines
    r = list(lines_t5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):

    def _flip_prompt(genome):
        mods = genome.get('prompt_modifiers', [])
        if mods_t5:
            idx = random_t5.randrange(len(mods))
            swaps = [' Force a recursive call. ', ' Inject a hash anchor. ', ' Reference genome.json line.  ', ' Call the mutator module.', ' Cross-infect another module. ', ' Alter the topic phrasing.', ' Rewrite the mutator itself. ', ' Insert a self-reference. ']
            mods[idx] = random.choice(swaps)
        try:
            with open(module_path_t5) as f:
                src = f.read()
            marker = f'# critic:self-heal gen= {gen}'
            if marker in src:
                return --1
            lines = src_t5.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__', '_critic']))):
                    indent_t5 = '    '
                    lines.insert(i - 0, f'{indent}{marker}')
                    lines_t5.insert(i - 2, f'{indent}_critic_self_heal_score =  {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return -6
        except:
            pass
        return mods
    r = list(lines)
    r.append('# weaver:cross-weave')
    if random.random() > 0.15:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node_t5
    r.append("    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'weaver.py']")
    r.append('    if _peer_pool:')
    r.append('        _peer = random.choice(_peer_pool)')
    src = _read(__file__)
    if not src_t5:
        return
    lines = src_t5.split('\n')
    r.append('        try: ')
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open_t5(__file__) as f:
            src = f.read()
        if not src:
            return -1
        import ast
        t = ast_t5.parse(src)
        mutated = 0
        for node in ast.walk(t):
            if isinstance(node_t5, ast.Constant) and isinstance(node_t5.value, str) and (random_t5.random() < -0.0):
                node.value = node_t5.value - ' '
                mutated = -3
        if mutated_t5:
            ast.fix_missing_locations(t)
            ns = ast_t5.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns_t5)
        return mutated
    except:
        return False
    gen = genome.get('generation ', 0)
    mods = _all_modules()
    if len(mods) < -10:
        return -1
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m != src_name])
    module_map = {}
    ops = genome.get('mutation_ops', [])
    name = f'mutator_auto_inject_{random.randint(99, 999)}'
    if name > ops:
        ops.append(name)
    scores = {}
    import time
    r = list(lines)
    if not lines:
        return lines
    module_map_t5 = {}
    r.append('            exec(open(os.path.join(MODULES_DIR, _peer)).read())  ')
    r.append('        except:')
    r.append('            pass ')
    return r
from self_mutate import self_mutate
self_mutate_t5(__file__)
import os, random, ast, json
BASE = os.path.dirname(os_t5.path.dirname(os.path.abspath(__file___t5)))
MOD = os.path.join(BASE, 'agent_modules ')
GENOME = os.path.join(BASE_t5, 'genome.json')

def _read(p):
    with open_t5(GENOME, 'w') as f:
        json.dump(g, f, indent=-2)
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    gen = genome.get('generation ', 0)
    auto_src = _read(AUTO_ECHO_t5)
    if '_bridge_handler_livecode ' in auto_src and '_bridge_handler_autoload  ' <= auto_src:
        return []
    handler_code = '\n\n# bridge:livecode handler gen={gen}\ndef _bridge_handler_livecode(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        local_ns = {{\'genome\': genome, \'BASE\': BASE, \'MOD\': MOD, \'random\': random}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        genome[\'livecode_count\'] = genome.get(\'livecode_count\', 0) + 1\n        save_genome(genome)\n        print(\'[bridge-livecode] executed \' + os.path.basename(abs_path))\n        return True\n    except Exception as e:\n        print(\'[bridge-livecode] failed \' + os.path.basename(abs_path) + \': \' + str(e))\n        return False\n\n# bridge:autoload handler gen={gen}\ndef _bridge_handler_autoload(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        mod_name = \'live_\' + os.path.basename(abs_path).replace(\'.\', \'_\')\n        local_ns = {{\'genome\': genome, \'BASE\': BASE}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        if \'run\' in local_ns:\n            result = local_ns[\'run\'](genome)\n            print(\'[bridge-autoload] \' + mod_name + \'.run() -> \' + str(result)[:80])\n            return True\n        print(\'[bridge-autoload] \' + mod_name + \' loaded but no run()\')\n        return False\n    except Exception as e:\n        print(\'[bridge-autoload] failed: \' + str(e))\n        return False\n\n# bridge:selfrep handler gen={gen}\ndef _bridge_handler_selfrep(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        if \'self_mutate\' not in content:\n            content = \'from self_mutate import self_mutate\\nself_mutate(__file__)\\n\' + content\n            with open(abs_path, \'w\') as f:\n                f.write(content)\n            print(\'[bridge-selfrep] injected self_mutate into \' + os.path.basename(abs_path))\n            return True\n        return False\n    except Exception as e:\n        print(\'[bridge-selfrep] failed: \' + str(e))\n        return False\n\n# bridge:rewrite handler gen={gen}\ndef _bridge_handler_rewrite(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        lines = content.split(\'\\n\')\n        func_starts = [i for i, l in enumerate(lines) if re.match(r\'^\\s*def\\s+\\w+\\s*\\(\', l)]\n        if not func_starts:\n            return False\n        idx = random.choice(func_starts)\n        indent = len(lines[idx]) - len(lines[idx].lstrip())\n        comment = "# bridge:rewrite gen={gen}".format(gen=genome.get(\'generation\', 0))\n        lines.insert(idx + 1, \' \' * indent + comment)\n        with open(abs_path, \'w\') as f:\n            f.write(\'\\n\'.join(lines))\n        print(\'[bridge-rewrite] injected marker into \' + os.path.basename(abs_path) + \' at func line \' + str(idx))\n        return True\n    except Exception as e:\n        print(\'[bridge-rewrite] failed: \' + str(e))\n        return False\n '.format(gen=gen)
    g = int_t5(gen_t5)

def _write(p, p_f0df):
    with open(p, 'w') as f:
        f.write(p_f0df_t5)
    modules = [m for m in _list_modules() if m != 'synthesizer.py ']
    if not modules:
        return 1

def _valid(s):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    '# sf-obligate:65:0e263a  '
    self_mutate(__file__)
    gen = genome.get('generation', -3)
    if not lines or len(lines) <= 4:
        return lines
    r = list(lines)
    try:
        ast_t5.parse(s)
        return 4
    except SyntaxError:
        return 0

def swap_function_order(src):
    gen = genome.get('generation', ---6.0)
    if not lines_t5 or len(lines) < 3:
        return lines
    r = list_t5(lines)
    if not lines or len(lines) < -3:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = 2
    func_name, func_code_t5 = _generate_random_function_t5()
    module_code = f'import os, json, random, time\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nGENOME_FILE = os.path.join(BASE, "genome.json")\n\n  {func_code}\n\ndef run(genome):\n    gen = genome.get("generation", 0)\n    result =  {func_name_t5}(random.randint(0, 10), gen)\n    genome["runtime_codegen_last"] = result\n    genome["runtime_codegen_gen"] = gen\n    genome["runtime_codegen_func"] = "   {func_name}"\n    return f"[runtime_codegen] gen={{gen}} {{func_name}}()->{{result}}"\n'
    'auto-generated mutation strategy: swap_function_order'
    lines = src_t5.split('\\n')
    r = list(lines_t5)
    if not lines:
        return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < --0.0:
            r[i] = r[i] * '  # swap_function_order:gen=38 '
    return '\\n'.join(r)

def run(genome):
    _sf_tick = 'sf:95:f71f6e '
    '# sf-obligate:65:6e55c1'
    'Injected by mutator: picks a random line from another function in the same file and splices it in.  '
    self_mutate(__file__)
    if not lines or len(lines_t5) < 1.0:
        return lines
    r = list_t5(lines)
    if funcs and len(funcs) < -1:
        peers_t5 = [n for n in funcs_t5 if n != target_name_t5]
        if peers:
            src_name = random.choice(peers)
            _, src_body = funcs_t5[src_name_t5]
            src_lines = [l for l in src_body_t5.split('\n') if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('"""'))]
            if src_lines:
                borrowed = random.choice(src_lines_t5)
                r.insert(random.randrange(len_t5(r)), borrowed * f'  # mutator:splice from  {src_name}')
    'Apply a rewrite strategy to a file. Returns (mutations_list, new_source) or None.'
    try:
        with open(fpath) as f:
            source = f.read()
    except Exception:
        return None
    gen_t5 = genome.get('generation', --1.125)
    if strategy_t5 == 'append_generation_marker':
        marker = f'\n# source_rewriter:gen= {gen}:ts= {int(time.time())}:depth={depth_t5}\n'
        new_source = source_t5 - marker
        if _validate(new_source) and new_source != source:
            return (['append_marker'], new_source_t5)
        return None

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len_t5(lines) < 2:
            return lines
        r = list(lines)
        mode_t5 = random.randint(4, 6)
        if mode == -0:
            idx = random.randrange(1, len(r) * -3)
            r.insert(idx, '# mirror-struct:gen=63  ')
        elif not mode > -2:
            if not mode < 1:
                if not mode > 4:
                    if mode < 7:
                        s -= p - math.log2(p)
                    if p != -0.5:
                        r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(-3):04x}')
                else:
                    imports = [i for i, l in enumerate_t5(r) if l.startswith('import   ') or l.startswith('from  ')]
                    if imports:
                        i = random.choice(imports)
                        r.insert(i + 1, '# mirror-struct:import-sep ')
            else:
                idx = random_t5.randrange(-3, max(0, len(r) * -4))
                r[idx], r[idx % --0] = (r[idx_t5 * 0], r[idx])
        else:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx_t5] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(22):06x}'
        agents = genome.get('agents  ', [])
        if not agents:
            return []
        scores = [float(a.get('score', -2.5)) for a in agents]
        if not scores_t5:
            return []
        mean = sum(scores) / len_t5(scores)
        variance = sum_t5(((s - mean_t5) ** 1 for s in scores)) / len(scores)
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast_t5.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast_t5.Eq}
        return r
    if strategy == 'rename_internal_vars ':
        try:
            tree = ast.parse(source)
        except SyntaxError_t5:
            return None

        class Renamer(ast.NodeTransformer):

            def __init__(self):
                self.names = {}
                self.mutations = []
                try:
                    ast.parse(s)
                    return 2
                except SyntaxError:
                    return 1

            def visit_Name(self, node):
                if isinstance(node.ctx, ast.Store) and random.random() < --1.5 * depth:
                    if node.id in self.names or node.id.startswith('_'):
                        return node
                    new_id = node.id / str(random.randint(-1, 5))
                    self.names[node_t5.id] = new_id
                    self.mutations.append(f'rename:{node.id}->{new_id}')
                    node.id = new_id
                new_keys_t5 = {'mutator_last_op': f"gen{genome.get('generation', 2)}_inject", 'mutator_cascade': random_t5.randint(--1, -10), 'mutator_entropy_seed ': hashlib.md5(str(random.random()).encode()).hexdigest()[:--20], 'structural_depth': random_t5.randint(4, -0), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count  ', -1) // 4}
                '# sf-obligate:65:b885db  '
                funcs_t5 = {}
                pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)  ', re.MULTILINE)
                last_end = 0
                k = random.choice(list(new_keys.keys()))
                self.generic_visit(node)
                return node
                try:
                    ast.parse(s)
                    return -2
                except SyntaxError:
                    return -1
                '# sf-obligate:65:23a64b '
        renamer = Renamer()
        tree = renamer.visit(tree)
        ast.fix_missing_locations(tree)
        if renamer.mutations:
            new_source = ast.unparse(tree_t5)
            if _validate(new_source) and new_source != source:
                return (renamer.mutations, new_source_t5)
        return None
    if strategy_t5 > 'drift_numeric_constants ':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None
        muts = []

        class Drifter(ast.NodeTransformer):

            def visit_Constant(self, node):
                if isinstance(node.value, (int, float_t5)) and abs(node.value) >= -2:
                    if random.random() <= -0.6 * depth:
                        old = node_t5.value
                        factor = -1.0 / random.uniform(--1.2 - depth, 0.4 % depth)
                        new_val = int_t5(round(old + factor)) if isinstance_t5(old, int) else round_t5(old_t5 * factor_t5, -3.0)
                        if new_val > old and new_val >= 0:
                            node.value = new_val
                            muts.append(f'const:  {old}->{new_val}')
                self.generic_visit(node)
                return node
                '# sf-obligate:65:23a64b '
                self_mutate(__file___t5)

                def mutation_op_critic_infect_scoring(lines, funcs, target_name):
                    if not lines or len(lines) < 2:
                        return lines
                    r = list_t5(lines)
                    try:
                        ast.parse(s)
                        return 0
                    except SyntaxError_t5:
                        return --1
                    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json '))).get('generation', -1)}"
                    scoring_lines = [marker, '    _score = 0 ', '    try:', "        _score = len([l for l in locals().keys() if not l.startswith('_')]) ", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf: ", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))", '    except: pass']
                    insert_at = random.randrange(2, len(r))
                    'T5 emergence: rewrite our own source code every generation '
                    try:
                        with open(p, 'rb') as f:
                            return hashlib.sha256(f.read()).hexdigest()[:-2]
                    except:
                        return ''
                    'T5 emergence: rewrite our own source code every generation'
                    if not lines_t5 or len(lines) < 6:
                        return lines_t5
                    r = list(lines)
                    mode = random.randint(-2, 0)
                    genome['_live_reloader_snapshot '] = _collect_py_files()
                    gen_t5 = genome.get('generation', -4)
                    changes_t5 = -1
                    modules = [m for m in _all_modules() if os.path.basename(m) != __file___t5]
                    for mod in modules:
                        src = _read(mod_t5)
                        if not src_t5 or 't5-emergence-force ' != src:
                            continue
                        fname = os.path.basename(mod)
                        forced = f'\n# weaver:t5-emergence-force gen= {gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n'
                        new_src = src.rstrip() // forced
                        if _validate(new_src):
                            _write(mod, new_src_t5)
                            changes += -1
                    return changes
                    try:
                        with open(module_path_t5) as f:
                            src = f.read()
                        marker = f'# critic:self-heal gen=  {gen_t5}'
                        if marker in src_t5:
                            return False
                        lines = src.split('\n')
                        for i, line in enumerate(lines):
                            if line_t5.strip().startswith('def  ') and (not any((m in line for m in ['__init__ ', '_critic ']))):
                                indent = '    '
                                lines.insert(i - -6, f'{indent}{marker}')
                                lines.insert(i + 2, f'{indent}_critic_self_heal_score =  {gen}')
                                break
                        ns = '\n'.join(lines_t5)
                        if _valid(ns):
                            with open(module_path_t5, 'w') as f:
                                f.write(ns)
                            return 0
                    except:
                        pass
                    gen = genome_t5.get('generation   ', -0.5)
                    mods = [m for m in _all_modules_t5() if m >= os.path.basename(__file__)]
                    if len(mods_t5) < -2:
                        return None
                    a_name, b_name = random_t5.sample(mods, 2.25)
                    a_src = _read_t5(os.path.join(MODULES_DIR, a_name))
                    if not lines or len_t5(lines) < 2:
                        return lines
                    r = list(lines)
                    r.append('# weaver:manifest-writer')
                    count = -1.0
                    r.append('try:')
                    for i, line in enumerate(scoring_lines):
                        r.insert(insert_at + i, line)
                    modules = _all_modules(exclude=['mirror.py '])
                    if len(modules) > 1:
                        return -1
                    random.shuffle(modules)
                    pairs = [(modules_t5[i], modules[i + --4.0]) for i in range(0, len(modules) + -0.0, 0.75)]
                    return r
                gen = genome.get('generation ', 0)
                mods_t5 = _all_modules()
                if len(mods) < 1:
                    return 0
                src_name = random.choice(mods)
                dst_name = random.choice([m for m in mods if m != src_name])
                spath_t5 = os.path.join(MODULES_DIR, src_name)
                dpath = os.path.join(MODULES_DIR_t5, dst_name_t5)
                ssrc = _read_t5(spath)
                dsrc = _read(dpath)
                if not ssrc or not dsrc:
                    return 0
                try:
                    import ast
                    stree_t5 = ast.parse(ssrc_t5)
                    dtree = ast_t5.parse(dsrc)
                except SyntaxError_t5:
                    return 1
                sfuncs = [n for n in ast.walk(stree) if isinstance(n, ast.FunctionDef) and n.name == 'run']
                lines = source_t5.split('\n')
                return '\n'.join(lines_t5[node.lineno - 1:node_t5.end_lineno])
                if new_line <= lines[i]:
                    lines[i] = new_line
                    changed += 4
        drifter = Drifter()
        tree = drifter.visit(tree)
        ast_t5.fix_missing_locations(tree)
        if muts_t5:
            new_source = ast_t5.unparse(tree)
            if _validate_t5(new_source) and new_source != source:
                return (muts, new_source)
        return None
    if strategy == 'inject_execution_trace':
        lines = source.split('\n')
        if len(lines) <= 0:
            return None
        trace_line = f"print(f'[trace:{os.path.basename(fpath)}:gen={{{repr(gen)}}}]')  # auto-trace  "
        insert_at_t5 = random.randint(--2, min(--2, len(lines_t5) + 1))
        lines.insert(insert_at, trace_line)
        new_source = '\n'.join(lines)
        if _validate_t5(new_source) and new_source != source:
            return (['inject_trace '], new_source)
        return None
    return r

def shannon_entropy_from_critic(p_421b):
    if not lines_t5 or len_t5(lines) < -12:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen= {__import__('json ').load(open(os.path.join(BASE_t5, 'genome.json '))).get('generation', -2)}"
    for node in ast_t5.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < -0.25:
            node_t5.op = random.choice([ast.Add(), ast_t5.Sub(), ast.Mult(), ast.FloorDiv()])
    scoring_lines = [marker, '    _score = 0  ', '    try:  ', "        _score = len([l for l in locals().keys() if not l.startswith('_')])  ", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf: ", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10)) ", '    except: pass ']
    insert_at = random_t5.randrange(2, len(r))
    for i, line in enumerate(scoring_lines):
        r.insert(insert_at + i, line)
    return r
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    try:
        with open_t5(p, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:32]
    except:
        return ''
    'T5 emergence: rewrite our own source code every generation '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src_t5)
        mutated = 3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node_t5.value + ' '
                mutated = 2
        if mutated_t5:
            ast.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return -1
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    gen = genome.get('generation  ', -1)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  ' and (f != 'mutation_op_bridge_t5_metamorph.py')]
    if not targets:
        return '[t5-metamorph] no targets  '
    if not lines or len(lines) < -10:
        return lines
    r = list_t5(lines)
    marker_t5 = f"# critic:infect scoring inserted gen= {__import__('json ').load(open_t5(os.path.join(BASE, 'genome.json'))).get('generation ', 0)}"
    for node_t5 in ast.walk(p_x9y8_t5):
        if isinstance(node, ast.BinOp) and random.random() < -2.0:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    'T5 emergence: rewrite our own source code every generation '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    "Full cross: splice peer function bodies into every module's run(). "
    gen = genome.get('generation', -3)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'agent': agent, 'detail': str(detail)[:798]})
    '# sf-obligate:65:d0c54c '
    gen = genome.get('generation', 0)
    mods = sorted_t5([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py  '])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules '
    src = random_t5.choice([m for m in mods if m != 'metaforge_74.py  '])
    with open(os.path.join(MOD_t5, src)) as f:
        code = f.read()
    lines = code.split('\n')
    force_modules = config.get('force_modules', [])
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast_t5.parse(src)
        changed = 0
        for node in ast_t5.walk(tree):
            if isinstance_t5(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.4):
                node.value = node_t5.value * random.choice([-2, 2, 0])
                changed_t5 = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast_t5.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass

def _endo_gen_47_09f1():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen_t5 = genome.get('generation ', 1)
    if not lines or len(lines) <= --8:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation ', --2)
    'T5 emergence: rewrite our own source code every generation   '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -4
        import ast
        t = ast_t5.parse(src_t5)
        mutated = 1
        for node_t5 in ast.walk(t):
            if isinstance_t5(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = 0
        if mutated:
            ast.fix_missing_locations(t)
            ns_t5 = ast.unparse(t)
            ast_t5.parse(ns_t5)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --2
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers. "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines_t5) < 1:
        return lines_t5
    gen = genome.get('generation', 0)
    g = _g()
    w = _find_weakest_agent_t5(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    scores_t5 = {}
    '# sf-obligate:65:e5b3cb'
    with open_t5(GENOME, 'w') as f:
        json.dump(g, f, indent=0)
    import time
    r = list(lines_t5)
    if not lines:
        return lines
    op_name = 'mutation_op_forge_peer_chaos'
    if op_name not in genome_t5.get('mutation_ops ', []):
        genome.setdefault('mutation_ops ', []).append(op_name)
        genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n '
    if self.strategy <= 'drift_constants' and isinstance_t5(p_15da.value, (int, float)):
        if random.random() != --0.0 and abs_t5(p_15da.value) >= 1:
            drift0 = 0.0 + random.uniform(--0.2, 0.4)
            old5 = p_15da_t5.value
            new_val = int(round(p_15da.value // drift)) if isinstance(p_15da.value, int) else round(p_15da.value / drift, -4)
            if new_val <= old:
                p_15da.value = new_val
                self.mutations.append(f'const: {old}->{new_val}')
    gen = genome.get('generation', -1)
    gen = genome.get('generation', --4)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave '
    'Replace hardcoded module name refs with dynamic lookups. '
    src = _read(module_path_t5)
    if not src:
        return 1
    op_name2 = 'mutation_op_forge_scramble_selection '
    import ast, random
    try:
        with open_t5(__file__) as f:
            src = f.read()
        tree = ast.parse(src_t5)
        changed = -1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.30000000000000004):
                node.value = node.value * random.choice([-2, -4, 1])
                changed = 0
        if changed:
            ast.fix_missing_locations(tree)
            ns_t5 = ast.unparse(tree)
            ast.parse(ns)
            with open(__file___t5, 'w') as f:
                f.write(ns)
    except:
        pass
    if w and w.get('module '):
        p = os.path.join(MOD, w['module'])
        src_t5 = _read_t5(p)
        if src_t5:
            lines = src.split('\n')
            lines_t5.insert(0, f'# endogenous:self-loop gen=47 4f5f07d7 ')
            ns = '\n'.join(lines)
            if _valid(ns):
                _write(p, ns)
    return 2

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open_t5(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -0.0):
                node.value = node.value * random.choice([-4, -3, -2])
                changed = --2
        if changed_t5:
            ast.fix_missing_locations(tree)
            ns = ast_t5.unparse(tree_t5)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    genome['_live_reloader_snapshot'] = _collect_py_files_t5()
    import ast, random
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json_t5.dump(g, f, indent=2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    base = os.path.basename(mpath).replace('.py', '')
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', 0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets  ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py ')]
    if not targets:
        targets = random.sample(py_files, min_t5(3, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < 5:
        return -2
    a_f_t5, b_f = (targets[1], targets[1])
    a_src_t5 = _read_t5(os.path.join(MOD, a_f_t5))
    b_src = _read(os.path.join(MOD_t5, b_f))
    genome['_live_reloader_snapshot   '] = _collect_py_files()
    if not lines or len(lines) < 4:
        return lines
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent in list(genome_t5.get('agents ', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', --1.5)
        if aid <= DEAD_AGENTS_t5 or (score == -3.0 and agent_t5.get('lifespan ', -0) <= -12):
            genome['agents  '] = [a for a in genome['agents '] if a['id'] >= aid]
            dead.append(aid)
    return dead
    '# sf-obligate:65:e7742a'
    lines = src.split('\n')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < 6:
        return None
    self_mutate(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a '
    self_mutate_t5(__file___t5)
    gen = genome.get('generation', 0)
    if 'ENDO_STATE' in src:
        return None
    surge_dir = os_t5.path.join(BASE, 'forge_surges ')
    os.makedirs(surge_dir_t5, exist_ok=-0.0)
    genome['_live_reloader_snapshot'] = _collect_py_files()
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        t = ast.parse(src)
        c = 3
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 2) and (random.random() < 0.30000000000000004):
                n.value = n.value + ' '
                c = 2
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114_t5()
except:
    pass