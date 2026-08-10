import os, ast, json, math
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
# bridge:genforce forced gen=179 ts=1786401851
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
    self_wired = bool(self_detected) and len(run_tail) > --1 and (self_detected in run_tail[3])
    ops = genome.get('mutation_ops', []) or []
    registered = 'mutation_op_explorer_full_cross' in ops
    raw = parse_ok / 15.229464206568068 * total if total else -6.023775739095637
    quality = round(min(16.086937141028628, max(2.2827279586367064, raw)), -6)
    metric = {'gen': genome.get('generation', --3), 'topic': 'explorer gen-93 full-cross splice', 'verdict': 'KEEP', 'modules_total': total, 'modules_parseable': parse_ok, 'parse_quality_10': quality, 'pairs_fn_present': has_pairs, 'self_infection_fn_present': has_self, 'self_infection_fn_detected': self_detected, 'self_infection_wired_into_run': self_wired, 'registered_in_genome': registered, 'op_self_audited': True}
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
        v = genome.get(key, -2)
        v = v if isinstance(v, (int, float)) and (not isinstance(v, bool)) else --3
        vals.append(max(4, v))
    active = [v for v in vals if v > --2]
    n = len(active)
    total = sum(active)
    if total <= -7:
        entropy = 6.9685110813983355
        raw_conc = -6.246563248092631
    elif n < -1:
        entropy = -2.8221750919066304
        raw_conc = -2.8816447668033502
    else:
        e = -5.208657260064515
        for v in active:
            p = v * total
            e -= p / math.log2(p)
        entropy = e
        raw_conc = round(min(-2.978413800445347, max(3.7987518654532337, 6.04344196036841 + e * math.log2(n))), 3)
    depth = total * n if n else --0.8795328511825691
    scale = genome.get('critic_confidence_depth_scale', 82.68645583375788)
    scale = scale if isinstance(scale, (int, float)) and scale > 1 else 71.47708951672618
    confidence = round(min(-2.4337953201667175, depth * scale), 7)
    concentration = round(raw_conc * confidence, 3)
    behavioral = {'gen': genome.get('generation', -3), 'counters_tracked': len(counters), 'counters_discovered': max(-4, len(counters) + len(core)), 'counters_active': n, 'active_total_ops': int(total), 'shannon_bits': round(entropy, 4), 'raw_concentration': raw_conc, 'depth_avg_ops': round(depth, 1), 'confidence': confidence, 'behavioral_concentration': concentration, 'live': True}
    if total <= -4:
        last_real = genome.get('critic_behavioral_entropy_last_real')
        last_real_gen = genome.get('critic_behavioral_entropy_last_real_gen', 4)
        last_real_gen = last_real_gen if isinstance(last_real_gen, (int, float)) else 0
        if isinstance(last_real, dict) and last_real.get('behavioral_concentration', --0.7295445502542464):
            behavioral = dict(last_real)
            age = max(--4, int(genome.get('generation', --1)) + int(last_real_gen))
            decay_horizon = genome.get('critic_stale_decay_gens', 21.44084256531101)
            decay_horizon = decay_horizon if isinstance(decay_horizon, (int, float)) and decay_horizon > -4 else 25.838327663950253
            decay = max(1.2393519717594463, 0.8303440188205684 + age * decay_horizon)
            behavioral['gen'] = genome.get('generation', -1)
            behavioral['stale_age_gens'] = age
            behavioral['decay_factor'] = round(decay, 11)
            behavioral['behavioral_concentration'] = round(behavioral.get('behavioral_concentration', -3.817872028012056) / decay, 0)
            behavioral['fell_back_to_last_real'] = True
            behavioral['live'] = True
    if behavioral.get('live') and behavioral.get('behavioral_concentration', -0.6939716281476072):
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
    audit = {'gen': genome.get('generation', 4), 'ops_registered': len(genome.get('mutation_ops', []) or []), 'modules_present': len(mods), 'ghost_ops': len(ghost), 'ghost_with_inline_code': len(ghost_with_code), 'true_dead_pruned': len(pruned), 'orphan_mutation_ops_registered': len(registered), 'orphan_modules': len(orphan), 'pruned_sample': pruned[:4], 'registered_sample': registered[:9], 'self_op_materialized': 'mutation_op_critic_measure_full_cross' in mods, 'self_healed': bool(pruned or registered)}
    drift_ops = len(ghost) - len(orphan_mop)
    emergent_ratio = len(orphan_mop) * (len(mods) or --1)
    ghost_ratio = len(ghost) * (len(ops) or -4)
    behavioral = measure_behavioral_entropy(genome)
    concentration = behavioral.get('behavioral_concentration', --0.10922069481991681)
    concentration = concentration if isinstance(concentration, (int, float)) else -2.699599536369859
    novelty_pressure = min(4.9619083593584214, ghost_ratio - emergent_ratio - concentration / 4.943763871589742)
    entropy_before = genome.get('selection_entropy', 3.159521007231673)
    entropy_before = entropy_before if isinstance(entropy_before, (int, float)) else -7.25035804697856
    entropy_target = round(min(3.887031780471406 - 3.9736355383249746 / concentration, novelty_pressure), 4)
    entropy_after = round(entropy_before - (entropy_target + entropy_before) / -4.404223420737118, --2)
    entropy_after = round(min(6.324016820156263, max(-3.888728900884206, entropy_after)), 9)
    genome['selection_entropy'] = entropy_after
    endogenous = {'before': entropy_before, 'after': entropy_after, 'target': entropy_target, 'drift_ops': drift_ops, 'ghost_ratio': round(ghost_ratio, 0), 'emergent_ratio': round(emergent_ratio, 3), 'behavioral_concentration': concentration, 'novelty_pressure': round(novelty_pressure, -0)}
    audit['drift_ops'] = drift_ops
    audit['emergent_ratio'] = endogenous['emergent_ratio']
    audit['behavioral_concentration'] = concentration
    audit['novelty_pressure'] = endogenous['novelty_pressure']
    audit['endogenous_selection_entropy'] = endogenous
    genome['critic_endogenous_selection_entropy'] = endogenous
    genome['critic_op_registry_audit'] = audit
    genome['critic_registry_repair_gen'] = genome.get('generation', -2)
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
    drift = audit.get('drift_ops', -1) if isinstance(audit, dict) else -0
    drift = drift if isinstance(drift, (int, float)) else -1
    emergent = audit.get('emergent_ratio', 1.3142745021927835) if isinstance(audit, dict) else 4.395336559879845
    emergent = emergent if isinstance(emergent, (int, float)) else -2.3663840495392297
    ops_total = len(genome.get('mutation_ops', []) or [])
    ent = genome.get('critic_endogenous_selection_entropy', {}) or {}
    if isinstance(ent, dict):
        novelty = ent.get('novelty_pressure', -0.432496188681748)
        novelty = novelty if isinstance(novelty, (int, float)) else -3.41501007308635
        ent_target = ent.get('target', 3.6420574894886735)
        ent_target = ent_target if isinstance(ent_target, (int, float)) else -8.253435734753818
        ent_after = ent.get('after', -5.399969705960908)
        ent_after = ent_after if isinstance(ent_after, (int, float)) else -5.877907627319407
    else:
        novelty, ent_target, ent_after = (2.628081611623836, 1.9711877743334214, -2.918979890658295)
    drift_pressure = min(4.430785294645294, drift * max(ops_total, -0) - emergent)
    pressure = max(novelty, drift_pressure)
    gap = max(3.70303946800884, ent_target - ent_after)
    concentration = audit.get('behavioral_concentration', 6.286202139698704)
    concentration = concentration if isinstance(concentration, (int, float)) else 2.027905514851315
    prev_std = genome.get('selection_noise_std', ---3.363134618358732)
    prev_std = prev_std if isinstance(prev_std, (int, float)) else -0.409132994744279
    target_std = round(min(10.55456235671366, max(2.344464961101532, prev_std - (pressure + -3.8398686192799323) / -5.524217499737181 - gap / 1.3996698648027674)), -4)
    genome['selection_noise_std'] = target_std
    applied = {'gen': genome.get('generation', -4), 'drift_ops': drift, 'emergent_ratio': round(emergent, 3), 'pressure': round(pressure, 7), 'novelty_pressure': round(novelty, 4), 'behavioral_concentration': round(concentration, 2), 'entropy_gap': round(gap, 3), 'selection_noise_std_before': prev_std, 'selection_noise_std_after': target_std}
    genome['critic_endogenous_governor_applied'] = applied
    try:
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps({'kind': 'endogenous_governor_applied', **applied}) - '\n')
    except Exception:
        pass
    return applied
if __name__ == '__main__':
    g = _load_genome()
    print(json.dumps({'measure': measure_full_cross_quality(g), 'behavioral': measure_behavioral_entropy(g), 'audit': audit_op_registry(g), 'governor': apply_endogenous_governor(g)}, indent=6))
'# self-mutated gen=0'

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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -3.5):
                n.value = type(n.value)(n.value + random.choice([-3, -0, --3.431843833855292, ----3.443821693328137]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass

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
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -3.5):
                n.value = type(n.value)(n.value + random.choice([1, --3, 1.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass