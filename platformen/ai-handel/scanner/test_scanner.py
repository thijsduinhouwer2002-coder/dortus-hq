"""Tests voor de rekensom van de scanner en het rapport. Draaien: python3 -m unittest test_scanner (in deze map)."""
import json
import os
import tempfile
import unittest

import rapport
import scanner


class TestVul(unittest.TestCase):
    def test_geen_winst_als_kosten_groter(self):
        # laat 100, bod 100,3; kosten 0,2% + 0,2% = 0,4% > 0,3%
        m, uit, krijg = scanner.vul([(100, 10)], [(100.3, 10)], 0.002, 0.002, 1000)
        self.assertEqual(m, 0)

    def test_winst_en_plafond(self):
        m, uit, krijg = scanner.vul([(100, 10)], [(101, 10)], 0.001, 0.001, 500)
        self.assertAlmostEqual(uit, 500, places=6)
        self.assertGreater(krijg, uit)

    def test_stopt_bij_dunner_boek(self):
        # 1 munt te koop voor 100, daarna 102; bod 101 voor 5 munten: alleen de eerste munt is winst
        m, uit, krijg = scanner.vul([(100, 1), (102, 5)], [(101, 5)], 0, 0, 10000)
        self.assertAlmostEqual(m, 1)
        self.assertAlmostEqual(krijg - uit, 1)

    def test_meerdere_lagen(self):
        m, uit, krijg = scanner.vul([(100, 1), (100.5, 1)], [(102, 0.5), (101, 3)], 0, 0, 10000)
        self.assertAlmostEqual(m, 2)
        self.assertAlmostEqual(krijg - uit, 0.5 * 2 + 0.5 * 1 + 1 * 0.5)


class TestBereken(unittest.TestCase):
    def test_opnamekosten_eten_winst(self):
        r = scanner.bereken([(100, 10)], [(101, 10)], 0, 0, 0.02, 1.0)  # 0,02 munt = 2,02 euro opname
        self.assertAlmostEqual(r["winst100"], 1 - 2.02, places=4)   # 1 munt, 1 euro verschil, min 2,02
        self.assertAlmostEqual(r["winst_ruimte"], 10 - 2.02, places=4)  # 10 munten
        self.assertAlmostEqual(r["ruimte_eur"], 1000, places=2)

    def test_euro_omrekening(self):
        r = scanner.bereken([(1, 1000)], [(1.01, 1000)], 0, 0, 0, 0.9)
        self.assertAlmostEqual(r["ruimte_eur"], 900, places=2)
        self.assertAlmostEqual(r["winst_ruimte"], 9, places=3)

    def test_leeg_boek(self):
        self.assertIsNone(scanner.bereken([], [(1, 1)], 0, 0, 0, 1))
        self.assertFalse(scanner.is_kans(None))


class TestKandidaten(unittest.TestCase):
    def setUp(self):
        info = {"id": "x", "taker": 0.001, "contract": ""}
        self.paren = {"a": {("X", "USDT"): info, ("Y", "USDT"): info, ("Z", "EUR"): info},
                      "b": {("X", "USDT"): info, ("Y", "USDT"): info, ("Z", "USDT"): info}}

    def test_vindt_verschil_en_negeert_andere_quote(self):
        koersen = {"a": {("X", "USDT"): (0.99, 1.0), ("Z", "EUR"): (1, 1.01)},
                   "b": {("X", "USDT"): (1.01, 1.02), ("Z", "USDT"): (5, 5.1)}}
        kand, verg, verd = scanner.kandidaten(koersen, self.paren)
        self.assertEqual(verg, 1)  # Z staat in EUR en USDT: niet vergelijken
        self.assertEqual([(k[0], k[2], k[3]) for k in kand], [("X", "a", "b")])

    def test_verdacht(self):
        koersen = {"a": {("Y", "USDT"): (0.99, 1.0)}, "b": {("Y", "USDT"): (1.5, 1.6)}}
        kand, verg, verd = scanner.kandidaten(koersen, self.paren)
        self.assertEqual((kand, verd), ([], 1))


class TestNetwerk(unittest.TestCase):
    def w(self, **netten):
        return {"X": {"opname": True, "storting": True, "fee": 9.0, "contracten": set(),
                      "netwerken": {n: {"opname": o, "storting": st, "fee": fee} for n, (o, st, fee) in netten.items()}}}

    def test_open_dicht_onbekend(self):
        wallets = {"a": self.w(ETH=(True, True, 2.0), BSC=(True, True, 0.5)), "b": self.w(ETH=(True, True, None)),
                   "c": self.w(ETH=(True, False, None)), "d": self.w(SOL=(True, True, None)), "e": {}}
        self.assertEqual(scanner.netwerk_stand(wallets, "a", "b", "X"), ("open", 2.0))  # fee van het gedeelde net
        self.assertEqual(scanner.netwerk_stand(wallets, "a", "c", "X"), ("dicht", None))  # storten dicht op c
        self.assertEqual(scanner.netwerk_stand(wallets, "a", "d", "X"), ("onbekend", None))
        self.assertEqual(scanner.netwerk_stand(wallets, "a", "e", "X"), ("onbekend", None))

    def test_namen_koppelen(self):
        import beurzen
        self.assertEqual({beurzen.net(x) for x in ("ERC20", "Ethereum", "ETH", "Ethereum(ERC20)")}, {"ETH"})
        self.assertEqual({beurzen.net(x) for x in ("BEP20", "BNB Smart Chain", "BSC")}, {"BSC"})

    def test_grens_op_het_boek(self):
        r = scanner.bereken([(1, 1000)], [(1.2, 1000)], 0, 0, 0, 1.0)  # 20% op het boek
        self.assertFalse(scanner.is_kans(r))


class TestRooster(unittest.TestCase):
    """Open kansen met opnemen dicht mogen de nooit gecontroleerde kandidaten niet verdringen."""

    def test_dichte_kansen_wachten(self):
        n_munten = 30

        class A:
            naam = "a"
            def paren(self): return {(f"M{i}", "EUR"): {"id": f"M{i}", "taker": 0.0, "contract": ""} for i in range(n_munten)}
            def wallet(self): return {f"M{i}": {"opname": False, "storting": True, "fee": 0.0, "contracten": set()}
                                      for i in range(n_munten)}
            def koersen(self): return {(f"M{i}", "EUR"): (0.99, 1.0) for i in range(n_munten)}
            def boek(self, s): return [(0.99, 1000)], [(1.0, 1000)]

        class B(A):
            naam = "b"
            def koersen(self): return {(f"M{i}", "EUR"): (1.05, 1.06) for i in range(n_munten)}
            def boek(self, s): return [(1.05, 1000)], [(1.06, 1000)]

        with tempfile.TemporaryDirectory() as d:
            s = scanner.Scanner(d, max_checks=10, beurs_klassen=[A, B], log=lambda x: None)
            for _ in range(3):
                s.ronde()
            # 30 kandidaten (opnemen dicht op a), 10 per ronde: na 3 rondes is elke kandidaat één keer gezien
            self.assertEqual(len(s.gecheckt), n_munten)
            self.assertEqual(len(s.open), n_munten)
            s.pool.shutdown()


class TestScannerVolgen(unittest.TestCase):
    """Nepbeurzen: een kans die 3 rondes staat en dan weg is, geeft één regel met de juiste duur."""

    def test_kans_open_en_dicht(self):
        stappen = {"n": 0}

        class A:
            naam = "a"
            def paren(self): return {("X", "EUR"): {"id": "X-EUR", "taker": 0.001, "contract": ""}}
            def wallet(self): return {"X": {"opname": True, "storting": True, "fee": 0.1, "contracten": set()}}
            def koersen(self): return {("X", "EUR"): (0.99, 1.0)}
            def boek(self, s): return [(0.99, 1000)], [(1.0, 1000)]

        class B(A):
            naam = "b"
            def koersen(self):
                return {("X", "EUR"): (1.02, 1.03) if stappen["n"] < 3 else (0.99, 1.0)}
            def boek(self, s):
                return ([(1.02, 1000)], [(1.03, 1000)]) if stappen["n"] < 3 else ([(0.99, 1)], [(1.0, 1)])

        with tempfile.TemporaryDirectory() as d:
            s = scanner.Scanner(d, beurs_klassen=[A, B], log=lambda x: None)
            for i in range(5):
                stappen["n"] = i
                s.ronde()
            with open(os.path.join(d, "kansen.jsonl")) as fh:
                regels = [json.loads(x) for x in fh]
            self.assertEqual(len(regels), 1)
            r = regels[0]
            self.assertEqual((r["koop"], r["verkoop"], r["metingen"]), ("a", "b", 3))
            self.assertTrue(r["opname_koop"] and r["storting_verkoop"])
            self.assertGreater(r["winst500_med"], 0)
            s.pool.shutdown()


class TestRapport(unittest.TestCase):
    def regel(self, **kw):
        r = {"munt": "X", "quote": "USDT", "koop": "a", "verkoop": "b", "opname_koop": True,
             "storting_verkoop": True, "contract": "zelfde", "duur_s": 300, "ruimte_eur_med": 400,
             "winst_ruimte_med": 5, "winst100_med": 1, "winst500_med": 4, "winst1000_med": 4,
             "winst2500_med": 4, "begin": "2026-11-19T10:00:00Z", "eind": "2026-11-19T10:05:00Z",
             "opname_bron": "beurs", "netwerk": "open"}
        r.update(kw)
        return r

    def test_filter(self):
        self.assertTrue(rapport.echt(self.regel()))
        self.assertFalse(rapport.echt(self.regel(opname_koop=None)))
        self.assertFalse(rapport.echt(self.regel(storting_verkoop=False)))
        self.assertFalse(rapport.echt(self.regel(duur_s=60)))
        self.assertFalse(rapport.echt(self.regel(ruimte_eur_med=50)))
        self.assertFalse(rapport.echt(self.regel(contract="anders")))
        self.assertFalse(rapport.echt(self.regel(winst_ruimte_med=-1)))
        self.assertFalse(rapport.echt(self.regel(opname_bron="onbekend")))
        self.assertFalse(rapport.echt(self.regel(netwerk="dicht")))
        self.assertTrue(rapport.echt(self.regel(netwerk="onbekend", contract="onbekend")))

    def test_vergund_en_grijs(self):
        self.assertEqual(rapport.soort(self.regel(koop="kraken", verkoop="bitvavo")), "vergund")
        self.assertEqual(rapport.soort(self.regel(koop="mexc", verkoop="kraken")), "grijs")

    def test_samenvoegen(self):
        a = self.regel(koop="a", verkoop="b", winst500_med=4)
        b = self.regel(koop="c", verkoop="b", winst500_med=9, begin="2026-11-19T10:03:00Z")
        c = self.regel(begin="2026-11-19T11:00:00Z", eind="2026-11-19T11:05:00Z")
        d = self.regel(munt="Y")
        g = rapport.gebeurtenissen([a, b, c, d])
        self.assertEqual(len(g), 3)
        self.assertIn(b, g)  # de beste van de overlappende twee telt

    def test_rapport_draait(self):
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, "2026-11-19", "run1"))
            with open(os.path.join(d, "2026-11-19", "run1", "kansen.jsonl"), "w") as fh:
                for i in range(3):
                    fh.write(json.dumps(self.regel(duur_s=200 * (i + 1))) + "\n")
                fh.write(json.dumps(self.regel(opname_koop=False)) + "\n")
                fh.write(json.dumps(self.regel(koop="kraken", verkoop="bitvavo", munt="Z")) + "\n")
            with open(os.path.join(d, "2026-11-19", "run1", "stand.jsonl"), "w") as fh:
                fh.write(json.dumps({"t": "2026-11-19T10:00:00Z", "kandidaten": 100, "gecontroleerd": 50,
                                     "nooit_gecontroleerd": 40}) + "\n")
                fh.write(json.dumps({"t": "2026-11-19T12:00:00Z"}) + "\n")
            tekst = rapport.maak(d)
            self.assertIn("Echte kansen", tekst)
            self.assertIn("ondergrens", tekst)
            self.assertIn("Alleen MiCA", tekst)
            self.assertIn("| Alleen MiCA | €2.000,00 | bovengrens", tekst)  # som voor vergund apart
            self.assertIn("kraken > bitvavo | vergund", tekst)
            os.makedirs(os.path.join(d, "2026-11-19", "run2-proef"))
            with open(os.path.join(d, "2026-11-19", "run2-proef", "kansen.jsonl"), "w") as fh:
                fh.write(json.dumps(self.regel(munt="P")) + "\n")
            self.assertNotIn("P-USDT", rapport.maak(d))
            self.assertIn("P-USDT", rapport.maak(d, met_proef=True))


if __name__ == "__main__":
    unittest.main()
