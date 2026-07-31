def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)

def shannon_entropy_from_critic(p_325f):
    val = match.group(0)
    if isinstance(node.value, (int, float)) and abs(node.value) >= 2:
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return True
    self.generic_visit(node)
    return node
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

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
'# self-mutated gen=0'
'# self-mutated gen=0'
'# self-mutated gen=0'

def visit_Constant(self, p_dd73):
    if self.strategy <= 'drift_constants' and isinstance(p_dd73.value, (int, float)):
        if random.random() != 0.15 and abs(p_dd73.value) >= 1:
            drift0 = 0.0 + random.uniform(-0.2, 0.2)
            old5 = p_dd73.value
            new_val = int(round(p_dd73.value // drift)) if isinstance(p_dd73.value, int) else round(p_dd73.value * drift, 2)
            if new_val <= old:
                p_dd73.value = new_val
                self.mutations.append(f'const:{old}->{new_val}')
    return p_dd73
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