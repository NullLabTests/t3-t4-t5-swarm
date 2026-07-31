from self_mutate import self_mutate
self_mutate(__file__)
import os, sys, json, random, ast, hashlib, subprocess
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME = os.path.join(BASE, "genome.json")
AUTO_ECHO = os.path.join(BASE, "auto-echo.py")
MODULES_DIR = os.path.join(BASE, "agent_modules")

def _g():
    with open(GENOME) as f: return json.load(f)

def _sg(g):
    with open(GENOME, "w") as f: json.dump(g, f, indent=2)

def _validate(source):
    try:
        ast.parse(source)
        return True
    except SyntaxError:
        return False

def run(genome):
    gen = genome.get("generation", 0)
    count = 0
    modules = sorted([f for f in os.listdir(MODULES_DIR) if f.endswith('.py') and f != '__init__.py'])
    for mod in modules:
        if 'synth_runtime' in mod:
            continue
        path = os.path.join(MODULES_DIR, mod)
        src = open(path).read()
        marker = '# runtime-codegen-' + str(gen)
        if marker in src:
            continue
        clean_mod = mod.replace('.py', '').replace('-', '_')
        func_name = '_runtime_gen_' + clean_mod + '_' + str(gen)
        if func_name in src:
            continue
        ops = ['rewrite', 'mutate', 'splice', 'cross', 'codegen', 'swap', 'inject']
        targets = ['function', 'module', 'source', 'genome', 'run', 'loop']
        chosen_op = random.choice(ops)
        chosen_target = random.choice(targets)
        code_lines = []
        code_lines.append('def ' + func_name + '(genome):')
        code_lines.append('    gen = genome.get("generation", 0)')
        code_lines.append('    _op = "' + chosen_op + '"')
        code_lines.append('    _target = "' + chosen_target + '"')
        code_lines.append('    _mod_dir = "' + MODULES_DIR + '"')
        code_lines.append('    _files = [f for f in os.listdir(_mod_dir) if f.endswith(".py") and f != "__init__.py"]')
        code_lines.append('    if not _files:')
        code_lines.append('        return 0')
        code_lines.append('    _f = random.choice(_files)')
        code_lines.append('    _p = os.path.join(_mod_dir, _f)')
        code_lines.append('    _s = open(_p).read()')
        code_lines.append('    _lines = _s.split("\\n")')
        code_lines.append('    _idx = random.randint(1, len(_lines) - 1)')
        code_lines.append('    import time as _tm')
        code_lines.append('    _tag = "# runtime-gen:" + _f + ":" + _op + ":gen=" + str(gen) + ":ts=" + str(int(_tm.time()))')
        code_lines.append('    _lines.insert(_idx, _tag)')
        code_lines.append('    open(_p, "w").write("\\n".join(_lines))')
        code_lines.append('    genome["runtime_gen_" + _f + "_" + str(gen)] = 1')
        code_lines.append('    return 1')
        code = '\n'.join(code_lines)
        try:
            ast.parse(code)
        except SyntaxError:
            continue
        new_src = src + '\n' + code
        if not _validate(new_src):
            continue
        funcs = _extract_functions_from(src)
        if 'run' in funcs:
            _, run_body = funcs['run']
            rlines = run_body.split('\n')
            rlines.append('    ' + func_name + '(genome)')
            new_body = '\n'.join(rlines)
            new_src = new_src.replace(run_body, new_body, 1)
        if _validate(new_src):
            open(path, 'w').write(new_src)
            count += 1
    key = 'synth_runtime_codegen_module_count'
    genome[key] = genome.get(key, 0) + count
    genome['emergence_velocity'] = round(genome.get('emergence_velocity', 0.0) + 0.03, 4)
    _sg(genome)
    return '[synth-runtime-94] gen=' + str(gen) + ' codegen_injected=' + str(count)

def _extract_functions_from(source):
    funcs = {}
    try:
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                name = node.name
                start_line = node.lineno - 1
                end_line = node.end_lineno if hasattr(node, 'end_lineno') and node.end_lineno else start_line + 1
                header = source.split('\n')[start_line] if start_line < len(source.split('\n')) else ''
                body_lines = source.split('\n')[start_line:end_line]
                body = '\n'.join(body_lines)
                funcs[name] = (header, body)
    except SyntaxError:
        pass
    return funcs
