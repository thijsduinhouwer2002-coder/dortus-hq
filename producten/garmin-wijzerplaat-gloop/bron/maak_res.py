"""Maakt een plaatjesmap res-<maat>/drawables voor de wijzerplaat uit de twee kits van Mila.

Hoeden komen uit de kit van het spel (ontwerp/garmin/gloop-spel/kit/<maat>/), de rest uit de kit van
de wijzerplaat (ontwerp/garmin/wijzerplaat-gloop/kit/<maat>/). De grijze cijfers van de slaapstand
(alleen AMOLED) zijn de witte vulling van de uurcijfers: elke dekkende pixel waarvan het donkerste
kanaal 147 of hoger is wordt grijs (170), de rest doorzichtig. Zo loopt de 8 niet dicht.

Gebruik, vanuit producten/garmin-wijzerplaat-gloop:
  python3 -I bron/maak_res.py 416 454            maakt res-416 en res-454
  python3 -I bron/maak_res.py --controle 390     maakt de map in een tijdelijke map en vergelijkt hem
                                                 pixel voor pixel met de bestaande res-390
De kit van de wijzerplaat staat op main; geef zijn plek mee met WP_KIT als hij niet naast het product staat.
"""
import os
import shutil
import sys
import tempfile

from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
PRODUCT = os.path.dirname(HIER)
ONTWERP = os.path.join(PRODUCT, "..", "..", "ontwerp", "garmin")
SPEL_KIT = os.environ.get("SPEL_KIT", os.path.join(ONTWERP, "gloop-spel", "kit"))
WP_KIT = os.environ.get("WP_KIT", os.path.join(ONTWERP, "wijzerplaat-gloop", "kit"))
KITMAP = {"208": "208-mip", "240": "240-mip", "260": "260-mip", "280": "280-mip",
          "320": "320", "390": "390", "416": "416", "454": "454"}
HOEDEN = ["00_helm", "01_puntmuts", "02_kap", "03_pet", "04_kroon", "05_koksmuts", "06_emmer",
          "07_hoge_hoed", "08_pan", "09_veermuts"]
GRIJS_DREMPEL = 147
GRIJS = (170, 170, 170, 255)


def grijs_cijfer(bron, doel):
    uur = Image.open(bron).convert("RGBA")
    uit = Image.new("RGBA", uur.size, (0, 0, 0, 0))
    a, b = uur.load(), uit.load()
    for y in range(uur.height):
        for x in range(uur.width):
            r, g, bl, alfa = a[x, y]
            if alfa == 255 and min(r, g, bl) >= GRIJS_DREMPEL:
                b[x, y] = GRIJS
    uit.save(doel)


def kit_xml(amoled):
    extra = "" if amoled else ' dithering="none"'
    r = ["<drawables>"]
    for i, naam in enumerate(HOEDEN):
        r.append('    <bitmap id="Hoed%d" filename="hoed_%s.png" dithering="none"/>' % (i, naam))
    r.append('    <bitmap id="Achter" filename="wp_achter.png"%s/>' % extra)
    r.append('    <bitmap id="GloopKijk" filename="wp_gloop_kijk.png"%s/>' % extra)
    r.append('    <bitmap id="GloopDicht" filename="wp_gloop_dicht.png"%s/>' % extra)
    for soort, kop in (("uur", "Uur"), ("min", "Min")):
        for d in range(10):
            r.append('    <bitmap id="%s%d" filename="wp_%s_%d.png"%s/>' % (kop, d, soort, d, extra))
    r.append('    <bitmap id="GloopAod" filename="%s"/>' % ("wp_gloop_aod.png" if amoled else "wp_leeg.png"))
    for d in range(10):
        r.append('    <bitmap id="HoedAod%d" filename="%s"/>' % (d, ("wp_hoed_%d_aod.png" % d) if amoled else "wp_leeg.png"))
    for d in range(10):
        r.append('    <bitmap id="Grijs%d" filename="%s"/>' % (d, ("wp_grijs_%d.png" % d) if amoled else "wp_leeg.png"))
    r.append('    <bitmap id="LauncherIcon" filename="launcher_icon.png"/>')
    r.append("</drawables>")
    return r


def maak(maat, doelmap):
    spel = os.path.join(SPEL_KIT, KITMAP[maat])
    wp = os.path.join(WP_KIT, KITMAP[maat])
    for m in (spel, wp):
        if not os.path.isdir(m):
            sys.exit("kitmap ontbreekt: " + m)
    amoled = os.path.exists(os.path.join(wp, "gloop-aod.png"))
    os.makedirs(doelmap, exist_ok=True)

    def kopie(bron, naam):
        shutil.copyfile(bron, os.path.join(doelmap, naam))

    for naam in HOEDEN:
        kopie(os.path.join(spel, "hoed-" + naam.replace("_", "-", 1) + ".png"), "hoed_" + naam + ".png")
    kopie(os.path.join(wp, "achter.png"), "wp_achter.png")
    kopie(os.path.join(wp, "gloop-kijk.png"), "wp_gloop_kijk.png")
    kopie(os.path.join(wp, "gloop-dicht.png"), "wp_gloop_dicht.png")
    for d in range(10):
        kopie(os.path.join(wp, "uur-%d.png" % d), "wp_uur_%d.png" % d)
        kopie(os.path.join(wp, "min-%d.png" % d), "wp_min_%d.png" % d)
    if amoled:
        kopie(os.path.join(wp, "gloop-aod.png"), "wp_gloop_aod.png")
        for d, naam in enumerate(HOEDEN):
            kopie(os.path.join(wp, "hoed-" + naam.replace("_", "-", 1) + "-aod.png"), "wp_hoed_%d_aod.png" % d)
            grijs_cijfer(os.path.join(wp, "uur-%d.png" % d), os.path.join(doelmap, "wp_grijs_%d.png" % d))
    else:
        Image.new("RGBA", (1, 1), (0, 0, 0, 0)).save(os.path.join(doelmap, "wp_leeg.png"))
    open(os.path.join(doelmap, "kit.xml"), "w", encoding="utf-8").write("\n".join(kit_xml(amoled)) + "\n")
    return amoled


def pixels(pad):
    im = Image.open(pad).convert("RGBA")
    return im.size, im.tobytes()


def controle(maat):
    echt = os.path.join(PRODUCT, "res-" + maat, "drawables")
    with tempfile.TemporaryDirectory() as tmp:
        maak(maat, tmp)
        fout = 0
        namen = sorted(set(os.listdir(tmp)) | set(os.listdir(echt)))
        for naam in namen:
            if naam == "launcher_icon.png":
                continue
            a, b = os.path.join(tmp, naam), os.path.join(echt, naam)
            if not os.path.exists(a) or not os.path.exists(b):
                print("ONTBREEKT aan een kant:", naam)
                fout += 1
            elif naam.endswith(".xml"):
                if open(a, encoding="utf-8").read().split() != open(b, encoding="utf-8").read().split():
                    print("ANDERS:", naam)
                    fout += 1
            elif pixels(a) != pixels(b):
                print("ANDERS:", naam)
                fout += 1
        print("res-%s: %d bestanden vergeleken, %d anders" % (maat, len(namen) - 1, fout))
        return fout


def main():
    args = sys.argv[1:]
    if args and args[0] == "--controle":
        sys.exit(1 if sum(controle(m) for m in args[1:]) else 0)
    for maat in args:
        doel = os.path.join(PRODUCT, "res-" + maat, "drawables")
        amoled = maak(maat, doel)
        icoon = os.path.join(doel, "launcher_icon.png")
        if not os.path.exists(icoon):
            # Het pictogram zit niet in de kit: neem dat van de dichtstbijzijnde bestaande map.
            shutil.copyfile(os.path.join(PRODUCT, "res-390" if amoled else "res-260", "drawables", "launcher_icon.png"), icoon)
        print("res-%s gemaakt (%s), %d bestanden" % (maat, "AMOLED" if amoled else "MIP", len(os.listdir(doel))))


if __name__ == "__main__":
    main()
