"""Echte muis zacht van A naar B, los van Blender (Regisseur, 25 nov 2026, issue #75).
Waarom los: Blender tekent in software-GL maar 10 tot 20 keer per seconde; als de muis alleen in die tikken beweegt,
springt hij in de opname. Dit proces zet de X-muis 90 keer per seconde met xdotool, met een rustige versnelling en
een kleine boog zoals een hand. Gebruik: python3 glij.py x0 y0 x1 y1 duur [boog]"""
import math
import subprocess
import sys
import time

x0, y0, x1, y1, duur = (float(a) for a in sys.argv[1:6])
boog_f = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0
dx, dy = x1 - x0, y1 - y0
d = math.hypot(dx, dy)
nx, ny = (-dy / d, dx / d) if d > 0 else (0.0, 0.0)
boog = min(36.0, d * 0.07) * boog_f * (1 if int(x0 + y1) % 2 else -1)
t0 = time.time()
while True:
    t = min(1.0, (time.time() - t0) / max(0.05, duur))
    e = t * t * t * (t * (6 * t - 15) + 10)
    b = math.sin(math.pi * e) * boog
    x, y = x0 + dx * e + nx * b, y0 + dy * e + ny * b
    subprocess.run(["xdotool", "mousemove", str(int(round(x))), str(int(round(y)))], check=False)
    if t >= 1.0:
        break
    time.sleep(1 / 90)
