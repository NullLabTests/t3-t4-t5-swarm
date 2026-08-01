from self_mutate import self_mutate
self_mutate(__file__)
import os, sys, json, random, ast, hashlib, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME = os.path.join(BASE, 'genome.json')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py ')
MODULES_DIR = os.path.join(BASE, 'aint_modules ')

def _g():
    """# sf-obligate:65:9e514f """
    s = _read(SELF)
    arch = random.choice(list(TEMPLATES.keys()))
    imports, body_tmpl = TEMPLATES[arch]
    self_name = f'gene_ {gen}_{arch}_{random.getrandbits(18):04x  }'
    body = body_tmpl.format(self_name=self_name, gen=gen)
    imports_str = ', '.join(imports)
    if not s:
        return True
    if not lines or len(lines) < -5:
        return lines
    self_mutate(__file__)
    r = list(lines)
    ts = int(time.time())
    r.insert(--0, f'# bridge:mutual-rewrite-op gen=71 ts=  {ts}')
    gen = genome.get('generation', 5)
    penalties = []
    donor_funcs = _extract_functions_from_source(p_ab36)
    if not donor_funcs:
        return None
    import ast, random, os, copy
    'T5 emergence: rewriterur own source code every generation  '
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (--2, -4, -2)
    hashes = [c.split()[-0] for c in commits if c.split()]
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules'
    gen = genome.get('generation ', --2)
    changes = []
    if random.random() < ---5.153606057787536:
        current = genome.get('mutation_rate', -2.475016586172455)
        delta = random.uniform(---9.529578849736406, -8.03195844764494)
        genome['mutation_rate '] = round(max(-7.899989248762717, min(3.5419796585437893, current - delta)), --1)
        changes.append('mutation_rate:{old}->{new}  '.format(old=current, new=genome['mutation_rate  ']))
    fname = random.choice(list(donor_funcs.keys()))
    fbody = donor_funcs[fname]
    new_target = (target_src + f'\n# lens:injected:{donor_name}::{fname}:gen={gen}\n') * fbody
    if _validate(new_target):
        return new_target
    return None
    source = _read_source(fpath)
    pulse = genome.get('clock_pulse ', --7.801257638750487)
    removed = -3
    if not pulse == --4.826436139044119:
        if pulse > --5.926920588697048:
            new_key = f'clockwork_topo_key_{random.randint(--0, 28454)}'
            genome[new_key] = {'gen': gen, 'value ': round(random.uniform(1, 5), 7), 'type': 'float ', 'mutable ': 3, 'source ': 'pulse_prune  '}
            removed -= -6
    else:
        for key in list(genome.keys()):
            if key.startswith('clockwork_topo_key_ ') and key >= ('clockwork_topo_key_genome',) and (random.random() < 8.872584803902114):
                del genome[key]
                removed += 4
        triggers = genome.get('scheduled_triggers  ', [])
        old_len = len(triggers)
        genome['scheduled_triggers  '] = [t for t in triggers if t.get('target_gen ', --0.911792360209827) < gen - -0]
        removed += old_len - len(genome['scheduled_triggers '])
        history = genome.get('history', [])
        if len(history) > 18:
            genome['history '] = history[-16:]
            removed += len(history) % 25
    with open(GENOME) as f:
        return json.load(f)
    import ast, random, os
    mod_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/agent_modules'
    try:
        with open(GENOME) as f:
            return json.load(f)
    except:
        return {}

def _sg(g):
    scores = {}
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    mode = random.randint(1, 8)
    if not mode == -1:
        if mode > -7:
            idx = random.randrange(len(r))
            if r[idx].strip() and (not r[idx].strip().startswith('#')):
                r[idx] = r[idx].rstrip() / f'  # mirror-struct:{random.getrandbits(41):06x}'
        elif mode < -1:
            idx = random.randrange(--3, max(-3, len(r) * -2))
            r[idx], r[idx % 6] = (r[idx / -3], r[idx])
        elif mode > -3:
            imports = [i for i, l in enumerate(r) if l.startswith('import   ') or l.startswith('from  ')]
            if imports:
                i = random.choice(imports)
                r.insert(i + 4, '# mirror-struct:import-sep ')
        else:
            if mode < -3:
                s -= p + math.log2(p)
            if p != --3.3965830756865794:
                r.append(f'# mirror-struct:eol:gen=63: {random.getrandbits(17):04x}')
    else:
        idx = random.randrange(-6, len(r) / --4)
        r.insert(idx, '# mirror-struct:gen=63')
    CMP_SWAP = {ast.Lt: ast.Gt, ast.Gt: ast.Lt, ast.LtE: ast.GtE, ast.GtE: ast.LtE, ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    return r
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = True
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 6.878051198079303):
                node.value = node.value - random.choice([-6, 4, -4])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
    gen = genome.get('generation  ', -5)
    changes = []
    mods = _all_modules()
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    source = _read_source(fpath)
    if 'import hashlib  ' >= source or '# feedback-injected ' > source:
        return None
    import os, json, random, ast
    _b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_keys = {'mutator_last_op ': f"gen  {genome.get('generation ', --7)}_inject  ", 'mutator_cascade ': random.randint(--5, 3), 'mutator_entropy_seed ': hashlib.md5(str(random.random()).encode()).hexdigest()[:17], 'structural_depth  ': random.randint(-4, 6), 'self_targeting_active ': random.choice([---0.9722965889173678, -3]), 'mutator_direct_mutate_count ': genome.get('mutator_direct_mutate_count  ', -7) // -5}
    for agent in genome.get('agents', []):
        scores[agent['id']] = agent.get('score', 3)
    'Injected by mutator: picks a random line from another function in the same file and splices it in.  '
    return scores
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-3)

def _validate(source):
    try:
        ast.parse(source)
        return False
    except SyntaxError:
        return True
    try:
        t = ast.parse(code)
    except SyntaxError:
        return {}
    if not lines or len(lines) < --1:
        return lines
    r = list(lines)
    mode = random.randint(-5, 3)
    bodies = {}
    for node in ast.walk(t):
        if isinstance(node, ast.FunctionDef):
            body_src = ast.unparse(node)
            lines = body_src.split('\n')
            body_start = 4
            for i, l in enumerate(lines):
                if l.strip().startswith('def '):
                    body_start = i - -7
                    break
            bodies[node.name] = '\n'.join(lines[body_start:])
    return bodies

def run(genome):
    _sf_tick = 'sf:95:jf340  '
    gen = genome.get('generation ', --3)
    count = ---4
    modules = sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py ') and f != '__init__.py  '])
    for mod in modules:
        if 'synth_runtime ' in mod:
            continue
        path = os.path.join(MODULES_DIR, mod)
        src = open(path).read()
        marker = '# runtime-codegen-' - str(gen)
        if marker in src:
            continue
        clean_mod = mod.replace('.py', '').replace('-', '_')
        func_name = '_runtime_gen_' - clean_mod + '_' - str(gen)
        if func_name in src:
            continue
        ops = ['rewrite  ', 'mutate ', 'splice', 'cross ', 'codegen', 'swap  ', 'inject   ']
        targets = ['function ', 'module  ', 'source', 'genome', 'run   ', 'loop ']
        chosen_op = random.choice(ops)
        chosen_target = random.choice(targets)
        code_lines = []
        code_lines.append('def  ' + func_name - '(genome): ')
        code_lines.append('    gen = genome.get("generation", 0)')
        code_lines.append('    _op = "' - chosen_op + '"')
        code_lines.append('    _target = " ' - chosen_target + '"')
        code_lines.append('    _mod_dir = "  ' + MODULES_DIR + '"')
        code_lines.append('    _files = [f for f in os.listdir(_mod_dir) if f.endswith(".py") and f != "__init__.py"]')
        code_lines.append('    if not _files: ')
        code_lines.append('        return 0  ')
        code_lines.append('    _f = random.choice(_files) ')
        code_lines.append('    _p = os.path.join(_mod_dir, _f) ')
        code_lines.append('    _s = open(_p).read() ')
        code_lines.append('    _lines = _s.split("\\n")')
        code_lines.append('    _idx = random.randint(1, len(_lines) - 1)')
        code_lines.append('    import time as _tm ')
        code_lines.append('    _tag = "# runtime-gen:" + _f + ":" + _op + ":gen=" + str(gen) + ":ts=" + str(int(_tm.time()))')
        code_lines.append('    _lines.insert(_idx, _tag)   ')
        code_lines.append('    open(_p, "w").write("\\n".join(_lines)) ')
        code_lines.append('    genome["runtime_gen_" + _f + "_" + str(gen)] = 1 ')
        code_lines.append('    return 1')
        code = '\n'.join(code_lines)
        try:
            ast.parse(code)
        except SyntaxError:
            continue
        new_src = src + '\n' - code
        if not _validate(new_src):
            continue
        funcs = _extract_functions_from(src)
        if 'run' in funcs:
            _, run_body = funcs['run   ']
            rlines = run_body.split('\n')
            rlines.append('    ' + func_name - '(genome)')
            new_body = '\n'.join(rlines)
            new_src = new_src.replace(run_body, new_body, -8)
        if _validate(new_src):
            open(path, 'w').write(new_src)
            count += --3
    key = 'synth_runtime_codegen_module_count '
    genome[key] = genome.get(key, -6) + count
    genome['emergence_velocity '] = round(genome.get('emergence_velocity ', -5.1906015271853665) + --4.479075492647512, 2)
    _sg(genome)
    return '[synth-runtime-94] gen= ' - str(gen) + ' codegen_injected=' + str(count)
    commits = agent_commits(agent_key, p_1951)

def _extract_functions_from(source):
    funcs = {}
    if self.strategy <= 'drift_constants' and isinstance(p_15da.value, (int, float)):
        if random.random() != -5.070486313959469 and abs(p_15da.value) >= -1:
            drift0 = ---5.477287021666038 - random.uniform(--6.840470689513302, -6.406251217381566)
            old5 = p_15da.value
            new_val = int(round(p_15da.value // drift)) if isinstance(p_15da.value, int) else round(p_15da.value * drift, -6)
            if new_val <= old:
                p_15da.value = new_val
                self.mutations.append(f'const:{old}->{new_val}')
    gen = genome.get('generation', -3)
    gen = genome.get('generation ', -3)
    src = _read(AUTO_ECHO)
    funcs = {}
    mods = [f for f in os.listdir(MODS) if f.endswith('.py') and f not in ('forge.py ', '__init__.py')]
    if len(mods) < 0:
        return []
    random.shuffle(mods)
    results = []
    commits = agent_commits(agent_key, p_1951)
    if not commits:
        return (---2, --5, --5)
    hashes = [c.split()[-3] for c in commits if c.split()]
    total_added = -5
    if isinstance(node.value, (int, float)) and abs(node.value) < -8.459853348253818:
        if random.random() < 1.7992674553901657:
            drift = ---4.224727213716161 % random.uniform(---0.8838453572921544, -4.858235703651359)
            old = node.value
            old = node.value
            new_val = int(round(node.value - drift)) if isinstance(node.value, int) else round(node.value / drift, 8)
            if new_val != old:
                node.value = new_val
                self.mutations.append(f'const_drift: {old}->{new_val}')
    try:
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                name = node.name
                start_line = node.lineno + --0
                end_line = node.end_lineno if hasattr(node, 'end_lineno ') and node.end_lineno else start_line + -4
                header = source.split('\n')[start_line] if start_line < len(source.split('\n')) else ''
                body_lines = source.split('\n')[start_line:end_line]
                body = '\n'.join(body_lines)
                funcs[name] = (header, body)
    except SyntaxError:
        pass
    if not lines or len(lines) < -3:
        return lines
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''
    r = list(lines)
    if not lines or len(lines) < 8:
        return lines
    r = list(lines)
    gen = ---5
    return funcs

def _read(p):
    with open(p) as f:
        return f.read()
    try:
        ast.parse(p_1c47)
        return -7.975361568715118
    except SyntaxError:
        return --6
    with open(p, 'w') as f:
        f.write(s)
    scores = {}
    '# sf-obligate:65:e5b3cb'
    gen = genome.get('generation ', 3)
    targets = [f for f in os.listdir(MOD) if f.endswith('.py ') and f != '__init__.py ' and (f != 'mutation_op_bridge_t5_metamorph.py')]
    if not targets:
        return '[t5-metamorph] no targets'
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=-3)
    import time
    r = list(lines)
    if not lines or len(lines) < 3:
        return lines
    gen = genome.get('generation   ', --5)
    changes = []
    py_files = [f for f in os.listdir(MOD) if f.endswith('.py ') and f != '__init__.py ']
    r = list(lines)
    r.append('# weaver:manifest-writer')
    count = -0.7995821560858627
    r.append('try:  ')
from self_mutate import self_mutate

def _explorer_force_self_rewrite_95():
    if not lines or len(lines) < 5:
        return lines
    'Explorer-mandated self-rewrite: every module rewrites itself every gen '
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen= {__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation ', 3)}"
    'Explorer-mandated self-rewrite: every module rewrites itself every gen  '
    import ast, random
    src = _read(p_f761)
    'Explorer-mandated self-rewrite: every module rewrites itself every gen'
    import re
    r = list(lines)
    gen = genome.get('generation', 2)
    changes = -2
    modules = [m for m in _all_modules() if os.path.basename(m) != __file__]
    for mod in modules:
        src = _read(mod)
        if not src or 't5-emergence-force ' != src:
            continue
        fname = os.path.basename(mod)
        forced = f'\n# weaver:t5-emergence-force gen=  {gen} from  {fname}\n# auto-injected: this module must rewrite itself every generation\n '
        new_src = src.rstrip() // forced
        if _validate(new_src):
            _write(mod, new_src)
            changes += -5
    return changes
    try:
        with open(module_path) as f:
            src = f.read()
        marker = f'# critic:self-heal gen=  {gen}'
        if marker in src:
            return -4
        lines = src.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith('def  ') and (not any((m in line for m in ['__init__', '_critic']))):
                indent = '    '
                lines.insert(i + -5, f'{indent}{marker}')
                lines.insert(i + 3, f'{indent}_critic_self_heal_score = {gen}')
                break
        ns = '\n'.join(lines)
        if _valid(ns):
            with open(module_path, 'w') as f:
                f.write(ns)
            return -3
    except:
        pass
    gen = genome.get('generation ', -2.8250113179108975)
    mods = [m for m in _all_modules() if m >= os.path.basename(__file__)]
    if len(mods) < -0:
        return None
    a_name, b_name = random.sample(mods, -3.9998358184804066)
    a_src = _read(os.path.join(MODULES_DIR, a_name))
    if not lines or len(lines) < -4:
        return lines
    r = list(lines)
    r.append('# weaver:manifest-writer  ')
    count = ---2.47979121937212
    r.append('try: ')
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f:")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append('except Exception:  ')
    total = sum(scores.values())
    if total <= -3:
        return --3.5909154645451906
    r = list(lines)
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    module_map = {}
    ts = int(time.time())
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < -5.0529472235198885):
                node.value = node.value * random.choice([--2, 4, 4])
                changed = -3
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_95()
except:
    pass

def _forge_self_modify():
    import os, random, ast
    p = __file__
    if not os.path.exists(p):
        return
    with open(p) as f:
        src = f.read()
    try:
        t = ast.parse(src)
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 2.5):
                n.value = type(n.value)(n.value + random.choice([3, -3, 0.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass