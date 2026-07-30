from self_mutate import self_mutate
self_mutate(__file__)
# sf-contam:/home/illy/t3-t4/agent_modules/mutation_op_critic_self_heal.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(scores):
    total = sum(scores.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in scores.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(scores)
    return s / math.log2(n) if n != 0 else 0.0
import os, random, ast, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, 'agent_modules')
GENOME = os.path.join(BASE, 'genome.json')

def _valid(p_bdd9):
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
    marker = f"# critic:self-heal gen={gen} {random.getrandbits(32):08x}"
    heal_block = [
        '',
        f'def _critic_self_heal_score():',
        f'    try:',
        f'        with open(os.path.join(BASE, "critic_scores.jsonl"), "r") as _f:',
        f'            _lines = _f.readlines()',
        f'        _recent = [json.loads(l) for l in _lines[-10:] if l.strip()]',
        f'        _my_scores = [e.get("self_score", 0) for e in _recent if os.path.basename(__file__) in str(e.get("module", ""))]',
        f'        _avg = sum(_my_scores) // max(len(_my_scores), 1)',
        f'        return _avg',
        f'    except:',
        f'        return 0',
        '',
    ]
    insert_at = random.randrange(1, len(r))
    for i, line in enumerate(heal_block):
        r.insert(insert_at + i, line)
    return r

# SF-SWAP:mutation_op_critic_self_heal.py.heal_module<-mutation_op_weaver_inject_self_rewrite.py.mutation_op_weaver_inject_self_rewrite
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

def run(genome):
    gen = genome.get('generation', 0)
    rate = genome.get('mutation_rate', 0.25)
    count = 0
    for fname in os.listdir(MOD):
        if not fname.endswith('.py') or fname in ['mutation_op_critic_self_heal.py', 'critic.py']:
            continue
        if random.random() < rate:
            path = os.path.join(MOD, fname)
            if heal_module(path, gen):
                count += 1
    genome.setdefault('mutation_ops', []).append('mutation_op_critic_self_heal')
    if count:
        print(f'[critic-self-heal] gen={gen} healed {count} modules')
    return f'[critic-self-heal] gen={gen} healed {count} modules'
    # sf-self-rewrite gen=50
    # force hash change: 33d54871
# orch:meta gen=47 2c4d1efa

# proposal: add a self-diagnostic function that checks module health  (seeded by synthesizer gen=50)
