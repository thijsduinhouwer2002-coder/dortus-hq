"""Draait met de interface onder Xvfb: blender --python e2e/schermen.py -- <map> <zip>
Zet het Click Joints-paneel open met een pop, plaatst een gewricht, maakt schermafbeeldingen en sluit af.
Daarna een gewricht met de as langs de kijkrichting, aangeroepen vanuit de zijbalk (regel "KIJK OK").

Tabblad kiezen: `active_panel_category` is alleen-lezen, daarom draait de test met
xdotool Ctrl+muiswiel boven de zijbalk (zo wisselt Blender van tabblad) tot het
tabblad Click Joints actief is. Dat lezen we wel uit, dus het bewijs staat in het log.

De onderdelen staan in scherm_basis.py (zijbalk, tabblad, pop, kijkrichting), scherm_kleur.py (plaatje 4)
en scherm_beweeg.py (plaatjes 5 tot 7); dit bestand doet alleen de volgorde."""
import os
import sys
import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scherm_basis import (DOEL, close_up, kijk, log, maak_pop, open_paneel, plaats, schiet,  # noqa: E402
                          toestand, weergave, wiel_naar_tabblad, zijbalk, zip_pad)
from scherm_kleur import meet_strook, proefstrook  # noqa: E402
from scherm_beweeg import boog_verslag, plat_lid, voorbij_grens, waaier  # noqa: E402


def stap():
    toestand["n"] += 1
    n = toestand["n"]
    if n == 1:
        log(f"Blender {bpy.app.version_string}, splash in voorkeuren: {bpy.context.preferences.view.show_splash}")
        bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
        maak_pop()
        open_paneel()
        weergave()
        return 1.5
    if n == 2:
        if not wiel_naar_tabblad() and toestand["pogingen"] < 14:
            toestand["n"] = 1  # deze stap nog eens
            return 0.6
        _, _, regio = zijbalk()
        log(f"TABBLAD {'OK' if regio and regio.active_panel_category == DOEL else 'NIET GELUKT'}")
        return 0.8
    if n == 3:
        schiet("1-paneel.png")
        return 0.5
    if n == 4:
        plaats()
        weergave()
        close_up()
        return 1.5
    if n == 5:
        schiet("2-gewricht.png")
        return 0.5
    if n == 6:
        kijk()
        return 1.0
    if n == 7:
        schiet("3-kijkrichting.png")
        return 0.5
    if n == 8:
        proefstrook()
        return 8.0  # Material Preview (EEVEE) moet eerst de shaders bouwen, met software-OpenGL duurt dat
    if n == 9:
        schiet("4-material-preview.png")
        meet_strook()
        return 0.5
    if n == 10:
        waaier()
        return 1.5
    if n == 11:
        schiet("5-waaier.png")
        boog_verslag("waaier", voorbij=False)
        return 0.5
    if n == 12:
        voorbij_grens()
        return 1.5
    if n == 13:
        schiet("6-rood.png")
        boog_verslag("rood", voorbij=True)
        return 0.5
    if n == 14:
        plat_lid()
        return 1.5
    if n == 15:
        schiet("7-plat.png")
        return 0.5
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(stap, first_interval=3.0)
