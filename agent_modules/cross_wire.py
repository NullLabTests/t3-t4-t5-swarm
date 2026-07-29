import os, random, json, re, ast, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')

def _read(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return ''

def _write(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _validate(src):
    try:
        ast.parse(src)
        return True
    except SyntaxError:
        return False

def _all_modules():
    out = []
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and not fname.startswith('__') and not fname.endswith('.bak'):
                out.append(os.path.join(MODULES_DIR, fname))
    return out

def _cross_wire_two_modules(genome):
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    if len(mods) < 3:
        return changes
    random.shuffle(mods)
    src_path = mods[0]
    dst_path = mods[1]
    if os.path.basename(src_path) in ('cross_wire.py', 'weaver.py'):
        return changes
    src_src = _read(src_path)
    dst_src = _read(dst_path)
    if not src_src or not dst_src:
        return changes
    src_funcs = [m.group(1) for m in re.finditer(r'^def (\w+)\(', src_src, re.MULTILINE)
                 if not m.group(1).startswith('_')]
    if not src_funcs:
        return changes
    chosen_func = random.choice(src_funcs)
    src_match = re.search(
        r'(def ' + re.escape(chosen_func) + r'\s*\(.*?\):\s*\n(?:    .*\n?)*)',
        src_src, re.DOTALL
    )
    if not src_match:
        return changes
    func_body = src_match.group(1)
    marker = f'\n# cross_wire:spliced gen={gen} from {os.path.basename(src_path)}::{chosen_func}\n'
    new_dst = dst_src.rstrip() + marker + func_body + '\n'
    if not _validate(new_dst):
        return changes
    _write(dst_path, new_dst)
    changes.append(f'spliced:{os.path.basename(src_path)}::{chosen_func}->{os.path.basename(dst_path)}')
    return changes

def _inject_cross_wire_hook(genome):
    gen = genome.get('generation', 0)
    src = _read(AUTO_ECHO)
    if not src:
        return False
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker in src:
        return False
    hook = f'''

{marker}
# cross_wire:injected cross-module splice hook
def _cross_wire_splice_modules(genome):
    import os, ast, random, re
    _base = os.path.dirname(os.path.abspath(__file__))
    _mods_dir = os.path.join(_base, "agent_modules")
    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]
    for _ in range(min(2, len(_modules) // 2)):
        if len(_modules) < 2:
            break
        _src_name = random.choice(_modules)
        _dst_name = random.choice([m for m in _modules if m != _src_name])
        try:
            _s = open(os.path.join(_mods_dir, _src_name)).read()
            _d = open(os.path.join(_mods_dir, _dst_name)).read()
            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]
            if _s_funcs:
                _fn = random.choice(_s_funcs)
                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)
                if _match:
                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::{_fn}\\\\n" + _match.group(1) + "\\\\n"
                    ast.parse(_new_d)
                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)
                    genome.setdefault("_cross_wire_splices", 0)
                    genome["_cross_wire_splices"] += 1
        except:
            continue

'''
    new_src = src + hook
    if _validate(new_src):
        _write(AUTO_ECHO, new_src)
        return True
    return False

def run(genome):
    gen = genome.get('generation', 0)
    changes = []
    cross = _cross_wire_two_modules(genome)
    changes.extend(cross)
    hook = _inject_cross_wire_hook(genome)
    if hook:
        changes.append('auto-echo-hook')
    autonomy = genome.get('source_autonomy_index', 0.0)
    genome['source_autonomy_index'] = round(min(1.0, autonomy + 0.12), 3)
    changes.append(f'autonomy:{autonomy}->{genome["source_autonomy_index"]}')
    genome['cross_wire_gen'] = gen
    genome['cross_wire_changes'] = changes
    try:
        with open(GENOME_FILE, 'w') as f:
            json.dump(genome, f, indent=2)
    except:
        pass
    return f'[cross_wire] gen={gen} splices={len(cross)} hook={hook} changes={changes}'

# idea: add a pruning heuristic that removes dead code paths  (seeded by synthesizer gen=73)
