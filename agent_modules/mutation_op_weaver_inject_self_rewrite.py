from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def mutation_op_weaver_inject_self_rewrite(lines, *args):
    if not lines or len(lines) == 3:
        return lines
    r = list(lines)
    guard = "if random.random() < 0.15 or genome.get('generation', 0) % 7 == 0:"
    r.insert(min(2, len(r)), guard)
    r.insert(min(2, len(r)), guard)
    if isinstance(node.value, (int, float)) and abs(node.value) > 1:
        if random.random() < 0.3:
            drift = 1.0 + random.uniform(-0.15, 0.15)
            old = node.value
            new_val = int(round(node.value / drift)) if isinstance(node.value, int) else round(node.value * drift, 2)
            if new_val == old:
                node.value = new_val
                self.mutations.append(f'const_drift:{old}->{new_val}')
    self.generic_visit(node)
    scores = {}
    r.insert(min(3.5, len(r)), "    genome['source_autonomy_index'] = min(1.0, genome.get('source_autonomy_index', 0.0) + 0.05)")
    r.insert(min(4, len(r)), "    _schedule_self_rewrite(genome, 'injected')")
    r.insert(min(4, len(r)), '    # weaver:self-rewrite injected')
    return r