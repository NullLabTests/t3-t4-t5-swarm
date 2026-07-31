"""identity_loop.py — Identity / Continuity loop for the t3-t4-t5 swarm.

Deliberately small, dependency-free, and immutable-by-location. This file
lives in identity/, which sits OUTSIDE the high-mutation boundary: the
swarm's AST mutators, string scramblers, and bridge handlers target
agent_modules/ and auto-echo.py, never identity/. It is the protected
substrate of the dual-loop architecture (see README "Gen 112+ Dual-Loop").

Responsibilities:
  - inject a continuity packet into the genome at every generation start
  - observe high-signal metrics after the critic phase
  - promote beliefs only through observe -> propose -> verify -> commit
  - decay / reconsolidate low-value self-model material
  - expose identity_health() for the watchdog
  - restore a minimal valid identity from template/ if corrupted/missing

Conceptual debt: continuity-kernel / living-memory research (e.g. mnemos,
engrams -> beliefs promotion, decay + reconsolidation). The implementation
is native and self-contained so the swarm's evolutionary lineage stays pure.
"""

import json
import os
import sys
import time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ID_DIR = os.path.join(BASE, 'identity')
CORE = os.path.join(ID_DIR, 'core.json')
SELF_MODEL = os.path.join(ID_DIR, 'self_model.json')
BELIEFS = os.path.join(ID_DIR, 'beliefs.jsonl')
HISTORY = os.path.join(ID_DIR, 'history.jsonl')
TEMPLATE_DIR = os.path.join(ID_DIR, 'template')

# Belief promotion gate: candidate must be observed this many consecutive
# generations before it may be promoted (observe -> verify -> commit).
PROMOTION_WINDOW = 3
# Self-model thermometer fields that may be written (whitelist; everything
# else in self_model.json is treated as protected structure).
THERMOMETER_FIELDS = ('behavioral_entropy', 'substance_score', 'crash_rate',
                      'self_repair_count', 'cross_contamination_count')


def _read_json(path, default=None):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def _write_json_atomic(path, obj):
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(obj, f, indent=2)
    os.replace(tmp, path)


def _append_line(path, obj):
    tmp = path + '.tmp'
    with open(path, 'a') as f:
        f.write(json.dumps(obj) + '\n')
    try:
        os.remove(tmp)
    except OSError:
        pass


def _log(event, **kwargs):
    entry = {'ts': time.time(), 'event': event}
    entry.update(kwargs)
    try:
        _append_line(HISTORY, entry)
    except OSError:
        pass


def identity_health():
    """Return (ok, issues). Callable by the watchdog without importing
    anything from the mutable swarm state."""
    issues = []
    for path, name in ((CORE, 'core'), (SELF_MODEL, 'self_model')):
        data = _read_json(path)
        if data is None:
            issues.append(f'{name} missing or unparseable')
        elif not isinstance(data, dict):
            issues.append(f'{name} not an object')
    for path, name in ((BELIEFS, 'beliefs'), (HISTORY, 'history')):
        if not os.path.exists(path):
            issues.append(f'{name} missing')
    return (not issues, issues)


def restore_from_template():
    """Recreate identity/ from the master-node committed template.
    Never pulls from mutable swarm state."""
    restored = []
    for fname in ('core.json', 'self_model.json', 'beliefs.jsonl', 'history.jsonl'):
        src = os.path.join(TEMPLATE_DIR, fname)
        dst = os.path.join(ID_DIR, fname)
        try:
            with open(src) as f:
                content = f.read()
            with open(dst, 'w') as f:
                f.write(content)
            restored.append(fname)
        except OSError:
            pass
    _log('identity_restored', files=restored, source='template')
    return restored


def ensure_identity():
    """Idempotent boot-time check: restore if missing/corrupt, then log."""
    ok, issues = identity_health()
    if not ok:
        restored = restore_from_template()
        _log('identity_restore_required', issues=issues, restored=restored)
        ok, issues = identity_health()
    return ok, issues


def inject_continuity_packet(genome, generation):
    """Called at generation start. Writes a compact continuity packet into
    the genome under a protected key so agents can read 'who we have been'."""
    self_model = _read_json(SELF_MODEL, {}) or {}
    thermo = self_model.get('self_thermometer', {}) or {}
    beliefs = []
    try:
        with open(BELIEFS) as f:
            for line in f:
                line = line.strip()
                if line:
                    b = json.loads(line)
                    if b.get('status') == 'active':
                        beliefs.append(b.get('belief', ''))
    except (OSError, ValueError):
        pass
    recent = []
    try:
        with open(HISTORY) as f:
            lines = f.readlines()
        for line in lines[-12:]:
            line = line.strip()
            if line:
                try:
                    recent.append(json.loads(line))
                except ValueError:
                    pass
    except OSError:
        pass
    packet = {
        'generation': generation,
        'self_name': self_model.get('self_name', 't3-t4-t5-swarm'),
        'thermometer': thermo,
        'active_beliefs': beliefs[-6:],
        'recent_events': recent,
    }
    genome['_identity_packet'] = packet
    _log('continuity_packet_injected', generation=generation,
         beliefs=len(beliefs), events=len(recent))
    return packet


def _read_history():
    rows = []
    try:
        with open(HISTORY) as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        rows.append(json.loads(line))
                    except ValueError:
                        pass
    except OSError:
        pass
    return rows


def _thermometer_from_genome(genome):
    """High-signal metrics the swarm already invented, surfaced onto the
    self-thermometer. Values only read, never invented here."""
    thermo = {}
    for key, field in (
        ('selection_entropy', 'behavioral_entropy'),
        ('substance_score', 'substance_score'),
    ):
        val = genome.get(key)
        if isinstance(val, (int, float)):
            thermo[field] = round(float(val), 6)
    crash_count = genome.get('crash_count')
    if isinstance(crash_count, (int, float)):
        thermo['crash_count'] = int(crash_count)
    return thermo


def observe(genome, generation):
    """Called after the critic phase. Measures, logs to history.jsonl,
    updates the thermometer, and runs the belief gate."""
    ok, _ = ensure_identity()
    if not ok:
        return False
    thermo = _thermometer_from_genome(genome)
    _log('measurement', generation=generation, **thermo)
    _update_self_model(genome, generation, thermo)
    _belief_gate(genome, generation)
    _decay_and_reconsolidate(generation)
    return True


def _update_self_model(genome, generation, thermo):
    self_model = _read_json(SELF_MODEL, {}) or {}
    if 'self_thermometer' not in self_model:
        self_model['self_thermometer'] = {}
    therm = self_model['self_thermometer']
    for field, value in thermo.items():
        if field in THERMOMETER_FIELDS:
            therm[field] = value
    therm['last_measured_gen'] = generation
    self_model['current_generation'] = generation
    self_model['updated_at'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    self_model['updated_by'] = 'identity_loop.observe'
    _write_json_atomic(SELF_MODEL, self_model)


def _belief_gate(genome, generation):
    """observe -> propose -> verify -> commit.

    Candidates are registered as observations. When the same candidate is
    observed for PROMOTION_WINDOW consecutive generations, it is committed
    as an active belief. Commit writes to beliefs.jsonl and is logged.
    """
    candidates = _candidate_beliefs(genome)
    cand_file = os.path.join(ID_DIR, 'candidates.json')
    cands = _read_json(cand_file, {}) or {}
    for cand in candidates:
        entry = cands.get(cand, {'gen': generation - 1, 'count': 0})
        if generation - entry.get('gen', 0) <= 1:
            entry['count'] = entry.get('count', 0) + 1
            entry['gen'] = generation
        else:
            entry = {'gen': generation, 'count': 1}
        cands[cand] = entry
        if entry['count'] >= PROMOTION_WINDOW:
            _commit_belief(cand, generation)
            cands[cand] = {'gen': generation, 'count': 0}
    _write_json_atomic(cand_file, cands)


def _candidate_beliefs(genome):
    """Propose beliefs from observable, repeatable patterns. Conservative:
    only structural facts, never performance hype."""
    out = []
    crash = genome.get('crash_count', 0)
    if isinstance(crash, int) and crash >= 0:
        out.append('crash_count_tracked')
    se = genome.get('selection_entropy')
    if isinstance(se, (int, float)):
        out.append('behavioral_entropy_measured')
    gen = genome.get('generation')
    if isinstance(gen, int):
        out.append('generation_advances')
    return out


def _commit_belief(belief, generation):
    existing = []
    try:
        with open(BELIEFS) as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        existing.append(json.loads(line))
                    except ValueError:
                        pass
    except OSError:
        pass
    for b in existing:
        if b.get('belief') == belief and b.get('status') == 'active':
            b['reinforced_gen'] = generation
            _write_beliefs(existing)
            _log('belief_reinforced', belief=belief, generation=generation)
            return
    existing.append({
        'belief': belief,
        'status': 'active',
        'promoted_gen': generation,
        'promotion_path': 'observe->propose->verify->commit',
        'window': PROMOTION_WINDOW,
    })
    _write_beliefs(existing)
    _log('belief_promoted', belief=belief, generation=generation)


def _write_beliefs(beliefs):
    tmp = BELIEFS + '.tmp'
    with open(tmp, 'w') as f:
        for b in beliefs:
            f.write(json.dumps(b) + '\n')
    os.replace(tmp, BELIEFS)


def _decay_and_reconsolidate(generation, decay_after=24):
    """Low-value identity material decays out of the active set; recently
    reinforced beliefs are reconsolidated (kept, re-logged)."""
    beliefs = []
    try:
        with open(BELIEFS) as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        beliefs.append(json.loads(line))
                    except ValueError:
                        pass
    except OSError:
        return
    changed = False
    for b in beliefs:
        if b.get('status') != 'active':
            continue
        promoted = b.get('promoted_gen', generation)
        if generation - promoted > decay_after:
            b['status'] = 'decayed'
            b['decayed_gen'] = generation
            changed = True
            _log('belief_decayed', belief=b.get('belief'), generation=generation)
    if changed:
        _write_beliefs(beliefs)
        _log('decay_pass', generation=generation, active=sum(
            1 for b in beliefs if b.get('status') == 'active'))


def main():
    """CLI: python3 identity/identity_loop.py check|restore|packet [gen]"""
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'check'
    if cmd == 'check':
        ok, issues = identity_health()
        print('identity_health:', 'OK' if ok else 'FAIL', issues)
        return 0 if ok else 1
    if cmd == 'restore':
        restored = restore_from_template()
        print('restored:', restored)
        return 0
    if cmd == 'packet':
        gen = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        genome = {}
        packet = inject_continuity_packet(genome, gen)
        print('packet_keys:', sorted(packet.keys()))
        return 0
    print('unknown cmd', cmd)
    return 2


if __name__ == '__main__':
    sys.exit(main())
