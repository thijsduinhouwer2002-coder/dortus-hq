"""Toets voor de kortingscodes in het scorebord (Bram, 24 nov 2026).

python3 organisatie/controle/scorebord_codes_test.py
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scorebord as sb  # noqa: E402
import scorebord_bronnen as b  # noqa: E402

# vorm uit de Gumroad API-docs (GET /v2/products/:id/offer_codes), met verzonnen waarden
ANTWOORD = {"success": True, "offer_codes": [
    {"id": "c1", "name": "CYBER25", "percent_off": 25, "max_purchase_count": None, "universal": False, "times_used": 3},
    {"id": "c2", "name": "VRIENDGRATIS", "percent_off": 100, "max_purchase_count": 5, "universal": False, "times_used": 1},
    {"id": "c3", "name": "TIENKORT", "amount_cents": 1000, "universal": True, "times_used": 0},
]}


class Codes(unittest.TestCase):
    def setUp(self):
        self.oud_get, self.oud_env = b._get, os.environ.get("GUMROAD_ACCESS_TOKEN")
        os.environ["GUMROAD_ACCESS_TOKEN"] = "x"
        self.adressen = []

        def nep(url, koppen=None, **_):
            self.adressen.append(url)
            return ANTWOORD, None
        b._get = nep
        b.GUMROAD_PRODUCTEN[:] = [("p1", "Click Joints Pro"), ("p2", "Spiekbrief")]

    def tearDown(self):
        b._get = self.oud_get
        b.GUMROAD_PRODUCTEN[:] = []
        if self.oud_env is None:
            os.environ.pop("GUMROAD_ACCESS_TOKEN", None)
        else:
            os.environ["GUMROAD_ACCESS_TOKEN"] = self.oud_env

    def test_rijen(self):
        noten = []
        r = b.gumroad_codes(noten)
        self.assertEqual(noten, [])
        self.assertIn("https://api.gumroad.com/v2/products/p1/offer_codes", self.adressen)
        cyber = [x for x in r if x["code"] == "CYBER25"]
        self.assertEqual(len(cyber), 2)  # per product
        self.assertEqual((cyber[0]["korting"], cyber[0]["gebruikt"], cyber[0]["max"]), ("25%", 3, "geen"))
        # universele code maar één keer
        self.assertEqual(len([x for x in r if x["code"] == "TIENKORT"]), 1)
        self.assertEqual([x["korting"] for x in r if x["code"] == "TIENKORT"], ["$10.00"])

    def test_gratis_code_niet_voluit(self):
        tekst = " ".join(" ".join(map(str, x.values())) for x in b.gumroad_codes([]))
        self.assertNotIn("VRIENDGRATIS", tekst)
        self.assertIn("VR…", tekst)

    def test_tabel(self):
        t = "\n".join(sb.codes_tabel(b.gumroad_codes([])))
        self.assertIn("## Kortingscodes Gumroad", t)
        self.assertIn("| Click Joints Pro | CYBER25 | 25% | 3 | geen | nee |", t)
        self.assertIn("Niet gemeten", "\n".join(sb.codes_tabel(None)))

    def test_zonder_sleutel(self):
        os.environ.pop("GUMROAD_ACCESS_TOKEN")
        noten = []
        self.assertIsNone(b.gumroad_codes(noten))
        self.assertTrue(noten)


if __name__ == "__main__":
    unittest.main()
