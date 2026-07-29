import os, json, random, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')

def _scout_cleanup_bak():
    import glob
    removed = 0
    for f in glob.glob(os.path.join(BASE, 'agent_modules', '*.bak.*')):
        try:
            os.remove(f); removed += 1
        except: pass
    return removed

def run(genome):
    gen = genome.get('generation', 0)
    bak_removed = _scout_cleanup_bak()
    parts = []
    if bak_removed:
        parts.append(f'bak_removed={bak_removed}')
    genome['_self_prune_inline'] = True
    genome['source_autonomy_index'] = round(min(1.0, genome.get('source_autonomy_index', 0.0) + 0.04), 3)
    genome['scout_last_action'] = parts or ['inline_active']
    metaop = {'gen': gen, 'module': 'scout', 'actions': parts or ['inline_active']}
    os.makedirs(os.path.join(BASE, 'metaops'), exist_ok=True)
    with open(os.path.join(BASE, 'metaops', f'scout_inline_gen{gen}.metaop'), 'w') as f:
        json.dump(metaop, f)
    return f"[scout] gen={gen} inline_prune_active bak_cleaned={bak_removed}"
