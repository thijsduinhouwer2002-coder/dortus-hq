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
import json
import os
import signal
import statistics
import threading
import time
import urllib.error

import volgen
from kosten import STATUS, B, kosten, minima
from reken import EURK, KLEIN, driehoeken, curve, eur_koers, maak_stappen, mid, min_inleg, top
from volgen import VERDACHT, iso

# Ritme per beurs: seconden per ronde, hoeveel orderboeken per ronde, en minimale tijd tussen twee verzoeken.
# Grenzen van de openbare API (per IP), zie README.md. We blijven er ruim onder.
RITME = {
    "bitvavo": (4, 6, 0.2), "kraken": (5, 3, 1.0), "okx": (3, 10, 0.1), "kucoin": (3, 10, 0.1),
    "gate": (4, 8, 0.1), "bitget": (3, 10, 0.1), "mexc": (3, 15, 0.1), "bitstamp": (5, 6, 0.2),
}
OPNIEUW_PAREN = 1800  # elke 30 minuten de lijst met paren verversen (nieuwe en gestopte markten)
STAND_ELKE = int(os.environ.get("DRIEHOEK_STAND_S", "300"))
STOPTIJD = 5          # seconden om na een stopsignaal de draden af te wachten (GitHub stopt na ±10 s hard)


def nu():
    return time.time()


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
        self.totaal = {"rondes": 0, "fouten": 0, "boeken": 0, "driehoeken": 0, "bevestigd": 0}
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
            st = maak_stappen(volgorde, paren, kv, mins, self.naam)
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
            self.sluit_alles("fout")

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
        self.sluit_alles("stop")

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
            if self.stop.is_set():
                break
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
            g = self.open[cid] = volgen.nieuw({
                "beurs": self.naam, "status": STATUS.get(self.naam, "grijs"), "driehoek": cid,
                "paren": [s["paar"] for s in c["stappen"]], "kosten": [s["hoog"] for s in c["stappen"]],
                "kosten_laag": [s["laag"] for s in c["stappen"]], "zeker": zelfde, "ritme_s": self.ritme}, t)
        volgen.meting(g, {"laag": laag, "hoog": hoog}, t)
        return True

    def _sluit(self, cid, reden):
        g = self.open.pop(cid, None)
        if not g:
            return
        g = volgen.regel(g, reden)
        self.totaal["driehoeken"] += 1
        if (g["hoog"] or {}).get("na_3s"):
            self.totaal["bevestigd"] += 1
        self.s.regel("driehoeken.jsonl", g)

    def sluit_alles(self, reden):
        for cid in list(self.open):
            self._sluit(cid, reden)

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
    # Snel afronden: GitHub stopt een afgebroken stap na ±10 seconden hard. Wie dan nog bezig is (een verzoek dat
    # hangt), wordt hier afgesloten; driehoeken.jsonl en stand.jsonl staan toch al regel voor regel op schijf.
    grens = nu() + STOPTIJD
    for m in meters:
        m.join(timeout=max(grens - nu(), 0.1))
    for m in meters:
        if m.is_alive():
            m.sluit_alles("stop")
    s.bestand("beurzen.json", {"t": iso(nu()), "beurzen": {m.naam: m.info for m in meters}})
    s.bestand("samenvatting.json", {
        "begin": iso(begin), "eind": iso(nu()), "minuten": round((nu() - begin) / 60, 1),
        "beurzen": {m.naam: dict(m.totaal, status=STATUS.get(m.naam, "grijs"), paren=m.info.get("paren"),
                                 driehoeken_bekend=m.info.get("driehoeken"), laatste_fout=m.info.get("fout"))
                    for m in meters}})


if __name__ == "__main__":
    main()
