"""Draait met: blender -b --factory-startup --python e2e/test_achtergrond.py -- <pad naar zip>
Installeert Click Joints als extensie en toetst gewricht, speling, passing, Maak gesloten en STL-export,
plus de correcties van de controleur (toetsen_correcties.py). Hulpfuncties staan in hulp.py.
Alles wat hij meet staat in het log (regels met [cj-e2e]). Exit 1 bij elke fout."""
import os
import sys
import traceback

import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figuren  # noqa: E402

zip_pad = sys.argv[sys.argv.index("--") + 1]
from hulp import (delen, fouten, gesloten_delen, log, meting, plaats, speling_meten, stap,  # noqa: E402
                  toets_materiaal, toets_opening, toets_stl, toets_uit_elkaar, weg)
import toetsen_auto  # noqa: E402
import toetsen_correcties  # noqa: E402
import toetsen_schaal  # noqa: E402
import toetsen_uit_elkaar  # noqa: E402


def main():
    log(f"Blender {bpy.app.version_string}")
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    namen = [a.module for a in bpy.context.preferences.addons]
    stap("add-on staat aan", any(n.endswith("click_joints") for n in namen))
    for op in ("plaats", "controleer", "maak_gesloten", "exporteer"):
        stap(f"operator click_joints.{op} bestaat", op in dir(bpy.ops.click_joints))
    stap("paneel geregistreerd", hasattr(bpy.types, "CLICK_JOINTS_PT_paneel"))
    toetsen_schaal.alles()  # schaalwaarschuwing en lege exportmap, eindigt in de mm-scene
    figuren.mm_scene()

    # 1. Groot figuur: speling 0,1 / 0,2 / 0,3 mm, elk precies twee gesloten delen.
    arm = figuren.arm()
    for s in (0.1, 0.2, 0.3):
        lijst = plaats(f"arm speling {s}", arm, (0, 0, 0), (1, 0, 0), speling=s)
        gesloten_delen(f"arm {s}", lijst)
        stap(f"arm {s}: origineel verborgen bewaard", arm.name in bpy.data.objects and not arm.visible_get())
        if len(lijst) == 2:
            speling_meten(lijst, s)
            toets_opening(lijst, f"arm {s}")
            log(f"PASSING arm {s}: {lijst[0].get('cj_passing')}")
        if s == 0.3 and len(lijst) == 2:
            toets_stl(lijst)
            toets_uit_elkaar(lijst)
            toetsen_uit_elkaar.tweede_gewricht(lijst)
        weg(lijst)

    # 1b. Ronde e: automatische kogelmaat en geen selectie na Place joint.
    toetsen_auto.alles(arm)

    # 2. Te dunne plek: rood, geen snede, origineel heel.
    lijst = plaats("arm dunne plek", arm, (15, 0, 0), (1, 0, 0))
    rood = [o for o in bpy.context.scene.objects if o.get("cj_passing") == "rood"]
    log(f"DUN: delen={len(lijst)} rode_gewrichten={[o.name for o in rood]} wand={[o.get('cj_wand_mm') for o in rood]}")
    stap("dunne plek: cj_passing == rood", len(rood) == 1)
    for o in rood:
        toets_materiaal("dunne plek", o)
    stap("dunne plek: niet gesneden", len(lijst) == 0)
    fout, vol = meting(arm)
    stap(f"dunne plek: origineel heel en zichtbaar (foute_randen={fout})", fout == 0 and vol > 0 and arm.visible_get())
    weg(rood)
    arm.hide_set(True)

    # 2b. Echt dunne wand (staaf van 3,1 mm straal: wand 0,4 mm) moet rood, 1,1 mm moet oranje.
    for straal, verwacht in ((3.1, "rood"), (3.8, "oranje")):
        st = figuren.staaf(f"staaf_{straal}", straal)
        lijst = plaats(f"staaf {straal}", st, (0, 0, 0), (1, 0, 0))
        tekens = [o for o in bpy.context.scene.objects if o.get("cj_passing") and o.get("cj_bron") == st.name]
        kleur = tekens[0].get("cj_passing") if tekens else None
        wand = tekens[0].get("cj_wand_mm") if tekens else None
        log(f"WAND staaf straal {straal}: passing={kleur} wand={wand}mm delen={len(lijst)}")
        stap(f"staaf {straal}: passing {verwacht}", kleur == verwacht)
        if verwacht == "rood":
            stap(f"staaf {straal}: niet gesneden, origineel zichtbaar", len(lijst) == 0 and st.visible_get())
        else:
            gesloten_delen(f"staaf {straal}", lijst)
        weg([o for o in bpy.context.scene.objects if o.get("cj_bron") == st.name] + [st])

    # 3. Pop van bollen en cilinders.
    pop = figuren.pop(lijst_solver())
    fout, vol = meting(pop)
    log(f"POP: driehoeken={sum(len(p.vertices) - 2 for p in pop.data.polygons)} foute_randen={fout} volume={vol:.1f}")
    lijst = plaats("pop arm", pop, (11, 0, 3), (1, 0, 0), kogel=3.0)
    gesloten_delen("pop", lijst)
    weg(lijst)
    lijst = plaats("pop pen", pop, (-11, 0, 3), (-1, 0, 0), kogel=2.0, soort="PEN")
    gesloten_delen("pop pen", lijst)
    weg(lijst)
    pop.hide_set(True)

    # 4. Open figuur: eerst een nette melding, na Maak gesloten twee gesloten delen.
    open_ob = figuren.open_arm()
    fout, _ = meting(open_ob)
    log(f"OPEN: foute_randen={fout}")
    figuren.zet_cursor((0, 0, 0), (1, 0, 0))
    figuren.maak_actief(open_ob)
    melding = None
    try:
        uitslag = bpy.ops.click_joints.plaats()
        log(f"OPEN: uitslag zonder fout {uitslag}")
    except RuntimeError as e:
        melding = str(e).strip()
    log(f"OPEN: melding: {melding}")
    stap("open figuur: nette melding", bool(melding) and "not watertight" in melding)
    stap("open figuur: geen delen", len(delen()) == 0)
    bpy.context.scene.click_joints.voxel_mm = 0.4
    bpy.ops.click_joints.maak_gesloten()
    kopie = bpy.context.view_layer.objects.active
    fout, vol = meting(kopie)
    log(f"OPEN: na maak_gesloten {kopie.name} foute_randen={fout} volume={vol:.1f} vlakken={len(kopie.data.polygons)}")
    stap("open figuur: kopie is gesloten", fout == 0 and vol > 0 and kopie is not open_ob)
    lijst = plaats("gesloten kopie", kopie, (0, 0, 0), (1, 0, 0))
    gesloten_delen("na maak_gesloten", lijst)
    weg(lijst)
    for o in list(bpy.context.scene.objects):
        o.hide_set(True)

    # 5. Correcties van de controleur: Exact met en zonder Self Intersection, modifiers en spiegeling,
    #    kijkrichting zonder 3D-venster, en als laatste de scene in meters.
    toetsen_correcties.alles(arm)


def lijst_solver():
    from hulp import addon
    return addon("gewricht").solver_naam()


try:
    main()
except Exception:
    traceback.print_exc()
    fouten.append("uitzondering")

log(f"klaar, fouten: {fouten}")
sys.exit(1 if fouten else 0)
