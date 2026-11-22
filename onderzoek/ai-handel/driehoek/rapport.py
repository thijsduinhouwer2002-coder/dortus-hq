#!/usr/bin/env python3
"""Rapport van de driehoek-meter.

Gebruik:  python3 rapport.py <map met data> [--met-proef]   (bijv. een checkout van de tak ai-handel-data, map driehoek/)
Leest alle */*/driehoeken.jsonl en stand.jsonl daaronder en schrijft het rapport als Markdown naar stdout.
Proefruns (map eindigt op -proef) lopen gelijk met de vaste run en tellen dus niet mee, tenzij --met-proef.

Een ECHTE driehoek (alles moet waar zijn), gerekend met de kosten "hoog" (zie ontwerp.md):
  1. na drie keer takerkosten, afronding op de stapgrootte en de minimale ordergrootte blijft er winst over op het
     orderboek (niet alleen tegen de beste prijs);
  2. bevestigd: op twee metingen die minstens MIN_DUUR seconden uit elkaar liggen (en alle metingen daartussen)
     ging er minstens MIN_DIEPTE euro met winst doorheen;
  3. bij die latere meting (wat er na MIN_DUUR seconden nog stond) was de winst minstens MIN_WINST euro;
  4. niet verdacht (meer dan 5% winst per rondje is bijna altijd een dode markt of foute ticker).
Alle bedragen per kans zijn die van de latere meting, niet van het beste moment.
Samengevoegd tot één kans (ondergrens, zie kans.py): zelfde beurs, binnen SAMEN_S seconden van elkaar bevestigd,
een gedeeld paar dat geen paar van twee hoofdmunten is, zonder doorketenen. Los geteld staat ernaast (bovengrens). MiCA (de beurs of een EU-dochter heeft een vergunning in het ESMA-register) en grijs
staan apart. Elk cijfer is GEZIEN (uit onze eigen metingen) of GOK (een aanname, met reden).
Dit bestand draait met python3 -I; het zet zijn eigen map daarom zelf in het zoekpad (voor kans.py).
"""
import collections
import glob
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))   # draait met python3 -I: eigen map erbij
from kans import (INLEGGEN, KLEIN, MIN_DIEPTE, MIN_DUUR, MIN_WINST, SAMEN_S, SOORTEN, STAND_S, VANAF,  # noqa: E402
                  beste, echt, kansen, los, na, opgeteld, soort, van, wb)


def lees(map_, met_proef=False):
    rs, stand = [], []
    telt = lambda p: met_proef or not os.path.dirname(p).endswith("-proef")
    for naam, doel in (("driehoeken.jsonl", rs), ("stand.jsonl", stand)):
        for p in filter(telt, sorted(glob.glob(os.path.join(map_, "**", naam), recursive=True))):
            with open(p) as fh:
                for x in fh:
                    if x.strip():
                        try:
                            doel.append(json.loads(x))
                        except ValueError:
                            pass       # een halve regel (afgebroken run) overslaan
    return rs, stand


def lees_beurzen(map_, met_proef=False):
    """Laatste beursinfo per beurs (paren, kosten, minimale inleg) uit beurs-<naam>.json en beurzen.json."""
    uit = {}
    telt = lambda p: met_proef or not os.path.dirname(p).endswith("-proef")
    paden = glob.glob(os.path.join(map_, "**", "beurs-*.json"), recursive=True)
    paden += glob.glob(os.path.join(map_, "**", "beurzen.json"), recursive=True)
    for p in filter(telt, paden):
        try:
            with open(p) as fh:
                d = json.load(fh)
        except (OSError, ValueError):
            continue
        rij = d.get("beurzen") or {os.path.basename(p)[6:-5]: d}
        for b, info in rij.items():
            if info.get("min_inleg") and info.get("geladen", "") >= uit.get(b, {}).get("geladen", ""):
                uit[b] = info
    return uit


def med(w):
    return statistics.median(w) if w else None


def eur(x, d=2):
    if x is None:
        return "-"
    return f"€{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(x, d=3):
    return "-" if x is None else f"{x:.{d}f}%".replace(".", ",")


def getal(x, d=1):
    return str(round(x, d)).replace(".", ",")


def dag(r):
    return (r.get("hoog") or r.get("laag") or {}).get("begin", r.get("begin", ""))[:10]


def uren(stand, beurs=None):
    return sum(1 for s in stand if beurs is None or s.get("beurs") == beurs) * STAND_S / 3600


def kort_antwoord(echte, stand, gem_dagen):
    """Eén alinea in gewone woorden, voor alle tabellen (keuring moet 4)."""
    u = ["## Kort antwoord", ""]
    zinnen = []
    for s, n in (("vergund", "Op de beurzen met vergunning (MiCA, ook via een EU-dochter)"),
                 ("grijs", "Op de grijze beurzen (geen vergunning)")):
        groepen = [g for g in kansen(van(echte, s)) if wb(beste(g, 100), 100) > 0]
        losse = [g for g in los(van(echte, s)) if wb(g[0], 100) > 0]
        if not groepen:
            bm = [x["beste_marge_med"] for x in stand if soort(x) == s and x.get("beste_marge_med") is not None]
            zinnen.append(f"{n}: nog geen enkele driehoek die je met €100 tot €200 had kunnen pakken. Na de kosten"
                          f" en na {MIN_DUUR} seconden bleef er niets over met minstens {eur(MIN_DIEPTE, 0)} diepte."
                          + (f" De beste driehoek per ronde zat in de mediaan op {pct(med(bm), 2)} (negatief ="
                             " verlies; positief zegt nog niet dat er op het boek iets te halen was)." if bm else ""))
            continue
        w = {k: opgeteld(groepen, k)[0] / gem_dagen for k in (100, 200)}
        wl = {k: opgeteld(losse, k)[0] / gem_dagen for k in (100, 200)}
        zinnen.append(f"{n}: {len(groepen)} echte kansen die met €100 konden ({len(losse)} als je elke driehoek los"
                      f" telt; {getal(len(groepen) / gem_dagen)} per dag). Samen {eur(w[100])} tot {eur(wl[100])}"
                      f" per dag met €100 en {eur(w[200])} tot {eur(wl[200])} per dag met €200 (GOK; het lage getal"
                      " voegt driehoeken samen die hetzelfde stukje boek willen, het hoge telt ze los; allebei alsof"
                      " je ze allemaal als eerste pakt, met het geld al op de juiste beurs).")
    u.append(" ".join(zinnen))
    u += ["", "Uitleg: **takerkosten** zijn wat de beurs per order rekent als je meteen koopt of verkoopt tegen de"
              " prijs die er ligt (0% tot 0,8% per order; een driehoek is drie orders). **Diepte** is hoeveel euro je"
              " tegen die winstgevende prijzen echt kunt kopen en verkopen voordat de prijs slechter wordt. Wij meten"
              " elke 3 tot 5 seconden; snelle bots pakken zulke kansen meestal binnen milliseconden, dus wat hier staat"
              " is wat er na hen overbleef.", ""]
    return u


def maak(map_, met_proef=False):
    rs, stand = lees(map_, met_proef)
    info = lees_beurzen(map_, met_proef)
    echte = [r for r in rs if echt(r)]
    beurzen = sorted({s["beurs"] for s in stand} | {r["beurs"] for r in rs})
    status = {s["beurs"]: s.get("status") for s in stand}
    status.update({r["beurs"]: r.get("status") for r in rs})
    dagen = sorted({dag(r) for r in rs} | {s.get("t", "")[:10] for s in stand} - {""})
    per_beurs_uur = uren(stand) / max(len(beurzen), 1)
    gem_dagen = max(per_beurs_uur / 24, 1e-9)
    u = ["# Driehoek-meter: rapport", ""]
    u += kort_antwoord(echte, stand, gem_dagen)
    u += [f"Data: {len(rs)} driehoeken met winst op het boek gezien (ook kleine en korte), {len(dagen)} dag(en)"
          f" ({dagen[0] if dagen else '-'} tot {dagen[-1] if dagen else '-'}). Gemeten: ±{getal(per_beurs_uur)}"
          f" uur per beurs (GEZIEN, uit stand.jsonl).{' Proefruns tellen mee.' if met_proef else ''}", "",
          f"Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, op twee metingen die minstens"
          f" {MIN_DUUR} seconden uit elkaar liggen elk minstens {eur(MIN_DIEPTE, 0)} diepte, bij de latere meting minstens"
          f" {eur(MIN_WINST)} winst, en niet meer dan 5% winst (verdacht). Alle bedragen zijn die van de latere meting:"
          f" wat er na {MIN_DUUR} seconden nog stond. Driehoeken op dezelfde beurs die binnen {SAMEN_S} seconden van"
          " elkaar bevestigd werden en een paar delen dat geen paar van twee hoofdmunten is (EUR, USD, USDT, USDC,"
          " BTC, ETH), tellen als **één kans** (de beste telt): ze willen hetzelfde stukje orderboek. Er wordt niet"
          " doorgeketend: een driehoek hoort alleen bij een kans als hij met elk lid ervan dat stukje deelt. Omdat"
          " samenvoegen ook te streng kan zijn, staan aantallen en geld er ook los geteld bij (bovengrens).", "",
          f"Regels van vóór {VANAF.replace('T', ' ')} UTC (vóór de keuring) hebben geen meting na 3 seconden en"
          " tellen daarom nooit als echt. Daar zat ook niets in dat 3 seconden met €100 diepte stond.", ""]

    # ----- dekking per beurs
    u += ["## Per beurs: hoe gemeten en hoe dicht bij winst", "",
          "Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle"
          " rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen"
          " winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was"
          " (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge"
          " is nog geen winst: de bulk-koers kan achterlopen of er ligt maar een paar cent op die prijs; het"
          " orderboek beslist (kolom Winst op boek).", "",
          "| Beurs | Status | Paren | Driehoeken | Uur | Rondes | Fouten (te veel) | Beste marge mediaan | Beste marge hoogst | Kandidaten | Bekeken | Overgeslagen | Zelfde | Winst op boek | Echt |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for b in beurzen:
        ss = [s for s in stand if s["beurs"] == b]
        som = lambda k: sum(s.get(k) or 0 for s in ss)
        bm = [s["beste_marge_med"] for s in ss if s.get("beste_marge_med") is not None]
        bx = [s["beste_marge_max"] for s in ss if s.get("beste_marge_max") is not None]
        laatst = ss[-1] if ss else {}
        u.append(f"| {b} | {status.get(b) or '-'} | {laatst.get('paren') or '-'} | {laatst.get('driehoeken') or '-'} |"
                 f" {getal(uren(stand, b))} | {som('rondes')} | {som('fouten')} ({som('te_veel')}) | {pct(med(bm))} |"
                 f" {pct(max(bx) if bx else None)} | {som('kandidaten')} | {som('bekeken')} | {som('overgeslagen')} |"
                 f" {som('zelfde')} | {som('boek_winst')} | {sum(1 for r in echte if r['beurs'] == b)} |")
    over = sum(s.get("overgeslagen") or 0 for s in stand)
    kand = sum(s.get("kandidaten") or 0 for s in stand)
    if kand and over / kand > 0.05:
        u += ["", f"Let op: {over} van {kand} kandidaten ({100 * over / kand:.0f}%) zijn overgeslagen omdat het budget"
                  " van de ronde op was. De aantallen hieronder zijn dan een **ondergrens**."]
    u.append("")

    # ----- trechter
    hoog = lambda r: r.get("hoog") or {}
    u += ["## Trechter", "", "| Stap | " + " | ".join(n for _, n in SOORTEN) + " |", "|---|---|---|---|"]
    stappen = [
        ("winst op het boek, met de lage kosten (bovengrens)", lambda r: bool(r.get("laag"))),
        ("winst op het boek, met de gewone kosten", lambda r: bool(r.get("hoog"))),
        (f"en ooit minstens {eur(MIN_DIEPTE, 0)} diepte", lambda r: hoog(r).get("diepte_eur", 0) >= MIN_DIEPTE),
        (f"en na {MIN_DUUR} s nog steeds minstens {eur(MIN_DIEPTE, 0)} diepte", lambda r: bool(na(r))),
        (f"en dan minstens {eur(MIN_WINST)} winst", lambda r: bool(na(r)) and na(r)["winst_eur"] >= MIN_WINST),
        ("en niet verdacht = **echt**", echt),
    ]
    for naam, f in stappen:
        u.append(f"| {naam} | " + " | ".join(str(sum(1 for r in van(rs, s) if f(r))) for s, _ in SOORTEN) + " |")
    u.append("| echte **kansen** (samengevoegd als ze hetzelfde stukje boek willen; ondergrens) | "
             + " | ".join(str(len(kansen(van(echte, s)))) for s, _ in SOORTEN) + " |")
    u += ["", "De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo"
              " noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan"
              " gewoon.", ""]

    # ----- per dag
    u += ["## Per dag (echte kansen, bedragen na 3 seconden)", "",
          "| Dag | Soort | Driehoeken | Kansen | Mediane winst per kans | Mediane diepte | Mediane duur met €100 diepte | Totale winst (volle diepte) |",
          "|---|---|---|---|---|---|---|---|"]
    for d in dagen + ["totaal"]:
        for s, n in SOORTEN:
            g = [r for r in van(echte, s) if d == "totaal" or dag(r) == d]
            kk = [beste(k) for k in kansen(g)]
            u.append(f"| {d} | {n} | {len(g)} | {len(kk)} | {eur(med([na(r)['winst_eur'] for r in kk]))} |"
                     f" {eur(med([na(r)['diepte_eur'] for r in kk]), 0)} |"
                     f" {(getal(med([r['hoog'].get('duur_100_s', 0) for r in kk]), 0) + ' s') if kk else '-'} |"
                     f" {eur(sum(na(r)['winst_eur'] for r in kk))} |")
    u.append("")

    # ----- beste driehoeken per beurs
    u += ["## Beste driehoeken per beurs (echt, bedragen na 3 seconden)", ""]
    leeg = True
    for b in beurzen:
        g = collections.defaultdict(list)
        for r in echte:
            if r["beurs"] == b:
                g[r["driehoek"]].append(r)
        if not g:
            continue
        leeg = False
        u += [f"**{b}** ({status.get(b)})", "",
              "| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur met €100 diepte | Kosten per stap |",
              "|---|---|---|---|---|---|---|"]
        for d, lijst in sorted(g.items(), key=lambda kv: (-len(kv[1]), -sum(na(r)["winst_eur"] for r in kv[1])))[:5]:
            u.append(f"| {d} | {len(lijst)} | {eur(med([na(r)['winst_eur'] for r in lijst]))} |"
                     f" {eur(max(na(r)['winst_eur'] for r in lijst))} |"
                     f" {eur(med([na(r)['diepte_eur'] for r in lijst]), 0)} |"
                     f" {getal(med([r['hoog'].get('duur_100_s', 0) for r in lijst]), 0)} s |"
                     f" {' + '.join(pct(100 * k, 2) for k in lijst[0]['kosten'])} |")
        u.append("")
    if leeg:
        u += ["Nog geen echte driehoeken gezien.", ""]
    bijna = sorted((r for r in rs if r.get("hoog") and not echt(r)), key=lambda r: -r["hoog"].get("winst_eur", 0))[:8]
    if bijna:
        u += ["Grootste driehoeken die **niet** echt waren (te kort, te dun, te weinig winst of verdacht). Bedragen"
              " van het beste moment:", "",
              "| Beurs | Driehoek | Winst | Diepte | Duur | Na 3 s nog €100 diepte | Verdacht |",
              "|---|---|---|---|---|---|---|"]
        for r in bijna:
            h = r["hoog"]
            u.append(f"| {r['beurs']} | {r['driehoek']} | {eur(h.get('winst_eur'))} | {eur(h.get('diepte_eur'), 0)} |"
                     f" {round(h.get('duur_s', 0))} s | {'ja' if na(r) else 'nee'} | {'ja' if r.get('verdacht') else 'nee'} |")
        u.append("")

    # ----- kleine inleg
    u += ["## Kan een kleine inleg meedoen? (€100, €150, €200)", "",
          "Minimale ordergrootte per paar uit de openbare API van elke beurs (aantal munten en bedrag in de quote;"
          " Bitget: waarde in USDT). Per beurs: hoeveel driehoeken je met dat bedrag kunt rondmaken zonder dat een"
          " van de drie orders onder het minimum valt (tegen de beste prijzen, GEZIEN). Het kleinste bedrag dat we"
          " toetsen is €10; \"≤ €10\" betekent dus €10 of minder. Het aantal munten wordt per order naar beneden"
          " afgerond op de stapgrootte van de beurs (uit de API), en bij Bitvavo rekenen we per euro-order €0,01 extra"
          " (Bitvavo rondt de kosten naar boven af op de cent).", "",
          "| Beurs | Status | Driehoeken | Met EUR | Mediaan minimale inleg | Mogelijk met €100 | €150 | €200 | Met EUR en €100 |",
          "|---|---|---|---|---|---|---|---|---|"]
    for b in beurzen:
        m = (info.get(b) or {}).get("min_inleg")
        if not m:
            u.append(f"| {b} | {status.get(b) or '-'} | - | - | nog niet gemeten | - | - | - | - |")
            continue
        md = m.get("mediaan_eur")
        u.append(f"| {b} | {status.get(b) or '-'} | {m['driehoeken']} | {m.get('met_eur', '-')} |"
                 f" {('≤ €10' if md is not None and md <= 10 else eur(md, 0))} |"
                 + " |".join(f" {m.get(f'tot_{k}', '-')}" for k in KLEIN) + f" | {m.get('met_eur_tot_100', '-')} |")
    kl = [g for g in kansen(echte) if wb(beste(g, 100), 100) > 0]
    u += ["", f"Van de {len(kansen(echte))} echte kansen konden er {len(kl)} met €100 (minimale ordergrootte gehaald"
              " op alle drie de orders, winst na 3 seconden).", ""]

    # ----- opschaling
    u += ["## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)", "",
          "Per echte kans nemen we de winst die je bij die inleg na 3 seconden nog had kunnen maken (minder inleggen"
          " mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per gemeten"
          " dag en dan maal 30 voor een maand.", "",
          "Elk getal staat er twee keer: **samengevoegd** (ondergrens: driehoeken die op hetzelfde moment, binnen"
          f" {SAMEN_S} seconden na hun bevestiging, hetzelfde niet-hoofdpaar gebruiken, tellen als één kans; een paar"
          " van twee hoofdmunten zoals BTC/EUR of BTCUSDT telt daarbij niet, en er wordt niet doorgeketend) en"
          " **los** (bovengrens: elke driehoek apart).", "",
          "| Soort | Inleg | Kansen per dag (samengevoegd / los) | Winst per dag (samengevoegd / los) | Per maand (GOK, samengevoegd / los) | Alleen de beste beurs, per maand (GOK, samengevoegd) |",
          "|---|---|---|---|---|---|"]
    for s, n in SOORTEN:
        groepen, losse = kansen(van(echte, s)), los(van(echte, s))
        for inleg in INLEGGEN:
            w, per_b = opgeteld(groepen, inleg)
            wl, _ = opgeteld(losse, inleg)
            # met weinig geld staat alles op één beurs: ook de beste enkele beurs (achteraf gekozen)
            bb, bw = per_b.most_common(1)[0] if per_b else ("-", 0)
            u.append(f"| {n} | {eur(inleg, 0)} | {getal(len(groepen) / gem_dagen)} / {getal(len(losse) / gem_dagen)} |"
                     f" {eur(w / gem_dagen)} / {eur(wl / gem_dagen)} | {eur(30 * w / gem_dagen)} /"
                     f" {eur(30 * wl / gem_dagen)} | {bb}: {eur(30 * bw / gem_dagen)} |")
    u += ["", "Waarom dit te rooskleurig is (GOK):", "",
          "- Het is een **bovengrens**: je pakt elke kans, op elke beurs tegelijk, met het geld al op die beurs."
          " Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf"
          " gekozen, dus ook te rooskleurig).",
          "- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf"
          " pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap"
          " net weg zijn (dan zit je met een munt die je niet wilde, en verlies).",
          "- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.",
          "- De EU-versie van de beurs kan minder paren hebben dan de wereldwijde API die we meten.", "",
          "Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van"
          " taker, de 0%-paren van OKX die we niet konden ophalen, Bitstamp gratis onder $1.000 volume per 30 dagen)"
          " en sneller meten dan elke paar seconden laten meer zien.", ""]
    onzeker = [r for r in rs if not r.get("zeker") and echt(r, "laag")]
    if onzeker:
        u += [f"Met de lage kosten (Bitvavo B, C, D = 0%) zijn {len(onzeker)} driehoeken echt; dat is een bovengrens"
              " zolang Bitvavo geen getal noemt.", ""]
    u += ["Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map"
          " `driehoek/`. Kosten per stap en hun bron: README.md."]
    return "\n".join(u) + "\n"


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--met-proef"]
    print(maak(args[0] if args else ".", "--met-proef" in sys.argv), end="")
