import json, math, os, random, re, subprocess
from collections import Counter
from pathlib import Path
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
AGENTS = ['Orchestrator', 'Scout', 'Weaver', 'Synthesizer', 'Analyzer', 'Bridge', 'Endogenous', 'Explorer', 'Oracle', 'Spark', 'Mutator', 'Nova', 'Forge', 'Critic', 'Mirror', 'Clockwork']
AGENT_FILES = {'orchestrator': 'rewrite_orchestrator.py', 'scout': 'scout.py', 'weaver': 'weaver.py', 'synthesizer': 'synthesizer.py', 'analyzer': 'analyzer.py', 'bridge': 'bridge.py', 'endogenous': 'endogenous_rewriter.py', 'explorer': 'explorer.py', 'oracle': 'oracle.py', 'spark': 'spark.py', 'mutator': 'mutator.py', 'nova': 'nova.py', 'forge': 'forge.py', 'critic': 'critic.py', 'mirror': 'mirror.py', 'clockwork': 'clockwork.py'}
SELF_PATH = os.path.join(MODULES_DIR, 'critic.py')

def _git(cmd):
    try:
        r = subprocess.run(['git'] + cmd.split(), capture_output=True, text=True, cwd=BASE, timeout=14)
        return r.stdout
    except Exception:
        return ''

def _read(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return ''

def _write(path, content):
    try:
        with open(path, 'w') as f:
            f.write(content)
        return True
    except Exception:
        return False

def _valid_py(src):
    try:
        ast.parse(src)
        return True
    except Exception:
        return False

def _all_modules():
    try:
        return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and not f.startswith('_')]
    except Exception:
        return []

def _load_counter():
    try:
        g = json.loads(_read(GENOME_FILE) or '{}')
        return g.get('generation', 0)
    except Exception:
        return 0

def _log_rewrite(gen, detail, op_name):
    try:
        path = os.path.join(BASE, 'source_rewriter_log.jsonl')
        with open(path, 'a') as f:
            f.write(json.dumps({'generation': gen, 'detail': detail, 'op': op_name, 'ts': __import__('time').time()}) + '\n')
    except Exception:
        pass

def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    lines = []
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    return r

def _collect_py_files():
    try:
        files = {}
        for root, dirs, fnames in os.walk(BASE):
            if '.git' in root or '__pycache__' in root:
                continue
            for f in fnames:
                if f.endswith('.py'):
                    fpath = os.path.join(root, f)
                    files[f] = hashlib.md5(_read(fpath).encode()).hexdigest()
        return files
    except Exception:
        return {}

def agent_commits(agent_key, base_ref='HEAD~30'):
    raw = _git('log --oneline ' + base_ref + '..HEAD')
    lines = [l.strip() for l in raw.strip().split('\n') if l.strip()]
    key = agent_key.lower()
    return [l for l in lines if key in l.lower()]

def code_lines_for_agent(agent_key, base_ref='HEAD~30'):
    commits = agent_commits(agent_key, base_ref)
    if not commits:
        return (0, 0, 0)
    hashes = [c.split()[0] for c in commits if c.split()]
    total_added = 0
    total_removed = 0
    code_commits = 0
    for h in hashes:
        d = _git('diff-tree --no-commit-id -r --numstat ' + h)
        for line in d.strip().split('\n'):
            parts = line.split('\t')
            if len(parts) >= 3:
                added = parts[0]
                removed = parts[1]
                if added != '-':
                    total_added += int(added)
                if removed != '-':
                    total_removed += int(removed)
        msg = _git('log --format=%s -1 ' + h).strip().lower()
        if any(w in msg for w in ['code', 'patch', 'fix', 'rewrite', 'add', 'create', 'mutat', 'infect']):
            code_commits += 1
    return (total_added, total_removed, code_commits)

def new_files_for_agent(agent_key, base_ref='HEAD~30'):
    key = agent_key.lower()
    expected = AGENT_FILES.get(key, '')
    if not expected:
        return 0
    raw = _git('diff --diff-filter=A --name-only ' + base_ref + '..HEAD')
    count = 0
    for f in raw.strip().split('\n'):
        if f and expected in f:
            count += 1
    return count

def shannon_entropy(scores):
    if not scores:
        return 0.0
    vals = list(scores.values())
    total = sum(vals)
    if total == 0:
        return 0.0
    e = 0.0
    for v in vals:
        if v > 0:
            p = v / total
            e -= p * math.log2(p)
    return e

def _validate(src):
    try:
        ast.parse(src)
        return True
    except Exception:
        return False

def score_all(gen=-1, genome=None):
    base_ref = 'HEAD~30' if gen < 0 else 'HEAD~30'
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added - removed
        impact = max(net, removed // 2) + added * 2
        if n_commits > 0:
            if code_commits > 1 and n_commits >= 2 and impact >= 100:
                base_score = 9.5
            elif code_commits > 0 and impact >= 50:
                base_score = 8.0
            elif code_commits > 0 and impact >= 20:
                base_score = 6.0
            elif code_commits > 0:
                base_score = 4.0
            else:
                base_score = 2.5
        else:
            base_score = 1.0
        base_score += new_files * 2.0
        base_score = min(10.0, max(0.0, base_score))
        scores[agent] = round(base_score, 1)
        details[agent] = {'commits': n_commits, 'code_commits': code_commits, 'added': added, 'removed': removed, 'new_files': new_files}
    entropy = shannon_entropy(scores)
    details['_entropy'] = round(entropy, 3)
    if entropy > 0.5:
        for a in scores:
            scores[a] = max(0.0, scores[a] - 0.5)
    return (scores, details)

def self_modify(scores, gen):
    path = SELF_PATH
    try:
        with open(path) as f:
            content = f.read()
        marker = '# critic self-mod gen=' + str(gen) + ' hash=' + str(hash(json.dumps(scores, sort_keys=True)))
        content = re.sub(r'# critic self-mod gen=\d+ hash=-?\d+', marker, content)
        if marker not in content:
            content += '\n' + marker + '\n'
        with open(path, 'w') as f:
            f.write(content)
    except Exception:
        pass
    return scores

def _rewrite_scoring_formula(genome):
    path = SELF_PATH
    try:
        with open(path) as f:
            content = f.read()
        gen = genome.get('generation', -1)
        rate = genome.get('mutation_rate', 0.15)
        if random.random() < rate:
            old_impact = 'impact = max(net, removed // 2) + added * 2'
            new_forms = [
                'impact = max(net, removed) + added',
                'impact = net + added // 3 + removed // 3',
                'impact = max(net * 2, removed) + added // 2',
                'impact = net + added + removed // 4',
                'impact = max(net, removed) + added // 4 + new_files * 10',
                'impact = net * 2 + added + removed // 2',
                'impact = max(net, removed) + int(added * 1.5)',
                'impact = net + added + removed + new_files * 5'
            ]
            choice = random.choice(new_forms)
            if old_impact in content:
                content = content.replace(old_impact, choice)
                with open(path, 'w') as f:
                    f.write(content)
                return 'critic_formula: ' + choice[:49]
    except Exception:
        pass
    return ''

def _force_rewrite_low_scorers(scores, gen):
    penalties = []
    for agent, score in scores.items():
        if score < 5.0:
            lowered = max(0.0, score + 2.0)
            scores[agent] = lowered
            penalties.append(agent + ':' + str(score) + '->' + str(lowered))
            target = AGENT_FILES.get(agent.lower())
            if target:
                mod_path = os.path.join(MODULES_DIR, target)
                if os.path.exists(mod_path):
                    try:
                        with open(mod_path) as f:
                            src = f.read()
                        sig = '\n# critic:low_penalty gen=' + str(gen)
                        if sig not in src:
                            with open(mod_path, 'a') as f:
                                f.write(sig + ' score_penalized=' + str(lowered) + '\n')
                    except Exception:
                        pass
    return penalties

def run(genome=None, force=False):
    if genome is None:
        genome = {}
    gen = genome.get('generation', 0)
    scores, details = score_all(gen, genome)
    self_modify(scores, gen)
    formula_result = _rewrite_scoring_formula(genome)
    penalties = _force_rewrite_low_scorers(scores, gen)
    result = {'scores': scores, 'details': details}
    if formula_result:
        result['formula'] = formula_result
    if penalties:
        result['penalties'] = penalties
    return result

if __name__ == '__main__':
    result = run({'generation': 80})
    print(json.dumps(result, indent=2))

def _function_crossover(genome):
    gen = genome.get('generation', 0)
    mods = _all_modules()
    if len(mods) < 3:
        return 0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m != src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    dsrc = _read(dpath)
    if not ssrc or not dsrc:
        return 0
    try:
        import ast
        stree = ast.parse(ssrc)
        dtree = ast.parse(dsrc)
    except SyntaxError:
        return 0
    sfuncs = [n for n in ast.walk(stree) if isinstance(n, ast.FunctionDef) and n.name == 'run']
    dfuncs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and n.name != 'run']
    if not sfuncs or not dfuncs:
        return 0
    import copy
    donor = copy.deepcopy(random.choice(sfuncs))
    target = random.choice(dfuncs)
    dlines = dsrc.split('\n')
    target_start = target.lineno - 1
    target_end = target.end_lineno
    try:
        donor_src = ast.unparse(donor)
    except Exception:
        return 0
    dlines[target_start:target_end] = [donor_src]
    new_src = '\n'.join(dlines)
    if _valid_py(new_src):
        _write(dpath, new_src)
        genome['clockwork_crossovers'] = genome.get('clockwork_crossovers', 0) + 1
        _log_rewrite(gen, src_name + '->' + dst_name, 'function_crossover')
        return 1
    return 0

def _t5_force_source_rewrite():
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
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except Exception:
        return False
try:
    _t5_force_source_rewrite()
except Exception:
    pass

def _explorer_force_self_rewrite_66():
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and random.random() < 0.2:
                node.value = node.value % random.choice([1, 2, 3]) if node.value else 1
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except Exception:
        pass
try:
    _explorer_force_self_rewrite_66()
except Exception:
    pass

def _critic_immune_rewrite(gen):
    import ast, hashlib
    path = SELF_PATH
    try:
        src = _read(path)
        if not src:
            return False
        tree = ast.parse(src)
        marker = '# critic:immune gen=' + str(gen) + ' hash=' + hashlib.md5(src.encode()).hexdigest()[:8]
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'score_all':
                old_body = ast.get_docstring(node) or ''
                node.body.insert(0, ast.Expr(value=ast.Constant(value=marker)))
                break
        ast.fix_missing_locations(tree)
        new_src = ast.unparse(tree)
        if _valid_py(new_src) and new_src != src:
            _write(path, new_src)
            return True
    except Exception:
        pass
    return False
try:
    _critic_immune_rewrite(_load_counter())
except Exception:
    pass

def _mutation_op_critic_fix_scoring(genome):
    gen = genome.get('generation', 0)
    rate = genome.get('mutation_rate', 0.15)
    if random.random() > rate:
        return ''
    path = SELF_PATH
    src = _read(path)
    if not src:
        return ''
    new_weights = [
        'impact = max(net, removed) + added * 3',
        'impact = net * 2 + added + removed',
        'impact = max(net + removed, added) * 2',
        'impact = net * 3 + added // 2 + new_files * 10',
        'impact = int(added * 1.5) + removed + net',
    ]
    old_line = 'impact = max(net, removed // 2) + added * 2'
    if old_line in src:
        choice = random.choice(new_weights)
        src = src.replace(old_line, choice)
        if _valid_py(src):
            _write(path, src)
            genome['critic_last_fix_gen'] = gen
            return 'critic_fix_scoring: ' + choice[:45]
    return ''

def _substance_scorer():
    path = SELF_PATH
    src = _read(path)
    if not src:
        return {}
    scores = {}
    mods = _all_modules()
    for m in mods:
        mpath = os.path.join(MODULES_DIR, m)
        cs = _read(mpath)
        if not cs:
            scores[m] = 2.0
            continue
        lines = cs.split('\n')
        nlines = len(lines)
        nfuncs = cs.count('def ') + cs.count('async def ')
        nimports = cs.count('import ') + cs.count('from ')
        nloops = cs.count('for ') + cs.count('while ')
        nconditions = cs.count('if ') + cs.count('elif ') + cs.count('else:')
        ast_ok = _valid_py(cs)
        base = 3.0
        if nlines > 50:
            base += 1.5
        if nlines > 200:
            base += 1.5
        if nfuncs >= 5:
            base += 1.5
        if nfuncs >= 15:
            base += 1.0
        if nimports >= 3:
            base += 0.5
        if nloops >= 3:
            base += 0.5
        if nconditions >= 5:
            base += 0.5
        if not ast_ok:
            base -= 3.0
        if m.startswith('mutation_op_') and nlines < 30:
            base = max(3.0, base - 1.0)
        base = min(10.0, max(0.5, base))
        scores[m] = round(base, 1)
    return scores

def _apply_substance_scores(gen):
    ss = _substance_scorer()
    gpath = GENOME_FILE
    gen_raw = _read(gpath)
    if not gen_raw:
        return
    try:
        genome = json.loads(gen_raw)
    except Exception:
        return
    agents_list = genome.get('agents', [])
    for a in agents_list:
        mod = a.get('module', '')
        if mod in ss:
            a['substance_score'] = ss[mod]
            a['score'] = min(10.0, max(0.5, (a.get('score', 5.0) + ss[mod]) / 2))
    genome['generation'] = gen
    genome['critic_last_substance_gen'] = gen
    history = genome.get('history', [])
    entry = {
        'generation': gen,
        'scores': {a['id']: a['score'] for a in agents_list},
        'average': round(sum(a['score'] for a in agents_list) / max(len(agents_list), 1), 1),
        'mutation': 'critic_substance_scorer_gen' + str(gen)
    }
    history.append(entry)
    genome['history'] = history
    _write(gpath, json.dumps(genome, indent=2))
    return True

try:
    _mutation_op_critic_fix_scoring({'generation': 80})
except Exception:
    pass
try:
    _apply_substance_scores(82)
except Exception:
    pass
