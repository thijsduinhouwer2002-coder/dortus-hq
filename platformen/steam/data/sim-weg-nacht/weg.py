# Sanne 16 nov ±22:00 UTC: wat geeft 8 uur weg na het nieuwe ritme (HELD_ELKE_S 30)?
# Zelfde rekenwijze als producten/steam-hol/godot/systemen/voortgang.gd reken(): helden = weg*snelheid/30,
# kans_val = 1 - 0,65^vallen * 0,55^bewoners (begin: 1 put, 1 Gloop), per val 7 + graafbonus, vlucht 1 munt.
# Faam = gevallen. Drempels hol 2..12: 3/5/7/12/17/25/31/39/53/69/88. Winkel speeltestbuild 1048.
import random, statistics
DREMPELS = [3,5,7,12,17,25,31,39,53,69,88]
def hol(faam): return 1 + sum(1 for d in DREMPELS if faam >= d)
def nacht(snelheid, bonus, kans, zaad, uren=8):
    r = random.Random(zaad); helden = int(uren*3600*snelheid/30)
    gev = sum(1 for _ in range(helden) if r.random() < kans)
    return helden, gev, gev*(7+bonus) + (helden-gev)
start = 1 - 0.65*0.55
print("snelheid | bonus | kans | helden | gevallen | goud mediaan (max van 200) | hol vanaf 0 zonder plafond")
for s in [0.25, 0.17, 0.15, 0.12, 0.10]:
    for b, k in [(0, start), (3, start), (3, 0.85)]:
        uit = [nacht(s, b, k, z) for z in range(200)]
        g = [u[2] for u in uit]; f = [u[1] for u in uit]
        print(f"{s:.2f} | {b} | {k:.2f} | {uit[0][0]} | {statistics.median(f):.0f} | {statistics.median(g):.0f} ({max(g)}) | {hol(statistics.median(f))}")
