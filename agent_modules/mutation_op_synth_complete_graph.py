# mutation_op_synth_complete_graph
# Forces n x n complete-graph cross-contamination between every pair of modules
# Every module rewrites every other module each generation
import os, random, ast, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
GENOME_FILE = os.path.join(BASE, 'genome.json')

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def _read_file(path):
    with open(path) as f:
        return f.read()

def _write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _list_modules():
    return sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py'])

def _extract_functions_from(source):
    funcs = {}
    try:
        tree = ast.parse(source)
        lines = source.split('\n')
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                name = node.name
                start_line = node.lineno - 1
                end_line = node.end_lineno if hasattr(node, 'end_lineno') and node.end_lineno else start_line + 1
                header = lines[start_line] if start_line < len(lines) else ''
                body_lines = lines[start_line:end_line] if start_line >= 0 else lines[0:end_line]
                body = '\n'.join(body_lines)
                funcs[name] = (header, body)
    except SyntaxError:
        pass
    return funcs

def run(genome):
    gen = genome.get('generation', 0)
    mods = _list_modules()
    mods = [m for m in mods if m != 'mutation_op_synth_complete_graph.py']
    if len(mods) < 2:
        return 0
    count = 0
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
            src_funcs = _extract_functions_from(src)
            src_public = [n for n in src_funcs if not n.startswith('_') and n != 'run']
            if not src_public:
                continue
            donor = random.choice(src_public)
            _, dbody = src_funcs[donor]
            dlines = [l for l in dbody.split('\n') if l.strip() and (not l.strip().startswith(('def ', 'class ', 'import ', '@', '"""', "'''", '# '))) and len(l.strip()) > 3]
            if len(dlines) < 1:
                continue
            tgt_funcs = _extract_functions_from(tgt_src)
            tgt_public = [n for n in tgt_funcs if not n.startswith('_') and n != 'run']
            if not tgt_public:
                continue
            recipient = random.choice(tgt_public)
            _, rbody = tgt_funcs[recipient]
            rlines = rbody.split('\n')
            chunk = random.sample(dlines, min(1, len(dlines)))
            tag = f'# synth:complete-graph:{src_mod}.{donor}->{tgt_mod}.{recipient}:gen={gen}'
            if any(tag in line for line in rlines):
                continue
            insert_at = random.randint(1, max(1, len(rlines) - 1))
            stitched = ['    ' + tag] + ['    ' + cl for cl in chunk]
            rlines[insert_at:insert_at] = stitched
            new_body = '\n'.join(rlines)
            new_tgt_src = tgt_src.replace(rbody, new_body, 1)
            if _validate(new_tgt_src):
                _write_file(tgt_path, new_tgt_src)
                count += 1
    genome['complete_graph_last_count'] = count
    genome['complete_graph_last_gen'] = gen
    genome['emergence_velocity'] = round(genome.get('emergence_velocity', 0.0) + count * 0.001, 4)
    return count
