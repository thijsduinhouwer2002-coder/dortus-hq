# Omslag voor de itch.io-proefpagina van Hats of the Fallen (Sanne, 27 nov 2026, issue #314).
# Maat itch.io: 630 x 500 (aangeraden door itch.io; GOK dat dit nog zo is, niet te lezen met curl).
# Opbouw: bureaublad met lucht en het logo bovenin, daaronder een ECHT beeld uit het spel (strook van 160 px hoog,
# uit een film van het spel zelf, Godot 4.3 --write-movie), 1,75x vergroot (het spel tekent 3D-figuren, geen harde pixelkunst, dus zacht vergroten),
# en onderaan een taakbalk. Zo zie je in één beeld wat het spel is: een hol boven op je taakbalk.
# Gebruik: python3 maak_omslag.py <beeld 1920x160 uit het spel> <x-start uitsnede> <uit.png> [schaal, standaard 1.75]
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

HIER = Path(__file__).resolve().parent
ROOT = HIER.parents[2]
LOGO = ROOT / "ontwerp/steam/winkelpagina/logo-1082x720.png"
W, H = 630, 500


def lucht(w, h):
    im = Image.new("RGB", (w, h))
    px = im.load()
    for y in range(h):
        t = y / max(1, h - 1)
        r = int(84 + (150 - 84) * t)
        g = int(158 + (205 - 158) * t)
        b = int(232 + (240 - 232) * t)
        for x in range(w):
            px[x, y] = (r, g, b)
    wolk = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(wolk)
    for (cx, cy, rx, ry) in [(70, 60, 90, 26), (130, 48, 60, 24), (520, 80, 110, 28), (580, 62, 60, 22)]:
        d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=235)
    wolk = wolk.filter(ImageFilter.GaussianBlur(10))
    im.paste(Image.new("RGB", (w, h), (250, 252, 255)), (0, 0), wolk)
    return im


def main():
    bron = Image.open(sys.argv[1]).convert("RGB")
    x0 = int(sys.argv[2])
    uit = sys.argv[3]
    schaal = float(sys.argv[4]) if len(sys.argv) > 4 else 1.75
    uw = round(W / schaal)  # zoveel px uit het spel
    strook = bron.crop((x0, 0, x0 + uw, bron.height)).resize((W, round(bron.height * schaal)), Image.LANCZOS)
    taak_h = 34
    strook_y = H - taak_h - strook.height
    im = lucht(W, strook_y + 4)
    doek = Image.new("RGB", (W, H), (30, 32, 40))
    doek.paste(im, (0, 0))
    doek.paste(strook, (0, strook_y))
    # taakbalk met een paar app-knopjes, de onze in het midden met een streepje eronder
    d = ImageDraw.Draw(doek)
    d.rectangle([0, H - taak_h, W, H], fill=(30, 33, 44))
    kleuren = [(80, 150, 240), (240, 200, 80), (110, 200, 130), (230, 110, 90), (200, 200, 210)]
    bx = W // 2 - 3 * 26
    for i, k in enumerate(kleuren):
        x = bx + i * 26
        d.rounded_rectangle([x, H - taak_h + 8, x + 18, H - taak_h + 26], radius=4, fill=k)
    # logo bovenin, gecentreerd in de lucht
    logo = Image.open(LOGO).convert("RGBA")
    # het logo heeft een bijna onzichtbare witte waas (alfa 1 tot 20) over het hele vlak; die gaf een licht kader
    logo.putalpha(logo.getchannel("A").point(lambda a: 0 if a < 24 else a))
    lh = strook_y - 22
    lw = int(logo.width * lh / logo.height)
    if lw > W - 60:
        lw = W - 60
        lh = int(logo.height * lw / logo.width)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    schaduw = Image.new("RGBA", logo.size, (0, 0, 0, 0))
    schaduw.putalpha(logo.getchannel("A").point(lambda a: 90 if a > 128 else 0))
    schaduw = schaduw.filter(ImageFilter.GaussianBlur(6))
    lx = (W - lw) // 2
    ly = (strook_y - lh) // 2 + 2
    doek.paste(logo, (lx, ly), logo)
    doek.save(uit)
    print(uit, doek.size)


if __name__ == "__main__":
    main()
