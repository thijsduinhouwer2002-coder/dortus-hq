#!/usr/bin/env python3
"""Rapport van de koersverschil-scanner.

Gebruik:  python3 rapport.py <map met data> [--met-proef]   (bijv. een checkout van de tak ai-handel-data, map scanner/)
Leest alle */*/kansen.jsonl en stand.jsonl daaronder en schrijft het rapport als Markdown naar stdout.
Proefruns (map eindigt op -proef) lopen gelijk met de vaste run en tellen dus niet mee, tenzij --met-proef.

Een ECHTE kans (alles moet waar zijn):
  1. na takerkosten aan beide kanten en de opnamekosten van de munt blijft er winst over, en die opnamekosten
     zijn bekend (van de beurs of geschat uit andere beurzen; onbekend telt niet);
  2. opnemen op de koopbeurs en storten op de verkoopbeurs staan open (bekend, niet "onbekend"), en als beide
     beurzen hun netwerken geven: er is een netwerk dat aan beide kanten open is;
  3. er ligt minstens MIN_RUIMTE euro winstgevend op het boek;
  4. hij bleef minstens MIN_DUUR seconden staan;
  5. het is niet zichtbaar een andere munt met dezelfde naam (contractadressen verschillen niet).
Vergund en grijs staan apart: "vergund" = beide beurzen hebben (via een EU-dochter) een MiCA-vergunning in het
ESMA-register; "grijs" = minstens één beurs niet (zie README.md).
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
# Beurzen met een MiCA-vergunning in het ESMA-register (19 nov 2026, zie README.md). Vaak via een EU-dochter, die
# minder munten kan hebben dan de wereldwijde API die we meten (GOK).
MICA = {"bitvavo", "kraken", "coinbase", "bitstamp", "okx", "cryptocom", "bybit", "kucoin", "gate", "bingx"}
SOORTEN = (("alle", "Alle beurzen"), ("vergund", "Alleen MiCA-beurzen"), ("grijs", "Met minstens één grijze beurs"))


def echt(r):
    return (r.get("winst_ruimte_med") or 0) > 0 and r.get("opname_koop") is True \
        and r.get("storting_verkoop") is True and (r.get("ruimte_eur_med") or 0) >= MIN_RUIMTE \
        and (r.get("duur_s") or 0) >= MIN_DUUR and r.get("contract") != "anders" \
        and r.get("opname_bron") != "onbekend" and r.get("netwerk") != "dicht"


def soort(r):
    return "vergund" if r["koop"] in MICA and r["verkoop"] in MICA else "grijs"


def van(rs, s):
    return rs if s == "alle" else [r for r in rs if soort(r) == s]


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


def trechter(kansen):
    """Aantallen per stap. Elke stap is een deel van de vorige, behalve de regels met "waarvan"."""
    winst = [r for r in kansen if (r.get("winst_ruimte_med") or 0) > 0]
    dicht = [r for r in winst if r.get("opname_koop") is False or r.get("storting_verkoop") is False]
    open_ = [r for r in winst if r.get("opname_koop") is True and r.get("storting_verkoop") is True]
    onbekend = [r for r in winst if r not in open_ and r not in dicht]
    net = [r for r in open_ if r.get("netwerk") != "dicht"]
    fee = [r for r in net if r.get("opname_bron") != "onbekend"]
    ruimte = [r for r in fee if (r.get("ruimte_eur_med") or 0) >= MIN_RUIMTE]
    lang = [r for r in ruimte if (r.get("duur_s") or 0) >= MIN_DUUR]
    munt = [r for r in lang if r.get("contract") != "anders"]
    return [
        ("Verschillen met winst op het boek na alle kosten", len(winst)),
        ("...waarvan opnemen of storten dicht", len(dicht)),
        ("...waarvan status onbekend (beurs geeft het niet openbaar)", len(onbekend)),
        ("Opnemen en storten open", len(open_)),
        ("...en geen netwerk dat aan beide kanten open is: valt af", len(open_) - len(net)),
        ("...en opnamekosten onbekend: valt af", len(net) - len(fee)),
        (f"...en minstens {eur(MIN_RUIMTE)} op het boek", len(ruimte)),
        (f"...en minstens {MIN_DUUR // 60} minuten blijven staan", len(lang)),
        ("...en geen andere munt met dezelfde naam", len(munt)),
        ("   ...waarvan contractadres bekend en gelijk", sum(1 for r in munt if r.get("contract") == "zelfde")),
        ("   ...waarvan contractadres onbekend (telt mee, kan een andere munt zijn)",
         sum(1 for r in munt if r.get("contract") != "zelfde")),
        ("   ...waarvan netwerk gekoppeld en open", sum(1 for r in munt if r.get("netwerk") == "open")),
        ("   ...waarvan netwerk niet te koppelen (telt mee)", sum(1 for r in munt if r.get("netwerk") != "open")),
        ("**Echte kansen** (zelfde munt overlappend in de tijd samengevoegd, beste beurspaar telt)",
         len(gebeurtenissen(munt))),
        ("Ter vergelijking: zelfde eisen, maar opnamestatus onbekend (niet meegeteld)",
         len(gebeurtenissen([r for r in onbekend if echt({**r, "opname_koop": True, "storting_verkoop": True})]))),
    ]


def dekking(stand):
    """Hoeveel kandidaten worden er gecontroleerd? Uit stand.jsonl (alleen runs die het veld al schreven)."""
    rijen = [x for rij in stand for x in rij if "nooit_gecontroleerd" in x and x.get("kandidaten")]
    if not rijen:
        return None
    return {"kandidaten": med([x["kandidaten"] for x in rijen]), "gecontroleerd": med([x["gecontroleerd"] for x in rijen]),
            "nooit": med([x["nooit_gecontroleerd"] for x in rijen]), "metingen": len(rijen),
            "deel_nooit": med([x["nooit_gecontroleerd"] / x["kandidaten"] for x in rijen])}


def maak(map_, met_proef=False):
    kansen, stand = lees(map_, met_proef)
    uren = gemeten_uren(stand)
    uit = ["# Rapport koersverschil-scanner", ""]
    uit.append(f"Gemaakt {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC uit {len(stand)} runs, "
               f"samen ±{uren:.1f} uur gemeten (GEZIEN).")
    uit.append(f"Echte kans = winst na alle kosten (opnamekosten bekend), opnemen en storten open (en een netwerk "
               f"dat aan beide kanten open is, als de beurzen dat geven), minstens {eur(MIN_RUIMTE)} op het boek, "
               f"minstens {MIN_DUUR // 60} minuten blijven staan, geen andere munt met dezelfde naam.")
    uit.append("**Vergund** = beide beurzen hebben een MiCA-vergunning (ESMA-register), vaak via een EU-dochter die "
               "minder munten kan hebben dan de wereldwijde API die we meten (GOK). **Grijs** = minstens één beurs "
               "zonder vergunning (MEXC, Bitget, HTX, Poloniex, XT, Bitfinex, Binance). Zie README.md.")
    uit.append("")
    d = dekking(stand)
    ondergrens = bool(d and d["deel_nooit"] > 0.05)
    if d:
        uit += ["## Hoeveel wordt er gecontroleerd? (GEZIEN, stand.jsonl)", "",
                f"Per ronde (mediaan over {d['metingen']} metingen): {d['kandidaten']:.0f} kandidaten (verschil op de "
                f"ticker groter dan de takerkosten), {d['gecontroleerd']:.0f} met het orderboek gecontroleerd, "
                f"{d['nooit']:.0f} nog nooit gecontroleerd ({d['deel_nooit'] * 100:.0f}%).",
                ("**Daarom zijn de aantallen en sommen hieronder een ondergrens:** een deel van de kandidaten is nooit "
                 "met het boek bekeken." if ondergrens else
                 "Bijna alle kandidaten komen aan de beurt; de aantallen hieronder missen weinig."), ""]
    else:
        uit += ["Hoeveel kandidaten nooit gecontroleerd zijn, staat nog niet in de data (oudere runs); de aantallen "
                "hieronder zijn daarom een ondergrens.", ""]
        ondergrens = True
    if not kansen:
        uit.append("Nog geen kansen gemeten.")
        return "\n".join(uit)

    alle_echte = [r for r in kansen if echt(r)]
    per_soort = {s: gebeurtenissen(van(alle_echte, s)) for s, _ in SOORTEN}
    echte = per_soort["alle"]

    t = {s: trechter(van(kansen, s)) for s, _ in SOORTEN}
    uit += ["## Trechter (GEZIEN, eigen metingen)", "",
            "| Stap | " + " | ".join(n for _, n in SOORTEN) + " |", "|---|---|---|---|"]
    for i, (stap, _) in enumerate(t["alle"]):
        uit.append(f"| {stap} | " + " | ".join(str(t[s][i][1]) for s, _ in SOORTEN) + " |")
    uit.append("")

    per_dag = collections.defaultdict(list)
    for r in echte:
        per_dag[r["begin"][:10]].append(r)
    uit += ["## Echte kansen per dag (GEZIEN)", "",
            "| Dag | Echt, alleen MiCA | Echt, met grijs | Mediane winst per kans bij €500 (MiCA / grijs) | "
            "Mediane duur |", "|---|---|---|---|---|"]
    for dag in sorted(per_dag) + ["Totaal"]:
        rs = echte if dag == "Totaal" else per_dag[dag]
        v, g = van(rs, "vergund"), van(rs, "grijs")
        uit.append(f"| {dag} | {len(v)} | {len(g)} | {eur(med([r.get('winst500_med') for r in v]))} / "
                   f"{eur(med([r.get('winst500_med') for r in g]))} | "
                   f"{(med([r['duur_s'] for r in rs]) or 0) / 60:.1f} min |")
    uit.append("")

    if echte:
        for titel, sleutel in (("munten", lambda r: f"{r['munt']}-{r['quote']}"),
                               ("beursparen (kopen op > verkopen op)", lambda r: f"{r['koop']} > {r['verkoop']}")):
            som = collections.defaultdict(lambda: [0, 0.0, set()])
            for r in echte:
                x = som[sleutel(r)]
                x[0] += 1
                x[1] += r.get("winst500_med") or 0
                x[2].add(soort(r))
            top = sorted(som.items(), key=lambda x: -x[1][1])[:10]
            uit += [f"## Beste {titel} (GEZIEN)", "", "| | Soort | Kansen | Som winst bij €500 per kans |",
                    "|---|---|---|---|"]
            uit += [f"| {k} | {' en '.join(sorted(so))} | {n} | {eur(w)} |" for k, (n, w, so) in top]
            uit.append("")
        tel = collections.Counter()
        for r in echte:
            tel[r["koop"]] += 1
            tel[r["verkoop"]] += 1
        uit += ["Beurzen die het vaakst meedoen (koop of verkoop): " +
                ", ".join(f"{b}{'' if b in MICA else ' (grijs)'} {n}" for b, n in tel.most_common(8)) +
                " (GEZIEN).", ""]

    uit += ["## Hoeveel kansen blijven staan terwijl je geld schuift? (GEZIEN, duur uit eigen metingen)", "",
            "Wie geen voorraad op beide beurzen heeft, moet kopen, de munt opnemen, wachten tot hij binnen is en dan "
            "verkopen. Hoe lang dat duurt verschilt per munt en netwerk: een paar minuten (snelle ketens) tot een uur "
            "of meer (Bitcoin, beurzen die opnames met de hand keuren) (GOK, niet per munt gemeten).", "",
            "| Overmaaktijd | " + " | ".join(n for _, n in SOORTEN) + " |", "|---|---|---|---|"]
    for minuten in (5, 10, 30, 60):
        cellen = []
        for s, _ in SOORTEN:
            rs = per_soort[s]
            n = sum(1 for r in rs if r["duur_s"] >= minuten * 60)
            cellen.append(f"{n} van {len(rs)}" + (f" ({n / len(rs) * 100:.0f}%)" if rs else ""))
        uit.append(f"| {minuten} min | " + " | ".join(cellen) + " |")
    uit.append("")

    uit += ["## Wat zou het opleveren over 3 maanden? (GOK, doorgetrokken uit de metingen)", ""]
    if not echte or uren < 1:
        uit.append("Te weinig gemeten om door te trekken.")
    else:
        uit.append(f"Gemeten over ±{uren:.1f} uur (GEZIEN), doorgetrokken naar {DAGEN_PROJECTIE} dagen (GOK: aanname "
                   "dat de week die we maten gewoon is)." + (" Ondergrens: niet alle kandidaten zijn gecontroleerd."
                                                              if ondergrens else ""))
        uit += ["", "| Beurzen | Inleg | Model | Kansen per uur | Per kans (mediaan) | 3 maanden |",
                "|---|---|---|---|---|---|"]
        for s, naam in (("vergund", "Alleen MiCA"), ("alle", "Alle (met grijs)")):
            rs = per_soort[s]
            per_uur = len(rs) / uren
            for inleg in INLEGGEN:
                if not rs:
                    uit.append(f"| {naam} | {eur(inleg)} | geen echte kansen gemeten | 0 | | €0,00 |")
                    continue
                per = med([winst_bij(r, inleg / 2) for r in rs]) or 0
                uit.append(f"| {naam} | {eur(inleg)} | bovengrens: elke kans, geld overal tegelijk | {per_uur:.2f} | "
                           f"{eur(per)} | {eur(per * per_uur * 24 * DAGEN_PROJECTIE)} |")
                paren = collections.defaultdict(list)
                for r in rs:
                    paren[(r["koop"], r["verkoop"])].append(r)
                beste = max(paren.items(), key=lambda x: sum(winst_bij(r, inleg / 2) or 0 for r in x[1]))
                som = sum(winst_bij(r, inleg / 2) or 0 for r in beste[1])
                uit.append(f"| {naam} | {eur(inleg)} | alleen het beste beurspaar ({beste[0][0]} > {beste[0][1]}) | "
                           f"{len(beste[1]) / uren:.2f} | {eur(med([winst_bij(r, inleg / 2) for r in beste[1]]))} | "
                           f"{eur(som / uren * 24 * DAGEN_PROJECTIE)} |")
        uit += ["", "Bovengrens: elke kans met de helft van de inleg aan elke kant, alsof het geld op alle beurzen "
                "tegelijk staat (kan in het echt niet). Beste beurspaar: het paar is **achteraf** gekozen uit de "
                "metingen (vooraf kiezen levert minder op), en het model neemt aan dat je van elke munt al voorraad op "
                "de verkoopbeurs hebt.",
                "", "Waarom dit te rooskleurig is (GOK): elke kans wordt maar één keer geteld met het mediane boek, "
                "maar andere bots pakken hem ook; de munt die je als voorraad aanhoudt kan dalen; na een paar kansen "
                "moet de voorraad terug (opnamekosten en tijd); minimale opname- en ordergroottes tellen niet mee; en "
                "een kans die we 2 minuten zagen staan, staat er niet per se nog als jouw order binnenkomt. Waarom het te "
                "somber kan zijn: niet alle kandidaten zijn gecontroleerd, en met voorraad op beide beurzen kun je "
                "dezelfde kans vaker pakken als het boek zich aanvult; dat telt hier niet mee."]
    uit.append("")

    bronnen = collections.Counter(r.get("opname_bron") for r in echte)
    uit += ["## Over de meting", "",
            f"- Opnamekosten bij de echte kansen: {bronnen.get('netwerk', 0)} van een netwerk dat aan beide kanten "
            f"open is, {bronnen.get('beurs', 0)} van de beurs zelf (laagste open netwerk), {bronnen.get('geschat', 0)} "
            "geschat uit wat andere beurzen voor die munt vragen (GOK). Onbekende opnamekosten tellen niet als echte kans.",
            "- Netwerk: KuCoin, Gate, Bitget, HTX, XT, Bitstamp, Bitvavo en Poloniex geven hun netwerken per munt. Als "
            "beide beurzen dat doen en de namen te koppelen zijn, moet er een netwerk zijn dat aan beide kanten open "
            "is. Anders is het netwerk \"niet te koppelen\" en telt de kans mee (staat apart in de trechter).",
            "- De duur is gemeten in stappen van ±20 seconden; een kans kan een paar rondes eerder begonnen zijn dan we "
            "zagen.",
            "- Takerkosten: uit de API waar die ze per paar geeft, anders het standaardtarief uit de README (deels GOK)."]
    if stand:
        laatste = stand[-1][-1]
        uit.append(f"- Laatste run: {laatste.get('beurzen_ok')} beurzen antwoordden, "
                   f"{laatste.get('paren_vergeleken')} munt-quote-paren op minstens twee beurzen (GEZIEN).")
    return "\n".join(uit)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--met-proef"]
    print(maak(args[0] if args else ".", "--met-proef" in sys.argv))
