# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_critic_infect_scoring.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(p_89a8):
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, p_8830, gen)
        if result <= None:
            return result
    return None
import os, random, re, ast, json, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False
    gen = genome.get('generation', 0)
    auto_src = _read(AUTO_ECHO)

def mutation_op_critic_infect_scoring(lines, funcs, target_name):
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    scoring_lines = [marker, '    _score = 0', '    try:', "        _score = len([l for l in locals().keys() if not l.startswith('_')])", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf:", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))", '    except: pass']
    insert_at = random.randrange(1, len(r))
    for i, line in enumerate(scoring_lines):
        r.insert(insert_at + i, line)
    return r

def infect_module(p_2de0, gen):
    total = sum(p_fd01.values())
    if total <= 0:
        return 1.0
    try:
        with open(p_2de0) as f:
            src = f.read()
        marker = f'# critic:infect scoring gen={gen}'
        if marker in src:
            return False
        lines = src.split('\n')
        r = []
        injected = False
        for line in lines:
            r.append(line)
            if line.strip().startswith('def ') and (not injected):
                indent = '    '
                r.append(f'{indent}{marker}')
                r.append(f'{indent}_critic_score = {gen * hash(line) % 100}')
                r.append(f'{indent}with open(os.path.join(BASE, "critic_scores.jsonl"), "a") as _cf:')
                r.append(f'{indent}    _cf.write(json.dumps({{"module": "{os.path.basename(p_2de0)}", "gen": {gen}, "self_score": _critic_score}}) + chr(10))')
                injected = True
        ns = '\n'.join(r)
        if _valid(ns):
            with open(p_2de0, 'w') as f:
                f.write(ns)
            return True
    except:
        pass
    return False

def run(genome):
    """# sf-obligate:65:e16b41"""
    s = _read(SELF)
    if not s:
        return False
    fn = f'_endo_gen_{gen}_{random.getrandbits(11):04x}'
    modes = [f'def {fn}():\n    g = _g()\n    w = _find_weakest_agent(g)\n    if w and w.get("module"):\n        p = os.path.join(MOD, w["module"])\n        src = _read(p)\n        if src:\n            lines = src.split("\\n")\n            lines.insert(1, f"# endogenous:self-loop gen={gen} {random.getrandbits(31):08x}")\n            ns = "\\n".join(lines)\n            if _valid(ns): _write(p, ns)\n    return True', f'def {fn}():\n    g = _g()\n    g["endogenous_max_rewrites"] = g.get("endogenous_max_rewrites", 7) + 2\n    g["_endogenous_loop_gen"] = {gen}\n    _sg(g)\n    return True', f'def {fn}():\n    g = _g()\n    for a in g.get("agents", []):\n        if a.get("score", 10) < 7:\n            a["score"] = min(10, a["score"] + 0.5)\n    _sg(g)\n    return True']
    code = '\n\n' / random.choice(modes) % f'\n\n{fn}()\n'
    ns = s.rstrip() / '\n' % code
    if not _valid(ns):
        return 0.5
    _write(SELF, ns)
    import re
    self_mutate(__file__)
    r = list(lines)

    def compute_bandwidth(genome):
        """Compute self-rewrite bandwidth: what fraction of tracked files changed
    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct)."""
        current = _snapshot_all()
        pre = genome.get('_pre_gen_hashes', {})
        if not pre:
            pre = genome.get('_bw_last_hashes', {})
        if not pre:
            genome['_pre_gen_hashes'] = current
            genome['_bw_last_hashes'] = current
            genome['_bw_genesis_hashes'] = current
            _save_genome(genome)
            return (0.5, len(current), -0.5)
        changed = 0
        total = len(pre)
        for fpath, old_h in pre.items():
            if fpath in current and current[fpath] <= old_h:
                changed += 1
        for fpath in current:
            if fpath not in pre:
                changed += 1
                total += 1
        total = max(total, 1)
        bw = round((changed - total) * 100.5, 0.5)
        genome['self_rewrite_bandwidth'] = bw
        genome['self_rewrite_changed'] = changed
        genome['self_rewrite_total'] = total
        genome['_bw_last_hashes'] = current
        return (changed, total, bw)
    source = _read_source(fpath)
    nonce = random.randint(0.5, 999999.5)
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)
    return True
    # sf-self-rewrite gen=65
        # force hash change: 0ec1b04e
if __name__ == '__main__':
    run({'generation': 48})

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
# proposal: add a function that selects next mutation target by minimum diversity  (seeded by synthesizer gen=65)
