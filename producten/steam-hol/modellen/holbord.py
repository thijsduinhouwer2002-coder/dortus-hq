"""Bordje met het hol-niveau in 3D (Mila, 16 nov 2026; plaats en maat van Daan, ontwerp/steam/bordje/).

Een plankje op een paaltje links naast de stenen boog, in het gras. Zelfde hout, paal en camera als het pijlbordje
(versiering.py "bordje"), zodat de twee bordjes bij elkaar horen. Maat: plank 13 x 11 spelpixels, paaltje eronder.
De plank heeft een donkere lijst van 1 spelpixel en een lichter vlak; de onderste rij van de lijst is waar het spel
het balkje tekent (leeg donkerbruin, vol goud ffe07a). Het cijfer zit er niet in: dat komt als losse beelden 0 tot 9.

Cijfers: elk een blokjescijfer van 4 x 6 (zelfde vorm als Daans voorstel), room fbf2c0, iets uit het vlak, met een
donkere geschilderde schaduw 1 spelpixel naar rechtsonder, zodat het op ware grootte leest zoals de pijl.

Standen (argument 5): "leeg" (plank, paal, lijst, geen cijfer), "0" tot "9" (één cijfer, los), of een getal zoals
"12" (hele bord met cijfers, alleen voor proefbeelden).
    <venv>/bin/python holbord.py <uit.png> <breedte> <hoogte> <samples> [stand]
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy
import gedeeld as g
import versiering as v

SPX = v.SPX
W_PL, H_PL = 13, 11      # plank in spelpixels
PAAL = 5                 # paaltje onder de plank
CREME = "fbf2c0"
SCHADUW = "4a2418"
F = {"0": ["0110", "1001", "1001", "1001", "1001", "0110"],
     "1": ["0110", "1110", "0110", "0110", "0110", "1111"],
     "2": ["0110", "1001", "0010", "0100", "1000", "1111"],
     "3": ["1110", "0001", "0110", "0001", "0001", "1110"],
     "4": ["1001", "1001", "1001", "1111", "0001", "0001"],
     "5": ["1111", "1000", "1110", "0001", "1001", "0110"],
     "6": ["0110", "1000", "1110", "1001", "1001", "0110"],
     "7": ["1111", "0001", "0010", "0010", "0100", "0100"],
     "8": ["0110", "1001", "0110", "1001", "1001", "0110"],
     "9": ["0110", "1001", "1001", "0111", "0001", "0110"]}


def plank(ouder):
    s = SPX
    hout = v.m("hout", "8a4b2a", rough=0.7, spec=0.2)
    hout_d = v.m("hout_d", "6e4632", rough=0.75, spec=0.2)
    lijst = v.m("lijst", "4e2a1c", rough=0.8, spec=0.15)
    # paaltje, net als bij het pijlbordje
    v.blok(ouder, "bord_paal", (0, 0.2 * s, PAAL * s / 2 + 0.5 * s), (1.6 * s, 1.2 * s, (PAAL + 1) * s), hout_d, rond=0.3 * s)
    zm = PAAL * s + H_PL * s / 2   # midden van de plank
    # lijst: donker blok over de hele plank
    v.blok(ouder, "bord_lijst", (0, -0.4 * s, zm), (W_PL * s, 1.0 * s, H_PL * s), lijst, rond=0.35 * s)
    # vlak: licht hout, 1 spelpixel binnen de lijst, iets naar voren; onderaan blijft de lijst vrij voor het balkje
    v.blok(ouder, "bord_vlak", (0, -0.75 * s, zm + 0.0 * s), ((W_PL - 2) * s, 0.6 * s, (H_PL - 2) * s), hout, rond=0.25 * s)
    # twee spijkertjes bovenin, een klein detail voor wie inzoomt
    ijzer = v.m("ijzer", "4a4452", rough=0.45, metaal=0.7)
    for dx in (-4.6, 4.6):
        v.cil(ouder, "bord_spijker", (dx * s, -1.1 * s, zm + 3.7 * s), 0.35 * s, 0.3 * s, ijzer,
              rot=(math.radians(90), 0, 0), verts=10)
    return zm


def cijfer(ouder, ch, x0, z0):
    """Blokjescijfer 4 x 6 met linksboven op (x0, z0) in Blender-eenheden, vóór het vlak."""
    s = SPX
    room = v.m("cijfer", CREME, rough=0.55, emis=0.08)
    scha = v.m("cijfer_schaduw", SCHADUW, rough=0.9, spec=0.05)
    for r, rij in enumerate(F[ch]):
        for c, a in enumerate(rij):
            if a != "1":
                continue
            x = x0 + (c + 0.5) * s
            z = z0 - (r + 0.5) * s
            v.blok(ouder, "bord_cijfer", (x, -1.25 * s, z), (1.02 * s, 0.5 * s, 1.02 * s), room, rond=0.12 * s)
            # geschilderde schaduw rechtsonder, plat op het vlak
            v.blok(ouder, "bord_schaduw", (x + 0.55 * s, -1.08 * s, z - 0.55 * s), (1.0 * s, 0.1 * s, 1.0 * s), scha, rond=0)


def getal(ouder, txt, zm):
    s = SPX
    breed = len(txt) * 4 + (len(txt) - 1)
    x0 = -breed * s / 2
    z0 = zm + 3.5 * s
    for k, ch in enumerate(txt):
        cijfer(ouder, ch, x0 + k * 5 * s, z0)


# ---------- Wachtkaartje: "de rij bij de ingang" (Mila 16 nov, Sanne voortgang.md Versie 3 definitief punt 5) ----------
# Een papieren volgnummer zoals bij de bakker ("trek een nummertje"), met een rode punaise op het paaltje geprikt,
# net onder de plank. Erop een donker plusje en het aantal niveaus dat nog in de rij staat: "+7". Zelfde x = 0 en z = 0
# als het bordje, dus het spel legt het kaartje met hetzelfde anker en dezelfde nul_y op het bordje.
# kaart1: 9 breed (plus en één cijfer), kaart2: 13 breed (plus en twee cijfers). Kaartje links op x = -1 spelpixel.
PAPIER = "f2e4c2"
INKT = "3a1e14"
PLUS_ROOD = "c8382a"
KAART_X0, KAART_TOP, KAART_H = -1.0, PAAL - 0.5, 7
F3 = {"0": ["010", "101", "101", "101", "010"], "1": ["010", "110", "010", "010", "111"],
      "2": ["110", "001", "010", "100", "111"], "3": ["110", "001", "010", "001", "110"],
      "4": ["101", "101", "111", "001", "001"], "5": ["111", "100", "110", "001", "110"],
      "6": ["011", "100", "110", "101", "010"], "7": ["111", "001", "010", "010", "010"],
      "8": ["010", "101", "010", "101", "010"], "9": ["010", "101", "011", "001", "110"],
      "+": ["000", "010", "111", "010", "000"]}


def _klein(ouder, ch, kol, mat):
    """Teken een 3 x 5 teken in kolom kol van het kaartje (kolom 0 = linkerrand van het papier), rij 1 tot 5."""
    s = SPX
    for r, rij in enumerate(F3[ch]):
        for c, a in enumerate(rij):
            if a == "1":
                x = (KAART_X0 + kol + c + 0.5) * s
                z = (KAART_TOP - 1 - r - 0.5) * s
                v.blok(ouder, "kaart_inkt", (x, -1.62 * s, z), (1.0 * s, 0.25 * s, 1.0 * s), mat, rond=0.08 * s)


def kaartje(ouder, breed):
    s = SPX
    papier = v.m("papier", PAPIER, rough=0.85, spec=0.1)
    rand = v.m("papier_rand", "b89a72", rough=0.9, spec=0.05)
    rood = v.m("plus_rood", PLUS_ROOD, rough=0.5, emis=0.05)
    xm = (KAART_X0 + breed / 2) * s
    zm = (KAART_TOP - KAART_H / 2) * s
    # papier iets voor het paaltje, met een dun donker randje erachter zodat het loskomt van de aarde
    v.blok(ouder, "kaart_rand", (xm, -1.2 * s, zm), ((breed + 0.5) * s, 0.2 * s, (KAART_H + 0.5) * s), rand, rond=0.15 * s)
    v.blok(ouder, "kaart", (xm, -1.4 * s, zm), (breed * s, 0.25 * s, KAART_H * s), papier, rond=0.12 * s)
    # afscheurrandje onderaan: drie kleine tandjes in de rand, het teken van een volgnummer
    for k in range(1, int(breed) // 2):
        v.blok(ouder, "kaart_tand", ((KAART_X0 + 2 * k) * s, -1.55 * s, (KAART_TOP - KAART_H + 0.25) * s),
               (0.5 * s, 0.1 * s, 0.5 * s), rand, rond=0)
    # rode punaise linksboven, in het paaltje geprikt
    v.cil(ouder, "kaart_punaise", ((KAART_X0 + 1.0) * s, -1.8 * s, (KAART_TOP - 0.25) * s), 0.85 * s, 0.5 * s, rood,
          rot=(math.radians(90), 0, 0), verts=14)
    # plusje in dezelfde donkere inkt als het cijfer: een rood plus op wit las als EHBO-kruis ("+7 leven")
    _klein(ouder, "+", 1, v.m("kaart_inkt", INKT, rough=0.8, spec=0.05))


def kaart_cijfer(ouder, ch):
    """Eén donker cijfer op plek A van het kaartje (kolom 5). Bij twee cijfers tekent het spel de eenheden 4 spelpixels
    verder naar rechts."""
    _klein(ouder, ch, 5, v.m("kaart_inkt", INKT, rough=0.8, spec=0.05))


if __name__ == "__main__":
    uit = sys.argv[1]
    W, H, SAMPLES = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    stand = sys.argv[5] if len(sys.argv) > 5 else "12"
    g.leeg()
    ouder = bpy.data.objects.new("holbord", None)
    bpy.context.scene.collection.objects.link(ouder)
    zm = PAAL * SPX + H_PL * SPX / 2
    if stand in ("kaart1", "kaart2"):          # wachtkaartje zonder cijfer
        kaartje(ouder, 9 if stand == "kaart1" else 13)
    elif stand.startswith("k") and stand[1:].isdigit():   # k0 tot k9: cijfer voor het kaartje, los
        kaart_cijfer(ouder, stand[1])
    elif stand.startswith("proefkaart"):       # proefbeeld: bord + kaartje + getal, bv. "proefkaart12+7"
        bord, wacht = stand[len("proefkaart"):].split("+")
        plank(ouder); getal(ouder, bord, zm)
        kaartje(ouder, 9 if len(wacht) == 1 else 13)
        for i, ch in enumerate(wacht):
            _klein(ouder, ch, 5 + 4 * i, v.m("kaart_inkt", INKT, rough=0.8, spec=0.05))
    else:
        if stand == "leeg" or not stand.isdigit() or len(stand) > 1 or os.environ.get("BORD_HEEL"):
            plank(ouder)
        if stand.isdigit():
            getal(ouder, stand, zm)
    # zelfde camera en licht als versiering.py, op het bordje gericht; beeld 20 x 20 spelpixels
    kaart = stand.startswith("k") or stand.startswith("proefkaart")
    # kaartje hangt onder de plank: camera 4 spelpixels lager, zelfde schaal (alle standen van één blad delen hem)
    g.camera(hoogte_midden=zm - (4 * SPX if kaart else 0), schaal=22 * SPX * max(1.0, W / H))
    g.licht()
    sc = bpy.context.scene
    tl = bpy.data.lights.new("tegellicht", "AREA"); tl.shape = "RECTANGLE"; tl.size = 40; tl.size_y = 3.0
    tl.color = (1.0, 0.82, 0.86); tl.energy = 300 * 40 / 10.0
    tlo = bpy.data.objects.new("tegellicht", tl); tlo.location = (0.0, -3.0, 4.6)
    tlo.rotation_euler = (math.radians(52), 0, 0); sc.collection.objects.link(tlo)
    g.render(uit, W, H, SAMPLES, doorzichtig=True)
