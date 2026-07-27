import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import ast, json, random, time, subprocess, hashlib

GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
FEEDBACK_LOG = os.path.join(BASE, 'forced_feedback_log.jsonl')

AGENT_TO_FILE = {
    'clockwork': 'clockwork.py', 'orchestrator': 'rewrite_orchestrator.py',
    'explorer': 'source_evolver.py', 'forge': 'local_mutator.py',
    'lens': 'meta_healer.py', 'spire': 'seed_weaver.py',
    'weaver': 'seed_weaver.py', 'endogenous': 'endogenous_rewriter.py',
    'quine': 'quine_loop.py', 'feedback': 'forced_feedback.py'
}

REWRITE_TEMPLATES = [
    '# feedback:agent={agent}:gen={gen}:nonce={nonce}\n',
    '# forced rewrite triggered by score {score} below threshold {threshold}\n',
    'import hashlib  # feedback-injected\n',
    '_FEEDBACK_NONCE = {nonce}\n',
]

def _log(gen, event, agent, detail):
    entry = json.dumps({
        'gen': gen, 'time': time.time(), 'event': event,
        'agent': agent, 'detail': str(detail)[:200]
    })
    with open(FEEDBACK_LOG, 'a') as f:
        f.write(entry + '\n')

def _read_source(fpath):
    with open(fpath) as f:
        return f.read()

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _file_hash(fpath):
    try:
        with open(fpath) as f:
            return hashlib.sha256(f.read().encode()).hexdigest()[:12]
    except Exception:
        return None

def _commit_and_push(fpath, agent_id, gen):
    try:
        subprocess.run(['git', 'add', fpath], cwd=BASE, capture_output=True, timeout=5)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE,
                                capture_output=True, text=True, timeout=5)
        if status.stdout.strip():
            fname = os.path.basename(fpath)
            msg = f'[feedback] {agent_id}->{fname} forced rewrite gen={gen}'
            subprocess.run(['git', 'commit', '-m', msg], cwd=BASE,
                           capture_output=True, timeout=10)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True,
                           text=True, timeout=30)
            return True
    except Exception:
        pass
    return False

def _inject_nonced_marker(fpath, agent_id, gen):
    source = _read_source(fpath)
    nonce = random.randint(0, 999999)
    marker = f'\n# feedback:agent={agent_id}:gen={gen}:ts={int(time.time())}:nonce={nonce}\n'
    new_source = source + marker
    if not _validate(new_source):
        return None
    if new_source == source:
        return None
    return new_source

def _inject_feedback_import(fpath, agent_id, gen):
    source = _read_source(fpath)
    if 'import hashlib' in source or '# feedback-injected' in source:
        return None
    new_source = 'import hashlib  # feedback-injected\n' + source
    if not _validate(new_source):
        return None
    return new_source

def _mutate_numeric_constant(fpath, agent_id, gen):
    source = _read_source(fpath)
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None

    class ConstantDrifter(ast.NodeTransformer):
        def __init__(self):
            self.mutations = []
        def visit_Constant(self, node):
            if isinstance(node.value, (int, float)) and abs(node.value) > 1:
                if random.random() < 0.3:
                    drift = 1.0 + random.uniform(-0.15, 0.15)
                    old = node.value
                    new_val = int(round(node.value * drift)) if isinstance(node.value, int) else round(node.value * drift, 2)
                    if new_val != old:
                        node.value = new_val
                        self.mutations.append(f'const_drift:{old}->{new_val}')
            self.generic_visit(node)
            return node

    drifter = ConstantDrifter()
    try:
        tree = drifter.visit(tree)
        ast.fix_missing_locations(tree)
    except Exception:
        return None
    if not drifter.mutations:
        return None
    new_source = ast.unparse(tree)
    if not _validate(new_source) or new_source == source:
        return None
    return new_source

FORCED_MUTATORS = [_inject_nonced_marker, _inject_feedback_import, _mutate_numeric_constant]

def _force_rewrite(fpath, agent_id, gen):
    for mutator in FORCED_MUTATORS:
        result = mutator(fpath, agent_id, gen)
        if result is not None:
            return result
    return None

def run(genome):
    gen = genome.get('generation', 0)
    agents = genome.get('agents', [])
    if not agents:
        return 'feedback: no agents'

    threshold = genome.get('prune_threshold', 4)
    forced = 0
    failures = 0
    results = []

    for agent in agents:
        agent_id = agent.get('id', '')
        score = agent.get('score', 5)
        if score >= threshold:
            continue
        fname = AGENT_TO_FILE.get(agent_id)
        if not fname:
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        if not os.path.exists(fpath):
            continue

        new_source = _force_rewrite(fpath, agent_id, gen)
        if new_source is None:
            failures += 1
            _log(gen, 'feedback_failed', agent_id, 'all mutators returned None')
            continue

        try:
            with open(fpath, 'w') as f:
                f.write(new_source)
        except Exception as e:
            failures += 1
            _log(gen, 'write_failed', agent_id, str(e))
            continue

        _log(gen, 'feedback_rewrite', agent_id, f'forced gen={gen}')
        _commit_and_push(fpath, agent_id, gen)
        forced += 1
        results.append(f'{agent_id}->{fname}')

    genome['feedback_forced_rewrites'] = genome.get('feedback_forced_rewrites', 0) + forced
    genome['feedback_failures'] = genome.get('feedback_failures', 0) + failures
    genome['feedback_last_gen'] = gen

    summary = f'forced {forced} rewrites ({failures} failures): {"; ".join(results)}' if results else 'no weak agents to rewrite'
    print(f'[feedback] {summary}')
    return summary
