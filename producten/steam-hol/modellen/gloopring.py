"""Gloop is klaar: een rustige ring van licht om zijn voet (Mila, 25 nov 2026, issue #62).

Waarom: de regel "Big Gloop ready: click Gloop" gaat van het bord (Iris: tekst 6, aandacht 6; Thijs wil rustig).
Gloop laat het nu zelf zien: een ring van licht die op de vloer om hem heen ligt, licht mintgroen met een wit
hart, de kleur van Gloop zelf. Mint op de roodbruine aarde is het grootste kleurverschil dat we hebben, en de
goudschat achter hem blijft goud (een gouden ring viel daar weg). Vier lichtpareltjes op de ring zodat hij ook
op 96 px als ring leest en niet als een vlek.

Eén beeld, cel 36 x 12 spelpixels, midden van de ring = midden van de cel = de voet van Gloop (x 0, y 0).
Godot tekent de bovenste helft (achterkant van de ring) vóór Gloop en de onderste helft (voorkant) erna,
en laat de ring zacht ademen (licht en een tikje groter), geen knipperen.

Sinds Iris (keuring e39939e, "bijzonder, niet dat je hem kunt kopen") staat er een gouden munt op de ring, links
vooraan: in het hol betekent een munt "dit kun je kopen". Eigen blad gloopmunt.png naast de ring, zodat hij groter mag
zijn dan de onderste helft van de ring en toch helemaal vóór Gloop staat.

    <venv>/bin/python gloopring.py <uit.png> <px_per_spelpixel> <samples>   (maakt ook gloopmunt.png ernaast)
Bpy alleen, geen AI-beeld, geen gekocht pakket.
"""
import sys, os, math, tempfile
import bpy

CEL_W, CEL_H = 36, 12   # spelpixels
EENHEID = 5.0           # spelpixels per Blender-eenheid (zoals de klap-ster)
HOEK = 17.0             # graden waarmee de camera op de vloer kijkt: ring wordt een platte ellips
R = 2.4                 # straal van de ring in eenheden (±24 spelpixels breed, Gloop is ±21): de zijkanten steken uit
BUIS = 0.11             # dikte van de lichtbuis
MUNT_R = 0.56           # straal van de munt: ±14 schermpixels op strook 120, zo groot als de munt op het bord
MUNT_HOEK = 236.0       # plek op de ring: voor en links, naast zijn mond (nooit ervoor) en ver van de goudschat rechts
MUNT_CEL = 8            # spelpixels: eigen blad gloopmunt.png, vierkant, midden van de cel = midden van de munt


def munt_plek():
    h = math.radians(MUNT_HOEK)
    return (R + 0.1) * math.cos(h), (R + 0.1) * math.sin(h), MUNT_R + 0.01


def munt_op_scherm():
    """Midden van de munt in spelpixels ten opzichte van het midden van de ring (x naar rechts, y naar beneden)."""
    x, y, z = munt_plek()
    h = math.radians(HOEK)
    return x * EENHEID, -(y * math.sin(h) + z * math.cos(h)) * EENHEID


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
    for hoek in (0, 180, 215, 325):
        h = math.radians(hoek)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=BUIS * 2.3, location=(R * math.cos(h), R * math.sin(h), BUIS * 2.2),
                                             segments=16, ring_count=8)
        o = bpy.context.object; o.name = f"parel{hoek}"
        bpy.ops.object.shade_smooth()
        o.data.materials.append(parel)


def munt():
    """Een gouden munt die rechtop vooraan op de ring staat (Iris, keuring e39939e: "je ziet dat Gloop iets bijzonders
    heeft, niet dat je hem kunt kopen"). In het hol betekent een munt: dit kun je kopen (het muntje boven een put).
    Zo zegt de ring nu ook zonder tekst: Gloop kun je kopen. Goud met een lichte rand en een dieper midden, zoals de
    munt op het bord; hij gloeit zelf, dus hij leest op de donkere voet net zo goed als op de aarde."""
    x, y, z = munt_plek()
    straal = MUNT_R
    kant = math.radians(90) - math.radians(HOEK)   # recht naar de camera gedraaid
    bpy.ops.mesh.primitive_cylinder_add(radius=straal, depth=0.14, vertices=48, location=(x, y, z),
                                        rotation=(kant, 0, 0))
    rand = bpy.context.object; rand.name = "muntrand"
    bpy.ops.object.shade_smooth()
    rand.data.materials.append(gloei_mat("muntrand", "ffe27a", 2.4))
    bpy.ops.mesh.primitive_cylinder_add(radius=straal * 0.72, depth=0.16, vertices=48, location=(x, y, z),
                                        rotation=(kant, 0, 0))
    hart = bpy.context.object; hart.name = "munthart"
    bpy.ops.object.shade_smooth()
    hart.data.materials.append(gloei_mat("munthart", "e8a51c", 1.6))
    # klein lichtje linksboven op de munt, zoals een glans
    dx, dz = -straal * 0.32, straal * 0.32
    voor = 0.1
    bpy.ops.mesh.primitive_uv_sphere_add(radius=straal * 0.16, segments=12, ring_count=6,
                                         location=(x + dx, y - voor * math.cos(math.radians(HOEK)), z + dz))
    glans = bpy.context.object; glans.name = "muntglans"
    glans.data.materials.append(gloei_mat("muntglans", "fffbe6", 3.5))


def render(pad, px, samples, deel="ring"):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    cam = bpy.data.cameras.new("cam")
    cam.type = "ORTHO"
    if deel == "munt":
        munt()
        mx, my, mz = munt_plek()
        cel_w = cel_h = MUNT_CEL
    else:
        bouw()
        mx = my = mz = 0.0
        cel_w, cel_h = CEL_W, CEL_H
    cam.ortho_scale = cel_w / EENHEID
    co = bpy.data.objects.new("cam", cam)
    h = math.radians(HOEK)
    afst = 20.0
    co.location = (mx, my - afst * math.cos(h), mz + afst * math.sin(h))
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
    sc.render.resolution_x = cel_w * px * 2   # twee keer groter, dan verkleinen
    sc.render.resolution_y = cel_h * px * 2
    sc.view_settings.view_transform = "Standard"
    sc.render.filepath = pad
    bpy.ops.render.render(write_still=True)


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]
    uit, px, samples = argv[0], int(argv[1]), int(argv[2])
    from PIL import Image
    tmp = tempfile.mkdtemp()
    # twee bladen: de ring (uit) en de munt (gloopmunt.png ernaast)
    for deel, pad, maat in (("ring", uit, (CEL_W, CEL_H)),
                            ("munt", os.path.join(os.path.dirname(uit) or ".", "gloopmunt.png"), (MUNT_CEL, MUNT_CEL))):
        p = os.path.join(tmp, deel + ".png")
        render(p, px, samples, deel)
        im = Image.open(p).convert("RGBA")
        # verkleinen op voorvermenigvuldigde alfa (geen donkere randjes), zoals pijplijn/render.py
        im = im.convert("RGBa").resize((maat[0] * px, maat[1] * px), Image.LANCZOS).convert("RGBA")
        im.save(pad, optimize=True)
        print("gloopring:", pad, im.size)
    print("munt midden (spelpixels vanaf het midden van de ring): %.2f, %.2f" % munt_op_scherm())
