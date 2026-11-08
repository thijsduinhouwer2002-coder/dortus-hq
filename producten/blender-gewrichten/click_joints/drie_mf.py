"""3MF schrijven zonder extra add-on (Blender heeft geen eigen 3MF-export).

Een 3MF is een zip met drie vaste delen: [Content_Types].xml, _rels/.rels en 3D/3dmodel.model.
Het model bevat één object met de hoekpunten en driehoeken in millimeter (unit="millimeter"), zoals
Bambu Studio, PrusaSlicer en Cura het verwachten. Naam, vorm en plek zijn gelijk aan de STL-export:
de geëvalueerde mesh (modifiers toegepast) in wereldcoördinaten, keer `schaal` naar mm."""
import zipfile
from xml.sax.saxutils import escape

import bpy
from mathutils import Matrix, Vector
from mathutils.geometry import tessellate_polygon

TYPES = ('<?xml version="1.0" encoding="UTF-8"?>\n'
         '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
         '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
         '<Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>'
         '</Types>')
RELS = ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Target="/3D/3dmodel.model" Id="rel0" '
        'Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>'
        '</Relationships>')


def _veelhoek(vs, co, gebruikt):
    """Driehoeken (indexen in vs) voor één vlak. Elke driehoek staat in oplopende volgorde van de punten in het
    vlak: bij een opdeling langs diagonalen heeft elke driehoek dan dezelfde draairichting als het vlak, ook
    als hij plat is. Probeert elk beginpunt tot geen nieuwe diagonaal een rand is die al bestaat (ronde j:
    in de meterscene liepen 108 randen dubbel, een diagonaal viel samen met een rand elders)."""
    n = len(vs)
    if n == 3:
        return [(0, 1, 2)]
    eerste = None
    for start in range(n):
        if n == 4:
            stel = [(start % 4, (start + 1) % 4, (start + 2) % 4), (start % 4, (start + 2) % 4, (start + 3) % 4)] if start < 2 else None
            if stel is None:
                break
        else:
            rot = [(start + i) % n for i in range(n)]
            try:
                ruw = tessellate_polygon([[co[vs[i]] for i in rot]])
            except Exception:
                ruw = []
            stel = [tuple(rot[i] for i in t) for t in ruw]
            if len(stel) != n - 2:
                continue
        stel = [tuple(sorted(t)) for t in stel]
        diag = {tuple(sorted((vs[t[i]], vs[t[j]]))) for t in stel for i, j in ((0, 1), (1, 2), (0, 2))
                if (t[j] - t[i]) % n not in (1, n - 1)}
        if eerste is None:
            eerste = (stel, diag)
        if not diag & gebruikt:
            gebruikt |= diag
            return stel
    if eerste is None:  # geen opdeling gevonden: waaier vanaf punt 0 (topologisch altijd goed)
        stel = [(0, i, i + 1) for i in range(1, n - 1)]
        eerste = (stel, {tuple(sorted((vs[0], vs[i]))) for i in range(2, n - 1)})
    gebruikt |= eerste[1]
    return eerste[0]


def driehoeken(ob, schaal):
    """(hoekpunten in mm, driehoeken als drietallen indexen) van de geëvalueerde mesh in wereldcoördinaten.
    Eigen opdeling per vlak (`_veelhoek`): de loop_triangles van Blender en bmesh.ops.triangulate (BEAUTY en
    EAR_CLIP) gaven bij de holle n-hoeken uit de Boolean randen die dubbel liepen (ronde h en j).
    Bij een gespiegeld object (negatieve schaal) draait de volgorde om, zodat de normalen naar buiten wijzen."""
    graaf = bpy.context.evaluated_depsgraph_get()
    ev = ob.evaluated_get(graaf)
    me = ev.to_mesh()
    try:
        m = Matrix.Scale(schaal, 4) @ ob.matrix_world
        punten = [tuple(m @ v.co) for v in me.vertices]
        co = [Vector(p) for p in punten]
        gebruikt = {tuple(sorted(e.vertices)) for e in me.edges}
        om = ob.matrix_world.determinant() < 0
        lijst = []
        for p in me.polygons:
            vs = list(p.vertices)
            for t in _veelhoek(vs, co, gebruikt):
                d = (vs[t[0]], vs[t[1]], vs[t[2]])
                lijst.append(d[::-1] if om else d)
    finally:
        ev.to_mesh_clear()
    return punten, lijst


def model_xml(naam, punten, lijst):
    stukken = ['<?xml version="1.0" encoding="UTF-8"?>\n'
               '<model unit="millimeter" xml:lang="en-US" '
               'xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">'
               f'<metadata name="Application">Click Joints</metadata>'
               f'<resources><object id="1" type="model" name="{escape(naam, {chr(34): "&quot;"})}"><mesh><vertices>']
    stukken += [f'<vertex x="{x:.6f}" y="{y:.6f}" z="{z:.6f}"/>' for x, y, z in punten]
    stukken.append('</vertices><triangles>')
    stukken += [f'<triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in lijst]
    stukken.append('</triangles></mesh></object></resources><build><item objectid="1"/></build></model>')
    return "".join(stukken)


def schrijf(ob, pad, schaal):
    """Schrijft één deel als 3MF naar `pad`. Geeft het aantal driehoeken terug."""
    punten, lijst = driehoeken(ob, schaal)
    with zipfile.ZipFile(pad, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("3D/3dmodel.model", model_xml(ob.name, punten, lijst))
    return len(lijst)
