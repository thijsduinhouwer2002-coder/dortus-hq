#!/usr/bin/env python3
"""Rapport van de kansenradar.

Gebruik:  python3 radar_rapport.py <map met data> [--met-proef]   (bijv. een checkout van de tak ai-handel-data, map radar/)
Leest alle */*/ bestanden van de radar en schrijft het rapport als Markdown naar stdout. Proefruns (map eindigt op
-proef) lopen gelijk met de vaste run en tellen niet mee, tenzij --met-proef.

Wat telt als echt moment (GEZIEN = uit onze metingen, GOK = aanname):
  A en C1 (koop op beurs X, verkoop op beurs Y): na takerkosten en één opname van de munt blijft winst over, de
     opnamekosten zijn bekend of geschat, opnemen op X en storten op Y staan open (bekend), geen netwerk dat aan
     beide kanten dicht is, geen ander contractadres, en minstens 2 metingen (dus niet één toevallige blik).
  B (funding): positieve piek (spot kopen, perp shorten kan zonder lenen), er is een spotmarkt voor de munt.
     Negatieve pieken staan apart: dan moet je spot shorten, dat kan een particulier meestal niet.
  C2 (los van de koppeling): het boek zit minstens 0,3% van 1 dollar of 1 euro af. Geen arbitrage: je wint
     alleen als de koers terugkomt. Apart: hoeveel daarvan na takerkosten (2 keer) nog winst of 0,3% geven.
Winst per moment = de winst bij de eerste meting (meteen instappen), bij de gegeven inleg, uit het echte boek.
Kleine inleg (€100, €150, €200): een moment telt bij die inleg alleen als de minimale orderbedragen (en bij A en C1
het minimale opnamebedrag) bekend zijn en eronder liggen; onbekend staat apart.
"""
import collections
import datetime as dt
import glob
import json
import os
import statistics
import sys

INLEG = (100, 150, 200, 500, 2000, 5000)
KLEIN = (100, 150, 200)
MIN_UREN_WEEK = 3   # korter gemeten: geen som per week (te weinig om op te schalen)
MIN_RUIMTE = 100   # minstens zoveel euro winstgevend op het boek (zelfde grens als de scanner); anders een dode markt
# Beurzen met een MiCA-vergunning in het ESMA-register (19 nov 2026), zelfde lijst als ../scanner/README.md.
MICA = {"bitvavo", "kraken", "coinbase", "bitstamp", "okx", "cryptocom", "bybit", "kucoin", "gate", "bingx"}
# Perps: deze beurzen hebben een MiCA-vergunning voor spot. Of hun EU-dochter perps aan Nederlandse particulieren
# geeft, is niet nagekeken (GOK, vaak niet of beperkt). Hyperliquid en dYdX zijn DEX'en zonder vergunning.
MICA_PERP = {"okx", "gate", "kucoin", "bingx", "kraken"}
SOORTEN = (("alle", "alle"), ("vergund", "MiCA"), ("grijs", "grijs"))


def lees_jsonl(map_, naam, met_proef):
    uit = []
    for p in sorted(glob.glob(os.path.join(map_, "**", naam), recursive=True)):
        if not met_proef and os.path.dirname(p).endswith("-proef"):
            continue
        with open(p) as fh:
            rij = [json.loads(x) for x in fh if x.strip()]
        uit.append(rij) if naam == "stand.jsonl" else uit.extend(rij)
    return uit


def gemeten_uren(stand):
    uren = 0.0
    for rij in stand:
        if not rij:
            continue
        a = dt.datetime.strptime(rij[0]["t"], "%Y-%m-%dT%H:%M:%SZ")
        b = dt.datetime.strptime(rij[-1]["t"], "%Y-%m-%dT%H:%M:%SZ")
        uren += (b - a).total_seconds() / 3600 + 5 / 60
    return uren


def soort_paar(r):
    return "vergund" if r.get("koop") in MICA and r.get("verkoop") in MICA else "grijs"


def soort_funding(r):
    return "vergund" if r.get("beurs") in MICA_PERP and r.get("spot") in MICA else "grijs"


def soort_een(r):
    return "vergund" if r.get("beurs") in MICA else "grijs"


def echt_paar(r):
    return (r.get("winst_ruimte_med") or 0) > 0 and r.get("opname_koop") is True \
        and r.get("storting_verkoop") is True and r.get("netwerk") != "dicht" and r.get("contract") != "anders" \
        and r.get("opname_bron") != "onbekend" and (r.get("metingen") or 0) >= 2 \
        and (r.get("ruimte_eur_med") or 0) >= MIN_RUIMTE


def echt_funding(r):
    return r.get("richting") == "positief" and r.get("spot") and r.get("netto_pct") is not None


def winst(r, inleg):
    """Winst bij de eerste meting (A, C1, C2) of over de hele piek (B), in euro, bij deze inleg."""
    if "eerste" in r:
        return (r["eerste"] or {}).get(f"winst{inleg}")
    return r.get(f"winst{inleg}")


def haalbaar(r, inleg, hoek):
    """True/False als de minimale bedragen bekend zijn, None als een ervan onbekend is."""
    if hoek == "B":
        positie = inleg * 2 / 3
        mins = [r.get("min_spot_eur"), r.get("min_perp_eur")]
    elif hoek == "C2":
        positie, mins = inleg, [r.get("min_order_eur")]
    else:
        positie, mins = inleg, [r.get("min_koop_eur"), r.get("min_verkoop_eur"), r.get("min_opname_eur")]
    if any(m is None for m in mins):
        return None
    return all(m <= positie for m in mins)


def med(w):
    w = [x for x in w if isinstance(x, (int, float))]
    return statistics.median(w) if w else None


def eur(x, d=2):
    if x is None:
        return "-"
    t = f"{abs(x):,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{'-' if x < 0 else ''}€{t}"


def duur(s):
    if s is None:
        return "-"
    return f"{s / 60:.0f} min" if s >= 60 else f"{s:.0f} s"


def dag(r):
    return (r.get("begin") or r.get("t") or "")[:10]


def tabel_per_dag(rs, soort_fn, titel):
    uit = [f"**{titel}, per dag**", "", "| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |",
           "|---|---|---|---|"]
    per = collections.defaultdict(list)
    for r in rs:
        per[dag(r)].append(r)
    if not per:
        return uit[:1] + ["", "Nog geen momenten.", ""]
    for d in sorted(per):
        x = per[d]
        n_v = sum(1 for r in x if soort_fn(r) == "vergund")
        uit.append(f"| {d} | {len(x)} / {n_v} / {len(x) - n_v} | {eur(med(winst(r, 500) for r in x))} | "
                   f"{duur(med(r.get('duur_s') for r in x))} |")
    return uit + [""]


def tabel_inleg(rs, soort_fn, hoek, uren):
    """Per inleg: hoeveel momenten kunnen meedoen (minima), mediane winst, som over de meting en per week (GOK)."""
    uit = ["| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Mediane winst per keer | Som gemeten | "
           "Per week (GOK) |", "|---|---|---|---|---|---|"]
    for i in INLEG:
        if i in KLEIN:
            ok = [r for r in rs if haalbaar(r, i, hoek) is True]
            onb = sum(1 for r in rs if haalbaar(r, i, hoek) is None)
        else:
            ok = [r for r in rs if haalbaar(r, i, hoek) is not False]
            onb = sum(1 for r in rs if haalbaar(r, i, hoek) is None)
        w = [winst(r, i) for r in ok if winst(r, i) is not None]
        som = sum(w)
        week = som * 168 / uren if uren >= MIN_UREN_WEEK else None
        n_v = sum(1 for r in ok if soort_fn(r) == "vergund")
        uit.append(f"| {eur(i, 0)} | {len(ok)} / {n_v} | {onb} | {eur(med(w))} | {eur(som)} | {eur(week)} |")
    uit.append("")
    uit.append("Bij €100 tot €200 telt een moment alleen als de minimale bedragen bekend zijn en eronder liggen. Vanaf "
               "€500 telt onbekend mee (de minima liggen meestal tussen €1 en €10, GEZIEN in de API's).")
    return uit + [""]


def rapport(map_, met_proef=False):
    stand = lees_jsonl(map_, "stand.jsonl", met_proef)
    uren = gemeten_uren(stand)
    noteringen = lees_jsonl(map_, "noteringen.jsonl", met_proef)
    a = lees_jsonl(map_, "noteringen-kansen.jsonl", met_proef)
    b = lees_jsonl(map_, "funding.jsonl", met_proef)
    c1 = lees_jsonl(map_, "stable-tussen.jsonl", met_proef)
    c2 = lees_jsonl(map_, "stable-afwijking.jsonl", met_proef)
    nu = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    o = ["# Kansenradar: rapport", "",
         f"Gemaakt {nu}. Gemeten: **{uren:.1f} uur** in {len(stand)} run(s)"
         + (" (met proefruns)" if met_proef else "") + ". Alle aantallen en bedragen zijn GEZIEN (eigen metingen "
         "uit openbare API's), behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.", "",
         "**Wat we niet zien.** We kijken elke 15 seconden (stablecoins), elke minuut (boeken bij nieuwe noteringen), "
         "elke 2 minuten (funding) of elke 3 minuten (lijsten met paren). Snelle partijen kijken elke milliseconde en "
         "zitten vaak bij de beurs in de kast. Wat korter bestaat dan onze stap, zien we niet; wat we wel zien, is "
         "vaak al half weggekocht voor een gewone gebruiker zijn order plaatst. De sommen per week nemen aan dat je "
         "elk moment pakt dat wij zagen, en zijn daarom een **bovengrens (GOK)**.", ""]

    # ---- A ----
    echt_a = [r for r in a if echt_paar(r)]
    o += ["## A. Nieuwe noteringen", "",
          f"Nieuwe munten op een beurs gezien: **{len(noteringen)}** "
          f"(waarvan {sum(1 for n in noteringen if n.get('vlak_na_start'))} bij de eerste vergelijking na de start, "
          f"die kunnen in het gat tussen twee runs genoteerd zijn), "
          f"{sum(1 for n in noteringen if n.get('elders'))} stonden al op een andere beurs met dezelfde quote. "
          f"Prijsverschil-momenten daarna: {len(a)}, waarvan **{len(echt_a)} echt** (alles open en minstens "
          f"€{MIN_RUIMTE} winstgevend op het boek, zie boven).", ""]
    if noteringen:
        o += ["| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |", "|---|---|---|---|---|"]
        for n in noteringen[-15:]:
            o.append(f"| {n['t'][5:16]} | {n['beurs']}{'' if n['beurs'] in MICA else ' (grijs)'} | {n['munt']}-"
                     f"{n['quote']} | {', '.join(n.get('elders') or []) or '-'} | {n.get('opname')} / "
                     f"{n.get('storting')} |")
        o.append("")
    weg = collections.Counter()
    for r in a:
        if not echt_paar(r):
            weg["opnemen of storten dicht/onbekend" if not (r.get("opname_koop") is True and r.get(
                "storting_verkoop") is True) else "anders (netwerk, contract, opnamekosten onbekend of 1 meting)"] += 1
    if weg:
        o += ["Afgevallen: " + ", ".join(f"{k}: {v}" for k, v in weg.items()) + ".", ""]
    o += tabel_per_dag(echt_a, soort_paar, "Echte momenten A")
    o += tabel_inleg(echt_a, soort_paar, "A", uren)

    # ---- B ----
    pos = [r for r in b if echt_funding(r)]
    neg = [r for r in b if r.get("richting") == "negatief"]
    o += ["## B. Funding-pieken", "",
          f"Pieken boven 0,1% per 8 uur (gesloten onder 0,05%): **{len(pos)} positief met spotmarkt**, "
          f"{len(neg)} negatief (niet te dekken zonder spot te shorten), "
          f"{sum(1 for r in b if r.get('richting') == 'positief' and not r.get('spot'))} positief zonder spotmarkt. "
          f"Daarvan liepen er {sum(1 for r in pos if r.get('einde_run'))} nog bij het einde van een run en "
          f"{sum(1 for r in pos if r.get('al_bij_start'))} al bij de start (duur en winst te laag geteld). "
          f"Spotmunt met dezelfde naam maar een andere prijs (ander ding, niet geteld): "
          f"{sum(1 for r in b if r.get('spot_anders'))}. "
          f"Met winst na kosten: {sum(1 for r in pos if (r.get('netto_pct') or 0) > 0)}; "
          f"met minstens één verrekening: {sum(1 for r in pos if (r.get('verrekeningen') or 0) > 0)}; "
          f"met meer dan $1 miljoen handel per dag: {sum(1 for r in pos if (r.get('vol_usd') or 0) >= 1e6)}.", "",
          "Som per piek: funding die echt verrekend werd, min 4 keer takerkosten (spot in en uit, perp in en uit), "
          "plus of min het verschil tussen spot- en perpprijs bij in- en uitstappen. Inleg = 2/3 spot en 1/3 "
          "onderpand voor de short bij 2x hefboom (GOK, een gangbare verdeling).", ""]
    if pos:
        top = sorted(pos, key=lambda r: -(r.get("netto_pct") or -99))[:10]
        o += ["| Begin | Perp | Munt | Spot | Max per 8u | Verrekend | Kosten | Prijsverschil | Netto | Duur | Handel/dag |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in top:
            o.append(f"| {r['begin'][5:16]} | {r['beurs']} | {r['munt']} | {r.get('spot')} | {r['r8_max_pct']}% | "
                     f"{r['ontvangen_pct']}% ({r['verrekeningen']}x) | {r['kosten_pct']}% | {r.get('basis_pct')}% | "
                     f"**{r['netto_pct']}%** | {duur(r['duur_s'])} | ${(r.get('vol_usd') or 0) / 1e6:.1f} mln |")
        o.append("")
    o += tabel_per_dag(pos, soort_funding, "Positieve pieken B")
    o += tabel_inleg(pos, soort_funding, "B", uren)
    o += ["Vergund bij B betekent: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps "
          "aan Nederlandse particulieren geeft, is niet nagekeken (GOK: vaak niet of beperkt). De opschaling is "
          "lineair (GOK): bij een dunne perp (weinig handel per dag) kost een grotere order meer dan de laatste "
          "prijs, dat meten we niet.", ""]

    # ---- C ----
    echt_c1 = [r for r in c1 if echt_paar(r)]
    c2_diep = [r for r in c2 if (r.get("ruimte_eur_max") or 0) >= MIN_RUIMTE]
    na0 = [r for r in c2_diep if (r.get("na_kosten_pct_max") or -1) > 0]
    na3 = [r for r in c2_diep if (r.get("na_kosten_pct_max") or -1) >= 0.3]
    o += ["## C. Stablecoins", "",
          f"**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): "
          f"{len(c1)} momenten, waarvan **{len(echt_c1)} echt**.", ""]
    o += tabel_per_dag(echt_c1, soort_paar, "Echte momenten C1")
    o += tabel_inleg(echt_c1, soort_paar, "C1", uren)
    o += [f"**C2, los van de koppeling** (boek minstens 0,3% van 1 dollar of 1 euro): {len(c2)} momenten, waarvan "
          f"{len(c2_diep)} met minstens €{MIN_RUIMTE} op het boek (de rest is een dode markt); daarvan na 2 keer "
          f"takerkosten nog winst: {len(na0)}; na kosten nog minstens 0,3%: **{len(na3)}**. Geen arbitrage: je "
          "wint alleen als de koers terugkomt (GOK dat hij dat doet; bij USDC in maart 2023 kwam hij terug, bij UST "
          "in 2022 niet).", ""]
    tel = collections.Counter(f"{r['munt']}-{r['quote']} op {r['beurs']} ({r['kant']})" for r in c2_diep)
    if tel:
        o += ["Meest gezien: " + ", ".join(f"{k} {v}x" for k, v in tel.most_common(8)) + ".", ""]
    o += tabel_per_dag(na0, soort_een, "C2 met winst na kosten")
    o += tabel_inleg(na0, soort_een, "C2", uren)

    o += ["## Hoe eerlijk is de opschaling naar €2.000 en €5.000", "",
          "- A en C1: de winst bij €2.000 en €5.000 komt uit het echte orderboek op dat moment (dieper in het boek is "
          "duurder). Maar je hebt voorraad op beide beurzen nodig, of je moet overmaken, en dan is het gat vaak weg.",
          "- B: lineair opgeschaald, alleen begrensd door de minimale order. GOK.",
          "- C2: uit het boek, maar het is een gok op terugkeer, geen arbitrage.",
          "- Per week = som gemeten maal 168 uur gedeeld door de gemeten uren. Na een paar uur meten is dat een "
          "ruwe GOK; na 7 dagen een week aan metingen.",
          "- Kleine inleg: vaste kosten per keer (opnamekosten van de munt) wegen bij €100 zwaar; die zitten in de "
          "winst bij A en C1.", ""]
    return "\n".join(o)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    print(rapport(sys.argv[1], "--met-proef" in sys.argv))


if __name__ == "__main__":
    main()
