"""Beelden voor het YouTube-kanaal Dortus (@dortusstudio). Chris, 16 nov 2026, run 58 (arm aangepast in run 59).
Bouwt voort op het uniform van Mila (ontwerp/merk/bron/maak_uniform.py): zelfde deur-D, kleuren,
licht en spullen. Er komt alleen een kogelgewricht bij (Click Joints), want het kanaal gaat vooral over
Blender-tips voor 3D-printen. Draai: python3 maak_kanaal.py  (schrijft in deze map)."""
import os, sys, subprocess
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "../../../ontwerp/merk/bron"))
import maak_uniform as U   # alleen lezen, we schrijven niets in Abels map

W, H = 2560, 1440
# veilige zone (DERDEN, YouTube Help 10456525: 1235 x 338 op 2048 breed, dus 1546 x 423 op 2560)
VX0, VX1 = (W - 1546) / 2, (W + 1546) / 2      # 507 .. 2053
VY0, VY1 = (H - 423) / 2, (H + 423) / 2        # 508.5 .. 931.5

def gewricht(cx, cy, z):
    """Een geprinte arm met een kogelgewricht, zoals Click Joints hem maakt: onderarm (lila) plat op de vloer,
    bovenarm (creme) buigt omhoog vanuit de kogel. cx, cy = midden van het gewricht.
    Run 59, kan-punt van Daan (16 nov): de kom is een grote lila C die de witte kogel half omsluit, open naar
    de bovenarm, en beide delen zijn even dik; zo lees je een scharnier en geen hendel. Geen tweede kogel."""
    import math
    st = f'stroke="#2a1d33" stroke-width="{z*0.03:.1f}" stroke-linejoin="round"'
    r = z * 0.2                                                  # kogel
    dik = z * 0.28                                               # dikte van beide armdelen
    hoek = -40                                                   # bovenarm 40 graden omhoog
    uit = f'<ellipse cx="{cx-z*0.35:.1f}" cy="{cy+z*0.24:.1f}" rx="{z*0.85:.1f}" ry="{z*0.09:.1f}" fill="#000" fill-opacity="0.4"/>'
    # onderarm (achter de kom)
    uit += (f'<rect x="{cx-z*1.05:.1f}" y="{cy-dik/2:.1f}" width="{z*0.85:.1f}" height="{dik:.1f}" rx="{dik*0.45:.1f}" fill="{U.LILA}" {st}/>'
            f'<path d="M{cx-z*0.95:.1f},{cy-dik*0.15:.1f} H{cx-z*0.5:.1f}" stroke="#c9b9ff" stroke-width="{z*0.04:.1f}" stroke-linecap="round"/>')
    # bovenarm, even dik, vanuit het midden van de kogel
    uit += (f'<g transform="rotate({hoek} {cx:.1f} {cy:.1f})">'
            f'<rect x="{cx:.1f}" y="{cy-dik/2:.1f}" width="{z*0.9:.1f}" height="{dik:.1f}" rx="{dik*0.45:.1f}" fill="{U.CREME}" {st}/>'
            f'<path d="M{cx+z*0.32:.1f},{cy-dik*0.22:.1f} H{cx+z*0.78:.1f}" stroke="#ffffff" stroke-width="{z*0.04:.1f}" stroke-linecap="round"/></g>')
    # kogel
    uit += (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="#ffffff" {st}/>'
            f'<circle cx="{cx-r*0.35:.1f}" cy="{cy-r*0.4:.1f}" r="{r*0.22:.1f}" fill="#fffdf5"/>')
    # kom: lila C om de kogel, open naar de bovenarm (opening 2 x 55 graden)
    R1, R0 = r * 1.6, r * 1.06
    a1, a2 = math.radians(hoek + 55), math.radians(hoek - 55 + 360)
    def pt(R, a): return f"{cx+R*math.cos(a):.1f},{cy+R*math.sin(a):.1f}"
    uit += (f'<path d="M{pt(R1,a1)} A{R1:.1f},{R1:.1f} 0 1 1 {pt(R1,a2)} L{pt(R0,a2)} '
            f'A{R0:.1f},{R0:.1f} 0 1 0 {pt(R0,a1)} Z" fill="{U.LILA}" {st}/>')
    return uit

def banner():
    # het woordmerk links; zijn D is de deur, het licht valt eruit naar rechts over de vloer en daarin
    # liggen de spullen. Geen tweede grote D (les keuring Daan 6, Steam-kop).
    h = 210; wx, wy = VX0 + 40, VY0 + 40
    s = h / 560
    vloer = wy + h + 6                  # vloerlijn net onder het woordmerk
    ox = wx + 22 * s + 300 * s           # onder de lichte opening van de D
    bundel = (f'<linearGradient id="bb" x1="0" y1="0" x2="1" y2="0">'
              f'<stop offset="0" stop-color="{U.GOUD}" stop-opacity="0.6"/><stop offset="0.55" stop-color="{U.GOUD}" stop-opacity="0.3"/>'
              f'<stop offset="1" stop-color="{U.GOUD}" stop-opacity="0"/></linearGradient>'
              f'<filter id="zb" x="-0.1" y="-0.5" width="1.2" height="2"><feGaussianBlur stdDeviation="9"/></filter>')
    rechts = VX1 + 120
    inhoud = (f'<defs>{bundel}</defs><rect width="{W}" height="{H}" fill="{U.NACHT}"/>'
              f'<rect y="{vloer:.0f}" width="{W}" height="{H-vloer:.0f}" fill="url(#vloerdonker)"/>'
              f'<circle cx="{wx+150:.0f}" cy="{wy+110:.0f}" r="560" fill="url(#gloed)" opacity="0.85"/>'
              f'<circle cx="{(VX0+VX1)/2:.0f}" cy="{H/2:.0f}" r="1100" fill="url(#gloed)" opacity="0.22"/>'
              + U.sterren(W, vloer, int(W * vloer / 9000), zaad=23)
              + f'<g filter="url(#zb)"><path d="M{ox:.0f},{vloer-6:.0f} L{ox:.0f},{vloer+10:.0f} L{rechts:.0f},{vloer+150:.0f} L{rechts:.0f},{vloer-40:.0f} Z" fill="url(#bb)"/></g>'
              + f'<ellipse cx="{ox+30:.0f}" cy="{vloer+2:.0f}" rx="110" ry="12" fill="#fff6c9" fill-opacity="0.4"/>'
              + U.woord(wx, wy, h)
              # wat er uit de deur rolt, op de vloer rechts van het woord; nieuwste (gewricht) het verst weg en het grootst
              + U.haakjes(VX0 + 960, vloer - 40, 74)
              + U.kroon(VX0 + 1100, vloer - 24, 84)
              + U.dobbel(VX0 + 1225, vloer - 34, 62)
              + gewricht(VX0 + 1420, vloer - 30, 120)
              # regels onder de vloer, in de veilige zone
              + f'<text x="{wx+6:.0f}" y="{vloer+78:.0f}" font-family="Inter" font-weight="500" font-size="56" fill="{U.CREME}">Blender tips for 3D printing</text>'
              + f'<text x="{wx+6:.0f}" y="{vloer+134:.0f}" font-family="Inter" font-weight="500" font-size="38" fill="{U.LILA}">Focused tools today, small games on the way</text>')
    return U.svg(W, H, inhoud)

def schrijf(naam, svgtekst, breed):
    p = os.path.join(HIER, naam + ".svg")
    open(p, "w").write(svgtekst)
    subprocess.run(["rsvg-convert", p, "-w", str(breed), "-o", os.path.join(HIER, naam + ".png")], check=True)

if __name__ == "__main__":
    schrijf("banner-2560x1440", banner(), W)
    # profielfoto: de goedgekeurde avatar v2 (Daan, 10 nov), op 800 x 800
    subprocess.run(["rsvg-convert", os.path.join(HIER, "../../../ontwerp/merk/avatar-v2.svg"), "-w", "800",
                    "-o", os.path.join(HIER, "profielfoto-800.png")], check=True)
    # watermerk in video's (min 150 x 150, onder 1 MB): kleine D, leest beter op 150 dan de grote
    subprocess.run(["rsvg-convert", os.path.join(HIER, "../../../ontwerp/merk/merkteken-klein.svg"), "-w", "300",
                    "-o", os.path.join(HIER, "watermerk-300.png")], check=True)
