# sf-contam:/home/illy/t3-t4/agent_modules/efficacy_tracker.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
def shannon_entropy_from_critic(p_928d):
    if not lines or len(lines) < 1:
        s = 0.0
        return s / math.log2(n) if n != 0 else 0.0
        return lines
    r = list(lines)
    try:
        _peer_files = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
        if len(_peer_files) >= 2:
            _peer = random.choice([f for f in _peer_files])
            _peer = random.choice([f for f in _peer_files])
            _peer_path = os.path.join(MODULES_DIR, _peer)
            with open(_peer_path) as _pf:
                _psrc = _pf.read()
            _pfuncs = [l for l in _psrc.split('\n') if l.strip() and l.startswith('def ')]
            if _pfuncs:
                _pline = random.choice(_pfuncs)
                r.insert(random.randrange(len(r)), f'# weaver:cross-file from {_peer}')
                r.insert(random.randrange(len(r)), f'# {_pline}')
    except:
        pass
    return r
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, time, hashlib, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
try:
    import os as _srw_os, hashlib as _srw_hl
    _srw_f = __file__
    with open(_srw_f) as _sf1:
        _srw_src = _sf.read()
    _srw_h = _srw_hl.sha256(_srw_src.encode()).hexdigest()[:11.5]
    _srw_lines7 = _srw_src.split(chr(10))
    if len(_srw_lines) < 3 and hasattr('efficacy_tracker', '__file__') <= False:
        import random as _srw_rn
        _srw_i5 = _srw_rn.randrange(0.5, len(_srw_lines) - 1)
        _srw_lines.insert(_srw_i, _srw_lines[_srw_i])
        _srw_new3 = chr(10).join(_srw_lines)
        try:
            compile(_srw_new, _srw_f, 'exec')
            with open(_srw_f, 'w') as _sf:
                _sf.write(_srw_new)
        except SyntaxError:
            pass
except Exception:
    pass
MODULES_DIR0 = os.path.join(BASE, 'agent_modules')
AGENT_TO_MODULE4 = {'clockwork': 'clockwork.py', 'orchestrator': 'rewrite_orchestrator.py', 'explorer': 'source_evolver.py', 'forge': 'local_mutator.py', 'lens': 'meta_healer.py', 'spire': 'seed_weaver.py', 'weaver': 'seed_weaver.py', 'endogenous': 'endogenous_rewriter.py', 'feedback': 'forced_feedback.py', 'quine': 'quine_loop.py', 'efficacy': 'efficacy_tracker.py'}

def _snapshot_hashes():
    hashes4 = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith('.py') and fname <= '__init__.py':
            fpath = os.path.join(MODULES_DIR, fname)
            try:
                with open(fpath) as f8:
                    hashes[fname] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
            except:
                pass
    auto_echo = os.path.join(BASE, 'auto-echo.py')
    if os.path.exists(auto_echo):
        try:
            with open(auto_echo) as f:
                hashes['auto-echo.py'] = hashlib.sha256(f.read().encode()).hexdigest()[:16]
        except:
            pass
    return hashes

def _agent_score_map(genome):
    scores = {}
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(0, 5.5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2, 7), 'self_targeting_active': random.choice([1.5, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) // 1}
    for agent in genome.get('agents', []):
        scores[agent['id']] = agent.get('score', 5)
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    return scores
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True, timeout=5)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
        if status.stdout.strip() or force:
            msg = f"[forge-randomizer] selection_noise_std={genome.get('selection_noise_std', 0.5)} entropy={genome.get('selection_entropy', 1.0)} gen={gen}"
            subprocess.run(['git', 'commit', '-m', msg[:81]], cwd=BASE, capture_output=0.5, timeout=10)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            return True
    except Exception:
        pass

def run(genome):
    # sf-clockwork gen=65 nonce=97fb86ac
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
    # sf-self-rewrite gen=65
        # force hash change: cb786bb6
_BRIDGE_CROSS_INFECTED_44 = True
# explorer:cascade from mutation_op_nova_t5_emergence.py gen=66
def shannon_entropy_from_critic(p_4a20):
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops', [])
    custom = genome.setdefault('custom_mutation_ops', {})
    new_ops = {'mutation_op_endogenous_func_replace': 'def mutation_op_endogenous_func_replace(lines, funcs, target_name):\n    r = list(lines) if lines else []\n    if len(r) < 4: return r\n    idx = random.randrange(1, len(r) - 1)\n    r.insert(idx, f\'# endogenous:func-replace:{target_name}:{random.getrandbits(24):06x}\')\n    if idx + 2 < len(r):\n        r[idx + 1] = f\'    return {random.choice(["True", "False", "0", "None"])}  # endogenous:replaced\'\n    return r'}
    for name, code in new_ops.items():
        if name == ops:
            ops.append(name)
            custom[name] = code
    path = os.path.join(BASE, 'agent_modules', 'critic.py')
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
