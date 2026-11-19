#!/usr/bin/env python3
"""Koersverschil-scanner: meet of er tussen crypto-beurzen prijsverschillen boven de kosten bestaan, hoe lang ze
blijven staan en hoeveel euro er op het boek ligt. Alleen openbare API's: geen account, geen sleutel, geen handel.

Gebruik:  python3 scanner.py --minuten 10 --uit data/ [--interval 20] [--max-checks 60]

Elke ronde (±20 s):
  1. Van elke beurs in één verzoek bod en laat van alle paren (koersen).
  2. Per munt met dezelfde quote (USDT, USDC, EUR of USD; nooit omrekenen tussen quotes) op minstens twee beurzen:
     kopen op A tegen de laat, verkopen op B tegen het bod. Is dat verschil groter dan de takerkosten van A en B
     samen, dan is het een kandidaat. Boven 15% heet het "verdacht" (meestal een andere munt met dezelfde naam,
     of een dode markt) en telt het niet.
  3. Van de kandidaten (open kansen eerst, dan het grootste verschil) de orderboeken ophalen en uitrekenen
     hoeveel er echt te pakken is na takerkosten en opnamekosten van de munt.
  4. Een kans blijft open zolang er na alle kosten winst op het boek ligt. Sluit hij, dan komt er één regel in
     kansen.jsonl met begin, eind, duur, winst en de stand van opnemen en storten.
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import json
import os
import re
import signal
import statistics
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import beurzen  # noqa: E402

VERDACHT = 0.15          # bruto verschil boven 15%: bijna altijd een andere munt of een dode markt
PLAFONDS_EUR = (100, 500, 1000, 2500)   # winst uitgerekend bij deze bedragen per kans
RUIMTE_MAX_EUR = 20000   # hoe ver we het boek aflopen om de winstgevende ruimte te meten
META_ELKE_S = 1800       # paren, kosten en opnamestatus elk half uur opnieuw
SLUIT_NA_S = 180         # een open kans die zo lang niet gecontroleerd is, telt als gesloten
TRAAG_S = 55             # open kansen met opnemen of storten dicht of onbekend: hooguit eens per ±3 rondes controleren
# Hefboomtokens (ETH3S, BTC5L, ...) zijn producten van één beurs: niet over te maken, dus geen kans.
HEFBOOM = re.compile(r"(\d[LS]|BULL|BEAR)$")


def nu_s():
    return time.time()


def iso(t):
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def vul(laten, biedingen, fee_koop, fee_verkoop, plafond_quote):
    """Loop de laten van de koopbeurs en de biedingen van de verkoopbeurs tegelijk af, zolang kopen (met
    takerkosten) goedkoper is dan verkopen (met takerkosten), tot plafond_quote is uitgegeven.
    Geeft (munten, uitgegeven, ontvangen), alles in de quote. Zonder opnamekosten."""
    i = j = 0
    la = [list(x) for x in laten]
    bi = [list(x) for x in biedingen]
    munten = uit = ontvangen = 0.0
    while i < len(la) and j < len(bi) and uit < plafond_quote:
        pk, qk = la[i]
        pv, qv = bi[j]
        kost = pk * (1 + fee_koop)
        krijg = pv * (1 - fee_verkoop)
        if kost >= krijg:
            break
        q = min(qk, qv, (plafond_quote - uit) / kost)
        if q <= 0:
            break
        munten += q
        uit += q * kost
        ontvangen += q * krijg
        la[i][1] -= q
        bi[j][1] -= q
        if la[i][1] <= 1e-15:
            i += 1
        if bi[j][1] <= 1e-15:
            j += 1
    return munten, uit, ontvangen


def bereken(laten, biedingen, fee_koop, fee_verkoop, opname_munt, eur_per_quote):
    """Winst na alle kosten bij elk plafond, en de winstgevende ruimte op het boek. Bedragen in euro.
    opname_munt: opnamekosten in munten (één opname per kans), of None als onbekend (dan 0, en dat staat erbij)."""
    if not laten or not biedingen or eur_per_quote <= 0:
        return None
    fee_m = opname_munt or 0.0
    beste_bod = biedingen[0][0]
    uit = {}
    for p in PLAFONDS_EUR:
        m, kost, krijg = vul(laten, biedingen, fee_koop, fee_verkoop, p / eur_per_quote)
        uit[f"winst{p}"] = round((krijg - kost - fee_m * beste_bod) * eur_per_quote, 4) if m > 0 else None
    m, kost, krijg = vul(laten, biedingen, fee_koop, fee_verkoop, RUIMTE_MAX_EUR / eur_per_quote)
    uit["ruimte_eur"] = round(kost * eur_per_quote, 2)
    uit["winst_ruimte"] = round((krijg - kost - fee_m * beste_bod) * eur_per_quote, 4) if m > 0 else None
    uit["opname_eur"] = round(fee_m * beste_bod * eur_per_quote, 4)
    uit["bruto_pct"] = round((biedingen[0][0] / laten[0][0] - 1) * 100, 4)
    return uit


def is_kans(r):
    """Er ligt na alle kosten winst op het boek (bij de volle winstgevende ruimte), en het verschil op het boek is
    niet groter dan de grens voor "verdacht" (die geldt ook op het boek, niet alleen op de ticker; keuring A8)."""
    return bool(r) and r["winst_ruimte"] is not None and r["winst_ruimte"] > 0 and r["bruto_pct"] <= VERDACHT * 100


def kandidaten(koersen, paren, wallets=None, verdacht=VERDACHT):
    """Alle (munt, quote, koop, verkoop, bruto) waar bod op verkoop > laat op koop plus takerkosten.
    koersen: {beurs: {(munt, quote): (bod, laat)}}; paren: {beurs: {(munt, quote): info}}.
    Geeft (lijst kandidaten, aantal vergeleken paren, aantal verdacht)."""
    per = {}
    for b, ks in koersen.items():
        for k, (bod, laat) in ks.items():
            if bod > 0 and laat > 0 and laat >= bod * 0.5 and k in paren.get(b, {}) and not HEFBOOM.search(k[0]):
                per.setdefault(k, []).append((b, bod, laat))
    uit, vergeleken, n_verdacht = [], 0, 0
    for (munt, quote), rij in per.items():
        if len(rij) < 2:
            continue
        vergeleken += 1
        for a, _, laat_a in rij:
            for b, bod_b, _ in rij:
                if a == b:
                    continue
                bruto = bod_b / laat_a - 1
                drempel = taker(paren, a, (munt, quote)) + taker(paren, b, (munt, quote))
                if bruto <= drempel:
                    continue
                if bruto > verdacht:
                    n_verdacht += 1
                    continue
                uit.append((munt, quote, a, b, bruto))
    uit.sort(key=lambda x: -x[4])
    return uit, vergeleken, n_verdacht


def taker(paren, beurs, k):
    t = paren.get(beurs, {}).get(k, {}).get("taker")
    return beurzen.TAKER.get(beurs, 0.002) if t is None else t


def contract_stand(paren, wallets, a, b, k):
    """'zelfde' als beide beurzen een gemeenschappelijk contractadres hebben, 'anders' als ze allebei adressen
    hebben maar geen enkele gelijk (dan is het vaak een andere munt met dezelfde naam), anders 'onbekend'."""
    def adressen(beurs):
        s = set(wallets.get(beurs, {}).get(k[0], {}).get("contracten") or set())
        c = paren.get(beurs, {}).get(k, {}).get("contract")
        if c:
            s.add(c)
        return {x for x in s if x and len(x) > 10}
    ca, cb = adressen(a), adressen(b)
    if ca and cb:
        return "zelfde" if ca & cb else "anders"
    return "onbekend"


def opname_fee(wallets, beurs, munt):
    """(fee in munten, bron). Bron 'beurs' als de beurs hem openbaar geeft; 'geschat' = mediaan van de fees die
    andere beurzen voor deze munt geven (GOK); None als niemand hem geeft."""
    w = wallets.get(beurs, {}).get(munt)
    if w and w.get("fee") is not None:
        return w["fee"], "beurs"
    andere = [ws[munt]["fee"] for ws in wallets.values() if munt in ws and ws[munt].get("fee") is not None]
    if andere:
        return statistics.median(andere), "geschat"
    return None, "onbekend"


def netwerk_stand(wallets, a, b, munt):
    """Is er een netwerk waarover je de munt van A (opnemen) naar B (storten) krijgt? Geeft (stand, fee):
    "open" (een gemeenschappelijk netwerk is open; fee = laagste opnamefee op A over zo'n netwerk, of None),
    "dicht" (de beurzen hebben netwerken gemeen, maar geen enkele is aan beide kanten open), of "onbekend" (een
    van de twee geeft geen netwerken, of de namen zijn niet te koppelen)."""
    na = (wallets.get(a, {}).get(munt) or {}).get("netwerken") or {}
    nb = (wallets.get(b, {}).get(munt) or {}).get("netwerken") or {}
    samen = set(na) & set(nb)
    if not samen:
        return "onbekend", None
    open_ = [n for n in samen if na[n]["opname"] and nb[n]["storting"]]
    if not open_:
        return "dicht", None
    fees = [na[n]["fee"] for n in open_ if na[n].get("fee") is not None]
    return "open", (min(fees) if fees else None)


def wallet_stand(wallets, beurs, munt, veld):
    w = wallets.get(beurs, {}).get(munt)
    return None if w is None else w.get(veld)


class Scanner:
    def __init__(self, uitmap, interval=20, max_checks=120, beurs_klassen=None, log=print):
        self.uitmap = uitmap
        self.interval = interval
        self.max_checks = max_checks
        self.beurzen = [c() for c in (beurs_klassen or beurzen.ALLE)]
        self.paren, self.wallets = {}, {}
        self.meta_t = 0
        self.open = {}          # (munt, quote, koop, verkoop) -> toestand
        self.gecheckt = {}      # (munt, quote, koop, verkoop) -> laatste controle (tijd)
        self.log = log
        self.eur = {"EUR": 1.0}
        self.stand = {"rondes": 0, "kandidaten": 0, "checks": 0, "kansen_gesloten": 0, "fouten": {}, "ok": {}}
        self.pool = cf.ThreadPoolExecutor(max_workers=24)
        os.makedirs(uitmap, exist_ok=True)

    # ---------- meta ----------
    def ververs_meta(self):
        def een(b):
            p = b.paren()
            try:
                w = b.wallet()
            except Exception as e:  # opnamestatus is mooi, maar niet nodig om te meten
                self.fout(b.naam, "wallet", e)
                w = self.wallets.get(b.naam, {})
            return b.naam, p, w
        futs = [self.pool.submit(een, b) for b in self.beurzen]
        for fu, b in zip(futs, self.beurzen):
            try:
                naam, p, w = fu.result(timeout=90)
                self.paren[naam], self.wallets[naam] = p, w
            except Exception as e:
                self.fout(b.naam, "paren", e)
        self.meta_t = nu_s()
        with open(os.path.join(self.uitmap, "beurzen.json"), "w") as fh:
            json.dump({"t": iso(self.meta_t), "beurzen": {
                b.naam: {"paren": len(self.paren.get(b.naam, {})),
                         "wallet_munten": len(self.wallets.get(b.naam, {})),
                         "taker_uit_api": sum(1 for x in self.paren.get(b.naam, {}).values() if x["taker"] is not None),
                         "taker_standaard": beurzen.TAKER.get(b.naam)} for b in self.beurzen},
                "fouten": self.stand["fouten"]}, fh, indent=1)

    def fout(self, beurs, wat, e):
        sleutel = f"{beurs}:{wat}"
        self.stand["fouten"][sleutel] = self.stand["fouten"].get(sleutel, 0) + 1
        if self.stand["fouten"][sleutel] <= 3:
            self.log(f"  fout {sleutel}: {repr(e)[:160]}")

    # ---------- euro ----------
    def werk_eur_bij(self, koersen):
        """Euro per eenheid USDT/USDC/USD, alleen om winst in euro te tonen (geen handel tussen quotes)."""
        def mid(beurs, k):
            bod, laat = koersen.get(beurs, {}).get(k, (0, 0))
            return (bod + laat) / 2 if bod > 0 and laat > 0 else None
        usdt = mid("kraken", ("USDT", "EUR")) or mid("bitvavo", ("USDT", "EUR"))
        if usdt:
            self.eur["USDT"] = usdt
        usdc = mid("kraken", ("USDC", "EUR")) or mid("bitvavo", ("USDC", "EUR"))
        self.eur["USDC"] = usdc or self.eur.get("USDT", 0)
        eurusd = mid("kraken", ("EUR", "USD"))
        self.eur["USD"] = 1 / eurusd if eurusd else self.eur.get("USDT", 0)

    # ---------- ronde ----------
    def ronde(self):
        t0 = nu_s()
        if t0 - self.meta_t > META_ELKE_S:
            self.ververs_meta()
        koersen = {}
        futs = {self.pool.submit(b.koersen): b for b in self.beurzen if self.paren.get(b.naam)}
        for fu in cf.as_completed(futs, timeout=40):
            b = futs[fu]
            try:
                koersen[b.naam] = fu.result()
                self.stand["ok"][b.naam] = self.stand["ok"].get(b.naam, 0) + 1
            except Exception as e:
                self.fout(b.naam, "koersen", e)
        self.werk_eur_bij(koersen)
        kand, vergeleken, verdacht = kandidaten(koersen, self.paren)
        self.stand["rondes"] += 1
        self.stand["kandidaten"] += len(kand)

        # Rooster (keuring A5): eerst open kansen waar opnemen, storten en netwerk open zijn; dan kandidaten die nog
        # nooit gecontroleerd zijn (grootste verschil eerst); dan open kansen waar iets dicht of onbekend is, maar
        # hooguit eens per TRAAG_S seconden; dan de rest, langst niet gecontroleerd eerst. Zo vreten kansen die
        # toch niet meetellen (bijv. opnemen dicht, kan uren blijven staan) niet elke ronde de plekken op.
        sleutels = {(m, q, a, b): br for m, q, a, b, br in kand}
        self.gecheckt = {k: v for k, v in self.gecheckt.items() if k in sleutels}
        goed, traag = [], []
        for k in self.open:
            if k in sleutels:
                (goed if self.status_open(k) else traag).append(k)
        traag = [k for k in traag if t0 - self.gecheckt.get(k, 0) >= TRAAG_S]
        nooit = sorted((k for k in sleutels if k not in self.open and k not in self.gecheckt), key=lambda k: -sleutels[k])
        oud = sorted((k for k in sleutels if k not in self.open and k in self.gecheckt), key=lambda k: self.gecheckt[k])
        te_checken = (goed + nooit + traag + oud)[: self.max_checks]
        boeken = {}
        nodig = {(k[2], k[0], k[1]) for k in te_checken} | {(k[3], k[0], k[1]) for k in te_checken}
        bmap = {b.naam: b for b in self.beurzen}
        futs = {self.pool.submit(bmap[bn].boek, self.paren[bn][(m, q)]["id"]): (bn, m, q) for bn, m, q in nodig}
        for fu in cf.as_completed(futs, timeout=40):
            sl = futs[fu]
            try:
                boeken[sl] = fu.result()
            except Exception as e:
                self.fout(sl[0], "boek", e)
        tm = nu_s()
        for k in te_checken:
            m, q, a, b = k
            ba, bb = boeken.get((a, m, q)), boeken.get((b, m, q))
            if not ba or not bb:
                continue
            self.stand["checks"] += 1
            self.gecheckt[k] = tm
            netwerk, fee_net = netwerk_stand(self.wallets, a, b, m)
            if fee_net is not None:
                fee_m, fee_bron = fee_net, "netwerk"
            else:
                fee_m, fee_bron = opname_fee(self.wallets, a, m)
            r = bereken(ba[1], bb[0], taker(self.paren, a, (m, q)), taker(self.paren, b, (m, q)), fee_m,
                        self.eur.get(q, 0))
            if is_kans(r):
                self.werk_bij(k, r, tm, fee_bron, netwerk)
            elif k in self.open:
                self.sluit(k, tm)
        # kansen die niet meer bij de kandidaten staan, of te lang niet gecontroleerd zijn, sluiten
        for k in list(self.open):
            if k not in sleutels or tm - self.open[k]["laatst_t"] > SLUIT_NA_S:
                self.sluit(k, tm)
        nooit_na = sum(1 for k in sleutels if k not in self.gecheckt)
        self.schrijf_stand(t0, len(koersen), vergeleken, len(kand), verdacht, len(te_checken), nooit_na)
        return nu_s() - t0

    def status_open(self, k):
        o = self.open[k]
        return o["opname_koop"] is True and o["storting_verkoop"] is True and o.get("netwerk") != "dicht"

    def werk_bij(self, k, r, t, fee_bron, netwerk="onbekend"):
        o = self.open.get(k)
        if o is None:
            m, q, a, b = k
            o = self.open[k] = {
                "munt": m, "quote": q, "koop": a, "verkoop": b, "begin_t": t, "metingen": [],
                "opname_koop": wallet_stand(self.wallets, a, m, "opname"),
                "storting_verkoop": wallet_stand(self.wallets, b, m, "storting"),
                "contract": contract_stand(self.paren, self.wallets, a, b, (m, q)),
                "opname_bron": fee_bron, "netwerk": netwerk, "taker_koop": taker(self.paren, a, (m, q)),
                "taker_verkoop": taker(self.paren, b, (m, q)), "eur_per_quote": self.eur.get(q),
            }
        o["laatst_t"] = t
        o["metingen"].append(r)

    def sluit(self, k, t):
        o = self.open.pop(k)
        ms = o.pop("metingen")
        def med(veld):
            w = [x[veld] for x in ms if x.get(veld) is not None]
            return round(statistics.median(w), 4) if w else None
        def mx(veld):
            w = [x[veld] for x in ms if x.get(veld) is not None]
            return round(max(w), 4) if w else None
        regel = {
            **{x: o[x] for x in ("munt", "quote", "koop", "verkoop", "opname_koop", "storting_verkoop", "contract",
                                 "opname_bron", "netwerk", "taker_koop", "taker_verkoop", "eur_per_quote")},
            "begin": iso(o["begin_t"]), "eind": iso(o["laatst_t"]), "duur_s": round(o["laatst_t"] - o["begin_t"]),
            "metingen": len(ms), "bruto_pct_med": med("bruto_pct"), "bruto_pct_max": mx("bruto_pct"),
            "ruimte_eur_med": med("ruimte_eur"), "ruimte_eur_max": mx("ruimte_eur"),
            "winst_ruimte_med": med("winst_ruimte"), "winst_ruimte_max": mx("winst_ruimte"),
            "opname_eur": med("opname_eur"),
            **{f"winst{p}_med": med(f"winst{p}") for p in PLAFONDS_EUR},
            "eerste": ms[0],
        }
        with open(os.path.join(self.uitmap, "kansen.jsonl"), "a") as fh:
            fh.write(json.dumps(regel) + "\n")
        self.stand["kansen_gesloten"] += 1

    def schrijf_stand(self, t0, n_beurzen, vergeleken, n_kand, verdacht, n_checks, nooit=0):
        if self.stand["rondes"] % 15 != 1:   # elke ±5 minuten één regel
            return
        regel = {"t": iso(t0), "beurzen_ok": n_beurzen, "paren_vergeleken": vergeleken, "kandidaten": n_kand,
                 "verdacht": verdacht, "gecontroleerd": n_checks, "open": len(self.open),
                 "nooit_gecontroleerd": nooit,
                 "eur_per_usdt": round(self.eur.get("USDT", 0), 5), "duur_ronde_s": round(nu_s() - t0, 1)}
        with open(os.path.join(self.uitmap, "stand.jsonl"), "a") as fh:
            fh.write(json.dumps(regel) + "\n")
        self.log(f"{regel['t']} beurzen={n_beurzen} paren={vergeleken} kandidaten={n_kand} verdacht={verdacht} "
                 f"nooit={nooit} open={len(self.open)} gesloten={self.stand['kansen_gesloten']} "
                 f"ronde={regel['duur_ronde_s']}s")

    def draai(self, minuten):
        eind = nu_s() + minuten * 60
        try:
            while nu_s() < eind:
                try:
                    duur = self.ronde()
                except Exception as e:  # één mislukte ronde mag de meting niet stoppen
                    self.fout("scanner", "ronde", e)
                    duur = 0
                time.sleep(max(1.0, self.interval - duur))
        finally:
            for k in list(self.open):
                self.sluit(k, nu_s())
            with open(os.path.join(self.uitmap, "samenvatting.json"), "w") as fh:
                json.dump({"eind": iso(nu_s()), **self.stand}, fh, indent=1)
            self.pool.shutdown(wait=False, cancel_futures=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minuten", type=float, default=10)
    ap.add_argument("--uit", default="data")
    ap.add_argument("--interval", type=float, default=20)
    ap.add_argument("--max-checks", type=int, default=120)
    a = ap.parse_args()
    # Bij stoppen (workflow afgebroken) netjes afsluiten: open kansen wegschrijven.
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))
    signal.signal(signal.SIGINT, lambda *_: sys.exit(0))
    s = Scanner(a.uit, a.interval, a.max_checks, log=lambda x: print(x, flush=True))
    s.draai(a.minuten)
    print(json.dumps(s.stand, indent=1))


if __name__ == "__main__":
    main()
