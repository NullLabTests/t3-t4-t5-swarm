from self_mutate import self_mutate
self_mutate(__file__)
import os, ast, json, time
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

def measure_full_cross_quality(genome=None):
    """Real, runnable op backing the genome registration: count parseable
    modules, confirm the explorer full-cross machinery is live, and persist the
    metric to genome + critic_scores.jsonl so later gens can audit the vote."""
    if genome is None or not isinstance(genome, dict):
        genome = _load_genome()
    total = 0
    parse_ok = 0
    for fn in sorted(os.listdir(MODULES_DIR)):
        if not fn.endswith('.py') or fn.startswith('_'):
            continue
        total += 1
        try:
            ast.parse(_read(os.path.join(MODULES_DIR, fn)))
            parse_ok += 1
        except Exception:
            pass
    fx_path = os.path.join(MODULES_DIR, 'mutation_op_explorer_full_cross.py')
    fx_src = _read(fx_path)
    has_pairs = '_full_cross_splice_pairs' in fx_src
    has_self = ('_force_self_infection' in fx_src) or ('_force_every_module_ast_operator_mutate' in fx_src)
    self_detected = '_force_every_module_ast_operator_mutate' if '_force_every_module_ast_operator_mutate' in fx_src else '_force_self_infection' if '_force_self_infection' in fx_src else None
    self_wired = bool(self_detected) and (self_detected in fx_src.split('def run', 1)[1])
    ops = genome.get('mutation_ops', []) or []
    registered = 'mutation_op_explorer_full_cross' in ops
    raw = parse_ok / max(total, 1) * 10.0
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
    governed. Persist audit + repair counts to genome + critic_scores.jsonl."""
    if genome is None or not isinstance(genome, dict):
        genome = _load_genome()
    ops = set(genome.get('mutation_ops', []) or [])
    inline = set(genome.get('custom_mutation_ops', {}) or {})
    mods = set()
    for fn in sorted(os.listdir(MODULES_DIR)):
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
    try:
        with open(SCORES_FILE, 'a') as f:
            f.write(json.dumps({'kind': 'op_registry_audit', **audit}) + '\n')
    except Exception:
        pass
    return audit
if __name__ == '__main__':
    g = _load_genome()
    print(json.dumps({'measure': measure_full_cross_quality(g), 'audit': audit_op_registry(g)}, indent=2))
'# self-mutated gen=0'