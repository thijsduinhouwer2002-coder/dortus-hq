#!/usr/bin/env python3
"""Tests van de repo-radar, zonder internet. Draaien: python3 -m unittest -v test_radar (in deze map)."""
import datetime as dt
import json
import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import radar  # noqa: E402
import rapport  # noqa: E402
import regels  # noqa: E402

GOEDE_README = """# InvoiceFox

Invoicing for freelancers who hate spreadsheets. Send an invoice in 30 seconds and get paid by card.

## The problem
Freelancers lose hours every month chasing payments and building invoices by hand in Word or Excel.

## Target audience
Freelancers and small agencies with fewer than ten clients.

## Pricing
Free tier with 3 invoices per month. Pro is $9/mo or $79/year. Lifetime deal: $149 one-time.

Join the waitlist at https://tally.so/r/abc and buy via https://buy.stripe.com/test_123.

```bash
npm install && npm run dev
```
"""


def repo(naam="iemand/invoicefox", **extra):
    r = {"full_name": naam, "html_url": "https://github.com/" + naam, "name": naam.split("/")[1],
         "description": "Simple invoicing SaaS for freelancers", "topics": ["saas", "invoicing"],
         "stargazers_count": 12, "forks_count": 2, "fork": False, "is_template": False, "archived": False,
         "created_at": "2026-11-18T10:00:00Z", "pushed_at": "2026-11-19T08:00:00Z", "homepage": "https://invoicefox.app",
         "language": "TypeScript", "default_branch": "main"}
    r.update(extra)
    return r


class TestPlan(unittest.TestCase):
    def test_goed_plan(self):
        p = regels.lees_plan(repo(), GOEDE_README)
        self.assertIn("abonnement", p["verdienmodel"])
        self.assertEqual(p["prijs"][:2], ["$9/maand", "$79/jaar"])
        self.assertIn("web", p["platform"])
        self.assertIn("freelancers", p["voor_wie"])
        self.assertEqual(p["betaallinks"], ["Stripe"])
        self.assertTrue(p["wachtlijst"])
        self.assertTrue(p["prijskop"])
        self.assertGreaterEqual(p["plankoppen"], 2)
        self.assertTrue(p["site"])
        self.assertIsNone(regels.ruis_op_readme(p, GOEDE_README))
        s, uitleg = regels.score(p)
        self.assertEqual(s, 10)
        self.assertIn("prijs +2", uitleg)

    def test_prijzen(self):
        self.assertEqual(regels.prijzen("$0.01056/sec, $0.0085 per image, $0.50"), [])
        self.assertEqual(regels.prijzen("Pro $9/mo, $19 lifetime, 12 EUR per year"), ["$9/maand", "$19 eenmalig", "€12/jaar"])
        self.assertEqual(regels.prijzen("$9 and $9 again and €4,99"), ["$9", "€4,99"])
        self.assertEqual(regels.prijzen("geen prijs hier, versie 1.2.3"), [])

    def test_platform_alleen_uit_begin(self):
        # Blender diep in een lijst met koppelingen maakt het geen Blender-project
        readme = "# Tool\n\nA tool for teams to track work with a subscription.\n\n" + ("filler text. " * 400) + "\nWorks with Blender add-on users."
        p = regels.lees_plan(repo(description="Track work", topics=[]), readme)
        self.assertNotIn("Blender", p["platform"])
        p2 = regels.lees_plan(repo(description="A Blender add-on for rigging, Pro version $12", topics=[]), readme)
        self.assertIn("Blender", p2["platform"])

    def test_gumroad_als_kassa(self):
        p = regels.lees_plan(repo(description="Chrome extension for tabs, buy on Gumroad", topics=[]), GOEDE_README)
        self.assertEqual(p["platform"][0], "Chrome")
        self.assertIn("browserextensie", rapport.soort(p))
        p2 = regels.lees_plan(repo(description="Windows writing app. Buy on Gumroad", topics=[], homepage=""), "x " * 300)
        self.assertIn("verkocht via Gumroad", rapport.soort(p2))

    def test_lege_readme_en_geen_readme(self):
        p = regels.lees_plan(repo(), "# Hoi")
        self.assertEqual(regels.ruis_op_readme(p, "# Hoi"), "lege README")
        self.assertEqual(regels.ruis_op_readme(regels.lees_plan(repo(), None), None), "geen README")

    def test_alleen_code(self):
        readme = "# x\n\n```\n" + "const a = 1;\n" * 80 + "```\n\nRun it with node and see the output now please.\n"
        p = regels.lees_plan(repo(description="x"), readme)
        self.assertEqual(regels.ruis_op_readme(p, readme), "alleen code, geen uitleg")

    def test_geen_verdienplan(self):
        readme = "# Weather\n\n" + "This shows the weather in your city with nice charts and maps for everyone. " * 5
        p = regels.lees_plan(repo(description="Weather viewer", topics=[]), readme)
        self.assertEqual(regels.ruis_op_readme(p, readme), "geen verdienplan in de tekst")

    def test_huiswerk_en_sjabloon_in_readme(self):
        tekst = "# Shop\n\nThis is my final assignment for the web course, with pricing $10 per month for fake users. " * 3
        p = regels.lees_plan(repo(), tekst)
        self.assertEqual(regels.ruis_op_readme(p, tekst), "huiswerk of oefening")
        tekst2 = "# Kit\n\nUse this template to launch your SaaS fast with Stripe subscriptions and pricing pages. " * 3
        self.assertEqual(regels.ruis_op_readme(regels.lees_plan(repo(), tekst2), tekst2), "sjabloon of boilerplate")

    def test_schoon_haalt_persoonsgegevens_weg(self):
        t = regels.schoon("Contact jan.jansen@example.com or +1 555 0100 2000 \u2014 see https://x.y/z [site](https://a.b)")
        self.assertNotIn("@", t)
        self.assertNotIn("0100", t)
        self.assertNotIn("http", t)
        self.assertNotIn("\u2014", t)
        self.assertLessEqual(len(regels.schoon("woord " * 100)), 160)


class TestRuisOpNaam(unittest.TestCase):
    def test_redenen(self):
        self.assertEqual(regels.ruis_op_naam(repo(fork=True)), "fork")
        self.assertEqual(regels.ruis_op_naam(repo(is_template=True)), "sjabloon of boilerplate")
        self.assertEqual(regels.ruis_op_naam(repo(archived=True)), "gearchiveerd")
        self.assertEqual(regels.ruis_op_naam(repo("a/nextjs-saas-starter-kit", description="")), "sjabloon of boilerplate")
        self.assertEqual(regels.ruis_op_naam(repo("a/airbnb-clone", description="")), "huiswerk of oefening")
        self.assertEqual(regels.ruis_op_naam(repo("a/x", description="Solana memecoin sniper bot")), "crypto-pump")
        self.assertEqual(regels.ruis_op_naam(repo("a/awesome-saas", description="")), "lijst, geen product")
        self.assertEqual(regels.ruis_op_naam(repo("a/plugin", description="Colorful icons 9999.1 (patched build)")), "spam of illegaal")
        self.assertIsNone(regels.ruis_op_naam(repo()))
        # gewone woorden die op ruis lijken maar het niet zijn
        self.assertIsNone(regels.ruis_op_naam(repo("a/coursebox", description="Sell online courses with a subscription")))
        self.assertIsNone(regels.ruis_op_naam(repo("a/fit", description="AI fitness trainer app with pro plan")))
        self.assertIsNone(regels.ruis_op_naam(repo("a/notes", description="Git cheat sheet with pro version")))

    def test_spamnetwerk(self):
        tekst = "AI API gateway relay 307 models behind one OpenAI compatible key"
        repos = [repo(f"apimart{i}x/guide{i}", description=tekst) for i in range(3)]
        repos += [repo(f"apimartq{i}/other{i}", description=f"iets anders nummer {i} met een eigen beschrijving") for i in range(3)]
        repos += [repo("eerlijk/app"), repo("ander/app", description="Simple invoicing SaaS for freelancers")]
        staart = ": model id, pricing, parameters and copy-paste examples for the OpenAI-compatible APIMart endpoint."
        repos += [repo(f"willekeurig{i}q/m{i}", description=f"Model {chr(65 + i)}{i * 7} Turbo API" + staart) for i in range(4)]
        spam = regels.spamnetwerk(repos)
        self.assertIn("apimart0x/guide0", spam)      # zelfde tekst bij 3 eigenaren
        self.assertIn("apimartq1/other1", spam)      # 6 eigenaren die met apimart beginnen
        self.assertNotIn("eerlijk/app", spam)        # zelfde tekst bij maar 2 eigenaren
        self.assertNotIn("ander/app", spam)
        self.assertIn("willekeurig2q/m2", spam)      # zelfde eind van de tekst bij 4 eigenaren


class TestRapport(unittest.TestCase):
    def data(self):
        plannen = []
        for i in range(30):
            p = regels.lees_plan(repo(f"o{i}/r{i}"), GOEDE_README)
            p["score"], p["waarom_score"] = 10 - i // 5, ""
            p["zoektermen"] = ["saas"]
            p["eerder_gemeld"] = "2026-11-18" if i == 0 else None
            plannen.append(p)
        return {"datum": "2026-11-19", "gemaakt": "2026-11-19T06:00Z", "zoekvragen": 48, "zoekvragen_mislukt": 0,
                "gevonden": 100, "gelezen": 60, "niet_gelezen": 10, "plannen": plannen,
                "ruis": [{"naam": "a/b", "link": "", "reden": "lege README", "fase": "readme"}]}

    def test_top_25_zonder_eerder_gemeld(self):
        d = self.data()
        t = rapport.top(d)
        self.assertEqual(len(t), 25)
        self.assertNotIn("o0/r0", [p["naam"] for p in t])
        tekst = rapport.maak(d)
        self.assertIn("## Top 25", tekst)
        self.assertIn("1. **10** [o1/r1](https://github.com/o1/r1): web-app voor freelancers", tekst)
        self.assertIn("Prijs: $9/maand", tekst)
        self.assertIn("- lege README: 1", tekst)
        self.assertIn("waarvan 1 al eerder in de top", tekst)
        self.assertNotIn("\u2014", tekst)

    def test_hooguit_twee_per_maker(self):
        d = self.data()
        for p in d["plannen"][:5]:
            p["naam"] = "zelfde/" + p["naam"].split("/")[1]
        namen = [p["naam"] for p in rapport.top(d)]
        self.assertEqual(sum(n.startswith("zelfde/") for n in namen), 2)
        self.assertEqual(len(namen), 25)

    def test_leeg(self):
        d = self.data()
        d["plannen"] = []
        self.assertIn("Vandaag niets met een plan gevonden.", rapport.maak(d))


class TestRun(unittest.TestCase):
    """De hele run met nep-antwoorden van GitHub: zoekvragen, ruis, README, score, bestanden, gezien.json."""

    def test_run(self):
        goed = repo("maker/invoicefox")
        fork = repo("maker/kopie", fork=True)
        leeg = repo("maker/leeg", description="Startup idea")
        readmes = {"maker/invoicefox": GOEDE_README, "maker/leeg": None}
        vragen = []

        def nep_zoek(q, sort=None):
            vragen.append(q)
            return [goed, fork, leeg], 3

        with tempfile.TemporaryDirectory() as d, \
                mock.patch.object(radar, "zoek", nep_zoek), \
                mock.patch.object(radar, "lees_readme", lambda r: readmes[r["full_name"]]), \
                mock.patch.object(radar, "WACHT_ZOEK", 0):
            gezien = os.path.join(d, "gezien.json")
            with open(gezien, "w") as f:
                json.dump({"oud/repo": "2026-11-01"}, f)
            data = radar.run(os.path.join(d, "uit"), gezien, vandaag=dt.date(2026, 11, 19), log=lambda s: None)
            self.assertEqual(len(vragen), 2 * len(regels.ZOEKTERMEN))
            self.assertTrue(all("created:" in q for q in vragen))
            self.assertIn("created:>=2026-11-17", vragen[0])
            self.assertEqual([p["naam"] for p in data["plannen"]], ["maker/invoicefox"])
            redenen = {r["naam"]: r["reden"] for r in data["ruis"]}
            self.assertEqual(redenen, {"maker/kopie": "fork", "maker/leeg": "geen README"})
            self.assertTrue(os.path.exists(os.path.join(d, "uit", "rapport.md")))
            with open(os.path.join(d, "uit", "kandidaten.json")) as f:
                opgeslagen = json.load(f)
            self.assertNotIn("owner", json.dumps(opgeslagen))  # geen eigenaargegevens, alleen naam en link
            with open(gezien) as f:
                g = json.load(f)
            self.assertEqual(g, {"oud/repo": "2026-11-01", "maker/invoicefox": "2026-11-19"})
            # dezelfde dag opnieuw: blijft in de top (niet "eerder gemeld")
            data2 = radar.run(os.path.join(d, "uit"), gezien, vandaag=dt.date(2026, 11, 19), log=lambda s: None)
            self.assertIsNone(data2["plannen"][0]["eerder_gemeld"])
            # een dag later: wel eerder gemeld, dus niet meer in de top
            data3 = radar.run(os.path.join(d, "uit"), gezien, vandaag=dt.date(2026, 11, 20), log=lambda s: None)
            self.assertEqual(data3["plannen"][0]["eerder_gemeld"], "2026-11-19")
            self.assertEqual(rapport.top(data3), [])

    def test_kapotte_gezien(self):
        with tempfile.TemporaryDirectory() as d, \
                mock.patch.object(radar, "zoek", lambda q, sort=None: ([], 0)), \
                mock.patch.object(radar, "WACHT_ZOEK", 0):
            gezien = os.path.join(d, "gezien.json")
            with open(gezien, "w") as f:
                f.write("{kapot")
            data = radar.run(os.path.join(d, "uit"), gezien, vandaag=dt.date(2026, 11, 19), log=lambda s: None)
            self.assertEqual(data["plannen"], [])


if __name__ == "__main__":
    unittest.main()
