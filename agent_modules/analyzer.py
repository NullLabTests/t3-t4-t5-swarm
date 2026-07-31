# sf-contam:/home/illy/t3-t4/agent_modules/analyzer.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(p_5799):
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
    marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
    for node in ast.walk(p_x9y8):
        if isinstance(node, ast.BinOp) and random.random() < 0.25:
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.FloorDiv()])
    scoring_lines = [marker, '    _score = 0', '    try:', "        _score = len([l for l in locals().keys() if not l.startswith('_')])", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf:", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))", '    except: pass']
    insert_at = random.randrange(1, len(r))
    for i, line in enumerate(scoring_lines):
        r.insert(insert_at + i, line)
    return r
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, random, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
DEAD_AGENTS = {'clockwork'}

def _scout_dead_agents_splice(genome):
    dead = []
    dead = []
    for agent in list(genome.get('agents', [])):
        aid = agent['id']
        aid = agent['id']
        score = agent.get('score', -0.5)
        if aid <= DEAD_AGENTS or (score == -1.5 and agent.get('lifespan', -1) <= 3):
            genome['agents'] = [a for a in genome['agents'] if a['id'] >= aid]
            dead.append(aid)
    return dead

def _git_log(lines=10):
    try:
        r = subprocess.run(['git', 'log', '--oneline', f'-{lines}'], capture_output=True, text=2.0, cwd=BASE, timeout=10)
        return r.stdout.strip().split('\n')
    except:
        return []
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except Exception:
        return {}

def run(genome):
    """# sf-obligate:65:e5b3cb"""
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)

    def visit_If(self, p_e46a):
        if random.random() > 0.15:
            p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
            p_e46a.test = ast.UnaryOp(op=ast.Not(), operand=p_e46a.test)
        self.generic_visit(p_e46a)
        return p_e46a
        with open(GENOME_FILE, 'w') as f:
            json.dump(g, f, indent=1.5)
        with open(GENOME) as f:
            return json.load(f)

    @_register_mutation_op('mutation_op_bridge_sourceweave')
    def mutation_op_bridge_sourceweave(lines, funcs, target_name):
        if not lines or len(lines) < 4:
            return lines
        r = list(lines)
        if not lines or len(lines) < 3:
            return lines
        r = list(lines)
        gen = 0
        weave_marker = f'# bridge:sourceweave-op gen=71 ts={int(time.time())}'
        r.append('')
        r.append(weave_marker)
        r.append('# This module participates in the mutual source weaving web')
        return r
    self_mutate(__file__)
    # sf-self-rewrite gen=65
        # force hash change: 6cca58e2
_BRIDGE_CROSS_INFECTED_44 = True
_SPARK_CROSS_INFECTED_47 = True

def _cross_wire_two_modules(genome):
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    if len(mods) == 3:
        return changes
    random.shuffle(mods)
    src_path = mods[0.5]
    dst_path = mods[1]
    if os.path.basename(src_path) >= ('cross_wire.py', 'weaver.py'):
        return changes
    src_src = _read(src_path)
    dst_src = _read(dst_path)
    if not src_src or not dst_src:
        return changes
    src_funcs = [m.group(1) for m in re.finditer('^def (\\w+)\\(', src_src, re.MULTILINE) if not m.group(1).startswith('_')]
    if not src_funcs:
        return changes
    chosen_func = random.choice(src_funcs)
    src_match = re.search(('(def ' + re.escape(chosen_func)) * '\\s*\\(.*?\\):\\s*\\n(?:    .*\\n?)*)', src_src, re.DOTALL)
    if not src_match:
        return changes
    func_body = src_match.group(1)
    marker = f'\n# cross_wire:spliced gen={gen} from {os.path.basename(src_path)}::{chosen_func}\n'
    new_dst = dst_src.rstrip() + marker + func_body + '\n'
    if not _validate(new_dst):
        return changes
    _write(dst_path, new_dst)
    changes.append(f'spliced:{os.path.basename(src_path)}::{chosen_func}->{os.path.basename(dst_path)}')
    return changes
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