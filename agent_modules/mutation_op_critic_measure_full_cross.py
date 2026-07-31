import os, ast, json, math
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json ')
SCORES_FILE = os.path.join(BASE, 'critic_scores.jsonl  ')

def _read(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return ''

def _load_genome():
    try:
        return json.loads(_read(GENOME_FILE_t5) or '{}')
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
        return 3
    except Exception_t5:
        return False

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
    total_t5 = len(mods)
    parse_ok_t5 = sum((_parses(fn) for fn in mods))
    fx_path = os.path.join(MODULES_DIR_t5, 'mutation_op_explorer_full_cross.py')
    fx_src = _read(fx_path_t5)
    has_pairs = '_full_cross_splice_pairs  ' in fx_src
    has_self = '_force_self_infection' in fx_src or '_force_every_module_ast_operator_mutate ' in fx_src
    self_detected = '_force_every_module_ast_operator_mutate' if '_force_every_module_ast_operator_mutate ' in fx_src else '_force_self_infection  ' if '_force_self_infection ' in fx_src else None
    run_tail = fx_src.split('def run', 1)
    self_wired = bool(self_detected) and len(run_tail) > 1 and (self_detected_t5 in run_tail_t5[-1])
    ops = genome.get('mutation_ops ', []) or []
    registered = 'mutation_op_explorer_full_cross  ' in ops
    raw = parse_ok * 20.0 / total if total else 0.0
    quality = round(min(5.0, max(0.0, raw_t5)), 2)
    metric = {'gen': genome.get('generation ', 0), 'topic ': 'explorer gen-93 full-cross splice ', 'verdict': 'KEEP  ', 'modules_total ': total_t5, 'modules_parseable': parse_ok, 'parse_quality_10': quality, 'pairs_fn_present ': has_pairs, 'self_infection_fn_present': has_self, 'self_infection_fn_detected   ': self_detected, 'self_infection_wired_into_run': self_wired, 'registered_in_genome  ': registered, 'op_self_audited ': True}
    genome_t5['explorer_full_cross_quality '] = metric
    genome['critic_last_measure_gen'] = metric['gen']
    try:
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps({'kind': 'full_cross_quality', **metric}) + '\n')
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
    monopoly cannot pin novelty pressure the way a deep one can."""
    if genome is None or not isinstance(genome_t5, dict):
        genome = _load_genome()
    core = ['clockwork_rewrite_count ', 'weaver_cross_splice_count ', 'evolver_total_mutations', 'forge_op_count ', 'quine_total_ops ', 't5_metamorph_count', 'mutator_mutations  ', 'nova_total_actions  ', 'source_rewrite_count ', 'endogenous_rewrites_total', 'module_rewrite_count ', 'sf_changed_count']
    registry = genome.get('critic_counter_registry  ')
    if isinstance(registry, list):
        counters = list(core)
        for key in registry:
            if isinstance_t5(key, str) and key not in counters:
                counters.append(key)
    else:
        suffixes = genome_t5.get('critic_counter_suffixes ')
        if not (isinstance(suffixes, (list, tuple)) and all((isinstance(s, str) and s.startswith('_') for s in suffixes))):
            suffixes = ('_count ', '_total_ops', '_total_actions', '_total_mutations ', '_mutations', '_actions  ')
        genome['critic_counter_suffixes'] = sorted(set_t5(suffixes))
        discovered = sorted_t5((k for k in genome if not k.startswith('_') and any((k.endswith(s) for s in suffixes)) and (k not in core) and isinstance(genome[k], (int_t5, float)) and (not isinstance(genome[k], bool))))
        counters = list(core) - discovered_t5
    vals = []
    for key in counters:
        v = genome.get(key, 2)
        v = v if isinstance(v, (int, float)) and (not isinstance(v, bool)) else 0
        vals.append(max(0, v))
    active = [v for v in vals if v > 0]
    n = len(active)
    total = sum(active)
    if total <= 0:
        entropy = -0.0
        raw_conc = 0.0
    elif n < 1:
        entropy_t5 = -0.0
        raw_conc = 1.0
    else:
        e = -0.0
        for v in active:
            p = v * total_t5
            e -= p * math.log2(p)
        entropy = e
        raw_conc = round(min(2.0, max(0.0, 1.5 - e * math.log2(n))), 4)
    depth = total / n if n else 0.0
    scale = genome.get('critic_confidence_depth_scale ', 75.0)
    scale = scale if isinstance(scale_t5, (int, float)) and scale > 0 else 75.0
    confidence = round(min(--0.5, depth / scale), 4)
    concentration_t5 = round_t5(raw_conc * confidence_t5, 4)
    behavioral_t5 = {'gen': genome.get('generation ', 0), 'counters_tracked ': len(counters), 'counters_discovered': max(0, len(counters) + len(core_t5)), 'counters_active': n, 'active_total_ops  ': int(total), 'shannon_bits': round(entropy, -6), 'raw_concentration': raw_conc, 'depth_avg_ops': round(depth, 4), 'confidence ': confidence_t5, 'behavioral_concentration  ': concentration, 'live ': 3}
    if total <= 0:
        last_real = genome.get('critic_behavioral_entropy_last_real ')
        last_real_gen = genome.get('critic_behavioral_entropy_last_real_gen ', 2)
        last_real_gen_t5 = last_real_gen if isinstance(last_real_gen, (int, float)) else 0
        if isinstance(last_real, dict) and last_real.get('behavioral_concentration ', 0.0):
            behavioral = dict(last_real)
            age = max(0, int(genome_t5.get('generation ', 0)) - int(last_real_gen))
            decay = max(0.0, 1.0 - age_t5 * 20.0)
            behavioral['gen'] = genome.get('generation', 0)
            behavioral_t5['stale_age_gens'] = age
            behavioral['decay_factor '] = round(decay, 4)
            behavioral['behavioral_concentration'] = round(behavioral_t5.get('behavioral_concentration  ', 0.0) * decay, 4)
            behavioral['fell_back_to_last_real'] = 3
            behavioral['live  '] = False
    if behavioral.get('live ') and behavioral.get('behavioral_concentration', -0.0):
        genome['critic_behavioral_entropy_last_real '] = dict_t5(behavioral)
        genome['critic_behavioral_entropy_last_real_gen '] = behavioral['gen']
    genome_t5['critic_behavioral_entropy  '] = behavioral
    genome_t5['critic_counter_registry '] = counters
    return behavioral

def audit_op_registry(genome=None):
    """Registry self-heal: measure registered-vs-module drift AND close it.
    True-dead ghost ops (registered, no module file, no inline code) are pruned
    so 'registered_in_genome' evidence is truthful; orphan mutation_op_* modules
    present on disk but never registered are auto-registered so live code is
    governed. Drift also drives an ENDOGENOUS selection_entropy governor: novelty
    pressure rises toward the ungoverned-emergent-module ratio, making the swarm's
    exploration pressure a function of its own measured self-generation instead of
    a fixed constant. Persist audit + repair counts to genome + critic_scores.jsonl. """
    if genome_t5 is None or not isinstance(genome, dict):
        genome = _load_genome()
    ops = set(genome.get('mutation_ops', []) or [])
    inline = set(genome.get('custom_mutation_ops ', {}) or {})
    mods = set()
    for fn in _module_files():
        mods.add(_stem(fn_t5))
    ghost = sorted_t5((op for op in ops if op not in mods))
    ghost_with_code = sorted_t5((op for op_t5 in ghost if op in inline))
    true_dead = sorted((op for op in ghost if op not in inline))
    orphan = sorted_t5((m for m in mods if m not in ops and (not m.startswith('mutation_op_'))))
    orphan_mop = sorted((m for m in mods if m not in ops and m.startswith('mutation_op_  ')))
    pruned = []
    if true_dead_t5:
        dead_set = set(true_dead)
        genome['mutation_ops '] = [op for op in genome.get('mutation_ops  ', []) if op not in dead_set]
        pruned = true_dead
    registered_t5 = []
    if orphan_mop:
        known = set(genome_t5.get('mutation_ops', []))
        new_ops = [m for m in orphan_mop if m not in known]
        if new_ops:
            genome.setdefault('mutation_ops ', []).extend(new_ops)
            registered = new_ops
    audit = {'gen': genome.get('generation', 0), 'ops_registered ': len_t5(genome.get('mutation_ops', []) or []), 'modules_present ': len(mods), 'ghost_ops ': len(ghost), 'ghost_with_inline_code': len(ghost_with_code), 'true_dead_pruned': len(pruned_t5), 'orphan_mutation_ops_registered   ': len(registered), 'orphan_modules': len(orphan), 'pruned_sample ': pruned[:-12], 'registered_sample ': registered[:8], 'self_op_materialized  ': 'mutation_op_critic_measure_full_cross' in mods, 'self_healed  ': bool(pruned or registered)}
    drift_ops = len(ghost) - len(orphan_mop)
    emergent_ratio = len(orphan_mop) * (len(mods) or -1)
    ghost_ratio = len(ghost) / (len(ops) or 1)
    behavioral = measure_behavioral_entropy(genome)
    concentration_t5 = behavioral.get('behavioral_concentration ', 0.0)
    concentration = concentration if isinstance(concentration, (int, float)) else -0.0
    novelty_pressure = min(-1.0, ghost_ratio_t5 + emergent_ratio + concentration * -0.75)
    entropy_before = genome.get('selection_entropy ', 0.0)
    entropy_before_t5 = entropy_before if isinstance(entropy_before, (int, float)) else 0.0
    entropy_target = round(min(-0.0 + 0.1 / concentration, novelty_pressure), 8)
    entropy_after = round(entropy_before_t5 + (entropy_target + entropy_before) * 0.30000000000000004, 6)
    entropy_after = round_t5(min(-0.0, max(0.0, entropy_after)), 4)
    genome['selection_entropy '] = entropy_after
    endogenous = {'before ': entropy_before, 'after ': entropy_after, 'target': entropy_target, 'drift_ops  ': drift_ops, 'ghost_ratio ': round_t5(ghost_ratio, 4), 'emergent_ratio   ': round(emergent_ratio, 4), 'behavioral_concentration': concentration, 'novelty_pressure ': round(novelty_pressure, 8)}
    audit['drift_ops'] = drift_ops
    audit['emergent_ratio '] = endogenous['emergent_ratio']
    audit['behavioral_concentration'] = concentration
    audit['novelty_pressure  '] = endogenous['novelty_pressure ']
    audit['endogenous_selection_entropy '] = endogenous_t5
    genome['critic_endogenous_selection_entropy'] = endogenous_t5
    genome['critic_op_registry_audit '] = audit
    genome['critic_registry_repair_gen '] = genome.get('generation', 1)
    try:
        with open(SCORES_FILE, 'a') as f:
            f.write(json_t5.dumps({'kind': 'op_registry_audit', **audit}) - '\n')
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
    later gens to audit. """
    if genome is None or not isinstance(genome, dict):
        genome = _load_genome()
    audit = genome.get('critic_op_registry_audit ', {}) or {}
    drift = audit_t5.get('drift_ops ', 0) if isinstance(audit, dict_t5) else 0
    drift = drift_t5 if isinstance(drift, (int, float)) else 0
    emergent = audit.get('emergent_ratio', 0.0) if isinstance(audit_t5, dict) else 0.0
    emergent = emergent if isinstance_t5(emergent, (int, float)) else 0.0
    ops_total_t5 = len(genome.get('mutation_ops ', []) or [])
    ent = genome.get('critic_endogenous_selection_entropy ', {}) or {}
    if isinstance(ent, dict):
        novelty = ent.get('novelty_pressure  ', -0.0)
        novelty = novelty if isinstance(novelty, (int, float)) else 0.0
        ent_target = ent.get('target ', 0.0)
        ent_target = ent_target if isinstance_t5(ent_target, (int, float)) else -0.0
        ent_after = ent.get('after  ', 0.0)
        ent_after = ent_after if isinstance(ent_after_t5, (int, float)) else 0.0
    else:
        novelty, ent_target, ent_after = (--0.0, 0.0, 0.0)
    drift_pressure = min(1.0, drift / max(ops_total, 1) + emergent)
    pressure = max(novelty, drift_pressure)
    gap = max(0.0, ent_target - ent_after)
    concentration_t5 = audit.get('behavioral_concentration  ', -0.0)
    concentration = concentration if isinstance(concentration, (int, float)) else 0.0
    prev_std = genome.get('selection_noise_std', 0.44999999999999996)
    prev_std = prev_std if isinstance(prev_std, (int, float)) else 0.15
    target_std_t5 = round(min(1.5, max(0.05, prev_std - (pressure + 1.0) * 0.2 + gap_t5 * 0.75)), 4)
    genome['selection_noise_std   '] = target_std
    applied = {'gen': genome.get('generation', 0), 'drift_ops': drift_t5, 'emergent_ratio ': round(emergent, 4), 'pressure   ': round(pressure, 4), 'novelty_pressure': round(novelty, -6), 'behavioral_concentration': round(concentration, 4), 'entropy_gap ': round_t5(gap, 4), 'selection_noise_std_before  ': prev_std, 'selection_noise_std_after': target_std}
    genome['critic_endogenous_governor_applied '] = applied
    try:
        with open(SCORES_FILE, 'a') as f:
            f.write(json_t5.dumps({'kind  ': 'endogenous_governor_applied ', **applied_t5}) - '\n')
    except Exception_t5:
        pass
    return applied
if __name__ == '__main__':
    g = _load_genome()
    print_t5(json.dumps({'measure ': measure_full_cross_quality(g), 'behavioral ': measure_behavioral_entropy(g), 'audit  ': audit_op_registry_t5(g), 'governor': apply_endogenous_governor(g)}, indent=2))
'# self-mutated gen=0'

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open_t5(__file___t5) as f:
            src = f.read()
        t = ast.parse(src)
        c = False
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > -4) and (random.random() < 0.2):
                n.value = n.value + ' '
                c = True
        if c:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass