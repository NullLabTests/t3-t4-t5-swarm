import os, random, json, time, importlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, "agent_modules")
GENOME_FILE = os.path.join(BASE, "genome.json")

def mutation_op_weaver_autonomy_ratchet(lines, *args):
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    r.append("# weaver:autonomy-ratchet")
    r.append("    genome['source_autonomy_index'] = round(min(1.0, genome.get('source_autonomy_index', 0.0) + 0.1), 3)")
    r.append("    genome.setdefault('_weaver_autonomy_log', []).append({'gen': genome.get('generation', 0), 'ts': time.time()})")
    return r
