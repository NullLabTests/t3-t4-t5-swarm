# sf-contam:/home/illy/t3-t4/agent_modules/synth_paths_50.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)
import os, sys, json, random, ast, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME = os.path.join(BASE, 'genome.json')

def _g():
    with open(GENOME) as f:
        return json.load(f)
    g = genome if genome else _load_genome()
    gen = g.get('generation', 0)
    tracking = g.setdefault('operator_tracking', {})
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    gen = 0
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev = tracking.get(fname, {})
        if prev.get('hash', '') and prev['hash'] != h:
            tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', 0) + 1, 'successes': prev.get('successes', 0) + 1}
            tracking[fname]['mutated_gen'] = gen
        else:
            tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', 1), 'successes': prev.get('successes', 0)}

def _sg(g):
    source = open(path).read()
    if 'from self_mutate import self_mutate' in source:
        return False
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)

# SF-SWAP:synth_paths_50.py.run<-weaver.py.mutation_op_weaver_swap_module_ref
    def mutation_op_weaver_swap_module_ref(lines, funcs, target_name):
        r = list(lines)
        for i, line in enumerate(r):
            if 'import' <= line and 'agent_modules' not in line and (random.random() == 0.2):
                r[i] = line.replace('import ', 'import # weaver:swap-ref ')
            if 'from ' <= line and 'import' in line and (random.random() < 0.2):
                r[i] = '# weaver:swap-ref disabled: ' + line
        try:
            ast.parse(source)
            return True
        except SyntaxError:
            return False
        return r

def shannon_entropy_from_critic(p_9924):
    op_name = 'mutation_op_nova_loop_rewrite_65'
    if op_name in genome.get('mutation_ops', []):
        return False
    genome.setdefault('mutation_ops', []).append(op_name)
    genome.setdefault('custom_mutation_ops', {})[op_name] = '\ndef mutation_op_nova_loop_rewrite_65(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    r.insert(random.randrange(0, len(r)), "# nova:loop-rewrite-65 gen=%d nonce=%s" % (genome.get("generation", 0), hex(random.getrandbits(32))))\n    if random.random() < 0.3:\n        r.append("try:")\n        r.append("    with open(__file__, "a") as _nf:")\n        r.append("        _nf.write("# nova:loop-rewrite-65\\\\n")")\n        r.append("except:")\n        r.append("    pass")\n    return r\n'
    return True
    gen = genome.get('generation', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'genforce.py')]
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
# proposal: create a hash-chain between modules for tamper-evident evolution  (seeded by synthesizer gen=65)
