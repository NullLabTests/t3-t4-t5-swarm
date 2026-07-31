"""watchdog.py — outer-loop supervisor for the t3-t4 swarm.

Deliberately simple and immutable. It sits OUTSIDE the mutation boundary:
the swarm never reads or writes this file, so it cannot be corrupted by what
it supervises (the immune-proofreader principle from the README lessons).

Cycle:
  1. verify the engine (auto-echo.py) still compiles and invariants hold
     -> if not, restore from git (last master-node known-good commit)
  2. run `python3 -u auto-echo.py`, streaming output to swarm.log
  3. on exit, decide crash vs clean:
       - exit code 0  -> clean stop, restart normally
       - exit code 3  -> engine invalid, restore and retry
       - traceback in recent log tail -> crash, restore engine + restart
       - otherwise    -> restart (transient)
  4. backoff after repeated crashes; give up after MAX_CONSECUTIVE_CRASHES
     and leave the log for the master node.

Usage:  python3 watchdog.py [--dry-run]
"""
import os
import re
import subprocess
import sys
import time

BASE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.path.join(BASE, 'auto-echo.py')
LOG = os.path.join(BASE, 'swarm.log')
CMD = [sys.executable, '-u', os.path.join(BASE, 'auto-echo.py')]
MAX_CONSECUTIVE_CRASHES = 5
BACKOFF_BASE = 5

ENGINE_INVARIANTS = [
    ("MODULES_DIR", "MODULES_DIR = os.path.join(BASE, 'agent_modules')"),
    ("GENOME_FILE", "GENOME_FILE = os.path.join(BASE, 'genome.json')"),
    ("load_genome git self-heal", "['git', 'checkout', '--', 'genome.json']"),
    ("_get_mutation_ops key", "genome.get('mutation_ops', [])"),
    ("custom_mutation_ops key", "genome['custom_mutation_ops'][operator]"),
    ("novelty variance squared", "(s - mean) ** 2"),
    ("identity loop bridge", "os.path.join(BASE, 'identity', 'identity_loop.py')"),
    ("identity inject call", "_identity_loop('inject', genome, gen)"),
    ("identity observe call", "_identity_loop('observe', genome, gen)"),
]


def engine_valid() -> bool:
    try:
        with open(ENGINE) as f:
            src = f.read()
    except Exception as e:
        print(f'[watchdog] cannot read engine: {e}', flush=True)
        return False
    try:
        compile(src, ENGINE, 'exec')
    except SyntaxError as e:
        print(f'[watchdog] engine syntax broken (line {e.lineno}: {e.msg})', flush=True)
        return False
    missing = [name for name, needle in ENGINE_INVARIANTS if needle not in src]
    if missing:
        print(f'[watchdog] engine invariants corrupted: {missing}', flush=True)
        return False
    return True


def restore_engine() -> None:
    base_path = os.path.join(BASE, 'engine_base', 'auto-echo.py')
    if os.path.exists(base_path):
        print('[watchdog] restoring auto-echo.py from engine_base/', flush=True)
        subprocess.run(['cp', base_path, os.path.join(BASE, 'auto-echo.py')], capture_output=True, text=True)
    else:
        print('[watchdog] engine_base/ missing, falling back to git checkout', flush=True)
        subprocess.run(['git', 'checkout', '--', 'auto-echo.py'], cwd=BASE, capture_output=True, text=True)


def restore_genome_if_corrupt() -> None:
    path = os.path.join(BASE, 'genome.json')
    try:
        with open(path) as f:
            f.read(1)
    except (OSError, UnicodeDecodeError):
        print('[watchdog] genome.json unreadable, restoring from git', flush=True)
        subprocess.run(['git', 'checkout', '--', 'genome.json'], cwd=BASE, capture_output=True, text=True)


def tail_log(n: int = 2000) -> str:
    try:
        with open(LOG, errors='replace') as f:
            return f.read()[-n:]
    except OSError:
        return ''


def looks_like_crash(returncode: int) -> bool:
    if returncode == 3:
        return True
    if returncode == 0:
        return False
    tail = tail_log()
    return bool(re.search(r'Traceback \(most recent call last\)|SyntaxError|NameError|IndexError|KeyError', tail))


def identity_valid() -> bool:
    """Identity substrate health: delegated to identity/identity_loop.py
    so the check lives with the protected code (never with the swarm)."""
    try:
        r = subprocess.run([sys.executable, os.path.join(BASE, 'identity', 'identity_loop.py'), 'check'],
                           cwd=BASE, capture_output=True, text=True, timeout=30)
        return r.returncode == 0
    except Exception:
        return False


def restore_identity() -> None:
    print('[watchdog] restoring identity/ from template', flush=True)
    subprocess.run([sys.executable, os.path.join(BASE, 'identity', 'identity_loop.py'), 'restore'],
                   cwd=BASE, capture_output=True, text=True, timeout=60)


def main() -> int:
    dry_run = '--dry-run' in sys.argv
    consecutive = 0
    while True:
        if not engine_valid():
            restore_engine()
            if not engine_valid():
                print('[watchdog] engine still invalid after restore — stopping for master node', flush=True)
                return 2
        restore_genome_if_corrupt()
        if not identity_valid():
            restore_identity()
            if not identity_valid():
                print('[watchdog] identity still invalid after template restore — stopping for master node', flush=True)
                return 3
        print(f'[watchdog] starting swarm (attempt after {consecutive} crash(es))', flush=True)
        try:
            with open(LOG, 'w') as logf:
                proc = subprocess.run(CMD, cwd=BASE, stdout=logf, stderr=subprocess.STDOUT)
        except KeyboardInterrupt:
            print('[watchdog] interrupted — stopping', flush=True)
            return 0
        rc = proc.returncode if 'proc' in dir() else -1
        if dry_run:
            print(f'[watchdog] dry-run: process exited rc={rc}', flush=True)
            return 0
        if looks_like_crash(rc):
            consecutive += 1
            print(f'[watchdog] crash detected (rc={rc}, consecutive={consecutive})', flush=True)
            if consecutive >= MAX_CONSECUTIVE_CRASHES:
                print('[watchdog] too many consecutive crashes — stopping for master node', flush=True)
                return 1
            if not engine_valid():
                restore_engine()
            time.sleep(min(BACKOFF_BASE * (2 ** consecutive), 300))
        else:
            consecutive = 0
            print(f'[watchdog] swarm stopped cleanly (rc={rc}) — restarting', flush=True)
            time.sleep(2)


if __name__ == '__main__':
    sys.exit(main())
