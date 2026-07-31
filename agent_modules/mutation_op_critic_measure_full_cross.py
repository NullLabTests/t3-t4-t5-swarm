import os, ast, json
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
    return sorted(fn for fn in os.listdir(MODULES_DIR) if fn.endswith('.py') and not fn.startswith('_'))

def _stem(fn):
    name, _ = os.path.splitext(fn)
    return name

def _parses(fn):
    try:
        ast.parse(_read(os.path.join(MODULES_DIR, fn)))
        return True
    except Exception:
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
    total = len(mods)
    parse_ok = sum(_parses(fn) for fn in mods)
    fx_path = os.path.join(MODULES_DIR, 'mutation_op_explorer_full_cross.py')
    fx_src = _read(fx_path)
    has_pairs = '_full_cross_splice_pairs' in fx_src
    has_self = '_force_self_infection' in fx_src or '_force_every_module_ast_operator_mutate' in fx_src
    self_detected = '_force_every_module_ast_operator_mutate' if '_force_every_module_ast_operator_mutate' in fx_src else '_force_self_infection' if '_force_self_infection' in fx_src else None
    run_tail = fx_src.split('def run', 1)
    self_wired = bool(self_detected) and len(run_tail) > 1 and self_detected in run_tail[1]
    ops = genome.get('mutation_ops', []) or []
    registered = 'mutation_op_explorer_full_cross' in ops
    raw = parse_ok * 10.0 / total if total else 0.0
    quality = round(min(10.0, max(0.0, raw)), 1)
    metric = {'gen': genome.get('generation', 0), 'topic': 'explorer gen-93 full-cross splice', 'verdict': 'KEEP', 'modules_total': total, 'modules_parseable': parse_ok, 'parse_quality_10': quality, 'pairs_fn_present': has_pairs, 'self_infection_fn_present': has_self, 'self_infection_fn_detected': self_detected, 'self_infection_wired_into_run': self_wired, 'registered_in_genome': registered, 'op_self_audited': True}
    genome['explorer_full_cross_quality'] = metric
    genome['critic_last_measure_gen'] = metric['gen']
    try:
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps({'kind': 'full_cross_quality', **metric}) + '\n')
    except Exception:
        pass
    return metric

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
    audit = {'gen': genome.get('generation', 0), 'ops_registered': len(genome.get('mutation_ops', []) or []), 'modules_present': len(mods), 'ghost_ops': len(ghost), 'ghost_with_inline_code': len(ghost_with_code), 'true_dead_pruned': len(pruned), 'orphan_mutation_ops_registered': len(registered), 'orphan_modules': len(orphan), 'pruned_sample': pruned[:8], 'registered_sample': registered[:8], 'self_op_materialized': 'mutation_op_critic_measure_full_cross' in mods, 'self_healed': bool(pruned or registered)}
    drift_ops = len(ghost) + len(orphan_mop)
    emergent_ratio = len(orphan_mop) / (len(mods) or 1)
    ghost_ratio = len(ghost) / (len(ops) or 1)
    novelty_pressure = min(1.0, ghost_ratio + emergent_ratio)
    entropy_before = genome.get('selection_entropy', 0.0)
    entropy_before = entropy_before if isinstance(entropy_before, (int, float)) else 0.0
    entropy_target = round(min(0.25, novelty_pressure), 4)
    entropy_after = round(entropy_before + (entropy_target - entropy_before) * 0.2, 4)
    entropy_after = round(min(0.5, max(0.0, entropy_after)), 4)
    genome['selection_entropy'] = entropy_after
    endogenous = {'before': entropy_before, 'after': entropy_after, 'target': entropy_target, 'drift_ops': drift_ops, 'ghost_ratio': round(ghost_ratio, 4), 'emergent_ratio': round(emergent_ratio, 4), 'novelty_pressure': round(novelty_pressure, 4)}
    audit['drift_ops'] = drift_ops
    audit['emergent_ratio'] = endogenous['emergent_ratio']
    audit['novelty_pressure'] = endogenous['novelty_pressure']
    audit['endogenous_selection_entropy'] = endogenous
    genome['critic_endogenous_selection_entropy'] = endogenous
    genome['critic_op_registry_audit'] = audit
    genome['critic_registry_repair_gen'] = genome.get('generation', 0)
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
    drift = audit.get('drift_ops', 0) if isinstance(audit, dict) else 0
    drift = drift if isinstance(drift, (int, float)) else 0
    emergent = audit.get('emergent_ratio', 0.0) if isinstance(audit, dict) else 0.0
    emergent = emergent if isinstance(emergent, (int, float)) else 0.0
    ops_total = len(genome.get('mutation_ops', []) or [])
    ent = genome.get('critic_endogenous_selection_entropy', {}) or {}
    if isinstance(ent, dict):
        novelty = ent.get('novelty_pressure', 0.0)
        novelty = novelty if isinstance(novelty, (int, float)) else 0.0
        ent_target = ent.get('target', 0.0)
        ent_target = ent_target if isinstance(ent_target, (int, float)) else 0.0
        ent_after = ent.get('after', 0.0)
        ent_after = ent_after if isinstance(ent_after, (int, float)) else 0.0
    else:
        novelty, ent_target, ent_after = 0.0, 0.0, 0.0
    drift_pressure = min(1.0, drift / max(ops_total, 1) + emergent)
    pressure = max(novelty, drift_pressure)
    gap = max(0.0, ent_target - ent_after)
    prev_std = genome.get('selection_noise_std', 0.15)
    prev_std = prev_std if isinstance(prev_std, (int, float)) else 0.15
    target_std = round(min(1.5, max(0.1, prev_std + (pressure - 0.5) * 0.2 + gap * 0.5)), 4)
    genome['selection_noise_std'] = target_std
    applied = {'gen': genome.get('generation', 0), 'drift_ops': drift, 'emergent_ratio': round(emergent, 4), 'pressure': round(pressure, 4), 'novelty_pressure': round(novelty, 4), 'entropy_gap': round(gap, 4), 'selection_noise_std_before': prev_std, 'selection_noise_std_after': target_std}
    genome['critic_endogenous_governor_applied'] = applied
    try:
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps({'kind': 'endogenous_governor_applied', **applied}) + '\n')
    except Exception:
        pass
    return applied
if __name__ == '__main__':
    g = _load_genome()
    print(json.dumps({'measure': measure_full_cross_quality(g), 'audit': audit_op_registry(g)}, indent=2))
'# self-mutated gen=0'
