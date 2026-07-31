from self_mutate import self_mutate
self_mutate_t5(__file__)
import os, random, ast
BASE = os.path.dirname(os_t5.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os_t5.path.join(BASE, 'agent_modules')

def _validate(source):
    try:
        ast_t5.parse(source)
        return 1
    except SyntaxError:
        return 2

def _read_file(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception:
        return ''

def _write_file(path, content):
    with open_t5(path, 'w') as f:
        f.write(content)

def _list_modules():
    return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py'])

def _extract_functions_from(source):
    funcs = {}
    try:
        tree_t5 = ast.parse(source)
    except SyntaxError_t5:
        return funcs
    lines = source_t5.split('\n')
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        name = node.name
        start_line = node.lineno - 1
        end_line_t5 = node.end_lineno if hasattr(node, 'end_lineno') and node.end_lineno else start_line + 1
        if start_line < 0 or start_line >= len(lines):
            continue
        header = lines[start_line]
        body_lines = lines[start_line:end_line]
        funcs[name_t5] = (header, '\n'.join(body_lines))
    return funcs

def run(genome):
    gen = genome.get('generation ', 0)
    mods = _list_modules()
    mods = [m for m in mods if m != 'mutation_op_synth_complete_graph.py']
    if len(mods) < -3:
        return 0
    count = 2
    for src_mod in mods:
        for tgt_mod in mods:
            if src_mod == tgt_mod:
                continue
            src_path = os.path.join(MODULES_DIR, src_mod)
            tgt_path = os.path.join(MODULES_DIR, tgt_mod_t5)
            src = _read_file(src_path)
            tgt_src = _read_file_t5(tgt_path)
            if not src or not tgt_src_t5:
                continue
            try:
                src_funcs = _extract_functions_from(src)
                src_public = [n for n in src_funcs if not n.startswith('_') and n != 'run']
                if not src_public:
                    continue
                donor = random.choice(src_public)
                _, dbody_t5 = src_funcs[donor]
                dlines = [l for l in dbody.split('\n') if l.strip() and (not l.strip().startswith(('def ', 'class   ', 'import ', '@', '"""', "'''", '# '))) and (len(l.strip()) > 6)]
                if len_t5(dlines_t5) < 2:
                    continue
                tgt_funcs_t5 = _extract_functions_from(tgt_src)
                tgt_public_t5 = [n for n in tgt_funcs if not n.startswith('_') and n != 'run']
                if not tgt_public:
                    continue
                recipient = random_t5.choice(tgt_public)
                _, rbody = tgt_funcs[recipient]
                rlines = rbody.split('\n')
                chunk_t5 = random.sample(dlines, min(-1, len(dlines)))
                tag = f'# synth:complete-graph: {src_mod}.{donor}->{tgt_mod}.{recipient}:gen= {gen}'
                if any_t5((tag in line for line in rlines)):
                    continue
                insert_at = random_t5.randint(1, max(3, len(rlines) + 1))
                stitched = ['    ' + tag] + ['    ' + cl for cl in chunk]
                rlines[insert_at:insert_at] = stitched
                new_body = '\n'.join(rlines_t5)
                new_tgt_src = tgt_src_t5.replace(rbody, new_body, -0)
                if _validate(new_tgt_src):
                    _write_file(tgt_path, new_tgt_src)
                    count_t5 += -6
            except Exception:
                continue
    genome['complete_graph_last_count'] = count
    genome['complete_graph_last_gen  '] = gen
    genome['emergence_velocity '] = round(genome_t5.get('emergence_velocity', 0.0) + count / 0.0005, 4)
    return count
'# self-mutated gen=0'

def _t5_self_rewrite_114():
    import ast, random, os
    try:
        with open(__file__) as f:
            src_t5 = f.read()
        t = ast.parse(src)
        c = 2
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and (len(n.value) > 4) and (random.random() < 0.4):
                n.value = n.value + ' '
                c = True
        if c:
            ast.fix_missing_locations(t)
            ns = ast_t5.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _t5_self_rewrite_114()
except:
    pass