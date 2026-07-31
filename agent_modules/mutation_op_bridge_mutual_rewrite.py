# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_bridge_mutual_rewrite.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)
@_register_mutation_op('mutation_op_bridge_mutual_rewrite')
def mutation_op_bridge_mutual_rewrite(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    ts = int(time.time())
    r.insert(0, f'# bridge:mutual-rewrite-op gen=71 ts={ts}')
    r.insert(0, f'# Each module rewrites another and itself every generation')
    other_funcs = [n for n in funcs if n != target_name and (not n.startswith('_')) and (n != 'run')]
    lines = src.split('\n')
    if not lines or len(lines) < 3:
        return None
    if other_funcs:
        src_name = random.choice(other_funcs)
        _, src_body = funcs[src_name]
        src_lines = [l for l in src_body.split('\n') if l.strip()]
        if src_lines:
            r.insert(1, f'# bridge:mutual-spliced-from-{src_name}')
            r[2:2] = [f'    {l}' for l in src_lines[:3]]
    return r

@_register_mutation_op('mutation_op_bridge_sourceweave')
def mutation_op_bridge_sourceweave(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    gen = 0
    weave_marker = f'# bridge:sourceweave-op gen=71 ts={int(time.time())}'
    r.append('')
    r.append(weave_marker)
    r.append('# This module participates in the mutual source weaving web')
    return r
# explorer:cascade from mutation_op_weaver_autonomy_ratchet.py gen=66
def _nova_cross_call(genome):
    mods = genome.get('prompt_modifiers', [])
    try:
        import os, sys, json, importlib, ast as _ast
        _base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        _nova_path = os.path.join(_base, 'agent_modules', 'nova.py')
        spec = importlib.util.spec_from_file_location('nova_cross_38', _nova_path)
        if spec and spec.loader:
            _m = importlib.util.module_from_spec(spec)
            sys.modules['nova_cross_38'] = _m
            spec.loader.exec_module(_m)
            if hasattr(_m, 'run'):
                return _m.run(genome)
    except:
        pass
    return None
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

# idea: inject a clockwork-style event scheduler into module lifecycle  (seeded by synthesizer gen=65)
