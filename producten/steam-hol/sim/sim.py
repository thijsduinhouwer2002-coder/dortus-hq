"""Balans-simulatie Het Hol (Bram). Zelfde regels als systemen/held.gd en de getallen van platformen/steam/balans.md.
Draaien: python3 sim.py [uren] [zaden]   (standaard 10 uur open tijd, 5 zaden)
Speler koopt steeds het goedkoopste wat kan, zodra het kan (zoals de proef van Sanne).
Meet de balansdoelen uit features.md: eerste val binnen een minuut, ongeveer 1 op 3 vlucht, geen muur
(langste wachttijd tot de volgende aankoop), aartsvijanden per uur, afgerekende wrokken.
"""
import random, sys

KANS = {"slijm": 0.45, "put": 0.35}   # balans.md had 0,30 en 0,22; zie UITKOMST.md
UPGRADE = 0.07
ROEKELOOS = 0.10
BRUTAAL = 0.8
PLAT_S = 60
SCHIJT_OM = 0.5
GOUD_PER_BEZOEK = 3   # Sanne 9 nov 19:55: +3 goud per eerder bezoek (een terugkomer is een beloning)
AARTS_KANS = 0.15      # een aartsvijand die aan de beurt is, komt maar 15% van de keren echt (zeldzaam = feest)
# Voorstel Bram (uit deze sim, zie UITKOMST.md); balans.md had faam x 0,9 per niveau zonder bodem.
FAAM_FACTOR = 0.97
FAAM_BODEM = 0.75
TERUG_KANS = 0.25      # kans dat de volgende held een terugkomer is (als die er zijn)
BLIJFT_KANS = 0.6      # kans dat een gevluchte held ooit terugkomt (anders gaat hij met pensioen en vertelt over je hol)
UPG_BASIS = 45         # Sanne 10 nov 01:50 (balans.md): 45, 126, 353 (45 x 2,8^n); was 60
GRAAF_DREMPEL = 12     # Sanne 10 nov 01:50: graven 5 + 1,2 x gangen, plus 3 per gang boven de 12

def graaf_prijs(gangen):
    return 5 + 1.2 * gangen + 3 * max(0, gangen - GRAAF_DREMPEL)

STRATEGIE = "goedkoopst"   # of "spaar": koopt alleen upgrades, nooit graven (Sannes "als je niet graaft", features.md feature 5)
NAMEN = ["Bram", "Odo", "Wil", "Gerda", "Pim", "Rik", "Mara", "Joost", "Fenna", "Ties", "Lotte", "Kees"]

def speel(uren, zaad):
    rng = random.Random(zaad)
    t = 0.0
    goud = 0.0
    gangen = 6
    verd = [{"soort": "slijm", "plat_tot": -1}, {"soort": "put", "plat_tot": -1}]
    upg = {"slijm": 0, "put": 0}
    aantal = {"slijm": 1, "put": 1}
    helden = 0
    faam = 0
    terug = []            # terugkomers
    st = {"gevallen": 0, "gevlucht": 0, "hoard": 0, "afgerekend": 0, "aartsvijand_bezoek": 0,
          "eerste_val": None, "aankopen": [], "wrok_naar_vijand": 0, "hap_slijm": 0, "hap_tijden": []}
    nieuw_nr = 0
    volgende = 4.0
    eind = uren * 3600

    def koop_lijst():
        k = []
        if gangen < 40:
            k.append(("graaf", graaf_prijs(gangen)))
        for s in ("slijm", "put"):
            n = aantal[s]
            drempel = {1: 8, 2: 16, 3: 24}.get(n, 99)
            if n < 4 and gangen >= drempel:
                k.append(("extra_" + s, 40 * 2.6 ** n))
            if upg[s] < 3:
                k.append(("upg_" + s, UPG_BASIS * 2.8 ** upg[s]))
        if STRATEGIE == "spaar":
            k = [x for x in k if x[0].startswith("upg_")]
        return k

    while t < eind:
        t = volgende
        volgende = t + rng.uniform(25, 75)
        helden += 1
        faam = helden // 60
        # wie komt er?
        if terug and rng.random() < TERUG_KANS:
            i = rng.randrange(len(terug))
            if terug[i]["gevlucht"] < 3 or rng.random() < AARTS_KANS:
                h = terug.pop(i)
            else:
                h = None
        else:
            h = None
        if h is None:
            nieuw_nr += 1
            h = {"naam": "%s%d" % (rng.choice(NAMEN), nieuw_nr), "gevlucht": 0, "wrok": "", "hoard": False,
                 "trek": rng.choice(["hebzuchtig", "schijterig"]), "bezoeken": 0}
        if h["gevlucht"] >= 3:
            st["aartsvijand_bezoek"] += 1
        moet_vallen = helden == 1
        # pad: verdediging in volgorde van de gang (slijm en put om en om, zoals je ze neerzet)
        vijand = h["wrok"] if h["wrok"] in ("slijm", "put") and aantal[h["wrok"]] > 0 else ""
        if vijand:
            st["wrok_naar_vijand"] += 1
        klappen = 0
        uit = None
        geraakt_door = ""
        for i, v in enumerate(verd):
            if v["soort"] == "slijm" and t < v["plat_tot"]:
                continue
            kans = (KANS[v["soort"]] + UPGRADE * upg[v["soort"]]) * max(FAAM_BODEM, FAAM_FACTOR ** faam)
            is_vijand = v["soort"] == vijand
            if is_vijand:
                kans += ROEKELOOS
                vijand = ""   # na het duel door naar de schat
            if h["hoard"]:
                kans *= BRUTAAL
            if rng.random() < kans or (moet_vallen and klappen == 0 and i == 0):
                uit = "gevallen"
                if v["soort"] == "slijm":
                    st["hap_slijm"] += 1      # hoedentoren: elke hap is een hoed (Sanne toets 3, punt 4)
                    if v is verd[0]:
                        st["hap_tijden"].append(t)   # toren van Gloop zelf (elke slijm zijn eigen toren)
                if h["gevlucht"] > 0 and is_vijand:
                    st["afgerekend"] += 1
                break
            klappen += 1
            geraakt_door = v["soort"]
            if v["soort"] == "slijm":
                # Bouncy Gloop (godot/systemen/upgrades.gd, stap 2): plat 2/3 van de tijd
                v["plat_tot"] = t + PLAT_S * (2 / 3 if upg["slijm"] >= 2 else 1)
            # Deep Pit (stap 2 van de put): een schijterige held keert na zijn eerste klap van de put niet om
            # (10 nov 01:30: stond op "stekelput", maar in de sim heet hij "put", dus Deep Pit telde nooit mee)
            diep = v["soort"] == "put" and upg["put"] >= 2 and klappen < 2
            if (h["trek"] == "schijterig" and not diep and rng.random() < SCHIJT_OM) or klappen >= 2:
                uit = "gevlucht"
                break
        if uit is None:
            uit = "gevlucht"
            h["hoard"] = True
            st["hoard"] += 1
        if uit == "gevallen":
            st["gevallen"] += 1
            goud += 6 * (1 + 0.1 * faam) * (1 + gangen / 40) + GOUD_PER_BEZOEK * h["bezoeken"]
            if st["eerste_val"] is None:
                st["eerste_val"] = t
        else:
            st["gevlucht"] += 1
            h["gevlucht"] += 1
            h["bezoeken"] += 1
            if geraakt_door:
                h["wrok"] = geraakt_door
            if rng.random() < BLIJFT_KANS or h["gevlucht"] >= 3:
                terug.append(h)
        # kopen: steeds het goedkoopste wat kan
        while True:
            k = koop_lijst()
            if not k:
                break
            wat, prijs = min(k, key=lambda x: x[1])
            if goud < prijs:
                break
            goud -= prijs
            st["aankopen"].append((t, wat))
            if wat.startswith("upg_") and "eerste_upg" not in st:
                st["eerste_upg"] = t
            if wat == "graaf":
                gangen += 1
            elif wat.startswith("extra_"):
                s = wat[6:]
                aantal[s] += 1
                verd.append({"soort": s, "plat_tot": -1})
            else:
                upg[wat[4:]] += 1
    st["helden"] = helden
    st["klaar_alles"] = None if koop_lijst() else st["aankopen"][-1][0]
    return st

def wachttijden(aankopen, tot):
    ts = [0.0] + [a[0] for a in aankopen if a[0] <= tot]
    return max(b - a for a, b in zip(ts, ts[1:])) if len(ts) > 1 else tot

def ritme(zaden=20):
    """Wanneer kan de speler zijn eerste upgrade (UPG_BASIS) kopen? Sanne gokte ±10 min open tijd als je niet graaft."""
    global STRATEGIE
    for strat in ("spaar", "goedkoopst"):
        STRATEGIE = strat
        ts = sorted(speel(2, z).get("eerste_upg", 7200) / 60 for z in range(1, zaden + 1))
        keuze = []
        for z in range(1, zaden + 1):
            a = speel(1, z)["aankopen"]
            # minuten in het eerste uur waarin er niets te kopen viel (van aankoop tot aankoop, langste gat)
            keuze.append(wachttijden(a, 3600) / 60)
        print("%-10s eerste upgrade na %.1f / %.1f / %.1f min (min/mediaan/max), langste gat zonder aankoop in uur 1: %.1f tot %.1f min" % (
            strat, ts[0], ts[len(ts) // 2], ts[-1], min(keuze), max(keuze)))
    STRATEGIE = "goedkoopst"

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "ritme":
    ritme()
    sys.exit()

if __name__ == "__main__":
    uren = float(sys.argv[1]) if len(sys.argv) > 1 else 10
    zaden = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    if len(sys.argv) > 3:
        GOUD_PER_BEZOEK = float(sys.argv[3])   # python3 sim.py 10 8 0 = zonder bonus per bezoek
    print("goud per val: 6 x faam x gangen + %g per eerder bezoek" % GOUD_PER_BEZOEK)
    print("zaad | 1e val s | 1e koop s | vlucht % | hoard % | aankopen 1u/3u/10u | langste wacht 1u/3u/10u (min) | alles na (u) | aartsvijand/u | afgerekend | hoeden/u alle slijmen | Gloop: hoeden/u, 4 op hoofd na (min) | Gloop 5/25/100/300/1000/3000 hoeden na (u)")
    for z in range(1, zaden + 1):
        s = speel(uren, z)
        a = s["aankopen"]
        n = lambda u: sum(1 for x in a if x[0] <= u * 3600)
        w = lambda u: wachttijden(a, u * 3600) / 60
        alles = "%.1f" % (s["klaar_alles"] / 3600) if s["klaar_alles"] else "nee"
        ht = s["hap_tijden"]
        maat = lambda m: "%.1f" % (ht[m - 1] / 3600) if len(ht) >= m else "-"
        print("%4d | %8.0f | %9.0f | %8.0f | %7.0f | %4d/%d/%d | %5.1f/%.1f/%.1f | %s | %.2f | %d | %.1f | %s | %s" % (
            z, s["eerste_val"], a[0][0] if a else -1, 100 * s["gevlucht"] / s["helden"], 100 * s["hoard"] / s["helden"],
            n(1), n(3), n(10), w(1), w(3), w(10), alles, s["aartsvijand_bezoek"] / uren, s["afgerekend"],
            s["hap_slijm"] / uren, "%.1f, %s" % (len(ht) / uren, "%.0f" % (ht[3] / 60) if len(ht) >= 4 else "-"),
            "/".join(maat(m) for m in (5, 25, 100, 300, 1000, 3000))))
