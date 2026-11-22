"""C. Stablecoins: tussen beurzen (C1) en los van hun basislijn (C2). Deel van radar.Radar.

C2 meet niet tegen 1 dollar of 1 euro, maar tegen de basislijn: de mediaan van de slotkoersen per dag over de laatste
45 hele dagen (OHLC-API), omgerekend naar de koppeling. Een munt die al weken onder de koppeling staat (EURQ rond
0,97 euro) is dan geen kans; alleen een afwijking van zijn gewone prijs telt. Geen basislijn (te nieuw, geen bron):
het moment wordt bewaard met basis_ratio None en telt in het rapport niet mee."""
import collections
import concurrent.futures as cf
import json
import os
import statistics
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
sys.path.append(os.path.join(HIER, "..", "scanner"))   # achteraan: ../scanner/rapport.py mag niets hier verdringen
import basislijn  # noqa: E402
import beurzen  # noqa: E402
import minima  # noqa: E402
import perps  # noqa: E402
import scanner  # noqa: E402
from rekenen import *  # noqa: E402,F401,F403


class StableMixin:
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
            ref = self.ref_c2(m, q)[0]
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
            ref, bas = self.ref_c2(m, q)
            r = afwijking(boek[1], boek[0], ref, self.taker(b, m, q), DREMPEL_STABLE, self.eur.get(q, 0) or 1.0)
            if r:
                koppeling = peg(m, q, self.eurusd)
                r["afwijking_koppeling_pct"] = round((r["prijs"] / koppeling - 1) * 100, 4) if koppeling else None
                kansen2[(b, m, q, r["kant"])] = (r, {"beurs": b, "munt": m, "quote": q, "kant": r["kant"],
                                                     "taker": self.taker(b, m, q), "eurusd": self.eurusd,
                                                     "min_order_eur": self.min_order_eur(b, m, q, r["prijs"]),
                                                     "basis_ratio": bas["ratio"] if bas else None,
                                                     "basis_bron": bas["bron"] if bas else None,
                                                     "basis_dagen": bas["dagen"] if bas else None})
        self.volg_c2.stap(t, bekeken2, kansen2)
        self.stand["rondes"]["stable"] += 1

    def ref_c2(self, m, q):
        """Waar hoort de munt nu te staan (in de quote)? Koppeling maal de basislijn van de munt. Zonder basislijn
        de koppeling zelf (dan staat basis_ratio None bij het moment). Geeft (ref, basislijn of None)."""
        ref = peg(m, q, self.eurusd)
        bas = self.basis.get(m)
        if ref and bas:
            return ref * bas["ratio"], bas
        return ref, None

    def ververs_basis(self):
        """Basislijn per stablecoin: mediaan over de laatste BASIS_DAGEN hele dagen van slot / koppeling. Bron: de
        eerste beurs uit basislijn.BRONNEN die de munt heeft, liefst in een quote van dezelfde munteenheid (USDC
        tegen USDT, EURC tegen EUR), anders gekruist met EUR/USD van Kraken per dag."""
        haal = self.basis_bron or basislijn.dagslot
        if not self.paren:
            self.volgend["basis"] = 0   # nog geen lijsten: bij de volgende ronde opnieuw
            return
        taken = {}
        if ("EUR", "USD") in self.paren.get("kraken", {}):
            taken[("kraken", "basis", "EUR", "USD")] = (haal, ("kraken", self.paren["kraken"][("EUR", "USD")]["id"]))
        keuzes = {}
        for m in {m for (_, m, _) in self.stable_paren() if m in STABLE}:
            eigen = ("EUR",) if m in STABLE_EUR else ("USDT", "USDC", "USD")
            kruis = ("USD", "USDT", "USDC") if m in STABLE_EUR else ("EUR",)
            lijst = [(b, q) for q in eigen + kruis for b in basislijn.BRONNEN
                     if q != m and (m, q) in self.paren.get(b, {})][:3]
            keuzes[m] = lijst
            for b, q in lijst:
                taken[(b, "basis", m, q)] = (haal, (b, self.paren[b][(m, q)]["id"]))
        res = self.parallel(taken, timeout=90)
        eurusd = dict(res.get(("kraken", "basis", "EUR", "USD")) or [])
        for m, lijst in keuzes.items():
            for b, q in lijst:
                rij = res.get((b, "basis", m, q)) or []
                ratios = []
                for dag, slot in rij:
                    k = peg(m, q, eurusd.get(dag)) if (m in STABLE_EUR) != (q == "EUR") else peg(m, q, 1.0)
                    if k:
                        ratios.append(slot / k)
                if len(ratios) >= BASIS_MIN_DAGEN:
                    self.basis[m] = {"ratio": round(statistics.median(ratios), 6), "bron": f"{b} {m}-{q}",
                                     "dagen": len(ratios)}
                    break
        self.basis_t = nu_s()
        with open(os.path.join(self.uit, "basislijn.json"), "w") as fh:
            json.dump({"t": iso(self.basis_t), "basis": self.basis}, fh, indent=1)

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
