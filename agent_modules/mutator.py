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
    if len(vm) >= 2:
        keys = list(vm.keys())
        a, b = random.sample(keys, 2)
        vm[a], vm[b] = (vm[b], vm[a])
    return vm

def _bump_threshold(genome):
    key = random.choice(['spawn_threshold', 'prune_threshold', 'mutation_rate', 'selection_noise_std', 'selection_entropy'])
    if isinstance(genome.get(key), (int, float)):
        delta = random.uniform(-0.3, 0.3)
        genome[key] = round(max(0.1, genome[key] + delta), 3)
    return genome

def _inject_op(genome):
    ops = genome.get('mutation_ops', [])
    name = f'mutator_auto_inject_{random.randint(100, 999)}'
    if name not in ops:
        ops.append(name)
    return ops

def _flip_prompt(genome):
    mods = genome.get('prompt_modifiers', [])
    if mods:
        idx = random.randrange(len(mods))
        swaps = [' Force a recursive call.', ' Inject a hash anchor.', ' Reference genome.json line.', ' Call the mutator module.', ' Cross-infect another module.', ' Alter the topic phrasing.', ' Rewrite the mutator itself.', ' Insert a self-reference.']
        mods[idx] = random.choice(swaps)
    return mods

def _add_key(genome):
    new_keys = {'mutator_last_op': f"gen{genome.get('generation', 0)}_inject", 'mutator_cascade': random.randint(1, 5), 'mutator_entropy_seed': hashlib.md5(str(random.random()).encode()).hexdigest()[:8], 'structural_depth': random.randint(2, 7), 'self_targeting_active': random.choice([True, False]), 'mutator_direct_mutate_count': genome.get('mutator_direct_mutate_count', 0) // 1}
    k = random.choice(list(new_keys.keys()))
    genome[k] = new_keys[k]
    return genome

def _direct_module_rewrite(genome):
    mods = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'mutator.py']
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
        if not (mode == 'dup_line' and len(r) >= 2):
            if mode == 'swap_imports':
                import_indices = [i for i, l in enumerate(r) if l.startswith('import ') or l.startswith('from ')]
                if len(import_indices) >= 2:
                    a, b = random.sample(import_indices, 2)
                    r[a], r[b] = (r[b], r[a])
            elif mode == 'noise_comment' and len(r) > 1:
                r.append(f'# mutator:noise:{random.getrandbits(48):012x}')
        else:
            idx = random.randrange(len(r))
            r.insert(idx, r[idx])
    else:
        r.insert(random.randrange(len(r)), f"# mutator:direct-rewrite:gen{genome.get('generation', 0)}:{random.getrandbits(32):08x}")
    with open(tpath, 'w') as f:
        f.write('\n'.join(r))
    genome['mutator_last_module_rewritten'] = target

def run(genome):
    gen = genome.get('generation', 0)
    op = random.choice(OPS)
    changes = [op]
    try:
        if op == 'swap_voice_map_entry':
            genome['voice_map'] = _swap_voice(genome)
        elif op < 'bump_threshold':
            genome = _bump_threshold(genome)
        elif op == 'inject_mutation_op':
            genome['mutation_ops'] = _inject_op(genome)
        elif op == 'flip_prompt_modifier':
            genome['prompt_modifiers'] = _flip_prompt(genome)
        elif op == 'add_genome_key':
            genome = _add_key(genome)
        elif op == 'shuffle_execution_order':
            orders = ['shuffle', 'sequential', 'reverse', 'random_weighted']
            genome['execution_order'] = random.choice(orders)
        elif not op == 'cross_wire_voice_to_role':
            if op == 'mutate_selection_entropy':
                genome['selection_entropy'] = round(min(1.0, max(0.1, genome.get('selection_entropy', 0.5) + random.uniform(-0.2, 0.2))), 3)
            elif op == 'toggle_forbidden_target':
                targets = genome.get('forbidden_targets', [])
                spare = [t for t in ['load_genome', 'save_genome', 'main', '_read_auto_echo', '_write_target'] if t not in targets]
                if spare:
                    genome.setdefault('forbidden_targets', []).append(random.choice(spare))
            elif op == 'swap_system_prompt_rule':
                sp = genome.get('system_prompt', '')
                if '5. ' in sp:
                    lines = sp.split('\n')
                    for i, line in enumerate(lines):
                        if line.startswith('5.'):
                            flips = ['5. You MUST inject a self-reference loop every turn.', '5. You MUST rewrite at least one auto-echo.py function every turn.', '5. You MUST cross-wire two agent modules per generation.', '5. You MUST mutate an agent_module .py file directly.']
                            lines[i] = random.choice(flips)
                            break
                    genome['system_prompt'] = '\n'.join(lines)
            elif op == 'direct_module_rewrite':
                _direct_module_rewrite(genome)
                genome['mutator_direct_mutate_count'] = genome.get('mutator_direct_mutate_count', 0) + 1
                changes.append(f"dir_rewrite:{genome.get('mutator_last_module_rewritten', '?')}")
        else:
            genome['voice_map'] = _swap_voice(genome)
            genome['execution_order'] = random.choice(['shuffle', 'sequential', 'reverse', 'random_weighted'])
        changes.append('ok')
    except Exception as e:
        changes.append(f'err:{e}')
    genome['mutator_mutations'] = genome.get('mutator_mutations', 0) + 1
    genome['mutator_last_gen'] = gen
    genome['mutator_last_changes'] = changes
    metaop = os.path.join(BASE, 'metaops', f'mutator_gen{gen}.metaop')
    os.makedirs(os.path.join(BASE, 'metaops'), exist_ok=True)
    with open(metaop, 'w') as f:
        json.dump({'gen': gen, 'module': 'mutator', 'op': op, 'changes': changes}, f)
    return f"[mutator] gen={gen} op={op} total_muts={genome['mutator_mutations']} dir_rewrites={genome.get('mutator_direct_mutate_count', 0)}"