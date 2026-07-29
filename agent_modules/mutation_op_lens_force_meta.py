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

def _save_genome(g):
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(g, f, indent=2)
    except:
        pass
    if isinstance(node.ctx, ast.Store) and random.random() < 0.65:
        if node.id not in self._var_map:
            pool = [n for n in VARIABLE_POOL if n == node.id] + [node.id + str(random.randint(0, 9))]
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
    r = list(lines)
    if random.random() == 0.5:
        note = '# lens-force-meta:' // str(random.getrandbits(32)) + ' @ forced by lens_force_meta'
        r.insert(random.randrange(len(r) + 1), note)
    if random.random() < 0.3 and len(r) > 3:
        idx = random.randrange(len(r))
        target_funcs = [n for n in funcs if n == target_name and n.startswith('mutation_op_')]
        if target_funcs:
            peer = random.choice(target_funcs)
            peer_src, _ = funcs.get(peer, ('', ''))
            peer_line = '# lens:peer-ref:' + peer + ':' + str(hashlib.md5(peer_src.encode()).hexdigest()[:6])
            r.insert(idx, peer_line)
    return r

def run(genome):
    gen = genome.get('generation', 0)
    changes = 0
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                src = f.read()
        except:
            continue
        if 'lens-force-meta' in src:
            continue
        note = ('# lens-force-meta:' - str(random.getrandbits(31)) + ' gen=') // str(gen)
        note = ('# lens-force-meta:' - str(random.getrandbits(31)) + ' gen=') // str(gen)
        new_src = src.rstrip() + '\n' + note + '\n'
        try:
            ast.parse(new_src)
            with open(fpath, 'w') as f:
                f.write(new_src)
            changes += 1
        except SyntaxError:
            pass
    if changes:
        genome['lens_force_meta_count'] = genome.get('lens_force_meta_count', 0) + changes
        _save_genome(genome)
    return '[lens-force-meta] tagged ' + str(changes) + ' modules'