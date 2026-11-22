"""Openbare gegevens voor de voorraad-simulatie (alleen lezen, geen account): koersen uit candles voor het
koerseffect, en minimale order- en opnamebedragen per beurs en munt. Alles GEZIEN uit de API van de beurs."""
import bisect


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
    """koers(munt, t): slotkoers van de laatste gesloten candle, van de eerste beurs in de lijst die data geeft.
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
        """Slotkoers van de laatste candle die vóór of op t gesloten is (keuring S10); de eerste candle als er nog
        geen gesloten is."""
        c = self.rij.get(munt)
        if not c:
            return None
        iv = min((b[0] - a[0] for a, b in zip(c, c[1:]) if b[0] > a[0]), default=900)
        i = bisect.bisect_right(c, (t - iv, float("inf"))) - 1
        return c[max(i, 0)][1] or None


class Minima:
    """minima(beurs, munt, quote) -> {"order_q": in de quote, "order_m": in munten, "opname_m": in munten}, elk None
    als onbekend. Uit de openbare API van Bitvavo, Kraken, KuCoin en Gate (GEZIEN); andere beurzen of een fout: None."""

    def __init__(self, haal=None):
        import beurzen
        self.haal = haal or (lambda url: beurzen.haal(url, timeout=8))
        self.cache, self.eens = {}, {}

    def __call__(self, beurs, munt, quote):
        k = (beurs, munt, quote)
        if k not in self.cache:
            try:
                self.cache[k] = self._vraag(beurs, munt, quote)
            except Exception:
                self.cache[k] = None
        return self.cache[k]

    def _bulk(self, url):
        if url not in self.eens:
            self.eens[url] = self.haal(url)
        return self.eens[url]

    def _vraag(self, beurs, munt, quote):
        f = lambda x: float(x) if x not in (None, "") else None
        laagste = lambda w: min(w) if w else None
        if beurs == "bitvavo":
            m = next((x for x in self._bulk("https://api.bitvavo.com/v2/markets") if x.get("market") == f"{munt}-{quote}"), {})
            a = next((x for x in self._bulk("https://api.bitvavo.com/v2/assets") if x.get("symbol") == munt), {})
            return {"order_q": f(m.get("minOrderInQuoteAsset")), "order_m": f(m.get("minOrderInBaseAsset")),
                    "opname_m": f(a.get("withdrawalMinAmount"))}
        if beurs == "kraken":
            p = next(iter((self.haal(f"https://api.kraken.com/0/public/AssetPairs?pair={munt}{quote}")
                           .get("result") or {}).values()), {})
            return {"order_q": f(p.get("costmin")), "order_m": f(p.get("ordermin")), "opname_m": None}
        if beurs == "kucoin":
            sy = next((x for x in self._bulk("https://api.kucoin.com/api/v2/symbols")["data"]
                       if x.get("symbol") == f"{munt}-{quote}"), {})
            ketens = (self.haal(f"https://api.kucoin.com/api/v3/currencies/{munt}").get("data") or {}).get("chains") or []
            return {"order_q": f(sy.get("minFunds")), "order_m": f(sy.get("baseMinSize")),
                    "opname_m": laagste([f(k["withdrawalMinSize"]) for k in ketens
                                         if k.get("isWithdrawEnabled") and f(k.get("withdrawalMinSize")) is not None])}
        if beurs == "gate":
            pa = self.haal(f"https://api.gateio.ws/api/v4/spot/currency_pairs/{munt}_{quote}")
            ketens = self.haal(f"https://api.gateio.ws/api/v4/wallet/currency_chains?currency={munt}")
            return {"order_q": f(pa.get("min_quote_amount")), "order_m": f(pa.get("min_base_amount")),
                    "opname_m": laagste([f(k["withdraw_amount_min"]) for k in ketens if not k.get("is_withdraw_disabled")
                                         and f(k.get("withdraw_amount_min")) is not None])}
        return None
