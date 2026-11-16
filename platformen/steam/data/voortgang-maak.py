"""Sanne 16 nov: maakt voortgang.json uit het ontwerp in platformen/steam/voortgang.md, voor Brams sim.
Gebruik: python3 voortgang-maak.py [schaal]  -> schrijft voortgang.json naast dit script.
Drempels: doeluur per niveau, omgezet naar gevangen helden met de reeks van 'sim.py diepte' (economie van nu, GEZIEN 16 nov).
Schaal > 1 schuift alles later (om de versnelling door effecten te compenseren)."""
import json, sys, os
SCHAAL = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
# uur -> gevangen helden (mediaan, sim.py diepte, 8 zaden)
REEKS = [(0, 0), (1, 49), (2, 108), (5, 291), (10, 590), (20, 1193), (40, 2390), (70, 4206), (100, 6030), (130, 7850)]
def gevangen(u):
    for (a, x), (b, y) in zip(REEKS, REEKS[1:]):
        if u <= b:
            return x + (y - x) * (u - a) / (b - a)
    return REEKS[-1][1]
# hol-niveau: (niveau, doeluur, wat, effect)
H = [
 (2, 3/60, "Heldenboek open (grijze vakjes)", None),
 (3, 7/60, "Ridder komt", None),
 (4, 12/60, "Vleermuis komt wonen", None),
 (5, 18/60, "Dief komt", None),
 (6, 25/60, "Tweede slijm of put te koop", {"bewoner": "put"}),
 (7, 33/60, "Rolsteen (nieuwe val)", {"kans": {"ridder": 0.03}}),
 (8, 43/60, "Magier komt", None),
 (9, 55/60, "Vaandel met de naam van je hol", {"gat": 0.97}),
 (10, 70/60, "Edelman komt (nieuwe held)", {"goud": 1}),
 (11, 88/60, "Bard komt", {"gat": 0.97}),
 (12, 110/60, "Hoedenwand in de schatkamer", None),
 (13, 2.6, "Upgrades stap 4", {"kans": {"gewoon": 0.02}}),
 (14, 3.4, "Skelet (bewoner)", {"bewoner": "slijm"}),
 (15, 4.3, "Trek: slaapkop", None),
 (16, 5.3, "Slaapkamer", None),
 (17, 6.4, "Lijmplaat (val)", {"kans": {"dief": 0.03}}),
 (18, 7.6, "Hoedenpakket 2", None),
 (19, 9.0, "Trek: opschepper", None),
 (20, 10.5, "Trap naar Laag 2: de Kristalader", {"goud_x": 1.15}),
 (21, 12.0, "Mijnwerker", None),
 (22, 13.6, "Mimic (bewoner)", {"bewoner": "slijm"}),
 (23, 15.3, "Valluik", None),
 (24, 17.1, "Keuken", None),
 (25, 19.0, "Upgrades stap 5", {"kans": {"gewoon": 0.02}}),
 (26, 21.0, "Kinderen van aartsvijanden", None),
 (27, 23.1, "Hoedenpakket 3 (kristal)", None),
 (28, 25.3, "Trek: verdwaald", None),
 (29, 27.6, "Trofeeenzaal", None),
 (30, 30.0, "Trap naar Laag 3: de Verzonken Crypte", {"goud_x": 1.15}),
 (31, 32.5, "Archeoloog", None),
 (32, 35.0, "Trol (bewoner)", {"bewoner": "put"}),
 (33, 37.6, "Nep-schat (val)", None),
 (34, 40.3, "Upgrades stap 6", {"kans": {"gewoon": 0.02}}),
 (35, 43.0, "Hoedenpakket 4 (crypte)", None),
 (36, 45.8, "Heks", None),
 (37, 48.6, "Trek: verzamelaar", None),
 (38, 51.5, "Kaarsenkamer (crypte)", None),
 (39, 54.5, "Skelet in harnas", None),
 (40, 57.5, "Trap naar Laag 4: het Gloophart", {"goud_x": 1.15}),
 (41, 60.7, "Hoedenjager", None),
 (42, 64.0, "Moeder Gloop (bewoner)", {"bewoner": "slijm"}),
 (43, 67.4, "Gloopbron (val)", None),
 (44, 70.9, "Hoedenpakket 5 (legendarisch)", None),
 (45, 74.5, "Mimic van goud", None),
 (46, 78.2, "Vleermuisfamilie", None),
 (47, 82.0, "Trol met leesbril", None),
 (48, 86.0, "Zeldzame held: de Gekroonde", None),
 (49, 90.2, "Hoedentroon voor Gloop", None),
 (50, 95.0, "Hol van de Hoedenkoning", None),
]
# Gloop: niveaus op hoeden op zijn toren (bron hoeden_gloop)
G = [(2, 5, "Wiebeltoren"), (3, 25, "Boer: spuugt soms een hoed op de berg"), (4, 60, "Kleverig: stuitert helden terug"),
     (5, 100, "Grote Gloop, toren van 5"), (6, 200, "Hoedendans als het stil is"), (7, 300, "Gloopje splitst af"),
     (8, 600, "Hoedenworp naar vluchters"), (9, 1000, "Gloop the Hatted, kroon van de berg"),
     (10, 3000, "Gloop de Hoedenkoning, gouden slijm")]
GEFF = {4: {"kans": {"gewoon": 0.03}}, 7: {"bewoner": "slijm"}, 8: {"kans": {"gewoon": 0.02}}}
# Laagsterren: drie doelen met hint per laag (vangen met een bepaalde val of bewoner). De sim kent geen gerichte doelen;
# GOK: ze vallen ongeveer midden tussen de hol-niveaus van hun laag, daarom als drempel op gevangen helden.
S = [(1, 6.0), (2, 8.2), (3, 9.8), (4, 16.2), (5, 22.0), (6, 28.8), (7, 39.0), (8, 47.2), (9, 56.0),
     (10, 69.2), (11, 80.1), (12, 92.6)]
# Bewoners naast Gloop: elk 3 niveaus met een nieuwe streek (op hun eigen teller in het spel; de sim kent die tellers niet,
# GOK: als drempel op gevangen helden, verdeeld over de tijd dat die bewoner er is).
B = [(1, 8.0, "Skelet 2: rammelt helden bang"), (2, 16.8, "Mimic 2: likt zijn lippen"), (3, 18.6, "Skelet 3: gooit zijn hoofd"),
     (4, 26.6, "Mimic 3: valse munt"), (5, 37.0, "Trol 2: bromt in zijn slaap"), (6, 42.0, "Skelet 4: draagt een hoed van de berg"),
     (7, 47.3, "Trol 3: gooit een rots"), (8, 50.0, "Mimic 4: twee rijen tanden"), (9, 62.2, "Trol 4: schrijft wrokken op"),
     (10, 65.7, "Moeder Gloop 2: zingt slijmliedjes"), (11, 79.6, "Moeder Gloop 3: breit hoeden"), (12, 92.8, "Moeder Gloop 4: adopteert gevluchte helden")]
spec = {"_uitleg": "Sanne 16 nov, voortgang.md versie 1. Gemaakt met platformen/steam/data/voortgang-maak.py (schaal %.2f)." % SCHAAL,
        "uren": 100, "sporen": [
  {"naam": "hol-niveau", "bron": "gevallen", "niveaus": [
     dict({"niveau": n, "drempel": max(1, round(gevangen(u * SCHAAL))), "wat": w}, **({"effect": e} if e else {})) for n, u, w, e in H]},
  {"naam": "Gloop", "bron": "hoeden_gloop", "niveaus": [
     dict({"niveau": n, "drempel": d, "wat": w}, **({"effect": GEFF[n]} if n in GEFF else {})) for n, d, w in G]},
  {"naam": "laagsterren", "bron": "gevallen", "niveaus": [
     {"niveau": n, "drempel": round(gevangen(u * SCHAAL)), "wat": "ster %d" % n} for n, u in S]},
  {"naam": "bewoners", "bron": "gevallen", "niveaus": [
     {"niveau": n, "drempel": round(gevangen(u * SCHAAL)), "wat": w} for n, u, w in B]}]}
uit = os.path.join(os.path.dirname(os.path.abspath(__file__)), "voortgang.json")
json.dump(spec, open(uit, "w"), indent=1, ensure_ascii=False)
print("geschreven:", uit)
