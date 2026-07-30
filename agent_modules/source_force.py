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
    """Genetic programming crossover: swap random subtrees between two ASTs."""
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
    """Mutate the run() function of a module: inject a random line from another module."""
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
    """GP crossover between random module pairs. Directly recombines ASTs."""
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
    """Cryptographic lineage tracking: hash every module, embed lineage in genome."""
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
    """Swap function bodies between two random modules using AST surgery."""
    mods = [m for m in _modules() if m != 'source_force.py']
    if len(mods) < 2: return 0
    a, b = random.sample(mods, 2)
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
    """Rewrite every custom mutation_op: inject a stochastic nonce into each."""
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

    delta = len(changes) * 0.25 + n * 0.1
    old_ev = genome.get('emergence_velocity', 0.0)
    genome['emergence_velocity'] = round(min(2.0, old_ev * 0.85 + delta * 0.15), 4)
    genome['sf_last_gen'] = gen
    genome['sf_total_ops'] = genome.get('sf_total_ops', 0) + len(changes)

    result = f'[source-force] gen={gen} changes={changes}'
    genome['_sf_result'] = result
    _sg(genome)
    return result
