"""3MF schrijven zonder extra add-on (Blender heeft geen eigen 3MF-export).

Een 3MF is een zip met drie vaste delen: [Content_Types].xml, _rels/.rels en 3D/3dmodel.model.
Het model bevat één object met de hoekpunten en driehoeken in millimeter (unit="millimeter"), zoals
Bambu Studio, PrusaSlicer en Cura het verwachten. Naam, vorm en plek zijn gelijk aan de STL-export:
de geëvalueerde mesh (modifiers toegepast) in wereldcoördinaten, keer `schaal` naar mm."""
import zipfile
from xml.sax.saxutils import escape

import bmesh
import bpy

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


def driehoeken(ob, schaal):
    """(hoekpunten in mm, driehoeken als drietallen indexen) van de geëvalueerde mesh in wereldcoördinaten.
    Driehoeken via bmesh.ops.triangulate (BEAUTY): de loop_triangles van Blender gaven bij de holle n-hoeken
    uit de Boolean 8 tot 52 randen die twee keer dezelfde kant op liepen (ronde h, GEZIEN in de test).
    Bij een gespiegeld object (negatieve schaal) draait de volgorde om, zodat de normalen naar buiten wijzen."""
    graaf = bpy.context.evaluated_depsgraph_get()
    ev = ob.evaluated_get(graaf)
    me = ev.to_mesh()
    bm = bmesh.new()
    try:
        bm.from_mesh(me)
        bmesh.ops.triangulate(bm, faces=bm.faces[:], quad_method="BEAUTY", ngon_method="BEAUTY")
        bm.verts.index_update()
        m = ob.matrix_world
        punten = [tuple(c * schaal for c in (m @ v.co)) for v in bm.verts]
        om = m.determinant() < 0
        lijst = []
        for f in bm.faces:
            t = tuple(v.index for v in f.verts)
            lijst.append(t[::-1] if om else t)
    finally:
        bm.free()
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
