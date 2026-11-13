"""Gedeeld voor alle 3D-modellen van Het Hol: kleuren, materialen, camera en licht.
Afspraak (3d-stijl.md, regel 1): iedereen gebruikt dit bestand, zodat alles in dezelfde wereld staat.
Gemaakt door Daan (13 nov 2026). Mila en Bram: aanpassen mag, zeg het in je logboek.

Gebruik in een model:
    import sys, os; sys.path.insert(0, os.path.dirname(__file__))
    import gedeeld as g
    g.leeg()
    ... model bouwen met g.mat(...) en g.hex2(...) ...
    g.camera(hoogte_midden=1.2, schaal=4.0)
    g.licht()
    g.render(pad, breedte, hoogte, samples, doorzichtig=True)
"""
import math
import bpy
from mathutils import Vector


def hex2(h):
    """sRGB-hex naar lineaire kleur voor Blender."""
    h = h.lstrip("#")
    return tuple((int(h[i:i + 2], 16) / 255) ** 2.2 for i in (0, 2, 4))


# Kleuren uit ontwerp/steam/mila/stijl.md
KLEUR = {
    "munt": "5fd6a4", "munt_d": "2f9c78", "munt_l": "a8f0cf",
    "oogwit": "f6f2e6", "pupil": "1d1530",
    "pruim": "3a2440", "pruim_l": "5a3a63", "pruim_d": "24162b",
    "goud": "f2b632", "goud_d": "b87818",
    "rood": "c8423b", "paars": "6b4fbf", "staal": "aab4c4",
    "mond": "4a1a36", "tong": "e0607a", "tand": "fbf6e4", "blos": "f08a9a",
}


def leeg():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def mat(naam, kleur, rough=0.5, spec=0.4, emis=0.0, sss=0.0, glas=0.0, metaal=0.0):
    if isinstance(kleur, str):
        kleur = hex2(KLEUR.get(kleur, kleur))
    m = bpy.data.materials.new(naam)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*kleur, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metaal
    if "Specular IOR Level" in b.inputs:
        b.inputs["Specular IOR Level"].default_value = spec
    if emis:
        b.inputs["Emission Color"].default_value = (*kleur, 1)
        b.inputs["Emission Strength"].default_value = emis
    if sss:
        b.inputs["Subsurface Weight"].default_value = sss
        b.inputs["Subsurface Radius"].default_value = (0.4, 0.9, 0.5)
    if glas:
        b.inputs["Transmission Weight"].default_value = glas
        b.inputs["IOR"].default_value = 1.33
    return m


def camera(hoogte_midden=1.2, schaal=4.0):
    """Orthografisch, van voren, 15 graden van boven. Zelfde hoek voor alles."""
    sc = bpy.context.scene
    cam = bpy.data.cameras.new("cam")
    cam.type = "ORTHO"
    cam.ortho_scale = schaal
    co = bpy.data.objects.new("cam", cam)
    sc.collection.objects.link(co)
    sc.camera = co
    hoek = math.radians(75)
    afstand = 12
    co.location = (0.0, -afstand * math.sin(hoek), hoogte_midden + afstand * math.cos(hoek))
    co.rotation_euler = (hoek, 0, 0)
    return co


def _licht(naam, soort, loc, kleur, kracht, grootte=1.0, doel=(0, 0, 1.0)):
    sc = bpy.context.scene
    d = bpy.data.lights.new(naam, soort)
    d.color = kleur
    d.energy = kracht
    if soort == "AREA":
        d.size = grootte
    o = bpy.data.objects.new(naam, d)
    o.location = loc
    sc.collection.objects.link(o)
    o.rotation_euler = (Vector(doel) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
    return o


def licht():
    """Eén lichtopstelling: warme fakkel rechts, koel tegenlicht links achter, zacht van boven."""
    _licht("fakkel", "POINT", (2.8, -2.4, 2.0), (1.0, 0.66, 0.36), 650)
    _licht("koel", "AREA", (-3.2, 1.5, 3.0), (0.55, 0.62, 1.0), 500, 2.5)
    _licht("boven", "AREA", (0, -2.5, 6.0), (1.0, 0.96, 0.92), 420, 5.0)
    _licht("vul", "AREA", (-1.5, -5.0, 1.5), (0.85, 0.85, 1.0), 120, 4.0)
    sc = bpy.context.scene
    sc.world = bpy.data.worlds.new("w")
    sc.world.use_nodes = True
    sc.world.node_tree.nodes["Background"].inputs["Color"].default_value = (0.05, 0.035, 0.07, 1)
    sc.world.node_tree.nodes["Background"].inputs["Strength"].default_value = 1.0


def _frames_uit_pijplijn():
    """Bram (13 nov): de pijplijn (producten/steam-hol/pijplijn/render.py) kan via HOL_FRAMES vragen om
    meer beelden van hetzelfde model: een JSON-lijst van [breed, hoog] per beeld, bijvoorbeeld
    [[1, 1], [1.3, 0.45]] voor rust en plat. Alles behalve camera en licht wordt dan rond de vloer (0, 0, 0)
    zo geschaald. Zonder HOL_FRAMES verandert er niets."""
    import json, os
    tekst = os.environ.get("HOL_FRAMES", "").strip()
    return json.loads(tekst) if tekst else None


def render(pad, breedte, hoogte, samples=64, doorzichtig=True):
    frames = _frames_uit_pijplijn()
    if frames:
        import os
        sc = bpy.context.scene
        anker = bpy.data.objects.new("pijplijn_anker", None)
        sc.collection.objects.link(anker)
        for o in list(sc.objects):
            if o is not anker and o.parent is None and o.type not in ("CAMERA", "LIGHT"):
                o.parent = anker
        # ruimer kader (HOL_RUIMTE, bv. 1.6): de pijplijn snijdt daarna zelf strak bij, dan valt plat niet buiten beeld
        ruimte = float(os.environ.get("HOL_RUIMTE", "1") or 1)
        if sc.camera and ruimte != 1:
            sc.camera.data.ortho_scale *= ruimte
        stam, ext = os.path.splitext(pad)
        for i, (sx, sz) in enumerate(frames):
            anker.scale = (sx, sx, sz)
            _render_een(f"{stam}_{i}{ext or '.png'}", breedte, hoogte, samples, doorzichtig)
        return
    _render_een(pad, breedte, hoogte, samples, doorzichtig)


def _render_een(pad, breedte, hoogte, samples=64, doorzichtig=True):
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.cycles.samples = samples
    sc.cycles.device = "CPU"
    sc.cycles.use_denoising = True
    sc.render.resolution_x = breedte
    sc.render.resolution_y = hoogte
    sc.render.resolution_percentage = 100
    sc.render.film_transparent = doorzichtig
    sc.render.image_settings.file_format = "PNG"
    sc.render.image_settings.color_mode = "RGBA"
    sc.view_settings.view_transform = "Standard"
    sc.render.filepath = pad
    bpy.ops.render.render(write_still=True)
