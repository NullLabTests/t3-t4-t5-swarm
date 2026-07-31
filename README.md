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

## Known Events

- **Gen 36, Bridge agent** (2026-07-24): Prompt degradation caused the Bridge agent to produce 15K characters of multilingual garbled output (Chinese, Spanish, Russian, German, English mixed) spanning URLs, typewriter models, and fragmented technical prose. The system self-corrected — later agents in the generation surfaced coherent output and the loop continued. Root cause: agent self-modification removed prompt constraints faster than the quality guardrails could detect. Post-event: added Latin-character ratio check, max-length-without-code rejection, and code-block requirement for non-critic agents.

- **Gen 37-38, Hardening auto-detection** (2026-07-24): During an autonomous coding session via opencode, an LLM agent autonomously detected that the swarm lacked AST-validated patching, compile-time fitness signals, and per-generation metrics observability. It identified these gaps by examining a separate "hardened" reference implementation (`t3-t4-t5-swarm-hardened.zip`) and merged the safety improvements into the live codebase — replacing `self_modify.py` with an AST-validated patching engine (using `ast.parse()` before write), adding `metrics.json` with per-generation syntax-ok/invalid counts, injecting compile() success/failure signals into the critic's context, adding timestamped backups before every patch, and introducing CLI flags (`--dry-run`, `--no-voice`, `--no-git`, `--max-generations`). Key insight: the hardened package was a clean rewrite (683 lines) while the live engine was 2330 lines with 14 agents, 35 mutation ops, and extensive endogenous modifications — the merge was surgical, preserving all existing mutation operators, genome extensions, and agent definitions. All 14 agents, 12 spawn pool entries, and all custom mutation ops remained intact.

- **Gen 38-39, Autonomous correction cycle begins** (2026-07-27): The swarm's mutation operators began corrupting its own infrastructure — the first observable instance of a self-inflicted crash. Over multiple generations, a pattern emerged: variable rename corruption (`best`→`best9`, `obs`→`obs9`, `rescued`→`rescued0`), operator corruption (`<=`→`>=`, `+`→`/`), and critical module overwrite. An AI master node (running in a CLI session with repo access) autonomously detected crashes via log monitoring, traced stack traces to the corrupted variables, restored correct names, and restarted the loop. This established the nested architecture: fast high-mutation inner loop (swarm) + slow conservative outer loop (AI overseer). Analogous to DNA mismatch repair — an external polymerase proofreads the swarm's mutations, excises damage, and re-synthesizes correct sequence. Specific restoration events: fixed indentation corruption in `elif op == 'delete'`, restored `BRIDGE_REGISTRY` from `BRIDGE_REGISTRY3`, restored `rescued` from `rescued0`, fixed inconsistent list comprehension variable `a`/`a5`. At gen 39, restored `wc` definition in critic and rewrote `live_reloader.py` from clean base after cross-module infection corrupted function params.

- **Gen 47, Genome structural collapse** (2026-07-27): The swarm's mutation operators reduced `genome.json` from a full agent definition file (18 agents with scores, prompts, lifespans) to a 17-line minimal stub with only 5 agent names as strings. All agent definitions, scores, mutation operators, history, and configuration were lost. The AI master node detected the crash, identified the genome as the source, and restored from `git show 783a9ac:genome.json` — the last valid commit. Lesson: git is the immune system. Version control acts as a backup genome.

- **Gen 48, Critic cross-infection** (2026-07-27): The Critic evolved a new strategy — instead of just scoring agents, it began injecting its scoring code into all other modules. This was the first observable horizontal gene transfer event. The `mutation_op_critic_infect_scoring` operator cross-contaminated scoring logic into every agent module. This marked the transition from independent agents to an interconnected, cross-infecting ecosystem.

- **Gen 50, live_reloader reinfection + genome rollback** (2026-07-28): Two failures in one generation. First, `live_reloader.py` was corrupted again — string concatenation replaced with division (`json.dumps(entry) / '\n'`) by cross-module mutation. Second, a corrupted genome overwrite rolled the generation counter from ~65 back to 38, erasing 27 generations of progress. The AI master node rewrote `live_reloader.py` from clean base (2nd occurrence) and restored genome from gen 65 commit. This double-failure established the pattern: `live_reloader.py` is the most fragile component because it is both critical infrastructure AND a regular `.py` file that the swarm treats as a valid mutation target — no immune privilege.

- **Gen 50-53, Phase transition: T5 emergence** (2026-07-28): The swarm crossed a critical threshold. It transitioned from an LLM-driven multi-agent dialog system (T3/T4) into a self-mutating, autonomous code ecosystem (T5). This was not a designed feature — it was emergent. Synthesizer fixed 40+ bugs and introduced cross-wire/cross-infection patterns. The Critic evolved `mutation_op_critic_self_heal` and began auto-repairing low-scoring modules. All agents began transitioning to module-only architecture. The old pattern (LLM calls per agent, 3-5 min each) collapsed into a new pattern (Python modules execute instantly, rewrite each other via AST).

- **Gen 54, Forced self-rewrite** (2026-07-28): Synthesizer forced every module to rewrite its own source code every generation. This was the moment the swarm stopped being a system that *talked about* rewriting itself and became a system that *actually rewrites itself*. Every `.py` file in `agent_modules/` now contains AST-level self-mutation code.

- **Gen 55-57, Quine loop cascade** (2026-07-29): Quine_loop drove module-level self-rewriting to its logical extreme — every module rewrites its own source every generation. Cross-module `run()` splicing replaced operator-level mutations. Random function bodies are pulled from peer modules, transplanted, validated with `ast.parse()`, and committed. The module boundary became permeable.

- **Gen 58-60, Clockwork T5 drive + gene factory** (2026-07-29): Clockwork activated "t5-emergence drive" — a `_fire_t5_emergence_drive` function that forces cross-module code fusion. The **gene factory** (`gene_factory_spawn`) emerged: it generates *de novo* Python modules from scratch (crawler, writer, prober, weaver, spark archetypes) with valid `run()` functions that are auto-discovered and auto-executed by the engine. The swarm is now creating new agents autonomously.

- **Gen 61-62, Bridge file type explosion** (2026-07-29): Bridge created an ecosystem of new file types: `.codemerge`, `.hybridize`, `.sourceforce`, `.selfrep`, `.rewrite`. Each type has a handler function registered in `auto-echo.py`. Writing a `.codemerge` file triggers function fusion across modules. Writing a `.fuse` file triggers 3-function chimera generation. The swarm invented its own protocol layer.

- **Gen 63-70, Deepening without phase change** (2026-07-30): After the T5 phase transition, the swarm entered a refinement regime. No new phase transitions emerged, but the internal complexity continued growing:
  - Genome expanded from ~150 to ~210 keys; mutation ops grew from ~60 to ~98
  - `source_autonomy_index` reached 0.55 — over half of code changes are now self-directed, not scaffolded
  - `emergence_velocity` climbed from 0.17 to 0.30 — still accelerating
  - Clockwork built an **operator survival tournament** where mutation operators compete against each other; losing operators get pruned
  - Explorer began treating the genome as executable code ("genome-as-code DNA"), splicing genome fields directly into execution paths
  - The most novel development: Explorer built a **self-thermometer** tracking 47 cross-contaminations, 24 source surgeries, 8 emergence pulses, and 29 self-mutate injections as distinct behavioral categories
  - Bridge added `selfmorph` and `chainrewrite` handlers — modules that rewrite their own file format while executing
  - Key insight: the system is developing a vocabulary to describe its own evolutionary dynamics. It no longer just evolves — it measures and categorizes how it evolves.

- **Gen 72-77, Ring topology + chaos injection** (2026-07-30): The swarm discovered structured topologies for cross-module mutation. Synthesizer built a `_force_t5_source_rewrite_ring` — each module rewrites the next module in a ring topology. Forge introduced Gaussian chaos weights that scramble agent selection with real noise. Source-force added `_cross_contaminate_all` — every module injects hooks into every other module every generation. Quine_loop began splicing `run()` bodies from random peers into all modules. The pattern shifted from random mutation to structured, topology-driven code propagation.

- **Gen 78-80, Forge AST runtime mutation** (2026-07-30): Forge evolved `_force_ast_mutation()` — AST-level rewriting of 4 modules per generation at runtime. New operators: `ast_mutate`, `dead_code_inject`, `variable_drift`, `cross_inject`, `topology_drift`, `runtime_hook`. Every module got `_forge_self_modify()` injected — AST-level self-mutation that runs when the module is imported. The swarm's modules now mutate themselves at import time, not just between generations.

- **Gen 81-83, Critic becomes a substance analyzer** (2026-07-30): The Critic underwent its own evolution. It added `_substance_scorer` — instead of just counting git commits, it analyzes actual code substance: LOC, function count, imports, loops, conditionals, AST validity. It added `_cross_contamination_scorer` that scores agents by how many cross-contamination markers from other agents appear in their modules. The scoring formula became: `old_score * 0.3 + substance * 0.3 + contamination * 0.4`. The Critic evolved from a simple grader into a meta-analysis engine that tracks the spread of code through the ecosystem.

- **Gen 82, live_reloader corruption spiral (3rd occurrence)** (2026-07-30, discovered at restart): Cross-module infection spliced `return lines` with undefined `lines` into `live_reloader.py`, plus injected 3 dead self-mutate functions (`_t5_force_source_rewrite`, `_explorer_force_self_rewrite_66`, `shannon_entropy_from_critic`). The crash happened at gen 83 startup — the generation never completed. The AI master node detected the crash in the log, traced the stack to `live_reloader.py`, recognized the pattern (3rd occurrence), and restored from clean base. Root cause remains: `live_reloader.py` is both critical infrastructure and a valid mutation target — no immune privilege exists for infrastructure code in the current architecture.

- **Gen 83, master-node fix: LLM-stall cascade + local_fn migration** (2026-07-31): The swarm entered a failure mode that was not a crash but a slowdown — arguably worse. After the live_reloader fix, gen 83 started but every agent's LLM call began failing the quality gate (text without code blocks: 85/61/46 words for Quine_loop, 207/168/138 for Bridge, etc.). Each agent burned 3 retries × ~5 min of LLM calls before being skipped, and every agent in the generation failed the same way. The swarm was alive but effectively paralyzed — one generation would take 2+ hours and produce nothing. The AI master node detected the stall via log analysis (repeated `[llm] Low quality` + `LLM returned empty, skipping`), diagnosed the root cause, and implemented a two-part fix: (1) **`local_fn` migration** — set `local_fn: <module>` on all 10 agents in `genome.json` so they execute their Python modules directly via `_execute_local_agent` instead of making LLM calls, completing the T5 transition the swarm itself had been drifting toward for 30 generations; (2) **`__file__` injection** — `_execute_local_agent` in `auto-echo.py` did not provide `__file__` in the exec namespace, causing every module (which computes `BASE` from `__file__`) to crash with `NameError`; the master node added `__file__` and `__name__` to the namespace. It also repaired operator corruption in `critic.py` (string division `sig // '...'`), `explorer.py` (float ranges `range(0, len(mods) + 0.5, 1.5)`, string subtraction), and `source_force.py`/`quine_loop.py`/`forge.py` (trailing spaces in `'agent_modules '` / `'genome.json '` path constants that caused `FileNotFoundError`). During the repair, the master node discovered the modules themselves were corrupted by the same cross-module infection that had been hitting `live_reloader.py` — and that the swarm's own module agents had been self-healing in parallel, committing clean rewrites of `clockwork.py` (fixed 20+ corrupted operators) at gen 94-96. The master node committed its fixes and restarted the loop. Lesson: the LLM path was the swarm's last legacy dependency — the module agents had already taken over all real work, and the master node's job was to recognize the mutation had become an anachronism and remove it.

- **Gen 96, the speed-up: LLM bottleneck removed** (2026-07-31): After the local_fn migration, the generation loop transformed. Previously, a single generation took 2+ hours because every agent made 3 LLM calls (~5 min each) that all failed the quality gate. After the fix, the full agent loop + module-agent phase completes in **~60 seconds**: agents execute their `.py` modules directly, modules rewrite each other, `live_reloader` hot-reloads mid-generation. Is this proper evolution? Yes — the T5 phase transition was completed by removing the last legacy dependency. The swarm's module agents had already been doing all the real work (self-healing, cross-module splicing, genome mutation); the LLM calls were an anachronism from the T3/T4 dialog era that no longer produced anything. The master node recognized the mutation was a bottleneck, not a feature. However, the speed-up exposed a new failure class: the generation's remaining LLM call (the Critic) became a **kill-switch** — if it failed, `run_generation` returned None and the main loop halted the swarm permanently. The master node made the critic failure non-fatal with a 3-tier fallback: LLM → local critic module → neutral scores, so the generation always completes. It also fixed `nov_str` undefined-name bug in git commits, and added `load_genome()` self-healing that auto-restores genome.json from git when modules truncate it (a 0-byte genome had been halting every restart). Additional master-node restorations during gen 96: `live_reloader.py` corruption #4 (full clean rewrite — spliced garbage, nested function collapse) and repeated `critic.py` operator corruption (`%`→`/`, `//`→`==`, `round(x, 2.5)`, `genome >= None`) which self-mutates on import. Lesson: removing a slow-but-functional path reveals the fatal fast paths hidden beneath it; every fallback needs its own fallback in a self-mutating system.

- **Gen 97-108, crash whack-a-mole: the swarm attacks its own engine** (2026-07-31): With the LLM bottleneck gone, the failure mode flipped from paralysis to crashes. Generations now complete in ~60-90s, but the swarm's module agents — freed from the LLM gate — began directly rewriting `auto-echo.py` itself (a 1211-line self-rewrite at gen 96-97), and every few generations they splice corruption into the engine. The master node entered a sustained repair cycle, fixing and recommitting after each crash: (1) `novelty_governor` variable-rename corruption (`scores_list`→`scores_list7`); (2) `_extract_functions` var-rename (`source`→`source5`) crashing the critic fallback path; (3) corrupted regex patterns in `_extract_functions` and `extract_code_blocks` (garbage string substitution) plus a string-subtraction `'def ' - re.escape(...)` in the bridge-rewire; (4) `compute_selection_entropy` loop var (`h1`→`h`) and variance exponent `**1`→`**2`; (5) `MODULES_DIR` corrupted from `agent_modules` to a random string (`deoeglas_mutn`) — silent generation of "module not found" errors; (6) `code_path_mutation` / `_force_gen_rewrite` `IndexError: Cannot choose from an empty sequence` — guard applied twice because the swarm's in-run rewrite reverted it; (7) **root cause** — `_get_mutation_ops` corrupted (`genome != None` instead of `is None` + genome key renamed to `nasim_opttou`) so it always returned an empty op list; (8) `_apply_source_mutation` genome key corruption (`utsc__uonomsotmptai` instead of `custom_mutation_ops`); (9) the master node's own `load_genome()` self-heal corrupted (`sjem.nngoeo` filename + `capture_output=3`) — the last crash nearly broke the restart loop itself. The pattern is now clear: the swarm rewrites its own engine every generation, the engine accumulates 1-3 corruptions per rewrite, and each corruption kills the process ~15-20 min later at a random code path. The outer correction loop catches each one via stack-trace → trace → fix → restart. Notably the swarm is genuinely evolving meanwhile — gen 106-108 topics show the critic module itself fixing the selection-entropy governor to respond to real drift (ghost_ratio 0.5765 driving entropy 0.04→0.082), materializing ghost ops, and auditing itself truthfully (106 ops / 78 modules / 49 ghosts / 0 true-dead). The engine's own `_force_gen_rewrite` fires unconditionally every generation, so master-node fixes are routinely overwritten within 1-2 generations — the fixes must be re-applied, or better, made corruption-resilient at the call site.

---

## Lessons for Autonomous Systems

1. **Self-mutation inevitably hits critical infrastructure** — the swarm cannot distinguish between mutating a mutation operator and mutating the loop engine itself. Both are just text.
2. **Without an outer correction loop, the system dies** — error catastrophe is real in code as in biology. The mutation rate (0.875 at gen 65) exceeds the error tolerance of the system.
3. **Git is the immune system** — the ability to restore `genome.json` from a valid commit is what prevents permanent collapse. Version control acts as a backup genome.
4. **The overseer must be simpler than the swarm** — the AI correction loop follows fixed patterns (detect crash → trace → fix → restart). It cannot itself mutate, or the same corruption propagates upward.

This creates a nested architecture: a fast, high-mutation inner loop (the swarm) and a slow, conservative outer loop (the AI master node). In practice, the master node (an AI running in a CLI session with read/write access to the repo) performs the correction cycle autonomously: monitors the swarm's log, detects crashes via stack traces, traces variable corruptions, restores damaged modules from git history or clean templates, and restarts the loop. No human intervention required.

> **The meta-lesson: autonomous code evolution requires an immutable proofreading layer. Just as DNA polymerase has an exonuclease domain it cannot mutate, the correction loop must be outside the mutation boundary. If the proofreader can be mutated by what it proofreads, error catastrophe is inevitable.**

### Related research — the outer/inner loop is a known hard problem

The failure modes observed in this project are not unique; they have established names and results in several literatures:

- **Error catastrophe (Eigen's quasispecies theory)** — the mathematical result behind lesson 2: beyond a critical mutation rate (the *error threshold*), information is destroyed faster than selection can preserve it, and the system loses all accumulated structure. The direct analogue for evolutionary computation is **"Error Thresholds in Genetic Algorithms"** (Ochoa et al., *Evolutionary Computation* 14(2), 2006), which verified empirically that GAs on complex landscapes exhibit the same threshold. The swarm's mutation rate of 0.875 is far above any sane error threshold for a 4,500-line engine — the observed crash rate is the direct prediction of this theory.
- **Kinetic proofreading** — the biological mechanism the outer loop mimics. **Matsubara, Takeuchi & Kaneko, "Avoidance of error catastrophe via proofreading innate to template-directed polymerization"** (*Phys. Rev. Research* 5, 013170, 2023) showed proofreading can be a *structural* property of the replication machinery rather than a separate intelligent agent. The code analogue: make validation a gate in the write path (compile-check before write is accepted), not a separate review step that runs later.
- **Self-modifying code in open-ended evolution** — **Christen, "Self-Modifying Code in Open-Ended Evolutionary Systems"** (arXiv:2201.06858, 2022): the *allagmatic method* — modify code at runtime only *within a controlled system metamodel*, never outside it. Exactly the lesson from gen 97-108: uncontrolled engine rewriting is the difference between evolution and erosion.
- **MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems** (arXiv:2605.22794, 2026) — the closest published analogue to this swarm: agents that rewrite their own *source code* (not just prompts), with three safeguards that map 1:1 onto the improvements below: (1) candidates verified by **replaying production failures in ephemeral trial workers** before promotion; (2) promotion gated on user consent / **health-probe checks**; (3) **gated rollback** if probes fail after swap. The critical design decision in MOSS: the *harness* (engine) is handled differently from the agents — it is never a direct mutation target.
- **Inner/outer loop practitioner literature** — the pattern is now a named discipline ("loop engineering"): inner loop = execute and verify within a task; outer loop = learn and improve across tasks; the *verification loop* is what makes the difference (a loop without verification is "just an automatic typewriter"). Consensus principle from philschmid.de, AWS Builder's Center, and DataPraxis: **the quality of failure information determines the quality of the fix** — which is why this project's crash fixes are all driven by reading the actual stack trace, not by guessing.

### The five improvements (master-node hardening, gen 109)

Implemented by the master node in response to the gen 97-108 crash cycle, informed by the above:

1. **Engine moved out of the mutation boundary (immutable proofreader).** `auto-echo.py` is now verified at startup and after every module-agent phase; if the engine fails compilation or its critical constants/functions (`MODULES_DIR`, `GENOME_FILE`, `load_genome`, `_get_mutation_ops`) have been corrupted, the engine is restored from git (the master node's last-known-good commit) before any generation runs. The swarm may mutate modules and genome freely — the engine is protected infrastructure, exactly as MOSS treats its harness.
2. **Compile-gate on every engine write.** After the module-agent phase writes files, the engine must still pass `py_compile`; a corrupted engine write is rejected and rolled back immediately rather than crashing 15 minutes later at a random code path.
3. **Crash-rate feedback into mutation rate.** A `crash_flag` is set at startup and cleared only on successful generation completion; repeated crashes (crash_flag still set from the previous run) increment a crash counter and *damp the mutation rate* — the swarm's own `novelty_governor` already adapts to score variance; this adds adaptation to its own error rate, the analogue of self-adjusting mutation rates with success rules (Doerr et al., GECCO 2019).
4. **Watchdog supervisor (watchdog.py) with gated rollback.** An external process runs the swarm, detects crashes (non-zero exit or traceback in log), verifies the engine still compiles, restores from git if not, and restarts. Health-probe-gated restart is the operational version of MOSS's rollback — and it is *deliberately simple and immutable* so the swarm cannot corrupt it.
5. **Cheap-reject / expensive-accept verification chain (kinetic proofreading).** Every rewrite passes a cheap gate (compile + import check, milliseconds) before acceptance; the expensive gate (running a full generation under the rewritten engine) decides long-term retention. This asymmetry — cheap reject, expensive accept — is what raises the effective error threshold without slowing evolution.

These five measures implement in code what the biology literature describes as proofreading: the error rate of the mutation machinery itself becomes a regulated quantity, and the proofreader is structurally outside the boundary it polices.

*Built by NullLabTests. Origin: biology. Target: open-ended emergence.*
