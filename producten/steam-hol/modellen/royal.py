"""Royal-stukken van Gloop in 3D (Daan, 14 nov 2026), voor gloop.py stand cape, zoom en ster.

Vervangt de laatste pixels op Gloop zelf (slijm_upgrades2.png): cel 1 cape, cel 2 bovenzoom met gesp,
cel 0 glansster. Elk stuk rendert los, met de camera van stand rust (hoeden 0):
  cape  achter het lijf, op de vloer; links en rechts steekt hij uit. Lijf en gezicht niet in de render
        (slijm.gd tekent het lijf eroverheen), wel de contactschaduw op de vloer.
  zoom  gouden gesp met robijn linksboven op zijn schouder, onderaan de hoge kraag (geen kraag: zie zoom()).
        Lijf en gezicht als holdout: ze snijden weg wat erachter valt maar zijn zelf doorzichtig.
  ster  glansster met vier punten op zijn rechterschouder, licht gevend in het mint van het lijf.
Kleuren uit gedeeld.KLEUR (paars en goud), dezelfde stof als de heksenhoed, zodat het één wereld blijft.
"""
import math
import bpy
import gedeeld as g

TOP = 1.52


def _weg(objecten, holdout=False):
    for o in objecten:
        if holdout:
            o.is_holdout = True
        else:
            o.hide_render = True


def _knip(o, x=(-5, 5), y=(-5, 5), z=(-5, 5)):
    """Houd alleen het deel van o binnen het blok (boolean intersect met een verborgen kubus)."""
    bpy.ops.mesh.primitive_cube_add(size=1, location=((x[0] + x[1]) / 2, (y[0] + y[1]) / 2, (z[0] + z[1]) / 2))
    k = bpy.context.object
    k.scale = (x[1] - x[0], y[1] - y[0], z[1] - z[0]); k.hide_render = True; k.hide_viewport = True
    m = o.modifiers.new("knip", "BOOLEAN"); m.object = k; m.operation = "INTERSECT"
    return o


def hermelijn():
    """Witte bontrand met zwarte stipjes: het bekendste teken voor koning (ronde 2, frisse kijkers lazen geen koning)."""
    m = bpy.data.materials.new("hermelijn"); m.use_nodes = True
    nt = m.node_tree; b = nt.nodes["Principled BSDF"]
    b.inputs["Roughness"].default_value = 0.9
    vo = nt.nodes.new("ShaderNodeTexVoronoi"); vo.inputs["Scale"].default_value = 9.0
    ra = nt.nodes.new("ShaderNodeValToRGB")
    ra.color_ramp.elements[0].position = 0.06; ra.color_ramp.elements[0].color = (0.02, 0.02, 0.025, 1)
    ra.color_ramp.elements[1].position = 0.08; ra.color_ramp.elements[1].color = (0.92, 0.9, 0.86, 1)
    ra.color_ramp.interpolation = "CONSTANT"
    nt.links.new(vo.outputs["Distance"], ra.inputs["Fac"]); nt.links.new(ra.outputs["Color"], b.inputs["Base Color"])
    return m


def cape(lijf_delen, vloer):
    """Open mantel achter hem (alleen de achterste helft), klokvormig, met plooien die naar onder dieper worden.
    Hij komt aan de zijkanten iets naar voren, zodat je naast het lijf de buitenkant ziet, met een gouden zoom op de vloer."""
    import bmesh
    _weg(lijf_delen)                       # het lijf tekent het spel er zelf overheen
    fluweel = g.mat("cape", "paars", rough=0.78, spec=0.25, sss=0.05)
    voering = g.mat("cape_voering", "3a2470", rough=0.85, spec=0.15)
    goud = g.mat("cape_goud", "goud", rough=0.22, spec=1.0, metaal=0.9, emis=0.08)
    BX, BY, BZ, CY, VOOR = 1.3, 0.92, 1.32, 0.2, -0.3
    bpy.ops.mesh.primitive_uv_sphere_add(segments=128, ring_count=48, location=(0, 0, 0))
    m = bpy.context.object; m.name = "cape"
    bm = bmesh.new(); bm.from_mesh(m.data)
    weg = [v for v in bm.verts if v.co.z < -0.001 or v.co.y * BY + CY < VOOR]
    bmesh.ops.delete(bm, geom=weg, context="VERTS")
    for v in bm.verts:
        x, y, z = v.co.x * BX, v.co.y * BY + CY, v.co.z * BZ
        hoek = math.atan2(x, y - CY)
        diep = 0.25 + 0.75 * (1 - z / BZ)           # boven glad, onder diepe plooien
        r = 1 + 0.045 * diep * math.sin(11 * hoek)
        v.co = ((x) * r * (1 + 0.08 * (1 - z / BZ)), CY + (y - CY) * r, z)   # onderaan iets wijder: klok
    bm.to_mesh(m.data); bm.free()
    bpy.ops.object.shade_smooth()
    m.data.materials.append(fluweel); m.data.materials.append(voering)
    sol = m.modifiers.new("dik", "SOLIDIFY"); sol.thickness = 0.05; sol.material_offset = 1
    sub = m.modifiers.new("glad", "SUBSURF"); sub.levels = 1; sub.render_levels = 1
    # hoge kraag achter zijn kruin (Daan 07:50, frisse kijker: de koepel las niet als mantel): een open kelk
    # die naar boven uitwaaiert, met gouden rand. Zo valt de mantel zichtbaar van zijn schouders.
    bpy.ops.mesh.primitive_cone_add(vertices=96, radius1=0.42, radius2=0.74, depth=0.42, end_fill_type="NOTHING",
                                    location=(0.04, 0.2, 1.18), rotation=(math.radians(14), 0, 0))
    k = bpy.context.object; k.name = "cape_kraag"; bpy.ops.object.shade_smooth()
    k.data.materials.append(fluweel); k.data.materials.append(voering)
    ks = k.modifiers.new("dik", "SOLIDIFY"); ks.thickness = 0.04; ks.material_offset = 1
    _knip(k, y=(0.0, 5))
    bpy.ops.mesh.primitive_torus_add(major_radius=0.74, minor_radius=0.085, major_segments=96, minor_segments=16,
                                     location=(0.04, 0.2, 1.18), rotation=(math.radians(14), 0, 0))
    kr = bpy.context.object; kr.name = "cape_kraagrand"; bpy.ops.object.shade_smooth(); kr.data.materials.append(hermelijn())
    # de rand ligt op de bovenkant van de kelk: in de lokale z een halve diepte omhoog
    import mathutils
    kr.location = mathutils.Vector(kr.location) + mathutils.Euler(kr.rotation_euler).to_matrix() @ mathutils.Vector((0, 0, 0.21))
    _knip(kr, y=(0.0, 5))
    # gouden zoom langs de onderrand op de vloer (naast het lijf zichtbaar); geen bies langs de opening,
    # die las als een regenboog
    bpy.ops.mesh.primitive_torus_add(major_radius=1.0, minor_radius=0.09, major_segments=128, minor_segments=16,
                                     location=(0, CY, 0.04))
    o = bpy.context.object; o.name = "cape_zoom"; o.scale = (BX * 1.08 * 1.02, BY * 1.02, 1.0)
    bpy.ops.object.shade_smooth(); o.data.materials.append(hermelijn())
    _knip(o, y=(VOOR + 0.05, 5))


def zoom(lijf_delen, vloer):
    """Gouden gesp met robijn linksboven op zijn schouder, onderaan de hoge kraag van de cape: houdt de cape vast. Geen ring om zijn kruin: het grote oog
    zit daar vooraan, en een band over het oog las in pixels als een masker. Lijf en gezicht als holdout."""
    _weg(lijf_delen, holdout=True)
    vloer.hide_render = True
    goud = g.mat("gesp", "goud", rough=0.16, spec=1.0, metaal=0.9, emis=0.12)
    loc, draai = (-0.42, -0.24, 1.2), (math.radians(60), 0, math.radians(-30))   # op het lijf, naar buiten gekeerd
    bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=0.17, depth=0.07, location=loc, rotation=draai)
    s = bpy.context.object; s.name = "gesp"
    bv = s.modifiers.new("rond", "BEVEL"); bv.width = 0.025; bv.segments = 4
    bpy.ops.object.shade_smooth(); s.data.materials.append(goud)
    bpy.ops.mesh.primitive_torus_add(major_radius=0.17, minor_radius=0.035, major_segments=48, minor_segments=12,
                                     location=loc, rotation=draai)
    t = bpy.context.object; t.name = "gesp_rand"; bpy.ops.object.shade_smooth(); t.data.materials.append(goud)
    # robijn: een beetje naar voren
    import mathutils
    n = mathutils.Euler(draai).to_matrix() @ mathutils.Vector((0, 0, 1))
    if n.y > 0:
        n = -n
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, location=tuple(mathutils.Vector(loc) + n * 0.05))
    r = bpy.context.object; r.name = "gesp_steen"; r.scale = (0.085, 0.085, 0.085)
    bpy.ops.object.shade_smooth(); r.data.materials.append(g.mat("gesp_robijn", "rood", rough=0.1, emis=0.3))


def ster(lijf_delen, vloer):
    _weg(lijf_delen)
    vloer.hide_render = True
    glans = g.mat("ster", "munt", emis=1.2, rough=0.2)
    wit = g.mat("ster_hart", "munt_l", emis=3.0)
    loc = (0.66, -0.72, 1.2)               # rechterschouder, iets voor het lijf
    for hoek, lang in ((0, 0.21), (90, 0.21)):
        # lange platte punt: een bol, langgerekt en dun (vier punten = twee kruisende spillen)
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, location=loc,
                                             rotation=(0, math.radians(hoek), 0))
        p = bpy.context.object; p.name = "ster_punt"; p.scale = (lang, 0.03, 0.045)
        bpy.ops.object.shade_smooth(); p.data.materials.append(glans)
    for hoek in (45, 135):
        bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, location=loc,
                                             rotation=(0, math.radians(hoek), 0))
        p = bpy.context.object; p.name = "ster_punt"; p.scale = (0.1, 0.022, 0.026)
        bpy.ops.object.shade_smooth(); p.data.materials.append(glans)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, location=loc)
    h = bpy.context.object; h.name = "ster_hart"; h.scale = (0.06, 0.06, 0.06)
    bpy.ops.object.shade_smooth(); h.data.materials.append(wit)


def bouw(stand, lijf_delen, vloer):
    lijf_delen = [o for o in lijf_delen if o is not vloer]
    {"cape": cape, "zoom": zoom, "ster": ster}[stand](lijf_delen, vloer)
