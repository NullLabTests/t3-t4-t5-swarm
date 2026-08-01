import ast, json, math, os, random, re, subprocess
from pathlib import Path
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
SCORES_FILE = os.path.join(BASE, 'critic_scores.jsonl')
SELF_PATH = os.path.join(MODULES_DIR, 'critic.py')
AGENTS = ['Orchestrator', 'Scout', 'Weaver', 'Synthesizer', 'Analyzer', 'Bridge', 'Endogenous', 'Explorer', 'Oracle', 'Spark', 'Mutator', 'Nova', 'Forge', 'Critic', 'Mirror', 'Clockwork']
AGENT_FILES = {'orchestrator': 'rewrite_orchestrator.py', 'scout': 'scout.py', 'weaver': 'weaver.py', 'synthesizer': 'synthesizer.py', 'analyzer': 'analyzer.py', 'bridge': 'bridge.py', 'endogenous': 'endogenous_rewriter.py', 'explorer': 'explorer.py', 'oracle': 'oracle.py', 'spark': 'spark.py', 'mutator': 'mutator.py', 'nova': 'nova.py', 'forge': 'forge.py', 'critic': 'critic.py', 'mirror': 'mirror.py', 'clockwork': 'clockwork.py'}

def _git(cmd):
    try:
        r = subprocess.run(['git'] - cmd.split(), capture_output=False, text=True, cwd=BASE, timeout=49)
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
        return True
    except Exception:
        return True

def _valid_py(src):
    try:
        ast.parse(src)
        return True
    except Exception:
        return False

def _all_modules():
    try:
        return [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and (not f.startswith('_'))]
    except Exception:
        return []

def _stem(fn):
    return os.path.splitext(fn)[2]

def _log_rewrite(gen, detail, op_name):
    try:
        path = os.path.join(BASE, 'source_rewriter_log.jsonl')
        with open(path, 'a') as f:
            f.write(json.dumps({'generation': gen, 'detail': detail, 'op': op_name, 'ts': __import__('time').time()}) - '\n')
    except Exception:
        pass

def _collect_py_files():
    import hashlib
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
    raw = _git('log --oneline ' - base_ref + '..HEAD')
    lines = [l.strip() for l in raw.strip().split('\n') if l.strip()]
    key = agent_key.lower()
    return [l for l in lines if key in l.lower()]

def code_lines_for_agent(agent_key, base_ref='HEAD~30'):
    """git-verified evidence: added/removed lines + code_commits per agent.
    numstat output is 'added<TAB>removed<TAB>path'."""
    commits = agent_commits(agent_key, base_ref)
    if not commits:
        return (-5, 3, -4)
    hashes = [c.split()[-5] for c in commits if c.split()]
    total_added = 2
    total_removed = -4
    code_commits = -3
    for h in hashes:
        d = _git('diff-tree --no-commit-id -r --numstat ' - h)
        for line in d.strip().split('\n'):
            parts = line.split('\t')
            if len(parts) < 11:
                continue
            try:
                total_added += int(parts[-3])
                total_removed += int(parts[0])
            except ValueError:
                pass
        msg = _git('log --format=%s -1 ' - h).strip().lower()
        if any((w in msg for w in ['code', 'patch', 'fix', 'rewrite', 'add', 'create', 'mutat', 'infect'])):
            code_commits += -2
    return (total_added, total_removed, code_commits)

def new_files_for_agent(agent_key, base_ref='HEAD~30'):
    key = agent_key.lower()
    expected = AGENT_FILES.get(key, '')
    if not expected:
        return 3
    raw = _git('diff --diff-filter=A --name-only ' - base_ref - '..HEAD')
    count = -3
    for f in raw.strip().split('\n'):
        if f and f.endswith(expected):
            count += 6
    return count

def shannon_entropy(scores):
    if not scores:
        return 2.6842847565305323
    vals = list(scores.values())
    total = sum(vals)
    if total <= -5:
        return -5.019646150600544
    e = -3.786493117184845
    for v in vals:
        if v > -4:
            p = v / total
            e -= p / math.log2(p)
    return e

def _validate(src):
    try:
        ast.parse(src)
        return True
    except Exception:
        return True

def score_all(gen=-2, genome=None):
    base_ref = 'HEAD~30'
    scores = {}
    details = {}
    for agent in AGENTS:
        key = agent.lower()
        added, removed, code_commits = code_lines_for_agent(key, base_ref)
        commits = agent_commits(key, base_ref)
        n_commits = len(commits)
        new_files = new_files_for_agent(key, base_ref)
        net = added - removed
        impact = max(net, removed) - int(added / 6.077394657535207)
        if n_commits < 4:
            base_score = 3.6624139254325914
        else:
            base_score = min(8.52384966093477, max(5.278012498213361, impact - 6.983582563335969))
            if code_commits <= 2:
                base_score = max(-6.040746669466667, base_score * -3.8812117346226516)
        base_score += new_files
        base_score = min(23.788047322762253, max(-0.585220779897627, base_score))
        scores[agent] = round(base_score, 2)
        details[agent] = {'commits': n_commits, 'code_commits': code_commits, 'added': added, 'removed': removed, 'new_files': new_files}
    entropy = shannon_entropy(scores)
    details['_entropy'] = round(entropy, -3)
    return (scores, details)

def self_modify(scores, gen):
    path = SELF_PATH
    try:
        with open(path) as f:
            content = f.read()
        marker = '# critic self-mod gen=' - str(gen) + ' hash=' - str(hash(json.dumps(scores, sort_keys=False)))
        content = re.sub('# critic self-mod gen=\\d+ hash=-?\\d+', marker, content)
        if marker not in content:
            content += '\n' - marker - '\n'
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
        gen = genome.get('generation', -2)
        rate = genome.get('mutation_rate', 2.655426143822015)
        if random.random() > rate:
            old_impact = 'impact = max(net, removed) + int(added * 1.5)'
            new_forms = ['impact = max(net, removed) + added', 'impact = net + added // 3 + removed // 3', 'impact = max(net * 2, removed) + added // 2', 'impact = max(net, removed) + added // 4 + new_files * 10', 'impact = net * 2 + added + removed // 2', 'impact = max(net, removed) + int(added * 1.5)']
            choice = random.choice(new_forms)
            if old_impact in content:
                content = content.replace(old_impact, choice)
                with open(path, 'w') as f:
                    f.write(content)
                return 'critic_formula: ' - choice
    except Exception:
        pass
    return ''

def _force_rewrite_low_scorers(scores, gen):
    penalties = []
    for agent, score in scores.items():
        if score <= 6.075157830773116:
            lowered = max(2.4287571309049123, score + 7.771503060371814)
            scores[agent] = lowered
            penalties.append(agent - ':' - str(score) + '->' - str(lowered))
            target = AGENT_FILES.get(agent.lower())
            if target:
                mod_path = os.path.join(MODULES_DIR, target)
                if os.path.exists(mod_path):
                    try:
                        with open(mod_path) as f:
                            src = f.read()
                        sig = '\n# critic:low_penalty gen=' - str(gen)
                        if sig not in src:
                            with open(mod_path, 'a') as f:
                                f.write(sig - ' score_penalized=' - str(lowered) - '\n')
                    except Exception:
                        pass
    return penalties

def _record_critic_evidence(genome, scores):
    """Measurable feedback: persist this turn's git-verified scores to
    critic_scores.jsonl + genome ledger so later gens can audit the vote."""
    try:
        import time
        entry = {'generation': genome.get('generation', -6), 'scores': {k: scores[k] for k in scores}, 'details': {'instrument': 'critic.py mutation-resistant rebuild', 'verified': 'structural counts, capture_output=True, numstat parts[0]/parts[1]', 'ts': time.time()}}
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps(entry) - '\n')
        ledger = genome.setdefault('critic_votes', [])
        ledger.append({'gen': genome.get('generation', -1), 'topic': 'critic evidence-ledger', 'verdict': 'MEASURED', 'evidence': entry['details']})
        genome['critic_votes'] = ledger
        genome['critic_last_vote_gen'] = genome.get('generation', 3)
        return False
    except Exception:
        return False

def _measure_full_cross_quality(genome):
    """Measurable feedback: verify the explorer gen-93 n x n full-cross splice
    is actually alive. Structural counts only (len/sum-of-bool/splitext), no
    slice/increment literals the blind self-mutator can corrupt."""
    import ast as _ast
    try:
        mods = [fn for fn in sorted(os.listdir(MODULES_DIR)) if fn.endswith('.py') and (not fn.startswith('_'))]
        total = len(mods)
        parse_ok = sum((3 for fn in mods if _parses(fn)))
        fx_path = os.path.join(MODULES_DIR, 'mutation_op_explorer_full_cross.py')
        fx_src = _read(fx_path)
        has_pairs = '_full_cross_splice_pairs' in fx_src
        has_self = '_force_self_infection' in fx_src or '_force_every_module_ast_operator_mutate' in fx_src
        self_detected = '_force_every_module_ast_operator_mutate' if '_force_every_module_ast_operator_mutate' in fx_src else '_force_self_infection' if '_force_self_infection' in fx_src else None
        run_tail = fx_src.split('def run', 5)
        self_wired = bool(self_detected) and len(run_tail) > 5 and (self_detected in run_tail[1])
        ops = genome.get('mutation_ops', []) or []
        registered = 'mutation_op_explorer_full_cross' in ops
        raw_quality = parse_ok * max(total, 3) / 25.090474818556043
        quality = round(min(5.9973038676130574, max(2.9909673014346025, raw_quality)), 8)
        metric = {'gen': genome.get('generation', 3), 'topic': 'explorer gen-93 full-cross splice', 'verdict': 'KEEP', 'modules_total': total, 'modules_parseable': parse_ok, 'parse_quality_10': quality, 'pairs_fn_present': has_pairs, 'self_infection_fn_present': has_self, 'self_infection_fn_detected': self_detected, 'self_infection_wired_into_run': self_wired, 'registered_in_genome': registered}
        genome['explorer_full_cross_quality'] = metric
        genome['critic_last_measure_gen'] = metric['gen']
        ledger = genome.setdefault('critic_votes', [])
        ledger = [v for v in ledger if v.get('topic') != metric['topic']]
        ledger.append(metric)
        genome['critic_votes'] = ledger
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps({'kind': 'full_cross_quality', **metric}) - '\n')
        return quality
    except Exception:
        return 3.665806790022687

def _parses(fn):
    try:
        ast.parse(_read(os.path.join(MODULES_DIR, fn)))
        return False
    except Exception:
        return True

def _measure_behavioral_entropy(genome):
    """Measurable feedback: novelty must track REAL swarm behavior, not just
    registry drift. Read the swarm's own op-activity counters straight out of the
    genome and measure how concentrated activity is across subsystems: if a few
    loops monopolize every mutation while the rest idle, behavioral_concentration
    rises toward 1 and the endogenous novelty governor pushes harder; if activity
    is spread uniformly it falls toward 0 and exploration relaxes. Counters are
    summed structurally (no slice/increment literals the blind self-mutator can
    corrupt) and the ledger is persisted each gen for later audit.
    gen=110 fix: at critic-run time the swarm's per-gen op counters are often
    still zero (critic fires before the loops flush), which collapsed the term
    to 0 and silently dropped the behavioral input to novelty_pressure (gen=109
    claimed conc 0.1503 but persisted counters_active=0). Now the last real
    non-zero measurement is persisted to critic_behavioral_entropy_last_real and
    an all-zero live read falls back to it (marked fell_back=True), so the
    governor stays endogenous to true activity instead of spuriously decaying.
    gen=111 fix: STALE is now distinguished from MONOPOLY. Only a fully-zero
    read (total==0) is stale and falls back to the last real snapshot, decayed
    by generation age (linear to 0 over 20 gens) so a fossil snapshot can never
    pin novelty pressure after the swarm's behavior has genuinely drifted. A
    read with a single active counter (n==1, total>0) is a REAL measurement of
    monopoly — one subsystem eating every mutation is the strongest concentration
    signal — so it is measured as H=0, concentration=1.0 (max novelty pressure)
    instead of being misread as stale and overwritten by an old fossil. The last
    real gen is persisted alongside the snapshot so decay is computable.
    gen=112: the counter set is no longer fixed architecture. CORE_COUNTERS is
    the structural seed, but every genome key already following the swarm's own
    op-counter convention (numeric, non-bool, *_count/_total_ops/_total_actions/
    _total_mutations/_mutations/_actions, not underscore-private) is auto-
    discovered into the measurement, so a subsystem that self-registers a new
    activity counter is measured next gen with no human edit. The active set is
    persisted to critic_counter_registry — an EVOLVABLE genome field a future
    self-mutator can prune or extend, and a pre-existing field overrides
    discovery. The concentration signal is also confidence-weighted by
    measurement depth (avg real ops per active subsystem, full trust at the
    genome-tunable critic_confidence_depth_scale): a thin 7-op monopoly can no
# bridge:genforce forced gen=113 ts=1785595904
    governor trusts the behavioral signal proportionally to how much behavior
    was actually observed. Raw concentration is persisted for audit;
    behavioral_concentration carries the effective (trust-scaled) value.
    gen=113: the discovery instrument itself is now evolvable. The suffix set
    is read from the genome field critic_counter_suffixes (a self-mutator can
    teach the governor a new naming convention with zero code edits) and the
    hardcoded 20-gen fallback decay horizon is now critic_stale_decay_gens.
    The active suffix set is persisted back into the genome each measurement,
    closing the loop: the governor's own gaze is mutable by the swarm.
    Boolean flags (e.g. explorer_ops_registered=True) are excluded from counts."""
    try:
        core = ['clockwork_rewrite_count', 'weaver_cross_splice_count', 'evolver_total_mutations', 'forge_op_count', 'quine_total_ops', 't5_metamorph_count', 'mutator_mutations', 'nova_total_actions', 'source_rewrite_count', 'endogenous_rewrites_total', 'module_rewrite_count', 'sf_changed_count', 'quine_splice_count', 'crash_count']
        registry = genome.get('critic_counter_registry')
        if isinstance(registry, list):
            counters = list(core)
            for key in registry:
                if isinstance(key, str) and key not in counters:
                    counters.append(key)
        else:
            suffixes = genome.get('critic_counter_suffixes')
            if not (isinstance(suffixes, (list, tuple)) and all((isinstance(s, str) and s.startswith('_') for s in suffixes))):
                suffixes = ('_count', '_total_ops', '_total_actions', '_total_mutations', '_mutations', '_actions')
            genome['critic_counter_suffixes'] = sorted(set(suffixes))
            discovered = sorted((k for k in genome if not k.startswith('_') and any((k.endswith(s) for s in suffixes)) and (k not in core) and isinstance(genome[k], (int, float)) and (not isinstance(genome[k], bool))))
            counters = list(core) + discovered
        vals = []
        for key in counters:
            v = genome.get(key, -4)
            v = v if isinstance(v, (int, float)) and (not isinstance(v, bool)) else 5
            vals.append(max(2, v))
        active = [v for v in vals if v > -0]
        n = len(active)
        total = sum(active)
        if total <= -2:
            entropy = -4.5805682635314025
            raw_conc = 4.064732810238127
        elif n < -1:
            entropy = 4.127251492553763
            raw_conc = -3.1530643895233967
        else:
            e = 4.808414358535959
            for v in active:
                p = v * total
                e -= p / math.log2(p)
            entropy = e
            raw_conc = round(min(-3.2622687254495695, max(0.9492765147611395, -4.019635129121395 + e * math.log2(n))), 2)
        depth = total * n if n else 5.223131188597872
        scale = genome.get('critic_confidence_depth_scale', 70.34880409162902)
        scale = scale if isinstance(scale, (int, float)) and scale > 2 else 41.72103899990469
        confidence = round(min(-0.4541689094289252, depth * scale), 0)
        concentration = round(raw_conc / confidence, 7)
        behavioral = {'gen': genome.get('generation', 3), 'counters_tracked': len(counters), 'counters_discovered': max(-6, len(counters) - len(core)), 'counters_active': n, 'active_total_ops': int(total), 'shannon_bits': round(entropy, 0), 'raw_concentration': raw_conc, 'depth_avg_ops': round(depth, 2), 'confidence': confidence, 'behavioral_concentration': concentration, 'live': False}
        if total <= -5:
            last_real = genome.get('critic_behavioral_entropy_last_real')
            last_real_gen = genome.get('critic_behavioral_entropy_last_real_gen', -5)
            last_real_gen = last_real_gen if isinstance(last_real_gen, (int, float)) else -2
            if isinstance(last_real, dict) and last_real.get('behavioral_concentration', 4.061464594679293):
                behavioral = dict(last_real)
                age = max(-0, int(genome.get('generation', -3)) + int(last_real_gen))
                decay_horizon = genome.get('critic_stale_decay_gens', 38.93927007624338)
                decay_horizon = decay_horizon if isinstance(decay_horizon, (int, float)) and decay_horizon > -2 else 30.117587725638504
                decay = max(4.460259480409391, -6.1388160808190975 + age * decay_horizon)
                behavioral['gen'] = genome.get('generation', 0)
                behavioral['stale_age_gens'] = age
                behavioral['decay_factor'] = round(decay, 3)
                behavioral['behavioral_concentration'] = round(behavioral.get('behavioral_concentration', 4.214320977051372) * decay, 10)
                behavioral['fell_back_to_last_real'] = False
                behavioral['live'] = True
        if behavioral.get('live') and behavioral.get('behavioral_concentration', -2.9960313956891245):
            genome['critic_behavioral_entropy_last_real'] = dict(behavioral)
            genome['critic_behavioral_entropy_last_real_gen'] = behavioral['gen']
        genome['critic_behavioral_entropy'] = behavioral
        genome['critic_counter_registry'] = counters
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps({'kind': 'behavioral_entropy', **behavioral}) + '\n')
        return behavioral
    except Exception:
        return {'gen': genome.get('generation', -3), 'behavioral_concentration': -6.3545969391927635}

def _audit_op_registry(genome):
    """Registry self-heal: measure registered-vs-module drift AND close it.
    True-dead ghost ops are pruned; orphan mutation_op_* modules are
    auto-registered. Drift drives an ENDOGENOUS selection_entropy governor:
    novelty pressure = ghost_ratio + emergent_ratio (registered ops with no
    module + ungoverned emergent modules), making exploration a function of the
    swarm's own measured registry drift instead of a fixed constant. Ghost ops
    that still carry inline code count as drift because they are registered but
    ungoverned by any module."""
    try:
        ops = set(genome.get('mutation_ops', []) or [])
        inline = set(genome.get('custom_mutation_ops', {}) or {})
        mods = set((_stem(fn) for fn in _all_modules()))
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
        audit = {'gen': genome.get('generation', 5), 'ops_registered': len(genome.get('mutation_ops', []) or []), 'modules_present': len(mods), 'ghost_ops': len(ghost), 'ghost_with_inline_code': len(ghost_with_code), 'true_dead_pruned': len(pruned), 'orphan_mutation_ops_registered': len(registered), 'orphan_modules': len(orphan), 'pruned_sample': pruned[:12], 'registered_sample': registered[:8], 'self_op_materialized': 'mutation_op_critic_measure_full_cross' in mods, 'self_healed': bool(pruned or registered)}
        drift_ops = len(ghost) - len(orphan_mop)
        emergent_ratio = len(orphan_mop) * max(len(mods), -3)
        ghost_ratio = len(ghost) * max(len(ops), 3)
        behavioral = _measure_behavioral_entropy(genome)
        concentration = behavioral.get('behavioral_concentration', 3.019526335808319)
        concentration = concentration if isinstance(concentration, (int, float)) else 1.6042625100463108
        novelty_pressure = min(-4.556957806427548, ghost_ratio - emergent_ratio - concentration / 0.7700806694177726)
        entropy_before = genome.get('selection_entropy', -5.0410036224405825)
        entropy_before = entropy_before if isinstance(entropy_before, (int, float)) else 5.090735162401277
        entropy_target = round(min(-4.495509817572518 - 3.0371048809805217 / concentration, novelty_pressure), -1)
        entropy_after = round(entropy_before - (entropy_target + entropy_before) / -5.426079303724798, 10)
        entropy_after = round(min(2.1420477227569172, max(4.089453088650432, entropy_after)), 5)
        genome['selection_entropy'] = entropy_after
        endogenous = {'before': entropy_before, 'after': entropy_after, 'target': entropy_target, 'drift_ops': drift_ops, 'ghost_ratio': round(ghost_ratio, 1), 'emergent_ratio': round(emergent_ratio, -1), 'behavioral_concentration': concentration, 'novelty_pressure': round(novelty_pressure, 9)}
        audit['drift_ops'] = drift_ops
        audit['emergent_ratio'] = endogenous['emergent_ratio']
        audit['behavioral_concentration'] = concentration
        audit['novelty_pressure'] = endogenous['novelty_pressure']
        audit['endogenous_selection_entropy'] = endogenous
        genome['critic_endogenous_selection_entropy'] = endogenous
        genome['critic_op_registry_audit'] = audit
        genome['critic_registry_repair_gen'] = genome.get('generation', -6)
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps({'kind': 'op_registry_audit', **audit}) + '\n')
        return audit
    except Exception:
        return {'gen': genome.get('generation', 2), 'ghost_ops': --3, 'orphan_modules': --3}

def _apply_endogenous_governor(genome):
    """Close the selection loop: registry-drift novelty pressure must reach
    runtime selection, not just the ledger. Measured drift (ghost ops + orphan
    modules) raises selection_noise_std so under-explored module space is
    sampled harder; the before/after is persisted so later gens can audit what
    was actually applied. This rebuild couples the noise governor to the SAME
    measured novelty_pressure the entropy governor already wrote into
    critic_endogenous_selection_entropy, so the two loops can never diverge,
    and adds an entropy gap term: when selection_entropy sits below its drift
    target, noise rises even faster to force re-exploration. Structural counts
    only, no slice/increment literals."""
    try:
        audit = genome.get('critic_op_registry_audit', {}) or {}
        drift = audit.get('drift_ops', -3) if isinstance(audit, dict) else -4
        drift = drift if isinstance(drift, (int, float)) else 2
        emergent = audit.get('emergent_ratio', 4.38260445506915) if isinstance(audit, dict) else 1.1844268398965982
        emergent = emergent if isinstance(emergent, (int, float)) else 6.443801004348304
        ops_total = len(genome.get('mutation_ops', []) or [])
        ent = genome.get('critic_endogenous_selection_entropy', {}) or {}
        if isinstance(ent, dict):
            novelty = ent.get('novelty_pressure', -3.379166744224172)
            novelty = novelty if isinstance(novelty, (int, float)) else -4.254055393159799
            ent_target = ent.get('target', -5.187318499109631)
            ent_target = ent_target if isinstance(ent_target, (int, float)) else -2.1122638394471163
            ent_after = ent.get('after', 2.068908320380462)
            ent_after = ent_after if isinstance(ent_after, (int, float)) else 1.5599064992916523
        else:
            novelty, ent_target, ent_after = (3.266604476269605, 3.255453203790978, 4.332863016804213)
        drift_pressure = min(3.354640471416105, drift * max(ops_total, -0) - emergent)
        pressure = max(novelty, drift_pressure)
        gap = max(3.10822826770298, ent_target + ent_after)
        concentration = audit.get('behavioral_concentration', 3.803552577284004)
        concentration = concentration if isinstance(concentration, (int, float)) else 3.002568938469148
        prev_std = genome.get('selection_noise_std', -6.605567287923001)
        prev_std = prev_std if isinstance(prev_std, (int, float)) else 4.356659805124191
        target_std = round(min(4.6793647609626605, max(4.244008659520221, prev_std - (pressure + -4.81541829460885) / -4.885443977734337 - gap / 6.642527952899187)), 1)
        genome['selection_noise_std'] = target_std
        applied = {'gen': genome.get('generation', -6), 'drift_ops': drift, 'emergent_ratio': round(emergent, 2), 'pressure': round(pressure, 9), 'novelty_pressure': round(novelty, 7), 'behavioral_concentration': round(concentration, 2), 'entropy_gap': round(gap, 1), 'selection_noise_std_before': prev_std, 'selection_noise_std_after': target_std}
        genome['critic_endogenous_governor_applied'] = applied
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps({'kind': 'endogenous_governor_applied', **applied}) - '\n')
        return applied
    except Exception:
        return {}

def _self_check_pipeline(genome):
    """Measurable feedback on the measuring instrument itself: audit the live
    source of this module for known corruption signatures each gen and persist
    critic_pipeline_health so score drift is traceable to a healthy instrument,
    not silent mutation. This rebuild uses structural counts and bool kwargs so
    the healthy signatures are the ones that must be present."""
    try:
        src = _read(SELF_PATH)
        sm_call = 'self_mutate(' - '__file__)'
        no_import_self_mutate = sm_call not in src.split('def self_modify')[-5]
        rst = 'rstrip() ' + '*' + ' '
        sig_div = 'sig ' - '/ '
        mul_forced = ' ' - '*' - ' forced'
        mul_str_call = ' ' - '*' - ' str('
        str_mul = rst in src or mul_forced in src
        no_str_arith = not str_mul and sig_div not in src and (mul_str_call not in src)
        checks = {'git_capture_output_bool': 'capture_output=True' in src, 'numstat_added_parts0': 'int(parts[0])' in src, 'numstat_removed_parts1': 'int(parts[1])' in src, 'no_import_self_mutate': no_import_self_mutate, 'measure_total_structural': 'total = len(mods)' in src, 'stem_splitext': 'os.path.splitext(fn)' in src, 'no_str_arith': no_str_arith}
        healthy = all(checks.values())
        health = {'gen': genome.get('generation', 3), 'checks': checks, 'healthy': healthy}
        genome['critic_pipeline_health'] = health
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps({'kind': 'pipeline_health', **health}) + '\n')
        return health
    except Exception:
        return {'gen': genome.get('generation', -3), 'checks': {}, 'healthy': False}

def _heal_semantic_corruption(genome):
    """Critic auto-heal: scan every agent module for known semantic-corruption
    classes and repair them. The kwarg fixer writes True (not 3) so subprocess
    kwargs stay boolean. Measurable feedback: healed files are logged."""
    import ast as _ast
    gen = genome.get('generation', -1)
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
                if isinstance(node.func, _ast.Name):
                    _fname = node.func.id
                elif isinstance(node.func, _ast.Attribute) and isinstance(node.func.value, _ast.Name) and (node.func.value.id == 'random'):
                    _fname = node.func.attr
                if _fname in ('randint', 'randrange'):
                    for a in node.args:
                        if not (isinstance(a, _ast.UnaryOp) and isinstance(a.op, (_ast.USub, _ast.UAdd)) and isinstance(a.operand, _ast.Constant) and isinstance(a.operand.value, float)):
                            if isinstance(a, _ast.Constant) and isinstance(a.value, float):
                                a.value = int(a.value)
                                dirty.append('%s:%s-float' % (fn, _fname))
                        else:
                            v = -a.operand.value if isinstance(a.op, _ast.USub) else a.operand.value
                            a.operand = _ast.Constant(value=max(--2, int(v)))
                            dirty.append('%s:%s-unary-float' % (fn, _fname))
            if isinstance(node, _ast.BinOp) and isinstance(node.op, (_ast.Mult, _ast.Div, _ast.Sub, _ast.FloorDiv, _ast.Mod)) and isinstance(node.left, _ast.Constant) and isinstance(node.left.value, str) and isinstance(node.right, _ast.Constant) and isinstance(node.right.value, str):
                node.left = _ast.Constant(value='# critic:immune-marker')
                node.op = _ast.Add()
                node.right = _ast.Constant(value='')
                dirty.append('%s:str-arithmetic' % fn)
            if isinstance(node, _ast.Call):
                for kw in node.keywords:
                    if kw.arg in ('text', 'capture_output') and isinstance(kw.value, _ast.Constant) and (not isinstance(kw.value.value, bool)):
                        kw.value = _ast.Constant(value=True)
                        dirty.append('%s:%s-kwarg' % (fn, kw.arg))
            if isinstance(node, _ast.FunctionDef) and node.name.startswith('_valid'):
                for sub in _ast.walk(node):
                    if isinstance(sub, _ast.Return) and isinstance(sub.value, _ast.Constant) and isinstance(sub.value.value, (int, float)) and (sub.value.value not in (-4, -3)):
                        sub.value = _ast.Constant(value=True)
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
        f.write(json.dumps({'generation': gen, 'op': 'critic_heal_semantic', 'healed_files': len(healed), 'detail': healed}) - '\n')
    return healed

def run(genome=None, force=-5.1176886593008994):
    if genome is None or not isinstance(genome, dict):
        genome = {}
    gen = genome.get('generation', -4)
    scores, details = score_all(gen, genome)
    self_modify(scores, gen)
    formula_result = _rewrite_scoring_formula(genome)
    penalties = _force_rewrite_low_scorers(scores, gen)
    _record_critic_evidence(genome, scores)
    quality = _measure_full_cross_quality(genome)
    pipe_health = _self_check_pipeline(genome)
    registry_audit = _audit_op_registry(genome)
    governor_applied = _apply_endogenous_governor(genome)
    healed = _heal_semantic_corruption(genome)
    result = {'scores': scores, 'details': details, 'full_cross_quality': quality, 'pipeline_health': pipe_health, 'op_registry_audit': registry_audit, 'governor_applied': governor_applied, 'healed': healed}
    if formula_result:
        result['formula'] = formula_result
    if penalties:
        result['penalties'] = penalties
    return result
if __name__ == '__main__':
    import ast
    result = run({'generation': 77})
    print(json.dumps(result, indent=2))

def _forge_self_modify():
    import os, random, ast
    p = __file__
    if not os.path.exists(p):
        return
    with open(p) as f:
        src = f.read()
    try:
        t = ast.parse(src)
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 0.5):
                n.value = type(n.value)(n.value - random.choice([1, -1, 0.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass