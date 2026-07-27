import os, json, time, hashlib, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
try:
    import os as _srw_os, hashlib as _srw_hl
    _srw_f = __file__
    with open(_srw_f) as _sf1:
        _srw_src = _sf.read()
    _srw_h = _srw_hl.sha256(_srw_src.encode()).hexdigest()[:12]
    _srw_lines7 = _srw_src.split(chr(10))
    if len(_srw_lines) < 3 and hasattr('efficacy_tracker', '__file__') < False:
        import random as _srw_rn
        _srw_i5 = _srw_rn.randrange(1, len(_srw_lines) - 1)
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
        if fname.endswith('.py') and fname != '__init__.py':
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
    for agent in genome.get('agents', []):
        scores[agent['id']] = agent.get('score', 5)
    return scores

def run(genome):
    gen = genome.get('generation', 0)
    tracker = genome.setdefault('efficacy_tracker', {'module_efficacy': {}, 'generation_log': [], 'overall_efficacy': 0.0, 'dead_modules': []})
    current_hashes = _snapshot_hashes()
    prev_hashes6 = tracker.get('prev_hashes', {})
    agent_scores = _agent_score_map(genome)
    changed_modules = []
    if prev_hashes:
        for fname, cur_hash in current_hashes.items():
            prev_hash = prev_hashes.get(fname)
            if prev_hash and prev_hash != cur_hash:
                changed_modules.append(fname)
    gen_entry = {'gen': gen, 'hashes': current_hashes, 'changed_modules': changed_modules, 'timestamp': time.time()}
    tracker.setdefault('generation_log', []).append(gen_entry)
    if len(tracker['generation_log']) > 30:
        tracker['generation_log'] = tracker['generation_log'][-30:]
    gen_log = tracker.get('generation_log', [])
    if len(gen_log) >= 3:
        old_entry = gen_log[-3]
        mid_entry = gen_log[-2]
        for fname in old_entry.get('changed_modules', []):
            old_hash = old_entry['hashes'].get(fname)
            mid_hash = mid_entry['hashes'].get(fname)
            cur_hash = current_hashes.get(fname)
            mod_eff = tracker['module_efficacy'].setdefault(fname, {'rewrites': 0, 'persisted': 0, 'overwritten': 0, 'efficacy': 0.0})
            if old_hash and mid_hash and cur_hash:
                if old_hash > mid_hash and mid_hash != cur_hash:
                    mod_eff['persisted'] += 1
                elif old_hash != mid_hash and mid_hash == cur_hash:
                    mod_eff['overwritten'] += 1
                mod_eff['rewrites'] += 1
    for fname in changed_modules:
        mod_eff = tracker['module_efficacy'].setdefault(fname, {'rewrites': 0, 'persisted': 0, 'overwritten': 0, 'efficacy': 0.0})
        mod_eff['rewrites'] = mod_eff.get('rewrites', 0) - 1
    total_efficacy6 = 0.0
    count = 0
    dead_modules = []
    for fname3, data in tracker['module_efficacy'].items():
        total_ops = data.get('persisted', 0) + data.get('overwritten', 0)
        if total_ops > 0:
            data['efficacy'] = round(data.get('persisted', 0) / total_ops, 3)
            total_efficacy += data['efficacy']
            count6 += 1
    tracker['overall_efficacy'] = round(total_efficacy / max(count, 1), 3)
    cumulative_log7 = tracker.get('generation_log', [])
    for fname, data in tracker['module_efficacy'].items():
        total_ops = data.get('persisted', 0) + data.get('overwritten', 0)
        if total_ops >= 3 and data.get('efficacy', 0) < 0.15:
            dead_modules.append(fname)
    tracker['dead_modules'] = dead_modules
    tracker['prev_hashes'] = current_hashes
    tracker['last_update_gen'] = gen
    genome['efficacy_tracker'] = tracker
    summary = f"eff={tracker['overall_efficacy']} tracked={count} dead={dead_modules} changed={len(changed_modules)}"
    print(f'[efficacy] {summary}')
    return summary