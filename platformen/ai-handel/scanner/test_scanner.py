"""Tests voor de rekensom van de scanner en het rapport. Draaien: python3 -m unittest test_scanner (in deze map)."""
import json
import os
import tempfile
import unittest

import rapport
import scanner
import simrapport
import simulatie


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

    def test_kraken_tarief(self):
        import beurzen
        self.assertEqual(beurzen.taker_standaard("kraken", "SSV", "EUR"), 0.008)    # GEZIEN kraken.com/pro/fees
        self.assertEqual(beurzen.taker_standaard("kraken", "USDT", "EUR"), 0.002)   # stablecoin en FX
        self.assertEqual(beurzen.taker_standaard("bitvavo", "SSV", "EUR"), 0.0025)
        self.assertEqual(scanner.taker({}, "kraken", ("SSV", "EUR")), 0.008)

    def test_herreken_oud_kraken_tarief(self):
        r = rapport.herreken(self.regel(koop="kraken", taker_koop=0.004, taker_verkoop=0.001))
        self.assertTrue(r["herrekend"])
        self.assertAlmostEqual(r["taker_koop"], 0.008)
        self.assertAlmostEqual(r["winst100_med"], 1 - 0.4)                          # 0,4% van €100 extra
        self.assertAlmostEqual(r["winst_ruimte_med"], 5 - 1.6)                      # 0,4% van €400 extra
        self.assertAlmostEqual(r["winst500_med"], r["winst_ruimte_med"])            # boven de ruimte gelijk
        r = rapport.herreken(self.regel(verkoop="kraken", taker_verkoop=0.004, ruimte_eur_med=2000,
                                        winst100_med=0.5, winst500_med=1.5, winst1000_med=2.0,
                                        winst2500_med=2.2, winst_ruimte_med=2.2))
        self.assertEqual(r["ruimte_eur_med"], 100)                                  # ruimte krimpt
        self.assertAlmostEqual(r["winst_ruimte_med"], 0.1)
        self.assertAlmostEqual(r["winst1000_med"], 0.1)
        weg = rapport.herreken(self.regel(koop="kraken", taker_koop=0.004, winst100_med=0.3, winst500_med=1.2,
                                          winst1000_med=1.2, winst2500_med=1.2, winst_ruimte_med=1.2))
        self.assertFalse(rapport.echt(weg))                                         # geen winst meer: valt af
        nieuw = self.regel(koop="kraken", taker_koop=0.008)
        self.assertIs(rapport.herreken(nieuw), nieuw)                               # al met 0,80%: niets
        gewoon = self.regel()
        self.assertIs(rapport.herreken(gewoon), gewoon)                             # andere beurzen: niets

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


class TestSimulatie(unittest.TestCase):
    """Voorraad-simulatie op kunstmatige kansen (geen netwerk)."""

    def kans(self, minuut, **kw):
        r = {"munt": "X", "quote": "EUR", "koop": "a", "verkoop": "b", "eur_per_quote": 1.0,
             "begin": f"2026-11-19T10:{minuut:02d}:00Z", "eind": f"2026-11-19T10:{minuut + 3:02d}:00Z",
             "ruimte_eur_med": 1000, "winst100_med": 0.5, "winst500_med": 4.5, "winst1000_med": 9.5,
             "winst2500_med": 9.5, "winst_ruimte_med": 9.5, "opname_eur": 0.5}
        r.update(kw)
        return r

    def test_bruto_lineair_en_nooit_meer_dan_de_ruimte(self):
        r = self.kans(0, ruimte_eur_med=400, winst100_med=1, winst500_med=4, winst_ruimte_med=5)
        self.assertAlmostEqual(simulatie.bruto_bij(r, 100), 1.5)      # opnamekosten tellen niet per kans
        self.assertAlmostEqual(simulatie.bruto_bij(r, 250), 3.5)
        self.assertAlmostEqual(simulatie.bruto_bij(r, 1000), 5.5)     # niet meer dan de ruimte op het boek
        self.assertEqual(simulatie.bruto_bij(r, 0), 0)

    def test_voorraad_beperkt_en_terugschuiven(self):
        # inleg 2000: per beurs 500 euro en 500 euro aan munten. Kans 1 kan maar 500 (geld op a en munt op b op).
        # Daarna gaat de munt van a naar b (30 min) en het geld van b naar a (EUR: 1 dag, GOK): kans 2 en 3 gemist.
        ks = [self.kans(0), self.kans(10), self.kans(20)]
        s = simulatie.Sim(ks, 2000, ("a", "b")).draai()
        d = s.dagen()["2026-11-19"]
        self.assertEqual((d["kansen"], d["gemist"], d["beperkt"]), (3, 2, 1))
        self.assertAlmostEqual(d["bruto"], 5.0)                       # 4,5 + 0,5 opname terug
        self.assertEqual(d["schuif"], 2)
        self.assertAlmostEqual(d["kosten"], 0.5 + 1.0)                # munt (gemeten) en euro (GOK 1 EUR)
        self.assertAlmostEqual(s.waarde() - 2000, d["netto"], places=6)

    def test_munt_aangekomen_kans_weer_mogelijk(self):
        # Munt is na 30 minuten op b; met genoeg geld op a (USDT, 30 min) gaat kans 2 weer door.
        ks = [self.kans(0, quote="USDT"), self.kans(45, quote="USDT", eind="2026-11-19T10:50:00Z")]
        d = simulatie.Sim(ks, 2000, ("a", "b")).draai().dagen()["2026-11-19"]
        self.assertEqual(d["gemist"], 0)
        self.assertGreater(d["bruto"], 5.0)

    def test_niet_schuiven_als_kosten_te_hoog(self):
        ks = [self.kans(0, opname_eur=100.0, winst500_med=-95.5, winst100_med=-99.5, winst1000_med=-90.5,
                        winst2500_med=-90.5, winst_ruimte_med=-90.5)]
        s = simulatie.Sim(ks, 2000, ("a", "b")).draai()
        self.assertFalse(any(x[1] == "X" for x in s.schuif_log))     # 100 euro kosten op 500: niet schuiven

    def test_kostengrens_instelbaar(self):
        ks = [self.kans(0, opname_eur=10.0)]                          # 10 euro kosten op een schuif van 500: 2%
        s = simulatie.Sim(ks, 2000, ("a", "b")).draai()
        self.assertFalse(any(x[1] == "X" for x in s.schuif_log))     # standaard 1%: niet schuiven
        self.assertTrue(s.scheef())                                   # munt op b blijft leeg
        s = simulatie.Sim(ks, 2000, ("a", "b"), max_kosten=0.05).draai()
        self.assertTrue(any(x[1] == "X" for x in s.schuif_log))      # grens 5%: wel schuiven

    def test_koerseffect_apart_en_netto_klopt(self):
        t_mid = simulatie.ts("2026-11-19T10:05:00Z")
        koers = lambda munt, t: 1.0 if t < t_mid else 2.0             # munt verdubbelt om 10:05
        ks = [self.kans(0), self.kans(10)]
        s = simulatie.Sim(ks, 2000, ("a", "b"), koers).draai()
        d = s.dagen()["2026-11-19"]
        self.assertAlmostEqual(d["koers"], 1000 - 0.5, places=6)      # alle munten (1000, min opname) x2
        self.assertAlmostEqual(d["netto"], d["bruto"] - d["kosten"] + d["koers"])
        self.assertAlmostEqual(s.waarde() - 2000, d["netto"], places=6)
        self.assertTrue(s.koers_bekend)

    def test_koersen_uit_candles(self):
        def haal(beurs, munt, quote, van, tot):
            if beurs == "kraken":
                raise OSError("geen verbinding")
            return [(200, 3.0), (100, 2.0)]
        k = simulatie.Koersen({"X": ("EUR", ["kraken", "bitvavo"]), "Y": ("EUR", ["kraken"])}, 0, 300, haal)
        self.assertEqual(k("X", 250), 2.0)                            # candle 200 sluit pas om 300
        self.assertEqual(k("X", 300), 3.0)
        self.assertIsNone(k("Y", 150))                                # onbekend, niet 0

    def test_minimale_order_en_opname(self):
        # minimale order 600 euro op beurs a: een kans van 500 telt als gemist; opnameminimum hoogt een schuif op
        mi = lambda beurs, munt, quote: {"order_q": 600.0 if beurs == "a" else 5.0, "order_m": None, "opname_m": None}
        d = simulatie.Sim([self.kans(0)], 2000, ("a", "b"), minima=mi).draai().dagen()["2026-11-19"]
        self.assertEqual((d["gemist"], d["bruto"]), (1, 0))
        mi2 = lambda beurs, munt, quote: {"order_q": 5.0, "order_m": None, "opname_m": 1200.0}
        s = simulatie.Sim([self.kans(0)], 2000, ("a", "b"), lambda m, t: 1.0, minima=mi2).draai()
        self.assertFalse(any(x[1] == "X" for x in s.schuif_log))     # minimum 1200, er staan er maar 1000 op a
        mi3 = lambda beurs, munt, quote: {"order_q": 5.0, "order_m": None, "opname_m": 300.0}
        s = simulatie.Sim([self.kans(0)], 2000, ("a", "b"), lambda m, t: 1.0, minima=mi3).draai()
        self.assertAlmostEqual(next(x[4] for x in s.schuif_log if x[1] == "X"), 500)   # helft verschil >= 300
        mi4 = lambda beurs, munt, quote: {"order_q": 5.0, "order_m": None, "opname_m": 700.0}
        s = simulatie.Sim([self.kans(0)], 2000, ("a", "b"), lambda m, t: 1.0, minima=mi4).draai()
        self.assertAlmostEqual(next(x[4] for x in s.schuif_log if x[1] == "X"), 700)   # opgehoogd tot het minimum

    def test_heropende_kans_krijgt_niet_opnieuw_het_volle_boek(self):
        a = self.kans(0, quote="USDT", ruimte_eur_med=300, winst100_med=None, winst500_med=None,
                      winst_ruimte_med=2.5, opname_eur=0.5)
        b = dict(a, begin="2026-11-19T10:05:00Z", eind="2026-11-19T10:09:00Z")   # 2 min na het eind van a
        d = simulatie.Sim([a, b], 5000, ("a", "b")).draai().dagen()["2026-11-19"]
        self.assertAlmostEqual(d["ingezet"], 300)                     # samen niet meer dan één boek
        self.assertEqual(d["gemist"], 1)

    def test_handel_los_van_koerseffect(self):
        koers = lambda munt, t: 1.0 if t < simulatie.ts("2026-11-19T10:05:00Z") else 2.0
        d = simulatie.Sim([self.kans(0)], 2000, ("a", "b"), koers).draai().dagen()["2026-11-19"]
        self.assertAlmostEqual(d["handel"], d["bruto"] - d["kosten"])
        self.assertAlmostEqual(d["netto"], d["handel"] + d["koers"])
        ks = [self.kans(0, koop="bitvavo", verkoop="kraken")]
        tekst = "\n".join(simrapport.blok(ks, [], rapport.MICA))
        self.assertIn("Netto handel", tekst)
        self.assertNotIn("%' if", tekst)
        rij = next(x for x in tekst.split("\n") if x.startswith("| bitvavo - kraken | €150,00"))
        self.assertTrue(rij.rstrip(" |").endswith("onbekend*"))      # rendement met onbekende koers: geen getal
        self.assertIn("**Met €150: netto", tekst)
        self.assertIn("schuifdrempel 40%", tekst)
        self.assertIn("| kostengrens 5% (achteraf vergeleken) | €150,00 |", tekst)
        self.assertIn("| kostengrens 2% (achteraf vergeleken) | €2.000,00 |", tekst)
        self.assertIn("\"Per dag\" is hier één gemeten dag die begint met een gelijk verdeelde voorraad", tekst)

    def test_blok_in_rapport(self):
        ks = [self.kans(0, koop="bitvavo", verkoop="kraken"), self.kans(10, koop="mexc", verkoop="kraken")]
        tekst = "\n".join(simrapport.blok(ks, [], rapport.MICA))
        self.assertIn("| bitvavo - kraken | €2.000,00 | 2026-11-19 |", tekst)
        self.assertIn("| kraken - mexc | €5.000,00 |", tekst)
        self.assertIn("onbekend", tekst)                              # zonder koersen: koerseffect onbekend
        self.assertIn("**Aannames:**", tekst)


if __name__ == "__main__":
    unittest.main()
