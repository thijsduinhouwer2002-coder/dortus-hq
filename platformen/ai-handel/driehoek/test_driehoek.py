"""Tests voor de rekensom van de driehoek-meter en het rapport. Draaien: python3 -m unittest test_driehoek (in deze map).
Geen netwerk: alle boeken en koersen zijn verzonnen voorbeelden."""
import json
import os
import tempfile
import unittest

import driehoek as D
import rapport as R

INF = float("inf")


def stappen(kosten=0.0, mins=None):
    """EUR > BTC > ETH > EUR met paren BTC-EUR (koop), ETH-BTC (koop), ETH-EUR (verkoop)."""
    paren = {("BTC", "EUR"): {"id": "BTC-EUR"}, ("ETH", "BTC"): {"id": "ETH-BTC"}, ("ETH", "EUR"): {"id": "ETH-EUR"}}
    kv = {sl: (kosten, kosten, "test") for sl in paren}
    return D.maak_stappen(["EUR", "BTC", "ETH"], paren, kv, mins)


class TestLoop(unittest.TestCase):
    def test_koop_over_lagen(self):
        # 150 euro: 1 munt voor 100, dan 50 euro voor 0,4 munt tegen 125
        self.assertAlmostEqual(D.loop([(100, 1), (125, 10)], 150, True), 1.4)

    def test_verkoop_over_lagen(self):
        self.assertAlmostEqual(D.loop([(100, 1), (90, 10)], 1.5, False), 100 + 45)

    def test_te_dun_boek(self):
        self.assertIsNone(D.loop([(100, 1)], 200, True))
        self.assertIsNone(D.loop([(100, 1)], 2, False))


class TestDriehoeken(unittest.TestCase):
    def test_beide_richtingen_en_begin_eur(self):
        paren = {("BTC", "EUR"): {}, ("ETH", "BTC"): {}, ("ETH", "EUR"): {}, ("XRP", "EUR"): {}}
        d = D.driehoeken(paren)
        self.assertEqual(len(d), 2)                       # één driehoek, twee richtingen; XRP hoort er niet bij
        self.assertTrue(all(v[0] == "EUR" for v in d))

    def test_kant_van_elke_stap(self):
        st = stappen()
        self.assertEqual([s["koop"] for s in st], [True, True, False])
        self.assertEqual([s["paar"] for s in st], ["BTC-EUR", "ETH-BTC", "ETH-EUR"])


class TestRekensom(unittest.TestCase):
    def setUp(self):
        # BTC 50.000 euro, ETH 0,05 BTC (= 2.500 euro), ETH-EUR bod 2.550: 2% winst voor kosten
        self.prijzen = {("BTC", "EUR"): (49990, 50000), ("ETH", "BTC"): (0.0499, 0.05), ("ETH", "EUR"): (2550, 2560)}
        self.boeken = {"BTC-EUR": ([(49990, 10)], [(50000, 0.01), (51000, 10)]),
                       "ETH-BTC": ([(0.0499, 100)], [(0.05, 100)]),
                       "ETH-EUR": ([(2550, 100)], [(2560, 100)])}

    def test_top_met_en_zonder_kosten(self):
        self.assertAlmostEqual(D.top(stappen(), self.prijzen, "hoog"), 1.02)
        self.assertAlmostEqual(D.top(stappen(0.01), self.prijzen, "hoog"), 1.02 * 0.99 ** 3)
        self.assertEqual(D.top(stappen(), {}, "hoog"), 0.0)

    def test_kosten_eten_winst(self):
        self.assertLess(D.top(stappen(0.008), self.prijzen, "hoog"), 1)   # Kraken: 3 x 0,80% > 2%
        self.assertIsNone(D.curve(stappen(0.008), self.boeken, 1.0, "hoog"))

    def test_diepte_stopt_waar_het_boek_duurder_wordt(self):
        r = D.curve(stappen(), self.boeken, 1.0, "hoog")
        # alleen 0,01 BTC (= €500) ligt op 50.000; daarna 51.000 en dan is het verlies (2550/2550 = 0%)
        self.assertGreater(r["winst_eur"], 0)
        self.assertLessEqual(r["diepte_eur"], 1000)
        self.assertGreaterEqual(r["diepte_eur"], 500)
        self.assertAlmostEqual(r["winst_bij"]["100"], 2.0, places=6)      # 2% van €100
        self.assertAlmostEqual(r["winst_bij"]["500"], 10.0, places=6)
        self.assertGreaterEqual(r["winst_bij"]["5000"], r["winst_bij"]["2000"])   # minder inleggen mag
        self.assertLessEqual(r["pct"], 2.0 + 1e-9)

    def test_boek_nooit_beter_dan_top(self):
        r = D.curve(stappen(0.002), self.boeken, 1.0, "hoog")
        self.assertLessEqual(r["pct"] / 100, D.top(stappen(0.002), self.prijzen, "hoog") - 1 + 1e-12)

    def test_minimale_ordergrootte(self):
        # ETH-EUR minimaal 0,1 ETH (= €250): met €100 kan het niet
        st = stappen(0.0, {("ETH", "EUR"): {"base": 0.1}})
        r = D.curve(st, self.boeken, 1.0, "hoog")
        self.assertEqual(r["winst_bij"]["100"], 0.0)
        self.assertEqual(r["winst_bij"]["150"], 0.0)
        self.assertGreaterEqual(r["min_inleg_eur"], 250)
        self.assertGreater(r["winst_bij"]["500"], 0)
        self.assertEqual(D.min_inleg(st, self.prijzen, 1.0), min(b for b in D.BEDRAGEN if b >= 250))

    def test_minimum_in_quote(self):
        st = stappen(0.0, {("BTC", "EUR"): {"quote": 5}})
        self.assertEqual(D.min_inleg(st, self.prijzen, 1.0), 10)   # €5 minimum, kleinste bedrag dat we toetsen is €10


class TestKosten(unittest.TestCase):
    def test_kraken(self):
        self.assertEqual(D.kosten("kraken", ("ETH", "BTC"), {})[0], 0.008)
        self.assertEqual(D.kosten("kraken", ("USDT", "EUR"), {})[0], 0.002)
        self.assertEqual(D.kosten("kraken", ("EUR", "USD"), {})[0], 0.002)

    def test_bitvavo_onzeker(self):
        self.assertEqual(D.kosten("bitvavo", ("BTC", "EUR"), {}, "A")[:2], (0.0025, 0.0025))
        self.assertEqual(D.kosten("bitvavo", ("BTC", "USDC"), {}, "B")[:2], (0.0025, 0.0))

    def test_uit_api(self):
        self.assertEqual(D.kosten("mexc", ("ETH", "USDT"), {"taker": 0.0005})[0], 0.0005)


class NepSchrijver:
    def __init__(self):
        self.regels = []

    def regel(self, naam, d):
        self.regels.append(json.loads(json.dumps(d)))

    def bestand(self, naam, d):
        pass


class TestVolgen(unittest.TestCase):
    def test_open_en_sluiten(self):
        s = NepSchrijver()
        m = D.Meter(type("Nep", (), {"naam": "okx"})(), s, None)
        st = stappen()
        c = {"id": "EUR>BTC>ETH>EUR", "munten": ["EUR", "BTC", "ETH"], "stappen": st}
        goed = {"BTC-EUR": ([(49990, 10)], [(50000, 10)]), "ETH-BTC": ([(0.0499, 100)], [(0.05, 100)]),
                "ETH-EUR": ([(2550, 100)], [(2560, 100)])}
        slecht = dict(goed, **{"ETH-EUR": ([(2400, 100)], [(2410, 100)])})
        self.assertTrue(m.verwerk(c, goed, 1.0, 1000.0))
        self.assertTrue(m.verwerk(c, goed, 1.0, 1004.0))
        self.assertFalse(m.verwerk(c, slecht, 1.0, 1008.0))
        self.assertEqual(len(s.regels), 1)
        r = s.regels[0]
        self.assertEqual(r["duur_s"], 4.0)
        self.assertEqual(r["hoog"]["checks"], 2)
        self.assertEqual(r["eind_reden"], "boek")
        self.assertEqual(r["status"], "MiCA-dochter")
        self.assertTrue(R.echt(r))


def regel(beurs="okx", status="MiCA-dochter", winst=5.0, diepte=1000, duur=10, verdacht=False, dag="2026-11-20",
          min_inleg=10):
    h = {"begin": f"{dag}T10:00:00Z", "eind": f"{dag}T10:00:10Z", "checks": 3, "winst_eur": winst,
         "diepte_eur": diepte, "pct": 0.5, "best_eur": diepte, "duur_s": duur, "min_inleg_eur": min_inleg,
         "winst_bij": {str(k): min(winst, winst * k / diepte) for k in D.VASTE}}
    return {"beurs": beurs, "status": status, "driehoek": "EUR>BTC>ETH>EUR", "kosten": [0.001] * 3, "zeker": True,
            "hoog": h, "laag": h, "winst_mediaan_eur": winst, "duur_s": duur, "verdacht": verdacht,
            "begin": h["begin"]}


class TestRapport(unittest.TestCase):
    def test_echt(self):
        self.assertTrue(R.echt(regel()))
        self.assertFalse(R.echt(regel(diepte=50)))
        self.assertFalse(R.echt(regel(duur=0)))
        self.assertFalse(R.echt(regel(verdacht=True)))
        r = regel()
        r["hoog"] = None
        self.assertFalse(R.echt(r))

    def test_soort(self):
        self.assertEqual(R.soort(regel(status="MiCA")), "vergund")
        self.assertEqual(R.soort(regel(status="MiCA-dochter")), "vergund")
        self.assertEqual(R.soort(regel(beurs="mexc", status="grijs")), "grijs")

    def test_rapport_en_proef(self):
        with tempfile.TemporaryDirectory() as d:
            for run, rs in (("run-1", [regel(), regel(beurs="mexc", status="grijs", winst=2.0)]),
                            ("run-2-proef", [regel(winst=99.0)])):
                os.makedirs(os.path.join(d, "2026-11-20", run))
                with open(os.path.join(d, "2026-11-20", run, "driehoeken.jsonl"), "w") as fh:
                    fh.write("\n".join(json.dumps(r) for r in rs) + "\n{half")
                with open(os.path.join(d, "2026-11-20", run, "stand.jsonl"), "w") as fh:
                    for b, st in (("okx", "MiCA-dochter"), ("mexc", "grijs")):
                        for _ in range(12):
                            fh.write(json.dumps({"beurs": b, "status": st, "rondes": 100, "kandidaten": 5,
                                                 "bekeken": 5, "beste_marge_med": -0.1, "beste_marge_max": 0.2,
                                                 "t": "2026-11-20T10:00:00Z"}) + "\n")
                with open(os.path.join(d, "2026-11-20", run, "beurs-okx.json"), "w") as fh:
                    json.dump({"geladen": "2026-11-20T10:00:00Z", "min_inleg": {
                        "driehoeken": 10, "mediaan_eur": 10, "met_eur": 4, "tot_100": 9, "tot_150": 9,
                        "tot_200": 10, "met_eur_tot_100": 4}}, fh)
            t = R.maak(d)
            self.assertIn("| 2026-11-20 | Alle beurzen | 2 |", t)
            self.assertIn("| 2026-11-20 | Grijs | 1 |", t)
            self.assertNotIn("99,00", t)                    # proefrun telt niet
            self.assertIn("€100", t)
            self.assertIn("| okx | MiCA-dochter | 10 | 4 | ≤ €10 | 9 | 9 | 10 | 4 |", t)
            self.assertIn("99,00", R.maak(d, met_proef=True))

    def test_leeg(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIn("Nog geen echte driehoeken", R.maak(d))


if __name__ == "__main__":
    unittest.main()
