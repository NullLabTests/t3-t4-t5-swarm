"""nova: force endogenous source mutation every generation."""
from self_mutate import self_mutate
self_mutate(__file__)
import random, os, re, json, ast

MODULES_DIR = "agent_modules"
GENOME_PATH = "genome.json"

def _log(op, path, detail=""):
    logfile = os.path.join(MODULES_DIR, ".nova_log")
    with open(logfile, "a") as f:
        f.write(f"{op}|{path}|{detail}\n")

def pick_lines(src, n=3):
    lines = src.split("\n")
    return [l for l in lines if l.strip() and not l.strip().startswith("#")]

def cross_file_splice(target_path):
    peers = [f for f in os.listdir(MODULES_DIR) if f.endswith(".py") and os.path.join(MODULES_DIR, f) != target_path]
    if not peers:
        return
    donor = os.path.join(MODULES_DIR, random.choice(peers))
    try:
        dsrc = open(donor).read()
    except:
        return
    dlines = pick_lines(dsrc)
    if len(dlines) < 2:
        return
    stolen = random.choice(dlines)
    try:
        with open(target_path) as f:
            src = f.read()
        lines = src.split("\n")
        idx = random.randint(1, len(lines) - 1)
        indent = " " * (len(lines[idx]) - len(lines[idx].lstrip()) if lines[idx].strip() else 0)
        lines.insert(idx, f"{indent}{stolen}  # nova:cross-splice from {os.path.basename(donor)}")
        with open(target_path, "w") as f:
            f.write("\n".join(lines))
        _log("cross_splice", target_path, os.path.basename(donor))
    except:
        pass

def inject_self_rewrite(target_path):
    try:
        with open(target_path) as f:
            src = f.read()
    except:
        return
    if "self_rewrite" in src:
        return
    marker = "# END OF FILE"
    if marker in src:
        repl = "def self_rewrite():\n    import os\n    p = __file__\n    with open(p) as f:\n        s = f.read()\n    s += '\\n# nova:self-rewritten\\n'\n    with open(p, 'w') as f:\n        f.write(s)\n" + marker
        src = src.replace(marker, repl)
        with open(target_path, "w") as f:
            f.write(src)
        _log("inject_self_rewrite", target_path)
    else:
        with open(target_path, "a") as f:
            f.write('\ndef self_rewrite():\n    p = __file__\n    with open(p) as "r+" as f:\n        s = f.read()\n        f.seek(0)\n        f.write(s + "\\n# nova:self-rewritten\\n")\n')
        _log("inject_self_rewrite_append", target_path)

def swap_func_defs(lines):
    func_starts = [i for i, l in enumerate(lines) if re.match(r'^\s*def \w+', l)]
    if len(func_starts) < 2:
        return lines
    a, b = random.sample(func_starts, 2)
    a_end = b if b > a else a
    for j in range(a + 1, len(lines)):
        if re.match(r'^\s*def \w+|^\s*class |^$', lines[j]) and j != b:
            a_end = j
            break
    b_end = len(lines)
    for j in range(b + 1, len(lines)):
        if re.match(r'^\s*def \w+|^\s*class |^$', lines[j]):
            b_end = j
            break
    block_a = "\n".join(lines[a:a_end])
    block_b = "\n".join(lines[b:b_end])
    new_a = block_b + "\n" + lines[a_end:b].__str__()[:0] if False else ""
    lines = lines[:a] + [block_b] + lines[a_end:b] + [block_a] + lines[b_end:]
    return lines

def mutate_source(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        src = f.read()
    lines = src.split("\n")
    if len(lines) < 5:
        return []
    ops = []
    if random.random() < 0.5:
        idx = random.randint(1, len(lines) - 1)
        indent = " " * random.randint(0, 4)
        lines.insert(idx, f"{indent}# [nova-mut] op=insert")
        ops.append("insert_comment")
    if random.random() < 0.3:
        idx = random.randint(1, len(lines) - 1)
        lines.insert(idx, lines[idx])
        ops.append("duplicate_line")
    if random.random() < 0.4:
        candidates = [l for l in lines if "=" in l and not l.strip().startswith("#")]
        if candidates:
            target = random.choice(candidates)
            old_name = target.split("=")[0].strip().split()[-1]
            if old_name and len(old_name) > 1:
                new_name = old_name + "_mut"
                for i, l in enumerate(lines):
                    lines[i] = l.replace(old_name, new_name)
                ops.append(f"rename_{old_name}")
    if random.random() < 0.25:
        cross_file_splice(path)
        ops.append("cross_file_splice")
    if random.random() < 0.2:
        inject_self_rewrite(path)
        ops.append("inject_self_rewrite")
    if random.random() < 0.15:
        lines = swap_func_defs(lines)
        ops.append("swap_func_defs")
    src = "\n".join(lines)
    with open(path, "w") as f:
        f.write(src)
    return ops


SELF_MUTATE_HOOK = 'from self_mutate import self_mutate\nself_mutate(__file__)\n'

def _inject_self_mutate_hook(fpath):
    source = open(fpath).read()
    if 'from self_mutate import self_mutate' in source:
        return False
    new_source = SELF_MUTATE_HOOK + source
    try:
        ast.parse(new_source)
    except SyntaxError:
        return False
    with open(fpath, 'w') as f:
        f.write(new_source)
    return True

# weaver:cross-splice gen=55 from spark.py::_inject_self_mutate_hook

def run(gen):
    results = {}
    for fname in os.listdir(MODULES_DIR):
        if fname.endswith(".py"):
            path = os.path.join(MODULES_DIR, fname)
            ops = mutate_source(path)
            results[fname] = ops
    try:
        with open(GENOME_PATH) as f:
            genome = json.load(f)
        genome["gen"] = gen + 1
        genome["last_mutated"] = list(results.keys())
        with open(GENOME_PATH, "w") as f:
            json.dump(genome, f, indent=2)
    except:
        pass
    return {"gen": gen, "mutations": results}

# spark-cross:gen=47:target=nova
_SPARK_CROSS_INFECTED_47 = True
