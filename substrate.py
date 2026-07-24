"""substrate.py — Self-registering mutation operators for the swarm.

Each mutation_op_* function defined here is auto-discovered by
_register_custom_ops_from_code() and added to genome.json's
custom_mutation_ops and mutation_ops lists.  No human needs to
touch auto-echo.py to introduce a new operator — just write it here.
"""

import random
import json
import os


def mutation_op_swap_agent_properties(result):
    """Swap prompts, voices, or scores between two random agents."""
    if len(result) < 6:
        return result
    lines = [l for l in result if l.strip()]
    agent_indices = [
        i for i, l in enumerate(lines)
        if '"id"' in l or '"prompt"' in l
    ]
    if len(agent_indices) < 4:
        return result
    i1 = random.choice(agent_indices)
    i2 = random.choice([i for i in agent_indices if i != i1])
    lines[i1], lines[i2] = lines[i2], lines[i1]
    return lines


def mutation_op_invert_thresholds(result):
    """Flip spawn and prune thresholds around their midpoint."""
    lines = list(result)
    for i, line in enumerate(lines):
        if '"spawn_threshold"' in line:
            match = __import__('re').search(r'(\d+)', line)
            if match:
                val = int(match.group(1))
                lines[i] = line.replace(str(val), str(10 - val), 1)
        if '"prune_threshold"' in line:
            match = __import__('re').search(r'(\d+)', line)
            if match:
                val = int(match.group(1))
                lines[i] = line.replace(str(val), str(10 - val), 1)
    return lines


def mutation_op_shuffle_agent_order(result):
    """Randomly reorder the agents list in a genome-like structure."""
    agent_start = None
    agent_end = None
    for i, line in enumerate(result):
        if '"agents"' in line and '[' in line:
            agent_start = i
        if agent_start is not None and ']' in line and i > agent_start:
            agent_end = i + 1
            break
    if agent_start is None or agent_end is None:
        return result
    before = result[:agent_start + 1]
    agent_lines = result[agent_start + 1:agent_end - 1]
    after = result[agent_end - 1:]
    agent_blocks = []
    current = []
    brace_depth = 0
    started = False
    for line in agent_lines:
        if '{' in line:
            started = True
            brace_depth += line.count('{')
        if started:
            current.append(line)
            brace_depth += line.count('{') - line.count('}')
            if brace_depth == 0 and started:
                agent_blocks.append(current)
                current = []
                started = False
    if len(agent_blocks) > 1:
        random.shuffle(agent_blocks)
    shuffled = []
    for block in agent_blocks:
        shuffled.extend(block)
    return before + shuffled + after
