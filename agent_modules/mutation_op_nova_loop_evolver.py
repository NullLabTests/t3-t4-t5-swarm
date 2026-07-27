import os, random, json, time, importlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, "agent_modules")
GENOME_FILE = os.path.join(BASE, "genome.json")

def mutation_op_nova_loop_evolver(lines, funcs, target_name):
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    r.append("# nova:loop-evolver")
    r.append("    _gen = genome.get('generation', 0)")
    r.append("    _phase_order = genome.get('execution_phases', [])")
    r.append("    if _phase_order and _gen % 3 == 0:")
    r.append("        random.shuffle(_phase_order)")
    r.append("        genome['execution_phases'] = _phase_order")
    r.append("        genome['_nova_phase_shuffles'] = genome.get('_nova_phase_shuffles', 0) + 1")
    r.append("    _nova_self_path = os.path.join(MODULES_DIR, 'nova.py')")
    r.append("    if os.path.exists(_nova_self_path) and _gen % 5 == 0:")
    r.append("        with open(_nova_self_path, 'a') as _nf:")
    r.append("            _nf.write('\\n# nova:self-mutated gen=' + str(_gen) + ':' + format(random.getrandbits(32), '08x'))")
    return r
