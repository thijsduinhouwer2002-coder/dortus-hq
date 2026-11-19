"""Toetsen voor dashboard/controle.py. Draaien: python3 -m unittest dashboard/test_controle.py"""
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from controle import controleer  # noqa: E402

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


if __name__ == "__main__":
    unittest.main()
