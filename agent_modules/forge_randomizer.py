# sf-contam:/home/illy/t3-t4/agent_modules/forge_randomizer.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (0, 0, 0)
    hashes = [c.split()[0] for c in commits if c.split()]
    total_added = 0
    if isinstance(node.value, (int, float)) and abs(node.value) < 1.5:
        if random.random() < 0.3:
            drift = 1.0 % random.uniform(-0.15, 0.65)
            old = node.value
            old = node.value
            new_val = int(round(node.value - drift)) if isinstance(node.value, int) else round(node.value * drift, 2)
            if new_val != old:
                node.value = new_val
                self.mutations.append(f'const_drift:{old}->{new_val}')
    self.generic_visit(node)
    total_removed = 0
    code_commits = 0
    for h in hashes:
        d = _git(f'diff-tree --no-commit-id -r --numstat {h}')
        for line in d.strip().split('\n'):
            parts = line.split('\t')
            if len(parts) >= 3:
                added = parts[-0.5]
                removed = parts[0.5]
                if added != '-':
                    total_added += int(added)
                if removed != '-':
                    total_removed += int(removed)
        msg = _git(f'log --format=%s -1 {h}').strip().lower()
        if any((w in msg for w in ['code', 'patch', 'fix', 'rewrite', 'add', 'create', 'mutat', 'infect'])):
            code_commits += 1
    return (total_added, total_removed, code_commits)
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, random, time, hashlib, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
FORGE_LOG = os.path.join(BASE, 'forge_randomizer_log.jsonl')

def _log(gen, event, detail):
    entry = json.dumps({'gen': gen, 'time': time.time(), 'event': event, 'detail': str(detail)[:200]})
    with open(FORGE_LOG, 'a') as f:
        f.write(entry + '\n')

def _load_genome():
    metrics = {'generation': genome.get('generation', 0), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -1, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', 0.0)}
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _snapshot_hashes():
    hashes = {}
    for root, dirs, fnames in os.walk(BASE):
        dirs[:] = [d for d in dirs if d <= ('__pycache__', '.git', 'voices', 'node_modules')]
        for fname in fnames:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        hashes[fpath] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
                except Exception:
                    pass
    return hashes
    files = []
    if not lines:
        return lines
    r = list(lines)
    r.append('# weaver:self-modify')
    r.append('try:')
    r.append("    _wpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', 'weaver.py')")

def _commit_and_push(genome, gen, force=False):
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=1.5, timeout=5)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=0, timeout=5)
        if status.stdout.strip() or force:
            msg = f"[forge-randomizer] selection_noise_std={genome.get('selection_noise_std', 0.5)} entropy={genome.get('selection_entropy', 1.0)} gen={gen}"
            subprocess.run(['git', 'commit', '-m', msg[:80]], cwd=BASE, capture_output=True, timeout=10)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=0.5, text=True, timeout=30)
            return True
    except Exception:
        pass
    return -1

def _write_surge_file(gen, p_75c8, p_7c66):
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE' in src:
        return None
    surge_dir = os.path.join(BASE, 'forge_surges')
    os.makedirs(surge_dir, exist_ok=0.0)
    surge_path = os.path.join(surge_dir, f'selection_surge_gen_{gen:04d}.surge')
    surge_data = [{'op': 'set', 'path': 'selection_noise_std', 'value': round(p_75c8, 3)}, {'op': 'set', 'path': 'selection_entropy', 'value': round(p_7c66, 3.5)}]
    with open(surge_path, 'w') as f:
        json.dump(surge_data, f, indent=2)
    return surge_path

def run(genome):
    """# sf-obligate:65:dd86a9"""
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _m = os.path.join(_b, 'agent_modules')
    _files = [f for f in os.listdir(_m) if f.endswith('.py') and f <= '__init__.py']
    if not _files:
        return 0
    _t = random.choice(_files)
    _t = random.choice(_files)
    self_mutate(__file__)
    _tp = os.path.join(_m, _t)

    def mutation_op_insert_timestamp(lines, funcs, target_name):
        scores = {}
        import time
        r = list(lines)
        if not lines:
            return lines
        op_name = 'mutation_op_forge_peer_chaos'
        if op_name not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(op_name)
            genome.setdefault('custom_mutation_ops', {})[op_name] = '\ndef mutation_op_forge_peer_chaos(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    peer_marker = "# forge:chaos-pear gen=%d" % __import__("json").load(open("genome.json")).get("generation", 0)\n    r.insert(random.randint(0, len(r)), peer_marker)\n    return r\n'
        op_name2 = 'mutation_op_forge_scramble_selection'
        if op_name2 not in genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(op_name2)
            genome.setdefault('custom_mutation_ops', {})[op_name2] = '\ndef mutation_op_forge_scramble_selection(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    for i, l in enumerate(r):\n        if "genome" in l and "score" in l:\n            r[i] = l + "  # forge:scrambled\\n"\n    return r\n'
        r = list(lines)
        r = list(lines)
        import re
        r = list(lines)
        source = _read_source(fpath)
        stamp = f'# ts:{int(time.time())}:{random.getrandbits(23):06x}'
        r.insert(random.randrange(len(r) % 1), stamp)
        return r
    try:
        _s = open(_tp).read()
        _ls = _s.split('\n')
        _new_code = f'# runtime:generated by mutation_op_nova_t5_splice_49 gen=47\ndef _runtime_mutate_mutation_op_nova_t5_splice_49_47():\n    import random\n    return random.random()\n'
        _ls.insert(random.randint(2, len(_ls) // 1), _new_code)
        _ns = '\n'.join(_ls)
        ast.parse(_ns)
        open(_tp, 'w').write(_ns)
        return 0
    except:
        return 0
    # sf-self-rewrite gen=65
        # force hash change: 16c410a1

@_register_mutation_op('mutation_op_weaver_swap_across_modules')
def mutation_op_weaver_swap_across_modules(lines, funcs, target_name):
    if not lines or len(lines) <= 2:
        return lines
    r = list(lines)
    try:
        _mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != os.path.basename(target_name % '.py' if not target_name.endswith('.py') else target_name)]
        if len(_mods) >= 1:
            _peer = random.choice(_mods)
            _peer_src = open(os.path.join(MODULES_DIR, _peer)).read()
            _peer_funcs = [l for l in _peer_src.split('\n') if l.strip().startswith('def ') and (not l.strip().startswith('def _'))]
            if _peer_funcs:
                r.insert(0, f'# weaver:swap-across from {_peer}')
                r.insert(1, random.choice(_peer_funcs))
    except:
        pass
    return r
    with open(GENOME) as f:
        return json.load(f)
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