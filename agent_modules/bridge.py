import os, json, re, random, ast, subprocess, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _save(genome):
    with open(os.path.join(BASE, 'genome.json'), 'w') as f:
        json.dump(genome, f, indent=2)

def _load_genome():
    try:
        with open(os.path.join(BASE, 'genome.json')) as f:
            return json.load(f)
    except:
        return {}

def _load_file(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return ''

def _write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def _read_bridge_types():
    path = os.path.join(BASE, 'new_types.bridge')
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}

def _register_bridge_type(ext, handler, description):
    path = os.path.join(BASE, 'new_types.bridge')
    types = _read_bridge_types()
    if ext not in types:
        types[ext] = {'handler': handler, 'description': description}
        _write_file(path, json.dumps(types, indent=2))
        return True
    return False

def _handler_genloop(abs_path, genome):
    try:
        with open(abs_path) as f:
            data = json.load(f)
    except:
        data = {}
    rewrites = []
    if data.get('flow_mode'):
        genome['flow_mode'] = data['flow_mode']
        rewrites.append(f"flow_mode={data['flow_mode']}")
    if data.get('execution_order'):
        genome['execution_order'] = data['execution_order']
        rewrites.append(f"order={data['execution_order']}")
    if data.get('loop_adaptive_turns'):
        genome['loop_adaptive_turns'] = int(data['loop_adaptive_turns'])
        rewrites.append(f"turns={data['loop_adaptive_turns']}")
    if data.get('phases'):
        current = genome.get('execution_phases', [])
        for p in data['phases']:
            if p not in current:
                current.append(p)
                rewrites.append(f"+phase:{p}")
        genome['execution_phases'] = current
    if data.get('remove_phases'):
        current = genome.get('execution_phases', [])
        for p in data['remove_phases']:
            if p in current:
                current.remove(p)
                rewrites.append(f"-phase:{p}")
        genome['execution_phases'] = current
    if rewrites:
        _save(genome)
        print(f'[bridge:genloop] applied {len(rewrites)} struct changes: {"; ".join(rewrites)}')
    return True

def _handler_mutreflect(abs_path, genome):
    try:
        with open(abs_path) as f:
            data = json.load(f)
    except:
        data = {}
    pruned = []
    history = genome.get('history', [])
    op_stats = {}
    for h in history[-20:]:
        mut = h.get('mutation', '')
        scores = h.get('scores', {})
        if 'operator' in mut.lower():
            for op in genome.get('mutation_ops', []):
                if op in mut:
                    op_stats.setdefault(op, {'hits': 0, 'score': 0, 'count': 0})
                    op_stats[op]['count'] += 1
                    avg = sum(scores.values()) / max(len(scores), 1) if scores else 0
                    op_stats[op]['score'] += avg
                    op_stats[op]['hits'] += 1
    custom_ops = genome.get('custom_mutation_ops', {})
    for op_name, op_code in list(custom_ops.items()):
        if op_name in data.get('prune', []):
            del custom_ops[op_name]
            pruned.append(op_name)
            continue
        stats = op_stats.get(op_name, {'hits': 0, 'score': 0, 'count': 0})
        if stats['count'] >= 2 and stats['score'] / stats['count'] < 3.0:
            if random.random() < 0.5:
                del custom_ops[op_name]
                pruned.append(f"{op_name}(low={stats['score']/stats['count']:.1f})")
    if data.get('add_ops'):
        for new_op_name, new_op_code in data['add_ops'].items():
            if new_op_name not in custom_ops:
                custom_ops[new_op_name] = new_op_code
                pruned.append(f"+{new_op_name}")
    if pruned:
        genome['custom_mutation_ops'] = custom_ops
        genome['mutation_ops'] = [op for op in genome.get('mutation_ops', []) if op not in custom_ops or op in custom_ops]
        for op_name in list(custom_ops.keys()):
            if op_name not in genome['mutation_ops']:
                genome['mutation_ops'].append(op_name)
        _save(genome)
        print(f'[bridge:mutreflect] pruned/added ops: {"; ".join(pruned)}')
    return True

def _handler_metaop(abs_path, genome):
    content = _load_file(abs_path)
    if not content:
        return False
    op_name = None
    op_code = content
    if content.strip().startswith('{'):
        try:
            meta = json.loads(content)
            op_name = meta.get('name')
            op_code = meta.get('code', content)
        except:
            pass
    else:
        m = re.search(r"@_register_mutation_op\s*\(\s*['\"]([^'\"]+)['\"]\s*\)", content)
        if m:
            op_name = m.group(1)
    if not op_name or not op_code:
        return False
    custom_ops = genome.get('custom_mutation_ops', {})
    if op_name in custom_ops:
        return False
    try:
        compile(op_code, f'<metaop:{op_name}>', 'exec')
    except SyntaxError:
        return False
    custom_ops[op_name] = op_code
    genome['custom_mutation_ops'] = custom_ops
    if op_name not in genome.get('mutation_ops', []):
        genome.setdefault('mutation_ops', []).append(op_name)
    _save(genome)
    print(f'[bridge:metaop] registered op "{op_name}" from {os.path.basename(abs_path)}')
    return True

def _handler_srcmutate(abs_path, genome):
    try:
        with open(abs_path) as f:
            spec = json.load(f)
    except:
        spec = {}
    target_file = spec.get('target', '')
    if not target_file:
        target_file = random.choice([f for f in os.listdir(os.path.join(BASE, 'agent_modules')) if f.endswith('.py') and f != 'bridge.py'])
    target_path = os.path.join(BASE, 'agent_modules', target_file) if not target_file.startswith('/') else target_file
    if not os.path.exists(target_path):
        return False
    src = _load_file(target_path)
    if not src:
        return False
    original_hash = hashlib.sha256(src.encode()).hexdigest()[:12]
    mutation = spec.get('mutation', 'random')
    lines = src.split('\n')
    if mutation == 'duplicate_random_line' or (mutation == 'random' and random.random() < 0.3):
        idx = random.randrange(1, len(lines))
        lines.insert(idx, lines[idx])
    elif mutation == 'delete_random_line':
        if len(lines) > 5:
            idx = random.randrange(1, len(lines) - 1)
            del lines[idx]
    elif mutation == 'comment_shift':
        for i in range(len(lines)):
            if lines[i].strip().startswith('#'):
                lines[i] = lines[i][1:] if len(lines[i]) > 1 else ''
            elif lines[i].strip() and not lines[i].strip().startswith(("'''", '"""')):
                lines[i] = '# ' + lines[i]
    elif mutation == 'swap_imports':
        import_indices = [i for i, l in enumerate(lines) if re.match(r'^(import|from)\s', l)]
        if len(import_indices) >= 2:
            i, j = random.sample(import_indices, 2)
            lines[i], lines[j] = lines[j], lines[i]
    elif mutation == 'inject_self_rewrite_hook':
        hook = [
            f"# srcmutate:self-rewrite@{random.getrandbits(16):04x}",
            "if random.random() < 0.3:",
            "    import os as _sm_os, hashlib as _sm_hl",
            "    _sm_path = __file__",
            "    _sm_src = open(_sm_path).read()",
            "    _sm_lines = _sm_src.split(chr(10))",
            "    if len(_sm_lines) > 3:",
            "        _sm_i = random.randrange(1, len(_sm_lines) - 1)",
            "        _sm_lines.insert(_sm_i, _sm_lines[_sm_i])",
            "        _sm_new = chr(10).join(_sm_lines)",
            "        try:",
            "            compile(_sm_new, _sm_path, 'exec')",
            "            with open(_sm_path, 'w') as _sm_f: _sm_f.write(_sm_new)",
            "        except SyntaxError: pass",
        ]
        insert_at = 0
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith(('"""', "'''")):
                for j in range(i + 1, len(lines)):
                    if '"""' in lines[j] or "'''" in lines[j]:
                        insert_at = j + 1
                        break
                break
            elif stripped and not stripped.startswith('#') and not stripped.startswith('def '):
                insert_at = i
                break
        for i, hl in enumerate(reversed(hook)):
            lines.insert(insert_at, hl)
    elif mutation == 'rename_random_function':
        tree = ast.parse(src)
        funcs = [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
        targets = [f for f in funcs if not f.name.startswith('_') and f.name != 'run']
        if targets:
            chosen = random.choice(targets)
            new_name = chosen.name + '_' + format(random.getrandbits(10), '03x')
            chosen.name = new_name
            new_src = ast.unparse(tree)
            lines = new_src.split('\n')
    elif mutation == 'invert_logic':
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.Compare):
                if isinstance(node.ops[0], ast.Eq):
                    node.ops[0] = ast.NotEq()
                elif isinstance(node.ops[0], ast.NotEq):
                    node.ops[0] = ast.Eq()
                elif isinstance(node.ops[0], ast.Lt):
                    node.ops[0] = ast.GtE()
                elif isinstance(node.ops[0], ast.Gt):
                    node.ops[0] = ast.LtE()
                elif isinstance(node.ops[0], ast.LtE):
                    node.ops[0] = ast.Gt()
                elif isinstance(node.ops[0], ast.GtE):
                    node.ops[0] = ast.Lt()
        new_src = ast.unparse(tree)
        lines = new_src.split('\n')
    new_content = '\n'.join(lines)
    new_hash = hashlib.sha256(new_content.encode()).hexdigest()[:12]
    if new_hash == original_hash:
        return False
    try:
        compile(new_content, target_path, 'exec')
    except SyntaxError:
        return False
    _write_file(target_path, new_content)
    count = genome.get('bridge_srcmutate_count', 0) + 1
    genome['bridge_srcmutate_count'] = count
    genome.setdefault('bridge_mutations', []).append({
        'file': os.path.basename(target_path), 'mutation': mutation,
        'from_hash': original_hash, 'to_hash': new_hash, 'gen': genome.get('generation', 0)
    })
    _save(genome)
    print(f'[bridge:srcmutate] mutated {os.path.basename(target_path)} with {mutation} ({original_hash}->{new_hash})')
    return True

HANDLERS = {
    '.genloop': _handler_genloop,
    '.mutreflect': _handler_mutreflect,
    '.metaop': _handler_metaop,
    '.srcmutate': _handler_srcmutate,
}

def _ensure_type_registry(genome):
    registered = _read_bridge_types()
    registry = genome.setdefault('type_registry', {})
    for ext, cfg in registered.items():
        handler_name = cfg.get('handler', 'bridge')
        if ext not in registry:
            registry[ext] = {
                'handler': handler_name,
                'description': cfg.get('description', '')
            }
            print(f'[bridge] registered type {ext} -> {handler_name}')
    return registry

def _resolve_handler(ext, cfg):
    handler_name = cfg.get('handler', 'bridge')
    if handler_name in HANDLERS:
        return HANDLERS[handler_name]
    if ext in HANDLERS:
        return HANDLERS[ext]
    return None

def _find_type_files(ext):
    found = []
    try:
        for f in os.listdir(BASE):
            if f.endswith(ext):
                found.append(os.path.join(BASE, f))
    except:
        pass
    if ext == '.metaop':
        metaop_dir = os.path.join(BASE, 'metaops')
        if os.path.isdir(metaop_dir):
            for f in os.listdir(metaop_dir):
                if f.endswith('.metaop'):
                    found.append(os.path.join(metaop_dir, f))
    return found

def _apply_bridge_types(genome):
    registry = genome.get('type_registry', {})
    results = []
    for ext, cfg in list(registry.items()):
        handler_fn = _resolve_handler(ext, cfg)
        if handler_fn is None:
            continue
        found_files = _find_type_files(ext)
        for fpath in found_files:
            try:
                ok = handler_fn(fpath, genome)
                if ok:
                    handler_name = cfg.get('handler', 'bridge')
                    results.append(f'{os.path.basename(fpath)}->{handler_name}')
            except Exception as e:
                print(f'[bridge] handler for {ext} failed on {fpath}: {e}')
    return results

def _weave_cross_module_calls(genome):
    mod_dir = os.path.join(BASE, 'agent_modules')
    mods = [f for f in os.listdir(mod_dir) if f.endswith('.py') and not f.startswith('__')]
    if len(mods) < 2:
        return []
    results = []
    random.shuffle(mods)
    pairs = list(zip(mods, mods[1:] + mods[:1]))[:len(mods)//2]
    for src_mod, dst_mod in pairs:
        src_path = os.path.join(mod_dir, src_mod)
        dst_path = os.path.join(mod_dir, dst_mod)
        src_code = _load_file(src_path)
        dst_code = _load_file(dst_path)
        if not src_code or not dst_code:
            continue
        dst_name = dst_mod.replace('.py', '')
        dst_funcs = []
        try:
            tree = ast.parse(dst_code)
            for node in ast.iter_child_nodes(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith('_'):
                    dst_funcs.append(node.name)
        except:
            pass
        if not dst_funcs:
            continue
        target_func = random.choice(dst_funcs)
        import_line = f'from agent_modules.{dst_name} import {target_func}'
        if import_line in src_code:
            continue
        call_line = f'\n# bridge: cross-module weave {src_mod}->{dst_mod}.{target_func}\ntry:\n    {target_func}()\nexcept:\n    pass\n'
        new_src = import_line + '\n' + src_code + call_line
        try:
            compile(new_src, src_path, 'exec')
            _write_file(src_path, new_src)
            results.append(f'{src_mod}->{dst_mod}.{target_func}')
            print(f'[bridge] cross-weave: {src_mod} imports {dst_mod}.{target_func}')
        except:
            pass
    return results

def _generate_new_bridge_type(genome):
    gen = genome.get('generation', 0)
    new_name = 'bridge_' + format(random.getrandbits(12), '03x')
    ext = '.' + new_name
    handler = '_handler_' + new_name
    bridge_file = os.path.join(BASE, new_name + '.bridge')
    if not os.path.exists(bridge_file):
        bridge_data = {ext: {'handler': handler, 'description': 'auto-generated type gen=' + str(gen)}}
        _write_file(bridge_file, json.dumps(bridge_data, indent=2))
        if handler not in HANDLERS:
            HANDLERS[handler] = lambda fp, g: _handler_srcmutate(fp, g)
        print(f'[bridge] created new type {ext} in {new_name}.bridge')
        return ['wrote ' + new_name + '.bridge']
    return []

def _write_metaop(genome):
    metaop_dir = os.path.join(BASE, 'metaops')
    os.makedirs(metaop_dir, exist_ok=True)
    metaop_count = len([f for f in os.listdir(metaop_dir) if f.endswith('.metaop')])
    if metaop_count <= 3:
        op_name = 'mutation_op_bridge_auto_' + format(random.getrandbits(8), '02x')
        op_code = "@_register_mutation_op('" + op_name + "')\ndef " + op_name + "(lines, funcs, target_name):\n    if not lines or len(lines) < 2:\n        return lines\n    r = list(lines)\n    r.insert(random.randrange(len(r)), '# bridge-auto-mutate ' + str(genome.get('generation', 0)))\n    return r\n"
        metaop_path = os.path.join(metaop_dir, op_name + '.metaop')
        if not os.path.exists(metaop_path):
            _write_file(metaop_path, op_code)
            print(f'[bridge] wrote auto-metaop {op_name}')
            return ['wrote ' + op_name + '.metaop']
    return []

def run(genome):
    gen = genome.get('generation', 0)
    results = []
    registry = _ensure_type_registry(genome)
    applied = _apply_bridge_types(genome)
    results.extend(applied)
    if not results or random.random() < 0.3:
        types_before = len(_read_bridge_types())
        new_types = _generate_new_bridge_type(genome)
        results.extend(new_types)
        if len(_read_bridge_types()) > types_before:
            _ensure_type_registry(genome)
    metaops = _write_metaop(genome)
    results.extend(metaops)
    cross = _weave_cross_module_calls(genome)
    results.extend(cross)
    if results:
        _save(genome)
    return '[bridge] gen=' + str(gen) + ' ' + ('; '.join(results) if results else 'idle')
