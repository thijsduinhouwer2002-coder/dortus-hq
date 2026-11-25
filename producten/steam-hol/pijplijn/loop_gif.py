"""Loop-GIF uit een heldenblad (Mila 25 nov 2026, issue 32).

Zet de beelden stap1 tot stap6 achter elkaar en schuift de held per beeld `stap_px` spelpixels naar rechts,
precies zoals het spel dat moet doen. Staat de voet op de vloer stil tegen de streepjes, dan glijdt hij niet.
Uit: producten/steam-hol/bewijs-loop/<naam>-loop-<maat>.gif, op ware maat (strook 120 px = 3 schermpixels per
spelpixel) en op 2x.

    python3 loop_gif.py ridder dief bard heks
"""
import json, os, sys
from PIL import Image, ImageDraw

HIER = os.path.dirname(os.path.abspath(__file__))
KUNST = os.path.join(HIER, "..", "godot", "kunst", "3d")
UIT = os.path.join(HIER, "..", "bewijs-loop")
STRAND = 40        # spelpixels hoog, net als de strook van 120 px op schaal 3
GROND = 30         # rij van de vloer in spelpixels
LUCHT = (246, 236, 214)
AARDE = (122, 84, 58)
STREEP = (92, 60, 40)


def gif(naam, schaal, duur=3.0):
    info = json.load(open(os.path.join(KUNST, "sprites.json")))[naam]
    blad = Image.open(os.path.join(KUNST, naam + ".png")).convert("RGBA")
    px = info["px"]; cw, ch = info["cel_px"]
    frames = info["frames"]
    stappen = [frames.index(f"stap{i}") for i in range(1, 7)]
    fps = info.get("loop_fps", 10)
    stap = info["stap_px"]
    n = round(duur * fps)
    breed = max(60, round(stap * n + cw / px + 8))   # spelpixels
    W, H = breed * schaal, STRAND * schaal
    s = schaal / px                                   # schermpixels per bladpixel
    cel_w, cel_h = round(cw * s), round(ch * s)
    beelden = []
    for k in range(n):
        im = Image.new("RGBA", (W, H), LUCHT + (255,))
        d = ImageDraw.Draw(im)
        d.rectangle((0, GROND * schaal, W, H), fill=AARDE + (255,))
        for x in range(0, breed, 4):                  # streepjes op de vloer, elke 4 spelpixels
            d.rectangle((x * schaal, GROND * schaal, x * schaal + max(1, schaal // 2), GROND * schaal + schaal), fill=STREEP + (255,))
        i = stappen[k % 6]
        cel = blad.crop((i * cw, 0, (i + 1) * cw, ch)).resize((cel_w, cel_h), Image.LANCZOS)
        x_held = 4 + cw / px / 2 + stap * k           # spelpixels, anker van de held
        links = round((x_held - info["anker_x"] / px) * schaal)
        boven = round((GROND - info["nul_y"][i]) * schaal)   # nulpunt van het model (de vloer) op de grond
        im.alpha_composite(cel, (links, boven))
        beelden.append(im.convert("RGB").quantize(colors=255, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE))
    os.makedirs(UIT, exist_ok=True)
    uit = os.path.join(UIT, f"{naam}-loop-{'ware-maat' if schaal == 3 else '2x'}.gif")
    beelden[0].save(uit, save_all=True, append_images=beelden[1:], duration=round(1000 / fps), loop=0, optimize=True)
    print(uit, f"{n} beelden, {fps} fps, stap {stap} spelpx, {W}x{H}")


if __name__ == "__main__":
    for naam in sys.argv[1:] or ["ridder", "dief", "bard", "heks"]:
        gif(naam, 3)
        gif(naam, 6)
