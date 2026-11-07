"""Draait met: blender -b --factory-startup --python e2e/test_achtergrond.py -- <pad naar zip>
Installeert de add-on als extensie, zet hem aan en drukt op de knop. Faalt met exit 1."""
import sys
import traceback
import bpy

zip_pad = sys.argv[sys.argv.index("--") + 1]
fouten = []


def stap(naam, ok):
    print(f"[dortus-e2e] {'OK  ' if ok else 'FOUT'} {naam}")
    if not ok:
        fouten.append(naam)


try:
    print(f"[dortus-e2e] Blender {bpy.app.version_string}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    namen = [a.module for a in bpy.context.preferences.addons]
    print(f"[dortus-e2e] aan: {namen}")
    stap("add-on staat aan", any(n.endswith("dortus_proef") for n in namen))
    stap("operator bestaat", hasattr(bpy.ops.dortus, "hallo"))
    stap("paneel geregistreerd", hasattr(bpy.types, "DORTUS_PT_paneel"))
    bpy.ops.dortus.hallo()
    stap("knop zet vlag", bool(bpy.context.scene.get("dortus_hallo")))
except Exception:
    traceback.print_exc()
    fouten.append("uitzondering")

print(f"[dortus-e2e] klaar, fouten: {fouten}")
sys.exit(1 if fouten else 0)
