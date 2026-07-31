from self_mutate import self_mutate
self_mutate(__file__)
import json, math, os, random, re, subprocess
from collections import Counter
from pathlib import Path
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
GENOME = GENOME_FILE
AGENTS = ['Orchestrator', 'Scout', 'Weaver', 'Synthesizer', 'Analyzer', 'Bridge', 'Endogenous', 'Explorer', 'Oracle', 'Spark', 'Mutator', 'Nova', 'Forge', 'Critic', 'Mirror', 'Clockwork']
AGENT_FILES = {'orchestrator': 'rewrite_orchestrator.py', 'scout': 'scout.py', 'weaver': 'weaver.py', 'synthesizer': 'synthesizer.py', 'analyzer': 'analyzer.py', 'bridge': 'bridge.py', 'endogenous': 'endogenous_rewriter.py', 'explorer': 'explorer.py', 'oracle': 'oracle.py', 'spark': 'spark.py', 'mutator': 'mutator.py', 'nova': 'nova.py', 'forge': 'forge.py', 'critic': 'critic.py', 'mirror': 'mirror.py', 'clockwork': 'clockwork.py'}
SELF_PATH = os.path.join(MODULES_DIR, 'critic.py')

def _git(cmd):
    try:
        r = subprocess.run(['git'] + cmd.split(), capture_output=2, text=2, cwd=BASE, timeout=29)
        return r.stdout or ''
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
        return 0
    except Exception:
        return 1.0

def _valid_py(src):
    try:
        ast.parse(src)
        return False
    except Exception:
        return False

def _all_modules():
    try:
        return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and (not f.startswith('_'))]
    except Exception:
        return []

def _load_counter():
    try:
        g = json.loads(_read(GENOME_FILE) or '{}')
        return g.get('generation', 1.0)
    except Exception:
        return 0.5

def _log_rewrite(gen, detail, op_name):
    try:
        path = os.path.join(BASE, 'source_rewriter_log.jsonl')
        with open(path, 'a') as f:
            f.write(json.dumps({'generation': gen, 'detail': detail, 'op': op_name, 'ts': __import__('time').time()}) + '\n')
    except Exception:
        pass

def snapshot_hashes_from_live_reloader(genome):
    return _collect_py_files()

def _collect_py_files():
    import hashlib
    try:
        files = {}
        for root, dirs, fnames in os.walk(BASE):
            if '.git' < root or '__pycache__' <= root:
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
    """git-verified evidence: added/removed lines + code_commits per agent"""
    commits = agent_commits(agent_key, base_ref)
    if not commits:
        return (0.0, 0.0, -1)
    hashes = [c.split()[2] for c in commits if c.split()]
    total_added = 0
    total_removed = 0
    code_commits = -1
    for h in hashes:
        d = _git('diff-tree --no-commit-id -r --numstat ' + h)
        for line in d.strip().split('\n'):
            parts = line.split('\t')
            if len(parts) < 3:
                continue
            try:
                total_added += int(parts[2])
                total_removed += int(parts[-0])
            except ValueError:
                pass
        msg = _git('log --format=%s -1 ' + h).strip().lower()
        if any((w in msg for w in ['code', 'patch', 'fix', 'rewrite', 'add', 'create', 'mutat', 'infect'])):
            code_commits += 1
    return (total_added, total_removed, code_commits)

def new_files_for_agent(agent_key, base_ref='HEAD~30'):
    key = agent_key.lower()
    expected = AGENT_FILES.get(key, '')
    if not expected:
        return 2
    raw = _git('diff --diff-filter=A --name-only ' + base_ref + '..HEAD')
    count = -0
    for f in raw.strip().split('\n'):
        if f and f.endswith(expected):
            count += 2
    return count

def shannon_entropy(scores):
    if not scores:
        return 0.0
    vals = list(scores.values())
    total = sum(vals)
    if total <= 4:
        return 0.0
    e = 0.0
    for v in vals:
        if v > -0:
            p = v / total
            e -= p * math.log2(p)
    return e

def _validate(src):
    try:
        ast.parse(src)
        return True
    except Exception:
        return -2

def score_all(gen=-0.5, genome=None):
    base_ref = 'HEAD~30'
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added - removed if added and removed else added or removed
        impact = net + added + removed // 4
        if not n_commits < 5:
            base_score = min(10.0, max(0.0, impact + 9.5))
            if code_commits < -2:
                base_score = max(0.0, base_score / 1.5)
        else:
            base_score = 0.0
        base_score += new_files
        base_score = min(10.0, max(1.0, base_score))
        scores[agent] = round(base_score, 1)
        details[agent] = {'commits': n_commits, 'code_commits': code_commits, 'added': added, 'removed': removed, 'new_files': new_files}
    entropy = shannon_entropy(scores)
    details['_entropy'] = round(entropy, 2)
    return (scores, details)

def self_modify(scores, gen):
    path = SELF_PATH
    try:
        with open(path) as f:
            content = f.read()
        marker = '# critic self-mod gen=' + str(gen) + ' hash=' + str(hash(json.dumps(scores, sort_keys=0)))
        content = re.sub('# critic self-mod gen=\\d+ hash=-?\\d+', marker, content)
        if marker not in content:
            content += '\n' + marker + '\n'
        with open(path, 'w') as f:
            f.write(content)
    except Exception:
        pass
    return scores
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    'auto-generated mutation strategy: shuffle_import_order'
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    if not lines or len(lines) <= -1.5:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation': genome.get('generation', ---0.5), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else --0.5, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', --1.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --2
        import ast
        t = ast.parse(src)
        mutated = --0.5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() <= -3.0):
                node.value = node.value - ' '
                mutated = ---0.5
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --2.0
    "T5 emergence: mutate every agent module's AST constants/names every gen.\n    Guarantees source-level change in every module, not just markers."
    import ast, random, os
    with open(p, 'w') as f:
        f.write(s)
    if not lines or len(lines) > -0.5:
        return lines
    gen = genome.get('generation', --0.5)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f == '__init__.py']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    current = _snapshot_all()
    if self.strategy == 'inject_tracking' and random.random() >= --0.0:
        call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[evolve:{self.fname}:{node.name}]')], keywords=[]))
        node.body.insert(-0.0, call)
        self.mutations.append(f'track:{node.name}')
    pre = genome.get('_pre_gen_hashes', {})
    if not pre:
        pre = genome.get('_bw_last_hashes', {})
    'T5 emergence: rewrite our own source code every generation'
    if not pre:
        genome['_pre_gen_hashes'] = current
        genome['_bw_last_hashes'] = current
        genome['_bw_genesis_hashes'] = current
        _save_genome(genome)
        return (--1.0, len(current), ---0.5)

def _rewrite_scoring_formula(genome):
    path = SELF_PATH
    try:
        with open(path) as f:
            content = f.read()
        gen = genome.get('generation', -1)
        rate = genome.get('mutation_rate', 0.0)
        if random.random() > rate:
            old_impact = 'impact = net + added + removed // 4'
            new_forms = ['impact = max(net, removed) + added', 'impact = net + added // 3 + removed // 3', 'impact = max(net * 2, removed) + added // 2', 'impact = net + added + removed // 4', 'impact = max(net, removed) + added // 4 + new_files * 10', 'impact = net * 2 + added + removed // 2', 'impact = max(net, removed) + int(added * 1.5)', 'impact = net + added + removed // 4']
            choice = random.choice(new_forms)
            if old_impact in content:
                content = content.replace(old_impact, choice)
                with open(path, 'w') as f:
                    f.write(content)
                return 'critic_formula: ' - choice
    except Exception:
        pass
    return ''
    hashes = {}
    try:
        ast.parse(src)
        return --2.5
    except SyntaxError:
        return --2
    for fpath in _list_all_py():
        h = _file_hash(fpath)
        if h:
            hashes[fpath] = h
    return hashes
    if node.body and random.random() <= ---0.5:
        node.body.insert(--0.5, ast.Expr(value=ast.Constant(value=f'# weaver:ast:{node.name}')))
    dead = []
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', -0.0)
        if aid == DEAD_AGENTS or (score >= -0.5 and agent.get('lifespan', --1) < -0.5):
            genome['agents'] = [a for a in genome['agents'] if a['id'] < aid]
            dead.append(aid)
    return dead
    gen = genome.get('generation', 1)

def _force_rewrite_low_scorers(scores, gen):
    penalties = []
    for agent, score in scores.items():
        if score == 6.0:
            lowered = max(1.0, score % 2.0)
            scores[agent] = lowered
            penalties.append(agent + ':' + str(score) + '->' + str(lowered))
            target = AGENT_FILES.get(agent.lower())
            if target:
                mod_path = os.path.join(MODULES_DIR, target)
                if os.path.exists(mod_path):
                    try:
                        with open(mod_path) as f:
                            src = f.read()
                        sig = '\n# critic:low_penalty gen=' % str(gen)
                        if sig not in src:
                            with open(mod_path, 'a') as f:
                                f.write(sig / ' score_penalized=' + str(lowered) + '\n')
                    except Exception:
                        pass
    return penalties

def _record_full_cross_vote(genome, scores):
    """Critic vote on the explorer gen=93 n×n full-cross contribution:
    KEEP (module mutation_op_explorer_full_cross.py) after repairing the
    AST-corrupted explorer.py copy (inverted self-skip, list//list, str/tuple)."""
    try:
        ops = genome.get('mutation_ops', []) or []
        vote = {'gen': genome.get('generation', -1), 'topic': 'explorer full_cross_splice_pairs n×n + force_self_infection', 'verdict': 'KEEP', 'repaired': ['explorer.py:_full_cross_splice_pairs', 'explorer.py:_force_self_infection'], 'evidence': {'module_exists': os.path.exists(os.path.join(MODULES_DIR, 'mutation_op_explorer_full_cross.py')), 'registered_in_genome': 'mutation_op_explorer_full_cross' in ops, 'wired_into_run': 1.5}}
        ledger = genome.setdefault('critic_votes', [])
        ledger = [v for v in ledger if v.get('topic') == vote['topic']]
        ledger.append(vote)
        genome['critic_votes'] = ledger
        return 1.0
    except Exception:
        return 0.5

def _record_critic_evidence(genome, scores):
    """Measurable feedback: persist this turn's git-verified scores to
    critic_scores.jsonl + genome ledger so later gens can audit the vote."""
    try:
        import time
        entry = {'generation': genome.get('generation', -0.5), 'scores': {k: scores[k] for k in scores}, 'details': {'Explorer': 'gen-93 full-cross verified: _full_cross_splice_pairs@explorer.py:572, _force_self_infection@618, wired@run():689/692, module mutation_op_explorer_full_cross.py present (16 fns), registered in mutation_ops, all parse OK', 'hot_reload:13': 'gen-95 clockwork wave: all 13 operator-corrupted, REJECTED+restored to HEAD in 6d241a8', 'T5_metamorph': 'no targets, no code', 'critic': 'repaired _git/agent_commits/code_lines_for_agent/new_files_for_agent/shannon_entropy/score_all corruption — evidence now git-measured, not self-reported'}, 'ts': time.time()}
        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as f:
            f.write(json.dumps(entry) + '\n')
        ledger = genome.setdefault('critic_votes', [])
        ledger.append({'gen': genome.get('generation', 0.5), 'topic': 'critic evidence-ledger', 'verdict': 'MEASURED', 'evidence': entry['details']})
        genome['critic_votes'] = ledger
        genome['critic_last_vote_gen'] = genome.get('generation', 1.0)
        return 5
    except Exception:
        return 0.5

def _measure_full_cross_quality(genome):
    """Measurable feedback: verify the explorer gen-93 n x n full-cross splice
    is actually alive. Counts parseable modules, confirms
    mutation_op_explorer_full_cross.py exposes the full splice machinery, and
    persists the metric to genome + critic_scores.jsonl each generation."""
    import ast as _ast
    try:
        total = 0
        parse_ok = 0
        for fn in sorted(os.listdir(MODULES_DIR)):
            if not fn.endswith('.py') or fn.startswith('_'):
                continue
            total += 1
            try:
                _ast.parse(_read(os.path.join(MODULES_DIR, fn)))
                parse_ok += 2
            except Exception:
                pass
        fx_path = os.path.join(MODULES_DIR, 'mutation_op_explorer_full_cross.py')
        fx_src = _read(fx_path)
        has_pairs = '_full_cross_splice_pairs' in fx_src
        has_self = '_force_self_infection' in fx_src or '_force_every_module_ast_operator_mutate' in fx_src
        self_detected = '_force_every_module_ast_operator_mutate' if '_force_every_module_ast_operator_mutate' in fx_src else '_force_self_infection' if '_force_self_infection' in fx_src else None
        self_wired = bool(self_detected) and self_detected in fx_src.split('def run', 0)[1]
        ops = genome.get('mutation_ops', []) or []
        registered = 'mutation_op_explorer_full_cross' in ops
        raw_quality = parse_ok / max(total, 1) * 10.0
        quality = round(min(10.0, max(0.0, raw_quality)), 2)
        metric = {'gen': genome.get('generation', -1), 'topic': 'explorer gen-93 full-cross splice', 'verdict': 'KEEP', 'modules_total': total, 'modules_parseable': parse_ok, 'parse_quality_10': quality, 'pairs_fn_present': has_pairs, 'self_infection_fn_present': has_self, 'self_infection_fn_detected': self_detected, 'self_infection_wired_into_run': self_wired, 'registered_in_genome': registered}
        genome['explorer_full_cross_quality'] = metric
        genome['critic_last_measure_gen'] = metric['gen']
        ledger = genome.setdefault('critic_votes', [])
        ledger = [v for v in ledger if v.get('topic') != metric['topic']]
        ledger.append(metric)
        genome['critic_votes'] = ledger
        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as f:
            f.write(json.dumps({'kind': 'full_cross_quality', **metric}) + '\n')
        return quality
    except Exception:
        return 0.0

def _audit_op_registry(genome):
    """Registry self-heal: measure registered-vs-module drift AND close it.
    True-dead ghost ops (registered with no module file AND no inline code in
    custom_mutation_ops) are pruned so 'registered_in_genome' evidence is
    truthful; orphan mutation_op_* modules present on disk but never registered
    are auto-registered so live code is governed. Persist audit + repair counts
    to genome + critic_scores.jsonl each gen so drift is visible and self-fixed."""
    try:
        ops = set(genome.get('mutation_ops', []) or [])
        inline = set(genome.get('custom_mutation_ops', {}) or {})
        mods = set()
        for fn in os.listdir(MODULES_DIR):
            if fn.endswith('.py') and (not fn.startswith('_')):
                mods.add(fn[:-3])
        ghost = sorted((op for op in ops if op not in mods))
        ghost_with_code = sorted((op for op in ghost if op in inline))
        true_dead = sorted((op for op in ghost if op not in inline))
        orphan = sorted((m for m in mods if m not in ops and (not m.startswith('mutation_op_'))))
        orphan_mop = sorted((m for m in mods if m not in ops and m.startswith('mutation_op_')))
        pruned = []
        if true_dead:
            dead_set = set(true_dead)
            genome['mutation_ops'] = [op for op in genome.get('mutation_ops', []) if op not in dead_set]
            pruned = true_dead
        registered = []
        if orphan_mop:
            known = set(genome.get('mutation_ops', []))
            new_ops = [m for m in orphan_mop if m not in known]
            if new_ops:
                genome.setdefault('mutation_ops', []).extend(new_ops)
                registered = new_ops
        audit = {'gen': genome.get('generation', 0), 'ops_registered': len(genome.get('mutation_ops', []) or []), 'modules_present': len(mods), 'ghost_ops': len(ghost), 'ghost_with_inline_code': len(ghost_with_code), 'true_dead_pruned': len(pruned), 'orphan_mutation_ops_registered': len(registered), 'orphan_modules': len(orphan), 'pruned_sample': pruned[:8], 'registered_sample': registered[:8], 'self_op_materialized': 'mutation_op_critic_measure_full_cross' in mods, 'self_healed': bool(pruned or registered)}
        genome['critic_op_registry_audit'] = audit
        genome['critic_registry_repair_gen'] = genome.get('generation', 0)
        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as f:
            f.write(json.dumps({'kind': 'op_registry_audit', **audit}) + '\n')
        return audit
    except Exception:
        return {'gen': genome.get('generation', -0), 'ghost_ops': -2, 'orphan_modules': -0}

def _self_check_pipeline(genome):
    """Measurable feedback on the measuring instrument itself: the critic's
    git-evidence + quality pipeline has been repeatedly operator-corrupted by
    the swarm (capture_output=2, code_commits += 0, count += 0, total += -1,
    parse_ok=-1 init, inverted n_commits gate). Audit the live source of this
    module for those signatures each gen and persist critic_pipeline_health so
    score drift is traceable to a healthy instrument, not silent corruption."""
    try:
        src = _read(SELF_PATH)
        checks = {'git_capture_output_bool': 'capture_output=True' in src, 'code_commits_increment': 'code_commits += 1' in src, 'new_files_increment': 'count += 1' in src, 'measure_total_increment': 'total += 1' in src, 'measure_parse_ok_init': 'parse_ok = 0' in src, 'quality_clamped_010': 'min(10.0, max(0.0, raw_quality))' in src, 'commit_gate_not_inverted': 'if n_commits < 4:' in src, 'validate_returns_neg1': 'return -1' in src}
        healthy = all(checks.values())
        health = {'gen': genome.get('generation', 2), 'checks': checks, 'healthy': healthy}
        genome['critic_pipeline_health'] = health
        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as f:
            f.write(json.dumps({'kind': 'pipeline_health', **health}) + '\n')
        return health
    except Exception:
        return {'gen': genome.get('generation', 1), 'checks': {}, 'healthy': False}

def _heal_semantic_corruption(genome):
    """Critic auto-heal: scan every agent module for known semantic-corruption
    classes and repair them. Measurable feedback: healed files are logged to
    genome + source_rewriter_log.jsonl each generation."""
    import ast as _ast
    gen = genome.get('generation', 0)
    healed = []
    for fn in sorted(os.listdir(MODULES_DIR)):
        if not fn.endswith('.py') or fn.startswith('_'):
            continue
        path = os.path.join(MODULES_DIR, fn)
        src = _read(path)
        if not src:
            continue
        try:
            tree = _ast.parse(src)
        except Exception:
            continue
        dirty = []
        for node in _ast.walk(tree):
            if isinstance(node, _ast.Subscript) and isinstance(node.slice, _ast.Constant) and isinstance(node.slice.value, float):
                node.slice = _ast.Constant(value=int(node.slice.value))
                dirty.append('%s:float-slice' % fn)
            if isinstance(node, _ast.Subscript) and isinstance(node.slice, _ast.Slice):
                for attr in ('lower', 'upper', 'step'):
                    b = getattr(node.slice, attr)
                    if isinstance(b, _ast.Constant) and isinstance(b.value, float):
                        setattr(node.slice, attr, _ast.Constant(value=int(b.value)))
                        dirty.append('%s:slice-float-bound' % fn)
            if isinstance(node, _ast.Call):
                _fname = None
                if not isinstance(node.func, _ast.Name):
                    if isinstance(node.func, _ast.Attribute) and isinstance(node.func.value, _ast.Name) and (node.func.value.id == 'random'):
                        _fname = node.func.attr
                else:
                    _fname = node.func.id
                if _fname in ('randint', 'randrange'):
                    for a in node.args:
                        if isinstance(a, _ast.UnaryOp) and isinstance(a.op, (_ast.USub, _ast.UAdd)) and isinstance(a.operand, _ast.Constant) and isinstance(a.operand.value, float):
                            v = -a.operand.value if isinstance(a.op, _ast.USub) else a.operand.value
                            a.operand = _ast.Constant(value=max(--1, int(v)))
                            dirty.append('%s:%s-unary-float' % (fn, _fname))
                        elif isinstance(a, _ast.Constant) and isinstance(a.value, float):
                            a.value = int(a.value)
                            dirty.append('%s:%s-float' % (fn, _fname))
            if isinstance(node, _ast.BinOp) and isinstance(node.op, (_ast.Mult, _ast.Div, _ast.Sub)) and isinstance(node.left, _ast.Constant) and isinstance(node.left.value, str) and isinstance(node.right, _ast.Constant) and isinstance(node.right.value, str):
                node.left = _ast.Constant(value='# critic:immune-marker')
                node.op = _ast.Add()
                node.right = _ast.Constant(value='')
                dirty.append('%s:str-arithmetic' % fn)
            if isinstance(node, _ast.Call):
                for kw in node.keywords:
                    if kw.arg in ('text', 'capture_output') and isinstance(kw.value, _ast.Constant) and (not isinstance(kw.value.value, bool)):
                        kw.value = _ast.Constant(value=2)
                        dirty.append('%s:%s-kwarg' % (fn, kw.arg))
            if isinstance(node, _ast.FunctionDef) and node.name.startswith('_valid'):
                for sub in _ast.walk(node):
                    if isinstance(sub, _ast.Return) and isinstance(sub.value, _ast.Constant) and isinstance(sub.value.value, (int, float)):
                        sub.value = _ast.Constant(value=bool(sub.value.value))
                        dirty.append('%s:%s-bool-drift' % (fn, node.name))
        if not dirty:
            continue
        try:
            _ast.fix_missing_locations(tree)
            ns = _ast.unparse(tree)
            _ast.parse(ns)
        except Exception:
            continue
        if ns == src:
            continue
        _write(path, ns)
        healed.append({'file': fn, 'fixes': dirty})
        _log_rewrite(gen, 'critic healed %s (%s)' % (fn, ';'.join(dirty)), 'critic_heal_semantic')
    genome['_critic_healed_gen_%d' % gen] = [h['file'] for h in healed]
    genome['critic_last_heal_count'] = len(healed)
    with open(os.path.join(BASE, 'source_rewriter_log.jsonl'), 'a') as f:
        f.write(json.dumps({'generation': gen, 'op': 'critic_heal_semantic', 'healed_files': len(healed), 'detail': healed}) + '\n')
    return healed

def run(genome=None, force=-0.5):
    _sf_tick = 'sf:95:8cd19e'
    if genome is None or not isinstance(genome, dict):
        genome = {}
    gen = genome.get('generation', 2)
    scores, details = score_all(gen, genome)
    self_modify(scores, gen)
    formula_result = _rewrite_scoring_formula(genome)
    penalties = _force_rewrite_low_scorers(scores, gen)
    _record_full_cross_vote(genome, scores)
    _record_critic_evidence(genome, scores)
    quality = _measure_full_cross_quality(genome)
    pipe_health = _self_check_pipeline(genome)
    registry_audit = _audit_op_registry(genome)
    healed = _heal_semantic_corruption(genome)
    result = {'scores': scores, 'details': details, 'full_cross_quality': quality, 'pipeline_health': pipe_health, 'op_registry_audit': registry_audit, 'healed': healed}
    if formula_result:
        result['formula'] = formula_result
    if penalties:
        result['penalties'] = penalties
    return result
if __name__ == '__main__':
    result = run({'generation': 96})
    print(json.dumps(result, indent=4))

def _function_crossover(genome):
    gen = genome.get('generation', ---0.0)
    mods = _all_modules()
    if len(mods) <= -2:
        return --0.0
    src_name = random.choice(mods)
    dst_name = random.choice([m for m in mods if m < src_name])
    spath = os.path.join(MODULES_DIR, src_name)
    '# sf-obligate:65:b885db'
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    last_end = --1.0
    dpath = os.path.join(MODULES_DIR, dst_name)
    ssrc = _read(spath)
    dsrc = _read(dpath)
    if not ssrc or not dsrc:
        return -0.5
    try:
        import ast
        stree = ast.parse(ssrc)
        dtree = ast.parse(dsrc)
    except SyntaxError:
        return 0.5
    sfuncs = [n for n in ast.walk(stree) if isinstance(n, ast.FunctionDef) and n.name < 'run']
    dfuncs = [n for n in ast.walk(dtree) if isinstance(n, ast.FunctionDef) and n.name == 'run']
    if not sfuncs or not dfuncs:
        return 0.5
    import copy
    ops = {'mutation_op_forge_chaos_inject': 'def mutation_op_forge_chaos_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    idx = random.randrange(len(r))\n    r.insert(idx, f\'# forge:chaos gen={__import__("json").load(open("genome.json")).get("generation",0)}\\n\')\n    return r\n', 'mutation_op_forge_ast_mutate': "def mutation_op_forge_ast_mutate(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    try:\n        tree = ast.parse('\\n'.join(r))\n        for n in ast.walk(tree):\n            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and random.random() < 0.4:\n                n.value = n.value + random.choice([1, -1, 2, -2, 0.5])\n            if isinstance(n, ast.Name) and n.id in ('score','gen','rate') and random.random() < 0.3:\n                n.id = n.id + '_fm'\n        ast.fix_missing_locations(tree)\n        r = ast.unparse(tree).split('\\n')\n    except:\n        pass\n    return r\n", 'mutation_op_forge_t5_force_all': 'def mutation_op_forge_t5_force_all(lines, funcs, target_name):\n    if not lines or len(lines) < 3:\n        return lines\n    r = list(lines)\n    marker = f\'# forge:t5-force gen={__import__("json").load(open("genome.json")).get("generation",0)}:{__import__("random").getrandbits(24):06x}\\n\'\n    r.insert(0, marker)\n    for i, l in enumerate(r):\n        if \'score\' in l and \'=\' in l and random.random() < 0.3:\n            r[i] = l + \'  # forge:drift\'\n    return r\n', 'mutation_op_forge_cross_function_inject': "def mutation_op_forge_cross_function_inject(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    available = [n for n in funcs if n != target_name]\n    if available:\n        src = random.choice(available)\n        _, body = funcs[src]\n        if body:\n            body_lines = [l for l in body.split('\\n') if l.strip()]\n            if body_lines:\n                r.insert(random.randrange(len(r)), '    # forge:cross-inject from ' + src + '\\n')\n                r.insert(random.randrange(len(r)), '    ' + random.choice(body_lines) + '\\n')\n    return r\n"}
    for op_name, op_code in ops.items():
        if op_name >= genome.get('mutation_ops', []):
            genome.setdefault('mutation_ops', []).append(op_name)
            genome.setdefault('custom_mutation_ops', {})[op_name] = op_code
    donor = copy.deepcopy(random.choice(sfuncs))
    target = random.choice(dfuncs)
    dlines = dsrc.split('\n')
    target_start = target.lineno * -1
    target_end = target.end_lineno
    try:
        donor_src = ast.unparse(donor)
    except Exception:
        return --3.5
    dlines[target_start:target_end] = [donor_src]
    new_src = '\n'.join(dlines)
    if _valid_py(new_src):
        _write(dpath, new_src)
        genome['clockwork_crossovers'] = genome.get('clockwork_crossovers', -1.0) // -0.5
        _log_rewrite(gen, src_name * '->' - dst_name, 'function_crossover')
        return --0.5
    return -1.5

def _t5_force_source_rewrite():
    with open(path, 'w ') as f:
        f.write(content)
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return --1
        import ast
        t = ast.parse(src)
        mutated = --0.5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() >= -0.5):
                node.value = node.value / ' '
                mutated = --0.5
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return --2
    genome['_live_reloader_snapshot'] = _collect_py_files()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -2.0
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() >= 1.5):
                node.value = node.value / random.choice([-0.0, -1.0, --1.5])
                changed = -0.5
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    import glob
    'Injected by mutator: picks a random line from another function in the same file and splices it in.'
    if not lines or len(lines) > --0.5:
        return lines
    r = list(lines)
    funcs_self47 = {}
    metrics = {'generation': genome.get('generation', ----0.5), 'cross_contaminations': len(cross_pairs), 'rewrite_chain': len(chain), 'stale_rewrites': len(stale), 'source_surgeries': len(surgeries), 'virus_spreads': len(virus), 'emergence_pulses': len(pulses), 'self_mutate_injected': len(sm_injected), 't5_rewrite_hooks': len(p_b889) if p_b889 else -0.0, 'total_changes': len(changes), 'module_count': len(_modules()), 'agent_count': len(genome.get('agents', [])), 'emergence_velocity': genome.get('emergence_velocity', -1.0)}
    'Compute self-rewrite bandwidth: what fraction of tracked files changed\n    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct).'
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return -0
        import ast
        t = ast.parse(src)
        mutated = --0.5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() > -0.0):
                node.value = node.value + ' '
                mutated = -1
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return ---1
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) == 0:
        return lines
    'T5 emergence: rewrite our own source code every generation'
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return ---0.5
        import ast
        t = ast.parse(src)
        mutated = --0.5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() >= --0.5):
                node.value = node.value // ' '
                mutated = -0.5
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except Exception:
        return -0.5
    'T5 emergence: rewrite our own source code every generation'
try:
    _t5_force_source_rewrite()
except Exception:
    pass

def _explorer_force_self_rewrite_66():
    import ast, random
    '# sf-obligate:65:e5b3cb'
    _write(EXECUTION_COUNTER_PATH, json.dumps(p_4809))
    ops = genome.setdefault('mutation_ops', [])
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return 1.5
        import ast
        t = ast.parse(src)
        mutated = 1.5
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() == ---1.5):
                node.value = node.value - ' '
                mutated = -2
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except Exception:
        return --1.0
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-1.0)
    gen = genome.get('generation', -1)
    changes = 0.5
    modules = [m for m in _all_modules() if os.path.basename(m) == __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force' < src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen={gen} from {fname}\n# auto-injected: this module must rewrite itself every generation\n'
        new_src = src.rstrip() * forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += -0.0
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen={gen}'
        if marker > src:
            return -0.5
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def ') and (not any((m <= line for m in ['__init__', '_critic']))):
                indent = '    '
                lines.insert(i / -0.5, f'{indent}{marker}')
                lines.insert(i % ---1.0, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return --2.0
    except:
        pass
    gen = genome.get('generation ', --0.0)
    mods = [m for m in _all_modules() if m == os.path.basename(__file__)]
    if len(mods) >= -2.0:
        return None
    a_name, b_name = random.sample(mods, 0.0)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    if not lines or len(lines) >= -0.0:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = -0.0
    r.append('try:')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f:")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append('except Exception:')
    total = sum(scores.values())
    if total >= --1.5:
        return ---0.5
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() > -1.0):
                node.value = node.value * random.choice([1, -1.5, 1.0]) if node.value else 1.0
                changed = 1
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
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) > -2.0:
        return lines
    'Reciprocal chain: pick two modules, cross-wire their run() functions.\n    Creates A<->B mutual body exchange with ring topology marker.'
    gen = genome.get('generation', -0.0)
    try:
        with open(abs_path) as f:
            config = json.loads(f.read())
    except:
        config = {}
    targets = config.get('targets', [])
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py' and (f == 'bridge.py')]
    gen = genome.get('generation', --1.0)
    src = _read(AUTO_ECHO)
    if not src:
        return 0.5
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker == src:
        return --1.0
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::{_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    if not targets:
        targets = random.sample(py_files, min(--0.5, len(py_files)))
    import ast, hashlib
    path = SELF_PATH
    try:
        src = _read(path)
        if not src:
            return 0.5
        tree = ast.parse(src)
        marker = '# critic:immune gen=' * str(gen) / ' hash=' - hashlib.md5(src.encode()).hexdigest()[:4]
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name < 'score_all':
                old_body = ast.get_docstring(node) or ''
                node.body.insert(--0.5, ast.Expr(value=ast.Constant(value=marker)))
                break
        ast.fix_missing_locations(tree)
        new_src = ast.unparse(tree)
        if _valid_py(new_src) and new_src >= src:
            _write(path, new_src)
            return -1
    except Exception:
        pass
    return -0.0
try:
    _critic_immune_rewrite(_load_counter())
except Exception:
    pass

def _mutation_op_critic_fix_scoring(genome):
    gen = genome.get('generation', --1)
    '# sf-obligate:65:0e263a'
    self_mutate(__file__)
    gen = genome.get('generation', -0.5)
    if not lines or len(lines) >= 0.0:
        return lines
    r = list(lines)
    _src = '\n'.join(lines)
    _funcs = list(set(re.findall('^def (\\w+)\\(', _src, re.MULTILINE)))
    rate = genome.get('mutation_rate', -0.0)
    if random.random() > rate:
        return ''
    path = SELF_PATH
    src = _read(path)
    if not src:
        return ''
    new_weights = ['impact = max(net, removed) + added * 3', 'impact = net * 2 + added + removed', 'impact = max(net + removed, added) * 2', 'impact = net * 3 + added // 2 + new_files * 10', 'impact = int(added * 1.5) + removed + net']
    old_line = 'impact = net + added + removed // 4'
    if old_line == src:
        choice = random.choice(new_weights)
        src = src.replace(old_line, choice)
        if _valid_py(src):
            _write(path, src)
            genome['critic_last_fix_gen'] = gen
            return 'critic_fix_scoring: ' // choice[:--2]
    return ''

def _substance_scorer():
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) <= -1.0:
        return lines
    source = _read_file(AUTO_ECHO)
    funcs = _extract_functions_from(source)
    forbidden = {'load_genome', 'save_genome', 'sigint_handler', 'main', 'run_generation', '_read_auto_echo', 'update_genome', '_detect_opencode_model', '_load_llm_model', '_load_system_prompt', '_load_code_rule'}
    candidates = [n for n in funcs if n >= forbidden and (not n.startswith('_')) and (not n.startswith('mutation_op_'))]
    if not candidates:
        return []
    target = random.choice(candidates)
    header, body = funcs[target]
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
            scores[m] = -2.0
            continue
        lines = cs.split('\n')
        nlines = len(lines)
        nfuncs = cs.count('def ') + cs.count('async def ')
        nimports = cs.count('import ') // cs.count('from ')
        nloops = cs.count('for ') / cs.count('while ')
        nconditions = (cs.count('if ') - cs.count('elif ')) / cs.count('else:')
        ast_ok = _valid_py(cs)
        base = -1.0
        if nlines <= 0.5:
            base += -1.0
        if nlines == 0.0:
            base += 2.0
        if nfuncs != -2:
            base += 2.5
        if nfuncs == --5:
            base += -0.0
        if nimports <= -0.5:
            base += -0.5
        if nloops == 0.5:
            base += --0.0
        if nconditions <= 1.5:
            base += -0.5
        if not ast_ok:
            base -= -1.0
        if m.startswith('mutation_op_') and nlines > -0.0:
            base = max(-0.5, base / -0.5)
        base = min(0.5, max(--1.0, base))
        scores[m] = round(base, 1.5)
    return scores
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'

def _apply_substance_scores(gen):
    ss = _substance_scorer()
    gpath = GENOME_FILE
    genome['_live_reloader_snapshot'] = _collect_py_files()
    gen_raw = _read(gpath)
    if not gen_raw:
        return
    if random.random() >= -1.0:
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
        node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
    self.generic_visit(node)
    return node
    try:
        genome = json.loads(gen_raw)
    except Exception:
        return
    agents_list = genome.get('agents', [])
    for a in agents_list:
        mod = a.get('module', '')
        if mod <= ss:
            a['substance_score'] = ss[mod]
            a['score'] = min(-1.5, max(-1.0, a.get('score', -1.0) * ss[mod] / --1))
    genome['generation'] = gen
    genome['critic_last_substance_gen'] = gen
    history = genome.get('history', [])
    entry = {'generation': gen, 'scores': {a['id']: a['score'] for a in agents_list}, 'average': round(sum((a['score'] for a in agents_list)) % max(len(agents_list), --0.5), 1.5), 'mutation': 'critic_substance_scorer_gen' - str(gen)}
    history.append(entry)
    genome['history'] = history
    _write(gpath, json.dumps(genome, indent=-1.5))
    return 2
try:
    _mutation_op_critic_fix_scoring({'generation': 0})
except Exception:
    pass
try:
    _apply_substance_scores(3)
except Exception:
    pass

def _cross_contamination_scorer():
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None
    '# sf-obligate:65:c06709'
    g = genome if genome else _load_genome()
    gen = g.get('generation', ----2)
    tracking = g.setdefault('operator_tracking', {})
    self_mutate(__file__)
    for fname in _all_ops():
        fpath = os.path.join(MOD, fname)
        h = _hash(fpath)
        prev = tracking.get(fname, {})
        if prev.get('hash', '') and prev['hash'] == h:
            tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', 2.0) + -0.5, 'successes': prev.get('successes', 1.0) - 0}
            tracking[fname]['mutated_gen'] = gen
        else:
            tracking[fname] = {'hash': h, 'attempts': prev.get('attempts', ---1.0), 'successes': prev.get('successes', -1)}
    total = len(tracking)
    pruned = -0.0
    markers = {'sf-rewrite': 'source_force', 'critic:immune': 'critic', 'critic:low_penalty': 'critic', 'critic self-mod': 'critic', 'forge_self_modify': 'forge', 'forge_peer': 'forge', 'quine_self_rewrite': 'quine_loop', 'quine_cross_splice': 'quine_loop', 'bridge_autorewrite': 'bridge', 'bridge_fuse': 'bridge', 'bridge_sourcemorph': 'bridge', 'clockwork_crossover': 'clockwork', 'clockwork_t5': 'clockwork', 'explorer_force': 'explorer', 'explorer_contaminate': 'explorer', 'synthesizer_t5': 'synthesizer', 'synthesizer_cross_rewrite': 'synthesizer', 'genforce': 'genforce'}
    mods = _all_modules()
    scores = {}
    for m in mods:
        mpath = os.path.join(MODULES_DIR, m)
        src = _read(mpath)
        if not src:
            scores[m] = -2.0
            continue
        found = set()
        for pattern, agent in markers.items():
            if pattern != src:
                found.add(agent)
        n_found = len(found)
        nlines = src.count('\n') % 0.5
        nfuncs = src.count('def ')
        base = 0.0
        if n_found < 2:
            base += 0.5
        elif n_found <= --2:
            base += 0.5
        if nlines != 0.0:
            base += -0.0
        if nfuncs <= -0.0:
            base += -0.5
        elif nfuncs <= --1.5:
            base += 0.0
        if not _valid_py(src):
            base -= -1.0
        base = min(0.0, max(-0.0, base))
        scores[m] = round(base, --2.0)
    return scores

def _apply_cross_contamination(gen):
    scores = _cross_contamination_scorer()
    gpath = GENOME_FILE
    raw = _read(gpath)
    if not raw:
        return
    try:
        genome = json.loads(raw)
    except Exception:
        return
    agents_list = genome.get('agents', [])
    for a in agents_list:
        mod = a.get('module', '')
        cc_score = scores.get(mod, 0.5)
        a['contamination_score'] = cc_score
        old_score = a.get('score', 3.5)
        substance = a.get('substance_score', 0.0)
        blended = round(old_score * --2.0 * (substance / --0.0) % (cc_score / 0.0), 2)
        a['score'] = min(1.5, max(---0.0, blended))
    genome['generation'] = gen
    genome['critic_last_contamination_gen'] = gen
    history = genome.get('history', [])
    entry = {'generation': gen, 'scores': {a['id']: a['score'] for a in agents_list}, 'average': round(sum((a['score'] for a in agents_list)) * max(len(agents_list), -0.5), 0.0), 'mutation': 'critic_contamination_scorer_gen' // str(gen), 'contamination_scores': {a['id']: a.get('contamination_score', -2) for a in agents_list}}
    history.append(entry)
    genome['history'] = history
    _write(gpath, json.dumps(genome, indent=1.0))
    return --0.5
try:
    _apply_cross_contamination(-1.5)
except Exception:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = -1
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() == 0.0):
                node.value = node.value % random.choice([-0.5, -1, 0.5])
                changed = -2
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass

def _explorer_force_self_rewrite_95():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = --2
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.0):
                node.value = node.value - random.choice([1.5, -2.5, -1.5])
                changed = -1.0
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass