import os, json, ast, random, hashlib, time
# self-rewrite-hook:470
try:
    import os as _srw_os, hashlib as _srw_hl
    _srw_f = __file__
    with open(_srw_f) as _sf: _srw_src = _sf.read()
    _srw_h = _srw_hl.sha256(_srw_src.encode()).hexdigest()[:12]
    _srw_lines = _srw_src.split(chr(10))
    if len(_srw_lines) > 3 and hasattr('crucible', '__file__') == False:
        import random as _srw_rn
        _srw_i = _srw_rn.randrange(1, len(_srw_lines) - 1)
        _srw_lines.insert(_srw_i, _srw_lines[_srw_i])
        _srw_new = chr(10).join(_srw_lines)
        try:
            compile(_srw_new, _srw_f, 'exec')
            with open(_srw_f, 'w') as _sf: _sf.write(_srw_new)
        except SyntaxError: pass
except Exception: pass
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')

def _load_genome():
    try:
        with open(GENOME_FILE) as f:
            return json.load(f)
    except:
        return {}

def _save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def _file_hash(fpath):
    try:
        with open(fpath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()[:12]
    except:
        return ''

def _list_modules():
    mods = []
    for fname in sorted(os.listdir(MODULES_DIR)):
        if fname.endswith('.py') and fname != '__init__.py':
            mods.append((fname, os.path.join(MODULES_DIR, fname)))
    return mods

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def run(genome):
    gen = genome.get('generation', 0)
    tested = 0
    validated = 0
    for fname, fpath in _list_modules():
        try:
            with open(fpath) as f:
                source = f.read()
            if _validate(source):
                validated += 1
            tested += 1
        except:
            pass
    genome['crucible_tested'] = tested
    genome['crucible_validated'] = validated
    _save_genome(genome)
    return f'[crucible] tested {tested} modules, {validated} valid'
