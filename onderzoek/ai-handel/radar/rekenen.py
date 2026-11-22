"""Vaste waarden en losse rekensommen van de kansenradar (zonder internet, makkelijk te testen)."""
import datetime as dt
import json
import math
import os
import sys
import statistics
import time

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scanner"))
import scanner  # noqa: E402

ELKE_PAREN_S = 180      # A: lijst met paren per beurs
ELKE_NOTERING_S = 60    # A: boeken van gevolgde nieuwe noteringen
VOLG_NOTERING_S = 6 * 3600
MAX_GEVOLGD = 12        # A: hooguit zoveel noteringen tegelijk volgen (de nieuwste)
MAX_ELDERS = 6          # A: per notering hooguit zoveel andere beurzen
ELKE_FUNDING_S = 120    # B
DREMPEL_FUNDING = 0.001     # B: piek begint bij 0,1% per 8 uur
DREMPEL_FUNDING_UIT = 0.0005  # B: en eindigt onder 0,05% per 8 uur (anders flappert hij rond de grens)
ELKE_STABLE_S = 15      # C
ELKE_BASIS_S = 6 * 3600  # C2: basislijn (mediaan per dag) opnieuw ophalen
BASIS_DAGEN = 45        # C2: zoveel hele dagen terug
BASIS_MIN_DAGEN = 20    # C2: minder dagen geschiedenis: basislijn onbekend
MAX_GAT_S = 2 * 3600    # B: open pieken van de vorige run alleen afmaken als die run hooguit 2 uur geleden stopte
DREMPEL_STABLE = 0.003  # C2: afwijking van de basislijn vanaf 0,3%
ELKE_WALLET_S = 1800    # opname- en stortstatus van alle beurzen
ELKE_WALLET_GEVOLGD_S = 300  # en van beurzen met een gevolgde notering
SLUIT_NA_S = 180        # een open moment dat zo lang niet bekeken is, telt als gesloten
INLEG = (100, 150, 200, 500, 2000, 5000)   # Thijs: ook wat het met weinig geld oplevert
WINST = tuple(f"winst{i}" for i in INLEG)
MASSA_NIEUW = 25        # meer nieuwe munten tegelijk op één beurs: waarschijnlijk een storing in de lijst, niet tellen

STABLE_USD = {"USDT", "USDC", "FDUSD", "PYUSD", "USDE", "DAI", "TUSD", "USD1", "RLUSD", "USDG", "USDS", "USDP", "USDQ"}
STABLE_EUR = {"EURC", "EURE", "EURI", "EURCV", "EUROP", "EURT", "AEUR", "EURR", "EURQ", "EURAU"}
STABLE = STABLE_USD | STABLE_EUR
QUOTE_FIAT = {"EUR", "USD", "USDT", "USDC"}
MAX_BOEK_PER_BEURS = 4   # C: orderboeken per beurs per ronde van 15 s
GEBLOKKEERD = {"bybit", "binance"}  # weigeren vanaf de server en vanaf GitHub (VS): 403 en 451


def nu_s():
    return time.time()


def iso(t):
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def per8(rate, uur):
    """Funding per periode omgerekend naar per 8 uur, zodat beurzen met 1, 4 en 8 uur te vergelijken zijn."""
    return rate * 8 / uur if uur else 0.0


def bereken_inleg(laten, biedingen, fee_koop, fee_verkoop, opname_munt, eur_per_quote):
    """scanner.bereken plus de winst bij elke inleg in INLEG (€100 tot €5.000)."""
    r = scanner.bereken(laten, biedingen, fee_koop, fee_verkoop, opname_munt, eur_per_quote)
    if not r:
        return r
    fee_m = opname_munt or 0.0
    for p in INLEG:
        m, kost, krijg = scanner.vul(laten, biedingen, fee_koop, fee_verkoop, p / eur_per_quote)
        r[f"winst{p}"] = round((krijg - kost - fee_m * biedingen[0][0]) * eur_per_quote, 4) if m > 0 else None
    return r


def peg(munt, quote, eurusd):
    """Wat de munt in de quote hoort te kosten als alles op zijn koppeling staat. USDT en USDC als quote tellen als
    1 dollar (we meten juist hoe ver ze daarvan af zitten). None als er geen EUR/USD-koers is en die nodig is."""
    def usd(x):
        if x in STABLE_USD or x == "USD":
            return 1.0
        if x in STABLE_EUR or x == "EUR":
            return eurusd
        return None
    a, b = usd(munt), usd(quote)
    if not a or not b:
        return None
    return a / b


def afwijking(laten, biedingen, ref, fee, drempel=DREMPEL_STABLE, eur_per_quote=1.0):
    """C2: hoe ver zit het boek van de koppeling? Geeft None, of een meting voor de goedkope kant (kopen onder de
    koppeling, later verkopen op de koppeling) of de dure kant (verkopen boven de koppeling, later terugkopen op de
    koppeling). Winst na takerkosten bij kopen en bij terugdraaien (2 x fee), bij €500/2.000/5.000, en de ruimte:
    hoeveel euro op het boek ligt met minstens `drempel` afwijking. Alleen als de beste prijs al `drempel` afwijkt."""
    if not ref or ref <= 0:
        return None
    for kant, rijen in (("goedkoop", laten), ("duur", biedingen)):
        if not rijen:
            continue
        p0 = rijen[0][0]
        afw = (ref - p0) / ref if kant == "goedkoop" else (p0 - ref) / ref
        if afw < drempel:
            continue
        uit = {"kant": kant, "afwijking_pct": round(afw * 100, 4), "na_kosten_pct": round((afw - 2 * fee) * 100, 4),
               "prijs": p0, "ref": round(ref, 6)}
        ruimte = 0.0
        for p, q in rijen:
            a = (ref - p) / ref if kant == "goedkoop" else (p - ref) / ref
            if a < drempel:
                break
            ruimte += p * q
        uit["ruimte_eur"] = round(ruimte * eur_per_quote, 2)
        for inleg in INLEG:
            rest, winst = inleg / eur_per_quote, 0.0
            for p, q in rijen:
                # per eenheid quote ingezet: goedkoop = kopen op p, later verkopen op ref; duur = verkopen op p,
                # later terugkopen op ref. Takerkosten bij allebei.
                per = ref / p * (1 - fee) - (1 + fee) if kant == "goedkoop" else (1 - fee) - ref / p * (1 + fee)
                if per <= 0 or rest <= 0:
                    break
                deel = min(rest, p * q)
                winst += deel * per
                rest -= deel
            uit[f"winst{inleg}"] = round(winst * eur_per_quote, 4) if rest < inleg / eur_per_quote else None
        return uit
    return None


def zelfde_ding(spot, perp, marge=0.05):
    """Is de spotmunt waarschijnlijk hetzelfde als de perp? De prijzen moeten op 5% na gelijk zijn, of een macht
    van 10 schelen (1000PEPE, kPEPE). Anders is het vaak een andere munt met dezelfde naam (of een aandeel-token)."""
    if not spot or not perp or spot <= 0 or perp <= 0:
        return False
    x = math.log10(spot / perp)
    return abs(x - round(x)) <= math.log10(1 + marge)


class Volger:
    """Houdt momenten bij die een tijd open staan (A en C). Een moment begint bij de eerste meting waarin het er is,
    en sluit bij de eerste meting waarin het er niet meer is (of na SLUIT_NA_S zonder meting). Bij sluiten komt
    er één regel in het bestand: begin, eind, duur, aantal metingen, mediaan en maximum van de getallen, en de
    eerste meting (voor de winst als je meteen instapt)."""

    def __init__(self, pad, velden):
        self.pad = pad
        self.velden = velden
        self.open = {}
        self.gesloten = 0

    def zie(self, k, t, meting, vast):
        o = self.open.get(k)
        if o is None:
            o = self.open[k] = {"begin_t": t, "metingen": [], **vast}
        o["laatst_t"] = t
        o["metingen"].append(meting)

    def stap(self, t, bekeken, kansen):
        """bekeken: sleutels die deze ronde gemeten zijn; kansen: {sleutel: (meting, vaste velden)}."""
        for k, (m, vast) in kansen.items():
            self.zie(k, t, m, vast)
        for k in list(self.open):
            if k in kansen:
                continue
            if k in bekeken or t - self.open[k]["laatst_t"] > SLUIT_NA_S:
                self.sluit(k)

    def sluit(self, k, einde_run=False):
        o = self.open.pop(k)
        ms = o.pop("metingen")
        regel = {x: v for x, v in o.items() if not x.endswith("_t")}
        regel.update(begin=iso(o["begin_t"]), eind=iso(o["laatst_t"]), duur_s=round(o["laatst_t"] - o["begin_t"]),
                     metingen=len(ms), einde_run=einde_run)
        for v in self.velden:
            w = [x[v] for x in ms if isinstance(x.get(v), (int, float))]
            regel[f"{v}_med"] = round(statistics.median(w), 4) if w else None
            regel[f"{v}_max"] = round(max(w), 4) if w else None
        regel["eerste"] = ms[0]
        with open(self.pad, "a") as fh:
            fh.write(json.dumps(regel, ensure_ascii=False) + "\n")
        self.gesloten += 1

    def sluit_alles(self):
        for k in list(self.open):
            self.sluit(k, einde_run=True)

