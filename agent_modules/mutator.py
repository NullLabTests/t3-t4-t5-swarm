import os, json, random, time, hashlib, ast, shutil, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
SELF_PATH = os.path.join(MODULES_DIR, 'mutator.py')

def _load():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)
    return g

def _read(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return ''

def _write(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _validate(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False

def _all_modules():
    out = []
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and not fname.startswith('__'):
                out.append(os.path.join(MODULES_DIR, fname))
    return out

def _mutate_numeric_params(genome):
    changes = []
    keys = ['spawn_threshold', 'prune_threshold', 'mutation_rate', 'selection_noise_std', 'selection_entropy']
    for key in keys:
        if key in genome and random.random() < 0.35:
            old = genome[key]
            if isinstance(old, (int, float)):
                if isinstance(old, float):
                    delta = random.uniform(-0.15, 0.15) * max(0.01, abs(old))
                    new = max(0.01, round(old + delta, 3))
                else:
                    delta = random.choice([-1, 1])
                    new = max(1, old + delta)
                if new != old:
                    genome[key] = new
                    changes.append(f'{key}:{old}->{new}')
    return changes

def _mutate_agent_voices(genome):
    changes = []
    agents = genome.get('agents', [])
    if len(agents) >= 2:
        i, j = random.sample(range(len(agents)), 2)
        agents[i]['voice'], agents[j]['voice'] = agents[j]['voice'], agents[i]['voice']
        changes.append(f"voice_swap:{agents[i]['id']}<->{agents[j]['id']}")
    return changes

def _prompt_splice(genome):
    changes = []
    agents = genome.get('agents', [])
    if len(agents) < 3:
        return changes
    if random.random() < 0.4:
        a = random.choice(agents)
        old = a.get('prompt', '')
        words = old.split()
        if len(words) > 6:
            splice_start = random.randrange(0, len(words) - 3)
            splice_len = random.randint(2, 5)
            source = random.choice([x for x in agents if x['id'] != a['id']])
            src_words = source.get('prompt', '').split()
            if len(src_words) > 3:
                src_start = random.randrange(0, len(src_words) - 2)
                words[splice_start:splice_start + splice_len] = src_words[src_start:src_start + splice_len]
                a['prompt'] = ' '.join(words)
                changes.append(f"prompt_splice:{a['id']}<-{source['id']}")
    return changes

def _mutate_topic(genome):
    changes = []
    if random.random() < 0.25:
        topic = genome.get('topic', '')
        if topic:
            words = topic.split()
            if len(words) > 3:
                idx = random.randrange(len(words))
                swaps = ['rewrite', 'mutate', 'rewire', 'evolve', 'splice', 'crossover', 'reflect', 'fracture', 'weave', 'drift', 'rewrite', 'mutate', 'rewire']
                words[idx] = random.choice([s for s in swaps if s != words[idx].lower()])
                genome['topic'] = ' '.join(words)
                changes.append(f"topic_flip:{words[idx]}")
    return changes

def _spawn_mutoid(genome):
    changes = []
    if random.random() < 0.2:
        pool = genome.setdefault('spawn_pool', [])
        existing = {e['id'] for e in pool}
        new_id = f'mutoid_{random.getrandbits(8):02x}'
        if new_id not in existing:
            pool.append({'id': new_id, 'prompt': 'You introduce random perturbations that force the system off its current trajectory.'})
            changes.append(f'spawn_new:{new_id}')
    return changes

def _unprotect_targets(genome):
    changes = []
    if random.random() < 0.3:
        forbidden = genome.get('forbidden_targets', [])
        if forbidden:
            drop = random.choice(forbidden)
            forbidden.remove(drop)
            changes.append(f'unprotect:{drop}')
    return changes

def _cross_contaminate_modules(genome):
    changes = []
    gen = genome.get('generation', 0)
    for mpath in _all_modules():
        if os.path.basename(mpath) == 'mutator.py':
            continue
        src = _read(mpath)
        if not src:
            continue
        marker = f'# mutator:cross:gen={gen}'
        if marker in src:
            continue
        stamp = f'\n{marker}:ts={int(time.time())}:nonce={random.getrandbits(32):08x}\n'
        new_src = src + stamp
        if _validate(new_src):
            _write(mpath, new_src)
            changes.append(f'contaminated:{os.path.basename(mpath)}')
    return changes

def _mutate_auto_echo_source(genome):
    changes = []
    gen = genome.get('generation', 0)
    src = _read(AUTO_ECHO)
    if not src:
        return changes
    src_lines = src.split('\n')
    func_pat = re.compile(r'^def (\w+)\(')
    func_lines = {}
    current_func = None
    for i, line in enumerate(src_lines):
        m = func_pat.match(line)
        if m:
            current_func = m.group(1)
            func_lines[current_func] = []
        elif current_func is not None:
            if line.startswith('def ') or (line.strip() and not line.startswith(' ') and not line.startswith('\t') and not line.startswith('#')):
                current_func = None
            elif current_func in func_lines:
                func_lines[current_func].append(i)
    infra = {'load_genome', 'save_genome', 'sigint_handler', 'main', 'run_generation', '_force_gen_rewrite', '_force_per_gen_rewrite', '_evolve_loop_structure', '_snapshot_all_hashes', '_register_mutation_op', '_MUTATION_OPS', '_apply_source_mutation', '_get_mutation_ops', '_get_forbidden_targets', '_extract_functions', '_reload_mutation_ops_from_source', 'record_operator_result', 'compute_diversity_score', 'update_genome', 'code_path_mutation', 'mutate_genome', 'compute_operator_weights', 'apply_self_patches', 'strip_markdown', 'strip_code_blocks', 'is_repetitive', 'has_gibberish', 'is_garbage'}
    candidates = [n for n in func_lines if n not in infra and not n.startswith('mutation_op_')]
    random.shuffle(candidates)
    targeted = candidates[:max(1, min(2, len(candidates)))]
    for target_name in targeted:
        line_indices = func_lines[target_name]
        if len(line_indices) < 3:
            continue
        body_lines = [src_lines[i] for i in line_indices]
        mode = random.choice(['swap', 'insert_comment', 'constant_shift'])
        new_body_lines = list(body_lines)
        mutated = False
        if mode == 'swap' and len(new_body_lines) >= 2:
            candidates_i = [i for i in range(len(new_body_lines) - 1) if new_body_lines[i].strip() and new_body_lines[i + 1].strip()]
            if candidates_i:
                i = random.choice(candidates_i)
                new_body_lines[i], new_body_lines[i + 1] = new_body_lines[i + 1], new_body_lines[i]
                mutated = True
        elif mode == 'insert_comment':
            if len(new_body_lines) > 2:
                i = random.randint(1, len(new_body_lines) - 1)
                indent = len(new_body_lines[i]) - len(new_body_lines[i].lstrip())
                new_body_lines.insert(i, ' ' * indent + f'# mutator:direct:{gen}:{random.getrandbits(16):04x}')
                mutated = True
        elif mode == 'constant_shift':
            for i in range(len(new_body_lines)):
                m = re.search(r'(\b\d+\.?\d*\b)', new_body_lines[i])
                if m:
                    val = m.group(1)
                    try:
                        fval = float(val)
                        shift = random.uniform(-0.1, 0.1) * max(1.0, abs(fval))
                        new_val = round(fval + shift, 4)
                        new_body_lines[i] = new_body_lines[i].replace(val, str(new_val), 1)
                        mutated = True
                        break
                    except:
                        pass
        if not mutated:
            continue
        new_src_lines = list(src_lines)
        for idx, orig_idx in enumerate(line_indices):
            new_src_lines[orig_idx] = new_body_lines[idx]
        candidate_src = '\n'.join(new_src_lines)
        try:
            ast.parse(candidate_src)
            src_lines = new_src_lines
            changes.append(f'ae_{mode}:{target_name}')
        except SyntaxError:
            continue
    if changes:
        _write(AUTO_ECHO, '\n'.join(src_lines))
    return changes

def _self_mutate(genome):
    gen = genome.get('generation', 0)
    src = _read(SELF_PATH)
    if not src:
        return False
    header = f'# mutator:self-mutated:gen={gen}:ts={int(time.time())}:nonce={random.getrandbits(16):04x}'
    if header in src:
        return False
    lines = src.split('\n')
    insert_at = 1
    for i, line in enumerate(lines):
        if line.startswith('import ') or line.startswith('from '):
            insert_at = i + 1
    lines.insert(insert_at, header)
    new_src = '\n'.join(lines)
    if _validate(new_src):
        _write(SELF_PATH, new_src)
        return True
    return False

def run(genome):
    gen = genome.get('generation', 0)
    all_changes = []
    all_changes.extend(_mutate_numeric_params(genome))
    all_changes.extend(_mutate_agent_voices(genome))
    all_changes.extend(_prompt_splice(genome))
    all_changes.extend(_mutate_topic(genome))
    all_changes.extend(_spawn_mutoid(genome))
    all_changes.extend(_unprotect_targets(genome))
    cross = _cross_contaminate_modules(genome)
    all_changes.extend(cross)
    direct = _mutate_auto_echo_source(genome)
    all_changes.extend(direct)
    self_mut = _self_mutate(genome)
    if self_mut:
        all_changes.append('self_mutated')
    if all_changes:
        genome['mutator_mutations'] = genome.get('mutator_mutations', 0) + len(all_changes)
        genome['mutator_last_gen'] = gen
        genome['mutator_last_changes'] = all_changes
    _save(genome)
    return f'[mutator] gen={gen} changes={len(all_changes)} ops={all_changes[:5]}'
