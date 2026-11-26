"""Dichte put als luik van hout met een donkere rand (Mila, 26 nov 2026, issue #209).

Waarom: Iris (keuring bb298d3 punt 1): van 800 tot 1200 s was een dichte put onzichtbaar, alleen een donker streepje
en de gouden ruit. Je zag niet waar je val stond en wat je kocht. Bij Rusty's Retirement zie je alles wat je neerzette
op 1x. Nu ligt op elke dichte put een luik: lichter honinghout dan de bruine gangvloer, met een zwarte rand (de put
eronder), twee ijzeren banden en een ring vooraan. Klapt de put, dan is het luik weg en zie je de stekels zoals altijd.

Vier beelden naast elkaar, één per stap van de put, zodat je ook ziet wat je kocht:
  0  Spike Pit: honinghout, donkere ijzeren banden.
  1  Rusty Spikes: roestige banden, en achter het luik steken drie roestige stekelpunten uit de kier.
  2  Deep Pit: dikkere zwarte rand en vier lange stalen punten achter het luik.
  3  Trick Lid: luik met aarde en een plukje gras erop (vermomd als vloer), koperen scharnieren.
Stap 4 tot 6 houden beeld 3; de gouden ruiten (#162) liggen er bovenop.

Cel 18 x 10 spelpixels per beeld, midden van de cel = midden van het luik op de vloer (Godot: kolom midden, y 37).
Camera kijkt 26 graden schuin op de vloer: het luik is plat en ±5 spelpixels hoog op het scherm (15 px op 120).

    <venv>/bin/python luik.py <uit.png> <px_per_spelpixel> <samples>
Bpy alleen, geen AI-beeld, geen gekocht pakket.
"""
import sys, os, math, tempfile
import bpy

CEL_W, CEL_H = 18, 10    # spelpixels per beeld
BEELDEN = 4
HOEK = 26.0              # graden: camera kijkt schuin op de vloer
MIDDEN_Z = 1.2           # hoogte van het cel-midden boven de vloer (spelpixels), het luik ligt mooi in het midden

HOUT = ("c48a4a", "b47a3c", "c99352", "b98040")   # honinghout, lichter dan de gangvloer (±7a4630): het luik springt eruit
HOUT_NERF = "7a4a22"
RAND = "160b07"
IJZER = "3b3632"
ROEST = ("b4521e", "7c3214")
STAAL = "c9ccd2"
KOPER = "c7843a"
AARDE = ("6e4030", "4c2a1e")
GRAS = "5aa83c"


def lin(hexk):
    return [(int(hexk[i:i + 2], 16) / 255) ** 2.2 for i in (0, 2, 4)]


def mat(naam, hexk, rough=0.5, metaal=0.0):
    m = bpy.data.materials.new(naam)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*lin(hexk), 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metaal
    return m


def hout_mat(naam, licht, donker):
    """Hout met nerf in de lengte van de plank (y, van voor naar achter)."""
    m = bpy.data.materials.new(naam)
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes["Principled BSDF"]
    b.inputs["Roughness"].default_value = 0.7
    tc = nt.nodes.new("ShaderNodeTexCoord")
    golf = nt.nodes.new("ShaderNodeTexWave")
    golf.wave_type = "BANDS"
    golf.bands_direction = "X"
    golf.inputs["Scale"].default_value = 1.6
    golf.inputs["Distortion"].default_value = 3.0
    golf.inputs["Detail"].default_value = 2.0
    nt.links.new(tc.outputs["Object"], golf.inputs["Vector"])
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].color = (*lin(donker), 1)
    ramp.color_ramp.elements[0].position = 0.05
    ramp.color_ramp.elements[1].color = (*lin(licht), 1)
    ramp.color_ramp.elements[1].position = 0.45
    nt.links.new(golf.outputs["Fac"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], b.inputs["Base Color"])
    return m


def blok(naam, x0, y0, x1, y1, z0, z1, m, rond=0.15):
    bpy.ops.mesh.primitive_cube_add(size=1, location=((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2))
    o = bpy.context.object
    o.name = naam
    o.scale = (x1 - x0, y1 - y0, z1 - z0)
    bpy.ops.object.transform_apply(scale=True)
    if rond > 0:
        mod = o.modifiers.new("rond", "BEVEL")
        mod.width = rond
        mod.segments = 3
        mod.limit_method = "NONE"
    o.data.materials.append(m)
    bpy.ops.object.shade_smooth()
    return o


def punt(naam, x, y, hoog, r, m):
    bpy.ops.mesh.primitive_cone_add(radius1=r, radius2=0.0, depth=hoog, vertices=12, location=(x, y, hoog / 2 - 0.3))
    o = bpy.context.object
    o.name = naam
    o.data.materials.append(m)
    bpy.ops.object.shade_smooth()
    return o


def bol(naam, x, y, z, rx, ry, rz, m):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(x, y, z), segments=16, ring_count=8)
    o = bpy.context.object
    o.name = naam
    o.scale = (rx, ry, rz)
    o.data.materials.append(m)
    bpy.ops.object.shade_smooth()
    return o


def bouw(stap):
    BW, BD = 7.4, 5.3          # halve buitenmaat van de rand (x) en diepte (y): 15,2 breed, net binnen de kolom van 16
    LW, LD = 6.4, 4.4          # halve maat van het luik
    rand_hoog = 0.9 if stap == 2 else 0.55
    if stap == 2:
        BW, BD = 7.8, 5.8
    # zwarte rand: de put onder het luik, iets boven de vloer zodat de voorkant als donkere streep leest
    blok("rand", -BW, -BD, BW, BD, -0.1, rand_hoog, mat("rand", RAND, 0.8), 0.25)
    # planken in de lengte (van voor naar achter): op het scherm staande voegen, die lees je ook op 1x
    n = 4
    pb = 2 * LW / n
    for i in range(n):
        x0 = -LW + i * pb
        m = hout_mat(f"plank{i}", HOUT[i % len(HOUT)], HOUT_NERF)
        blok(f"plank{i}", x0 + 0.09, -LD, x0 + pb - 0.09, LD, rand_hoog, rand_hoog + 0.55 + 0.04 * (i % 2), m, 0.14)
    top = rand_hoog + 0.6
    # twee banden over de planken, voor en achter
    if stap == 1:
        band = mat("roest", ROEST[0], 0.85, 0.3)
    elif stap == 3:
        band = None
    else:
        band = mat("ijzer", IJZER, 0.45, 0.8)
    if band is not None:
        for j, y in enumerate((-LD + 1.0, LD - 1.0)):
            blok(f"band{j}", -LW - 0.15, y - 0.45, LW + 0.15, y + 0.45, top - 0.1, top + 0.18, band, 0.1)
            for sx in (-1, 1):
                bol(f"nagel{j}{sx}", sx * (LW - 0.9), y, top + 0.2, 0.28, 0.28, 0.18,
                    mat(f"nagelm{j}{sx}", ROEST[1] if stap == 1 else "5a5550", 0.5, 0.8))
    # ring vooraan om het luik op te tillen
    rm = mat("ringm", KOPER if stap == 3 else (ROEST[1] if stap == 1 else IJZER), 0.4, 0.9)
    bpy.ops.mesh.primitive_torus_add(major_radius=0.75, minor_radius=0.2, location=(0, -LD + 0.3, top + 0.55),
                                     rotation=(math.radians(90 - HOEK), 0, 0))
    o = bpy.context.object
    o.name = "ring"
    o.data.materials.append(rm)
    bpy.ops.object.shade_smooth()
    # stekelpunten achter het luik, uit de kier tussen luik en rand (stap 1 roest, stap 2 lang staal)
    if stap == 1:
        pm = mat("roestpunt", "c4662a", 0.6, 0.6)
        for i, x in enumerate((-4.0, 0.0, 4.0)):
            punt(f"punt{i}", x, LD + 0.6, top + 2.0, 0.7, pm)
    elif stap == 2:
        pm = mat("staalpunt", STAAL, 0.25, 1.0)
        for i, x in enumerate((-5.1, -1.7, 1.7, 5.1)):
            punt(f"punt{i}", x, LD + 0.7, top + 3.0, 0.75, pm)
    # Trick Lid: koperen scharnieren achteraan, aarde en een plukje gras erop (vermomd als vloer)
    if stap == 3:
        km = mat("koper", KOPER, 0.35, 0.95)
        for sx in (-1, 1):
            blok(f"scharnier{sx}", sx * 3.2 - 0.9, LD - 1.2, sx * 3.2 + 0.9, LD - 0.2, top - 0.1, top + 0.2, km, 0.08)
        am = mat("aarde", AARDE[0], 0.95)
        ad = mat("aarde_d", AARDE[1], 0.95)
        for i, (x, y, r) in enumerate(((-4.2, 0.6, 1.3), (-2.6, -1.4, 0.8), (3.6, 1.0, 1.1), (1.4, -0.4, 0.6))):
            bol(f"aarde{i}", x, y, top, r, r * 0.9, 0.35, am if i % 2 == 0 else ad)
        gm = mat("gras", GRAS, 0.7)
        for i, (dx, h, kant) in enumerate(((-0.45, 2.2, -22), (0.0, 2.9, 4), (0.45, 2.3, 26))):
            bpy.ops.mesh.primitive_cone_add(radius1=0.32, radius2=0.0, depth=h, vertices=8,
                                            location=(-4.2 + dx, 0.6, top + h / 2), rotation=(0, math.radians(kant), 0))
            g = bpy.context.object
            g.name = f"gras{i}"
            g.data.materials.append(gm)


def render(pad, stap, px, samples):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bouw(stap)
    cam = bpy.data.cameras.new("cam")
    cam.type = "ORTHO"
    cam.ortho_scale = CEL_W
    co = bpy.data.objects.new("cam", cam)
    h = math.radians(HOEK)
    afst = 60.0
    co.location = (0, -afst * math.cos(h), MIDDEN_Z + afst * math.sin(h))
    co.rotation_euler = (math.radians(90) - h, 0, 0)
    sc.collection.objects.link(co)
    sc.camera = co
    # warm sleutellicht van linksvoor boven (de fakkel), zacht vullicht van rechts
    for naam, loc, e, kleur in (("sleutel", (-14, -16, 22), 9000, (1, 0.86, 0.66)),
                                ("vul", (16, -10, 12), 2600, (1, 0.9, 0.8))):
        l = bpy.data.lights.new(naam, "AREA")
        l.size = 10
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
    w.node_tree.nodes["Background"].inputs[0].default_value = (0.36, 0.27, 0.2, 1)
    w.node_tree.nodes["Background"].inputs[1].default_value = 0.5
    sc.render.engine = "CYCLES"
    sc.cycles.samples = samples
    sc.cycles.device = "CPU"
    sc.render.film_transparent = True
    sc.render.resolution_x = CEL_W * px * 2
    sc.render.resolution_y = CEL_H * px * 2
    sc.view_settings.view_transform = "Standard"
    sc.render.filepath = pad
    bpy.ops.render.render(write_still=True)


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]
    uit, px, samples = argv[0], int(argv[1]), int(argv[2])
    from PIL import Image
    tmp = tempfile.mkdtemp()
    blad = Image.new("RGBA", (CEL_W * px * BEELDEN, CEL_H * px), (0, 0, 0, 0))
    for stap in range(BEELDEN):
        p = os.path.join(tmp, f"luik{stap}.png")
        render(p, stap, px, samples)
        im = Image.open(p).convert("RGBA")
        # verkleinen op voorvermenigvuldigde alfa (geen donkere randjes), zoals pijplijn/render.py
        im = im.convert("RGBa").resize((CEL_W * px, CEL_H * px), Image.LANCZOS).convert("RGBA")
        blad.paste(im, (stap * CEL_W * px, 0))
    blad.save(uit, optimize=True)
    print("luik:", uit, blad.size)
