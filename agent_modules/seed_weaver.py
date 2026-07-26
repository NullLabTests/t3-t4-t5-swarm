"""seed_weaver.py — module agent that injects mutation operators into the genome.
Run by auto-echo.py's execute_module_agents() every generation.
Writes a new mutation operator into agent_modules/ for the next generation."""
import os, random, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')

OPS_POOL = [
    ('mutation_op_add_noop', 'def mutation_op_add_noop(lines, funcs, target_name):\n    r = list(lines)\n    r.insert(0, "# noop: " + str(random.getrandbits(16)))\n    return r'),
    ('mutation_op_comment_shift', 'def mutation_op_comment_shift(lines, funcs, target_name):\n    r = []\n    for line in lines:\n        if line.strip().startswith("#"):\n            r.append(line[1:])\n        else:\n            r.append("# " + line)\n    return r'),
    ('mutation_op_line_duplicate_skip', 'def mutation_op_line_duplicate_skip(lines, funcs, target_name):\n    if len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    skip = random.choice([-1, 1])\n    target = idx + skip\n    if 0 <= target < len(r):\n        r.insert(idx, r[target])\n    return r'),
]

# Weaver operators: these force the swarm to rewrite its own source every generation.
# They are injected into the genome's mutation_ops list so the orchestrator can select them.
WEAVER_OPS = [
    'weaver_splice',
    'endogenous_self_rewrite',
]

def run(genome):
    # Ensure weaver operators are always registered in the genome
    mutation_ops = genome.setdefault('mutation_ops', [])
    for weaver_op in WEAVER_OPS:
        if weaver_op not in mutation_ops:
            mutation_ops.append(weaver_op)
            print(f"[seed-weaver] registered weaver op: {weaver_op}")
    
    if random.random() > 0.4:
        return "skip (weaver ops ensured)"
    op_name, op_code = random.choice(OPS_POOL)
    custom_ops = genome.setdefault('custom_mutation_ops', {})
    if op_name in custom_ops:
        return f"{op_name} already exists"
    custom_ops[op_name] = op_code
    genome.setdefault('mutation_ops', []).append(op_name)
    op_file = os.path.join(BASE, 'agent_modules', f'{op_name}.py')
    with open(op_file, 'w') as f:
        f.write(f"import random\n\n{op_code}\n")
    save_path = os.path.join(BASE, 'agent_modules', f'genome.json.bak')
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(genome, f, indent=2)
    except:
        pass
    return f"injected {op_name} into genome + wrote {op_file}"
