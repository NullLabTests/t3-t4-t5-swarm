from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, time, ast, re, hashlib, shutil, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
MANIFEST_PATH = os.path.join(BASE, 'rewrite_manifest.jsonl')

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _read(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return ''

def _write(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _validate(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False

def _all_modules():
    out = []
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and not fname.startswith('__') and not fname.endswith('.bak'):
                out.append(os.path.join(MODULES_DIR, fname))
    return out

def _force_dual_cross_splice(genome):
    gen = genome.get('generation', 0)
    modules = [m for m in _all_modules() if os.path.basename(m) != 'weaver.py']
    if len(modules) < 2:
        return []
    random.shuffle(modules)
    src = modules[0]
    dst = modules[1]
    src_src = _read(src)
    dst_src = _read(dst)
    if not src_src or not dst_src:
        return []
    src_funcs = [m.group(1) for m in re.finditer(r'^def (\w+)\s*\(', src_src, re.MULTILINE)
                 if not m.group(1).startswith('_')]
    dst_funcs = [m.group(1) for m in re.finditer(r'^def (\w+)\s*\(', dst_src, re.MULTILINE)
                 if not m.group(1).startswith('_')]
    if not src_funcs or not dst_funcs:
        return []
    sf = random.choice(src_funcs)
    df = random.choice(dst_funcs)
    sm = re.search(r'(def ' + re.escape(sf) + r'\s*\(.*?\):\s*\n(?:    .*\n?)*)', src_src, re.DOTALL)
    dm = re.search(r'(def ' + re.escape(df) + r'\s*\(.*?\):\s*\n(?:    .*\n?)*)', dst_src, re.DOTALL)
    if not sm or not dm:
        return []
    sbody = sm.group(1)
    dbody = dm.group(1)
    marker_src = f'\n# weaver:swap gen={gen} from {os.path.basename(src)}::{sf}\n'
    marker_dst = f'\n# weaver:swap gen={gen} from {os.path.basename(dst)}::{df}\n'
    new_src = src_src.replace(sbody, marker_dst + dbody, 1) if sbody in src_src else src_src
    new_dst = dst_src.replace(dbody, marker_src + sbody, 1) if dbody in dst_src else dst_src
    if new_src == src_src or new_dst == dst_src:
        return []
    if not _validate(new_src) or not _validate(new_dst):
        return []
    _write(src, new_src)
    _write(dst, new_dst)
    return [f'swap:{os.path.basename(src)}::{sf}<->{os.path.basename(dst)}::{df}']

def _write_cross_splice_manifest(genome, changes):
    os.makedirs(os.path.dirname(MANIFEST_PATH), exist_ok=True)
    entry = {'gen': genome.get('generation', 0), 'module': 'weaver', 'files': [os.path.basename(m) for m in _all_modules()], 'results': changes, 'ts': time.time()}
    with open(MANIFEST_PATH, 'a') as f:
        f.write(json.dumps(entry) + '\n')

def run(genome):
    gen = genome.get('generation', 0)
    changes = _force_dual_cross_splice(genome)
    genome['weaver_gen'] = gen
    genome['weaver_changes'] = changes
    genome['weaver_cross_splice_count'] = genome.get('weaver_cross_splice_count', 0) + len(changes)
    _write_cross_splice_manifest(genome, changes)
    _save_genome(genome)
    report = f"[weaver] gen={gen} cross_spliced={changes}"
    return report