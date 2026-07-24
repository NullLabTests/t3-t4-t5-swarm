#!/usr/bin/env python3
"""Echo: multi-agent self-dialogue engine. Usage:
  python3 echo.py record          -> record mic, print transcribed text
  python3 echo.py speak <role> text  -> speak text as role, log it
  python3 echo.py log             -> print the full conversation log

Roles: explorer, analyzer, synthesizer, critic
Voices: southern (exp), alan (anl), lessac (syn), amy (crit)

All logs written to ~/t3-t4/echo_conversation.jsonl
"""
import pyaudio, wave, struct, os, sys, json, subprocess
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
VOICES_DIR = os.path.join(BASE, 'voices')
LOG_FILE = os.path.join(BASE, 'echo_conversation.jsonl')
os.environ['XDG_CACHE_HOME'] = '/tmp'

AGENTS = {
    "explorer":      {"voice": "southern", "name": "Explorer"},
    "analyzer":      {"voice": "alan",     "name": "Analyzer"},
    "synthesizer":   {"voice": "lessac",   "name": "Synthesizer"},
    "critic":        {"voice": "amy",      "name": "Critic"},
}

def record():
    CHUNK = 1024; FORMAT = pyaudio.paInt16; RATE = 44100; SECONDS = 6; GAIN = 5.0
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)
    frames = []
    for _ in range(0, int(RATE / CHUNK * SECONDS)):
        frames.append(stream.read(CHUNK))
    stream.stop_stream(); stream.close()
    raw = b''.join(frames)
    samples = list(struct.unpack('<' + 'h' * (len(raw)//2), raw))
    samples = [max(-32768, min(32767, int(s * GAIN))) for s in samples]
    with wave.open('/tmp/mic_capture.wav', 'wb') as wf:
        wf.setnchannels(1); wf.setsampwidth(p.get_sample_size(FORMAT)); wf.setframerate(RATE)
        wf.writeframes(struct.pack('<' + 'h' * len(samples), *samples))
    p.terminate()
    import whisper
    model = whisper.load_model('tiny')
    result = model.transcribe('/tmp/mic_capture.wav', fp16=False, language='en')
    return result['text'].strip()

def speak(role, text):
    if role not in AGENTS:
        print(f"Unknown role: {role}. Options: {list(AGENTS.keys())}")
        return
    voice = AGENTS[role]["voice"]
    model_path = os.path.join(VOICES_DIR, f'{voice}.onnx')
    proc = subprocess.Popen(
        ['piper', '--model', model_path, '--output-raw'],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    sox = subprocess.Popen(
        ['sox', '-t', 'raw', '-r', '22050', '-e', 'signed', '-b', '16', '-c', '1',
         '-', '-t', 'raw', '-', 'pitch', '-300'],
        stdin=proc.stdout, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    aplay_p = subprocess.Popen(
        ['aplay', '-r', '22050', '-f', 'S16_LE', '-c', '1'],
        stdin=sox.stdout, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    proc.stdin.write(text.encode('utf-8'))
    proc.stdin.close()
    proc.wait(); sox.wait(); aplay_p.wait()
    entry = json.dumps({
        "time": datetime.now().isoformat(), "role": role,
        "agent": AGENTS[role]["name"], "text": text
    })
    with open(LOG_FILE, 'a') as f:
        f.write(entry + '\n')

def show_log():
    if not os.path.exists(LOG_FILE):
        print("(empty)")
        return
    with open(LOG_FILE) as f:
        for line in f:
            e = json.loads(line)
            print(f'[{e["time"][:19]}] {e["agent"]}: {e["text"]}')

def evolve_status():
    """Print current evolution state and next agent due."""
    subprocess.run([sys.executable, os.path.join(BASE, 'evolve.py'), 'status'])
    print()
    subprocess.run([sys.executable, os.path.join(BASE, 'evolve.py'), 'next'])

def show_prompt(role):
    """Show the generation prompt for an agent role."""
    subprocess.run([sys.executable, os.path.join(BASE, 'evolve.py'), 'prompt', role])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'record':
        text = record(); print(text)
    elif cmd == 'speak':
        if len(sys.argv) < 4:
            print("Usage: python3 echo.py speak <role> <text>")
            sys.exit(1)
        speak(sys.argv[2], sys.argv[3])
    elif cmd == 'log':
        show_log()
    elif cmd == 'evolve':
        evolve_status()
    elif cmd == 'prompt':
        if len(sys.argv) < 3:
            print("Usage: python3 echo.py prompt <role>")
            sys.exit(1)
        show_prompt(sys.argv[2])
    else:
        print(__doc__)
