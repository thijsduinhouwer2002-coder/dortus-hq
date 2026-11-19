#!/usr/bin/env python3
"""Kansenradar: meet een week lang drie zeldzame momenten op crypto-beurzen. Alleen openbare API's: geen account,
geen sleutel, geen handel, geen geld. Uitleg in README.md.

  A. Nieuwe noteringen: elke 3 minuten de lijst met paren van 15 beurzen naast de vorige leggen. Komt er een munt
     bij die de beurs nog niet had, dan volgt de radar die munt 6 uur lang: elke minuut de orderboeken op de nieuwe
     beurs en op de beurzen waar hij al stond (zelfde quote), winst na takerkosten en opnamekosten, diepte, duur,
     en of opnemen en storten open staan.
  B. Funding-pieken: elke 2 minuten de funding van alle perpetuals op 9 beurzen. Boven 0,1% per 8 uur begint een
     piek; de radar doet alsof je dan spot koopt en de perp shortt (gedekt), telt de funding die echt verrekend
     wordt, en sluit als de funding onder 0,05% per 8 uur zakt. Winst na 4 keer takerkosten en het verschil
     tussen spot- en perpprijs bij in- en uitstappen.
  C. Stablecoins: elke 15 seconden de orderboeken van alle stablecoin-paren (USDC, USDT, EURC, EURe, ...) tegen
     EUR, USD, USDT en USDC. Twee soorten momenten: (1) tussen beurzen, dezelfde munt goedkoper kopen dan hij
     elders verkocht wordt, na alle kosten (echte arbitrage); (2) los van de koppeling, meer dan 0,3% van 1 dollar
     of 1 euro (geen arbitrage: je wint alleen als hij terugkomt).

Gebruik:  python3 radar.py --minuten 10 --uit /tmp/radar [--vorige paren-laatst.json]
"""
import argparse
import collections
import concurrent.futures as cf
import datetime as dt
import json
import math
import os
import signal
import statistics
import sys
import time

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
sys.path.append(os.path.join(HIER, "..", "scanner"))   # achteraan: ../scanner/rapport.py mag rapport.py hier niet verdringen
import beurzen  # noqa: E402
import minima  # noqa: E402
import perps  # noqa: E402
import scanner  # noqa: E402  (hergebruik: vul, bereken, is_kans, taker, opname_fee, netwerk_stand, contract_stand)

ELKE_PAREN_S = 180      # A: lijst met paren per beurs
ELKE_NOTERING_S = 60    # A: boeken van gevolgde nieuwe noteringen
VOLG_NOTERING_S = 6 * 3600
MAX_GEVOLGD = 12        # A: hooguit zoveel noteringen tegelijk volgen (de nieuwste)
MAX_ELDERS = 6          # A: per notering hooguit zoveel andere beurzen
ELKE_FUNDING_S = 120    # B
DREMPEL_FUNDING = 0.001     # B: piek begint bij 0,1% per 8 uur
DREMPEL_FUNDING_UIT = 0.0005  # B: en eindigt onder 0,05% per 8 uur (anders flappert hij rond de grens)
ELKE_STABLE_S = 15      # C
DREMPEL_STABLE = 0.003  # C2: afwijking van de koppeling vanaf 0,3%
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


class Radar:
    def __init__(self, uitmap, vorige=None, spot_klassen=None, perp_bronnen=None, log=print):
        self.uit = uitmap
        os.makedirs(uitmap, exist_ok=True)
        self.log = log
        self.spot = {c.naam: c() for c in (spot_klassen or [k for k in beurzen.ALLE if k.naam not in GEBLOKKEERD])}
        self.perps = perp_bronnen if perp_bronnen is not None else perps.ALLE
        self.pool = cf.ThreadPoolExecutor(max_workers=24)
        self.paren, self.wallets, self.wallet_t = {}, {}, {}
        self.min_spot, self.min_opname, self.min_perp = {}, {}, {}
        self.ooit = {}          # beurs -> alle munten die we er ooit zagen (deze run en de vorige lijst)
        self.vorige_t = None
        if vorige and os.path.exists(vorige):
            try:
                with open(vorige) as fh:
                    d = json.load(fh)
                self.ooit = {b: set(ms) for b, ms in d.get("munten", {}).items()}
                self.vorige_t = d.get("t")
            except (ValueError, OSError) as e:
                self.log(f"vorige lijst niet te lezen: {e!r}")
        self.eerste_vergelijking = {b: True for b in self.spot}
        self.gevolgd = {}       # (beurs, munt, quote) -> {"t": begin, "elders": [...]}
        self.eur = {"EUR": 1.0}
        self.eurusd = None
        self.funding_vorig = {}  # (beurs, munt) -> laatste meting
        self.pieken = {}        # (beurs, munt) -> open piek
        self.volg_a = Volger(os.path.join(uitmap, "noteringen-kansen.jsonl"),
                             ("bruto_pct", *WINST, "ruimte_eur", "winst_ruimte"))
        self.volg_c1 = Volger(os.path.join(uitmap, "stable-tussen.jsonl"),
                              ("bruto_pct", *WINST, "ruimte_eur", "winst_ruimte"))
        self.volg_c2 = Volger(os.path.join(uitmap, "stable-afwijking.jsonl"),
                              ("afwijking_pct", "na_kosten_pct", *WINST, "ruimte_eur"))
        self.stand = {"start": iso(nu_s()), "vorige_lijst": self.vorige_t, "rondes": {"paren": 0, "noteringen": 0,
                      "funding": 0, "stable": 0}, "noteringen": 0, "pieken_gesloten": 0, "stable_boeken": 0,
                      "fouten": {}, "ok": {}}
        self.volgend = {"paren": 0, "noteringen": 0, "funding": 0, "stable": 0, "wallet": 0, "stand": 0}

    # ---------- hulp ----------
    def fout(self, wie, wat, e):
        k = f"{wie}:{wat}"
        self.stand["fouten"][k] = self.stand["fouten"].get(k, 0) + 1
        if self.stand["fouten"][k] <= 3:
            self.log(f"  fout {k}: {repr(e)[:160]}")

    def parallel(self, taken, timeout=60):
        """taken: {sleutel: (functie, argumenten)}. Geeft {sleutel: uitkomst}; fouten worden geteld, niet gegooid."""
        futs = {self.pool.submit(fn, *args): k for k, (fn, args) in taken.items()}
        uit = {}
        try:
            for fu in cf.as_completed(futs, timeout=timeout):
                k = futs[fu]
                try:
                    uit[k] = fu.result()
                except Exception as e:
                    self.fout(k[0] if isinstance(k, tuple) else k, k[1] if isinstance(k, tuple) and len(k) > 1
                              and isinstance(k[1], str) and k[1] in ("paren", "wallet", "boek", "funding", "koersen")
                              else "verzoek", e)
        except cf.TimeoutError:
            self.fout("radar", "timeout", "verzoeken te traag")
        return uit

    def taker(self, beurs, munt, quote):
        return scanner.taker(self.paren, beurs, (munt, quote))

    # ---------- wallets ----------
    def ververs_wallets(self, welke):
        uit = self.parallel({(b, "wallet"): (self.spot[b].wallet, ()) for b in welke if b in self.spot}, timeout=90)
        t = nu_s()
        for (b, _), w in uit.items():
            self.wallets[b] = w
            self.wallet_t[b] = t

    def ververs_minima(self):
        """Minimale order- en opnamebedragen (elk half uur, samen met de wallets). Fouten: dan onbekend."""
        taken = {(b, "min_spot"): (minima.spot, (b,)) for b in self.spot}
        taken.update({(b, "min_opname"): (minima.opname, (b,)) for b in self.spot})
        taken.update({(b, "min_perp"): (minima.perp, (b,)) for b in self.perps})
        for (b, soort), d in self.parallel(taken, timeout=90).items():
            getattr(self, soort)[b] = d

    def min_order_eur(self, beurs, munt, quote, prijs):
        return minima.in_eur(self.min_spot.get(beurs, {}).get((munt, quote)), prijs, self.eur.get(quote, 0))

    def min_opname_eur(self, beurs, munt, prijs, quote):
        m = self.min_opname.get(beurs, {}).get(munt)
        return round(m * prijs * self.eur.get(quote, 0), 4) if m and prijs else None

    # ---------- A: noteringen ----------
    def ronde_paren(self):
        t = nu_s()
        uit = self.parallel({(b, "paren"): (s.paren, ()) for b, s in self.spot.items()}, timeout=90)
        nieuw = []
        for (b, _), p in uit.items():
            if not p:
                continue
            oud_paren = self.paren.get(b)
            self.paren[b] = p
            munten = {m for m, _ in p}
            ooit = self.ooit.get(b)
            if ooit is None:      # eerste lijst van deze beurs, geen vorige: alleen onthouden
                self.ooit[b] = munten
                self.eerste_vergelijking[b] = False
                continue
            erbij = sorted(munten - ooit)
            if oud_paren is not None and len(p) < 0.5 * len(oud_paren):
                erbij = []        # lijst ineens half zo groot: storing, niet vergelijken (en niets vergeten)
            if len(erbij) > MASSA_NIEUW:
                self.log(f"  {b}: {len(erbij)} nieuwe munten tegelijk, waarschijnlijk een storing; niet geteld")
                erbij = []
            for m in erbij:
                for (mm, q) in p:
                    if mm == m:
                        nieuw.append((b, m, q, self.eerste_vergelijking.get(b, False)))
            self.ooit[b] = ooit | munten
            self.eerste_vergelijking[b] = False
        if nieuw:
            self.ververs_wallets({b for b, *_ in nieuw})
        for b, m, q, laat in nieuw:
            self.nieuwe_notering(b, m, q, laat, t)
        self.stand["rondes"]["paren"] += 1
        self.bewaar_lijst()

    def nieuwe_notering(self, b, m, q, laat, t):
        elders = sorted((x for x, p in self.paren.items() if x != b and (m, q) in p),
                        key=lambda x: (x not in ("kraken", "bitvavo", "okx", "kucoin", "gate", "mexc", "bitget"), x))
        andere_quote = sorted(x for x, p in self.paren.items() if x != b and any(mm == m for mm, _ in p))
        contracten = {x: scanner.contract_stand(self.paren, self.wallets, b, x, (m, q)) for x in elders}
        w = self.wallets.get(b, {}).get(m, {})
        regel = {"t": iso(t), "beurs": b, "munt": m, "quote": q, "elders": elders, "elders_andere_quote": andere_quote,
                 "contract": contracten, "opname": w.get("opname"), "storting": w.get("storting"),
                 "vlak_na_start": laat, "vorige_lijst": self.vorige_t if laat else None}
        with open(os.path.join(self.uit, "noteringen.jsonl"), "a") as fh:
            fh.write(json.dumps(regel, ensure_ascii=False) + "\n")
        self.stand["noteringen"] += 1
        self.log(f"  NIEUW {b} {m}-{q}, al op: {', '.join(elders) or 'geen enkele andere beurs (zelfde quote)'}"
                 + (" (eerste vergelijking na start)" if laat else ""))
        if elders:
            self.gevolgd[(b, m, q)] = {"t": t, "elders": elders[:MAX_ELDERS], "laat": laat}
            if len(self.gevolgd) > MAX_GEVOLGD:
                oudste = min(self.gevolgd, key=lambda k: self.gevolgd[k]["t"])
                del self.gevolgd[oudste]

    def bewaar_lijst(self):
        with open(os.path.join(self.uit, "paren-laatst.json"), "w") as fh:
            json.dump({"t": iso(nu_s()), "munten": {b: sorted(ms) for b, ms in self.ooit.items()}}, fh)

    def ronde_noteringen(self):
        t = nu_s()
        for k in [k for k, v in self.gevolgd.items() if t - v["t"] > VOLG_NOTERING_S]:
            del self.gevolgd[k]
        if not self.gevolgd:
            return
        oud = {x for (b, _, _), v in self.gevolgd.items() for x in [b] + v["elders"]
               if t - self.wallet_t.get(x, 0) > ELKE_WALLET_GEVOLGD_S}
        if oud:
            self.ververs_wallets(oud)
        nodig = {(x, m, q) for (b, m, q), v in self.gevolgd.items() for x in [b] + v["elders"]}
        boeken = self.parallel({(x, "boek", m, q): (self.spot[x].boek, (self.paren[x][(m, q)]["id"],))
                                for x, m, q in nodig if (m, q) in self.paren.get(x, {})}, timeout=40)
        boeken = {(x, m, q): v for (x, _, m, q), v in boeken.items()}
        bekeken, kansen = set(), {}
        for (b, m, q), v in self.gevolgd.items():
            for x in v["elders"]:
                for koop, verkoop in ((b, x), (x, b)):
                    ba, bv = boeken.get((koop, m, q)), boeken.get((verkoop, m, q))
                    if not ba or not bv:
                        continue
                    sl = (b, m, q, koop, verkoop)
                    bekeken.add(sl)
                    r, vast = self.reken_paar(m, q, koop, verkoop, ba, bv)
                    if scanner.is_kans(r):
                        r["min_sinds_notering"] = round((t - v["t"]) / 60, 1)
                        vast.update(nieuwe_beurs=b, vlak_na_start=v["laat"])
                        kansen[sl] = (r, vast)
        self.volg_a.stap(t, bekeken, kansen)
        self.stand["rondes"]["noteringen"] += 1

    def reken_paar(self, m, q, koop, verkoop, boek_koop, boek_verkoop):
        """Winst bij kopen op `koop` en verkopen op `verkoop` (zoals de scanner): takerkosten aan beide kanten en
        één opname van de munt. Geeft (meting, vaste velden over opnemen, storten, netwerk en contract)."""
        netwerk, fee_net = scanner.netwerk_stand(self.wallets, koop, verkoop, m)
        if fee_net is not None:
            fee_m, bron = fee_net, "netwerk"
        else:
            fee_m, bron = scanner.opname_fee(self.wallets, koop, m)
        r = bereken_inleg(boek_koop[1], boek_verkoop[0], self.taker(koop, m, q), self.taker(verkoop, m, q), fee_m,
                          self.eur.get(q, 0))
        vast = {"munt": m, "quote": q, "koop": koop, "verkoop": verkoop,
                "opname_koop": scanner.wallet_stand(self.wallets, koop, m, "opname"),
                "storting_verkoop": scanner.wallet_stand(self.wallets, verkoop, m, "storting"),
                "netwerk": netwerk, "opname_bron": bron,
                "contract": scanner.contract_stand(self.paren, self.wallets, koop, verkoop, (m, q)),
                "taker_koop": self.taker(koop, m, q), "taker_verkoop": self.taker(verkoop, m, q)}
        pk, pv = boek_koop[1][0][0] if boek_koop[1] else 0, boek_verkoop[0][0][0] if boek_verkoop[0] else 0
        vast.update(min_koop_eur=self.min_order_eur(koop, m, q, pk), min_verkoop_eur=self.min_order_eur(verkoop, m, q, pv),
                    min_opname_eur=self.min_opname_eur(koop, m, pk, q))
        return r, vast

    # ---------- B: funding ----------
    def spot_voor(self, beurs, munt):
        """Waar koop je de spotkant? Bij dezelfde beurs als die de munt in USDT/USDC/USD heeft, anders bij de beurs
        met de laagste takerkosten die hem heeft. Geeft (spotbeurs, quote) of (None, None)."""
        def quotes(b):
            return [q for q in ("USDT", "USDC", "USD") if (munt, q) in self.paren.get(b, {})]
        if beurs in perps.SPOT_ZELFDE and quotes(beurs):
            return beurs, quotes(beurs)[0]
        kandidaten = [(self.taker(b, munt, quotes(b)[0]), b, quotes(b)[0]) for b in self.paren if quotes(b)]
        if not kandidaten:
            return None, None
        _, b, q = min(kandidaten)
        return b, q

    def ronde_funding(self):
        t = nu_s()
        data = self.parallel({(b, "funding"): (fn, ()) for b, fn in self.perps.items()}, timeout=60)
        data = {b: d for (b, _), d in data.items()}
        for b in data:
            self.stand["ok"][f"perp:{b}"] = self.stand["ok"].get(f"perp:{b}", 0) + 1
        # welke spotkoersen zijn nodig: voor open pieken en voor nieuwe pieken
        nodig = {}
        for b, d in data.items():
            for m, x in d.items():
                if (b, m) in self.pieken or abs(per8(x["rate"], x["uur"])) >= DREMPEL_FUNDING:
                    if (b, m) in self.pieken:
                        sb, sq = self.pieken[(b, m)]["spot"], self.pieken[(b, m)]["spot_quote"]
                    else:
                        sb, sq = self.spot_voor(b, m)
                    if sb:
                        nodig.setdefault(sb, set()).add((m, sq))
        koersen = self.parallel({(sb, "koersen"): (self.spot[sb].koersen, ()) for sb in nodig}, timeout=40)
        koersen = {sb: k for (sb, _), k in koersen.items()}
        for b, d in data.items():
            for m, x in d.items():
                self.funding_stap(b, m, x, t, koersen)
            # perps die verdwenen zijn: piek sluiten
            for (pb, pm) in [k for k in self.pieken if k[0] == b and k[1] not in d]:
                self.sluit_piek((pb, pm), t, koersen, reden="perp weg")
        self.stand["rondes"]["funding"] += 1

    def funding_stap(self, b, m, x, t, koersen):
        k = (b, m)
        vorig = self.funding_vorig.get(k)
        self.funding_vorig[k] = x
        r8 = per8(x["rate"], x["uur"])
        p = self.pieken.get(k)
        if p is not None:
            if p["spot"] and (p["munt"], p["spot_quote"]) in koersen.get(p["spot"], {}):
                p["spot_laatst"] = koersen[p["spot"]][(p["munt"], p["spot_quote"])]
                if not p["spot_in"]:   # bij het begin geen spotkoers: instappen telt vanaf nu
                    p["spot_in"] = p["spot_laatst"][1 if p["richting"] == "positief" else 0] or None
                    p["prijs_perp_in"] = x["prijs"]
            for veld, waarde in (("min_spot_eur", lambda: self.min_order_eur(p["spot"], m, p["spot_quote"],
                                                                              p["spot_in"]) if p["spot"] else None),
                                 ("min_perp_eur", lambda: self.min_perp_eur(b, m, x["prijs"]))):
                if p.get(veld) is None:   # bij de eerste ronde was de euro-koers nog niet bekend
                    p[veld] = waarde()
            # verrekening gezien: het tijdstip van de volgende verrekening schoof op, dus de vorige rate is betaald
            if vorig and x["volgende"] > vorig["volgende"] + 60 and vorig["volgende"] > p["begin_t"]:
                teken = 1 if p["richting"] == "positief" else -1
                p["ontvangen"] += teken * vorig["rate"]
                p["verrekeningen"] += 1
            p["laatst_t"] = t
            p["max_r8"] = max(p["max_r8"], abs(r8))
            p["prijs_perp_uit"] = x["prijs"]
            p["r8s"].append(r8)
            # Uitstappen pas na minstens één verrekening: bij perps die elk uur verrekenen schommelt de voorspelde
            # rate per minuut, en niemand stapt in om vóór de eerste betaling weer uit te stappen.
            if p["verrekeningen"] >= 1 and (abs(r8) < DREMPEL_FUNDING_UIT or (r8 > 0) != (p["richting"] == "positief")):
                self.sluit_piek(k, t, koersen)
            return
        if abs(r8) < DREMPEL_FUNDING:
            return
        sb, sq = self.spot_voor(b, m)
        bod, laat = koersen.get(sb, {}).get((m, sq), (0, 0)) if sb else (0, 0)
        spot_anders = False
        if sb and not zelfde_ding(laat or bod, x["prijs"]):
            spot_anders, sb, sq, bod, laat = True, None, None, 0, 0
        self.pieken[k] = {
            "beurs": b, "munt": m, "richting": "positief" if r8 > 0 else "negatief", "begin_t": t, "laatst_t": t,
            "uur": x["uur"], "r8_begin": r8, "max_r8": abs(r8), "r8s": [r8], "ontvangen": 0.0, "verrekeningen": 0,
            "prijs_perp_in": x["prijs"], "prijs_perp_uit": x["prijs"], "vol_usd": x["vol_usd"],
            "spot": sb, "spot_quote": sq, "spot_in": (laat if r8 > 0 else bod) or None,
            "taker_perp": perps.TAKER_PERP.get(b, 0.0006),
            "taker_spot": self.taker(sb, m, sq) if sb else None,
            "min_spot_eur": self.min_order_eur(sb, m, sq, laat or bod) if sb else None,
            "min_perp_eur": self.min_perp_eur(b, m, x["prijs"]),
            "spot_anders": spot_anders, "al_bij_start": self.stand["rondes"]["funding"] == 0,
        }

    def min_perp_eur(self, b, m, prijs):
        mp = self.min_perp.get(b, {}).get(m)
        if not mp:
            return None
        w = [v for v in ((mp.get("usd") or 0) * self.eur.get("USD", 0),
                         (mp.get("munten") or 0) * (prijs or 0) * self.eur.get("USDT", 0)) if v]
        return round(max(w), 4) if w else None

    def sluit_piek(self, k, t, koersen, reden="onder drempel", einde_run=False):
        p = self.pieken.pop(k)
        bod, laat = koersen.get(p["spot"], {}).get((p["munt"], p["spot_quote"])) or p.get("spot_laatst") or (0, 0) \
            if p["spot"] else (0, 0)
        spot_uit = (bod if p["richting"] == "positief" else laat) or None
        teken = 1 if p["richting"] == "positief" else -1
        basis = None
        if p["spot_in"] and spot_uit and p["prijs_perp_in"] and p["prijs_perp_uit"]:
            # gedekt: spot gaat mee met de munt, de perp de andere kant op. Verhoudingen, dus 1000PEPE mag.
            basis = teken * ((spot_uit / p["spot_in"] - 1) - (p["prijs_perp_uit"] / p["prijs_perp_in"] - 1))
        kosten = 2 * (p["taker_perp"] + (p["taker_spot"] or 0)) if p["spot"] else None
        netto = p["ontvangen"] - kosten + (basis or 0) if kosten is not None else None
        positie = {i: i * 2 / 3 for i in INLEG}  # 2/3 spot, 1/3 onderpand voor de short bij 2x (GOK, zie README)
        regel = {x: p[x] for x in ("beurs", "munt", "richting", "uur", "verrekeningen", "vol_usd", "spot",
                                   "spot_quote", "taker_perp", "taker_spot", "min_spot_eur", "min_perp_eur",
                                   "spot_anders", "al_bij_start")}
        regel.update(
            begin=iso(p["begin_t"]), eind=iso(p["laatst_t"]), duur_s=round(p["laatst_t"] - p["begin_t"]),
            reden=reden, einde_run=einde_run, r8_begin_pct=round(p["r8_begin"] * 100, 4),
            r8_max_pct=round(p["max_r8"] * 100, 4), r8_med_pct=round(statistics.median(p["r8s"]) * 100, 4),
            ontvangen_pct=round(p["ontvangen"] * 100, 4), kosten_pct=round(kosten * 100, 4) if kosten is not None
            else None, basis_pct=round(basis * 100, 4) if basis is not None else None,
            netto_pct=round(netto * 100, 4) if netto is not None else None,
            **{f"winst{i}": round(netto * positie[i], 2) if netto is not None else None for i in INLEG})
        with open(os.path.join(self.uit, "funding.jsonl"), "a") as fh:
            fh.write(json.dumps(regel, ensure_ascii=False) + "\n")
        self.stand["pieken_gesloten"] += 1

    # ---------- C: stablecoins ----------
    def stable_paren(self):
        """Alle stablecoin-paren (munt in STABLE, quote EUR, USD, USDT of USDC) per beurs, plus EUR/USD als referentie."""
        uit = set()
        for b, p in self.paren.items():
            for (m, q) in p:
                if (m in STABLE and q in QUOTE_FIAT and m != q) or (m, q) == ("EUR", "USD"):
                    uit.add((b, m, q))
        return uit

    def ronde_stable(self):
        """Elke 15 s: per beurs in één verzoek bod en laat van alle paren (zoals de scanner). Alleen waar de ticker
        een afwijking of een gat tussen beurzen laat zien, halen we het orderboek (hooguit MAX_BOEK_PER_BEURS per
        beurs per ronde, open momenten eerst), zodat we ruim binnen de limieten blijven (Kraken: ±1 per seconde)."""
        t = nu_s()
        lijst = self.stable_paren()
        welke = {b for b, _, _ in lijst}
        res = self.parallel({(b, "koersen"): (self.spot[b].koersen, ()) for b in welke}, timeout=30)
        tick = {}
        for (b, _), ks in res.items():
            for (m, q), (bod, laat) in ks.items():
                if (b, m, q) in lijst and bod > 0 and laat > 0:
                    tick[(b, m, q)] = (bod, laat)
        self.werk_koersen_bij(tick)
        # kandidaten uit de ticker
        kand_c1, kand_c2 = {}, {}
        per = {}
        for (b, m, q), (bod, laat) in tick.items():
            if m == "EUR":
                continue
            per.setdefault((m, q), []).append(b)
            ref = peg(m, q, self.eurusd)
            if ref:
                afw = max((ref - laat) / ref, (bod - ref) / ref)
                if afw >= DREMPEL_STABLE:
                    kand_c2[(b, m, q)] = afw
        for (m, q), bs in per.items():
            for koop in bs:
                for verkoop in bs:
                    if koop != verkoop:
                        laat, bod = tick[(koop, m, q)][1], tick[(verkoop, m, q)][0]
                        if bod > laat * (1 + self.taker(koop, m, q) + self.taker(verkoop, m, q)):
                            kand_c1[(m, q, koop, verkoop)] = bod / laat - 1
        # welke boeken: open momenten eerst, dan grootste afwijking; per beurs hooguit MAX_BOEK_PER_BEURS
        wens = []
        for k in self.volg_c2.open:
            wens.append((0, (k[0], k[1], k[2])))
        for k in self.volg_c1.open:
            wens += [(0, (k[2], k[0], k[1])), (0, (k[3], k[0], k[1]))]
        wens += [(-v, k) for k, v in kand_c2.items()]
        for (m, q, a, b), v in kand_c1.items():
            wens += [(-v, (a, m, q)), (-v, (b, m, q))]
        gekozen, per_beurs = [], collections.Counter()
        for _, k in sorted(wens):
            if k in gekozen or k not in tick:
                continue
            if per_beurs[k[0]] < MAX_BOEK_PER_BEURS:
                gekozen.append(k)
                per_beurs[k[0]] += 1
        res = self.parallel({(b, "boek", m, q): (self.spot[b].boek, (self.paren[b][(m, q)]["id"],))
                             for b, m, q in gekozen}, timeout=30)
        boeken = {(b, m, q): v for (b, _, m, q), v in res.items() if v and v[0] and v[1]}
        self.stand["stable_boeken"] += len(boeken)
        # C1 tussen beurzen. Bekeken = de ticker zegt "geen gat" of we hebben beide boeken.
        bekeken, kansen = set(), {}
        for (m, q), bs in per.items():
            for koop in bs:
                for verkoop in bs:
                    if koop == verkoop:
                        continue
                    sl = (m, q, koop, verkoop)
                    ba, bv = boeken.get((koop, m, q)), boeken.get((verkoop, m, q))
                    if sl not in kand_c1:
                        bekeken.add(sl)
                        continue
                    if not ba or not bv:
                        continue
                    bekeken.add(sl)
                    r, vast = self.reken_paar(m, q, koop, verkoop, ba, bv)
                    if scanner.is_kans(r):
                        kansen[sl] = (r, vast)
        self.volg_c1.stap(t, bekeken, kansen)
        # C2 los van de koppeling
        bekeken2, kansen2 = set(), {}
        for (b, m, q) in tick:
            if m == "EUR":
                continue
            if (b, m, q) not in kand_c2:
                bekeken2 |= {(b, m, q, "goedkoop"), (b, m, q, "duur")}
                continue
            boek = boeken.get((b, m, q))
            if not boek:
                continue
            bekeken2 |= {(b, m, q, "goedkoop"), (b, m, q, "duur")}
            r = afwijking(boek[1], boek[0], peg(m, q, self.eurusd), self.taker(b, m, q), DREMPEL_STABLE,
                          self.eur.get(q, 0) or 1.0)
            if r:
                kansen2[(b, m, q, r["kant"])] = (r, {"beurs": b, "munt": m, "quote": q, "kant": r["kant"],
                                                     "taker": self.taker(b, m, q), "eurusd": self.eurusd,
                                                     "min_order_eur": self.min_order_eur(b, m, q, r["prijs"])})
        self.volg_c2.stap(t, bekeken2, kansen2)
        self.stand["rondes"]["stable"] += 1

    def werk_koersen_bij(self, tick):
        """EUR/USD (referentie voor C2) en euro per USDT/USDC/USD (alleen om winst in euro te tonen)."""
        def mid(b, m, q):
            v = tick.get((b, m, q))
            return (v[0] + v[1]) / 2 if v else None
        eurusd = mid("kraken", "EUR", "USD") or mid("bitstamp", "EUR", "USD")
        if eurusd:
            self.eurusd = eurusd
            self.eur["USD"] = 1 / eurusd
        for st in ("USDT", "USDC"):
            v = mid("kraken", st, "EUR") or mid("bitvavo", st, "EUR")
            if v:
                self.eur[st] = v
        self.eur.setdefault("USDC", self.eur.get("USDT", 0))

    # ---------- lus ----------
    def schrijf_stand(self):
        regel = {"t": iso(nu_s()), "beurzen_paren": len(self.paren), "gevolgd": len(self.gevolgd),
                 "noteringen": self.stand["noteringen"], "open_a": len(self.volg_a.open),
                 "pieken_open": len(self.pieken), "pieken_gesloten": self.stand["pieken_gesloten"],
                 "open_c1": len(self.volg_c1.open), "open_c2": len(self.volg_c2.open),
                 "stable_paren": len(self.stable_paren()), "eurusd": self.eurusd, "eur_per_usdt": self.eur.get("USDT"),
                 "perps": {b: len(d) for b, d in self._perp_tellers().items()}, "rondes": dict(self.stand["rondes"])}
        with open(os.path.join(self.uit, "stand.jsonl"), "a") as fh:
            fh.write(json.dumps(regel) + "\n")
        self.log(f"{regel['t']} beurzen={regel['beurzen_paren']} noteringen={regel['noteringen']} "
                 f"gevolgd={regel['gevolgd']} A_open={regel['open_a']} pieken_open={regel['pieken_open']} "
                 f"pieken_dicht={regel['pieken_gesloten']} C1_open={regel['open_c1']} C2_open={regel['open_c2']} "
                 f"stablepaar={regel['stable_paren']}")

    def _perp_tellers(self):
        uit = {}
        for (b, _m) in self.funding_vorig:
            uit.setdefault(b, []).append(1)
        return uit

    def draai(self, minuten):
        eind = nu_s() + minuten * 60
        taken = (("paren", ELKE_PAREN_S, self.ronde_paren), ("wallet", ELKE_WALLET_S,
                 lambda: (self.ververs_wallets(list(self.spot)), self.ververs_minima())), ("stable", ELKE_STABLE_S, self.ronde_stable),
                 ("funding", ELKE_FUNDING_S, self.ronde_funding), ("noteringen", ELKE_NOTERING_S, self.ronde_noteringen),
                 ("stand", 300, self.schrijf_stand))
        try:
            while nu_s() < eind:
                for naam, elke, fn in taken:
                    if nu_s() >= self.volgend[naam]:
                        self.volgend[naam] = nu_s() + elke
                        try:
                            fn()
                        except Exception as e:  # één mislukte ronde mag de meting niet stoppen
                            self.fout("radar", naam, e)
                time.sleep(max(0.5, min(self.volgend.values()) - nu_s()))
        finally:
            self.afsluiten()

    def afsluiten(self):
        t = nu_s()
        for k in list(self.pieken):
            self.sluit_piek(k, t, {}, reden="einde run", einde_run=True)
        for v in (self.volg_a, self.volg_c1, self.volg_c2):
            v.sluit_alles()
        if self.ooit:
            self.bewaar_lijst()
        with open(os.path.join(self.uit, "samenvatting.json"), "w") as fh:
            json.dump({"eind": iso(t), **self.stand, "a_gesloten": self.volg_a.gesloten,
                       "c1_gesloten": self.volg_c1.gesloten, "c2_gesloten": self.volg_c2.gesloten}, fh, indent=1)
        self.pool.shutdown(wait=False, cancel_futures=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minuten", type=float, default=10)
    ap.add_argument("--uit", default="data")
    ap.add_argument("--vorige", default=None, help="paren-laatst.json van de vorige run (lijst munten per beurs)")
    a = ap.parse_args()
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))
    signal.signal(signal.SIGINT, lambda *_: sys.exit(0))
    r = Radar(a.uit, a.vorige, log=lambda x: print(x, flush=True))
    r.draai(a.minuten)
    print(json.dumps(r.stand, indent=1))


if __name__ == "__main__":
    main()
