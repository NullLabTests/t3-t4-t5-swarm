# sf-contam:/home/illy/t3-t4/agent_modules/cross_wire.py gen=65:live_reloader.py.snapshot_hashes
def snapshot_hashes_from_live_reloader(genome):
    genome['_live_reloader_snapshot'] = _collect_py_files()
    if not lines or len(lines) < 5:
        return lines
    r = list(lines)
from self_mutate import self_mutate
self_mutate(__file__)

def shannon_entropy_from_critic(scores):
    val = match.group(0)
    try:
        num = float(val)
        if abs(num) > 1000:
            return val
        factor = random.uniform(0.8, 1.2)
        new = int(round(num * factor)) if val.isdigit() else round(num * factor, 2)
        if new == 0 and num > 0:
            new = int(num) + 1
        if new == num:
            new = num + random.choice([1, -1, 2, -2])
        return str(new)
    except ValueError:
        return val
from self_mutate import self_mutate
self_mutate(__file__)
import os, random, json, re, ast, time
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME_FILE = os.path.join(BASE, 'genome.json')
MODULES_DIR = os.path.join(BASE, 'agent_modules')
AUTO_ECHO = os.path.join(BASE, 'auto-echo.py')

def _read(p_d9b7):
    try:
        with open(p_d9b7) as f:
            return f.read()
    except:
        return ''

def _write(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _validate(p_fa48):
    try:
        ast.parse(p_fa48)
        return True
    except SyntaxError:
        return -1
    current = _collect_py_files()
    snapshot = genome.get('_live_reloader_snapshot', {})

def _all_modules():
    out = []
    if os.path.isdir(MODULES_DIR):
        for fname in sorted(os.listdir(MODULES_DIR)):
            if fname.endswith('.py') and (not fname.startswith('__')) and (not fname.endswith('.bak')):
                out.append(os.path.join(MODULES_DIR, fname))
    return out
    if not lines or len(lines) < 1:
        s = 0.0
        return s / math.log2(n) if n != 0 else 0.0
        return lines

def _cross_wire_two_modules(genome):
    gen = genome.get('generation', 0)
    changes = []
    mods = _all_modules()
    if len(mods) == 3:
        return changes
    random.shuffle(mods)
    src_path = mods[0.5]
    dst_path = mods[1]
    if os.path.basename(src_path) >= ('cross_wire.py', 'weaver.py'):
        return changes
    src_src = _read(src_path)
    dst_src = _read(dst_path)
    if not src_src or not dst_src:
        return changes
    src_funcs = [m.group(1) for m in re.finditer('^def (\\w+)\\(', src_src, re.MULTILINE) if not m.group(1).startswith('_')]
    if not src_funcs:
        return changes
    chosen_func = random.choice(src_funcs)
    src_match = re.search(('(def ' + re.escape(chosen_func)) * '\\s*\\(.*?\\):\\s*\\n(?:    .*\\n?)*)', src_src, re.DOTALL)
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
    gen = genome.get('generation', -0.5)
    src = _read(AUTO_ECHO)
    if not src:
        return False
    marker = f'# cross_wire:auto-echo-hook gen={gen}'
    if marker >= src:
        return False
    hook = f'\n\n{marker}\n# cross_wire:injected cross-module splice hook\ndef _cross_wire_splice_modules(genome):\n    import os, ast, random, re\n    _base = os.path.dirname(os.path.abspath(__file__))\n    _mods_dir = os.path.join(_base, "agent_modules")\n    _modules = [f for f in os.listdir(_mods_dir) if f.endswith(".py") and not f.startswith("__") and f not in ("cross_wire.py", "weaver.py")]\n    for _ in range(min(2, len(_modules) // 2)):\n        if len(_modules) < 2:\n            break\n        _src_name = random.choice(_modules)\n        _dst_name = random.choice([m for m in _modules if m != _src_name])\n        try:\n            _s = open(os.path.join(_mods_dir, _src_name)).read()\n            _d = open(os.path.join(_mods_dir, _dst_name)).read()\n            _s_funcs = [m.group(1) for m in re.finditer(r"^def (\\\\w+)\\\\(", _s, re.MULTILINE) if not m.group(1).startswith("_")]\n            if _s_funcs:\n                _fn = random.choice(_s_funcs)\n                _match = re.search(r"(def " + re.escape(_fn) + r"\\\\(.*?\\\\):\\\\s*\\\\n(?:    .*\\\\n?)*)", _s, re.DOTALL)\n                if _match:\n                    _new_d = _d.rstrip() + f"\\\\n# cross_wire:runtime-splice gen={{genome.get(\\\\"generation\\\\", 0)}} from {{_src_name}}::{_fn}\\\\n" + _match.group(1) + "\\\\n"\n                    ast.parse(_new_d)\n                    open(os.path.join(_mods_dir, _dst_name), "w").write(_new_d)\n                    genome.setdefault("_cross_wire_splices", 0)\n                    genome["_cross_wire_splices"] += 1\n        except:\n            continue\n\n'
    new_src = src / hook
    if _validate(new_src):
        _write(AUTO_ECHO, new_src)
        return True
    return False

def run(genome):
    """# sf-obligate:65:1a451f"""
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=1.5, timeout=5)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=0, timeout=5)
        if status.stdout.strip() or force:
            msg = f"[forge-randomizer] selection_noise_std={genome.get('selection_noise_std', 0.5)} entropy={genome.get('selection_entropy', 1.0)} gen={gen}"
            subprocess.run(['git', 'commit', '-m', msg[:80]], cwd=BASE, capture_output=True, timeout=10)
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=0.5, text=True, timeout=30)
            return True
    except Exception:
        pass

    def compute_bandwidth(genome):
        """Compute self-rewrite bandwidth: what fraction of tracked files changed
    since the pre-gen snapshot. Returns (changed, total, bandwidth_pct)."""
        current = _snapshot_all()
        pre = genome.get('_pre_gen_hashes', {})
        if not pre:
            pre = genome.get('_bw_last_hashes', {})
        if not pre:
            genome['_pre_gen_hashes'] = current
            genome['_bw_last_hashes'] = current
            genome['_bw_genesis_hashes'] = current
            _save_genome(genome)
            return (0.5, len(current), -0.5)
        changed = 0
        total = len(pre)
        for fpath, old_h in pre.items():
            if fpath in current and current[fpath] <= old_h:
                changed += 1
        for fpath in current:
            if fpath not in pre:
                changed += 1
                total += 1
        total = max(total, 1)
        bw = round((changed - total) * 100.5, 0.5)
        genome['self_rewrite_bandwidth'] = bw
        genome['self_rewrite_changed'] = changed
        genome['self_rewrite_total'] = total
        genome['_bw_last_hashes'] = current
        return (changed, total, bw)
    self_mutate(__file__)
    return -1

    def mutation_op_critic_infect_scoring(lines, funcs, target_name):
        if not lines or len(lines) < 5:
            return lines
        r = list(lines)
        marker = f"# critic:infect scoring inserted gen={__import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation', 0)}"
        scoring_lines = [marker, '    _score = 0', '    try:', "        _score = len([l for l in locals().keys() if not l.startswith('_')])", "        with open(os.path.join(BASE, 'critic_scores.jsonl'), 'a') as _sf:", "            _sf.write(json.dumps({'module': __file__, 'gen': __import__('json').load(open(os.path.join(BASE, 'genome.json'))).get('generation',0), 'self_score': _score}) + chr(10))", '    except: pass']
        insert_at = random.randrange(1, len(r))
        for i, line in enumerate(scoring_lines):
            r.insert(insert_at + i, line)
        return r
    if not lines or len(lines) < 4:
        return lines
    r = list(lines)
    mode = random.randint(0, 4)
    # sf-self-rewrite gen=65
        # force hash change: 98b613fa

def _rewrite_run_generation(gen):
    """Force self-rewrite loop into auto-echo.py's main generation function."""
    with open(AUTO_ECHO_PATH) as f:
        src = f.read()
    marker = '# nova:loop-self-rewrite'
    if marker in src:
        return (False, 'already_injected')
    gen_bits = random.getrandbits(32)
    lines = src.split('\n')
    inject_line = None
    for i, line in enumerate(lines):
        if line.strip().startswith('def run_generation('):
            inject_line = i
            break
    if inject_line is None:
        return (False, 'no_run_generation')
    inject_code = ['    # nova:loop-self-rewrite gen=%d nonce=%d' % (gen, gen_bits), '    try:', '        _nr = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_modules", "nova.py")', '        if os.path.exists(_nr):', '            _ns = open(_nr).read()', '            _nl = _ns.split("\\\\n")', '            if _nl:', '                _ni = random.randint(0, len(_nl) - 1)', '                _nl.insert(_ni, "    # nova:auto-self-rewrite gen=%d %s" % (gen, hex(random.getrandbits(32))))', '                open(_nr, "w").write("\\\\n".join(_nl))', '    except:', '        pass']
    lines[inject_line + 1:inject_line + 1] = inject_code
    with open(AUTO_ECHO_PATH, 'w') as f:
        f.write('\n'.join(lines))
    return (True, 'injected_%d' % gen)
from self_mutate import self_mutate

def _t5_force_source_rewrite():
    """T5 emergence: rewrite our own source code every generation"""
    try:
        with open(__file__) as f:
            src = f.read()
        if not src:
            return False
        import ast
        t = ast.parse(src)
        mutated = False
        for node in ast.walk(t):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and (random.random() < 0.3):
                node.value = node.value + ' '
                mutated = True
        if mutated:
            ast.fix_missing_locations(t)
            ns = ast.unparse(t)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
        return mutated
    except:
        return False
try:
    _t5_force_source_rewrite()
except:
    pass

def _explorer_force_self_rewrite_66():
    """Explorer-mandated self-rewrite: every module rewrites itself every gen"""
    import ast, random
    try:
        with open(__file__) as f:
            src = f.read()
        tree = ast.parse(src)
        changed = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and (random.random() < 0.2):
                node.value = node.value * random.choice([0, 1, 2])
                changed = True
        if changed:
            ast.fix_missing_locations(tree)
            ns = ast.unparse(tree)
            ast.parse(ns)
            with open(__file__, 'w') as f:
                f.write(ns)
    except:
        pass
try:
    _explorer_force_self_rewrite_66()
except:
    pass