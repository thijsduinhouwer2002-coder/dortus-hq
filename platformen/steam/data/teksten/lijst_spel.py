"""Sanne 17 nov: alle kroniekregels per soort, in volgorde van hoe vaak een speler ze ziet, voor Thijs (teksten-thijs.md).
Draai: python3 -I lijst_spel.py <godot-map> <hol.log> > tabel.md
Telt per soort hoe vaak een regel van die soort in de kroniek van de duurtest kwam (sjabloon met vullers als joker)."""
import re, sys, pathlib, collections
god = pathlib.Path(sys.argv[1]); log = sys.argv[2]

def voorraad(pad):
    t = (god / pad).read_text(encoding="utf-8")
    blok = t[t.index("const VOORRAAD := {"):]
    blok = blok[:blok.index("\n}")]
    uit = {}
    for m in re.finditer(r'"([a-z_]+)":\s*\[(.*?)\]', blok, re.S):
        uit[m.group(1)] = re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(2))
    return uit
eigen = voorraad("kern/regels.gd"); bram = voorraad("systemen/kroniek_regels.gd")
soorten = dict(eigen)   # regels.gd gaat voor (zoals kies()); daarna Brams soorten die hier niet staan
for k, v in bram.items():
    soorten.setdefault(k, v)
gezien = [re.sub(r" \+\d+$", "", m.group(1)) for l in open(log) for m in [re.match(r"HOL kroniek [\d.]+ \(wacht [\d.]+\): (.*)$", l)] if m]
def patroon(s):
    return re.compile("^" + re.sub(r"\\\{[A-Za-z]+\\\}", ".+?", re.escape(s)) + "$")
tel = collections.Counter(); per_regel = collections.Counter()
for g in gezien:
    for soort, lijst in soorten.items():
        hit = [s for s in lijst if patroon(s).match(g)]
        if hit:
            tel[soort] += 1; per_regel[(soort, hit[0])] += 1; break
volg = sorted(soorten, key=lambda s: (-tel[s], s))
print("| soort | keer in 75 min | regels (CONCEPT), tussen haakjes hoe vaak gezien |")
print("|---|---|---|")
for s in volg:
    rg = " / ".join("`%s`%s" % (r, " (%d)" % per_regel[(s, r)] if per_regel[(s, r)] else "") for r in soorten[s])
    print("| %s | %d | %s |" % (s, tel[s], rg))
print("\n%d kroniekregels gezien, %d herkend, %d soorten, %d regels in de voorraad." % (len(gezien), sum(tel.values()), len(soorten), sum(len(v) for v in soorten.values())))
