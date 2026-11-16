# Sanne 16 nov ±22:50 UTC: speeltestavond van een graver. 30 min spelen (graver verdient ±351, Olafs graaftoets 234 per 20 min),
# koopt put 1+2 en slijm 1+2 (342), houdt ±29 over. Dan 8 uur weg op 0,12 (115 helden), kans met 4 stappen (+7 procentpunt per stap,
# zelfde formule als voortgang.gd reken()). Vraag: staat er de volgende ochtend nog iets in de winkel (de laatste twee kosten 706)?
import random, statistics
def nacht(kans, bonus, z):
    r = random.Random(z); h = 115; g = sum(1 for _ in range(h) if r.random() < kans); return g*(7+bonus) + (h-g)
kans = 1 - (1-0.49)*(1-0.59)
print("graafbonus | kans | goud in de ochtend mediaan (laagste, hoogste) | deel zaden met lege winkel")
for b in (0, 3):
    n = [nacht(kans, b, z) + 29 for z in range(200)]
    print(f"{b} | {kans:.2f} | {statistics.median(n):.0f} ({min(n)}, {max(n)}) | {sum(1 for x in n if x >= 706)/200:.0%}")
