"""Mila: poef.png, het boze wolkje dat knapt als een held met een wrok in een val valt (Olaf 10 nov 01:40 UTC).
4 beelden van 12 x 10, zelfde kleuren als tekens.png. Midden van het wolkje = (6, 3), dus teken het beeld op
(x_wolkje - 2, y_wolkje) als het oude wolkje op (x_wolkje, y_wolkje) stond. 10 fps, één keer, dan weg.
Gebruik: python3 poef.py <uit.png>"""
import sys
from PIL import Image
K = {"d": (42, 26, 31), "1": (93, 85, 82), "2": (132, 122, 114), "3": (172, 161, 150), "r": (238, 106, 79), "w": (255, 244, 224)}
B = [
# 1: het wolkje zwelt op, de bliksem flitst wit
["...dd.ddd...",
 "..d33d333d..",
 ".d3333333d..",
 "d332333233d.",
 "d222222222d.",
 ".d2111112d..",
 "..ddwwddd...",
 "....wr......",
 "...wr.......",
 "............"],
# 2: het knapt: vier wolkjes vliegen uit elkaar, een witte vonk in het midden
["..dd....dd..",
 ".d33d..d33d.",
 ".d22d..d22d.",
 "..dd.w..dd..",
 ".....ww.....",
 "..dd.w..dd..",
 ".d32d..d32d.",
 ".d21d..d21d.",
 "..dd....dd..",
 "............"],
# 3: verder weg en kleiner, een rood vonkje van de bliksem
["d3.......d3.",
 "21.......21.",
 "............",
 ".....r......",
 "............",
 "............",
 "d3.......d3.",
 "21.......21.",
 "............",
 "............"],
# 4: alleen nog stof
["2.........2.",
 "............",
 "............",
 "............",
 "............",
 "............",
 "............",
 "1.........1.",
 "............",
 "............"],
]
im = Image.new("RGBA", (12 * len(B), 10), (0, 0, 0, 0))
for f, rijen in enumerate(B):
    for y, rij in enumerate(rijen):
        for x, c in enumerate(rij):
            if c != ".": im.putpixel((f * 12 + x, y), K[c] + (255,))
im.save(sys.argv[1])
