#!/usr/bin/env python3
"""Rapport van de kansenradar.

Gebruik:  python3 radar_rapport.py <map met data> [--met-proef]   (bijv. de tak ai-handel-data, map radar/)
Leest alle bestanden van de radar onder de map en schrijft het rapport als Markdown naar stdout. Proefruns (map
eindigt op -proef) lopen gelijk met de vaste run en tellen niet mee, tenzij --met-proef. Alleen standaardbibliotheek
(draait met python3 -I).

Wat telt (GEZIEN = uit onze metingen, GOK = aanname):
  A en C1 (koop op beurs X, verkoop op beurs Y): winst na takerkosten en één opname van de munt, opnamekosten bekend
     of geschat, opnemen en storten open (bekend), geen netwerk dat aan beide kanten dicht is, geen ander
     contractadres, minstens 2 metingen en minstens €100 winstgevend op het boek.
  B (funding): positieve piek, ingestapt met een spotkoers die bij de perp past (spotstand "ok"), afgerond (niet
     doorgeknipt door het einde van een run). Winst = verrekende funding min 4 x takerkosten, plus of min het
     prijsverschil spot/perp, min één keer overmaken als spot en perp op twee beurzen zitten.
  C2 (los van de basislijn): het boek zit minstens 0,3% naast de mediaan van de laatste 45 dagen en na 2 x
     takerkosten blijft winst over, met minstens €100 op het boek. Geen arbitrage.
Apart (niet in de sommen): data met het oude Kraken-tarief (0,40% in plaats van 0,80%, of 0,40/0,80% op een
stablecoin-paar in plaats van 0,20%), funding-pieken uit de oude code (doorgeknipt, zonder overmaken), C2 zonder
basislijn.

Sommen per inleg: met één pot. Je pakt een moment als je pot vrij is (het vorige moment dat je pakte is voorbij);
starten er twee tegelijk, dan het beste. Zo telt niets dubbel wat met hetzelfde geld niet kan. Kleine inleg (€100,
€150, €200): een moment doet alleen mee als de minimale order- (en bij A, C1 en B overmaak-)bedragen bekend zijn en
eronder liggen.
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
MIN_UREN_WEEK = 3   # korter gemeten: geen som per week
MIN_RUIMTE = 100
# Beurzen met een MiCA-vergunning in het ESMA-register (19 nov 2026), zelfde lijst als ../scanner/README.md.
MICA = {"bitvavo", "kraken", "coinbase", "bitstamp", "okx", "cryptocom", "bybit", "kucoin", "gate", "bingx"}
# Perps: spotvergunning onder MiCA. Of de EU-dochter perps aan Nederlandse particulieren geeft: GOK, zie README.
MICA_PERP = {"okx", "gate", "kucoin", "bingx", "kraken"}
# Stablecoins en fiat voor het Kraken-tarief (0,20% op stablecoin- en FX-paren, anders 0,80%). Gelijk aan radar.
STABIEL = {"USDT", "USDC", "FDUSD", "PYUSD", "USDE", "DAI", "TUSD", "USD1", "RLUSD", "USDG", "USDS", "USDP", "USDQ",
           "EURC", "EURE", "EURI", "EURCV", "EUROP", "EURT", "AEUR", "EURR", "EURQ", "EURAU", "EUR", "USD"}


# ---------- lezen ----------
def lees_jsonl(map_, naam, met_proef):
    uit = []
    for p in sorted(glob.glob(os.path.join(map_, "**", naam), recursive=True)):
        if not met_proef and os.path.dirname(p).endswith("-proef"):
            continue
        with open(p) as fh:
            rij = [json.loads(x) for x in fh if x.strip()]
        uit.append(rij) if naam == "stand.jsonl" else uit.extend(rij)
    return uit


def tijd(s):
    return dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")


def gemeten_uren(stand):
    uren = 0.0
    for rij in stand:
        if rij:
            uren += (tijd(rij[-1]["t"]) - tijd(rij[0]["t"])).total_seconds() / 3600 + 5 / 60
    return uren


def ontdubbel_funding(rs):
    """Een piek die bij een herstart al was opgeslagen en daarna door de volgende run is afgemaakt, kan twee keer
    in de data staan (zelfde perp, munt en begin). Dan telt de regel die het laatst eindigt."""
    beste = {}
    for r in rs:
        k = (r.get("beurs"), r.get("munt"), r.get("begin"))
        if k not in beste or (r.get("eind") or "") > (beste[k].get("eind") or ""):
            beste[k] = r
    return list(beste.values())


# ---------- tarief en soort ----------
def kraken_taker(munt, quote):
    return 0.002 if munt in STABIEL and quote in STABIEL else 0.008


def oud_tarief(r):
    """True als een Kraken-tarief in de regel niet het huidige is (data van vóór de fix van 19 nov)."""
    paren = [(r.get("koop"), r.get("taker_koop"), r.get("munt"), r.get("quote")),
             (r.get("verkoop"), r.get("taker_verkoop"), r.get("munt"), r.get("quote")),
             (r.get("spot"), r.get("taker_spot"), r.get("munt"), r.get("spot_quote")),
             (r.get("beurs") if "taker" in r else None, r.get("taker"), r.get("munt"), r.get("quote"))]
    return any(b == "kraken" and t is not None and abs(t - kraken_taker(m, q)) > 1e-9 for b, t, m, q in paren)


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


def winst(r, inleg):
    if "eerste" in r:
        return (r["eerste"] or {}).get(f"winst{inleg}")
    return r.get(f"winst{inleg}")


def haalbaar(r, inleg, hoek):
    """True/False als de minimale bedragen bekend zijn, None als een ervan onbekend is."""
    if hoek == "B":
        positie = inleg * 2 / 3
        mins = [(r.get("min_spot_eur"), positie), (r.get("min_perp_eur"), positie),
                (r.get("overmaak_min_eur", 0.0), inleg / 3)]    # het onderpand (1/3) gaat naar de perpbeurs
    elif hoek == "C2":
        mins = [(r.get("min_order_eur"), inleg)]
    else:
        mins = [(r.get("min_koop_eur"), inleg), (r.get("min_verkoop_eur"), inleg), (r.get("min_opname_eur"), inleg)]
    if any(m is None for m, _ in mins):
        return None
    return all(m <= grens for m, grens in mins)


def doet_mee(r, inleg, hoek):
    h = haalbaar(r, inleg, hoek)
    return h is True if inleg in KLEIN else h is not False


# ---------- één pot ----------
def begin_van(r):
    return tijd(r.get("instap") or r["begin"])


def pot(rs, inleg, hoek):
    """Wat pak je met één pot van `inleg`? Momenten op volgorde van begin; je pakt er een als de pot vrij is, bij
    gelijke start de beste. De pot zit vast tot het moment voorbij is (bij B tot je uitstapt). Geeft (gepakt, som)."""
    kand = [r for r in rs if doet_mee(r, inleg, hoek) and winst(r, inleg) is not None]
    kand.sort(key=lambda r: (begin_van(r), -winst(r, inleg)))
    vrij, gepakt = None, []
    for r in kand:
        b = begin_van(r)
        if vrij is None or b >= vrij:
            gepakt.append(r)
            vrij = max(tijd(r["eind"]), b + dt.timedelta(seconds=1))
    return gepakt, sum(winst(r, inleg) for r in gepakt)


def max_tegelijk(rs):
    gebeurt = []
    for r in rs:
        b = begin_van(r)
        gebeurt += [(b, 1), (max(tijd(r["eind"]), b + dt.timedelta(seconds=1)), -1)]
    n = hoogst = 0
    for _, d in sorted(gebeurt):
        n += d
        hoogst = max(hoogst, n)
    return hoogst


# ---------- opmaak (komma als decimaalteken) ----------
def getal(x, d=2):
    if x is None:
        return "-"
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def eur(x, d=2):
    if x is None:
        return "-"
    return f"{'-' if x < 0 else ''}€{getal(abs(x), d)}"


def pct(x, d=2):
    return "-" if x is None else f"{getal(x, d)}%"


def duur(s):
    if s is None:
        return "-"
    if s >= 7200:
        return f"{getal(s / 3600, 1)} uur"
    return f"{s / 60:.0f} min" if s >= 60 else f"{s:.0f} s"


def med(w):
    w = [x for x in w if isinstance(x, (int, float))]
    return statistics.median(w) if w else None


def janee(x):
    return {True: "open", False: "dicht"}.get(x, "onbekend")


def tabel_per_dag(rs, soort_fn, titel):
    per = collections.defaultdict(list)
    for r in rs:
        per[(r.get("begin") or "")[:10]].append(r)
    if not per:
        return [f"**{titel}, per dag:** nog geen momenten.", ""]
    uit = [f"**{titel}, per dag**", "", "| Dag | Aantal (alle / MiCA / grijs) | Mediane winst bij €500 | Mediane duur |",
           "|---|---|---|---|"]
    for d in sorted(per):
        x = per[d]
        n_v = sum(1 for r in x if soort_fn(r) == "vergund")
        uit.append(f"| {d} | {len(x)} / {n_v} / {len(x) - n_v} | {eur(med(winst(r, 500) for r in x))} | "
                   f"{duur(med(r.get('duur_s') for r in x))} |")
    return uit + [""]


def tabel_inleg(rs, soort_fn, hoek, uren):
    uit = ["| Inleg | Kan meedoen (alle / MiCA) | Minimum onbekend | Tegelijk open (hoogst) | Met één pot gepakt | "
           "Mediane winst per keer | Winst met één pot | Per week (GOK) |", "|---|---|---|---|---|---|---|---|"]
    for i in INLEG:
        mee = [r for r in rs if doet_mee(r, i, hoek)]
        onb = sum(1 for r in rs if haalbaar(r, i, hoek) is None)
        gepakt, som = pot(rs, i, hoek)
        week = som * 168 / uren if uren >= MIN_UREN_WEEK else None
        n_v = sum(1 for r in mee if soort_fn(r) == "vergund")
        uit.append(f"| {eur(i, 0)} | {len(mee)} / {n_v} | {onb} | {max_tegelijk(mee)} | {len(gepakt)} | "
                   f"{eur(med(winst(r, i) for r in gepakt))} | {eur(som)} | {eur(week)} |")
    uit += ["", "Met één pot: je pakt een moment als je geld vrij is, bij gelijke start het beste. \"Tegelijk open\" "
            "zegt hoeveel potten je nodig had om alles te pakken. Bij €100 tot €200 doet een moment alleen mee als de "
            "minimale bedragen bekend zijn en eronder liggen; vanaf €500 telt onbekend mee (meestal €1 tot €10).", ""]
    return uit


# ---------- rapport ----------
def zin_pot(rs, hoek, inleg=150):
    gepakt, som = pot(rs, inleg, hoek)
    if not gepakt:
        return f"met één pot van €{inleg} had je hier tot nu toe niets kunnen pakken"
    return f"met één pot van €{inleg} had je {len(gepakt)} keer kunnen instappen, samen {eur(som)}"


def rapport(map_, met_proef=False):
    stand = lees_jsonl(map_, "stand.jsonl", met_proef)
    uren = gemeten_uren(stand)
    noteringen = lees_jsonl(map_, "noteringen.jsonl", met_proef)
    a_alle = lees_jsonl(map_, "noteringen-kansen.jsonl", met_proef)
    b_alle = ontdubbel_funding(lees_jsonl(map_, "funding.jsonl", met_proef))
    c1_alle = lees_jsonl(map_, "stable-tussen.jsonl", met_proef)
    c2_alle = lees_jsonl(map_, "stable-afwijking.jsonl", met_proef)

    a_oud = [r for r in a_alle if oud_tarief(r)]
    echt_a = [r for r in a_alle if echt_paar(r) and not oud_tarief(r)]

    b_oudcode = [r for r in b_alle if "spotstand" not in r]
    b_nieuw = [r for r in b_alle if "spotstand" in r]
    b_oud = [r for r in b_nieuw if oud_tarief(r)]
    b_nieuw = [r for r in b_nieuw if not oud_tarief(r)]
    pos = [r for r in b_nieuw if r.get("richting") == "positief"]
    b_ok = [r for r in pos if r.get("spotstand") == "ok" and not r.get("einde_run") and r.get("netto_pct") is not None
            and r.get("overmaak_eur") is not None]
    b_tel = collections.Counter(r.get("spotstand") for r in pos)
    b_gat = [r for r in pos if r.get("einde_run")]
    neg = [r for r in b_nieuw if r.get("richting") == "negatief"]

    c1_oud = [r for r in c1_alle if oud_tarief(r)]
    echt_c1 = [r for r in c1_alle if echt_paar(r) and not oud_tarief(r)]

    c2_oudcode = [r for r in c2_alle if "basis_ratio" not in r]
    c2_nieuw = [r for r in c2_alle if "basis_ratio" in r and not oud_tarief(r)]
    c2_oud = [r for r in c2_alle if "basis_ratio" in r and oud_tarief(r)]
    c2_zonder = [r for r in c2_nieuw if r.get("basis_ratio") is None]
    c2_met = [r for r in c2_nieuw if r.get("basis_ratio") is not None]
    c2_diep = [r for r in c2_met if (r.get("ruimte_eur_max") or 0) >= MIN_RUIMTE]
    c2_ok = [r for r in c2_diep if ((r.get("eerste") or {}).get("na_kosten_pct") or -1) > 0]

    nu = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    apart = len(a_oud) + len(b_oud) + len(b_oudcode) + len(c1_oud) + len(c2_oud) + len(c2_oudcode)
    o = ["# Kansenradar: rapport", "",
         f"Gemaakt {nu}. Gemeten: **{getal(uren, 1)} uur** in {len(stand)} run(s)"
         + (" (met proefruns)" if met_proef else "") + ". Cijfers zijn GEZIEN (eigen metingen uit openbare API's), "
         "behalve waar GOK staat. Uitleg: `platformen/ai-handel/radar/README.md`.", "",
         "## Het antwoord tot nu toe", "",
         f"- **A, nieuwe noteringen:** {len(noteringen)} nieuwe munten gezien, {len(echt_a)} echte prijsverschillen "
         f"daarna; {zin_pot(echt_a, 'A')}.",
         f"- **B, funding-pieken:** {len(b_ok)} pieken afgerond met spot en perp, waarvan "
         f"{sum(1 for r in b_ok if (winst(r, 150) or 0) > 0)} met winst na alle kosten bij €150; "
         f"{zin_pot(b_ok, 'B')} (van €150 gaat €100 in de positie, GOK).",
         f"- **C1, stablecoin tussen beurzen:** {len(echt_c1)} echte momenten; {zin_pot(echt_c1, 'C1')}.",
         f"- **C2, stablecoin naast zijn gewone prijs:** {len(c2_ok)} momenten met winst na kosten; "
         f"{zin_pot(c2_ok, 'C2')}. Dit is geen arbitrage: je wint alleen als de koers terugkomt.",
         "",
         "Alle sommen zijn een **bovengrens (GOK)**: we kijken elke 15 seconden tot 3 minuten, snelle partijen elke "
         "milliseconde. Wat we zien, is vaak al deels weg voor een gewone gebruiker zijn order plaatst."
         + (f" Apart gezet en niet geteld: {apart} regels uit de eerste uren (oude code of het oude Kraken-tarief, "
            "zie onderaan)." if apart else ""), ""]

    # ---- A ----
    o += ["## A. Nieuwe noteringen", "",
          f"Nieuwe munten op een beurs: **{len(noteringen)}** (waarvan "
          f"{sum(1 for n in noteringen if n.get('vlak_na_start'))} bij de eerste vergelijking na de start: die kunnen "
          f"in het gat tussen twee runs genoteerd zijn); {sum(1 for n in noteringen if n.get('elders'))} stonden al "
          f"op een andere beurs met dezelfde quote. Prijsverschillen daarna: {len(a_alle)}, waarvan "
          f"**{len(echt_a)} echt**.", ""]
    if noteringen:
        o += ["| Tijd | Beurs | Munt | Al op | Opnemen / storten op de nieuwe beurs |", "|---|---|---|---|---|"]
        for n in noteringen[-15:]:
            o.append(f"| {n['t'][5:16].replace('T', ' ')} | {n['beurs']}{'' if n['beurs'] in MICA else ' (grijs)'} | "
                     f"{n['munt']}-{n['quote']} | {', '.join(n.get('elders') or []) or '-'} | "
                     f"{janee(n.get('opname'))} / {janee(n.get('storting'))} |")
        o.append("")
    o += tabel_per_dag(echt_a, soort_paar, "Echte momenten A")
    o += tabel_inleg(echt_a, soort_paar, "A", uren)

    # ---- B ----
    o += ["## B. Funding-pieken", "",
          f"Positieve pieken (boven 0,1% per 8 uur, uit onder 0,05% na minstens één verrekening): **{len(b_ok)} "
          f"afgerond en te rekenen**. Verder: spotkoers onbekend {b_tel.get('onbekend', 0)}, andere munt met dezelfde "
          f"naam {b_tel.get('ander ding', 0)}, geen spotmarkt {b_tel.get('geen spotmarkt', 0)}, onderbroken door een "
          f"te lang gat tussen runs {len(b_gat)}; negatieve pieken {len(neg)} (dan moet je spot shorten, dat kan "
          "een particulier meestal niet). Open pieken gaan mee naar de volgende run, dus een piek betaalt maar één "
          "keer de kosten.", "",
          "Som per piek: verrekende funding, min 4 keer takerkosten (spot in en uit, perp in en uit), plus of min het "
          "prijsverschil tussen spot en perp, min één keer overmaken (opname van USDT of USDC) als spot en perp op "
          "twee beurzen zitten. Inleg = 2/3 spot en 1/3 onderpand voor de short bij 2x hefboom (GOK). Bij 2x kan een "
          "sprong van ±50% de short liquideren; dat zit niet in de som.", ""]
    if b_ok:
        o += ["| Begin | Perp | Munt | Spot | Hoogste funding per 8 uur | Ontvangen funding | Kosten | Prijsverschil | "
              "Overmaken | Netto | Winst bij €150 | Duur | Handel per dag |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in sorted(b_ok, key=lambda r: -(winst(r, 150) or -99))[:10]:
            o.append(f"| {r['begin'][5:16].replace('T', ' ')} | {r['beurs']} | {r['munt']} | {r.get('spot')} | "
                     f"{pct(r.get('r8_max_pct'))} | {pct(r.get('ontvangen_pct'))} ({r.get('verrekeningen')} keer) | "
                     f"{pct(r.get('kosten_pct'))} | {pct(r.get('basis_pct'))} | {eur(r.get('overmaak_eur'))} | "
                     f"**{pct(r.get('netto_pct'))}** | {eur(winst(r, 150))} | {duur(r.get('duur_s'))} | "
                     f"${getal((r.get('vol_usd') or 0) / 1e6, 1)} mln |")
        o.append("")
    o += tabel_per_dag(b_ok, soort_funding, "Afgeronde pieken B")
    o += tabel_inleg(b_ok, soort_funding, "B", uren)
    o += ["Vergund bij B: perp- en spotbeurs hebben een MiCA-vergunning voor spot. Of de EU-dochter perps aan "
          "Nederlandse particulieren geeft, is niet nagekeken (GOK, vaak niet of beperkt). De som is lineair in de "
          "inleg (GOK): bij een dunne perp kost een grotere order meer dan de laatste prijs.", ""]

    # ---- C ----
    o += ["## C. Stablecoins", "",
          f"**C1, tussen beurzen** (dezelfde stablecoin goedkoper kopen dan elders verkopen, na alle kosten): "
          f"{len(c1_alle) - len(c1_oud)} momenten, waarvan **{len(echt_c1)} echt**.", ""]
    o += tabel_per_dag(echt_c1, soort_paar, "Echte momenten C1")
    o += tabel_inleg(echt_c1, soort_paar, "C1", uren)
    o += [f"**C2, naast de gewone prijs** (minstens 0,3% naast de basislijn: de mediaan per dag over de laatste 45 "
          f"dagen): {len(c2_met)} momenten met basislijn, waarvan {len(c2_diep)} met minstens €{MIN_RUIMTE} op het "
          f"boek en **{len(c2_ok)} met winst na 2 keer takerkosten** (bij de eerste meting). Zonder basislijn (munt te "
          f"nieuw of geen bron, niet geteld): {len(c2_zonder)}. Geen arbitrage: je wint alleen als de koers naar zijn "
          "gewone prijs terugkomt (GOK).", ""]
    tel = collections.Counter(f"{r['munt']}-{r['quote']} op {r['beurs']} ({r['kant']})" for r in c2_diep)
    if tel:
        o += ["Meest gezien: " + ", ".join(f"{k} {v} keer" for k, v in tel.most_common(8)) + ".", ""]
    o += tabel_per_dag(c2_ok, soort_een, "C2 met winst na kosten")
    o += tabel_inleg(c2_ok, soort_een, "C2", uren)

    o += ["## Apart gezet (niet in de sommen)", "",
          f"- Oude Kraken-tarief (0,40% gerekend waar het 0,80% is, of 0,40/0,80% op een stablecoin-paar waar het "
          f"0,20% is): A {len(a_oud)}, B {len(b_oud)}, C1 {len(c1_oud)}, C2 {len(c2_oud)}.",
          f"- Funding-pieken uit de eerste code (doorgeknipt bij het einde van een run, zonder overmaken): "
          f"{len(b_oudcode)} (waarvan {sum(1 for r in b_oudcode if r.get('richting') == 'positief')} positief), "
          f"waarvan {sum(1 for r in b_oudcode if r.get('einde_run'))} doorgeknipt. Die zijn niet "
          "na te rekenen (de rest van de piek is niet gevolgd) en tellen niet mee.",
          f"- C2 uit de eerste code (gemeten tegen 1 dollar of 1 euro, zonder basislijn; vooral EURQ, die al weken "
          f"rond 0,97 euro staat): {len(c2_oudcode)}.", "",
          "## Hoe eerlijk zijn de sommen", "",
          "- A en C1: de winst bij elke inleg komt uit het echte orderboek op dat moment. Je hebt wel voorraad op "
          "beide beurzen nodig, of je moet overmaken, en dan is het gat vaak weg.",
          "- B: lineair in de inleg, met de vaste kosten van overmaken. Bij €100 tot €200 wegen die zwaar.",
          "- C2: uit het boek, maar een gok op terugkeer naar de gewone prijs.",
          f"- Per week = winst met één pot maal 168 uur gedeeld door de gemeten uren (pas vanaf {MIN_UREN_WEEK} uur). "
          "Na een paar uur is dat een ruwe GOK; na 7 dagen een week aan metingen.", ""]
    return "\n".join(o)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    print(rapport(sys.argv[1], "--met-proef" in sys.argv))


if __name__ == "__main__":
    main()
