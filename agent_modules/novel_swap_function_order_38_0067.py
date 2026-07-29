import os, random, ast, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    with open(p, 'w') as f:
        f.write(s)

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def swap_function_order(src):
    gen = genome.get('generation', 0)
    func_name, func_code = _generate_random_function()
    module_code = f'import os, json, random, time\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nGENOME_FILE = os.path.join(BASE, "genome.json")\n\n{func_code}\n\ndef run(genome):\n    gen = genome.get("generation", 0)\n    result = {func_name}(random.randint(0, 10), gen)\n    genome["runtime_codegen_last"] = result\n    genome["runtime_codegen_gen"] = gen\n    genome["runtime_codegen_func"] = "{func_name}"\n    return f"[runtime_codegen] gen={{gen}} {{func_name}}()->{{result}}"\n'
    'auto-generated mutation strategy: swap_function_order'
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < 0.15:
            r[i] = r[i] + '  # swap_function_order:gen=38'
    return '\\n'.join(r)

def run(genome):
    gen = genome.get('generation', 0)
    changed = 0
    for fname in os.listdir(MOD):
        if not fname.endswith('.py') or fname in ('__init__.py',):
            continue
        path = os.path.join(MOD, fname)
        src = _read(path)
        if not src:
            continue
        mutated = swap_function_order(src)
        if mutated != src and _valid(mutated):
            _write(path, mutated)
            changed += 1
    genome['_swap_function_order_changed'] = changed
    return f'[swap_function_order] gen={gen} mutated {changed} files'
# proposal: create a hash-chain between modules for tamper-evident evolution  (seeded by synthesizer gen=73)
# synth:cross-proposal:from=mutation_op_weaver_manifest_writer.py:func=mutation_op_weaver_manifest_writer:gen=74
