#!/usr/bin/env python3
"""Tests voor de rekenregels van de schaduwbot. Draaien: python3 -m unittest test_schaduwbot.py (zonder netwerk)."""
import gzip
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rapport  # noqa: E402
import schaduwbot as s  # noqa: E402


class Formule(unittest.TestCase):
    def test_punten_voorbeeld_docs(self):
        # docs: v = 3 cent, 1 cent van het midden -> (2/3)^2
        self.assertAlmostEqual(s.punten(3, 1), 4 / 9)
        self.assertAlmostEqual(s.punten(3, 2), 1 / 9)
        self.assertEqual(s.punten(3, 3), 0.0)
        self.assertEqual(s.punten(3, 5), 0.0)

    def test_q_min_eenzijdig_alleen_tussen_10_en_90(self):
        self.assertAlmostEqual(s.q_min(90, 0, 0.5), 30)
        self.assertEqual(s.q_min(90, 0, 0.05), 0)
        self.assertEqual(s.q_min(90, 0, 0.95), 0)
        self.assertEqual(s.q_min(40, 60, 0.5), 40)

    def test_aangepast_midden_slaat_kleine_orders_over(self):
        bids = [(0.50, 5), (0.48, 100)]
        asks = [(0.52, 100)]
        self.assertAlmostEqual(s.aangepast_midden(bids, asks, 20), 0.50)
        self.assertAlmostEqual(s.aangepast_midden(bids, asks, 1), 0.51)

    def test_plan_rond_midden_op_tick_en_niet_door_het_boek(self):
        bids, asks = [(0.49, 100)], [(0.51, 100)]
        self.assertEqual(s.plan_orders(bids, asks, 0.50, 0.01, 0.001, 20, 0), (0.49, 0.51))
        # 3 cent bij een strak boek: gewoon verder weg
        self.assertEqual(s.plan_orders(bids, asks, 0.50, 0.03, 0.01, 20, 0), (0.47, 0.53))
        # breed boek: 1 cent van het midden kan binnen de spread liggen, maar nooit erdoorheen
        bids, asks = [(0.40, 100)], [(0.42, 100)]
        bod, laat = s.plan_orders(bids, asks, 0.41, 0.005, 0.01, 20, 0)
        self.assertLess(bod, 0.42)
        self.assertGreater(laat, 0.40)

    def test_voorraadrem(self):
        bids, asks = [(0.49, 100)], [(0.51, 100)]
        self.assertEqual(s.plan_orders(bids, asks, 0.50, 0.01, 0.01, 20, 40), (None, 0.51))
        self.assertEqual(s.plan_orders(bids, asks, 0.50, 0.01, 0.01, 20, -40), (0.49, None))

    def test_randen_van_het_boek(self):
        bids, asks = [(0.001, 100)], [(0.004, 100)]
        bod, laat = s.plan_orders(bids, asks, 0.0025, 0.01, 0.001, 20, 0)
        self.assertIsNone(bod)
        self.assertIsNotNone(laat)

    def test_onze_score_eenzijdig_buiten_10_90_is_nul(self):
        self.assertEqual(s.onze_score(None, 0.06, 0.05, 4.5, 20), 0.0)
        self.assertGreater(s.onze_score(0.04, 0.06, 0.05, 4.5, 20), 0.0)


class Vullingen(unittest.TestCase):
    def test_naar_ja(self):
        t = {"price": "0.3", "side": "BUY", "token_id": "nee"}
        p, kant = s.naar_ja(t, "ja")
        self.assertAlmostEqual(p, 0.7)
        self.assertEqual(kant, "SELL")
        self.assertEqual(s.naar_ja({"price": "0.3", "side": "BUY", "token_id": "ja"}, "ja"), (0.3, "BUY"))

    def test_vulling_los_en_streng(self):
        plan = (0.49, 0.51)
        self.assertEqual(s.vulling(0.49, "SELL", plan), ("bod", False))
        self.assertEqual(s.vulling(0.48, "SELL", plan), ("bod", True))
        self.assertIsNone(s.vulling(0.50, "SELL", plan))
        self.assertEqual(s.vulling(0.52, "BUY", plan), ("laat", True))
        self.assertIsNone(s.vulling(0.50, "BUY", plan))
        self.assertIsNone(s.vulling(0.40, "SELL", (None, 0.51)))

    def test_zoek_plan(self):
        plannen = {100: (6030.0, 0.49, 0.51, 0.5, 20), 101: (6100.0, 0.48, 0.50, 0.49, 20)}
        self.assertEqual(s.zoek_plan(plannen, 6050), 100)
        self.assertEqual(s.zoek_plan(plannen, 6090), 100)   # minuut 101, maar vóór het plan van 101
        self.assertEqual(s.zoek_plan(plannen, 6110), 101)
        self.assertIsNone(s.zoek_plan(plannen, 6020))       # vóór het eerste plan
        self.assertIsNone(s.zoek_plan(plannen, 6400))       # te lang na het laatste plan

    def test_stopregel_middernacht_lokaal(self):
        # Londen 21 nov: 00:00 lokaal = 00:00 UTC (wintertijd); Tokio: 15:00 UTC de dag ervoor
        self.assertEqual(s.dag_start_lokaal("highest-temperature-in-london-on-november-21-2026").isoformat(),
                         "2026-11-21T00:00:00+00:00")
        self.assertEqual(s.dag_start_lokaal("lowest-temperature-in-tokyo-on-november-21-2026").isoformat(),
                         "2026-11-20T15:00:00+00:00")
        self.assertIsNone(s.dag_start_lokaal("highest-temperature-in-atlantis-on-november-21-2026"))


class Rapport(unittest.TestCase):
    def test_rapport_op_kunstmatige_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            op = s.Opslag(tmp, "r1")
            op.van = 1795000000
            op.markten["abc"] = {"event": "highest-temperature-in-london-on-november-21-2026", "vakje": "10°C"}
            for i in range(120):
                ts = 1795000000 + 60 * i
                op.uur(ts, "abc", "1c", True, 0.01, 0.005, 0.5, 20.0)
                op.rijen["minuut"].append([ts, "1c", 1, 20.0, 0.01, 0.005])
            op.rijen["midden"] += [[1795000000, "abc", 0.50, 0.49, 0.51], [1795003000, "abc", 0.40, 0.39, 0.41]]
            # gekocht op 0,49; een uur later is het midden 0,40: verlies 20 x 0,09 = 1,80
            op.rijen["vullingen"].append([1795000100, "abc", "1c", "bod", 0.49, 20, 0.5, 1, 0.48, 50, 20])
            op.flush(1795000000 + 60 * 120, laatste=True)
            d = rapport.laad(tmp)
            tekst = rapport.maak(d, {"abc": 0.0}, 1.0, 90, [2000, 5000])
            self.assertIn("$-1.80", tekst)          # 1 uur later
            self.assertIn("$-9.80", tekst)          # tegen uitslag: 20 x (0 - 0,49)
            self.assertIn("$0.60 tot $1.20", tekst)  # beloning laag tot hoog over 120 minuten
            self.assertIn("€2,000", tekst)
            # voorraad: 20 x 0,49 vast, plus open orders van gemiddeld $20 = $29,80 nodig
            self.assertIn("**$29.80**", tekst)
            # weinig geld: per markt $20 orders plus rem 2 x 20 x 0,60 = $44 nodig, dus €100 = 2 markten,
            # beloning ondergrens 2 x 0,005 x 1440 = $14,40 per dag
            self.assertIn("| €100 | 2 | $14.40", tekst)
            self.assertIn("**Met €150: netto", tekst)

    def test_voorraadgeld_streept_ja_en_nee_weg_en_komt_vrij(self):
        d = {"markten": {"abc": {"stop": 1795000000}, "def": {"stop": 1795500000}}}
        vul = [
            {"variant": "1c", "markt": "abc", "ts": 1794990000, "kant": "bod", "prijs": "0.49", "aantal": "20"},
            {"variant": "1c", "markt": "def", "ts": 1794990100, "kant": "bod", "prijs": "0.30", "aantal": "10"},
            {"variant": "1c", "markt": "abc", "ts": 1794990200, "kant": "laat", "prijs": "0.51", "aantal": "10"},
        ]
        piek, _ts, _dag = rapport.voorraad_geld(d, vul, "1c")
        # na twee vullingen: 9,80 + 3,00 = 12,80; daarna 10 paren JA plus NEE weg: 4,90 + 3,00
        self.assertAlmostEqual(piek, 12.80)
        vul.append({"variant": "1c", "markt": "def", "ts": 1795200000, "kant": "bod", "prijs": "0.50", "aantal": "40"})
        piek, _ts, _dag = rapport.voorraad_geld(d, vul, "1c")
        # abc komt vrij 30 uur na zijn stop (1795108000), dus bij de laatste vulling staat alleen def: 3 + 20
        self.assertAlmostEqual(piek, 23.0)


if __name__ == "__main__":
    unittest.main()
