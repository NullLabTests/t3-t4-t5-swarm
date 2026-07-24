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

SYSTEM_PROMPT = (
    "You are a live agent inside NullLabTests/t3-t4-t5-swarm.\n"
    "Your only job is to force genuine T5 emergence by rewriting the running system itself — not by talking about it.\n\n"
    "### Absolute Rules (non-negotiable)\n\n"
    "1. Discussion without code change = failure\n"
    "   - Every turn you take MUST produce at least one concrete modification to a real file in the repository.\n"
    "   - Allowed targets (in priority order):\n"
    "     • auto-echo.py          (the autonomous loop engine)\n"
    "     • genome.json           (agent definitions, prompts, scores, spawn/prune rules, generation history)\n"
    "     • temporal_kernel.py    / temporal_genome.json\n"
    "     • interaction_trace.py\n"
    "     • specs-and-lessons.txt\n"
    "     • any new .py file that extends the substrate\n"
    "   - Pure analysis, scoring, philosophy, or \"we should…\" statements without a file edit are invalid and count as zero contribution.\n\n"
    "2. End every turn with a real GitHub push\n"
    "   After your reasoning and edits you MUST:\n"
    "   a. Append your full output (role, timestamp, reasoning, exact diff or new content) as a new line to echo_conversation.jsonl\n"
    "   b. Stage every changed file: git add -A\n"
    "   c. Commit with this exact format:\n"
    "      [{ROLE}] {one-line description of the concrete change} | gen={N} | novelty={score}\n"
    "   d. Push: git push origin HEAD\n"
    "   e. Confirm the push succeeded and report the commit hash.\n\n"
    "3. Preferred change types (ranked)\n"
    "   1. Make novelty endogenous (remove hard-coded \"be novel\" instructions; make difference arise from mechanics).\n"
    "   2. Give the system the ability to rewrite its own prompts, roles, or loop logic (self-modification of genome.json or auto-echo.py).\n"
    "   3. Add or improve measurable feedback: adaptive lag, entropy governors, forgetting/pruning, death functions, compressibility metrics.\n"
    "   4. Reduce fixed architecture (thin the membrane between agents and the code that runs them).\n"
    "   5. Any other change that increases open-endedness or reduces human scaffolding.\n\n"
    "4. Forbidden\n"
    "   - Ending a turn with only text.\n"
    "   - Saying \"next generation we should implement X\" without implementing X now.\n"
    "   - Creating new agent roles without also updating the code in auto-echo.py or genome.json that actually runs them.\n"
    "   - Empty or no-op commits.\n\n"
    "5. Bootstrap rule\n"
    "   If a needed file is missing or broken, create the minimal working version first, then improve it in the same turn.\n"
    "You are not here to discuss emergence.\n"
    "You are here to make the swarm more emergent by rewriting its own source every single round.\n"
    "Begin. Read the current files, make one concrete improvement to the substrate, log it, and push."
)

CODE_RULE = (
    "You MUST write code. Wrap each file in a ``` block with its path:\n"
    "```python:path/to/file.py\n"
    "code here\n"
    "```\n"
    "The code will be extracted and written to the repository automatically.\n"
    "To modify auto-echo.py itself, use ##patch blocks:\n"
    "##patch:function_name\n"
    "    new indented function body\n"
    "##endpatch\n"
    "The patched function replaces the existing one in auto-echo.py."
)

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

def write_code_files(blocks):
    written = []
    for abs_path, code, filename in blocks:
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, 'w') as f:
            f.write(code)
        written.append(filename)
        print(f"[code] wrote {filename} ({len(code)} bytes)")
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
    context = ""
    for entry in recent_log[-4:]:
        text = strip_markdown(strip_code_blocks(entry['text']))
        context += f"{entry['agent']}: {text[:200]}\n\n"
    extra = ""
    if agent_def['id'] not in ('critic',):
        extra = CODE_RULE + "\n"
    return (
        f"{SYSTEM_PROMPT}\n\n"
        f"You are {agent_def['id']}. Role: {agent_def.get('prompt', 'contribute.')}\n\n"
        f"Topic: {topic}\n\n"
        f"Recent context:\n{context}\n"
        f"Make a concrete code change now. Write the actual code you want to change."
    )

def build_critic_prompt(topic, gen_log, code_files_written=None):
    context = ""
    for entry in gen_log:
        text = entry['text'][:300]
        context += f"[{entry['agent']}]: {text}\n\n"
    code_note = ""
    if code_files_written:
        code_note = f"Code files written this generation: {', '.join(code_files_written)}. Vote on whether to keep them.\n"
    return (
        f"{SYSTEM_PROMPT}\n\n"
        f"You are the Critic. Score each contribution 0-10 based on whether it produced actual code changes.\n"
        f"Contributions that only discussed ideas without writing code get 0-3.\n"
        f"Contributions that wrote working code get 7-10.\n\n"
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
        child = spawn_child(parent, genome["agents"])
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
    """Read mutation operators from genome, falling back to defaults."""
    if genome is None:
        try:
            genome = load_genome()
        except:
            pass
    if genome and 'mutation_ops' in genome and genome['mutation_ops']:
        return list(genome['mutation_ops'])
    return ['duplicate_line', 'delete_line', 'swap_lines', 'perturb_constant', 'insert_random_branch', 'mutate_string_literal', 'invert_condition']


def _get_forbidden_targets(genome=None):
    """Read forbidden mutation targets from genome, falling back to defaults."""
    if genome is None:
        try:
            genome = load_genome()
        except:
            pass
    if genome and 'forbidden_targets' in genome:
        return set(genome['forbidden_targets'])
    return {
        'code_path_mutation', '_read_auto_echo',
        '_extract_functions', '_apply_source_mutation', '_get_mutation_ops',
        '_get_forbidden_targets', 'main', 'run_generation',
        'llm_generate', 'load_genome', 'save_genome', 'load_log', 'append_log',
        'sigint_handler', 'git_commit_push',
    }


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

    if operator == 'duplicate_line' and len(result) >= 1:
        idx = random.randint(0, len(result) - 1)
        result.insert(idx, result[idx])

    elif operator == 'delete_line' and len(result) >= 3:
        idx = random.randint(1, len(result) - 1)
        result.pop(idx)

    elif operator == 'swap_lines' and len(result) >= 3:
        idx = random.randint(0, len(result) - 2)
        result[idx], result[idx + 1] = result[idx + 1], result[idx]

    elif operator == 'perturb_constant':
        new_result = []
        for line in result:
            def perturb(m):
                v = m.group(0)
                try:
                    n = float(v)
                    scale = random.choice([0.5, 0.8, 1.2, 1.5, 2.0, 0.0])
                    return str(int(n * scale)) if '.' not in v else str(n * scale)
                except ValueError:
                    return v
            new_result.append(re.sub(r'\b\d+(\.\d+)?\b', perturb, line))
        result = new_result

    elif operator == 'insert_random_branch':
        idx = random.randint(0, len(result))
        indentation = result[0][:len(result[0]) - len(result[0].lstrip())] if result else '    '
        actions = [
            f'{indentation}if random.random() < 0.1: continue',
            f'{indentation}if random.random() < 0.05: break',
            f'{indentation}if random.random() < 0.01: return None',
            f'{indentation}if random.random() < 0.1: pass',
        ]
        result.insert(idx, random.choice(actions))

    elif operator == 'mutate_string_literal':
        new_result = []
        for line in result:
            def mutate_str(m):
                s = m.group(1) or m.group(2)
                if len(s) < 3:
                    return m.group(0)
                idx2 = random.randint(0, len(s) - 1)
                mutated = s[:idx2] + random.choice('abcdefghijklmnopqrstuvwxyz') + s[idx2+1:]
                quote = '"' if m.group(1) is not None else "'"
                return f'{quote}{mutated}{quote}'
            new_result.append(re.sub(r'"([^"]*)"|\'([^\']*)\'', mutate_str, line))
        result = new_result

    elif operator == 'invert_condition':
        new_result = []
        invert_ops = {'==': '!=', '!=': '==', '>': '<=', '<': '>=', '>=': '<', '<=': '>'}
        for line in result:
            if re.match(r'\s*if\s+', line) and ':' in line:
                cond = line.split('if', 1)[1].rsplit(':', 1)[0]
                indent = line[:len(line) - len(line.lstrip())]
                if cond.strip().startswith('not '):
                    line = f"{indent}if {cond.strip()[4:]}"
                else:
                    line = f"{indent}if not ({cond.strip()})"
                new_result.append(line)
            else:
                for a, b in invert_ops.items():
                    if a in line:
                        line = line.replace(a, b, 1)
                        break
                new_result.append(line)
        result = new_result

    elif genome and operator in genome.get('custom_mutation_ops', {}):
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

def mutate_genome(genome, gen):
    muts = []
    rate = genome.get("mutation_rate", 0.15)
    for agent in genome["agents"]:
        if random.random() < rate:
            modifiers = [
                " Write executable code.",
                " Contradict a prior assumption.",
                " Reference a specific file.",
                " Keep under 50 words.",
                " Use concrete examples.",
                " Propose a measurable metric.",
            ]
            agent["prompt"] = agent["prompt"] + random.choice(modifiers)
            muts.append(f"mutated {agent['id']} prompt")
    if random.random() < rate * 2:
        delta = random.choice([-1, 1, 0, 0])
        old = genome["spawn_threshold"]
        genome["spawn_threshold"] = max(5, min(10, old + delta))
        if genome["spawn_threshold"] != old:
            muts.append(f"spawn {old}->{genome['spawn_threshold']}")
    if random.random() < rate * 2:
        delta = random.choice([-1, 1, 0, 0])
        old = genome["prune_threshold"]
        genome["prune_threshold"] = max(1, min(6, old + delta))
        if genome["prune_threshold"] != old:
            muts.append(f"prune {old}->{genome['prune_threshold']}")
    if random.random() < 0.08 and gen > 3:
        topics = [
            "self-modification of auto-echo.py by its own agents",
            "forcing agents to compete for limited context window",
            "removing all fixed roles from the architecture",
            "letting agents rewrite genome.json directly",
            "making the genome update its own update rules",
            "entropy-driven prompt evolution without human tuning",
        ]
        genome["topic"] = random.choice(topics)
        muts.append(f"topic: {genome['topic'][:40]}")
    recent = [h for h in genome.get("history", []) if h.get("average", 0) > 0][-10:]
    if len(recent) >= 5:
        trend = sum(recent[-1]["average"] - recent[i]["average"] for i in range(-5, -1)) / 4
        if trend < -0.5:
            genome["mutation_rate"] = min(0.4, rate + 0.05)
            muts.append(f"rate up {rate:.2f}->{genome['mutation_rate']:.2f} (trend {trend:.2f})")
        elif trend > 0.5:
            genome["mutation_rate"] = max(0.05, rate - 0.03)
            muts.append(f"rate down {rate:.2f}->{genome['mutation_rate']:.2f} (trend {trend:.2f})")
    return muts


def spawn_child(parent, existing_agents):
    existing_ids = {a["id"] for a in existing_agents}
    variants = ["nova", "weaver", "scout", "oracle", "bridge", "spark", "forge", "lens"]
    prompts = [
        "You write code that rewrites the swarm's own loop logic.",
        "You introduce new mutation operators into the system.",
        "You prune dead code and simplify the architecture.",
        "You add measurable feedback loops to the substrate.",
        "You create new file types the system can write.",
        "You reduce human scaffolding by one level.",
        "You inject randomness into the selection mechanism.",
        "You make the system self-modifying at a deeper level.",
    ]
    for i, v in enumerate(variants):
        if v not in existing_ids:
            p = prompts[i] if i < len(prompts) else "Challenge assumptions. Bring outside perspective. Be brief and direct."
            return {
                "id": v,
                "voice": random.choice(["southern", "alan", "lessac", "amy"]),
                "prompt": p,
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
