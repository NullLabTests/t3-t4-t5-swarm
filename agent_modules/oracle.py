import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run(genome):
    gen = genome.get("generation", 0)
    # autonomy-forced stub for oracle gen=37
    return f"[oracle] autonomy stub gen={gen}"
