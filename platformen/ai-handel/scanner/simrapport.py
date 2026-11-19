"""Het blok "Wat houd je echt over?" in het rapport: draait simulatie.Sim per beurspaar en inleg en zet de uitkomst
in Markdown, met de andere keuzes (schuifdrempel, kostengrens, minder munten) en de aannames.
Losgehaald uit simulatie.py (keuring, kan-punt: onder de ±400 regels).
"""
import collections

from simulatie import (DREMPEL, HEROPEN_S, INLEGGEN, MAX_KOSTEN_DEEL, MIN_ORDER_EUR, MUNT_REIS_S, QUOTE_MIN, Sim,
                       bruto_bij, dag, paren, quote_opname, ts)

VOORKEUR = ("bitvavo", "kucoin", "gate", "kraken")   # waar we de koers voor het koerseffect het liefst vandaan halen


def _eur(x):
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def meet_venster(stand, echte):
    """Begin en eind van de meting (eerste en laatste standregel), en gemeten uren per dag (één regel per ±5 min)."""
    ts_ = sorted(ts(x["t"]) for rij in stand for x in rij if x.get("t"))
    uren = collections.Counter()
    for t in ts_:
        uren[dag(t)] += 5 / 60
    if not ts_:
        ts_ = sorted([ts(r["begin"]) for r in echte] + [ts(r["eind"]) for r in echte])
    return ts_[0], ts_[-1], uren


def varianten(alle_paren, vergund, koers, t0, t1, minima, inleggen=(150, 2000)):
    """Wat doet een andere schuifdrempel, een andere kostengrens voor terugschuiven, of minder munten met meer voorraad
    per munt? Voor het MiCA-paar met de meeste bruto winst (keuringen). Alleen netto handel: het koerseffect is hier
    geen maat."""
    if not vergund:
        return []
    p = max(vergund, key=lambda p: sum(bruto_bij(r, 1000) for r in alle_paren[p]))
    ks = alle_paren[p]
    per_munt = collections.Counter()
    for r in ks:
        per_munt[r["munt"]] += bruto_bij(r, 1000)
    top2 = [m for m, _ in per_munt.most_common(2)]
    uit = [f"### Andere keuzes bij {p[0]} - {p[1]} (netto handel, alle dagen samen; GOK)", "",
           "| Keuze | Inleg | Kansen | Gemist | Bruto winst | Kosten terugschuiven | Netto handel |",
           "|---|---|---|---|---|---|---|"]
    std = f"schuifdrempel {DREMPEL:.0%}, kostengrens {MAX_KOSTEN_DEEL:.0%}"
    keuzes = [(f"standaard ({std})", ks, DREMPEL, MAX_KOSTEN_DEEL)]
    keuzes += [(f"schuifdrempel {d:.0%}", ks, d, MAX_KOSTEN_DEEL) for d in (0.10, 0.40)]
    keuzes += [(f"kostengrens {k:.0%} (achteraf vergeleken)", ks, DREMPEL, k) for k in (0.02, 0.05)]
    keuzes.append((f"alleen {' en '.join(top2)} (meer voorraad per munt, achteraf gekozen)",
                   [r for r in ks if r["munt"] in top2], DREMPEL, MAX_KOSTEN_DEEL))
    for naam, lijst, d, k in keuzes:
        for inleg in inleggen:
            c = collections.Counter()
            for dg in Sim(lijst, inleg, p, koers, t0, t1, minima, d, k).draai().dagen().values():
                c.update({k: dg[k] for k in ("kansen", "gemist", "bruto", "kosten", "handel")})
            uit.append(f"| {naam} | {_eur(inleg)} | {c['kansen']} | {c['gemist']} | {_eur(c['bruto'])} | "
                       f"{_eur(c['kosten'])} | **{_eur(c['handel'])}** |")
    return uit + ["", f"Kostengrens: terugschuiven mag alleen als de opnamekosten hooguit dat deel van het bedrag zijn. "
                  f"De standaard van {MAX_KOSTEN_DEEL:.0%} is **achteraf** gekozen, nadat bleek dat bij 5% de kosten de "
                  "winst opaten; de rijen met 2% en 5% laten zien hoeveel de uitkomst van die ene regel afhangt. "
                  "Bij \"alleen ...\" tellen de kansen in andere munten niet mee (je hebt die munten dan niet).", ""]


def blok(echte, stand, mica, koersbron=None, inleggen=INLEGGEN, grijs_top=5, minima=None):
    """Markdown-regels voor het rapport. echte: alle echte kansen (niet samengevoegd: elk paar is los).
    koersbron(bronnen, van, tot) -> koers(munt, t); None = geen koersen ophalen (koerseffect onbekend)."""
    uit = ["## Wat houd je echt over? Voorraad op twee beurzen (simulatie)", "",
           "Per beurspaar: geld en munten op beide beurzen, elke echte kans uitgevoerd tegen het boek zoals gemeten "
           "(niet meer dan de ruimte op het boek en niet meer dan de voorraad op die beurs), terugschuiven als een "
           "kant leeg dreigt te raken (met opnamekosten en tijd onderweg), en het koerseffect van de aangehouden "
           "munten apart. Netto = bruto min kosten terugschuiven plus koerseffect. **Gemeten** (GEZIEN): de kansen, "
           "het boek en de koersen; **de rest is een rekenmodel** (GOK, aannames onder de tabel). Geen advies.", ""]
    if not echte:
        return uit + ["Nog geen echte kansen om mee te rekenen.", ""]
    t0, t1, uren = meet_venster(stand, echte)
    kop, bij150, n_dagen, scheef = len(uit), [], 0, False
    alle_paren = paren(echte)
    vergund = sorted(p for p in alle_paren if p[0] in mica and p[1] in mica)
    grijs = sorted((p for p in alle_paren if p not in vergund),
                   key=lambda p: -sum(bruto_bij(r, inleggen[-1] / 4) for r in alle_paren[p]))[:grijs_top]
    koers = None
    if koersbron:
        bronnen = {}
        for p in vergund + grijs:
            for r in alle_paren[p]:
                # eerst de beurzen van het paar, dan elke andere beurs met candles (keuring S5)
                lijst = sorted(VOORKEUR, key=lambda b: (b not in p, VOORKEUR.index(b)))
                bronnen.setdefault(r["munt"], (r["quote"], lijst))
        koers = koersbron(bronnen, t0, t1)
    for titel, lijst in (("Alleen MiCA-beurzen (alle paren met echte kansen)", vergund),
                         (f"Met minstens één grijze beurs (de {grijs_top} paren met de meeste bruto winst)", grijs)):
        uit += [f"### {titel}", ""]
        if not lijst:
            uit += ["Geen echte kansen op zo'n paar.", ""]
            continue
        uit += ["| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | "
                "Bruto winst | Kosten terugschuiven | **Netto handel (bruto min kosten)** | Rendement handel | "
                "Koerseffect voorraad | Netto met koerseffect | Rendement met koerseffect |", "|---" * 14 + "|"]
        notities = []
        for p in lijst:
            for inleg in inleggen:
                s = Sim(alle_paren[p], inleg, p, koers, t0, t1, minima).draai()
                if inleg == 150 and lijst is vergund:
                    dg = s.dagen().values()
                    n_dagen = max(n_dagen, len(dg))
                    scheef = scheef or s.scheef()
                    bij150.append(f"{_eur(sum(c['handel'] for c in dg) / len(dg))} per dag op {p[0]} - {p[1]}"
                                  + (f" (koerseffect erbovenop {_eur(sum(c['koers'] for c in dg) / len(dg))})"
                                     if s.koers_bekend else " (koerseffect onbekend)"))
                for d, c in s.dagen().items():
                    kb = s.koers_bekend
                    rend = f"{c['rendement'] * 100:.2f}%" if kb else "onbekend*"
                    uit.append(f"| {p[0]} - {p[1]} | {_eur(inleg)} | {d} | {uren.get(d, 0):.1f} u | {c['kansen']} | "
                               f"{c['gemist']} | {c['beperkt']} | {_eur(c['bruto'])} | {_eur(c['kosten'])} "
                               f"({c['schuif']}x) | **{_eur(c['handel'])}** | {c['rendement_handel'] * 100:.2f}% | "
                               f"{_eur(c['koers']) if kb else 'onbekend'} | {_eur(c['netto']) if kb else 'onbekend*'} | "
                               f"{rend} |")
                tot = s.dagen().values()
                notities.append(f"- {p[0]} - {p[1]}, {_eur(inleg)}: munten {', '.join(s.munten)}; bruto zonder "
                                f"voorraadgrens zou {_eur(sum(c['vol'] for c in tot))} zijn, met voorraad "
                                f"{_eur(sum(c['bruto'] for c in tot))} (GEZIEN boek, GOK model).")
        uit += [""] + notities + [""]
    if bij150:
        dagen = ("één gemeten dag die begint" if n_dagen == 1 else
                 f"gemiddeld over {n_dagen} gemeten dagen achter elkaar; de eerste begint")
        uit[kop:kop] = [f"**Met €150: netto {', '.join(bij150)} (GOK: netto handel, rekenmodel op ±"
                        f"{sum(uren.values()) / max(len(uren), 1):.1f} uur meting per dag, alleen MiCA).** "
                        f"\"Per dag\" is hier {dagen} met een gelijk verdeelde voorraad"
                        + ("; aan het eind staat de voorraad scheef, dus een volgende dag levert waarschijnlijk minder "
                           "op, tenzij kansen de andere kant op hem terugbrengen (GOK)." if scheef else ".") , ""]
    uit += varianten(alle_paren, vergund, koers, t0, t1, minima)
    uit.append("Dag en Gemeten: de kansen komen alleen uit de uren dat de scanner mat (GEZIEN); het koerseffect loopt "
               "door over de hele tijd van de eerste tot de laatste meting. Rendement = netto gedeeld door de inleg, "
               "voor die dag. * = koers niet op te halen, koerseffect onbekend (niet als 0 bedoeld). **Het koerseffect is "
               "het risico van de voorraad, geen opbrengst van de methode:** bij één munt over een paar uur is het "
               "vooral toeval. Kijk voor wat de methode oplevert naar Netto handel.")
    uit += ["", "**Aannames:**", ""] + [f"- {a}" for a in AANNAMES]
    gezien = sorted({(b, q) for p in vergund + grijs for b in p for q in {r["quote"] for r in alle_paren[p]}})
    uit += ["- Geld terugschuiven per beurs: " + "; ".join(
        f"{b} {q}: {quote_opname(b, q)[0]:g} {q}, {quote_opname(b, q)[2]}"
        + (f", minimum {QUOTE_MIN[(b, q)][0]:g} {q} ({QUOTE_MIN[(b, q)][1]})" if (b, q) in QUOTE_MIN else "")
        for b, q in gezien) + ".", ""]
    return uit


AANNAMES = [
    "Winst per kans: de mediaan van wat de scanner op het boek mat bij €100, €500, €1.000, €2.500 en de volle ruimte "
    "(GEZIEN), lineair daartussen (GOK). Uitgevoerd 2 minuten na het begin (dan pas weet je dat hij meetelt), één keer per "
    f"kans; gaat dezelfde kans binnen {HEROPEN_S // 60} minuten weer open, dan is het deel van het boek dat je al "
    "gebruikte op (GOK).",
    "Inleg: de helft geld (de quote van de kansen), de helft munten, verdeeld over de munten die op dat paar echte "
    "kansen hadden, en alles half op elke beurs (GOK). Die munten zijn **achteraf** gekozen; vooraf weet je dat niet.",
    f"Terugschuiven zodra een kant onder {DREMPEL:.0%} van zijn beginvoorraad komt: de helft van het verschil gaat "
    f"terug, alleen als de opnamekosten hooguit {MAX_KOSTEN_DEEL:.0%} van het bedrag zijn (GOK, eigen regel). Die "
    f"{MAX_KOSTEN_DEEL:.0%} is **achteraf** gekozen: eerst stond hier 5%, en pas nadat bleek dat de kosten bij 5% de "
    "winst opaten, is het 1% geworden (reden: een kans levert ±0,3 tot 1% bruto). Zie de rijen kostengrens 2% en 5% "
    "bij Andere keuzes.",
    "Opnamekosten van de munt: wat de scanner bij die beurs zag (GEZIEN uit de API van de beurs; bij Kraken en Gate "
    "geschat uit andere beurzen, GOK). Geld: zie de tabel hieronder.",
    f"Een munt is na {MUNT_REIS_S // 60} minuten op de andere beurs (GOK). Zolang iets onderweg is, telt het niet "
    "als voorraad; kansen die daardoor niet of kleiner konden, staan als gemist of beperkt.",
    "Minimale order (in euro en in munten) en minimale opname van de munt per beurs en munt: uit de openbare API van "
    "Bitvavo, Kraken, KuCoin en Gate (GEZIEN, opgehaald bij het maken van het rapport). Een kans onder het minimum "
    f"telt als gemist; een terugschuif onder het opnameminimum wordt opgehoogd tot het minimum. Andere beurzen of geen "
    f"antwoord: minimale order {MIN_ORDER_EUR} euro (GOK). Kraken geeft zijn opnameminimum niet openbaar: daar geen "
    "minimum (GOK). USDT telt tegen de koers van het moment van de kans; de koers USDT-EUR zelf beweegt niet mee (GOK).",
    "Koerseffect: slotkoers per 15 minuten (of per uur) uit de openbare candles van Bitvavo, Kraken, KuCoin of Gate "
    "(GEZIEN), over alle aangehouden munten, ook als de scanner tussen twee runs even niet mat.",
    "Niet meegeteld: andere bots die dezelfde kans pakken, dat het boek zich na jouw order aanvult (dan kan het "
    "vaker), belasting, en dat de EU-versie van een beurs minder munten kan hebben dan de API die we meten.",
]
