"""Fit test logic without bpy: which clearances to test, block layout, and the saved clearance per printer and
material (a JSON text in the add-on preferences). Tested with plain Python in e2e/test_logica.py.

The fit test is one small block with four holes for your own pin (same diameter, same depth as in Split), each
with a different clearance engraved in front of it, plus four pins. Print it, push a pin in every hole, keep
the clearance of the hole where the pin goes in by hand and does not wobble."""
import json

AANTAL = 4
STAP_MM = 0.05
MAX_MM = 1.0         # highest clearance the setting allows
LETTER_MM = 4.0      # height of the engraved clearance
GRAVEER_MM = 0.6     # engraving depth
VLOER_MM = 2.0       # material under the deepest hole
RUIMTE_MM = 1.5      # gap between hole and its number

MATERIALEN = (
    ("PLA", "PLA", "PLA and PLA+"),
    ("PETG", "PETG", "PETG"),
    ("ABS", "ABS / ASA", "ABS and ASA"),
    ("TPU", "TPU", "Flexible filament"),
    ("RESIN", "Resin", "Resin printer"),
    ("OTHER", "Other", "Any other material"),
)

# Start clearance (mm per side) per material, used until a fit test is saved for that printer and material.
# The fit test then tests one step below to two steps above, so the value that fits is on the block.
# Sources: SnapSplit profiles.py (PLA 0.20, PETG 0.30, ABS/ASA 0.25, TPU 0.35, resin 0.10) and Hubs (SLA
# needs about 0.6 of the FDM clearance). Where they differ the start sits so both are on the test block.
STARTSPELING = {"PLA": 0.20, "PETG": 0.25, "ABS": 0.25, "TPU": 0.30, "RESIN": 0.10, "OTHER": 0.20}


def startspeling(materiaal):
    """Start clearance for a material; unknown gives the PLA value."""
    return STARTSPELING.get(materiaal, STARTSPELING["PLA"])


def spelingen(s):
    """Four clearances (mm per side) around s: one step below, s itself, two steps above. Never below 0 and
    never above MAX_MM (else a button would save a value the setting cannot hold, keurder M3)."""
    start = min(max(0.0, round(s - STAP_MM, 3)), MAX_MM - (AANTAL - 1) * STAP_MM)  # all four stay settable
    return [round(start + k * STAP_MM, 3) for k in range(AANTAL)]


def tekst(s):
    """Engraved text for a clearance: 0.15 (two decimals, always with a dot)."""
    return f"{s:.2f}"


def sleutel(printer, materiaal):
    return f"{printer}|{materiaal}"


def lees(json_tekst):
    """Saved clearances {key: mm}; broken or empty text gives {}."""
    try:
        d = json.loads(json_tekst or "{}")
    except (ValueError, TypeError):
        return {}
    if not isinstance(d, dict):
        return {}
    uit = {}
    for k, v in d.items():
        try:
            v = float(v)
        except (TypeError, ValueError):
            continue
        if 0.0 <= v <= 1.0:
            uit[str(k)] = round(v, 3)
    return uit


def bewaar(json_tekst, printer, materiaal, s):
    """New JSON text with s saved for this printer and material."""
    d = lees(json_tekst)
    d[sleutel(printer, materiaal)] = round(float(s), 3)
    return json.dumps(d, sort_keys=True)


def opgeslagen(json_tekst, printer, materiaal):
    """Saved clearance for this printer and material, or None."""
    return lees(json_tekst).get(sleutel(printer, materiaal))


def maten(pen_d, pen_lengte, wand, s, extra_diepte):
    """Layout of the block in mm. Holes along X on the top face, numbers in front of them (toward -Y).
    Returns a dict with the box (mn, mx), every hole (center on the top face, r_gat, depth, clearance) and every
    number (center on the top face, text, height)."""
    lijst = spelingen(s)
    r_max = pen_d / 2.0 + lijst[-1]
    w = max(wand, 2.0) + 1.0  # a test block may be a bit sturdier than the minimum wall
    breedte_tekst = (4 * len(tekst(lijst[-1])) - 1) * LETTER_MM / 5.0
    cel = max(2 * r_max + 2 * w, breedte_tekst + 5.0)  # clear gap between two numbers
    diepte = pen_lengte / 2.0 + extra_diepte
    hoogte = diepte + VLOER_MM
    y_voor = -(r_max + RUIMTE_MM + LETTER_MM + w)
    y_achter = r_max + w
    gaten, nummers = [], []
    for k, sp in enumerate(lijst):
        x = (k + 0.5) * cel
        gaten.append({"p": [x, 0.0, hoogte], "as": 2, "teken": 1, "r_gat": pen_d / 2.0 + sp, "diepte": diepte,
                      "pen_d": pen_d, "speling": sp})
        nummers.append({"tekst": tekst(sp), "p": [x, -(r_max + RUIMTE_MM + LETTER_MM / 2.0), hoogte],
                        "as": 2, "teken": 1, "h": LETTER_MM, "breed": cel - 1.0})
    return {"mn": [0.0, y_voor, 0.0], "mx": [AANTAL * cel, y_achter, hoogte], "gaten": gaten,
            "nummers": nummers, "spelingen": lijst, "cel": cel}
