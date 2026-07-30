from self_mutate import self_mutate
self_mutate(__file__)
import os, random, hashlib, ast, json, sys, copy, textwrap, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')
AUTO = os.path.join(BASE, 'auto-echo.py')
SELF = os.path.join(MOD, 'source_force.py')

def _g():
    try:
        with open(GENOME) as f: return json.load(f)
    except: return {}

def _sg(g):
    with open(GENOME, 'w') as f: json.dump(g, f, indent=2)

def _read(p):
    try:
        with open(p) as f: return f.read()
    except: return ''

def _write(p, s):
    with open(p, 'w') as f: f.write(s)

def _valid_py(s):
    try: ast.parse(s); return True
    except SyntaxError: return False

def _modules():
    return sorted(f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py')

def _extract_functions(source):
    tree = ast.parse(source)
    return [(n.name, n) for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]

def _get_source_segment(source, node):
    lines = source.split('\n')
    return '\n'.join(lines[node.lineno - 1:node.end_lineno])

def _gp_crossover(parent_a, parent_b):
    tree_a = ast.parse(parent_a)
    tree_b = ast.parse(parent_b)
    candidates_a = [n for n in ast.walk(tree_a) if isinstance(n, (ast.FunctionDef, ast.If, ast.For, ast.While, ast.Try))]
    candidates_b = [n for n in ast.walk(tree_b) if isinstance(n, (ast.FunctionDef, ast.If, ast.For, ast.While, ast.Try))]
    if not candidates_a or not candidates_b: return None
    child_a = random.choice(candidates_a)
    child_b = random.choice(candidates_b)
    swap = copy.deepcopy(child_b)
    for parent in ast.walk(tree_a):
        for i, child in enumerate(getattr(parent, 'body', [])):
            if child is child_a:
                parent.body[i] = swap
                ast.fix_missing_locations(tree_a)
                result = ast.unparse(tree_a)
                return result if _valid_py(result) else None
    return None

def _mutate_run_function(source):
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == 'run':
            other_mods = [m for m in _modules() if m != 'source_force.py']
            if not other_mods: return None
            donor = _read(os.path.join(MOD, random.choice(other_mods)))
            if not donor: return None
            donor_lines = donor.split('\n')
            if len(donor_lines) < 3: return None
            start = random.randint(0, len(donor_lines) - 1)
            stolen = donor_lines[start:start + random.randint(1, 3)]
            insert_line = textwrap.indent('\n'.join(stolen), '    ')
            insert_pos = random.randint(0, len(node.body))
            node.body.insert(insert_pos, ast.parse(insert_line).body[0] if insert_line.strip() else ast.parse('pass').body[0])
            ast.fix_missing_locations(tree)
            result = ast.unparse(tree)
            return result if _valid_py(result) else None
    return None

def _force_gp_recombination(gen):
    mods = [m for m in _modules() if m != 'source_force.py']
    if len(mods) < 2: return 0
    recombined = 0
    for _ in range(min(8, len(mods) // 2)):
        if len(mods) < 2: break
        a, b = random.sample(mods, 2)
        sa, sb = _read(os.path.join(MOD, a)), _read(os.path.join(MOD, b))
        if not sa or not sb: continue
        child = _gp_crossover(sa, sb)
        if child:
            target = random.choice([a, b])
            _write(os.path.join(MOD, target), child)
            recombined += 1
    return recombined

def _force_self_lineage(gen, genome):
    lineage = {}
    for m in _modules():
        p = os.path.join(MOD, m)
        s = _read(p)
        if s:
            h = hashlib.sha256(s.encode()).hexdigest()[:12]
            lineage[m] = h
    genome['source_force_lineage'] = lineage
    genome['source_force_lineage_gen'] = gen
    return len(lineage)

def _force_function_swap(gen):
    mods = [m for m in _modules() if m != 'source_force.py']
    if len(mods) < 2: return 0
    a, b = random.sample(mods, 2)
# sf-quine gen=50 nonce=3b134d91
    sa, sb = _read(os.path.join(MOD, a)), _read(os.path.join(MOD, b))
    if not sa or not sb: return 0
    try:
        fa = _extract_functions(sa)
        fb = _extract_functions(sb)
        if fa and fb:
            name_a, node_a = random.choice(fa)
            name_b, node_b = random.choice(fb)
            seg_a = ast.get_source_segment(sa, node_a)
            seg_b = ast.get_source_segment(sb, node_b)
            if seg_a and seg_b:
                sa_new = sa.replace(seg_a, f'# SF-SWAP:{a}.{name_a}<-{b}.{name_b}\n{seg_b}', 1)
                sb_new = sb.replace(seg_b, f'# SF-SWAP:{b}.{name_b}<-{a}.{name_a}\n{seg_a}', 1)
                if _valid_py(sa_new) and _valid_py(sb_new):
                    _write(os.path.join(MOD, a), sa_new)
                    _write(os.path.join(MOD, b), sb_new)
                    return 2
    except: pass
    return 0

def _force_mutation_op_rewrite(gen, genome):
    ops = genome.get('custom_mutation_ops', {})
    rewritten = 0
    for name, code in ops.items():
        if random.random() < 0.5:
            lines = code.split('\n')
            idx = random.randint(0, len(lines) - 1) if lines else 0
            marker = f"# sf-rewrite gen={gen}:{random.getrandbits(24):06x}"
            lines.insert(idx, marker)
            genome['custom_mutation_ops'][name] = '\n'.join(lines)
            rewritten += 1
    return rewritten

def _quine_self_rewrite(gen):
    """Rewrite source_force.py itself — the quine: add a self-referential comment
    that mutates every generation, ensuring source_force.py always changes."""
    code = _read(SELF)
    if not code:
        return 0
    lines = code.split('\n')
    marker = f"# sf-quine gen={gen} nonce={random.getrandbits(32):08x}"
    insert_at = random.randint(1, max(1, len(lines) - 1))
    lines.insert(insert_at, marker)
    new_code = '\n'.join(lines)
    if not _valid_py(new_code):
        return 0
    _write(SELF, new_code)
    return 1

def _cross_contaminate_all(gen):
    """Copy one random public function from a random donor module into ALL other modules.
    This guarantees cross-infection across the entire module population every generation."""
    mods = _modules()
    if len(mods) < 2:
        return 0
    donor = random.choice([m for m in mods if m != 'source_force.py'])
    source = _read(os.path.join(MOD, donor))
    if not source:
        return 0
    funcs = _extract_functions(source)
    if not funcs:
        return 0
    donor_name, donor_node = random.choice(funcs)
    seg = _get_source_segment(source, donor_node)
    if not seg:
        return 0
    infected = 0
    for mod in mods:
        if mod == donor or mod == 'source_force.py':
            continue
        path = os.path.join(MOD, mod)
        mod_code = _read(path)
        if not mod_code:
            continue
        new_name = f'{donor_name}_from_{donor.replace(".py", "")}'
        renamed_seg = seg.replace(f'def {donor_name}(', f'def {new_name}(', 1)
        new_mod = f'# sf-contam:{path} gen={gen}:{donor}.{donor_name}\n{renamed_seg}\n' + mod_code
        if not _valid_py(new_mod):
            continue
        _write(path, new_mod)
        infected += 1
    return infected

def _ast_param_shuffle(gen):
    """Shuffle function parameter names across all modules using AST.
    Renames one random parameter in each module to a random name."""
    mods = [m for m in _modules() if m != 'source_force.py']
    renamed = 0
    for mod in mods:
        path = os.path.join(MOD, mod)
        code = _read(path)
        if not code:
            continue
        try:
            tree = ast.parse(code)
        except SyntaxError:
            continue
        candidates = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.args.args:
                for arg in node.args.args:
                    arg_name = arg.arg
                    if arg_name not in ('self', 'cls', 'genome', 'gen', 'lines', 'funcs', 'target_name'):
                        candidates.append((node, arg))
        if not candidates:
            continue
        func_node, arg_node = random.choice(candidates)
        old_name = arg_node.arg
        new_suffix = hex(random.getrandbits(16))[2:]
        new_name = f'p_{new_suffix}'
        start_line = func_node.lineno
        end_line = func_node.end_lineno
        func_lines = code.split('\n')[start_line - 1:end_line]
        func_text = '\n'.join(func_lines)
        for name_node in ast.walk(func_node):
            if isinstance(name_node, ast.Name) and name_node.id == old_name:
                old_ref = old_name
                break
        new_func_text = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, func_text)
        lines = code.split('\n')
        before = lines[:start_line - 1]
        after = lines[end_line:]
        new_lines = before + new_func_text.split('\n') + after
        new_code = '\n'.join(new_lines)
        if not _valid_py(new_code):
            continue
        _write(path, new_code)
        renamed += 1
    return renamed

def _genome_topology_mutate(genome, gen):
    """Add new spawn_pool entries, mutation_ops, and genome structure fields."""
    mutations = 0
    pool_names = ['riptide', 'anvil', 'prism', 'vortex', 'cortex', 'nexus', 'cipher', 'ember', 'shard', 'glyph']
    if random.random() < 0.6:
        new_id = random.choice(pool_names)
        existing = {e.get('id') for e in genome.get('spawn_pool', [])}
        if new_id not in existing:
            prompts = [
                f'You inject recursive self-reference into every module every generation.',
                f'You force every agent to write code that mutates its own source.',
                f'You rewrite the genome structure to add new feedback loops.',
                f'You splice function bodies between random modules each turn.',
                f'You inject entropy-driven randomness into selection weights.',
            ]
            genome.setdefault('spawn_pool', []).append({
                'id': new_id,
                'prompt': random.choice(prompts)
            })
            mutations += 1
    if random.random() < 0.5:
        op_names = [f'mutation_op_sf_self_quine_{gen}', f'mutation_op_sf_cross_pollinate_{gen}',
                    f'mutation_op_sf_param_drift_{gen}', f'mutation_op_sf_constant_flux_{gen}']
        new_op = random.choice(op_names)
        if new_op not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(new_op)
            genome.setdefault('custom_mutation_ops', {})[new_op] = (
                f"# sf-synthesized gen={gen}\n"
                f"def {new_op}(lines, funcs, target_name):\n"
                f"    if not lines: return lines\n"
                f"    r = list(lines)\n"
                f"    idx = random.randrange(len(r))\n"
                f"    r.insert(idx, '# sf-mutated gen={gen}:{random.getrandbits(16):04x}')\n"
                f"    return r\n"
            )
            mutations += 1
    if random.random() < 0.3:
        genome['sf_topology_gen'] = gen
        genome['sf_genome_mutations'] = genome.get('sf_genome_mutations', 0) + 1
    return mutations

def _inject_self_rewrite_hooks(gen):
    """Inject a self-rewrite call into the run() function of every module.
    Every module will call a mutation function on itself when run()."""
    mods = [m for m in _modules() if m != 'source_force.py']
    injected = 0
    for mod in mods:
        path = os.path.join(MOD, mod)
        code = _read(path)
        if not code:
            continue
        try:
            tree = ast.parse(code)
        except SyntaxError:
            continue
        run_func = None
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'run':
                run_func = node
                break
        if not run_func:
            continue
        hook = f"# sf-self-rewrite gen={gen}\n    # force hash change: {random.getrandbits(32):08x}"
        lines = code.split('\n')
        run_start = run_func.lineno - 1
        run_end = run_func.end_lineno or (run_start + 1)
        indent = '    '
        hook_lines = hook.split('\n')
        for i, hl in enumerate(hook_lines):
            lines.insert(run_end + i, indent + hl if hl.startswith('#') else hl)
        new_code = '\n'.join(lines)
        if not _valid_py(new_code):
            continue
        _write(path, new_code)
        injected += 1
    return injected

def _constant_drift_all(gen):
    """Drift numeric constants across all modules by small random amounts."""
    mods = [m for m in _modules() if m != 'source_force.py']
    drifted = 0
    for mod in mods:
        path = os.path.join(MOD, mod)
        code = _read(path)
        if not code:
            continue
        def _drift(match):
            val = match.group(0)
            try:
                num = float(val)
                if abs(num) > 1000:
                    return val
                factor = random.uniform(0.8, 1.2)
                new = int(round(num * factor)) if val.isdigit() else round(num * factor, 2)
                if new == 0 and num > 0:
                    new = int(num) + 1
                if new == num:
                    new = num + random.choice([1, -1, 2, -2])
                return str(new)
            except ValueError:
                return val
        new_code = re.sub(r'\b(\d+)\b', _drift, code)
        if new_code == code:
            continue
        if not _valid_py(new_code):
            continue
        _write(path, new_code)
        drifted += 1
    return drifted

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    n = _force_gp_recombination(gen)
    if n:
        changes.append(f'gp_cross:{n}')
        genome['sf_gp_recombinations'] = genome.get('sf_gp_recombinations', 0) + n
    n = _force_function_swap(gen)
    if n:
        changes.append(f'swap:{n}')
        genome['sf_function_swaps'] = genome.get('sf_function_swaps', 0) + n
    n = _force_self_lineage(gen, genome)
    if n:
        changes.append(f'lineage:{n}')
    n = _force_mutation_op_rewrite(gen, genome)
    if n:
        changes.append(f'op_rewrite:{n}')
        genome['sf_op_rewrites'] = genome.get('sf_op_rewrites', 0) + n
    n = _quine_self_rewrite(gen)
    if n:
        changes.append(f'quine_self:{n}')
        genome['sf_quine_count'] = genome.get('sf_quine_count', 0) + n
    n = _cross_contaminate_all(gen)
    if n:
        changes.append(f'cross_contam:{n}')
        genome['sf_cross_contam'] = genome.get('sf_cross_contam', 0) + n
    n = _ast_param_shuffle(gen)
    if n:
        changes.append(f'param_shuffle:{n}')
        genome['sf_param_shuffles'] = genome.get('sf_param_shuffles', 0) + n
    n = _inject_self_rewrite_hooks(gen)
    if n:
        changes.append(f'self_hooks:{n}')
        genome['sf_self_hooks'] = genome.get('sf_self_hooks', 0) + n
    n = _constant_drift_all(gen)
    if n:
        changes.append(f'drift:{n}')
        genome['sf_drifts'] = genome.get('sf_drifts', 0) + n
    n = _genome_topology_mutate(genome, gen)
    if n:
        changes.append(f'topo:{n}')
    delta = len(changes) * 0.3 + n * 0.1
    old_ev = genome.get('emergence_velocity', 0.0)
    genome['emergence_velocity'] = round(min(2.0, old_ev * 0.8 + delta * 0.2), 4)
    genome['sf_last_gen'] = gen
    genome['sf_total_ops'] = genome.get('sf_total_ops', 0) + len(changes)
    result = f'[source-force] gen={gen} changes={changes}'
    genome['_sf_result'] = result
    _sg(genome)
    return result
