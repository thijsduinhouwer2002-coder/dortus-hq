import os, sys, unittest
sys.path.insert(0, os.path.dirname(__file__))
import blindtest as b


class Test(unittest.TestCase):
    def test_lees_antwoord(self):
        d = b.lees_antwoord('```json\n{"ranking":["c","A","D","B"],"reasons":{}}\n```')
        self.assertEqual(d["ranking"], ["C", "A", "D", "B"])

    def test_ongeldig(self):
        with self.assertRaises(ValueError):
            b.lees_antwoord('{"ranking":["A","A","B","C"]}')

    def test_plek(self):
        self.assertEqual(b.plek_van(["C", "A", "D", "B"], "A"), 2)

    def test_volgorde_vast_per_zaad_en_anders_per_ronde(self):
        items = [{"naam": n} for n in "wxyz"]
        self.assertEqual(b.volgorde(items, "s|0"), b.volgorde(items, "s|0"))
        rondes = {tuple(i["naam"] for i in b.volgorde(items, f"s|{r}")) for r in range(6)}
        self.assertGreater(len(rondes), 1)

    def test_zonder_sleutels_niets(self):
        for k in ("GEMINI_API_KEY", "OPENAI_API_KEY"):
            os.environ.pop(k, None)
        self.assertEqual(b.main(os.path.join(os.path.dirname(__file__), "sets", "click-joints-pro-superhive.json"), "/tmp/x.md"), 0)


if __name__ == "__main__":
    unittest.main()
