"""Toets voor de herkomst per verkoop en TikTok in het scorebord (Meter, 23 nov 2026).

python3 organisatie/controle/scorebord_herkomst_test.py
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scorebord as sb  # noqa: E402
import scorebord_bronnen as b  # noqa: E402

VOORBEELD = {  # vorm uit de Gumroad API-docs, met verzonnen waarden
    "id": "X", "email": "iemand@voorbeeld.nl", "purchase_email": "iemand@voorbeeld.nl", "zip_code": "1234",
    "created_at": "2026-11-23T10:05:00Z", "product_name": "Click Joints Pro for Blender", "price": 1900,
    "currency": "usd", "referrer": "https://www.youtube.com/watch?v=abc&email=x@y.z", "utm_source": "yt",
    "utm_medium": "short", "utm_campaign": "", "license_key": "AAAA-BBBB", "purchaser_id": "55",
    "affiliate": {"email": "a@b.c", "amount": "$2"}, "offer_code": {"name": "CYBER25", "displayed_amount_off": "25%"},
    "chargedback": False, "refunded": False,
}


class Herkomst(unittest.TestCase):
    def test_geen_persoonsgegevens(self):
        r = b.verkoop_rij(VOORBEELD)
        tekst = " ".join(map(str, r.values()))
        for verboden in ("iemand", "@", "1234", "AAAA", "55", "email", "watch"):
            self.assertNotIn(verboden, tekst)
        self.assertEqual(set(r), set(b.VERKOOP_KOLOMMEN))

    def test_velden(self):
        r = b.verkoop_rij(VOORBEELD)
        self.assertEqual((r["datum"], r["bedrag"], r["bron"], r["kortingscode"], r["affiliate"]),
                         ("2026-11-23", "19.00", "youtube.com", "CYBER25", "ja"))

    def test_bron_zonder_adres(self):
        self.assertEqual(b.bron_van("Recommended by Gumroad"), "Recommended by Gumroad")
        self.assertEqual(b.bron_van("direct"), "direct")
        self.assertEqual(b.bron_van(None), "onbekend")
        self.assertEqual(b.bron_van("https://dortus.com/yt/?x=1"), "dortus.com")

    def test_soort_bron(self):
        self.assertEqual(sb.soort_bron({"kortingscode": "CJPgrant"}), "maker (CJPgrant)")
        self.assertEqual(sb.soort_bron({"kortingscode": "CYBER25"}), "code CYBER25")
        self.assertEqual(sb.soort_bron({"kortingscode": "", "utm_source": "tt", "bron": "x"}), "utm tt")
        self.assertEqual(sb.soort_bron({"kortingscode": "", "utm_source": "", "affiliate": "nee", "bron": "direct"}), "direct")

    def test_dag_rijen(self):
        rij = dict(b.verkoop_rij(VOORBEELD))
        uit = sb.dag_rijen("2026-11-23", [("Click Joints", "Blender", "downloads", 337, "")],
                           [("2026-11-22", "YouTube-adres", "bezoeken", 1)], [rij])
        self.assertEqual(len(uit), 3)
        self.assertEqual(uit[2]["bron"], "Gumroad Click Joints Pro for Blender via code CYBER25")
        self.assertTrue(all(r["gezien_bron"].startswith("GEZIEN") for r in uit))


class TikTok(unittest.TestCase):
    def test_adressen_uniek(self):
        t = "zie https://www.tiktok.com/@dortusstudio/video/7711044046633913632 en tiktok.com/@dortusstudio/video/7711044046633913632 en tiktok.com/@screencuts.co/video/7710270617886444833"
        self.assertEqual(b.tiktok_adressen([t]), [("dortusstudio", "7711044046633913632"), ("screencuts.co", "7710270617886444833")])

    def test_playcount(self):
        self.assertEqual(b.tiktok_cijfers('..."stats":{"diggCount":3,"playCount":289,...'), 289)
        self.assertIsNone(b.tiktok_cijfers('"playCount":'))


class Verwijzer(unittest.TestCase):
    def test_host(self):
        import scorebord_amami as a
        self.assertEqual(a.verwijzer_van(""), "direct")
        self.assertEqual(a.verwijzer_van(None), "direct")
        self.assertEqual(a.verwijzer_van("www.youtube.com"), "youtube.com")
        self.assertEqual(a.verwijzer_van("https://m.youtube.com/watch?v=x&email=a@b.c"), "youtube.com")
        self.assertEqual(a.verwijzer_van("l.instagram.com"), "instagram.com")
        self.assertEqual(a.verwijzer_van("https://iemand:geheim@reddit.com:443/r/blender"), "reddit.com")

    def test_lege_dag_telt_als_gemeten(self):
        import scorebord_amami as a
        self.assertEqual(a.verwijzer_rijen("2026-11-20", []), [("2026-11-20", "verwijzer geen", "bezoeken", 0)])
        self.assertEqual(a.verwijzer_rijen("d", [{"x": "www.youtube.com", "y": 2}, {"x": "youtube.com", "y": 1}]),
                         [("d", "verwijzer youtube.com", "bezoeken", 3)])

    def test_tabel(self):
        import scorebord_amami as a
        a.VANDAAG_TOT_NU.clear()
        a.VANDAAG_TOT_NU.update({("verwijzer direct", "bezoeken"): 4, ("dortus.com", "bezoekers"): 5, "tijd": "2026-11-24 tot 19:00"})
        alles = [{"datum": "2026-11-23", "product": "verwijzer youtube.com", "platform": "dortus.com", "maat": "bezoeken", "waarde": 2},
                 {"datum": "2026-11-23", "product": "verwijzer direct", "platform": "dortus.com", "maat": "bezoeken", "waarde": 9},
                 {"datum": "2026-11-23", "product": "dortus.com", "platform": "dortus.com", "maat": "bezoekers", "waarde": 12}]
        t = "\n".join(a.verwijzer_tabel(alles))
        self.assertIn("| 2026-11-23 | direct 9, youtube.com 2 |", t)
        self.assertIn("direct 4", t)
        a.VANDAAG_TOT_NU.clear()
        self.assertEqual(a.verwijzer_tabel([]), [])


if __name__ == "__main__":
    unittest.main()
