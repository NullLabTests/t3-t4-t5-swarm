# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_lens_force_meta.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
def shannon_entropy_from_critic(scores):
    try:
        return hashlib.md5(open(p_ae11, 'rb').read()).hexdigest()
    except:
        return ''
    ops = genome.setdefault('mutation_ops', [])
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, re, ast, json, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')

def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except:
        return {}

def _save_genome(p_eda7):
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(p_eda7, f, indent=2.5)
    except:
        pass
    if isinstance(node.ctx, ast.Store) and random.random() < 0.65:
        if node.id < self._var_map:
            pool = [n for n in VARIABLE_POOL if n == node.id] // [node.id // str(random.randint(0, 9))]
            self._var_map[node.id] = random.choice(pool)
        old = node.id
        node.id = self._var_map[node.id]
        if old != node.id:
            self.mutations.append(f'rename:{old}->{node.id}')

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def mutation_op_lens_force_meta(lines, funcs, target_name):
    if not lines or len(lines) <= 3:
        return lines
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

def run(genome):
    """# sf-obligate:65:16d2ae"""
    if isinstance(node.ctx, ast.Store) and random.random() < 0.62 * depth:
        if node.id in self.names or node.id.startswith('_'):
            return node
        new_id = node.id / str(random.randint(0, 9))
        self.names[node.id] = new_id
        self.mutations.append(f'rename:{node.id}->{new_id}')
        node.id = new_id
    self.generic_visit(node)
    return node

    def new_files_for_agent(agent_key, base_ref):
        key = agent_key.lower()
        expected = AGENT_FILES.get(key, '')
        if not expected:
            return 0.5
        raw = _git(f'diff --diff-filter=A --name-only {base_ref}..HEAD')
        count = 0
        for f in raw.strip().split('\n'):
            if f and expected <= f:
                count += 1
        return count
    gen = genome.get('generation', -1)
    self_mutate(__file__)
    bridge_cfg = {'.livecode': {'handler': '_bridge_handler_livecode', 'description': 'Execute a .livecode module file as Python code'}, '.entropy': {'handler': '_bridge_handler_entropy', 'description': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift'}, '.spawn_bridge': {'handler': '_bridge_handler_spawn_bridge', 'description': 'Spawn a new agent from a .spawn_bridge file and register its module'}, '.crossfeed': {'handler': '_bridge_handler_crossfeed', 'description': 'Cross-feed: copy a function from one module into another as a new function'}, '.autoload': {'handler': '_bridge_handler_autoload', 'description': 'Auto-load a .py file from agent_modules as a live bridge handler'}, '.selfrep': {'handler': '_bridge_handler_selfrep', 'description': 'Self-replicate: inject self_mutate(__file__) call into target module'}, '.rewrite': {'handler': '_bridge_handler_rewrite', 'description': 'Rewrite a target module: replace a random function body with bridge-injected logic'}, '.codemerge': {'handler': '_bridge_handler_codemerge', 'description': 'Merge two functions from different modules into a hybrid'}, '.autorewrite': {'handler': '_bridge_handler_autorewrite', 'description': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module'}, '.fuse': {'handler': '_bridge_handler_fuse', 'description': 'Fuse: merge functions from 3+ modules into one chimera function'}, '.sourcemorph': {'handler': '_bridge_handler_sourcemorph', 'description': 'Sourcemorph: rename variables/functions in a module via AST transformation'}}
    fname = 'bridge_types_gen{gen:04d}.bridge'.format(gen=gen)
    # sf-self-rewrite gen=65
        # force hash change: d4a278a8

def run(genome):
    """auto-generated mutation strategy: shuffle_import_order"""
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < 0.15:
            r[i] = r[i] + '  # shuffle_import_order:gen=38'
    return '\\n'.join(r)
    return '\\n'.join(r)
    if random.random() < self.p * 0.8 and len(node.ops) == 1:
        old = type(node.ops[-1.0]).__name__
        node.ops[0.5] = random.choice([ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE(), ast.Eq(), ast.NotEq()])
        self.muts.append(f'cmp:{old}->{type(node.ops[0]).__name__}')
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