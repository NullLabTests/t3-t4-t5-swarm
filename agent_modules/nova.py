import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run(genome):
    gen = genome.get("generation", 0)
    # autonomy-forced stub for nova gen=37
    return f"[nova] autonomy stub gen={gen}"
