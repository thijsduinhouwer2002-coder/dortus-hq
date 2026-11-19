"""Kosten, minimale ordergrootte en stapgrootte per paar, en de vergunning per beurs. Bronnen: README.md.

Hergebruikt de koppelingen van ../scanner/beurzen.py en zet daar de grens op de quote open (de scanner kijkt
alleen naar USDT, USDC, EUR en USD; voor driehoeken zijn ook paren als ETH-BTC nodig).
"""
import math
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scanner"))  # achteraan: eigen bestanden gaan voor
import beurzen as B  # noqa: E402


class _Alles:
    """De koppelingen kijken met `in QUOTES`; dit laat elke quote door."""
    def __contains__(self, x):
        return bool(x)


B.QUOTES = _Alles()

# Vergunning (ESMA-register, 19 nov 2026, zie ../scanner/README.md). "MiCA-dochter": de vergunning hoort bij een
# EU-dochter met een eigen site; de API die we meten is de wereldwijde versie.
STATUS = {"bitvavo": "MiCA", "kraken": "MiCA", "bitstamp": "MiCA", "okx": "MiCA-dochter",
          "kucoin": "MiCA-dochter", "gate": "MiCA-dochter", "bitget": "grijs", "mexc": "grijs"}

FIAT = {"EUR", "USD", "GBP", "CAD", "AUD", "JPY", "CHF"}
STABIEL = {"USDT", "USDC", "DAI", "PYUSD", "EURC", "USDG", "RLUSD", "USD1", "TUSD", "USDE", "FDUSD", "EURQ",
           "EUROP", "EURCV", "USDQ", "USDS", "EURR", "USDR"}
# Kraken "pegged-token pairs" (voorbeeld op de tarievenpagina: TBTC/BTC). Staking-munten als LSETH/ETH en METH/ETH
# rekenen we voorzichtig als gewone cryptoparen (0,80%): de pagina noemt ze niet.
GEKOPPELD = {("TBTC", "BTC"), ("WBTC", "BTC")}

KRAKEN = "GEZIEN kraken.com/pro/fees 19 nov 2026"
BITSTAMP = "DERDEN tradingview.com/broker/Bitstamp"


def kosten(beurs, sleutel, info, bitvavo_cat=None):
    """Takerkosten van één paar als (hoog, laag, bron). Hoog = wat we voor waar aannemen; laag = alleen anders
    als het tarief onzeker is (bovengrens voor de winst)."""
    b, q = sleutel
    vast = FIAT | STABIEL
    if beurs == "kraken":
        if "USDE" in sleutel:
            return 0.0, 0.0, f"{KRAKEN}: alle USDe-paren 0%"
        if "USDG" in sleutel:
            return 0.0001, 0.0001, f"{KRAKEN}: USDG-paren 0,01%"
        if sleutel in GEKOPPELD:
            return 0.002, 0.002, f"{KRAKEN}: pegged-token paren 0,20%"
        if b in vast and q in vast:
            return 0.002, 0.002, f"{KRAKEN}: FX en stablecoin 0,20%"
        return 0.008, 0.008, f"{KRAKEN}: crypto 0,80% (tier 1)"
    if beurs == "bitvavo":
        if (bitvavo_cat or "A") == "A":
            return 0.0025, 0.0025, "GEZIEN support.bitvavo.com: maximaal 0,25% taker"
        return 0.0025, 0.0, f"categorie {bitvavo_cat}: lager dan 0,25% volgens Bitvavo, getal onbekend (GOK)"
    if beurs == "bitstamp":
        if b in vast and q in vast:
            return 0.0008, 0.0008, f"{BITSTAMP}: FX en stablecoin 80% korting op 0,40%"
        return 0.004, 0.004, f"{BITSTAMP}: 0,40% laagste trede"
    if beurs == "okx" and info.get("taker") is None:
        return 0.001, 0.001, "DERDEN okx.com/en-eu/fees: Regular user taker 0,10%"
    if info.get("taker") is not None:
        return info["taker"], info["taker"], "GEZIEN uit de API, per paar"
    t = B.TAKER.get(beurs, 0.004)
    return t, t, "GOK standaardtarief laagste trede"


def vaste_kosten_eur(beurs, sleutel):
    """Bitvavo rondt de kosten in euro naar boven af op de cent (support.bitvavo.com): tot €0,01 per stap."""
    return 0.01 if beurs == "bitvavo" and "EUR" in sleutel else 0.0


def _getal(x):
    try:
        v = float(x)
        return v if v > 0 else 0.0
    except (TypeError, ValueError):
        return 0.0


def _decimalen(d):
    try:
        return 10.0 ** -int(d)
    except (TypeError, ValueError):
        return 0.0


def minima(naam):
    """Uit de openbare API, per paar: {(munt, quote): {"base", "quote", "usdt", "stap"}}.
    base = minimaal aantal munten, quote = minimaal bedrag in de quote, usdt = minimale waarde in USDT (Bitget),
    stap = stapgrootte van het aantal munten (je koopt en verkoopt alleen veelvouden daarvan)."""
    n, h, uit = B.norm, B.haal, {}
    if naam == "bitvavo":
        for m in h(f"{B.Bitvavo.B}/markets"):
            uit[(n(m["base"]), n(m["quote"]))] = {"base": _getal(m.get("minOrderInBaseAsset")),
                                                  "quote": _getal(m.get("minOrderInQuoteAsset")),
                                                  "stap": _decimalen(m.get("quantityDecimals"))}
    elif naam == "kraken":
        for p in h(f"{B.Kraken.B}/AssetPairs")["result"].values():
            if "/" in p.get("wsname", ""):
                b, q = p["wsname"].split("/")
                uit[(n(b), n(q))] = {"base": _getal(p.get("ordermin")), "quote": _getal(p.get("costmin")),
                                     "stap": _decimalen(p.get("lot_decimals"))}
    elif naam == "okx":
        for i in h(f"{B.Okx.B}/public/instruments?instType=SPOT")["data"]:
            uit[(n(i["baseCcy"]), n(i["quoteCcy"]))] = {"base": _getal(i.get("minSz")), "stap": _getal(i.get("lotSz"))}
    elif naam == "kucoin":
        for x in h(f"{B.Kucoin.B}/v2/symbols")["data"]:
            uit[(n(x["baseCurrency"]), n(x["quoteCurrency"]))] = {
                "base": _getal(x.get("baseMinSize")), "quote": max(_getal(x.get("quoteMinSize")), _getal(x.get("minFunds"))),
                "stap": _getal(x.get("baseIncrement"))}
    elif naam == "gate":
        for p in h(f"{B.Gate.B}/spot/currency_pairs"):
            uit[(n(p["base"]), n(p["quote"]))] = {"base": _getal(p.get("min_base_amount")),
                                                  "quote": _getal(p.get("min_quote_amount")),
                                                  "stap": _decimalen(p.get("amount_precision"))}
    elif naam == "bitget":
        for x in h(f"{B.Bitget.B}/public/symbols")["data"]:
            uit[(n(x["baseCoin"]), n(x["quoteCoin"]))] = {"base": _getal(x.get("minTradeAmount")),
                                                          "usdt": _getal(x.get("minTradeUSDT")),
                                                          "stap": _decimalen(x.get("quantityPrecision"))}
    elif naam == "mexc":
        for x in h(f"{B.Mexc.B}/exchangeInfo")["symbols"]:
            uit[(n(x["baseAsset"]), n(x["quoteAsset"]))] = {
                "base": _getal(x.get("baseSizePrecision")),
                "quote": _getal(x.get("quoteAmountPrecisionMarket") or x.get("quoteAmountPrecision")),
                "stap": _decimalen(x.get("baseAssetPrecision"))}
    elif naam == "bitstamp":
        for m in h(f"{B.Bitstamp.B}/trading-pairs-info/"):
            if "/" in m.get("name", ""):
                uit[tuple(n(x) for x in m["name"].split("/"))] = bitstamp_minimum(m)
    return uit


def bitstamp_minimum(m):
    """Bitstamp: "minimum_order": "10.00 USD" (in de quote) of in de munt; base_decimals = stapgrootte."""
    b, q = (B.norm(x) for x in m["name"].split("/"))
    uit = {"stap": _decimalen(m.get("base_decimals"))}
    delen = str(m.get("minimum_order", "")).split()
    if len(delen) == 2:
        uit["quote" if B.norm(delen[1]) == q else "base"] = _getal(delen[0])
    return uit


def afronden(hoeveel, stap):
    """Naar beneden afronden op de stapgrootte (0 = geen stapgrootte bekend)."""
    if not stap:
        return hoeveel
    return math.floor(hoeveel / stap + 1e-9) * stap
