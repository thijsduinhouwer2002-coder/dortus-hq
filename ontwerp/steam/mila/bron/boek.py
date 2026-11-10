# Mila 10 nov: het Heldenboek (Sanne features.md 03:10, Bram systemen/boek.gd). kunst/boek.png, 10 beelden van 8 x 8:
#  0 boekje dicht (rechtsboven in het paneel bij hover), 1 boekje open (onder de muis / nieuwe bladzijde),
#  2 stempel nog leeg, 3 door Gloop, 4 door de put, 5 ontsnapt, 6 hoedenberg (1000, 3000, 10.000), 7 aartsvijand,
#  8 pijl links, 9 pijl rechts.
# Stempels zijn een gouden ring met een teken erin, zodat ze op het pruimen paneel lezen (rode inkt verdwijnt erop).
import os
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", "..", ".."))
K = os.path.join(R, "producten", "steam-hol", "godot", "kunst")
C = {".": (0, 0, 0, 0),
     "A": (42, 26, 31, 255),                                     # omtrek
     "Y": (240, 180, 60, 255), "W": (255, 224, 122, 255),        # goud, licht goud
     "P": (122, 70, 140, 255), "Q": (88, 48, 104, 255),          # kaft pruim
     "B": (243, 226, 192, 255), "b": (200, 178, 150, 255),       # bladzijden
     "G": (87, 196, 156, 255), "g": (47, 143, 122, 255), "w": (255, 255, 255, 255), "z": (28, 18, 22, 255),  # Gloop
     "S": (169, 182, 191, 255), "s": (108, 120, 132, 255),       # stekels
     "R": (238, 106, 79, 255), "r": (178, 58, 60, 255),          # rood (hoeden, wrok)
     "L": (122, 92, 128, 255), "J": (138, 91, 51, 255),                                     # lege ring
     "K": (111, 159, 240, 255)}                                  # blauw (puntmuts)
B = [
 [".AAAAAA.",   # 0 boekje dicht: pruimen kaft, gouden hoedje erop
  "AQPPPPPA",
  "AQPWYPPA",
  "AQWYYWPA",
  "AQPPPPPA",
  "AQPPPPPA",
  "AbBBBBBA",
  ".AAAAAA."],
 ["........",   # 1 boekje open
  "AAA..AAA",
  "ABBAABBA",
  "ABbBBbBA",
  "ABBBBBBA",
  "ABbBBbBA",
  "AAAAAAAA",
  ".AQ..QA."],
 ["..L..L..",   # 2 leeg: gestippelde ring
  ".L....L.",
  "L......L",
  "........",
  "........",
  "L......L",
  ".L....L.",
  "..L..L.."],
 ["..YYYY..",   # 3 door Gloop: Gloop met zijn ene oog
  ".Y....Y.",
  "Y.AAAA.Y",
  "YAGwwGAY",
  "YAGwzGAY",
  "YAgGGgAY",
  ".YAAAAY.",
  "..YYYY.."],
 ["..YYYY..",   # 4 door de put: twee stekels met een witte punt boven een zwart gat
  ".Y....Y.",
  "Y.W..W.Y",
  "Y.S..S.Y",
  "YSSsSSsY",
  "YzzzzzzY",
  ".YAAAAY.",
  "..YYYY.."],
 ["..YYYY..",   # 5 ontsnapt: een laars die wegrent, met vaartstreepjes (de laars is ons teken: Gloop spuugt er een uit)
  ".Y....Y.",
  "Y..AA..Y",
  "YB.AJA.Y",
  "Y..AJJAY",
  "YB.AAAAY",
  ".Y....Y.",
  "..YYYY.."],
 ["..YYYY..",   # 6 hoedenberg: drie hoeden op een stapel
  ".Y.AA.Y.",
  "Y.AKKA.Y",
  "Y.ARRA.Y",
  "YARRRRAY",
  "YAYWYYAY",
  ".YAAAAY.",
  "..YYYY.."],
 ["..YYYY..",   # 7 aartsvijand: onweerswolkje (zijn wrok) in de ring
  ".Y....Y.",
  "Y.AAAA.Y",
  "YAssSsAY",
  "YAsssSAY",
  "Y.ARAA.Y",
  ".Y.R..Y.",
  "..YYYY.."],
 ["........",   # 8 pijl links
  "....AA..",
  "...AYA..",
  "..AYYA..",
  "..AYYA..",
  "...AYA..",
  "....AA..",
  "........"],
 ["........",   # 9 pijl rechts
  "..AA....",
  "..AYA...",
  "..AYYA..",
  "..AYYA..",
  "..AYA...",
  "..AA....",
  "........"],
]
im = Image.new("RGBA", (8 * len(B), 8))
for f, rijen in enumerate(B):
    assert len(rijen) == 8, f
    for y, r in enumerate(rijen):
        assert len(r) == 8, (f, y)
        for x, ch in enumerate(r):
            im.putpixel((f * 8 + x, y), C[ch])
im.save(os.path.join(K, "boek.png"))

# Voorbeeld: een bladzijde in het paneel op ware schaal 3, strook 120 px (paneel 3 regels hoog), naast de 10x van de beelden.
D = os.path.join(R, "ontwerp", "steam", "mila")
v = Image.new("RGBA", (8 * len(B) + len(B) + 1, 10), (0x2b, 0x1d, 0x35, 255))
for f in range(len(B)):
    v.alpha_composite(im.crop((f * 8, 0, f * 8 + 8, 8)), (1 + f * 9, 1))
v.resize((v.width * 10, v.height * 10), Image.NEAREST).save(os.path.join(D, "boek-10x.png"))
