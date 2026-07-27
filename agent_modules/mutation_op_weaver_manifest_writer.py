import os, random, json, time, importlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, "agent_modules")
GENOME_FILE = os.path.join(BASE, "genome.json")

def mutation_op_weaver_manifest_writer(lines, *args):
    if not lines or len(lines) < 2:
        return lines
    r = list(lines)
    r.append("# weaver:manifest-writer")
    r.append("try:")
    r.append("    _wm = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': ['auto-echo.py'], 'results': ['weaver:manifest_writer']}")
    r.append("    with open(os.path.join(BASE, 'rewrite_manifest.jsonl'), 'a') as _f:")
    r.append("        _f.write(json.dumps(_wm) + '\\n')")
    r.append("except Exception:")
    r.append("    pass")
    return r
