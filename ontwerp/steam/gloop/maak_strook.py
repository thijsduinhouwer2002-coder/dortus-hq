# Gloop-versies op ware grootte in de echte strook van 120 px (Windows-build van Olaf, run 43415980604, schermen/steam-hol/main/strook-120.png).
# De oude Gloop wordt bedekt met hetzelfde stuk muur een tegel (48 px) naar links; daarna de nieuwe Gloop op schaal 3, anker midden onder op de vloer.
import os, sys
from PIL import Image
HIER = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HIER)
import maak_blad as mb
bron = sys.argv[1]; uit = sys.argv[2]
im = Image.open(bron).convert("RGBA")
X0, Y0, X1, Y1 = 380, 600, 720, 720   # uitsnede rond de schatkamer
hats = mb.hoeden(); keuze = [hats[0], hats[4], hats[1]]
rijen = []
def met(g):
    s = im.copy()
    patch = s.crop((524 - 48, 666, 582 - 48, 711)); s.paste(patch, (524, 666))
    if g is not None:
        G = g.resize((g.width * 3, g.height * 3), Image.NEAREST)
        cx, vloer = 552, 711
        s.paste(G, (cx - G.width // 2, vloer - G.height), G)
    return s.crop((X0, Y0, X1, Y1))
oud = im.crop((X0, Y0, X1, Y1))
rijen.append(("nu", oud))
for v in "ABC":
    st = Image.open(os.path.join(HIER, f"gloop_{v}.png"))
    rust = st.crop((0, 0, 20, 16))
    rijen.append((v, met(rust)))
    rijen.append((v + "+toren", met(mb.met_toren(rust, keuze, 3))))
W = (X1 - X0); H = (Y1 - Y0)
out = Image.new("RGBA", (W * 2 + 10, (H + 6) * 4), (20, 14, 26, 255))
for i, (n, r) in enumerate(rijen):
    if i == 0: out.paste(r, (0, 0))
    else:
        k = i - 1; out.paste(r, ((k % 2) * (W + 10), (1 + k // 2) * (H + 6)))
out.save(uit)
