"""Bord rechts in de strook als planken bord in de aarde (Mila, 26 nov 2026, issue #197).
Vervangt het krijtbord (krijtbord.py, groen lei in een honingkleurige lijst met koperen hoeken). Iris (3fddb22 en
bb298d3): "bord leest als los venster", het grootste vlak dat niet bij het hol hoort. Rusty's Retirement heeft geen
los paneel: alles zit in de wereld.

Wat: horizontale planken in de kleuren van het hout in het hol (kamerhout 6e4632 en de donkere stut 34180e uit
hol.py), met donkere voegen ertussen, in een lijst van ruwe donkere balken zoals de stutten, vier ijzeren spijkers in
de hoeken en aarde die onderaan tegen het bord ligt. Geen goud en geen koper meer in de lijst: het goud zit alleen nog
in het muntje en het getal. De crème tekst (f3e2c0) blijft licht op donker hout.

Zelfde 9-slice als krijtbord.py: vierkant, rand = 1/3 van de breedte (384 px, rand 128), zodat kern/tekst.gd alleen
de textuur hoeft te wisselen. Wat rekt (randstroken en midden) heeft alleen nerf, voegen en aarde in de rekrichting;
spijkers en de hoopjes aarde zitten helemaal in de hoekvakken en rekken nooit.

    <venv>/bin/python plankbord.py <uit.png> <px> <samples>
Bpy alleen, geen AI-beeld, geen gekocht pakket.
"""
import sys, math
import bpy

PLANK = ("4e3020", "45291b", "4b2e1f")   # kamerhout van het hol, per plank een tikje anders
PLANK_NERF = "33200f"
STUT = "3a2014"
STUT_NERF = "22120a"
VOEG = "2c180e"   # niet zwart: de voeg in het midden loopt tussen de regels, letters mogen hem raken
IJZER = "5a5650"
AARDE = "7e4a34"
AARDE_D = "4a281a"


def lin(hexk):
    return [(int(hexk[i:i + 2], 16) / 255) ** 2.2 for i in (0, 2, 4)]


def hout_mat(naam, licht, donker, richting, schaal=3.5, ruw=0.75):
    """Hout met nerf: banden die in de lengte van de balk lopen (richting = waar de banden over varieren)."""
    m = bpy.data.materials.new(naam)
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes["Principled BSDF"]
    b.inputs["Roughness"].default_value = ruw
    tc = nt.nodes.new("ShaderNodeTexCoord")
    golf = nt.nodes.new("ShaderNodeTexWave")
    golf.wave_type = "BANDS"
    golf.bands_direction = richting
    golf.inputs["Scale"].default_value = schaal
    golf.inputs["Distortion"].default_value = 2.5
    golf.inputs["Detail"].default_value = 2.0
    golf.inputs["Detail Scale"].default_value = 0.8
    nt.links.new(tc.outputs["Object"], golf.inputs["Vector"])
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].color = (*lin(donker), 1)
    ramp.color_ramp.elements[0].position = 0.1
    ramp.color_ramp.elements[1].color = (*lin(licht), 1)
    ramp.color_ramp.elements[1].position = 0.6
    nt.links.new(golf.outputs["Fac"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], b.inputs["Base Color"])
    return m


def aarde_mat():
    """Aarde met korrel in de breedte (rekt de onderste strook in x, dan wordt het een langere wal)."""
    m = bpy.data.materials.new("aarde")
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes["Principled BSDF"]
    b.inputs["Roughness"].default_value = 0.95
    tc = nt.nodes.new("ShaderNodeTexCoord")
    sch = nt.nodes.new("ShaderNodeMapping")
    sch.inputs["Scale"].default_value = (3.0, 12.0, 12.0)
    nt.links.new(tc.outputs["Object"], sch.inputs["Vector"])
    ruis = nt.nodes.new("ShaderNodeTexNoise")
    ruis.inputs["Scale"].default_value = 3.0
    ruis.inputs["Detail"].default_value = 4.0
    nt.links.new(sch.outputs["Vector"], ruis.inputs["Vector"])
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].color = (*lin(AARDE_D), 1)
    ramp.color_ramp.elements[0].position = 0.35
    ramp.color_ramp.elements[1].color = (*lin(AARDE), 1)
    ramp.color_ramp.elements[1].position = 0.65
    nt.links.new(ruis.outputs["Fac"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], b.inputs["Base Color"])
    return m


def mat(naam, hexk, rough=0.4, metaal=0.0):
    m = bpy.data.materials.new(naam)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*lin(hexk), 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metaal
    return m


def blok(naam, x0, y0, x1, y1, z, d, m, rond=0.03):
    bpy.ops.mesh.primitive_cube_add(size=1, location=((x0 + x1) / 2, (y0 + y1) / 2, z + d / 2))
    o = bpy.context.object
    o.name = naam
    o.scale = (x1 - x0, y1 - y0, d)
    bpy.ops.object.transform_apply(scale=True)
    mod = o.modifiers.new("rond", "BEVEL")
    mod.width = rond
    mod.segments = 4
    mod.limit_method = "NONE"
    o.data.materials.append(m)
    bpy.ops.object.shade_smooth()
    return o


def hoopje(naam, x, y, rx, ry, rz, m):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(x, y, 0.2), segments=24, ring_count=12)
    o = bpy.context.object
    o.name = naam
    o.scale = (rx, ry, rz)
    o.data.materials.append(m)
    bpy.ops.object.shade_smooth()
    return o


def bouw():
    H = 1.0
    B = 0.27           # balkbreedte (randvak is 0,667: de lijst is ±6 px op 120, zoals het krijtbord)
    blok("voeg", -H + 0.05, -H + 0.05, H - 0.05, H - 0.05, 0.0, 0.04, mat("voeg", VOEG, 0.9), 0.01)
    # planken: 4 brede rijen, alleen nerf in x, smalle voeg van 0,016 ertussen (±1 px op 120). Bij 4 valt er in het midden van de
    # 9-slice maar één voeg (precies tussen de twee regels tekst), niet drie
    hoog = (2 * H - 0.1) / 4
    for i in range(4):
        y0 = -H + 0.05 + i * hoog
        m = hout_mat(f"plank{i}", PLANK[i % 3], PLANK_NERF, "Y", schaal=6.0 + 1.5 * (i % 2))
        blok(f"plank{i}", -H + 0.05, y0 + 0.008, H - 0.05, y0 + hoog - 0.008, 0.04, 0.06 + 0.008 * (i % 2), m, 0.018)
    hx = hout_mat("stut_x", STUT, STUT_NERF, "Y", 7.0, 0.85)   # boven en onder: nerf loopt in x
    hy = hout_mat("stut_y", STUT, STUT_NERF, "X", 7.0, 0.85)   # links en rechts: nerf loopt in y
    blok("balk_boven", -H, H - B, H, H, 0.10, 0.14, hx, 0.045)
    blok("balk_onder", -H, -H, H, -H + B, 0.10, 0.14, hx, 0.045)
    blok("balk_links", -H, -H + B, -H + B, H - B, 0.10, 0.12, hy, 0.045)
    blok("balk_rechts", H - B, -H + B, H, H - B, 0.10, 0.12, hy, 0.045)
    ijzer = mat("ijzer", IJZER, 0.45, 0.85)
    for sx in (-1, 1):
        for sy in (-1, 1):
            x0, y0 = sx * (H - B / 2), sy * (H - B / 2)
            bpy.ops.mesh.primitive_cylinder_add(radius=0.062, depth=0.03, location=(x0, y0, 0.255), vertices=20)
            o = bpy.context.object
            o.name = f"spijker{sx}{sy}"
            mod = o.modifiers.new("rond", "BEVEL")
            mod.width = 0.012
            mod.segments = 3
            o.data.materials.append(ijzer)
            bpy.ops.object.shade_smooth()
    # aarde onderaan: een lage wal over de hele onderbalk (rekt in x) en een hoopje in elke onderhoek (rekt nooit)
    am = aarde_mat()
    blok("wal", -H, -H, H, -H + 0.15, 0.20, 0.10, am, 0.06)
    for sx in (-1, 1):
        hoopje(f"hoop{sx}", sx * (H - 0.22), -H + 0.02, 0.30, 0.24, 0.22, am)
        hoopje(f"hoop_klein{sx}", sx * (H - 0.50), -H + 0.01, 0.14, 0.17, 0.2, am)


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]
    uit, PX, SAMPLES = argv[0], int(argv[1]), int(argv[2])
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bouw()
    cam = bpy.data.cameras.new("cam")
    cam.type = "ORTHO"
    cam.ortho_scale = 2.0
    co = bpy.data.objects.new("cam", cam)
    co.location = (0, 0, 5)
    sc.collection.objects.link(co)
    sc.camera = co
    # warm licht van linksboven (de fakkel en de schat staan links van het bord), zacht vullicht
    for naam, loc, e, kleur in (("sleutel", (-3, 3, 5), 600, (1, 0.82, 0.6)), ("vul", (3, -2, 5), 180, (1, 0.85, 0.75))):
        l = bpy.data.lights.new(naam, "AREA")
        l.size = 4
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
    w.node_tree.nodes["Background"].inputs[1].default_value = 0.6
    sc.render.engine = "CYCLES"
    sc.cycles.samples = SAMPLES
    sc.cycles.device = "CPU"
    sc.render.film_transparent = True
    sc.render.resolution_x = sc.render.resolution_y = PX
    sc.view_settings.view_transform = "Standard"
    sc.render.filepath = uit
    bpy.ops.render.render(write_still=True)
