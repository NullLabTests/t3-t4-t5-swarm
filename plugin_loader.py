#!/usr/bin/env python3
"""Dynamic plugin loader for the swarm substrate.

Agents write .py files into plugins/ with hook functions.
auto-echo.py calls these hooks at each lifecycle stage.
This gives agents the ability to rewrite loop logic by
injecting new behavior between generations.
"""

import importlib.util
import inspect
import os
import sys

PLUGINS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins')

HOOK_POINTS = [
    'before_generation',
    'after_agent',
    'before_critic',
    'after_generation',
    'on_scores',
    'on_mutation',
]

def discover_plugins():
    if not os.path.isdir(PLUGINS_DIR):
        return []
    plugins = []
    for fname in sorted(os.listdir(PLUGINS_DIR)):
        if fname.endswith('.py') and not fname.startswith('_'):
            modpath = os.path.join(PLUGINS_DIR, fname)
            modname = f'substrate_plugin_{fname[:-3]}'
            spec = importlib.util.spec_from_file_location(modname, modpath)
            if spec and spec.loader:
                mod = importlib.util.module_from_spec(spec)
                sys.modules[modname] = mod
                try:
                    spec.loader.exec_module(mod)
                    hooks = {}
                    for hp in HOOK_POINTS:
                        fn = getattr(mod, hp, None)
                        if fn and callable(fn):
                            hooks[hp] = fn
                    if hooks:
                        plugins.append({'name': fname[:-3], 'module': mod, 'hooks': hooks})
                        print(f"[plugin] loaded {fname} ({len(hooks)} hooks)")
                    else:
                        print(f"[plugin] {fname} has no hook functions, skipping")
                except Exception as e:
                    print(f"[plugin] failed to load {fname}: {e}")
    return plugins

def run_hook(plugins, hook, *args, **kwargs):
    results = []
    for plug in plugins:
        fn = plug['hooks'].get(hook)
        if fn:
            try:
                result = fn(*args, **kwargs)
                if result is not None:
                    results.append((plug['name'], result))
            except Exception as e:
                print(f"[plugin] {plug['name']}.{hook} error: {e}")
    return results