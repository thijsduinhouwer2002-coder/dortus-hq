# Telt kroniekregels in een hol.log tegen Iris' keurregel (keuring 21/22).
# Gebruik: python3 tel_regels.py <kroniek_regels.gd> <hol.log>
# Eis: minstens 1 Dame, minstens 2 hap-regels (hap_<soort>), val_bewoner hooguit 6 per regel, terugslag minstens 5.
import re, sys, collections

gd = open(sys.argv[1], encoding="utf-8").read()
log = open(sys.argv[2], encoding="utf-8", errors="replace").read().splitlines()

voorraad = {}
# robuuster: zoek elk "sleutel": [ ... ] blok, ook over meerdere regels
for m in re.finditer(r'"([a-z_]+)":\s*\[((?:[^\[\]"]|"(?:[^"\\]|\\.)*")*)\]', gd):
    voorraad[m.group(1)] = re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(2))


def naar_regex(t):
    delen = re.split(r"(\{[a-zA-Z]+\})", t)
    uit = ""
    for d in delen:
        if d.startswith("{") and d.endswith("}"):
            uit += r".+?"
        else:
            uit += re.escape(d)
    return re.compile(uit + r"(?:\s*[+-]\d+)?\s*$")


soorten = ["ridder", "dief", "magier", "bard", "slaapkop", "wraakzuchtig", "opschepper"]
groepen = {"val_bewoner": ["val_bewoner"],
           "hap_soort": ["hap_" + s for s in soorten],
           "terugslag": ["val_" + s for s in soorten] + ["vlucht_" + s for s in soorten]}

kroniek = [r for r in log if re.match(r"\s*HOL kroniek \d", r)]  # alleen getoonde regels, niet "zelfde held vervangen"
tel = collections.Counter()
per_regel = collections.Counter()
dame = 0
for r in kroniek:
    if "Dame " in r:
        dame += 1
    for groep, sleutels in groepen.items():
        for s in sleutels:
            for t in voorraad.get(s, []):
                if naar_regex(t).search(r):
                    tel[groep] += 1
                    per_regel[(s, t)] += 1
                    break
            else:
                continue
            break

print("regels in log:", len(kroniek))
print("Dame:", dame, "(eis >= 1)")
print("hap per soort:", tel["hap_soort"], "(eis >= 2)")
print("terugslag:", tel["terugslag"], "(eis >= 5)")
for t in voorraad.get("val_bewoner", []):
    print("val_bewoner", repr(t), per_regel[("val_bewoner", t)], "(eis <= 6)")
print("meest gebruikte regels:")
for (s, t), n in per_regel.most_common(8):
    print(" ", n, s, t)
tv = sum(n for (s, t), n in per_regel.items() if s.startswith("val_") and s != "val_bewoner")
tl = sum(n for (s, t), n in per_regel.items() if s.startswith("vlucht_"))
print("terugslag gesplitst: vangst", tv, "vlucht", tl)
