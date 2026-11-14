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
    vo = nt.nodes.new("ShaderNodeTexVoronoi"); vo.inputs["Scale"].default_value = 7.0
    tc = nt.nodes.new("ShaderNodeTexCoord"); nt.links.new(tc.outputs["Object"], vo.inputs["Vector"])
    ra = nt.nodes.new("ShaderNodeValToRGB")
    ra.color_ramp.elements[0].position = 0.11; ra.color_ramp.elements[0].color = (0.02, 0.02, 0.025, 1)
    ra.color_ramp.elements[1].position = 0.12; ra.color_ramp.elements[1].color = (0.92, 0.9, 0.86, 1)
    ra.color_ramp.interpolation = "CONSTANT"
    nt.links.new(vo.outputs["Distance"], ra.inputs["Fac"]); nt.links.new(ra.outputs["Color"], b.inputs["Base Color"])
    return m


KUSSEN = False  # ronde 4: hij zit op een rood kussen met gouden kwasten (eigen teken van rijkdom)
SCEPTER = True  # gouden scepter met bol, schuin tegen zijn rechterflank (frisse kijker 3b: een eigen koningsstuk)
KRANS = False   # stralenkrans achter hem: ronde 3a las als stekels of schrik, dus uit
RONDE = 3   # 3: rood fluweel, wijde sleep, hermelijn als zoom, stralenkrans (Daan 14 nov 08:45); 2: paarse kelk


def cape(lijf_delen, vloer):
    """Ronde 3 (frisse kijker ronde 2: 4, "tovenaar, niet koning; witte uiteinden lijken handjes en voetjes"):
    - koningsrood fluweel in plaats van paars: paars verdween in het paarse hol en las als tovenaar;
    - een wijde sleep die op de vloer duidelijk breder uitwaaiert dan het lijf (silhouet anders, ook klein);
    - hermelijn is het onderste stuk van de mantel zelf, geen losse ring: geen losse witte uiteinden meer;
    - geen kraag boven zijn schouders (die las als schelp of handjes);
    - een gouden stralenkrans achter hem: dit is de duurste upgrade, die mag glanzen (betaald mag gloed hebben)."""
    import bmesh
    _weg(lijf_delen)                       # het lijf tekent het spel er zelf overheen
    fluweel = g.mat("cape", "a3182e", rough=0.72, spec=0.3, sss=0.05)
    voering = g.mat("cape_voering", "5e0c1c", rough=0.85, spec=0.15)
    bont = hermelijn()
    BX, BY, BZ, CY, VOOR = 1.0, 0.85, 1.3, 0.22, -0.4
    WIJD = 0.7 if not KUSSEN else 0.3                             # extra breedte onderaan (sleep)
    ZOOM_Z = 0.17                           # tot hier hermelijn
    bpy.ops.mesh.primitive_uv_sphere_add(segments=128, ring_count=48, location=(0, 0, 0))
    m = bpy.context.object; m.name = "cape"
    bm = bmesh.new(); bm.from_mesh(m.data)
    weg = [v for v in bm.verts if v.co.z < -0.001 or v.co.y * BY + CY < VOOR]
    bmesh.ops.delete(bm, geom=weg, context="VERTS")
    for v in bm.verts:
        x, y, z = v.co.x * BX, v.co.y * BY + CY, v.co.z * BZ
        hoek = math.atan2(x, y - CY)
        laag = 1 - z / BZ
        diep = 0.2 + 0.8 * laag                # boven glad, onder diepe plooien
        r = 1 + 0.05 * diep * math.sin(9 * hoek)
        v.co = (x * r * (1 + WIJD * laag ** 1.6), CY + (y - CY) * r * (1 + 0.25 * laag ** 2), z)
    bm.to_mesh(m.data); bm.free()
    bpy.ops.object.shade_smooth()
    goudrand = g.mat("cape_goudrand", "goud", rough=0.2, spec=1.0, metaal=0.9, emis=0.1)
    for mt in (fluweel, voering, bont, bont, goudrand, goudrand):
        m.data.materials.append(mt)
    for f in m.data.polygons:
        if f.center.z < ZOOM_Z:
            f.material_index = 2
        elif f.center.z < ZOOM_Z + 0.07:
            f.material_index = 4      # gouden bies boven het bont (frisse kijker 3b: meer goud)
    sol = m.modifiers.new("dik", "SOLIDIFY"); sol.thickness = 0.06; sol.material_offset = 1
    sub = m.modifiers.new("glad", "SUBSURF"); sub.levels = 1; sub.render_levels = 1
    # geen losse bontrol op de vloer meer: die las als een witte plas (ronde 3a)
    if KUSSEN:
        _kussen()
    if SCEPTER:
        _scepter()
    if not KRANS:
        return
    # gouden stralenkrans achter hem: 16 spitse stralen, om en om lang en kort, plat en licht gevend
    goud = g.mat("krans", "goud", rough=0.25, spec=0.8, metaal=0.6, emis=0.6)
    me = bpy.data.meshes.new("krans")
    pts, vlakken = [(0, 0, 0)], []
    N = 16
    for i in range(N):
        a0 = 2 * math.pi * i / N
        lang = 1.3 if i % 2 == 0 else 1.05
        for da, rr in ((-0.14, 0.5), (0.0, lang), (0.14, 0.5)):
            pts.append((rr * math.sin(a0 + da), 0, rr * math.cos(a0 + da)))
        k = 1 + 3 * i
        vlakken.append([k, k + 1, k + 2])
    me.from_pydata(pts, [], vlakken)
    kr = bpy.data.objects.new("cape_krans", me)
    bpy.context.scene.collection.objects.link(kr)
    kr.location = (0, 0.95, 0.95); kr.data.materials.append(goud)
    so = kr.modifiers.new("dik", "SOLIDIFY"); so.thickness = 0.03


def _kussen():
    """Plat, bol kussen van rood fluweel onder hem, met een gouden bies en vier gouden kwasten op de hoeken.
    Het spel tekent het lijf eroverheen, dus je ziet het links, rechts en voor zijn onderkant."""
    import bmesh
    fluweel = g.mat("kussen", "b81d34", rough=0.6, spec=0.35, sss=0.05)
    goud = g.mat("kussen_goud", "goud", rough=0.2, spec=1.0, metaal=0.9, emis=0.1)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, -0.1, 0.2))
    k = bpy.context.object; k.name = "kussen"; k.scale = (3.3, 1.9, 0.6)
    bpy.ops.object.transform_apply(scale=True)
    sub = k.modifiers.new("bol", "SUBSURF"); sub.levels = 3; sub.render_levels = 3
    bpy.ops.object.shade_smooth(); k.data.materials.append(fluweel)
    # gouden bies rond het midden
    bpy.ops.mesh.primitive_torus_add(major_radius=1.0, minor_radius=0.035, major_segments=96, minor_segments=12,
                                     location=(0, -0.1, 0.2))
    b = bpy.context.object; b.name = "kussen_bies"; b.scale = (1.38, 0.74, 1); b.data.materials.append(goud)
    bpy.ops.object.shade_smooth()
    for sx in (-1, 1):
        for sy in (-1, 1):
            x, y = 1.3 * sx, -0.1 + 0.66 * sy
            bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, radius=0.07, location=(x, y, 0.22))
            o = bpy.context.object; o.name = "kwast_knop"; o.data.materials.append(goud); bpy.ops.object.shade_smooth()
            bpy.ops.mesh.primitive_cone_add(vertices=24, radius1=0.1, radius2=0.03, depth=0.2,
                                            location=(x + 0.07 * sx, y - 0.02, 0.1))
            o = bpy.context.object; o.name = "kwast"; o.data.materials.append(goud); bpy.ops.object.shade_smooth()


def _scepter():
    """Staf van goud met een rode bol en een kruisje erop, onderaan op de vloer rechts naast hem, schuin tegen zijn flank.
    Groot genoeg om op spelgrootte als staf met bol te lezen (bol ±0,22 = ±2 spelpixels)."""
    goud = g.mat("scepter_goud", "goud", rough=0.18, spec=1.0, metaal=0.9, emis=0.12)
    rood = g.mat("scepter_bol", "c8203a", rough=0.12, spec=0.8, emis=0.15)
    import mathutils
    voet = mathutils.Vector((1.15, -0.15, 0.0)); top = mathutils.Vector((0.92, -0.15, 1.3))
    as_ = top - voet; lang = as_.length; rot = as_.to_track_quat("Z", "Y").to_euler()
    bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=0.07, depth=lang, location=(voet + top) / 2, rotation=rot)
    st = bpy.context.object; st.name = "scepter_staf"; st.data.materials.append(goud); bpy.ops.object.shade_smooth()
    for t, r in ((0.35, 0.1), (0.7, 0.095), (0.97, 0.12)):
        bpy.ops.mesh.primitive_torus_add(major_radius=r, minor_radius=0.035, location=voet + as_ * t, rotation=rot)
        o = bpy.context.object; o.name = "scepter_ring"; o.data.materials.append(goud); bpy.ops.object.shade_smooth()
    bol = top + as_.normalized() * 0.24
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=0.26, location=bol)
    b = bpy.context.object; b.name = "scepter_bol"; b.data.materials.append(rood); bpy.ops.object.shade_smooth()
    bpy.ops.mesh.primitive_torus_add(major_radius=0.26, minor_radius=0.04, location=bol, rotation=(0, math.radians(90), 0))
    o = bpy.context.object; o.name = "scepter_band"; o.data.materials.append(goud); bpy.ops.object.shade_smooth()
    kr = bol + as_.normalized() * 0.38
    for sx, sz in ((0.07, 0.24), (0.2, 0.07)):
        bpy.ops.mesh.primitive_cube_add(size=1, location=kr, rotation=rot)
        o = bpy.context.object; o.name = "scepter_kruis"; o.scale = (sx, 0.06, sz); o.data.materials.append(goud)


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
    glans = g.mat("ster", "goud", emis=1.6, rough=0.2)
    wit = g.mat("ster_hart", "fff3c4", emis=3.0)
    loc = (0.66, -0.72, 1.2)               # rechterschouder, iets voor het lijf
    for hoek, lang in ((0, 0.3), (90, 0.3)):
        # lange platte punt: een bol, langgerekt en dun (vier punten = twee kruisende spillen)
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, location=loc,
                                             rotation=(0, math.radians(hoek), 0))
        p = bpy.context.object; p.name = "ster_punt"; p.scale = (lang, 0.035, 0.06)
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
