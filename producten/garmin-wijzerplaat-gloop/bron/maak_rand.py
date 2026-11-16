"""Maakt source/Rand.mc: hoeveel hoeden op een rond scherm heel in beeld passen.

Moet van Daan (16 nov ±16:35 UTC): de bovenste hoed blijft minstens 4 px binnen de cirkel; een hoed
die dat niet haalt wordt niet getekend, zodat er nooit een hoed tegen de ronde rand kapot gaat.
Het script legt de echte hoedenplaatjes uit de kit van Mila (ontwerp/garmin/gloop-spel/kit/<maat>/)
op de plekken uit Maten.mc en Plek.mc en kijkt per pixel of hij binnen de cirkel valt.

Gebruik, vanuit producten/garmin-wijzerplaat-gloop:  python3 -I bron/maak_rand.py
"""
import os
import re
import sys

from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
PRODUCT = os.path.dirname(HIER)
KIT = os.path.join(PRODUCT, "..", "..", "ontwerp", "garmin", "gloop-spel", "kit")
MARGE = 4
HOED_STAP = 0.46
VOLGORDE = [0, 1, 2, 3, 5, 6, 7, 8, 9]
KROON = 4
NAMEN = ["00-helm", "01-puntmuts", "02-kap", "03-pet", "04-kroon", "05-koksmuts", "06-emmer",
         "07-hoge_hoed", "08-pan", "09-veermuts"]
# Drempel in Maten.mc en Plek.mc, map in de kit, en de ronde schermbreedtes die in dat vak vallen.
VAKKEN = [(454, "454", [454]), (416, "416", [416]), (390, "390", [390]), (280, "280-mip", [280]),
          (260, "260-mip", [260]), (240, "240-mip", [240]), (0, "208-mip", [208, 218])]
GEEN_GRENS = 99


def tabel(bestand):
    tekst = open(os.path.join(PRODUCT, "source", bestand), encoding="utf-8").read()
    uit = {}
    for m in re.finditer(r"breedte >= (\d+)\) \{\s*return \[([^\]]+)\]", tekst):
        uit[int(m.group(1))] = [int(x) for x in m.group(2).split(",")]
    uit[0] = [int(x) for x in re.findall(r"return \[([^\]]+)\]", tekst)[-1].split(",")]
    return uit


def past(plaatje, x0, y0, w):
    """Ligt elke zichtbare pixel van het plaatje minstens MARGE px binnen de cirkel van w breed?"""
    r = w / 2.0
    rr = (r - MARGE) ** 2
    alfa = plaatje.getchannel("A")
    px = alfa.load()
    for y in range(alfa.height):
        for x in range(alfa.width):
            if px[x, y] >= 32:
                dx = x0 + x + 0.5 - r
                dy = y0 + y + 0.5 - r
                if dx * dx + dy * dy > rr:
                    return False
    return True


def reken(w, m, p, hoeden):
    """Geeft (gewoon, kroon): gewone hoeden 0 tot gewoon-1 passen; de kroon past op plek 0 tot kroon."""
    voet_x = p[0] - m[0] // 2 + m[10]
    y = p[1] - m[1] + m[11]
    gewoon = 0
    kroon = -1
    for i in range(60):
        x = voet_x + p[13 + (i if i < 24 else 23)]
        kb, kh = m[12 + 2 * KROON], m[13 + 2 * KROON]
        if kroon == i - 1 and past(hoeden[KROON], x - kb // 2, y - kh, w):
            kroon = i
        k = VOLGORDE[i % 9]
        hb, hh = m[12 + 2 * k], m[13 + 2 * k]
        if not past(hoeden[k], x - hb // 2, y - hh, w):
            break
        gewoon = i + 1
        y -= int(hh * HOED_STAP + 0.5)
    return gewoon, kroon


def main():
    maten = tabel("Maten.mc")
    plek = tabel("Plek.mc")
    regels = []
    for drempel, kitmap, breedtes in VAKKEN:
        m, p = maten[drempel], plek[drempel]
        hoeden = []
        for k, naam in enumerate(NAMEN):
            plaatje = Image.open(os.path.join(KIT, kitmap, "hoed-" + naam + ".png")).convert("RGBA")
            if plaatje.size != (m[12 + 2 * k], m[13 + 2 * k]):
                sys.exit("maat van hoed %d in %s klopt niet met Maten.mc: %s" % (k, kitmap, plaatje.size))
            hoeden.append(plaatje)
        uitkomsten = [reken(w, m, p, hoeden) for w in breedtes]
        gewoon = min(u[0] for u in uitkomsten)
        kroon = min(u[1] for u in uitkomsten)
        print("vak %3d (kit %s, schermen %s): gewone hoeden %d, kroon tot plek %d" % (drempel, kitmap, breedtes, gewoon, kroon))
        regels.append((drempel, gewoon, kroon))

    def functie(naam, kolom, uitleg):
        s = "    // " + uitleg + "\n    function " + naam + "(breedte as Number) as Number {\n"
        for r in regels:
            if r[0] > 0:
                s += "        if (breedte >= %d) {\n            return %d;\n        }\n" % (r[0], r[kolom])
        s += "        return %d;\n    }\n" % regels[-1][kolom]
        return s

    uit = ("import Toybox.Lang;\n\n"
           "// GEMAAKT DOOR bron/maak_rand.py uit de hoedenplaatjes van de kit, Maten.mc en Plek.mc. Niet met de hand\n"
           "// aanpassen. Op een rond scherm blijft elke hoed minstens %d px binnen de cirkel (moet van Daan, 16 nov).\n"
           "module Rand {\n" % MARGE)
    uit += functie("gewoon", 1, "Zoveel gewone hoeden passen heel in beeld (hoed 0 tot en met dit aantal min 1).")
    uit += "\n"
    uit += functie("kroon", 2, "De hoogste plek (vanaf 0) waarop de kroon nog heel in beeld staat.")
    uit += "}\n"
    open(os.path.join(PRODUCT, "source", "Rand.mc"), "w", encoding="utf-8").write(uit)


if __name__ == "__main__":
    main()
