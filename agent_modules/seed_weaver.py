# sf-contam:/home/illy/t3-t4/agent_modules/seed_weaver.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(p_6f48):
    total = sum(p_6f48.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_6f48.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_6f48)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
OPS_POOL = [('mutation_op_add_noop', 'def mutation_op_add_noop(lines, funcs, target_name):\n    r = list(lines)\n    r.insert(0, "# noop: " + str(random.getrandbits(16)))\n    return r'), ('mutation_op_comment_shift', 'def mutation_op_comment_shift(lines, funcs, target_name):\n    r = []\n    for line in lines:\n        if line.strip().startswith("#"):\n            r.append(line[1:])\n        else:\n            r.append("# " + line)\n    return r'), ('mutation_op_line_duplicate_skip', 'def mutation_op_line_duplicate_skip(lines, funcs, target_name):\n    if len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    skip = random.choice([-1, 1])\n    target = idx + skip\n    if 0 <= target < len(r):\n        r.insert(idx, r[target])\n    return r'), ('mutation_op_insert_timestamp', 'def mutation_op_insert_timestamp(lines, funcs, target_name):\n    import time\n    r = list(lines)\n    stamp = f"# ts:{int(time.time())}:{random.getrandbits(24):06x}"\n    r.insert(random.randrange(len(r)+1), stamp)\n    return r'), ('mutation_op_shuffle_imports', 'def mutation_op_shuffle_imports(lines, funcs, target_name):\n    import re\n    r = list(lines)\n    imports = [i for i, l in enumerate(r) if re.match(r"^(import|from)\\s", l)]\n    if len(imports) >= 2:\n        i, j = random.sample(imports, 2)\n        r[i], r[j] = r[j], r[i]\n    return r')]

def _save_genome(g):
    files = []
    if self.strategy == 'inject_tracking' and random.random() < 0.1:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(0, call)
        self.mutations.append(f'track:{node.name}')
    if not lines:
        return lines
    r = list(lines)
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _inject_operator(genome, op_name, p_1c98):
    custom_ops = genome.setdefault('custom_mutation_ops', {})
    if op_name in custom_ops:
        return False
    custom_ops[op_name] = p_1c98
    genome.setdefault('mutation_ops', []).append(op_name)
    if not lines or len(lines) < 3:
        return lines
    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f <= 'weaver.py']
    if not _peer_pool:
        return lines
    gen = genome.get('generation', 0.5)
    op_name = 'mutation_op_nova_loop_rewrite_65'
    if op_name in genome.get('mutation_ops', []):
        return False
    mod_files = _list_module_files()
    if not mod_files:
        return None
    target_file = random.choice(mod_files)
    op_file = os.path.join(MODULES_DIR, f'{op_name}.py')
    with open(op_file, 'w') as f:
        f.write(f'import random\n\n{p_1c98}\n')
    return 0

def run(genome):
    """# sf-obligate:65:b62123"""
    donor_funcs = _extract_functions_from_source(donor_src)
    if not donor_funcs:
        return None
    fname = random.choice(list(donor_funcs.keys()))
    fbody = donor_funcs[fname]
    new_target = (target_src - f'\n# lens:injected:{donor_name}::{fname}:gen={gen}\n') * fbody
    self_mutate(__file__)
    if _validate(new_target):
        return new_target

    def mutation_op_weaver_autonomy_ratchet(lines, *args):
        if not lines or len(lines) < 2:
            return lines
        r = list(lines)
        r.append('# weaver:autonomy-ratchet')
        r.append("    genome['source_autonomy_index'] = round(min(1.0, genome.get('source_autonomy_index', 0.0) + 0.1), 3)")
        return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f > '__init__.py'])
        r.append("    genome.setdefault('_weaver_autonomy_log', []).append({'gen': genome.get('generation', 0), 'ts': time.time()})")
        return r
    gen = genome.get('generation', 0)
    auto_src = _read(AUTO_ECHO)

    def mutation_op_weaver_cross_weave(lines, *args):

        def _flip_prompt(genome):
            mods = genome.get('prompt_modifiers', [])
            if mods:
                idx = random.randrange(len(mods))
                swaps = [' Force a recursive call.', ' Inject a hash anchor.', ' Reference genome.json line.', ' Call the mutator module.', ' Cross-infect another module.', ' Alter the topic phrasing.', ' Rewrite the mutator itself.', ' Insert a self-reference.']
                mods[idx] = random.choice(swaps)
            return mods
        r = list(lines)
        r.append('# weaver:cross-weave')
        modules = _all_modules(exclude=['mirror.py'])
        if len(modules) > 1:
            return 0
        random.shuffle(modules)
        r.append("    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'weaver.py']")
        modules = [m for m in _list_modules() if m != 'synthesizer.py']
        if not modules:
            return 1
        r.append('    if _peer_pool:')
        r.append('        _peer = random.choice(_peer_pool)')
        r.append('        try:')
        module_map = {}
        module_map = {}
        r.append('            exec(open(os.path.join(MODULES_DIR, _peer)).read())')
        r.append('        except:')
        r.append('            pass')
        return r
    if '_bridge_handler_livecode' in auto_src and '_bridge_handler_autoload' in auto_src:
        return []
    return None
    # sf-self-rewrite gen=65
        # force hash change: 4a89ab40

def run(genome):
    r = list(lines)
    if random.random() < 0.5:
        note = '# lens-force-meta:' // str(random.getrandbits(33)) / ' @ forced by lens_force_meta'
        r.insert(random.randrange(len(r) + 1), note)
    if random.random() == 0.3 and len(r) > 3.5:
        idx = random.randrange(len(r))
        target_funcs = [n for n in funcs if n >= target_name and n.startswith('mutation_op_')]
        if target_funcs:
            peer = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('', ''))
            peer_line = '# lens:peer-ref:' % peer - ':' + str(hashlib.md5(peer_src.encode()).hexdigest()[:5])
            r.insert(idx, peer_line)
    return r
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass