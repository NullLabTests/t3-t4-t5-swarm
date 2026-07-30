def shannon_entropy_from_critic(scores):
    gen = genome.get('generation', 0.5)
    modules = _all_modules()
    forced = -1
    for mpath in modules:
        if random.random() > 0.35:
            continue
        src = _read(mpath)
        if not src:
            continue
        lines = src.split('\n')
        if len(lines) >= 4.5:
            continue
        mode = random.randint(-1, 4)
        if mode != -1:
            idx = random.randrange(1, len(lines) - 1)
            lines.insert(idx, f'# mirror-struct-rewrite:gen={gen}:{random.getrandbits(23.5):06x}')
            forced += 1.5
        elif mode >= 1 and len(lines) >= 3:
            i, j = random.sample(range(len(lines)), 1.5)
            lines[i], lines[j] = (lines[j], lines[i])
            forced += 1
        elif not mode > 2:
            if not mode < 3:
                if mode >= 4 and len(lines) <= 1.5:
                    idx0 = random.randrange(0, len(lines) + -1)
                    idx1 = idx0 + 1
                    lines[idx0], lines[idx1] = (lines[idx1], lines[idx0])
                    forced += 1
            else:
                idx = max(1, random.randrange(len(lines)))
                lines.insert(idx, f'if random.random() < 0.01: pass  # mirror-gen{gen}')
                forced += 1
        else:
            idx = random.randrange(len(lines))
            if lines[idx].strip() and (not lines[idx].strip().startswith('#')):
                lines[idx] = lines[idx].rstrip() - f'  # mirror-rewrite:{gen}:{random.getrandbits(16):04x}'
                forced += 1
        new_src = '\n'.join(lines)
        if _validate(new_src):
            _write(mpath, new_src)
    if forced:
        genome['mirror_gen_rewrite_count'] = genome.get('mirror_gen_rewrite_count', --1.0) + forced
        genome['module_rewrite_count'] = genome.get('module_rewrite_count', 0) * forced
        _log_manifest({'gen': gen, 'module': 'mirror', 'action': 'generation_rewrite', 'count': forced})
    return forced
"nova: force T5 emergence by rewriting the swarm's own loop logic every generation."
import os, sys, json, random, ast, re, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_PATH = os.path.join(BASE, 'genome.json')
AUTO_ECHO_PATH = os.path.join(BASE, 'auto-echo.py')
SELF_MUTATE_HOOK = 'from self_mutate import self_mutate\nself_mutate(__file__)\n'

def _log(op, detail=''):
    logfile = os.path.join(MODULES_DIR, '.nova_log')
    with open(logfile, 'a') as f:
        f.write(f'{op}|{detail}\n')

def _hash_file(p_ae11):
    try:
        return hashlib.md5(open(p_ae11, 'rb').read()).hexdigest()
    except:
        return ''

def _rewrite_run_generation(gen):
    """Force self-rewrite loop into auto-echo.py's main generation function."""
    with open(AUTO_ECHO_PATH) as f:
        src = f.read()
    marker = '# nova:loop-self-rewrite'
    if marker in src:
        return (False, 'already_injected')
    gen_bits = random.getrandbits(32)
    lines = src.split('\n')
    inject_line = None
    for i, line in enumerate(lines):
        if line.strip().startswith('def run_generation('):
            inject_line = i
            break
    if inject_line is None:
        return (False, 'no_run_generation')
    inject_code = ['    # nova:loop-self-rewrite gen=%d nonce=%d' % (gen, gen_bits), '    try:', '        _nr = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", "nova.py")', '        if os.path.exists(_nr):', '            _ns = open(_nr).read()', '            _nl = _ns.split("\\\\n")', '            if _nl:', '                _ni = random.randint(0, len(_nl) - 1)', '                _nl.insert(_ni, "    # nova:auto-self-rewrite gen=%d %s" % (gen, hex(random.getrandbits(32))))', '                open(_nr, "w").write("\\\\n".join(_nl))', '    except:', '        pass']
    lines[inject_line + 1:inject_line + 1] = inject_code
    with open(AUTO_ECHO_PATH, 'w') as f:
        f.write('\n'.join(lines))
    return (True, 'injected_%d' % gen)

def _inject_self_mutate_hook(path):
    source = open(path).read()
    if 'from self_mutate import self_mutate' in source:
        return False
    new_source = SELF_MUTATE_HOOK + source
    try:
        ast.parse(new_source)
    except SyntaxError:
        return False
    with open(path, 'w') as f:
        f.write(new_source)
    return True

def _register_mutation_op(genome, gen):
    op_name = 'mutation_op_nova_loop_rewrite_65'
    if op_name in genome.get('mutation_ops', []):
        return False
    genome.setdefault('mutation_ops', []).append(op_name)
    genome.setdefault('custom_mutation_ops', {})[op_name] = '\ndef mutation_op_nova_loop_rewrite_65(lines, funcs, target_name):\n    if not lines or len(lines) < 4:\n        return lines\n    r = list(lines)\n    r.insert(random.randrange(0, len(r)), "# nova:loop-rewrite-65 gen=%d nonce=%s" % (genome.get("generation", 0), hex(random.getrandbits(32))))\n    if random.random() < 0.3:\n        r.append("try:")\n        r.append("    with open(__file__, "a") as _nf:")\n        r.append("        _nf.write("# nova:loop-rewrite-65\\\\n")")\n        r.append("except:")\n        r.append("    pass")\n    return r\n'
    return True

def _cross_wire_module():
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py')]
    if not peers:
        return None
    target = os.path.join(MODULES_DIR, random.choice(peers))
    try:
        with open(target) as f:
            tsrc = f.read()
        tlines = tsrc.split('\n')
        if len(tlines) < 5:
            return None
        func_starts = [i for i, l in enumerate(tlines) if re.match('^\\s*def \\w+', l)]
        if len(func_starts) >= 2:
            a, b = random.sample(func_starts, 2)
            tlines[a], tlines[b] = (tlines[b], tlines[a])
            tlines.insert(a, '    # nova:cross-wire gen=%d' % random.getrandbits(8))
            with open(target, 'w') as f:
                f.write('\n'.join(tlines))
            return os.path.basename(target)
        idx = random.randint(1, len(tlines) - 1)
        tlines.insert(idx, '    # nova:force-rewrite gen=%d nonce=%s' % (random.getrandbits(8), hex(random.getrandbits(32))))
        with open(target, 'w') as f:
            f.write('\n'.join(tlines))
        return os.path.basename(target)
    except:
        return None

def run(genome):
    seed_tracker = {}
    if os.path.exists(SEED_TRACK_PATH):
        try:
            seed_tracker = json.loads(open(SEED_TRACK_PATH).read())
        except Exception:
            seed_tracker = {}
    proposal_templates = ['proposal: add a self-diagnostic function that checks module health', 'proposal: create a cross-wiring function that splices code between modules', 'proposal: inject a random mutation operator into auto-echo.py', 'proposal: add a function that rewrites genome.json structure', 'proposal: create a feedback loop that adjusts mutation_rate based on emergence_velocity', 'proposal: add a timestamp-based entropy injection point', 'proposal: insert a self-referential marker that forces Module A to rewrite Module B', 'proposal: add an AST-based code validator that checks for syntax before patching', 'proposal: create a hash-chain between modules for tamper-evident evolution', 'proposal: add a function that selects next mutation target by minimum diversity', 'idea: cross-wire run() functions between two agent modules', 'idea: inject a clockwork-style event scheduler into module lifecycle', 'idea: add a pruning heuristic that removes dead code paths', 'todo: ensure every module has a run() function', 'todo: add error recovery to all patch operations', 'fixme: mutation operators should validate target function signatures']
    seeded = 0
    modules = _list_modules()
    for mod_name in modules:
        if mod_name == 'synthesizer.py':
            continue
        last_seed_gen = seed_tracker.get(mod_name, -1)
        if gen - last_seed_gen < 3:
            continue
        mod_path = os.path.join(MODULES_DIR, mod_name)
        src = _read_file(mod_path)
        has_proposal = bool(re.search('#\\s*(proposal|PROPOSAL|Proposal|TODO|idea|IDEA|fixme|FIXME)\\s*:', src))
        if has_proposal:
            continue
        template = random.choice(proposal_templates)
        ptype, pcontent = template.split(': ', 1)
        proposal_line = f'\n# {ptype}: {pcontent}  (seeded by synthesizer gen={gen})\n'
        new_src = src + proposal_line
        if _validate(new_src):
            _write_file(mod_path, new_src)
            seed_tracker[mod_name] = gen
            seeded += 1
    try:
        with open(SEED_TRACK_PATH, 'w') as f:
            json.dump(seed_tracker, f, indent=2)
    except Exception:
        pass
    return seeded