"""Draait met: blender -b --factory-startup --python e2e/test_betaald.py -- <betaalde zip> <gratis zip>
Betaalde build (ontwerp betaald v1.1): installeren en aanzetten werkt, het betaalde deel is geladen en de
kern doet het nog (operators, paneel). Daarna de weigering bij dubbel aanstaan (eis 7), in beide volgordes met de gratis zip in een
tweede repository: (a) gratis aan, dan betaald: geweigerd met de melding; (b) betaald aan, dan gratis: de
betaalde gaat eerst netjes uit met dezelfde melding en de gratis werkt; na het uitzetten van de gratis kan
de betaalde weer gewoon aan.
Regels met [cj-betaald] in het log. Exit 1 bij elke fout."""
import os
import sys
import traceback

import addon_utils
import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import toetsen_scharnier  # noqa: E402
import toetsen_scharnier_afstand  # noqa: E402
from hulp_scharnier import cursor as _cursor  # noqa: E402

args = sys.argv[sys.argv.index("--") + 1:]
zip_betaald, zip_gratis = args[0], args[1]
fout = 0


def stap(naam, ok, extra=""):
    global fout
    print(f"[cj-betaald] {'OK' if ok else 'FOUT'} {naam} {extra}".rstrip())
    fout += 0 if ok else 1


def aan():
    return [a.module for a in bpy.context.preferences.addons if a.module.endswith("click_joints")]


def main():
    print(f"[cj-betaald] Blender {bpy.app.version_string}")
    enable_orig = addon_utils.enable
    bpy.ops.extensions.package_install_files(filepath=zip_betaald, repo="user_default", enable_on_install=True)
    mods = aan()
    stap("betaalde build staat aan", len(mods) == 1, str(mods))
    eigen = mods[0] if mods else ""
    betaald = sys.modules.get(eigen + ".betaald")
    stap("betaald deel geladen", betaald is not None and getattr(betaald, "ACTIEF", False))
    for op in ("plaats", "controleer", "maak_gesloten", "exporteer"):
        stap(f"operator click_joints.{op} bestaat", op in dir(bpy.ops.click_joints))
    stap("paneel geregistreerd", hasattr(bpy.types, "CLICK_JOINTS_PT_paneel"))
    if betaald is None:
        return
    stap("operator click_joints.plaats_scharnier bestaat", "plaats_scharnier" in dir(bpy.ops.click_joints))
    try:
        toetsen_scharnier.toets(stap, eigen)  # eis 1 van het scharnier (ontwerp betaald v1.1)
    except Exception:
        traceback.print_exc()
        stap("toetsen scharnier liepen zonder fout", False)
    try:
        toetsen_scharnier_afstand.toets(stap, eigen, _cursor)  # eis 6: kogel naast scharnier, alle scharnieren
    except Exception:
        traceback.print_exc()
        stap("toetsen afstand scharnier liepen zonder fout", False)
    gewricht, maat = sys.modules[eigen + ".gewricht"], sys.modules[eigen + ".maat"]
    stap("betaalde omhult gewricht.te_dicht en gewricht.markeer zolang hij aan staat",
         gewricht.te_dicht is not maat.te_dicht and gewricht.markeer.__module__ != gewricht.__name__)
    # Rekentoets van de weigering zelf.
    stap("andere_versies ziet gratis naast betaald",
         betaald.andere_versies(["bl_ext.blender_org.click_joints", eigen], eigen) == ["bl_ext.blender_org.click_joints"])
    stap("andere_versies negeert zichzelf en andere add-ons",
         betaald.andere_versies([eigen, "bl_ext.user_default.iets_anders"], eigen) == [])
    stap("betaalde omhult addon_utils.enable zolang hij aan staat", addon_utils.enable is not enable_orig)
    # (a) Echt: gratis in een eigen repository erbij, betaalde uit, gratis aan, betaalde weer aan -> geweigerd.
    addon_utils.disable(eigen, default_set=True)
    stap("uitzetten zet addon_utils.enable terug", addon_utils.enable is enable_orig)
    stap("uitzetten zet gewricht.te_dicht en gewricht.markeer terug",
         gewricht.te_dicht is maat.te_dicht and gewricht.markeer.__module__ == gewricht.__name__)
    bpy.ops.preferences.extension_repo_add(name="cj_gratis", type="LOCAL")
    repo = bpy.context.preferences.extensions.repos[-1]
    bpy.ops.extensions.package_install_files(filepath=zip_gratis, repo=repo.module, enable_on_install=True)
    gratis_mod = f"bl_ext.{repo.module}.click_joints"
    stap("gratis staat aan in eigen repository", gratis_mod in aan(), str(aan()))
    meldingen = []

    def fout_cb(e):
        meldingen.append(str(e))
        print(f"[cj-betaald] melding: {e}")

    addon_utils.enable(eigen, default_set=True, handle_error=fout_cb)
    stap("(a) gratis aan, dan betaald: betaalde weigert", eigen not in aan(), str(aan()))
    stap("(a) weigermelding gegeven", any(betaald.MELDING in m for m in meldingen), " | ".join(meldingen))
    stap("(a) gratis blijft werken", "plaats" in dir(bpy.ops.click_joints) and hasattr(bpy.types.Scene, "click_joints"))
    stap("(a) geen omhulsel na weigering", addon_utils.enable is enable_orig)
    # Gratis weer uit: dan kan de betaalde gewoon aan.
    addon_utils.disable(gratis_mod, default_set=True)
    addon_utils.enable(eigen, default_set=True, handle_error=fout_cb)
    stap("gratis uit, dan kan betaald weer aan", aan() == [eigen], str(aan()))
    stap("betaald werkt weer (scharnier-operator)", "plaats_scharnier" in dir(bpy.ops.click_joints))
    # (b) Betaald aan, dan gratis aan -> betaalde gaat eerst uit met de melding, gratis werkt.
    betaald = sys.modules.get(eigen + ".betaald", betaald)  # zelfde module als het omhulsel
    betaald.LAATSTE_MELDING[0] = None
    bpy.ops.preferences.addon_enable(module=gratis_mod)  # zelfde weg als het vinkje in de voorkeuren
    stap("(b) betaald aan, dan gratis: betaalde is uit", eigen not in aan(), str(aan()))
    stap("(b) gratis staat aan", gratis_mod in aan(), str(aan()))
    stap("(b) weigermelding gegeven", betaald.LAATSTE_MELDING[0] == betaald.MELDING_UIT, str(betaald.LAATSTE_MELDING[0]))
    stap("(b) gratis werkt (operators, paneel, scene.click_joints)",
         "plaats" in dir(bpy.ops.click_joints) and hasattr(bpy.types, "CLICK_JOINTS_PT_paneel")
         and hasattr(bpy.types.Scene, "click_joints") and "plaats_scharnier" not in dir(bpy.ops.click_joints))
    stap("(b) omhulsel opgeruimd", addon_utils.enable is enable_orig)
    stap("(b) gratis instelling leesbaar", bpy.context.scene.click_joints is not None)
    # En terug: gratis uit, betaald aan.
    addon_utils.disable(gratis_mod, default_set=True)
    addon_utils.enable(eigen, default_set=True, handle_error=fout_cb)
    stap("(b) gratis weer uit, dan kan betaald weer aan", aan() == [eigen], str(aan()))
    stap("(b) betaald werkt weer", "plaats_scharnier" in dir(bpy.ops.click_joints)
         and addon_utils.enable is not enable_orig)


try:
    main()
except Exception:
    traceback.print_exc()
    fout += 1
print(f"[cj-betaald] klaar: {fout} FOUT")
sys.exit(1 if fout else 0)
