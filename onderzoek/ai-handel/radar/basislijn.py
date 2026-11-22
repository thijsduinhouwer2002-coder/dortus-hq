"""Slotkoersen per dag (OHLC) van een spotpaar, uit openbare API's. Voor de basislijn van stablecoins bij C2: waar
staat een munt normaal? EURQ stond de laatste 45 dagen rond 0,97 euro (keuring A8): 1% onder de euro is daar geen
afwijking, maar gewoon de prijs. Geen account, alleen lezen.

  dagslot(beurs, symbool) -> [(dag als epoch s, slotkoers), ...]   alleen hele dagen (vandaag niet), oud naar nieuw
"""
import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scanner"))
import beurzen  # noqa: E402

f, haal = beurzen.f, beurzen.haal
# Volgorde waarin we een bron voor de basislijn zoeken: eerst de beurzen met veel stablecoin-paren.
BRONNEN = ("kraken", "bitvavo", "okx", "gate", "mexc", "bitget", "kucoin")


def _vandaag():
    return int(time.time()) // 86400 * 86400


def dagslot(beurs, sym, dagen=45):
    if beurs == "kraken":
        r = haal(f"https://api.kraken.com/0/public/OHLC?pair={sym}&interval=1440")["result"]
        rijen = [(int(x[0]), f(x[4])) for k, v in r.items() if k != "last" for x in v]
    elif beurs == "bitvavo":
        rijen = [(int(x[0]) // 1000, f(x[4])) for x in haal(f"https://api.bitvavo.com/v2/{sym}/candles?interval=1d"
                                                            f"&limit={dagen + 2}")]
    elif beurs == "okx":
        rijen = [(int(x[0]) // 1000, f(x[4])) for x in
                 haal(f"https://www.okx.com/api/v5/market/candles?instId={sym}&bar=1Dutc&limit={dagen + 2}")["data"]]
    elif beurs == "gate":
        rijen = [(int(x[0]), f(x[2])) for x in
                 haal(f"https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair={sym}&interval=1d"
                      f"&limit={dagen + 2}")]
    elif beurs == "mexc":
        rijen = [(int(x[0]) // 1000, f(x[4])) for x in
                 haal(f"https://api.mexc.com/api/v3/klines?symbol={sym}&interval=1d&limit={dagen + 2}")]
    elif beurs == "bitget":
        rijen = [(int(x[0]) // 1000, f(x[4])) for x in
                 haal(f"https://api.bitget.com/api/v2/spot/market/candles?symbol={sym}&granularity=1day"
                      f"&limit={dagen + 2}")["data"]]
    elif beurs == "kucoin":
        rijen = [(int(x[0]), f(x[2])) for x in
                 haal(f"https://api.kucoin.com/api/v1/market/candles?type=1day&symbol={sym}")["data"]]
    else:
        return []
    vandaag = _vandaag()
    rijen = sorted((t // 86400 * 86400, c) for t, c in rijen if c > 0 and t < vandaag)
    return rijen[-dagen:]
