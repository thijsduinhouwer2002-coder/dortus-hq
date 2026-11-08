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
    """Punten (n x 3) in wereldmaat, loop_start, loop_total en hoekpunt per loop als numpy-arrays.
    Omgerekend met matrix_world zonder de delta van Exploded view (zoals uit_elkaar.echte_matrix)."""
    me = ob.data
    co = np.empty(len(me.vertices) * 3, dtype=np.float32)
    me.vertices.foreach_get("co", co)
    m = ob.matrix_world.copy()
    m.translation -= ob.delta_location
    afwijking = max(abs(m[i][j] - (1.0 if i == j else 0.0)) for i in range(4) for j in range(4))
    log(f"matrix {ob.name}: echte matrix_world wijkt {afwijking:.2e} af van de eenheidsmatrix")
    m = np.array(m)
    ls = np.empty(len(me.polygons), dtype=np.int32)
    lt = np.empty(len(me.polygons), dtype=np.int32)
    me.polygons.foreach_get("loop_start", ls)
    me.polygons.foreach_get("loop_total", lt)
    lv = np.empty(len(me.loops), dtype=np.int32)
    me.loops.foreach_get("vertex_index", lv)
    co = co.reshape(-1, 3).astype(np.float64) @ m[:3, :3].T + m[:3, 3]
    return co, ls, lt, lv


def uitsnede(mesh, c, as_r, r_uit, r_in, nek_r=None, vlak=None):
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
    if vlak is not None:  # (punt op het snijvlak, marge): vlakken met alle hoekpunten in het snijvlak weg
        z = np.abs((co - vlak[0]) @ as_r)[lv]
        houd &= np.maximum.reduceat(z, ls) > vlak[1]
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
    """BVH van de grootste uitsnede één keer; de kleinste per hoek gedraaid met numpy en een nieuwe BVH.
    Deel B over +hoek draaien ten opzichte van A is hetzelfde als deel A over -hoek draaien ten opzichte van B,
    dus we draaien wat het minst kost om opnieuw in een BVH te zetten (bij de variant nek: de 64 nekvlakken)."""

    def __init__(self, a, b, c, as_r):
        self.c, self.as_r = c, as_r
        self.teken = 1.0 if len(b[1]) <= len(a[1]) else -1.0
        vast, self.b = (a, b) if self.teken > 0 else (b, a)
        self.bvh_a = BVHTree.FromPolygons(vast[0].tolist(), vast[1])
        self.draaiend = "B" if self.teken > 0 else "A"
        u = as_r.orthogonal().normalized()
        w = as_r.cross(u).normalized()
        self.richtingen = [u * math.cos(2 * math.pi * k / RICHTINGEN) + w * math.sin(2 * math.pi * k / RICHTINGEN)
                           for k in range(RICHTINGEN)]
        self.toetsen = 0

    def raakt(self, k, hoek):
        """Raakt deel B, gedraaid over hoek graden met zijn as naar richting k, deel A?"""
        self.toetsen += 1
        m = np.array(Matrix.Rotation(math.radians(self.teken * hoek), 3, self.as_r.cross(self.richtingen[k])))
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
    vlak = (np.array(a_deel["cj_snijpunt"]), 0.05 * hulp.u())
    for variant, nek, vl in (("volledig", None, None), ("zonder_snijvlak", None, vlak), ("nek", 0.48 * r, None)):
        t0 = time.perf_counter()
        a = uitsnede(ma, np.array(c), np.array(as_r), r_uit, r_in, nek, vl)
        b = uitsnede(mb, np.array(c), np.array(as_r), r_uit, r_in, None, vl)
        t_snede = time.perf_counter() - t0
        log(f"figuur={figuur} variant={variant} uitsnede A={len(a[1])} vlakken B={len(b[1])} vlakken "
            f"(van {len(a_deel.data.polygons)} en {len(b_deel.data.polygons)}) inlezen={t_np:.3f} s "
            f"uitsnijden={t_snede:.3f} s")
        uitslag[variant] = {}
        proef = Meter(a, b, np.array(c), as_r)
        for k in range(RICHTINGEN):
            log(f"figuur={figuur} variant={variant} richting={k * 360 // RICHTINGEN} raakt_bij_0={proef.raakt(k, 0.0)} "
                f"raakt_bij_0.1={proef.raakt(k, 0.1)}")
        for methode in ("vast", "grof"):
            t0 = time.perf_counter()
            meter = Meter(a, b, np.array(c), as_r)
            grenzen = [getattr(meter, methode)(k) for k in range(RICHTINGEN)]
            tijd = time.perf_counter() - t0
            for k, g in enumerate(grenzen):
                log(f"figuur={figuur} variant={variant} methode={methode} richting={k * 360 // RICHTINGEN} "
                    f"grens={g:.1f} graden")
            log(f"figuur={figuur} variant={variant} methode={methode} tijd={tijd:.3f} s toetsen={meter.toetsen} "
                f"draaiend_deel={meter.draaiend} per_toets={tijd / max(meter.toetsen, 1) * 1000:.1f} ms "
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
    2. nek: de nek (straal n = 0,48 r) bestaat alleen boven het snijvlak van A, van -h tot de kogel. De wand
       van de klikopening (x = a = 0,85 r, z van -h tot de kom) draait naar de nek: een wandpunt (a, z) komt op
       x' = a*cos(t) + z*sin(t), z' = z*cos(t) - a*sin(t). De onderrand zelf zakt onder het snijvlak (z' < -h),
       daar is geen nek. Het eerste raakpunt is de voet van de nek (straal n op het snijvlak van A) tegen de
       wand: met z' = -h volgt x' = (a - h*sin(t)) / cos(t) = n, dus h*sin(t) + n*cos(t) = a,
       t = asin(a / wortel(h^2 + n^2)) - atan2(n, h). In het draaivlak ligt de wand het dichtst bij de nek.
       (Eerste rekensom, de onderrand tegen de nek, gaf acos(n / wortel(a^2 + h^2)) - atan2(h, a): fout, want
       dat raakpunt ligt onder het snijvlak.)"""
    r = a_deel["cj_kogel_r"]
    a, n = a_deel["cj_open_r"], 0.48 * r
    h = (Vector(a_deel["cj_centrum"]) - Vector(a_deel["cj_snijpunt"])).dot(Vector(a_deel["cj_as"]).normalized())
    nek = math.degrees(math.asin(a / math.hypot(h, n)) - math.atan2(n, h))
    oud = math.degrees(math.acos(n / math.hypot(a, h)) - math.atan2(h, a))
    log(f"staaf rekensom r={r:.3f} opening_r={a:.3f} nek_r={n:.3f} h={h:.4f} (kogelmidden boven snijvlak) "
        f"volledig=0.0 nek={nek:.2f} graden (eerste, foute rekensom onderrand: {oud:.2f})")
    return {"volledig": 0.0, "nek": nek}  # zonder_snijvlak: geen rekensom, alleen gelogd


def figuur_meten(naam, ob):
    lijst = hulp.plaats(naam, ob, (0, 0, 0), (1, 0, 0), speling=0.2, kogel=5.0)
    eis(f"{naam}: twee delen geplaatst", len(lijst) == 2)
    if len(lijst) != 2:
        return None, None, lijst
    a = next(d for d in lijst if d["cj_deel"] == "A")
    b = next(d for d in lijst if d["cj_deel"] == "B")
    log(f"figuur={naam} passing={a.get('cj_passing')} wand={a.get('cj_wand_mm')} mm centrum="
        f"{tuple(round(x, 4) for x in a['cj_centrum'])}")
    uitslag = meet(naam, a, b)
    return uitslag, a, lijst


def main():
    log(f"blender {bpy.app.version_string}")
    zip_pad = sys.argv[sys.argv.index("--") + 1]
    bpy.ops.extensions.package_install_files(filepath=zip_pad, repo="user_default", enable_on_install=True)
    eis("add-on staat aan", any(a.module.endswith("click_joints") for a in bpy.context.preferences.addons))
    figuren.mm_scene()

    arm, _, lijst = figuur_meten("arm", figuren.arm())
    hulp.weg(lijst)  # anders telt de staaf vier delen
    if arm:
        for variant in arm:
            snelst = min(t for _, t in arm[variant].values())
            log(f"arm variant={variant} snelste hele bereik {snelst:.3f} s")
        snelst = min(t for _, t in arm["nek"].values())
        eis(f"arm nek: hele bereik (8 richtingen) onder 1 s ({snelst:.3f} s)", snelst < 1.0)
        log("LET OP: de 1 s-eis is alleen bewezen voor de nekvariant (64 draaiende vlakken). Volledig raakte bij de "
            "eerste stap, dus daar is geen echt bereik doorlopen; met twee grote delen kost een toets ±40-50 ms.")

    staaf, a, _ = figuur_meten("staaf", figuren.staaf("staaf", 5.0, lengte=40.0))
    if staaf:
        verwacht = rekensom(a)
        for variant, v in verwacht.items():
            for methode in ("vast", "grof"):
                grenzen = staaf[variant][methode][0]
                stap = math.floor(v / STAP + 1e-9) * STAP  # laatste vrije stap voor de rekensom
                verschil = max(abs(g - v) for g in grenzen)
                log(f"staaf variant={variant} methode={methode} verwacht={v:.2f} laatste_vrije_stap={stap:.1f} "
                    f"gemeten={min(grenzen):.1f} tot {max(grenzen):.1f} verschil={verschil:.2f} graden")
                eis(f"staaf {variant} {methode}: elke richting precies {stap:.1f} graden",
                    all(abs(g - stap) < 1e-9 for g in grenzen))

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
