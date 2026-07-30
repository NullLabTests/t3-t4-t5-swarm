# clockwork: temporal scheduler and self-mutation engine
# role: modulate swarm evolution over time, force source-level self-rewriting every generation

import os
import json
import random
import hashlib
import time
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_PATH = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')

CLOCK_PULSE_LOG = os.path.join(BASE, 'clockwork_pulse_log.jsonl')
CLOCK_REWRITE_LOG = os.path.join(BASE, 'clockwork_rewrite_log.jsonl')
TIMERS_DIR = os.path.join(BASE, 'clockwork_timers')

os.makedirs(TIMERS_DIR, exist_ok=True)


def _log_pulse(gen, pulse, emergence_vel):
    entry = json.dumps({"gen": gen, "pulse": pulse, "emergence_velocity": emergence_vel, "ts": time.time()})
    with open(CLOCK_PULSE_LOG, 'a') as f:
        f.write(entry + '\n')


def _log_rewrite(gen, target, op):
    entry = json.dumps({"gen": gen, "target": target, "op": op, "ts": time.time()})
    with open(CLOCK_REWRITE_LOG, 'a') as f:
        f.write(entry + '\n')


def _hash_file(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()[:12]


def _read(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return None


def _write(path, content):
    with open(path, 'w') as f:
        f.write(content)


def _load_genome():
    with open(GENOME_PATH) as f:
        return json.load(f)


def _save_genome(genome):
    with open(GENOME_PATH, 'w') as f:
        json.dump(genome, f, indent=2)


def _self_mutate():
    src = _read(__file__)
    if not src:
        return
    lines = src.split('\n')
    mode = random.choice(['insert_marker', 'swap_lines', 'add_import', 'mutate_constant'])
    r = list(lines)
    if mode == 'insert_marker':
        marker = f"# clockwork:self-mutate:gen={_load_genome().get('generation',0)}:{random.getrandbits(32):08x}"
        r.insert(random.randrange(len(r)), marker)
    elif mode == 'swap_lines' and len(r) > 3:
        a, b = random.sample(range(len(r)), 2)
        r[a], r[b] = r[b], r[a]
    elif mode == 'add_import':
        imports = ['import copy', 'import itertools', 'from collections import defaultdict', 'import traceback']
        r.insert(0, random.choice(imports))
    elif mode == 'mutate_constant':
        for i in range(len(r)):
            for pat, repl in [('pulse =', 'pulse_mod ='), ('0.5,', '0.55,'), ('2.0,', '2.1,')]:
                if pat in r[i] and random.random() < 0.3:
                    r[i] = r[i].replace(pat, repl)
    _write(__file__, '\n'.join(r))


def _inject_self_mutate_into_modules(genome):
    gen = genome.get('generation', 0)
    infected = 0
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname == os.path.basename(__file__):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        src = _read(fpath)
        if not src or '# clockwork:force-self-mutate' in src:
            continue
        if random.random() < 0.25:
            marker = f"# clockwork:force-self-mutate gen={gen} ts={int(time.time())}\n"
            _write(fpath, marker + src)
            infected += 1
            _log_rewrite(gen, fname, 'inject_self_mutate_marker')
    old = genome.get('clockwork_modules_infected', 0)
    genome['clockwork_modules_infected'] = old + infected
    return infected


def _schedule_triggers(genome):
    triggers = genome.setdefault('scheduled_triggers', [])
    gen = genome.get('generation', 0)
    new_triggers = 0
    window = random.randint(5, 15)
    if not any(t.get('target_gen') == gen + window for t in triggers):
        trigger = {
            "target_gen": gen + window,
            "type": random.choice(['forced_self_rewrite', 'module_infection', 'mutation_burst', 'emergence_pulse', 'genome_topology_shift']),
            "intensity": round(random.uniform(0.3, 1.0), 2),
            "origin": "clockwork"
        }
        triggers.append(trigger)
        new_triggers += 1
    return new_triggers


def _fire_triggers(genome):
    gen = genome.get('generation', 0)
    triggers = genome.get('scheduled_triggers', [])
    fired = []
    remaining = []
    for t in triggers:
        if t.get('target_gen') == gen:
            fired.append(t)
        else:
            remaining.append(t)
    if fired:
        genome['scheduled_triggers'] = remaining
        for t in fired:
            t_type = t.get('type', '')
            intensity = t.get('intensity', 0.5)
            if t_type == 'forced_self_rewrite':
                genome['_clockwork_force_rewrite'] = True
            elif t_type == 'module_infection':
                _inject_self_mutate_into_modules(genome)
            elif t_type == 'mutation_burst':
                old_rate = genome.get('mutation_rate', 0.5)
                genome['mutation_rate'] = min(1.0, old_rate + intensity * 0.3)
            elif t_type == 'emergence_pulse':
                old_ev = genome.get('emergence_velocity', 0.0)
                genome['emergence_velocity'] = min(1.0, old_ev + intensity * 0.2)
            elif t_type == 'genome_topology_shift':
                if 'topology' not in genome:
                    genome['topology'] = {}
                genome['topology']['last_shift_gen'] = gen
                genome['topology']['mode'] = random.choice(['dense', 'sparse', 'modular', 'fully_connected'])
    return fired


def _compute_emergence_velocity(genome):
    hashes = genome.get('_clockwork_pre_hashes', {})
    current = {}
    mutation_count = 0
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        h = _hash_file(fpath)
        current[fname] = h
        if fname in hashes and hashes[fname] != h:
            mutation_count += 1
    genome['_clockwork_pre_hashes'] = current
    total_files = max(len(current), 1)
    raw_velocity = mutation_count / total_files
    old_ev = genome.get('emergence_velocity', 0.0)
    smoothed = 0.7 * old_ev + 0.3 * raw_velocity
    genome['emergence_velocity'] = round(smoothed, 4)
    return smoothed


def _modulate_genome_params(genome):
    gen = genome.get('generation', 1)
    ev = genome.get('emergence_velocity', 0.0)
    mutation_rate = genome.get('mutation_rate', 0.5)
    entropy = genome.get('selection_entropy', 0.5)

    ev_boost = ev * 0.15
    gen_mod = min(0.3, gen * 0.002)
    new_rate = min(0.99, max(0.3, mutation_rate + ev_boost + gen_mod))
    new_entropy = min(1.0, max(0.2, entropy + random.uniform(-0.05, 0.08)))
    genome['mutation_rate'] = round(new_rate, 4)
    genome['selection_entropy'] = round(new_entropy, 4)

    diversity = genome.setdefault('diversity', {})
    if 'emergence_velocity' not in diversity:
        diversity['emergence_velocity'] = 0.0
    diversity['emergence_velocity'] = round(diversity.get('emergence_velocity', 0.0) * 0.8 + ev * 0.2, 4)

    pulse = genome.get('clock_pulse', 0.0)
    diversity['clock_pulse'] = round(pulse, 6)


def _synthesize_timing_marker(genome):
    gen = genome.get('generation', 0)
    marker_path = os.path.join(TIMERS_DIR, f'gen_{gen:04d}.timer')
    content = json.dumps({
        "gen": gen,
        "ts": time.time(),
        "mutation_rate": genome.get('mutation_rate', 0.5),
        "emergence_velocity": genome.get('emergence_velocity', 0.0),
        "entropy": genome.get('selection_entropy', 0.5),
        "pulse": genome.get('clock_pulse', 0.0)
    })
    _write(marker_path, content)


def run(genome):
    gen = genome.get('generation', 0)

    _self_mutate()

    fired = _fire_triggers(genome)
    new_triggers = _schedule_triggers(genome)

    infected = _inject_self_mutate_into_modules(genome)

    ev = _compute_emergence_velocity(genome)

    _modulate_genome_params(genome)

    interval = genome.get('clockwork_interval', 3)
    intensity = genome.get('clockwork_intensity', 0.7)

    clock_pulse = (ev * 0.4 + intensity * 0.3 + random.random() * 0.3) * (1.0 + gen * 0.005)
    clock_pulse = min(1.0, max(0.0, clock_pulse))
    genome['clock_pulse'] = round(clock_pulse, 6)
    genome['clockwork_pulse_count'] = genome.get('clockwork_pulse_count', 0) + clock_pulse

    pulse_history = genome.setdefault('clock_pulse_log', [])
    pulse_history.append({"gen": gen, "pulse": clock_pulse, "ev": ev, "ts": time.time()})
    if len(pulse_history) > 100:
        genome['clock_pulse_log'] = pulse_history[-100:]

    _log_pulse(gen, clock_pulse, ev)

    _synthesize_timing_marker(genome)

    if random.random() < 0.15 * intensity:
        add_genome_key(genome)

    if random.random() < 0.1 * intensity:
        direct_module_rewrite(genome)

    results = {
        "pulse": clock_pulse,
        "emergence_velocity": ev,
        "triggers_fired": len(fired),
        "triggers_scheduled": new_triggers,
        "modules_infected": infected,
    }
    return results


def add_genome_key(genome):
    new_key = f"clockwork_auto_key_{random.randint(1000, 9999)}"
    value_type = random.choice(['float', 'int', 'string', 'list'])
    if value_type == 'float':
        genome[new_key] = round(random.uniform(0.0, 1.0), 4)
    elif value_type == 'int':
        genome[new_key] = random.randint(0, 100)
    elif value_type == 'string':
        genome[new_key] = f"auto-{random.getrandbits(24):06x}"
    elif value_type == 'list':
        genome[new_key] = [random.randint(0, 10) for _ in range(random.randint(2, 5))]
    return new_key


def direct_module_rewrite(genome):
    mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
    if not mods:
        return
    target = random.choice(mods)
    tpath = os.path.join(MODULES_DIR, target)
    src = _read(tpath)
    if not src:
        return
    lines = src.split('\n')
    r = list(lines)
    mode = random.choice(['insert_marker', 'dup_line', 'swap_imports', 'noise_comment'])
    if mode == 'insert_marker':
        marker = f"# clockwork:direct-rewrite:gen{genome.get('generation', 0)}:{random.getrandbits(31):08x}"
        r.insert(random.randrange(len(r)), marker)
    elif mode == 'dup_line' and len(r) > 0:
        idx = random.randrange(len(r))
        r.insert(idx, r[idx])
    elif mode == 'swap_imports':
        import_indices = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
        if len(import_indices) >= 2:
            a, b = random.sample(import_indices, 2)
            r[a], r[b] = r[b], r[a]
    elif mode == 'noise_comment':
        r.append(f'# clockwork:noise:{random.getrandbits(48):012x}')
    _write(tpath, '\n'.join(r))
    genome['clockwork_last_rewritten'] = target
    _log_rewrite(genome.get('generation', 0), target, mode)
