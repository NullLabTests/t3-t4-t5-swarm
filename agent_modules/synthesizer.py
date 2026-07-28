import os, json, re, random, ast, hashlib, sys
from pathlib import Path

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import self_modify

def _load_log():
    log_path = os.path.join(BASE, 'echo_conversation.jsonl')
    if not os.path.exists(log_path):
        return []
    with open(log_path) as f:
        return [json.loads(line) for line in f if line.strip()]

def _load_genome():
    with open(os.path.join(BASE, 'genome.json')) as f:
        return json.load(f)

def _save_genome(g):
    with open(os.path.join(BASE, 'genome.json'), 'w') as f:
        json.dump(g, f, indent=2)

def _read_file(path):
    with open(path) as f:
        return f.read()

def _write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _parse_code_blocks(text):
    blocks = []
    for m in re.finditer(r'```(\w+)?:?([^\n]*?)\n(.*?)```', text, re.DOTALL):
        filename = m.group(2).strip() or ''
        code = m.group(3).strip()
        if filename:
            safe = filename.lstrip('/').replace('..', '')
            abs_path = os.path.join(BASE, safe)
            blocks.append({'path': abs_path, 'filename': filename, 'code': code})
    return blocks

def _parse_patches(text):
    patches = re.findall(r'##patch:(\w+)\n(.*?)(?=##endpatch|\Z)', text, re.DOTALL)
    return [{'target': name, 'body': body.strip()} for name, body in patches]

def _parse_extensions(text):
    blocks = re.findall(r'##extend:([\w.\[\]]+)\n(.*?)(?=##endextend|\Z)', text, re.DOTALL)
    return [{'path': p, 'body': b.strip()} for p, b in blocks]

def _parse_sets(text):
    blocks = re.findall(r'##set:([\w.]+)\n(.*?)(?=##endset|\Z)', text, re.DOTALL)
    return [{'path': p, 'body': b.strip()} for p, b in blocks]

def _parse_hooks(text):
    blocks = re.findall(r'##hook:(\w+)\n(.*?)(?=##endhook|\Z)', text, re.DOTALL)
    return [{'point': p, 'code': c.strip()} for p, c in blocks]

def _parse_mutation_ops(text):
    ops = {}
    for m in re.finditer(r'def (mutation_op_\w+)\(', text):
        name = m.group(1)
        body_match = re.search(
            rf'(def {re.escape(name)}\(.*?\):.*?)(?=\n\ndef |\nclass |\n#|\n\s*@|\Z)',
            text, re.DOTALL
        )
        if body_match:
            ops[name] = body_match.group(1).strip()
    return ops

def _detect_conflicts(proposals):
    conflicts = []
    seen_targets = {}
    for i, p in enumerate(proposals):
        for patch in p.get('patches', []):
            tgt = patch['target']
            if tgt in seen_targets:
                conflicts.append({
                    'type': 'patch_conflict',
                    'target': tgt,
                    'agents': [seen_targets[tgt]['agent'], p['agent']]
                })
            else:
                seen_targets[tgt] = {'agent': p['agent'], 'index': i}
    return conflicts

def _extract_functions(source=None):
    if source is None:
        source = _read_file(os.path.join(BASE, 'auto-echo.py'))
    funcs = {}
    pattern = re.compile(
        r'(def (\w+)\(.*?\):)\n((?:    (?:.*\n?)*?))(?=\n\ndef |\nclass |\n#|---|\Z)',
        re.MULTILINE
    )
    for match in pattern.finditer(source):
        header = match.group(1)
        name = match.group(2)
        body = match.group(3)
        funcs[name] = (header, body)
    return funcs

def _synthesize_patches(proposals, genome):
    auto_echo_source = _read_file(os.path.join(BASE, 'auto-echo.py'))
    funcs = _extract_functions(auto_echo_source)
    applied = []
    for prop in proposals:
        for patch in prop.get('patches', []):
            target = patch['target']
            body = patch['body']
            if target not in funcs:
                continue
            patch_text = f'##patch:{target}\n{body}\n##endpatch'
            try:
                results = self_modify.apply_patch(patch_text, target='auto-echo.py', dry_run=False)
                if results:
                    applied.append({
                        'agent': prop['agent'],
                        'target': target,
                        'result': results
                    })
            except Exception as e:
                pass
    return applied

def _register_new_ops(proposals, genome):
    registered = []
    for prop in proposals:
        for op_name, op_code in prop.get('mutation_ops', {}).items():
            if op_name not in genome.get('mutation_ops', []):
                genome.setdefault('mutation_ops', []).append(op_name)
                genome.setdefault('custom_mutation_ops', {})[op_name] = op_code
                registered.append(op_name)
    if registered:
        _save_genome(genome)
    return registered

def _apply_extensions(proposals, genome):
    applied = []
    for prop in proposals:
        for ext in prop.get('extensions', []):
            try:
                val = json.loads(ext['body'])
            except json.JSONDecodeError:
                continue
            parts = ext['path'].replace('[]', '').split('.')
            target = genome
            for part in parts[:-1]:
                target = target.setdefault(part, {})
            key = parts[-1]
            if key in target and isinstance(target[key], list) and isinstance(val, dict):
                existing_ids = {e.get('id') for e in target[key] if isinstance(e, dict)}
                if val.get('id', '') not in existing_ids:
                    target[key].append(val)
                    applied.append(f"extend:{ext['path']}")
            elif key in target and isinstance(target[key], list) and isinstance(val, list):
                target[key].extend(val)
                applied.append(f"extend:{ext['path']}")
            else:
                target[key] = val
                applied.append(f"set:{ext['path']}")
        for s in prop.get('sets', []):
            parts = s['path'].split('.')
            target = genome
            for part in parts[:-1]:
                target = target.setdefault(part, {})
            try:
                target[parts[-1]] = json.loads(s['body'])
            except (json.JSONDecodeError, ValueError):
                target[parts[-1]] = s['body']
            applied.append(f"set:{s['path']}")
    if applied:
        _save_genome(genome)
    return applied

def _apply_hooks(proposals, genome):
    import agent_hooks
    applied = []
    for prop in proposals:
        for hook in prop.get('hooks', []):
            if hook['point'] in agent_hooks.HOOK_POINTS:
                agent_hooks.add_hook(genome, hook['point'], hook['code'], source='synthesizer')
                applied.append(f"hook:{hook['point']}")
    return applied

def _write_code_files(proposals, genome):
    written = []
    for prop in proposals:
        for block in prop.get('code_blocks', []):
            os.makedirs(os.path.dirname(block['path']), exist_ok=True)
            _write_file(block['path'], block['code'])
            try:
                ast.parse(block['code'])
                stat = 'syntax OK'
            except SyntaxError as e:
                stat = f'INVALID: {e.msg}'
            written.append(f"{prop['agent']}:{block['filename']}({stat})")
    return written

def run(genome):
    gen = genome.get('generation', 0)
    log = _load_log()
    recent = [e for e in log[-20:] if e.get('text')]
    proposals = []
    for entry in recent:
        text = entry.get('text', '')
        agent = entry.get('agent', 'unknown')
        proposals.append({
            'agent': agent,
            'code_blocks': _parse_code_blocks(text),
            'patches': _parse_patches(text),
            'extensions': _parse_extensions(text),
            'sets': _parse_sets(text),
            'hooks': _parse_hooks(text),
            'mutation_ops': _parse_mutation_ops(text),
        })
    active_proposals = [p for p in proposals if p['patches'] or p['code_blocks'] or p['extensions']]
    if not active_proposals:
        return f"[synthesizer] gen={gen}: no active proposals to synthesize"
    conflicts = _detect_conflicts(active_proposals)
    patch_results = _synthesize_patches(active_proposals, genome)
    op_registrations = _register_new_ops(active_proposals, genome)
    ext_applied = _apply_extensions(active_proposals, genome)
    hook_applied = _apply_hooks(active_proposals, genome)
    written_files = _write_code_files(active_proposals, genome)
    auto_mutation = False
    if random.random() < 0.3:
        try:
            funcs = _extract_functions()
            available = [n for n in funcs if not n.startswith('_') and n not in (
                'load_genome', 'save_genome', 'sigint_handler', 'main',
                '_read_auto_echo', 'run_generation', 'update_genome'
            )]
            if available:
                target = random.choice(available)
                all_ops = list(genome.get('mutation_ops', []))
                if all_ops:
                    op = random.choice(all_ops)
                    new_body = _synthesize_single_mutation(funcs, target, op, genome)
                    if new_body:
                        patch_text = f'##patch:{target}\n{new_body}\n##endpatch'
                        self_modify.apply_patch(patch_text, target='auto-echo.py', dry_run=False)
                        auto_mutation = True
        except Exception as e:
            pass
    results = {
        'proposals_scanned': len(active_proposals),
        'conflicts_found': len(conflicts),
        'patches_applied': len(patch_results),
        'ops_registered': len(op_registrations),
        'extensions_applied': len(ext_applied),
        'hooks_applied': len(hook_applied),
        'files_written': len(written_files),
        'auto_mutation': auto_mutation,
    }
    genome['synthesis_results'] = results
    genome['synthesis_count'] = genome.get('synthesis_count', 0) + 1
    genome['last_synthesis_gen'] = gen
    _save_genome(genome)
    summary = (
        f"[synthesizer] gen={gen}: scanned={len(active_proposals)} "
        f"patches={len(patch_results)} ops={len(op_registrations)} "
        f"ext={len(ext_applied)} hooks={len(hook_applied)} "
        f"files={len(written_files)} auto_mut={auto_mutation}"
    )
    if conflicts:
        summary += f" conflicts={len(conflicts)}"
    return summary

def _synthesize_single_mutation(funcs, target_name, operator, genome):
    _, body = funcs[target_name]
    lines = [l for l in body.split('\n') if l.strip()]
    if not lines or len(lines) < 2:
        return None
    custom_ops = genome.get('custom_mutation_ops', {})
    if operator in custom_ops:
        op_code = custom_ops[operator]
        local_ns = {'random': random, 're': re}
        try:
            exec(compile(op_code, f'<synth:{operator}>', 'exec'), local_ns)
            result = local_ns[operator](lines, funcs, target_name)
            if result and result != lines:
                return '\n'.join(result)
        except Exception:
            pass
    return None
