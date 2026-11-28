"""r3 van de YouTube-miniatuur (#346, Beeldmaker): r2 plus de echte regels Diameter en Clearance uit het paneel.

Gemini in de kop-aan-kop-test van r2: "Show more of the configuration settings panel" en "Add visual indicators of
customization options or tolerances". Uitsnede uit het echte schermbeeld Blender 5.3.0
(ontwerp/pro-galerij/beelden/paneel-rig-scherm-na.jpg, Pro 1.2.9: Diameter 7.0 Auto, Clearance 0.20), als kaartje onder
het paneel van r2. Verder niets veranderd.
    python3 miniatuur_r3.py <yt-pro-r2-1280x720.jpg> <paneel-rig-scherm-na.jpg> <uit.jpg>
"""
import sys
from PIL import Image, ImageDraw, ImageFilter

r2, scherm, uit = sys.argv[1:4]
W, H = 2560, 1440
im = Image.open(r2).convert("RGB").resize((W, H), Image.LANCZOS).convert("RGBA")
GOUD = (255, 185, 56)
rij = Image.open(scherm).convert("RGBA").crop((2474, 495, 2820, 571))
B = 600  # breedte van de regels in px op 2560
k = B / rij.width
rij = rij.resize((B, int(rij.height * k)), Image.LANCZOS)
pad = 10
kaart = Image.new("RGBA", (B + 2 * pad, rij.height + 2 * pad), (48, 48, 48, 255))
kaart.alpha_composite(rij, (pad, pad))
X, top = 114, 1262  # onder het paneel van r2 (dat eindigt op y ±1246)
sl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sl).rounded_rectangle([X - 6, top + 12, X + kaart.width + 6, top + kaart.height + 26], radius=22, fill=(0, 0, 0, 200))
im.alpha_composite(sl.filter(ImageFilter.GaussianBlur(20)))
m = Image.new("L", kaart.size, 0)
ImageDraw.Draw(m).rounded_rectangle([0, 0, kaart.width - 1, kaart.height - 1], radius=18, fill=255)
im.paste(kaart, (X, top), m)
d = ImageDraw.Draw(im)
d.rounded_rectangle([X, top, X + kaart.width - 1, top + kaart.height - 1], radius=18, outline=(90, 80, 110, 255), width=3)
out = im.convert("RGB").resize((1280, 720), Image.LANCZOS)
out.save(uit, quality=92)
out.resize((320, 180), Image.LANCZOS).save(uit.replace(".jpg", "-320.jpg"), quality=92)
print("klaar", uit, kaart.size, "top", top)
