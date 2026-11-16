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
AARTS_NA_HELDEN = 0   # zelfde regel, geteld in nieuwe helden (helden_nr in de save van strook.gd)
AARTS_NA = 0          # Sanne: geen aartsvijand in het eerste uur; 3600 = regel aan (python3 sim.py aarts meet beide)
AARTS_KANS = 0.15      # een aartsvijand die aan de beurt is, komt maar 15% van de keren echt (zeldzaam = feest)
# Voorstel Bram (uit deze sim, zie UITKOMST.md); balans.md had faam x 0,9 per niveau zonder bodem.
FAAM_FACTOR = 0.97
FAAM_BODEM = 0.75
TERUG_KANS = 0.25      # kans dat de volgende held een terugkomer is (als die er zijn)
BLIJFT_KANS = 0.6      # kans dat een gevluchte held ooit terugkomt (anders gaat hij met pensioen en vertelt over je hol)
START_GOUD = 20        # Olaf 13 nov: nieuw spel begint met 20 goud (kern/kaartje.gd START_GOUD, demolijst 3)
UPG_BASIS = 45         # Sanne 10 nov 01:50 (balans.md): 45, 126, 353 (45 x 2,8^n); was 60
GRAAF_DREMPEL = 12     # Sanne 10 nov 01:50: graven 5 + 1,2 x gangen, plus 3 per gang boven de 12
# Ritme en begin zoals het spel sinds 16 nov (kern/ritme.gd, kern/strook.gd BEGIN, kern/binnenkomst.gd). Bram 16 nov:
# de sim rekende nog met een held per 25 tot 75 s en alleen "eerste held valt". Nu: eerste held op 4 s, de vijf vaste
# stappen van een nieuw spel (vallen in de put, opgegeten door Gloop, vluchten met wrok, die vluchter terug naar zijn
# vijand, Hoard-Toucher), gaten 5 tot 7 s, 18 tot 22 s, dan 35 tot 45 s in het begin en 40 tot 60 s daarna.
# RITME_SPEL = False geeft de oude sim (python3 sim.py ... met omgeving SIM_OUD=1).
import os
RITME_SPEL = os.environ.get("SIM_OUD", "") != "1"
BEGIN = ["vallen", "opgegeten", "vluchten", "terug", "doorlopen"]
LOOP_HAP_S = 17.0      # zoveel s loopt een held van de ingang tot Gloop (log echte spel 16 nov: binnen ±10 s, hap 26,3 tot 27,8)

def graaf_prijs(gangen):
    return 5 + 1.2 * gangen + 3 * max(0, gangen - GRAAF_DREMPEL)

# Heldensoorten (versie 1, godot/systemen/heldensoort.gd): zelfde getallen. Aan met: python3 sim.py soorten
SOORTEN = False
SOORT_DATA = {"ridder": ({"slijm": 0.7, "put": 1.4}, True), "dief": ({"slijm": 1.15, "put": 0.5}, False),
              "magier": ({"slijm": 1.25, "put": 0.3}, False), "bard": ({"slijm": 1.1, "put": 1.1}, False)}  # ridder en bard: Sanne 10 nov 03:05 (balans.md)
SOORT_GEWICHT = {"": 55, "ridder": 15, "dief": 15, "magier": 10, "bard": 5}
LIED_HELDEN = 2
TRICK_MAGIER = 1.0   # None = uit; 1.0 = Trick Lid zet de factor van de magier voor de put op 1,0 (meting 10 nov 03:30)

# Bram 16 nov: het spel zelf (kern/afloop.gd) geeft per val 6 + 3 per eerder bezoek, zonder faam en zonder gangfactor;
# graven is gratis en er zijn geen extra bewoners te koop, dus de winkel is alleen de 6 stappen van upgrades.gd.
# SPEL_ECONOMIE = True rekent zo (diepte, drempels en voortgang zetten het aan; SIM_ECONOMIE=oud geeft de oude sim).
SPEL_ECONOMIE = False
REEKS = False   # True: speel() bewaart na elke held de tellers in st["reeks"] (zie diepte() onderaan)
STRATEGIE = "goedkoopst"   # of "spaar": koopt alleen upgrades, nooit graven (Sannes "als je niet graaft", features.md feature 5)
NAMEN = ["Bram", "Odo", "Wil", "Gerda", "Pim", "Rik", "Mara", "Joost", "Fenna", "Ties", "Lotte", "Kees"]

def speel(uren, zaad):
    rng = random.Random(zaad)
    t = 0.0
    goud = float(START_GOUD)
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
    lied_extra = 0
    st["soort_tel"] = {}
    volgende = 4.0
    eind = uren * 3600
    begin_i = 0           # zoveel vaste stappen van BEGIN zijn gedaan (alleen met RITME_SPEL)
    begin_vlucht = None   # de held van stap "vluchten", die komt bij stap "terug" terug

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
        if STRATEGIE == "spaar" or SPEL_ECONOMIE:
            k = [x for x in k if x[0].startswith("upg_")]
        return k

    while t < eind:
        t = volgende
        stap = BEGIN[begin_i] if RITME_SPEL and begin_i < len(BEGIN) else ""
        if RITME_SPEL:
            if stap:
                begin_i += 1
                gat = (5, 7) if begin_i == 1 else (18, 22) if begin_i == 2 else (35, 45)
            else:
                gat = (40, 60)
            volgende = t + (rng.uniform(8, 20) if lied_extra > 0 else rng.uniform(*gat))
        else:
            volgende = t + (rng.uniform(8, 20) if lied_extra > 0 else rng.uniform(25, 75))
        lied_extra = max(0, lied_extra - 1)
        helden += 1
        faam = 0 if SPEL_ECONOMIE else helden // 60
        # wie komt er?
        if stap == "terug" and begin_vlucht is not None:
            if begin_vlucht in terug:
                terug.remove(begin_vlucht)
            h = begin_vlucht
        elif stap:
            h = None
        elif terug and rng.random() < TERUG_KANS:
            i = rng.randrange(len(terug))
            if terug[i]["gevlucht"] < 3 or (t >= AARTS_NA and nieuw_nr >= AARTS_NA_HELDEN and rng.random() < AARTS_KANS):
                h = terug.pop(i)
            else:
                h = None
        else:
            h = None
        if h is None:
            nieuw_nr += 1
            if t < 3600:
                st["nieuw_uur1"] = nieuw_nr
            h = {"naam": "%s%d" % (rng.choice(NAMEN), nieuw_nr), "gevlucht": 0, "wrok": "", "hoard": False,
                 "trek": rng.choice(["hebzuchtig", "schijterig"]), "bezoeken": 0, "soort": ""}
            if SOORTEN and nieuw_nr > 10:
                h["soort"] = rng.choices(list(SOORT_GEWICHT), weights=list(SOORT_GEWICHT.values()))[0]
                if rng.random() < 0.2:   # heldensoort.kies_trek: slaapkop, wraakzuchtig, opschepper (gedragen zich verder als hebzuchtig)
                    h["trek"] = rng.choice(["slaapkop", "wraakzuchtig", "opschepper"])
        sd = SOORT_DATA.get(h.get("soort", ""), ({}, False))
        if h["gevlucht"] >= 3:
            st["aartsvijand_bezoek"] += 1
            if st.get("eerste_aarts") is None:
                st["eerste_aarts"] = t
        st["soort_tel"][h.get("soort", "")] = st["soort_tel"].get(h.get("soort", ""), 0) + 1
        moet_vallen = helden == 1 and not RITME_SPEL
        # vaste stap: waar hij heen moet ("put", "slijm"), of vluchten na een klap van de put, of de schat aanraken
        dwing = {"vallen": "put", "opgegeten": "slijm", "vluchten": "vlucht", "doorlopen": "hoard",
                 "terug": h["wrok"] or "put"}.get(stap, "")
        # pad: verdediging in volgorde van de gang (slijm en put om en om, zoals je ze neerzet)
        vijand = h["wrok"] if h["wrok"] in ("slijm", "put") and aantal[h["wrok"]] > 0 else ""
        if vijand:
            st["wrok_naar_vijand"] += 1
        klappen = 0
        uit = None
        geraakt_door = ""
        if dwing in ("put", "slijm"):
            v = next(x for x in verd if x["soort"] == dwing)
            uit = "gevallen"
            if dwing == "slijm":
                st["hap_slijm"] += 1
                if v is verd[0]:
                    st["hap_tijden"].append(t)
                if st.get("eerste_hap") is None:
                    st["eerste_hap"] = t + LOOP_HAP_S
            if h["gevlucht"] > 0 and dwing == h["wrok"]:
                st["afgerekend"] += 1
                st.setdefault("eerste_wrok_af", t)
        elif dwing == "vlucht":
            uit = "gevlucht"
            geraakt_door = "put"
            begin_vlucht = h
        for i, v in enumerate(verd if not dwing else []):
            if v["soort"] == "slijm" and t < v["plat_tot"]:
                continue
            # soortfactor alleen op de basiskans, zoals held.gd (controleur 10 nov): upgrade en ROEKELOOS komen erbij
            fs = sd[0].get(v["soort"], 1.0)
            if TRICK_MAGIER is not None and h.get("soort", "") == "magier" and v["soort"] == "put" and upg["put"] >= 3:
                fs = TRICK_MAGIER   # Trick Lid: de put ziet eruit als vloer, de magier ziet hem niet (idee Sanne 10 nov 03:10)
            kans = (KANS[v["soort"]] * fs + UPGRADE * upg[v["soort"]]) * max(FAAM_BODEM, FAAM_FACTOR ** faam)
            is_vijand = v["soort"] == vijand
            if is_vijand:
                kans += ROEKELOOS * (2 if h["trek"] == "wraakzuchtig" else 1)
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
            if (h["trek"] == "schijterig" and not diep and not (sd[1] and klappen < 2) and rng.random() < SCHIJT_OM) or klappen >= 2:
                uit = "gevlucht"
                break
        if uit is None:
            uit = "gevlucht"
            h["hoard"] = True
            st["hoard"] += 1
        if uit == "gevallen" and st.get("eerste_hap") is None and geraakt_door == "" and not dwing and st["hap_slijm"] > 0:
            st["eerste_hap"] = t + LOOP_HAP_S
        if uit == "gevallen":
            st["gevallen"] += 1
            erbij = (6 if SPEL_ECONOMIE else 6 * (1 + 0.1 * faam) * (1 + gangen / 40)) + GOUD_PER_BEZOEK * h["bezoeken"]
            goud += erbij
            st["goud_totaal"] = st.get("goud_totaal", 0.0) + erbij
            if st["eerste_val"] is None:
                st["eerste_val"] = t
        else:
            st["gevlucht"] += 1
            h["gevlucht"] += 1
            if h.get("soort") == "bard":
                lied_extra += LIED_HELDEN   # de bard zingt over je hol: er komen helden bij
                st["liederen"] = st.get("liederen", 0) + 1
            h["bezoeken"] += 1
            if geraakt_door:
                h["wrok"] = geraakt_door
            if rng.random() < BLIJFT_KANS or h["gevlucht"] >= 3 or h is begin_vlucht:
                terug.append(h)
        if REEKS:
            # tellers na elke held, voor de voortgang over ±100 uur (diepte(), voortgang(), drempels())
            st.setdefault("reeks", []).append((t, helden, st["gevallen"], st.get("goud_totaal", 0.0),
                                               len(st["hap_tijden"]), st["hap_slijm"], faam, len(st["aankopen"])))
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
            st.setdefault("uitgaven", []).append((t, prijs))
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

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "soorten":
    # zelfde doelen met en zonder heldensoorten (8 zaden, 10 uur)
    for aan in (False, True):
        SOORTEN = aan
        rij = []
        for z in range(1, 9):
            s = speel(10, z)
            a = s["aankopen"]
            rij.append((100 * s["gevlucht"] / s["helden"], s["helden"] / 10, wachttijden(a, 3600) / 60,
                        s["klaar_alles"] / 3600 if s["klaar_alles"] else 99, s["aartsvijand_bezoek"] / 10, s.get("liederen", 0) / 10))
        k = lambda i: "%.1f tot %.1f" % (min(r[i] for r in rij), max(r[i] for r in rij))
        print("soorten %-5s | vlucht %% %s | helden/u %s | langste wacht uur 1 %s min | alles na %s u | aartsvijand/u %s | liederen/u %s" % (
            aan, k(0), k(1), k(2), k(3), k(4), k(5)))
    sys.exit()

# Sanne features.md (eerste tien minuten): geen aartsvijand in het eerste uur van een nieuw spel. Hoe vaak gebeurt dat nu?
def aarts(zaden=60, uren=6):
    tijden = []
    uur1 = []
    for z in range(zaden):
        s = speel(uren, 1000 + z)
        tijden.append(s.get("eerste_aarts"))
        uur1.append(s.get("nieuw_uur1", 0))
    uur1.sort()
    print("nieuwe helden in uur 1: min %d, mediaan %d, max %d |" % (uur1[0], uur1[len(uur1) // 2], uur1[-1]), end=" ")
    echt = sorted(x / 3600 for x in tijden if x is not None)
    in_uur1 = sum(1 for x in echt if x < 1)
    mediaan = echt[len(echt) // 2] if echt else None
    print("aarts | %d zaden, %d u | eerste aartsvijand in uur 1: %d (%.0f%%) | ooit binnen %d u: %d | vroegste %.2f u | mediaan %s u" % (
        zaden, uren, in_uur1, 100 * in_uur1 / zaden, uren, len(echt), echt[0] if echt else -1,
        "%.2f" % mediaan if mediaan is not None else "-"))

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "aarts":
    for sr in (False, True):
        SOORTEN = sr
        for na, nh in ((0, 0), (3600, 0), (0, 60)):
            AARTS_NA, AARTS_NA_HELDEN = na, nh
            print("soorten %s, aartsvijand pas na %d s / %d nieuwe helden:" % (sr, na, nh), end=" ")
            aarts()
    sys.exit(0)

# Bram 16 nov: de eerste minuten van een nieuw spel naast de echte spel-log (Olaf, eisen 16 nov 07:20 in taken.md):
# hap uiterlijk ±35 s, vluchter terug binnen 300 s, eerste koop niet later dan ±245 s, daarna 35 tot 45 s.
def begin(zaden=40):
    rij = []
    for z in range(1, zaden + 1):
        s = speel(1, z)
        a = s["aankopen"]
        tien = sum(1 for x in s["hap_tijden"] if x + LOOP_HAP_S <= 600)
        global STRATEGIE
        STRATEGIE = "spaar"   # eerste upgrade als je niet graaft (zoals ritme()); de rest met "goedkoopst"
        upg1 = speel(1, z).get("eerste_upg", 9999)
        STRATEGIE = "goedkoopst"
        rij.append((s.get("eerste_hap") or 9999, s.get("eerste_wrok_af") or 9999, upg1, tien, len(s["hap_tijden"])))
    k = lambda i: sorted(r[i] for r in rij)
    for naam, i, f in (("eerste hap (aankomst + %g s lopen)" % LOOP_HAP_S, 0, "%.0f s"), ("vluchter terug en afgerekend", 1, "%.0f s"),
                       ("eerste upgrade (spaar, niet graven)", 2, "%.0f s"), ("hoeden op Gloop in de eerste 10 min", 3, "%d"), ("hoeden op Gloop in uur 1", 4, "%d")):
        v = k(i)
        print(("%-40s min " + f + ", mediaan " + f + ", gemiddeld %.1f, max " + f) % (naam, v[0], v[len(v) // 2], sum(v) / len(v), v[-1]))

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "begin":
    begin()
    sys.exit()

# ---------------------------------------------------------------------------------------------------------------
# Bram 16 nov: voortgang over ±100 uur (opdracht hoofdchat 13:10 NL, besluit Thijs 13:01: diep spel met level ups).
# Sanne ontwerpt de niveaus in platformen/steam/voortgang.md; deze drie stukken rekenen ze na met de economie van nu.
#   python3 sim.py diepte [zaden]            wat een speler bij uur 1, 2, 5 ... 100 heeft verzameld (bronnen voor niveaus)
#   python3 sim.py drempels N uren p bron     drempels zodat niveau n valt op uren x ((n-1)/(N-1))^p (voorstel, geen besluit)
#   python3 sim.py voortgang bestand.json     wanneer valt elke ontgrendeling, langste gat, muur, laatste ontgrendeling
# Bronnen: helden (binnengekomen), gevallen (gevangen helden), goud (verdiend, opgeteld), hoeden_gloop (hoeden op de toren
# van Gloop), hoeden (alle slijmen), uren (vaste open tijd). Let op: na ±7 uur is alles van de winkel gekocht, daarna
# groeien de bronnen recht evenredig. Nieuwe inhoud uit voortgang.md (andere bewoners, lagen) verandert dat; zet die eerst
# in speel() voor je de getallen als vast neemt.
UUR_PUNTEN = [1, 2, 5, 10, 20, 40, 70, 100]
BRON_KOLOM = {"helden": 1, "gevallen": 2, "goud": 3, "hoeden_gloop": 4, "hoeden": 5}
MUUR_S = 2 * 3600       # features.md: nooit langer dan 2 uur open tijd zonder iets nieuws (zelfde plafond als de winkel)
_reeks_cache = {}

def reeksen(zaden, uren=100):
    global REEKS, SPEL_ECONOMIE, SOORTEN
    sleutel = (zaden, uren)
    if sleutel not in _reeks_cache:
        REEKS = True
        if os.environ.get("SIM_ECONOMIE", "") != "oud":
            SPEL_ECONOMIE, SOORTEN = True, True   # zoals het spel nu: heldensoorten aan (heldensoort.gd), goud 6 + 3 per bezoek
        _reeks_cache[sleutel] = [speel(uren, z) for z in range(1, zaden + 1)]
        REEKS = False
    return _reeks_cache[sleutel]

def waarde_op(st, bron, t):
    """stand van een bron op open tijd t (s)"""
    if bron == "uren":
        return t / 3600
    k = BRON_KOLOM[bron]
    r = st["reeks"]
    lo, hi = 0, len(r)
    while lo < hi:
        m = (lo + hi) // 2
        if r[m][0] <= t:
            lo = m + 1
        else:
            hi = m
    return r[lo - 1][k] if lo else 0

def tijd_van(st, bron, drempel):
    """open tijd (s) waarop een bron de drempel haalt, of None"""
    if bron == "uren":
        return drempel * 3600
    k = BRON_KOLOM[bron]
    for rij in st["reeks"]:
        if rij[k] >= drempel:
            return rij[0]
    return None

def mediaan(v):
    v = sorted(v)
    return v[len(v) // 2]

def diepte(zaden=8):
    alle = reeksen(zaden)
    print("diepte | %d zaden, economie %s, mediaan (min tot max) per open-uur" % (zaden, "van het spel nu" if SPEL_ECONOMIE else "oude sim (faam, gangen, graven)"))
    print("%5s | %-18s | %-18s | %-22s | %-18s | %-16s | %4s | %s" % ("uur", "helden", "gevallen", "goud verdiend", "hoeden Gloop", "hoeden alle", "faam", "aankopen"))
    for u in UUR_PUNTEN:
        t = u * 3600
        kol = []
        for bron in ("helden", "gevallen", "goud", "hoeden_gloop", "hoeden"):
            v = sorted(waarde_op(st, bron, t) for st in alle)
            kol.append("%d (%d-%d)" % (mediaan(v), v[0], v[-1]))
        faam = mediaan([next((r[6] for r in reversed(st["reeks"]) if r[0] <= t), 0) for st in alle])
        aank = mediaan([sum(1 for a in st["aankopen"] if a[0] <= t) for st in alle])
        print("%5d | %-18s | %-18s | %-22s | %-18s | %-16s | %4d | %d" % (u, kol[0], kol[1], kol[2], kol[3], kol[4], faam, aank))
    ka = sorted(st["klaar_alles"] / 3600 if st["klaar_alles"] else 999 for st in alle)
    print("winkel helemaal gekocht na: mediaan %.1f u (min %.1f, max %.1f); goud op de bank bij 100 u: mediaan %d" % (
        mediaan(ka), ka[0], ka[-1], mediaan([START_GOUD + waarde_op(st, "goud", 360000) - sum(p for _, p in st.get("uitgaven", [])) for st in alle])))
    # tempo na "alles gekocht": per uur tussen 20 en 100 uur
    print("tempo per uur tussen 20 en 100 u (mediaan):", ", ".join(
        "%s %.0f" % (b, mediaan([(waarde_op(st, b, 360000) - waarde_op(st, b, 72000)) / 80 for st in alle]))
        for b in ("helden", "gevallen", "goud", "hoeden_gloop", "hoeden")))

def mooi(x):
    """rond een drempel af op een getal dat een speler kan onthouden"""
    if x < 20:
        return max(1, int(round(x)))
    stap = 10 ** (len(str(int(x))) - 2)   # twee cijfers die tellen: 47, 480, 4800
    return int(round(x / stap) * stap)

def drempels(N=50, uren=100.0, p=2.0, bron="gevallen", zaden=8, toon=True):
    """Voorstel: drempel voor niveau n = mediane stand van de bron op uren x ((n-1)/(N-1))^p. Niveau 1 = start."""
    alle = reeksen(zaden, max(100, int(uren) + 1))
    uit = []
    for n in range(2, N + 1):
        t = uren * 3600 * ((n - 1) / (N - 1)) ** p
        uit.append((n, mooi(mediaan([waarde_op(st, bron, t) for st in alle])), t / 3600))
    # dubbele drempels opschuiven, zodat elk niveau iets kost
    for i in range(1, len(uit)):
        if uit[i][1] <= uit[i - 1][1]:
            uit[i] = (uit[i][0], uit[i - 1][1] + 1, uit[i][2])
    if toon:
        print("drempels | %d niveaus over %g u open tijd, vorm p=%g, bron %s, %d zaden" % (N, uren, p, bron, zaden))
        print("niveau: drempel (gemikt op uur)")
        print("  " + "  ".join("%d: %d (%.2f)" % x for x in uit))
    return [{"niveau": n, "drempel": d} for n, d, _ in uit]

def voortgang(pad, zaden=8):
    """Rekent een voortgang na. JSON: {"sporen": [{"naam": "hol-niveau", "bron": "gevallen",
    "niveaus": [{"niveau": 2, "drempel": 5, "wat": "..."}, ...]}, ...]}. Alle sporen samen tellen voor gaten en muren."""
    import json
    spec = json.load(open(pad))
    uren = max(100, int(spec.get("uren", 100)))
    alle = reeksen(zaden, uren)
    per_zaad = []
    for st in alle:
        ev = []
        for sp in spec["sporen"]:
            for nv in sp["niveaus"]:
                tt = tijd_van(st, sp["bron"], nv["drempel"])
                ev.append((tt, sp["naam"], nv.get("niveau"), nv.get("wat", "")))
        if spec.get("winkel", True):
            # de 6 upgrades van de winkel (upgrades.gd) zijn ook ontgrendelingen; "winkel": false laat ze weg
            ev += [(a[0], "winkel", i + 1, a[1]) for i, a in enumerate(st["aankopen"])]
        per_zaad.append(ev)
    eind = uren * 3600
    print("voortgang | %s | %d zaden, %d u open tijd, muur = gat langer dan %.0f u zonder ontgrendeling, winkel %s" % (
        pad, zaden, uren, MUUR_S / 3600, "telt mee" if spec.get("winkel", True) else "telt niet mee"))
    # per spoor: mediane tijd per niveau
    for sp in spec["sporen"]:
        regels = []
        for nv in sp["niveaus"]:
            ts = [tijd_van(st, sp["bron"], nv["drempel"]) for st in alle]
            ok = [x for x in ts if x is not None]
            if len(ok) * 2 > len(ts):
                regels.append("%s:%s" % (nv.get("niveau"), uur_tekst(mediaan([x if x is not None else 9e9 for x in ts]))))
            else:
                regels.append("%s:niet binnen %d u" % (nv.get("niveau"), uren))
        print("  %s (%s): %s" % (sp["naam"], sp["bron"], "  ".join(regels)))
    # samen: gaten per uurblok, muren, laatste ontgrendeling, aantal per blok
    blokken = [(0, 1), (1, 2), (2, 5), (5, 10), (10, 20), (20, 40), (40, 70), (70, 100)]
    print("  samen per blok (mediaan over zaden): ontgrendelingen | langste gat")
    rij = []
    for a, b in blokken:
        aant, gat = [], []
        for ev in per_zaad:
            ts = sorted(x[0] for x in ev if x[0] is not None and x[0] <= eind)
            aant.append(sum(1 for x in ts if a * 3600 < x <= b * 3600))
            # langste gat dat in dit blok eindigt (van de ontgrendeling ervoor, ook als die in een eerder blok viel);
            # in het laatste blok telt ook het gat van de laatste ontgrendeling tot het eind
            alle_ts = [0.0] + ts + ([eind] if b * 3600 >= eind else [])
            g = max([y - x for x, y in zip(alle_ts, alle_ts[1:]) if a * 3600 < y <= b * 3600] + [0.0])
            gat.append(g)
        rij.append("%d-%d u: %d | %s" % (a, b, mediaan(aant), uur_tekst(mediaan(gat))))
    print("    " + "\n    ".join(rij))
    muren, laatst = [], []
    for ev in per_zaad:
        ts = [0.0] + sorted(x[0] for x in ev if x[0] is not None and x[0] <= eind)
        laatst.append(ts[-1])
        muren.append(sum(1 for x, y in zip(ts, ts[1:]) if y - x > MUUR_S))
    print("  muren (gaten > %.0f u, tot de laatste ontgrendeling): mediaan %d, max %d" % (MUUR_S / 3600, mediaan(muren), max(muren)))
    print("  laatste ontgrendeling: mediaan %s (min %s, max %s)" % (uur_tekst(mediaan(laatst)), uur_tekst(min(laatst)), uur_tekst(max(laatst))))
    na24 = mediaan([sum(1 for x in ev if x[0] is not None and x[0] > 24 * 3600) for ev in per_zaad])
    print("  ontgrendelingen na 24 u open tijd (3 werkdagen van 8 u): mediaan %d" % na24)

def uur_tekst(s):
    return "%.0f min" % (s / 60) if s < 3600 else "%.1f u" % (s / 3600)

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "diepte":
    diepte(int(sys.argv[2]) if len(sys.argv) > 2 else 8)
    sys.exit()

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "drempels":
    a = sys.argv[2:]
    drempels(int(a[0]) if a else 50, float(a[1]) if len(a) > 1 else 100, float(a[2]) if len(a) > 2 else 2.0, a[3] if len(a) > 3 else "gevallen")
    sys.exit()

if __name__ == "__main__" and len(sys.argv) > 2 and sys.argv[1] == "voortgang":
    voortgang(sys.argv[2])
    sys.exit()

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
