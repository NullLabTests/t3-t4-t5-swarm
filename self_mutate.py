from __future__ import annotations
import ast, os, hashlib, random, sys, re, shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Tuple, Optional

def _swap_binary_ops(tree):
    swapped = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp):
            if random.random() < 0.2:
                old = node.op
                replacements = [ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.FloorDiv(), ast.Mod()]
                node.op = random.choice([r for r in replacements if type(r) != type(old)])
                swapped += 1
        if isinstance(node, ast.Compare):
            if random.random() < 0.2 and len(node.ops) == 1:
                old = type(node.ops[0])
                replacements = [ast.Eq(), ast.NotEq(), ast.Lt(), ast.Gt(), ast.LtE(), ast.GtE()]
                node.ops[0] = random.choice([r for r in replacements if type(r) != old])
                swapped += 1
    return swapped

def _invert_if_guards(tree):
    inverted = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            if random.random() < 0.15 and node.body and node.orelse:
                node.body, node.orelse = (node.orelse, node.body)
                if isinstance(node.test, ast.UnaryOp) and isinstance(node.test.op, ast.Not):
                    node.test = node.test.operand
                else:
                    node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
                inverted += 1
    return inverted

def _shuffle_function_body(tree):
    shuffled = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and len(node.body) >= 4 and random.random() < 0.12:
            non_doc_lines = [n for n in node.body if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str))]
            if len(non_doc_lines) >= 3:
                chunk = non_doc_lines[:3]
                random.shuffle(chunk)
                shuffled += 1
    return shuffled

def _perturb_constants(tree):
    perturbed = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and random.random() < 0.1:
            node.value = node.value + random.choice([-1, 1, 0.5, -0.5])
            perturbed += 1
    return perturbed

def _append_gen_marker(tree, gen):
    for node in ast.walk(tree):
        if isinstance(node, ast.Module) and node.body:
            marker = ast.Expr(value=ast.Constant(value=f'# self-mutated gen={gen}'))
            node.body.append(marker)
            return True
    return False

def self_mutate(filepath, gen=0):
    if not os.path.exists(filepath):
        return False
    try:
        with open(filepath) as f:
            source = f.read()
    except Exception:
        return False
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    touched = False
    for fn in [_swap_binary_ops, _invert_if_guards, _shuffle_function_body, _perturb_constants]:
        try:
            if fn(tree) > 0:
                touched = True
        except Exception:
            pass
    if not touched:
        try:
            if _append_gen_marker(tree, gen):
                touched = True
        except Exception:
            pass
    if not touched:
        return False
    try:
        ast.fix_missing_locations(tree)
    except Exception:
        return False
    new_source = ast.unparse(tree)
    if new_source == source:
        return False
    try:
        ast.parse(new_source)
    except SyntaxError:
        return False
    with open(filepath, 'w') as f:
        f.write(new_source)
    return True

class PatchResult:
    def __init__(self, success: bool, message: str, target: str=''):
        self.success = success
        self.message = message
        self.target = target
    def __str__(self):
        status = 'OK' if self.success else 'FAIL'
        return f'[{status}] {self.target}: {self.message}'

def _timestamp() -> str:
    return datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')

def backup_file(path: str | Path) -> Optional[str]:
    path = Path(path)
    if not path.exists():
        return None
    bak = path.with_suffix(path.suffix + f'.bak.{_timestamp()}')
    shutil.copy2(path, bak)
    return str(bak)

def validate_python(source: str) -> Tuple[bool, str]:
    try:
        ast.parse(source)
        return (True, '')
    except SyntaxError as e:
        return (False, f'SyntaxError at line {e.lineno}: {e.msg}')
    except Exception as e:
        return (False, str(e))

def extract_patches(text: str) -> List[dict]:
    patches = []
    for m in re.finditer('##(patch|add):([a-zA-Z_][a-zA-Z0-9_]*)\\n(.*?)(?=##end(?:patch|add)|\\Z)', text, re.DOTALL | re.IGNORECASE):
        kind = m.group(1).lower()
        name = m.group(2).strip()
        body = m.group(3).strip()
        body = re.sub('\\n##end(?:patch|add)\\s*$', '', body, flags=re.IGNORECASE).strip()
        if name and body:
            patches.append({'kind': kind, 'name': name, 'body': body})
    return patches

def apply_patches(source_path: str | Path, patch_text: str, *, dry_run: bool=False, create_backup: bool=True) -> List[PatchResult]:
    source_path = Path(source_path)
    results: List[PatchResult] = []
    if not source_path.exists():
        results.append(PatchResult(False, 'source file does not exist', str(source_path)))
        return results
    original = source_path.read_text(encoding='utf-8')
    patches = extract_patches(patch_text)
    if not patches:
        results.append(PatchResult(False, 'no ##patch or ##add blocks found', ''))
        return results
    current = original
    applied_any = False
    for p in patches:
        name = p['name']
        body = p['body']
        kind = p['kind']
        indented_body = '\n'.join(('    ' + line if line.strip() else line for line in body.splitlines()))
        if kind == 'add':
            new_func = f'\n\ndef {name}():\n{indented_body}\n'
            ok, err = validate_python(f'def {name}():\n{indented_body}\n')
            if not ok:
                results.append(PatchResult(False, f'new function invalid: {err}', name))
                continue
            candidate = current + new_func
            ok, err = validate_python(candidate)
            if not ok:
                results.append(PatchResult(False, f'file would become invalid after add: {err}', name))
                continue
            current = candidate
            results.append(PatchResult(True, 'function added', name))
            applied_any = True
            continue
        pattern = re.compile(f'(def {re.escape(name)}\\s*\\([^)]*\\)\\s*(?:->\\s*[^:]+)?\\s*:)\\n(.*?)(?=\\n(?:def |class |@)|\\Z)', re.DOTALL)
        m = pattern.search(current)
        if not m:
            results.append(PatchResult(False, 'function not found in source', name))
            continue
        header = m.group(1)
        replacement = header + '\n' + indented_body + '\n'
        candidate = current[:m.start()] + replacement + current[m.end():]
        ok, err = validate_python(candidate)
        if not ok:
            results.append(PatchResult(False, f'patch would make file invalid: {err}', name))
            continue
        current = candidate
        results.append(PatchResult(True, 'function body replaced', name))
        applied_any = True
    if applied_any and (not dry_run):
        if create_backup:
            bak = backup_file(source_path)
            if bak:
                results.append(PatchResult(True, f'backup created at {bak}', 'backup'))
        source_path.write_text(current, encoding='utf-8')
        results.append(PatchResult(True, 'source written to disk', str(source_path)))
    elif applied_any and dry_run:
        results.append(PatchResult(True, 'dry-run: changes NOT written', str(source_path)))
    return results

def apply_patch(patch_text: str, target: str='auto-echo.py', dry_run: bool=False) -> List[str]:
    base = Path(__file__).resolve().parent
    path = base / target if not Path(target).is_absolute() else Path(target)
    results = apply_patches(path, patch_text, dry_run=dry_run, create_backup=not dry_run)
    return [str(r) for r in results]

if __name__ == '__main__':
    print('self_mutate.py loaded. Self-mutation and patching ready.')
