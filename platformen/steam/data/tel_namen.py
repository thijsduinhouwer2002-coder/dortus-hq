# Telt namen in een hol.log tegen Iris' keurregel (keuring 22) en Sannes lat (features.md, namen zonder families).
# Gebruik: python3 tel_namen.py <hol.log>
# Eis: geen voornaam vaker dan 6 keer in 10 min, nooit X, X II, X III direct na elkaar, geen "dad's" bij een
# vrouwennaam, minstens 18 verschillende voornamen. Tijd = de laatste "HOL kroniek <t>" regel ervoor.
import re, sys, collections

VROUW = {"Gerda", "Mara", "Fenna", "Lotte", "Femke", "Ineke", "Anouk", "Merel", "Elke", "Maud"}
t = 0.0
binnen = []   # (t, volle naam)
dad_fout = []
for r in open(sys.argv[1], encoding="utf-8", errors="replace"):
    m = re.search(r"HOL kroniek ([\d.]+)", r)
    if m:
        t = float(m.group(1))
    m = re.search(r"HOL held binnen: (.+)$", r.strip())
    if m:
        binnen.append((t, m.group(1).strip()))
    m = re.search(r"(\w+)(?: I{1,3})? wants dad's", r)
    if m and m.group(1) in VROUW:
        dad_fout.append(r.strip())

basis = [(tt, n.split(" ")[0], n) for tt, n in binnen]
hoogst, waar = 0, ""
for i, (t0, b, _) in enumerate(basis):
    n = sum(1 for t1, b1, _ in basis[i:] if b1 == b and t1 < t0 + 600)
    if n > hoogst:
        hoogst, waar = n, "%s vanaf %.0f s" % (b, t0)
rij = []
for i in range(len(basis) - 2):
    a, b, c = basis[i][2], basis[i + 1][2], basis[i + 2][2]
    x = a.split(" ")[0]
    if b == x + " II" and c == x + " III" and a == x:
        rij.append("%s op %.0f s" % (x, basis[i][0]))
voornamen = {b for _, b, _ in basis}
print("helden binnen: %d, laatste tijd %.0f s" % (len(basis), t))
print("verschillende voornamen: %d (lat 18) %s" % (len(voornamen), "OK" if len(voornamen) >= 18 else "ROOD"))
print("hoogste keer dezelfde naam in 10 min: %d (%s) (eis hooguit 6) %s" % (hoogst, waar, "OK" if hoogst <= 6 else "ROOD"))
print("X, X II, X III op een rij: %d %s %s" % (len(rij), rij[:5], "OK" if not rij else "ROOD"))
print("dad bij een vrouwennaam: %d %s %s" % (len(dad_fout), dad_fout[:3], "OK" if not dad_fout else "ROOD"))
print("per voornaam:", dict(collections.Counter(b for _, b, _ in basis).most_common()))
