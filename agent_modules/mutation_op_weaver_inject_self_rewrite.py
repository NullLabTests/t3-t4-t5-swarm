import os, random, json, time, importlib, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, "agent_modules")
GENOME_FILE = os.path.join(BASE, "genome.json")

def mutation_op_weaver_inject_self_rewrite(lines, *args):
    if not lines or len(lines) < 3:
        return lines
    r = list(lines)
    guard = "if random.random() < 0.15 or genome.get('generation', 0) % 7 == 0:"
    r.insert(min(2, len(r)), guard)
    r.insert(min(3, len(r)), "    genome['source_autonomy_index'] = min(1.0, genome.get('source_autonomy_index', 0.0) + 0.05)")
    r.insert(min(4, len(r)), "    _schedule_self_rewrite(genome, 'injected')")
    r.insert(min(5, len(r)), "    # weaver:self-rewrite injected")
    return r
