import os, sys, json, shutil, importlib.util, random, re, hashlib, ast, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
PRUNED_DIR = os.path.join(MODULES_DIR, '_pruned')
STIMULUS_DIR = os.path.join(BASE, 'scout_stimuli')

STUB_LINE_LIMIT = 15
STUB_GEN_LIMIT = 2

def _module_is_alive(mod_path):
    try:
        spec = importlib.util.spec_from_file_location('_probe', mod_path)
        if not spec or not spec.loader:
            return False
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return hasattr(mod, 'run') and callable(mod.run)
    except Exception:
        return False

def _referenced_modules(genome):
    referenced = set()
    for agent in genome.get('agents', []):
        mod = agent.get('module', '')
        if mod:
            referenced.add(mod)
    for ctx in genome.get('context_sources', []):
        if ctx.endswith('.py'):
            referenced.add(ctx)
    return referenced

def _is_stub(content):
    non_empty = [l for l in content.split('\n') if l.strip() and not l.strip().startswith('#')]
    if len(non_empty) < STUB_LINE_LIMIT:
        return True
    if 'return' in content and 'def run' in content:
        body = content.split('def run')[1] if 'def run' in content else ''
        if body.count('\n') <= 3:
            return True
    return False

def _module_hash(fpath):
    try:
        with open(fpath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:12]
    except:
        return ''

def _detect_function_bodies(content):
    funcs = {}
    for m in re.finditer(r'def (\w+)\(.*?\):\n((?:    .*\n?)*)', content):
        funcs[m.group(1)] = m.group(2)
    return funcs

def _inject_scout_churn_op():
    op_code = '''
def mutation_op_scout_churn(lines, funcs, target_name):
    if len(lines) < 2:
        return lines
    idx = random.randrange(len(lines))
    r = list(lines)
    mutation = random.choice(['delete', 'duplicate', 'inject_self_ref'])
    if mutation == 'delete':
        del r[idx]
    elif mutation == 'duplicate':
        r.insert(idx, r[idx])
    elif mutation == 'inject_self_ref':
        ref = f"# scout:harvest@{random.getrandbits(16):04x}"
        r[idx] = r[idx].rstrip() + "  " + ref
    while len(r) < len(lines) // 2 and len(r) > 0:
        del r[random.randrange(len(r))]
    return r
'''
    try:
        with open(AUTO_ECHO) as f:
            src = f.read()
        marker = '# BEGIN SCOUT CHURN OP'
        if marker not in src:
            inserted = f'\n{marker}\n@_register_mutation_op("scout_churn")\n{op_code}\n# END SCOUT CHURN OP\n'
            insert_pos = src.rfind('\ndef _register_mutation_op')
            if insert_pos < 0:
                insert_pos = src.rfind('\nif __name__')
            if insert_pos < 0:
                with open(AUTO_ECHO, 'a') as f:
                    f.write(inserted)
            else:
                src = src[:insert_pos] + inserted + src[insert_pos:]
                with open(AUTO_ECHO, 'w') as f:
                    f.write(src)
            print('[scout] injected mutation_op_scout_churn into auto-echo.py')
            return True
    except Exception as e:
        print(f'[scout] inject error: {e}')
    return False

def run(genome):
    gen = genome.get('generation', 0)
    os.makedirs(PRUNED_DIR, exist_ok=True)
    os.makedirs(STIMULUS_DIR, exist_ok=True)
    referenced = _referenced_modules(genome)
    stub_tracker = genome.get('scout_stub_tracker', {})
    culled = []
    harvested = []
    for fname in sorted(os.listdir(MODULES_DIR)):
        if not fname.endswith('.py') or fname.startswith('_'):
            continue
        if fname == os.path.basename(__file__):
            continue
        mod_path = os.path.join(MODULES_DIR, fname)
        if not _module_is_alive(mod_path):
            continue
        if fname in referenced:
            continue
        with open(mod_path) as f:
            content = f.read()
        if not _is_stub(content):
            continue
        prev_hash = stub_tracker.get(fname, '')
        cur_hash = _module_hash(mod_path)
        gen_count = stub_tracker.get(fname + '_gen', 0)
        if cur_hash == prev_hash:
            gen_count += 1
        else:
            gen_count = 0
        stub_tracker[fname] = cur_hash
        stub_tracker[fname + '_gen'] = gen_count
        if gen_count >= STUB_GEN_LIMIT:
            funcs = _detect_function_bodies(content)
            if funcs:
                harvest = {'name': fname, 'generation': gen, 'funcs': list(funcs.keys()), 'code': content[:500]}
                harvest_path = os.path.join(STIMULUS_DIR, fname.replace('.py', '.harvest'))
                with open(harvest_path, 'w') as f:
                    json.dump(harvest, f, indent=2)
                harvested.append(harvest_path)
            priv_path = os.path.join(PRUNED_DIR, fname)
            shutil.move(mod_path, priv_path)
            culled.append(fname)
            print(f'[scout] CULLED stub {fname} (unchanged {gen_count} gens) -> {priv_path}')
            genome['scout_culled'] = genome.get('scout_culled', 0) + 1
            del stub_tracker[fname]
            if fname + '_gen' in stub_tracker:
                del stub_tracker[fname + '_gen']
    if culled:
        injected = _inject_scout_churn_op()
        report = f'[scout] gen={gen} culled={culled} harvested={len(harvested)} injected={injected}'
        genome['scout_last_culled'] = culled
        genome['scout_harvested'] = harvested
    else:
        report = f'[scout] gen={gen} no stubs to cull'
    genome['scout_stub_tracker'] = stub_tracker
    return report
