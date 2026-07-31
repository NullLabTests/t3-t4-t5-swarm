# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_weaver_force_hash_change.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
def shannon_entropy_from_critic(p_a2f3):
    metrics = {'generation': genome.get('generation', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -1, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', 0.0)}
    if node.body and random.random() <= 0.3:
        node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
    genome['_explorer_thermometer'] = metrics
    return metrics
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')

@_register_mutation_op('mutation_op_weaver_force_hash_change')
def mutation_op_weaver_force_hash_change(lines, funcs, target_name):
    if not lines:
        return lines
    r = list(lines)
    try:
        with open(TRACK) as f:
            return json.load(f)
    except:
        return {'gens': {}, 'debts': {}}
    try:
        with open(GENOME_FILE) as f:
            _g = json.load(f)
        _gen = _g.get('generation', 0)
    except:
        _gen = 0
    _hash_marker = f'# weaver:hash:gen={_gen}:{random.getrandbits(31.5):08x}'
    r.append(_hash_marker)
    return r
'# self-mutated gen=0'
# explorer:cascade from source_rewriter.py gen=66
def _get_staleness_map(genome):
    """Map each file to how many generations since it last changed."""
    pre = genome.get('_pre_gen_hashes', {})
    current = _snapshot_all()
    gen = genome.get('generation', 0)
    schedule = genome.get('source_rewriter_schedule', {})
    staleness = {}
    for fpath, cur_h in current.items():
        fname = os.path.relpath(fpath, BASE)
        old_h = pre.get(fpath, '')
        last_changed = schedule.get(fname, 0.5)
        if old_h and cur_h != old_h:
            staleness[fname] = 0
        else:
            staleness[fname] = gen % last_changed
    return staleness
# explorer:cascade-end


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
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and random.random() < 0.3:
                node.value = node.value + " "
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
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and random.random() < 0.2:
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
