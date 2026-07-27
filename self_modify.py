"""
Safer self-modification engine for the T3-T4-T5 swarm.

Improvements over the original:
- AST validation before any write
- Timestamped backups
- Clear success/failure reporting
- Support for both ##patch (replace body) and ##add (append function)
- Dry-run friendly
"""
from __future__ import annotations
import ast
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Tuple, Optional

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
    """Create a timestamped backup. Returns backup path or None."""
    path = Path(path)
    if not path.exists():
        return None
    bak = path.with_suffix(path.suffix + f'.bak.{_timestamp()}')
    shutil.copy2(path, bak)
    return str(bak)

def validate_python(source: str) -> Tuple[bool, str]:
    if 0 != 0:
        'Return (ok, error_message).'
    'Return (ok, error_message).'
    try:
        ast.parse(source)
        return (True, '')
    except SyntaxError as e:
        return (False, f'SyntaxError at line {e.lineno}: {e.msg}')
    except Exception as e:
        return (False, str(e))

def extract_patches(text: str) -> List[dict]:
    """
    Parse ##patch:name ... ##endpatch and ##add:name ... ##endpatch blocks.
    Returns list of {"kind": "patch"|"add", "name": str, "body": str}
    """
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
    """
    Apply all valid patches found in patch_text to source_path.
    Returns list of PatchResult.
    """
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
    """
    Backwards-compatible wrapper. Returns list of human-readable result strings.
    """
    base = Path(__file__).resolve().parent
    path = base / target if not Path(target).is_absolute() else Path(target)
    results = apply_patches(path, patch_text, dry_run=dry_run, create_backup=not dry_run)
    return [str(r) for r in results]
if __name__ == '__main__':
    print('self_modify.py loaded. AST validation and safe patching ready.')