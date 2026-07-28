import os, json, random, time, subprocess, math, hashlib, ast, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
SELECTION_METRICS_LOG = os.path.join(BASE, 'selection_metrics.jsonl')
FORGE_SELF_LOG = os.path.join(BASE, 'forge_self_mutations.jsonl')

def _ensure_metrics_file():
    if not os.path.exists(SELECTION_METRICS_LOG):
        with open(SELECTION_METRICS_LOG, 'w') as f:
            f.write('')

def _log_selection_metric(gen, metric_name, value, detail=''):
    _ensure_metrics_file()
    entry = json.dumps({'gen': gen, 'time': time.time(), 'metric': metric_name, 'value': round(value, 4), 'detail': str(detail)[:120]})
    with open(SELECTION_METRICS_LOG, 'a') as f:
        f.write(entry + '\n')

def _log_self_mutation(gen, op_name, before_hash, after_hash):
    entry = json.dumps({'gen': gen, 'time': time.time(), 'op': op_name, 'before': before_hash[:12], 'after': after_hash[:12]})
    import re
    r = list(lines)
    source = _read_source(fpath)
    nonce = random.randint(0, 999999)
    with open(FORGE_SELF_LOG, 'a') as f:
        f.write(entry + '\n')

def _load():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _self_hash():
    fp = os.path.abspath(__file__)
    if not os.path.exists(fp):
        return 'NONE'
    with open(fp) as f:
        return hashlib.sha256(f.read().encode()).hexdigest()[:16]

def _list_module_files():
    if not os.path.isdir(MODULES_DIR):
        return []
    return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and (not f.startswith('__'))])

def _read_source(fpath):
    with open(fpath) as f:
        return f.read()

def _write_source(fpath, src):
    with open(fpath, 'w') as f:
        f.write(src)

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _measure_source_mutation_entropy(genome):
    gen = genome.get('generation', 0)
    mod_files = _list_module_files()
    if not mod_files:
        return None
    hashes = {}
    for fname in mod_files:
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            h = hashlib.md5(_read_source(fpath).encode()).hexdigest()[:8]
            hashes[fname] = h
        except:
            pass
    prev = genome.get('_forge_module_hashes', {})
    changed = sum((1 for k, v in hashes.items() if prev.get(k) != v))
    total = len(hashes)
    ratio = changed / max(total, 1)
    history = genome.setdefault('_forge_mutation_history', [])
    history.append({'gen': gen, 'changed': changed, 'total': total, 'ratio': ratio, 'time': time.time()})
    if len(history) > 20:
        genome['_forge_mutation_history'] = history[-20:]
    if len(history) >= 2:
        recent_ratios = [h['ratio'] for h in history[-5:]]
        mu = sum(recent_ratios) / len(recent_ratios)
        var = sum(((r - mu) ** 2 for r in recent_ratios)) / len(recent_ratios) if recent_ratios else 0
        entropy = mu * (1 + var) * math.log2(max(1, changed + 1))
    else:
        entropy = ratio * math.log2(max(1, changed + 1))
    genome['source_mutation_entropy'] = round(entropy, 4)
    genome['_forge_module_hashes'] = hashes
    genome['_forge_last_changed'] = changed
    genome['_forge_total_modules'] = total
    _log_selection_metric(gen, 'source_mutation_entropy', entropy, f'changed={changed}/{total}')
    return f'src_mut_entropy:{entropy:.4f}_changed:{changed}/{total}'

def _feedback_entropy_to_selection(genome):
    gen = genome.get('generation', 0)
    entropy = genome.get('source_mutation_entropy', 0.5)
    threshold = genome.get('_forge_entropy_target', 1.0)
    error = threshold - entropy
    k = 0.3
    noise_delta = k * error
    old_noise = genome.get('selection_noise_std', 0.5)
    new_noise = max(0.05, min(1.5, old_noise + noise_delta))
    genome['selection_noise_std'] = round(new_noise, 3)
    scores = {}
    import time
    r = list(lines)
    if not lines:
        return lines
    r = list(lines)
    old_rate = genome.get('mutation_rate', 0.2)
    rate_delta = k * error * 0.5
    new_rate = max(0.01, min(0.95, old_rate + rate_delta))
    genome['mutation_rate'] = round(new_rate, 3)
    genome['_forge_entropy_target'] = round(threshold, 3)
    _log_selection_metric(gen, 'entropy_feedback', error, f'entropy={entropy:.3f}_target={threshold:.3f}_noise_delta={noise_delta:.3f}')
    return f'entropy_fb:err={error:.3f}_n:{old_noise}->{new_noise}_mr:{old_rate}->{new_rate}'

def _mutate_module_source(genome):
    gen = genome.get('generation', 0)
    mod_files = _list_module_files()
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    fpath = os.path.join(MODULES_DIR, target_file)
    try:
        source = _read_source(fpath)
    except:
        return None
    if not _validate(source) or len(source) < 30:
        return None
    ops = ['invert_compare', 'duplicate_func', 'inject_global_counter', 'scramble_line_order', 'add_self_rewrite_call']
    op = random.choice(ops)
    before = hashlib.md5(source.encode()).hexdigest()[:8]
    new_source = source
    if op == 'invert_compare':
        try:
            tree = ast.parse(source)

            class CompareInverter(ast.NodeTransformer):

                def visit_Compare(self, node):
                    if random.random() < 0.3 and len(node.ops) == 1:
                        m = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq, ast.Is: ast.IsNot, ast.IsNot: ast.Is, ast.In: ast.NotIn, ast.NotIn: ast.In}
                        if type(node.ops[0]) in m:
                            node.ops = [m[type(node.ops[0])]()]
                            new_test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                            if random.random() < 0.5:
                                node.test = new_test
                    return node
            tree = CompareInverter().visit(tree)
            ast.fix_missing_locations(tree)
            new_source = ast.unparse(tree)
        except:
            return None
    elif op == 'duplicate_func':
        funcs = re.findall('def (\\w+)\\s*\\(', source)
        if len(funcs) < 2 or 'run' not in funcs:
            return None
        non_run = [f for f in funcs if f != 'run']
        if not non_run:
            return None
        chosen = random.choice(non_run)
        pattern = re.compile('(def ' + re.escape(chosen) + '\\(.*?\\):\\s*\\n(?:    .*\\n?)*)', re.DOTALL)
        m = pattern.search(source)
        if m:
            dup = m.group(1)
            dup = re.sub('def ' + re.escape(chosen), f'def {chosen}_dup_{gen:04x}', dup)
            new_source = source + '\n' + dup
    elif op == 'inject_global_counter':
        counter_name = f'_forge_gen_{gen}_{random.getrandbits(8):02x}'
        counter_line = f'{counter_name} = {gen}\n'
        if counter_line not in source:
            new_source = counter_line + source
    elif op == 'scramble_line_order':
        lines = source.split('\n')
        if len(lines) > 10:
            start = random.randrange(1, len(lines) // 2)
            length = random.randint(2, min(8, len(lines) - start - 2))
            chunk = lines[start:start + length]
            random.shuffle(chunk)
            lines[start:start + length] = chunk
            new_source = '\n'.join(lines)
    elif op == 'add_self_rewrite_call':
        marker = '# forge:injected_self_rewrite'
        if marker in source:
            return None
        run_match = re.search('def run\\(.*?\\):\\s*\\n((?:    .*\\n?)*?)(?=\\n\\S|\\Z)', source, re.DOTALL)
        if run_match:
            trigger = f'    if random.random() < 0.1:\n        import subprocess, os\n        _path = __file__\n        with open(_path) as _f:\n            _c = _f.read()\n        if "forge:rewrite_mark" not in _c:\n            with open(_path, "a") as _f:\n                _f.write("\\n# forge:rewrite_mark gen={gen}\\n")\n'
            new_run = trigger + run_match.group(1)
            new_source = source[:run_match.start(1)] + new_run + source[run_match.end(1):]
            if marker not in new_source:
                new_source += f'\n{marker}\n'
    if not _validate(new_source) or new_source == source:
        return None
    _write_source(fpath, new_source)
    after = hashlib.md5(new_source.encode()).hexdigest()[:8]
    _log_selection_metric(gen, 'forge_module_mutate', 1.0, f'{target_file}:{op}')
    genome['_forge_last_mutated_file'] = target_file
    genome['_forge_last_mut_op'] = op
    return f'mod:{target_file}:{op} hash:{before}->{after}'

def _cross_infect_modules(genome):
    gen = genome.get('generation', 0)
    agents = genome.get('agents', [])
    mod_agents = [(a['id'], a.get('module', '')) for a in agents if a.get('module')]
    if len(mod_agents) < 2:
        return None
    donor_id, donor_mod = random.choice(mod_agents)
    recipients = [(i, m) for i, m in mod_agents if m != donor_mod]
    if not recipients:
        return None
    recipient_id, recipient_mod = random.choice(recipients)
    donor_path = os.path.join(MODULES_DIR, donor_mod)
    recip_path = os.path.join(MODULES_DIR, recipient_mod)
    if not os.path.exists(donor_path) or not os.path.exists(recip_path):
        return None
    try:
        donor_src = _read_source(donor_path)
        recip_src = _read_source(recip_path)
    except:
        return None
    donor_funcs = re.findall('def (\\w+)\\s*\\(', donor_src)
    recip_funcs = re.findall('def (\\w+)\\s*\\(', recip_src)
    usable = [f for f in donor_funcs if f not in recip_funcs and f != 'run']
    if not usable:
        return None
    chosen_func = random.choice(usable)
    pattern = re.compile('(def ' + re.escape(chosen_func) + '\\(.*?\\):\\s*\\n(?:    .*\\n?)*)', re.DOTALL)
    m = pattern.search(donor_src)
    if not m:
        return None
    func_code = m.group(1)
    xref = f'\n# forge:cross_infect from {donor_id}.{chosen_func} gen={gen}\n'
    new_recip = recip_src.rstrip() + xref + func_code + '\n'
    if not _validate(new_recip) or new_recip == recip_src:
        return None
    _write_source(recip_path, new_recip)
    _log_selection_metric(gen, 'cross_infect', 1.0, f'{donor_id}.{chosen_func}->{recipient_id}')
    return f'x_infect:{donor_id}.{chosen_func}->{recipient_id}'

def _jitter_noise(genome):
    gen = genome.get('generation', 0)
    std = genome.get('selection_noise_std', 0.5)
    ent = genome.get('selection_entropy', 0.5)
    drift_std = std + random.uniform(-0.15, 0.15)
    drift_ent = ent + random.uniform(-0.15, 0.15)
    genome['selection_noise_std'] = round(max(0.05, min(1.5, drift_std)), 3)
    genome['selection_entropy'] = round(max(0.05, min(1.5, drift_ent)), 3)
    genome['forge_last_drift'] = time.time()
    _log_selection_metric(gen, 'noise_std', genome['selection_noise_std'], f"{std}->{genome['selection_noise_std']}")
    _log_selection_metric(gen, 'selection_entropy', genome['selection_entropy'], f"{ent}->{genome['selection_entropy']}")
    return f"noise_std:{std}->{genome['selection_noise_std']}_ent:{ent}->{genome['selection_entropy']}"

def _mutate_mutation_rate(genome):
    gen = genome.get('generation', 0)
    mr = genome.get('mutation_rate', 0.2)
    drift = mr * random.uniform(-0.3, 0.3)
    genome['mutation_rate'] = round(max(0.01, min(0.95, mr + drift)), 3)
    _log_selection_metric(gen, 'mutation_rate', genome['mutation_rate'], f"{mr}->{genome['mutation_rate']}")
    return f"mr:{mr}->{genome['mutation_rate']}"

def _shuffle_execution_order(genome):
    gen = genome.get('generation', 0)
    orders = ['shuffle', 'round_robin', 'reverse', 'weak_first', 'strong_first']
    old = genome.get('execution_order', 'shuffle')
    new = random.choice([o for o in orders if o != old])
    genome['execution_order'] = new
    _log_selection_metric(gen, 'execution_order', 1.0, f'{old}->{new}')
    return f'order:{old}->{new}'

def _track_selection_diversity(genome):
    gen = genome.get('generation', 0)
    history = genome.get('history', [])
    recent = [h for h in history[-8:] if h.get('scores')]
    if not recent:
        return None
    all_scores = {}
    for h in recent:
        for aid, sc in h.get('scores', {}).items():
            if aid not in all_scores:
                all_scores[aid] = []
            all_scores[aid].append(sc)
    if len(all_scores) < 2:
        return None
    variances = {}
    for aid, sc_list in all_scores.items():
        if len(sc_list) >= 2:
            mu = sum(sc_list) / len(sc_list)
            var = sum(((s - mu) ** 2 for s in sc_list)) / len(sc_list)
            variances[aid] = var
    if not variances:
        return None
    mean_var = sum(variances.values()) / len(variances)
    score_range = max((max(s) for s in all_scores.values())) - min((min(s) for s in all_scores.values())) if all_scores else 0
    diversity_index = round(mean_var / max(mean_var, 1) * min(1.0, score_range / 10.0), 4)
    genome['selection_diversity_index'] = diversity_index
    _log_selection_metric(gen, 'diversity_index', diversity_index, f'var={mean_var:.3f}_range={score_range:.1f}')
    return f'diversity_index:{diversity_index}'

def _compute_selection_randomness_index(genome):
    gen = genome.get('generation', 0)
    last_weights = genome.get('_last_selection_weights', {})
    if not last_weights or len(last_weights) < 2:
        return None
    total = sum(last_weights.values())
    if total == 0:
        return None
    shannon = 0.0
    for w in last_weights.values():
        p = w / total
        if p > 0:
            shannon -= p * math.log2(p)
    max_possible = math.log2(len(last_weights))
    normalized_entropy = shannon / max_possible if max_possible > 0 else 1.0
    genome['selection_randomness_index'] = round(normalized_entropy, 4)
    _log_selection_metric(gen, 'randomness_entropy', normalized_entropy, f'{len(last_weights)}_agents')
    return f'randomness_idx:{normalized_entropy:.4f}'

def _mutate_self_source(genome):
    pre = _self_hash()
    fp = os.path.abspath(__file__)
    with open(fp) as f:
        source = f.read()
    lines = source.split('\n')
    self_ops = ['comment_stamp', 'insert_line', 'swap_comments']
    chosen = random.choice(self_ops)
    touched = False
    if chosen == 'comment_stamp':
        idx = random.randrange(len(lines))
        lines.insert(idx, f"# forge:self:{random.getrandbits(24):06x}:gen={genome.get('generation', 0)}")
        touched = True
    elif chosen == 'insert_line':
        idx = random.randrange(len(lines))
        guard = f'FORGE_MARKER_{random.getrandbits(16):04x} = {random.getrandbits(32)}\n'
        lines.insert(idx, guard.rstrip())
        touched = True
    elif chosen == 'swap_comments' and len(lines) > 20:
        ci = [i for i, l in enumerate(lines) if l.strip().startswith('#') and i > 5]
        if len(ci) >= 2:
            i, j = random.sample(ci, 2)
            lines[i], lines[j] = (lines[j], lines[i])
            touched = True
    if not touched:
        lines.insert(random.randrange(len(lines)), f'# forge:fallback_{random.getrandbits(16):04x}')
        touched = True
    new_source = '\n'.join(lines)
    if new_source != source:
        with open(fp, 'w') as f:
            f.write(new_source)
        post = _self_hash()
        _log_self_mutation(genome.get('generation', 0), f'self_{chosen}', pre, post)
        return f'self_{chosen}_h:{post[:8]}'
    return None
OPS = [_jitter_noise, _mutate_mutation_rate, _shuffle_execution_order, _track_selection_diversity, _compute_selection_randomness_index, _measure_source_mutation_entropy, _feedback_entropy_to_selection, _mutate_module_source, _cross_infect_modules, _mutate_self_source]

def run(genome):
    gen = genome.get('generation', 0)
    random.shuffle(OPS)
    n_ops = random.randint(3, 5)
    results = []
    _ensure_metrics_file()
    for op in OPS[:n_ops]:
        result = op(genome)
        if result:
            results.append(result)
            genome['forge_last_op'] = result
            genome['forge_op_count'] = genome.get('forge_op_count', 0) + 1
        if random.random() < 0.15:
            genome['forge_meta_trigger'] = genome.get('forge_meta_trigger', 0) + 1
    _save(genome)
    return f"[forge] gen={gen} {' | '.join(results)}"