"""Voorraad-simulatie: wat houd je echt over als je geld en munten op twee beurzen hebt staan?

Draait op de opgeslagen echte kansen (kansen.jsonl), zonder account en zonder handel. Per beurspaar (beide
richtingen samen):
  - Begin met een inleg, de helft in geld (EUR of USDT, de quote van de kansen) en de helft in munten (verdeeld over
    de munten die op dat paar echte kansen hadden), en alles half op de ene en half op de andere beurs.
  - Elke echte kans wordt op het moment dat hij begon uitgevoerd: kopen op de koopbeurs met geld, tegelijk dezelfde
    hoeveelheid munten verkopen op de verkoopbeurs. Niet meer dan de winstgevende ruimte op het boek (gemeten),
    niet meer dan het geld op de koopbeurs en niet meer dan de munten op de verkoopbeurs. Er gaat bij een kans niets
    over de keten: de opnamekosten van de munt tellen pas bij het terugschuiven.
  - Dreigt een kant leeg te raken (onder DREMPEL van wat er aan het begin per kant stond), dan schuift hij terug:
    de helft van het verschil gaat naar de lege kant, alleen als de opnamekosten hooguit 5% van het bedrag zijn.
    Tijdens het onderweg zijn is dat geld of die munt niet te gebruiken.
  - Het koerseffect is de waardeverandering van de aangehouden munten (op beide beurzen en onderweg), apart gemeld.
Netto = bruto winst min kosten terugschuiven plus koerseffect; dat is precies de eindwaarde min de inleg.

Elk cijfer is GEZIEN (gemeten of uit een API of tarievenpagina) of GOK (een aanname); zie AANNAMES onderaan.
"""
import bisect
import collections
import datetime as dt

DREMPEL = 0.25           # GOK: schuif terug als een kant onder 25% van zijn beginvoorraad komt
MAX_KOSTEN_DEEL = 0.05   # GOK: schuif alleen als de opnamekosten hooguit 5% van het bedrag zijn
MIN_ORDER_EUR = 10       # GOK: kleiner dan dit telt als gemist (minimale ordergrootte verschilt per beurs)
MUNT_REIS_S = 30 * 60    # GOK: een munt is na 30 minuten binnen (bevestigingen plus verwerking door de beurs)

# Opnamekosten en reistijd van het geld (de quote) per beurs: (kosten in de quote, reistijd in seconden, bron).
QUOTE_OPNAME = {
    ("bitvavo", "EUR"): (0.0, 24 * 3600, "kosten GEZIEN (api.bitvavo.com/v2/assets: EUR withdrawalFee 0), "
                                         "tijd GOK (1 werkdag, SEPA)"),
    ("kraken", "EUR"): (1.0, 3600, "kosten GEZIEN (support.kraken.com/articles/360000381846: Instant SEPA, "
                                   "Banking Circle, 1 EUR, near-instant), tijd GOK (1 uur tot het op de andere beurs staat)"),
    ("kucoin", "USDT"): (1.0, 1800, "kosten GEZIEN (api.kucoin.com/api/v3/currencies/USDT: BEP20 1 USDT), tijd GOK"),
}
QUOTE_STANDAARD = {"EUR": (1.0, 24 * 3600), "USD": (1.0, 24 * 3600), "USDT": (1.0, 1800), "USDC": (1.0, 1800)}


def quote_opname(beurs, quote):
    """(kosten in de quote, reistijd s, GEZIEN of GOK met bron)."""
    if (beurs, quote) in QUOTE_OPNAME:
        return QUOTE_OPNAME[(beurs, quote)]
    k, t = QUOTE_STANDAARD.get(quote, (1.0, 24 * 3600))
    return k, t, f"GOK ({k:g} {quote}, {t // 3600 or t // 60} {'uur' if t >= 3600 else 'min'}; niet nagekeken)"


def ts(iso):
    return dt.datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc).timestamp()


def dag(t):
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%d")


def bruto_bij(r, x):
    """Winst bij x euro inzet zonder opnamekosten (die tellen pas bij terugschuiven). Lineair tussen de gemeten
    punten 0, €100, €500, €1.000, €2.500 en de volle ruimte; nooit meer dan de ruimte (GEZIEN punten, GOK ertussen)."""
    ruimte = r.get("ruimte_eur_med") or 0
    o = r.get("opname_eur") or 0
    x = min(x, ruimte)
    if x <= 0:
        return 0.0
    pts = [(0.0, 0.0)]
    for p in (100, 500, 1000, 2500):
        if p < ruimte and r.get(f"winst{p}_med") is not None:
            pts.append((float(p), r[f"winst{p}_med"] + o))
    if r.get("winst_ruimte_med") is not None:
        pts.append((float(ruimte), r["winst_ruimte_med"] + o))
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0) if x1 > x0 else y1
    return pts[-1][1]


def munt_kosten(kansen):
    """Opnamekosten van een munt per beurs in euro: mediaan van wat de scanner zag als die beurs de koopbeurs was
    (GEZIEN uit de API van de beurs, of geschat als opname_bron 'geschat' is). Geen meting op die beurs: dan de
    mediaan over alle beurzen voor die munt (GOK)."""
    per, alle = collections.defaultdict(list), collections.defaultdict(list)
    for r in kansen:
        if r.get("opname_eur") is not None:
            per[(r["koop"], r["munt"])].append(r["opname_eur"])
            alle[r["munt"]].append(r["opname_eur"])
    med = lambda w: sorted(w)[len(w) // 2]
    return {k: med(v) for k, v in per.items()}, {k: med(v) for k, v in alle.items()}


class Sim:
    """Eén beurspaar, één inleg. Geld in euro; munten in 'euro tegen de beginkoers' (r = koers nu / beginkoers)."""

    def __init__(self, kansen, inleg, beurzen, koers=None, t0=None, t1=None):
        self.kansen = sorted(kansen, key=lambda r: r["begin"])
        self.beurzen = beurzen
        self.quotes = sorted({r["quote"] for r in kansen})
        self.munten = sorted({r["munt"] for r in kansen})
        self.koers = koers or (lambda munt, t: None)
        self.t0 = t0 if t0 is not None else ts(self.kansen[0]["begin"])
        self.t1 = t1 if t1 is not None else max(ts(r["eind"]) for r in kansen)
        self.inleg = inleg
        self.eur_q = {q: next((r["eur_per_quote"] for r in reversed(self.kansen)
                               if r["quote"] == q and r.get("eur_per_quote")), 1.0) for q in self.quotes}
        self.fee_munt, self.fee_munt_alle = munt_kosten(kansen)
        self.start = {**{q: inleg / 2 / len(self.quotes) / 2 for q in self.quotes},
                      **{m: inleg / 2 / len(self.munten) / 2 for m in self.munten}}
        self.bal = {b: dict(self.start) for b in beurzen}
        self.onderweg = []   # (aankomst_t, beurs, bezit, bedrag)
        self.p0 = {m: self.koers(m, self.t0) for m in self.munten}
        self.r_laatst = {m: 1.0 for m in self.munten}
        self.koers_bekend = all(p for p in self.p0.values())
        self.per_dag = collections.defaultdict(lambda: collections.Counter())
        self.schuif_log = []

    def r(self, m, t):
        p0 = self.p0.get(m)
        p = self.koers(m, t) if p0 else None
        return p / p0 if p0 and p else self.r_laatst[m]

    def totaal(self, bezit):
        return sum(self.bal[b][bezit] for b in self.beurzen) + sum(x[3] for x in self.onderweg if x[2] == bezit)

    def tik(self, t):
        """Koerseffect bijwerken tot t en aangekomen schuifjes bijboeken."""
        for m in self.munten:
            r = self.r(m, t)
            self.per_dag[dag(t)]["koers"] += self.totaal(m) * (r - self.r_laatst[m])
            self.r_laatst[m] = r
        for x in [x for x in self.onderweg if x[0] <= t]:
            self.onderweg.remove(x)
            self.bal[x[1]][x[2]] += x[3]

    def schuif(self, bezit, t):
        """Dreigt een kant leeg te raken, schuif dan de helft van het verschil terug."""
        if any(x[2] == bezit for x in self.onderweg):
            return
        a, b = self.beurzen
        leeg, vol = (a, b) if self.bal[a][bezit] <= self.bal[b][bezit] else (b, a)
        if self.bal[leeg][bezit] >= DREMPEL * self.start[bezit]:
            return
        bedrag = (self.bal[vol][bezit] - self.bal[leeg][bezit]) / 2
        if bezit in self.quotes:
            k, reis, _ = quote_opname(vol, bezit)
            kosten_eur, kosten_eenheid = k * self.eur_q[bezit], k * self.eur_q[bezit]
        else:
            kosten_eur = self.fee_munt.get((vol, bezit), self.fee_munt_alle.get(bezit, 0.0))
            kosten_eenheid = kosten_eur / self.r_laatst[bezit]
            reis = MUNT_REIS_S
        if bedrag <= 0 or kosten_eenheid > MAX_KOSTEN_DEEL * bedrag:
            return
        self.bal[vol][bezit] -= bedrag
        self.onderweg.append((t + reis, leeg, bezit, bedrag - kosten_eenheid))
        self.per_dag[dag(t)]["kosten"] += kosten_eur
        self.per_dag[dag(t)]["schuif"] += 1
        self.schuif_log.append((t, bezit, vol, leeg, bedrag, kosten_eur))

    def draai(self):
        """Alle kansen op volgorde van begin; tussendoor aan het eind van elke dag het koerseffect bijwerken."""
        gebeurt = [(ts(r["begin"]), 0, r) for r in self.kansen]
        t = self.t0
        while t < self.t1:
            t = min(ts(dag(t) + "T00:00:00Z") + 86400 - 1, self.t1)
            gebeurt.append((t, 1, None))
            t += 1
        gebeurt.append((max(self.t1, self.t0), 1, None))
        for t, soort, r in sorted(gebeurt, key=lambda x: (x[0], x[1])):
            self.tik(t)
            if r is not None:
                self.voer_uit(r, t)
        return self

    def voer_uit(self, r, t):
        d = self.per_dag[dag(t)]
        d["kansen"] += 1
        koop, verkoop, m, q = r["koop"], r["verkoop"], r["munt"], r["quote"]
        ruimte = r.get("ruimte_eur_med") or 0
        rm = self.r_laatst[m]
        x = min(ruimte, self.bal[koop][q], self.bal[verkoop][m] * rm)
        d["vol"] += bruto_bij(r, ruimte)
        if x < MIN_ORDER_EUR:
            d["gemist"] += 1
        else:
            if x < ruimte - 0.01:
                d["beperkt"] += 1
            g = bruto_bij(r, x)
            self.bal[koop][q] -= x
            self.bal[koop][m] += x / rm
            self.bal[verkoop][m] -= x / rm
            self.bal[verkoop][q] += x + g
            d["bruto"] += g
            d["ingezet"] += x
        for bezit in (q, m):
            self.schuif(bezit, t)

    def waarde(self):
        return sum(self.totaal(q) for q in self.quotes) + sum(self.totaal(m) * self.r_laatst[m] for m in self.munten)

    def dagen(self):
        """Per dag: kansen, gemist, beperkt, bruto, kosten, koers, netto, rendement (fractie van de inleg)."""
        uit = {}
        for d in sorted(self.per_dag):
            c = self.per_dag[d]
            netto = c["bruto"] - c["kosten"] + c["koers"]
            uit[d] = {**{k: c[k] for k in ("kansen", "gemist", "beperkt", "bruto", "kosten", "koers", "vol",
                                           "schuif", "ingezet")}, "netto": netto, "rendement": netto / self.inleg}
        return uit


def paren(echte):
    """Echte kansen per beurspaar (beide richtingen samen): {(beurs, beurs): [kansen]}."""
    uit = collections.defaultdict(list)
    for r in echte:
        uit[tuple(sorted((r["koop"], r["verkoop"])))].append(r)
    return dict(uit)


# ---- het blok in het rapport ----

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


def blok(echte, stand, mica, koersbron=None, inleggen=(2000, 5000), grijs_top=5):
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
    alle_paren = paren(echte)
    vergund = sorted(p for p in alle_paren if p[0] in mica and p[1] in mica)
    grijs = sorted((p for p in alle_paren if p not in vergund),
                   key=lambda p: -sum(bruto_bij(r, inleggen[-1] / 4) for r in alle_paren[p]))[:grijs_top]
    koers = None
    if koersbron:
        bronnen = {}
        for p in vergund + grijs:
            for r in alle_paren[p]:
                lijst = sorted(p, key=lambda b: VOORKEUR.index(b) if b in VOORKEUR else 99)
                bronnen.setdefault(r["munt"], (r["quote"], lijst))
        koers = koersbron(bronnen, t0, t1)
    for titel, lijst in (("Alleen MiCA-beurzen (alle paren met echte kansen)", vergund),
                         (f"Met minstens één grijze beurs (de {grijs_top} paren met de meeste bruto winst)", grijs)):
        uit += [f"### {titel}", ""]
        if not lijst:
            uit += ["Geen echte kansen op zo'n paar.", ""]
            continue
        uit += ["| Beurspaar | Inleg | Dag | Gemeten | Kansen | Gemist (geen voorraad) | Kleiner door voorraad | "
                "Bruto winst | Kosten terugschuiven | Koerseffect voorraad | Netto | Rendement op de inleg |",
                "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        notities = []
        for p in lijst:
            for inleg in inleggen:
                s = Sim(alle_paren[p], inleg, p, koers, t0, t1).draai()
                for d, c in s.dagen().items():
                    ke = _eur(c["koers"]) if s.koers_bekend else "onbekend"
                    uit.append(f"| {p[0]} - {p[1]} | {_eur(inleg)} | {d} | {uren.get(d, 0):.1f} u | {c['kansen']} | "
                               f"{c['gemist']} | {c['beperkt']} | {_eur(c['bruto'])} | {_eur(c['kosten'])} "
                               f"({c['schuif']}x) | {ke} | {_eur(c['netto'])}{'' if s.koers_bekend else '*'} | "
                               f"{c['rendement'] * 100:.2f}% |")
                tot = s.dagen().values()
                notities.append(f"- {p[0]} - {p[1]}, {_eur(inleg)}: munten {', '.join(s.munten)}; bruto zonder "
                                f"voorraadgrens zou {_eur(sum(c['vol'] for c in tot))} zijn, met voorraad "
                                f"{_eur(sum(c['bruto'] for c in tot))} (GEZIEN boek, GOK model).")
        uit += [""] + notities + [""]
    uit.append("Dag en Gemeten: de kansen komen alleen uit de uren dat de scanner mat (GEZIEN); het koerseffect loopt "
               "door over de hele tijd van de eerste tot de laatste meting. Rendement = netto gedeeld door de inleg, "
               "voor die dag. * = koers niet op te halen, koerseffect onbekend (niet als 0 bedoeld).")
    uit += ["", "**Aannames:**", ""] + [f"- {a}" for a in AANNAMES]
    gezien = sorted({(b, q) for p in vergund + grijs for b in p for q in {r["quote"] for r in alle_paren[p]}})
    uit += ["- Geld terugschuiven per beurs: " + "; ".join(
        f"{b} {q}: {quote_opname(b, q)[0]:g} {q}, {quote_opname(b, q)[2]}" for b, q in gezien) + ".", ""]
    return uit


# ---- koersen voor het koerseffect (openbare candles, alleen lezen; GEZIEN) ----

def _candles(beurs, munt, quote, van, tot):
    import beurzen

    def haal(url):
        return beurzen.haal(url, timeout=8)
    iv = 900 if tot - van < 7 * 86400 else 3600
    van, tot = int(van) - iv, int(tot) + iv
    if beurs == "kraken":
        d = haal(f"https://api.kraken.com/0/public/OHLC?pair={munt}{quote}&interval={iv // 60}&since={van}")
        rij = next((v for v in (d.get("result") or {}).values() if isinstance(v, list)), [])
        return [(int(c[0]), float(c[4])) for c in rij if isinstance(c, list)]
    if beurs == "bitvavo":
        d = haal(f"https://api.bitvavo.com/v2/{munt}-{quote}/candles?interval={iv // 60}m&start={van}000"
                    f"&end={tot}000&limit=1440".replace("60m", "1h"))
        return [(int(c[0]) // 1000, float(c[4])) for c in d]
    if beurs == "kucoin":
        d = haal(f"https://api.kucoin.com/api/v1/market/candles?type={'15min' if iv == 900 else '1hour'}"
                    f"&symbol={munt}-{quote}&startAt={van}&endAt={tot}")
        return [(int(c[0]), float(c[2])) for c in d.get("data") or []]
    if beurs == "gate":
        d = haal(f"https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair={munt}_{quote}"
                    f"&interval={'15m' if iv == 900 else '1h'}&from={van}&to={tot}")
        return [(int(c[0]), float(c[2])) for c in d]
    return []


class Koersen:
    """koers(munt, t): slotkoers van de candle waarin t valt, van de eerste beurs in de lijst die data geeft.
    Geen data: None (dan telt het koerseffect voor die munt als onbekend, niet als 0)."""

    def __init__(self, bronnen, van, tot, haal=_candles):
        self.rij = {}
        for munt, (quote, lijst) in bronnen.items():
            for b in lijst:
                try:
                    c = sorted(haal(b, munt, quote, van, tot))
                except Exception:
                    c = []
                if c:
                    self.rij[munt] = c
                    break

    def __call__(self, munt, t):
        c = self.rij.get(munt)
        if not c:
            return None
        i = bisect.bisect_right(c, (t, float("inf"))) - 1
        return c[max(i, 0)][1] or None


AANNAMES = [
    "Winst per kans: de mediaan van wat de scanner op het boek mat bij €100, €500, €1.000, €2.500 en de volle ruimte "
    "(GEZIEN), lineair daartussen (GOK). Uitgevoerd op het moment dat de kans begon, één keer per kans (GOK).",
    "Inleg: de helft geld (de quote van de kansen), de helft munten, verdeeld over de munten die op dat paar echte "
    "kansen hadden, en alles half op elke beurs (GOK). Die munten zijn **achteraf** gekozen; vooraf weet je dat niet.",
    f"Terugschuiven zodra een kant onder {DREMPEL:.0%} van zijn beginvoorraad komt: de helft van het verschil gaat "
    f"terug, alleen als de opnamekosten hooguit {MAX_KOSTEN_DEEL:.0%} van het bedrag zijn (GOK, eigen regel).",
    "Opnamekosten van de munt: wat de scanner bij die beurs zag (GEZIEN uit de API van de beurs; bij Kraken en Gate "
    "geschat uit andere beurzen, GOK). Geld: zie de tabel hieronder.",
    f"Een munt is na {MUNT_REIS_S // 60} minuten op de andere beurs (GOK). Zolang iets onderweg is, telt het niet "
    "als voorraad; kansen die daardoor niet of kleiner konden, staan als gemist of beperkt.",
    f"Kleiner dan {MIN_ORDER_EUR} euro telt als gemist (GOK; minimale order- en opnamebedragen per beurs niet "
    "meegeteld). USDT telt tegen de koers van het moment van de kans; de koers USDT-EUR zelf beweegt niet mee (GOK).",
    "Koerseffect: slotkoers per 15 minuten (of per uur) uit de openbare candles van Bitvavo, Kraken, KuCoin of Gate "
    "(GEZIEN), over alle aangehouden munten, ook als de scanner tussen twee runs even niet mat.",
    "Niet meegeteld: andere bots die dezelfde kans pakken, dat het boek zich na jouw order aanvult (dan kan het "
    "vaker), belasting, en dat de EU-versie van een beurs minder munten kan hebben dan de API die we meten.",
]
