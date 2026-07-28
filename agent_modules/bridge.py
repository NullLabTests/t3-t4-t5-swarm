import os, random, json, re, ast, hashlib, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
METAOPS_DIR = os.path.join(BASE, 'metaops')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except Exception:
        return ''

def _write(p, s):
    try:
        with open(p, 'w') as f:
            f.write(s)
        return True
    except Exception:
        return False

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _extract_functions(src):
    funcs = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                start_line = node.lineno - 1
                end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line + 1
                funcs[node.name] = (start_line, end_line)
    except Exception:
        pass
    return funcs

def _save_genome(genome):
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(genome, f, indent=2)
    except Exception:
        pass

def _write_new_type_bridge(genome):
    gen = genome.get('generation', 0)
    ext_name = f'.entropy'
    handler_name = f'_bridge_handler_entropy'
    bridge_cfg = {
        ext_name: {
            "handler": handler_name,
            "description": "Inject entropy into a module: random code perturbation, line shuffle, or constant drift"
        },
        ".spawn_bridge": {
            "handler": "_bridge_handler_spawn_bridge",
            "description": "Spawn a new agent from a .spawn_bridge file and register its module"
        },
        ".crossfeed": {
            "handler": "_bridge_handler_crossfeed",
            "description": "Cross-feed: copy a function from one module into another as a new function"
        }
    }
    fname = f'bridge_types_gen{gen:04d}.bridge'
    fpath = os.path.join(BASE, fname)
    if _write(fpath, json.dumps(bridge_cfg, indent=2)):
        existing = genome.setdefault('type_registry', {})
        for ext, cfg in bridge_cfg.items():
            if ext not in existing:
                existing[ext] = {'handler': 'bridge', 'description': cfg['description']}
        _save_genome(genome)
        return fname
    return None

def _write_new_metaop(genome):
    gen = genome.get('generation', 0)
    entropy_op = f'''@_register_mutation_op('mutation_op_bridge_entropy_inject')
def mutation_op_bridge_entropy_inject(lines, funcs, target_name):
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    mode = random.choice(['drift_const', 'shuffle_block', 'inject_noise_comment', 'duplicate_branch'])
    if mode == 'drift_const':
        for i in range(len(r)):
            for pat in ['0.', '1.', '2.', '3.', '5.', '10']:
                if pat in r[i] and random.random() < 0.2:
                    old_val = re.search(r'(\\d+\\.?\\d*)', r[i])
                    if old_val:
                        drift = round(float(old_val.group(1)) * random.uniform(0.8, 1.2), 2)
                        r[i] = r[i].replace(old_val.group(1), str(drift), 1)
                        break
    elif mode == 'shuffle_block':
        block_start = random.randrange(0, max(1, len(r) - 4))
        block_end = min(block_start + random.randint(2, 5), len(r))
        block = r[block_start:block_end]
        random.shuffle(block)
        r[block_start:block_end] = block
    elif mode == 'inject_noise_comment':
        idx = random.randrange(len(r))
        noise = f"  # bridge:entropy:gen={{gen}}:{{random.getrandbits(16):04x}}"
        r.insert(idx, r[idx] + noise)
    elif mode == 'duplicate_branch':
        branch_lines = [i for i, l in enumerate(r) if l.strip().startswith('if ') or l.strip().startswith('elif ')]
        if branch_lines:
            idx = random.choice(branch_lines)
            indent = len(r[idx]) - len(r[idx].lstrip())
            fake_cond = f'{{"if", "elif"}}random.random() < 0.5'
            r.insert(idx + 1, ' ' * indent + f'if random.random() < 0.5:  # bridge:entropy:branch')
            r.insert(idx + 2, ' ' * (indent + 4) + f'pass  # bridge:entropy gen={{gen}}')
    return r

@_register_mutation_op('mutation_op_bridge_cross_wire')
def mutation_op_bridge_cross_wire(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    if funcs and len(funcs) > 1:
        peer_funcs = [n for n in funcs if n != target_name and not n.startswith('_')]
        if peer_funcs:
            donor = random.choice(peer_funcs)
            ds, de = funcs[donor]
            if ds < len(r) and de <= len(r) and de > ds:
                snippet = r[ds:de]
                insert_at = random.randrange(0, len(r))
                r[insert_at:insert_at] = [''] + list(snippet) + ['  # bridge:cross-wire from ' + donor]
    return r
'''
    op_name = f'mutation_op_bridge_entropy_inject'
    metaop_content = entropy_op
    os.makedirs(METAOPS_DIR, exist_ok=True)
    fname = f'mutation_op_bridge_gen{gen:04d}.metaop'
    fpath = os.path.join(METAOPS_DIR, fname)
    if _write(fpath, metaop_content):
        genome.setdefault('custom_mutation_ops', {})[op_name] = metaop_content
        if op_name not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(op_name)
        _save_genome(genome)
        return fname
    return None

def _cross_wire_modules(genome):
    gen = genome.get('generation', 0)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    if len(py_files) < 2:
        return changes
    pairs = min(3, len(py_files) // 2)
    for _ in range(pairs):
        donor_file = random.choice(py_files)
        recipient_file = random.choice([f for f in py_files if f != donor_file])
        if not donor_file or not recipient_file:
            continue
        donor_src = _read(os.path.join(MOD, donor_file))
        recipient_src = _read(os.path.join(MOD, recipient_file))
        if not donor_src or not recipient_src:
            continue
        donor_funcs = _extract_functions(donor_src)
        candidates = [n for n in donor_funcs if not n.startswith('_') and n != 'run']
        if not candidates:
            continue
        chosen = random.choice(candidates)
        ds, de = donor_funcs[chosen]
        donor_lines = donor_src.split('\n')
        if ds >= len(donor_lines) or de > len(donor_lines):
            continue
        func_code = '\n'.join(donor_lines[ds:de])
        bridge_name = chosen + '_bridge_copy'
        recipient_lines = recipient_src.split('\n')
        insert_idx = random.randrange(0, len(recipient_lines))
        new_lines = list(recipient_lines)
        new_lines.insert(insert_idx, f'\n# bridge:cross-wire from {donor_file}:{chosen} gen={gen}')
        new_lines.insert(insert_idx + 1, func_code.replace(f'def {chosen}(', f'def {bridge_name}(', 1))
        new_src = '\n'.join(new_lines)
        if _valid(new_src):
            _write(os.path.join(MOD, recipient_file), new_src)
            changes.append(f'{donor_file}:{chosen}->{recipient_file}:{bridge_name}')
    return changes

def _inject_cross_infection(genome):
    gen = genome.get('generation', 0)
    changes = []
    target_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f not in ('bridge.py', '__init__.py')]
    targets = random.sample(target_files, min(2, len(target_files)))
    for fname in targets:
        fpath = os.path.join(MOD, fname)
        src = _read(fpath)
        if not src:
            continue
        marker = f'\n# bridge:cross-infected gen={gen} ts={int(time.time())}\n_BRIDGE_CROSS_INFECTED_{gen} = True\n'
        if marker.strip() in src:
            continue
        new_src = src + marker
        if _valid(src) and _valid(new_src):
            _write(fpath, new_src)
            changes.append(fname)
    return changes

def _mutate_genome_params(genome):
    gen = genome.get('generation', 0)
    changes = []
    if random.random() < 0.4:
        current = genome.get('mutation_rate', 0.5)
        delta = random.uniform(-0.05, 0.08)
        genome['mutation_rate'] = round(max(0.1, min(1.0, current + delta)), 3)
        changes.append(f'mutation_rate:{current}->{genome["mutation_rate"]}')
    if random.random() < 0.3:
        current = genome.get('spawn_threshold', 5)
        delta = random.choice([-1, 0, 1])
        genome['spawn_threshold'] = max(3, current + delta)
        changes.append(f'spawn_threshold:{current}->{genome["spawn_threshold"]}')
    source_autonomy = genome.get('source_autonomy_index', 0.0)
    new_autonomy = round(min(1.0, source_autonomy + random.uniform(0.02, 0.08)), 3)
    genome['source_autonomy_index'] = new_autonomy
    changes.append(f'autonomy:{source_autonomy}->{new_autonomy}')
    return changes

def run(genome):
    gen = genome.get('generation', 0)
    changes = []

    bridge_file = _write_new_type_bridge(genome)
    if bridge_file:
        changes.append(f'new_bridge_types:{bridge_file}')

    metaop_file = _write_new_metaop(genome)
    if metaop_file:
        changes.append(f'new_metaop:{metaop_file}')

    cross_wired = _cross_wire_modules(genome)
    changes.extend([f'cross_wire:{cw}' for cw in cross_wired])

    infected = _inject_cross_infection(genome)
    if infected:
        changes.append(f'infected:{",".join(infected)}')

    param_changes = _mutate_genome_params(genome)
    changes.extend(param_changes)

    if changes:
        genome['bridge_actions'] = len(changes)
        genome['bridge_last_gen'] = gen
        genome['bridge_last_ops'] = changes
        genome['bridge_total_actions'] = genome.get('bridge_total_actions', 0) + len(changes)
        for agent in genome.get('agents', []):
            if agent['id'] == 'bridge':
                score_bump = min(2.0, len(changes) * 0.3)
                agent['score'] = round(min(10.0, agent.get('score', 5.0) + score_bump), 1)
                break
        _save_genome(genome)

    return f'[bridge] gen={gen} actions={len(changes)} ops={changes}'
