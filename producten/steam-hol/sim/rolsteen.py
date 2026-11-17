"""Rolsteen en edelman in de sim (Bram 17 nov 2026, vraag Sanne 17 nov ±00:00 UTC, features.md "De rolsteen en de edelman").

sim.py blijft zoals hij is: dit script past de bron in het geheugen aan (zoals Sannes scripts in platformen/steam/data/).
Speeltestbuild: nieuw ritme (28 tot 38 s, 15% paar 6 tot 10 s, Gloop 30 s plat), drempels zoals hol_niveau.gd DREMPEL,
upgrades 45 / 126 / 353 (3 per verdediger), graven gratis, SPEL_ECONOMIE (6 goud per val + 3 per eerder bezoek).

Rolsteen (te koop vanaf hol 7 voor 1 uur goud van dat moment, ligt in de eerste gang, voor de put en Gloop):
- klaar: de held die de gang in loopt laat hem rollen; hij raakt die held met kans 0,35 x soort (dief 1,4, ridder 0,6,
  magier 1,0, bard 1,1, edelman 1,0), en ook de volgende held als die al in de gang loopt: dat is zo als het gat tot de
  volgende held x 10 spelpixels per s / 16 spelpixels per cel korter is dan de gang (6 cellen), of als de volgende een
  edelman is die 2 cellen achter hem loopt. Raak = gevangen, mis = een klap zoals bij de andere vallen.
- daarna niet klaar tot er een held naar buiten loopt (vluchter of held die de schat aantikte en vertrekt).
Edelman (gewicht 5 vanaf hol 10): wacht op de volgende held (tot 40 s), loopt achter hem, kans 0 voor de val die de
voorloper pakte; alleen x 1,2 op alle vallen; +EDEL_GOUD goud per val.

Draai: python3 -I producten/steam-hol/sim/rolsteen.py
"""
import os, sys, json, copy, statistics as S

HIER = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HIER, "sim.py")).read().split('if __name__ == "__main__"')[0]
DREMPEL = [0, 3, 5, 7, 12, 17, 25, 31, 39, 53, 69, 88]


def vervang(s, oud, nieuw):
    assert s.count(oud) == 1, oud[:60]
    return s.replace(oud, nieuw)


def bron(steen_basis, edel_goud, gang_cellen=6, steen_x=None, edel_aan=True, steen_eerst=True, mis_klap="alle"):
    sx = steen_x or {"dief": 1.4, "ridder": 0.6, "magier": 1.0, "bard": 1.1}
    s = src
    # toestand
    s = vervang(s, "    tegen_koop = []       # [(naam, prijs)] te koop, op volgorde van vrijkomen\n",
                "    tegen_koop = []       # [(naam, prijs)] te koop, op volgorde van vrijkomen\n"
                "    steen_klaar = True; steen_volg = False; edel_wacht = None; edel_beurt = False; edel_volg_t = None; voor_val = None\n")
    s = vervang(s, "    st[\"soort_tel\"] = {}\n",
                "    st[\"soort_tel\"] = {}\n"
                "    st['steen'] = {'worp': 0, 'paar_worp': 0, 'paar_twee': 0, 'twee': 0, 'edel': 0, 'edel_achter': 0, 'edel_val': 0}\n")
    # edelman: het gat na de voorloper hoort bij de volgende gewone held
    s = vervang(s, "        lied_extra = max(0, lied_extra - 1)\n        helden += 1\n",
                "        if edel_beurt:\n"
                "            volgende = edel_volg_t\n"
                "        lied_extra = max(0, lied_extra - 1)\n        helden += 1\n")
    s = vervang(s, "        if stap == \"terug\" and begin_vlucht is not None:",
                "        if edel_beurt:\n"
                "            h = edel_wacht\n"
                "        elif stap == \"terug\" and begin_vlucht is not None:")
    s = vervang(s, "                h[\"soort\"] = rng.choices(list(gw), weights=list(gw.values()))[0]\n",
                "                if %r and hol_hoogst >= 10:\n"
                "                    gw['edelman'] = 5\n"
                "                h[\"soort\"] = rng.choices(list(gw), weights=list(gw.values()))[0]\n" % edel_aan)
    s = vervang(s, "        sd = SOORT_DATA.get(h.get(\"soort\", \"\"), ({}, False))\n",
                "        is_edel_volg = edel_beurt\n"
                "        if edel_beurt:\n"
                "            edel_beurt = False; edel_wacht = None\n"
                "        elif h.get('soort') == 'edelman' and edel_wacht is None and not stap:\n"
                "            st['steen']['edel'] += 1\n"
                "            if volgende - t <= 40:\n"
                "                edel_wacht = h; helden -= 1\n"
                "                st['steen']['edel_achter'] += 1\n"
                "                continue\n"
                "        sd = SOORT_DATA.get(h.get(\"soort\", \"\"), ({}, False))\n"
                "        voor_val_nu = None\n")
    # rolsteen: voor de gewone vallen
    s = vervang(s, "        for i, v in enumerate(verd if not dwing and uit is None else []):\n",
                "        if 'rolsteen' in tegen and not dwing and uit is None and (steen_klaar or steen_volg):\n"
                "            if steen_klaar:\n"
                "                steen_klaar = False\n"
                "                st['steen']['worp'] += 1\n"
                "                volg_in_gang = edel_wacht is not None or (volgende - t) * 10.0 / 16.0 < %r\n"
                "                steen_volg = volg_in_gang\n"
                "                st['steen']['_paar'] = volg_in_gang\n"
                "                st['steen']['_raak'] = 0\n"
                "                if volg_in_gang:\n"
                "                    st['steen']['paar_worp'] += 1\n"
                "            else:\n"
                "                steen_volg = False\n"
                "            kans_s = %r * %r.get(hs_, 1.0) * (1.2 if hs_ == 'edelman' and not is_edel_volg else 1.0)\n"
                "            if rng.random() < kans_s:\n"
                "                uit = 'gevallen'; voor_val_nu = 'steen'\n"
                "                st['steen']['_raak'] += 1\n"
                "                if st['steen']['_raak'] == 2:\n"
                "                    st['steen']['twee'] += 1\n"
                "                    st['steen']['paar_twee'] += 1\n"
                "            elif %r == 'alle' or (%r == 'ridder' and hs_ == 'ridder'):\n"
                "                klappen += 1; geraakt_door = 'steen'\n"
                "                if klappen >= 2 or (h['trek'] == 'schijterig' and not sd[1] and rng.random() < SCHIJT_OM):\n"
                "                    uit = 'gevlucht'\n"
                "        for i, v in enumerate(verd if not dwing and uit is None else []):\n" % (gang_cellen, steen_basis, sx, mis_klap, mis_klap))
    s = vervang(s, "            kans = (KANS[v[\"soort\"]] * fs + UPGRADE * upg[v[\"soort\"]] + eff[\"kans\"].get(v[\"soort\"], 0.0)) * max(FAAM_BODEM, FAAM_FACTOR ** faam)\n",
                "            kans = (KANS[v[\"soort\"]] * fs + UPGRADE * upg[v[\"soort\"]] + eff[\"kans\"].get(v[\"soort\"], 0.0)) * max(FAAM_BODEM, FAAM_FACTOR ** faam)\n"
                "            if hs_ == 'edelman':\n"
                "                kans = 0.0 if (is_edel_volg and voor_val == i) else kans * (1.0 if is_edel_volg else 1.2)\n")
    s = vervang(s, "            if rng.random() < kans or (moet_vallen and klappen == 0 and i == 0):\n                uit = \"gevallen\"\n",
                "            if rng.random() < kans or (moet_vallen and klappen == 0 and i == 0):\n                uit = \"gevallen\"; voor_val_nu = i\n")
    # goud edelman
    s = vervang(s, "            if gbonus and SPEL_ECONOMIE:\n",
                "            if hs_ == 'edelman':\n"
                "                erbij += %r; st['steen']['edel_val'] += 1\n"
                "            if gbonus and SPEL_ECONOMIE:\n" % edel_goud)
    # naar buiten: steen rolt terug
    s = vervang(s, "            st[\"gevlucht\"] += 1\n",
                "            st[\"gevlucht\"] += 1\n"
                "            if not steen_volg:\n"
                "                steen_klaar = True\n")
    # na de voorloper: de edelman meteen erachter, daarna weer het gewone gat
    s = vervang(s, "        # kopen: steeds het goedkoopste wat kan\n",
                "        if edel_wacht is not None and not is_edel_volg:\n"
                "            edel_beurt = True; edel_volg_t = volgende; volgende = t + 0.5; voor_val = voor_val_nu\n"
                "        # kopen: steeds het goedkoopste wat kan\n")
    if steen_eerst:   # een speler koopt de nieuwe val zodra hij het goud heeft, voor de goedkopere upgrades
        s = vervang(s, "            wat, prijs = min(k, key=lambda x: x[1])\n",
                    "            wat, prijs = min(k, key=lambda x: (not x[0].startswith('tegen_'), x[1]))\n")
    ns = {"__file__": os.path.join(HIER, "sim.py")}
    exec(s, ns)
    ns["SPEL_ECONOMIE"] = ns["SOORTEN"] = ns["REEKS"] = True
    ns["PLAT_S"] = 30
    return ns


def spec(steen=True, graaf=False):
    sp = copy.deepcopy(json.load(open(os.path.join(HIER, "voortgang-v3-weg-bram.json"))))
    for n in sp["sporen"][0]["niveaus"]:
        if 2 <= n["niveau"] <= 12:
            n["drempel"] = DREMPEL[n["niveau"] - 1]
    sp["graven"] = False
    sp["upg_prijs"] = [45, 126, 353, 99999, 99999, 99999]
    sp.pop("weg", None)
    sp["laag_helden"] = {"helden": {}, "tegen": {"rolsteen": {"hol": 7, "prijs_u": 1.0}} if steen else {}}
    return sp


def meet(ns, steen=True, zaden=60, uren=3.0):
    r = {"vlucht": [], "vlucht_na": [], "worp": 0, "paar_worp": 0, "paar_twee": 0, "twee": [], "steen_t": [], "leeg": [],
         "edel": 0, "edel_achter": 0, "edel_val": 0, "h12": [], "h10": []}
    for z in range(1, zaden + 1):
        st = ns["speel"](uren, z, spec(steen))
        rk = st["reeks"]
        a = [x for x in st["aankopen"]]
        ks = [x[0] for x in a if x[1] == "tegen_rolsteen"]
        t_steen = ks[0] if ks else None
        r["steen_t"].append(t_steen / 60 if t_steen else 999)
        upg = [x[0] for x in a if x[1].startswith("upg_")]
        alles = upg[5] if len(upg) >= 6 else None
        if steen:
            alles = max(alles, t_steen) if (alles and t_steen) else None
        r["leeg"].append(alles / 60 if alles else 999)
        # vluchten: deel van de helden die naar buiten liepen, vanaf de koop van de steen (of 30 min zonder steen) tot het eind
        van = t_steen if t_steen else 3600
        def deel(van):
            na = [x for x in rk if x[0] >= van]
            if len(na) < 2:
                return None
            v0, g0 = na[0][1] - na[0][2], na[0][2]
            v1, g1 = na[-1][1] - na[-1][2], na[-1][2]
            return (v1 - v0) / max(1, (v1 - v0) + (g1 - g0))
        r["vlucht_na"].append(deel(van))
        r["vlucht"].append(deel(0))
        ss = st["steen"]
        for k in ("worp", "paar_worp", "paar_twee", "edel", "edel_achter", "edel_val"):
            r[k] += ss[k]
        r["twee"].append(ss["twee"])
        hol = {x[2]: x[0] / 60 for x in st.get("ontgrendeld", []) if x[1] == "hol-niveau"}
        r["h12"].append(hol.get(12, 999)); r["h10"].append(hol.get(10, 999))
    return r


def regel(naam, r):
    vn = [x for x in r["vlucht_na"] if x is not None]
    return ("%-34s vluchten na koop %4.1f%% (alles %4.1f%%) | worpen %4d, met paar %3d, paar allebei %3d (%4.0f%%) | "
            "steen gekocht %5.1f min | winkel leeg %5.1f min (vroegst %5.1f, laatst %5.1f) | hol 10 %5.1f, 12 %5.1f | "
            "edelman %d (achter %d), gevangen %d" % (
                naam, 100 * S.mean(vn), 100 * S.mean([x for x in r["vlucht"] if x is not None]), r["worp"], r["paar_worp"], r["paar_twee"],
                100 * r["paar_twee"] / max(1, r["paar_worp"]), S.median(r["steen_t"]), S.median(r["leeg"]), min(r["leeg"]),
                max(r["leeg"]), S.median(r["h10"]), S.median(r["h12"]), r["edel"], r["edel_achter"], r["edel_val"]))


if __name__ == "__main__":
    Z = int(os.environ.get("ZADEN", "60"))
    print("Rolsteen en edelman, speeltestbuild, %d zaden, 3 uur open spel, niet graven, steen in de eerste gang" % Z)
    print("vluchten = gevluchte / (gevluchte + gevangen) helden; 'na koop' vanaf de koop van de steen (zonder steen vanaf 60 min)")
    vars_ = [("zonder steen, zonder edelman", dict(steen_basis=0.35, edel_goud=2, edel_aan=False), False),
             ("zonder steen, edelman +2", dict(steen_basis=0.35, edel_goud=2), False),
             ("steen 0,35 + edelman +2 (Sanne)", dict(steen_basis=0.35, edel_goud=2), True),
             ("steen 0,35, edelman +1", dict(steen_basis=0.35, edel_goud=1), True),
             ("steen 0,35, edelman +0", dict(steen_basis=0.35, edel_goud=0), True),
             ("steen 0,35, koopt goedkoopst eerst", dict(steen_basis=0.35, edel_goud=2, steen_eerst=False), True),
             ("steen 0,35, gang 4 cellen", dict(steen_basis=0.35, edel_goud=2, gang_cellen=4), True),
             ("steen 0,35, mis = klap alleen ridder", dict(steen_basis=0.35, edel_goud=2, mis_klap="ridder"), True),
             ("steen 0,50, mis = klap alleen ridder", dict(steen_basis=0.50, edel_goud=2, mis_klap="ridder"), True),
             ("steen 0,50, mis = nooit een klap", dict(steen_basis=0.50, edel_goud=2, mis_klap="geen"), True),
             ("steen 0,45, mis = klap alleen ridder", dict(steen_basis=0.45, edel_goud=2, mis_klap="ridder"), True),
             ("steen 0,50", dict(steen_basis=0.50, edel_goud=2), True),
             ("steen 0,60", dict(steen_basis=0.60, edel_goud=2), True)]
    for naam, kw, steen in vars_:
        print(regel(naam, meet(bron(**kw), steen, Z)))
