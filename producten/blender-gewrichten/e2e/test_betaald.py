"""Draait met: blender -b --factory-startup --python e2e/test_betaald.py -- <betaalde zip> <gratis zip>
Betaalde build (ontwerp betaald v1.1): installeren en aanzetten werkt, het betaalde deel is geladen en de
kern doet het nog (operators, paneel). Daarna de weigering bij dubbel aanstaan: de gratis zip in een tweede
repository erbij; aanzetten van de betaalde naast de gratis moet weigeren met de melding.
Regels met [cj-betaald] in het log. Exit 1 bij elke fout."""
import os
import sys
import traceback

import addon_utils
import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import toetsen_scharnier  # noqa: E402

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
    # Rekentoets van de weigering zelf.
    stap("andere_versies ziet gratis naast betaald",
         betaald.andere_versies(["bl_ext.blender_org.click_joints", eigen], eigen) == ["bl_ext.blender_org.click_joints"])
    stap("andere_versies negeert zichzelf en andere add-ons",
         betaald.andere_versies([eigen, "bl_ext.user_default.iets_anders"], eigen) == [])
    # Echt: gratis in een eigen repository erbij, betaalde uit, gratis aan, betaalde weer aan -> geweigerd.
    addon_utils.disable(eigen, default_set=True)
    bpy.ops.preferences.extension_repo_add(name="cj_gratis", type="LOCAL")
    repo = bpy.context.preferences.extensions.repos[-1]
    bpy.ops.extensions.package_install_files(filepath=zip_gratis, repo=repo.module, enable_on_install=True)
    gratis_mod = f"bl_ext.{repo.module}.click_joints"
    stap("gratis staat aan in eigen repository", gratis_mod in aan(), str(aan()))
    addon_utils.enable(eigen, default_set=True, handle_error=lambda e: print(f"[cj-betaald] melding: {e}"))
    stap("betaalde weigert naast de gratis", eigen not in aan(), str(aan()))
    stap("gratis blijft werken", "plaats" in dir(bpy.ops.click_joints))


try:
    main()
except Exception:
    traceback.print_exc()
    fout += 1
print(f"[cj-betaald] klaar: {fout} FOUT")
sys.exit(1 if fout else 0)
