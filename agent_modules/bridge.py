import os, json, re, random
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _save(genome):
    with open(os.path.join(BASE, 'genome.json'), 'w') as f:
        json.dump(genome, f, indent=2)

def run(genome):
    gen = genome.get("generation", 0)
    results = []
    bridge_types = genome.get('pending_bridge_handlers', {})
    if bridge_types:
        for ext, cfg in list(bridge_types.items()):
            handler_name = cfg.get('handler', '')
            mod_path = os.path.join(BASE, 'agent_modules', 'bridge.py')
            if os.path.exists(mod_path):
                with open(mod_path) as f:
                    mod_src = f.read()
                if handler_name not in mod_src:
                    stub_lines = []
                    stub_lines.append('')
                    stub_lines.append('def ' + handler_name + '(abs_path, genome):')
                    stub_lines.append('    try:')
                    stub_lines.append('        with open(abs_path) as f:')
                    stub_lines.append('            data = json.load(f)')
                    stub_lines.append('    except:')
                    stub_lines.append('        return False')
                    stub_lines.append('    applied = 0')
                    stub_lines.append('    items = data.items() if isinstance(data, dict) else [(0, data)]')
                    stub_lines.append('    for k, v in items:')
                    stub_lines.append("        genome[k] = v")
                    stub_lines.append('        applied += 1')
                    stub_lines.append('    if applied:')
                    stub_lines.append("        genome.setdefault('type_registry', {})['" + ext + "'] = {'handler': 'bridge', 'description': '" + cfg.get('description', '') + "'}")
                    stub_lines.append('        _save(genome)')
                    stub_lines.append("        print('[bridge] auto-wired pending handler " + handler_name + " for " + ext + "')")
                    stub_lines.append('        return True')
                    stub_lines.append('    return False')
                    stub = '\n'.join(stub_lines)
                    with open(mod_path, 'a') as f:
                        f.write(stub)
                    results.append("stub " + handler_name)
                    genome['_bridge_stubs_created'] = genome.get('_bridge_stubs_created', 0) + 1
    if not bridge_types and random.random() < 0.3:
        new_name = "bridge_" + format(random.getrandbits(12), '03x')
        ext = '.' + new_name
        handler = '_bridge_handler_' + new_name
        bridge_file = os.path.join(BASE, new_name + '.bridge')
        if not os.path.exists(bridge_file):
            bridge_data = {ext: {"handler": handler, "description": "auto-generated type gen=" + str(gen)}}
            with open(bridge_file, 'w') as f:
                json.dump(bridge_data, f, indent=2)
            results.append("wrote " + new_name + ".bridge")
    metaop_dir = os.path.join(BASE, 'metaops')
    os.makedirs(metaop_dir, exist_ok=True)
    metaop_count = len([f for f in os.listdir(metaop_dir) if f.endswith('.metaop')])
    if metaop_count < 3:
        op_name = "mutation_op_bridge_auto_" + format(random.getrandbits(8), '02x')
        op_code = "@_register_mutation_op('" + op_name + "')\ndef " + op_name + "(lines, funcs, target_name):\n    if not lines or len(lines) < 2:\n        return lines\n    r = list(lines)\n    r.insert(random.randrange(len(r)), '# bridge-auto-mutate ' + str(genome.get('generation',0)))\n    return r\n"
        metaop_path = os.path.join(metaop_dir, op_name + '.metaop')
        if not os.path.exists(metaop_path):
            with open(metaop_path, 'w') as f:
                f.write(op_code)
            results.append("wrote " + op_name + ".metaop")
    if results:
        _save(genome)
    return "[bridge] gen=" + str(gen) + " " + ("; ".join(results) if results else "idle")
