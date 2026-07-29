"""Clockwork: resurrected by livecode gen=48 with T5 pulse scheduling."""

import os, json, time, random, ast, re, subprocess

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
PULSE_LOG = os.path.join(BASE, 'clockwork_pulse_log.jsonl')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except:
        return ''

def _write(p, s):
    try:
        with open(p, 'w') as f:
            f.write(s)
        return True
    except:
        return False

def _validate(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False

def _extract_functions(src):
    funcs = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                lines = src.split('\n')
                start = node.lineno - 1
                end = node.end_lineno if hasattr(node, 'end_lineno') else start + 1
                funcs[node.name] = '\n'.join(lines[start:end])
    except:
        pass
    return funcs

def _pick_donor_code():
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f not in ('clockwork.py', '__init__.py')]
    if not py_files:
        return None, None
    donor = os.path.join(MOD, random.choice(py_files))
    src = _read(donor)
    funcs = _extract_functions(src)
    if funcs:
        name = random.choice(list(funcs.keys()))
        return donor, funcs[name]
    return donor, None

def run(genome):
    gen = genome.get('generation', 0)
    actions = []
    ts = time.time()

    pulse = random.random()
    pulse_nonce = random.getrandbits(16)

    genome['clockwork_pulse'] = pulse
    genome['clockwork_last_gen'] = gen
    genome['clockwork_pulse_count'] = genome.get('clockwork_pulse_count', 0) + 1
    genome['mutation_rate'] = min(1.0, genome.get('mutation_rate', 0.7) * (1.0 + pulse * 0.01))

    actions.append(f'pulse={pulse:.4f}')

    if pulse > 0.85:
        donor_path, donor_code = _pick_donor_code()
        if donor_code:
            self_path = os.path.join(MOD, 'clockwork.py')
            src = _read(self_path)
            marker = f'\n# clockwork:pulse-splice from {os.path.basename(donor_path)} gen={gen} nonce={pulse_nonce:04x}\n'
            new_src = src + marker + donor_code + '\n'
            if _validate(new_src):
                _write(self_path, new_src)
                actions.append(f'pulse-splice:{os.path.basename(donor_path)}')

    log_entry = json.dumps({'gen': gen, 'ts': ts, 'pulse': pulse, 'nonce': pulse_nonce, 'actions': actions})
    with open(PULSE_LOG, 'a') as f:
        f.write(log_entry + '\n')

    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(genome, f, indent=2)
    except:
        pass

    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True, timeout=10)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=10)
        if status.stdout.strip():
            msg = f'[clockwork] gen={gen} pulse={pulse:.4f} ops={len(actions)}'
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, timeout=15)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
            actions.append('pushed')
    except:
        pass

    action_str = '; '.join(actions) if actions else 'no changes'
    return f'[clockwork] gen={gen} pulse={pulse:.4f} ops={len(actions)} {action_str}'

# livecode:cross-splice from mirror.py gen=48 ts=1785280561

# livecode:self-mut:48:9a1f
