"""Trilha do anúncio (30 s), composta em MIDI e renderizada com FluidSynth + FluidR3_GM (licença MIT).
Seção A (0–13,25 s): tensão em Ré menor. Seção B (13,25–30 s): virada confiante, 124,4 BPM,
com compassos alinhados às cenas (21,0 s = capa; 26,75 s = carimbo ENVIADO)."""
import subprocess, sys, wave
import numpy as np
import mido

HERE = '/tmp/claude-0/-home-user-minc/cfea5460-ff64-5d6e-92a7-67dee7b7da1d/scratchpad/video'
SF2 = '/usr/share/sounds/sf2/FluidR3_GM.sf2'
BEAT = 13.5 / 28            # 0,4821 s → 124,4 BPM
TPB = 480
DROP = 13.6
BAR = BEAT * 4

ev = []                     # (segundos, mensagem)
def note(ch, n, t, dur, vel):
    ev.append((t, mido.Message('note_on', channel=ch, note=n, velocity=int(max(1, min(127, vel))))))
    ev.append((t + dur, mido.Message('note_off', channel=ch, note=n, velocity=0)))
def chord(ch, ns, t, dur, vel):
    for n in ns:
        note(ch, n, t, dur, vel)
def cc(ch, num, val, t):
    ev.append((t, mido.Message('control_change', channel=ch, control=num, value=int(max(0, min(127, val))))))
def prog(ch, p, vol, pan=64, rev=60):
    ev.append((0, mido.Message('program_change', channel=ch, program=p)))
    cc(ch, 7, vol, 0); cc(ch, 10, pan, 0); cc(ch, 91, rev, 0); cc(ch, 11, 127, 0)
def ramp(ch, num, v0, v1, t0, t1, steps=24):
    for i in range(steps + 1):
        cc(ch, num, v0 + (v1 - v0) * i / steps, t0 + (t1 - t0) * i / steps)

PIANO, STR, TREM, PAD, BASS, TIMP, TAIKO, CHOIR, DR = 0, 1, 2, 3, 4, 5, 6, 7, 9
prog(PIANO, 0, 108, 60, 70)
prog(STR, 48, 92, 70, 80)
prog(TREM, 44, 88, 58, 80)
prog(PAD, 89, 70, 64, 90)
prog(BASS, 33, 100, 64, 30)
prog(TIMP, 47, 112, 64, 70)
prog(TAIKO, 116, 110, 64, 60)
prog(CHOIR, 52, 72, 64, 90)
cc(DR, 7, 104, 0); cc(DR, 91, 40, 0)


# ================================================ VÍDEO 2 (17 s)
DUR2 = 17.0
# Cena 1 (0–6,4): tensão em Ré menor
chord(TREM, [50, 53, 57], 0.0, 6.5, 72); ramp(TREM, 11, 55, 112, 0.0, 6.3)
t = 0.0
while t < 6.4:
    note(PIANO, 38, t, BEAT * 0.45, 55 + 25 * t / 6.4); note(PIANO, 26, t, BEAT * 0.45, 45 + 20 * t / 6.4)
    t += BEAT
note(TAIKO, 50, 0.0, 1.0, 118); note(TIMP, 38, 0.0, 1.5, 105)
note(TAIKO, 50, 2.60, 1.0, 127); note(TIMP, 38, 2.60, 2.0, 122); note(DR, 49, 2.60, 1.6, 92)
chord(PIANO, [26, 33, 38], 2.60, 1.8, 104)
for n, at in [(69, 3.6), (65, 4.4), (64, 5.2), (62, 6.0)]:
    note(PIANO, n, at, 0.8, 68); note(PIANO, n + 12, at, 0.8, 38)
# Cena 2 (6,6–10,6): respiro — Si bemol → Fá, coro e pad
chord(PAD, [58, 62, 65, 70], 6.6, 2.0, 72); chord(PAD, [57, 60, 65, 69], 8.6, 2.1, 76)
chord(CHOIR, [62, 70], 6.6, 2.0, 66); chord(CHOIR, [60, 69], 8.6, 2.1, 72)
chord(STR, [46, 53, 58], 6.6, 2.0, 70); chord(STR, [41, 48, 57], 8.6, 2.1, 76)
note(TIMP, 34, 6.6, 1.5, 100); note(DR, 49, 6.6, 1.5, 60)
arp = [70, 74, 77, 74]; t = 6.6; k = 0
while t < 8.6:
    note(PIANO, arp[k % 4], t, BEAT * 0.5, 62); t += BEAT / 2; k += 1
arp = [69, 72, 77, 72]
while t < 10.6:
    note(PIANO, arp[k % 4], t, BEAT * 0.5, 66); t += BEAT / 2; k += 1
# Cena 3 (10,8–13,0): a porta fecha — subida e rufo, golpe e silêncio
chord(TREM, [45, 49, 52], 10.8, 2.2, 90); ramp(TREM, 11, 60, 127, 10.8, 12.95)
for i, n in enumerate(range(57, 69)):
    note(STR, n, 10.8 + i * 0.18, 0.2, 70 + i * 3)
t = 11.0
while t < 12.98:
    note(DR, 38, t, 0.05, 30 + 90 * (t - 11.0) / 2.0); note(TIMP, 45, t, 0.1, 40 + 70 * (t - 11.0) / 2.0)
    t += BEAT / 4
note(TAIKO, 50, 10.85, 1.0, 112)
note(TAIKO, 50, 13.0, 1.2, 127); note(TIMP, 38, 13.0, 1.0, 127); chord(PIANO, [21, 26, 33], 13.0, 0.5, 120)
# Cena 4 (13,6–17): resolução — Si bemol → Fá maior
for b, (strs, root, pv) in enumerate([([46, 50, 53], 34, [62, 65, 70])]):
    t0 = DROP
    chord(STR, strs + [strs[0] + 12], t0, BAR, 86); chord(PAD, [n + 12 for n in strs], t0, BAR, 62)
    for e in range(8):
        note(BASS, root, t0 + e * BEAT / 2, BEAT * 0.42, 92 if e % 2 == 0 else 74)
    for off, d, v in [(0, 1.0, 90), (1.5, 0.5, 72), (2.0, 1.0, 86), (3.5, 0.5, 72)]:
        chord(PIANO, pv, t0 + off * BEAT, d * BEAT * 0.95, v)
    for q in range(4):
        tq = t0 + q * BEAT
        note(DR, 36, tq, 0.1, 110); note(DR, 42, tq + BEAT / 2, 0.05, 50)
        if q in (1, 3):
            note(DR, 39, tq, 0.1, 90)
    for n, off, d in [(77, 0, 1.5), (79, 1.5, 0.5), (81, 2, 2)]:
        note(PIANO, n, t0 + off * BEAT, d * BEAT * 0.95, 98)
note(DR, 49, DROP, 2.0, 118); note(TAIKO, 50, DROP, 1.0, 112)
END = DROP + BAR
chord(STR, [41, 48, 53, 57, 60, 65], END, 1.6, 98); chord(PIANO, [29, 41, 60, 65, 69, 72], END, 1.6, 102)
chord(PAD, [65, 69, 72, 77], END, 1.6, 72); note(BASS, 29, END, 1.4, 100)
note(DR, 49, END, 1.6, 110); note(DR, 36, END, 0.2, 118); note(TIMP, 41, END, 1.5, 110)

# ------------------------------------------------ grava MIDI
mid = mido.MidiFile(ticks_per_beat=TPB)
tr = mido.MidiTrack(); mid.tracks.append(tr)
tr.append(mido.MetaMessage('set_tempo', tempo=int(BEAT * 1e6), time=0))
ev.sort(key=lambda x: (x[0], 0 if x[1].type in ('program_change', 'control_change') else (1 if x[1].type == 'note_off' else 2)))
last = 0
for t, m in ev:
    tick = int(round(t / BEAT * TPB))
    m.time = max(0, tick - last); last = max(last, tick)
    tr.append(m)
mid.save(HERE + '/trilha2.mid')

raw = HERE + '/trilha2_raw.wav'
subprocess.run(['fluidsynth', '-ni', '-q', '-g', '0.7', '-r', '44100', '-F', raw, SF2, HERE + '/trilha2.mid'], check=True)

# ------------------------------------------------ masterização simples
with wave.open(raw) as w:
    sr = w.getframerate(); ch = w.getnchannels()
    x = np.frombuffer(w.readframes(w.getnframes()), '<i2').astype(np.float32).reshape(-1, ch) / 32768
n = int(sr * DUR2)
x = np.vstack([x, np.zeros((max(0, n - len(x)), ch), np.float32)])[:n]
tt = np.arange(n) / sr
x *= np.clip((DUR2 - tt) / 0.5, 0, 1)[:, None]                  # fade final
x *= 0.95 / max(1e-6, np.abs(x).max())
x = np.tanh(x * 1.6) / np.tanh(1.6)                             # compressão suave
x *= 0.89 / np.abs(x).max()
with wave.open(HERE + '/trilha2.wav', 'wb') as w:
    w.setnchannels(ch); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((x * 32767).astype('<i2').tobytes())
print('ok', len(ev), 'eventos')
