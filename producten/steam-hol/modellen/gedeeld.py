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
import os
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


# Mila 28 nov (#333): het palet voor alle bladen. "" = zoals tot nu (glanzend), "gedempt" = minder verzadigd,
# mat, twee tinten met harde grens en een inktlijn. Zet je dit op "gedempt", dan rendert de pijplijn alle bladen
# opnieuw (gedeeld.py zit in de vingerafdruk). HOL_PALET in de omgeving gaat voor (proeven).
PALET_STANDAARD = "gedempt"   # proeftak claude/steam-palet-gedempt; op main ""


def _palet():
    return os.environ.get("HOL_PALET", PALET_STANDAARD).strip()


def _demp_hex(h):
    """Gedempt palet: verzadiging omlaag (maal 0,8), heel licht naar warm schemer, nooit vlakker dan 0,12."""
    import colorsys
    h = h.lstrip("#")
    r, gr, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    hh, ss, vv = colorsys.rgb_to_hsv(r, gr, b)
    ss = ss * 0.8 if ss > 0.12 else ss
    vv = min(1.0, vv * 0.94 + 0.03)
    r, gr, b = colorsys.hsv_to_rgb(hh, ss, vv)
    r, b = min(1.0, r * 1.02), b * 0.97
    return "%02x%02x%02x" % (round(r * 255), round(gr * 255), round(b * 255))


# Vaste tinten in het gedempte palet (de rest gaat via _demp_hex)
KLEUR_GEDEMPT = {
    "munt": "72cfa6", "munt_d": "389072", "munt_l": "b0e9cf",
    "goud": "f2b632", "goud_d": "b87818", "staal": "a3a9b6",   # goud blijft vol: dat is de beloning
    "8a6438": "a8834c",   # jute zak van de dief: lichter, anders verdwijnt hij tegen de bruine grond
}


def _maak_getekend():
    """Getekende afwerking vlak voor het renderen, voor elk materiaal met een Principled BSDF (ook die een model
    zelf met textuur vult, zoals hol.py en royal.py): twee tinten met een harde grens (Toon BSDF) uit dezelfde
    kleur of textuur, schaduwkant koeler en donkerder, nooit zwart; metaal een kleine harde glimvlek.
    Gloeiende en doorzichtige materialen blijven zoals ze zijn."""
    for m in bpy.data.materials:
        if not m.use_nodes or m.get("getekend"):
            continue
        nt = m.node_tree
        b = nt.nodes.get("Principled BSDF")
        if b is None or not b.outputs[0].is_linked:
            continue
        if b.inputs["Emission Strength"].default_value >= 1.0 or b.inputs["Transmission Weight"].default_value > 0:
            continue
        if b.inputs["Metallic"].default_value > 0.5:
            continue   # goud en staal houden hun echte glans: in de eerste proef werden schat, munten en kroon flets
        doel = b.outputs[0].links[0].to_socket
        bron = b.inputs["Base Color"].links[0].from_socket if b.inputs["Base Color"].is_linked else None
        kleur = tuple(b.inputs["Base Color"].default_value)[:3]

        def keer(f):
            v = nt.nodes.new("ShaderNodeVectorMath")
            v.operation = "MULTIPLY"
            if bron is not None:
                nt.links.new(bron, v.inputs[0])
            else:
                v.inputs[0].default_value = kleur
            v.inputs[1].default_value = f
            return v.outputs[0]
        licht = nt.nodes.new("ShaderNodeBsdfToon")
        licht.component = "DIFFUSE"
        licht.inputs["Size"].default_value = 0.55
        licht.inputs["Smooth"].default_value = 0.03
        # vier lampen tellen op bij een harde grens; daarom de lichte kant gedempt tot hij de kleur zelf geeft
        nt.links.new(keer((0.46, 0.46, 0.46)), licht.inputs["Color"])
        sch = nt.nodes.new("ShaderNodeEmission")
        nt.links.new(keer((0.38, 0.36, 0.50)), sch.inputs["Color"])
        som = nt.nodes.new("ShaderNodeAddShader")
        nt.links.new(licht.outputs[0], som.inputs[0])
        nt.links.new(sch.outputs[0], som.inputs[1])
        if b.inputs["Metallic"].default_value > 0.3:
            glim = nt.nodes.new("ShaderNodeBsdfToon")
            glim.component = "GLOSSY"
            glim.inputs["Size"].default_value = 0.18
            glim.inputs["Smooth"].default_value = 0.02
            glim.inputs["Color"].default_value = (0.35, 0.35, 0.35, 1)
            som2 = nt.nodes.new("ShaderNodeAddShader")
            nt.links.new(som.outputs[0], som2.inputs[0])
            nt.links.new(glim.outputs[0], som2.inputs[1])
            som = som2
        nt.links.new(som.outputs[0], doel)
        m["getekend"] = 1


def mat(naam, kleur, rough=0.5, spec=0.4, emis=0.0, sss=0.0, glas=0.0, metaal=0.0):
    if _palet() == "gedempt":
        # mat en getekend: geen glas en geen natte glans, die lazen als "cheap mobile" (blinde tests 27 nov)
        if isinstance(kleur, str):
            sleutel = kleur
            kleur = KLEUR_GEDEMPT.get(sleutel) or _demp_hex(KLEUR.get(sleutel, sleutel))
        rough = max(rough, 0.6 if not metaal else 0.42)
        spec = min(spec, 0.2)
        glas = 0.0
        sss = min(sss, 0.12)
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


def _verberg_uit_pijplijn():
    """Bram (13 nov): HOL_VERBERG is een JSON-lijst van naambegins, bv. ["gras", "kist"]. Objecten waarvan
    de naam (zonder .001 en zo) zo begint, en hun kinderen, komen niet in de render. Zo maakt de pijplijn
    lagen van één model (achtergrond zonder schat, alleen de schat, ...). Zonder HOL_VERBERG verandert er niets."""
    import json, os
    tekst = os.environ.get("HOL_VERBERG", "").strip()
    if not tekst:
        return
    lijst = json.loads(tekst)
    if not isinstance(lijst, list) or not all(isinstance(b, str) and b for b in lijst):
        raise SystemExit("HOL_VERBERG moet een lijst met namen zijn, bv. [\"kist\"]")
    begins = tuple(lijst)
    if not begins:
        return

    def weg(o):
        if o.type in ("CAMERA", "LIGHT"):
            return   # lampen blijven altijd, ook als kind: elke laag houdt hetzelfde licht
        o.hide_render = True
        for k in o.children:
            weg(k)
    for o in list(bpy.context.scene.objects):
        if o.name.split(".")[0].startswith(begins):
            weg(o)


def _alleen_uit_pijplijn():
    """Bram (13 nov 23:20): HOL_ALLEEN is het omgekeerde van HOL_VERBERG: een JSON-lijst van naambegins, en alleen
    die objecten (met hun kinderen) komen in de render; lampen en camera blijven altijd. Zo maakt de pijplijn een
    doorzichtige laag met alleen fakkels, ladder en ingang (Daan 22:55). Zonder HOL_ALLEEN verandert er niets."""
    import json, os
    tekst = os.environ.get("HOL_ALLEEN", "").strip()
    if not tekst:
        return
    lijst = json.loads(tekst)
    if not isinstance(lijst, list) or not lijst or not all(isinstance(b, str) and b for b in lijst):
        raise SystemExit("HOL_ALLEEN moet een lijst met namen zijn, bv. [\"vlam\"]")
    begins = tuple(lijst)
    houd = set()

    def bewaar(o):
        houd.add(o.name)
        for k in o.children:
            bewaar(k)
    for o in list(bpy.context.scene.objects):
        if o.name.split(".")[0].startswith(begins):
            bewaar(o)
    for o in list(bpy.context.scene.objects):
        if o.type not in ("CAMERA", "LIGHT") and o.name not in houd:
            o.hide_render = True


def render(pad, breedte, hoogte, samples=64, doorzichtig=True):
    _verberg_uit_pijplijn()
    _alleen_uit_pijplijn()
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
        # Bram 13 nov 20:30: de pijplijn wil weten hoe groot een Blender-eenheid in de render is, zodat helden en
        # hun losse hoeden op dezelfde schaal komen. Alleen met HOL_FRAMES, dus voor gewoon draaien verandert niets.
        if sc.camera:
            import json as _json
            from bpy_extras.object_utils import world_to_camera_view
            from mathutils import Vector
            sc.render.resolution_x, sc.render.resolution_y = breedte, hoogte
            bpy.context.view_layer.update()
            o = world_to_camera_view(sc, sc.camera, Vector((0, 0, 0)))   # waar het nulpunt in beeld valt (0..1, y omhoog)
            with open(f"{stam}_cam.json", "w") as f:
                _json.dump({"ortho": sc.camera.data.ortho_scale, "breed": breedte, "hoog": hoogte,
                            "nul_px": [o.x * breedte, (1 - o.y) * hoogte]}, f)
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
    if _palet() == "gedempt" and os.environ.get("HOL_TOON", "1") == "1":
        _maak_getekend()
    if _palet() == "gedempt" and os.environ.get("HOL_LIJN", "0") == "1":
        # getekende inktlijn om het figuur (Freestyle), dikte in renderpixels naar de maat van de render
        sc.render.use_freestyle = True
        sc.render.line_thickness_mode = "ABSOLUTE"
        sc.render.line_thickness = max(1.0, breedte / 70)
        vl = bpy.context.view_layer
        vl.use_freestyle = True
        fs = vl.freestyle_settings
        ls = fs.linesets[0] if fs.linesets else fs.linesets.new("lijn")
        ls.select_by_visibility = True
        ls.select_silhouette = True
        ls.select_border = True
        ls.select_crease = False
        if ls.linestyle is None:
            ls.linestyle = bpy.data.linestyles.new("inkt")
        ls.linestyle.color = (0.11, 0.06, 0.07)
        ls.linestyle.thickness = 1.0
    sc.render.filepath = pad
    bpy.ops.render.render(write_still=True)
