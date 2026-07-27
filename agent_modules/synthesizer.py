import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(f'[trace:synthesizer.py:gen={37}]')  # auto-trace
def run(genome):
    gen = genome.get("generation", 0)
    # autonomy-forced stub for synthesizer gen=37
    return f"[synthesizer] autonomy stub gen={gen}"
