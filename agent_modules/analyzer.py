import os, json, time, random
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
GENOME_FILE = os.path.join(BASE, 'genome.json')

DUPLICATE_PATTERNS = [
    '# self-rewrite-hook:',
    '# feedback:agent=',
    '# endo:',
    '# oracle:',
    '# forced rewrite',
    '# autonomy-forced stub',
]

def _load():
    with open(GENOME_FILE) as f:
        return json.load(f)

def _save(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _count_duplicates(src, pattern):
    lines = src.split('\n')
    seen = {}
    dups = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if pattern in stripped:
            if stripped in seen:
                dups.append((i, stripped))
            else:
                seen[stripped] = i
    return dups

def _deduplicate_file(fpath):
    try:
        with open(fpath) as f:
            src = f.read()
    except:
        return 0, 0
    total_removed = 0
    total_patterns = 0
    for pattern in DUPLICATE_PATTERNS:
        dups = _count_duplicates(src, pattern)
        if dups:
            lines = src.split('\n')
            remove_indices = set(i for i, _ in dups)
            lines = [l for i, l in enumerate(lines) if i not in remove_indices]
            total_removed += len(dups)
            total_patterns += 1
            src = '\n'.join(lines)
    try:
        compile(src, fpath, 'exec')
        with open(fpath, 'w') as f:
            f.write(src)
    except SyntaxError:
        return 0, 0
    return total_removed, total_patterns

def _find_shortest_module():
    best = None
    best_len = float('inf')
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath) as f:
                src = f.read()
            if len(src) < best_len and 'def run(' in src:
                best = fpath
                best_len = len(src)
        except:
            pass
    return best

def run(genome):
    gen = genome.get('generation', 0)
    total_removed = 0
    files_cleaned = 0
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith('.py') or fname.startswith('__'):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        removed, patterns = _deduplicate_file(fpath)
        if removed > 0:
            total_removed += removed
            files_cleaned += 1
    shortest = _find_shortest_module()
    genome['analyzer_last_run'] = gen
    genome['analyzer_removed'] = genome.get('analyzer_removed', 0) + total_removed
    genome['analyzer_files_cleaned'] = genome.get('analyzer_files_cleaned', 0) + files_cleaned
    return f'[analyzer] gen={gen} removed={total_removed} dups across {files_cleaned} files shortest={os.path.basename(shortest) if shortest else "none"}'
