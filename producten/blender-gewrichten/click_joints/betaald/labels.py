"""Mooier overlay (23 nov 2026): rustiger beeld bij een figuur.

1. Schakelaar "Labels" (Selected / All / None, standaard Selected) in het paneel Figure joints. Bij een figuur met
   negen gewrichten stonden negen getallen plus een kopregel in beeld (keuring Shorts 3, A1). Nu krijgt alleen het
   gekozen gewricht een boog met label; de rest laat alleen de groene band op het model zien. Zoals het meetgereedschap
   van Blender zelf: het mes toont alleen de hoek bij de cursor, en kiest met "Measurements" wat je ziet.
   Alleen voor gewrichten van een figuur (cj_figuur); een los gewricht tekent zoals altijd.
2. Label als pil: donkere, halfdoorzichtige achtergrond met ronde hoeken, een bolletje in de passingkleur en witte
   tekst. Zoals de liniaal en het mes van Blender (zwart, 50 procent, 4 px rand), maar iets donkerder en rond, zodat
   het op een grijs, oranje of turquoise model leesbaar blijft.
3. Donkere onderlijn onder een boog, zodat een groene boog ook op een licht model los staat.
Tekenen gebeurt alleen met scherm; de keuze zelf is ook zonder scherm te toetsen (toon)."""
import math

import bpy

STANDEN = (
    ("SELECTED", "Selected", "Show the bend range and label only for the selected joint"),
    ("ALL", "All", "Show the bend range and label for every joint of the figure"),
    ("NONE", "None", "Show no bend ranges or labels on the figure (clean view for renders)"),
)
ACHTER = (0.067, 0.071, 0.082, 0.86)  # #111215, 86 procent: donkerder dan Blender (50 procent), leest op elk model
ROOD_ACHTER = (0.86, 0.20, 0.20, 0.95)  # pil voorbij de stop: rood vlak met witte tekst
WIT = (1.0, 1.0, 1.0)
FIGUUR_X_ALLE = 0.7  # zelfde als scharnier_boog.FIGUUR_X en figuur_teken.FIGUUR_X (stand All)


def stand(context=None):
    wm = (context or bpy.context).window_manager
    return getattr(wm, "cj_labels", "ALL")


def gekozen(context, *delen):
    """True als een van de delen het actieve object is of geselecteerd is."""
    act = getattr(context.view_layer.objects, "active", None)
    for d in delen:
        if d is None:
            continue
        if d is act:
            return True
        try:
            if d.select_get():
                return True
        except RuntimeError:  # object niet in deze view layer
            pass
    return False


def toon(context, a, b):
    """Teken de boog en het label van dit gewricht? Los gewricht: altijd. Figuur: volgens de schakelaar."""
    if not (b is not None and b.get("cj_figuur")):
        return True
    s = stand(context)
    if s == "NONE":
        return False
    if s == "ALL":
        return True
    return gekozen(context, a, b)


def met_naam(context, b):
    """In de stand Selected staat de naam in het label ("Right knee  0-120°") in plaats van bovenin het beeld."""
    return stand(context) == "SELECTED" and b is not None and bool(b.get("cj_naam"))


def label_tekst(b, n, naam=False):
    """Tekst van een scharnierlabel bij een figuur: "120°", of met naam "Right knee  0–120°" (stand Selected)."""
    if naam and b.get("cj_naam"):
        return f"{b['cj_naam']}  0\u2013{n}°"
    return f"{n}°"


def figuur_x(context=None):
    """Verkleining van boog en wig bij een figuur: 0,7 als er meer tegelijk staan (stand All, zes waaiers naast
    elkaar mogen niet overlappen), heel (1,0) in de stand Selected, want dan staat er meestal maar één."""
    return 1.0 if stand(context) == "SELECTED" else FIGUUR_X_ALLE


def _rond_vlak(x0, y0, x1, y1, r, stappen=6):
    """Driehoeken van een rechthoek met ronde hoeken (straal r), als waaier vanuit het midden."""
    r = max(0.0, min(r, (x1 - x0) / 2.0, (y1 - y0) / 2.0))
    hoeken = ((x1 - r, y1 - r, 0), (x0 + r, y1 - r, 90), (x0 + r, y0 + r, 180), (x1 - r, y0 + r, 270))
    rand = []
    for cx, cy, start in hoeken:
        for i in range(stappen + 1):
            t = math.radians(start + 90.0 * i / stappen)
            rand.append((cx + r * math.cos(t), cy + r * math.sin(t)))
    mx, my = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    drie = []
    for i in range(len(rand)):
        p, q = rand[i], rand[(i + 1) % len(rand)]
        drie += [(mx, my, 0.0), (p[0], p[1], 0.0), (q[0], q[1], 0.0)]
    return drie


def _vlak(drie, kleur):
    import gpu
    from gpu_extras.batch import batch_for_shader
    sh = gpu.shader.from_builtin("UNIFORM_COLOR")
    sh.uniform_float("color", kleur)
    batch_for_shader(sh, "TRIS", {"pos": drie}).draw(sh)


def maat(tekst, px, schaal=1.0, bol=True):
    """(breed, hoog) van de pil in pixels, voor tekst met grootte px."""
    import blf
    blf.size(0, px)
    b, _h = blf.dimensions(0, tekst)
    _b, h = blf.dimensions(0, "0123456789°")
    pad_x, pad_y = 10.0 * schaal, 6.0 * schaal
    extra = (h * 0.55 + 7.0 * schaal) if bol else 0.0
    return b + 2 * pad_x + extra, h + 2 * pad_y


def pil(punt, tekst, px, schaal=1.0, accent=None, achter=ACHTER, tekstkleur=WIT):
    """Tekent een label als pil met het midden op punt. accent: kleur van het bolletje links (None: geen bolletje).
    Geeft het vak (x0, y0, x1, y1) terug, of None als er geen punt is."""
    import blf
    if punt is None:
        return None
    breed, hoog = maat(tekst, px, schaal, accent is not None)
    x0, y0 = punt.x - breed / 2.0, punt.y - hoog / 2.0
    x1, y1 = x0 + breed, y0 + hoog
    _vlak(_rond_vlak(x0, y0, x1, y1, hoog / 2.0), achter)
    blf.size(0, px)
    _b, h = blf.dimensions(0, "0123456789°")
    tx = x0 + 10.0 * schaal
    if accent is not None:
        r = h * 0.275
        cx, cy = tx + r, (y0 + y1) / 2.0
        _vlak(_rond_vlak(cx - r, cy - r, cx + r, cy + r, r, 4), (*accent[:3], 1.0))
        tx += 2 * r + 7.0 * schaal
    blf.disable(0, blf.SHADOW)
    blf.color(0, tekstkleur[0], tekstkleur[1], tekstkleur[2], 1.0)
    blf.position(0, tx, (y0 + y1) / 2.0 - h / 2.0, 0)
    blf.draw(0, tekst)
    return (x0, y0, x1, y1)


def onderlijn(regio, punten, dik):
    """Donkere, zachte lijn onder een boog (twee keer zo dik, 35 procent zwart)."""
    import gpu
    from gpu_extras.batch import batch_for_shader
    pts = [(x.x, x.y, 0.0) for x in punten if x is not None]
    if len(pts) < 2:
        return
    sh = gpu.shader.from_builtin("POLYLINE_UNIFORM_COLOR")
    sh.uniform_float("viewportSize", (regio.width, regio.height))
    sh.uniform_float("lineWidth", dik)
    sh.uniform_float("color", (0.0, 0.0, 0.0, 0.35))
    batch_for_shader(sh, "LINE_STRIP", {"pos": pts}).draw(sh)


def register():
    from .scharnier_boog import herteken
    bpy.types.WindowManager.cj_labels = bpy.props.EnumProperty(
        name="Labels", items=STANDEN, default="SELECTED",
        description="Which joints of a figure show their bend range and label in the viewport", update=herteken)


def unregister():
    if hasattr(bpy.types.WindowManager, "cj_labels"):
        del bpy.types.WindowManager.cj_labels
