"""Klap-ster bij een val (Mila, 25 nov 2026, issue #43). Vervangt de 6 witte streepjes in kern/klap.gd.

Iris (keuring 52aa730): de oude ster is beige-grijs, ±12 px, één beeld lang en leest als een stofwolk.
Nieuw: een dikke stripster, wit hart, geel lijf, oranje rand en een donkere rand eromheen zodat hij op de
rode aarde, op de gang en op het gras leest. Vier beelden, bedoeld voor 8 per seconde (0,5 s):
  0 inslag: klein wit hart met korte punten (het moment van raken)
  1 ster:   volle ster, ±11 spelpixels breed (±33 px op de strook van 120, oude ster ±12 px)
  2 groot:  ster op zijn grootst, punten dunner, hart kleiner, vier vonkjes los
  3 vonken: ster weg, zes vonkjes vliegen uit en worden kleiner
Cel 16 x 16 spelpixels, midden van de cel = plek van de klap. Vaste camera voor alle beelden (geen bijsnijden),
dus Olaf tekent elk beeld op dezelfde plek.

    <venv>/bin/python klapster.py <uit.png> <px_per_spelpixel> <samples>
Schrijft een blad van 4 cellen naast elkaar (breedte 4 x 16 x px, hoogte 16 x px).
Bpy alleen, geen AI-beeld, geen gekocht pakket.
"""
import sys, os, math, tempfile
import bpy, bmesh

CEL = 16            # spelpixels
EENHEID = 3.2       # Blender-eenheden over de cel (1 eenheid = 5 spelpixels)

DONKER = "3b1405"
ORANJE = "ff8a1c"
GEEL = "ffd23a"
LICHTGEEL = "fff07a"
WIT = "fffdf0"


def lin(hexk):
    c = [int(hexk[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [x ** 2.2 for x in c]


def mat(naam, hexk, gloei=0.75):
    """Glanzend maar fel: een deel eigen licht zodat de kleur op elke ondergrond fel blijft, de rest schaduw van de bol."""
    m = bpy.data.materials.new(naam)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    c = lin(hexk)
    b.inputs["Base Color"].default_value = (*c, 1)
    b.inputs["Roughness"].default_value = 0.35
    b.inputs["Emission Color"].default_value = (*c, 1)
    b.inputs["Emission Strength"].default_value = gloei
    return m


def ster(naam, punten, R, r, z, dik, m, draai=0.0, wiebel=0.0, x=0.0, y=0.0, rand=0.04):
    """Platte ster met afgeronde kanten. wiebel: om en om iets langere punten (stripster, geen wiel)."""
    me = bpy.data.meshes.new(naam)
    bm = bmesh.new()
    vs = []
    for i in range(punten * 2):
        hoek = draai + math.pi * i / punten
        if i % 2 == 0:
            rr = R * (1.0 + (wiebel if (i // 2) % 2 == 0 else -wiebel))
        else:
            rr = r
        vs.append(bm.verts.new((x + rr * math.cos(hoek), y + rr * math.sin(hoek), z)))
    f = bm.faces.new(vs)
    ex = bmesh.ops.extrude_face_region(bm, geom=[f])
    for v in ex["geom"]:
        if isinstance(v, bmesh.types.BMVert):
            v.co.z += dik
    bm.to_mesh(me)
    bm.free()
    o = bpy.data.objects.new(naam, me)
    bpy.context.scene.collection.objects.link(o)
    mod = o.modifiers.new("rond", "BEVEL")
    mod.width = rand
    mod.segments = 4
    mod.limit_method = "ANGLE"
    o.data.materials.append(m)
    for p in o.data.polygons:
        p.use_smooth = True
    return o


def bol(naam, straal, x, y, z, m):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=straal, location=(x, y, z), segments=24, ring_count=12)
    o = bpy.context.object
    o.name = naam
    o.scale.z = 0.35
    o.data.materials.append(m)
    bpy.ops.object.shade_smooth()
    return o


def vonk(naam, x, y, maat, mats, draai=0.0):
    """Klein vierpuntig glimsterretje met donkere rand."""
    ster(naam + "_rand", 4, maat * 1.0 + 0.07, maat * 0.42 + 0.06, 0.0, 0.04, mats["donker"], draai, x=x, y=y, rand=0.015)
    ster(naam, 4, maat, maat * 0.34, 0.05, 0.05, mats["geel"], draai, x=x, y=y, rand=0.015)
    ster(naam + "_hart", 4, maat * 0.5, maat * 0.2, 0.1, 0.04, mats["wit"], draai, x=x, y=y, rand=0.01)


def bouw(beeld, mats):
    D = 0.09   # dikte van de donkere rand (in eenheden; 0,45 spelpixel = ±1,4 px op 120)
    if beeld == 0:
        # inslag: wit hart met korte dikke punten
        R, r = 0.62, 0.38
        ster("rand", 8, R + D, r + D * 0.9, 0.0, 0.05, mats["donker"], 0.2, 0.08)
        ster("lijf", 8, R, r, 0.06, 0.06, mats["geel"], 0.2, 0.08)
        bol("hart", 0.38, 0, 0, 0.16, mats["wit"])
    elif beeld == 1:
        R, r = 1.05, 0.50
        ster("rand", 8, R + D, r + D * 0.9, 0.0, 0.05, mats["donker"], 0.2, 0.12)
        ster("lijf", 8, R, r, 0.06, 0.06, mats["oranje"], 0.2, 0.12)
        ster("binnen", 8, R * 0.74, r * 0.78, 0.12, 0.05, mats["geel"], 0.2, 0.12)
        ster("licht", 8, R * 0.46, r * 0.62, 0.18, 0.04, mats["lichtgeel"], 0.2, 0.12)
        bol("hart", 0.30, 0, 0, 0.24, mats["wit"])
    elif beeld == 2:
        R, r = 1.25, 0.44
        ster("rand", 8, R + D, r + D * 0.9, 0.0, 0.05, mats["donker"], 0.2, 0.12)
        ster("lijf", 8, R, r, 0.06, 0.06, mats["oranje"], 0.2, 0.12)
        ster("binnen", 8, R * 0.72, r * 0.72, 0.12, 0.05, mats["geel"], 0.2, 0.12)
        bol("hart", 0.18, 0, 0, 0.2, mats["wit"])
        for i in range(4):
            h = math.pi / 4 + i * math.pi / 2 + 0.2
            vonk(f"v{i}", 1.25 * math.cos(h), 1.25 * math.sin(h), 0.17, mats, h)
    else:
        for i in range(6):
            h = i * math.pi / 3 + 0.5
            afst = 1.3 if i % 2 == 0 else 1.05
            maat = 0.21 if i % 2 == 0 else 0.16
            vonk(f"v{i}", afst * math.cos(h), afst * math.sin(h), maat, mats, h)


def render_beeld(beeld, pad, px, samples):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    mats = {"donker": mat("donker", DONKER, 0.0), "oranje": mat("oranje", ORANJE), "geel": mat("geel", GEEL),
            "lichtgeel": mat("lichtgeel", LICHTGEEL), "wit": mat("wit", WIT, 1.0)}
    mats["donker"].node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.7
    bouw(beeld, mats)
    cam = bpy.data.cameras.new("cam")
    cam.type = "ORTHO"
    cam.ortho_scale = EENHEID
    co = bpy.data.objects.new("cam", cam)
    co.location = (0, 0, 5)
    sc.collection.objects.link(co)
    sc.camera = co
    for naam, loc, e, kleur in (("sleutel", (-2.5, 3, 5), 500, (1, 0.95, 0.85)), ("vul", (3, -2, 4), 120, (1, 0.9, 0.8))):
        l = bpy.data.lights.new(naam, "AREA")
        l.size = 3
        l.energy = e
        l.color = kleur
        o = bpy.data.objects.new(naam, l)
        o.location = loc
        sc.collection.objects.link(o)
        doel = bpy.data.objects.new("doel_" + naam, None)
        sc.collection.objects.link(doel)
        con = o.constraints.new("TRACK_TO")
        con.target = doel
    w = bpy.data.worlds.new("w")
    sc.world = w
    w.use_nodes = True
    w.node_tree.nodes["Background"].inputs[0].default_value = (0.5, 0.42, 0.35, 1)
    w.node_tree.nodes["Background"].inputs[1].default_value = 0.5
    sc.render.engine = "CYCLES"
    sc.cycles.samples = samples
    sc.cycles.device = "CPU"
    sc.render.film_transparent = True
    sc.render.resolution_x = sc.render.resolution_y = CEL * px * 2   # twee keer groter, dan verkleinen
    sc.view_settings.view_transform = "Standard"
    sc.render.filepath = pad
    bpy.ops.render.render(write_still=True)


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]
    uit, px, samples = argv[0], int(argv[1]), int(argv[2])
    from PIL import Image
    tmp = tempfile.mkdtemp()
    cel = CEL * px
    blad = Image.new("RGBA", (cel * 4, cel), (0, 0, 0, 0))
    for b in range(4):
        p = os.path.join(tmp, f"k{b}.png")
        render_beeld(b, p, px, samples)
        im = Image.open(p).convert("RGBA")
        # verkleinen op voorvermenigvuldigde alfa (geen donkere randjes), zoals pijplijn/render.py
        im = im.convert("RGBa").resize((cel, cel), Image.LANCZOS).convert("RGBA")
        blad.paste(im, (b * cel, 0))
    blad.save(uit, optimize=True)
    print("klapster:", uit, blad.size)
