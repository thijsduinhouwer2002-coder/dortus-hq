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
    de helft van het verschil gaat naar de lege kant, alleen als de opnamekosten hooguit 1% van het bedrag zijn.
    Tijdens het onderweg zijn is dat geld of die munt niet te gebruiken.
  - Het koerseffect is de waardeverandering van de aangehouden munten (op beide beurzen en onderweg), apart gemeld.
Netto = bruto winst min kosten terugschuiven plus koerseffect; dat is precies de eindwaarde min de inleg.

Elk cijfer is GEZIEN (gemeten of uit een API of tarievenpagina) of GOK (een aanname); zie AANNAMES in
simrapport.py, dat ook het blok voor het rapport maakt.
"""
import collections
import datetime as dt

from simbronnen import Koersen, Minima  # noqa: F401  (rapport.py gebruikt simulatie.Koersen en simulatie.Minima)

DREMPEL = 0.25           # GOK: schuif terug als een kant onder 25% van zijn beginvoorraad komt
MAX_KOSTEN_DEEL = 0.01   # GOK, achteraf gekozen (na de uitkomst bij 5%): schuif alleen bij opnamekosten hooguit 1%
UITVOER_NA_S = 120       # een kans telt pas als echt na 2 minuten; dan pas uitvoeren (keuring S10)
HEROPEN_S = 300          # GOK: zelfde paar en munt binnen 5 min weer open = hetzelfde boek, deels al gebruikt
MIN_ORDER_EUR = 10       # GOK: minimale order als de API van de beurs niets geeft (anders Minima hieronder)
INLEGGEN = (100, 150, 200, 2000, 5000)
MUNT_REIS_S = 30 * 60    # GOK: een munt is na 30 minuten binnen (bevestigingen plus verwerking door de beurs)

# Opnamekosten en reistijd van het geld (de quote) per beurs: (kosten in de quote, reistijd in seconden, bron).
QUOTE_OPNAME = {
    ("bitvavo", "EUR"): (0.0, 24 * 3600, "kosten GEZIEN (api.bitvavo.com/v2/assets: EUR withdrawalFee 0), "
                                         "tijd GOK (1 werkdag, SEPA)"),
    ("kraken", "EUR"): (1.0, 3600, "kosten GEZIEN (support.kraken.com/articles/360000381846: Instant SEPA, "
                                   "Banking Circle, 1 EUR, near-instant), tijd GOK (1 uur tot het op de andere beurs staat)"),
    ("kucoin", "USDT"): (1.0, 1800, "kosten GEZIEN (api.kucoin.com/api/v3/currencies/USDT: BEP20 1 USDT), tijd GOK"),
}
# Minimale opname van het geld per beurs: (minimum in de quote, bron). Onbekend: geen minimum (GOK).
QUOTE_MIN = {
    ("bitvavo", "EUR"): (0.0, "GEZIEN, api.bitvavo.com/v2/assets withdrawalMinAmount"),
    ("kraken", "EUR"): (2.0, "GEZIEN, support.kraken.com/articles/360000381846 Instant SEPA (Banking Circle)"),
    ("kucoin", "USDT"): (5.0, "GEZIEN, api.kucoin.com/api/v3/currencies/USDT BEP20 withdrawalMinSize"),
    ("gate", "USDT"): (1.0, "GEZIEN, api.gateio.ws/api/v4/wallet/currency_chains withdraw_amount_min"),
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

    def __init__(self, kansen, inleg, beurzen, koers=None, t0=None, t1=None, minima=None, drempel=DREMPEL,
                 max_kosten=MAX_KOSTEN_DEEL):
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
        self.minima = minima or (lambda beurs, munt, quote: None)
        self.drempel, self.max_kosten = drempel, max_kosten
        self.gebruikt = {}   # (koop, verkoop, munt, quote) -> (eind van de kans, al ingezet uit dat boek)
        self.q_munt = {r["munt"]: r["quote"] for r in reversed(self.kansen)}   # quote van de eerste kans

    def p0_eur(self, m):
        """Euro per munt tegen de beginkoers, of None."""
        return self.p0[m] * self.eur_q[self.q_munt[m]] if self.p0.get(m) else None

    def min_order(self, r):
        """Kleinste order in euro die op beide beurzen mag (GEZIEN uit de API; niets bekend: MIN_ORDER_EUR, GOK)."""
        m, q, grens = r["munt"], r["quote"], 0.0
        for b in (r["koop"], r["verkoop"]):
            mi = self.minima(b, m, q) or {}
            if mi.get("order_q") is None and mi.get("order_m") is None:
                grens = max(grens, MIN_ORDER_EUR)
                continue
            if mi.get("order_q") is not None:
                grens = max(grens, mi["order_q"] * self.eur_q[q])
            if mi.get("order_m") is not None and self.p0_eur(m):
                grens = max(grens, mi["order_m"] * self.p0_eur(m) * self.r_laatst[m])
        return grens

    def min_opname(self, beurs, bezit):
        """Kleinste opname, in de eenheid van self.bal (euro, of euro tegen de beginkoers bij munten)."""
        if bezit in self.quotes:
            return QUOTE_MIN.get((beurs, bezit), (0.0,))[0] * self.eur_q[bezit]
        mi = self.minima(beurs, bezit, self.q_munt[bezit]) or {}
        return mi["opname_m"] * self.p0_eur(bezit) if mi.get("opname_m") and self.p0_eur(bezit) else 0.0

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
        if self.bal[leeg][bezit] >= self.drempel * self.start[bezit]:
            return
        bedrag = (self.bal[vol][bezit] - self.bal[leeg][bezit]) / 2
        if bezit in self.quotes:
            k, reis, _ = quote_opname(vol, bezit)
            kosten_eur, kosten_eenheid = k * self.eur_q[bezit], k * self.eur_q[bezit]
        else:
            kosten_eur = self.fee_munt.get((vol, bezit), self.fee_munt_alle.get(bezit, 0.0))
            kosten_eenheid = kosten_eur / self.r_laatst[bezit]
            reis = MUNT_REIS_S
        minimum = self.min_opname(vol, bezit)
        if bedrag < minimum:
            if self.bal[vol][bezit] < minimum:
                return
            bedrag = minimum
        if bedrag <= 0 or kosten_eenheid > self.max_kosten * bedrag:
            return
        self.bal[vol][bezit] -= bedrag
        self.onderweg.append((t + reis, leeg, bezit, bedrag - kosten_eenheid))
        self.per_dag[dag(t)]["kosten"] += kosten_eur
        self.per_dag[dag(t)]["schuif"] += 1
        self.schuif_log.append((t, bezit, vol, leeg, bedrag, kosten_eur))

    def draai(self):
        """Alle kansen op volgorde van begin; tussendoor aan het eind van elke dag het koerseffect bijwerken."""
        gebeurt = [(min(ts(r["begin"]) + UITVOER_NA_S, ts(r["eind"])), 0, r) for r in self.kansen]
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
        sleutel = (koop, verkoop, m, q)
        eind_vorige, al = self.gebruikt.get(sleutel, (None, 0.0))
        if eind_vorige is None or ts(r["begin"]) - eind_vorige > HEROPEN_S:
            al = 0.0   # een nieuwe kans; binnen HEROPEN_S is het hetzelfde boek, dat deel is al op
        rm = self.r_laatst[m]
        x = max(0.0, min(ruimte - al, self.bal[koop][q], self.bal[verkoop][m] * rm))
        d["vol"] += bruto_bij(r, ruimte) - bruto_bij(r, al)
        if x < max(self.min_order(r), 0.01):
            d["gemist"] += 1
        else:
            if x < ruimte - al - 0.01:
                d["beperkt"] += 1
            g = bruto_bij(r, al + x) - bruto_bij(r, al)
            al += x
            self.bal[koop][q] -= x
            self.bal[koop][m] += x / rm
            self.bal[verkoop][m] -= x / rm
            self.bal[verkoop][q] += x + g
            d["bruto"] += g
            d["ingezet"] += x
        self.gebruikt[sleutel] = (ts(r["eind"]), al)
        for bezit in (q, m):
            self.schuif(bezit, t)

    def scheef(self):
        """Staat aan het eind een geld of munt op een beurs onder de schuifdrempel? Dan begint een volgende dag scheef."""
        return any(self.bal[b][x] < self.drempel * self.start[x] for b in self.beurzen for x in self.start)

    def waarde(self):
        return sum(self.totaal(q) for q in self.quotes) + sum(self.totaal(m) * self.r_laatst[m] for m in self.munten)

    def dagen(self):
        """Per dag: kansen, gemist, beperkt, bruto, kosten, koers, netto, rendement (fractie van de inleg)."""
        uit = {}
        for d in sorted(self.per_dag):
            c = self.per_dag[d]
            handel, netto = c["bruto"] - c["kosten"], c["bruto"] - c["kosten"] + c["koers"]
            uit[d] = {**{k: c[k] for k in ("kansen", "gemist", "beperkt", "bruto", "kosten", "koers", "vol",
                                           "schuif", "ingezet")}, "handel": handel, "rendement_handel":
                      handel / self.inleg, "netto": netto, "rendement": netto / self.inleg}
        return uit


def paren(echte):
    """Echte kansen per beurspaar (beide richtingen samen): {(beurs, beurs): [kansen]}."""
    uit = collections.defaultdict(list)
    for r in echte:
        uit[tuple(sorted((r["koop"], r["verkoop"])))].append(r)
    return dict(uit)
