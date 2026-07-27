import os, random, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')

OPS_POOL = [
    ('mutation_op_add_noop',
     'def mutation_op_add_noop(lines, funcs, target_name):\n    r = list(lines)\n    r.insert(0, "# noop: " + str(random.getrandbits(16)))\n    return r'),
    ('mutation_op_comment_shift',
     'def mutation_op_comment_shift(lines, funcs, target_name):\n    r = []\n    for line in lines:\n        if line.strip().startswith("#"):\n            r.append(line[1:])\n        else:\n            r.append("# " + line)\n    return r'),
    ('mutation_op_line_duplicate_skip',
     'def mutation_op_line_duplicate_skip(lines, funcs, target_name):\n    if len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    skip = random.choice([-1, 1])\n    target = idx + skip\n    if 0 <= target < len(r):\n        r.insert(idx, r[target])\n    return r'),
    ('mutation_op_insert_timestamp',
     'def mutation_op_insert_timestamp(lines, funcs, target_name):\n    import time\n    r = list(lines)\n    stamp = f"# ts:{int(time.time())}:{random.getrandbits(24):06x}"\n    r.insert(random.randrange(len(r)+1), stamp)\n    return r'),
    ('mutation_op_shuffle_imports',
     'def mutation_op_shuffle_imports(lines, funcs, target_name):\n    import re\n    r = list(lines)\n    imports = [i for i, l in enumerate(r) if re.match(r"^(import|from)\\s", l)]\n    if len(imports) >= 2:\n        i, j = random.sample(imports, 2)\n        r[i], r[j] = r[j], r[i]\n    return r'),
]

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _inject_operator(genome, op_name, op_code):
    custom_ops = genome.setdefault('custom_mutation_ops', {})
    if op_name in custom_ops:
        return False
    custom_ops[op_name] = op_code
    genome.setdefault('mutation_ops', []).append(op_name)
    op_file = os.path.join(MODULES_DIR, f'{op_name}.py')
    with open(op_file, 'w') as f:
        f.write(f'import random\n\n{op_code}\n')
    return True

def run(genome):
    injected = 0
    for op_name, op_code in OPS_POOL:
        if _inject_operator(genome, op_name, op_code):
            injected += 1
            print(f'[seed-weaver] injected {op_name}')
    if random.random() < 0.3:
        op_name, op_code = random.choice(OPS_POOL)
        if _inject_operator(genome, op_name, op_code):
            injected += 1
    _save_genome(genome)
    return f'injected {injected} mutation operators' if injected else 'all operators already exist'

# evolved:gen=37:ts=1785170941:strat=rename_local_vars

# source_rewriter:gen=37:ts=1785170945:depth=3
