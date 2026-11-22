"""A. Nieuwe noteringen: lijsten met paren vergelijken en nieuwe munten volgen. Deel van radar.Radar."""
import collections
import concurrent.futures as cf
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
sys.path.append(os.path.join(HIER, "..", "scanner"))   # achteraan: ../scanner/rapport.py mag niets hier verdringen
import beurzen  # noqa: E402
import minima  # noqa: E402
import perps  # noqa: E402
import scanner  # noqa: E402
from rekenen import *  # noqa: E402,F401,F403


class NoteringenMixin:
    def ronde_paren(self):
        t = nu_s()
        uit = self.parallel({(b, "paren"): (s.paren, ()) for b, s in self.spot.items()}, timeout=90)
        nieuw = []
        for (b, _), p in uit.items():
            if not p:
                continue
            oud_paren = self.paren.get(b)
            self.paren[b] = p
            munten = {m for m, _ in p}
            ooit = self.ooit.get(b)
            if ooit is None:      # eerste lijst van deze beurs, geen vorige: alleen onthouden
                self.ooit[b] = munten
                self.eerste_vergelijking[b] = False
                continue
            erbij = sorted(munten - ooit)
            if oud_paren is not None and len(p) < 0.5 * len(oud_paren):
                erbij = []        # lijst ineens half zo groot: storing, niet vergelijken (en niets vergeten)
            if len(erbij) > MASSA_NIEUW:
                self.log(f"  {b}: {len(erbij)} nieuwe munten tegelijk, waarschijnlijk een storing; niet geteld")
                erbij = []
            for m in erbij:
                for (mm, q) in p:
                    if mm == m:
                        nieuw.append((b, m, q, self.eerste_vergelijking.get(b, False)))
            self.ooit[b] = ooit | munten
            self.eerste_vergelijking[b] = False
        if nieuw:
            self.ververs_wallets({b for b, *_ in nieuw})
        for b, m, q, laat in nieuw:
            self.nieuwe_notering(b, m, q, laat, t)
        self.stand["rondes"]["paren"] += 1
        self.bewaar_lijst()

    def nieuwe_notering(self, b, m, q, laat, t):
        elders = sorted((x for x, p in self.paren.items() if x != b and (m, q) in p),
                        key=lambda x: (x not in ("kraken", "bitvavo", "okx", "kucoin", "gate", "mexc", "bitget"), x))
        andere_quote = sorted(x for x, p in self.paren.items() if x != b and any(mm == m for mm, _ in p))
        contracten = {x: scanner.contract_stand(self.paren, self.wallets, b, x, (m, q)) for x in elders}
        w = self.wallets.get(b, {}).get(m, {})
        regel = {"t": iso(t), "beurs": b, "munt": m, "quote": q, "elders": elders, "elders_andere_quote": andere_quote,
                 "contract": contracten, "opname": w.get("opname"), "storting": w.get("storting"),
                 "vlak_na_start": laat, "vorige_lijst": self.vorige_t if laat else None}
        with open(os.path.join(self.uit, "noteringen.jsonl"), "a") as fh:
            fh.write(json.dumps(regel, ensure_ascii=False) + "\n")
        self.stand["noteringen"] += 1
        self.log(f"  NIEUW {b} {m}-{q}, al op: {', '.join(elders) or 'geen enkele andere beurs (zelfde quote)'}"
                 + (" (eerste vergelijking na start)" if laat else ""))
        if elders:
            self.gevolgd[(b, m, q)] = {"t": t, "elders": elders[:MAX_ELDERS], "laat": laat}
            if len(self.gevolgd) > MAX_GEVOLGD:
                oudste = min(self.gevolgd, key=lambda k: self.gevolgd[k]["t"])
                del self.gevolgd[oudste]

    def bewaar_lijst(self):
        with open(os.path.join(self.uit, "paren-laatst.json"), "w") as fh:
            json.dump({"t": iso(nu_s()), "munten": {b: sorted(ms) for b, ms in self.ooit.items()}}, fh)

    def ronde_noteringen(self):
        t = nu_s()
        for k in [k for k, v in self.gevolgd.items() if t - v["t"] > VOLG_NOTERING_S]:
            del self.gevolgd[k]
        if not self.gevolgd:
            return
        oud = {x for (b, _, _), v in self.gevolgd.items() for x in [b] + v["elders"]
               if t - self.wallet_t.get(x, 0) > ELKE_WALLET_GEVOLGD_S}
        if oud:
            self.ververs_wallets(oud)
        nodig = {(x, m, q) for (b, m, q), v in self.gevolgd.items() for x in [b] + v["elders"]}
        boeken = self.parallel({(x, "boek", m, q): (self.spot[x].boek, (self.paren[x][(m, q)]["id"],))
                                for x, m, q in nodig if (m, q) in self.paren.get(x, {})}, timeout=40)
        boeken = {(x, m, q): v for (x, _, m, q), v in boeken.items()}
        bekeken, kansen = set(), {}
        for (b, m, q), v in self.gevolgd.items():
            for x in v["elders"]:
                for koop, verkoop in ((b, x), (x, b)):
                    ba, bv = boeken.get((koop, m, q)), boeken.get((verkoop, m, q))
                    if not ba or not bv:
                        continue
                    sl = (b, m, q, koop, verkoop)
                    bekeken.add(sl)
                    r, vast = self.reken_paar(m, q, koop, verkoop, ba, bv)
                    if scanner.is_kans(r):
                        r["min_sinds_notering"] = round((t - v["t"]) / 60, 1)
                        vast.update(nieuwe_beurs=b, vlak_na_start=v["laat"])
                        kansen[sl] = (r, vast)
        self.volg_a.stap(t, bekeken, kansen)
        self.stand["rondes"]["noteringen"] += 1

    def reken_paar(self, m, q, koop, verkoop, boek_koop, boek_verkoop):
        """Winst bij kopen op `koop` en verkopen op `verkoop` (zoals de scanner): takerkosten aan beide kanten en
        één opname van de munt. Geeft (meting, vaste velden over opnemen, storten, netwerk en contract)."""
        netwerk, fee_net = scanner.netwerk_stand(self.wallets, koop, verkoop, m)
        if fee_net is not None:
            fee_m, bron = fee_net, "netwerk"
        else:
            fee_m, bron = scanner.opname_fee(self.wallets, koop, m)
        r = bereken_inleg(boek_koop[1], boek_verkoop[0], self.taker(koop, m, q), self.taker(verkoop, m, q), fee_m,
                          self.eur.get(q, 0))
        vast = {"munt": m, "quote": q, "koop": koop, "verkoop": verkoop,
                "opname_koop": scanner.wallet_stand(self.wallets, koop, m, "opname"),
                "storting_verkoop": scanner.wallet_stand(self.wallets, verkoop, m, "storting"),
                "netwerk": netwerk, "opname_bron": bron,
                "contract": scanner.contract_stand(self.paren, self.wallets, koop, verkoop, (m, q)),
                "taker_koop": self.taker(koop, m, q), "taker_verkoop": self.taker(verkoop, m, q)}
        pk, pv = boek_koop[1][0][0] if boek_koop[1] else 0, boek_verkoop[0][0][0] if boek_verkoop[0] else 0
        vast.update(min_koop_eur=self.min_order_eur(koop, m, q, pk), min_verkoop_eur=self.min_order_eur(verkoop, m, q, pv),
                    min_opname_eur=self.min_opname_eur(koop, m, pk, q))
        return r, vast
