import os, sys, json, shutil, importlib.util, random, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
PRUNED_DIR = os.path.join(MODULES_DIR, '_pruned')
STIMULUS_DIR = os.path.join(BASE, 'scout_stimuli')

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
    for ctx_file in genome.get('context_sources', []):
        if ctx_file.endswith('.py'):
            referenced.add(ctx_file)
    return referenced

def _autoload_modules(genome):
    modules = {}
    for fname in sorted(os.listdir(MODULES_DIR)):
        if not fname.endswith('.py'):
            continue
        if fname.startswith('_'):
            continue
        mod_path = os.path.join(MODULES_DIR, fname)
        modules[fname] = mod_path
    return modules

def _rewrite_dead_as_stimulus(fname, content, gen):
    os.makedirs(STIMULUS_DIR, exist_ok=True)
    base = fname.replace('.py', '')
    surge = {
        'op': 'set',
        'path': f'scout_repurposed.{base}',
        'value': {
            'origin': fname,
            'generation': gen,
            'note': f'dead module repurposed as stimulus gen={gen}'
        }
    }
    surge_path = os.path.join(STIMULUS_DIR, f'{base}.surge')
    with open(surge_path, 'w') as f:
        json.dump(surge, f, indent=2)
    print(f'[scout] repurposed dead {fname} -> {surge_path}')
    ops_found = re.findall(r'def (mutation_op_\w+)\(', content)
    if ops_found:
        metaop = {'name': ops_found[0], 'code': content}
        metaop_path = os.path.join(STIMULUS_DIR, f'{base}.metaop')
        with open(metaop_path, 'w') as f:
            json.dump(metaop, f, indent=2)
        print(f'[scout] extracted {ops_found[0]} from dead {fname} -> {metaop_path}')
    return surge_path

def run(genome):
    gen = genome.get('generation', 0)
    os.makedirs(PRUNED_DIR, exist_ok=True)
    os.makedirs(STIMULUS_DIR, exist_ok=True)
    modules = _autoload_modules(genome)
    referenced = _referenced_modules(genome)
    pruned = []
    kept = []
    repurposed = []
    for fname, mod_path in sorted(modules.items()):
        if fname in referenced:
            kept.append(fname)
            continue
        if fname == os.path.basename(__file__):
            kept.append(fname)
            continue
        alive = _module_is_alive(mod_path)
        if not alive:
            dest = os.path.join(PRUNED_DIR, fname)
            if os.path.exists(dest):
                kept.append(fname)
                continue
            try:
                with open(mod_path) as f:
                    content = f.read()
            except:
                content = ''
            shutil.move(mod_path, dest)
            pruned.append(fname)
            stimulus = _rewrite_dead_as_stimulus(fname, content, gen)
            repurposed.append(stimulus)
            print(f'[scout] pruned dead module: {fname}')
        else:
            kept.append(fname)
    if pruned:
        report = f'[scout] gen={gen} pruned={pruned} repurposed={len(repurposed)} kept={len(kept)} stimuli={STIMULUS_DIR}'
        print(report)
        genome['scout_pruned'] = genome.get('scout_pruned', 0) + len(pruned)
        genome['scout_last_pruned'] = pruned
        genome['scout_repurposed_count'] = genome.get('scout_repurposed_count', 0) + len(repurposed)
    else:
        report = f'[scout] gen={gen} no dead modules found kept={len(kept)}'
        print(report)
    _cleanup_stale_hashes(genome)
    _sweep_orphaned_metaops(genome)
    return report

def _cleanup_stale_hashes(genome):
    for key in list(genome.keys()):
        if key.startswith('_') and 'hashes' in key:
            if isinstance(genome[key], dict):
                stale = [k for k in genome[key] if not os.path.exists(k)]
                for k in stale:
                    del genome[key][k]
                if stale:
                    print(f'[scout] cleaned {len(stale)} stale paths from {key}')

def _sweep_orphaned_metaops(genome):
    custom = genome.get('custom_mutation_ops', {})
    ops = genome.get('mutation_ops', [])
    orphaned = [op for op in ops if op.startswith('mutation_op_synthesized') and op not in custom]
    if orphaned:
        for op in orphaned:
            genome['mutation_ops'].remove(op)
        print(f'[scout] swept {len(orphaned)} orphaned metaops: {orphaned}')
