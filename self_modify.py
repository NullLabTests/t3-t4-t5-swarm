"""Self-modification engine: agents patch auto-echo.py via ##patch blocks.

Usage in agent output:
    ##patch:function_name
    new function body here
    ##endpatch

The engine finds the target function by name and replaces its body.
Supports appending new functions with ##add instead of ##patch.
"""
import re, os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(BASE, 'auto-echo.py')

def _read_target():
    with open(TARGET) as f:
        return f.read()

def _write_target(content):
    with open(TARGET, 'w') as f:
        f.write(content)

def apply_patch(patch_text):
    source = _read_target()
    patches = re.findall(r'##patch:(\w+)\n(.*?)(?=##endpatch|##patch:|##add:|\Z)', patch_text, re.DOTALL)
    adds = re.findall(r'##add:(\w+)\n(.*?)(?=##endpatch|##patch:|##add:|\Z)', patch_text, re.DOTALL)
    mutated = []

    for func_name, body in patches:
        body = body.strip()
        pattern = re.compile(
            r'(def ' + re.escape(func_name) + r'\s*\(.*?\):)\n(.*?)(?=\n\ndef |\nclass |\Z)',
            re.DOTALL
        )
        match = pattern.search(source)
        if match:
            header = match.group(1)
            indent = '    '
            indented_body = '\n'.join(indent + line if line.strip() else '' for line in body.split('\n'))
            replacement = header + '\n' + indented_body
            source = source[:match.start()] + replacement + source[match.end():]
            mutated.append(f"patched {func_name}")
        else:
            mutated.append(f"FAILED to find {func_name}")

    for func_name, body in adds:
        body = body.strip()
        indent = '    '
        indented_body = '\n'.join(indent + line if line.strip() else '' for line in body.split('\n'))
        new_func = f'\n\ndef {func_name}():\n{indented_body}\n'
        source += new_func
        mutated.append(f"added {func_name}")

    if mutated:
        backup = TARGET + '.bak'
        if not os.path.exists(backup):
            shutil.copy2(TARGET, backup)
        _write_target(source)
    return mutated

def extract_patch_blocks(text):
    blocks = []
    pattern = re.compile(r'(##patch:|##add:)(\w+)\n(.*?)(?=##endpatch|##patch:|##add:|\Z)', re.DOTALL)
    for match in pattern.finditer(text):
        tag = match.group(1)
        target = match.group(2).strip()
        body = match.group(3).strip()
        blocks.append((tag, target, body))
    return blocks