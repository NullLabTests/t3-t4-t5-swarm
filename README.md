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
- **T5 (self-evolving)**: Active — autonomous loop running, genome tracking generations, spawn/prune/mutation rules defined

## Known Events

- **Gen 36, Bridge agent** (2026-07-24): Prompt degradation caused the Bridge agent to produce 15K characters of multilingual garbled output (Chinese, Spanish, Russian, German, English mixed) spanning URLs, typewriter models, and fragmented technical prose. The system self-corrected — later agents in the generation surfaced coherent output and the loop continued. Root cause: agent self-modification removed prompt constraints faster than the quality guardrails could detect. Post-event: added Latin-character ratio check, max-length-without-code rejection, and code-block requirement for non-critic agents.

---

*Built by NullLabTests. Origin: biology. Target: open-ended emergence.*
