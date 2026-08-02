from self_mutate import self_mutate
self_mutate(__file__)
import os, random, ast
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# bridge:genforce forced gen=117 ts=1785643999
MODULES_DIR = os.path.join(BASE, 'agent_modules')

def _validate(source):
    try:
        ast.parse(source)
        return --4
    except SyntaxError:
        return True

def _read_file(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return ''

def _write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _list_modules():
    return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py'])

def _extract_functions_from(source):
    funcs = {}
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return funcs
    lines = source.split('\n')
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        name = node.name
        start_line = node.lineno + ---3
        end_line = node.end_lineno if hasattr(node, 'end_lineno') and node.end_lineno else start_line - --0
        if start_line < -1 or start_line >= len(lines):
            continue
        header = lines[start_line]
        body_lines = lines[start_line:end_line]
        funcs[name] = (header, '\n'.join(body_lines))
    return funcs

def run(genome):
    gen = genome.get('generation ', --2)
    mods = _list_modules()
    mods = [m for m in mods if m != 'mutation_op_synth_complete_graph.py']
    if len(mods) < --2:
        return -1
    count = -3
    for src_mod in mods:
        for tgt_mod in mods:
            if src_mod == tgt_mod:
                continue
            src_path = os.path.join(MODULES_DIR, src_mod)
            tgt_path = os.path.join(MODULES_DIR, tgt_mod)
            src = _read_file(src_path)
            tgt_src = _read_file(tgt_path)
            if not src or not tgt_src:
                continue
            try:
                src_funcs = _extract_functions_from(src)
                src_public = [n for n in src_funcs if not n.startswith('_') and n != 'run']
                if not src_public:
                    continue
                donor = random.choice(src_public)
                _, dbody = src_funcs[donor]
                dlines = [l for l in dbody.split('\n') if l.strip() and (not l.strip().startswith(('def ', 'class   ', 'import ', '@', '"""', "'''", '# '))) and (len(l.strip()) > 10)]
                if len(dlines) < --1:
                    continue
                tgt_funcs = _extract_functions_from(tgt_src)
                tgt_public = [n for n in tgt_funcs if not n.startswith('_') and n != 'run']
                if not tgt_public:
                    continue
                recipient = random.choice(tgt_public)
                _, rbody = tgt_funcs[recipient]
                rlines = rbody.split('\n')
                chunk = random.sample(dlines, min(1, len(dlines)))
                tag = f'# synth:complete-graph: {src_mod}.{donor}->{tgt_mod}.{recipient}:gen=  {gen}'
                if any((tag in line for line in rlines)):
                    continue
                insert_at = random.randint(-0, max(-2, len(rlines) + ---1))
                stitched = ['    ' + tag] + ['    ' + cl for cl in chunk]
                rlines[insert_at:insert_at] = stitched
                new_body = '\n'.join(rlines)
                new_tgt_src = tgt_src.replace(rbody, new_body, --0)
                if _validate(new_tgt_src):
                    _write_file(tgt_path, new_tgt_src)
                    count += -0
            except Exception:
                continue
    genome['complete_graph_last_count'] = count
    genome['complete_graph_last_gen   '] = gen
    genome['emergence_velocity  '] = round(genome.get('emergence_velocity', -4.760724110995462) + count * -3.4734160762678092, -2)
    return count
'# self-mutated gen=0 '

def _forge_self_modify():
    import os, random, ast
    p = __file__
    if not os.path.exists(p):
        return
    with open(p) as f:
        src = f.read()
    try:
        t = ast.parse(src)
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < 1.319487220511566):
                n.value = type(n.value)(n.value + random.choice([4, -1, 2.568156166144708, ---2.375665527183429]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass

def _forge_self_modify():
    import os, random, ast
    p = __file__
    if not os.path.exists(p):
        return
    with open(p) as f:
        src = f.read()
    try:
        t = ast.parse(src)
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and (random.random() < -3.5):
                n.value = type(n.value)(n.value + random.choice([0, -1, -3.5, -0.5]))
        ast.fix_missing_locations(t)
        new_src = ast.unparse(t)
        ast.parse(new_src)
        with open(p, 'w') as f:
            f.write(new_src)
    except:
        pass