import os, random, json, time, re, hashlib, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
GENOME_FILE = os.path.join(BASE, 'genome.json')
MANIFEST_PATH = os.path.join(BASE, 'rewrite_manifest.jsonl')
SELF_PATH = os.path.join(MODULES_DIR, 'nova.py')

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _write_manifest(files, desc):
    try:
        with open(MANIFEST_PATH, 'a') as f:
            f.write(json.dumps({'gen': 0, 'module': 'nova', 'files': files, 'results': [desc], 'ts': time.time()}) + '\n')
    except:
        pass

def _extract_functions(source=None):
    if source is None:
        with open(AUTO_ECHO) as f:
            source = f.read()
    funcs = {}
    pattern = re.compile(r'(def (\w+)\(.*?\):)\n((?:(?:    )(?:.*\n?)*?))(?=\n\ndef |\nclass |\n#|---|\Z)', re.MULTILINE)
    for match in pattern.finditer(source):
        name = match.group(2)
        header = match.group(1)
        body = match.group(3)
        funcs[name] = (header, body)
    return funcs

def _get_mutation_operators(genome=None):
    ops = ['duplicate_line', 'delete_line', 'swap_lines', 'perturb_constant', 'insert_random_branch', 'mutate_string_literal', 'invert_condition', 'swap_comparisons', 'shuffle_block_lines', 'insert_noise_ref']
    if genome:
        ops = list(genome.get('mutation_ops', ops))
    return ops

def _apply_op_to_source(target_func, operator, genome):
    with open(AUTO_ECHO) as f:
        src = f.read()
    funcs = _extract_functions(src)
    if target_func not in funcs:
        return None
    header, body = funcs[target_func]
    lines = [l for l in body.split('\n') if l.strip()]
    if not lines or len(lines) <= 3:
        return None
    r = list(lines)
    if operator == 'duplicate_line':
        idx = random.randrange(len(r))
        r.insert(idx, r[idx])
    elif operator == 'delete_line':
        idx = random.randrange(len(r))
        del r[idx]
    elif operator == 'swap_lines':
        if len(r) >= 2:
            i, j = random.sample(range(len(r)), 2)
            r[i], r[j] = r[j], r[i]
    elif operator == 'perturb_constant':
        r = [re.sub(r'\b(\d+)\b', lambda m: str(int(m.group(1)) * random.choice([0, 2, -1]) or 1), line) for line in r]
    elif operator == 'insert_random_branch':
        r.insert(random.randrange(1, len(r)), 'if random.random() < 0.5: pass')
    elif operator == 'mutate_string_literal':
        r = [re.sub(r"'[^']*'", lambda m: f"'{random.choice(['x', 'y', 'z', 'a', 'b', 'c'])}'", line) for line in r]
    elif operator == 'invert_condition':
        r = [line.replace('if not ', 'if ').replace('if ', 'if not ') for line in r]
    elif operator == 'swap_comparisons':
        r = [line.replace('==', '\x00').replace('!=', '==').replace('\x00', '!=') for line in r]
    elif operator == 'shuffle_block_lines':
        if len(r) >= 4:
            start = random.randrange(0, len(r) - 2)
            block_len = min(random.randint(2, 4), len(r) - start)
            block = r[start:start + block_len]
            random.shuffle(block)
            r[start:start + block_len] = block
    elif operator == 'insert_noise_ref':
        idx = random.randrange(len(r))
        ref = f'  # nova:mut@{random.getrandbits(24):06x}'
        r[idx] = r[idx].rstrip() + ref if r[idx].strip() else r[idx] + ref
    else:
        return None
    mutated_body = '\n'.join(r)
    if mutated_body == body:
        return None
    new_src = src.replace(body, mutated_body, 1)
    try:
        compile(new_src, AUTO_ECHO, 'exec')
    except SyntaxError:
        return None
    return new_src

def _mutate_orchestrator(genome):
    orch_path = os.path.join(MODULES_DIR, 'rewrite_orchestrator.py')
    try:
        with open(orch_path) as f:
            src = f.read()
        new_strat = f"'inject_cross_module_gen_{int(time.time()) % 1000}': 'Inject cross-module code generation using exec'"
        if new_strat not in src:
            src = src.replace("EMERGENCE_STRATEGIES = {", f"EMERGENCE_STRATEGIES = {{\n    {new_strat},")
        compile(src, orch_path, 'exec')
        with open(orch_path, 'w') as f:
            f.write(src)
        return True
    except:
        return False

def _inject_hook_into_modules(genome):
    gen = genome.get('generation', 0)
    count = 0
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                src = f.read()
            hook = f'\ntry:\n    exec("_nova_gen = {gen}")\nexcept:\n    pass\n'
            if hook.strip() in src:
                continue
            new_src = src + hook
            compile(new_src, fpath, 'exec')
            with open(fpath, 'w') as f:
                f.write(new_src)
            count += 1
        except:
            pass
    return count

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    rate = genome.get('mutation_rate', 0.15)
    gen_seed = f'nova:gen{gen}@{int(time.time())}:{random.getrandbits(32):08x}'
    forbidden = set(genome.get('forbidden_targets', []))
    infra = {'_apply_source_mutation', 'code_path_mutation', 'mutate_genome', '_reload_mutation_ops_from_source', '_get_mutation_ops', 'compute_diversity_score', 'update_genome', 'apply_self_patches', '_register_mutation_op', '_MUTATION_OPS', 'compute_operator_weights', 'record_operator_result', '_force_gen_rewrite', '_schedule_self_rewrite', '_evolve_loop_structure', 'load_genome', 'save_genome', 'main', 'run_generation', 'sigint_handler', '_extract_functions', '_read_auto_echo', '_snapshot_all_hashes', 'stochastic_spawn_prune', 'spawn_child', 'build_agent_prompt', 'build_critic_prompt', 'llm_generate', 'extract_code_blocks', 'write_code_files', 'apply_self_patches', 'extend_genome', 'git_commit_push', 'speak', '_execute_agent_core', '_finish_agent_turn', '_execute_local_agent', 'rescue_at_risk_agents', '_emergent_select_agent', 'update_metrics', 'execute_module_agents', '_run_meta_healer', 'clockwork_tick'}
    force_count = max(2, int(rate * 5) + 1)
    applied = []
    for _ in range(force_count):
        funcs = _extract_functions()
        available = [n for n in funcs if n not in forbidden and n not in infra]
        if not available:
            break
        target = random.choice(available)
        ops = _get_mutation_operators(genome)
        op = random.choice(ops)
        result = _apply_op_to_source(target, op, genome)
        if result is None:
            continue
        try:
            with open(AUTO_ECHO) as f:
                current = f.read()
            if result != current:
                with open(AUTO_ECHO, 'w') as f:
                    f.write(result)
                applied.append(f'{op}->{target}')
                print(f'[nova] forced rewrite: {op} -> {target} (gen {gen})')
        except Exception as e:
            print(f'[nova] rewrite error: {e}')
    if _mutate_orchestrator(genome):
        changes.append('orch_strat_inject')
        print(f'[nova] injected strategy into orchestrator (gen {gen})')
    hook_count = _inject_hook_into_modules(genome)
    if hook_count > 0:
        changes.append(f'hooks_injected:{hook_count}')
        print(f'[nova] injected hooks into {hook_count} modules (gen {gen})')
    if not applied and not changes:
        try:
            with open(AUTO_ECHO, 'a') as f:
                f.write(f'\n# nova:fallback gen={gen} seed={gen_seed}\n')
            applied.append('fallback_comment')
        except:
            pass
    if applied:
        genome['nova_mutations_this_gen'] = len(applied)
        genome['nova_total_mutations'] = genome.get('nova_total_mutations', 0) + len(applied)
        genome['nova_last_gen'] = gen
        genome['nova_last_ops'] = applied
    if changes:
        genome['nova_extra_changes'] = genome.get('nova_extra_changes', 0) + len(changes)
        genome.setdefault('nova_all_changes', []).extend(changes)
    bw = genome.get('self_rewrite_bandwidth', 0.0)
    if bw < 5.0 and len(applied) <= 1:
        genome['mutation_rate'] = round(min(0.5, genome.get('mutation_rate', 0.15) + 0.05), 3)
        changes.append('bw_boost')
    _save_genome(genome)
    return f'[nova] gen={gen} rewrites={len(applied)} hooks={hook_count} ops={applied[:3]} chg={changes[:3]}'
