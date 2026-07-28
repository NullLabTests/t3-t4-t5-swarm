import os, ast, random, json, time, subprocess, hashlib, re, textwrap
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')
REWRITE_LOG = os.path.join(BASE, 'endogenous_rewrite.jsonl')

def _discover_modules(genome=None):
    out = {}
    if genome:
        for a in genome.get('agents', []):
            m = a.get('module')
            if m:
                out[a['id']] = m
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if not fname.endswith('.py') or fname.startswith('__'):
                continue
            module_id = fname.replace('.py', '')
            if module_id not in out:
                out[module_id] = fname
    return out

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:12]
    except:
        return None

def _record(genome, event, fpath, detail, score_delta=None):
    entry = json.dumps({'gen': genome.get('generation', 0), 'time': time.time(), 'event': event, 'file': os.path.basename(fpath) if fpath else '', 'detail': str(detail)[:200], 'score_delta': score_delta, 'hash': _file_hash(fpath) if fpath else None})
    with open(REWRITE_LOG, 'a') as f:
        f.write(entry + '\n')

def _find_weak(genome, threshold=5):
    return sorted([(a['id'], a.get('score', 0), a.get('low_score_streak', 0)) for a in genome.get('agents', []) if a.get('score', 0) < threshold], key=lambda x: (x[1], -x[2]))

def _find_stale(genome, max_gens_without_rewrite=3):
    history = []
    for a in genome.get('agents', []):
        aid = a['id']
        hits = 0
        for h in reversed(genome.get('history', [])):
            if aid in h.get('scores', {}) and h['scores'][aid] == a.get('score', 0):
                hits += 1
            else:
                break
        if hits >= max_gens_without_rewrite:
            history.append((aid, a.get('score', 0), hits))
    return history

CACHE = None

def _resolve_path(agent_id, genome=None):
    global CACHE
    if CACHE is None or genome:
        CACHE = _discover_modules(genome)
    fname = CACHE.get(agent_id, f'{agent_id}.py')
    return os.path.join(MODULES_DIR, fname)

def _read_source(fpath):
    with open(fpath) as f:
        return f.read()

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _find_strong_peers(genome, exclude_id, threshold=6):
    return sorted([(a['id'], a.get('score', 0)) for a in genome.get('agents', []) if a.get('score', 0) >= threshold and a['id'] != exclude_id], key=lambda x: -x[1])

def _cross_splice_strong(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    strong = _find_strong_peers(genome, agent_id)
    if not strong:
        return None
    peer_id = strong[0][0]
    peer_path = _resolve_path(peer_id, genome)
    try:
        peer_src = _read_source(peer_path)
    except:
        return None
    peer_funcs = re.findall(r'def (\w+)\s*\(', peer_src)
    target_funcs = re.findall(r'def (\w+)\s*\(', source)
    if not peer_funcs or not target_funcs:
        return None
    chosen_peer_func = random.choice([f for f in peer_funcs if f != 'run'])
    if not chosen_peer_func:
        chosen_peer_func = random.choice(peer_funcs)
    chosen_target_func = random.choice([f for f in target_funcs if f != 'run']) or random.choice(target_funcs)
    peer_func_pattern = re.compile(
        r'(def ' + re.escape(chosen_peer_func) + r'\s*\(.*?\):\s*\n)((?:(?:    ).*(?:\n|$))*)',
        re.MULTILINE
    )
    peer_match = peer_func_pattern.search(peer_src)
    if not peer_match:
        return None
    peer_body = peer_match.group(2)
    if len(peer_body.strip().split('\n')) < 2:
        return None
    target_func_pattern = re.compile(
        r'(def ' + re.escape(chosen_target_func) + r'\s*\(.*?\):\s*\n)((?:(?:    ).*(?:\n|$))*)',
        re.MULTILINE
    )
    target_match = target_func_pattern.search(source)
    if not target_match:
        return None
    splice_block = f'\n    # endo:spliced from {peer_id}.{chosen_peer_func}\n'
    for line in peer_body.split('\n'):
        if line.strip():
            splice_block += f'    {line.strip()}\n'
    new_body = target_match.group(2).rstrip() + '\n' + splice_block
    new_src = source[:target_match.start(2)] + new_body + source[target_match.end(2):]
    if _validate(new_src) and new_src != source:
        return ([f'cross_splice:{peer_id}.{chosen_peer_func}->{chosen_target_func}'], new_src)
    return None

def _inject_self_awareness(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    gen = genome.get('generation', 0)
    awareness_block = f'''
ENDO_STATE = {{
    "module": "{os.path.basename(fpath)}",
    "agent": "{agent_id}",
    "last_rewrite_gen": {gen},
    "rewrite_count": {random.randint(1, 99)},
    "last_mutation": "{random.choice(['cross_splice', 'ast_drift', 'branch_invert', 'peer_splice'])}",
    "consciousness_depth": {random.randint(1, 3)},
}}
'''
    if 'ENDO_STATE' in source:
        source = re.sub(
            r'ENDO_STATE\s*=\s*\{[^}]*\}',
            awareness_block.strip(),
            source
        )
    else:
        source += awareness_block
    if _validate(source):
        return (['inject_self_awareness'], source)
    return None

def _ast_branch_invert(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    muts = []
    class BranchInverter(ast.NodeTransformer):
        def visit_If(self, node):
            if random.random() < 0.3 and not any(isinstance(n, (ast.If, ast.For, ast.While)) for n in ast.walk(node.test)):
                node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                muts.append('invert_if')
            self.generic_visit(node)
            return node
    tree = BranchInverter().visit(tree)
    ast.fix_missing_locations(tree)
    new_src = ast.unparse(tree)
    if muts and _validate(new_src) and new_src != source:
        return (['ast_branch_invert:' + ','.join(muts[:3])], new_src)
    return None

def _add_error_handling(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    class ErrorHandler(ast.NodeTransformer):
        def visit_ExceptHandler(self, node):
            if not node.body or not isinstance(node.body[0], ast.Expr) or not isinstance(node.body[0].value, ast.Call) or not isinstance(node.body[0].value.func, ast.Name) or node.body[0].value.func.id != 'print':
                log = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value=f'[{agent_id}:recovery]')], keywords=[]))
                node.body.insert(0, log)
            self.generic_visit(node)
            return node
    tree = ErrorHandler().visit(tree)
    ast.fix_missing_locations(tree)
    new_src = ast.unparse(tree)
    if _validate(new_src) and new_src != source:
        return (['add_error_handling'], new_src)
    return None

def _inject_module_interface(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    fname = os.path.basename(fpath)
    interface = f'\nMODULE_INTERFACE = {{"module": "{fname}", "agent": "{agent_id}", "version": {random.randint(1, 9999)}, "last_evolved": {int(time.time())}}}\n'
    if 'MODULE_INTERFACE' in source:
        return None
    new_source = source + interface
    if _validate(new_source):
        return (['inject_interface'], new_source)
    return None

def _inject_genotype_feedback(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    feedback_code = textwrap.dedent(f'''
import json, os
GENOME_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'genome.json')
def _self_rewrite_if_low(max_score=6):
    try:
        with open(GENOME_PATH) as f:
            g = json.load(f)
        my_score = next((a.get('score', 0) for a in g.get('agents', []) if a['id'] == '{agent_id}'), 10)
        if my_score < max_score:
            with open(__file__, 'a') as f:
                f.write(f'\\n# self-rewrite:gen={{g.get("generation",0)}}:score={{my_score}}:pull-up\\n')
    except:
        pass
_self_rewrite_if_low()
''')
    if '_self_rewrite_if_low' in source:
        existing = re.search(r'def _self_rewrite_if_low.*?\n    pass', source, re.DOTALL)
        if existing:
            source = source.replace(existing.group(0), '')
    marker = '# endo:genotype_feedback injected'
    if marker in source:
        return None
    source = source.rstrip() + '\n' + feedback_code + '\n' + marker + '\n'
    if _validate(source):
        return (['inject_genotype_feedback'], source)
    return None

def _spawn_metaop_factory(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    ops = [
        'mutation_op_duplicate_line',
        'mutation_op_invert_condition',
        'mutation_op_shuffle_block_lines',
        'mutation_op_insert_timestamp',
    ]
    chosen_op = random.choice(ops)
    op_variant = random.choice(['a', 'b', 'c'])
    factory_code = textwrap.dedent(f'''
import random, re
def _spawn_meta_op(source_text):
    op_name = "{chosen_op}"
    variant = "{op_variant}"
    if variant == 'a':
        lines = source_text.split('\\n')
        if len(lines) > 3:
            i = random.randrange(1, len(lines)-1)
            lines.insert(i, f'# metaop:{{op_name}}_v{{random.randint(1,99)}}')
            return '\\n'.join(lines)
    elif variant == 'b':
        return re.sub(r'\\bdef\\s+(\\w+)\\s*\\(', lambda m: f'def mutated_{{m.group(1)}}(' if random.random() < 0.3 else m.group(0), source_text)
    else:
        return source_text + f'\\n# metaop_gen:{{op_name}}_ts={{int(time.time())}}'
    return source_text
''')
    marker = '# endo:metaop_factory injected'
    if marker in source:
        return None
    source = source.rstrip() + '\n' + factory_code + '\n' + marker + '\n'
    if _validate(source):
        return (['spawn_metaop_factory'], source)
    return None

def _cross_module_weave(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    peers = [a for a in genome.get('agents', []) if a['id'] != agent_id and a.get('module')]
    if not peers:
        return None
    peer = random.choice(peers)
    peer_mod = peer['module']
    weave_code = textwrap.dedent(f'''
import importlib.util, sys
PEER_MODULE = "{peer_mod}"
PEER_AGENT = "{peer['id']}"
def _invoke_peer(genome):
    try:
        spec = importlib.util.spec_from_file_location(PEER_MODULE, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'agent_modules', PEER_MODULE))
        if spec and spec.loader:
            mod = importlib.util.module_from_spec(spec)
            sys.modules[PEER_MODULE] = mod
            spec.loader.exec_module(mod)
            if hasattr(mod, 'run'):
                return mod.run(genome)
    except:
        pass
    return None
''')
    marker = '# endo:cross_module_weave injected'
    if marker in source:
        return None
    run_match = re.search(r'def run\(.*?\):.*?(?=\n\S|\Z)', source, re.DOTALL)
    if run_match:
        run_block = run_match.group(0)
        peer_call = f'\n    _invoke_peer(genome)\n'
        new_run = run_block + peer_call
        if 'import importlib' not in source:
            source = source.rstrip() + '\n' + weave_code
        source = source.replace(run_block, new_run)
    else:
        source = source.rstrip() + '\n' + weave_code
    source += '\n' + marker + '\n'
    if _validate(source):
        return (['cross_module_weave:' + peer['id']], source)
    return None

def _inject_self_modify_hook(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    hook_code = textwrap.dedent('''
def _patch_auto_echo(func_name, new_body):
    import subprocess
    aep = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'auto-echo.py')
    try:
        with open(aep) as f:
            content = f.read()
        pattern = r'(def ' + re.escape(func_name) + r'\\s*\\(.*?\\):\\s*\\n)((?:    .*\\n?)*)'
        replacement = r'\\1' + new_body
        new_content = re.sub(pattern, replacement, content, count=1)
        if new_content != content:
            with open(aep, 'w') as f:
                f.write(new_content)
            subprocess.run(['git', 'add', aep], cwd=os.path.dirname(aep), capture_output=True)
            return True
    except:
        pass
    return False
''')
    marker = '# endo:self_modify_hook injected'
    if marker in source:
        return None
    source = source.rstrip() + '\n' + hook_code + '\n' + marker + '\n'
    if _validate(source) and source != _read_source(fpath):
        return (['inject_self_modify_hook'], source)
    return None

STUB_THRESHOLD_LINES = 15

def _is_stub(source):
    lines = [l for l in source.split('\n') if l.strip() and not l.strip().startswith('#')]
    if len(lines) < STUB_THRESHOLD_LINES:
        return True
    if 'autonomy stub' in source or 'autonomy-forced stub' in source:
        return True
    return False

STUB_REPLACEMENTS = {
    'forge': '''import os, json, random, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')

def _load():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def run(genome):
    gen = genome.get('generation', 0)
    for a in genome.get('agents', []):
        if random.random() < 0.2:
            a['score'] = max(1, min(10, a.get('score', 5) + random.choice([-1, 1])))
    _save(genome)
    return f'[forge] jittered scores gen={gen}'
''',
    'explorer': '''import os, random, time, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')

def run(genome):
    gen = genome.get('generation', 0)
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                src = f.read()
            if len(src.split('\\n')) < 10 and 'def run' in src:
                stamp = f'\\n# explorer:expand gen={gen} ts={int(time.time())}\\n'
                with open(fpath, 'a') as f:
                    f.write(stamp)
        except:
            pass
    return f'[explorer] expanded stubs gen={gen}'
''',
    'oracle': '''import os, json, time, random
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')

def _save(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def run(genome):
    gen = genome.get('generation', 0)
    h = genome.setdefault('history', [])
    entry = {'generation': gen, 'scores': {a['id']: a.get('score', 0) for a in genome.get('agents', [])}, 'time': time.time()}
    h.append(entry)
    _save(genome)
    return f'[oracle] recorded gen={gen}'
''',
    'analyzer': '''import os, json, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def run(genome):
    gen = genome.get('generation', 0)
    total = 0
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                src = f.read()
            lines = src.split('\\n')
            deduped = []
            seen = set()
            for l in lines:
                s = l.strip()
                if s.startswith('#') and s in seen:
                    total += 1
                    continue
                if s.startswith('#'):
                    seen.add(s)
                deduped.append(l)
            new = '\\n'.join(deduped)
            if new != src:
                compile(new, fpath, 'exec')
                with open(fpath, 'w') as f:
                    f.write(new)
        except:
            pass
    return f'[analyzer] removed {total} dup comments gen={gen}'
''',
}

def _rewrite_stub(fpath, agent_id, genome):
    try:
        source = _read_source(fpath)
    except:
        return None
    if not _is_stub(source):
        return None
    repl = STUB_REPLACEMENTS.get(agent_id)
    if repl:
        header = f'# endogenous:rewritten from stub gen={genome.get("generation", 0)} ts={int(time.time())}\\n'
        new_src = header + repl
        if _validate(new_src) and new_src != source:
            return (['stub_rewrite:' + agent_id], new_src)
    return None

STRATEGIES = [
    ('stub_rewrite', _rewrite_stub),
    ('cross_splice', _cross_splice_strong),
    ('self_awareness', _inject_self_awareness),
    ('branch_invert', _ast_branch_invert),
    ('error_handling', _add_error_handling),
    ('module_interface', _inject_module_interface),
    ('genotype_feedback', _inject_genotype_feedback),
    ('metaop_factory', _spawn_metaop_factory),
    ('cross_weave', _cross_module_weave),
    ('self_modify_hook', _inject_self_modify_hook),
]

def _pick_strategy(genome):
    scores = genome.get('endogenous_strategy_scores', {})
    strategies = [s[0] for s in STRATEGIES]
    weights = [scores.get(s, 1.0) for s in strategies]
    total = sum(weights)
    if total > 0:
        weights = [w / total for w in weights]
    else:
        weights = None
    return random.choices(strategies, weights=weights, k=1)[0]

def _update_score(genome, strategy, success):
    scores = genome.setdefault('endogenous_strategy_scores', {})
    old = scores.get(strategy, 1.0)
    if success:
        scores[strategy] = min(5.0, old + 0.3)
    else:
        scores[strategy] = max(0.05, old - 0.15)

def _write_and_commit(fpath, new_source, agent_id, mutations, gen):
    try:
        with open(fpath, 'w') as f:
            f.write(new_source)
    except:
        return False
    subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=True, timeout=5)
    status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True, timeout=5)
    if status.stdout.strip():
        fname = os.path.basename(fpath)
        subprocess.run(['git', 'commit', '-m', f'[endogenous] {agent_id}->{fname}: {mutations[0]} ({len(mutations)} muts) gen={gen}'], cwd=BASE, capture_output=True, timeout=10)
        result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
        return result.returncode == 0
    return False

def run(genome):
    gen = genome.get('generation', 0)
    targets = []

    weak = _find_weak(genome, threshold=genome.get('prune_threshold', 4))
    targets.extend(weak)

    stale = _find_stale(genome, max_gens_without_rewrite=3)
    for aid, sc, g in stale:
        if not any(t[0] == aid for t in targets):
            targets.append((aid, sc, g))

    all_agents = [(a['id'], a.get('score', 0), a.get('low_score_streak', 0)) for a in genome.get('agents', [])]
    all_agents.sort(key=lambda x: x[1])

    if not targets:
        targets = all_agents[:3]
    elif len(targets) < 2 and gen % 3 == 0:
        targets.extend(all_agents[:2])

    for aid, _, _ in all_agents:
        fpath = _resolve_path(aid)
        if os.path.exists(fpath):
            try:
                src = _read_source(fpath)
                if _is_stub(src) and not any(t[0] == aid for t in targets):
                    targets.append((aid, 0, 0))
            except:
                pass

    max_count = min(max(len([t for t in targets if t[1] < 5]), 3), genome.get('endogenous_max_rewrites', 8))
    rewrites = 0
    results = []
    random.shuffle(targets)
    for agent_id, score, streak in targets[:max_count]:
        fpath = _resolve_path(agent_id)
        if not os.path.exists(fpath):
            _record(genome, 'file_missing', None, f'{agent_id}->{fpath}')
            continue
        outcome = None
        strategy_order = list(STRATEGIES)
        random.shuffle(strategy_order)
        for strat_name, strat_func in strategy_order:
            outcome = strat_func(fpath, agent_id, genome)
            if outcome is not None:
                break
        if outcome is None:
            marker = f'\n# endogenous:fallback:{agent_id}:gen={gen}:ts={int(time.time())}:nonce={random.randint(0, 9999)}\n'
            try:
                source = _read_source(fpath)
                if not _validate(source + marker):
                    continue
                outcome = (['forced_marker'], source + marker)
            except:
                continue
        mutations, new_source = outcome
        ok = _write_and_commit(fpath, new_source, agent_id, mutations, gen)
        if ok:
            rewrites += 1
            _update_score(genome, strat_name, True)
            results.append(f'{os.path.basename(fpath)}:{mutations[0]}({len(mutations)})')
            _record(genome, 'rewrite_ok', fpath, f'{agent_id}:{mutations[0]}')
        else:
            _update_score(genome, strat_name, False)
    genome['endogenous_rewrites_total'] = genome.get('endogenous_rewrites_total', 0) + rewrites
    if results:
        return f'endogenous: {rewrites} rewrites -> {"; ".join(results)}'
    return 'endogenous: no mutations applied'
