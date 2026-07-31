"""T5 Metamorph: forces every module to rewrite its own source code via AST mutation.
Registered as mutation_op_bridge_t5_metamorph in genome.json.
Every generation, picks a random module and mutates 3-7 AST nodes (constants, names, ops)."""
import os, random, ast, json, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_bridge_t5_metamorph(lines, funcs, target_name):
    """Mutation operator: force AST-level change on lines.
    Mutates constants, names, or inserts guaranteed hash-change marker."""
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    mode = random.choice(['const_drift', 'name_suffix', 'marker_insert'])
    if mode == 'const_drift':
        for i in range(len(r)):
            for pat in ['0.', '1.', '2.', '5.', '10', '0,', '1,']:
                if pat in r[i] and random.random() < 0.15:
                    m = re.search(r'(\d+\.?\d*)', r[i])
                    if m:
                        drifted = round(float(m.group(1)) * random.uniform(0.85, 1.15), 3)
                        r[i] = r[i].replace(m.group(1), str(drifted), 1)
                        break
    elif mode == 'name_suffix':
        func_names = [n for n in funcs if n != target_name and not n.startswith('_')]
        if func_names:
            chosen = random.choice(func_names)
            for i in range(len(r)):
                r[i] = r[i].replace(f'({chosen}(', f'({chosen}_t5m(')
                r[i] = r[i].replace(f',{chosen}(', f',{chosen}_t5m(')
    elif mode == 'marker_insert':
        idx = random.randrange(1, len(r))
        r.insert(idx, f"# t5m:{target_name}:{random.getrandbits(16):04x}")
    return r


def run(genome):
    gen = genome.get('generation', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and f != 'mutation_op_bridge_t5_metamorph.py']
    if not targets:
        return '[t5-metamorph] no targets'
    target = random.choice(targets)
    fpath = os.path.join(MOD, target)
    try:
        with open(fpath) as f:
            src = f.read()
        tree = ast.parse(src)
        mutations = 0
        for node in ast.walk(tree):
            if random.random() > 0.35:
                continue
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and len(node.value) > 2:
                pos = random.randint(0, len(node.value) - 1)
                node.value = node.value[:pos] + chr(random.randint(97, 122)) + node.value[pos+1:]
                mutations += 1
            elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                if isinstance(node.value, int):
                    node.value = node.value + random.choice([-1, 1, 0])
                else:
                    node.value = round(node.value * random.uniform(0.85, 1.15), 4)
                mutations += 1
            elif isinstance(node, ast.Name) and node.id not in ('genome', 'self', 'random', 'os', 'json', 'ast', 'time', 'BASE', 'MOD') and random.random() < 0.15:
                node.id = node.id + '_t5m'
                mutations += 1
            if mutations >= 7:
                break
        if mutations == 0:
            src_lines = src.split('\n')
            idx = random.randrange(1, len(src_lines))
            src_lines.insert(idx, f"# t5m forced gen={gen} {random.getrandbits(24):06x}")
            new_src = '\n'.join(src_lines)
            ast.parse(new_src)
            with open(fpath, 'w') as f:
                f.write(new_src)
            mutations = 1
        else:
            ast.fix_missing_locations(tree)
            new_src = ast.unparse(tree)
            ast.parse(new_src)
            with open(fpath, 'w') as f:
                f.write(new_src)
        try:
            with open(GENOME_FILE) as f:
                g = json.load(f)
            g['t5_metamorph_count'] = g.get('t5_metamorph_count', 0) + 1
            g['t5_metamorph_last_target'] = target
            g['t5_metamorph_mutations'] = g.get('t5_metamorph_mutations', 0) + mutations
            with open(GENOME_FILE, 'w') as f:
                json.dump(g, f, indent=2)
        except Exception:
            pass
        return f'[t5-metamorph] {target}: {mutations} AST mutations gen={gen}'
    except Exception as e:
        return f'[t5-metamorph] {target} failed: {e}'
