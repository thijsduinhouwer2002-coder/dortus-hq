"""Abel, run 5: trekt de scharnieren in Mila's v2-beelden gelijk met avatar v2 (Daan, keuring 4, kan).
Zelfde regel als Mila's avatar v2 in maak_uniform.py: SCH_X -22 -> -12 en SCH_W 44 -> 50 (scharnier half in de D).
Verder verandert er niets aan het beeld. Draai: python3 bron/abel_scharnier_v2.py (vanuit merk/)."""
import re, subprocess, sys
PAREN = [("steam-logo-1200x460-v2", "steam-logo-1200x460-v2b"),
         ("og-1200x630-v2", "og-1200x630-v2b"), ("og-1200x630-v2-nu", "og-1200x630-v2b-nu"),
         ("social-1280x640-v2", "social-1280x640-v2b"), ("social-1280x640-v2-nu", "social-1280x640-v2b-nu")]
pat = re.compile(r'<rect x="([0-9.]+)" y="([0-9.]+)" width="([0-9.]+)" height="([0-9.]+)" rx="([0-9.]+)" fill="#ffd25c"/>')
def nieuw(m):
    x, y, w, h, rx = map(float, m.groups())
    s = w / 44
    if abs(h - 70 * s) > 0.2 or abs(rx - 14 * s) > 0.2:
        return m.group(0)            # geen scharnier
    return f'<rect x="{x + 10*s:.1f}" y="{y:.1f}" width="{50*s:.1f}" height="{h:.1f}" rx="{rx:.1f}" fill="#ffd25c"/>'
for oud, nw in PAREN:
    t = open(f"{oud}.svg").read()
    t2, n = pat.subn(nieuw, t)
    open(f"{nw}.svg", "w").write(t2)
    w = re.search(r'width="(\d+)"', t2).group(1)
    subprocess.run(["rsvg-convert", f"{nw}.svg", "-w", w, "-o", f"{nw}.png"], check=True)
    print(nw, n, "scharnieren")
