#!/usr/bin/env python3
"""Zet de spritekit van Mila (ontwerp/garmin/gloop-spel/kit/) in de resources van het spel.

Gebruik: python3 maak_kit.py <pad naar kit>   (de kit staat op main, dit product op een tak)
Maakt res-208/ tot res-454/ (plaatjes plus drawables.xml) en source/Maten.mc (maten en ankers
uit kit.json). Niets met de hand aanpassen in die mappen: draai dit script opnieuw als de kit verandert.
"""
import json, os, shutil, sys

KIT = sys.argv[1]
HIER = os.path.dirname(os.path.abspath(__file__))
# schermbreedte -> map in de kit, en of het een MIP-scherm is (64 kleuren, dithering uit)
MAPPEN = {208: ("208-mip", True), 240: ("240-mip", True), 260: ("260-mip", True), 280: ("280-mip", True),
          320: ("320", False), 390: ("390", False), 416: ("416", False), 454: ("454", False)}
VAST = ["gloop-rust", "gloop-hap", "gloop-blij", "gloop-slok", "held-val", "helm-vlieg"]
# Launchericoon van Mila (gekeurd door Daan, 16 nov): map icoon/ naast de kit. De compiler schaalt
# naar de maat van het horloge; 40 heeft een eigen tekening voor kleine maten.
# Maat die elk horloge vraagt (compiler.json in de SDK, gelezen in run 43820999649): FR255, fenix 7,
# fenix 7X en Venu Sq 2 40 px, FR265 60 px, Venu 3S en Venu 3 70 px (die krijgen 80, de compiler verkleint).
ICOON = {208: 40, 240: 40, 260: 40, 280: 40, 320: 40, 390: 80, 416: 60, 454: 80}
HOEDEN = ["hoed-00-helm", "hoed-01-puntmuts", "hoed-02-kap", "hoed-03-pet", "hoed-04-kroon",
          "hoed-05-koksmuts", "hoed-06-emmer", "hoed-07-hoge_hoed", "hoed-08-pan", "hoed-09-veermuts"]
IDS = ["GloopRust", "GloopHap", "GloopBlij", "GloopSlok", "HeldVal", "HelmVlieg"] + ["Hoed%d" % i for i in range(10)]

kit = json.load(open(os.path.join(KIT, "kit.json")))
takken = []
for breedte, (naam, mip) in sorted(MAPPEN.items()):
    doel = os.path.join(HIER, "res-%d" % breedte, "drawables")
    shutil.rmtree(os.path.join(HIER, "res-%d" % breedte), ignore_errors=True)
    os.makedirs(doel)
    regels = ["<drawables>"]
    for ident, stuk in zip(IDS, VAST + HOEDEN):
        bestand = stuk.replace("-", "_") + ".png"
        shutil.copy(os.path.join(KIT, naam, stuk + ".png"), os.path.join(doel, bestand))
        extra = ' dithering="none"' if mip else ""
        regels.append('    <bitmap id="%s" filename="%s"%s/>' % (ident, bestand, extra))
    # Titelplaatje "GLOOP / HAT TOWER" voor het startscherm en het launchericoon.
    shutil.copy(os.path.join(KIT, naam, "titel.png"), os.path.join(doel, "titel.png"))
    regels.append('    <bitmap id="Titel" filename="titel.png"%s/>' % (' dithering="none"' if mip else ""))
    if not mip:
        # Donkere grot van Mila (16 nov): het hele scherm als plaatje van 16 kleuren, alleen AMOLED.
        # De code laadt hem in de functie met (:amoled); monkey.jungle sluit die uit op MIP.
        shutil.copy(os.path.join(KIT, naam, "grot-donker.png"), os.path.join(doel, "grot_donker.png"))
        regels.append('    <bitmap id="Grot" filename="grot_donker.png"/>')
    shutil.copy(os.path.join(KIT, "..", "icoon", "launcher-%d-keus.png" % ICOON[breedte]),
                os.path.join(doel, "launcher_icon.png"))
    regels.append('    <bitmap id="LauncherIcon" filename="launcher_icon.png"/>')
    regels.append("</drawables>")
    open(os.path.join(doel, "kit.xml"), "w").write("\n".join(regels) + "\n")
    m = kit[naam]
    a = m["_ankers"]
    rij = [m["gloop-rust"][0], m["gloop-rust"][1], m["gloop-hap"][1], m["gloop-blij"][1],
           m["gloop-slok"][0], m["gloop-slok"][1], m["held-val"][0], m["held-val"][1],
           m["helm-vlieg"][0], m["helm-vlieg"][1], a["toren_voet"][0], a["toren_voet"][1]]
    for hd in HOEDEN:
        rij += m[hd]
    from PIL import Image
    rij += list(Image.open(os.path.join(KIT, naam, "titel.png")).size)
    takken.append((breedte, rij))

uit = ["import Toybox.Lang;", "",
       "// GEMAAKT DOOR maak_kit.py uit ontwerp/garmin/gloop-spel/kit/kit.json. Niet met de hand aanpassen.",
       "// Volgorde: 0 Gloop breed, 1 rust hoog, 2 hap hoog, 3 blij hoog, 4 slok breed, 5 slok hoog,",
       "// 6 held breed, 7 held hoog, 8 helm breed, 9 helm hoog, 10 en 11 voet van de toren (px in de",
       "// rustsprite), daarna per hoed breed en hoog (12 en 13 voor hoed 0, tot 30 en 31 voor hoed 9),",
       "// 32 en 33 de titel breed en hoog.",
       "module Maten {",
       "    function voor(breedte as Number) as Array<Number> {"]
for breedte, rij in sorted(takken, reverse=True):
    if breedte == min(MAPPEN):
        continue
    uit.append("        if (breedte >= %d) {" % breedte)
    uit.append("            return %s as Array<Number>;" % json.dumps(rij))
    uit.append("        }")
uit.append("        return %s as Array<Number>;" % json.dumps(dict(takken)[min(MAPPEN)]))
uit += ["    }", "}", ""]
open(os.path.join(HIER, "source", "Maten.mc"), "w").write("\n".join(uit))
print("klaar:", [b for b, _ in takken])
