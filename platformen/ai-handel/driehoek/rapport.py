#!/usr/bin/env python3
"""Rapport van de driehoek-meter.

Gebruik:  python3 rapport.py <map met data> [--met-proef]   (bijv. een checkout van de tak ai-handel-data, map driehoek/)
Leest alle */*/driehoeken.jsonl en stand.jsonl daaronder en schrijft het rapport als Markdown naar stdout.
Proefruns (map eindigt op -proef) lopen gelijk met de vaste run en tellen dus niet mee, tenzij --met-proef.

Een ECHTE driehoek (alles moet waar zijn), gerekend met de kosten "hoog" (zie ontwerp.md):
  1. na drie keer takerkosten blijft er winst over op het orderboek (niet alleen tegen de beste prijs);
  2. er gaat minstens MIN_DIEPTE euro met winst doorheen;
  3. hij bleef minstens MIN_DUUR seconden staan (dus minstens twee metingen na elkaar);
  4. niet verdacht (meer dan 5% winst per rondje is bijna altijd een dode markt of foute ticker).
MiCA (de beurs of een EU-dochter heeft een vergunning in het ESMA-register) en grijs staan apart.
Elk cijfer is GEZIEN (uit onze eigen metingen) of GOK (een aanname, met reden).
"""
import collections
import glob
import json
import os
import statistics
import sys

MIN_DIEPTE = 100
MIN_DUUR = 3
INLEGGEN = (100, 150, 200, 2000, 5000)
KLEIN = (100, 150, 200)
STAND_S = 300
VERGUND = {"MiCA", "MiCA-dochter"}
SOORTEN = (("alle", "Alle beurzen"), ("vergund", "MiCA (ook via EU-dochter)"), ("grijs", "Grijs"))


def soort(r):
    return "vergund" if r.get("status") in VERGUND else "grijs"


def van(rs, s):
    return rs if s == "alle" else [r for r in rs if soort(r) == s]


def echt(r, scen="hoog"):
    o = r.get(scen)
    return bool(o) and o.get("winst_eur", 0) > 0 and o.get("diepte_eur", 0) >= MIN_DIEPTE \
        and o.get("duur_s", 0) >= MIN_DUUR and not r.get("verdacht")


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


def dag(r):
    return (r.get("hoog") or r.get("laag") or {}).get("begin", r.get("begin", ""))[:10]


def uren(stand, beurs=None):
    return sum(1 for s in stand if beurs is None or s.get("beurs") == beurs) * STAND_S / 3600


def maak(map_, met_proef=False):
    rs, stand = lees(map_, met_proef)
    info = lees_beurzen(map_, met_proef)
    echte = [r for r in rs if echt(r)]
    beurzen = sorted({s["beurs"] for s in stand} | {r["beurs"] for r in rs})
    status = {s["beurs"]: s.get("status") for s in stand}
    status.update({r["beurs"]: r.get("status") for r in rs})
    dagen = sorted({dag(r) for r in rs} | {s.get("t", "")[:10] for s in stand} - {""})
    u = [f"# Driehoek-meter: rapport", "",
         f"Data: {len(rs)} driehoeken met winst op het boek gezien (ook kleine en korte), {len(dagen)} dag(en)"
         f" ({dagen[0] if dagen else '-'} tot {dagen[-1] if dagen else '-'}). Gemeten: ±{str(round(uren(stand) / max(len(beurzen), 1), 1)).replace('.', ',')}"
         f" uur per beurs (GEZIEN, uit stand.jsonl).{' Proefruns tellen mee.' if met_proef else ''}", "",
         "**Lees dit eerst.** Wij meten elke 3 tot 5 seconden met de openbare API. Snelle partijen (bots naast de"
         " server van de beurs) pakken een winstgevende driehoek meestal binnen milliseconden. Wat wij zien, is wat er"
         " na hen overbleef: driehoeken die korter stonden dan onze ronde zien we vaak niet, en wat wij wel zien, kan"
         " jij alleen pakken als je sneller bent dan wie hem nu laat liggen. De sommen onderaan zijn GOK.", "",
         f"Een **echte driehoek**: winst na drie keer takerkosten op het orderboek, minstens {eur(MIN_DIEPTE, 0)} diepte,"
         f" minstens {MIN_DUUR} seconden blijven staan (twee metingen na elkaar), niet meer dan 5% winst (verdacht).", ""]

    # ----- dekking per beurs
    u += ["## Per beurs: hoe gemeten en hoe dicht bij winst", "",
          "Beste marge = per ronde de beste driehoek tegen de beste prijzen na kosten (mediaan en hoogste over alle"
          " rondes). Negatief = zelfs de beste driehoek verloor geld. Kandidaten = driehoeken die met de beste prijzen"
          " winst gaven; daarvan haalt hij de orderboeken op (bekeken), tenzij het budget van die ronde op was"
          " (overgeslagen) of de koersen sinds de vorige controle niet veranderden (zelfde). Een positieve beste marge"
          " is nog geen winst: de bulk-ticker kan achterlopen of er ligt maar een paar cent op die prijs; het"
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
                 f" {str(round(uren(stand, b), 1)).replace('.', ',')} | {som('rondes')} | {som('fouten')} ({som('te_veel')}) | {pct(med(bm))} |"
                 f" {pct(max(bx) if bx else None)} | {som('kandidaten')} | {som('bekeken')} | {som('overgeslagen')} |"
                 f" {som('zelfde')} | {som('boek_winst')} | {sum(1 for r in echte if r['beurs'] == b)} |")
    over = sum(s.get("overgeslagen") or 0 for s in stand)
    kand = sum(s.get("kandidaten") or 0 for s in stand)
    if kand and over / kand > 0.05:
        u += ["", f"Let op: {over} van {kand} kandidaten ({100 * over / kand:.0f}%) zijn overgeslagen omdat het budget"
                  " van de ronde op was. De aantallen hieronder zijn dan een **ondergrens**."]
    u.append("")

    # ----- trechter
    u += ["## Trechter", "", "| Stap | " + " | ".join(n for _, n in SOORTEN) + " |", "|---|---|---|---|"]
    stappen = [
        ("winst op het boek, met de lage kosten (bovengrens)", lambda r: bool(r.get("laag"))),
        ("winst op het boek, met de gewone kosten", lambda r: bool(r.get("hoog"))),
        (f"en minstens {eur(MIN_DIEPTE, 0)} diepte", lambda r: bool(r.get("hoog")) and r["hoog"]["diepte_eur"] >= MIN_DIEPTE),
        (f"en minstens {MIN_DUUR} s blijven staan", lambda r: bool(r.get("hoog")) and r["hoog"]["diepte_eur"] >= MIN_DIEPTE
         and r["hoog"].get("duur_s", 0) >= MIN_DUUR),
        ("en niet verdacht = **echt**", echt),
    ]
    for naam, f in stappen:
        u.append(f"| {naam} | " + " | ".join(str(sum(1 for r in van(rs, s) if f(r))) for s, _ in SOORTEN) + " |")
    u += ["", "De lage kosten verschillen alleen bij Bitvavo (categorie B, C en D: USDC- en stablecoinparen; Bitvavo"
              " noemt ze lager dan 0,25% maar geeft geen getal, dus laag = 0%, GOK). Overal elders is laag gelijk aan"
              " gewoon.", ""]

    # ----- per dag
    u += ["## Per dag (echte driehoeken)", "",
          "| Dag | Soort | Aantal | Mediane winst per keer | Mediane diepte | Mediane duur | Totale winst (beste moment, volle diepte) |",
          "|---|---|---|---|---|---|---|"]
    for d in dagen + ["totaal"]:
        for s, n in SOORTEN:
            g = [r for r in van(echte, s) if d == "totaal" or dag(r) == d]
            u.append(f"| {d} | {n} | {len(g)} | {eur(med([r['winst_mediaan_eur'] for r in g]))} |"
                     f" {eur(med([r['hoog']['diepte_eur'] for r in g]), 0)} |"
                     f" {(str(round(med([r['hoog']['duur_s'] for r in g]))) + ' s') if g else '-'} |"
                     f" {eur(sum(r['hoog']['winst_eur'] for r in g))} |")
    u.append("")

    # ----- beste driehoeken per beurs
    u += ["## Beste driehoeken per beurs (echt)", ""]
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
              "| Driehoek | Keren | Mediane winst | Hoogste winst | Mediane diepte | Mediane duur | Kosten per stap |",
              "|---|---|---|---|---|---|---|"]
        for d, lijst in sorted(g.items(), key=lambda kv: (-len(kv[1]), -sum(r["hoog"]["winst_eur"] for r in kv[1])))[:5]:
            u.append(f"| {d} | {len(lijst)} | {eur(med([r['winst_mediaan_eur'] for r in lijst]))} |"
                     f" {eur(max(r['hoog']['winst_eur'] for r in lijst))} |"
                     f" {eur(med([r['hoog']['diepte_eur'] for r in lijst]), 0)} |"
                     f" {round(med([r['hoog']['duur_s'] for r in lijst]))} s |"
                     f" {' + '.join(pct(100 * k, 2) for k in lijst[0]['kosten'])} |")
        u.append("")
    if leeg:
        u += ["Nog geen echte driehoeken gezien.", ""]
    bijna = sorted((r for r in rs if r.get("hoog") and not echt(r)), key=lambda r: -r["hoog"]["winst_eur"])[:8]
    if bijna:
        u += ["Grootste driehoeken die **niet** echt waren (te kort, te dun of verdacht):", "",
              "| Beurs | Driehoek | Winst | Diepte | Duur | Verdacht |", "|---|---|---|---|---|---|"]
        for r in bijna:
            h = r["hoog"]
            u.append(f"| {r['beurs']} | {r['driehoek']} | {eur(h['winst_eur'])} | {eur(h['diepte_eur'], 0)} |"
                     f" {h.get('duur_s', 0)} s | {'ja' if r.get('verdacht') else 'nee'} |")
        u.append("")

    # ----- kleine inleg
    u += ["## Kan een kleine inleg meedoen? (€100, €150, €200)", "",
          "Minimale ordergrootte per paar uit de openbare API van elke beurs (aantal munten en bedrag in de quote;"
          " Bitget: waarde in USDT). Per beurs: hoeveel driehoeken je met dat bedrag kunt rondmaken zonder dat een"
          " van de drie orders onder het minimum valt (tegen de beste prijzen, GEZIEN). Het kleinste bedrag dat we"
          " toetsen is €10; \"≤ €10\" betekent dus €10 of minder. Afronding op de stapgrootte van de beurs rekenen we"
          " niet mee (bij €100 een paar cent, GOK).", "",
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
    kl = [r for r in echte if (r["hoog"].get("min_inleg_eur") or 0) <= 100]
    u += ["", f"Van de {len(echte)} echte driehoeken konden er {len(kl)} met €100 of minder (minimale ordergrootte"
              " gehaald op alle drie stappen).", ""]

    # ----- opschaling
    u += ["## Opschaling naar €100, €150, €200, €2.000 en €5.000 inleg (GOK)", "",
          "Per echte driehoek nemen we de winst die je bij die inleg had kunnen maken op het beste moment (minder"
          " inleggen mag als het boek dunner is; alleen bedragen die de minimale ordergrootte halen). Opgeteld per"
          " gemeten dag en dan maal 30 voor een maand.", "",
          "| Soort | Inleg | Echte driehoeken per dag | Winst per dag | Per maand (GOK) | Alleen de beste beurs, per maand (GOK) |",
          "|---|---|---|---|---|---|"]
    gem_dagen = max(uren(stand) / max(len(beurzen), 1) / 24, 1e-9)
    wb = lambda r, inleg: (r["hoog"].get("winst_bij") or {}).get(str(inleg), 0)
    for s, n in SOORTEN:
        g = van(echte, s)
        for inleg in INLEGGEN:
            w = sum(wb(r, inleg) for r in g)
            # met weinig geld staat alles op één beurs: ook de beste enkele beurs (achteraf gekozen)
            per_b = collections.Counter()
            for r in g:
                per_b[r["beurs"]] += wb(r, inleg)
            bb, bw = per_b.most_common(1)[0] if per_b else ("-", 0)
            u.append(f"| {n} | {eur(inleg, 0)} | {str(round(len(g) / gem_dagen, 1)).replace('.', ',')} |"
                     f" {eur(w / gem_dagen)} | {eur(30 * w / gem_dagen)} | {bb}: {eur(30 * bw / gem_dagen)} |")
    u += ["", "Waarom dit te rooskleurig is (GOK):",
          "- Het is een **bovengrens**: je pakt elke driehoek, op elke beurs tegelijk, met het geld al op die beurs."
          " Met weinig geld staat alles op één beurs; de laatste kolom neemt alleen de beste beurs (achteraf"
          " gekozen, dus ook te rooskleurig).",
          "- Snelle partijen zitten er in milliseconden bovenop. Wat wij na seconden nog zien, is het restje. Ga je zelf"
          " pakken, dan concurreer je met hen en met iedereen die het restje ook ziet; bij elke poging kan een stap"
          " net weg zijn (dan zit je met een munt die je niet wilde, en verlies).",
          "- Drie orders na elkaar kosten tijd; tussen stap 1 en 3 kan de prijs bewegen.",
          "- Afronding op de stapgrootte en de EU-versie van de beurs (minder paren) rekenen we niet mee.",
          "Waarom het te somber kan zijn: lagere kosten (meer handelsvolume, eigen beurs-token, maker in plaats van"
          " taker) en sneller meten dan elke paar seconden laten meer zien.", ""]
    onzeker = [r for r in rs if not r.get("zeker") and echt(r, "laag")]
    if onzeker:
        u += [f"Met de lage kosten (Bitvavo B, C, D = 0%) komen er {len(onzeker)} echte driehoeken bij of blijven ze"
              " echt; dat is een bovengrens zolang Bitvavo geen getal noemt.", ""]
    u += ["Bron van alle aantallen en bedragen: eigen metingen (GEZIEN), data op de tak `ai-handel-data`, map"
          " `driehoek/`. Kosten per stap en hun bron: README.md."]
    return "\n".join(u) + "\n"


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--met-proef"]
    print(maak(args[0] if args else ".", "--met-proef" in sys.argv), end="")
