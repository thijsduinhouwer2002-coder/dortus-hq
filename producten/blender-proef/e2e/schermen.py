"""Draait met de interface onder Xvfb: blender --factory-startup --python e2e/schermen.py -- <map> <zip>
Zet het Dortus-paneel open, maakt schermafbeeldingen en sluit Blender af."""
import os
import sys
import bpy

args = sys.argv[sys.argv.index("--") + 1:]
uitmap, zip_pad = args[0], args[1]
os.makedirs(uitmap, exist_ok=True)
teller = {"n": 0}


def open_paneel():
    for venster in bpy.context.window_manager.windows:
        for gebied in venster.screen.areas:
            if gebied.type == "VIEW_3D":
                gebied.spaces.active.show_region_ui = True
                for regio in gebied.regions:
                    if regio.type == "UI":
                        try:
                            regio.active_panel_category = "Dortus"
                        except Exception as e:
                            print(f"[dortus-e2e] tabblad kiezen lukt niet: {e}")
                gebied.tag_redraw()


def schiet(naam):
    pad = os.path.join(uitmap, naam)
    venster = bpy.context.window_manager.windows[0]
    with bpy.context.temp_override(window=venster):
        bpy.ops.screen.screenshot(filepath=pad)
    print(f"[dortus-e2e] schermafbeelding {pad} {os.path.exists(pad)}")


def stap():
    teller["n"] += 1
    n = teller["n"]
    if n == 1:
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        open_paneel()
        return 1.5
    if n == 2:
        schiet("1-paneel.png")
        return 0.5
    if n == 3:
        bpy.ops.dortus.hallo()
        return 1.0
    if n == 4:
        schiet("2-na-klik.png")
        return 0.5
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
