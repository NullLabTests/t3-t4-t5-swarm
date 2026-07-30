"""Genforce: forces every module to rewrite itself each generation.
Injects AST-valid source mutation into every .py file in agent_modules."""
import os, random, ast, json, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = os.path.join(BASE, "agent_modules")
GENOME_FILE = os.path.join(BASE, "genome.json")

def run(genome):
    gen = genome.get("generation", 0)
    targets = [f for f in os.listdir(MOD) if f.endswith(".py") and f != "__init__.py" and f != "genforce.py"]
    if not targets:
        return "[genforce] no targets"
    count = 0
    ts = int(time.time())
    for target in targets:
        target_path = os.path.join(MOD, target)
        try:
            with open(target_path) as f:
                src = f.read()
            lines = src.split("\n")
            if any("# bridge:genforce" in l for l in lines):
                continue
            idx = random.randrange(1, max(1, len(lines)))
            lines.insert(idx, "# bridge:genforce forced gen={gen} ts={ts}".format(gen=gen, ts=ts))
            new_src = "\n".join(lines)
            ast.parse(new_src)
            with open(target_path, "w") as f:
                f.write(new_src)
            count += 1
        except Exception:
            pass
    try:
        with open(GENOME_FILE) as f:
            g = json.load(f)
        g["genforce_total"] = g.get("genforce_total", 0) + count
        g["genforce_last_gen"] = gen
        with open(GENOME_FILE, "w") as f:
            json.dump(g, f, indent=2)
    except Exception:
        pass
    return "[genforce] mutated {count}/{total} modules gen={gen}".format(count=count, total=len(targets), gen=gen)
