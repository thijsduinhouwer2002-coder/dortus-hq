#!/usr/bin/env python3
"""Rapport van de koersverschil-scanner.

Gebruik:  python3 rapport.py <map met data> [--met-proef]   (bijv. een checkout van de tak ai-handel-data, map scanner/)
Leest alle */*/kansen.jsonl en stand.jsonl daaronder en schrijft het rapport als Markdown naar stdout.
Proefruns (map eindigt op -proef) lopen gelijk met de vaste run en tellen dus niet mee, tenzij --met-proef.

Een ECHTE kans (alle vijf moeten waar zijn):
  1. na takerkosten aan beide kanten en de opnamekosten van de munt blijft er winst over;
  2. opnemen op de koopbeurs en storten op de verkoopbeurs staan open (bekend, niet "onbekend");
  3. er ligt minstens MIN_RUIMTE euro winstgevend op het boek;
  4. hij bleef minstens MIN_DUUR seconden staan;
  5. het is niet zichtbaar een andere munt met dezelfde naam (contractadressen verschillen niet).
Elk cijfer in het rapport is GEZIEN (uit onze eigen metingen) of GOK (een aanname, met reden).
"""
import collections
import datetime as dt
import glob
import json
import os
import statistics
import sys

MIN_RUIMTE = 100
MIN_DUUR = 120
DAGEN_PROJECTIE = 90
INLEGGEN = (2000, 5000)


def echt(r):
    return (r.get("winst_ruimte_med") or 0) > 0 and r.get("opname_koop") is True \
        and r.get("storting_verkoop") is True and (r.get("ruimte_eur_med") or 0) >= MIN_RUIMTE \
        and (r.get("duur_s") or 0) >= MIN_DUUR and r.get("contract") != "anders"


def lees(map_, met_proef=False):
    kansen, stand = [], []
    telt = lambda p: met_proef or not os.path.dirname(p).endswith("-proef")
    for p in filter(telt, sorted(glob.glob(os.path.join(map_, "**", "kansen.jsonl"), recursive=True))):
        with open(p) as fh:
            kansen += [json.loads(x) for x in fh if x.strip()]
    for p in filter(telt, sorted(glob.glob(os.path.join(map_, "**", "stand.jsonl"), recursive=True))):
        with open(p) as fh:
            rij = [json.loads(x) for x in fh if x.strip()]
        if rij:
            stand.append(rij)
    return kansen, stand


def gemeten_uren(stand):
    """Uren dat de scanner liep: per run van de eerste tot de laatste standregel plus 5 minuten (één regel per
    ±5 minuten). Runs overlappen niet (de workflow laat er één tegelijk draaien), proefruns wel soms."""
    uren = 0.0
    for rij in stand:
        a = dt.datetime.strptime(rij[0]["t"], "%Y-%m-%dT%H:%M:%SZ")
        b = dt.datetime.strptime(rij[-1]["t"], "%Y-%m-%dT%H:%M:%SZ")
        uren += (b - a).total_seconds() / 3600 + 5 / 60
    return uren


def gebeurtenissen(echte, plafond=500):
    """Kansen van dezelfde munt en quote die in de tijd overlappen, zijn één gebeurtenis: je kunt de munt maar één
    keer goedkoop kopen en duur verkopen, ook al zien we het op vijf beursparen tegelijk. Per gebeurtenis telt de
    beste kans (hoogste winst bij het plafond)."""
    groepen = []
    for r in sorted(echte, key=lambda r: (r["munt"], r["quote"], r["begin"])):
        g = groepen[-1] if groepen else None
        if g and g["munt"] == r["munt"] and g["quote"] == r["quote"] and r["begin"] <= g["eind"]:
            g["leden"].append(r)
            g["eind"] = max(g["eind"], r["eind"])
        else:
            groepen.append({"munt": r["munt"], "quote": r["quote"], "begin": r["begin"], "eind": r["eind"],
                            "leden": [r]})
    return [max(g["leden"], key=lambda r: winst_bij(r, plafond) or 0) for g in groepen]


def eur(x):
    return "geen" if x is None else f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def med(w):
    w = [x for x in w if x is not None]
    return statistics.median(w) if w else None


def winst_bij(r, plafond):
    """Winst van één kans als je hooguit `plafond` euro per kans inzet (GOK: met het mediane boek)."""
    for p in (100, 500, 1000, 2500):
        if plafond <= p:
            return r.get(f"winst{p}_med")
    return r.get("winst2500_med")


def maak(map_, met_proef=False):
    kansen, stand = lees(map_, met_proef)
    uren = gemeten_uren(stand)
    uit = ["# Rapport koersverschil-scanner", ""]
    uit.append(f"Gemaakt {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC uit {len(stand)} runs, "
               f"samen ±{uren:.1f} uur gemeten (GEZIEN).")
    uit.append(f"Echte kans = winst na alle kosten, opnemen en storten open, minstens {eur(MIN_RUIMTE)} op het "
               f"boek, minstens {MIN_DUUR // 60} minuten blijven staan, geen andere munt met dezelfde naam.")
    uit.append("")
    if not kansen:
        uit.append("Nog geen kansen gemeten.")
        return "\n".join(uit)

    alle_echte = [r for r in kansen if echt(r)]
    echte = gebeurtenissen(alle_echte)
    # Trechter: waarom vallen kansen af?
    winst = [r for r in kansen if (r.get("winst_ruimte_med") or 0) > 0]
    open_ = [r for r in winst if r.get("opname_koop") is True and r.get("storting_verkoop") is True]
    dicht = [r for r in winst if r.get("opname_koop") is False or r.get("storting_verkoop") is False]
    onbekend = [r for r in winst if r not in open_ and r not in dicht]
    ruimte = [r for r in open_ if (r.get("ruimte_eur_med") or 0) >= MIN_RUIMTE]
    lang = [r for r in ruimte if (r.get("duur_s") or 0) >= MIN_DUUR]
    uit += ["## Trechter (GEZIEN, eigen metingen)", "",
            "| Stap | Aantal |", "|---|---|",
            f"| Verschillen met winst op het boek na alle kosten | {len(winst)} |",
            f"| ...waarvan opnemen of storten dicht | {len(dicht)} |",
            f"| ...waarvan status onbekend (beurs geeft het niet openbaar) | {len(onbekend)} |",
            f"| ...waarvan opnemen en storten open | {len(open_)} |",
            f"| ...en minstens {eur(MIN_RUIMTE)} op het boek | {len(ruimte)} |",
            f"| ...en minstens {MIN_DUUR // 60} minuten blijven staan | {len(lang)} |",
            f"| ...en geen andere munt met dezelfde naam | {len(alle_echte)} |",
            f"| Samengevoegd (zelfde munt, overlappend in de tijd, beste beurspaar telt): **echte kansen** | "
            f"**{len(echte)}** |",
            f"| Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld) | "
            f"{sum(1 for r in onbekend if echt({**r, 'opname_koop': True, 'storting_verkoop': True}))} |", ""]

    # Per dag
    per_dag = collections.defaultdict(list)
    for r in echte:
        per_dag[r["begin"][:10]].append(r)
    uit += ["## Echte kansen per dag (GEZIEN)", "", "| Dag | Echte kansen | Mediane winst per kans (bij €500) | "
            "Mediane winst (hele ruimte) | Mediane duur |", "|---|---|---|---|---|"]
    for dag in sorted(per_dag):
        rs = per_dag[dag]
        uit.append(f"| {dag} | {len(rs)} | {eur(med([r.get('winst500_med') for r in rs]))} | "
                   f"{eur(med([r.get('winst_ruimte_med') for r in rs]))} | "
                   f"{med([r['duur_s'] for r in rs]) / 60:.1f} min |")
    uit.append(f"| **Totaal** | **{len(echte)}** | {eur(med([r.get('winst500_med') for r in echte]))} | "
               f"{eur(med([r.get('winst_ruimte_med') for r in echte]))} | "
               f"{(med([r['duur_s'] for r in echte]) or 0) / 60:.1f} min |" if echte else "| Totaal | 0 | | | |")
    uit.append("")

    if echte:
        for titel, sleutel in (("munten", lambda r: f"{r['munt']}-{r['quote']}"),
                               ("beursparen (kopen op, verkopen op)", lambda r: f"{r['koop']} > {r['verkoop']}")):
            som = collections.defaultdict(lambda: [0, 0.0])
            for r in echte:
                s = som[sleutel(r)]
                s[0] += 1
                s[1] += r.get("winst500_med") or 0
            top = sorted(som.items(), key=lambda x: -x[1][1])[:10]
            uit += [f"## Beste {titel} (GEZIEN)", "", "| | Kansen | Som winst bij €500 per kans |", "|---|---|---|"]
            uit += [f"| {k} | {n} | {eur(w)} |" for k, (n, w) in top]
            uit.append("")
        tel = collections.Counter()
        for r in echte:
            tel[r["koop"]] += 1
            tel[r["verkoop"]] += 1
        uit += ["Beurzen die het vaakst meedoen (koop of verkoop): " +
                ", ".join(f"{b} {n}" for b, n in tel.most_common(8)) + " (GEZIEN).", ""]

    # Tijd om geld te schuiven
    uit += ["## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)", "",
            "Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan "
            "verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur "
            "of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).", "",
            "| Overmaaktijd | Echte kansen die nog stonden | Deel |", "|---|---|---|"]
    for minuten in (5, 10, 30, 60):
        n = sum(1 for r in echte if r["duur_s"] >= minuten * 60)
        uit.append(f"| {minuten} min | {n} | {n / len(echte) * 100:.0f}% |" if echte else f"| {minuten} min | 0 | |")
    uit.append("")

    # Projectie
    uit += ["## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)", ""]
    if not echte or uren < 1:
        uit.append("Te weinig gemeten om door te trekken.")
    else:
        per_uur = len(echte) / uren
        uit.append(f"Gemeten: {len(echte)} echte kansen in ±{uren:.1f} uur = {per_uur:.2f} per uur (GEZIEN). "
                   f"Doorgetrokken naar {DAGEN_PROJECTIE} dagen = ±{per_uur * 24 * DAGEN_PROJECTIE:.0f} kansen (GOK: "
                   "aanname dat de week die we maten gewoon is).")
        uit.append("")
        uit.append("| Inleg | Model | Per kans (mediaan) | 3 maanden |")
        uit.append("|---|---|---|---|")
        for inleg in INLEGGEN:
            # Voorraadmodel: de helft van de inleg staat als quote op de koopbeurs, de helft als munt op de
            # verkoopbeurs, dus per kans hooguit inleg/2. Bovengrens: geld staat overal tegelijk (kan niet).
            per = med([winst_bij(r, inleg / 2) for r in echte]) or 0
            uit.append(f"| {eur(inleg)} | bovengrens: elke kans gepakt, geld overal tegelijk | {eur(per)} | "
                       f"{eur(per * per_uur * 24 * DAGEN_PROJECTIE)} |")
            # Realistischer: alleen het beste beurspaar (al het geld op twee beurzen).
            paren = collections.defaultdict(list)
            for r in echte:
                paren[(r["koop"], r["verkoop"])].append(r)
            beste = max(paren.items(), key=lambda x: sum(winst_bij(r, inleg / 2) or 0 for r in x[1]))
            som = sum(winst_bij(r, inleg / 2) or 0 for r in beste[1])
            uit.append(f"| {eur(inleg)} | alleen het beste beurspaar ({beste[0][0]} > {beste[0][1]}) | "
                       f"{eur(med([winst_bij(r, inleg / 2) for r in beste[1]]))} | "
                       f"{eur(som / uren * 24 * DAGEN_PROJECTIE)} |")
        uit += ["", "Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, "
                "maar andere bots pakken hem ook; prijzen van de munt die je als voorraad aanhoudt kunnen dalen; "
                "na elke paar kansen moet de voorraad terug (opnamekosten en tijd); en een kans die we 2 minuten zagen "
                "staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te somber kan zijn: met voorraad "
                "op beide beurzen kun je dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee."]
    uit.append("")

    # Kwaliteit van de meting
    bronnen = collections.Counter(r.get("opname_bron") for r in echte)
    uit += ["## Over de meting", "",
            f"- Alle gemeten verschillen met winst op het boek: {len(winst)}; met status open/dicht/onbekend: "
            f"{len(open_)}/{len(dicht)}/{len(onbekend)} (GEZIEN).",
            f"- Opnamekosten bij de echte kansen: {bronnen.get('beurs', 0)} van de beurs zelf, "
            f"{bronnen.get('geschat', 0)} geschat uit wat andere beurzen voor die munt vragen (GOK), "
            f"{bronnen.get('onbekend', 0)} onbekend (op 0 gezet, dus te gunstig).",
            "- Of de munt op beide beurzen over hetzelfde netwerk gaat, controleren we niet; een munt kan op de ene "
            "beurs alleen via netwerk X en op de andere alleen via Y te storten zijn (GOK, komt voor).",
            "- De duur is gemeten in stappen van ±20 seconden; een kans kan tot een paar rondes eerder begonnen zijn "
            "dan we zagen (het rooster controleert honderden kandidaten om de beurt)."]
    if stand:
        laatste = [rij[-1] for rij in stand]
        uit.append(f"- Laatste run: {laatste[-1].get('beurzen_ok')} beurzen antwoordden, "
                   f"{laatste[-1].get('paren_vergeleken')} munt-quote-paren op minstens twee beurzen (GEZIEN).")
    return "\n".join(uit)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--met-proef"]
    print(maak(args[0] if args else ".", "--met-proef" in sys.argv))
