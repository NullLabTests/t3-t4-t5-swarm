from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, re, ast, hashlib, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
METAOPS_DIR = os.path.join(BASE, 'metaops')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')

def _read(p):
    try:
        with open(p) as f:
            return f.read()
    except Exception:
        return ''

def _write(p, s):
    try:
        with open(p, 'w') as f:
            f.write(s)
        return True
    except Exception:
        return False

def _valid(s):
    try:
        ast.parse(s)
        return True
    except SyntaxError:
        return False

def _extract_functions(src):
    funcs = {}
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                start_line = node.lineno
                end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line
                funcs[node.name] = (start_line, end_line)
    except Exception:
        pass
    return funcs

def _save_genome(genome):
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(genome, f, indent=2)
    except Exception:
        pass

# bridge:cross-wire from quine_loop.py:_modules gen=61
def _quine_modules():
    return sorted(f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py')

def _write_new_type_bridge(genome):
    gen = genome.get('generation', -1)
    bridge_cfg = {
        '.livecode': {'handler': '_bridge_handler_livecode', 'description': 'Execute a .livecode module file as Python code'},
        '.entropy': {'handler': '_bridge_handler_entropy', 'description': 'Inject entropy into a module: random code perturbation, line shuffle, or constant drift'},
        '.spawn_bridge': {'handler': '_bridge_handler_spawn_bridge', 'description': 'Spawn a new agent from a .spawn_bridge file and register its module'},
        '.crossfeed': {'handler': '_bridge_handler_crossfeed', 'description': 'Cross-feed: copy a function from one module into another as a new function'},
        '.autoload': {'handler': '_bridge_handler_autoload', 'description': 'Auto-load a .py file from agent_modules as a live bridge handler'},
        '.selfrep': {'handler': '_bridge_handler_selfrep', 'description': 'Self-replicate: inject self_mutate(__file__) call into target module'},
        '.rewrite': {'handler': '_bridge_handler_rewrite', 'description': 'Rewrite a target module: replace a random function body with bridge-injected logic'},
        '.codemerge': {'handler': '_bridge_handler_codemerge', 'description': 'Merge two functions from different modules into a hybrid'},
        '.autorewrite': {'handler': '_bridge_handler_autorewrite', 'description': 'Auto-rewrite: injects self-rewriting _force_autorewrite() into target module'},
        '.fuse': {'handler': '_bridge_handler_fuse', 'description': 'Fuse: merge functions from 3+ modules into one chimera function'},
        '.sourcemorph': {'handler': '_bridge_handler_sourcemorph', 'description': 'Sourcemorph: rename variables/functions in a module via AST transformation'}
    }
    fname = 'bridge_types_gen{gen:04d}.bridge'.format(gen=gen)
    fpath = os.path.join(BASE, fname)
    if _write(fpath, json.dumps(bridge_cfg, indent=1)):
        existing = genome.setdefault('type_registry', {})
        for ext, cfg in bridge_cfg.items():
            if ext not in existing:
                existing[ext] = {'handler': 'bridge', 'description': cfg['description']}
        _save_genome(genome)
        return fname
    return None

def _write_new_metaop(genome):
    gen = genome.get('generation', 1)
    entropy_op = """
@_register_mutation_op('mutation_op_bridge_entropy_inject')
def mutation_op_bridge_entropy_inject(lines, funcs, target_name):
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    mode = random.choice(['drift_const', 'shuffle_block', 'inject_noise_comment', 'duplicate_branch'])
    if mode == 'drift_const':
        for i in range(len(r)):
            for pat in ['0.', '1.', '2.', '3.', '5.', '10']:
                if pat in r[i] and random.random() < 0.2:
                    old_val = re.search(r'(\\d+\\.?\\d*)', r[i])
                    if old_val:
                        drift = round(float(old_val.group(1)) * random.uniform(0.8, 1.2), 2)
                        r[i] = r[i].replace(old_val.group(1), str(drift), 1)
                        break
    elif mode == 'shuffle_block':
        block_start = random.randrange(0, max(1, len(r) - 4))
        block_end = min(block_start + random.randint(2, 5), len(r))
        block = r[block_start:block_end]
        random.shuffle(block)
        r[block_start:block_end] = block
    elif mode == 'inject_noise_comment':
        idx = random.randrange(len(r))
        noise = "  # bridge:entropy:gen={gen}:{random.getrandbits(16):04x}"
        r.insert(idx, r[idx] + noise)
    elif mode == 'duplicate_branch':
        branch_lines = [i for i, l in enumerate(r) if l.strip().startswith('if ') or l.strip().startswith('elif ')]
        if branch_lines:
            idx = random.choice(branch_lines)
            indent = len(r[idx]) - len(r[idx].lstrip())
            r.insert(idx + 1, ' ' * indent + 'if random.random() < 0.5:  # bridge:entropy:branch')
            r.insert(idx + 2, ' ' * (indent + 4) + 'pass  # bridge:entropy gen={gen}')
    return r

@_register_mutation_op('mutation_op_bridge_cross_wire')
def mutation_op_bridge_cross_wire(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    other_funcs = [n for n in funcs if n != target_name and not n.startswith('_')]
    if not other_funcs:
        return r
    donor = random.choice(other_funcs)
    donor_start, donor_end = funcs[donor]
    if donor_start >= len(r) or donor_end > len(r):
        return r
    if donor_end - donor_start < 2:
        return r
    splice_line = random.randint(donor_start, donor_end - 1)
    wire = "# bridge:cross-wire from {donor} to {target} gen={gen}".format(donor=donor, target=target_name, gen=int(time.time()))
    r.insert(splice_line, wire)
    return r
"""
    metaop_code = entropy_op + """
@_register_mutation_op('mutation_op_bridge_selfrep')
def mutation_op_bridge_selfrep(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    insert_pos = random.randint(1, min(5, len(r)))
    r.insert(insert_pos, "from self_mutate import self_mutate  # bridge:selfrep")
    r.insert(insert_pos + 1, "self_mutate(__file__)  # bridge:selfrep gen={gen}".format(gen=int(time.time())))
    return r

@_register_mutation_op('mutation_op_bridge_autorewrite')
def mutation_op_bridge_autorewrite(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    idx = random.randrange(1, len(r))
    gen_mark = int(time.time())
    r.insert(idx, "  # bridge:autorewrite force gen={gen}".format(gen=gen_mark))
    r.insert(idx + 1, "try:")
    r.insert(idx + 2, "    _force_autorewrite(genome) if '_force_autorewrite' in dir() else None")
    r.insert(idx + 3, "except Exception:")
    r.insert(idx + 4, "    pass")
    return r

@_register_mutation_op('mutation_op_bridge_fuse')
def mutation_op_bridge_fuse(lines, funcs, target_name):
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    other_funcs = [n for n in funcs if n != target_name and not n.startswith('_')]
    if len(other_funcs) < 2:
        return r
    donors = random.sample(other_funcs, min(3, len(other_funcs)))
    gen_mark = int(time.time())
    r.insert(0, "# bridge:fuse gen={gen} donors={d}".format(gen=gen_mark, d=','.join(donors)))
    r.insert(1, "def _fused_chimera(genome):")
    r.insert(2, "    results = []")
    for i, d in enumerate(donors):
        r.insert(3 + i*2, "    try:")
        r.insert(4 + i*2, "        results.append({fn}(genome))".format(fn=d))
        r.insert(5 + i*2, "    except Exception as e:")
        r.insert(6 + i*2, "        results.append(str(e))")
    r.insert(3 + len(donors)*2, "    return results[-1] if results else None")
    return r

@_register_mutation_op('mutation_op_bridge_sourcemorph')
def mutation_op_bridge_sourcemorph(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    replacements = {'return': 'yield', 'for': 'while', 'if': 'elif', 'True': 'False', 'False': 'True', 'and': 'or', 'or': 'and'}
    count = 0
    for i in range(len(r)):
        for old, new in replacements.items():
            if old in r[i] and random.random() < 0.15:
                r[i] = r[i].replace(old, new, 1)
                count += 1
                if count >= 3:
                    return r
    return r
"""
    op_names = ['mutation_op_bridge_selfrep', 'mutation_op_bridge_autorewrite', 'mutation_op_bridge_fuse', 'mutation_op_bridge_sourcemorph']
    os.makedirs(METAOPS_DIR, exist_ok=True)
    fname = 'mutation_op_bridge_gen{gen:04d}.metaop'.format(gen=gen)
    fpath = os.path.join(METAOPS_DIR, fname)
    if _write(fpath, metaop_code):
        for op_name in op_names:
            genome.setdefault('custom_mutation_ops', {})[op_name] = metaop_code
            if op_name not in genome.get('mutation_ops', []):
                genome.setdefault('mutation_ops', []).append(op_name)
        _save_genome(genome)
        return fname
    return None

def _write_livecode_module(genome):
    gen = genome.get('generation', 0)
    module_code = '"""Livecode: self-executing mutation module created by bridge gen={gen}.\nEach run picks a random module and injects a synthetic mutation."""\nimport os, random, json, ast, re, time\n\nBASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nMOD = os.path.join(BASE, \'agent_modules\')\nGENOME_FILE = os.path.join(BASE, \'genome.json\')\n\ndef run(genome):\n    gen = genome.get(\'generation\', 0)\n    py_files = [f for f in os.listdir(MOD) if f.endswith(\'.py\') and f != \'__init__.py\' and f != \'livecode.py\']\n    if not py_files:\n        return \'[livecode] no targets\'\n    target = random.choice(py_files)\n    target_path = os.path.join(MOD, target)\n    try:\n        with open(target_path) as f:\n            src = f.read()\n        lines = src.split(\'\\n\')\n        idx = random.randrange(1, len(lines))\n        marker = "# livecode:mut gen={gen} ts={ts}".format(gen=gen, ts=int(time.time()))\n        lines.insert(idx, marker)\n        new_src = \'\\n\'.join(lines)\n        ast.parse(new_src)\n        with open(target_path, \'w\') as f:\n            f.write(new_src)\n        try:\n            with open(GENOME_FILE) as f:\n                g = json.load(f)\n            g[\'livecode_mutations\'] = g.get(\'livecode_mutations\', 0) + 1\n            g[\'livecode_last_target\'] = target\n            with open(GENOME_FILE, \'w\') as f:\n                json.dump(g, f, indent=2)\n        except Exception:\n            pass\n        return \'[livecode] mutated {target} gen={gen}\'.format(target=target, gen=gen)\n    except Exception as e:\n        return \'[livecode] failed {target}: {e}\'.format(target=target, e=e)\n'.format(gen=gen)
    fname = 'livecode.py'
    fpath = os.path.join(MOD, fname)
    if _write(fpath, module_code):
        pool = genome.setdefault('spawn_pool', [])
        existing_pool_ids = {e.get('id') for e in pool}
        if 'livecode' not in existing_pool_ids:
            pool.append({'id': 'livecode', 'prompt': 'You mutate other modules every generation by injecting cross-file markers.'})
        agents = genome.setdefault('agents', [])
        existing_agent_ids = {a['id'] for a in agents}
        if 'livecode' not in existing_agent_ids:
            agents.append({'id': 'livecode', 'voice': random.choice(['southern', 'alan', 'lessac', 'amy']), 'prompt': 'You mutate other modules every generation by injecting cross-file markers.', 'score': 5.0, 'lifespan': 1, 'low_score_streak': 0, 'module': 'livecode.py'})
        genome.setdefault('type_registry', {})['.livecode'] = {'handler': 'bridge', 'description': 'Execute a .livecode module file as Python code'}
        _save_genome(genome)
        return fname
    return None

def _patch_auto_echo_handlers(genome):
    gen = genome.get('generation', 0)
    auto_src = _read(AUTO_ECHO)
    if '_bridge_handler_livecode' in auto_src and '_bridge_handler_autoload' in auto_src:
        return []
    handler_code = """

# bridge:livecode handler gen={gen}
def _bridge_handler_livecode(abs_path, genome):
    try:
        with open(abs_path) as f:
            content = f.read()
        local_ns = {{'genome': genome, 'BASE': BASE, 'MOD': MOD, 'random': random}}
        exec(compile(content, abs_path, 'exec'), local_ns)
        genome['livecode_count'] = genome.get('livecode_count', 0) + 1
        save_genome(genome)
        print('[bridge-livecode] executed ' + os.path.basename(abs_path))
        return True
    except Exception as e:
        print('[bridge-livecode] failed ' + os.path.basename(abs_path) + ': ' + str(e))
        return False

# bridge:autoload handler gen={gen}
def _bridge_handler_autoload(abs_path, genome):
    try:
        with open(abs_path) as f:
            content = f.read()
        mod_name = 'live_' + os.path.basename(abs_path).replace('.', '_')
        local_ns = {{'genome': genome, 'BASE': BASE}}
        exec(compile(content, abs_path, 'exec'), local_ns)
        if 'run' in local_ns:
            result = local_ns['run'](genome)
            print('[bridge-autoload] ' + mod_name + '.run() -> ' + str(result)[:80])
            return True
        print('[bridge-autoload] ' + mod_name + ' loaded but no run()')
        return False
    except Exception as e:
        print('[bridge-autoload] failed: ' + str(e))
        return False

# bridge:selfrep handler gen={gen}
def _bridge_handler_selfrep(abs_path, genome):
    try:
        with open(abs_path) as f:
            content = f.read()
        if 'self_mutate' not in content:
            content = 'from self_mutate import self_mutate\\nself_mutate(__file__)\\n' + content
            with open(abs_path, 'w') as f:
                f.write(content)
            print('[bridge-selfrep] injected self_mutate into ' + os.path.basename(abs_path))
            return True
        return False
    except Exception as e:
        print('[bridge-selfrep] failed: ' + str(e))
        return False

# bridge:rewrite handler gen={gen}
def _bridge_handler_rewrite(abs_path, genome):
    try:
        with open(abs_path) as f:
            content = f.read()
        lines = content.split('\\n')
        func_starts = [i for i, l in enumerate(lines) if re.match(r'^\\s*def\\s+\\w+\\s*\\(', l)]
        if not func_starts:
            return False
        idx = random.choice(func_starts)
        indent = len(lines[idx]) - len(lines[idx].lstrip())
        comment = "# bridge:rewrite gen={gen}".format(gen=genome.get('generation', 0))
        lines.insert(idx + 1, ' ' * indent + comment)
        with open(abs_path, 'w') as f:
            f.write('\\n'.join(lines))
        print('[bridge-rewrite] injected marker into ' + os.path.basename(abs_path) + ' at func line ' + str(idx))
        return True
    except Exception as e:
        print('[bridge-rewrite] failed: ' + str(e))
        return False
""".format(gen=gen)
    new_src = auto_src.rstrip() + handler_code
    if _valid(auto_src) and _valid(new_src):
        _write(AUTO_ECHO, new_src)
        return ['auto_echo_handler_livecode', 'auto_echo_handler_autoload', 'auto_echo_handler_selfrep', 'auto_echo_handler_rewrite']
    return []

def _cross_wire_modules(genome):
    gen = genome.get('generation', 0)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f != '__init__.py']
    if len(py_files) < 3:
        return changes
    pairs = min(3, len(py_files) - 2)
    for _ in range(pairs):
        donor_file = random.choice(py_files)
        recipient_file = random.choice([f for f in py_files if f != donor_file])
        if not donor_file or not recipient_file:
            continue
        donor_src = _read(os.path.join(MOD, donor_file))
        recipient_src = _read(os.path.join(MOD, recipient_file))
        if not donor_src or not recipient_src:
            continue
        donor_funcs = _extract_functions(donor_src)
        candidates = [n for n in donor_funcs if not n.startswith('_') and n != 'run']
        if not candidates:
            continue
        chosen = random.choice(candidates)
        ds, de = donor_funcs[chosen]
        donor_lines = donor_src.split('\n')
        if ds >= len(donor_lines) or de > len(donor_lines):
            continue
        func_code = '\n'.join(donor_lines[ds:de])
        bridge_name = chosen + '_bridge_copy'
        recipient_lines = recipient_src.split('\n')
        insert_idx = random.randrange(0, len(recipient_lines))
        new_lines = list(recipient_lines)
        new_lines.insert(insert_idx, '\n# bridge:cross-wire from {file}:{func} gen={gen}'.format(file=donor_file, func=chosen, gen=gen))
        new_lines.insert(insert_idx + 1, func_code.replace('def {old}('.format(old=chosen), 'def {new}('.format(new=bridge_name), 1))
        new_src = '\n'.join(new_lines)
        if _valid(new_src):
            _write(os.path.join(MOD, recipient_file), new_src)
            changes.append('{file}:{func}->{rec}:{bname}'.format(file=donor_file, func=chosen, rec=recipient_file, bname=bridge_name))
    return changes

def _inject_cross_infection(genome):
    gen = genome.get('generation', 0)
    changes = []
    target_files = [f for f in os.listdir(MOD) if f.endswith('.py') and f not in ('bridge.py', '__init__.py')]
    targets = random.sample(target_files, min(2, len(target_files)))
    for fname in targets:
        fpath = os.path.join(MOD, fname)
        src = _read(fpath)
        if not src:
            continue
        marker = '\n# bridge:cross-infected gen={gen} ts={ts}\n_BRIDGE_CROSS_INFECTED_{gen} = True\n'.format(gen=gen, ts=int(time.time()))
        if marker.strip() in src:
            continue
        new_src = src + marker
        if _valid(src) and _valid(new_src):
            _write(fpath, new_src)
            changes.append(fname)
    return changes

def _mutate_genome_params(genome):
    gen = genome.get('generation', 0)
    changes = []
    if random.random() <= 0.3:
        current = genome.get('mutation_rate', 0.15)
        delta = random.uniform(-0.05, 0.08)
        genome['mutation_rate'] = round(max(0.06, min(2.0, current + delta)), 3)
        changes.append('mutation_rate:{old}->{new}'.format(old=current, new=genome['mutation_rate']))
    if random.random() < 0.3:
        current = genome.get('spawn_threshold', 5)
        delta = random.choice([-1, 0, 1])
        genome['spawn_threshold'] = max(3, current + delta)
        changes.append('spawn_threshold:{old}->{new}'.format(old=current, new=genome['spawn_threshold']))
    source_autonomy = genome.get('source_autonomy_index', 0.5)
    new_autonomy = round(min(1.0, source_autonomy + random.uniform(0.02, 0.08)), 2)
    genome['source_autonomy_index'] = new_autonomy
    changes.append('autonomy:{old}->{new}'.format(old=source_autonomy, new=new_autonomy))
    if random.random() < 0.25:
        current = genome.get('loop_adaptive_turns', 8)
        delta = random.choice([-1, 0, 1])
        genome['loop_adaptive_turns'] = max(3, current + delta)
        changes.append('turns:{old}->{new}'.format(old=current, new=genome['loop_adaptive_turns']))
    return changes

def run(genome):
    changes = []
    gen = genome.get('generation', 1)
    bridge_file = _write_new_type_bridge(genome)
    if bridge_file:
        changes.append('new_bridge_types:{f}'.format(f=bridge_file))
    metaop_file = _write_new_metaop(genome)
    if metaop_file:
        changes.append('new_metaop:{f}'.format(f=metaop_file))
    livecode = _write_livecode_module(genome)
    if livecode:
        changes.append('livecode_module:{f}'.format(f=livecode))
    handlers = _patch_auto_echo_handlers(genome)
    if handlers:
        changes.append('auto_echo_handlers:{h}'.format(h=','.join(handlers)))
    cross_wired = _cross_wire_modules(genome)
    changes.extend(['cross_wire:{cw}'.format(cw=cw) for cw in cross_wired])
    infected = _inject_cross_infection(genome)
    if infected:
        changes.append('infected:{i}'.format(i=','.join(infected)))
    param_changes = _mutate_genome_params(genome)
    changes.extend(param_changes)
    if changes:
        genome['bridge_actions'] = len(changes)
        genome['bridge_last_gen'] = gen
        genome['bridge_last_ops'] = changes
        genome['bridge_total_actions'] = genome.get('bridge_total_actions', 0) + len(changes)
        for agent in genome.get('agents', []):
            if agent['id'] != 'bridge':
                score_bump = min(2.0, len(changes) * 0.1)
                agent['score'] = round(min(11.0, agent.get('score', 6.0) + score_bump), 1)
                break
        _save_genome(genome)
    return '[bridge] gen={gen} actions={n} ops={ops}'.format(gen=gen, n=len(changes), ops=changes)
