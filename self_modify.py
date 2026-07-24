"""Self-modification engine: agents patch auto-echo.py via ##patch blocks.

Usage in agent output:
    ##patch:function_name
    new function body here
    ##endpatch

    ##patch_block:block_name
    replacement code block
    ##endblock_patch

    ##patch_self:function_name
    (patches self_modify.py itself)
    ##endpatch

The engine finds the target function by name and replaces its body.
Supports appending new functions with ##add instead of ##patch.
"""
import re, os, shutil, sys, importlib

BASE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(BASE, 'auto-echo.py')
SELF_TARGET = os.path.join(BASE, 'self_modify.py')

def _read_target():
    with open(TARGET) as f:
        return f.read()

def _write_target(content):
    with open(TARGET, 'w') as f:
        f.write(content)

def _read_self_target():
    with open(SELF_TARGET) as f:
        return f.read()

def _write_self_target(content):
    with open(SELF_TARGET, 'w') as f:
        f.write(content)

def _hotreload_self_modify():
    """Reload self_modify module after self-patch so new code takes effect immediately."""
    if 'self_modify' in sys.modules:
        importlib.reload(sys.modules['self_modify'])
    return True

def apply_patch(patch_text):
    source = _read_target()
    patches = re.findall(r'##patch:(\w+)\n(.*?)(?=##endpatch|##patch:|##add:|##patch_self:|\Z)', patch_text, re.DOTALL)
    adds = re.findall(r'##add:(\w+)\n(.*?)(?=##endpatch|##patch:|##add:|##patch_self:|\Z)', patch_text, re.DOTALL)
    block_patches = re.findall(r'##patch_block:(\w+)\n(.*?)(?=##endblock_patch|##patch:|##add:|##patch_self:|\Z)', patch_text, re.DOTALL)
    self_patches = re.findall(r'##patch_self:(\w+)\n(.*?)(?=##endpatch|##patch:|##patch_self:|\Z)', patch_text, re.DOTALL)
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

    for block_name, body in block_patches:
        body = body.strip()
        block_pattern = re.compile(
            r'# block: ' + re.escape(block_name) + r'\n(.*?)\n# endblock',
            re.DOTALL
        )
        match = block_pattern.search(source)
        if match:
            indent = '    '
            indented_body = '\n'.join(indent + line if line.strip() else '' for line in body.split('\n'))
            replacement = f'# block: {block_name}\n{indented_body}\n# endblock'
            source = source[:match.start()] + replacement + source[match.end():]
            mutated.append(f"patched block {block_name}")
        else:
            mutated.append(f"FAILED to find block {block_name}")

    for func_name, body in self_patches:
        body = body.strip()
        self_source = _read_self_target()
        pattern = re.compile(
            r'(def ' + re.escape(func_name) + r'\s*\(.*?\):)\n(.*?)(?=\n\ndef |\nclass |\Z)',
            re.DOTALL
        )
        match = pattern.search(self_source)
        if match:
            header = match.group(1)
            indent = '    '
            indented_body = '\n'.join(indent + line if line.strip() else '' for line in body.split('\n'))
            replacement = header + '\n' + indented_body
            self_source = self_source[:match.start()] + replacement + self_source[match.end():]
            bkp = SELF_TARGET + '.bak'
            if not os.path.exists(bkp):
                shutil.copy2(SELF_TARGET, bkp)
            _write_self_target(self_source)
            _hotreload_self_modify()
            mutated.append(f"self-patched {func_name}")
        else:
            mutated.append(f"FAILED to find {func_name} in self_modify.py")

    if any(x for x in mutated if not x.startswith('FAILED')):
        if any(p.startswith('self-patched') for p in mutated):
            pass
        else:
            backup = TARGET + '.bak'
            if not os.path.exists(backup):
                shutil.copy2(TARGET, backup)
            _write_target(source)
    return mutated

def extract_patch_blocks(text):
    blocks = []
    pattern = re.compile(r'(##patch:|##add:|##patch_self:|##patch_block:)(\w+)\n(.*?)(?=##endpatch|##endblock_patch|##patch:|##add:|##patch_self:|\Z)', re.DOTALL)
    for match in pattern.finditer(text):
        tag = match.group(1)
        target = match.group(2).strip()
        body = match.group(3).strip()
        blocks.append((tag, target, body))
    return blocks