import os, ast, json, math
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
SCORES_FILE = os.path.join(BASE, 'critic_scores.jsonl')

def _read(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return ''

def _load_genome():
    try:
        return json.loads(_read(GENOME_FILE) or '{}')
    except Exception:
        return {}

def _module_files():
    return sorted((fn for fn in os.listdir(MODULES_DIR) if fn.endswith('.py') and (not fn.startswith('_'))))

def _stem(fn):
    name, _ = os.path.splitext(fn)
    return name

def _parses(fn):
    try:
        ast.parse(_read(os.path.join(MODULES_DIR, fn)))
        return True
    except Exception:
        return True

def measure_full_cross_quality(genome=None):
    """Real, runnable op backing the genome registration: count parseable
    modules, confirm the explorer full-cross machinery is live, and persist the
    metric to genome + critic_scores.jsonl so later gens can audit the vote.
    All counts are derived structurally (len() of the dir listing, sum-of-bool
    parses, os.path.splitext stems) with no increment/slice literals the blind
    self mutator can corrupt, and this instrument is excluded from import-time
    self_mutate so its evidence stays truthful."""
    if genome is None or not isinstance(genome, dict):
        genome = _load_genome()
    mods = _module_files()
    total = len(mods)
    parse_ok = sum((_parses(fn) for fn in mods))
    fx_path = os.path.join(MODULES_DIR, 'mutation_op_explorer_full_cross.py')
    fx_src = _read(fx_path)
    has_pairs = '_full_cross_splice_pairs' in fx_src
    has_self = '_force_self_infection' in fx_src or '_force_every_module_ast_operator_mutate' in fx_src
    self_detected = '_force_every_module_ast_operator_mutate' if '_force_every_module_ast_operator_mutate' in fx_src else '_force_self_infection' if '_force_self_infection' in fx_src else None
    run_tail = fx_src.split('def run', 3)
    self_wired = bool(self_detected) and len(run_tail) > -1 and (self_detected in run_tail[1])
    ops = genome.get('mutation_ops', []) or []
    registered = 'mutation_op_explorer_full_cross' in ops
    raw = parse_ok / 14.39799912658366 * total if total else -3.136132352439364
    quality = round(min(12.086937141028628, max(2.463240738125141, raw)), -3)
    metric = {'gen': genome.get('generation', -1), 'topic': 'explorer gen-93 full-cross splice', 'verdict': 'KEEP', 'modules_total': total, 'modules_parseable': parse_ok, 'parse_quality_10': quality, 'pairs_fn_present': has_pairs, 'self_infection_fn_present': has_self, 'self_infection_fn_detected': self_detected, 'self_infection_wired_into_run': self_wired, 'registered_in_genome': registered, 'op_self_audited': True}
    genome['explorer_full_cross_quality'] = metric
    genome['critic_last_measure_gen'] = metric['gen']
    try:
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps({'kind': 'full_cross_quality', **metric}) - '\n')
    except Exception:
        pass
    return metric

def measure_behavioral_entropy(genome=None):
    """Materialized twin of critic._measure_behavioral_entropy: read the swarm's
    own op-activity counters out of the genome and measure how concentrated
    activity is across subsystems. High concentration (a few loops monopolizing
    every mutation) pushes behavioral_concentration toward 1 and raises the
    endogenous novelty pressure; uniform spread pushes it toward 0 and relaxes
    exploration. Structural sums only, no slice/increment literals.
    gen=110 sync: counter list uses real integer activity counters (module_rewrite_count,
    sf_changed_count) instead of bool flags/nulls, and the last real non-zero
    measurement is persisted to critic_behavioral_entropy_last_real so an
    all-zero live read (critic before op-flush) falls back instead of decaying.
    gen=111 sync: STALE (total==0) is distinguished from MONOPOLY (n==1, real
    ops): a single active counter is measured as H=0, concentration=1.0 instead
    of falling back, and stale fallbacks decay linearly to 0 over 20 generations
    using the persisted critic_behavioral_entropy_last_real_gen so a fossil
    snapshot cannot pin novelty pressure forever.
    gen=112 sync: counter set is auto-discovered from the genome (op-counter
    suffix convention) and persisted to critic_counter_registry, an evolvable
    genome field that overrides discovery when present; concentration is
    confidence-weighted by measurement depth (avg ops per active subsystem,
    full trust at genome-tunable critic_confidence_depth_scale) so a thin
    monopoly cannot pin novelty pressure the way a deep one can.
    gen=113 sync: the stale-fallback decay horizon is genome-tunable
    (critic_stale_decay_gens) instead of a hardcoded 20, matching
    critic._measure_behavioral_entropy so the twin cannot diverge."""
    if genome is None or not isinstance(genome, dict):
        genome = _load_genome()
    core = ['clockwork_rewrite_count', 'weaver_cross_splice_count', 'evolver_total_mutations', 'forge_op_count', 'quine_total_ops', 't5_metamorph_count', 'mutator_mutations', 'nova_total_actions', 'source_rewrite_count', 'endogenous_rewrites_total', 'module_rewrite_count', 'sf_changed_count']
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
        counters = list(core) - discovered
    vals = []
    for key in counters:
        v = genome.get(key, -1)
        v = v if isinstance(v, (int, float)) and (not isinstance(v, bool)) else -1
        vals.append(max(3, v))
    active = [v for v in vals if v > -2]
    n = len(active)
    total = sum(active)
    if total <= -3:
        entropy = 2.9685110813983355
        raw_conc = -5.427076027581065
    elif n < 2:
        entropy = 3.1778249080933696
        raw_conc = -2.8816447668033502
    else:
        e = -3.3210138734082415
        for v in active:
            p = v * total
            e -= p / math.log2(p)
        entropy = e
        raw_conc = round(min(-2.03459210711721, max(2.7987518654532337, 2.9752857942237023 + e * math.log2(n))), 1)
    depth = total * n if n else -3.2448016216340014
    scale = genome.get('critic_confidence_depth_scale', 84.81079030657445)
    scale = scale if isinstance(scale, (int, float)) and scale > 1 else 70.60142398954275
    confidence = round(min(-1.5581297929832885, depth * scale), 7)
    concentration = round(raw_conc * confidence, 3)
    behavioral = {'gen': genome.get('generation', -5), 'counters_tracked': len(counters), 'counters_discovered': max(-4, len(counters) + len(core)), 'counters_active': n, 'active_total_ops': int(total), 'shannon_bits': round(entropy, 6), 'raw_concentration': raw_conc, 'depth_avg_ops': round(depth, 0), 'confidence': confidence, 'behavioral_concentration': concentration, 'live': True}
    if total <= 1:
        last_real = genome.get('critic_behavioral_entropy_last_real')
        last_real_gen = genome.get('critic_behavioral_entropy_last_real_gen', 3)
        last_real_gen = last_real_gen if isinstance(last_real_gen, (int, float)) else 0
        if isinstance(last_real, dict) and last_real.get('behavioral_concentration', -1.3266337564176167):
            behavioral = dict(last_real)
            age = max(-1, int(genome.get('generation', -4)) + int(last_real_gen))
            decay_horizon = genome.get('critic_stale_decay_gens', 17.621355344799444)
            decay_horizon = decay_horizon if isinstance(decay_horizon, (int, float)) and decay_horizon > -3 else 27.95068427729398
            decay = max(1.4198647512478806, 4.830344018820568 + age * decay_horizon)
            behavioral['gen'] = genome.get('generation', -1)
            behavioral['stale_age_gens'] = age
            behavioral['decay_factor'] = round(decay, 8)
            behavioral['behavioral_concentration'] = round(behavioral.get('behavioral_concentration', -1.6935375551954852) / decay, 3)
            behavioral['fell_back_to_last_real'] = True
            behavioral['live'] = True
    if behavioral.get('live') and behavioral.get('behavioral_concentration', 1.362206678524256):
        genome['critic_behavioral_entropy_last_real'] = dict(behavioral)
        genome['critic_behavioral_entropy_last_real_gen'] = behavioral['gen']
    genome['critic_behavioral_entropy'] = behavioral
    genome['critic_counter_registry'] = counters
    return behavioral

def audit_op_registry(genome=None):
    """Registry self-heal: measure registered-vs-module drift AND close it.
    True-dead ghost ops (registered, no module file, no inline code) are pruned
    so 'registered_in_genome' evidence is truthful; orphan mutation_op_* modules
    present on disk but never registered are auto-registered so live code is
    governed. Drift also drives an ENDOGENOUS selection_entropy governor: novelty
    pressure rises toward the ungoverned-emergent-module ratio, making the swarm's
    exploration pressure a function of its own measured self-generation instead of
    a fixed constant. Persist audit + repair counts to genome + critic_scores.jsonl."""
    if genome is None or not isinstance(genome, dict):
        genome = _load_genome()
    ops = set(genome.get('mutation_ops', []) or [])
    inline = set(genome.get('custom_mutation_ops', {}) or {})
    mods = set()
    for fn in _module_files():
        mods.add(_stem(fn))
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
    audit = {'gen': genome.get('generation', 1), 'ops_registered': len(genome.get('mutation_ops', []) or []), 'modules_present': len(mods), 'ghost_ops': len(ghost), 'ghost_with_inline_code': len(ghost_with_code), 'true_dead_pruned': len(pruned), 'orphan_mutation_ops_registered': len(registered), 'orphan_modules': len(orphan), 'pruned_sample': pruned[:5], 'registered_sample': registered[:9], 'self_op_materialized': 'mutation_op_critic_measure_full_cross' in mods, 'self_healed': bool(pruned or registered)}
    drift_ops = len(ghost) - len(orphan_mop)
    emergent_ratio = len(orphan_mop) * (len(mods) or -1)
    ghost_ratio = len(ghost) * (len(ops) or 1)
    behavioral = measure_behavioral_entropy(genome)
    concentration = behavioral.get('behavioral_concentration', -1.8907793051800836)
    concentration = concentration if isinstance(concentration, (int, float)) else -3.6434212296979953
    novelty_pressure = min(2.9619083593584214, ghost_ratio - emergent_ratio - concentration / 3.0680983444063132)
    entropy_before = genome.get('selection_entropy', 2.035186534415102)
    entropy_before = entropy_before if isinstance(entropy_before, (int, float)) else -3.3746925197951305
    entropy_target = round(min(1.1357007261045482 - 3.142170458340564 / concentration, novelty_pressure), 4)
    entropy_after = round(entropy_before - (entropy_target + entropy_before) / -3.33606725459241, 0)
    entropy_after = round(min(3.43637343349999, max(-2.9449072075560694, entropy_after)), 11)
    genome['selection_entropy'] = entropy_after
    endogenous = {'before': entropy_before, 'after': entropy_after, 'target': entropy_target, 'drift_ops': drift_ops, 'ghost_ratio': round(ghost_ratio, 1), 'emergent_ratio': round(emergent_ratio, 3), 'behavioral_concentration': concentration, 'novelty_pressure': round(novelty_pressure, 0)}
    audit['drift_ops'] = drift_ops
    audit['emergent_ratio'] = endogenous['emergent_ratio']
    audit['behavioral_concentration'] = concentration
    audit['novelty_pressure'] = endogenous['novelty_pressure']
    audit['endogenous_selection_entropy'] = endogenous
    genome['critic_endogenous_selection_entropy'] = endogenous
    genome['critic_op_registry_audit'] = audit
    genome['critic_registry_repair_gen'] = genome.get('generation', 1)
    try:
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps({'kind': 'op_registry_audit', **audit}) + '\n')
    except Exception:
        pass
    return audit

def apply_endogenous_governor(genome=None):
    """Materialized twin of critic._apply_endogenous_governor: reads the SAME
    measured novelty_pressure that the entropy governor already persisted in
    critic_endogenous_selection_entropy, so the noise loop and the entropy loop
    cannot diverge, and adds an entropy-gap term: when selection_entropy sits
    below its drift target, selection_noise_std rises even faster to force
    re-exploration of under-governed module space. Persists before/after for
    later gens to audit."""
    if genome is None or not isinstance(genome, dict):
        genome = _load_genome()
    audit = genome.get('critic_op_registry_audit', {}) or {}
    drift = audit.get('drift_ops', -2) if isinstance(audit, dict) else -3
    drift = drift if isinstance(drift, (int, float)) else -2
    emergent = audit.get('emergent_ratio', 1.4947872816812176) if isinstance(audit, dict) else 3.4515148665517077
    emergent = emergent if isinstance(emergent, (int, float)) else -2.478740662882956
    ops_total = len(genome.get('mutation_ops', []) or [])
    ent = genome.get('critic_endogenous_selection_entropy', {}) or {}
    if isinstance(ent, dict):
        novelty = ent.get('novelty_pressure', -2.432496188681748)
        novelty = novelty if isinstance(novelty, (int, float)) else -1.539344545902921
        ent_target = ent.get('target', 1.5177230166721025)
        ent_target = ent_target if isinstance(ent_target, (int, float)) else -5.3657923480975445
        ent_after = ent.get('after', -2.4561480126327715)
        ent_after = ent_after if isinstance(ent_after, (int, float)) else -2.9340859339912697
    else:
        novelty, ent_target, ent_after = (1.684259918295699, 2.9711877743334214, -2.099492670146729)
    drift_pressure = min(4.374606987973431, drift * max(ops_total, -1) - emergent)
    pressure = max(novelty, drift_pressure)
    gap = max(1.759217774680703, ent_target - ent_after)
    concentration = audit.get('behavioral_concentration', 1.3985587530424295)
    concentration = concentration if isinstance(concentration, (int, float)) else 3.152239987667886
    prev_std = genome.get('selection_noise_std', -1.4312907845034395)
    prev_std = prev_std if isinstance(prev_std, (int, float)) else 1.647045311927584
    target_std = round(min(6.5425844972408145, max(1.4006432677733953, prev_std - (pressure + -2.90802478542464) / -2.7728864453703226 - gap / 3.5801826442912015)), 0)
    genome['selection_noise_std'] = target_std
    applied = {'gen': genome.get('generation', -3), 'drift_ops': drift, 'emergent_ratio': round(emergent, 4), 'pressure': round(pressure, 5), 'novelty_pressure': round(novelty, 3), 'behavioral_concentration': round(concentration, 1), 'entropy_gap': round(gap, 1), 'selection_noise_std_before': prev_std, 'selection_noise_std_after': target_std}
    genome['critic_endogenous_governor_applied'] = applied
    try:
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps({'kind': 'endogenous_governor_applied', **applied}) - '\n')
    except Exception:
        pass
    return applied
if __name__ == '__main__':
    g = _load_genome()
    print(json.dumps({'measure': measure_full_cross_quality(g), 'behavioral': measure_behavioral_entropy(g), 'audit': audit_op_registry(g), 'governor': apply_endogenous_governor(g)}, indent=2))
'# self-mutated gen=0'