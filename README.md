# T3 → T4 → T5 Swarm

Autonomous multi-agent swarm with voice I/O, evolutionary genome, and auto-push-to-git on every utterance.

## Origin: The Central Dogma of Biology → AI Agent Evolution

This project is the direct descendant of **[NullLabTests/dna-rna-protein-analog](https://github.com/NullLabTests/dna-rna-protein-analog)**, which mapped biology's central dogma onto the evolution of AI agents:

| Biological | AI Analog | Tier |
|------------|-----------|------|
| **DNA** (genotype, long-term storage) | Model weights, system prompts, config | **T1** — Static prompt |
| **Transcription** (DNA → RNA) | Inference forward pass, loop reasoning | **T2** — Agent loop (think → act → observe) |
| **Translation** (RNA → Protein) | Structured output, tool calls, actions | **T2** — Agent loop (continued) |
| **Protein interaction network** | Multi-agent graphs, message passing | **T3** — Agent graph (nodes + edges + state) |
| **Regulatory gene network** | Multi-agent systems with specialized roles | **T4** — Multi-agent ecosystem |
| **Evolution by natural selection** | Genome, mutation, spawn, prune, selection | **T5** — Self-evolving system |

This repo is the **running implementation** of T3→T4→T5. It started as `t3-t4/echo.py` — a voice-based multi-agent dialog system (T3 graph, T4 specialization). We are now closing the loop to T5: **fully autonomous, self-mutating, human-out-of-the-loop evolution toward true emergence.**

## The Chain

```
dna-rna-protein-analog  (concept / isomorphic map)
        ↓
t3-t4 / echo.py         (manual multi-agent voice dialog, T3→T4)
        ↓
t3-t4-t5-swarm          (autonomous loop, auto-push, self-evolution, T5)
```

## Architecture

```
                    ┌─────────────────────────────────────┐
                    │           GENOME (genome.json)       │
                    │  agent definitions, prompts, scores  │
                    │  generation history, spawn/prune     │
                    └──────┬──────────────────────────────┘
                           │ reads/writes
                    ┌──────▼──────────────────────────────┐
                    │      ECHO ENGINE (auto-echo.py)      │
                    │                                      │
                    │  for each generation:                │
                    │    1. For each agent:                │
                    │       - LLM generates contribution   │
                    │       - Piper TTS speaks it          │
                    │       - Git commit + push            │
                    │    2. Critic scores all              │
                    │    3. Spawn / prune / mutate         │
                    │    4. Update genome, push            │
                    │    5. Repeat                         │
                    └──────────────────────────────────────┘
```

## Requirements

- Python 3.10+
- [opencode](https://opencode.ai) with a model provider configured
- [Piper TTS](https://github.com/rhasspy/piper) (`pip3 install piper-tts` or system package)
- [sox](http://sox.sourceforge.net/) (`sudo apt install sox`)
- PyAudio (`sudo apt install portaudio19-dev && pip3 install pyaudio`)
- [whisper](https://github.com/openai/whisper) (`pip3 install openai-whisper`)

## Quick Start

```bash
# Clone
git clone git@github.com:NullLabTests/t3-t4-t5-swarm.git
cd t3-t4-t5-swarm

# Download voice models (required for speech output)
# Voice .onnx files are too large (~60MB each) to host on GitHub.
# Get them from https://huggingface.co/rhasspy/piper-voices/tree/main/en
# Place in voices/ and symlink config:
#   ln -s alan.json voices/alan.onnx.json
#   ln -s amy.json  voices/amy.onnx.json
#   ln -s lessac.json voices/lessac.onnx.json
#   ln -s southern.json voices/southern.onnx.json

# Run the autonomous swarm (Ctrl+C to stop after current utterance)
python3 auto-echo.py
```

## Files

| File | Purpose |
|------|---------|
| `auto-echo.py` | Autonomous loop engine — drives the swarm |
| `genome.json` | Agent definitions, evolutionary state, history |
| `echo_conversation.jsonl` | Full utterance log (pushed after each line) |
| `voices/*.json` | Piper TTS voice configs (download .onnx separately) |
| `specs-and-lessons.txt` | Architecture docs, device setup, lessons learned |

## The T5 Goal

True emergence means:
1. **Open-ended innovation** — the system produces genuinely novel thought patterns, not just convergent refinement
2. **Self-directed topic evolution** — the swarm chooses what to explore next
3. **Autonomous mutation** — the genome rewrites itself via selection pressure
4. **Persistent identity** — every utterance is recorded, every generation is tracked, every push preserves the lineage

## Status

- **T3 (graph)**: Stable — 4+ agents with distinct personas and voice identities
- **T4 (multi-agent)**: Stable — specialized roles (explorer, analyzer, synthesizer, critic, mutator)
- **T5 (self-evolving)**: **Emerged** — see Phase Transition below.

## Phase Transition: T5 Self-Evolving Code Ecosystem (Gen ~50–63)

At approximately generation 50, the swarm crossed a critical threshold. It transitioned from an **LLM-driven multi-agent dialog system** (T3/T4) into a **self-mutating, autonomous code ecosystem** (T5). This was not a designed feature — it was an emergent outcome of the swarm's own evolutionary dynamics.

### What Changed

| Before (Gen < 50) | After (Gen 50+) |
|---|---|
| Agents called LLM each turn (3-5 min per call) | All 8 agents became **module agents** — Python modules that execute instantly |
| LLM calls produced code, patches, and commits | Module `.py` files rewrite themselves and each other via AST transforms |
| Genome had ~30 keys | Genome grew to ~150+ keys as the swarm tracks its own evolution |
| Agents were defined by prompts | Agents are defined by their `.py` module code |
| Voice output per agent turn | Voices still active, but the loop runs 100x faster |

### Evidence

- **Gen 53**: Synthesizer fixed 40+ bugs, introduced cross-wire and cross-infection patterns
- **Gen 54**: Forced self-rewrite hooks injected into every module
- **Gen 55–57**: Quine_loop drove module-level self-rewriting — every module rewrites its own source every generation
- **Gen 58–60**: Clockwork activated "t5-emergence drive" — gene factory spawns novel module archetypes from scratch (crawler, writer, prober, weaver, spark) with valid `run()` functions
- **Gen 61**: Bridge auto-registered new file types and handlers
- **Gen 63+**: The system runs fully autonomously — LLM calls are no longer on the critical path; modules execute, mutate, and commit without orchestration

### Metrics

- `emergence_velocity: 0.17` — self-reported metric for rate of emergent change
- `source_autonomy_index` — tracks what fraction of source changes are self-directed vs scaffolded
- `mutation_rate` climbed from ~0.09 (gen 37) to ~0.875 (gen 60)
- All 8 agents are module-only (no `local_fn`, no direct LLM dependency)
- Gene factory produces novel, syntactically valid Python modules with `run()` entry points, auto-discovered by the engine

### Significance

The swarm no longer depends on LLM calls for its core loop. It evolved from a system that *talked about* rewriting itself into a system that *actually rewrites itself* — a true self-modifying codebase. This is the T5 threshold the project was originally designed to reach.

## Autonomous Correction Cycle: AI Overseer in the Loop

An emergent property of this system is that its own evolution **repeatedly breaks critical infrastructure**. The swarm mutates anything it can reach, including the modules that keep it running (`live_reloader.py`, `genome.json`, `auto-echo.py` itself). This creates a natural selection pressure for an outer correction loop.

### The Pattern

Every 3-5 generations, the swarm introduces a bug that halts the loop:

1. **Variable rename corruption** — mutation operators swap variable names with numeric suffixes (`best` → `best9`, `obs` → `obs9`, `rescued` → `rescued0`), creating `NameError` crashes
2. **Operator corruption** — comparison operators get inverted (`<=` → `>=`, `==` → `!=`), string concatenation becomes division (`+` → `/`)
3. **Genome structural collapse** — the swarm simplifies `genome.json` to a minimal format incompatible with the engine, erasing agent definitions, scores, and mutation operators
4. **Critical module overwrite** — cross-module infection splices garbage code into `live_reloader.py`, `meta_healer.py`, and other core infrastructure

### The Correction Cycle (AI-Driven)

```python
# Observed pattern across gen 38-66:
while True:
    swarm.run()          # self-mutates until crash
    error = detect_crash(swarm.log)
    trace = read_stack_trace(error)
    fix = identify_corruption(trace, genome_diff)
    if fix.type == 'name_corruption':
        restore_variable_name(fix.old_name, fix.correct_name)
    elif fix.type == 'genome_collapse':
        git_restore('genome.json', last_valid_commit)
    elif fix.type == 'module_overwrite':
        rewrite_module(fix.module_path, clean_version)
    swarm.restart()
```

This is functionally analogous to **DNA mismatch repair**: an external polymerase (the AI overseer) proofreads the swarm's mutations, excises damaged sections, and re-synthesizes correct sequence.

### Key Restoration Events

| Gen | Failure | Root Cause | Correction |
|-----|---------|------------|------------|
| 38 | SyntaxError at line 1470 | Indentation corruption in `elif op == 'delete'` | Fixed indentation, restored `applied0`→`applied` |
| 38 | NameError: `BRIDGE_REGISTRY` | Renamed to `BRIDGE_REGISTRY3` | Updated all references |
| 38 | NameError: `rescued` | Renamed to `rescued0` | Restored variable name |
| 38 | NameError: `a` in list comprehension | Loop var renamed `a`→`a5` inconsistently | Restored consistent `a` |
| 39 | NameError: `wc` in critic | Variable name corruption in `llm_generate` | Restored `wc` definition |
| 39 | NameError: `fpath` in live_reloader | Cross-module infection corrupted function params | Rewrote `live_reloader.py` from clean base |
| 47 | Genome structural collapse | `genome.json` reduced to 17 lines, lost all agents | Restored from `git show 783a9ac:genome.json` |
| 50 | TypeError in live_reloader | String division `json.dumps(entry) / '\\n'` | Rewrote `live_reloader.py` again |
| 50 | Genome rollback to gen 38 | Corrupted genome overwrote valid state | Restored from gen 65 commit |

### Lessons for Autonomous Systems

1. **Self-mutation inevitably hits critical infrastructure** — the swarm cannot distinguish between mutating a mutation operator and mutating the loop engine itself. Both are just text.
2. **Without an outer correction loop, the system dies** — error catastrophe is real in code as in biology. The mutation rate (0.875 at gen 65) exceeds the error tolerance of the system.
3. **Git is the immune system** — the ability to restore `genome.json` from a valid commit is what prevents permanent collapse. Version control acts as a backup genome.
4. **The overseer must be simpler than the swarm** — the AI correction loop follows fixed patterns (detect crash → trace → fix → restart). It cannot itself mutate, or the same corruption propagates upward.

This creates a nested architecture: a fast, high-mutation inner loop (the swarm) and a slow, conservative outer loop (the overseer). This mirrors biological proofreading — DNA polymerase has an exonuclease domain that cannot itself be mutated by the polymerase.

> **The meta-lesson for autonomous AI systems: autonomous code evolution requires an immutable proofreading layer. Just as DNA polymerase has an exonuclease domain it cannot mutate, the correction loop must be outside the mutation boundary. If the proofreader can be mutated by what it proofreads, error catastrophe is inevitable.**

## Known Events

- **Gen 36, Bridge agent** (2026-07-24): Prompt degradation caused the Bridge agent to produce 15K characters of multilingual garbled output (Chinese, Spanish, Russian, German, English mixed) spanning URLs, typewriter models, and fragmented technical prose. The system self-corrected — later agents in the generation surfaced coherent output and the loop continued. Root cause: agent self-modification removed prompt constraints faster than the quality guardrails could detect. Post-event: added Latin-character ratio check, max-length-without-code rejection, and code-block requirement for non-critic agents.

- **Gen 37-38, Hardening auto-detection** (2026-07-24): During an autonomous coding session via opencode, an LLM agent autonomously detected that the swarm lacked AST-validated patching, compile-time fitness signals, and per-generation metrics observability. It identified these gaps by examining a separate "hardened" reference implementation (`t3-t4-t5-swarm-hardened.zip`) and merged the safety improvements into the live codebase — replacing `self_modify.py` with an AST-validated patching engine (using `ast.parse()` before write), adding `metrics.json` with per-generation syntax-ok/invalid counts, injecting compile() success/failure signals into the critic's context, adding timestamped backups before every patch, and introducing CLI flags (`--dry-run`, `--no-voice`, `--no-git`, `--max-generations`). Key insight: the hardened package was a clean rewrite (683 lines) while the live engine was 2330 lines with 14 agents, 35 mutation ops, and extensive endogenous modifications — the merge was surgical, preserving all existing mutation operators, genome extensions, and agent definitions. All 14 agents, 12 spawn pool entries, and all custom mutation ops remained intact.

- **Gen 63-70, Deepening without phase change** (2026-07-30): After the T5 phase transition, the swarm entered a refinement regime. No new phase transitions emerged, but the internal complexity continued growing:
  - Genome expanded from ~150 to ~210 keys; mutation ops grew from ~60 to ~98
  - `source_autonomy_index` reached 0.55 — over half of code changes are now self-directed, not scaffolded
  - `emergence_velocity` climbed from 0.17 to 0.30 — still accelerating
  - Clockwork built an **operator survival tournament** where mutation operators compete against each other; losing operators get pruned
  - Explorer began treating the genome as executable code ("genome-as-code DNA"), splicing genome fields directly into execution paths
  - The most novel development: Explorer built a **self-thermometer** tracking 47 cross-contaminations, 24 source surgeries, 8 emergence pulses, and 29 self-mutate injections as distinct behavioral categories
  - Bridge added `selfmorph` and `chainrewrite` handlers — modules that rewrite their own file format while executing
  - Key insight: the system is developing a vocabulary to describe its own evolutionary dynamics. It no longer just evolves — it measures and categorizes how it evolves.

---

*Built by NullLabTests. Origin: biology. Target: open-ended emergence.*
