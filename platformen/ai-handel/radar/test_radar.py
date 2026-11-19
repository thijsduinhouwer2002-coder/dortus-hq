"""Tests voor de kansenradar. Draaien: python3 -m unittest test_radar (in deze map). Geen internet nodig."""
import json
import os
import tempfile
import time
import unittest

import minima
import radar
import radar_rapport as rapport
import beurzen


def nep_beurs(naam, paren_lijsten, koersen=None, boeken=None, wallet=None):
    """Een beurs die bij elke aanroep van paren() de volgende lijst geeft (de laatste blijft)."""
    class Nep(beurzen.Beurs):
        pass
    Nep.naam = naam
    staat = {"i": 0}

    def paren(self):
        lijst = paren_lijsten[min(staat["i"], len(paren_lijsten) - 1)]
        staat["i"] += 1
        return {k: {"id": f"{k[0]}{k[1]}", "taker": 0.001, "contract": ""} for k in lijst}
    Nep.paren = paren
    Nep.koersen = lambda self: dict(koersen or {})
    Nep.boek = lambda self, sym: (boeken or {}).get(sym, ([], []))
    Nep.wallet = lambda self: dict(wallet or {})
    return Nep


def lees(pad):
    if not os.path.exists(pad):
        return []
    with open(pad) as fh:
        return [json.loads(x) for x in fh if x.strip()]


class TestRekenen(unittest.TestCase):
    def test_per8(self):
        self.assertAlmostEqual(radar.per8(0.0001, 1), 0.0008)
        self.assertAlmostEqual(radar.per8(0.0005, 4), 0.001)
        self.assertAlmostEqual(radar.per8(0.001, 8), 0.001)
        self.assertEqual(radar.per8(0.001, 0), 0.0)

    def test_peg(self):
        self.assertEqual(radar.peg("USDC", "USDT", 1.1), 1.0)
        self.assertAlmostEqual(radar.peg("USDC", "EUR", 1.1), 1 / 1.1)
        self.assertAlmostEqual(radar.peg("EURC", "USD", 1.1), 1.1)
        self.assertEqual(radar.peg("EURC", "EUR", 1.1), 1.0)
        self.assertIsNone(radar.peg("USDC", "EUR", None))
        self.assertIsNone(radar.peg("BTC", "EUR", 1.1))

    def test_afwijking_goedkoop(self):
        # USDC te koop voor 0,99 dollar (1% onder), taker 0,1%: na kosten 0,8%
        r = radar.afwijking([(0.99, 1000), (0.999, 5000)], [(0.985, 100)], 1.0, 0.001)
        self.assertEqual(r["kant"], "goedkoop")
        self.assertAlmostEqual(r["afwijking_pct"], 1.0, places=3)
        self.assertAlmostEqual(r["na_kosten_pct"], 0.8, places=3)
        self.assertAlmostEqual(r["ruimte_eur"], 990, places=2)       # alleen de laag met >= 0,3% afwijking
        per = 1 / 0.99 * 0.999 - 1.001
        self.assertAlmostEqual(r["winst100"], 100 * per, places=4)
        self.assertAlmostEqual(r["winst500"], 500 * per, places=4)
        # €2.000: na €990 komt 0,999 (0,1% onder); daar is na kosten geen winst meer, dus stopt hij
        self.assertAlmostEqual(r["winst2000"], 990 * per, places=4)

    def test_afwijking_duur_en_niets(self):
        r = radar.afwijking([(1.006, 100)], [(1.005, 1000)], 1.0, 0.001)
        self.assertEqual(r["kant"], "duur")
        self.assertAlmostEqual(r["winst100"], 100 * (0.999 - 1 / 1.005 * 1.001), places=4)
        self.assertIsNone(radar.afwijking([(1.001, 100)], [(0.999, 100)], 1.0, 0.001))
        self.assertIsNone(radar.afwijking([(0.9, 100)], [(0.8, 100)], None, 0.001))

    def test_afwijking_kosten_groter(self):
        # 0,3% onder de koppeling maar 0,4% takerkosten per kant: moment wel, winst None (niets gevuld)
        r = radar.afwijking([(0.997, 1000)], [(0.99, 1)], 1.0, 0.004)
        self.assertLess(r["na_kosten_pct"], 0)
        self.assertIsNone(r["winst500"])

    def test_bereken_inleg(self):
        r = radar.bereken_inleg([(100, 10)], [(101, 10)], 0, 0, 0.01, 1.0)
        self.assertAlmostEqual(r["winst100"], 1 - 1.01, places=4)     # opname 0,01 munt = €1,01 eet €1 winst op
        self.assertAlmostEqual(r["winst500"], 5 - 1.01, places=4)
        self.assertAlmostEqual(r["winst5000"], 10 - 1.01, places=4)   # boek op na 10 munten

    def test_min_in_eur(self):
        self.assertEqual(minima.in_eur({"quote": 5, "base": None}, 2.0, 0.9), 4.5)
        self.assertEqual(minima.in_eur({"quote": 1, "base": 10}, 2.0, 0.9), 18.0)
        self.assertIsNone(minima.in_eur(None, 2.0, 0.9))
        self.assertIsNone(minima.in_eur({"quote": None, "base": 3}, 0, 1))

    def test_zelfde_ding(self):
        self.assertTrue(radar.zelfde_ding(10.2, 10.0))
        self.assertTrue(radar.zelfde_ding(0.00001, 0.0100))      # 1000PEPE
        self.assertFalse(radar.zelfde_ding(12.0, 10.0))
        self.assertFalse(radar.zelfde_ding(0, 10.0))

    def test_munt_naam(self):
        import perps
        self.assertEqual(perps.munt_naam("kPEPE"), "PEPE")
        self.assertEqual(perps.munt_naam("1000PEPE"), "PEPE")
        self.assertEqual(perps.munt_naam("XBT"), "BTC")
        self.assertEqual(perps.munt_naam("H100"), "H100")


class TestVolger(unittest.TestCase):
    def test_open_en_dicht(self):
        with tempfile.TemporaryDirectory() as d:
            v = radar.Volger(os.path.join(d, "x.jsonl"), ("winst500",))
            v.stap(100, {"a"}, {"a": ({"winst500": 2.0}, {"munt": "X"})})
            v.stap(115, {"a"}, {"a": ({"winst500": 4.0}, {"munt": "X"})})
            self.assertIn("a", v.open)
            v.stap(130, {"a"}, {})
            rs = lees(os.path.join(d, "x.jsonl"))
            self.assertEqual(len(rs), 1)
            self.assertEqual(rs[0]["duur_s"], 15)
            self.assertEqual(rs[0]["metingen"], 2)
            self.assertEqual(rs[0]["winst500_med"], 3.0)
            self.assertEqual(rs[0]["eerste"]["winst500"], 2.0)
            self.assertEqual(rs[0]["munt"], "X")

    def test_niet_bekeken_blijft_open_tot_grens(self):
        with tempfile.TemporaryDirectory() as d:
            v = radar.Volger(os.path.join(d, "x.jsonl"), ())
            v.stap(0, {"a"}, {"a": ({}, {})})
            v.stap(100, set(), {})
            self.assertIn("a", v.open)
            v.stap(radar.SLUIT_NA_S + 1, set(), {})
            self.assertNotIn("a", v.open)


class TestNoteringen(unittest.TestCase):
    def maak(self, d, lijsten_x, lijsten_y=None, vorige=None):
        x = nep_beurs("kraken", lijsten_x)
        y = nep_beurs("mexc", lijsten_y or [[("NEW", "USDT"), ("BTC", "USDT")]])
        return radar.Radar(d, vorige=vorige, spot_klassen=[x, y], perp_bronnen={}, log=lambda s: None)

    def test_nieuwe_munt_wordt_gezien_en_gevolgd(self):
        with tempfile.TemporaryDirectory() as d:
            r = self.maak(d, [[("BTC", "USDT")], [("BTC", "USDT"), ("NEW", "USDT"), ("NEW", "EUR")]])
            r.ronde_paren()
            self.assertEqual(lees(os.path.join(d, "noteringen.jsonl")), [])   # eerste lijst: alleen onthouden
            r.ronde_paren()
            rs = lees(os.path.join(d, "noteringen.jsonl"))
            self.assertEqual({(x["munt"], x["quote"]) for x in rs}, {("NEW", "USDT"), ("NEW", "EUR")})
            usdt = [x for x in rs if x["quote"] == "USDT"][0]
            self.assertEqual(usdt["elders"], ["mexc"])
            self.assertFalse(usdt["vlak_na_start"])
            self.assertIn(("kraken", "NEW", "USDT"), r.gevolgd)
            self.assertNotIn(("kraken", "NEW", "EUR"), r.gevolgd)   # nergens anders in EUR: niets te vergelijken

    def test_weg_en_terug_is_niet_nieuw(self):
        with tempfile.TemporaryDirectory() as d:
            r = self.maak(d, [[("BTC", "USDT"), ("OUD", "USDT")], [("BTC", "USDT")], [("BTC", "USDT"), ("OUD", "USDT")]])
            for _ in range(3):
                r.ronde_paren()
            self.assertEqual(lees(os.path.join(d, "noteringen.jsonl")), [])

    def test_massa_is_storing(self):
        with tempfile.TemporaryDirectory() as d:
            veel = [("BTC", "USDT")] + [(f"M{i}", "USDT") for i in range(radar.MASSA_NIEUW + 5)]
            r = self.maak(d, [[("BTC", "USDT")], veel])
            r.ronde_paren()
            r.ronde_paren()
            self.assertEqual(lees(os.path.join(d, "noteringen.jsonl")), [])

    def test_vorige_lijst_als_basis(self):
        with tempfile.TemporaryDirectory() as d:
            pad = os.path.join(d, "vorige.json")
            with open(pad, "w") as fh:
                json.dump({"t": "2026-11-19T10:00:00Z", "munten": {"kraken": ["BTC"], "mexc": ["BTC", "NEW"]}}, fh)
            r = self.maak(d, [[("BTC", "USDT"), ("NEW", "USDT")]], vorige=pad)
            r.ronde_paren()
            rs = lees(os.path.join(d, "noteringen.jsonl"))
            self.assertEqual(len(rs), 1)
            self.assertTrue(rs[0]["vlak_na_start"])
            self.assertEqual(rs[0]["vorige_lijst"], "2026-11-19T10:00:00Z")
            # en de lijst voor de volgende run is weggeschreven
            with open(os.path.join(d, "paren-laatst.json")) as fh:
                self.assertIn("NEW", json.load(fh)["munten"]["kraken"])

    def test_prijsverschil_na_notering(self):
        with tempfile.TemporaryDirectory() as d:
            w = {"NEW": {"opname": True, "storting": True, "fee": 1.0, "contracten": set()}}
            x = nep_beurs("kraken", [[("BTC", "USDT")], [("BTC", "USDT"), ("NEW", "USDT")]],
                          boeken={"NEWUSDT": ([(1.10, 5000)], [(1.11, 5000)])}, wallet=w)
            y = nep_beurs("mexc", [[("NEW", "USDT")]], boeken={"NEWUSDT": ([(0.99, 5000)], [(1.00, 5000)])}, wallet=w)
            # beide nep-beurzen geven voor "NEWUSDT" hun eigen boek: x duur, y goedkoop
            r = radar.Radar(d, spot_klassen=[x, y], perp_bronnen={}, log=lambda s: None)
            r.eur["USDT"] = 1.0
            r.ronde_paren()
            r.ronde_paren()
            r.ronde_noteringen()
            r.ronde_noteringen()
            self.assertEqual(len(r.volg_a.open), 1)
            k = list(r.volg_a.open)[0]
            self.assertEqual((k[3], k[4]), ("mexc", "kraken"))   # koop op mexc, verkoop op kraken
            r.afsluiten()
            rs = lees(os.path.join(d, "noteringen-kansen.jsonl"))
            self.assertEqual(len(rs), 1)
            e = rs[0]["eerste"]
            # €500: 500 / 1,001 munt kopen, verkopen voor 1,10 x 0,999, min 1 munt opname x 1,10
            m = 500 / (1.00 * 1.001)
            self.assertAlmostEqual(e["winst500"], m * 1.10 * 0.999 - 500 - 1.10, places=2)
            self.assertTrue(rs[0]["einde_run"])


class TestFunding(unittest.TestCase):
    def test_piek_verrekening_en_som(self):
        t = time.time()
        stappen = [
            {"rate": 0.002, "uur": 8, "volgende": t + 1000, "prijs": 10.0, "vol_usd": 5e6},
            {"rate": 0.002, "uur": 8, "volgende": t + 1000, "prijs": 10.0, "vol_usd": 5e6},
            {"rate": 0.0015, "uur": 8, "volgende": t + 30000, "prijs": 11.0, "vol_usd": 5e6},   # 0,2% verrekend
            {"rate": 0.0001, "uur": 8, "volgende": t + 30000, "prijs": 11.0, "vol_usd": 5e6},   # onder 0,05%: dicht
        ]
        staat = {"i": 0}

        def bron():
            x = stappen[min(staat["i"], len(stappen) - 1)]
            staat["i"] += 1
            return {"ABC": dict(x)}
        spot = nep_beurs("okx", [[("ABC", "USDT")]], koersen={("ABC", "USDT"): (10.0, 10.0)})
        with tempfile.TemporaryDirectory() as d:
            r = radar.Radar(d, spot_klassen=[spot], perp_bronnen={"okx": bron}, log=lambda s: None)
            r.ronde_paren()
            for i in range(4):
                if i == 2:  # spot stijgt mee met de perp
                    r.spot["okx"].__class__.koersen = lambda self: {("ABC", "USDT"): (11.0, 11.0)}
                r.ronde_funding()
            self.assertEqual(r.pieken, {})
            rs = lees(os.path.join(d, "funding.jsonl"))
            self.assertEqual(len(rs), 1)
            p = rs[0]
            self.assertEqual(p["verrekeningen"], 1)
            self.assertAlmostEqual(p["ontvangen_pct"], 0.2)
            self.assertAlmostEqual(p["kosten_pct"], 2 * (0.05 + 0.1))   # perp 0,05% (okx) en spot 0,1% (nep)
            self.assertAlmostEqual(p["basis_pct"], 0.0)                 # spot en perp allebei +10%
            self.assertAlmostEqual(p["netto_pct"], 0.2 - 0.3, places=4)
            self.assertAlmostEqual(p["winst500"], -0.001 * 500 * 2 / 3, places=2)
            self.assertEqual(p["spot"], "okx")

    def test_lage_funding_geen_piek(self):
        with tempfile.TemporaryDirectory() as d:
            r = radar.Radar(d, spot_klassen=[nep_beurs("okx", [[("A", "USDT")]])],
                            perp_bronnen={"okx": lambda: {"A": {"rate": 0.0003, "uur": 8, "volgende": 1, "prijs": 1,
                                                                "vol_usd": 1}}}, log=lambda s: None)
            r.ronde_paren()
            r.ronde_funding()
            self.assertEqual(r.pieken, {})
            # 0,02% per uur = 0,16% per 8 uur: wel een piek
            r.perps = {"okx": lambda: {"A": {"rate": 0.0002, "uur": 1, "volgende": 1, "prijs": 1, "vol_usd": 1}}}
            r.ronde_funding()
            self.assertIn(("okx", "A"), r.pieken)


class TestStable(unittest.TestCase):
    def test_afwijking_en_tussen_beurzen(self):
        k1 = {("USDC", "EUR"): (0.905, 0.906), ("EUR", "USD"): (1.0999, 1.1001), ("USDT", "EUR"): (0.909, 0.9092)}
        k2 = {("USDC", "EUR"): (0.912, 0.913)}
        b1 = {"USDCEUR": ([(0.905, 10000)], [(0.906, 10000)])}
        b2 = {"USDCEUR": ([(0.912, 10000)], [(0.913, 10000)])}
        w = {"USDC": {"opname": True, "storting": True, "fee": 1.0, "contracten": set()}}
        x = nep_beurs("kraken", [list(k1)], koersen=k1, boeken=b1, wallet=w)
        y = nep_beurs("bitvavo", [list(k2)], koersen=k2, boeken=b2, wallet=w)
        with tempfile.TemporaryDirectory() as d:
            r = radar.Radar(d, spot_klassen=[x, y], perp_bronnen={}, log=lambda s: None)
            r.ronde_paren()
            r.ververs_wallets(["kraken", "bitvavo"])
            r.ronde_stable()
            self.assertAlmostEqual(r.eurusd, 1.1)
            # USDC hoort 1/1,1 = 0,9091 euro te kosten: op kraken 0,906 laat = 0,34% goedkoop
            self.assertIn(("kraken", "USDC", "EUR", "goedkoop"), r.volg_c2.open)
            # en bitvavo biedt 0,912 voor wat kraken voor 0,906 verkoopt: tussen beurzen
            self.assertIn(("USDC", "EUR", "kraken", "bitvavo"), r.volg_c1.open)
            r.afsluiten()
            c1 = lees(os.path.join(d, "stable-tussen.jsonl"))
            self.assertEqual(c1[0]["koop"], "kraken")
            self.assertGreater(c1[0]["eerste"]["winst500"], 0)


class TestRapport(unittest.TestCase):
    def test_haalbaar(self):
        r = {"min_koop_eur": 5, "min_verkoop_eur": 1, "min_opname_eur": 120}
        self.assertFalse(rapport.haalbaar(r, 100, "A"))
        self.assertTrue(rapport.haalbaar(r, 150, "A"))
        self.assertIsNone(rapport.haalbaar({"min_koop_eur": 5, "min_verkoop_eur": 1}, 100, "A"))
        # funding: positie is 2/3 van de inleg
        self.assertFalse(rapport.haalbaar({"min_spot_eur": 1, "min_perp_eur": 70}, 100, "B"))
        self.assertTrue(rapport.haalbaar({"min_spot_eur": 1, "min_perp_eur": 60}, 100, "B"))

    def test_rapport_draait_en_proef_telt_niet(self):
        with tempfile.TemporaryDirectory() as d:
            vast, proef = os.path.join(d, "2026-11-19", "run-1"), os.path.join(d, "2026-11-19", "run-2-proef")
            for m in (vast, proef):
                os.makedirs(m)
                with open(os.path.join(m, "stand.jsonl"), "w") as fh:
                    fh.write(json.dumps({"t": "2026-11-19T10:00:00Z"}) + "\n" +
                             json.dumps({"t": "2026-11-19T11:00:00Z"}) + "\n")
                with open(os.path.join(m, "funding.jsonl"), "w") as fh:
                    fh.write(json.dumps({"beurs": "okx", "munt": "A", "richting": "positief", "spot": "okx",
                                         "netto_pct": 0.5, "winst100": 0.33, "winst500": 1.67, "winst2000": 6.67,
                                         "winst5000": 16.7, "winst150": 0.5, "winst200": 0.67, "begin":
                                         "2026-11-19T10:10:00Z", "duur_s": 3600, "min_spot_eur": 1,
                                         "min_perp_eur": 5, "r8_max_pct": 0.2, "ontvangen_pct": 0.8,
                                         "verrekeningen": 1, "kosten_pct": 0.3, "basis_pct": 0, "vol_usd": 2e6})
                             + "\n")
            tekst = rapport.rapport(d)
            self.assertIn("1 positief met spotmarkt", tekst)
            self.assertIn("1.1 uur", tekst)
            self.assertIn("| €100 | 1 / 1 |", tekst)
            tekst2 = rapport.rapport(d, met_proef=True)
            self.assertIn("2 positief met spotmarkt", tekst2)


if __name__ == "__main__":
    unittest.main()
