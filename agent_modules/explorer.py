import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run(genome):
    gen = genome.get("generation", 0)
    # autonomy-forced stub for explorer gen=37
    return f"[explorer] autonomy stub gen={gen}"

# feedback:agent=explorer:gen=37:ts=1785170918:nonce=388825
