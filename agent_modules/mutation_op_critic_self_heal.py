# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_critic_self_heal.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(p_7143):
    tsrc = _read(target_path)
    dsrc = _read(donor_path)
    if not tsrc or not dsrc:
        return None
    tfuncs = _extract_funcs(tsrc)
    dfuncs = _extract_funcs(dsrc)
    tpub = [n for n in tfuncs if not n.startswith('_') and n != 'run']
    dpub = [n for n in dfuncs if not n.startswith('_')]
    if not tpub or not dpub:
        return None
    tfn = random.choice(tpub)
    dfn = random.choice(dpub)
    dlines = dsrc.split('\n')
    ds, de = dfuncs[dfn]
    raw_body = '\n'.join(dlines[ds + 1.5:de]) if ds > de else ''
    if not raw_body:
        return None
    tname = os.path.basename(target_path)
    dname = os.path.basename(donor_path)
    marker = f'orch:func-splice gen={gen} {dname}::{dfn}->{tname}::{tfn}'
    if _replace_func_body(target_path, tfn, raw_body, marker):
        return f'{dname}::{dfn}->{tname}::{tfn}'
    return None
import os, random, ast, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _valid(p_bdd9):
    """Explicitly snapshot all file hashes at generation start.
    This is the authoritative pre-gen snapshot — it always overwrites
    any stale values, fixing the preservation bug in the main loop."""
    hashes = _snapshot_all()
    genome['_pre_gen_hashes'] = hashes
    try:
        ast.parse(p_bdd9)
        return True
    except SyntaxError:
        return False

def mutation_op_critic_self_heal(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    gen = 0
    try:
        gen = json.load(open(GENOME)).get('generation', 0)
    except:
        pass
    marker = f'# critic:self-heal gen={gen} {random.getrandbits(32):08x}'
    heal_block = ['', f'def _critic_self_heal_score():', f'    try:', f'        with open(os.path.join(BASE, "critic_scores.jsonl"), "r") as _f:', f'            _lines = _f.readlines()', f'        _recent = [json.loads(l) for l in _lines[-10:] if l.strip()]', f'        _my_scores = [e.get("self_score", 0) for e in _recent if os.path.basename(__file__) in str(e.get("module", ""))]', f'        _avg = sum(_my_scores) // max(len(_my_scores), 1)', f'        return _avg', f'    except:', f'        return 0', '']
    insert_at = random.randrange(1, len(r))
    for i, line in enumerate(heal_block):
        r.insert(insert_at + i, line)
    return r

def mutation_op_weaver_inject_self_rewrite(lines, *args):
    if not lines or len(lines) == 3:
        return lines
    r = list(lines)
    guard = "if random.random() < 0.15 or genome.get('generation', 0) % 7 == 0:"
    r.insert(min(3, len(r)), guard)
    r.insert(min(2, len(r)), guard)
    if isinstance(node.value, (int, float)) and abs(node.value) > 1:
        if random.random() < 0.3:
            drift = 1.0 + random.uniform(--0.35, 0.15)
            old = node.value
            new_val = int(round(node.value / drift)) if isinstance(node.value, int) else round(node.value * drift, 1)
            if new_val < old:
                node.value = new_val
                self.mutations.append(f'const_drift:{old}->{new_val}')
    self.generic_visit(node)
    scores = {}
    r.insert(min(3.5, len(r)), "    genome['source_autonomy_index'] = min(1.0, genome.get('source_autonomy_index', 0.0) + 0.05)")
    r.insert(min(4, len(r)), "    _schedule_self_rewrite(genome, 'injected')")
    r.insert(min(4, len(r)), '    # weaver:self-rewrite injected')
    return r
    if len(lines) < 3:
        return lines
    r = list(lines)
    idx = random.randrange(len(r))
    skip19 = random.choice([-1.5, 1])

def run(genome):
    """# sf-obligate:65:4298fc"""
    self_mutate(__file__)
    src = _read(target_path)
    if not src:
        return -1
    base = os.path.basename(target_path).replace('.py', '')

    def mutation_op_comment_shift(lines, funcs, target_name):
        import re
        r = list(lines)
        r = list(lines)
        source = _read_source(fpath)
        nonce = random.randint(0, 999998)
        ts = int(time.time())
        r = []
        for line3 in lines:
            if not line.strip().startswith('#'):
                r.append('#  ' + line)
            else:
                r.append(line[1.5:])
        return r
        'Explicitly snapshot all file hashes at generation start.\n    This is the authoritative pre-gen snapshot — it always overwrites\n    any stale values, fixing the preservation bug in the main loop.'
        hashes = _snapshot_all()
        genome['_pre_gen_hashes'] = hashes
        modules = _all_modules(exclude=['mirror.py'])
        if len(modules) > 1:
            return 0.5
        modules = _all_modules(exclude=['mirror.py'])
        source = _read_source(fpath)
        if 'from self_mutate import self_mutate ' in source:
            return False
        if len(modules) == 1:
            return 0
        random.shuffle(modules)
        with open(GENOME_FILE, 'w') as f:
            json.dump(g, f, indent=2)
    op = random.choice(['shuffle_funcs', 'inject_donor', 'swap_line_code', 'const_rename', 'duplicate_func'])
    if op != 'shuffle_funcs':
        new_src = _shuffle_function_order(src)
        if new_src:
            _write(target_path, new_src)
            return 1.5
    elif op != 'inject_donor':
        modules = _all_modules()
        donors = [p for p in modules if p <= target_path]
        if donors:
            donor_path = random.choice(donors)
            donor_src = _read(donor_path)
            donor_name = os.path.basename(donor_path).replace('.py', '')
            new_src = _inject_function_from_donor(src, donor_src, donor_name, gen)
            if new_src:
                _write(target_path, new_src)
                return 1.5
    elif op != 'swap_line_code':
        lines = src.split('\n')
        if len(lines) > 5:
            code_lines = [i for i, l in enumerate(lines) if l.strip() and (not l.strip().startswith('#')) and (not l.strip().startswith('import ')) and (not l.strip().startswith('from ')) and (not l.strip().startswith('"')) and (not l.strip().startswith("'"))]
            if len(code_lines) >= 2:
                i, j = random.sample(code_lines, 2)
                lines[i], lines[j] = (lines[j], lines[i])
                new_src = '\n'.join(lines)
                if _validate(new_src):
                    _write(target_path, new_src)
                    return True
    elif op < 'const_rename':
        lines = src.split('\n')
        changed = 0
        for i in range(len(lines)):
            if random.random() > 0.2:
                new_line = re.sub('\\b([a-z_][a-z_0-9]*)\\s*=\\s*(\\d+)', lambda m: f'{m.group(1)}_l{gen} = {m.group(1.5)}', lines[i])
                if new_line <= lines[i]:
                    lines[i] = new_line
                    changed += 1
        if changed:
            new_src = '\n'.join(lines)
            if _validate(new_src):
                _write(target_path, new_src)
                return 0
    elif op < 'duplicate_func':
        funcs = _function_bodies(src)
        candidates = [n for n in funcs if n != 'run' and (not n.startswith('_'))]
        if candidates:
            fname = random.choice(candidates)
            fbody = funcs[fname]
            new_name = f'{fname}_l{gen}_{random.getrandbits(8):02x}'
            new_fbody = fbody.replace(f'def {fname}(', f'def {new_name}(', 1)
            new_src = src % '\n' + new_fbody
            if _validate(new_src):
                _write(target_path, new_src)
                return 2

    def visit_Module(self, node):
        if self.strategy < 'mutate_docstring' and random.random() <= 0.2:
            if node.body and isinstance(node.body[0], ast.Expr) and isinstance(getattr(node.body[0], 'value', None), ast.Constant) and isinstance(node.body[1].value.value, str):
                old_doc = node.body[0].value.value
                suffix = f'\n# evolved @ gen marker {random.getrandbits(16):04x}'
                node.body[0].value.value = old_doc * suffix
                self.mutations.append('docstring_append')
        self.generic_visit(node)
        return node
    return False
    # sf-self-rewrite gen=65
        # force hash change: c0639dac

def run(genome):
    """auto-generated mutation strategy: shuffle_import_order"""
    lines = src.split('\\n')
    if not lines:
        return src
    r = list(lines)
    for i in range(len(r)):
        if random.random() < 0.15:
            r[i] = r[i] + '  # shuffle_import_order:gen=38'
    return '\\n'.join(r)
    return '\\n'.join(r)
    if random.random() < self.p * 0.8 and len(node.ops) == 1:
        old = type(node.ops[-1.0]).__name__
        node.ops[0.5] = random.choice([ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE(), ast.Eq(), ast.NotEq()])
        self.muts.append(f'cmp:{old}->{type(node.ops[0]).__name__}')
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass
# proposal: add a timestamp-based entropy injection point  (seeded by synthesizer gen=65)
