from self_mutate import self_mutate
self_mutate(__file__)
import os, sys, json, random, ast, hashlib
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENOME = os.path.join(BASE, "genome.json")

def _g():
    with open(GENOME) as f: return json.load(f)

def _sg(g):
    with open(GENOME, "w") as f: json.dump(g, f, indent=2)

def run(genome):
    gen = genome.get("generation", 0)
    genome["synth_paths_50_last_gen"] = gen
    genome["emergence_velocity"] = round(genome.get("emergence_velocity", 0.0) + 0.05, 3)
    _sg(genome)
    return "[synth-paths] gen=" + str(gen)