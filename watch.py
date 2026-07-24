#!/usr/bin/env python3
"""watch.py — TUI dashboard for the echo swarm. Read-only, won't disturb the loop.

Usage:  python3 watch.py
Quit:   q or Ctrl+C
"""
import curses, json, os, subprocess, time
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
GENOME = os.path.join(BASE, 'genome.json')
LOG = os.path.join(BASE, 'echo_conversation.jsonl')

def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return None

def read_log(n=8):
    try:
        with open(LOG) as f:
            lines = f.readlines()
        return [json.loads(l) for l in lines[-n:] if l.strip()]
    except:
        return []

def git_log(n=5):
    try:
        r = subprocess.run(['git', 'log', '--oneline', f'-{n}'], capture_output=True, text=True, cwd=BASE, timeout=3)
        return r.stdout.strip().split('\n') if r.stdout.strip() else []
    except:
        return []

def last_commit_age():
    try:
        r = subprocess.run(['git', 'log', '-1', '--format=%ct'], capture_output=True, text=True, cwd=BASE, timeout=3)
        if r.stdout.strip():
            ts = int(r.stdout.strip())
            return int(time.time()) - ts
    except:
        pass
    return -1

def current_agent():
    """Find the opencode run subprocess and extract which agent is being generated."""
    try:
        r = subprocess.run(['ps', 'aux'], capture_output=True, text=True, timeout=3)
        for line in r.stdout.split('\n'):
            if 'opencode run' in line and 'auto-echo.py' not in line:
                parts = line.split()
                if len(parts) >= 10:
                    elapsed = parts[9] if ':' in parts[9] else '?'
                    cpu = parts[2]
                    cmd = ' '.join(parts[10:])
                    for aid in ['explorer','analyzer','synthesizer','critic','mutator',
                                'nova','weaver','scout','oracle','bridge','spark','forge','lens']:
                        if f'You are {aid}' in cmd or f'role: {aid}' in cmd.lower():
                            return aid, elapsed, cpu
                    return '?', elapsed, cpu
    except:
        pass
    return None, None, None

def draw(std):
    curses.curs_set(0)
    std.nodelay(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    while True:
        key = std.getch()
        if key in (ord('q'), ord('Q'), 27):
            break

        g = load_json(GENOME)
        entries = read_log()
        commits = git_log()
        alive = loop_alive()
        agent_id, elapsed, cpu = current_agent()
        staleness = last_commit_age()

        h, w = std.getmaxyx()
        std.clear()

        gen = g['generation'] if g else '?'
        topic = (g['topic'][:w-30] if g and g.get('topic') else '?')
        status = "RUNNING" if alive else "STOPPED"
        sc = curses.color_pair(2) if alive else curses.color_pair(3)

        std.addstr(0, 0, f" ECHO SWARM  gen={gen}  {status} ", sc)
        std.addstr(0, w-len(topic)-1, topic[:w-30])

        # Current agent & progress
        line2 = ""
        if alive and agent_id:
            line2 = f" Cooking: {agent_id} ({elapsed})  cpu={cpu}%"
            std.addstr(1, 0, line2, curses.color_pair(4))
        elif alive:
            std.addstr(1, 0, " Cooking: (idle — between agents)", curses.color_pair(4))
        else:
            std.addstr(1, 0, " LOOP STOPPED", curses.color_pair(3))

        # Staleness
        if staleness > 300:  # 5 min
            warn = f"  STALE: {staleness//60}m since last push"
            std.addstr(1, len(line2)+2, warn, curses.color_pair(3))

        if g and g.get('agents'):
            agents = sorted(g['agents'], key=lambda a: a['score'], reverse=True)
            std.addstr(3, 0, f"{'AGENT':<14} {'SCORE':<6} {'VOICE':<12} {'LIFE':<6} STREAK")
            std.addstr(4, 0, f"{'-'*14} {'-'*6} {'-'*12} {'-'*6} {'-'*6}")
            for i, a in enumerate(agents[:8], 5):
                if i >= h-1: break
                s = a.get('score', 0)
                streak = a.get('low_score_streak', 0)
                pg = g.get('prune_generations', 2) or 2
                warn = " PRUNE!" if streak >= pg else ""
                c = curses.color_pair(3) if streak >= pg else curses.A_NORMAL
                std.addstr(i, 0, f"{a['id']:<14} {s:<6} {a.get('voice','?'):<12} {a.get('lifespan',0):<6} {streak}{warn}", c)

        utop = min(14, h-10)
        std.addstr(utop, 0, "--- RECENT UTTERANCES ---")
        for i, e in enumerate(entries, utop+1):
            if i >= h-5: break
            role = e.get('role', '?')[:10]
            text = e.get('text', '')[:w-20].replace('\n', ' ')
            std.addstr(i, 0, f" [{role:>10}] {text[:w-16]}")

        gtop = utop + len(entries) + 2
        if gtop < h-1:
            std.addstr(gtop, 0, "--- LAST PUSHES ---")
            for i, c in enumerate(commits, gtop+1):
                if i >= h-2: break
                std.addstr(i, 0, f" {c[:w-2]}")

        std.addstr(h-1, 0, " [q] quit  |  read-only — does not touch the loop")
        std.refresh()
        time.sleep(2)

def loop_alive():
    try:
        r = subprocess.run(['ps', 'aux'], capture_output=True, text=True, timeout=3)
        return 'auto-echo.py' in r.stdout
    except:
        return False

def main():
    curses.wrapper(draw)

if __name__ == '__main__':
    main()