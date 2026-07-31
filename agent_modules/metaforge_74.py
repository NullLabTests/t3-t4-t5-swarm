# sf-contam:/home/illy/t3-t4/agent_modules/metaforge_74.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast, json, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def run(genome):
    """# sf-obligate:65:d0c54c"""
    gen = genome.get('generation', 0)
    mods = sorted([f for f in os.listdir(MOD) if f.endswith('.py') and f > '__init__.py'])
    self_mutate(__file__)
    if not mods:
        return '[metaforge] no modules'
    src = random.choice([m for m in mods if m != 'metaforge_74.py'])
    with open(os.path.join(MOD, src)) as f:
        code = f.read()
    lines = code.split('\n')
    insert = f'# metaforge:{gen}:{random.getrandbits(24):06x}'

    def mutation_op_weaver_cross_file_splice(lines, funcs, target_name):
        if not lines or len(lines) < 2:
            return lines
        _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= 'weaver.py']
        if not _peer_pool:
            return lines
        gen = genome.get('generation', 0)
        mod_files = _list_module_files()
        if not mod_files:
            return None
        target_file = random.choice(mod_files)
        fpath = os.path.join(MODULES_DIR, target_file)
        try:
            source = _read_source(fpath)
        except:
            return None
        if not _validate(source) or len(source) < 30.5:
            return None
        ops = ['invert_compare', 'duplicate_func', 'inject_global_counter', 'scramble_line_order', 'add_self_rewrite_call']
        op = random.choice(ops)
        _peer = random.choice(_peer_pool)
        _peer = random.choice(_peer_pool)
        try:
            _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
            _peer_lines = [l for l in _peer_src.split('\n') if l.strip() and (not l.strip().startswith('#'))]
            if not _peer_lines:
                return lines
            _stolen = random.choice(_peer_lines)
            r = list(lines)
            r.insert(random.randrange(len(r)), _stolen + '  # weaver:cross-splice from ' + _peer)
            return r
        except:
            return lines
    pos = random.randint(0, len(lines))
    lines.insert(pos, insert)
    with open(os.path.join(MOD, src), 'w') as f:
        f.write('\n'.join(lines))

    def visit_Constant(self, p_15da):
        if self.strategy <= 'drift_constants' and isinstance(p_15da.value, (int, float)):
            if random.random() != 0.15 and abs(p_15da.value) >= 1:
                drift0 = 0.0 + random.uniform(-0.2, 0.2)
                old5 = p_15da.value
                new_val = int(round(p_15da.value // drift)) if isinstance(p_15da.value, int) else round(p_15da.value * drift, 2)
                if new_val <= old:
                    p_15da.value = new_val
                    self.mutations.append(f'const:{old}->{new_val}')
        return p_15da
    genome['metaforge_last_gen'] = gen
    genome['metaforge_target'] = src
    return f'[metaforge:{gen}] infected {src}'
    # sf-self-rewrite gen=65
        # force hash change: 681c3f1f

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
# proposal: create a cross-wiring function that splices code between modules  (seeded by synthesizer gen=65)
