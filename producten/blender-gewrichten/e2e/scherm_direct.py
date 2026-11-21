"""Schermen van de direct-zip (Pro-knoppen op slot, Afkijker 21 nov): het echte paneel met de drie knoppen met slot en
"Upgrade to Pro", en het venstertje na een klik op een slot.
    blender --gpu-backend opengl start.blend --python e2e/scherm_direct.py -- <map> <direct zip>
Plaatjes: d1-slot (hele scherm) en d1-slot-paneel (uitsnede zijbalk), d2-venster en d2-venster-paneel (na een klik op
"Figure from rig"). Regels "DIRECT OK <naam>" in het log; d1 is verplicht, d2 is een extra (een venster bij de muis
onder Xvfb lukt niet altijd) en geeft bij mislukken "DIRECT LET OP". Afsluitcode 1 als d1 ontbreekt."""
import os
import subprocess
import sys
import time

import bpy

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from scherm_basis import log, maak_pop, open_paneel, toestand, uitmap, weergave, wiel_naar_tabblad, xdo, zijbalk, zip_pad  # noqa: E402

fouten = []


def schiet(naam, verplicht=True):
    pad = os.path.join(uitmap, naam + ".png")
    subprocess.run(["import", "-window", "root", pad], capture_output=True)
    venster, _gebied, regio = zijbalk()
    if os.path.exists(pad) and regio:
        x = venster.x + regio.x
        y = venster.y + venster.height - (regio.y + regio.height)
        subprocess.run(["convert", pad, "-crop", f"{regio.width}x{regio.height}+{x}+{y}", "+repage",
                        os.path.join(uitmap, naam + "-paneel.png")], capture_output=True)
    ok = os.path.exists(os.path.join(uitmap, naam + "-paneel.png"))
    if not ok and verplicht:
        fouten.append(naam)
    log(f"DIRECT {'OK' if ok else ('FOUT' if verplicht else 'LET OP')} {naam}")


def venster():
    """Klik op het slot zoals de gebruiker: operator met INVOKE in de context van de zijbalk, muis boven het paneel."""
    win, gebied, regio = zijbalk()
    x = win.x + regio.x + regio.width // 2
    y = win.y + win.height - (regio.y + regio.height // 2)
    xdo("mousemove", str(x), str(y))
    time.sleep(0.3)
    with bpy.context.temp_override(window=win, area=gebied, region=regio):
        uit = bpy.ops.click_joints.pro_slot("INVOKE_DEFAULT", functie="Figure from rig")
    log(f"DIRECT venster {uit}")


def verloop():
    log(f"Blender {bpy.app.version_string}, direct-zip {zip_pad}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    yield 1.0
    maak_pop()
    weergave()
    open_paneel()
    yield 1.0
    while not wiel_naar_tabblad() and toestand["pogingen"] < 14:
        yield 0.5
    _w, _g, regio = zijbalk()
    if not (regio and regio.active_panel_category == "Click Joints"):
        fouten.append("tabblad")
        log("DIRECT FOUT tabblad Click Joints niet actief")
    yield 2.0
    schiet("d1-slot")
    try:
        venster()
    except Exception as e:  # noqa: BLE001
        log(f"DIRECT LET OP venster faalde: {e!r}")
    yield 1.5
    schiet("d2-venster", verplicht=False)
    log(f"DIRECT KLAAR {len(fouten)} FOUT {fouten}")
    os._exit(1 if fouten else 0)


gang = verloop()


def stap():
    try:
        return next(gang)
    except StopIteration:
        return None
    except Exception as e:  # noqa: BLE001  een fout in de timer mag Blender niet open laten hangen
        log(f"DIRECT FOUT uitzondering {e!r}")
        os._exit(1)


bpy.app.timers.register(stap, first_interval=3.0)
