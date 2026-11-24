"""Contactblad etalage-audit 24 nov 2026: kleine versie van elk beeld dat een klant nu ziet, met het cijfer (deel C).
Gebruik: python3 -I contactblad.py <map met downloads> <uit.png>
De downloads zijn met curl gehaald (zie organisatie/etalage-audit-2026-11-24.md). Niets wordt geplaatst."""
import os, sys
from PIL import Image, ImageDraw, ImageFont

BRON = sys.argv[1]
UIT = sys.argv[2]
F = '/usr/share/fonts/opentype/inter/'
def font(naam, maat):
    try:
        return ImageFont.truetype(F + naam, maat)
    except OSError:
        return ImageFont.load_default()
KOP = font('Inter-Bold.otf', 34); SUB = font('Inter-Regular.otf', 20)
LBL = font('Inter-Medium.otf', 16); CIJ = font('Inter-Bold.otf', 30)

# (winkel, [(code, bestand, korte naam, cijfer)])
GROEPEN = [
 ("Gumroad: Click Joints Pro ($19, sale do 26 nov)", [
  ("G1", "gumroad/pro-cover-1.png", "cover 1 tekenpop", 7),
  ("G2", "gumroad/pro-cover-2.png", "cover 2 MakeHuman-scherm", 4),
  ("G3", "gumroad/pro-cover-3.png", "cover 3 elleboog 0-115", 4),
  ("G4", "gumroad/pro-cover-4.png", "cover 4 +3 past limit", 3),
  ("G5", "gumroad/pro-cover-5.png", "cover 5 grijze buis 20", 2),
  ("G6", "gumroad/pro-cover-6.png", "cover 6 grijze buis +8", 2),
  ("G7", "gumroad/pro-thumb.png", "vierkant (Discover)", 4),
  ("G8", "gumroad/free-otgj.png", "winkel-avatar (standaard)", 2),
  ("F1", "gumroad/free-cover-1.jpg", "gratis: cover", 6)]),
 ("Superhive: Click Joints Pro", [
  ("S1", "superhive/featured.jpg", "featured tekenpop", 7),
  ("S2", "superhive/gal-1.jpg", "galerij 1 +3 past limit", 3),
  ("S3", "superhive/gal-2.jpg", "galerij 2 elleboog", 4),
  ("S4", "superhive/gal-3.jpg", "galerij 3 grijze buis", 2),
  ("S5", "superhive/gal-4.jpg", "galerij 4 grijze buis +8", 2),
  ("S6", "superhive/yt-4-3l3MZZWPc.jpg", "video-beeld", 4),
  ("S7", "superhive/avatar.jpg", "avatar Dortus", 7)]),
 ("Blender Extensions: Click Joints (gratis)", [
  ("B1", "blender/icoon.png", "icoon", 7),
  ("B2", "blender/featured.webp", "featured", 5),
  ("B3", "blender/preview-1.webp", "preview Drag the bend", 5),
  ("B4", "blender/preview-2.webp", "preview Good fit", 5),
  ("B5", "blender/video-thumb.webp", "video-beeld", 3)]),
 ("dortus.com", [
  ("D1", "dortus/assets_og-dortus-home.png", "deelbeeld home", 7),
  ("D2", "dortus/click-joints_poster-1200.jpg", "kaart Click Joints", 5),
  ("D3", "dortus/ebb_og-1200.jpg", "kaart Ebb", 7),
  ("D4", "dortus/rollwright_poster-1200.jpg", "kaart Rollwright", 7),
  ("D5", "dortus/bison-flex_poster-v2.jpg", "kaart Bison & Flex", 7),
  ("D6", "dortus/assets_hats-of-the-fallen-462.jpg", "kaart Hats", 6),
  ("D7", "dortus/assets_devlog_hats-week-1.jpg", "devlog Hats", 5),
  ("D8", "dortus/click-joints_bend-loop-first.jpg", "/click-joints held", 6),
  ("D9", "dortus/click-joints_bend.jpg", "/click-joints bend", 5),
  ("D10", "dortus/click-joints_panel.jpg", "/click-joints paneel", 5),
  ("D11", "dortus/click-joints_pro-rig.jpg", "/click-joints Pro-rig", 4)]),
 ("YouTube (beeld bij de video)", [
  ("Y1", "youtube/yt-awtDyH5hOPI.jpg", "rig to print (221)", 4),
  ("Y2", "youtube/yt-lcUBuWMaJ_A.jpg", "how far knee (1195)", 4),
  ("Y3", "youtube/yt-pCyyQ4Qa9Gw.jpg", "printable parts (648)", 3),
  ("Y4", "youtube/yt-eQsepIbHdgU.jpg", "make poseable (625)", 3),
  ("Y5", "youtube/yt-4-3l3MZZWPc.jpg", "lang Pro (6)", 4),
  ("Y6", "youtube/yt-I78weVdhwdw.jpg", "10 parts (1115)", 4),
  ("Y7", "youtube/yt-Ij-jc6t4WNo.jpg", "knee bend (606)", 3),
  ("Y8", "youtube/yt-m3sNvDOJYQ0.jpg", "lang hinge 115 (17)", 4),
  ("Y9", "youtube/yt-WqgDSDL5twg.jpg", "hinge stop (1452)", 5),
  ("Y10", "youtube/yt-65JiRlDupNc.jpg", "see bend free (1219)", 5),
  ("Y11", "youtube/yt-sgcC965GVps.jpg", "Ebb buzz (98)", 5)]),
 ("JetBrains Marketplace: Bison & Flex", [
  ("J1", "jetbrains/icon.png", "icoon", 6),
  ("J2", "jetbrains/screen-1.png", "scherm 1", 7),
  ("J3", "jetbrains/screen-2.png", "scherm 2", 6),
  ("J4", "jetbrains/screen-3.png", "scherm 3", 6),
  ("J5", "jetbrains/screen-4.png", "scherm 4", 7),
  ("J6", "jetbrains/screen-5.png", "scherm 5", 7)]),
 ("Garmin: Ebb, Ebb Calm, Gloop's Hat Tower", [
  ("E1", "garmin/ebb-icoon.png", "Ebb icoon", 8),
  ("E2", "garmin/ebb-scherm-1.png", "Ebb 1", 7),
  ("E3", "garmin/ebb-scherm-2.png", "Ebb 2", 7),
  ("E4", "garmin/ebb-scherm-3.png", "Ebb 3", 7),
  ("E5", "garmin/ebb-scherm-4.png", "Ebb 4", 7),
  ("E6", "garmin/ebb-scherm-5.png", "Ebb 5", 7),
  ("C1", "garmin/calm-icoon.png", "Calm icoon", 8),
  ("C2", "garmin/calm-scherm-1.png", "Calm 1", 7),
  ("C3", "garmin/calm-scherm-2.png", "Calm 2", 7),
  ("C4", "garmin/calm-scherm-3.png", "Calm 3", 6),
  ("C5", "garmin/calm-scherm-4.png", "Calm 4", 6),
  ("C6", "garmin/calm-scherm-5.png", "Calm 5", 6),
  ("T1", "garmin/tower-icoon.png", "Tower icoon", 8),
  ("T2", "garmin/tower-scherm-1.png", "Tower 1", 5),
  ("T3", "garmin/tower-scherm-2.png", "Tower 2", 5),
  ("T4", "garmin/tower-scherm-3.png", "Tower 3", 5),
  ("T5", "garmin/tower-scherm-4.png", "Tower 4", 6),
  ("T6", "garmin/tower-scherm-5.png", "Tower 5", 5)]),
 ("Obsidian: Rollwright", [
  ("O1", "obsidian/poster.png", "poster", 8),
  ("O2", "obsidian/demo.gif", "demo-gif", 7),
  ("O3", "obsidian/roll-log.jpg", "roll log", 6),
  ("O4", "obsidian/skins.jpg", "skins", 6)]),
 ("Hats of the Fallen: geplande Steam-beelden (NIET live)", [
  ("H1", "hats/header-920x430.png", "header", 6),
  ("H2", "hats/main-1232x706.png", "main", 6),
  ("H3", "hats/klein-462x174.png", "klein", 5),
  ("H4", "hats/staand-748x896.png", "staand", 6),
  ("H5", "hats/library-600x900.png", "library", 6),
  ("H6", "hats/hero-3840x1240.png", "hero", 6),
  ("H7", "hats/logo-1082x720.png", "logo", 7),
  ("H8", "hats/1-bureaublad-pijl.png", "scherm 1 pijl", 4),
  ("H9", "hats/1-hoedentoren.png", "hoedentoren", 5),
  ("H10", "hats/3-hap.png", "hap", 5),
  ("H11", "hats/4-val.png", "val", 5),
  ("H12", "hats/5-kaartje.png", "kaartje", 5),
  ("H13", "hats/5-naast-werk.png", "scherm 5 naast werk", 4)]),
 ("Staat klaar voor Pro (nog niet live): vervangt G2 tot G6 en S2 tot S5", [
  ("N1", "nieuw/held-3-voor-na.png", "held-3 voor en na", 8),
  ("N2", "nieuw/held-1-knie.png", "held-1 knie", 7),
  ("N3", "nieuw/held-2-spiraal.png", "held-2 spiraal", 7),
  ("N4", "nieuw/held-4-fit-test-strip.png", "held-4 fit test", 7),
  ("N5", "nieuw/tekenpop-sale.png", "tekenpop -sale", 7)]),
]

CW, CH = 300, 190   # vak voor het beeld
LH = 30             # regel onder het beeld
COLS = 6
PAD = 14
W = PAD + COLS * (CW + PAD)

def kleur(c):
    if c >= 8: return (46, 160, 90)
    if c >= 5: return (224, 140, 30)
    return (205, 50, 50)

def vak(pad):
    im = Image.open(pad); im.seek(0); im = im.convert('RGBA')
    bg = Image.new('RGBA', im.size, (60, 60, 66, 255)); bg.alpha_composite(im); im = bg.convert('RGB')
    im.thumbnail((CW, CH), Image.LANCZOS)
    c = Image.new('RGB', (CW, CH), (24, 22, 30)); c.paste(im, ((CW - im.width) // 2, (CH - im.height) // 2))
    return c

hoogte = 120
for _, items in GROEPEN:
    rijen = (len(items) + COLS - 1) // COLS
    hoogte += 56 + rijen * (CH + LH + PAD)
hoogte += 40
blad = Image.new('RGB', (W, hoogte), (250, 248, 244))
d = ImageDraw.Draw(blad)
d.text((PAD, 18), "Etalage-audit Dortus, 24 nov 2026: wat een klant nu ziet", font=KOP, fill=(20, 20, 24))
d.text((PAD, 64), "Cijfer 1 tot 10 op deel C (ziet het er top uit, zou ik het kopen). Rood onder 5, oranje 5 tot 7, groen 8 en hoger. "
       "Details en wat het moet worden: organisatie/etalage-audit-2026-11-24.md", font=SUB, fill=(70, 70, 80))
y = 120
alle = []
for titel, items in GROEPEN:
    d.text((PAD, y + 14), titel, font=KOP.font_variant(size=24), fill=(20, 20, 24))
    y += 56
    for i, (code, rel, naam, cijfer) in enumerate(items):
        x = PAD + (i % COLS) * (CW + PAD)
        yy = y + (i // COLS) * (CH + LH + PAD)
        blad.paste(vak(os.path.join(BRON, rel)), (x, yy))
        d.rectangle([x + CW - 52, yy + 6, x + CW - 6, yy + 46], fill=kleur(cijfer))
        tw = d.textlength(str(cijfer), font=CIJ)
        d.text((x + CW - 29 - tw / 2, yy + 8), str(cijfer), font=CIJ, fill='white')
        d.text((x, yy + CH + 6), f"{code}  {naam}", font=LBL, fill=(30, 30, 36))
        alle.append(cijfer)
    y += ((len(items) + COLS - 1) // COLS) * (CH + LH + PAD)
blad.save(UIT, optimize=True)
live = [c for (t, its) in GROEPEN if 'NIET live' not in t and 'nog niet live' not in t for (_, _, _, c) in its]
print(UIT, blad.size, 'live beelden', len(live), 'gemiddeld', round(sum(live) / len(live), 1), 'onder 5:', sum(1 for c in live if c < 5))
