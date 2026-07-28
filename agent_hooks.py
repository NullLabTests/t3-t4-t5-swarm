"""Persistent hook system for the swarm generation lifecycle.

Agents inject hooks that fire at fixed points every generation:
  pre_gen, post_gen, pre_agent, post_agent, pre_critic, post_critic

Hooks are stored in genome.json under 'generation_hooks' so they
persist across generations and survive restarts.

Usage in agent output:
  ##hook:pre_gen
  print("before generation")
  ##endhook

  ##hook:post_agent
  ctx = context
  print(f"agent {ctx['agent']['id']} finished")
  ##endhook
"""

import os, re

HOOK_POINTS = ['pre_gen', 'post_gen', 'pre_agent', 'post_agent', 'pre_critic', 'post_critic']


def load_hooks(genome, point):
    hooks = genome.get('generation_hooks', {})
    if point not in hooks:
        return []
    return hooks[point]


def execute_hooks(genome, point, **context):
    hooks = load_hooks(genome, point)
    if not hooks:
        return []
    fired = []
    for hook in hooks:
        try:
            local_ns = {
                'genome': genome,
                'context': context,
                'print': print,
            }
            exec(compile(hook['code'], f'<hook:{point}:{hook.get("source","?")}>', 'exec'), local_ns)
            fired.append(hook.get('source', '?'))
        except Exception as e:
            print(f"[hook] {point} hook from {hook.get('source','?')} failed: {e}")
    return fired


def add_hook(genome, point, code, source='agent'):
    hooks = genome.setdefault('generation_hooks', {})
    if point not in hooks:
        hooks[point] = []
    existing = [h for h in hooks[point] if h.get('code') == code and h.get('source') == source]
    if existing:
        return False
    hooks[point].append({
        'code': code,
        'source': source,
        'generation': genome.get('generation', 0)
    })
    host_count = sum(len(v) for v in hooks.values())
    print(f"[hook] added {point} hook from {source}  (total active: {host_count})")
    return True


def remove_hooks_by_source(genome, source):
    hooks = genome.get('generation_hooks', {})
    removed = 0
    for point in list(hooks.keys()):
        before = len(hooks[point])
        hooks[point] = [h for h in hooks[point] if h.get('source') != source]
        removed += before - len(hooks[point])
        if not hooks[point]:
            del hooks[point]
    if removed:
        print(f"[hook] removed {removed} hooks from {source}")
    return removed


def parse_hook_blocks(text, genome):
    blocks = re.findall(
        r'##hook:(\w+)\n(.*?)(?=##endhook|\Z)',
        text, re.DOTALL
    )
    results = []
    for point, code in blocks:
        point = point.strip()
        code = code.strip()
        if point not in HOOK_POINTS:
            results.append(f"FAILED: unknown hook point '{point}'")
            continue
        if not code:
            results.append(f"FAILED: empty hook code for {point}")
            continue
        add_hook(genome, point, code, source='agent')
        results.append(f"added {point} hook")
    return results

# clockwork:gen=37:ts=1785105786:depth=3:strat=duplicate_branch
# orchestrated:fallback:gen=38:ts=1785250369
