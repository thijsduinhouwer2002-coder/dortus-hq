"""Spoor van de echte X-muis tijdens de opname (Regisseur, 25 nov 2026, issue #75).
Waarom: ffmpeg x11grab tekent de muispijl onder Xvfb maar af en toe (lokale proef: in 3 s maar 9 beelden met pijl),
dus de pijl springt en verdwijnt. Dit proces leest 60 keer per seconde de echte plek van de muis (xdotool
getmouselocation) met de tijd; de montage zet op elk beeld de pijl op die echte plek, zoals OBS dat ook doet.
Gebruik: python3 muisspoor.py <uitbestand>  (stopt bij SIGTERM/SIGINT)"""
import signal
import subprocess
import sys
import time

uit = open(sys.argv[1], "w", buffering=1)
loop = [True]
signal.signal(signal.SIGTERM, lambda *_: loop.__setitem__(0, False))
signal.signal(signal.SIGINT, lambda *_: loop.__setitem__(0, False))
while loop[0]:
    r = subprocess.run(["xdotool", "getmouselocation", "--shell"], capture_output=True, text=True).stdout
    w = dict(regel.split("=", 1) for regel in r.split() if "=" in regel)
    if "X" in w:
        uit.write(f"{time.time():.4f} {w['X']} {w['Y']}\n")
    time.sleep(1 / 60)
