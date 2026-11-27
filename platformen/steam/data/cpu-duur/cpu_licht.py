"""CPU binnen één run in korte blokken: lichte rand om de held (#256) aan tegen uit. Olaf 27 nov 2026.

Gebruik: python3 cpu_licht.py <blok in s> <map> [...]
De map heeft cpu.txt (per seconde "<unix> <utime+stime in ticks>" van het Godot-proces, meet_tekens.sh).
Startargument wissel=licht licht_blok=<B> zet het licht aan als int(unix/B) even is, uit als oneven; wissel=nep schrijft
hetzelfde maar laat het aan (placebo). Met korte blokken (3 s) vallen de wisselingen in het spel (helden, hol opnieuw
tekenen) over aan en uit gelijk; alleen meetstukjes die helemaal in één blok vallen tellen, de eerste 30 s niet.
Uitkomst: per buurpaar (elk uit-blok tegen het gemiddelde van de aan-blokken ervoor en erna), gemiddeld en fout.
"""
import sys, statistics as S
B = float(sys.argv[1])
for d in sys.argv[2:]:
    r = [tuple(map(float, x.split())) for x in open(d + '/cpu.txt') if len(x.split()) == 2]
    blok = {}
    for (t0, c0), (t1, c1) in zip(r, r[1:]):
        if t0 - r[0][0] < 30 or t1 <= t0 or int(t0 // B) != int(t1 // B):
            continue
        blok.setdefault(int(t0 // B), [0.0, 0.0])
        blok[int(t0 // B)][0] += c1 - c0
        blok[int(t0 // B)][1] += t1 - t0
    gem = {b: v[0] / v[1] for b, v in blok.items() if v[1] > 0.5}
    rel = [((gem[b - 1] + gem[b + 1]) / 2 / gem[b] - 1) * 100 for b in gem if b % 2 == 1 and b - 1 in gem and b + 1 in gem]
    aan = [v for b, v in gem.items() if b % 2 == 0]
    uit = [v for b, v in gem.items() if b % 2 == 1]
    print(f"{d.rstrip('/').split('/')[-1]}: blokken aan {len(aan)}, uit {len(uit)}; aan {S.mean(aan):.2f} uit {S.mean(uit):.2f} ticks/s, "
          f"verschil {(S.mean(aan) / S.mean(uit) - 1) * 100:+.2f} procent")
    print(f"  buurparen {len(rel)}: gemiddeld {S.mean(rel):+.2f} procent, fout van het gemiddelde {S.stdev(rel) / len(rel) ** 0.5:.2f}")
