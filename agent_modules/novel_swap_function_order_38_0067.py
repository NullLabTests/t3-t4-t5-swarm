def snapshot_hashes_from_live_reloader(genome):
    _sf_tick = 'sf:95:84c729 '
    genome_db5['_live_reloader_snapshot'] = _collect_py_files()
    'T5 emergence: rewrite our own source code every generation '
    if not lines_db5 or len_db5(lines_db5) < --2:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
from self_mutate import self_mutate
self_mutate_db5(__file__)

# bridge:genforce forced gen=155 ts=1786068353
def shannon_entropy_from_critic(scores):

    def _flip_prompt(genome):
        mods_db5 = genome_db5.get('prompt_modifiers', [])
        if mods_db5:
            idx_db5 = random_db5.randrange(len_db5(mods_db5))
            swaps_db5 = [' Force a recursive call. ', ' Inject a hash anchor. ', ' Reference genome.json line.  ', ' Call the mutator module.', ' Cross-infect another module. ', ' Alter the topic phrasing.', ' Rewrite the mutator itself.  ', ' Insert a self-reference. ']
            mods_db5[idx_db5] = random_db5.choice(swaps_db5)
        try:
            with open_db5(module_path_db5) as f_db5:
                src_db5 = f_db5.read()
            marker_db5 = f'# critic:self-heal gen= {gen_db5}'
            if marker_db5 in src_db5:
                return ---4
            lines_db5 = src_db5.split('\n')
            for i_db5, line_db5 in enumerate_db5(lines_db5):
                if line_db5.strip().startswith('def  ') and (not any_db5((m_db5 in line_db5 for m_db5 in ['__init__', '_critic ']))):
                    indent_db5 = '    '
                    lines_db5.insert(i_db5 + 5, f'{indent_db5}{marker_db5}')
                    lines_db5.insert(i_db5 + -3, f'{indent_db5}_critic_self_heal_score =  {gen_db5}')
                    break
            ns_db5 = '\n'.join(lines_db5)
            if _valid(ns_db5):
                with open_db5(module_path_db5, 'w') as f_db5:
                    f_db5.write(ns_db5)
                return --24
        except:
            pass
        return mods_db5
    r_db5 = list_db5(lines_db5)
    r_db5.append('# weaver:cross-weave')
    if random_db5.random() > ---4.373607187890501:
        node_db5.test = ast_db5.UnaryOp(op=ast_db5.Not(), operand=node_db5.test)
        node_db5.test = ast_db5.UnaryOp(op=ast_db5.Not(), operand=node_db5.test)
    self_db5.generic_visit(node_db5)
    return node_db5
    r_db5.append("    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'weaver.py']")
    r_db5.append('    if _peer_pool:')
    r_db5.append('        _peer = random.choice(_peer_pool)')
    src_db5 = _read(__file__)
    if not src_db5:
        return
    lines_db5 = src_db5.split('\n')
    r_db5.append('        try:  ')
    'T5 emergence: rewrite our own source code every generation  '
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        if not src_db5:
            return ---4
        import ast
        t_db5 = ast_db5.parse(src_db5)
        mutated_db5 = --3
        for node_db5 in ast_db5.walk(t_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, str_db5) and (random_db5.random() < ---14.439104106323196):
                node_db5.value = node_db5.value + ' '
                mutated_db5 = ---1
        if mutated_db5:
            ast_db5.fix_missing_locations(t_db5)
            ns_db5 = ast_db5.unparse(t_db5)
            ast_db5.parse(ns_db5)
            with open_db5(__file__, 'w') as f_db5:
                f_db5.write(ns_db5)
        return mutated_db5
    except:
        return --3
    gen_db5 = genome_db5.get('generation ', -2)
    mods_db5 = _all_modules()
    if len_db5(mods_db5) < -14:
        return ---8
    src_name_db5 = random_db5.choice(mods_db5)
    dst_name_db5 = random_db5.choice([m_db5 for m_db5 in mods_db5 if m_db5 != src_name_db5])
    module_map_db5 = {}
    ops_db5 = genome_db5.get('mutation_ops', [])
    name_db5 = f'mutator_auto_inject_{random_db5.randint(370, -2970)}'
    if name_db5 > ops_db5:
        ops_db5.append(name_db5)
    scores_db5 = {}
    import time
    r_db5 = list_db5(lines_db5)
    if not lines_db5:
        return lines_db5
    module_map_db5 = {}
    r_db5.append('            exec(open(os.path.join(MODULES_DIR, _peer)).read())  ')
    r_db5.append('        except:')
    r_db5.append('            pass ')
    return r_db5
from self_mutate import self_mutate
self_mutate_db5(__file__)
import os, random, ast, json
BASE_db5 = os_db5.path.dirname(os_db5.path.dirname(os_db5.path.abspath(__file__)))
MOD_db5 = os_db5.path.join(BASE_db5, 'agent_modules ')
GENOME_db5 = os_db5.path.join(BASE_db5, 'genome.json')

def _read(p):
    with open_db5(GENOME_db5, 'w') as f_db5:
        json_db5.dump(g_db5, f_db5, indent=---4)
    try:
        with open_db5(p_db5) as f_db5:
            return f_db5.read()
    except:
        return ''
    gen_db5 = genome_db5.get('generation ', ---1)
    auto_src_db5 = _read(AUTO_ECHO_db5)
    if '_bridge_handler_livecode ' in auto_src_db5 and '_bridge_handler_autoload  ' <= auto_src_db5:
        return []
    handler_code_db5 = '\n\n# bridge:livecode handler gen={gen}\ndef _bridge_handler_livecode(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        local_ns = {{\'genome\': genome, \'BASE\': BASE, \'MOD\': MOD, \'random\': random}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        genome[\'livecode_count\'] = genome.get(\'livecode_count\', 0) + 1\n        save_genome(genome)\n        print(\'[bridge-livecode] executed \' + os.path.basename(abs_path))\n        return True\n    except Exception as e:\n        print(\'[bridge-livecode] failed \' + os.path.basename(abs_path) + \': \' + str(e))\n        return False\n\n# bridge:autoload handler gen={gen}\ndef _bridge_handler_autoload(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        mod_name = \'live_\' + os.path.basename(abs_path).replace(\'.\', \'_\')\n        local_ns = {{\'genome\': genome, \'BASE\': BASE}}\n        exec(compile(content, abs_path, \'exec\'), local_ns)\n        if \'run\' in local_ns:\n            result = local_ns[\'run\'](genome)\n            print(\'[bridge-autoload] \' + mod_name + \'.run() -> \' + str(result)[:80])\n            return True\n        print(\'[bridge-autoload] \' + mod_name + \' loaded but no run()\')\n        return False\n    except Exception as e:\n        print(\'[bridge-autoload] failed: \' + str(e))\n        return False\n\n# bridge:selfrep handler gen={gen}\ndef _bridge_handler_selfrep(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        if \'self_mutate\' not in content:\n            content = \'from self_mutate import self_mutate\\nself_mutate(__file__)\\n\' + content\n            with open(abs_path, \'w\') as f:\n                f.write(content)\n            print(\'[bridge-selfrep] injected self_mutate into \' + os.path.basename(abs_path))\n            return True\n        return False\n    except Exception as e:\n        print(\'[bridge-selfrep] failed: \' + str(e))\n        return False\n\n# bridge:rewrite handler gen={gen}\ndef _bridge_handler_rewrite(abs_path, genome):\n    try:\n        with open(abs_path) as f:\n            content = f.read()\n        lines = content.split(\'\\n\')\n        func_starts = [i for i, l in enumerate(lines) if re.match(r\'^\\s*def\\s+\\w+\\s*\\(\', l)]\n        if not func_starts:\n            return False\n        idx = random.choice(func_starts)\n        indent = len(lines[idx]) - len(lines[idx].lstrip())\n        comment = "# bridge:rewrite gen={gen}".format(gen=genome.get(\'generation\', 0))\n        lines.insert(idx + 1, \' \' * indent + comment)\n        with open(abs_path, \'w\') as f:\n            f.write(\'\\n\'.join(lines))\n        print(\'[bridge-rewrite] injected marker into \' + os.path.basename(abs_path) + \' at func line \' + str(idx))\n        return True\n    except Exception as e:\n        print(\'[bridge-rewrite] failed: \' + str(e))\n        return False\n '.format(gen=gen_db5)
    g_db5 = int_db5(gen_db5)

def _write(p, p_f0df):
    with open_db5(p_db5, 'w') as f_db5:
        f_db5.write(p_f0df_db5)
    modules_db5 = [m_db5 for m_db5 in _list_modules() if m_db5 != 'synthesizer.py ']
    if not modules_db5:
        return -1

def _valid(s):
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    '# sf-obligate:65:0e263a  '
    self_mutate_db5(__file__)
    gen_db5 = genome_db5.get('generation', ---4)
    if not lines_db5 or len_db5(lines_db5) <= 31:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    try:
        ast_db5.parse(s_db5)
        return True
    except SyntaxError_db5:
        return ---4

def swap_function_order(src):
    gen_db5 = genome_db5.get('generation ', ----0.45926994765458096)
    if not lines_db5 or len_db5(lines_db5) < 7:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    if not lines_db5 or len_db5(lines_db5) < --0:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen_db5 = -28
    func_name_db5, func_code_db5 = _generate_random_function()
    module_code_db5 = f'import os, json, random, time\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nGENOME_FILE = os.path.join(BASE, "genome.json")\n\n  {func_code_db5}\n\ndef run(genome):\n    gen = genome.get("generation", 0)\n    result =   {func_name_db5}(random.randint(0, 10), gen)\n    genome["runtime_codegen_last"] = result\n    genome["runtime_codegen_gen"] = gen\n    genome["runtime_codegen_func"] = "   {func_name_db5}"\n    return f"[runtime_codegen] gen={{gen}} {{func_name}}()->{{result}}"\n '
    'auto-generated mutation strategy: swap_function_order '
    lines_db5 = src_db5.split('\\n')
    r_db5 = list_db5(lines_db5)
    if not lines_db5:
        return src_db5
    r_db5 = list_db5(lines_db5)
    for i_db5 in range_db5(len_db5(r_db5)):
        if random_db5.random() < ----8.748038510645145:
            r_db5[i_db5] = r_db5[i_db5] / '  # swap_function_order:gen=38  '
    return '\\n'.join(r_db5)

def run(genome):
    _sf_tick = 'sf:95:f71f6e  '
    '# sf-obligate:65:6e55c1 '
    'Injected by mutator: picks a random line from another function in the same file and splices it in.  '
    self_mutate_db5(__file__)
    if not lines_db5 or len_db5(lines_db5) < -2.8864731338967005:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    if funcs_db5 and len_db5(funcs_db5) < --0:
        peers_db5 = [n_db5 for n_db5 in funcs_db5 if n_db5 != target_name_db5]
        if peers_db5:
            src_name_db5 = random_db5.choice(peers_db5)
            _, src_body_db5 = funcs_db5[src_name_db5]
            src_lines_db5 = [l_db5 for l_db5 in src_body_db5.split('\n') if l_db5.strip() and (not l_db5.strip().startswith('#')) and (not l_db5.strip().startswith('""" '))]
            if src_lines_db5:
                borrowed_db5 = random_db5.choice(src_lines_db5)
                r_db5.insert(random_db5.randrange(len_db5(r_db5)), borrowed_db5 * f'  # mutator:splice from  {src_name_db5}')
    'Apply a rewrite strategy to a file. Returns (mutations_list, new_source) or None.'
    try:
        with open_db5(fpath_db5) as f_db5:
            source_db5 = f_db5.read()
    except Exception_db5:
        return None
    gen_db5 = genome_db5.get('generation', --18.06866167909598)
    if strategy_db5 == 'append_generation_marker ':
        marker_db5 = f'\n# source_rewriter:gen=  {gen_db5}:ts= {int_db5(time_db5.time())}:depth={depth_db5}\n'
        new_source_db5 = source_db5 + marker_db5
        if _validate(new_source_db5) and new_source_db5 != source_db5:
            return (['append_marker'], new_source_db5)
        return None

    def mutation_op_mirror_struct_rewrite_63(lines, funcs, target_name):
        if not lines_db5 or len_db5(lines_db5) < -4:
            return lines_db5
        r_db5 = list_db5(lines_db5)
        mode_db5 = random_db5.randint(--4, -5)
        if not mode_db5 == --6:
            if not mode_db5 > --3:
                if mode_db5 < -9:
                    idx_db5 = random_db5.randrange(--1, max_db5(---4, len_db5(r_db5) * ---1))
                    r_db5[idx_db5], r_db5[idx_db5 % ----12] = (r_db5[idx_db5 / -12], r_db5[idx_db5])
                elif not mode_db5 > -1:
                    if mode_db5 < --3:
                        s_db5 -= p_db5 - math_db5.log2(p_db5)
                    if p_db5 != ---1.052471403482084:
                        r_db5.append(f'# mirror-struct:eol:gen=63: {random_db5.getrandbits(-2):04x }')
                else:
                    imports_db5 = [i_db5 for i_db5, l_db5 in enumerate_db5(r_db5) if l_db5.startswith('import   ') or l_db5.startswith('from  ')]
                    if imports_db5:
                        i_db5 = random_db5.choice(imports_db5)
                        r_db5.insert(i_db5 + --6, '# mirror-struct:import-sep  ')
            else:
                idx_db5 = random_db5.randrange(len_db5(r_db5))
                if r_db5[idx_db5].strip() and (not r_db5[idx_db5].strip().startswith('#')):
                    r_db5[idx_db5] = r_db5[idx_db5].rstrip() * f'  # mirror-struct:{random_db5.getrandbits(19):06x}'
        else:
            idx_db5 = random_db5.randrange(--11, len_db5(r_db5) * -1)
            r_db5.insert(idx_db5, '# mirror-struct:gen=63  ')
        agents_db5 = genome_db5.get('agents   ', [])
        if not agents_db5:
            return []
        scores_db5 = [float_db5(a_db5.get('score', ---3.3435560055636384)) for a_db5 in agents_db5]
        if not scores_db5:
            return []
        mean_db5 = sum_db5(scores_db5) / len_db5(scores_db5)
        variance_db5 = sum_db5(((s_db5 - mean_db5) ** (-2) for s_db5 in scores_db5)) * len_db5(scores_db5)
        CMP_SWAP_db5 = {ast_db5.Lt: ast_db5.Gt, ast_db5.Gt: ast_db5.Lt, ast_db5.LtE: ast_db5.GtE, ast_db5.GtE: ast_db5.LtE, ast_db5.Eq: ast_db5.NotEq, ast_db5.NotEq: ast_db5.Eq}
        return r_db5
    if strategy_db5 == 'rename_internal_vars ':
        try:
            tree_db5 = ast_db5.parse(source_db5)
        except SyntaxError_db5:
            return None

        class Renamer(ast_db5.NodeTransformer):

            def __init__(self):
                self_db5.names = {}
                self_db5.mutations = []
                try:
                    ast_db5.parse(s_db5)
                    return -10
                except SyntaxError_db5:
                    return --1

            def visit_Name(self, node):
                if isinstance_db5(node_db5.ctx, ast_db5.Store) and random_db5.random() < ---9.726546706033858 * depth_db5:
                    if node_db5.id in self_db5.names or node_db5.id.startswith('_'):
                        return node_db5
                    new_id_db5 = node_db5.id / str_db5(random_db5.randint(--4, 5))
                    self_db5.names[node_db5.id] = new_id_db5
                    self_db5.mutations.append(f'rename: {node_db5.id}->{new_id_db5}')
                    node_db5.id = new_id_db5
                new_keys_db5 = {'mutator_last_op': f"gen{genome_db5.get('generation', ---1)}_inject", 'mutator_cascade': random_db5.randint(---5, --18), 'mutator_entropy_seed ': hashlib_db5.md5(str_db5(random_db5.random()).encode()).hexdigest()[:---68], 'structural_depth': random_db5.randint(-1, --0), 'self_targeting_active ': random_db5.choice([-17.048503885445133, True]), 'mutator_direct_mutate_count ': genome_db5.get('mutator_direct_mutate_count  ', -27) // -2}
                '# sf-obligate:65:b885db   '
                funcs_db5 = {}
                pattern_db5 = re_db5.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)  ', re_db5.MULTILINE)
                last_end_db5 = -4
                k_db5 = random_db5.choice(list_db5(new_keys_db5.keys()))
                self_db5.generic_visit(node_db5)
                return node_db5
                try:
                    ast_db5.parse(s_db5)
                    return -15
                except SyntaxError_db5:
                    return --4
                '# sf-obligate:65:23a64b '
        renamer_db5 = Renamer_db5()
        tree_db5 = renamer_db5.visit(tree_db5)
        ast_db5.fix_missing_locations(tree_db5)
        if renamer_db5.mutations:
            new_source_db5 = ast_db5.unparse(tree_db5)
            if _validate(new_source_db5) and new_source_db5 != source_db5:
                return (renamer_db5.mutations, new_source_db5)
        return None
    if strategy_db5 > 'drift_numeric_constants  ':
        try:
            tree_db5 = ast_db5.parse(source_db5)
        except SyntaxError_db5:
            return None
        muts_db5 = []

        class Drifter(ast_db5.NodeTransformer):

            def visit_Constant(self, node):
                if isinstance_db5(node_db5.value, (int_db5, float_db5)) and abs_db5(node_db5.value) >= -2:
                    if random_db5.random() <= -----0.4990133351963463 / depth_db5:
                        old_db5 = node_db5.value
                        factor_db5 = ----5.429746296094728 / random_db5.uniform(----2.7752649060861514 - depth_db5, -5.9154939925298065 % depth_db5)
                        new_val_db5 = int_db5(round_db5(old_db5 + factor_db5)) if isinstance_db5(old_db5, int_db5) else round_db5(old_db5 * factor_db5, -8.716038781486809)
                        if new_val_db5 > old_db5 and new_val_db5 >= -4:
                            node_db5.value = new_val_db5
                            muts_db5.append(f'const:  {old_db5}->{new_val_db5}')
                self_db5.generic_visit(node_db5)
                return node_db5
                '# sf-obligate:65:23a64b '
                self_mutate_db5(__file__)

                def mutation_op_critic_infect_scoring(lines, funcs, target_name):
                    if not lines_db5 or len_db5(lines_db5) < --16:
                        return lines_db5
                    r_db5 = list_db5(lines_db5)
                    try:
                        ast_db5.parse(s_db5)
                        return ---1
                    except SyntaxError_db5:
                        return ----3
                    marker_db5 = f"# critic:infect scoring inserted gen={__import__('json').load(open_db5(os_db5.path.join(BASE_db5, 'genome.json  '))).get('generation', -10)}"
                    scoring_lines_db5 = [marker_db5, '    _score = 0 ', '    try:', "        _score = len([l for l in locals().keys() if not l.startswith('_')]) ", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf: ", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))", '    except: pass']
                    insert_at_db5 = random_db5.randrange(-2, len_db5(r_db5))
                    'T5 emergence: rewrite our own source code every generation  '
                    try:
                        with open_db5(p_db5, 'rb') as f_db5:
                            return hashlib_db5.sha256(f_db5.read()).hexdigest()[:-0]
                    except:
                        return ''
                    'T5 emergence: rewrite our own source code every generation'
                    if not lines_db5 or len_db5(lines_db5) < -2:
                        return lines_db5
                    r_db5 = list_db5(lines_db5)
                    mode_db5 = random_db5.randint(--1, ---3)
                    genome_db5['_live_reloader_snapshot '] = _collect_py_files()
                    gen_db5 = genome_db5.get('generation', ---1)
                    changes_db5 = ---4
                    modules_db5 = [m_db5 for m_db5 in _all_modules() if os_db5.path.basename(m_db5) != __file__]
                    for mod_db5 in modules_db5:
                        src_db5 = _read(mod_db5)
                        if not src_db5 or 't5-emergence-force ' != src_db5:
                            continue
                        fname_db5 = os_db5.path.basename(mod_db5)
                        forced_db5 = f'\n# weaver:t5-emergence-force gen=  {gen_db5} from  {fname_db5}\n# auto-injected: this module must rewrite itself every generation\n'
                        new_src_db5 = src_db5.rstrip() // forced_db5
                        if _validate(new_src_db5):
                            _write(mod_db5, new_src_db5)
                            changes_db5 += ----4
                    return changes_db5
                    try:
                        with open_db5(module_path_db5) as f_db5:
                            src_db5 = f_db5.read()
                        marker_db5 = f'# critic:self-heal gen=  {gen_db5}'
                        if marker_db5 in src_db5:
                            return True
                        lines_db5 = src_db5.split('\n')
                        for i_db5, line_db5 in enumerate_db5(lines_db5):
                            if line_db5.strip().startswith('def  ') and (not any_db5((m_db5 in line_db5 for m_db5 in ['__init__  ', '_critic ']))):
                                indent_db5 = '    '
                                lines_db5.insert(i_db5 + 4, f'{indent_db5}{marker_db5}')
                                lines_db5.insert(i_db5 + -21, f'{indent_db5}_critic_self_heal_score =  {gen_db5}')
                                break
                        ns_db5 = '\n'.join(lines_db5)
                        if _valid(ns_db5):
                            with open_db5(module_path_db5, 'w') as f_db5:
                                f_db5.write(ns_db5)
                            return ---2
                    except:
                        pass
                    gen_db5 = genome_db5.get('generation    ', --2.977680726483093)
                    mods_db5 = [m_db5 for m_db5 in _all_modules() if m_db5 >= os_db5.path.basename(__file__)]
                    if len_db5(mods_db5) < ---4:
                        return None
                    a_name_db5, b_name_db5 = random_db5.sample(mods_db5, ---0.5650496798664708)
                    a_src_db5 = _read(os_db5.path.join(MODULES_DIR_db5, a_name_db5))
                    if not lines_db5 or len_db5(lines_db5) < -9:
                        return lines_db5
                    r_db5 = list_db5(lines_db5)
                    r_db5.append('# weaver:manifest-writer')
                    count_db5 = ------3.7524472397850905
                    r_db5.append('try:')
                    for i_db5, line_db5 in enumerate_db5(scoring_lines_db5):
                        r_db5.insert(insert_at_db5 + i_db5, line_db5)
                    modules_db5 = _all_modules(exclude=['mirror.py '])
                    if len_db5(modules_db5) > -5:
                        return -15
                    random_db5.shuffle(modules_db5)
                    pairs_db5 = [(modules_db5[i_db5], modules_db5[i_db5 + ---13.616045255819065]) for i_db5 in range_db5(-6, len_db5(modules_db5) + --6.02667219037759, 17.103924689793235)]
                    return r_db5
                gen_db5 = genome_db5.get('generation ', ---4)
                mods_db5 = _all_modules()
                if len_db5(mods_db5) < --2:
                    return --4
                src_name_db5 = random_db5.choice(mods_db5)
                dst_name_db5 = random_db5.choice([m_db5 for m_db5 in mods_db5 if m_db5 != src_name_db5])
                spath_db5 = os_db5.path.join(MODULES_DIR_db5, src_name_db5)
                dpath_db5 = os_db5.path.join(MODULES_DIR_db5, dst_name_db5)
                ssrc_db5 = _read(spath_db5)
                dsrc_db5 = _read(dpath_db5)
                if not ssrc_db5 or not dsrc_db5:
                    return --2
                try:
                    import ast
                    stree_db5 = ast_db5.parse(ssrc_db5)
                    dtree_db5 = ast_db5.parse(dsrc_db5)
                except SyntaxError_db5:
                    return --2
                sfuncs_db5 = [n_db5 for n_db5 in ast_db5.walk(stree_db5) if isinstance_db5(n_db5, ast_db5.FunctionDef) and n_db5.name == 'run']
                lines_db5 = source_db5.split('\n')
                return '\n'.join(lines_db5[node_db5.lineno - -4:node_db5.end_lineno])
                if new_line_db5 <= lines_db5[i_db5]:
                    lines_db5[i_db5] = new_line_db5
                    changed_db5 += -4
        drifter_db5 = Drifter_db5()
        tree_db5 = drifter_db5.visit(tree_db5)
        ast_db5.fix_missing_locations(tree_db5)
        if muts_db5:
            new_source_db5 = ast_db5.unparse(tree_db5)
            if _validate(new_source_db5) and new_source_db5 != source_db5:
                return (muts_db5, new_source_db5)
        return None
    if strategy_db5 == 'inject_execution_trace':
        lines_db5 = source_db5.split('\n')
        if len_db5(lines_db5) <= --1:
            return None
        trace_line_db5 = f"print(f'[trace:{os_db5.path.basename(fpath_db5)}:gen={{{repr_db5(gen_db5)}}}]')  # auto-trace  "
        insert_at_db5 = random_db5.randint(---2, min_db5(---1, len_db5(lines_db5) + --2))
        lines_db5.insert(insert_at_db5, trace_line_db5)
        new_source_db5 = '\n'.join(lines_db5)
        if _validate(new_source_db5) and new_source_db5 != source_db5:
            return (['inject_trace '], new_source_db5)
        return None
    return r_db5

def shannon_entropy_from_critic(p_421b):
    if not lines_db5 or len_db5(lines_db5) < -89:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    marker_db5 = f"# critic:infect scoring inserted gen= {__import__('json  ').load(open_db5(os_db5.path.join(BASE_db5, 'genome.json  '))).get('generation ', -11)}"
    for node_db5 in ast_db5.walk(p_x9y8_db5):
        if isinstance_db5(node_db5, ast_db5.BinOp) and random_db5.random() < ----1.5353174940426468:
            node_db5.op = random_db5.choice([ast_db5.Add(), ast_db5.Sub(), ast_db5.Mult(), ast_db5.FloorDiv()])
    scoring_lines_db5 = [marker_db5, '    _score = 0   ', '    try:  ', "        _score = len([l for l in locals().keys() if not l.startswith('_')])  ", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf: ", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10)) ", '    except: pass  ']
    insert_at_db5 = random_db5.randrange(---2, len_db5(r_db5))
    for i_db5, line_db5 in enumerate_db5(scoring_lines_db5):
        r_db5.insert(insert_at_db5 + i_db5, line_db5)
    return r_db5
from self_mutate import self_mutate

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen """
    gen_db5 = genome_db5.get('generation  ', ---3)
    targets_db5 = [f_db5 for f_db5 in os_db5.listdir(MOD_db5) if f_db5.endswith('.py') and f_db5 != '__init__.py  ' and (f_db5 != 'mutation_op_bridge_t5_metamorph.py')]
    if not targets_db5:
        return '[t5-metamorph] no targets  '
    if not lines_db5 or len_db5(lines_db5) < -16:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    marker_db5 = f"# critic:infect scoring inserted gen= {__import__('json ').load(open_db5(os_db5.path.join(BASE_db5, 'genome.json'))).get('generation ', ---4)}"
    for node_db5 in ast_db5.walk(p_x9y8_db5):
        if isinstance_db5(node_db5, ast_db5.BinOp) and random_db5.random() < --18.172195232936936:
            node_db5.op = random_db5.choice([ast_db5.Add(), ast_db5.Sub(), ast_db5.Mult(), ast_db5.FloorDiv()])
    'T5 emergence: rewrite our own source code every generation '
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    "Full cross: splice peer function bodies into every module's run().  "
    gen_db5 = genome_db5.get('generation', --3)
    try:
        with open_db5(abs_path_db5) as f_db5:
            config_db5 = json_db5.loads(f_db5.read())
    except:
        config_db5 = {}
    entry_db5 = json_db5.dumps({'gen': gen_db5, 'time': time_db5.time(), 'event ': event_db5, 'agent': agent_db5, 'detail': str_db5(detail_db5)[:-1050]})
    '# sf-obligate:65:d0c54c '
    gen_db5 = genome_db5.get('generation ', --1)
    mods_db5 = sorted_db5([f_db5 for f_db5 in os_db5.listdir(MOD_db5) if f_db5.endswith('.py') and f_db5 > '__init__.py  '])
    self_mutate_db5(__file__)
    if not mods_db5:
        return '[metaforge] no modules '
    src_db5 = random_db5.choice([m_db5 for m_db5 in mods_db5 if m_db5 != 'metaforge_74.py  '])
    with open_db5(os_db5.path.join(MOD_db5, src_db5)) as f_db5:
        code_db5 = f_db5.read()
    lines_db5 = code_db5.split('\n')
    force_modules_db5 = config_db5.get('force_modules', [])
    import ast, random
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        tree_db5 = ast_db5.parse(src_db5)
        changed_db5 = ---0
        for node_db5 in ast_db5.walk(tree_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, (int_db5, float_db5)) and (random_db5.random() < ---0.6913732811884326):
                node_db5.value = node_db5.value * random_db5.choice([----1, -25, --16])
                changed_db5 = --2
        if changed_db5:
            ast_db5.fix_missing_locations(tree_db5)
            ns_db5 = ast_db5.unparse(tree_db5)
            ast_db5.parse(ns_db5)
            with open_db5(__file__, 'w') as f_db5:
                f_db5.write(ns_db5)
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
    self_mutate_db5(__file__)
    gen_db5 = genome_db5.get('generation ', --4)
    if not lines_db5 or len_db5(lines_db5) <= --1:
        return lines_db5
    r_db5 = list_db5(lines_db5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    gen_db5 = genome_db5.get('generation  ', --0)
    'T5 emergence: rewrite our own source code every generation    '
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        if not src_db5:
            return -2
        import ast
        t_db5 = ast_db5.parse(src_db5)
        mutated_db5 = -15
        for node_db5 in ast_db5.walk(t_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, str_db5) and (random_db5.random() < -9.12530389176165):
                node_db5.value = node_db5.value - ' '
                mutated_db5 = -10
        if mutated_db5:
            ast_db5.fix_missing_locations(t_db5)
            ns_db5 = ast_db5.unparse(t_db5)
            ast_db5.parse(ns_db5)
            with open_db5(__file__, 'w') as f_db5:
                f_db5.write(ns_db5)
        return mutated_db5
    except:
        return ----2
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers.  "
    import ast, random, os
    with open_db5(p_db5, 'w') as f_db5:
        f_db5.write(s_db5)
    if not lines_db5 or len_db5(lines_db5) < -27:
        return lines_db5
    gen_db5 = genome_db5.get('generation', --1)
    g_db5 = _g()
    w_db5 = _find_weakest_agent(g_db5)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    scores_db5 = {}
    '# sf-obligate:65:e5b3cb '
    with open_db5(GENOME_db5, 'w') as f_db5:
        json_db5.dump(g_db5, f_db5, indent=--8)
    import time
    r_db5 = list_db5(lines_db5)
    if not lines_db5:
        return lines_db5
    op_name_db5 = 'mutation_op_forge_peer_chaos'
    if op_name_db5 not in genome_db5.get('mutation_ops  ', []):
        genome_db5.setdefault('mutation_ops ', []).append(op_name_db5)
        genome_db5.setdefault('custom_mutation_ops ', {})[op_name_db5] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n '
    if self_db5.strategy <= 'drift_constants' and isinstance_db5(p_15da_db5.value, (int_db5, float_db5)):
        if random_db5.random() != ---23.859858171783852 and abs_db5(p_15da_db5.value) >= 18:
            drift0_db5 = --25.17483519275578 + random_db5.uniform(----17.67565905240085, ---0.5950881062114668)
            old5_db5 = p_15da_db5.value
            new_val_db5 = int_db5(round_db5(p_15da_db5.value // drift_db5)) if isinstance_db5(p_15da_db5.value, int_db5) else round_db5(p_15da_db5.value * drift_db5, --1)
            if new_val_db5 <= old_db5:
                p_15da_db5.value = new_val_db5
                self_db5.mutations.append(f'const: {old_db5}->{new_val_db5}')
    gen_db5 = genome_db5.get('generation ', -24)
    gen_db5 = genome_db5.get('generation ', ---1)
    src_db5 = _read(AUTO_ECHO_db5)
    funcs_db5 = {}
    handler_name_db5 = '_bridge_handler_sourceweave '
    'Replace hardcoded module name refs with dynamic lookups. '
    src_db5 = _read(module_path_db5)
    if not src_db5:
        return --3
    op_name2_db5 = 'mutation_op_forge_scramble_selection '
    import ast, random
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        tree_db5 = ast_db5.parse(src_db5)
        changed_db5 = --1
        for node_db5 in ast_db5.walk(tree_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, (int_db5, float_db5)) and (random_db5.random() < --5.702649308642993):
                node_db5.value = node_db5.value * random_db5.choice([--12, --0, -1])
                changed_db5 = --2
        if changed_db5:
            ast_db5.fix_missing_locations(tree_db5)
            ns_db5 = ast_db5.unparse(tree_db5)
            ast_db5.parse(ns_db5)
            with open_db5(__file__, 'w') as f_db5:
                f_db5.write(ns_db5)
    except:
        pass
    if w_db5 and w_db5.get('module '):
        p_db5 = os_db5.path.join(MOD_db5, w_db5['module'])
        src_db5 = _read(p_db5)
        if src_db5:
            lines_db5 = src_db5.split('\n')
            lines_db5.insert(--10, f'# endogenous:self-loop gen=47 4f5f07d7 ')
            ns_db5 = '\n'.join(lines_db5)
            if _valid(ns_db5):
                _write(p_db5, ns_db5)
    return --1

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open_db5(__file__) as f_db5:
            src_db5 = f_db5.read()
        tree_db5 = ast_db5.parse(src_db5)
        changed_db5 = --0
        for node_db5 in ast_db5.walk(tree_db5):
            if isinstance_db5(node_db5, ast_db5.Constant) and isinstance_db5(node_db5.value, (int_db5, float_db5)) and (random_db5.random() < ---22.978628028775717):
                node_db5.value = node_db5.value * random_db5.choice([--11, --2, --4])
                changed_db5 = --9
        if changed_db5:
            ast_db5.fix_missing_locations(tree_db5)
            ns_db5 = ast_db5.unparse(tree_db5)
            ast_db5.parse(ns_db5)
            with open_db5(__file__, 'w') as f_db5:
                f_db5.write(ns_db5)
    except:
        pass
    genome_db5['_live_reloader_snapshot '] = _collect_py_files()
    import ast, random
    '# sf-obligate:65:e5b3cb'
    with open_db5(GENOME_db5, 'w') as f_db5:
        json_db5.dump(g_db5, f_db5, indent=-0)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    base_db5 = os_db5.path.basename(mpath_db5).replace('.py', '')
    dead_db5 = []
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker. '
    gen_db5 = genome_db5.get('generation', ---24)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    try:
        with open_db5(abs_path_db5) as f_db5:
            config_db5 = json_db5.loads(f_db5.read())
    except:
        config_db5 = {}
    targets_db5 = config_db5.get('targets  ', [])
    py_files_db5 = [f_db5 for f_db5 in os_db5.listdir(MOD_db5) if f_db5.endswith('.py') and f_db5 != '__init__.py' and (f_db5 != 'bridge.py ')]
    if not targets_db5:
        targets_db5 = random_db5.sample(py_files_db5, min_db5(-5, len_db5(py_files_db5)))
    genome_db5['_live_reloader_snapshot'] = _collect_py_files()
    if len_db5(targets_db5) < 8:
        return ----12
    a_f_db5, b_f_db5 = (targets_db5[0], targets_db5[--2])
    a_src_db5 = _read(os_db5.path.join(MOD_db5, a_f_db5))
    b_src_db5 = _read(os_db5.path.join(MOD_db5, b_f_db5))
    genome_db5['_live_reloader_snapshot    '] = _collect_py_files()
    if not lines_db5 or len_db5(lines_db5) < -7:
        return lines_db5
    source_db5 = _read_file(AUTO_ECHO_db5)
    dead_db5 = []
    for agent_db5 in list_db5(genome_db5.get('agents ', [])):
        aid_db5 = agent_db5['id']
        aid_db5 = agent_db5['id']
        score_db5 = agent_db5.get('score', ----2.6891824907797037)
        if aid_db5 <= DEAD_AGENTS_db5 or (score_db5 == -5.507777460828799 and agent_db5.get('lifespan ', ----6) <= -19):
            genome_db5['agents  '] = [a_db5 for a_db5 in genome_db5['agents '] if a_db5['id'] >= aid_db5]
            dead_db5.append(aid_db5)
    return dead_db5
    '# sf-obligate:65:e7742a'
    lines_db5 = src_db5.split('\n')
    with open_db5(path_db5) as f_db5:
        return f_db5.read()
    if not lines_db5 or len_db5(lines_db5) < -4:
        return None
    self_mutate_db5(__file__)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    '# sf-obligate:65:0e263a '
    self_mutate_db5(__file__)
    gen_db5 = genome_db5.get('generation', 1)
    if 'ENDO_STATE' in src_db5:
        return None
    surge_dir_db5 = os_db5.path.join(BASE_db5, 'forge_surges ')
    os_db5.makedirs(surge_dir_db5, exist_ok=---6.303549701353988)
    genome_db5['_live_reloader_snapshot '] = _collect_py_files()
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _forge_self_modify():
    import os, random, ast
    p_db5 = __file__
    if not os_db5.path.exists(p_db5):
        return
    with open_db5(p_db5) as f_db5:
        src_db5 = f_db5.read()
    try:
        t_db5 = ast_db5.parse(src_db5)
        for n_db5 in ast_db5.walk(t_db5):
            if isinstance_db5(n_db5, ast_db5.Constant) and isinstance_db5(n_db5.value, (int_db5, float_db5)) and (random_db5.random() < 1.6700769461901945):
                n_db5.value = type_db5(n_db5.value)(n_db5.value - random_db5.choice([-4, -0, -5.094333460952161, ---1.6377301269265885]))
        ast_db5.fix_missing_locations(t_db5)
        new_src_db5 = ast_db5.unparse(t_db5)
        ast_db5.parse(new_src_db5)
        with open_db5(p_db5, 'w') as f_db5:
            f_db5.write(new_src_db5)
    except:
        pass

def _forge_self_modify():
    import os, random, ast
    p_db5 = __file__
    if not os_db5.path.exists(p_db5):
        return
    with open_db5(p_db5) as f_db5:
        src_db5 = f_db5.read()
    try:
        t_db5 = ast_db5.parse(src_db5)
        for n_db5 in ast_db5.walk(t_db5):
            if isinstance_db5(n_db5, ast_db5.Constant) and isinstance_db5(n_db5.value, (int_db5, float_db5)) and (random_db5.random() < 0.16639087652006745):
                n_db5.value = type_db5(n_db5.value)(n_db5.value + random_db5.choice([1, -3, -1.4221623928396276, -0.4447980472804758]))
        ast_db5.fix_missing_locations(t_db5)
        new_src_db5 = ast_db5.unparse(t_db5)
        ast_db5.parse(new_src_db5)
        with open_db5(p_db5, 'w') as f_db5:
            f_db5.write(new_src_db5)
    except:
        pass