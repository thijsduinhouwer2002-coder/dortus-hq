"""CPU binnen één run: spelregel-blokken aan en uit (startargument wissel=regels, kern/proef.gd). Bram 17 nov 2026.

Vraag Sanne 17 nov 04:01: zit de +28% per beeld van het .exe-paar in de spelregel-commits van 959aef4?
Het spel draait per minuut een vaste rondgang van vier standen (minuut % 4):
  0 alles aan, 1 kaartje uit, 2 regels uit (plat/op, naamgenoot, graafbonus), 3 alles uit.
Gebruik: python3 cpu_regels.py <map met cpu-per-10s.txt en hol.log> [...]

Elke meting `HOL meting t=` beslaat de 10 s ervoor; alleen metingen midden in een minuut (t%60 van 20 tot 50) tellen.
Uitlijning (Iris keuring 15): één vaste L voor de hele run, standaard -1; met L=<n> als extra argument een andere.
De L staat in de uitvoer. Binnen één run is er geen tweede runner, dus wat overblijft is de prijs van het blok.
"""
import re, sys, statistics as S

STANDEN = {0: 'alles aan', 1: 'kaartje uit', 2: 'regels uit', 3: 'alles uit'}

L = -1
mappen = []
for a in sys.argv[1:]:
    if a.startswith('L='):
        L = int(a[2:])
    else:
        mappen.append(a)

for d in mappen:
    cpu = [float(x) for x in open(d + '/cpu-per-10s.txt').read().split()]
    log = open(d + '/hol.log').read()
    m = [(int(a), int(b), int(c)) for a, b, c in re.findall(r'meting t=(\d+) beelden=(\d+) helden=(\d+)', log)]
    wissels = len(re.findall(r'HOL wissel regels stand', log))
    c = cpu[max(0, L):]
    mm = m[max(0, -L):]
    n = min(len(c), len(mm))
    groep = {k: [] for k in STANDEN}
    for (t, b, h), x in zip(mm[:n], c[:n]):
        if not (20 <= t % 60 <= 50):
            continue
        groep[(t // 60) % 4].append((x, b, h))
    print(f"{d}\n  vaste L {L}, wissels in log {wissels}, metingen {n}")
    basis = None
    for k, rij in groep.items():
        if not rij:
            print(f"  {STANDEN[k]}: geen metingen")
            continue
        cp = [r[0] for r in rij]; be = [r[1] for r in rij]
        met = [r for r in rij if r[2] > 0]; zon = [r for r in rij if r[2] == 0]
        ms = 1000 * sum(cp) / max(1, sum(be))
        ms_met = 1000 * sum(r[0] for r in met) / max(1, sum(r[1] for r in met))
        if k == 0:
            basis = ms
        tov = f", {100 * (ms / basis - 1):+.0f}% per beeld tegen alles aan" if basis and k else ""
        print(f"  {STANDEN[k]:11s}: n {len(rij)}, CPU {S.mean(cp):.3f} per 10 s, beelden {S.mean(be):.0f}, "
              f"{ms:.1f} ms per beeld{tov}; met held {ms_met:.1f} ms per beeld (n {len(met)}), zonder held n {len(zon)}")
