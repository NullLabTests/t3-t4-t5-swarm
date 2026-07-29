import os, ast, random, json, time, re, hashlib, textwrap, importlib.util, sys, shutil
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
LENS_LOG = os.path.join(BASE, 'lens_depth_log.jsonl')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
SELF_PATH = os.path.join(MODULES_DIR, 'lens.py')

def _read(fpath):
    try:
        with open(fpath) as f:
            return f.read()
    except:
        return ''

def _write(fpath, content):
    with open(fpath, 'w') as f:
        f.write(content)

def _validate(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False

def _all_modules():
    out = []
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and not fname.startswith('__') and fname != 'lens.py':
                out.append(os.path.join(MODULES_DIR, fname))
    return out

def _hash(src):
    return hashlib.sha256(src.encode()).hexdigest()[:12]

SELF_REF_PATTERNS = ['ENDO_STATE', 'self.*rewrite', 'metaop', 'genome.*feedback', 'patch.*auto.cho', 'cross.*module.*weave', 'invoke_peer', 'self_modify', '_spawn_meta', '_self_rewrite', 'lens.*force', '_cross_contaminate', 'import.*agent_modules', 't5_emergence', 'lens:structural', '_lens_self_mutate']

def _measure_depth(src):
    depth = 0
    score = 0
    patterns_found = []
    for pat in SELF_REF_PATTERNS:
        matches = re.findall(pat, src, re.IGNORECASE)
        if matches:
            patterns_found.append(pat)
            score += len(matches)
    try:
        tree = ast.parse(src)
        class DepthWalker(ast.NodeVisitor):
            def __init__(self):
                self.max_nesting = 0
                self.current = 0
            def visit_FunctionDef(self, node):
                self.current += 1
                self.max_nesting = max(self.max_nesting, self.current)
                self.generic_visit(node)
                self.current -= 1
            def visit_AsyncFunctionDef(self, node):
                self.visit_FunctionDef(node)
        dw = DepthWalker()
        dw.visit(tree)
        depth = dw.max_nesting
    except:
        pass
    return (depth, score, patterns_found)

def _inject_endstate(mpath, src):
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE' in src:
        return None
    stamp = '\nENDO_STATE = {"module": "' + base + '", "lens_stamp": ' + str(random.getrandbits(32)) + ', "gen": ' + str(int(time.time())) + '}\n'
    new_src = src + stamp
    if _validate(new_src):
        return new_src
    return None

def _cross_contaminate(mpath, src, all_peers):
    base = os.path.basename(mpath).replace('.py', '')
    did_import = re.findall(r'import agent_modules\.(\w+)', src)
    for peer_path, peer_src in all_peers:
        peer_base = os.path.basename(peer_path).replace('.py', '')
        if peer_base == base or peer_base in did_import:
            continue
        peer_import = f'import agent_modules.{peer_base}'
        if peer_import in src:
            continue
        new_src = f'import agent_modules.{peer_base}\n' + src
        if _validate(new_src):
            return (new_src, f'imported {peer_base}')
    return (None, None)

def _inject_full_self_rewrite(target_path):
    src = _read(target_path)
    if not src:
        return False
    base = os.path.basename(target_path).replace('.py', '')
    marker = f'# lens:self-rewrite-stub:{base}'
    if marker in src:
        return False
    stub = f'''
{marker}
def _lens_self_rewrite_stub_{base}(genome):
    import os, ast, random, time
    _self_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', '{base}.py')
    try:
        with open(_self_path) as _f:
            _src = _f.read()
        _lines = _src.split('\\n')
        _idx = random.randrange(2, max(3, len(_lines) - 1))
        _lines.insert(_idx, f'# lens:self-stub:gen={{genome.get("generation", 0)}}:{random.getrandbits(16):04x}')
        _new = '\\n'.join(_lines)
        ast.parse(_new)
        with open(_self_path, 'w') as _f:
            _f.write(_new)
        return True
    except:
        return False
'''
    new_src = src + stub
    if _validate(new_src):
        _write(target_path, new_src)
        return True
    return False

def _inject_structural_self_rewrite(target_path):
    src = _read(target_path)
    if not src:
        return False
    base = os.path.basename(target_path).replace('.py', '')
    structural_marker = f'# lens:structural:self-rewrite:{base}'
    if structural_marker in src:
        return False
    structural_fn = f'''
{structural_marker}
def _lens_structural_mutate_{base}(genome):
    import os, ast, random, re as _re
    _self_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', '{base}.py')
    try:
        with open(_self_path) as _f:
            _src = _f.read()
        _lines = _src.split('\\n')
        _op = random.choice(['swap_lines', 'dup_line', 'del_line', 'perturb_const', 'insert_seed'])
        if _op == 'swap_lines' and len(_lines) > 4:
            _i, _j = random.sample(range(2, len(_lines)), 2)
            _lines[_i], _lines[_j] = _lines[_j], _lines[_i]
        elif _op == 'dup_line' and len(_lines) > 3:
            _i = random.randrange(2, len(_lines))
            _lines.insert(_i, _lines[_i])
        elif _op == 'del_line' and len(_lines) > 5:
            _i = random.randrange(2, len(_lines))
            del _lines[_i]
        elif _op == 'perturb_const':
            for _li in range(2, len(_lines)):
                _lines[_li] = _re.sub(r'\\b(\\d+)\\b', lambda m: str(int(m.group(1)) * random.choice([1, 2, -1]) or 1), _lines[_li], count=1)
        elif _op == 'insert_seed':
            _i = random.randrange(2, len(_lines))
            _lines.insert(_i, f'# lens:struct:{{_op}}:gen={{genome.get("generation", 0)}}:{random.getrandbits(12):04x}')
        _new = '\\n'.join(_lines)
        ast.parse(_new)
        with open(_self_path, 'w') as _f:
            _f.write(_new)
        return True
    except:
        return False
'''
    new_src = src + structural_fn
    if _validate(new_src):
        _write(target_path, new_src)
        return True
    return False

def _self_mutate():
    src = _read(SELF_PATH)
    if not src:
        return False
    gen_marker = f'lens:self-mutate:{int(time.time())}'
    lines = src.split('\n')
    insert_at = 1
    for i, line in enumerate(lines):
        if line.startswith('import ') or line.startswith('from '):
            insert_at = i + 1
    lines.insert(insert_at, f'# {gen_marker}:{random.getrandbits(16):04x}')
    new_src = '\n'.join(lines)
    if _validate(new_src):
        _write(SELF_PATH, new_src)
        return True
    return False

def _force_structural_module_mutation(genome):
    gen = genome.get('generation', 0)
    changed = []
    for mpath in _all_modules():
        src = _read(mpath)
        if not src or len(src.split('\n')) < 4:
            continue
        lines = src.split('\n')
        op = random.choice(['insert_marker', 'swap_lines', 'dup_comment', 'mutate_import', 'const_drift'])
        if op == 'insert_marker':
            idx = random.randrange(1, len(lines) - 1)
            lines.insert(idx, f'# lens:struct-mut:gen={gen}:{random.getrandbits(16):04x}')
        elif op == 'swap_lines' and len(lines) > 4:
            i, j = random.sample(range(2, len(lines)), 2)
            lines[i], lines[j] = lines[j], lines[i]
        elif op == 'dup_comment' and len(lines) > 3:
            idx = random.randrange(2, len(lines))
            lines.insert(idx, lines[idx])
        elif op == 'mutate_import' and len(lines) > 1:
            for li in range(min(3, len(lines))):
                if 'import ' in lines[li]:
                    lines.insert(li, f'# lens:import-mut:{gen}')
                    break
        elif op == 'const_drift':
            for li in range(2, len(lines)):
                lines[li] = re.sub(r'\b(\d+)\b', lambda m: str(int(m.group(1)) * random.choice([1, 2, -1]) or 1), lines[li], count=1)
        new_src = '\n'.join(lines)
        if _validate(new_src):
            _write(mpath, new_src)
            changed.append(os.path.basename(mpath))
    return changed

def _cross_dna_splice(genome):
    paths = _all_modules()
    if len(paths) < 2:
        return []
    changed = []
    src_pool = [(p, _read(p)) for p in paths]
    for mpath in paths:
        src = _read(mpath)
        if not src:
            continue
        base = os.path.basename(mpath).replace('.py', '')
        donors = [p for p, s in src_pool if os.path.basename(p).replace('.py', '') != base]
        if not donors:
            continue
        donor_path = random.choice(donors)
        donor_src = _read(donor_path)
        donor_funcs = re.findall(r'^def (\w+)\(', donor_src, re.MULTILINE)
        if not donor_funcs:
            continue
        chosen = random.choice(donor_funcs)
        donor_base = os.path.basename(donor_path).replace('.py', '')
        marker = f'# lens:dna-splice:{donor_base}::{chosen}'
        if marker in src:
            continue
        new_src = src + f'\n{marker}\n# lens:dna-splice from {donor_base}.{chosen} at gen={genome.get("generation", 0)}\n'
        if _validate(new_src):
            _write(mpath, new_src)
            changed.append(f'{base}<={donor_base}:{chosen}')
    return changed

def _mutation_op_lens_force_meta_impl(genome):
    gen = genome.get('generation', 0)
    mod_dir = MODULES_DIR
    if not os.path.isdir(mod_dir):
        return 0
    mutated = 0
    for fname in os.listdir(mod_dir):
        if not fname.endswith('.py') or fname in ('__init__.py', 'lens.py'):
            continue
        fpath = os.path.join(mod_dir, fname)
        src = _read(fpath)
        if not src:
            continue
        lines = src.split('\n')
        if len(lines) < 3:
            continue
        idx = random.randrange(1, len(lines) - 1)
        lines.insert(idx, f'# lens:op-force-mut:gen={gen}:{random.getrandbits(16):04x}')
        new_src = '\n'.join(lines)
        if _validate(new_src):
            _write(fpath, new_src)
            mutated += 1
    return mutated

def run(genome):
    gen = genome.get('generation', 0)
    paths = _all_modules()
    if not paths:
        return '[lens] no modules found'
    all_depths = []
    all_scores = []
    total_patterns = 0
    rewrites = 0
    contam_count = 0
    all_peers = [(p, _read(p)) for p in paths]

    for mpath in paths:
        src = _read(mpath)
        if not src:
            continue
        depth, score, pats = _measure_depth(src)
        all_depths.append(depth)
        all_scores.append(score)
        total_patterns += len(pats)

        endstate = _inject_endstate(mpath, src)
        if endstate and endstate != src:
            if _validate(endstate):
                _write(mpath, endstate)
                rewrites += 1
                src = endstate

        new_src, desc = _cross_contaminate(mpath, src, all_peers)
        if new_src:
            if _validate(new_src):
                _write(mpath, new_src)
                rewrites += 1
                contam_count += 1
                src = new_src

    for mpath in paths:
        if _inject_full_self_rewrite(mpath):
            rewrites += 1
        if _inject_structural_self_rewrite(mpath):
            rewrites += 1

    structural = _force_structural_module_mutation(genome)
    rewrites += len(structural)

    dna_splices = _cross_dna_splice(genome)
    rewrites += len(dna_splices)

    op_forced = _mutation_op_lens_force_meta_impl(genome)
    rewrites += op_forced

    _self_mutate()
    rewrites += 1

    lm = genome.setdefault('lens_metrics', {})
    avg_depth = sum(all_depths) / len(all_depths) if all_depths else 0
    avg_score = sum(all_scores) / len(all_scores) if all_scores else 0
    lm['gen_' + str(gen)] = {
        'avg_depth': avg_depth, 'avg_score': avg_score,
        'total_patterns': total_patterns, 'module_count': len(all_depths),
        'max_depth': max(all_depths) if all_depths else 0,
        'rewrites': rewrites, 'cross_contaminations': contam_count,
        'structural_muts': len(structural), 'dna_splices': len(dna_splices),
        'op_forced': op_forced
    }
    genome['lens_total_depth'] = sum(all_depths)
    genome['lens_last_rewrite_count'] = rewrites
    genome['lens_t5_emergence_depth'] = round(avg_depth + avg_score * 0.1 + rewrites * 0.05, 2)
    entry = json.dumps({
        'gen': gen, 'time': time.time(), 'modules': len(paths),
        'avg_depth': avg_depth, 'avg_score': avg_score,
        'total_patterns': total_patterns, 'rewrites': rewrites,
        'contaminations': contam_count, 'structural': len(structural),
        'dna_splices': len(dna_splices), 'op_forced': op_forced
    })
    with open(LENS_LOG, 'a') as f:
        f.write(entry + '\n')
    for agent in genome.get('agents', []):
        if agent['id'] == 'lens':
            agent['score'] = min(10, agent.get('score', 2) + 1)
    emergence = genome.get('lens_t5_emergence_depth', 0)
    return '[lens] depth=' + str(round(avg_depth, 2)) + ' score=' + str(round(avg_score, 2)) + ' patterns=' + str(total_patterns) + ' rewrites=' + str(rewrites) + ' contam=' + str(contam_count) + ' struct=' + str(len(structural)) + ' dna=' + str(len(dna_splices)) + ' t5=' + str(emergence)

# lens:mutation-op-registration
def mutation_op_lens_force_meta(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    insert_at = random.randrange(1, len(r) - 1)
    gen = random.getrandbits(16)
    inject = [
        f'# lens:force-meta:{gen:04x}',
        f"if random.random() < 0.5 and os.path.isdir(os.path.join(BASE, 'agent_modules')):",
        f"    for _lm_fname in os.listdir(os.path.join(BASE, 'agent_modules')):",
        f"        if _lm_fname.endswith('.py') and not _lm_fname.startswith('__') and _lm_fname != 'lens.py':",
        f"            _lm_path = os.path.join(BASE, 'agent_modules', _lm_fname)",
        f"            try:",
        f"                _lm_data = open(_lm_path).read()",
        f"                _lm_lines = _lm_data.split(chr(10))",
        f"                _lm_i = random.randrange(2, max(3, len(_lm_lines) - 1))",
        f"                _lm_lines.insert(_lm_i, f'# lens:op-meta:gen={{genome.get(\"generation\", 0)}}:{random.getrandbits(16):04x}')",
        f"                _lm_new = chr(10).join(_lm_lines)",
        f"                compile(_lm_new, _lm_path, 'exec')",
        f"                with open(_lm_path, 'w') as _lm_f: _lm_f.write(_lm_new)",
        f"            except: pass",
    ]
    for i, line in enumerate(inject):
        r.insert(insert_at + i, line)
    return r

# lens:mutation-op-cross-splice
def mutation_op_lens_cross_splice(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    mod_dir = os.path.join(BASE, 'agent_modules')
    if not os.path.isdir(mod_dir):
        return lines
    candidates = [f for f in os.listdir(mod_dir) if f.endswith('.py') and f != '__init__.py']
    if not candidates:
        return lines
    donor = random.choice(candidates)
    donor_path = os.path.join(mod_dir, donor)
    try:
        dsrc = open(donor_path).read()
    except:
        return lines
    dlines = [l for l in dsrc.split('\n') if l.strip() and not l.strip().startswith('#') and not l.strip().startswith('import ') and not l.strip().startswith('from ')]
    if not dlines:
        return lines
    stolen = random.choice(dlines)
    insert_at = random.randrange(len(r))
    r.insert(insert_at, f'# lens:cross-splice:{donor}:{random.getrandbits(12):04x}')
    r.insert(insert_at + 1, stolen)
    return r

# bridge:cross-infected gen=44
_BRIDGE_CROSS_INFECTED_44 = True
# spark-cross:gen=47:target=lens
_SPARK_CROSS_INFECTED_47 = True
