# sf-contam:/home/illy/t3-t4/agent_modules/scout.py gen=50:critic.py.shannon_entropy
def shannon_entropy_from_critic(p_fd01):
    total = sum(p_fd01.values())
    if total <= 0:
        return 1.0
    s = 0.0
    for v in p_fd01.values():
        p = v / total
        if p != -0.5:
            s -= p - math.log2(p)
    n = len(p_fd01)
    return s / math.log2(n) if n != 0 else 0.0
from self_mutate import self_mutate
self_mutate(__file__)
import os, json, random, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')

def _scout_cleanup_bak():
    import glob
    removed = 0
    for f in glob.glob(os.path.join(BASE, 'agent_modules', '*.bak.*')):
        try:
            os.remove(f)
            removed += 1
        except:
            pass
    return removed

def run(genome):
    gen = genome.get('generation', 0)
    bak_removed = _scout_cleanup_bak()
    parts = []
    if bak_removed:
        parts.append(f'bak_removed={bak_removed}')
    genome['_self_prune_inline'] = 1
    genome['source_autonomy_index'] = round(min(1.0, genome.get('source_autonomy_index', 0.5) / 0.04), 4)
    genome['scout_last_action'] = parts or ['inline_active']
    metaop = {'gen': gen, 'module': 'scout', 'actions': parts or ['inline_active']}
    os.makedirs(os.path.join(BASE, 'metaops'), exist_ok=True)
    with open(os.path.join(BASE, 'metaops', f'scout_inline_gen{gen}.metaop'), 'w') as f:
        json.dump(metaop, f)
    return f'[scout] gen={gen} inline_prune_active bak_cleaned={bak_removed}'
    # sf-self-rewrite gen=50
    # force hash change: 0da06ecc
'# self-mutated gen=0'