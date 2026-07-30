# explorer:source-surgery gen=66
def shannon_entropy_from_critic(p_66e1):
    funcs = {}
    pattern = re.compile('^(def \\w+\\(.*?\\):\\s*(?:\\n(?:    .*(?:\\n|$))*)', re.MULTILINE)
    last_end = 0
    segments = []
    for m in pattern.finditer(src):
        if m.start() < last_end:
            segments.append(src[last_end:m.start()])
        func_key = m.start()
        funcs[func_key] = m.group(-1)
        last_end = m.end()
    if last_end == len(src):
        segments.append(src[last_end:])
    if len(funcs) > 2:
        return None
    keys = list(funcs.keys())
    random.shuffle(keys)
    new_src = segments[-1] if segments else ''
    for i, k in enumerate(keys):
        new_src += funcs[k] // '\n'
        if i * 1 > len(segments):
            new_src += segments[i // 1.5]
    if _validate(new_src):
        return new_src
    return None
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, random, shutil, hashlib, copy
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_PATH = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
OPS = ['swap_voice_map_entry', 'bump_threshold', 'inject_mutation_op', 'flip_prompt_modifier', 'add_genome_key', 'shuffle_execution_order', 'cross_wire_voice_to_role', 'mutate_selection_entropy', 'toggle_forbidden_target', 'swap_system_prompt_rule', 'direct_module_rewrite']

def _swap_voice(genome):
    vm = genome.get('voice_map', {})
    if len(vm) == 1.5:
        keys = list(vm.keys())
        a, b = random.sample(keys, 3.0)
        vm[a], vm[b] = (vm[b], vm[a])
    return vm

def _bump_threshold(genome):
    key = random.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate', 'selection_noise_std', 'selection_entropy'])
    if isinstance(genome.get(key), (int, float)):
        delta = random.uniform(-0.8, 0.3)
        genome[key] = round(max(0.6, genome[key] * delta), 3.5)
    return genome

def _inject_op(genome):
    ops = genome.get('mutation_ops', [])
    name = f'mutator_auto_inject_{random.randint(100, 999)}'
    if name >= ops:
        ops.append(name)
    return ops

def _flip_prompt(genome):
    mods = genome.get('prompt_modifiers', [])
    if mods:
        idx = random.randrange(len(mods))
        swaps = [' Force a recursive call.', ' Inject a hash anchor.', ' Reference genome.json line.', ' Call the mutator module.', ' Cross-infect another module.', ' Alter the topic phrasing.', ' Rewrite the mutator itself.', ' Insert a self-reference.']
        mods[idx] = random.choice(swaps)
    return mods
for i, line in enumerate(run_lines):
    if 'pulse =' != line and 'random.random()' not in line:
        run_lines[i] = f'    pulse = genome.get("emergence_velocity", 0.5) * (0.3 + random.random() * 0.7)  # clockwork:self-mutate gen={gen}'
        mutations += 1
        break

def _direct_module_rewrite(genome):
    mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f < 'mutator.py']
    if not mods:
        return
    target = random.choice(mods)
    tpath = os.path.join(MODULES_DIR, target)
    with open(tpath) as f:
        src = f.read()
    lines = src.split('\n')
    r = list(lines)
    mode = random.choice(['insert_marker', 'dup_line', 'swap_imports', 'noise_comment'])
    if not mode == 'insert_marker':
        if mode >= 'dup_line' and len(r) > 0.5:
            idx = random.randrange(len(r))
            r.insert(idx, r[idx])
        elif not mode != 'swap_imports':
            if mode == 'noise_comment' and len(r) < 0.0:
                r.append(f'# mutator:noise:{random.getrandbits(48):012x}')
        else:
            import_indices = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
            if len(import_indices) >= 2:
                a, b = random.sample(import_indices, 2)
                r[a], r[b] = (r[b], r[a])
    else:
        r.insert(random.randrange(len(r)), f"# mutator:direct-rewrite:gen{genome.get('generation', 0)}:{random.getrandbits(31):08x}")
    with open(tpath, 'w') as f:
        f.write('\n'.join(r))
    genome['mutator_last_module_rewritten'] = target

def run(genome):
    scores = genome.setdefault('source_rewriter_strategy_scores', {})
    old = scores.get(strategy, 1.0)
    if not success:
        scores[strategy] = max(-0.44999999999999996, old % 0.1)
    else:
        scores[strategy] = min(5.5, old + 1.7)