# Vormen van Mila's krabwereld v2 (ontwerp/garmin/bron/werelden_v2.py, 12 nov) als gegevens voor de bouw.
# Gebruik: python3 bron/krab_v2_vormen.py > bron/krab-v2-vormen.json
# Mila tekent de teenslipper met een formule (82 punten). Voor het horloge maken we er een veelhoek van hoogstens
# 32 punten van, in de lokale maat van de slipper (hak op x 0, neus op x 62, y omlaag, zonder draaiing en schaal):
# de bouw draait en schaalt zelf (hoek en sch per scherm). Het script meet hoe ver de dunne veelhoek van de
# echte omtrek afwijkt en weigert boven 0,6 (1/260 D bij sch 1).
import json, math, sys
def w(x):
    hak = math.sqrt(max(0, 13 ** 2 - x ** 2)) if x < 0 else 13 - 4.2 * min(1, x / 26)
    neus = math.sqrt(max(0, 15 ** 2 - (x - 50) ** 2)) if x > 50 else 8.8 + 6.2 * min(1, max(0, (x - 26) / 24))
    return hak if x < 26 else neus
def omtrek(n):
    xs = [-13 + i * 78 / n for i in range(n + 1)]
    return [(x, -w(x) * .8) for x in xs] + [(x, w(x) * .8) for x in reversed(xs)]
def afstand(p, a, b):
    (px, py), (ax, ay), (bx, by) = p, a, b
    dx, dy = bx - ax, by - ay
    t = 0 if dx == dy == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    return math.hypot(px - ax - t * dx, py - ay - t * dy)
vol = omtrek(40)
# Douglas-Peucker tot hoogstens 32 punten
def dp(pts, eps):
    if len(pts) < 3: return pts
    k, m = max(((i, afstand(pts[i], pts[0], pts[-1])) for i in range(1, len(pts) - 1)), key=lambda t: t[1])
    if m <= eps: return [pts[0], pts[-1]]
    return dp(pts[:k + 1], eps)[:-1] + dp(pts[k:], eps)
eps = 0.1
half = len(vol) // 2
while True:
    dun = dp(vol[:half], eps)[:-1] + dp(vol[half:] + [vol[0]], eps)[:-1]
    if len(dun) <= 32: break
    eps += 0.05
fout = max(min(afstand(p, dun[i], dun[(i + 1) % len(dun)]) for i in range(len(dun))) for p in omtrek(200))
assert fout <= 0.6, 'veelhoek wijkt %.2f af' % fout
r1 = lambda p: [round(p[0], 1), round(p[1], 1)]
uit = {
    'bron': 'ontwerp/garmin/bron/werelden_v2.py (Mila, 12 nov 2026), functies slipper, bandje, wereld_onder',
    'eenheid': '1/260 D; slipper in eigen maat (hak 0,0; neus x 62), bouw draait (hoek) en schaalt (sch)',
    'slipper': {'zool': [r1(p) for p in dun], 'kleur': 'FF55AA', 'rand': 'FFFFFF', 'rand_dik': 2.2,
                'glans': {'p': [[30, -4.5], [46, -6], [58, -4], [46, -3]], 'kleur': 'FFAAFF'},
                'teen': {'p': [[52, -1], [57, -3.5], [61, -1], [57, 1.5]], 'kleur': 'AA0055'},
                'bandje': {'paal': [50, -6], 'paal_r': 3, 'kanten': [[24, -9.5], [26, 9]], 'kant_r': 2.1, 'dik': 5, 'kleur': 'FFFFFF'},
                'afwijking': round(fout, 2), 'punten': len(dun)},
    'onder_water': {
        'verder': [[40, 176, 60, 26], [150, 186, 70, 20], [240, 168, 46, 30]],
        'ver': [[10, 192, 52, 36], [78, 208, 46, 20], [186, 206, 50, 20], [252, 186, 50, 40]],
        'zand': [{'kleur': 'AAAA55', 'vak': [-40, 222, 300, 330]}, {'kleur': 'FFFFAA', 'vak': [-30, 226, 290, 330]}],
        'rots_links': {'c': [36, 202], 'r': [34, 26], 'kleur': '5555AA', 'rand': 'AAAAFF', 'rand_dik': 2.2},
        'anemoon': {'voet': [36, 180, 22, 7], 'voet_kleur': 'AA55FF', 'y0': 180, 'tentakels': [[18, 12, 158], [26, 22, 150], [36, 36, 146], [46, 50, 150], [54, 60, 160]],
                    'dik': 5.6, 'rand_dik': 8.6, 'top_r': 3.6, 'top_rand_r': 4.3, 'kleur': 'AA55FF', 'top': 'FF55AA', 'rand': 'FFFFFF'},
        'rots_rechts': {'c': [222, 210], 'r': [30, 22], 'kleur': '5555AA', 'rand': 'AAAAFF'},
        'zeester': {'c': [218, 197], 'r_buiten': 11, 'r_binnen': 4.6, 'kleur': 'FFFF55', 'rand': 'FFFFFF', 'rand_dik': 1.8},
        'held': {'x': 106, 'slipper_x': 100, 'slipper_sch_per_maat': 1.3 / 30, 'slipper_dy_per_maat': 0.62, 'hoek': -4,
                 'schaduw': {'dx': 40, 'dy': 17, 'rx': 54, 'ry': 6, 'kleur': 'AAAA55'}},
        'mip': {'dag': {'water': ['005555', '000055'], 'grens_y': 150, 'rand': '0055FF', 'ver': '000055', 'verder': '0055AA'},
                'nacht': {'water': ['000055', '000055'], 'rand': '5555FF', 'ver': '0000AA', 'verder': '000055'}},
        'oppervlak': {'y': 7, 'amp': 2.5, 'golven': 5},
    },
}
json.dump(uit, sys.stdout, indent=1)
