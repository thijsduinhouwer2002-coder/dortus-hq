"""Koppelingen met de openbare API's van crypto-beurzen. Geen account, geen sleutel, alleen lezen.

Per beurs drie dingen:
  paren()   -> {(munt, quote): {"id": symbool op de beurs, "taker": fractie of None, "contract": adres of ""}}
  koersen() -> {(munt, quote): (beste bod, beste laat)}   in één verzoek voor alle paren
  boek(id)  -> (biedingen, laten), elk een lijst (prijs, hoeveelheid), beste eerst
  wallet()  -> {munt: {"opname": True/False/None, "storting": ..., "fee": munten of None, "contracten": set()}}

Takerkosten: waar de API ze per paar geeft (Gate, MEXC, Bitget, KuCoin) nemen we die (GEZIEN, API). Anders het
standaardtarief van de laagste trede uit TAKER hieronder; de bron staat in README.md.
"""
import gzip
import json
import os
import re
import ssl
import urllib.request

AGENT = "koersverschil-scanner/1.0 (onderzoek, alleen lezen)"
_CTX = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE") or None)

# Standaard takerkosten (fractie) als de API ze niet per paar geeft. Bron en GEZIEN/GOK: README.md.
TAKER = {
    "kraken": 0.0080, "bitvavo": 0.0025, "coinbase": 0.0120, "bitstamp": 0.0040, "okx": 0.0010,
    "kucoin": 0.0010, "gate": 0.0020, "mexc": 0.0005, "bybit": 0.0010, "bitget": 0.0010, "htx": 0.0020,
    "cryptocom": 0.0050, "poloniex": 0.0020, "xt": 0.0020, "bingx": 0.0010, "bitfinex": 0.0, "binance": 0.0010,
}

# Kraken rekent op stablecoin- en FX-paren (bijv. USDT-EUR) 0,20% in plaats van 0,80% (GEZIEN, kraken.com/pro/fees:
# "FX, stablecoin-base and pegged-token pairs"). STABIEL_FIAT is ook de lijst stablecoins van de kansenradar.
TAKER_STABIEL = {"kraken": 0.0020}
STABIEL_FIAT = {"USDT", "USDC", "EUR", "USD", "DAI", "PYUSD", "EURC", "USDG", "FDUSD", "USDE", "TUSD", "USD1", "RLUSD",
                "USDS", "USDP", "USDQ", "EURE", "EURI", "EURCV", "EUROP", "EURT", "AEUR", "EURR", "EURQ", "EURAU"}
# Kraken heeft voor alle paren met USDe (0% taker) en USDG (0,01% taker) een eigen tarief (GEZIEN, kraken.com/pro/fees,
# 19 nov 2026: "USDG pair fees 0.00% maker, 0.01% taker", "USDG and USDe pair fees"; voorbeeldpaar USDG/USD).
TAKER_MUNT = {"kraken": {"USDE": 0.0, "USDG": 0.0001}}


def taker_standaard(beurs, munt, quote, standaard=0.002):
    """Standaard takerkosten (fractie) voor een paar als de API er per paar geen geeft."""
    eigen = TAKER_MUNT.get(beurs, {})
    for x in (munt, quote):
        if x in eigen:
            return eigen[x]
    if beurs in TAKER_STABIEL and munt in STABIEL_FIAT and quote in STABIEL_FIAT:
        return TAKER_STABIEL[beurs]
    return TAKER.get(beurs, standaard)


# Andere namen voor dezelfde munt. XBT en XDG zijn namen van Kraken; die van Bitfinex staan bij Bitfinex zelf
# (keuring A9: UST en IOT niet op elke beurs omzetten, daar kunnen het andere munten zijn).
ALIAS = {"XBT": "BTC", "XDG": "DOGE"}
ALIAS_BITFINEX = {"UST": "USDT", "UDC": "USDC", "DSH": "DASH", "IOT": "IOTA"}
QUOTES = {"USDT", "USDC", "EUR", "USD"}

# Netwerknamen verschillen per beurs ("ERC20", "ETH", "Ethereum"); dit maakt ze vergelijkbaar. Een naam die hier
# niet staat, blijft zoals hij is (hoofdletters, zonder leestekens). Lukt het niet om een gemeenschappelijk netwerk
# te vinden, dan is de netwerkstand "onbekend", niet "dicht".
NET = {"ERC20": "ETH", "ETHEREUM": "ETH", "ETHERC20": "ETH", "ETHEREUMERC20": "ETH",
       "BEP20": "BSC", "BNBSMARTCHAIN": "BSC", "BEP20BSC": "BSC", "BSCBEP20": "BSC", "BNBSMARTCHAINBEP20": "BSC",
       "TRC20": "TRX", "TRON": "TRX", "TRONTRC20": "TRX", "SOLANA": "SOL", "SPL": "SOL",
       "ARBITRUM": "ARB", "ARBITRUMONE": "ARB", "ARBEVM": "ARB", "ARBONE": "ARB", "ARBI": "ARB",
       "OPTIMISM": "OP", "OPMAINNET": "OP", "OPETH": "OP", "BASEEVM": "BASE", "BASEMAINNET": "BASE",
       "MATIC": "POLYGON", "POLYGONPOS": "POLYGON", "POL": "POLYGON",
       "AVAXCCHAIN": "AVAXC", "CCHAIN": "AVAXC", "AVALANCHECCHAIN": "AVAXC"}


def norm(s):
    s = (s or "").upper().strip()
    return ALIAS.get(s, s)


def net(s):
    k = re.sub(r"[^A-Z0-9]", "", str(s or "").upper())
    return NET.get(k, k)


def haal(url, timeout=12):
    req = urllib.request.Request(url, headers={"User-Agent": AGENT, "Accept-Encoding": "gzip",
                                               "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout, context=_CTX) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    return json.loads(data)


def f(x):
    try:
        v = float(x)
        return v if v == v else 0.0
    except (TypeError, ValueError):
        return 0.0


def _rijen(lijst):
    return [(f(r[0]), f(r[1])) for r in lijst or [] if f(r[0]) > 0 and f(r[1]) > 0]


def _ja(x):
    return str(x).lower() in ("true", "1", "ok", "enabled", "allowed", "yes")


def _wallet_uit_ketens(ketens, open_opname, open_storting, fee_veld, contract_veld=None, naam_veld=None):
    """Eén munt: opname open als minstens één keten open is; fee = laagste fee van een open keten.
    "netwerken": per netwerk (genormaliseerde naam) opname, storting en fee, zodat de scanner kan kijken of er
    een netwerk is dat op beide beurzen open is."""
    opname = storting = False
    fee = None
    contracten = set()
    netwerken = {}
    for k in ketens or []:
        o, s = open_opname(k), open_storting(k)
        opname |= o
        storting |= s
        v = k.get(fee_veld) if fee_veld else None
        kfee = f(v) if v not in (None, "") else None
        if o and kfee is not None:
            fee = kfee if fee is None else min(fee, kfee)
        if contract_veld and k.get(contract_veld):
            contracten.add(str(k[contract_veld]).lower())
        if naam_veld and k.get(naam_veld):
            n = net(k[naam_veld])
            oud = netwerken.get(n)
            if oud is None or (o and not oud["opname"]):
                netwerken[n] = {"opname": o, "storting": s or bool(oud and oud["storting"]), "fee": kfee}
            else:
                oud["storting"] |= s
    return {"opname": opname, "storting": storting, "fee": fee, "contracten": contracten, "netwerken": netwerken}


class Beurs:
    naam = ""

    def paren(self):
        raise NotImplementedError

    def koersen(self):
        raise NotImplementedError

    def boek(self, sym):
        raise NotImplementedError

    def wallet(self):
        return {}


class Kraken(Beurs):
    naam = "kraken"
    B = "https://api.kraken.com/0/public"

    def paren(self):
        uit = {}
        self._sleutel = {}
        for k, p in haal(f"{self.B}/AssetPairs")["result"].items():
            ws = p.get("wsname", "")
            if "/" not in ws or k.endswith(".d") or p.get("status", "online") != "online":
                continue
            b, q = ws.split("/")
            sleutel = (norm(b), norm(q))
            if sleutel[1] in QUOTES:
                uit[sleutel] = {"id": k, "taker": None, "contract": ""}
                self._sleutel[k] = sleutel
        return uit

    def koersen(self):
        uit = {}
        for k, t in haal(f"{self.B}/Ticker")["result"].items():
            if k in self._sleutel:
                uit[self._sleutel[k]] = (f(t["b"][0]), f(t["a"][0]))
        return uit

    def boek(self, sym):
        r = list(haal(f"{self.B}/Depth?pair={sym}&count=50")["result"].values())[0]
        return _rijen(r["bids"]), _rijen(r["asks"])

    def wallet(self):
        uit = {}
        for a in haal(f"{self.B}/Assets")["result"].values():
            st = a.get("status", "")
            uit[norm(a.get("altname"))] = {"opname": st in ("enabled", "withdrawal_only"),
                                          "storting": st in ("enabled", "deposit_only"),
                                          "fee": None, "contracten": set()}
        return uit


class Bitvavo(Beurs):
    naam = "bitvavo"
    B = "https://api.bitvavo.com/v2"

    def paren(self):
        uit = {}
        for m in haal(f"{self.B}/markets"):
            if m.get("status") == "trading" and norm(m["quote"]) in QUOTES:
                uit[(norm(m["base"]), norm(m["quote"]))] = {"id": m["market"], "taker": None, "contract": ""}
        return uit

    def koersen(self):
        return {(norm(t["market"].split("-")[0]), norm(t["market"].split("-")[1])): (f(t.get("bid")), f(t.get("ask")))
                for t in haal(f"{self.B}/ticker/book") if "-" in t.get("market", "")}

    def boek(self, sym):
        r = haal(f"{self.B}/{sym}/book?depth=50")
        return _rijen(r["bids"]), _rijen(r["asks"])

    def wallet(self):
        uit = {}
        for a in haal(f"{self.B}/assets"):
            o, s = a.get("withdrawalStatus") == "OK", a.get("depositStatus") == "OK"
            fee = f(a.get("withdrawalFee")) if a.get("withdrawalFee") not in (None, "") else None
            uit[norm(a["symbol"])] = {"opname": o, "storting": s, "fee": fee, "contracten": set(),
                                      "netwerken": {net(n): {"opname": o, "storting": s, "fee": fee}
                                                    for n in a.get("networks") or []}}
        return uit


class Coinbase(Beurs):
    """Coinbase geeft geen bod en laat voor alle paren tegelijk; voor de eerste schifting nemen we de laatste
    prijs (bod = laat = prijs). Het orderboek bij de controle is wel echt."""
    naam = "coinbase"

    def paren(self):
        uit = {}
        self._p = {}
        d = haal("https://api.coinbase.com/api/v3/brokerage/market/products?product_type=SPOT")
        for p in d.get("products", []):
            if p.get("status") != "online" or p.get("trading_disabled") or p.get("is_disabled") or p.get("alias"):
                continue
            s = (norm(p["base_currency_id"]), norm(p["quote_currency_id"]))
            if s[1] in QUOTES:
                uit[s] = {"id": p["product_id"], "taker": None, "contract": ""}
        return uit

    def koersen(self):
        uit = {}
        d = haal("https://api.coinbase.com/api/v3/brokerage/market/products?product_type=SPOT")
        for p in d.get("products", []):
            s = (norm(p["base_currency_id"]), norm(p["quote_currency_id"]))
            prijs = f(p.get("price"))
            if prijs > 0 and not p.get("alias"):
                uit[s] = (prijs, prijs)
        return uit

    def boek(self, sym):
        r = haal(f"https://api.exchange.coinbase.com/products/{sym}/book?level=2")
        return _rijen(r["bids"][:50]), _rijen(r["asks"][:50])

    def wallet(self):
        uit = {}
        for c in haal("https://api.exchange.coinbase.com/currencies"):
            if c.get("status") != "online":
                uit[norm(c["id"])] = {"opname": False, "storting": False, "fee": None, "contracten": set()}
        return uit  # online zegt niets over opnemen: onbekend


class Bitstamp(Beurs):
    naam = "bitstamp"
    B = "https://www.bitstamp.net/api/v2"

    def paren(self):
        uit = {}
        for m in haal(f"{self.B}/trading-pairs-info/"):
            if m.get("trading") != "Enabled" or "/" not in m.get("name", ""):
                continue
            b, q = m["name"].split("/")
            if norm(q) in QUOTES:
                uit[(norm(b), norm(q))] = {"id": m["url_symbol"], "taker": None, "contract": ""}
        return uit

    def koersen(self):
        uit = {}
        for t in haal(f"{self.B}/ticker/"):
            if "/" in t.get("pair", ""):
                b, q = t["pair"].split("/")
                uit[(norm(b), norm(q))] = (f(t.get("bid")), f(t.get("ask")))
        return uit

    def boek(self, sym):
        r = haal(f"{self.B}/order_book/{sym}/")
        return _rijen(r["bids"][:50]), _rijen(r["asks"][:50])

    def wallet(self):
        uit = {}
        for c in haal(f"{self.B}/currencies/"):
            if c.get("type") != "crypto":
                continue
            w = _wallet_uit_ketens(c.get("networks"), lambda k: k.get("withdrawal") == "Enabled",
                                   lambda k: k.get("deposit") == "Enabled", None, None, "network")
            if not c.get("networks"):
                w.update(opname=c.get("withdrawal") == "Enabled", storting=c.get("deposit") == "Enabled")
            uit[norm(c["currency"])] = w
        return uit


class Okx(Beurs):
    naam = "okx"
    B = "https://www.okx.com/api/v5"

    def paren(self):
        uit = {}
        for i in haal(f"{self.B}/public/instruments?instType=SPOT")["data"]:
            if i.get("state") == "live" and norm(i["quoteCcy"]) in QUOTES:
                uit[(norm(i["baseCcy"]), norm(i["quoteCcy"]))] = {"id": i["instId"], "taker": None, "contract": ""}
        return uit

    def koersen(self):
        uit = {}
        for t in haal(f"{self.B}/market/tickers?instType=SPOT")["data"]:
            b, q = t["instId"].split("-")[:2]
            uit[(norm(b), norm(q))] = (f(t.get("bidPx")), f(t.get("askPx")))
        return uit

    def boek(self, sym):
        r = haal(f"{self.B}/market/books?instId={sym}&sz=50")["data"][0]
        return _rijen(r["bids"]), _rijen(r["asks"])


class Kucoin(Beurs):
    naam = "kucoin"
    B = "https://api.kucoin.com/api"

    def paren(self):
        uit = {}
        self._sym = {}
        for s in haal(f"{self.B}/v2/symbols")["data"]:
            if not s.get("enableTrading") or norm(s["quoteCurrency"]) in ("",) or norm(s["quoteCurrency"]) not in QUOTES:
                continue
            # KuCoin: klasse A/B/C = 0,1/0,2/0,3% taker (standaard, GOK), maal de coëfficiënt uit de API
            taker = 0.001 * int(s.get("feeCategory") or 1) * f(s.get("takerFeeCoefficient") or 1)
            k = (norm(s["baseCurrency"]), norm(s["quoteCurrency"]))
            uit[k] = {"id": s["symbol"], "taker": taker, "contract": ""}
            self._sym[s["symbol"]] = k
        return uit

    def koersen(self):
        return {self._sym[t["symbol"]]: (f(t.get("buy")), f(t.get("sell")))
                for t in haal(f"{self.B}/v1/market/allTickers")["data"]["ticker"] if t["symbol"] in self._sym}

    def boek(self, sym):
        r = haal(f"{self.B}/v1/market/orderbook/level2_20?symbol={sym}")["data"]
        return _rijen(r["bids"]), _rijen(r["asks"])

    def wallet(self):
        uit = {}
        for c in haal(f"{self.B}/v3/currencies")["data"]:
            uit[norm(c["currency"])] = _wallet_uit_ketens(
                c.get("chains"), lambda k: bool(k.get("isWithdrawEnabled")), lambda k: bool(k.get("isDepositEnabled")),
                "withdrawalMinFee", "contractAddress", "chainName")
        return uit


class Gate(Beurs):
    naam = "gate"
    B = "https://api.gateio.ws/api/v4"

    def paren(self):
        uit = {}
        self._sym = {}
        for p in haal(f"{self.B}/spot/currency_pairs"):
            if p.get("trade_status") != "tradable" or norm(p["quote"]) not in QUOTES:
                continue
            k = (norm(p["base"]), norm(p["quote"]))
            uit[k] = {"id": p["id"], "taker": f(p.get("fee")) / 100 if p.get("fee") else None, "contract": ""}
            self._sym[p["id"]] = k
        return uit

    def koersen(self):
        return {self._sym[t["currency_pair"]]: (f(t.get("highest_bid")), f(t.get("lowest_ask")))
                for t in haal(f"{self.B}/spot/tickers") if t["currency_pair"] in self._sym}

    def boek(self, sym):
        r = haal(f"{self.B}/spot/order_book?currency_pair={sym}&limit=50")
        return _rijen(r["bids"]), _rijen(r["asks"])

    def wallet(self):
        uit = {}
        for c in haal(f"{self.B}/spot/currencies"):
            if c.get("delisted"):
                uit[norm(c["currency"])] = {"opname": False, "storting": False, "fee": None, "contracten": set()}
                continue
            w = _wallet_uit_ketens(c.get("chains") or [{"withdraw_disabled": c.get("withdraw_disabled"),
                                                        "deposit_disabled": c.get("deposit_disabled")}],
                                   lambda k: not k.get("withdraw_disabled"), lambda k: not k.get("deposit_disabled"),
                                   None, "addr", "name")
            uit[norm(c["currency"])] = w  # fee van Gate is niet openbaar
        return uit


class Mexc(Beurs):
    naam = "mexc"
    B = "https://api.mexc.com/api/v3"

    def paren(self):
        uit = {}
        self._sym = {}
        for s in haal(f"{self.B}/exchangeInfo")["symbols"]:
            if str(s.get("status")) not in ("1", "ENABLED") or not s.get("isSpotTradingAllowed", True):
                continue
            if norm(s["quoteAsset"]) not in QUOTES:
                continue
            k = (norm(s["baseAsset"]), norm(s["quoteAsset"]))
            tk = s.get("takerCommission")
            uit[k] = {"id": s["symbol"], "taker": f(tk) if tk not in (None, "") else None,
                      "contract": str(s.get("contractAddress") or "").lower()}
            self._sym[s["symbol"]] = k
        return uit

    def koersen(self):
        return {self._sym[t["symbol"]]: (f(t.get("bidPrice")), f(t.get("askPrice")))
                for t in haal(f"{self.B}/ticker/bookTicker") if t["symbol"] in self._sym}

    def boek(self, sym):
        r = haal(f"{self.B}/depth?symbol={sym}&limit=50")
        return _rijen(r["bids"]), _rijen(r["asks"])


class Bybit(Beurs):
    naam = "bybit"
    B = "https://api.bybit.com/v5/market"

    def paren(self):
        uit = {}
        self._sym = {}
        for s in haal(f"{self.B}/instruments-info?category=spot")["result"]["list"]:
            if s.get("status") == "Trading" and norm(s["quoteCoin"]) in QUOTES:
                k = (norm(s["baseCoin"]), norm(s["quoteCoin"]))
                uit[k] = {"id": s["symbol"], "taker": None, "contract": ""}
                self._sym[s["symbol"]] = k
        return uit

    def koersen(self):
        return {self._sym[t["symbol"]]: (f(t.get("bid1Price")), f(t.get("ask1Price")))
                for t in haal(f"{self.B}/tickers?category=spot")["result"]["list"] if t["symbol"] in self._sym}

    def boek(self, sym):
        r = haal(f"{self.B}/orderbook?category=spot&symbol={sym}&limit=50")["result"]
        return _rijen(r["b"]), _rijen(r["a"])


class Bitget(Beurs):
    naam = "bitget"
    B = "https://api.bitget.com/api/v2/spot"

    def paren(self):
        uit = {}
        self._sym = {}
        for s in haal(f"{self.B}/public/symbols")["data"]:
            if s.get("status") != "online" or norm(s["quoteCoin"]) not in QUOTES:
                continue
            k = (norm(s["baseCoin"]), norm(s["quoteCoin"]))
            tk = s.get("takerFeeRate")
            uit[k] = {"id": s["symbol"], "taker": f(tk) if tk not in (None, "") else None, "contract": ""}
            self._sym[s["symbol"]] = k
        return uit

    def koersen(self):
        return {self._sym[t["symbol"]]: (f(t.get("bidPr")), f(t.get("askPr")))
                for t in haal(f"{self.B}/market/tickers")["data"] if t["symbol"] in self._sym}

    def boek(self, sym):
        r = haal(f"{self.B}/market/orderbook?symbol={sym}&limit=50")["data"]
        return _rijen(r["bids"]), _rijen(r["asks"])

    def wallet(self):
        uit = {}
        for c in haal(f"{self.B}/public/coins")["data"]:
            uit[norm(c["coin"])] = _wallet_uit_ketens(c.get("chains"), lambda k: _ja(k.get("withdrawable")),
                                                     lambda k: _ja(k.get("rechargeable")), "withdrawFee",
                                                     "contractAddress", "chain")
        return uit


class Htx(Beurs):
    naam = "htx"
    B = "https://api.huobi.pro"

    def paren(self):
        uit = {}
        self._sym = {}
        for s in haal(f"{self.B}/v1/settings/common/market-symbols")["data"]:
            if s.get("state") != "online" or norm(s["qc"]) not in QUOTES:
                continue
            k = (norm(s["bc"]), norm(s["qc"]))
            uit[k] = {"id": s["symbol"], "taker": None, "contract": ""}
            self._sym[s["symbol"]] = k
        return uit

    def koersen(self):
        return {self._sym[t["symbol"]]: (f(t.get("bid")), f(t.get("ask")))
                for t in haal(f"{self.B}/market/tickers")["data"] if t["symbol"] in self._sym}

    def boek(self, sym):
        r = haal(f"{self.B}/market/depth?symbol={sym}&type=step0&depth=20")["tick"]
        return _rijen(r["bids"]), _rijen(r["asks"])

    def wallet(self):
        uit = {}
        for c in haal(f"{self.B}/v2/reference/currencies")["data"]:
            uit[norm(c["currency"])] = _wallet_uit_ketens(c.get("chains"), lambda k: k.get("withdrawStatus") == "allowed",
                                                         lambda k: k.get("depositStatus") == "allowed",
                                                         "transactFeeWithdraw", None, "displayName")
        return uit


class Cryptocom(Beurs):
    naam = "cryptocom"
    B = "https://api.crypto.com/exchange/v1/public"

    def paren(self):
        uit = {}
        self._sym = {}
        for i in haal(f"{self.B}/get-instruments")["result"]["data"]:
            if i.get("inst_type") != "CCY_PAIR" or not i.get("tradable", True) or norm(i["quote_ccy"]) not in QUOTES:
                continue
            k = (norm(i["base_ccy"]), norm(i["quote_ccy"]))
            uit[k] = {"id": i["symbol"], "taker": None, "contract": ""}
            self._sym[i["symbol"]] = k
        return uit

    def koersen(self):
        return {self._sym[t["i"]]: (f(t.get("b")), f(t.get("k")))
                for t in haal(f"{self.B}/get-tickers")["result"]["data"] if t["i"] in self._sym}

    def boek(self, sym):
        r = haal(f"{self.B}/get-book?instrument_name={sym}&depth=50")["result"]["data"][0]
        return _rijen(r["bids"]), _rijen(r["asks"])


class Poloniex(Beurs):
    naam = "poloniex"
    B = "https://api.poloniex.com"

    def paren(self):
        uit = {}
        self._sym = {}
        for m in haal(f"{self.B}/markets"):
            if m.get("state") != "NORMAL" or norm(m.get("quoteCurrencyName")) not in QUOTES:
                continue
            k = (norm(m["baseCurrencyName"]), norm(m["quoteCurrencyName"]))
            uit[k] = {"id": m["symbol"], "taker": None, "contract": ""}
            self._sym[m["symbol"]] = k
        return uit

    def koersen(self):
        return {self._sym[t["symbol"]]: (f(t.get("bid")), f(t.get("ask")))
                for t in haal(f"{self.B}/markets/ticker24h") if t["symbol"] in self._sym}

    def boek(self, sym):
        r = haal(f"{self.B}/markets/{sym}/orderBook?limit=50")
        paar = lambda v: [(f(v[i]), f(v[i + 1])) for i in range(0, len(v) - 1, 2) if f(v[i]) > 0 and f(v[i + 1]) > 0]
        return paar(r.get("bids", [])), paar(r.get("asks", []))

    def wallet(self):
        uit = {}
        for rij in haal(f"{self.B}/currencies"):
            for naam, c in rij.items():
                weg = c.get("delisted") or c.get("walletState") != "ENABLED"
                o = not weg and c.get("walletWithdrawalState") == "ENABLED"
                s = not weg and c.get("walletDepositState") == "ENABLED"
                fee = f(c.get("withdrawalFee")) if c.get("withdrawalFee") not in (None, "") else None
                uit[norm(naam)] = {"opname": o, "storting": s, "fee": fee, "contracten": set(),
                                   "netwerken": {net(c["blockchain"]): {"opname": o, "storting": s, "fee": fee}}
                                   if c.get("blockchain") else {}}
        return uit


class Xt(Beurs):
    naam = "xt"
    B = "https://sapi.xt.com/v4/public"

    def paren(self):
        uit = {}
        self._sym = {}
        for s in haal(f"{self.B}/symbol")["result"]["symbols"]:
            if s.get("state") != "ONLINE" or not s.get("tradingEnabled", True) or norm(s["quoteCurrency"]) not in QUOTES:
                continue
            k = (norm(s["baseCurrency"]), norm(s["quoteCurrency"]))
            uit[k] = {"id": s["symbol"], "taker": None, "contract": ""}
            self._sym[s["symbol"]] = k
        return uit

    def koersen(self):
        return {self._sym[t["s"]]: (f(t.get("bp")), f(t.get("ap")))
                for t in haal(f"{self.B}/ticker/book")["result"] if t["s"] in self._sym}

    def boek(self, sym):
        r = haal(f"{self.B}/depth?symbol={sym}&limit=50")["result"]
        return _rijen(r["bids"]), _rijen(r["asks"])

    def wallet(self):
        uit = {}
        for c in haal(f"{self.B}/wallet/support/currency")["result"]:
            uit[norm(c["currency"])] = _wallet_uit_ketens(c.get("supportChains"), lambda k: bool(k.get("withdrawEnabled")),
                                                         lambda k: bool(k.get("depositEnabled")), "withdrawFeeAmount",
                                                         "contract", "chain")
        return uit


class Bingx(Beurs):
    naam = "bingx"
    B = "https://open-api.bingx.com/openApi/spot/v1"

    def paren(self):
        uit = {}
        self._sym = {}
        for s in haal(f"{self.B}/common/symbols")["data"]["symbols"]:
            if s.get("status") != 1 or "-" not in s["symbol"]:
                continue
            b, q = s["symbol"].split("-")[:2]
            if norm(q) in QUOTES:
                uit[(norm(b), norm(q))] = {"id": s["symbol"], "taker": None, "contract": ""}
                self._sym[s["symbol"]] = (norm(b), norm(q))
        return uit

    def koersen(self):
        return {self._sym[t["symbol"]]: (f(t.get("bidPrice")), f(t.get("askPrice")))
                for t in haal(f"{self.B}/ticker/bookTicker")["data"] if t["symbol"] in self._sym}

    def boek(self, sym):
        r = haal(f"{self.B}/market/depth?symbol={sym}&limit=50")["data"]
        return _rijen(r["bids"]), _rijen(r["asks"])


class Bitfinex(Beurs):
    naam = "bitfinex"
    B = "https://api-pub.bitfinex.com/v2"

    @staticmethod
    def _splits(sym):
        s = sym[1:]
        if ":" in s:
            b, q = s.split(":")
        elif len(s) == 6:
            b, q = s[:3], s[3:]
        else:
            return None
        b, q = b.upper(), q.upper()
        return norm(ALIAS_BITFINEX.get(b, b)), norm(ALIAS_BITFINEX.get(q, q))

    def paren(self):
        uit = {}
        self._sym = {}
        for rij in haal(f"{self.B}/tickers?symbols=ALL"):
            if not rij[0].startswith("t"):
                continue
            k = self._splits(rij[0])
            if k and k[1] in QUOTES and "TEST" not in rij[0]:
                uit[k] = {"id": rij[0], "taker": None, "contract": ""}
                self._sym[rij[0]] = k
        return uit

    def koersen(self):
        return {self._sym[r[0]]: (f(r[1]), f(r[3])) for r in haal(f"{self.B}/tickers?symbols=ALL") if r[0] in self._sym}

    def boek(self, sym):
        r = haal(f"{self.B}/book/{sym}/P0?len=25")
        bids = [(f(p), f(a)) for p, _, a in r if f(a) > 0]
        asks = [(f(p), -f(a)) for p, _, a in r if f(a) < 0]
        return bids, asks


class Binance(Beurs):
    naam = "binance"
    B = "https://api.binance.com/api/v3"

    def paren(self):
        uit = {}
        self._sym = {}
        for s in haal(f"{self.B}/exchangeInfo")["symbols"]:
            if s.get("status") == "TRADING" and norm(s["quoteAsset"]) in QUOTES:
                k = (norm(s["baseAsset"]), norm(s["quoteAsset"]))
                uit[k] = {"id": s["symbol"], "taker": None, "contract": ""}
                self._sym[s["symbol"]] = k
        return uit

    def koersen(self):
        return {self._sym[t["symbol"]]: (f(t.get("bidPrice")), f(t.get("askPrice")))
                for t in haal(f"{self.B}/ticker/bookTicker") if t["symbol"] in self._sym}

    def boek(self, sym):
        r = haal(f"{self.B}/depth?symbol={sym}&limit=50")
        return _rijen(r["bids"]), _rijen(r["asks"])


ALLE = [Kraken, Bitvavo, Coinbase, Bitstamp, Okx, Kucoin, Gate, Mexc, Bybit, Bitget, Htx, Cryptocom, Poloniex, Xt,
        Bingx, Bitfinex, Binance]
