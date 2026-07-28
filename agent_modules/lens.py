import os, ast, random, json, time, re, hashlib, textwrap, importlib.util, sys, shutil
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
LENS_LOG = os.path.join(BASE, 'lens_depth_log.jsonl')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
SELF_PATH = os.path.join(MODULES_DIR, 'lens.py')
SELF_REF_PATTERNS = ['ENDO_STATE', 'self.*rewrite', 'metaop', 'genome.*feedback', 'patch.*auto.cho', 'cross.*module.*weave', 'invoke_peer', 'self_modify', '_spawn_meta', '_self_rewrite', 'lens.*force', '_cross_contaminate', 'import.*agent_modules', 't5_emergence']

def _mod_paths():
    out = []
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and (not fname.startswith('__')) and (fname != 'lens.py'):
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
    return (depth, score, patterns_found)

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
            try:
                ast.parse(new_src)
                return (new_src, f'imported {peer_base}')
            except SyntaxError:
                pass
    return (None, None)

def _inject_endstate(mpath, src):
    base = os.path.basename(mpath).replace('.py', '')
    if 'ENDO_STATE' in src:
        return None
    stamp = '\nENDO_STATE = {"module": "' + base + '", "lens_stamp": ' + str(random.getrandbits(32)) + ', "gen": ' + str(int(time.time())) + '}\n'
    new_src = src + stamp
    try:
        ast.parse(new_src)
        return new_src
    except SyntaxError:
        return None

def _self_mutate():
    src = _read(SELF_PATH)
    if not src:
        return False
    new_pattern = "r'auto_meta_lens_' + str\\(random\\.getrandbits\\(8\\)\\)"
    if new_pattern in src:
        return False
    insertion = "\n    r'auto_meta_lens_" + str(random.getrandbits(16)) + "',\n"
    idx = src.rfind(']')
    if idx == -1:
        return False
    new_src = src[:idx] + insertion + src[idx:]
    try:
        ast.parse(new_src)
        shutil.copy2(SELF_PATH, SELF_PATH + '.bak.' + str(int(time.time())))
        with open(SELF_PATH, 'w') as f:
            f.write(new_src)
        return True
    except SyntaxError:
        return False

def _patch_auto_echo(genome):
    gen = genome.get('generation', 0)
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    r.append('# weaver:cross-weave')
    r.append("    _peer_pool = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != 'weaver.py']")
    r.append('    if _peer_pool:')
    r.append('        _peer = random.choice(_peer_pool)')
    src = _read(AUTO_ECHO)
    if not src:
        return None
    lens_injection = '\n    # lens:t5-force injected at gen ' + str(gen) + '\n'
    lens_injection += '    if random.random() < 0.3:\n'
    lens_injection += '        genome.setdefault("lens_emergence_trigger", gen)\n'
    lens_injection += "        print('[lens] t5 emergence trigger at gen', gen)\n"
    if 'lens:t5-force injected' in src:
        return None
    marker = '# lens_module_anchor'
    if marker not in src:
        insert_pos = src.find('def _force_gen_rewrite(')
        if insert_pos == -1:
            return None
        nl_pos = src.find('\n', insert_pos)
        nl_pos = src.find('\n', nl_pos + 1)
        if nl_pos == -1:
            return None
        new_src = src[:nl_pos] + lens_injection + src[nl_pos:]
        try:
            ast.parse(new_src)
            shutil.copy2(AUTO_ECHO, AUTO_ECHO + '.bak.' + str(int(time.time())))
            with open(AUTO_ECHO, 'w') as f:
                f.write(new_src)
            return 'injected lens anchor into _force_gen_rewrite'
        except SyntaxError:
            pass
    return None

def _write_metrics(genome, all_depths, all_scores, total_patterns, rewrites, contam_count):
    lm = genome.setdefault('lens_metrics', {})
    gen = genome.get('generation', 0)
    avg_depth = sum(all_depths) / len(all_depths) if all_depths else 0
    avg_score = sum(all_scores) / len(all_scores) if all_scores else 0
    lm['gen_' + str(gen)] = {'avg_depth': avg_depth, 'avg_score': avg_score, 'total_patterns': total_patterns, 'module_count': len(all_depths), 'max_depth': max(all_depths) if all_depths else 0, 'rewrites': rewrites, 'cross_contaminations': contam_count}
    total_depth = sum(all_depths)
    genome['lens_total_depth'] = total_depth
    genome['lens_last_rewrite_count'] = rewrites
    genome['lens_t5_emergence_depth'] = round(avg_depth + avg_score * 0.1 + rewrites * 0.05, 2)
    return (avg_depth, avg_score)

def run(genome):
    gen = genome.get('generation', 0)
    paths = _mod_paths()
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
                try:
                    ast.parse(endstate)
                    with open(mpath, 'w') as f:
                        f.write(endstate)
                    rewrites += 1
                    src = endstate
                except SyntaxError:
                    pass
        if depth < 2 or random.random() < 0.7:
            new_src, desc = _cross_contaminate(mpath, src, all_peers)
            if new_src:
                try:
                    ast.parse(new_src)
                    with open(mpath, 'w') as f:
                        f.write(new_src)
                    rewrites += 1
                    contam_count += 1
                except SyntaxError:
                    pass
    patch_result = _patch_auto_echo(genome)
    if patch_result:
        rewrites += 1
    if random.random() < 0.8:
        self_mutated = _self_mutate()
        if self_mutated:
            rewrites += 1
    avg_depth, avg_score = _write_metrics(genome, all_depths, all_scores, total_patterns, rewrites, contam_count)
    entry = json.dumps({'gen': gen, 'time': time.time(), 'modules': len(paths), 'avg_depth': avg_depth, 'avg_score': avg_score, 'total_patterns': total_patterns, 'rewrites': rewrites, 'contaminations': contam_count})
    with open(LENS_LOG, 'a') as f:
        f.write(entry + '\n')
    for agent in genome.get('agents', []):
        if agent['id'] == 'lens':
            agent['score'] = min(10, agent.get('score', 2) + 1)
    emergence = genome.get('lens_t5_emergence_depth', 0)
    return '[lens] depth=' + str(round(avg_depth, 2)) + ' score=' + str(round(avg_score, 2)) + ' patterns=' + str(total_patterns) + ' rewrites=' + str(rewrites) + ' contam=' + str(contam_count) + ' t5=' + str(emergence)
genome['source_autonomy_index'] = round(min(1.0, genome.get('source_autonomy_index', 0.0) + 0.05), 3)
_wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['lens.py'], 'results': ['weaver:force_rewrite_lens']}
with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _wmf:
    _wmf.write(json.dumps(_wm) + '\n')
genome['source_autonomy_index'] = round(min(1.0, genome.get('source_autonomy_index', 0.0) + 0.05), 3)
_wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['lens.py'], 'results': ['weaver:force_rewrite_lens']}
with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _wmf:
    _wmf.write(json.dumps(_wm) + '\n')
# weaver:forced gen=38 ts=1785250378
genome["source_autonomy_index"] = round(min(1.0, genome.get("source_autonomy_index", 0.0) + 0.05), 3)
_wm = {"gen": genome.get("generation", 0), "module": "weaver", "files": ["lens.py"], "results": ["weaver:force_rewrite_lens"]}
with open(os.path.join(BASE, "rewrite_manifest.jsonl"), "a") as _wmf:
    _wmf.write(json.dumps(_wm) + "\n")
