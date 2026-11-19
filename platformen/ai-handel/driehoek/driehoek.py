#!/usr/bin/env python3
"""Driehoek-meter: bestaan er binnen één beurs driehoeken (bijv. EUR > BTC > ETH > EUR) met winst na kosten?

Onderzoek voor Thijs zelf, geen Dortus-product en geen advies. Alleen openbare API's: geen account, geen sleutel,
geen handel, geen geld. Uitleg: README.md, keuzes: ontwerp.md.

Per beurs een eigen draad met een eigen ritme:
  1. bod en laat van alle paren in één verzoek (de koppelingen van ../scanner/beurzen.py);
  2. elke driehoek in beide richtingen doorrekenen tegen de beste prijzen met de takerkosten per stap;
  3. alleen waar dat winst geeft: de drie orderboeken ophalen en aflopen (diepte, niet alleen de beste prijs);
  4. een driehoek met winst op het boek volgen tot hij weg is, en dan één regel wegschrijven.

Gebruik:  python3 driehoek.py --minuten 10 --uit /tmp/dh/2026-11-19/run-1
Schrijft in --uit: driehoeken.jsonl (één regel per driehoek met winst), stand.jsonl (elke ±5 minuten per beurs),
beurzen.json (paren, driehoeken, kosten) en samenvatting.json (aan het eind).
"""
import argparse
import itertools
import json
import os
import signal
import statistics
import sys
import threading
import time
import urllib.error

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(HIER, "..", "scanner"))   # achteraan: eigen rapport.py gaat voor
import beurzen as B  # noqa: E402


class _Alles:
    """De scanner neemt alleen paren met quote USDT, USDC, EUR of USD. Voor driehoeken zijn ook paren als ETH-BTC
    nodig; dit zet die grens open (de koppelingen kijken met `in QUOTES`)."""
    def __contains__(self, x):
        return bool(x)


B.QUOTES = _Alles()

# Vergunning (ESMA-register, 19 nov 2026, zie ../scanner/README.md). "MiCA-dochter": de vergunning hoort bij een
# EU-dochter met een eigen site; de API die we meten is de wereldwijde versie.
STATUS = {"bitvavo": "MiCA", "kraken": "MiCA", "bitstamp": "MiCA", "okx": "MiCA-dochter",
          "kucoin": "MiCA-dochter", "gate": "MiCA-dochter", "bitget": "grijs", "mexc": "grijs"}

# Ritme per beurs: seconden per ronde, hoeveel orderboeken per ronde, en minimale tijd tussen twee verzoeken.
# Grenzen van de openbare API (per IP), zie README.md. We blijven er ruim onder.
RITME = {
    "bitvavo": (4, 6, 0.2), "kraken": (5, 3, 1.0), "okx": (3, 10, 0.1), "kucoin": (3, 10, 0.1),
    "gate": (4, 8, 0.1), "bitget": (3, 10, 0.1), "mexc": (3, 10, 0.1), "bitstamp": (5, 6, 0.2),
}

FIAT = {"EUR", "USD", "GBP", "CAD", "AUD", "JPY", "CHF"}
STABIEL = {"USDT", "USDC", "DAI", "PYUSD", "EURC", "USDG", "RLUSD", "USD1", "TUSD", "USDE", "FDUSD", "EURQ",
           "EUROP", "EURCV", "USDQ", "USDS", "EURR", "USDR"}
VOORKEUR = ("EUR", "USDT", "USDC", "USD", "BTC", "ETH")
VASTE = (100, 150, 200, 500, 1000, 2000, 5000, 10000)
BEDRAGEN = sorted({round(10 * 1.25 ** i, 2) for i in range(41)} | set(VASTE))   # €10 tot ±€75.000
KLEIN = (100, 150, 200)
VERDACHT = 0.05      # meer dan 5% winst per rondje: bijna altijd een dode markt of een foute ticker
OPNIEUW_PAREN = 1800  # elke 30 minuten de lijst met paren verversen (nieuwe en gestopte markten)
STAND_ELKE = int(os.environ.get("DRIEHOEK_STAND_S", "300"))

EURK = {}            # gedeelde euro-koersen (munt -> euro per munt), gevuld door alle draden
SLOT = threading.Lock()


def nu():
    return time.time()


def iso(t):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))


# ---------------------------------------------------------------------------------------------------- kosten
def kosten(beurs, sleutel, info, bitvavo_cat=None):
    """Takerkosten van één paar als (hoog, laag, bron). Hoog = wat we voor waar aannemen; laag = alleen anders
    als het tarief onzeker is (bovengrens voor de winst). Bronnen staan in README.md."""
    b, q = sleutel
    if beurs == "kraken":
        if b in FIAT | STABIEL and q in FIAT | STABIEL:
            return 0.002, 0.002, "GEZIEN kraken.com/pro/fees: FX en stablecoin 0,20%"
        return 0.008, 0.008, "GEZIEN kraken.com/pro/fees: crypto 0,80% (tier 1)"
    if beurs == "bitvavo":
        if (bitvavo_cat or "A") == "A":
            return 0.0025, 0.0025, "GEZIEN support.bitvavo.com: maximaal 0,25% taker"
        return 0.0025, 0.0, f"categorie {bitvavo_cat}: lager dan 0,25% volgens Bitvavo, getal onbekend (GOK)"
    if info.get("taker") is not None:
        return info["taker"], info["taker"], "GEZIEN uit de API, per paar"
    t = B.TAKER.get(beurs, 0.004)
    return t, t, "GOK standaardtarief laagste trede"


# ---------------------------------------------------------------------------------------------------- minima
def _getal(x):
    try:
        v = float(x)
        return v if v > 0 else 0.0
    except (TypeError, ValueError):
        return 0.0


def minima(naam):
    """Minimale ordergrootte per paar uit de openbare API: {(munt, quote): {"base", "quote", "usdt"}}.
    base = minimaal aantal munten, quote = minimaal bedrag in de quote, usdt = minimale waarde in USDT (Bitget).
    Geeft {} als de beurs het niet geeft of de API faalt; dan rekenen we zonder minimum (staat in de data)."""
    n, h, uit = B.norm, B.haal, {}
    if naam == "bitvavo":
        for m in h(f"{B.Bitvavo.B}/markets"):
            uit[(n(m["base"]), n(m["quote"]))] = {"base": _getal(m.get("minOrderInBaseAsset")),
                                                  "quote": _getal(m.get("minOrderInQuoteAsset"))}
    elif naam == "kraken":
        for p in h(f"{B.Kraken.B}/AssetPairs")["result"].values():
            if "/" in p.get("wsname", ""):
                b, q = p["wsname"].split("/")
                uit[(n(b), n(q))] = {"base": _getal(p.get("ordermin")), "quote": _getal(p.get("costmin"))}
    elif naam == "okx":
        for i in h(f"{B.Okx.B}/public/instruments?instType=SPOT")["data"]:
            uit[(n(i["baseCcy"]), n(i["quoteCcy"]))] = {"base": _getal(i.get("minSz"))}
    elif naam == "kucoin":
        for x in h(f"{B.Kucoin.B}/v2/symbols")["data"]:
            uit[(n(x["baseCurrency"]), n(x["quoteCurrency"]))] = {
                "base": _getal(x.get("baseMinSize")), "quote": max(_getal(x.get("quoteMinSize")), _getal(x.get("minFunds")))}
    elif naam == "gate":
        for p in h(f"{B.Gate.B}/spot/currency_pairs"):
            uit[(n(p["base"]), n(p["quote"]))] = {"base": _getal(p.get("min_base_amount")),
                                                  "quote": _getal(p.get("min_quote_amount"))}
    elif naam == "bitget":
        for x in h(f"{B.Bitget.B}/public/symbols")["data"]:
            uit[(n(x["baseCoin"]), n(x["quoteCoin"]))] = {"base": _getal(x.get("minTradeAmount")),
                                                          "usdt": _getal(x.get("minTradeUSDT"))}
    elif naam == "mexc":
        for x in h(f"{B.Mexc.B}/exchangeInfo")["symbols"]:
            uit[(n(x["baseAsset"]), n(x["quoteAsset"]))] = {"base": _getal(x.get("baseSizePrecision")),
                                                            "quote": _getal(x.get("quoteAmountPrecisionMarket")
                                                                            or x.get("quoteAmountPrecision"))}
    elif naam == "bitstamp":
        for m in h(f"{B.Bitstamp.B}/trading-pairs-info/"):
            if "/" not in m.get("name", ""):
                continue
            b, q = (n(x) for x in m["name"].split("/"))
            delen = str(m.get("minimum_order", "")).split()
            if len(delen) == 2:
                uit[(b, q)] = {"quote": _getal(delen[0])} if n(delen[1]) == q else {"base": _getal(delen[0])}
    return uit


# ---------------------------------------------------------------------------------------------------- rekenen
def loop(kant, bedrag, koop):
    """Loop één kant van het boek af. koop: bedrag in quote, kant = laten, uit = basismunt.
    Verkoop: bedrag in basismunt, kant = biedingen, uit = quote. None als het opgehaalde boek te dun is."""
    uit = 0.0
    for prijs, hv in kant:
        if koop:
            k = prijs * hv
            if bedrag <= k:
                return uit + bedrag / prijs
            uit += hv
            bedrag -= k
        else:
            if bedrag <= hv:
                return uit + bedrag * prijs
            uit += hv * prijs
            bedrag -= hv
    return None


def rondje(stappen, boeken, x, scen, x_eur=None):
    """Stuur x begin-munten door de drie stappen. Geeft (wat er terugkomt na kosten, past) of (None, False).
    past = elke stap haalt de minimale ordergrootte van de beurs (munten, quote-bedrag, en bij Bitget de
    waarde in USDT, via x_eur benaderd)."""
    a = x
    past = True
    for st in stappen:
        bied, laat = boeken[st["paar"]]
        b = loop(laat if st["koop"] else bied, a, st["koop"])
        if b is None:
            return None, False
        munten, quote = (b, a) if st["koop"] else (a, b)
        mn = st.get("min") or {}
        if munten < mn.get("base", 0) or quote < mn.get("quote", 0):
            past = False
        if mn.get("usdt") and x_eur is not None and x_eur < mn["usdt"] * EURK.get("USDT", 1.0):
            past = False
        a = b * (1 - st[scen])
    return a, past


def top(stappen, prijzen, scen):
    """Opbrengst per 1 begin-munt tegen de beste prijzen (bovengrens: verder in het boek wordt het slechter)."""
    m = 1.0
    for st in stappen:
        p = prijzen.get(st["sleutel"])
        if not p:
            return 0.0
        bod, laat = p
        if bod <= 0 or laat <= 0:
            return 0.0
        m *= (1 / laat if st["koop"] else bod) * (1 - st[scen])
    return m


def curve(stappen, boeken, eur_per_munt, scen):
    """Winst in euro bij elk bedrag van BEDRAGEN. Geeft None als er nergens winst is, anders een dict."""
    punten = []
    for e in BEDRAGEN:
        x = e / eur_per_munt
        terug, past = rondje(stappen, boeken, x, scen, e)
        if terug is None:
            break
        punten.append((e, (terug - x) * eur_per_munt, past))
    goed = [p for p in punten if p[2]]
    if not goed:
        return None
    best_e, best_w, _ = max(goed, key=lambda p: p[1])
    if best_w <= 0:
        return None
    winst_bij = {}
    for s in VASTE:
        w = [p[1] for p in goed if p[0] <= s and p[1] > 0]
        winst_bij[str(s)] = round(max(w), 4) if w else 0.0
    return {"winst_eur": round(best_w, 4), "best_eur": best_e,
            # diepte: het kleinste bedrag waarmee je (bijna) alle winst pakt; meer erin levert niets meer op
            "diepte_eur": min(p[0] for p in goed if p[1] >= 0.99 * best_w),
            "min_inleg_eur": min(p[0] for p in goed),
            "pct": round(100 * best_w / best_e, 4), "boek_op": len(punten) < len(BEDRAGEN),
            "winst_bij": winst_bij}


def min_inleg(stappen, prijzen, eur_per_munt):
    """Kleinste bedrag uit BEDRAGEN waarbij alle drie stappen de minimale ordergrootte halen, tegen de beste
    prijzen (boek met oneindige diepte). None als het niet te rekenen is."""
    boeken = {}
    for st in stappen:
        p = prijzen.get(st["sleutel"])
        if not p or p[0] <= 0 or p[1] <= 0:
            return None
        boeken[st["paar"]] = ([(p[0], float("inf"))], [(p[1], float("inf"))])
    for e in BEDRAGEN:
        terug, past = rondje(stappen, boeken, e / eur_per_munt, "hoog", e)
        if terug is not None and past:
            return e
    return None


def driehoeken(paren):
    """Alle driehoeken van 3 munten waarvan elk paar op de beurs bestaat, in beide richtingen.
    Geeft lijst van (begin, [m1, m2, m3]) met de munten in volgorde (begin > m2 > m3 > begin)."""
    buren = {}
    for (b, q) in paren:
        buren.setdefault(b, set()).add(q)
        buren.setdefault(q, set()).add(b)
    gezien = set()
    for a in buren:
        for x, y in itertools.combinations(sorted(buren[a]), 2):
            if y in buren.get(x, ()):
                gezien.add(frozenset((a, x, y)))
    uit = []
    for d in sorted(gezien, key=sorted):
        ms = sorted(d, key=lambda m: (VOORKEUR.index(m) if m in VOORKEUR else len(VOORKEUR), m))
        s, x, y = ms
        uit.append([s, x, y])
        uit.append([s, y, x])
    return uit


def maak_stappen(volgorde, paren, kosten_van, mins=None):
    st = []
    for van, naar in zip(volgorde, volgorde[1:] + volgorde[:1]):
        if (van, naar) in paren:
            sl, koop = (van, naar), False          # verkoop van basismunt tegen het bod
        elif (naar, van) in paren:
            sl, koop = (naar, van), True           # koop van basismunt tegen de laat
        else:
            return None
        hoog, laag, _ = kosten_van[sl]
        st.append({"sleutel": sl, "paar": paren[sl]["id"], "koop": koop, "hoog": hoog, "laag": laag,
                   "min": (mins or {}).get(sl) or {}})
    return st


def mid(p):
    return (p[0] + p[1]) / 2 if p and p[0] > 0 and p[1] > 0 else None


def eur_koers(munt, prijzen):
    if munt == "EUR":
        return 1.0
    m = mid(prijzen.get((munt, "EUR")))
    if m:
        return m
    m = mid(prijzen.get(("EUR", munt)))
    if m:
        return 1 / m
    if EURK.get(munt):
        return EURK[munt]
    for q in ("USDT", "USDC", "USD", "BTC", "ETH"):
        m = mid(prijzen.get((munt, q)))
        if m and q != munt and EURK.get(q):
            return m * EURK[q]
    return None


# ---------------------------------------------------------------------------------------------------- schrijven
class Schrijver:
    def __init__(self, uit):
        self.uit = uit
        os.makedirs(uit, exist_ok=True)
        self.slot = threading.Lock()

    def regel(self, naam, d):
        with self.slot, open(os.path.join(self.uit, naam), "a") as fh:
            fh.write(json.dumps(d, ensure_ascii=False) + "\n")

    def bestand(self, naam, d):
        with self.slot, open(os.path.join(self.uit, naam), "w") as fh:
            json.dump(d, fh, ensure_ascii=False, indent=1)


# ---------------------------------------------------------------------------------------------------- meter
class Meter(threading.Thread):
    def __init__(self, beurs, schrijver, stop):
        super().__init__(daemon=True)
        self.b = beurs
        self.naam = beurs.naam
        self.s = schrijver
        self.stop = stop
        self.ritme, self.max_boeken, self.tussen = RITME.get(self.naam, (5, 5, 0.2))
        self.open = {}
        self.niet = {}      # driehoek -> prijzen bij de laatste boekcontrole zonder winst (zelfde prijzen: overslaan)
        self.cycli = []
        self.info = {"paren": 0, "driehoeken": 0, "kosten": {}, "fout": None}
        self.tel = self._leeg()
        self.totaal = {"rondes": 0, "fouten": 0, "boeken": 0, "driehoeken": 0, "echt_ruw": 0}
        self.laatste_verzoek = 0.0
        self.pauze_tot = 0.0
        self.foutreeks = 0

    @staticmethod
    def _leeg():
        return {"rondes": 0, "fouten": 0, "te_veel": 0, "boeken": 0, "kandidaten": 0, "bekeken": 0,
                "overgeslagen": 0, "zelfde": 0, "boek_winst": 0, "beste_marge": [], "ronde_s": [], "ticker_s": []}

    # verzoeken met een minimale tussentijd per beurs
    def _wacht(self):
        d = self.laatste_verzoek + self.tussen - nu()
        if d > 0:
            time.sleep(d)
        self.laatste_verzoek = nu()

    def laad(self):
        self._wacht()
        paren = self.b.paren()
        cat = {}
        if self.naam == "bitvavo":
            self._wacht()
            for m in B.haal(f"{B.Bitvavo.B}/markets"):
                cat[(B.norm(m["base"]), B.norm(m["quote"]))] = m.get("feeCategory")
        kv = {sl: kosten(self.naam, sl, inf, cat.get(sl)) for sl, inf in paren.items()}
        self._wacht()
        try:
            mins = minima(self.naam)
        except Exception as e:  # noqa: BLE001 (zonder minima meten we door; staat in beurs-<naam>.json)
            mins, self.info["fout"] = {}, f"minima: {type(e).__name__} {str(e)[:100]}"
        cycli = []
        for volgorde in driehoeken(paren):
            st = maak_stappen(volgorde, paren, kv, mins)
            if st:
                cycli.append({"id": ">".join(volgorde + volgorde[:1]), "munten": volgorde, "stappen": st})
        self.paren, self.cycli = paren, cycli
        bronnen = {}
        for sl, (h, l, bron) in kv.items():
            bronnen.setdefault(bron, [h, l, 0])[2] += 1
        self.info = {"paren": len(paren), "driehoeken": len(cycli), "status": STATUS.get(self.naam, "grijs"),
                     "ritme_s": self.ritme, "max_boeken": self.max_boeken,
                     "kosten": {b: {"hoog": h, "laag": l, "paren": n} for b, (h, l, n) in bronnen.items()},
                     "minima_paren": sum(1 for sl in paren if mins.get(sl)), "geladen": iso(nu())}
        self.geladen = nu()
        self.min_klaar = False

    def _fout(self, e):
        self.tel["fouten"] += 1
        self.totaal["fouten"] += 1
        self.foutreeks += 1
        code = getattr(e, "code", None)
        if code in (418, 429, 403):
            self.tel["te_veel"] += 1
        wacht = min(120, 5 * 2 ** min(self.foutreeks, 5)) if code in (418, 429, 403) else min(60, 2 * self.foutreeks)
        self.pauze_tot = nu() + wacht
        self.info["fout"] = f"{iso(nu())} {type(e).__name__} {code or ''} {str(e)[:120]}"
        # een gat van meer dan een minuut: open driehoeken sluiten, we weten niet wat er gebeurde
        if self.foutreeks >= 3 or wacht >= 60:
            for cid in list(self.open):
                self._sluit(cid, "fout")

    def run(self):
        while not self.stop.is_set():
            try:
                if not self.cycli or nu() - self.geladen > OPNIEUW_PAREN:
                    self.laad()
                    self.s.bestand(f"beurs-{self.naam}.json", self.info)
                self.ronde()
                self.foutreeks = 0
            except Exception as e:  # noqa: BLE001 (één beurs mag de rest niet stoppen)
                self._fout(e)
            wacht = max(self.pauze_tot - nu(), 0)
            self.stop.wait(wacht)
        for cid in list(self.open):
            self._sluit(cid, "stop")

    def ronde(self):
        t0 = nu()
        self._wacht()
        prijzen = self.b.koersen()
        t1 = nu()
        for (b, q), p in prijzen.items():
            if q == "EUR" and b in ("USDT", "USDC", "USD", "BTC", "ETH") and mid(p):
                EURK[b] = mid(p)
            elif b == "EUR" and q in ("USD", "USDT", "USDC") and mid(p):
                EURK[q] = 1 / mid(p)
        if not self.min_klaar:
            self.min_klaar = True
            self.info["min_inleg"] = self.min_overzicht(prijzen)
            self.s.bestand(f"beurs-{self.naam}.json", self.info)
        kand = []
        beste = 0.0
        for c in self.cycli:
            ml = top(c["stappen"], prijzen, "laag")
            if ml > 1 or c["id"] in self.open:
                kand.append((c["id"] in self.open, ml, c))
            mh = ml if all(s["laag"] == s["hoog"] for s in c["stappen"]) else top(c["stappen"], prijzen, "hoog")
            if 0 < mh < 1 + VERDACHT:
                beste = max(beste, mh)
        if beste:
            self.tel["beste_marge"].append(round((beste - 1) * 100, 4))
        # open driehoeken die met de beste prijzen geen winst meer geven: weg
        ids = {c["id"] for o, ml, c in kand if ml > 1}
        for cid in list(self.open):
            if cid not in ids:
                self._sluit(cid, "ticker")
        kand = [k for k in kand if k[1] > 1]
        kand.sort(key=lambda k: (not k[0], -k[1]))
        self.tel["kandidaten"] += len(kand)
        boeken = {}
        eurs = {}
        for _, ml, c in kand:
            sleutel = tuple(prijzen.get(st["sleutel"]) for st in c["stappen"])
            if self.niet.get(c["id"]) == sleutel:
                self.tel["zelfde"] += 1      # ticker niet veranderd sinds het boek "geen winst" zei
                continue
            nodig = [s["paar"] for s in c["stappen"] if s["paar"] not in boeken]
            if len(boeken) + len(nodig) > self.max_boeken:
                self.tel["overgeslagen"] += 1
                continue
            try:
                for p in nodig:
                    self._wacht()
                    boeken[p] = self.b.boek(p)
                    self.tel["boeken"] += 1
                    self.totaal["boeken"] += 1
            except urllib.error.HTTPError as e:
                if e.code in (418, 429, 403):
                    raise
                continue
            except Exception:  # noqa: BLE001 (één boek dat niet komt: deze driehoek overslaan)
                continue
            self.tel["bekeken"] += 1
            beg = c["munten"][0]
            if beg not in eurs:
                eurs[beg] = eur_koers(beg, prijzen)
            if not eurs[beg]:
                continue
            if self.verwerk(c, boeken, eurs[beg], t1):
                self.niet.pop(c["id"], None)
            else:
                self.niet[c["id"]] = sleutel
        self.tel["rondes"] += 1
        self.totaal["rondes"] += 1
        self.tel["ronde_s"].append(nu() - t0)
        self.tel["ticker_s"].append(t1 - t0)
        rest = self.ritme - (nu() - t0)
        if rest > 0:
            self.stop.wait(rest)

    def min_overzicht(self, prijzen):
        """Hoeveel driehoeken op deze beurs kun je met €100, €150 of €200 rondmaken (minimale ordergrootte)?"""
        mi = []      # (heeft EUR, kleinste inleg in euro of oneindig)
        for c in self.cycli:
            e = eur_koers(c["munten"][0], prijzen)
            if e:
                m = min_inleg(c["stappen"], prijzen, e)
                mi.append(("EUR" in c["munten"], m if m is not None else float("inf")))
        md = statistics.median([m for _, m in mi]) if mi else None
        uit = {"driehoeken": len(mi), "mediaan_eur": md if md not in (None, float("inf")) else None,
               "met_eur": sum(1 for e, _ in mi if e)}
        for k in KLEIN:
            uit[f"tot_{k}"] = sum(1 for _, m in mi if m <= k)
            uit[f"met_eur_tot_{k}"] = sum(1 for e, m in mi if e and m <= k)
        return uit

    def verwerk(self, c, boeken, eur_per_munt, t):
        laag = curve(c["stappen"], boeken, eur_per_munt, "laag")
        cid = c["id"]
        if not laag:
            if cid in self.open:
                self._sluit(cid, "boek")
            return False
        zelfde = all(s["laag"] == s["hoog"] for s in c["stappen"])
        hoog = laag if zelfde else curve(c["stappen"], boeken, eur_per_munt, "hoog")
        self.tel["boek_winst"] += 1
        g = self.open.get(cid)
        if g is None:
            g = self.open[cid] = {
                "beurs": self.naam, "status": STATUS.get(self.naam, "grijs"), "driehoek": cid,
                "paren": [s["paar"] for s in c["stappen"]], "kosten": [s["hoog"] for s in c["stappen"]],
                "kosten_laag": [s["laag"] for s in c["stappen"]], "zeker": zelfde, "ritme_s": self.ritme,
                "begin": t, "eind": t, "checks": 0, "hoog": None, "laag": None, "winsten": []}
        g["eind"] = t
        g["checks"] += 1
        for naam, r in (("laag", laag), ("hoog", hoog)):
            if not r:
                continue
            o = g[naam]
            if o is None:
                o = g[naam] = {"begin": t, "eind": t, "checks": 0, "winst_eur": 0, "diepte_eur": 0, "pct": 0,
                               "best_eur": 0, "min_inleg_eur": None, "boek_op": False, "winst_bij": {str(s): 0.0 for s in VASTE}}
            o["eind"] = t
            o["checks"] += 1
            if r["winst_eur"] > o["winst_eur"]:
                o.update(winst_eur=r["winst_eur"], best_eur=r["best_eur"], pct=r["pct"])
            o["diepte_eur"] = max(o["diepte_eur"], r["diepte_eur"])
            o["min_inleg_eur"] = r["min_inleg_eur"] if o["min_inleg_eur"] is None else min(o["min_inleg_eur"], r["min_inleg_eur"])
            o["boek_op"] |= r["boek_op"]
            for s, w in r["winst_bij"].items():
                o["winst_bij"][s] = max(o["winst_bij"][s], w)
            if naam == "hoog":
                g["winsten"].append(r["winst_eur"])
        return True

    def _sluit(self, cid, reden):
        g = self.open.pop(cid, None)
        if not g:
            return
        w = g.pop("winsten")
        for naam in ("laag", "hoog"):
            o = g[naam]
            if o:
                o["duur_s"] = round(o["eind"] - o["begin"], 1)
                o["begin"], o["eind"] = iso(o["begin"]), iso(o["eind"])
        g["winst_mediaan_eur"] = round(statistics.median(w), 4) if w else 0.0
        g["duur_s"] = round(g["eind"] - g["begin"], 1)
        g["begin"], g["eind"] = iso(g["begin"]), iso(g["eind"])
        g["eind_reden"] = reden
        g["verdacht"] = bool((g["laag"] or {}).get("pct", 0) > VERDACHT * 100)
        self.totaal["driehoeken"] += 1
        if g["hoog"]:
            self.totaal["echt_ruw"] += 1
        self.s.regel("driehoeken.jsonl", g)

    def stand(self):
        t, self.tel = self.tel, self._leeg()
        bm = t.pop("beste_marge")
        rs, ts = t.pop("ronde_s"), t.pop("ticker_s")
        t.update(beurs=self.naam, status=STATUS.get(self.naam, "grijs"), open=len(self.open),
                 paren=self.info.get("paren"), driehoeken=self.info.get("driehoeken"),
                 beste_marge_med=round(statistics.median(bm), 4) if bm else None,
                 beste_marge_max=max(bm) if bm else None,
                 ronde_s_med=round(statistics.median(rs), 2) if rs else None,
                 ticker_s_med=round(statistics.median(ts), 2) if ts else None, laatste_fout=self.info.get("fout"))
        return t


KLASSEN = {"bitvavo": B.Bitvavo, "kraken": B.Kraken, "okx": B.Okx, "kucoin": B.Kucoin, "gate": B.Gate,
           "bitget": B.Bitget, "mexc": B.Mexc, "bitstamp": B.Bitstamp}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minuten", type=float, default=10)
    ap.add_argument("--uit", required=True)
    ap.add_argument("--beurzen", default=",".join(KLASSEN))
    a = ap.parse_args()
    s = Schrijver(a.uit)
    stop = threading.Event()
    signal.signal(signal.SIGTERM, lambda *_: stop.set())
    signal.signal(signal.SIGINT, lambda *_: stop.set())
    meters = [Meter(KLASSEN[n](), s, stop) for n in a.beurzen.split(",") if n in KLASSEN]
    begin = nu()
    eind = begin + a.minuten * 60
    for m in meters:
        m.geladen = 0
        m.start()
        time.sleep(0.3)
    volgende = begin + STAND_ELKE
    while not stop.is_set() and nu() < eind:
        stop.wait(min(5, max(eind - nu(), 0)))
        if nu() >= volgende or stop.is_set() or nu() >= eind:
            volgende = nu() + STAND_ELKE
            for m in meters:
                r = m.stand()
                r["t"] = iso(nu())
                s.regel("stand.jsonl", r)
            print(iso(nu()), " ".join(f"{m.naam}:{m.totaal['rondes']}r/{m.totaal['boeken']}b/"
                                       f"{m.totaal['driehoeken']}d" for m in meters), flush=True)
    stop.set()
    for m in meters:
        m.join(timeout=30)
    s.bestand("beurzen.json", {"t": iso(nu()), "beurzen": {m.naam: m.info for m in meters}})
    s.bestand("samenvatting.json", {
        "begin": iso(begin), "eind": iso(nu()), "minuten": round((nu() - begin) / 60, 1),
        "beurzen": {m.naam: dict(m.totaal, status=STATUS.get(m.naam, "grijs"), paren=m.info.get("paren"),
                                 driehoeken_bekend=m.info.get("driehoeken"), laatste_fout=m.info.get("fout"))
                    for m in meters}})


if __name__ == "__main__":
    main()
