"""Gloop is klaar: een rustige ring van licht om zijn voet (Mila, 25 nov 2026, issue #62).

Waarom: de regel "Big Gloop ready: click Gloop" gaat van het bord (Iris: tekst 6, aandacht 6; Thijs wil rustig).
Gloop laat het nu zelf zien: een ring van licht die op de vloer om hem heen ligt, licht mintgroen met een wit
hart, de kleur van Gloop zelf. Mint op de roodbruine aarde is het grootste kleurverschil dat we hebben, en de
goudschat achter hem blijft goud (een gouden ring viel daar weg). Vier lichtpareltjes op de ring zodat hij ook
op 96 px als ring leest en niet als een vlek.

Eén beeld, cel 36 x 12 spelpixels, midden van de ring = midden van de cel = de voet van Gloop (x 0, y 0).
Godot tekent de bovenste helft (achterkant van de ring) vóór Gloop en de onderste helft (voorkant) erna,
en laat de ring zacht ademen (licht en een tikje groter), geen knipperen.

    <venv>/bin/python gloopring.py <uit.png> <px_per_spelpixel> <samples>
Bpy alleen, geen AI-beeld, geen gekocht pakket.
"""
import sys, os, math, tempfile
import bpy

CEL_W, CEL_H = 36, 12   # spelpixels
EENHEID = 5.0           # spelpixels per Blender-eenheid (zoals de klap-ster)
HOEK = 17.0             # graden waarmee de camera op de vloer kijkt: ring wordt een platte ellips
R = 2.4                 # straal van de ring in eenheden (±24 spelpixels breed, Gloop is ±21): de zijkanten steken uit
BUIS = 0.11             # dikte van de lichtbuis


def lin(hexk):
    c = [int(hexk[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [x ** 2.2 for x in c]


def gloei_mat(naam, hexk, sterkte):
    m = bpy.data.materials.new(naam)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    uit = nt.nodes.new("ShaderNodeOutputMaterial")
    em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value = (*lin(hexk), 1)
    em.inputs["Strength"].default_value = sterkte
    nt.links.new(em.outputs[0], uit.inputs[0])
    return m


def waas_mat():
    """Zachte gloed op de vloer: licht dat op de ring het sterkst is en naar binnen en buiten wegloopt.
    Alfa komt uit dezelfde verloop, zodat het op elke ondergrond als licht leest en nooit als een plaatje."""
    m = bpy.data.materials.new("waas")
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    uit = nt.nodes.new("ShaderNodeOutputMaterial")
    tc = nt.nodes.new("ShaderNodeTexCoord")
    # afstand tot het midden in het vlak (objectcoördinaten, vlak heeft maat 1 = 1 eenheid)
    afst = nt.nodes.new("ShaderNodeVectorMath"); afst.operation = "LENGTH"
    nt.links.new(tc.outputs["Object"], afst.inputs[0])
    # |afstand - R|
    min_r = nt.nodes.new("ShaderNodeMath"); min_r.operation = "SUBTRACT"; min_r.inputs[1].default_value = R
    nt.links.new(afst.outputs["Value"], min_r.inputs[0])
    absw = nt.nodes.new("ShaderNodeMath"); absw.operation = "ABSOLUTE"
    nt.links.new(min_r.outputs[0], absw.inputs[0])
    # breedte van de gloed: binnen iets breder dan buiten zou mooi zijn, maar één maat leest rustiger
    deel = nt.nodes.new("ShaderNodeMath"); deel.operation = "DIVIDE"; deel.inputs[1].default_value = 0.42
    nt.links.new(absw.outputs[0], deel.inputs[0])
    kw = nt.nodes.new("ShaderNodeMath"); kw.operation = "POWER"; kw.inputs[1].default_value = 2.0
    nt.links.new(deel.outputs[0], kw.inputs[0])
    neg = nt.nodes.new("ShaderNodeMath"); neg.operation = "MULTIPLY"; neg.inputs[1].default_value = -1.0
    nt.links.new(kw.outputs[0], neg.inputs[0])
    ex = nt.nodes.new("ShaderNodeMath"); ex.operation = "EXPONENT"
    nt.links.new(neg.outputs[0], ex.inputs[0])
    sterk = nt.nodes.new("ShaderNodeMath"); sterk.operation = "MULTIPLY"; sterk.inputs[1].default_value = 0.6
    nt.links.new(ex.outputs[0], sterk.inputs[0])
    em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value = (*lin("8dffd9"), 1)
    em.inputs["Strength"].default_value = 1.6
    tr = nt.nodes.new("ShaderNodeBsdfTransparent")
    mix = nt.nodes.new("ShaderNodeMixShader")
    nt.links.new(sterk.outputs[0], mix.inputs[0])
    nt.links.new(tr.outputs[0], mix.inputs[1])
    nt.links.new(em.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], uit.inputs[0])
    return m


def bouw():
    # de lichtbuis: wit hart in een mint mantel
    bpy.ops.mesh.primitive_torus_add(major_radius=R, minor_radius=BUIS * 1.9, major_segments=128, minor_segments=16,
                                     location=(0, 0, BUIS))
    mantel = bpy.context.object; mantel.name = "mantel"
    bpy.ops.object.shade_smooth()
    mantel.data.materials.append(gloei_mat("mint", "5ef2c4", 2.2))
    bpy.ops.mesh.primitive_torus_add(major_radius=R, minor_radius=BUIS, major_segments=128, minor_segments=16,
                                     location=(0, 0, BUIS * 2.3))
    hart = bpy.context.object; hart.name = "hart"
    bpy.ops.object.shade_smooth()
    hart.data.materials.append(gloei_mat("wit", "f4fff9", 4.0))
    # gloed op de vloer
    bpy.ops.mesh.primitive_plane_add(size=2 * (R + 1.6), location=(0, 0, 0.005))
    waas = bpy.context.object; waas.name = "waas"
    waas.data.materials.append(waas_mat())
    # vier lichtpareltjes op de ring (links, rechts, voor en schuin achter): de ring leest als ring, ook klein
    parel = gloei_mat("parel", "ffffff", 6.0)
    for hoek in (0, 180, 250, 320):
        h = math.radians(hoek)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=BUIS * 2.3, location=(R * math.cos(h), R * math.sin(h), BUIS * 2.2),
                                             segments=16, ring_count=8)
        o = bpy.context.object; o.name = f"parel{hoek}"
        bpy.ops.object.shade_smooth()
        o.data.materials.append(parel)


def render(pad, px, samples):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bouw()
    cam = bpy.data.cameras.new("cam")
    cam.type = "ORTHO"
    cam.ortho_scale = CEL_W / EENHEID
    co = bpy.data.objects.new("cam", cam)
    h = math.radians(HOEK)
    afst = 20.0
    co.location = (0, -afst * math.cos(h), afst * math.sin(h))
    co.rotation_euler = (math.radians(90) - h, 0, 0)
    sc.collection.objects.link(co)
    sc.camera = co
    w = bpy.data.worlds.new("w"); sc.world = w
    w.use_nodes = True
    w.node_tree.nodes["Background"].inputs[1].default_value = 0.0
    sc.render.engine = "CYCLES"
    sc.cycles.samples = samples
    sc.cycles.device = "CPU"
    sc.render.film_transparent = True
    sc.render.resolution_x = CEL_W * px * 2   # twee keer groter, dan verkleinen
    sc.render.resolution_y = CEL_H * px * 2
    sc.view_settings.view_transform = "Standard"
    sc.render.filepath = pad
    bpy.ops.render.render(write_still=True)


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]
    uit, px, samples = argv[0], int(argv[1]), int(argv[2])
    from PIL import Image
    tmp = tempfile.mkdtemp()
    p = os.path.join(tmp, "ring.png")
    render(p, px, samples)
    im = Image.open(p).convert("RGBA")
    # verkleinen op voorvermenigvuldigde alfa (geen donkere randjes), zoals pijplijn/render.py
    im = im.convert("RGBa").resize((CEL_W * px, CEL_H * px), Image.LANCZOS).convert("RGBA")
    im.save(uit, optimize=True)
    print("gloopring:", uit, im.size)
