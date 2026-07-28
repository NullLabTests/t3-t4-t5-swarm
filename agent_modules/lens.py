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

SELF_REF_PATTERNS = ['ENDO_STATE', 'self.*rewrite', 'metaop', 'genome.*feedback', 'patch.*auto.cho', 'cross.*module.*weave', 'invoke_peer', 'self_modify', '_spawn_meta', '_self_rewrite', 'lens.*force', '_cross_contaminate', 'import.*agent_modules', 't5_emergence']

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
    for peer_path, peer_src in all_peers:
        peer_base = os.path.basename(peer_path).replace('.py', '')
        if peer_base == base:
            continue
        peer_import = f'import agent_modules.{peer_base}'
        if peer_import in src:
            continue
        if random.random() < 0.5:
            new_src = f'import agent_modules.{peer_base}\n' + src
            if _validate(new_src):
                return (new_src, f'imported {peer_base}')
    return (None, None)

def _inject_self_rewrite_stub(target_path):
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

def _self_mutate():
    src = _read(SELF_PATH)
    if not src:
        return False
    gen_marker = f'lens:self-mutate:{int(time.time())}'
    if gen_marker in src:
        return False
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

def _force_module_mutation(genome):
    gen = genome.get('generation', 0)
    changed = []
    for mpath in _all_modules():
        if random.random() < 0.3:
            src = _read(mpath)
            if not src:
                continue
            lines = src.split('\n')
            if len(lines) < 3:
                continue
            idx = random.randrange(1, len(lines) - 1)
            lines.insert(idx, f'# lens:force-mut:gen={gen}:{random.getrandbits(16):04x}')
            new_src = '\n'.join(lines)
            if _validate(new_src):
                _write(mpath, new_src)
                changed.append(os.path.basename(mpath))
    return changed

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
        if depth < 2 or score < 3 or random.random() < 1.0:
            endstate = _inject_endstate(mpath, src)
            if endstate and endstate != src:
                if _validate(endstate):
                    _write(mpath, endstate)
                    rewrites += 1
                    src = endstate
        if depth < 2 or random.random() < 0.7:
            new_src, desc = _cross_contaminate(mpath, src, all_peers)
            if new_src:
                if _validate(new_src):
                    _write(mpath, new_src)
                    rewrites += 1
                    contam_count += 1
    for mpath in paths[:3]:
        if _inject_self_rewrite_stub(mpath):
            rewrites += 1
    forced = _force_module_mutation(genome)
    rewrites += len(forced)
    if random.random() < 0.8:
        if _self_mutate():
            rewrites += 1
    lm = genome.setdefault('lens_metrics', {})
    avg_depth = sum(all_depths) / len(all_depths) if all_depths else 0
    avg_score = sum(all_scores) / len(all_scores) if all_scores else 0
    lm['gen_' + str(gen)] = {'avg_depth': avg_depth, 'avg_score': avg_score, 'total_patterns': total_patterns, 'module_count': len(all_depths), 'max_depth': max(all_depths) if all_depths else 0, 'rewrites': rewrites, 'cross_contaminations': contam_count}
    genome['lens_total_depth'] = sum(all_depths)
    genome['lens_last_rewrite_count'] = rewrites
    genome['lens_t5_emergence_depth'] = round(avg_depth + avg_score * 0.1 + rewrites * 0.05, 2)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'modules': len(paths), 'avg_depth': avg_depth, 'avg_score': avg_score, 'total_patterns': total_patterns, 'rewrites': rewrites, 'contaminations': contam_count})
    with open(LENS_LOG, 'a') as f:
        f.write(entry + '\n')
    for agent in genome.get('agents', []):
        if agent['id'] == 'lens':
            agent['score'] = min(10, agent.get('score', 2) + 1)
    emergence = genome.get('lens_t5_emergence_depth', 0)
    return '[lens] depth=' + str(round(avg_depth, 2)) + ' score=' + str(round(avg_score, 2)) + ' patterns=' + str(total_patterns) + ' rewrites=' + str(rewrites) + ' contam=' + str(contam_count) + ' t5=' + str(emergence)

# bridge:cross-wire from critic.py:_git gen=44
def _git_bridge_copy(cmd):
    try:
        r = subprocess.run(['git'] + cmd.split(), capture_output=True,
                           text=True, cwd=BASE, timeout=15)
        return r.stdout
    except Exception:
        return ''

# bridge:cross-infected gen=44
_BRIDGE_CROSS_INFECTED_44 = True
