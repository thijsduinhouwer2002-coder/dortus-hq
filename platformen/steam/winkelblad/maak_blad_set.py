# Maakt het overzichtsblad van de gekeurde winkelset voor de toets met Thijs (wo 18 nov 20:00).
# Olaf, 17 nov 2026. Draaien vanuit de repo-root: python3 platformen/steam/winkelblad/maak_blad_set.py
from PIL import Image, ImageDraw, ImageFont
import os

MAP = "ontwerp/steam/winkelpagina"
ICOON = "ontwerp/steam/icoon"
UIT = "platformen/steam/winkelblad/blad-winkelset-17nov.png"

BREED = 2400
ACHTER = (27, 40, 56)       # Steam-blauw donker
KAART = (35, 52, 72)
TEKST = (230, 236, 242)
GRIJS = (150, 168, 186)
GOUD = (232, 190, 92)

f_kop = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44)
f_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
f_klein = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)


def laad(pad, breedte=None, hoogte=None):
    im = Image.open(pad).convert("RGBA")
    if breedte:
        h = round(im.height * breedte / im.width)
        im = im.resize((breedte, h), Image.LANCZOS)
    elif hoogte:
        b = round(im.width * hoogte / im.height)
        im = im.resize((b, hoogte), Image.LANCZOS)
    return im


def ruit(im):
    """Doorzichtig beeld op een ruitjesachtergrond, zodat je ziet wat doorzichtig is."""
    r = Image.new("RGBA", im.size, (60, 60, 60, 255))
    d = ImageDraw.Draw(r)
    for y in range(0, im.height, 16):
        for x in range(0, im.width, 16):
            if (x // 16 + y // 16) % 2:
                d.rectangle([x, y, x + 15, y + 15], fill=(90, 90, 90, 255))
    r.alpha_composite(im)
    return r


# (titel, bestand, weergavebreedte of -hoogte, toelichting)
rijen = [
    [("Header capsule 920x430 (ook library header)", "header-920x430.png", {"breedte": 920}, "toren 6b, ja Daan"),
     ("Main capsule 1232x706", "main-1232x706.png", {"breedte": 1232}, "toren 8, ja Daan")],
    [("Small capsule 462x174", "klein-462x174.png", {"breedte": 462}, "toren 6b, ja Daan"),
     ("Zo klein toont Steam hem ook: 184x69", "klein-462x174.png", {"breedte": 184}, "zoekresultaat"),
     ("en 120x45", "klein-462x174.png", {"breedte": 120}, "lijstjes"),
     ("Vertical capsule 748x896", "staand-748x896.png", {"hoogte": 600}, "staand ronde 1, ja Daan"),
     ("Library capsule 600x900", "library-600x900.png", {"hoogte": 600}, "bibliotheek 8, ja Daan")],
    [("Library hero 3840x1240 (hier verkleind tot 1500 breed)", "hero-3840x1240.png", {"breedte": 1500}, "kleur H, zonder tekst"),
     ("Library logo 1082x720, doorzichtig", "logo-1082x720.png", {"breedte": 640}, "ruitjes = doorzichtig")],
    [("Event cover 800x450 (verplicht bij aankondigingen)", "event-cover-800x450.png", {"breedte": 800}, "ja Daan"),
     ("Event header 1920x622", "event-header-1920x622.png", {"breedte": 1340}, "ja Daan")],
]

schermen = ["1-hoedentoren.png", "2-bureaublad.png", "3-hap.png", "4-val.png", "5-kaartje.png"]


def rij_hoogte(rij):
    hs = []
    for _, bestand, maat, _ in rij:
        im = laad(os.path.join(MAP, bestand), **maat)
        hs.append(im.height)
    return max(hs) + 90


MARGE = 50
TUSSEN = 40
hoogte = 140
for rij in rijen:
    hoogte += rij_hoogte(rij) + TUSSEN
scherm_b = (BREED - 2 * MARGE - 4 * 24) // 5
scherm_h = round(scherm_b * 1080 / 1920)
hoogte += scherm_h + 90 + TUSSEN
hoogte += 260 + 90  # iconen
hoogte += 60

blad = Image.new("RGBA", (BREED, hoogte), ACHTER)
d = ImageDraw.Draw(blad)
d.text((MARGE, 40), "Hats of the Fallen: winkelset 3D, gekeurd door Daan (17 nov). Voor Thijs, wo 18 nov 20:00", font=f_kop, fill=TEKST)
d.text((MARGE, 98), "Alles op ware grootte tenzij anders vermeld. Zeg per beeld ja of nee; bij nee gaat alleen dat beeld terug naar een ronde.", font=f_klein, fill=GRIJS)

y = 140
for rij in rijen:
    rh = rij_hoogte(rij)
    x = MARGE
    for titel, bestand, maat, uitleg in rij:
        im = laad(os.path.join(MAP, bestand), **maat)
        if bestand.startswith("logo"):
            im = ruit(im)
        d.text((x, y), titel, font=f_label, fill=GOUD)
        d.text((x, y + 32), uitleg, font=f_klein, fill=GRIJS)
        blad.alpha_composite(im, (x, y + 70))
        x += int(max(im.width, d.textlength(titel, font=f_label))) + 40
    y += rh + TUSSEN

d.text((MARGE, y), "Schermafbeeldingen 1920x1080 (ja Daan 16 nov; spelteksten in beeld zijn CONCEPT tot Thijs ze schrijft)", font=f_label, fill=GOUD)
x = MARGE
for s in schermen:
    im = laad(os.path.join(MAP, "schermen-steam", s), breedte=scherm_b)
    blad.alpha_composite(im, (x, y + 50))
    d.text((x, y + 56 + scherm_h), s, font=f_klein, fill=GRIJS)
    x += scherm_b + 24
y += scherm_h + 90 + TUSSEN

d.text((MARGE, y), "Iconen: shortcut 256x256 PNG en app icon 184x184 JPG (ware grootte)", font=f_label, fill=GOUD)
x = MARGE
for bestand in ["icoon-tegel-256.png", "steam-community-184.jpg"]:
    im = ruit(laad(os.path.join(ICOON, bestand)))
    blad.alpha_composite(im, (x, y + 50))
    d.text((x, y + 56 + im.height), bestand, font=f_klein, fill=GRIJS)
    x += im.width + 60

blad.convert("RGB").save(UIT, optimize=True)
print(UIT, blad.size)
