"""Minimale orderbedragen (spot en perp) en minimale opnamebedragen per beurs, uit de openbare API's. Zo zegt het
rapport of een kleine inleg (€100, €150, €200) kan meedoen. Alleen lezen, geen account.

  spot(beurs)  -> {(munt, quote): {"quote": minimum in de quote of None, "base": minimum in munten of None}}
  opname(beurs) -> {munt: minimum opname in munten}   (alleen beurzen die het openbaar geven)
  perp(beurs)  -> {munt: {"usd": minimum in dollar of None, "munten": minimum in munten of None}}

Waar een beurs het niet geeft, staat er niets: het rapport noemt dat "onbekend" (en rekent het niet als 0).
Bronnen (GEZIEN, veldnamen uit de API, 19 nov 2026): zie README.md, tabel "Minimale bedragen".
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scanner"))
import beurzen  # noqa: E402
import perps  # noqa: E402

f, haal, norm = beurzen.f, beurzen.haal, beurzen.norm


def _m(quote=None, base=None):
    q, b = f(quote), f(base)
    return {"quote": q or None, "base": b or None}


def spot(beurs):
    uit = {}
    if beurs == "kraken":
        for p in haal("https://api.kraken.com/0/public/AssetPairs")["result"].values():
            if "/" in p.get("wsname", ""):
                b, q = p["wsname"].split("/")
                uit[(norm(b), norm(q))] = _m(p.get("costmin"), p.get("ordermin"))
    elif beurs == "bitvavo":
        for m in haal("https://api.bitvavo.com/v2/markets"):
            uit[(norm(m["base"]), norm(m["quote"]))] = _m(m.get("minOrderInQuoteAsset"), m.get("minOrderInBaseAsset"))
    elif beurs == "coinbase":
        for p in haal("https://api.coinbase.com/api/v3/brokerage/market/products?product_type=SPOT").get("products", []):
            uit[(norm(p["base_currency_id"]), norm(p["quote_currency_id"]))] = _m(p.get("quote_min_size"),
                                                                                p.get("base_min_size"))
    elif beurs == "bitstamp":
        for m in haal("https://www.bitstamp.net/api/v2/trading-pairs-info/"):
            if "/" in m.get("name", ""):
                b, q = m["name"].split("/")
                uit[(norm(b), norm(q))] = _m(str(m.get("minimum_order", "")).split(" ")[0])
    elif beurs == "okx":
        for i in haal("https://www.okx.com/api/v5/public/instruments?instType=SPOT")["data"]:
            uit[(norm(i["baseCcy"]), norm(i["quoteCcy"]))] = _m(None, i.get("minSz"))
    elif beurs == "kucoin":
        for s in haal("https://api.kucoin.com/api/v2/symbols")["data"]:
            uit[(norm(s["baseCurrency"]), norm(s["quoteCurrency"]))] = _m(s.get("minFunds") or s.get("quoteMinSize"),
                                                                        s.get("baseMinSize"))
    elif beurs == "gate":
        for p in haal("https://api.gateio.ws/api/v4/spot/currency_pairs"):
            uit[(norm(p["base"]), norm(p["quote"]))] = _m(p.get("min_quote_amount"), p.get("min_base_amount"))
    elif beurs == "mexc":
        for s in haal("https://api.mexc.com/api/v3/exchangeInfo")["symbols"]:
            uit[(norm(s["baseAsset"]), norm(s["quoteAsset"]))] = _m(s.get("quoteAmountPrecision"))
    elif beurs == "bitget":
        for s in haal("https://api.bitget.com/api/v2/spot/public/symbols")["data"]:
            uit[(norm(s["baseCoin"]), norm(s["quoteCoin"]))] = _m(s.get("minTradeUSDT"), s.get("minTradeAmount"))
    elif beurs == "htx":
        for s in haal("https://api.huobi.pro/v1/settings/common/market-symbols")["data"]:
            uit[(norm(s["bc"]), norm(s["qc"]))] = _m(s.get("minov"), s.get("minoa"))
    elif beurs == "cryptocom":
        for i in haal("https://api.crypto.com/exchange/v1/public/get-instruments")["result"]["data"]:
            if i.get("inst_type") == "CCY_PAIR":
                uit[(norm(i["base_ccy"]), norm(i["quote_ccy"]))] = _m(None, i.get("qty_tick_size"))
    elif beurs == "poloniex":
        for m in haal("https://api.poloniex.com/markets"):
            lim = m.get("symbolTradeLimit") or {}
            uit[(norm(m["baseCurrencyName"]), norm(m["quoteCurrencyName"]))] = _m(lim.get("minAmount"),
                                                                                lim.get("minQuantity"))
    elif beurs == "xt":
        for s in haal("https://sapi.xt.com/v4/public/symbol")["result"]["symbols"]:
            q = next((x.get("min") for x in s.get("filters") or [] if x.get("filter") == "QUOTE_QTY"), None)
            uit[(norm(s["baseCurrency"]), norm(s["quoteCurrency"]))] = _m(q)
    elif beurs == "bingx":
        for s in haal("https://open-api.bingx.com/openApi/spot/v1/common/symbols")["data"]["symbols"]:
            if "-" in s["symbol"]:
                b, q = s["symbol"].split("-")[:2]
                uit[(norm(b), norm(q))] = _m(s.get("minNotional"), s.get("minQty"))
    elif beurs == "bitfinex":
        for sym, info in haal("https://api-pub.bitfinex.com/v2/conf/pub:info:pair")[0]:
            k = beurzen.Bitfinex._splits("t" + sym)
            if k and len(info) > 3:
                uit[k] = _m(None, info[3])
    return uit


def opname(beurs):
    uit = {}
    if beurs == "bitvavo":
        for a in haal("https://api.bitvavo.com/v2/assets"):
            if f(a.get("withdrawalMinAmount")):
                uit[norm(a["symbol"])] = f(a["withdrawalMinAmount"])
    elif beurs in ("kucoin", "bitget", "htx", "xt"):
        url, lijst, ketens, veld, naam = {
            "kucoin": ("https://api.kucoin.com/api/v3/currencies", lambda d: d["data"], "chains", "withdrawalMinSize",
                       "currency"),
            "bitget": ("https://api.bitget.com/api/v2/spot/public/coins", lambda d: d["data"], "chains",
                       "minWithdrawAmount", "coin"),
            "htx": ("https://api.huobi.pro/v2/reference/currencies", lambda d: d["data"], "chains", "minWithdrawAmt",
                    "currency"),
            "xt": ("https://sapi.xt.com/v4/public/wallet/support/currency", lambda d: d["result"], "supportChains",
                   "withdrawMinAmount", "currency"),
        }[beurs]
        for c in lijst(haal(url)):
            w = [f(k.get(veld)) for k in c.get(ketens) or [] if f(k.get(veld)) > 0]
            if w:
                uit[norm(c[naam])] = min(w)   # het netwerk met het laagste minimum (GOK: dat is ook het goedkoopste)
    return uit


def perp(beurs):
    uit = {}
    if beurs == "okx":
        for i in haal("https://www.okx.com/api/v5/public/instruments?instType=SWAP")["data"]:
            if i["instId"].endswith("-USDT-SWAP") and i.get("ctValCcy") == i["instId"].split("-")[0]:
                uit[perps.munt_naam(i["instId"].split("-")[0])] = {"usd": None,
                                                                   "munten": f(i.get("ctVal")) * f(i.get("minSz"))}
    elif beurs == "gate":
        for c in haal("https://api.gateio.ws/api/v4/futures/usdt/contracts"):
            if c["name"].endswith("_USDT"):
                uit[perps.munt_naam(c["name"][:-5])] = {"usd": None, "munten": f(c.get("quanto_multiplier")) *
                                                        (f(c.get("order_size_min")) or 1)}
    elif beurs == "mexc":
        for c in haal("https://contract.mexc.com/api/v1/contract/detail")["data"]:
            if c["symbol"].endswith("_USDT"):
                uit[perps.munt_naam(c["symbol"][:-5])] = {"usd": None, "munten": f(c.get("contractSize")) *
                                                          (f(c.get("minVol")) or 1)}
    elif beurs == "bitget":
        for c in haal("https://api.bitget.com/api/v2/mix/market/contracts?productType=USDT-FUTURES")["data"]:
            if c["symbol"].endswith("USDT"):
                uit[perps.munt_naam(c["symbol"][:-4])] = {"usd": f(c.get("minTradeUSDT")) or None,
                                                          "munten": f(c.get("minTradeNum")) or None}
    elif beurs == "kucoin":
        for c in haal("https://api-futures.kucoin.com/api/v1/contracts/active")["data"]:
            if c["symbol"].endswith("USDTM"):
                uit[perps.munt_naam(c["baseCurrency"])] = {"usd": None, "munten": f(c.get("multiplier")) *
                                                           (f(c.get("lotSize")) or 1)}
    elif beurs == "bingx":
        for c in haal("https://open-api.bingx.com/openApi/swap/v2/quote/contracts")["data"]:
            if c["symbol"].endswith("-USDT"):
                uit[perps.munt_naam(c["symbol"][:-5])] = {"usd": f(c.get("tradeMinUSDT")) or None,
                                                          "munten": f(c.get("tradeMinQuantity")) or None}
    elif beurs == "dydx":
        for k, m in haal("https://indexer.dydx.trade/v4/perpetualMarkets")["markets"].items():
            if k.endswith("-USD"):
                uit[perps.munt_naam(k[:-4])] = {"usd": None, "munten": f(m.get("stepSize")) or None}
    return uit   # Kraken Futures en Hyperliquid: niet in de openbare lijst; onbekend


def in_eur(minimum, prijs, eur_per_quote):
    """Minimum ordergrootte in euro: het grootste van het minimum in de quote en in munten. None als onbekend."""
    if not minimum:
        return None
    w = []
    if minimum.get("quote"):
        w.append(minimum["quote"] * eur_per_quote)
    if minimum.get("base") and prijs:
        w.append(minimum["base"] * prijs * eur_per_quote)
    return round(max(w), 4) if w else None
