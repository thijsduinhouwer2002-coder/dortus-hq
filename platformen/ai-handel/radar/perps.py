"""Funding van perpetuals bij 9 beurzen, uit openbare API's. Geen account, geen sleutel, alleen lezen.

Per beurs één functie die in één of twee verzoeken alle USDT- of USD-perpetuals geeft:
  {munt: {"rate": funding per periode (fractie), "uur": lengte van de periode in uren,
          "volgende": tijdstip (epoch s) waarop deze rate verrekend wordt, "prijs": laatste of markprijs,
          "vol_usd": handel in 24 uur in dollar (0 als onbekend)}}

Welke rate: steeds de rate die bij de eerstvolgende verrekening betaald wordt (GEZIEN in de API-velden, zie
README.md). Binance en Bybit weigeren vanaf de server en waarschijnlijk vanaf GitHub (VS): niet gemeten.
Takerkosten op de perp (standaard laagste trede) staan in TAKER_PERP. GEZIEN in de contract-API (19 nov, curl,
veld takerFeeRate of taker_fee_rate bij BTC): Gate 0,075%, MEXC 0,02%, Bitget en KuCoin 0,06%, BingX 0,05%.
Kraken Futures 0,05%: DERDEN (de keurder zag het op kraken.com/pro/fees). OKX, Hyperliquid en dYdX: GOK.
"""
import json
import os
import re
import ssl
import sys
import time
import urllib.request

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scanner"))
import beurzen  # noqa: E402

TAKER_PERP = {"okx": 0.0005, "gate": 0.00075, "mexc": 0.0002, "bitget": 0.0006, "kucoin": 0.0006,
              "bingx": 0.0005, "kraken": 0.0005, "hyperliquid": 0.00045, "dydx": 0.0005}
# Welke spotbeurs bij de perpbeurs hoort (zelfde naam in beurzen.py). Hyperliquid en dYdX hebben geen spot die we
# meten: daar kiest de radar een andere spotbeurs (laagste takerkosten).
SPOT_ZELFDE = {"okx", "gate", "mexc", "bitget", "kucoin", "bingx", "kraken"}

_CTX = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE") or None)


def post(url, body, timeout=15):
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"User-Agent": beurzen.AGENT, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout, context=_CTX) as r:
        return json.loads(r.read())


f = beurzen.f
haal = beurzen.haal


def munt_naam(s):
    """BTC, XBT, kPEPE, 1000PEPE en 1000000MOG naar de naam op de spotbeurs. De prijs schaalt dan mee (1000x),
    maar de radar rekent alleen met verhoudingen (prijs later gedeeld door prijs eerder), dus dat maakt niet uit."""
    s = str(s or "").strip()
    if re.match(r"^k[A-Z0-9]{2,}$", s):
        s = s[1:]
    s = s.upper()
    m = re.match(r"^(1000000|100000|10000|1000|1M)([A-Z].*)$", s)
    if m:
        s = m.group(2)
    return beurzen.norm(s)


def volgend_heel_uur(t=None):
    t = time.time() if t is None else t
    return (int(t) // 3600 + 1) * 3600


def okx():
    uit = {}
    prijs = {}
    for t in haal("https://www.okx.com/api/v5/market/tickers?instType=SWAP")["data"]:
        prijs[t["instId"]] = (f(t.get("last")), f(t.get("volCcy24h")) * f(t.get("last")))
    for r in haal("https://www.okx.com/api/v5/public/funding-rate?instId=ANY")["data"]:
        iid = r.get("instId", "")
        if not iid.endswith("-USDT-SWAP") or r.get("fundingRate") in (None, ""):
            continue
        ft, nt = f(r.get("fundingTime")) / 1000, f(r.get("nextFundingTime")) / 1000
        p, v = prijs.get(iid, (0, 0))
        uit[munt_naam(iid.split("-")[0])] = {"rate": f(r["fundingRate"]), "uur": round((nt - ft) / 3600, 3) or 8,
                                              "volgende": ft, "prijs": p, "vol_usd": v}
    return uit


def bitget():
    B = "https://api.bitget.com/api/v2/mix/market"
    tick = {t["symbol"]: t for t in haal(f"{B}/tickers?productType=USDT-FUTURES")["data"]}
    uit = {}
    for r in haal(f"{B}/current-fund-rate?productType=USDT-FUTURES")["data"]:
        s = r["symbol"]
        if not s.endswith("USDT"):
            continue
        t = tick.get(s, {})
        uit[munt_naam(s[:-4])] = {"rate": f(r.get("fundingRate")), "uur": f(r.get("fundingRateInterval")) or 8,
                                  "volgende": f(r.get("nextUpdate")) / 1000, "prijs": f(t.get("lastPr")),
                                  "vol_usd": f(t.get("usdtVolume"))}
    return uit


def gate():
    B = "https://api.gateio.ws/api/v4/futures/usdt"
    vol = {t["contract"]: f(t.get("volume_24h_quote")) for t in haal(f"{B}/tickers")}
    uit = {}
    for c in haal(f"{B}/contracts"):
        if c.get("in_delisting") or c.get("status", "trading") != "trading" or not c["name"].endswith("_USDT"):
            continue
        uit[munt_naam(c["name"][:-5])] = {"rate": f(c.get("funding_rate")),
                                          "uur": f(c.get("funding_interval")) / 3600 or 8,
                                          "volgende": f(c.get("funding_next_apply")), "prijs": f(c.get("last_price")),
                                          "vol_usd": vol.get(c["name"], 0.0)}
    return uit


def mexc():
    B = "https://contract.mexc.com/api/v1/contract"
    tick = {t["symbol"]: t for t in haal(f"{B}/ticker")["data"]}
    uit = {}
    for r in haal(f"{B}/funding_rate")["data"]:
        s = r["symbol"]
        if not s.endswith("_USDT"):
            continue
        t = tick.get(s, {})
        uit[munt_naam(s[:-5])] = {"rate": f(r.get("fundingRate")), "uur": f(r.get("collectCycle")) or 8,
                                  "volgende": f(r.get("nextSettleTime")) / 1000, "prijs": f(t.get("lastPrice")),
                                  "vol_usd": f(t.get("amount24"))}
    return uit


def kucoin():
    uit = {}
    for c in haal("https://api-futures.kucoin.com/api/v1/contracts/active")["data"]:
        if not c["symbol"].endswith("USDTM") or c.get("isInverse") or c.get("fundingFeeRate") is None:
            continue
        gran = f(c.get("currentFundingRateGranularity") or c.get("fundingRateGranularity")) / 3.6e6
        uit[munt_naam(c["baseCurrency"])] = {"rate": f(c["fundingFeeRate"]), "uur": gran or 8,
                                             "volgende": f(c.get("nextFundingRateDateTime")) / 1000,
                                             "prijs": f(c.get("lastTradePrice")) or f(c.get("markPrice")),
                                             "vol_usd": f(c.get("turnoverOf24h"))}
    return uit


def bingx():
    B = "https://open-api.bingx.com/openApi/swap/v2/quote"
    tick = {t["symbol"]: t for t in haal(f"{B}/ticker")["data"]}
    uit = {}
    for r in haal(f"{B}/premiumIndex")["data"]:
        s = r.get("symbol", "")
        if not s.endswith("-USDT") or r.get("lastFundingRate") in (None, ""):
            continue
        t = tick.get(s, {})
        uit[munt_naam(s[:-5])] = {"rate": f(r["lastFundingRate"]), "uur": f(r.get("fundingIntervalHours")) or 8,
                                  "volgende": f(r.get("nextFundingTime")) / 1000,
                                  "prijs": f(t.get("lastPrice")) or f(r.get("markPrice")),
                                  "vol_usd": f(t.get("quoteVolume"))}
    return uit


def kraken():
    """Kraken Futures verrekent elk uur (GEZIEN: historicalfundingrates heeft één regel per heel uur). De rate als
    fractie staat in relativeFundingRatePrediction (voor het komende uur)."""
    uit = {}
    for t in haal("https://futures.kraken.com/derivatives/api/v3/tickers")["tickers"]:
        if t.get("tag") != "perpetual" or t.get("suspended") or not str(t.get("symbol", "")).startswith("PF_"):
            continue
        b, _, q = str(t.get("pair", "")).partition(":")
        if q != "USD" or t.get("relativeFundingRatePrediction") is None:
            continue
        uit[munt_naam(b)] = {"rate": f(t["relativeFundingRatePrediction"]), "uur": 1, "volgende": volgend_heel_uur(),
                             "prijs": f(t.get("last")) or f(t.get("markPrice")), "vol_usd": f(t.get("volumeQuote"))}
    return uit


def hyperliquid():
    """Hyperliquid verrekent elk uur; "funding" is de rate per uur (D-arbitrage.md, GEZIEN)."""
    meta, ctx = post("https://api.hyperliquid.xyz/info", {"type": "metaAndAssetCtxs"})
    uit = {}
    for u, c in zip(meta["universe"], ctx):
        if u.get("isDelisted") or c.get("funding") is None:
            continue
        uit[munt_naam(u["name"])] = {"rate": f(c["funding"]), "uur": 1, "volgende": volgend_heel_uur(),
                                     "prijs": f(c.get("markPx")), "vol_usd": f(c.get("dayNtlVlm"))}
    return uit


def dydx():
    """dYdX v4 verrekent elk uur (GEZIEN: historicalFunding heeft één regel per uur); nextFundingRate is per uur."""
    uit = {}
    for k, m in haal("https://indexer.dydx.trade/v4/perpetualMarkets")["markets"].items():
        if m.get("status") != "ACTIVE" or not k.endswith("-USD"):
            continue
        uit[munt_naam(k[:-4])] = {"rate": f(m.get("nextFundingRate")), "uur": 1, "volgende": volgend_heel_uur(),
                                  "prijs": f(m.get("oraclePrice")), "vol_usd": f(m.get("volume24H"))}
    return uit


ALLE = {"okx": okx, "bitget": bitget, "gate": gate, "mexc": mexc, "kucoin": kucoin, "bingx": bingx,
        "kraken": kraken, "hyperliquid": hyperliquid, "dydx": dydx}
