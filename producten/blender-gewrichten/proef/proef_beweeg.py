"""Bouwproef beweegproef: hoe ver buigt een kogelgewricht van Click Joints, en hoe snel is dat te meten.

Draait in de echte Blender zonder scherm:
  blender -b --factory-startup --python proef/proef_beweeg.py -- /tmp/click_joints.zip
Plaatst met de echte add-on een kogelgewricht op de testarm (±261K driehoeken) en op een staaf van 10 mm,
draait deel B om het kogelmidden in 8 richtingen en zoekt het eerste raakpunt met deel A (BVH-overlap).
Twee varianten:
  volledig: alle vlakken van A en B binnen 3 kogeldiameters, behalve kogel en kom.
  nek:      van deel A alleen de nek (wat zou het bereik zijn als de snijvlakken elkaar niet raken).
Twee methodes: vaste stap van 2,5 graden, en grof (10 graden) met bisectie tot 2,5 graden.
Alle regels met BEWEEG in het log; exit 1 als een eis faalt.
"""
import math
import os
import sys
import time

import bpy
import numpy as np
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "e2e"))
import figuren  # noqa: E402
import hulp  # noqa: E402

STAP = 2.5        # graden
GROF = 10.0       # graden, eerste ronde van de bisectie
MAX_HOEK = 180.0
RICHTINGEN = 8
BEREIK = 3.0      # kogeldiameters rond het kogelmidden
MARGE = 0.05      # keer de kogelstraal, bovenop kogelstraal plus speling
fouten = []


def log(tekst):
    print(f"BEWEEG {tekst}", flush=True)


def eis(naam, ok):
    log(f"EIS {'OK' if ok else 'FOUT'} {naam}")
    if not ok:
        fouten.append(naam)


def mesh_np(ob):
    """Punten (n x 3), loop_start, loop_total en hoekpunt per loop als numpy-arrays (mesh in wereldmaat)."""
    me = ob.data
    co = np.empty(len(me.vertices) * 3, dtype=np.float32)
    me.vertices.foreach_get("co", co)
    ls = np.empty(len(me.polygons), dtype=np.int32)
    lt = np.empty(len(me.polygons), dtype=np.int32)
    me.polygons.foreach_get("loop_start", ls)
    me.polygons.foreach_get("loop_total", lt)
    lv = np.empty(len(me.loops), dtype=np.int32)
    me.loops.foreach_get("vertex_index", lv)
    return co.reshape(-1, 3).astype(np.float64), ls, lt, lv


def uitsnede(mesh, c, as_r, r_uit, r_in, nek_r=None):
    """Vlakken met minstens één hoekpunt binnen r_uit van het kogelmidden, zonder de vlakken waarvan
    ALLE hoekpunten binnen r_in liggen (kogel en kom). Met nek_r: alleen vlakken waarvan alle hoekpunten op de
    nekcilinder liggen, onder het kogelmidden. Geeft (punten, vlakken) met hernummerde punten."""
    co, ls, lt, lv = mesh
    rel = co - c
    d = np.linalg.norm(rel, axis=1)
    order = np.argsort(ls)  # reduceat wil oplopende beginpunten
    ls, lt = ls[order], lt[order]
    dl = d[lv]
    houd = (np.minimum.reduceat(dl, ls) <= r_uit) & (np.maximum.reduceat(dl, ls) > r_in)
    if nek_r is not None:
        t = rel @ as_r
        rad = np.linalg.norm(rel - np.outer(t, as_r), axis=1)
        houd &= np.maximum.reduceat(np.abs(rad - nek_r)[lv], ls) < 0.02 * nek_r
        houd &= np.maximum.reduceat(t[lv], ls) < 0.0
    gekozen = np.nonzero(houd)[0]
    idx = np.concatenate([lv[ls[i]:ls[i] + lt[i]] for i in gekozen]) if len(gekozen) else np.zeros(0, np.int32)
    punten = np.unique(idx)
    nieuw = np.searchsorted(punten, idx).tolist()
    vlakken, k = [], 0
    for n in lt[gekozen].tolist():
        vlakken.append(nieuw[k:k + n])
        k += n
    return co[punten], vlakken


class Meter:
    """BVH van deel A één keer; deel B per hoek gedraaid met numpy en een nieuwe BVH uit de uitsnede."""

    def __init__(self, a, b, c, as_r):
        self.a, self.b, self.c, self.as_r = a, b, c, as_r
        self.bvh_a = BVHTree.FromPolygons(a[0].tolist(), a[1])
        u = as_r.orthogonal().normalized()
        w = as_r.cross(u).normalized()
        self.richtingen = [u * math.cos(2 * math.pi * k / RICHTINGEN) + w * math.sin(2 * math.pi * k / RICHTINGEN)
                           for k in range(RICHTINGEN)]
        self.toetsen = 0

    def raakt(self, k, hoek):
        """Raakt deel B, gedraaid over hoek graden met zijn as naar richting k, deel A?"""
        self.toetsen += 1
        m = np.array(Matrix.Rotation(math.radians(hoek), 3, self.as_r.cross(self.richtingen[k])))
        pb = (self.b[0] - self.c) @ m.T + self.c
        bvh_b = BVHTree.FromPolygons(pb.tolist(), self.b[1])
        return bool(self.bvh_a.overlap(bvh_b))

    def vast(self, k):
        hoek = STAP
        while hoek <= MAX_HOEK + 1e-9:
            if self.raakt(k, hoek):
                return hoek - STAP
            hoek += STAP
        return MAX_HOEK

    def grof(self, k):
        hoek = GROF
        while hoek <= MAX_HOEK + 1e-9:
            if self.raakt(k, hoek):
                vrij, raak = hoek - GROF, hoek
                while raak - vrij > STAP + 1e-9:
                    mid = (vrij + raak) / 2
                    if self.raakt(k, mid):
                        raak = mid
                    else:
                        vrij = mid
                return vrij
            hoek += GROF
        return MAX_HOEK


def meet(figuur, a_deel, b_deel):
    """Meet beide varianten met beide methodes. Geeft {variant: {methode: (grenzen, tijd)}}."""
    c = Vector(a_deel["cj_centrum"])
    as_r = Vector(a_deel["cj_as"]).normalized()
    r = a_deel["cj_kogel_r"]
    s = a_deel["cj_speling_mm"] * hulp.u()
    r_uit, r_in = BEREIK * 2 * r, r + s + MARGE * r
    log(f"figuur={figuur} delta_B={tuple(round(x, 3) for x in b_deel.delta_location)} kogel_r={r:.3f} "
        f"speling={s:.3f} uitsluiten_binnen={r_in:.3f} bereik={r_uit:.3f}")
    t0 = time.perf_counter()
    ma, mb = mesh_np(a_deel), mesh_np(b_deel)
    t_np = time.perf_counter() - t0
    uitslag = {}
    for variant, nek in (("volledig", None), ("nek", 0.48 * r)):
        t0 = time.perf_counter()
        a = uitsnede(ma, np.array(c), np.array(as_r), r_uit, r_in, nek)
        b = uitsnede(mb, np.array(c), np.array(as_r), r_uit, r_in)
        t_snede = time.perf_counter() - t0
        log(f"figuur={figuur} variant={variant} uitsnede A={len(a[1])} vlakken B={len(b[1])} vlakken "
            f"(van {len(a_deel.data.polygons)} en {len(b_deel.data.polygons)}) inlezen={t_np:.3f} s "
            f"uitsnijden={t_snede:.3f} s")
        uitslag[variant] = {}
        for methode in ("vast", "grof"):
            t0 = time.perf_counter()
            meter = Meter(a, b, np.array(c), as_r)
            grenzen = [getattr(meter, methode)(k) for k in range(RICHTINGEN)]
            tijd = time.perf_counter() - t0
            for k, g in enumerate(grenzen):
                log(f"figuur={figuur} variant={variant} methode={methode} richting={k * 360 // RICHTINGEN} "
                    f"grens={g:.1f} graden")
            log(f"figuur={figuur} variant={variant} methode={methode} tijd={tijd:.3f} s toetsen={meter.toetsen} "
                f"(met inlezen en uitsnijden {tijd + t_np + t_snede:.3f} s)")
            log(f"figuur={figuur} variant={variant} methode={methode} Bends {min(grenzen):.1f} to "
                f"{max(grenzen):.1f} degrees")
            uitslag[variant][methode] = (grenzen, tijd + t_np + t_snede)
        eis(f"{figuur} {variant}: vast en grof geven dezelfde grenzen",
            uitslag[variant]["vast"][0] == uitslag[variant]["grof"][0])
    return uitslag


def rekensom(a_deel):
    """Verwachte grens uit de vorm van het gewricht (zie maten() in click_joints/gewricht.py).
    Frame met het kogelmidden C in de oorsprong, as naar deel B. Het snijvlak ligt op afstand h onder C.
    1. volledig: de snijvlakken van A en B vallen samen (A eindigt waar B begint). Bij elke draaiing > 0
       zakt de buitenrand van het snijvlak van B (straal rho) rho*sin(t) - h*(1 - cos(t)) > 0 in deel A,
       dus de grens is 0 graden.
    2. nek: de onderrand van de klikopening (straal a = 0,85 r, op hoogte -h) draait naar de nek (straal
       n = 0,48 r). Dat punt komt op afstand a*cos(t) - h*sin(t) van de as; raak als dat n is:
       t = acos(n / R) - atan2(h, a), met R = wortel(a^2 + h^2). Het punt van de rand in het draaivlak
       komt het eerst bij de nek (dichter bij de as dan elk ander punt op de rand)."""
    r = a_deel["cj_kogel_r"]
    a, n = a_deel["cj_open_r"], 0.48 * r
    h = (Vector(a_deel["cj_centrum"]) - Vector(a_deel["cj_snijpunt"])).dot(Vector(a_deel["cj_as"]).normalized())
    rr = math.hypot(a, h)
    nek = math.degrees(math.acos(n / rr) - math.atan2(h, a))
    log(f"staaf rekensom r={r:.3f} opening_r={a:.3f} nek_r={n:.3f} h={h:.4f} (kogelmidden boven snijvlak) "
        f"volledig=0.0 nek={nek:.2f} graden")
    return {"volledig": 0.0, "nek": nek}


def figuur_meten(naam, ob):
    lijst = hulp.plaats(naam, ob, (0, 0, 0), (1, 0, 0), speling=0.2, kogel=5.0)
    eis(f"{naam}: twee delen geplaatst", len(lijst) == 2)
    if len(lijst) != 2:
        return None, None
    a = next(d for d in lijst if d["cj_deel"] == "A")
    b = next(d for d in lijst if d["cj_deel"] == "B")
    log(f"figuur={naam} passing={a.get('cj_passing')} wand={a.get('cj_wand_mm')} mm centrum="
        f"{tuple(round(x, 4) for x in a['cj_centrum'])}")
    return meet(naam, a, b), a


def main():
    log(f"blender {bpy.app.version_string}")
    zip_pad = sys.argv[sys.argv.index("--") + 1]
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    eis("add-on staat aan", any(a.module.endswith("click_joints") for a in bpy.context.preferences.addons))
    figuren.mm_scene()

    arm, _ = figuur_meten("arm", figuren.arm())
    if arm:
        for variant in arm:
            snelst = min(t for _, t in arm[variant].values())
            eis(f"arm {variant}: hele bereik (8 richtingen) onder 1 s ({snelst:.3f} s)", snelst < 1.0)

    staaf, a = figuur_meten("staaf", figuren.staaf("staaf", 5.0, lengte=40.0))
    if staaf:
        verwacht = rekensom(a)
        for variant, v in verwacht.items():
            for methode in ("vast", "grof"):
                grenzen = staaf[variant][methode][0]
                verschil = max(abs(g - v) for g in grenzen)
                log(f"staaf variant={variant} methode={methode} verwacht={v:.2f} gemeten={min(grenzen):.1f} tot "
                    f"{max(grenzen):.1f} verschil={verschil:.2f} graden")
                eis(f"staaf {variant} {methode}: elke richting binnen 2,5 graden van de rekensom", verschil <= 2.5)

    if hulp.fouten:
        log(f"fouten in de hulp: {hulp.fouten}")
    log(f"UITSLAG {'GROEN' if not fouten else 'ROOD'} fouten={fouten}")
    sys.exit(1 if fouten else 0)


try:
    main()
except SystemExit:
    raise
except Exception:  # noqa: BLE001
    import traceback
    traceback.print_exc()
    sys.exit(1)
