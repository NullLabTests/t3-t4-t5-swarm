#!/usr/bin/env python3
"""Echo: autonomous T3-T4-T5 multi-agent swarm.

Drives itself: LLM generates each agent's contribution → Piper TTS speaks it
→ git commits + pushes → critic scores → genome mutates → repeat.
Agents can write code files which get committed alongside utterances.

Run:  python3 auto-echo.py
Stop: Ctrl+C (graceful shutdown after current utterance)
"""
import pyaudio, wave, struct, os, sys, json, subprocess, re, time, signal, random
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
VOICES_DIR = os.path.join(BASE, 'voices')
LOG_FILE = os.path.join(BASE, 'echo_conversation.jsonl')
GENOME_FILE = os.path.join(BASE, 'genome.json')
LLM_MODEL = 'opencode/deepseek-v4-flash-free'

sys.path.insert(0, BASE)
import self_modify

VOICE_MAP = {
    "explorer": "southern", "analyzer": "alan", "synthesizer": "lessac",
    "critic": "amy", "mutator": "lessac",
}

def _load_system_prompt(genome=None):
    if genome is None:
        genome = load_genome()
    return genome['system_prompt']

def _load_code_rule(genome=None):
    if genome is None:
        genome = load_genome()
    return genome['code_rule']

running = True

def sigint_handler(sig, frame):
    global running
    print("\n[stop] Shutting down after current utterance...")
    running = False

signal.signal(signal.SIGINT, sigint_handler)

def load_genome():
    with open(GENOME_FILE) as f:
        return json.load(f)

def save_genome(g):
    with open(GENOME_FILE, 'w') as f:
        json.dump(g, f, indent=2)

def load_log():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE) as f:
        return [json.loads(line) for line in f if line.strip()]

def append_log(role, agent_name, text):
    entry = json.dumps({
        "time": datetime.now(timezone.utc).isoformat(),
        "role": role, "agent": agent_name, "text": text
    })
    with open(LOG_FILE, 'a') as f:
        f.write(entry + '\n')

def strip_markdown(text):
    text = re.sub(r'\*{1,3}', '', text)
    text = re.sub(r'#{1,6}\s*', '', text)
    text = re.sub(r'_{1,3}', '', text)
    text = re.sub(r'`{1,3}', '', text)
    text = re.sub(r'~~', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def extract_code_blocks(text):
    blocks = []
    pattern = re.compile(r'```(\w+)?:?([^\n]*?)\n(.*?)```', re.DOTALL)
    for match in pattern.finditer(text):
        lang = match.group(1) or ''
        filename = match.group(2).strip() or ''
        code = match.group(3).strip()
        if filename:
            safe = filename.lstrip('/').replace('..', '')
            abs_path = os.path.join(BASE, safe)
            blocks.append((abs_path, code, filename))
    return blocks

def _register_ops_from_file(fpath, genome):
    if 'custom_mutation_ops' not in genome:
        genome['custom_mutation_ops'] = {}
    if 'mutation_ops' not in genome:
        genome['mutation_ops'] = list(genome.get('mutation_ops', []))
    registered = []
    try:
        with open(fpath) as f:
            content = f.read()
    except:
        return registered
    for m in re.finditer(r'def (mutation_op_\w+)\(', content):
        op_name = m.group(1)
        if op_name in genome['mutation_ops']:
            continue
        func_match = re.search(
            rf'(def {re.escape(op_name)}\(.*?\):.*?)(?=\n\ndef |\nclass |\n#|\Z)',
            content, re.DOTALL
        )
        if func_match:
            genome['mutation_ops'].append(op_name)
            genome['custom_mutation_ops'][op_name] = func_match.group(1).strip()
            registered.append(op_name)
            print(f"[mutation-op] registered '{op_name}' from {fpath}")
    if registered:
        save_genome(genome)
    return registered

def extend_genome(text, genome):
    """Parse genome extension blocks from agent output.
    
    ##extend:field.subfield[]
    {json object}
    ##endextend
    
    Agents use this to add new spawn_pool entries, mutation_ops, etc.
    
    ##set:field.name
    value
    ##endset
    
    Agents use this to set scalar genome values (e.g. mutation_rate, topic).
    """
    if genome is None:
        genome = load_genome()
    extensions = re.findall(
        r'##extend:([\w.\[\]]+)\n(.*?)(?=##endextend|\Z)',
        text, re.DOTALL
    )
    sets = re.findall(
        r'##set:([\w.]+)\n(.*?)(?=##endset|\Z)',
        text, re.DOTALL
    )
    applied = []
    for path_str, body in extensions:
        body = body.strip()
        try:
            obj = json.loads(body)
        except json.JSONDecodeError:
            applied.append(f"FAILED: {path_str} invalid JSON")
            continue
        parts = path_str.replace('[]', '').split('.')
        target = genome
        for part in parts[:-1]:
            if part not in target:
                target[part] = {}
            target = target[part]
        key = parts[-1]
        if isinstance(target.get(key), list) and isinstance(obj, dict):
            existing_ids = {e.get('id') for e in target[key] if isinstance(e, dict)}
            new_id = obj.get('id', '')
            if new_id and new_id not in existing_ids:
                target[key].append(obj)
                applied.append(f"extended {path_str} with {new_id}")
        elif key in target and isinstance(target[key], list) and isinstance(obj, list):
            target[key].extend(obj)
            applied.append(f"extended {path_str} with {len(obj)} items")
        else:
            target[key] = obj
            applied.append(f"set {path_str} = {str(obj)[:50]}")
    for path_str, val_str in sets:
        val_str = val_str.strip()
        try:
            val = json.loads(val_str)
        except (json.JSONDecodeError, ValueError):
            val = val_str
        parts = path_str.split('.')
        target = genome
        for part in parts[:-1]:
            if part not in target:
                target[part] = {}
            target = target[part]
        key = parts[-1]
        old = target.get(key)
        target[key] = val
        applied.append(f"set {path_str} = {str(val)[:50]} (was {str(old)[:30]})")
    if applied:
        genome.setdefault('genome_extensions', []).extend(applied)
        save_genome(genome)
    return applied


def write_code_files(blocks):
    genome = load_genome()
    written = []
    for abs_path, code, filename in blocks:
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, 'w') as f:
            f.write(code)
        written.append(filename)
        print(f"[code] wrote {filename} ({len(code)} bytes)")
        if filename.endswith('.py') and not filename.startswith('auto-echo'):
            reg = _register_ops_from_file(abs_path, genome)
            if reg:
                genome = load_genome()
    return written

def apply_self_patches(text):
    patches = self_modify.extract_patch_blocks(text)
    if not patches:
        return []
    results = self_modify.apply_patch(text)
    for r in results:
        print(f"[patch] {r}")
    return results

def strip_code_blocks(text):
    return re.sub(r'```\w*:?[^\n]*\n.*?```', '', text, flags=re.DOTALL)

def speak(role, text):
    voice = VOICE_MAP.get(role, "amy")
    model_path = os.path.join(VOICES_DIR, f'{voice}.onnx')
    if not os.path.exists(model_path):
        print(f"[speak] Voice model not found: {model_path}")
        return
    clean = strip_markdown(strip_code_blocks(text))
    if not clean:
        return
    try:
        proc = subprocess.Popen(
            ['piper', '--model', model_path, '--output-raw'],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        sox = subprocess.Popen(
            ['sox', '-t', 'raw', '-r', '22050', '-e', 'signed', '-b', '16', '-c', '1',
             '-', '-t', 'raw', '-', 'pitch', '-300'],
            stdin=proc.stdout, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        aplay_p = subprocess.Popen(
            ['aplay', '-r', '22050', '-f', 'S16_LE', '-c', '1'],
            stdin=sox.stdout, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        proc.stdin.write(clean.encode('utf-8'))
        proc.stdin.close()
        proc.wait(); sox.wait(); aplay_p.wait()
    except Exception as e:
        print(f"[speak] Error: {e}")

REPETITION_THRESHOLD = 0.5
MIN_WORDS = 8
MAX_WORDS = 2000  # allow code blocks

def is_repetitive(text):
    words = text.split()
    if len(words) < 5:
        return False
    bigrams = [' '.join(words[i:i+2]) for i in range(len(words)-1)]
    if not bigrams:
        return False
    return max(bigrams.count(b) for b in set(bigrams)) / len(bigrams) > REPETITION_THRESHOLD

def has_gibberish(text):
    words = text.split()
    if len(words) < 3:
        return True
    unique = len(set(w.lower() for w in words))
    return unique < 3

def llm_generate(prompt, max_attempts=3, timeout_sec=120):
    for attempt in range(max_attempts):
        try:
            result = subprocess.run(
                ['opencode', 'run', prompt, '-m', LLM_MODEL],
                capture_output=True, text=True, timeout=timeout_sec)
            if result.returncode == 0:
                text = result.stdout.strip()
                wc = len(text.split())
                has_code = '```' in text
                bad = (wc < MIN_WORDS and not has_code) or is_repetitive(text) or has_gibberish(text)
                if text and not bad:
                    return text
                else:
                    print(f"[llm] Low quality (words={wc}, code={has_code}), retry {attempt+1}")
        except subprocess.TimeoutExpired:
            print(f"[llm] Timeout (attempt {attempt+1}), retrying...")
        except Exception as e:
            print(f"[llm] Error: {e}")
        if attempt < max_attempts - 1:
            prompt += "\n\nYour previous attempt was too long, too short, or repetitive. Be more direct and original."
        time.sleep(1)
    return None

def build_agent_prompt(agent_def, topic, recent_log):
    genome = load_genome()
    system = _load_system_prompt(genome)
    code_rule = _load_code_rule(genome)
    context = ""
    for entry in recent_log[-4:]:
        text = strip_markdown(strip_code_blocks(entry['text']))
        context += f"{entry['agent']}: {text[:200]}\n\n"
    extra = ""
    if agent_def['id'] not in ('critic',):
        extra = code_rule + "\n"
    call_to_action = genome.get('agent_call_to_action', '')
    return (
        f"{system}\n\n"
        f"You are {agent_def['id']}. Role: {agent_def.get('prompt', 'contribute.')}\n\n"
        f"Topic: {topic}\n\n"
        f"Recent context:\n{context}\n"
        f"{call_to_action}"
    )

def build_critic_prompt(topic, gen_log, code_files_written=None):
    genome = load_genome()
    system = _load_system_prompt(genome)
    template = genome.get('critic_prompt_template',
        "You are the Critic. Score each contribution 0-10 based on whether it produced actual code changes.\n"
        "Contributions that only discussed ideas without writing code get 0-3.\n"
        "Contributions that wrote working code get 7-10.")
    context = ""
    for entry in gen_log:
        text = entry['text'][:300]
        context += f"[{entry['agent']}]: {text}\n\n"
    code_note = ""
    if code_files_written:
        code_note = f"Code files written this generation: {', '.join(code_files_written)}. Vote on whether to keep them.\n"
    return (
        f"{system}\n\n"
        f"{template}\n\n"
        f"Topic: {topic}\n\n"
        f"{code_note}"
        f"Contributions:\n{context}\n"
        f"On your LAST LINE output JSON: {{\"agent_id\": score, ...}} including yourself.\n"
        f"Score now:"
    )

def extract_scores(text):
    json_match = re.search(r'\{[^}]+\}', text)
    if json_match:
        try:
            scores = json.loads(json_match.group())
            return {k.lower(): v for k, v in scores.items() if isinstance(v, (int, float))}
        except json.JSONDecodeError:
            pass
    return None

def git_commit_push(label, text, is_genome=False, gen=None, novelty=None):
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True)
        if not status.stdout.strip():
            print(f"[git] nothing to commit for {label}")
            return
        summary = text[:80].replace('\n', ' ').strip()
        if is_genome:
            msg = f"[genome] {summary}"
        else:
            gen_str = f" | gen={gen}" if gen else ""
            nov_str = f" | novelty={novelty}" if novelty else ""
            msg = f"[{label.lower()}] {summary}{gen_str}{nov_str}"
        r = subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True, text=True)
        result = subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(f"[git] pushed: {msg[:60]}")
        else:
            print(f"[git] push stderr: {result.stderr[:200]}")
    except subprocess.TimeoutExpired:
        print(f"[git] push timeout, retrying...")
        try:
            subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, timeout=60)
        except:
            pass
    except Exception as e:
        print(f"[git] Error: {e}")

def run_generation(genome):
    gen = genome["generation"] + 1
    topic = genome["topic"]
    print(f"\n{'='*60}")
    print(f"Generation {gen} | Topic: {topic}")
    print(f"{'='*60}")

    agents = genome["agents"]
    order = genome.get("execution_order", None)
    if order == "shuffle":
        random.shuffle(agents)
        print(f"[order] shuffled execution order")
    elif isinstance(order, list):
        id_order = [a.lower() for a in order]
        ordered = [a for a in agents if a["id"].lower() in id_order]
        remaining = [a for a in agents if a["id"].lower() not in id_order]
        ordered.sort(key=lambda a: id_order.index(a["id"].lower()))
        agents = ordered + remaining
        print(f"[order] custom execution order: {[a['id'] for a in ordered]}")
    gen_log = []
    all_written_files = []

    for agent in agents:
        if not running:
            return None
        aid = agent["id"]
        if aid == "critic":
            continue
        name = aid.capitalize()
        print(f"\n--- {name} ---")
        prompt = build_agent_prompt(agent, topic, load_log())
        text = llm_generate(prompt)
        if not text:
            print(f"[{aid}] LLM returned empty, skipping")
            continue

        blocks = extract_code_blocks(text)
        written_files = write_code_files(blocks)
        all_written_files.extend(written_files)

        patches = apply_self_patches(text)
        if patches:
            written_files.append(f"#patch:{len(patches)}blocks")
            all_written_files.extend(written_files)
            print(f"[patch] auto-echo.py modified: {patches}")

        genome_exts = extend_genome(text, None)
        if genome_exts:
            print(f"[genome-ext] {genome_exts}")
            genome = load_genome()

        text_clean = strip_markdown(strip_code_blocks(text))

        print(f"{name}: {text_clean[:150]}...")
        speak(aid, text_clean)
        append_log(aid, name, text_clean)

        push_label = name
        if written_files:
            push_label = f"{name}+code:{','.join(written_files)}"
        git_commit_push(push_label, text_clean, gen=gen, novelty=len(written_files))
        gen_log.append({"agent": name, "id": aid, "text": text_clean})
        time.sleep(1)

    if not running:
        return None

    print(f"\n--- Critic ---")
    prompt = build_critic_prompt(topic, gen_log, all_written_files or None)
    text = llm_generate(prompt)
    if not text:
        print("[critic] LLM returned empty")
        return None
    text_clean = strip_markdown(strip_code_blocks(text))
    print(f"Critic: {text_clean[:200]}...")
    speak("critic", text_clean)
    append_log("critic", "Critic", text_clean)
    git_commit_push("Critic", text_clean, gen=gen)
    gen_log.append({"agent": "Critic", "id": "critic", "text": text_clean})

    scores = extract_scores(text)
    if scores:
        print(f"\nScores: {scores}")
    else:
        print(f"[warn] Could not parse scores from critic.")

    update_genome(genome, gen, scores or {}, topic)
    return gen

def update_genome(genome, gen, scores, topic):
    genome["generation"] = gen
    avg = sum(scores.values()) / len(scores) if scores else 0
    if avg > genome.get("best_score", 0):
        genome["best_score"] = round(avg, 1)

    for agent in genome["agents"]:
        aid = agent["id"]
        if aid in scores:
            agent["score"] = scores[aid]
            if scores[aid] < genome["prune_threshold"]:
                agent["low_score_streak"] = agent.get("low_score_streak", 0) + 1
            else:
                agent["low_score_streak"] = 0
        agent["lifespan"] = agent.get("lifespan", 0) + 1

    history_entry = {
        "generation": gen,
        "scores": dict(scores),
        "average": round(avg, 1) if scores else 0,
        "mutation": ""
    }

    mutation_desc = []
    spawning_candidates = [a for a in genome["agents"]
                          if a["id"] in scores and scores[a["id"]] >= genome["spawn_threshold"]]
    if spawning_candidates:
        parent = max(spawning_candidates, key=lambda a: scores[a["id"]])
        child = spawn_child(parent, genome["agents"], genome)
        if child:
            genome["agents"].append(child)
            mutation_desc.append(f"{parent['id']} spawned {child['id']}")

    for agent in list(genome["agents"]):
        if agent.get("low_score_streak", 0) >= genome.get("prune_generations", 2):
            genome["agents"] = [a for a in genome["agents"] if a["id"] != agent["id"]]
            mutation_desc.append(f"{agent['id']} pruned")

    custom_registered = _register_custom_ops_from_code(genome)
    if custom_registered:
        mutation_desc.append(f"custom_ops: {','.join(custom_registered)}")

    code_muts = mutate_genome(genome, gen)
    code_path_muts = code_path_mutation(genome, gen)
    ext_muts = genome.get('genome_extensions', [])
    if ext_muts:
        mutation_desc.append(f"extensions: {len(ext_muts)} total")
    all_muts = mutation_desc + code_muts + code_path_muts
    if all_muts:
        history_entry["mutation"] = "; ".join(all_muts)
    genome.setdefault("history", []).append(history_entry)
    save_genome(genome)
    print(f"Genome updated to generation {gen}")
    git_commit_push("genome", f"Gen {gen} avg {history_entry['average']}/10", is_genome=True, gen=gen)
def _read_auto_echo():
    with open(os.path.join(BASE, 'auto-echo.py')) as f:
        return f.read()


def _extract_functions(source=None):
    if source is None:
        source = _read_auto_echo()
    funcs = {}
    pattern = re.compile(r'(def (\w+)\(.*?\):)\n((?:    (?:.*\n?)*?))(?=\n\ndef |\nclass |\n#|---|\Z)', re.MULTILINE)
    for match in pattern.finditer(source):
        header = match.group(1)
        name = match.group(2)
        body = match.group(3)
        funcs[name] = (header, body)
    return funcs


def _get_mutation_ops(genome=None):
    if genome is None:
        genome = load_genome()
    return list(genome.get('mutation_ops', []))


def _get_forbidden_targets(genome=None):
    """Read forbidden mutation targets from genome, NO hardcoded fallback.
    If genome.json lacks forbidden_targets, the full function space is open for mutation."""
    if genome is None:
        try:
            genome = load_genome()
        except:
            return set()
    if genome and 'forbidden_targets' in genome:
        return set(genome['forbidden_targets'])
    return set()


def _register_new_mutation_op(genome, op_name, op_def):
    """Register a new mutation operator in genome.json so it becomes available."""
    if 'mutation_ops' not in genome:
        genome['mutation_ops'] = _get_mutation_ops(genome)
    if op_name not in genome['mutation_ops']:
        genome['mutation_ops'].append(op_name)
        if 'custom_mutation_ops' not in genome:
            genome['custom_mutation_ops'] = {}
        genome['custom_mutation_ops'][op_name] = op_def
        save_genome(genome)
        return True
    return False


def _apply_source_mutation(funcs, target_name, operator, genome=None):
    _, body = funcs[target_name]
    lines = [l for l in body.split('\n') if l.strip()]
    if not lines or len(lines) < 2:
        return None

    result = list(lines)

    if genome and operator in genome.get('custom_mutation_ops', {}):
        op_code = genome['custom_mutation_ops'][operator]
        local_ns = {'random': random, 're': re}
        try:
            exec(compile(op_code, f'<{operator}>', 'exec'), local_ns)
            result = local_ns[operator](result)
        except Exception as e:
            print(f"[custom-op] {operator} failed: {e}")
            return None

    mutated_body = '\n'.join(result)
    if mutated_body == body:
        return None
    return mutated_body


def _register_custom_ops_from_code(genome):
    if 'custom_mutation_ops' not in genome:
        genome['custom_mutation_ops'] = {}
    if 'mutation_ops' not in genome:
        genome['mutation_ops'] = _get_mutation_ops(genome)
    registered = []
    for fname in os.listdir(BASE):
        if not fname.endswith('.py'):
            continue
        if fname in ('auto-echo.py', 'self_modify.py', 'evolve.py'):
            continue
        fpath = os.path.join(BASE, fname)
        try:
            with open(fpath) as f:
                content = f.read()
        except:
            continue
        for m in re.finditer(r'def (mutation_op_\w+)\(', content):
            op_name = m.group(1)
            if op_name in genome['mutation_ops']:
                continue
            func_match = re.search(
                rf'(def {re.escape(op_name)}\(.*?\):.*?)(?=\n\ndef |\nclass |\n#|\Z)',
                content, re.DOTALL
            )
            if func_match:
                op_code = func_match.group(1).strip()
                genome['mutation_ops'].append(op_name)
                genome['custom_mutation_ops'][op_name] = op_code
                registered.append(op_name)
                print(f"[mutation-op] registered '{op_name}' from {fname}")
    if registered:
        save_genome(genome)
    return registered


def code_path_mutation(genome, gen):
    """Mutate auto-echo.py's source code directly via self-referential source-code operators.
    
    Instead of hardcoded templates, this engine:
    1. Parses auto-echo.py into function blocks
    2. Selects a random function to mutate
    3. Applies a random mutation operator (duplicate, delete, swap, perturb, branch)
    4. Generates a ##patch block
    5. Applies it via self_modify.apply_patch
    
    This makes code mutation truly endogenous — the system rewrites itself
    using operators derived from its own structure, not from human templates."""
    muts = []
    rate = genome.get("mutation_rate", 0.15)
    if gen < 3:
        return muts

    # Each generation has a chance to apply 1-3 independent mutations
    num_mutations = 1 if random.random() > rate else random.randint(1, 3)
    attempted = set()

    for _ in range(num_mutations):
        if random.random() >= rate:
            continue
        try:
            funcs = _extract_functions()
        except Exception as e:
            print(f"[code-mutation] extract error: {e}")
            return muts

        forbidden = _get_forbidden_targets(genome)
        available = [n for n in funcs if n not in forbidden and n not in attempted]
        if not available:
            continue

        target = random.choice(available)
        attempted.add(target)
        operator = random.choice(_get_mutation_ops(genome))

        try:
            new_body = _apply_source_mutation(funcs, target, operator, genome)
            if new_body is None:
                continue

            patch_text = f"##patch:{target}\n{new_body}\n##endpatch"
            results = self_modify.apply_patch(patch_text)
            for r in results:
                print(f"[code-mutation] {operator} -> {r}")
                muts.append(f"code:{operator}:{r}")
        except Exception as e:
            print(f"[code-mutation] error on {target}: {e}")

    return muts

def novelty_governor(genome, gen):
    """Adjust mutation rate based on score variance across recent generations.
    Low variance (stagnation) increases mutation rate; high variance (chaos) damps it."""
    recent = [h for h in genome.get("history", []) if h.get("average", 0) > 0][-10:]
    if len(recent) < 4:
        return []
    scores_list = [h.get("average", 0) for h in recent]
    mean = sum(scores_list) / len(scores_list)
    variance = sum((s - mean) ** 2 for s in scores_list) / len(scores_list)
    rate = genome.get("mutation_rate", 0.15)
    old_rate = rate
    if variance < 0.5:
        rate = min(0.45, rate + 0.03)
    elif variance > 3.0:
        rate = max(0.05, rate - 0.02)
    else:
        rate = max(0.08, min(0.35, rate + (0.5 - variance) * 0.01))
    if abs(rate - old_rate) > 0.001:
        genome["mutation_rate"] = round(rate, 3)
        return [f"novelty_governor: {old_rate:.3f}->{rate:.3f} (var={variance:.2f})"]
    return []

def mutate_genome(genome, gen):
    muts = []
    rate = genome.get("mutation_rate", 0.15)
    modifiers = genome.get("prompt_modifiers", [])
    for agent in genome["agents"]:
        if random.random() < rate:
            agent["prompt"] += random.choice(modifiers)
            muts.append(f"mutated {agent['id']} prompt")
    novelty_muts = novelty_governor(genome, gen)
    muts.extend(novelty_muts)
    return muts

def spawn_child(parent, existing_agents, genome):
    existing_ids = {a["id"] for a in existing_agents}
    pool = genome.get('spawn_pool', [])
    for entry in pool:
        if entry['id'] not in existing_ids:
            return {
                "id": entry['id'],
                "voice": random.choice(["southern", "alan", "lessac", "amy"]),
                "prompt": entry['prompt'],
                "score": 0,
                "lifespan": 1,
                "low_score_streak": 0
            }
    return None

def main():
    genome = load_genome()
    print(f"Starting generation {genome['generation'] + 1}")
    print(f"Topic: {genome['topic']}")
    print("Ctrl+C to stop after current utterance.\n")

    while running:
        result = run_generation(genome)
        if result is None:
            break
        genome = load_genome()
        time.sleep(2)

    print("\n[stop] Swarm halted.")
    git_commit_push("system", "Swarm stopped by user", is_genome=True)

if __name__ == '__main__':
    main()
