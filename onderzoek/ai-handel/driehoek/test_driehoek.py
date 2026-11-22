"""Tests voor de rekensom van de driehoek-meter en het rapport. Draaien: python3 -m unittest test_driehoek (in deze map).
Geen netwerk: alle boeken en koersen zijn verzonnen voorbeelden."""
import json
import os
import tempfile
import unittest

import driehoek as D
import kosten as K
import rapport as R
import reken as Rk
import volgen as V

INF = float("inf")


def stappen(kosten=0.0, mins=None):
    """EUR > BTC > ETH > EUR met paren BTC-EUR (koop), ETH-BTC (koop), ETH-EUR (verkoop)."""
    paren = {("BTC", "EUR"): {"id": "BTC-EUR"}, ("ETH", "BTC"): {"id": "ETH-BTC"}, ("ETH", "EUR"): {"id": "ETH-EUR"}}
    kv = {sl: (kosten, kosten, "test") for sl in paren}
    return Rk.maak_stappen(["EUR", "BTC", "ETH"], paren, kv, mins)


class TestLoop(unittest.TestCase):
    def test_koop_over_lagen(self):
        # 150 euro: 1 munt voor 100, dan 50 euro voor 0,4 munt tegen 125
        self.assertAlmostEqual(Rk.loop([(100, 1), (125, 10)], 150, True), 1.4)

    def test_verkoop_over_lagen(self):
        self.assertAlmostEqual(Rk.loop([(100, 1), (90, 10)], 1.5, False), 100 + 45)

    def test_te_dun_boek(self):
        self.assertIsNone(Rk.loop([(100, 1)], 200, True))
        self.assertIsNone(Rk.loop([(100, 1)], 2, False))


class TestDriehoeken(unittest.TestCase):
    def test_beide_richtingen_en_begin_eur(self):
        paren = {("BTC", "EUR"): {}, ("ETH", "BTC"): {}, ("ETH", "EUR"): {}, ("XRP", "EUR"): {}}
        d = Rk.driehoeken(paren)
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
        self.assertAlmostEqual(Rk.top(stappen(), self.prijzen, "hoog"), 1.02)
        self.assertAlmostEqual(Rk.top(stappen(0.01), self.prijzen, "hoog"), 1.02 * 0.99 ** 3)
        self.assertEqual(Rk.top(stappen(), {}, "hoog"), 0.0)

    def test_kosten_eten_winst(self):
        self.assertLess(Rk.top(stappen(0.008), self.prijzen, "hoog"), 1)   # Kraken: 3 x 0,80% > 2%
        self.assertIsNone(Rk.curve(stappen(0.008), self.boeken, 1.0, "hoog"))

    def test_diepte_stopt_waar_het_boek_duurder_wordt(self):
        r = Rk.curve(stappen(), self.boeken, 1.0, "hoog")
        # alleen 0,01 BTC (= €500) ligt op 50.000; daarna 51.000 en dan is het verlies (2550/2550 = 0%)
        self.assertGreater(r["winst_eur"], 0)
        self.assertLessEqual(r["diepte_eur"], 1000)
        self.assertGreaterEqual(r["diepte_eur"], 500)
        self.assertAlmostEqual(r["winst_bij"]["100"], 2.0, places=6)      # 2% van €100
        self.assertAlmostEqual(r["winst_bij"]["500"], 10.0, places=6)
        self.assertGreaterEqual(r["winst_bij"]["5000"], r["winst_bij"]["2000"])   # minder inleggen mag
        self.assertLessEqual(r["pct"], 2.0 + 1e-9)

    def test_boek_nooit_beter_dan_top(self):
        r = Rk.curve(stappen(0.002), self.boeken, 1.0, "hoog")
        self.assertLessEqual(r["pct"] / 100, Rk.top(stappen(0.002), self.prijzen, "hoog") - 1 + 1e-12)

    def test_minimale_ordergrootte(self):
        # ETH-EUR minimaal 0,1 ETH (= €250): met €100 kan het niet
        st = stappen(0.0, {("ETH", "EUR"): {"base": 0.1}})
        r = Rk.curve(st, self.boeken, 1.0, "hoog")
        self.assertEqual(r["winst_bij"]["100"], 0.0)
        self.assertEqual(r["winst_bij"]["150"], 0.0)
        self.assertGreaterEqual(r["min_inleg_eur"], 250)
        self.assertGreater(r["winst_bij"]["500"], 0)
        self.assertEqual(Rk.min_inleg(st, self.prijzen, 1.0), min(b for b in Rk.BEDRAGEN if b >= 250))

    def test_minimum_in_quote(self):
        st = stappen(0.0, {("BTC", "EUR"): {"quote": 5}})
        self.assertEqual(Rk.min_inleg(st, self.prijzen, 1.0), 10)   # €5 minimum, kleinste bedrag dat we toetsen is €10

    def test_stapgrootte_hele_munten(self):
        # ETH alleen in hele munten (stap 1): €100 levert 0,04 ETH op, naar beneden afgerond 0: kan niet
        st = stappen(0.0, {("ETH", "BTC"): {"stap": 1.0}})
        r = Rk.curve(st, self.boeken, 1.0, "hoog")
        self.assertEqual(r["winst_bij"]["100"], 0.0)
        self.assertGreaterEqual(r["min_inleg_eur"], 2500)

    def test_afronding_eet_winst_niet_op_bij_fijne_stap(self):
        st = stappen(0.0, {("ETH", "BTC"): {"stap": 0.0001}})
        r = Rk.curve(st, self.boeken, 1.0, "hoog")
        self.assertAlmostEqual(r["winst_bij"]["100"], 2.0, places=2)   # 2% van wat rondging, bijna €100

    def test_vaste_kosten_bitvavo(self):
        st = stappen(0.0)
        for x in st:
            x["vast_eur"] = K.vaste_kosten_eur("bitvavo", x["sleutel"])
        self.assertEqual([x["vast_eur"] for x in st], [0.01, 0.0, 0.01])   # alleen de euro-orders
        r = Rk.curve(st, self.boeken, 1.0, "hoog")
        self.assertAlmostEqual(r["winst_bij"]["100"], 2.0 - 0.02, places=6)


class TestKosten(unittest.TestCase):
    def test_kraken(self):
        self.assertEqual(K.kosten("kraken", ("ETH", "BTC"), {})[0], 0.008)
        self.assertEqual(K.kosten("kraken", ("USDT", "EUR"), {})[0], 0.002)
        self.assertEqual(K.kosten("kraken", ("EUR", "USD"), {})[0], 0.002)

    def test_kraken_usde_usdg_gekoppeld(self):
        self.assertEqual(K.kosten("kraken", ("USDE", "EUR"), {})[0], 0.0)
        self.assertEqual(K.kosten("kraken", ("USDE", "USDT"), {})[0], 0.0)
        self.assertEqual(K.kosten("kraken", ("USDG", "USD"), {})[0], 0.0001)
        self.assertEqual(K.kosten("kraken", ("TBTC", "BTC"), {})[0], 0.002)
        self.assertEqual(K.kosten("kraken", ("WBTC", "BTC"), {})[0], 0.002)
        self.assertEqual(K.kosten("kraken", ("LSETH", "ETH"), {})[0], 0.008)   # niet genoemd: voorzichtig
        self.assertEqual(K.kosten("kraken", ("USDGO", "USD"), {})[0], 0.002)   # andere stablecoin dan USDG: 0,20%

    def test_bitstamp_en_okx(self):
        self.assertEqual(K.kosten("bitstamp", ("BTC", "EUR"), {})[0], 0.004)
        self.assertEqual(K.kosten("bitstamp", ("USDT", "EUR"), {})[0], 0.0008)
        self.assertEqual(K.kosten("okx", ("BTC", "EUR"), {"taker": None})[0], 0.001)

    def test_bitstamp_minimum_lezen(self):
        m = {"name": "ETH/BTC", "minimum_order": "0.00005000 BTC", "base_decimals": 8}
        self.assertEqual(K.bitstamp_minimum(m), {"stap": 1e-8, "quote": 0.00005})
        m = {"name": "BTC/USD", "minimum_order": "10.00 USD", "base_decimals": 8}
        self.assertEqual(K.bitstamp_minimum(m)["quote"], 10.0)

    def test_afronden(self):
        self.assertAlmostEqual(K.afronden(1.23456, 0.01), 1.23)
        self.assertEqual(K.afronden(0.9, 1.0), 0.0)
        self.assertEqual(K.afronden(3.0, 1.0), 3.0)       # geen fout door 2.9999999
        self.assertEqual(K.afronden(1.5, 0), 1.5)

    def test_bitvavo_onzeker(self):
        self.assertEqual(K.kosten("bitvavo", ("BTC", "EUR"), {}, "A")[:2], (0.0025, 0.0025))
        self.assertEqual(K.kosten("bitvavo", ("BTC", "USDC"), {}, "B")[:2], (0.0025, 0.0))

    def test_uit_api(self):
        self.assertEqual(K.kosten("mexc", ("ETH", "USDT"), {"taker": 0.0005})[0], 0.0005)


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
        self.assertEqual(r["hoog"]["na_3s"]["t"], "1970-01-01T00:16:44Z")    # de latere meting (t = 1004)

    def test_na_3_seconden_te_dun_is_niet_echt(self):
        # keuring A9: eerste meting veel diepte, 4 s later nog maar ±€20, daarna weg
        s = NepSchrijver()
        m = D.Meter(type("Nep", (), {"naam": "okx"})(), s, None)
        c = {"id": "EUR>BTC>ETH>EUR", "munten": ["EUR", "BTC", "ETH"], "stappen": stappen()}
        diep = {"BTC-EUR": ([(49990, 10)], [(50000, 10)]), "ETH-BTC": ([(0.0499, 100)], [(0.05, 100)]),
                "ETH-EUR": ([(2550, 100)], [(2560, 100)])}
        dun = dict(diep, **{"BTC-EUR": ([(49990, 10)], [(50000, 0.0004), (52000, 10)])})
        weg = dict(diep, **{"ETH-EUR": ([(2400, 100)], [(2410, 100)])})
        m.verwerk(c, diep, 1.0, 1000.0)
        m.verwerk(c, dun, 1.0, 1004.0)
        m.verwerk(c, weg, 1.0, 1008.0)
        r = s.regels[0]
        self.assertGreaterEqual(r["hoog"]["diepte_eur"], 5000)          # het beste moment was diep
        self.assertIsNone(r["hoog"]["na_3s"])
        self.assertFalse(R.echt(r))

    def test_bevestigd(self):
        m = lambda t, d, w=1.0: {"t": t, "diepte_eur": d, "winst_eur": w}
        self.assertEqual(V.bevestigd([m(0, 500), m(3, 200)])[0]["t"], 3)
        self.assertIsNone(V.bevestigd([m(0, 500), m(2, 200)])[0])          # te kort
        self.assertIsNone(V.bevestigd([m(0, 500), m(2, 50), m(4, 500)])[0])   # onderbroken
        self.assertEqual(V.bevestigd([m(0, 50), m(2, 500), m(5, 500)])[0]["t"], 5)
        self.assertEqual(V.bevestigd([m(0, 500), m(4, 500), m(9, 500)])[1], 9)


def regel(beurs="okx", status="MiCA-dochter", winst=5.0, diepte=1000, duur=10, verdacht=False, dag="2026-11-20",
          min_inleg=10, begin="10:00:00", eind="10:00:10", na_t=None, driehoek="EUR>BTC>ETH>EUR", na_3s=True):
    wb = {str(k): min(winst, winst * k / diepte) for k in Rk.VASTE}
    na = {"t": f"{dag}T{na_t or begin}Z", "winst_eur": winst, "diepte_eur": diepte, "pct": 0.5, "best_eur": diepte,
          "min_inleg_eur": min_inleg, "winst_bij": wb} if na_3s and duur >= 3 and diepte >= 100 else None
    h = {"begin": f"{dag}T{begin}Z", "eind": f"{dag}T{eind}Z", "checks": 3, "winst_eur": winst,
         "diepte_eur": diepte, "pct": 0.5, "best_eur": diepte, "duur_s": duur, "duur_100_s": duur,
         "min_inleg_eur": min_inleg, "winst_bij": wb, "na_3s": na}
    m = driehoek.split(">")
    return {"beurs": beurs, "status": status, "driehoek": driehoek, "kosten": [0.001] * 3, "zeker": True,
            "paren": [f"{m[i]}-{m[i + 1]}" for i in range(3)], "hoog": h, "laag": h, "winst_mediaan_eur": winst,
            "duur_s": duur, "verdacht": verdacht, "begin": h["begin"], "eind": h["eind"]}


class TestRapport(unittest.TestCase):
    def test_echt(self):
        self.assertTrue(R.echt(regel()))
        self.assertFalse(R.echt(regel(diepte=50)))
        self.assertFalse(R.echt(regel(duur=0)))
        self.assertFalse(R.echt(regel(verdacht=True)))
        self.assertFalse(R.echt(regel(winst=0.04)))                     # ondergrens €0,05
        r = regel()
        r["hoog"] = None
        self.assertFalse(R.echt(r))

    def test_zelfde_kans_via_eur_en_usdt_telt_een_keer(self):
        # één scheve XRP/BTC-prijs, gezien via EUR en via USDT in dezelfde ronde: één kans, de beste telt
        a = regel(winst=5.0, driehoek="EUR>BTC>XRP>EUR", na_t="10:00:03")
        b = regel(winst=3.0, driehoek="USDT>BTC>XRP>USDT", na_t="10:00:04")
        self.assertEqual(len(R.kansen([a, b])), 1)
        self.assertEqual(R.beste([a, b])["hoog"]["winst_eur"], 5.0)
        self.assertEqual(len(R.kansen([a, regel(winst=3.0, driehoek="USDT>BTC>XRP>USDT", na_t="10:00:09")])), 2)
        self.assertEqual(len(R.kansen([a, regel(winst=3.0, driehoek="USDT>BTC>XRP>USDT", na_t="10:00:04",
                                               beurs="mexc", status="grijs")])), 2)
        with tempfile.TemporaryDirectory() as dd:
            os.makedirs(os.path.join(dd, "2026-11-20", "run-1"))
            with open(os.path.join(dd, "2026-11-20", "run-1", "driehoeken.jsonl"), "w") as fh:
                fh.write("\n".join(json.dumps(r) for r in (a, b)) + "\n")
            with open(os.path.join(dd, "2026-11-20", "run-1", "stand.jsonl"), "w") as fh:
                for _ in range(288):     # 24 uur aan standregels van één beurs
                    fh.write(json.dumps({"beurs": "okx", "status": "MiCA-dochter", "t": "2026-11-20T10:00:00Z"}) + "\n")
            t = R.maak(dd)
            self.assertIn("| 2026-11-20 | Alle beurzen | 2 | 1 |", t)
            self.assertIn("| Alle beurzen | €5.000 | 1,0 / 2,0 | €5,00 / €8,00 |", t)   # samengevoegd en los
            self.assertIn("1 echte kansen die met €100 konden (2 als je elke driehoek los telt", t)

    def test_keuring_a_alleen_hoofdpaar_gedeeld(self):
        # (a) twee losse scheve paren (BTC/XRP en BTC/ADA) die alleen het diepe BTC/EUR delen: twee kansen
        a = regel(winst=5.0, driehoek="EUR>BTC>XRP>EUR", na_t="10:00:03")
        b = regel(winst=4.0, driehoek="EUR>BTC>ADA>EUR", na_t="10:00:03")
        self.assertEqual(len(R.kansen([a, b])), 2)

    def test_keuring_b_geen_ketting(self):
        # (b) A deelt EUR/XRP met B, B deelt EUR/DOT met C, A en C delen niets: A en C nooit samen
        a = regel(winst=3.0, driehoek="EUR>XRP>BTC>EUR", na_t="10:00:03")
        b = regel(winst=5.0, driehoek="EUR>XRP>DOT>EUR", na_t="10:00:03")
        c = regel(winst=4.0, driehoek="EUR>DOT>SOL>EUR", na_t="10:00:03")
        groepen = R.kansen([a, b, c])
        self.assertEqual(len(groepen), 2)
        for g in groepen:
            self.assertFalse(a in g and c in g)

    def test_keuring_c_lange_open_tijd_voegt_niet_samen(self):
        # (c) een driehoek die 2 uur openstaat, voegt twee kansen die 80 minuten uit elkaar liggen niet samen
        a = regel(winst=3.0, driehoek="EUR>BTC>XRP>EUR", begin="10:00:00", eind="10:00:10", na_t="10:00:03")
        b = regel(winst=5.0, driehoek="USDT>BTC>XRP>USDT", begin="10:00:00", eind="12:00:00", na_t="10:00:04")
        c = regel(winst=4.0, driehoek="USDC>BTC>XRP>USDC", begin="11:20:00", eind="11:20:10", na_t="11:20:03")
        groepen = R.kansen([a, b, c])
        self.assertEqual(len(groepen), 2)
        for g in groepen:
            self.assertFalse(a in g and c in g)

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
            self.assertIn("| 2026-11-20 | Alle beurzen | 2 | 2 |", t)
            self.assertIn("| 2026-11-20 | Grijs | 1 | 1 |", t)
            self.assertLess(t.index("## Kort antwoord"), t.index("| Beurs |"))
            self.assertNotIn("99,00", t)                    # proefrun telt niet
            self.assertIn("€100", t)
            self.assertIn("| okx | MiCA-dochter | 10 | 4 | ≤ €10 | 9 | 9 | 10 | 4 |", t)
            self.assertIn("99,00", R.maak(d, met_proef=True))

    def test_leeg(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIn("Nog geen echte driehoeken", R.maak(d))


if __name__ == "__main__":
    unittest.main()
