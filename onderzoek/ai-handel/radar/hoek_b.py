"""B. Funding-pieken: gedekte positie (spot kopen, perp shorten) volgen. Deel van radar.Radar."""
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


class FundingMixin:
    """Een piek begint boven DREMPEL_FUNDING (per 8 uur). Instappen kan pas als er een spotkoers is: zonder koers
    (verzoek mislukt, paar niet in de ticker) wacht de piek op de volgende ronde en is hij "spotkoers onbekend";
    alleen een echte spotkoers die niet bij de perp past, maakt hem een "ander ding". Funding telt alleen als hij
    na het instappen verrekend werd. Open pieken gaan bij het einde van een run naar pieken-open.json en de
    volgende run maakt ze af: zo betaalt een piek één keer 4 x takerkosten, ook als hij dagen duurt."""

    def spot_voor(self, beurs, munt):
        """Waar koop je de spotkant? Bij dezelfde beurs als die de munt in USDT/USDC/USD heeft, anders bij de beurs
        met de laagste takerkosten die hem heeft. Geeft (spotbeurs, quote) of (None, None)."""
        def quotes(b):
            return [q for q in ("USDT", "USDC", "USD") if (munt, q) in self.paren.get(b, {})]
        if beurs in perps.SPOT_ZELFDE and quotes(beurs):
            return beurs, quotes(beurs)[0]
        kandidaten = [(self.taker(b, munt, quotes(b)[0]), b, quotes(b)[0]) for b in self.paren if quotes(b)]
        if not kandidaten:
            return None, None
        _, b, q = min(kandidaten)
        return b, q

    def ronde_funding(self):
        t = nu_s()
        data = self.parallel({(b, "funding"): (fn, ()) for b, fn in self.perps.items()}, timeout=60)
        data = {b: d for (b, _), d in data.items()}
        for b in data:
            self.stand["ok"][f"perp:{b}"] = self.stand["ok"].get(f"perp:{b}", 0) + 1
        # welke spotkoersen zijn nodig: voor open pieken en voor nieuwe pieken
        nodig = set()
        for b, d in data.items():
            for m, x in d.items():
                if (b, m) in self.pieken:
                    nodig.add(self.pieken[(b, m)]["spot"])
                elif abs(per8(x["rate"], x["uur"])) >= DREMPEL_FUNDING:
                    nodig.add(self.spot_voor(b, m)[0])
        nodig.discard(None)
        koersen = self.parallel({(sb, "koersen"): (self.spot[sb].koersen, ()) for sb in nodig if sb in self.spot},
                                timeout=40)
        koersen = {sb: k for (sb, _), k in koersen.items()}
        for b, d in data.items():
            for m, x in d.items():
                self.funding_stap(b, m, x, t, koersen)
            # perps die verdwenen zijn: piek sluiten
            for (pb, pm) in [k for k in self.pieken if k[0] == b and k[1] not in d]:
                self.sluit_piek((pb, pm), t, koersen, reden="perp weg")
        self.stand["rondes"]["funding"] += 1
        self.bewaar_pieken()

    def instappen(self, p, x, koersen, t):
        """Spotkant kopen als er een koers is. Past de koers niet bij de perp, dan is het een ander ding."""
        k = koersen.get(p["spot"], {}).get((p["munt"], p["spot_quote"]))
        if not k:
            return
        p["spot_laatst"] = list(k)
        if p["spot_in"]:
            return
        prijs = k[1] if p["richting"] == "positief" else k[0]
        if not prijs:
            return
        if not zelfde_ding(prijs, x["prijs"]):
            p["spot_anders"] = True
            return
        p.update(spot_in=prijs, prijs_perp_in=x["prijs"], instap_t=t)

    def funding_stap(self, b, m, x, t, koersen):
        k = (b, m)
        vorig = self.funding_vorig.get(k)
        self.funding_vorig[k] = x
        r8 = per8(x["rate"], x["uur"])
        p = self.pieken.get(k)
        if p is None:
            if abs(r8) < DREMPEL_FUNDING:
                return
            sb, sq = self.spot_voor(b, m)
            p = self.pieken[k] = {
                "beurs": b, "munt": m, "richting": "positief" if r8 > 0 else "negatief", "begin_t": t,
                "laatst_t": t, "instap_t": None, "uur": x["uur"], "r8_begin": r8, "max_r8": abs(r8), "r8s": [r8],
                "ontvangen": 0.0, "verrekeningen": 0, "verrekeningen_geschat": 0, "prijs_perp_in": None,
                "prijs_perp_uit": x["prijs"], "vol_usd": x["vol_usd"], "spot": sb, "spot_quote": sq, "spot_in": None,
                "spot_laatst": None, "spot_anders": False, "taker_perp": perps.TAKER_PERP.get(b, 0.0006),
                "taker_spot": self.taker(sb, m, sq) if sb else None, "min_spot_eur": None, "min_perp_eur": None,
                "al_bij_start": self.stand["rondes"]["funding"] == 0, "uit_vorige_run": False,
            }
            p.update(self.overmaken(b, sb))
        if p["spot"] and not p["spot_anders"]:
            self.instappen(p, x, koersen, t)
        if p.get("min_spot_eur") is None and p["spot"] and p["spot_laatst"]:
            p["min_spot_eur"] = self.min_order_eur(p["spot"], m, p["spot_quote"], p["spot_laatst"][1])
        if p.get("min_perp_eur") is None:
            p["min_perp_eur"] = self.min_perp_eur(b, m, x["prijs"])
        # verrekening gezien: het tijdstip van de volgende verrekening schoof op, dus de vorige rate is betaald.
        # Na een gat (tussen twee runs) kunnen het er meer zijn: dan tellen we ze met de laatste bekende rate (GOK).
        if vorig and p["instap_t"] and x["volgende"] > vorig["volgende"] + 60 and vorig["volgende"] > p["instap_t"]:
            n = max(1, round((x["volgende"] - vorig["volgende"]) / (3600 * (x["uur"] or 8))))
            teken = 1 if p["richting"] == "positief" else -1
            p["ontvangen"] += teken * vorig["rate"] * n
            p["verrekeningen"] += n
            p["verrekeningen_geschat"] += n - 1
        p["laatst_t"] = t
        p["max_r8"] = max(p["max_r8"], abs(r8))
        p["prijs_perp_uit"] = x["prijs"]
        p["r8s"] = (p["r8s"] + [r8])[-200:]   # mediaan over de laatste 200 metingen (±6 uur)
        # Uitstappen pas na minstens één verrekening (bij perps die elk uur verrekenen schommelt de voorspelde
        # rate per minuut). Nooit ingestapt (geen spotkoers of ander ding): dicht zodra de piek weg is.
        weg = abs(r8) < DREMPEL_FUNDING_UIT or (r8 > 0) != (p["richting"] == "positief")
        if weg and (p["verrekeningen"] >= 1 or not p["instap_t"]):
            self.sluit_piek(k, t, koersen)

    def overmaken(self, perp, spot):
        """Staan spot en perp op twee beurzen, dan moet er minstens één keer een stablecoin heen (onderpand voor de
        short): opnamekosten van USDT of USDC op de spotbeurs (de goedkoopste die bekend is, anders de mediaan van
        andere beurzen, GOK), en het minimale opnamebedrag uit minima.py. Vast bedrag per piek in euro."""
        if not spot or spot == perp:
            return {"overmaak_eur": 0.0, "overmaak_bron": "zelfde beurs", "overmaak_min_eur": 0.0}
        beste = None
        for munt in ("USDT", "USDC"):
            fee, bron = scanner.opname_fee(self.wallets, spot, munt)
            if fee is not None:
                eur = fee * (self.eur.get(munt) or self.eur.get("USDT") or 0)
                if eur and (beste is None or eur < beste[0]):
                    beste = (eur, bron, munt)
        if beste is None:
            return {"overmaak_eur": None, "overmaak_bron": "onbekend", "overmaak_min_eur": None}
        mn = self.min_opname.get(spot, {}).get(beste[2])
        return {"overmaak_eur": round(beste[0], 4), "overmaak_bron": f"{beste[2]} {beste[1]}",
                "overmaak_min_eur": round(mn * (self.eur.get(beste[2]) or 0), 4) if mn else None}

    def min_perp_eur(self, b, m, prijs):
        mp = self.min_perp.get(b, {}).get(m)
        if not mp:
            return None
        w = [v for v in ((mp.get("usd") or 0) * self.eur.get("USD", 0),
                         (mp.get("munten") or 0) * (prijs or 0) * self.eur.get("USDT", 0)) if v]
        return round(max(w), 4) if w else None

    def sluit_piek(self, k, t, koersen, reden="onder drempel", einde_run=False):
        p = self.pieken.pop(k)
        k_uit = koersen.get(p["spot"], {}).get((p["munt"], p["spot_quote"])) if p["spot"] else None
        bod, laat = (k_uit or p.get("spot_laatst") or (0, 0)) if p["spot"] else (0, 0)
        spot_uit = (bod if p["richting"] == "positief" else laat) or None
        teken = 1 if p["richting"] == "positief" else -1
        basis = None
        if p["spot_in"] and spot_uit and p["prijs_perp_in"] and p["prijs_perp_uit"]:
            # gedekt: spot gaat mee met de munt, de perp de andere kant op. Verhoudingen, dus 1000PEPE mag.
            basis = teken * ((spot_uit / p["spot_in"] - 1) - (p["prijs_perp_uit"] / p["prijs_perp_in"] - 1))
        if p["spot_anders"]:
            spotstand = "ander ding"
        elif not p["spot"]:
            spotstand = "geen spotmarkt"
        elif not p["spot_in"] or basis is None:
            spotstand = "onbekend"
        else:
            spotstand = "ok"
        kosten = 2 * (p["taker_perp"] + (p["taker_spot"] or 0)) if spotstand == "ok" else None
        netto = p["ontvangen"] - kosten + basis if kosten is not None else None
        positie = {i: i * 2 / 3 for i in INLEG}  # 2/3 spot, 1/3 onderpand voor de short bij 2x (GOK, zie README)
        vast = p["overmaak_eur"]
        regel = {x: p.get(x) for x in ("beurs", "munt", "richting", "uur", "verrekeningen", "verrekeningen_geschat",
                                       "vol_usd", "spot", "spot_quote", "taker_perp", "taker_spot", "min_spot_eur",
                                       "min_perp_eur", "spot_anders", "al_bij_start", "uit_vorige_run",
                                       "overmaak_eur", "overmaak_bron", "overmaak_min_eur")}
        regel.update(
            begin=iso(p["begin_t"]), eind=iso(p["laatst_t"]), duur_s=round(p["laatst_t"] - p["begin_t"]),
            instap=iso(p["instap_t"]) if p["instap_t"] else None, spotstand=spotstand,
            reden=reden, einde_run=einde_run, r8_begin_pct=round(p["r8_begin"] * 100, 4),
            r8_max_pct=round(p["max_r8"] * 100, 4), r8_med_pct=round(statistics.median(p["r8s"]) * 100, 4),
            ontvangen_pct=round(p["ontvangen"] * 100, 4), kosten_pct=round(kosten * 100, 4) if kosten is not None
            else None, basis_pct=round(basis * 100, 4) if basis is not None else None,
            netto_pct=round(netto * 100, 4) if netto is not None else None,
            **{f"winst{i}": round(netto * positie[i] - vast, 2) if netto is not None and vast is not None else None
               for i in INLEG})
        with open(os.path.join(self.uit, "funding.jsonl"), "a") as fh:
            fh.write(json.dumps(regel, ensure_ascii=False) + "\n")
        self.stand["pieken_gesloten"] += 1

    # ---------- open pieken bewaren en afmaken ----------
    def bewaar_pieken(self):
        """Alle open pieken met hun laatste funding-meting naar pieken-open.json (na elke ronde en aan het eind)."""
        d = {"t": nu_s(), "pieken": [{"sleutel": list(k), "piek": p, "vorig": self.funding_vorig.get(k)}
                                     for k, p in self.pieken.items()]}
        tmp = os.path.join(self.uit, "pieken-open.json.tmp")
        with open(tmp, "w") as fh:
            json.dump(d, fh)
        os.replace(tmp, os.path.join(self.uit, "pieken-open.json"))

    def laad_pieken(self, pad):
        """Open pieken van de vorige run overnemen. Stopte die run meer dan MAX_GAT_S geleden, dan weten we niet
        wat er in het gat gebeurde: dan sluiten we ze als "gat te lang" (einde_run, apart in het rapport)."""
        if not pad or not os.path.exists(pad):
            return
        try:
            with open(pad) as fh:
                d = json.load(fh)
        except (ValueError, OSError) as e:
            self.log(f"open pieken niet te lezen: {e!r}")
            return
        t = nu_s()
        for x in d.get("pieken", []):
            k, p = tuple(x["sleutel"]), x["piek"]
            p["uit_vorige_run"] = True
            self.pieken[k] = p
            if x.get("vorig"):
                self.funding_vorig[k] = x["vorig"]
            if t - float(d.get("t") or 0) > MAX_GAT_S:
                self.sluit_piek(k, p["laatst_t"], {}, reden="gat te lang", einde_run=True)
        self.stand["pieken_overgenomen"] = len(self.pieken)
        self.log(f"open pieken van de vorige run: {len(d.get('pieken', []))}, overgenomen {len(self.pieken)}")
