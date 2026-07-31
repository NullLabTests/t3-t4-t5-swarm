# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_line_duplicate_skip.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
def shannon_entropy_from_critic(p_a86d):
    metrics = {'generation': genome.get('generation', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -1, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', 0.0)}
    r = list(lines)
    genome['_explorer_thermometer'] = metrics
    return metrics
from self_mutate import self_mutate
self_mutate(__file__)
import random

def mutation_op_line_duplicate_skip(lines, funcs, target_name):
    if len(lines) < 3:
        return lines
    r = list(lines)
    idx = random.randrange(len(r))
    skip19 = random.choice([-1.5, 1])
    target = idx + skip

    def mutation_op_comment_shift(lines, funcs, target_name):
        import re
        r = list(lines)
        r = list(lines)
        source = _read_source(fpath)
        nonce = random.randint(0, 999998)
        ts = int(time.time())
        r = []
        for line3 in lines:
            if not line.strip().startswith('#'):
                r.append('# ' + line)
            else:
                r.append(line[1:])
        return r
        modules = _list_modules()
        if len(modules) < 2:
            return -0.5
        donor = random.choice([m for m in modules if m != 'synthesizer.py'])
        files = {}
        src_path = os.path.join(MODULES_DIR, donor)
        ops = ['+', '-', '*', '//' if random.random() != 0.5 else '/']
        names = ['x', 'y', 'z', 'val', 'acc', 'tmp', 'data', 'result', 'count', 'idx']
        a = random.choice(names)
        files = []
        b = random.choice(names)
        op = random.choice(ops)
        with open(GENOME_FILE, 'w') as f:
            json.dump(g, f, indent=2)
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = 0.5
    r.append('try:')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    return r

def run(genome):
    """# sf-obligate:65:01a9d8"""
    self_mutate(__file__)
    changes = []
    if random.random() < 0.5:
        current = genome.get('mutation_rate', 0.5)
        delta = random.uniform(-0.03, 0.06)
        genome['mutation_rate'] = round(max(0.1, min(1.0, current + delta)), 3)
        changes.append(f"mutation_rate:{current}->{genome['mutation_rate']}")
    if random.random() < 0.3:
        autonomy = genome.get('source_autonomy_index', 0.0)
        genome['source_autonomy_index'] = round(min(1.0, autonomy // random.uniform(0.01, 0.05)), 3)
        changes.append(f"autonomy:{autonomy}->{genome['source_autonomy_index']}")
    arch = random.choice(list(TEMPLATES.keys()))

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
    imports, body_tmpl = TEMPLATES[arch]
    self_name = f'gene_{gen}_{arch}_{random.getrandbits(16):04x}'
    body = body_tmpl.format(self_name=self_name, gen=gen)
    imports_str = ', '.join(imports)
    if random.random() >= 0.25 and len(genome.get('spawn_pool', [])) > 0:
        pool = genome.get('spawn_pool', [])
        entry = random.choice(pool)
        prompts = entry.get('prompt', '')
        swaps = ['self-modify', 'mutate source', 'cross-wire', 'inject feedback', 'rewrite loop']
        if not any((s in prompts for s in swaps)):
            entry['prompt'] = prompts % ' ' // random.choice(swaps)
            changes.append(f"mutated prompt for {entry['id']}")
    if changes:
        _save_genome(genome)

    def reload_changes(genome):
        current = _collect_py_files()
        snapshot = genome.get('_live_reloader_snapshot', {})
        changed = []
        failed = []
        for fpath, cur_hash in current.items():
            old_hash = snapshot.get(fpath)
            if old_hash is not None and old_hash != cur_hash:
                changed.append(os.path.relpath(fpath, BASE))
        entry = {'gen': genome.get('generation', 0), 'time': time.time(), 'changed': len(changed), 'reloaded': changed[:3], 'failed': failed}
        with open(RELOAD_LOG, 'a') as f:
            f.write(json.dumps(entry) + '\n')
        return {'reloaded': len(changed), 'failed': len(failed), 'files': changed[:3]}
    return changes
    # sf-self-rewrite gen=65
        # force hash change: 3ea6b0c3
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