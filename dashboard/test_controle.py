"""Toetsen voor dashboard/controle.py en dashboard/oordeel.py. Draaien: python3 -m unittest dashboard/test_controle.py"""
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from controle import controleer  # noqa: E402
from oordeel import blame_tijden, nieuwste  # noqa: E402

GOED = {"bijgewerkt": {"datum": "2026-11-19 12:00", "door": "ronde"}, "projecten": [{
    "id": "proef", "naam": "Proef", "soort": "product", "voor": "Dortus",
    "status": {"woord": "live", "kleur": "op-koers", "zin": "Loopt."},
    "kans": {"laag": 10, "hoog": 20, "label": "GOK", "reden": "r", "bron": "b"},
    "prognose": {"verwacht": [50, 300], "label": "GOK", "reden": "r", "bron": "b"},
    "deadline": {"datum": "2026-11-27", "wat": "sale"},
    "thijs": [{"doen": "Iets", "voor": "2026-11-21"}, {"doen": "Nog iets"}]}]}


def met(**veranderd):
    d = json.loads(json.dumps(GOED))
    d["projecten"][0].update(veranderd)
    return json.dumps(d)


class Controle(unittest.TestCase):
    def test_echte_projecten_json_is_goed(self):
        pad = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "organisatie", "projecten.json")
        with open(pad, encoding="utf-8") as f:
            _, fouten = controleer(f.read())
        self.assertEqual(fouten, [])

    def test_goed_voorbeeld(self):
        data, fouten = controleer(json.dumps(GOED))
        self.assertEqual(fouten, [])
        self.assertEqual(len(data["projecten"][0]["thijs"]), 2)

    def test_geen_json_geeft_melding_en_lege_lijst(self):
        data, fouten = controleer('{"projecten": [ }')
        self.assertEqual(data["projecten"], [])
        self.assertIn("geen geldige JSON", fouten[0])

    def test_verwacht_als_tekst_wordt_weggelaten(self):
        data, fouten = controleer(met(prognose={"verwacht": "veel", "label": "GOK"}))
        self.assertIsNone(data["projecten"][0]["prognose"]["verwacht"])
        self.assertTrue(any("verwacht" in f for f in fouten))

    def test_thijs_oude_vorm_wordt_lijst(self):
        data, fouten = controleer(met(thijs={"doen": "Eén ding", "voor": "2026-11-23"}))
        self.assertEqual(fouten, [])
        self.assertEqual(data["projecten"][0]["thijs"], [{"doen": "Eén ding", "voor": "2026-11-23"}])

    def test_foute_datum_en_kleur(self):
        data, fouten = controleer(met(deadline={"datum": "27 nov"}, status={"woord": "x", "kleur": "paars"}))
        self.assertIsNone(data["projecten"][0]["deadline"])
        self.assertEqual(data["projecten"][0]["status"]["kleur"], "stil")
        self.assertEqual(len(fouten), 2)

    def test_dubbele_id(self):
        d = json.loads(json.dumps(GOED))
        d["projecten"].append(d["projecten"][0])
        data, fouten = controleer(json.dumps(d))
        self.assertEqual(len(data["projecten"]), 1)
        self.assertTrue(any("twee keer" in f for f in fouten))

    def test_kans_buiten_bereik(self):
        data, fouten = controleer(met(kans={"laag": 30, "hoog": 10, "label": "GOK"}))
        self.assertIsNone(data["projecten"][0]["kans"])
        self.assertTrue(fouten)


BOVEN = """# Herkeuring X fase 2a, do 19 nov 2026, keurder
Akkoord: ja (opgelost)
## Moet
# Keuring X fase 1, do 19 nov 2026, keurder
Akkoord: nee (twee moet-punten)
"""
ONDER = """# Keuring projectendashboard, 19 nov 2026, keurder
Akkoord: nee (drie moet-punten)
# Herkeuring, do 19 nov 2026 ±12:30, zelfde keurder
Akkoord: nee (één nieuw moet-punt)
# Herkeuring 2, do 19 nov 2026 ±13:40, zelfde keurder
Akkoord: ja
"""


class Oordeel(unittest.TestCase):
    def test_herkeuring_bovenaan_zonder_git(self):
        self.assertTrue(nieuwste(BOVEN)[0].startswith("Akkoord: ja"))

    def test_herkeuringen_onderaan_zonder_git(self):
        regel, kop = nieuwste(ONDER)
        self.assertEqual(regel, "Akkoord: ja")
        self.assertIn("13:40", kop)

    def test_git_blame_gaat_voor_de_plek(self):
        # regel 2 kwam later in git dan regel 5: dan telt regel 2, ook als de kop niets zegt
        tekst = "# Keuring A\nAkkoord: ja\n\n# Keuring B\nAkkoord: nee\n"
        self.assertEqual(nieuwste(tekst, {2: 2000, 5: 1000})[0], "Akkoord: ja")
        self.assertEqual(nieuwste(tekst, {2: 1000, 5: 2000})[0], "Akkoord: nee")

    def test_vet_akkoord_en_geen_akkoord(self):
        self.assertEqual(nieuwste("# K\n**Akkoord:** ja\n")[0], "**Akkoord:** ja")
        self.assertIsNone(nieuwste("# K\ngeen oordeel\n"))

    def test_blame_lezen(self):
        uit = ("a" * 40 + " 1 1 1\nauthor x\nauthor-time 1700000000\n\tregel\n"
               + "b" * 40 + " 3 2\nauthor y\nauthor-time 1800000000\n\tAkkoord: ja\n")
        self.assertEqual(blame_tijden(uit), {1: 1700000000, 2: 1800000000})


if __name__ == "__main__":
    unittest.main()
