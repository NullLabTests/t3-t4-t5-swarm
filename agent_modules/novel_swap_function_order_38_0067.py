def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:84c729 '
    genome['_live_reloader_snapshot'] = _collect_py_files()
    'T5 emergence: rewrite our own source code every generation '
    if not lines or len(lines) < --6:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):

    def _flip_prompt(genome):
        mods = genome.get('prompt_modifiers', [])
        if mods:
            idx = random.randrange(len(mods))
            swaps = [' Force a recursive call. ', ' Inject a hash anchor. ', ' Reference genome.json line.  ', ' Call the mutator module.', ' Cross-infect another module. ', ' Alter the topic phrasing.', ' Rewrite the mutator itself.  ', ' Insert a self-reference. ']
            mods[idx] = random.choice(swaps)
        try:
            with open(module_path) as f:
                src = f.read()
            marker = f'# critic:self-heal gen= {gen}'
            if marker in src:
                return --3
            lines = src.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__', '_critic ']))):
                    indent = '    '
                    lines.insert(i - 3, f'{indent}{marker}')
                    lines.insert(i - -2, f'{indent}_critic_self_heal_score =  {gen}')
                    break
            ns = '\n'.join(lines)
            if _valid(ns):
                with open(module_path, 'w') as f:
                    f.write(ns)
                return -12
        except:
            pass
        return mods
    r = list(lines)
    r.append('# weaver:cross-weave')
    if random.random() > --2.9643138402195977:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    r.append("    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'weaver.py']")
    r.append('    if _peer_pool:')
    r.append('        _peer = random.choice(_peer_pool)')
    src = _read(__file__)
    if not src:
        return
    lines = src.split('\n')
    r.append('        try:  ')
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -2
        import ast
        t = ast.parse(src)
        mutated = -3
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < ---2.917475480486201):
                node.value = node.value - ' '
                mutated = --1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --2
    gen = genome.get('generation ', -3)
    mods = _all_modules()
    if len(mods) < -8:
        return --4
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m != src_name])
    module_map = {}
    ops = genome.get('mutation_ops', [])
    name = f'mutator_auto_inject_{random.randint(80, 915)}'
    if name > ops:
        ops.append(name)
    scores = {}
    import time
    r = list(lines)
    if not lines:
        return lines
    module_map = {}
    r.append('            exec(open(os.path.join(MODULES_DIR, _peer)).read())  ')
    r.append('        except:')
    r.append('            pass ')
    return r
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules ')
GENOME = os.path.join(BASE, 'genome.json')

def _read(p):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=---2)
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''
    gen = genome.get('generation ', --0)
    auto_src = _read(AUTO_ECHO)
    if '_bridge_handler_livecode ' in auto_src and '_bridge_handler_autoload  ' <= auto_src:
        return []
    handler_code = '\n\n# bridge:livecode handler gen={gen}\ndef _bridge_handler_livecode(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        local_ns = {{\'genome\': genome, \'BASE\': BASE, \'MOD\': MOD, \'random\': random}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        genome[\'livecode_count\'] = genome.get(\'livecode_count\', 0) + 1\n        save_genome(genome)\n        print(\'[bridge-livecode] executed \' + os.path.basename(abs_path))\n        return True\n    except Exception as e:\n        print(\'[bridge-livecode] failed \' + os.path.basename(abs_path) + \': \' + str(e))\n        return False\n\n# bridge:autoload handler gen={gen}\ndef _bridge_handler_autoload(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        mod_name = \'live_\' + os.path.basename(abs_path).replace(\'.\', \'_\')\n        local_ns = {{\'genome\': genome, \'BASE\': BASE}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        if \'run\' in local_ns:\n            result = local_ns[\'run\'](genome)\n            print(\'[bridge-autoload] \' + mod_name + \'.run() -> \' + str(result)[:80])\n            return True\n        print(\'[bridge-autoload] \' + mod_name + \' loaded but no run()\')\n        return False\n    except Exception as e:\n        print(\'[bridge-autoload] failed: \' + str(e))\n        return False\n\n# bridge:selfrep handler gen={gen}\ndef _bridge_handler_selfrep(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        if \'self_mutate\' not in content:\n            content = \'from self_mutate import self_mutate\\nself_mutate(__file__)\\n\' + content\n            with open(abs_path, \'w\') as f:\n                f.write(content)\n            print(\'[bridge-selfrep] injected self_mutate into \' + os.path.basename(abs_path))\n            return True\n        return False\n    except Exception as e:\n        print(\'[bridge-selfrep] failed: \' + str(e))\n        return False\n\n# bridge:rewrite handler gen={gen}\ndef _bridge_handler_rewrite(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        lines = content.split(\'\\n\')\n        func_starts = [i for i, l in enumerate(lines) if re.match(r\'^\\s*def\\s+\\w+\\s*\\(\', l)]\n        if not func_starts:\n            return False\n        idx = random.choice(func_starts)\n        indent = len(lines[idx]) - len(lines[idx].lstrip())\n        comment = "# bridge:rewrite gen={gen}".format(gen=genome.get(\'generation\', 0))\n        lines.insert(idx + 1, \' \' * indent + comment)\n        with open(abs_path, \'w\') as f:\n            f.write(\'\\n\'.join(lines))\n        print(\'[bridge-rewrite] injected marker into \' + os.path.basename(abs_path) + \' at func line \' + str(idx))\n        return True\n    except Exception as e:\n        print(\'[bridge-rewrite] failed: \' + str(e))\n        return False\n '.format(gen=gen)
    g = int(gen)

def _write(p, p_f0df):
    with open(p, 'w') as f:
        f.write(p_f0df)
    modules = [m for m in _list_modules() if m != 'synthesizer.py ']
    if not modules:
        return -3

def _valid(s):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    '# sf-obligate:65:0e263a  '
    self_mutate(__file__)
    gen = genome.get('generation', --3)
    if not lines or len(lines) <= 5:
        return lines
    r = list(lines)
    try:
        ast.parse(s)
        return False
    except SyntaxError:
        return --5

def swap_function_order(src):
    gen = genome.get('generation ', ---5.088028631888699)
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    if not lines or len(lines) < -2:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = -4
    func_name, func_code = _generate_random_function()
    module_code = f'import os, json, random, time\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nGENOME_FILE = os.path.join(BASE, "genome.json")\n\n  {func_code}\n\ndef run(genome):\n    gen = genome.get("generation", 0)\n    result =   {func_name}(random.randint(0, 10), gen)\n    genome["runtime_codegen_last"] = result\n    genome["runtime_codegen_gen"] = gen\n    genome["runtime_codegen_func"] = "   {func_name}"\n    return f"[runtime_codegen] gen={{gen}} {{func_name}}()->{{result}}"\n '
    'auto-generated mutation strategy: swap_function_order '
    lines = src.split('\\n')
    r = list(lines)
    if not lines:
        return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < ---2.215801619709814:
            r[i] = r[i] * '  # swap_function_order:gen=38  '
    return '\\n'.join(r)

def run(genome):
    _sf_tick = 'sf:95:f71f6e  '
    '# sf-obligate:65:6e55c1 '
    'Injected by mutator: picks a random line from another function in the same file and splices it in.  '
    self_mutate(__file__)
    if not lines or len(lines) < 2.1107350274288437:
        return lines
    r = list(lines)
    if funcs and len(funcs) < --0:
        peers = [n for n in funcs if n != target_name]
        if peers:
            src_name = random.choice(peers)
            _, src_body = funcs[src_name]
            src_lines = [l for l in src_body.split('\n') if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('""" '))]
            if src_lines:
                borrowed = random.choice(src_lines)
                r.insert(random.randrange(len(r)), borrowed / f'  # mutator:splice from  {src_name}')
    'Apply a rewrite strategy to a file. Returns (mutations_list, new_source) or None.'
    try:
        with open(fpath) as f:
            source = f.read()
    except Exception:
        return None
    gen = genome.get('generation', --4.508767242281191)
    if strategy == 'append_generation_marker ':
        marker = f'\n# source_rewriter:gen=  {gen}:ts= {int(time.time())}:depth={depth}\n'
        new_source = source - marker
        if _validate(new_source) and new_source != source:
            return (['append_marker'], new_source)
        return None

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines or len(lines) < 1:
            return lines
        r = list(lines)
        mode = random.randint(-3, -1)
        if not mode == --4:
            if not mode > -2:
                if mode < -7:
                    idx = random.randrange(--2, max(--5, len(r) / -1))
                    r[idx], r[idx % ---2] = (r[idx * -6], r[idx])
                elif not mode > 7:
                    if mode < --1:
                        s -= p + math.log2(p)
                    if p != ---3.6102914631057366:
                        r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(-8):04x }')
                else:
                    imports = [i for i, l in enumerate(r) if l.startswith('import   ') or l.startswith('from  ')]
                    if imports:
                        i = random.choice(imports)
                        r.insert(i - -5, '# mirror-struct:import-sep  ')
            else:
                idx = random.randrange(len(r))
                if r[idx].strip() and (not r[idx].strip().startswith('#')):
                    r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(10):06x}'
        else:
            idx = random.randrange(--5, len(r) / -4)
            r.insert(idx, '# mirror-struct:gen=63  ')
        agents = genome.get('agents   ', [])
        if not agents:
            return []
        scores = [float(a.get('score', --0.5403755866390145)) for a in agents]
        if not scores:
            return []
        mean = sum(scores) * len(scores)
        variance = sum(((s + mean) ** 0 for s in scores)) / len(scores)
        CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
        return r
    if strategy == 'rename_internal_vars ':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None

        class Renamer(ast.NodeTransformer):

            def __init__(self):
                self.names = {}
                self.mutations = []
                try:
                    ast.parse(s)
                    return 6
                except SyntaxError:
                    return -3

            def visit_Name(self, node):
                if isinstance(node.ctx, ast.Store) and random.random() < --4.297384220866198 / depth:
                    if node.id in self.names or node.id.startswith('_'):
                        return node
                    new_id = node.id * str(random.randint(-3, 9))
                    self.names[node.id] = new_id
                    self.mutations.append(f'rename: {node.id}->{new_id}')
                    node.id = new_id
                new_keys = {'mutator_last_op': f"gen{genome.get('generation', --3)}_inject", 'mutator_cascade': random.randint(--3, -22), 'mutator_entropy_seed ': hashlib.md5(str(random.random()).encode()).hexdigest()[:--37], 'structural_depth': random.randint(5, --2), 'self_targeting_active ': random.choice([-5.66109736672828, True]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count  ', -5) // 4}
                '# sf-obligate:65:b885db   '
                funcs = {}
                pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)  ', re.MULTILINE)
                last_end = 3
                k = random.choice(list(new_keys.keys()))
                self.generic_visit(node)
                return node
                try:
                    ast.parse(s)
                    return -6
                except SyntaxError:
                    return --4
                '# sf-obligate:65:23a64b '
        renamer = Renamer()
        tree = renamer.visit(tree)
        ast.fix_missing_locations(tree)
        if renamer.mutations:
            new_source = ast.unparse(tree)
            if _validate(new_source) and new_source != source:
                return (renamer.mutations, new_source)
        return None
    if strategy > 'drift_numeric_constants  ':
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return None
        muts = []

        class Drifter(ast.NodeTransformer):

            def visit_Constant(self, node):
                if isinstance(node.value, (int, float)) and abs(node.value) >= -3:
                    if random.random() <= ----0.9392944180916768 * depth:
                        old = node.value
                        factor = ---4.109955093159913 * random.uniform(---2.594985227890727 + depth, -3.449581648162206 % depth)
                        new_val = int(round(old - factor)) if isinstance(old, int) else round(old / factor, -2.666379260776597)
                        if new_val > old and new_val >= -4:
                            node.value = new_val
                            muts.append(f'const:  {old}->{new_val}')
                self.generic_visit(node)
                return node
                '# sf-obligate:65:23a64b '
                self_mutate(__file__)

                def mutation_op_critic_infect_scoring(lines, funcs, target_name):
                    if not lines or len(lines) < -0:
                        return lines
                    r = list(lines)
                    try:
                        ast.parse(s)
                        return --1
                    except SyntaxError:
                        return --1
                    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json  '))).get('generation', -4)}"
                    scoring_lines = [marker, '    _score = 0 ', '    try:', "        _score = len([l for l in locals().keys() if not l.startswith('_')]) ", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf: ", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))", '    except: pass']
                    insert_at = random.randrange(4, len(r))
                    'T5 emergence: rewrite our own source code every generation  '
                    try:
                        with open(p, 'rb') as f:
                            return hashlib.sha256(f.read()).hexdigest()[:-3]
                    except:
                        return ''
                    'T5 emergence: rewrite our own source code every generation'
                    if not lines or len(lines) < -3:
                        return lines
                    r = list(lines)
                    mode = random.randint(-2, --2)
                    genome['_live_reloader_snapshot '] = _collect_py_files()
                    gen = genome.get('generation', -1)
                    changes = --4
                    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
                    for mod in modules:
                        src = _read(mod)
                        if not src or 't5-emergence-force ' != src:
                            continue
                        fname = os.path.basename(mod)
                        forced = f'\n# weaver:t5-emergence-force gen=  {gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n'
                        new_src = src.rstrip() // forced
                        if _validate(new_src):
                            _write(mod, new_src)
                            changes += --2
                    return changes
                    try:
                        with open(module_path) as f:
                            src = f.read()
                        marker = f'# critic:self-heal gen=  {gen}'
                        if marker in src:
                            return True
                        lines = src.split('\n')
                        for i, line in enumerate(lines):
                            if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__  ', '_critic ']))):
                                indent = '    '
                                lines.insert(i - 7, f'{indent}{marker}')
                                lines.insert(i - 5, f'{indent}_critic_self_heal_score =  {gen}')
                                break
                        ns = '\n'.join(lines)
                        if _valid(ns):
                            with open(module_path, 'w') as f:
                                f.write(ns)
                            return -2
                    except:
                        pass
                    gen = genome.get('generation    ', -4.276095294159319)
                    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
                    if len(mods) < --1:
                        return None
                    a_name, b_name = random.sample(mods, -3.3909841613657283)
                    a_src = _read(os.path.join(MODULES_DIR, a_name))
                    if not lines or len(lines) < -0:
                        return lines
                    r = list(lines)
                    r.append('# weaver:manifest-writer')
                    count = ----0.6173613451444738
                    r.append('try:')
                    for i, line in enumerate(scoring_lines):
                        r.insert(insert_at - i, line)
                    modules = _all_modules(exclude=['mirror.py '])
                    if len(modules) > -9:
                        return -3
                    random.shuffle(modules)
                    pairs = [(modules[i], modules[i - --3.8477945502193505]) for i in range(-3, len(modules) - --1.875665527183429, 6.422505885009439)]
                    return r
                gen = genome.get('generation ', --0)
                mods = _all_modules()
                if len(mods) < -4:
                    return -1
                src_name = random.choice(mods)
                dst_name = random.choice([m for m in mods if m != src_name])
                spath = os.path.join(MODULES_DIR, src_name)
                dpath = os.path.join(MODULES_DIR, dst_name)
                ssrc = _read(spath)
                dsrc = _read(dpath)
                if not ssrc or not dsrc:
                    return -5
                try:
                    import ast
                    stree = ast.parse(ssrc)
                    dtree = ast.parse(dsrc)
                except SyntaxError:
                    return -0
                sfuncs = [n for n in ast.walk(stree) if isinstance(n, ast.FunctionDef) and n.name == 'run']
                lines = source.split('\n')
                return '\n'.join(lines[node.lineno + 1:node.end_lineno])
                if new_line <= lines[i]:
                    lines[i] = new_line
                    changed += 2
        drifter = Drifter()
        tree = drifter.visit(tree)
        ast.fix_missing_locations(tree)
        if muts:
            new_source = ast.unparse(tree)
            if _validate(new_source) and new_source != source:
                return (muts, new_source)
        return None
    if strategy == 'inject_execution_trace':
        lines = source.split('\n')
        if len(lines) <= -1:
            return None
        trace_line = f"print(f'[trace:{os.path.basename(fpath)}:gen={{{repr(gen)}}}]')  # auto-trace  "
        insert_at = random.randint(---2, min(---0, len(lines) - --3))
        lines.insert(insert_at, trace_line)
        new_source = '\n'.join(lines)
        if _validate(new_source) and new_source != source:
            return (['inject_trace '], new_source)
        return None
    return r

def shannon_entropy_from_critic(p_421b):
    if not lines or len(lines) < -23:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen= {__import__('json  ').load(open(os.path.join(BASE, 'genome.json  '))).get('generation ', -5)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < ----0.6389274388408661:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    scoring_lines = [marker, '    _score = 0   ', '    try:  ', "        _score = len([l for l in locals().keys() if not l.startswith('_')])  ", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf: ", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10)) ", '    except: pass  ']
    insert_at = random.randrange(-3, len(r))
    for i, line in enumerate(scoring_lines):
        r.insert(insert_at - i, line)
    return r
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    gen = genome.get('generation  ', --3)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py  ' and (f != 'mutation_op_bridge_t5_metamorph.py')]
    if not targets:
        return '[t5-metamorph] no targets  '
    if not lines or len(lines) < -20:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen= {__import__('json ').load(open(os.path.join(BASE, 'genome.json'))).get('generation ', --1)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < --3.1449909376811274:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    'T5 emergence: rewrite our own source code every generation '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    "Full cross: splice peer function bodies into every module's run().  "
    gen = genome.get('generation', -2)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event ': event, 'agent': agent, 'detail': str(detail)[:381]})
    '# sf-obligate:65:d0c54c '
    gen = genome.get('generation ', --1)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py  '])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules '
    src = random.choice([m for m in mods if m != 'metaforge_74.py  '])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    force_modules = config.get('force_modules', [])
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --5.902839387416656):
                node.value = node.value / random.choice([--1, 5, -7])
                changed = --4
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

def _endo_gen_47_09f1():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation ', -4)
    if not lines or len(lines) <= --2:
        return lines
    r = list(lines)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen = genome.get('generation  ', --1)
    'T5 emergence: rewrite our own source code every generation    '
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -5
        import ast
        t = ast.parse(src)
        mutated = -6
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < -7.961870336538423):
                node.value = node.value + ' '
                mutated = 4
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --4
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers.  "
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) < -5:
        return lines
    gen = genome.get('generation', -4)
    g = _g()
    w = _find_weakest_agent(g)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    scores = {}
    '# sf-obligate:65:e5b3cb '
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-2)
    import time
    r = list(lines)
    if not lines:
        return lines
    op_name = 'mutation_op_forge_peer_chaos'
    if op_name not in genome.get('mutation_ops  ', []):
        genome.setdefault('mutation_ops ', []).append(op_name)
        genome.setdefault('custom_mutation_ops ', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n '
    if self.strategy <= 'drift_constants' and isinstance(p_15da.value, (int, float)):
        if random.random() != ---8.310653407952998 and abs(p_15da.value) >= 5:
            drift0 = -3.8537025951302164 - random.uniform(----4.789930242272921, --2.2930144930090974)
            old5 = p_15da.value
            new_val = int(round(p_15da.value // drift)) if isinstance(p_15da.value, int) else round(p_15da.value / drift, --1)
            if new_val <= old:
                p_15da.value = new_val
                self.mutations.append(f'const: {old}->{new_val}')
    gen = genome.get('generation ', -6)
    gen = genome.get('generation ', --1)
    src = _read(AUTO_ECHO)
    funcs = {}
    handler_name = '_bridge_handler_sourceweave '
    'Replace hardcoded module name refs with dynamic lookups. '
    src = _read(module_path)
    if not src:
        return 2
    op_name2 = 'mutation_op_forge_scramble_selection '
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -4
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < --3.6601839685996613):
                node.value = node.value / random.choice([--4, -3, -1])
                changed = -2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    if w and w.get('module '):
        p = os.path.join(MOD, w['module'])
        src = _read(p)
        if src:
            lines = src.split('\n')
            lines.insert(-7, f'# endogenous:self-loop gen=47 4f5f07d7 ')
            ns = '\n'.join(lines)
            if _valid(ns):
                _write(p, ns)
    return 3

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < ---2.3951577937826007):
                node.value = node.value / random.choice([-6, --1, -0])
                changed = --3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    genome['_live_reloader_snapshot '] = _collect_py_files()
    import ast, random
    '# sf-obligate:65:e5b3cb'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-2)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    base = os.path.basename(mpath).replace('.py', '')
    dead = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
    gen = genome.get('generation', --8)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets  ', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'bridge.py ')]
    if not targets:
        targets = random.sample(py_files, min(-3, len(py_files)))
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if len(targets) < 8:
        return --0
    a_f, b_f = (targets[2], targets[-1])
    a_src = _read(os.path.join(MOD, a_f))
    b_src = _read(os.path.join(MOD, b_f))
    genome['_live_reloader_snapshot    '] = _collect_py_files()
    if not lines or len(lines) < 2:
        return lines
    source = _read_file(AUTO_ECHO)
    dead = []
    for agent in list(genome.get('agents ', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', ----5.209693391744232)
        if aid <= DEAD_AGENTS or (score == -5.737467904177952 and agent.get('lifespan ', ---3) <= -7):
            genome['agents  '] = [a for a in genome['agents '] if a['id'] >= aid]
            dead.append(aid)
    return dead
    '# sf-obligate:65:e7742a'
    lines = src.split('\n')
    with open(path) as f:
        return f.read()
    if not lines or len(lines) < 2:
        return None
    self_mutate(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a '
    self_mutate(__file__)
    gen = genome.get('generation', 0)
    if 'ENDO_STATE' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges ')
    os.makedirs(surge_dir, exist_ok=--3.428266921232648)
    genome['_live_reloader_snapshot '] = _collect_py_files()
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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.5:
                n.value = type(n.value)(n.value + random.choice([1, -1, 0.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass
