"""Ronde h: 3MF-export (Daan, beoordeling 2, punt 2). Exporteert via de add-on met de keuze 3MF en leest
het bestand zelf terug: de vaste zip-delen, unit millimeter, aantal driehoeken, maat in mm gelijk aan het deel,
geen foute randen erbij ten opzichte van de mesh zelf (elke rand één keer heen en één keer terug), en het volume
gelijk aan het deel (positief, dus de normalen wijzen naar buiten)."""
import os
import tempfile
import zipfile
import xml.etree.ElementTree as ET

import bpy

from hulp import log, meting, stap, u

NS = "{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}"


def lees(pad):
    with zipfile.ZipFile(pad) as z:
        namen = set(z.namelist())
        model = ET.fromstring(z.read("3D/3dmodel.model")) if "3D/3dmodel.model" in namen else None
    return namen, model


def foute_randen(vlakken):
    """Gerichte randen die niet precies één keer heen en één keer terug voorkomen (gesloten en dezelfde
    draairichting). Geeft (aantal, soorten): dubbel = zelfde richting vaker (omgedraaid vlak), open = geen terug."""
    randen = {}
    for v in vlakken:
        for i in range(len(v)):
            e = (v[i], v[(i + 1) % len(v)])
            randen[e] = randen.get(e, 0) + 1
    dubbel = sum(1 for n in randen.values() if n > 1)
    open_ = sum(1 for (a, b) in randen if (b, a) not in randen)
    fout = sum(1 for (a, b), n in randen.items() if n != 1 or randen.get((b, a), 0) != 1)
    return fout, {"dubbel": dubbel, "open": open_}


def toets(lijst, label="3MF"):
    inst = bpy.context.scene.click_joints
    inst.exportmap = os.path.join(tempfile.gettempdir(), "cj_export_3mf") + os.sep
    inst.formaat = "3MF"
    uitslag = bpy.ops.click_joints.exporteer()
    inst.formaat = "STL"  # terug naar de standaard voor de toetsen hierna
    stap(f"{label}: export klaar ({uitslag})", uitslag == {"FINISHED"})
    stap(f"{label}: na export niets geselecteerd", not any(o.select_get() for o in bpy.context.view_layer.objects))
    for d in lijst:
        pad = d.get("cj_3mf", "")
        stap(f"{label} {os.path.basename(pad)} bestaat", bool(pad) and os.path.exists(pad))
        if not pad or not os.path.exists(pad):
            continue
        namen, model = lees(pad)
        stap(f"{label} {d.name}: vaste delen in de zip",
             {"[Content_Types].xml", "_rels/.rels", "3D/3dmodel.model"} <= namen)
        if model is None:
            continue
        stap(f"{label} {d.name}: unit millimeter", model.get("unit") == "millimeter")
        punten = [(float(v.get("x")), float(v.get("y")), float(v.get("z"))) for v in model.iter(NS + "vertex")]
        drie = [(int(t.get("v1")), int(t.get("v2")), int(t.get("v3"))) for t in model.iter(NS + "triangle")]
        verwacht = sum(len(p.vertices) - 2 for p in d.data.polygons)
        stap(f"{label} {d.name}: {len(drie)} driehoeken, deel heeft er {verwacht}", len(drie) == verwacht > 0)
        maat = [max(p[i] for p in punten) - min(p[i] for p in punten) for i in range(3)]
        maat_deel = [x / u() for x in d.dimensions]
        verschil = max(abs(a - b) for a, b in zip(maat, maat_deel))
        stap(f"{label} {d.name}: maat {tuple(round(x, 3) for x in maat)} mm gelijk aan het deel binnen 0,01 mm "
             f"(verschil {verschil:.5f})", verschil < 0.01)
        fout, soort = foute_randen(drie)
        bron, bron_soort = foute_randen([tuple(p.vertices) for p in d.data.polygons])
        log(f"3MF {d.name}: foute randen in 3MF {fout} {soort}, in de mesh zelf {bron} {bron_soort}")
        stap(f"{label} {d.name}: 3MF voegt geen foute randen toe (3MF {fout}, mesh {bron})", fout <= bron)
        vol = 0.0
        for a, b, c in drie:
            (x1, y1, z1), (x2, y2, z2), (x3, y3, z3) = punten[a], punten[b], punten[c]
            vol += (x1 * (y2 * z3 - y3 * z2) - x2 * (y1 * z3 - y3 * z1) + x3 * (y1 * z2 - y2 * z1)) / 6.0
        _, vol_deel = meting(d)
        stap(f"{label} {d.name}: volume {vol:.2f} mm3 gelijk aan het deel ({vol_deel:.2f}) binnen 0,1%",
             vol > 0 and abs(vol - vol_deel) <= 0.001 * abs(vol_deel))
        log(f"3MF {d.name}: {os.path.getsize(pad)} bytes, {len(punten)} punten, {len(drie)} driehoeken")
