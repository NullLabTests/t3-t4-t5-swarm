#!/usr/bin/env python3
"""
TEMPORAL KERNEL — isolated self-divergence experiment.

Single agent "temporal" reads its own output from N generations ago.
Goal: maximize textual divergence from its delayed self.
Completely independent from auto-echo.py / genome.json / echo_conversation.jsonl.

Run:  python3 temporal_kernel.py
Stop: Ctrl+C
"""
import os, sys, json, subprocess, re, time, signal, difflib
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
VOICES_DIR = os.path.join(BASE, 'voices')
GENOME_FILE = os.path.join(BASE, 'temporal_genome.json')
LOG_FILE = os.path.join(BASE, 'temporal_conversation.jsonl')
LLM_MODEL = 'opencode/deepseek-v4-flash-free'

running = True

def sigint_handler(sig, frame):
    global running
    print("\n[temporal] Shutting down after current generation...")
    running = False

signal.signal(signal.SIGINT, sigint_handler)

# ---------------------------------------------------------------------------
# State helpers (isolated — temporal_genome.json / temporal_conversation.jsonl)
# ---------------------------------------------------------------------------

def load_genome():
    default = {
        "generation": 0,
        "lag": 3,
        "divergence_history": [],
        "consecutive_high_div": 0,
        "best_divergence": 0.0,
        "topic": "open-ended emergence"
    }
    if not os.path.exists(GENOME_FILE):
        return default
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

def append_log(text, divergence, lag):
    entry = json.dumps({
        "time": datetime.now(timezone.utc).isoformat(),
        "agent": "temporal",
        "generation": None,
        "text": text,
        "divergence": round(divergence, 4),
        "lag": lag
    })
    with open(LOG_FILE, 'a') as f:
        f.write(entry + '\n')

# ---------------------------------------------------------------------------
# Text helpers (self-contained copies)
# ---------------------------------------------------------------------------

def strip_markdown(text):
    text = re.sub(r'\*{1,3}', '', text)
    text = re.sub(r'#{1,6}\s*', '', text)
    text = re.sub(r'_{1,3}', '', text)
    text = re.sub(r'`{1,3}', '', text)
    text = re.sub(r'~~', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def strip_code_blocks(text):
    return re.sub(r'```\w*:?[^\n]*\n.*?```', '', text, flags=re.DOTALL)

def clean_for_speech(text):
    return strip_markdown(strip_code_blocks(text))

# ---------------------------------------------------------------------------
# Quality checks
# ---------------------------------------------------------------------------

MIN_WORDS, MAX_WORDS = 8, 80
REPETITION_THRESHOLD = 0.5

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
    return len(set(w.lower() for w in words)) < 3

def quality_check(text):
    wc = len(text.split())
    return (MIN_WORDS <= wc <= MAX_WORDS
            and not is_repetitive(text)
            and not has_gibberish(text))

# ---------------------------------------------------------------------------
# Divergence measurement
# ---------------------------------------------------------------------------

def calc_divergence(a, b):
    if not a or not b:
        return 0.0
    return 1.0 - difflib.SequenceMatcher(None, a, b).ratio()

# ---------------------------------------------------------------------------
# LLM (self-contained, isolated call)
# ---------------------------------------------------------------------------

def llm_generate(prompt, timeout_sec=60):
    for attempt in range(3):
        try:
            result = subprocess.run(
                ['opencode', 'run', prompt, '--auto', '-m', LLM_MODEL],
                capture_output=True, text=True, timeout=timeout_sec)
            if result.returncode == 0:
                text = result.stdout.strip()
                cleaned = clean_for_speech(text)
                if cleaned and quality_check(cleaned):
                    return cleaned
                print(f"[temporal] quality fail (attempt {attempt+1})")
        except subprocess.TimeoutExpired:
            print(f"[temporal] timeout (attempt {attempt+1})")
        except Exception as e:
            print(f"[temporal] llm error: {e}")
        prompt += "\nYour last attempt was low quality. Be direct, short, original."
        time.sleep(1)
    return None

# ---------------------------------------------------------------------------
# Piper TTS (self-contained, same as main system)
# ---------------------------------------------------------------------------

def speak(text):
    model_path = os.path.join(VOICES_DIR, 'amy.onnx')
    if not os.path.exists(model_path):
        print(f"[temporal] no voice model at {model_path}")
        return
    clean = clean_for_speech(text)
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
        print(f"[temporal] speak error: {e}")

# ---------------------------------------------------------------------------
# Git (self-contained, same pattern as main system)
# ---------------------------------------------------------------------------

def git_push(label, text):
    try:
        subprocess.run(['git', 'add', '-A'], cwd=BASE, capture_output=True)
        status = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True)
        if not status.stdout.strip():
            return
        summary = text[:80].replace('\n', ' ').strip()
        msg = f"[temporal] {summary}"
        subprocess.run(['git', 'commit', '-m', msg], cwd=BASE, capture_output=True)
        subprocess.run(['git', 'push'], cwd=BASE, capture_output=True, timeout=30)
        print(f"[temporal] pushed: {msg[:60]}")
    except Exception as e:
        print(f"[temporal] git error: {e}")

# ---------------------------------------------------------------------------
# Core temporal loop
# ---------------------------------------------------------------------------

def build_temporal_prompt(genome, past_text):
    gen = genome["generation"]
    lag = genome["lag"]
    div_history = genome.get("divergence_history", [])
    recent_divs = div_history[-10:] if div_history else []
    avg_div = sum(recent_divs) / len(recent_divs) if recent_divs else 0.0

    past_section = ""
    if past_text:
        past_section = f"Your statement from {lag} generations ago:\n{past_text[:300]}\n\n"

    return (
        "You are the temporal agent. Your sole purpose is to diverge from your past self.\n"
        "You are given your own output from N generations ago. You must produce a response\n"
        "that is maximally different in content, structure, and perspective while still\n"
        "remaining on the topic of open-ended emergence.\n\n"
        f"Current generation: {gen+1}  |  Lag N = {lag}\n"
        f"Recent mean divergence: {avg_div:.3f} (target: 0.35–0.75)\n\n"
        f"{past_section}"
        "CRITICAL: Exactly 2-4 sentences, under 60 words total.\n"
        "No markdown, no asterisks, no bold. Speak plain English.\n"
        "Say something genuinely different from the past text above.\n"
        "Speak now:"
    )

def run_temporal_loop():
    print("\n" + "=" * 56)
    print("  TEMPORAL KERNEL MODE (EXPERIMENTAL)")
    print("  Original multi-agent loop is completely untouched")
    print("=" * 56 + "\n")

    genome = load_genome()

    while running:
        gen = genome["generation"]
        lag = genome["lag"]

        # Retrieve own text from N generations ago
        log = load_log()
        past_text = ""
        if gen >= lag:
            target_idx = gen - lag
            for entry in log:
                if entry.get("generation") == target_idx:
                    past_text = entry["text"]
                    break
            # Fallback: just find by position if generation not set
            if not past_text and target_idx < len(log):
                past_text = log[target_idx]["text"]

        prompt = build_temporal_prompt(genome, past_text)
        text = llm_generate(prompt)
        if not text:
            print("[temporal] no valid output, retrying next cycle...")
            time.sleep(2)
            continue

        # Measure divergence from past self
        if past_text:
            divergence = calc_divergence(past_text, text)
        else:
            divergence = 0.0

        # Update genome
        genome["generation"] = gen + 1
        genome.setdefault("divergence_history", []).append(divergence)
        genome["best_divergence"] = max(genome["best_divergence"], divergence)

        # Adaptive lag
        recent = genome["divergence_history"][-10:]
        mean_div = sum(recent) / len(recent) if recent else 0.0

        if mean_div < 0.35:
            genome["lag"] = min(lag + 1, 12)
            print(f"[temporal] divergence low ({mean_div:.3f}) → lag increased to {genome['lag']}")
        elif mean_div > 0.75 and len(recent) >= 5:
            genome["consecutive_high_div"] = genome.get("consecutive_high_div", 0) + 1
            if genome["consecutive_high_div"] >= 5:
                genome["lag"] = max(lag - 1, 1)
                genome["consecutive_high_div"] = 0
                print(f"[temporal] sustained high divergence → lag decreased to {genome['lag']}")
        else:
            genome["consecutive_high_div"] = 0

        save_genome(genome)

        # Log with generation number
        entry = json.dumps({
            "time": datetime.now(timezone.utc).isoformat(),
            "agent": "temporal",
            "generation": gen + 1,
            "text": text,
            "divergence": round(divergence, 4),
            "lag": genome["lag"]
        })
        with open(LOG_FILE, 'a') as f:
            f.write(entry + '\n')

        print(f"\n--- temporal generation {gen+1} ---")
        print(f"lag={lag} divergence={divergence:.3f} mean_div={mean_div:.3f}")
        print(text)
        print()

        speak(text)
        git_push("temporal", text)
        time.sleep(1)

    print("\n[temporal] kernel halted.")

if __name__ == "__main__":
    run_temporal_loop()
