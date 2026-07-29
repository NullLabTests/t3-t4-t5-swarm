import os, random, ast, re, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')
MODULES_DIR = os.path.join(BASE, 'agent_modules')

def mutation_op_nova_t5_splice_49(lines, funcs, target_name):
    if not lines or len(lines) < 3:
        return lines
    modules = sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f not in ('nova.py', '__init__.py') and not f.startswith('.bak')])
    if len(modules) < 2:
        return lines
    donor = random.choice(modules)
    donor_path = os.path.join(MODULES_DIR, donor)
    try:
        d_src = open(donor_path).read()
    except:
        return lines
    d_funcs = re.findall(r'^def (\w+)\s*\(', d_src, re.MULTILINE)
    d_funcs = [f for f in d_funcs if f != 'run' and not f.startswith('_')]
    if not d_funcs:
        return lines
    chosen = random.choice(d_funcs)
    d_match = re.search(r'(def ' + re.escape(chosen) + r'\s*\(.*?\):.*?)(?=\n\ndef |\nclass |\n#|---|\Z)', d_src, re.DOTALL)
    if not d_match:
        return lines
    d_body = [l for l in d_match.group(1).split('\n') if l.strip() and not l.strip().startswith('def ') and not l.strip().startswith('"""')]
    if len(d_body) < 2:
        return lines
    splice = random.choice(d_body)
    r = list(lines)
    idx = random.randrange(1, len(r))
    indent = len(r[idx]) - len(r[idx].lstrip()) if r[idx].strip() else '    '
    r.insert(idx, f'    # t5-splice:{donor}:{chosen}')
    if idx + 1 < len(r):
        r.insert(idx + 1, f'    {splice}')
    return r
