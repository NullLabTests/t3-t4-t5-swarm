import os, json, ast, random, hashlib, time
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
