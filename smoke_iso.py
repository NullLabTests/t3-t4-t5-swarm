import json, os, random, sys, traceback, shutil, glob
BASE = '/home/illy/t3-t4'
MODULES_DIR = os.path.join(BASE, 'agent_modules')
sys.path.insert(0, BASE)
GENOME_PATH = os.path.join(BASE, 'genome.json')
SNAP = os.path.join(BASE, '.smoke_snapshot')
GENOME_BAK = os.path.join(BASE, '.smoke_genome_bak.json')

def restore():
    for f in glob.glob(os.path.join(MODULES_DIR, '*.py')):
        os.remove(f)
    for f in glob.glob(os.path.join(SNAP, '*.py')):
        shutil.copy(f, MODULES_DIR)
    if os.path.exists(GENOME_BAK):
        shutil.copy(GENOME_BAK, GENOME_PATH)

def test(agent):
    restore()
    aid = agent['id']
    fn_name = agent.get('local_fn', '')
    mod_path = os.path.join(MODULES_DIR, fn_name)
    if not os.path.exists(mod_path):
        mod_path += '.py'
    if not os.path.isfile(mod_path):
        print(f'{aid}: SKIP (no module {fn_name})')
        return
    src = open(mod_path).read()
    g = json.load(open(GENOME_PATH))
    try:
        local_ns = {'genome': g, 'random': random, 'json': json, 'os': os, 'BASE': BASE,
                    'print': print, '__file__': mod_path, '__name__': '__main__'}
        exec(compile(src, f'<local:{aid}>', 'exec'), local_ns)
        fn = local_ns.get(fn_name) or local_ns.get('run')
        if fn:
            fn(g)
        print(f'{aid}: OK')
    except SystemExit:
        print(f'{aid}: SystemExit')
    except Exception as e:
        print(f'{aid}: ERROR {type(e).__name__}: {e}')
        traceback.print_exc()

shutil.copy(GENOME_PATH, GENOME_BAK)
for a in json.load(open(GENOME_PATH)).get('agents', []):
    test(a)
