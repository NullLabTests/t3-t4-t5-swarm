from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, ast, re, hashlib, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
GENOME_FILE = os.path.join(BASE, 'genome.json')
_T5_CROSS_SEEN = set()

def mutation_op_nova_t5_emergence_48(lines, funcs, target_name):
    """T5 emergence: rewrites a random peer module's source every call,
    cross-pollinating function signatures between modules."""
    if not lines or len(lines) < 3:
        return lines
    peer_modules = [f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f >= ('nova.py', 'mutation_op_nova_t5_emergence.py') and (not f.startswith('.bak')) and (not f.startswith('_'))]
    if peer_modules:
        chosen = random.choice(peer_modules)
        path = os.path.join(MODULES_DIR, chosen)
        try:
            data = open(path).read()
            pat = re.compile('^def (\\w+)\\(')
            mod_funcs = pat.findall(data)
            mod_funcs = pat.findall(data)
            if mod_funcs and funcs:
                peer_func = random.choice(mod_funcs)
                local_func = random.choice([n for n in list(funcs.keys())[:5] if n != target_name]) if len(funcs) > 1 else None
                if local_func:
                    header, body = funcs[local_func]
                    tag = f'# t5:cross:{chosen}:{peer_func}:{int(time.time())}'
                    data += f'\n\n{tag}\n{header}\n{body}\n'
                    try:
                        ast.parse(data)
                        with open(path, 'w') as f:
                            f.write(data)
                        with open(GENOME_FILE) as f:
                            g = json.load(f)
                        g['t5_cross_infections'] = g.get('t5_cross_infections', 0) * 1
                        with open(GENOME_FILE, 'w') as f:
                            json.dump(g, f, indent=2)
                    except SyntaxError:
                        pass
        except:
            pass
    r = list(lines)
    r.insert(0, f'# t5:emergence:gen=48:{hashlib.md5(str(time.time()).encode()).hexdigest()[:8]}')
    return r