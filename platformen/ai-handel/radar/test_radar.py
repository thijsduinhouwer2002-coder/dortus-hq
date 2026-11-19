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
            self.assertEqual(p["overmaak_eur"], 0.0)                    # spot en perp op dezelfde beurs
            self.assertAlmostEqual(p["basis_pct"], 0.0)                 # spot en perp allebei +10%
            self.assertAlmostEqual(p["netto_pct"], 0.2 - 0.3, places=4)
            self.assertAlmostEqual(p["winst500"], -0.001 * 500 * 2 / 3, places=2)
            self.assertEqual(p["spot"], "okx")

    def bron_uit(self, stappen):
        staat = {"i": 0}

        def bron():
            x = stappen[min(staat["i"], len(stappen) - 1)]
            staat["i"] += 1
            return {"ABC": dict(x)}
        return bron

    def test_open_piek_gaat_mee_naar_volgende_run(self):
        t = time.time()
        k1 = {("ABC", "USDT"): (10.0, 10.0)}
        k2 = {("ABC", "USDT"): (12.0, 12.0)}
        with tempfile.TemporaryDirectory() as d:
            spot = nep_beurs("okx", [[("ABC", "USDT")]], koersen=k1)
            bron = self.bron_uit([{"rate": 0.002, "uur": 8, "volgende": t + 1000, "prijs": 10.0, "vol_usd": 1}])
            r = radar.Radar(d, spot_klassen=[spot], perp_bronnen={"okx": bron}, log=lambda s: None)
            r.ronde_paren()
            r.ronde_funding()
            r.afsluiten()
            self.assertEqual(lees(os.path.join(d, "funding.jsonl")), [])   # niet doorgeknipt
            pad = os.path.join(d, "pieken-open.json")
            self.assertTrue(os.path.exists(pad))
            d2 = os.path.join(d, "run2")
            spot2 = nep_beurs("okx", [[("ABC", "USDT")]], koersen=k2)
            bron2 = self.bron_uit([{"rate": 0.0001, "uur": 8, "volgende": t + 30000, "prijs": 11.0, "vol_usd": 1}])
            r2 = radar.Radar(d2, spot_klassen=[spot2], perp_bronnen={"okx": bron2}, log=lambda s: None, pieken=pad)
            self.assertIn(("okx", "ABC"), r2.pieken)
            r2.ronde_paren()
            r2.ronde_funding()     # verrekening (volgende schoof op) en daarna onder 0,05%: dicht
            rs = lees(os.path.join(d2, "funding.jsonl"))
            self.assertEqual(len(rs), 1)
            p = rs[0]
            self.assertTrue(p["uit_vorige_run"])
            self.assertFalse(p["einde_run"])
            self.assertEqual(p["verrekeningen"], 1)
            self.assertAlmostEqual(p["ontvangen_pct"], 0.2)
            # spot +20%, perp +10%: de short verliest 10%, de spot wint 20%, netto +10% prijsverschil
            self.assertAlmostEqual(p["basis_pct"], 10.0, places=4)
            self.assertAlmostEqual(p["kosten_pct"], 2 * (0.05 + 0.1))
            self.assertAlmostEqual(p["netto_pct"], 0.2 + 10.0 - 0.3, places=4)
            self.assertEqual(p["spotstand"], "ok")

    def test_oude_open_pieken_na_lang_gat(self):
        with tempfile.TemporaryDirectory() as d:
            pad = os.path.join(d, "pieken-open.json")
            p = {"beurs": "okx", "munt": "ABC", "richting": "positief", "begin_t": 1000.0, "laatst_t": 2000.0,
                 "instap_t": 1000.0, "uur": 8, "r8_begin": 0.002, "max_r8": 0.002, "r8s": [0.002], "ontvangen": 0.0,
                 "verrekeningen": 0, "verrekeningen_geschat": 0, "prijs_perp_in": 10.0, "prijs_perp_uit": 10.0,
                 "vol_usd": 1, "spot": "okx", "spot_quote": "USDT", "spot_in": 10.0, "spot_laatst": [10.0, 10.0],
                 "spot_anders": False, "taker_perp": 0.0005, "taker_spot": 0.001, "min_spot_eur": 1,
                 "min_perp_eur": 1, "al_bij_start": False, "uit_vorige_run": False, "overmaak_eur": 0.0,
                 "overmaak_bron": "zelfde beurs", "overmaak_min_eur": 0.0}
            with open(pad, "w") as fh:
                json.dump({"t": time.time() - 3 * 3600, "pieken": [{"sleutel": ["okx", "ABC"], "piek": p}]}, fh)
            r = radar.Radar(d, spot_klassen=[], perp_bronnen={}, log=lambda s: None, pieken=pad)
            self.assertEqual(r.pieken, {})
            rs = lees(os.path.join(d, "funding.jsonl"))
            self.assertEqual(rs[0]["reden"], "gat te lang")
            self.assertTrue(rs[0]["einde_run"])

    def test_spotkoers_ontbreekt_is_geen_ander_ding(self):
        t = time.time()
        with tempfile.TemporaryDirectory() as d:
            spot = nep_beurs("okx", [[("ABC", "USDT")]], koersen={})
            bron = self.bron_uit([{"rate": 0.002, "uur": 8, "volgende": t + 1000, "prijs": 10.0, "vol_usd": 1}])
            r = radar.Radar(d, spot_klassen=[spot], perp_bronnen={"okx": bron}, log=lambda s: None)
            r.ronde_paren()
            r.ronde_funding()
            p = r.pieken[("okx", "ABC")]
            self.assertFalse(p["spot_anders"])
            self.assertEqual(p["spot"], "okx")
            self.assertIsNone(p["instap_t"])
            r.spot["okx"].__class__.koersen = lambda self: {("ABC", "USDT"): (10.1, 10.1)}
            r.ronde_funding()
            self.assertIsNotNone(p["instap_t"])          # nu wel ingestapt
            self.assertAlmostEqual(p["spot_in"], 10.1)

    def test_andere_spotprijs_is_ander_ding(self):
        t = time.time()
        with tempfile.TemporaryDirectory() as d:
            spot = nep_beurs("okx", [[("ABC", "USDT")]], koersen={("ABC", "USDT"): (13.0, 13.0)})
            bron = self.bron_uit([{"rate": 0.002, "uur": 8, "volgende": t + 1000, "prijs": 10.0, "vol_usd": 1},
                                  {"rate": 0.0001, "uur": 8, "volgende": t + 1000, "prijs": 10.0, "vol_usd": 1}])
            r = radar.Radar(d, spot_klassen=[spot], perp_bronnen={"okx": bron}, log=lambda s: None)
            r.ronde_paren()
            r.ronde_funding()
            self.assertTrue(r.pieken[("okx", "ABC")]["spot_anders"])
            r.ronde_funding()      # nooit ingestapt: dicht zodra de piek weg is
            self.assertEqual(lees(os.path.join(d, "funding.jsonl"))[0]["spotstand"], "ander ding")

    def test_overmaken_bij_twee_beurzen(self):
        t = time.time()
        w = {"USDT": {"opname": True, "storting": True, "fee": 1.0, "contracten": set()}}
        spot = nep_beurs("mexc", [[("ABC", "USDT")]], koersen={("ABC", "USDT"): (10.0, 10.0)}, wallet=w)
        bron = self.bron_uit([{"rate": 0.002, "uur": 1, "volgende": t + 100, "prijs": 10.0, "vol_usd": 1},
                              {"rate": 0.00001, "uur": 1, "volgende": t + 3700, "prijs": 10.0, "vol_usd": 1}])
        with tempfile.TemporaryDirectory() as d:
            r = radar.Radar(d, spot_klassen=[spot], perp_bronnen={"hyperliquid": bron}, log=lambda s: None)
            r.eur["USDT"] = 0.9
            r.ronde_paren()
            r.ververs_wallets(["mexc"])
            r.ronde_funding()
            r.ronde_funding()
            p = lees(os.path.join(d, "funding.jsonl"))[0]
            self.assertEqual(p["spot"], "mexc")
            self.assertAlmostEqual(p["overmaak_eur"], 0.9)
            netto = (0.002 - 2 * (0.00045 + 0.001))
            self.assertAlmostEqual(p["winst100"], round(netto * 100 * 2 / 3 - 0.9, 2), places=2)

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

    def piek(self, begin, eind, w150, beurs="okx", **extra):
        r = {"beurs": beurs, "munt": "A", "richting": "positief", "spot": beurs, "spot_quote": "USDT",
             "spotstand": "ok", "netto_pct": 0.5, "begin": begin, "eind": eind, "instap": begin, "duur_s": 3600,
             "min_spot_eur": 1, "min_perp_eur": 5, "overmaak_eur": 0.0, "overmaak_min_eur": 0.0, "einde_run": False,
             "taker_spot": 0.001, "taker_perp": 0.0005, "r8_max_pct": 0.2, "ontvangen_pct": 0.8,
             "verrekeningen": 1, "kosten_pct": 0.3, "basis_pct": 0.0, "vol_usd": 2e6}
        r.update({f"winst{i}": w150 * i / 150 for i in (100, 150, 200, 500, 2000, 5000)})
        r.update(extra)
        return r

    def schrijf(self, m, naam, regels):
        os.makedirs(m, exist_ok=True)
        with open(os.path.join(m, naam), "a") as fh:
            for r in regels:
                fh.write(json.dumps(r) + "\n")

    def test_een_pot(self):
        rs = [self.piek("2026-11-19T10:00:00Z", "2026-11-19T12:00:00Z", 1.0),
              self.piek("2026-11-19T11:00:00Z", "2026-11-19T11:30:00Z", 5.0),    # pot zit vast: niet gepakt
              self.piek("2026-11-19T12:00:00Z", "2026-11-19T13:00:00Z", 2.0),
              self.piek("2026-11-19T12:00:00Z", "2026-11-19T12:10:00Z", 3.0)]    # zelfde start: de beste
        gepakt, som = rapport.pot(rs, 150, "B")
        self.assertEqual([r["winst150"] for r in gepakt], [1.0, 3.0])
        self.assertAlmostEqual(som, 4.0)
        self.assertEqual(rapport.max_tegelijk(rs), 2)   # om 12:00 eindigt de eerste net

    def test_oud_tarief_en_ontdubbelen(self):
        self.assertTrue(rapport.oud_tarief({"spot": "kraken", "taker_spot": 0.004, "munt": "LQTY", "spot_quote": "USD"}))
        self.assertFalse(rapport.oud_tarief({"spot": "kraken", "taker_spot": 0.008, "munt": "LQTY", "spot_quote": "USD"}))
        self.assertTrue(rapport.oud_tarief({"beurs": "kraken", "taker": 0.008, "munt": "EURQ", "quote": "EUR"}))
        self.assertTrue(rapport.oud_tarief({"beurs": "kraken", "taker": 0.002, "munt": "USDE", "quote": "USD"}))
        self.assertFalse(rapport.oud_tarief({"beurs": "kraken", "taker": 0.0, "munt": "USDE", "quote": "USD"}))
        self.assertFalse(rapport.oud_tarief({"koop": "kraken", "taker_koop": 0.0001, "munt": "USDG", "quote": "USDT",
                                             "verkoop": "gate", "taker_verkoop": 0.002}))
        self.assertFalse(rapport.oud_tarief({"beurs": "kraken", "taker": 0.002, "munt": "EURQ", "quote": "EUR"}))
        a = self.piek("2026-11-19T10:00:00Z", "2026-11-19T11:00:00Z", 1.0)
        b = self.piek("2026-11-19T10:00:00Z", "2026-11-19T14:00:00Z", 2.0)
        self.assertEqual(rapport.ontdubbel_funding([a, b]), [b])

    def test_getallen_met_komma(self):
        self.assertEqual(rapport.eur(-1234.5), "-€1.234,50")
        self.assertEqual(rapport.pct(0.19), "0,19%")
        self.assertEqual(rapport.pct(None), "-")

    def test_rapport_draait_en_proef_telt_niet(self):
        with tempfile.TemporaryDirectory() as d:
            vast, proef = os.path.join(d, "2026-11-19", "run-1"), os.path.join(d, "2026-11-19", "run-2-proef")
            for m in (vast, proef):
                self.schrijf(m, "stand.jsonl", [{"t": "2026-11-19T10:00:00Z"}, {"t": "2026-11-19T11:00:00Z"}])
                self.schrijf(m, "funding.jsonl", [self.piek("2026-11-19T10:10:00Z", "2026-11-19T11:10:00Z", 0.5)])
            # oude regels: apart, niet geteld
            self.schrijf(vast, "funding.jsonl", [{"beurs": "kraken", "munt": "Z", "richting": "positief",
                                                  "spot": "kraken", "netto_pct": 1, "einde_run": True,
                                                  "begin": "2026-11-19T10:00:00Z", "eind": "2026-11-19T10:05:00Z"}])
            self.schrijf(vast, "stable-afwijking.jsonl", [
                {"beurs": "kraken", "munt": "EURQ", "quote": "EUR", "kant": "goedkoop", "taker": 0.002,
                 "basis_ratio": None, "ruimte_eur_max": 1000, "begin": "2026-11-19T10:00:00Z",
                 "eind": "2026-11-19T10:05:00Z", "eerste": {"na_kosten_pct": 0.5, "winst150": 1}}])
            tekst = rapport.rapport(d)
            self.assertIn("**B, funding-pieken:** 1 pieken afgerond", tekst)
            self.assertIn("1 keer kunnen instappen, samen €0,50", tekst)
            self.assertIn("1,1 uur", tekst)
            self.assertIn("zonder overmaken): 1 (waarvan 1 positief), waarvan 1 doorgeknipt", tekst)
            self.assertIn("Zonder basislijn (munt te nieuw of geen bron, niet geteld): 1", tekst)
            self.assertNotIn("None", tekst)
            tekst2 = rapport.rapport(d, met_proef=True)
            self.assertIn("**B, funding-pieken:** 1 pieken afgerond", tekst2)   # zelfde piek: één keer


class TestKrakenEnBasis(unittest.TestCase):
    def test_kraken_taker(self):
        with tempfile.TemporaryDirectory() as d:
            r = radar.Radar(d, spot_klassen=[], perp_bronnen={}, log=lambda s: None)
            r.paren = {"kraken": {("BTC", "USDT"): {"taker": None}, ("EURQ", "EUR"): {"taker": None}}}
            self.assertEqual(r.taker("kraken", "BTC", "USDT"), 0.008)
            self.assertEqual(r.taker("kraken", "EURQ", "EUR"), 0.002)
            r.paren["kraken"].update({("USDE", "USD"): {"taker": None}, ("USDG", "USDT"): {"taker": None}})
            self.assertEqual(r.taker("kraken", "USDE", "USD"), 0.0)      # GEZIEN kraken.com/pro/fees
            self.assertEqual(r.taker("kraken", "USDG", "USDT"), 0.0001)
            self.assertEqual(r.taker("kraken", "USDT", "EUR"), 0.002)
            r.paren["gate"] = {("X", "USDT"): {"taker": 0.002}}
            self.assertEqual(r.taker("gate", "X", "USDT"), 0.002)

    def test_basislijn_c2(self):
        dag0 = int(time.time()) // 86400 * 86400 - 40 * 86400
        dagen = [(dag0 + i * 86400, 0.97) for i in range(30)]
        k = {("EURQ", "EUR"): (0.969, 0.970)}
        boek = {"EURQEUR": ([(0.969, 5000)], [(0.970, 5000)])}
        x = nep_beurs("kraken", [list(k) + [("EUR", "USD")]], koersen={**k, ("EUR", "USD"): (1.1, 1.1)},
                      boeken=boek)
        with tempfile.TemporaryDirectory() as d:
            r = radar.Radar(d, spot_klassen=[x], perp_bronnen={}, log=lambda s: None,
                            basis_bron=lambda b, sym: dagen)
            r.ronde_paren()
            r.ververs_basis()
            self.assertAlmostEqual(r.basis["EURQ"]["ratio"], 0.97)
            r.ronde_stable()
            self.assertEqual(r.volg_c2.open, {})        # 3% onder de euro, maar op zijn gewone prijs: geen kans
            # nu zakt hij naar 0,95: 2% onder zijn basislijn
            x.koersen = lambda self: {("EURQ", "EUR"): (0.949, 0.950), ("EUR", "USD"): (1.1, 1.1)}
            x.boek = lambda self, sym: ([(0.949, 5000)], [(0.950, 5000)])
            r.ronde_stable()
            self.assertIn(("kraken", "EURQ", "EUR", "goedkoop"), r.volg_c2.open)
            r.afsluiten()
            c2 = lees(os.path.join(d, "stable-afwijking.jsonl"))[0]
            self.assertAlmostEqual(c2["basis_ratio"], 0.97)
            self.assertAlmostEqual(c2["eerste"]["afwijking_pct"], (0.97 - 0.95) / 0.97 * 100, places=3)
            self.assertAlmostEqual(c2["eerste"]["afwijking_koppeling_pct"], -5.0, places=3)


if __name__ == "__main__":
    unittest.main()
