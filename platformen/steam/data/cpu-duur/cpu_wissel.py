"""CPU binnen één run: muisvlak aan tegen uit (startargument wissel=vlak, kern/proef.gd). Bram 16 nov 2026.

Gebruik: python3 cpu_wissel.py <map met cpu-per-10s.txt en hol.log> [...]
Het spel zet het vlak in oneven minuten (t 60-120, 180-240, ...) uit. Elke meting `HOL meting t=` beslaat de 10 s
ervoor; alleen metingen midden in een minuut (t%60 van 20 tot 50) tellen mee. De CPU-reeks van de workflow wordt op de metingen
gelegd met de verschuiving (-3 tot 3) waarbij CPU en beelden het best samengaan, zoals cpu_per_beeld.py.
"""
import re, sys, statistics as S


def cor(a, b):
    n = min(len(a), len(b))
    try:
        return S.correlation(a[:n], b[:n]) if n > 3 else 0
    except S.StatisticsError:   # een reeks zonder spreiding
        return 0


for d in sys.argv[1:]:
    cpu = [float(x) for x in open(d + '/cpu-per-10s.txt').read().split()]
    log = open(d + '/hol.log').read()
    m = [(int(a), int(b), int(c)) for a, b, c in re.findall(r'meting t=(\d+) beelden=(\d+) helden=(\d+)', log)]
    wissels = len(re.findall(r'HOL wissel [a-z]*', log))
    bl = [x[1] for x in m]
    L = max(range(-3, 4), key=lambda L: cor(cpu[max(0, L):], bl[max(0, -L):]))
    c = cpu[max(0, L):]
    mm = m[max(0, -L):]
    n = min(len(c), len(mm))
    groep = {'aan': [], 'uit': []}
    for (t, b, h), x in zip(mm[:n], c[:n]):
        # t is int(t): de meting beslaat ±(t-10, t+1]. Alleen het midden van elke minuut telt (t%60 tussen 20 en 50),
        # want de CPU-blokken van de workflow liggen tot 10 s anders dan de metingen (keurder 16 nov, 3a en 3b).
        if not (20 <= t % 60 <= 50):
            continue
        staat = 'uit' if (t // 60) % 2 == 1 else 'aan'
        groep[staat].append((x, b, h))
    print(f"{d}  verschuiving {L}, wissels in log {wissels}")
    for staat, rij in groep.items():
        if not rij:
            print(f"  {staat}: geen metingen")
            continue
        cp = [r[0] for r in rij]; be = [r[1] for r in rij]
        met = [r[0] for r in rij if r[2] > 0]; zon = [r[0] for r in rij if r[2] == 0]
        print(f"  vlak {staat}: n {len(rij)}, CPU {S.mean(cp):.3f} per 10 s, beelden {S.mean(be):.0f} per 10 s, "
              f"{1000 * sum(cp) / max(1, sum(be)):.1f} ms per beeld; met held {S.mean(met) if met else 0:.2f} (n {len(met)}), "
              f"zonder {S.mean(zon) if zon else 0:.2f} (n {len(zon)})")
