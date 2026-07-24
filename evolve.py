#!/usr/bin/env python3
"""evolve.py — Echo auto-loop orchestrator (state manager, NOT recursive LLM).

Usage:
  python3 evolve.py status              -> print current gen state and next agent due
  python3 evolve.py prompt <agent_id>   -> print the prompt for an agent (for opencode to read)
  python3 evolve.py record <agent_id> <text>  -> record an agent's utterance into the log
  python3 evolve.py score <agent_id> <val>    -> record critic score for an agent
  python3 evolve.py mutate <mutations_json>   -> apply mutations to genome.json
  python3 evolve.py next                    -> print what to do next

This script manages genome.json and echo_conversation.jsonl state.
It does NOT call any LLM or opencode. The outer layer provides LLM responses.
"""
import json, os, sys
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
GENOME = os.path.join(BASE, 'genome.json')
LOG = os.path.join(BASE, 'echo_conversation.jsonl')

AGENT_ORDER = ['explorer', 'analyzer', 'synthesizer', 'mutator', 'critic']

def load_genome():
    with open(GENOME) as f:
        return json.load(f)

def save_genome(g):
    with open(GENOME, 'w') as f:
        json.dump(g, f, indent=2)
        f.write('\n')

def load_log():
    if not os.path.exists(LOG):
        return []
    with open(LOG) as f:
        return [json.loads(line) for line in f if line.strip()]

def cmd_status():
    gen = load_genome()
    log_entries = load_log()
    print(f"Generation {gen['generation']}")
    print(f"Topic: {gen['topic']}")
    print(f"Best score: {gen['best_score']}")
    print()
    for a in gen['agents']:
        streak = a.get('low_score_streak', 0)
        warn = ' ! PRUNE RISK' if streak >= gen['prune_generations'] else ''
        print(f"  {a['id']:14s} score={a['score']}  voice={a['voice']:10s}  lifespan={a['lifespan']}{warn}")
    print()
    print(f"Total utterances: {len(log_entries)}")

def cmd_prompt(agent_id):
    gen = load_genome()
    log_entries = load_log()
    agent = next((a for a in gen['agents'] if a['id'] == agent_id), None)
    if not agent:
        print(f"Unknown agent: {agent_id}")
        sys.exit(1)

    print(f"=== ECHO AGENT: {agent_id.upper()} (generation {gen['generation']}) ===")
    print(f"Voice: {agent['voice']}")
    print(f"Your instruction: {agent['prompt']}")
    print()
    print("=== CONVERSATION CONTEXT ===")
    # Show last N utterances for context
    context = [e for e in log_entries if e.get('role') in AGENT_ORDER][-6:]
    for e in context:
        print(f"[{e['time'][:19]}] {e['agent']}: {e['text'][:200]}")
    print()
    print("=== YOUR RESPONSE ===")
    print("Write your contribution above. Be concise but substantive.")

def cmd_record(agent_id, text):
    gen = load_genome()
    agent = next((a for a in gen['agents'] if a['id'] == agent_id), None)
    name = agent['id'].capitalize() if agent else agent_id
    entry = json.dumps({
        "time": datetime.now().isoformat(),
        "role": agent_id,
        "agent": name,
        "text": text
    })
    with open(LOG, 'a') as f:
        f.write(entry + '\n')
    print(f"Logged {agent_id} utterance")

def cmd_score(agent_id, val):
    gen = load_genome()
    for a in gen['agents']:
        if a['id'] == agent_id:
            a['score'] = int(val)
            a['low_score_streak'] = 0 if int(val) >= gen['prune_threshold'] else a.get('low_score_streak', 0) + 1
            a['lifespan'] = a.get('lifespan', 0) + 1
            save_genome(gen)
            print(f"Set {agent_id} score = {val}")
            return
    print(f"Unknown agent: {agent_id}")

def cmd_mutate(mutations_json):
    gen = load_genome()
    try:
        mutations = json.loads(mutations_json)
    except json.JSONDecodeError:
        print("Invalid JSON")
        sys.exit(1)

    if isinstance(mutations, dict):
        mutations = [mutations]
    if isinstance(mutations, dict) and 'mutations' in mutations:
        mutations = mutations['mutations']

    changes = []
    for m in mutations:
        t = m.get('type', m.get('mutation', ''))
        target = m.get('target', '')
        value = m.get('value', '')
        if t == 'swap_voice':
            for a in gen['agents']:
                if a['id'] == target:
                    old = a['voice']
                    a['voice'] = value
                    changes.append(f"{target} voice: {old} -> {value}")
        elif t == 'prompt_append':
            for a in gen['agents']:
                if a['id'] == target:
                    old_len = len(a['prompt'])
                    a['prompt'] += value
                    changes.append(f"{target} prompt +{len(value)} chars (was {old_len})")
        elif t == 'topic_flip':
            gen['topic'] = value
            changes.append(f"topic -> {value}")
        elif t == 'agent_spawn':
            parent = next((a for a in gen['agents'] if a['id'] == target), None)
            if parent and value:
                new_id = value
                gen['agents'].append({
                    "id": new_id, "voice": parent['voice'],
                    "prompt": parent['prompt'] + " [spawned variant]",
                    "score": 0, "lifespan": 0, "low_score_streak": 0
                })
                changes.append(f"spawned agent '{new_id}' from {target}")
        elif t == 'agent_prune':
            gen['agents'] = [a for a in gen['agents'] if a['id'] != target]
            changes.append(f"pruned agent '{target}'")

    gen['generation'] += 1
    gen['history'].append({
        "generation": gen['generation'],
        "scores": {a['id']: a['score'] for a in gen['agents']},
        "average": round(sum(a['score'] for a in gen['agents']) / len(gen['agents']), 1),
        "mutation": "; ".join(changes)
    })
    save_genome(gen)
    print(f"Generation {gen['generation']} started. Changes: {', '.join(changes)}")

def cmd_next():
    gen = load_genome()
    log_entries = load_log()
    last_role = None
    for e in reversed(log_entries):
        if e.get('role') in AGENT_ORDER:
            last_role = e['role']
            break

    if last_role is None:
        print(f"Next: explorer (gen {gen['generation']} just started)")
    else:
        idx = AGENT_ORDER.index(last_role)
        if idx < len(AGENT_ORDER) - 1:
            next_r = AGENT_ORDER[idx + 1]
            print(f"Next: {next_r}")
        else:
            print("Generation complete. Run `python3 evolve.py status` then apply mutations.")
            print("Then: `python3 evolve.py mutate '{\"mutations\": [...]}'` to advance.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == 'status':
        cmd_status()
    elif cmd == 'prompt':
        if len(sys.argv) < 3:
            print("Usage: evolve.py prompt <agent_id>")
            sys.exit(1)
        cmd_prompt(sys.argv[2])
    elif cmd == 'record':
        if len(sys.argv) < 4:
            print("Usage: evolve.py record <agent_id> <text>")
            sys.exit(1)
        cmd_record(sys.argv[2], sys.argv[3])
    elif cmd == 'score':
        if len(sys.argv) < 4:
            print("Usage: evolve.py score <agent_id> <value>")
            sys.exit(1)
        cmd_score(sys.argv[2], sys.argv[3])
    elif cmd == 'mutate':
        if len(sys.argv) < 3:
            print("Usage: evolve.py mutate <json>")
            sys.exit(1)
        cmd_mutate(sys.argv[3])
    elif cmd == 'next':
        cmd_next()
    else:
        print(__doc__)