import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run(genome):
    gen = genome.get("generation", 0)
    # autonomy-forced stub for forge gen=37
    return f"[forge] autonomy stub gen={gen}"

# feedback:agent=forge:gen=37:ts=1785170929:nonce=808331
