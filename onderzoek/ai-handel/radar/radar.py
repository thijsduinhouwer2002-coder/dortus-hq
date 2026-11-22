#!/usr/bin/env python3
"""Kansenradar: meet een week lang drie zeldzame momenten op crypto-beurzen. Alleen openbare API's: geen account,
geen sleutel, geen handel, geen geld. Uitleg in README.md.

  A. Nieuwe noteringen: elke 3 minuten de lijst met paren van 15 beurzen naast de vorige leggen. Komt er een munt
     bij die de beurs nog niet had, dan volgt de radar die munt 6 uur lang: elke minuut de orderboeken op de nieuwe
     beurs en op de beurzen waar hij al stond (zelfde quote), winst na takerkosten en opnamekosten, diepte, duur,
     en of opnemen en storten open staan.
  B. Funding-pieken: elke 2 minuten de funding van alle perpetuals op 9 beurzen. Boven 0,1% per 8 uur begint een
     piek; de radar doet alsof je dan spot koopt en de perp shortt (gedekt), telt de funding die echt verrekend
     wordt, en sluit als de funding onder 0,05% per 8 uur zakt (na minstens één verrekening). Winst na 4 keer
     takerkosten, het verschil tussen spot- en perpprijs, en één keer overmaken als spot en perp op twee beurzen
     zitten. Open pieken gaan mee naar de volgende run (pieken-open.json), zodat niets doorgeknipt wordt.
  C. Stablecoins: elke 15 seconden de orderboeken van alle stablecoin-paren (USDC, USDT, EURC, EURe, ...) tegen
     EUR, USD, USDT en USDC. Twee soorten momenten: (1) tussen beurzen, dezelfde munt goedkoper kopen dan hij
     elders verkocht wordt, na alle kosten (echte arbitrage); (2) los van de basislijn: meer dan 0,3% naast de mediaan
     van de laatste 45 dagen (geen arbitrage: je wint alleen als hij terugkomt).

Gebruik:  python3 radar.py --minuten 10 --uit /tmp/radar [--vorige paren-laatst.json] [--pieken pieken-open.json]
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
import hoek_a  # noqa: E402
import hoek_b  # noqa: E402
import hoek_c  # noqa: E402
import minima  # noqa: E402
import perps  # noqa: E402
import scanner  # noqa: E402,F401  (hergebruik: vul, bereken, is_kans, opname_fee, netwerk_stand, contract_stand)

from rekenen import *  # noqa: E402,F401,F403


class Radar(hoek_a.NoteringenMixin, hoek_b.FundingMixin, hoek_c.StableMixin):
    def __init__(self, uitmap, vorige=None, spot_klassen=None, perp_bronnen=None, log=print, pieken=None,
                 basis_bron=None):
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
        self.basis, self.basis_t = {}, 0   # C2: munt -> basislijn (mediaan per dag, zie hoek_c.py)
        self.basis_bron = basis_bron       # voor tests: functie (beurs, id) -> lijst (dag, slot)
        self.volg_a = Volger(os.path.join(uitmap, "noteringen-kansen.jsonl"),
                             ("bruto_pct", *WINST, "ruimte_eur", "winst_ruimte"))
        self.volg_c1 = Volger(os.path.join(uitmap, "stable-tussen.jsonl"),
                              ("bruto_pct", *WINST, "ruimte_eur", "winst_ruimte"))
        self.volg_c2 = Volger(os.path.join(uitmap, "stable-afwijking.jsonl"),
                              ("afwijking_pct", "na_kosten_pct", *WINST, "ruimte_eur"))
        self.stand = {"start": iso(nu_s()), "vorige_lijst": self.vorige_t, "rondes": {"paren": 0, "noteringen": 0,
                      "funding": 0, "stable": 0}, "noteringen": 0, "pieken_gesloten": 0, "stable_boeken": 0,
                      "fouten": {}, "ok": {}}
        self.volgend = {"paren": 0, "noteringen": 0, "funding": 0, "stable": 0, "wallet": 0, "stand": 0, "basis": 0}
        if pieken:
            self.laad_pieken(pieken)   # open funding-pieken van de vorige run afmaken (hoek_b.py)

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
        """Takerkosten van een spotpaar: uit de API als de beurs ze per paar geeft, anders
        beurzen.taker_standaard van de scanner (Kraken 0,80%; stablecoin- en FX-paren 0,20%; USDe 0%; USDG 0,01%).
        Eén plek voor scanner, radar en rapport."""
        t = self.paren.get(beurs, {}).get((munt, quote), {}).get("taker")
        return beurzen.taker_standaard(beurs, munt, quote) if t is None else t

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
                 lambda: (self.ververs_wallets(list(self.spot)), self.ververs_minima())), ("basis", ELKE_BASIS_S, self.ververs_basis),
                 ("stable", ELKE_STABLE_S, self.ronde_stable),
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
        self.bewaar_pieken()   # open pieken niet doorknippen: de volgende run maakt ze af (hoek_b.py)
        for v in (self.volg_a, self.volg_c1, self.volg_c2):
            v.sluit_alles()
        if self.ooit:
            self.bewaar_lijst()
        with open(os.path.join(self.uit, "samenvatting.json"), "w") as fh:
            json.dump({"eind": iso(t), **self.stand, "pieken_open_bewaard": len(self.pieken), "a_gesloten": self.volg_a.gesloten,
                       "c1_gesloten": self.volg_c1.gesloten, "c2_gesloten": self.volg_c2.gesloten}, fh, indent=1)
        self.pool.shutdown(wait=False, cancel_futures=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minuten", type=float, default=10)
    ap.add_argument("--uit", default="data")
    ap.add_argument("--vorige", default=None, help="paren-laatst.json van de vorige run (lijst munten per beurs)")
    ap.add_argument("--pieken", default=None, help="pieken-open.json van de vorige run (open funding-pieken)")
    a = ap.parse_args()
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))
    signal.signal(signal.SIGINT, lambda *_: sys.exit(0))
    r = Radar(a.uit, a.vorige, log=lambda x: print(x, flush=True), pieken=a.pieken)
    r.draai(a.minuten)
    print(json.dumps(r.stand, indent=1))


if __name__ == "__main__":
    main()
