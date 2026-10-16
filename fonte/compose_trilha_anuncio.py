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
DROP = 13.25
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

# ------------------------------------------------ SEÇÃO A: tensão (Ré menor)
# cordas em trêmolo crescendo
chord(TREM, [50, 53, 57], 0.0, 7.35, 70)            # Dm
chord(TREM, [46, 50, 53], 7.35, 3.0, 80)             # Bb
chord(TREM, [45, 49, 52], 10.35, 2.9, 88)            # A (dominante)
ramp(TREM, 11, 50, 110, 0.0, 7.0)
ramp(TREM, 11, 90, 127, 7.35, 13.2)
# pulso grave do piano em cada tempo (relógio correndo)
t = 0.0; i = 0
while t < DROP - 0.05:
    vel = 52 + 30 * (t / DROP)
    note(PIANO, 38, t, BEAT * 0.45, vel)
    if t > 3.2:
        note(PIANO, 26, t, BEAT * 0.45, vel - 10)
    t += BEAT; i += 1
# motivo agudo (pergunta sem resposta)
for k, (n, at) in enumerate([(69, 3.25), (65, 4.2), (64, 5.15), (62, 6.1)]):
    note(PIANO, n, at, 0.9, 70)
    note(PIANO, n + 12, at, 0.9, 40)
# revelação (7,35 s): pad + coro + arpejo acelerando
chord(PAD, [62, 65, 69, 74], 7.35, 5.9, 70)
ramp(PAD, 11, 40, 120, 7.35, 13.0)
chord(CHOIR, [62, 69], 7.35, 3.0, 64); chord(CHOIR, [62, 70], 10.35, 2.9, 72)
arp = [62, 65, 69, 74, 69, 65]
t = 7.35; k = 0
while t < 12.25:
    note(PIANO, arp[k % 6], t, BEAT * 0.5, 58 + 30 * (t - 7.35) / 5)
    t += BEAT / 2; k += 1
arpA = [61, 64, 69, 73, 76]                          # Lá maior subindo
t = 12.25; k = 0
while t < DROP - 0.06:
    note(PIANO, arpA[k % 5] + 12 * (k // 5), t, BEAT * 0.25, 80 + k * 2)
    t += BEAT / 4; k += 1
# rufo de caixa crescendo para a virada
t = 12.0; k = 0
while t < DROP - 0.04:
    note(DR, 38, t, 0.05, 30 + 85 * (t - 12.0) / (DROP - 12.0))
    t += BEAT / 4; k += 1
# impactos sincronizados com o texto
note(TAIKO, 50, 0.0, 1.0, 120); note(TIMP, 38, 0.0, 1.5, 110)
note(TAIKO, 50, 1.30, 1.0, 127); note(TIMP, 38, 1.30, 2.0, 120); note(DR, 49, 1.30, 1.5, 90)
chord(PIANO, [26, 33, 38], 1.30, 1.6, 100)
note(TAIKO, 50, 3.45, 1.0, 110); note(TIMP, 45, 3.70, 1.2, 100)
note(TIMP, 38, 7.35, 2.0, 110); note(DR, 49, 7.35, 2.0, 70)
note(TAIKO, 50, 8.0, 1.0, 105); note(TAIKO, 50, 8.4, 1.0, 112)

# ------------------------------------------------ SEÇÃO B: virada (124,4 BPM)
#                 acorde (cordas)        baixo  piano (voicing)
prog_b = [([50, 53, 57], 38, [62, 65, 69]),     # Dm
          ([46, 50, 53], 34, [62, 65, 70]),     # Bb
          ([48, 53, 57], 41, [60, 65, 69]),     # F
          ([48, 52, 55], 36, [60, 64, 67]),     # C
          ([50, 53, 57], 38, [62, 65, 69]),     # Dm  (capa, 21 s)
          ([46, 50, 53], 34, [62, 65, 70]),     # Bb
          ([48, 53, 57], 41, [60, 65, 69]),     # F
          ([48, 52, 55], 36, [60, 64, 67])]     # C   (carimbo, 26,75 s)
melody = {4: [(81, 0, 1.5), (79, 1.5, 0.5), (77, 2, 1), (76, 3, 1)],
          5: [(77, 0, 1.5), (76, 1.5, 0.5), (74, 2, 2)],
          6: [(72, 0, 1), (77, 1, 1), (81, 2, 1.5), (79, 3.5, 0.5)],
          7: [(79, 0, 2), (76, 2, 1), (74, 3, 1)]}
for b, (strs, root, pv) in enumerate(prog_b):
    t0 = DROP + b * BAR
    full = b >= 2
    chord(STR, strs + [strs[0] + 12], t0, BAR, 74 + 4 * b)
    chord(PAD, [n + 12 for n in strs], t0, BAR, 60)
    # baixo em colcheias
    for e in range(8):
        note(BASS, root, t0 + e * BEAT / 2, BEAT * 0.42, 92 if e % 2 == 0 else 74)
    # piano: acordes sincopados
    for off, d, v in [(0, 1.0, 88), (1.5, 0.5, 70), (2.0, 1.0, 84), (3.5, 0.5, 70)]:
        chord(PIANO, pv, t0 + off * BEAT, d * BEAT * 0.95, v)
        note(PIANO, root + 12, t0 + off * BEAT, d * BEAT * 0.95, v - 10)
    # melodia a partir da capa
    for n, off, d in melody.get(b, []):
        note(PIANO, n, t0 + off * BEAT, d * BEAT * 0.95, 96)
        note(STR, n - 12, t0 + off * BEAT, d * BEAT * 0.95, 70)
    # bateria
    for q in range(4):
        tq = t0 + q * BEAT
        if full or q in (0, 2):
            note(DR, 36, tq, 0.1, 112 if q in (0, 2) else 96)
        if full and q in (1, 3):
            note(DR, 39, tq, 0.1, 96); note(DR, 38, tq, 0.1, 60)
        note(DR, 42, tq + BEAT / 2, 0.05, 52)
        if full:
            note(DR, 42, tq, 0.05, 40)
    if b in (0, 4, 7):
        note(DR, 49, t0, 2.0, 110 if b else 120)
    if b == 3:                                       # virada de tons antes da capa
        for k, n in enumerate([50, 48, 47, 45, 43, 41]):
            note(DR, n, t0 + 3 * BEAT + k * BEAT / 6, 0.1, 80 + k * 6)
note(TAIKO, 50, DROP, 1.0, 120); note(TIMP, 38, DROP, 1.5, 115)
note(TAIKO, 50, DROP + 4 * BAR, 1.0, 110)
note(TAIKO, 50, DROP + 7 * BAR, 1.0, 127); note(TIMP, 41, DROP + 7 * BAR, 1.5, 115)
# acorde final (Fá maior) soando até o fim
END = DROP + 8 * BAR
chord(STR, [41, 48, 53, 57, 60, 65], END, 2.5, 96)
chord(PIANO, [29, 41, 60, 65, 69, 72], END, 2.5, 100)
chord(PAD, [65, 69, 72, 77], END, 2.5, 70)
note(BASS, 29, END, 1.5, 100)
note(DR, 49, END, 2.5, 112); note(DR, 36, END, 0.2, 120); note(TIMP, 41, END, 2.0, 110)

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
mid.save(HERE + '/trilha.mid')

raw = HERE + '/trilha_raw.wav'
subprocess.run(['fluidsynth', '-ni', '-q', '-g', '0.7', '-r', '44100', '-F', raw, SF2, HERE + '/trilha.mid'], check=True)

# ------------------------------------------------ masterização simples
with wave.open(raw) as w:
    sr = w.getframerate(); ch = w.getnchannels()
    x = np.frombuffer(w.readframes(w.getnframes()), '<i2').astype(np.float32).reshape(-1, ch) / 32768
n = int(sr * 30.0)
x = np.vstack([x, np.zeros((max(0, n - len(x)), ch), np.float32)])[:n]
tt = np.arange(n) / sr
x *= np.clip((30.0 - tt) / 0.6, 0, 1)[:, None]                  # fade final
x *= 0.95 / max(1e-6, np.abs(x).max())
x = np.tanh(x * 1.6) / np.tanh(1.6)                             # compressão suave
x *= 0.89 / np.abs(x).max()
with wave.open(HERE + '/trilha.wav', 'wb') as w:
    w.setnchannels(ch); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((x * 32767).astype('<i2').tobytes())
print('ok', len(ev), 'eventos')
