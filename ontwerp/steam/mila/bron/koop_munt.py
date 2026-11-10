# Mila 10 nov: het muntje "hier kun je kopen", 2 beelden van 8 x 8 (draait: plat, dan op zijn kant). kunst/koop_munt.png.
# Zelfde kleuren als het muntje dat hol.gd nu met rechthoekjes tekent (#7a4a12, #f2c14e, #fff4c0), plus een middentoon.
import os
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", "..", ".."))
K = os.path.join(R, "producten", "steam-hol", "godot", "kunst")
C = {"X": (0x7a, 0x4a, 0x12, 255), "Y": (0xf2, 0xc1, 0x4e, 255), "O": (0xc9, 0x8a, 0x25, 255), "W": (0xff, 0xf4, 0xc0, 255), ".": (0, 0, 0, 0)}
B = [[".......W",
      "..XXXX..",
      ".XWYYYX.",
      ".XYOOYX.",
      ".XYOOYX.",
      ".XYYYOX.",
      "..XXXX..",
      "........"],
     ["........",
      "...XX...",
      "..XWYX..",
      "..XYOX..",
      "..XYOX..",
      "..XYOX..",
      "...XX...",
      "........"]]
im = Image.new("RGBA", (16, 8))
for f, rijen in enumerate(B):
    for y, r in enumerate(rijen):
        for x, ch in enumerate(r): im.putpixel((f * 8 + x, y), C[ch])
im.save(os.path.join(K, "koop_munt.png"))
p = Image.new("RGBA", (20, 10), (0x2b, 0x1d, 0x35, 255)); p.alpha_composite(im, (1, 1)); p.alpha_composite(im.crop((0, 0, 8, 8)), (1, 1))
p.resize((200, 100), Image.NEAREST).save(os.path.join(R, "ontwerp", "steam", "mila", "koop-munt-10x.png"))
