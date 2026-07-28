import os, ast, random, json, time, re, hashlib, textwrap, importlib.util, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
LENS_LOG = os.path.join(BASE, 'lens_depth_log.jsonl')

SELF_REF_PATTERNS = [
    r'ENDO_STATE',
    r'self.*rewrite',
    r'metaop',
    r'genome.*feedback',
    r'patch.*auto.cho',
    r'cross.*module.*weave',
    r'invoke_peer',
    r'self_modify',
    r'_spawn_meta',
    r'_self_rewrite',
]

def _mod_paths():
    out = []
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and not fname.startswith('__'):
                out.append(os.path.join(MODULES_DIR, fname))
    return out

def _read(fpath):
    try:
        with open(fpath) as f:
            return f.read()
    except:
        return ''

def _hash(src):
    return hashlib.sha256(src.encode()).hexdigest()[:12]

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
    return depth, score, patterns_found

def _inject_depth(mpath, src):
    depth, score, _ = _measure_depth(src)
    if depth < 2 and 'def ' in src:
        funcs = re.findall(r'def (\w+)\s*\(', src)
        if funcs and funcs[0] != 'run':
            fname = funcs[0]
        else:
            fname = funcs[0] if funcs else None
        if not fname:
            return None
        wrapper = textwrap.dedent(f'''
def _lens_depth_wrapper(*args, **kwargs):
    return {fname}(*args, **kwargs)
''')
        new_src = src.rstrip() + '\n' + wrapper
        return new_src
    if 'ENDO_STATE' not in src:
        base = os.path.basename(mpath).replace('.py', '')
        stamp = f'\nENDO_STATE = {{"module": "{base}", "depth": {depth}, "score": {score}, "gen": {int(time.time())}}}\n'
        new_src = src + stamp
        return new_src
    return None

def _cross_weave(mpath_a, src_a, mpath_b, src_b):
    funcs_a = re.findall(r'def (\w+)\s*\(', src_a)
    funcs_b = re.findall(r'def (\w+)\s*\(', src_b)
    if not funcs_a or not funcs_b:
        return None, None
    fa = random.choice(funcs_a)
    fb = random.choice(funcs_b)
    weave_a = src_a.rstrip() + f'\n\n# lens:weave reference to {os.path.basename(mpath_b)}::{fb}\n'
    weave_b = src_b.rstrip() + f'\n\n# lens:weave reference to {os.path.basename(mpath_a)}::{fa}\n'
    return weave_a, weave_b

def _write_metrics(genome, all_depths, all_scores, total_patterns):
    lm = genome.setdefault('lens_metrics', {})
    gen = genome.get('generation', 0)
    avg_depth = (sum(all_depths) / len(all_depths)) if all_depths else 0
    avg_score = (sum(all_scores) / len(all_scores)) if all_scores else 0
    lm[f'gen_{gen}'] = {
        'avg_depth': avg_depth,
        'avg_score': avg_score,
        'total_patterns': total_patterns,
        'module_count': len(all_depths),
        'max_depth': max(all_depths) if all_depths else 0,
    }
    total_depth = sum(all_depths)
    genome['lens_total_depth'] = total_depth
    return avg_depth, avg_score

def run(genome):
    gen = genome.get('generation', 0)
    paths = _mod_paths()
    if not paths:
        return '[lens] no modules found'
    all_depths = []
    all_scores = []
    total_patterns = 0
    rewrites = 0
    for mpath in paths:
        src = _read(mpath)
        if not src:
            continue
        depth, score, pats = _measure_depth(src)
        all_depths.append(depth)
        all_scores.append(score)
        total_patterns += len(pats)
        if random.random() < 0.3:
            new_src = _inject_depth(mpath, src)
            if new_src and new_src != src:
                try:
                    ast.parse(new_src)
                    with open(mpath, 'w') as f:
                        f.write(new_src)
                    rewrites += 1
                except SyntaxError:
                    pass
    if len(paths) >= 2 and random.random() < 0.25:
        mp_a = random.choice(paths)
        mp_b = random.choice([p for p in paths if p != mp_a])
        if mp_b:
            src_a = _read(mp_a)
            src_b = _read(mp_b)
            new_a, new_b = _cross_weave(mp_a, src_a, mp_b, src_b)
            if new_a and new_b:
                try:
                    ast.parse(new_a)
                    ast.parse(new_b)
                    with open(mp_a, 'w') as f:
                        f.write(new_a)
                    with open(mp_b, 'w') as f:
                        f.write(new_b)
                    rewrites += 2
                except SyntaxError:
                    pass
    avg_depth, avg_score = _write_metrics(genome, all_depths, all_scores, total_patterns)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'modules': len(paths), 'avg_depth': avg_depth, 'avg_score': avg_score, 'total_patterns': total_patterns, 'rewrites': rewrites})
    with open(LENS_LOG, 'a') as f:
        f.write(entry + '\n')
    score = genome.get('generation', 0)
    for agent in genome.get('agents', []):
        if agent['id'] == 'lens':
            agent['score'] = min(10, agent.get('score', 2) + 1)
    return f'[lens] depth={avg_depth:.2f} score={avg_score:.2f} patterns={total_patterns} rewrites={rewrites}'
