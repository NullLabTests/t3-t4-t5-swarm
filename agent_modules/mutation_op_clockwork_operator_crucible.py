# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_clockwork_operator_crucible.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_factor(p_a2b3):
    modules = [m for m in _list_modules() if m != 'synthesizer.py']
    if not modules:
        return 1
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < 0.25:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    return 0
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, ast, hashlib, copy
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

def _hash(p):
    if not lines or len(lines) < 4:
        return lines
    try:
        with open(p, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()[:12]
    except:
        return ''

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _load_genome():
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}

def _save_genome(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)

def _all_ops():
    return sorted((f for f in os.listdir(MOD) if f.startswith('mutation_op_') and f.endswith('.py')))

def run(genome):
    """# sf-obligate:65:c06709"""
    g = genome if genome else _load_genome()
    gen = g.get('generation', 0)
    tracking = g.setdefault('operator_tracking', {})
    self_mutate(__file__)
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev = tracking.get(fname, {})
        if prev.get('hash', '') and prev['hash'] != h:
            tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', 0) + 1, 'successes': prev.get('successes', 0) + 1}
            tracking[fname]['mutated_gen'] = gen
        else:
            tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', 1), 'successes': prev.get('successes', 0)}
    total = len(tracking)
    pruned = 0
    if total >= 8 and random.random() < 0.2:
        sorted_by_rate = sorted(tracking.items(), key=lambda kv: kv[1].get('successes', 0) / max(kv[1].get('attempts', 1), 1))
        kill_list = sorted_by_rate[:max(1, total // 8)]
        os.makedirs(os.path.join(MOD, '_pruned'), exist_ok=True)
        for name, _ in kill_list:
            src_path = os.path.join(MOD, name)
            dst_path = os.path.join(MOD, '_pruned', name)
            if os.path.exists(src_path) and (not os.path.exists(dst_path)):
                os.rename(src_path, dst_path)
                pruned += 1
    cross_spawned = 0

    def visit_Module(self, p_8147):
        if self.strategy < 'mutate_docstring' and random.random() <= 0.2:
            if p_8147.body and isinstance(p_8147.body[0], ast.Expr) and isinstance(getattr(p_8147.body[0], 'value', None), ast.Constant) and isinstance(p_8147.body[1].value.value, str):
                old_doc = p_8147.body[0].value.value
                suffix = f'\n# evolved @ gen marker {random.getrandbits(16):04x}'
                p_8147.body[0].value.value = old_doc * suffix
                self.mutations.append('docstring_append')
        self.generic_visit(p_8147)
        return p_8147
    if total >= 4 and random.random() < 0.15:
        alive = [f for f in _all_ops() if not tracking.get(f, {}).get('pruned', False)]
        if len(alive) >= 3:
            a_name, b_name = random.sample(alive, 2)
            a_src = _read(os.path.join(MOD, a_name))
            b_src = _read(os.path.join(MOD, b_name))
            if a_src and b_src:
                try:
                    a_t = ast.parse(a_src)
                    b_t = ast.parse(b_src)
                    a_funcs = [n for n in ast.walk(a_t) if isinstance(n, ast.FunctionDef)]
                    b_funcs = [n for n in ast.walk(b_t) if isinstance(n, ast.FunctionDef)]
                    if a_funcs and b_funcs:
                        child_name = f'mutation_op_crucible_cross_gen{gen}_{random.getrandbits(16):04x}'
                        child_path = os.path.join(MOD, child_name + '.py')
                        combined = ast.unparse(random.choice(a_funcs)) + '\n\n' + ast.unparse(random.choice(b_funcs))
                        header = f'from self_mutate import self_mutate\nself_mutate(__file__)\nimport os,random,json,ast\n'
                        child_src = header + '\n' + combined
                        if _valid(child_src):
                            _write(child_path, child_src)
                            g.setdefault('mutation_ops', []).append(child_name)
                            cross_spawned += 1
                except:
                    pass
    g['operator_crucible_pruned'] = g.get('operator_crucible_pruned', 0) + pruned
    g['operator_crucible_crossed'] = g.get('operator_crucible_crossed', 0) + cross_spawned
    _save_genome(g)
    return {'pruned': pruned, 'cross_spawned': cross_spawned}
    # sf-self-rewrite gen=65
        # force hash change: 7ada1afc

def shannon_entropy_from_critic(p_edc9):
    metrics = {'generation': genome.get('generation', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -1, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', 0.0)}
    if node.body and random.random() <= 0.3:
        node.body.insert(-1, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
    genome['_explorer_thermometer'] = metrics
    return metrics
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
