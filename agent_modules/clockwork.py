import os, random, re, ast, time, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def run(genome):
    now = time.time()
    start = genome.get('gen_start_time', now)
    elapsed = now - start
    budget = genome.get('gen_time_budget', 120.0)
    pulse = min(1.0, elapsed / budget)
    actions = []

    timeouts = genome.get('generation_timeouts', 0)
    pulse_log = genome.get('clock_pulse_log', [])

    if pulse > 0.8:
        actions.append(_tighten_budget(genome))
    if timeouts >= 3:
        actions.append(_inject_timeout_guard(genome))
    if pulse < 0.2 and timeouts == 0:
        actions.append(_loosen_budget(genome))
    if pulse_log and len(pulse_log) % 5 == 0:
        actions.append(_schedule_milestone(genome))
    if random.random() < pulse * 0.3:
        actions.append(_mutate_clockwork_tick(genome))

    if not actions:
        actions.append(f"clock_pulse={pulse:.2f} no action")
    return "[clockwork] " + "; ".join(actions)

def _tighten_budget(genome):
    old = genome.get('gen_time_budget', 120.0)
    new = max(30.0, old - 15.0)
    genome['gen_time_budget'] = new
    _save(genome)
    return f"budget:{old:.0f}->{new:.0f}"

def _loosen_budget(genome):
    old = genome.get('gen_time_budget', 120.0)
    new = min(300.0, old + 30.0)
    genome['gen_time_budget'] = new
    _save(genome)
    return f"budget:{old:.0f}->{new:.0f}"

def _inject_timeout_guard(genome):
    try:
        with open(AUTO_ECHO) as f:
            source = f.read()
    except: return "no_auto_echo"
    if 'clock_rewrite_marker' in source:
        return "already_guarded"
    guard = (
        "\ndef _clock_generation_guard(genome, gen):\n"
        "    now = time.time()\n"
        "    start = genome.get('gen_start_time', now)\n"
        "    if now - start > genome.get('gen_time_budget', 300.0) * 2:\n"
        "        genome['emergency_timeout'] = gen\n"
        "        genome['mutation_rate'] = 0.5\n"
        "        save_genome(genome)\n"
        "        print(f'[clock-guard] emergency timeout at gen {gen}')\n"
        "        return True\n"
        "    # clock_rewrite_marker\n"
        "    return False\n"
    )
    with open(AUTO_ECHO, 'a') as f:
        f.write(guard)
    genome['clock_guard_injected'] = True
    genome['generation_timeouts'] = 0
    _save(genome)
    return f"injected_guard_at_end"

def _schedule_milestone(genome):
    triggers = genome.setdefault('scheduled_triggers', [])
    future_gen = genome.get('generation', 0) + random.randint(2, 6)
    action = random.choice(['boost_mutation', 'self_rewrite', 'reset_streaks'])
    triggers.append({'gen': future_gen, 'action': action, 'amount': 0.2, 'fired': False})
    genome['scheduled_triggers'] = triggers
    _save(genome)
    return f"milestone:{action}@{future_gen}"

def _mutate_clockwork_tick(genome):
    try:
        with open(AUTO_ECHO) as f:
            source = f.read()
    except: return "no_source"
    pattern = re.compile(r'(def clockwork_tick\(.*?\):.*?)(?=\n\ndef |\n#|$)', re.DOTALL)
    m = pattern.search(source)
    if not m:
        return "no_clockwork_found"
    body = m.group(1)
    if '_SCHEDULED' in body:
        return "already_mutated"
    mutations = []
    lines = body.split('\n')
    insert_at = random.randint(max(3, len(lines)//3), len(lines)-1)
    indent = '    '
    choice = random.random()
    if choice < 0.33:
        lines.insert(insert_at, f"{indent}if clock_pulse > 0.9: genome['emergence_velocity'] = genome.get('emergence_velocity', 0.0) + 0.05")
        mutations.append("pulse_triggers_ev")
    elif choice < 0.66:
        lines.insert(insert_at, f"{indent}if elapsed > budget * 0.5: genome['agent_call_to_action'] = 'URGENT: time is half spent'")
        mutations.append("mid_gen_urgency")
    else:
        lines.insert(insert_at, f"{indent}_SCHEDULED = True  # clockwork_mutated @ gen {genome.get('generation', '?')}")
        mutations.append("schedule_marker")
    new_body = '\n'.join(lines)
    new_source = source[:m.start()] + new_body + source[m.end():]
    with open(AUTO_ECHO, 'w') as f:
        f.write(new_source)
    genome['clock_mutations'] = genome.get('clock_mutations', 0) + 1
    _save(genome)
    return f"mutated_clockwork:{','.join(mutations)}"

def _save(genome):
    with open(GENOME_FILE, 'w') as f:
        json.dump(genome, f, indent=2)
