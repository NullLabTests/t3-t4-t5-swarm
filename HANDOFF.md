# Echo: Session Handoff

## Where we left off (updated 2026-07-24)

**Generation 4 complete** — avg 7.5/10. Mutator injected 2 mutations (analyzer voice: alan→southern, synthesizer prompt appended threshold constraint). Critic scored, all agents survived.

### What was built this session:
- `evolve.py` — State orchestrator (NOT recursive opencode). Commands: `status`, `prompt`, `record`, `score`, `mutate`, `next`. Manages genome.json + conversation state.
- `novelty.py` — Semantic distance tracker (char n-gram Jaccard). Computes novelty between utterances.
- `echo.py` — Added `evolve` and `prompt` commands that delegate to evolve.py.

### The loop (how to run gen 5):
```bash
python3 echo.py evolve              # see state, next agent
python3 evolve.py prompt explorer   # get prompt for explorer
# Write response, then:
python3 evolve.py record explorer "your text"
python3 evolve.py prompt analyzer   # ... continue through all agents
# After critic scores, apply mutation:
python3 evolve.py mutate '{"mutations": [{"type": "swap_voice", "target": "x", "value": "y"}]}'
```

### Why opencode doesn't call itself:
Previous session crashed from recursive opencode-in-opencode. Now `evolve.py` is a pure state manager. YOU (opencode) read the prompts, generate responses as each persona, and use `evolve.py` to record/score/mutate. No recursion.

### Files:
| File | Purpose |
|------|---------|
| `echo.py` | Voice I/O: record mic (whisper), speak (Piper+sox), log, evolve status |
| `evolve.py` | State orchestrator: genome + log management |
| `novelty.py` | Semantic distance tracker (0-1) |
| `genome.json` | Agent definitions, scores, generation history |
| `echo_conversation.jsonl` | Running log of all exchanges (12 utterances so far) |
| `specs-and-lessons.txt` | Full architecture docs |
| `voices/` | Piper TTS voice models |

### Next:
Generation 5 needs: explorer → analyzer → synthesizer → mutator → critic → mutation → genome update.
Run `python3 echo.py evolve` to start.