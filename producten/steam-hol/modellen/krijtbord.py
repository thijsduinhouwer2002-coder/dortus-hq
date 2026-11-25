"""Kader rechts in de strook als krijtbord in een houten lijst (Mila, 25 nov 2026, issue #43).
Vervangt kunst/paneel_3d.png (egaal bruin met goud). Iris (keuring 52aa730): het kader is het grootste vlak in beeld
en saai bruin. Rusty's Retirement en Spirit City zijn op ware maat fel en duidelijk.

Wat: een donkergroen leien bord (kleurverschil met de rode aarde, de crème en gouden tekst blijft goed leesbaar)
met vage krijtvegen, in een lijst van warm honingkleurig hout met nerf in de lengte van elke balk, en koperen
hoekbeslag met een klinknagel. Zelfde 9-slice als het oude paneel: vierkant, rand = 1/3 van de breedte
(bij 384 px dus 128 px), zodat kern/tekst.gd alleen de textuur hoeft te wisselen (BRON_RAND blijft 128).
Alles wat rekt (randstroken en midden) heeft alleen nerf of vegen in de rekrichting, dus uitrekken ziet er niet uit
als uitrekken. Het hoekbeslag zit helemaal in de hoekvakken en rekt nooit.

    <venv>/bin/python krijtbord.py <uit.png> <px> <samples>
Bpy alleen, geen AI-beeld, geen gekocht pakket.
"""
import sys, math
import bpy

HOUT = "c08040"
HOUT_DONKER = "93582a"
LEI = "26372f"
LEI_VEEG = "3d5048"
KOPER = "d99a3e"


def lin(hexk):
    return [(int(hexk[i:i + 2], 16) / 255) ** 2.2 for i in (0, 2, 4)]


def hout_mat(naam, richting):
    """Hout met nerf: banden die in de lengte van de balk lopen (richting 'X' of 'Y' = waar de banden over varieren)."""
    m = bpy.data.materials.new(naam)
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes["Principled BSDF"]
    b.inputs["Roughness"].default_value = 0.6
    tc = nt.nodes.new("ShaderNodeTexCoord")
    golf = nt.nodes.new("ShaderNodeTexWave")
    golf.wave_type = "BANDS"
    golf.bands_direction = richting
    golf.inputs["Scale"].default_value = 3.5
    golf.inputs["Distortion"].default_value = 6.0
    golf.inputs["Detail"].default_value = 1.5
    golf.inputs["Detail Scale"].default_value = 0.6
    nt.links.new(tc.outputs["Object"], golf.inputs["Vector"])
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].color = (*lin(HOUT_DONKER), 1)
    ramp.color_ramp.elements[0].position = 0.15
    ramp.color_ramp.elements[1].color = (*lin(HOUT), 1)
    ramp.color_ramp.elements[1].position = 0.75
    nt.links.new(golf.outputs["Fac"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], b.inputs["Base Color"])
    return m


def lei_mat():
    """Lei met vage, brede krijtvegen in de breedte (rekt het midden in x, dan worden het langere vegen)."""
    m = bpy.data.materials.new("lei")
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes["Principled BSDF"]
    b.inputs["Roughness"].default_value = 0.9
    tc = nt.nodes.new("ShaderNodeTexCoord")
    sch = nt.nodes.new("ShaderNodeMapping")
    sch.inputs["Scale"].default_value = (0.6, 2.2, 1.0)   # vegen lopen in x
    nt.links.new(tc.outputs["Object"], sch.inputs["Vector"])
    ruis = nt.nodes.new("ShaderNodeTexNoise")
    ruis.inputs["Scale"].default_value = 2.0
    ruis.inputs["Detail"].default_value = 2.0
    nt.links.new(sch.outputs["Vector"], ruis.inputs["Vector"])
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].color = (*lin(LEI), 1)
    ramp.color_ramp.elements[0].position = 0.5
    ramp.color_ramp.elements[1].color = (*lin(LEI_VEEG), 1)
    ramp.color_ramp.elements[1].position = 0.75
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
    mod.segments = 5
    mod.limit_method = "NONE"
    o.data.materials.append(m)
    bpy.ops.object.shade_smooth()
    return o


def bouw():
    B = 0.30           # balkbreedte (van de 2 eenheden; 1/3 van de breedte = 0,667 is het randvak)
    H = 1.0
    blok("lei", -H + 0.1, -H + 0.1, H - 0.1, H - 0.1, 0.0, 0.08, lei_mat(), 0.02)
    hx = hout_mat("hout_x", "Y")   # boven en onder: nerf loopt in x
    hy = hout_mat("hout_y", "X")   # links en rechts: nerf loopt in y
    blok("balk_boven", -H, H - B, H, H, 0.08, 0.16, hx)
    blok("balk_onder", -H, -H, H, -H + B, 0.08, 0.16, hx)
    blok("balk_links", -H, -H + B, -H + B, H - B, 0.08, 0.14, hy)
    blok("balk_rechts", H - B, -H + B, H, H - B, 0.08, 0.14, hy)
    koper = mat("koper", KOPER, 0.3, 0.8)
    nagel = mat("nagel", "f2d27a", 0.25, 0.9)
    L = 0.46           # beslag blijft binnen het hoekvak van 0,667
    for sx in (-1, 1):
        for sy in (-1, 1):
            x0, y0 = sx * H, sy * H
            # L-vormig beslag: twee platte strips over de hoek
            blok(f"beslag_a{sx}{sy}", min(x0, x0 - sx * L), min(y0, y0 - sy * 0.22), max(x0, x0 - sx * L), max(y0, y0 - sy * 0.22), 0.24, 0.04, koper, 0.025)
            blok(f"beslag_b{sx}{sy}", min(x0, x0 - sx * 0.22), min(y0, y0 - sy * L), max(x0, x0 - sx * 0.22), max(y0, y0 - sy * L), 0.245, 0.04, koper, 0.025)
            bpy.ops.mesh.primitive_uv_sphere_add(radius=0.055, location=(x0 - sx * 0.11, y0 - sy * 0.11, 0.28), segments=20, ring_count=10)
            o = bpy.context.object
            o.scale.z = 0.5
            o.data.materials.append(nagel)
            bpy.ops.object.shade_smooth()


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
    for naam, loc, e, kleur in (("sleutel", (-3, 3, 6), 700, (1, 0.88, 0.7)), ("vul", (3, -2, 5), 160, (1, 0.85, 0.75))):
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
