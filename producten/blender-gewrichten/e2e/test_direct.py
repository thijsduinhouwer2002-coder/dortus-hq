"""Draait met: blender -b --factory-startup --python e2e/test_direct.py -- <direct zip>
Direct-zip (Pro-knoppen op slot, Afkijker 21 nov): installeren en aanzetten werkt, de kern doet het nog (operators,
paneel, Report a problem onderaan), het slot-deel is geladen (operator click_joints.pro_slot, tekenfunctie onder het
hoofdpaneel), er zit geen betaalde functie in (geen scharnier, geen betaald/), de knop opent geen link vanzelf, en
uit- en weer aanzetten laat niets achter. Het scherm zelf: scherm_direct.py. Regels [cj-direct]. Exit 1 bij elke fout."""
import sys
import traceback

import addon_utils
import bpy

args = sys.argv[sys.argv.index("--") + 1:]
zip_direct = args[0]
fout = 0


def stap(naam, ok, extra=""):
    global fout
    print(f"[cj-direct] {'OK' if ok else 'FOUT'} {naam} {extra}".rstrip())
    fout += 0 if ok else 1


def aan():
    return [a.module for a in bpy.context.preferences.addons if a.module.endswith("click_joints")]


def tekenfuncties():
    draw = bpy.types.CLICK_JOINTS_PT_paneel.draw
    return list(getattr(draw, "_draw_funcs", []))


def main():
    print(f"[cj-direct] Blender {bpy.app.version_string}")
    bpy.ops.extensions.package_install_files(filepath=zip_direct, repo="user_default", enable_on_install=True)
    mods = aan()
    stap("direct-zip staat aan", len(mods) == 1, str(mods))
    if not mods:
        return
    eigen = mods[0]
    direct = sys.modules.get(eigen + ".direct")
    stap("slot-deel geladen", direct is not None and getattr(direct, "ACTIEF", False))
    stap("geen betaald deel", sys.modules.get(eigen + ".betaald") is None)
    for op in ("plaats", "controleer", "maak_gesloten", "exporteer", "meld", "pro_slot"):
        stap(f"operator click_joints.{op} bestaat", op in dir(bpy.ops.click_joints))
    for op in ("plaats_scharnier", "figuur_uit_rig", "testkaart"):
        stap(f"geen betaalde operator click_joints.{op}", op not in dir(bpy.ops.click_joints))
    stap("Report a problem blijft subpaneel onderaan",
         getattr(bpy.types, "CLICK_JOINTS_PT_meld", None) is not None
         and bpy.types.CLICK_JOINTS_PT_meld.bl_parent_id == "CLICK_JOINTS_PT_paneel")
    if direct is None:
        return
    stap("slotknoppen hangen onder het hoofdpaneel", direct.teken in tekenfuncties())
    stap("drie functies met slot", direct.FUNCTIES == ("Figure from rig", "Hinge with end stop", "Body-part presets"))
    stap("link naar de Pro-pagina", direct.URL == "https://dortus.com/click-joints/")
    stap("teksten", (direct.VENSTER, direct.KNOP, direct.ONDERAAN)
         == ("This is in Click Joints Pro", "See Click Joints Pro", "Upgrade to Pro"))
    # Zonder venster (achtergrond) doet de knop niets en opent hij geen link; het venster zelf staat op het scherm.
    try:
        uit = bpy.ops.click_joints.pro_slot("EXEC_DEFAULT", functie="Figure from rig")
    except Exception:
        traceback.print_exc()
        uit = None
    stap("knop met slot geeft FINISHED zonder venster", uit == {"FINISHED"})
    # Uit en weer aan: geen dubbele tekenfunctie, niets blijft hangen.
    addon_utils.disable(eigen, default_set=True)
    stap("uit: operator weg", "pro_slot" not in dir(bpy.ops.click_joints))
    stap("uit: paneel weg", not hasattr(bpy.types, "CLICK_JOINTS_PT_paneel"))
    addon_utils.enable(eigen, default_set=True)
    direct = sys.modules.get(eigen + ".direct")
    stap("weer aan: precies één tekenfunctie",
         hasattr(bpy.types, "CLICK_JOINTS_PT_paneel") and sum(f.__name__ == "teken" for f in tekenfuncties()) == 1)
    stap("weer aan: operator terug", "pro_slot" in dir(bpy.ops.click_joints))


try:
    main()
except Exception:
    traceback.print_exc()
    stap("test liep zonder fout", False)
print(f"[cj-direct] KLAAR {fout} FOUT")
sys.exit(1 if fout else 0)
