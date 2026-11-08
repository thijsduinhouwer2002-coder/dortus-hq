"""Plaatje 4 van de schermtest: de drie passingmaterialen in Material Preview en de kleurmeting op het X-scherm.
Opgesplitst uit schermen.py (opruimen 8 nov)."""
import os
import subprocess
import bpy
from mathutils import Vector

from scherm_basis import log, staat, zijbalk
import scherm_basis


# Eén scherm in Material Preview (Daan, beoordeling 2, punt 1 en controleur punt c): de drie echte
# passingmaterialen van de add-on (kleur.materiaal, dus kleur uit passing.KLEUREN) als cilinders naast elkaar.
# Zo zien we of het felle geel in Material Preview bleker wordt. De oude proefstrook met vier geeltinten is
# weg sinds de keuze (#FFEA00) in de add-on staat.
KIJK_STROOK = Vector((0.8, 0.6, -0.3))


def proefstrook():
    import bmesh
    import importlib
    naam = next(a.module for a in bpy.context.preferences.addons if a.module.endswith("click_joints"))
    kleur = importlib.import_module(naam + ".kleur")
    passing = importlib.import_module(naam + ".passing")
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob)
    venster, gebied, _ = zijbalk()
    ruimte = gebied.spaces.active
    ruimte.show_region_ui = False  # zijbalk dicht: de hele weergave voor de strook
    rv3d = ruimte.region_3d
    rv3d.view_perspective = "PERSP"
    rv3d.view_rotation = KIJK_STROOK.normalized().to_track_quat("-Z", "Y")
    rechts = rv3d.view_rotation @ Vector((1.0, 0, 0))
    rechts.z = 0
    rechts.normalize()
    staat["strook"] = []
    soorten = ["groen", "oranje", "rood"]
    for i, soort in enumerate(soorten):
        mat = kleur.materiaal(soort)
        rgb = passing.KLEUREN[soort][:3]
        hx = "#" + "".join(f"{round(255 * (c * 12.92 if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055)):02X}"
                           for c in rgb)
        plek = rechts * (i - (len(soorten) - 1) / 2) * 6.0
        bm = bmesh.new()
        bmesh.ops.create_cone(bm, cap_ends=True, segments=64, radius1=2.0, radius2=2.0, depth=10.0)
        me = bpy.data.meshes.new(f"tint_{soort}")
        bm.to_mesh(me)
        bm.free()
        for v in me.polygons:
            v.use_smooth = True  # glad, zoals Daan het voor de lijstplaatjes wil
        ob = bpy.data.objects.new(f"tint_{soort}", me)
        ob.location = plek
        bpy.context.scene.collection.objects.link(ob)
        me.materials.append(mat)
        tekst = bpy.data.curves.new(f"label_{soort}", "FONT")
        tekst.body, tekst.size, tekst.align_x = f"{kleur.NAMEN[soort]}\n{hx}", 1.0, "CENTER"  # twee regels, anders lopen ze in elkaar
        lab = bpy.data.objects.new(f"label_{soort}", tekst)
        lab.location = plek + Vector((0, 0, -7.5))
        lab.rotation_mode = "QUATERNION"
        lab.rotation_quaternion = rv3d.view_rotation
        bpy.context.scene.collection.objects.link(lab)
        staat["strook"].append((f"{kleur.NAMEN[soort]} {hx}", ob))
    ruimte.shading.type = "MATERIAL"
    regio = next(r for r in gebied.regions if r.type == "WINDOW")
    with bpy.context.temp_override(window=venster, area=gebied, region=regio):
        bpy.ops.view3d.view_all()
    gebied.tag_redraw()
    log(f"proefstrook: Material Preview met {[n for n, _ in staat['strook']]}, weergave {ruimte.shading.type}")


def meet_strook(naam="4-material-preview-x.png"):
    """Leest per cilinder de kleur op het X-scherm langs een horizontale lijn door het midden:
    de lichtste plek (belichte kant) en de donkerste."""
    from bpy_extras.view3d_utils import location_3d_to_region_2d
    venster, gebied, _ = zijbalk()
    regio = next(r for r in gebied.regions if r.type == "WINDOW")
    rv3d = gebied.spaces.active.region_3d
    pad = os.path.join(scherm_basis.uitmap, naam)
    log(f"KLEUR meting op {naam}, weergave {bpy.context.scene.view_settings.view_transform}")
    if not os.path.exists(pad):
        log("KLEUR: geen X-scherm")
        return
    for hx, ob in staat["strook"]:
        punten = []
        for f in [x / 10.0 for x in range(-8, 9)]:
            rel = (rv3d.view_rotation @ Vector((1.0, 0, 0))) * (2.0 * f)
            p2 = location_3d_to_region_2d(regio, rv3d, ob.location + rel)
            if p2 is None:
                continue
            x = int(venster.x + regio.x + p2.x)
            y = int(venster.y + venster.height - (regio.y + p2.y))
            r = subprocess.run(["convert", pad, "-format", f"%[hex:p{{{x},{y}}}]", "info:"],
                               capture_output=True, text=True)
            h = r.stdout.strip()[:6]
            if len(h) == 6:
                punten.append(h)
        if not punten:
            log(f"KLEUR {hx}: niets gemeten")
            continue
        helder = lambda h: 0.2126 * int(h[0:2], 16) + 0.7152 * int(h[2:4], 16) + 0.0722 * int(h[4:6], 16)
        licht, donker = max(punten, key=helder), min(punten, key=helder)
        log(f"KLEUR {hx}: belicht #{licht} schaduw #{donker} monsters={len(punten)}")
