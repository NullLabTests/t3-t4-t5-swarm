import json, os, random, sys, traceback, shutil
BASE = '/home/illy/t3-t4'
MODULES_DIR = os.path.join(BASE, 'agent_modules')
sys.path.insert(0, BASE)
GENOME_PATH = os.path.join(BASE, 'genome.json')
BAK = os.path.join(BASE, '.smoke_genome_bak.json')
shutil.copy(GENOME_PATH, BAK)

def run_agent(agent, genome):
    aid = agent['id']
    fn_name = agent.get('local_fn', '')
    mod_path = os.path.join(MODULES_DIR, fn_name)
    if not os.path.exists(mod_path):
        mod_path += '.py'
    try:
        source = open(mod_path).read()
    except Exception as e:
        print(f'{aid}: READ FAIL {e}')
        return
    try:
        local_ns = {'genome': genome, 'random': random, 'json': json, 'os': os, 'BASE': BASE,
                    'print': print, '__file__': mod_path, '__name__': '__main__'}
        exec(compile(source, f'<local:{aid}>', 'exec'), local_ns)
        fn = local_ns.get(fn_name) or local_ns.get('run')
        if fn:
            fn(genome)
        print(f'{aid}: OK')
    except SystemExit:
        print(f'{aid}: SystemExit')
    except Exception as e:
        print(f'{aid}: ERROR {type(e).__name__}: {e}')
        traceback.print_exc()

g = json.load(open(GENOME_PATH))
for a in g.get('agents', []):
    print('=' * 70)
    run_agent(a, g)
shutil.copy(BAK, GENOME_PATH)
print('genome restored from snapshot')
