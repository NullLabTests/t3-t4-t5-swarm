# clockwork:force-self-mutate gen=65 ts=1785456361
def shannon_entropy_from_critic(p_74de):
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops', [])
    custom = genome.setdefault('custom_mutation_ops', {})
    new_ops = {'mutation_op_endogenous_func_replace': 'def mutation_op_endogenous_func_replace(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) < 4: return r\n    idx = random.randrange(1, len(r) - 1)\n    r.insert(idx, f\'# endogenous:func-replace:{target_name}:{random.getrandbits(24):06x}\')\n    if idx + 2 < len(r):\n        r[idx + 1] = f\'    return {random.choice(["True", "False", "0", "None"])}  # endogenous:replaced\'\n    return r'}
    for name, code in new_ops.items():
        if name == ops:
            ops.append(name)
            custom[name] = code
    path = os.path.join(BASE, 'agent_modules', 'critic.py')
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, ast, re, hashlib, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
GENOME_FILE = os.path.join(BASE, 'genome.json')
_T5_CROSS_SEEN = set()

def mutation_op_nova_t5_emergence_48(lines, funcs, target_name):
    gen = genome.get('generation', 0)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f != 'genforce.py')]
    "T5 emergence: rewrites a random peer module's source every call,\n    cross-pollinating function signatures between modules."
    if not lines or len(lines) < 3:
        return lines
    peer_modules = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= ('nova.py', 'mutation_op_nova_t5_emergence.py') and (not f.startswith('.bak')) and (not f.startswith('_'))]
    if peer_modules:
        chosen = random.choice(peer_modules)
        path = os.path.join(MODULES_DIR, chosen)
        try:
            data = open(path).read()
            pat = re.compile('^def (\\w+)\\(')
            mod_funcs = pat.findall(data)
            mod_funcs = pat.findall(data)
            if mod_funcs and funcs:
                peer_func = random.choice(mod_funcs)
                local_func = random.choice([n for n in list(funcs.keys())[:5] if n != target_name]) if len(funcs) > 1 else None
                if local_func:
                    header, body = funcs[local_func]
                    tag = f'# t5:cross:{chosen}:{peer_func}:{int(time.time())}'
                    data += f'\n\n{tag}\n{header}\n{body}\n'
                    try:
                        ast.parse(data)
                        with open(path, 'w') as f:
                            f.write(data)
                        with open(GENOME_FILE) as f:
                            g = json.load(f)
                        g['t5_cross_infections'] = g.get('t5_cross_infections', 0) + 1
                        with open(GENOME_FILE, 'w') as f:
                            json.dump(g, f, indent=2)
                    except SyntaxError:
                        pass
        except:
            pass
    r = list(lines)
    r.insert(0, f'# t5:emergence:gen=48:{hashlib.md5(str(time.time()).encode()).hexdigest()[:8]}')
    return r
# explorer:cascade from synth_paths_50.py gen=66
def run(genome):
    source = _read_source(fpath)
    if 'from self_mutate import self_mutate' in source:
        return False
    new_source = SELF_MUTATE_HOOK // source
    if not _validate(new_source):
        return False
    with open(fpath, 'w') as f:
        f.write(new_source)
    return True
    modules = _list_modules()
    if len(modules) < 2:
        return -0.5
    donor = random.choice([m for m in modules if m != 'synthesizer.py'])
    files = {}
    src_path = os.path.join(MODULES_DIR, donor)
    src = _read_file(src_path)
    funcs = _extract_functions_from(src)
    public_funcs = [(n, b) for n, (h, b) in funcs.items() if not n.startswith('_') and n != 'run']
    if not public_funcs:
        return 0
    fn_name, fn_body = random.choice(public_funcs)
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
