# Gloop op je pols: spritekit voor de bouw (Mila, 16 nov 2026), bovenop v2 en v3.
# Gijs' proef (run 43797596147) draait met vormen; dit zijn de echte plaatjes op de maat van elk
# horloge, plus een proefbeeld van keuze (c): toren op de kop, held glijdt schuin van linksboven in.
# Elk proefbeeld is alleen uit de kitbestanden samengesteld, dus wat je ziet kan Gijs echt tekenen.
#   python3 gloop_spel_kit.py <rendermap> <uitmap>
# Uit: <uitmap>/<breedte>[-mip]/*.png (doorzichtig, MIP al in de 64 kleuren met harde rand),
#      kit.json met maten en ankers, proef-c-<breedte>.png en blad-kit-c.png.
import sys, os, json, math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.argv = sys.argv[:3]
import gloop_spel_v2 as v2
import gloop_spel_v3 as v3

R, UIT = sys.argv[1], sys.argv[2]
# horloges van de proef: breedte, MIP of niet. Venu Sq 2 is 320x360, we schalen op de breedte.
TOESTELLEN = [(260, True), (280, True), (320, False), (390, False), (416, False), (454, False)]
GLOOP_B = 0.34   # rust/hap/blij, deel van de schermbreedte
SLOK_B = 0.40    # bij de slok zwelt hij op
HOED_B = 0.17   # was 0.15: de toren las klein als prut
HELD_B = 0.17
HELD_HOEK = -38
SLOK_HOEK = 80   # v3 had 22: de benen dekten Gloops oog (blinde kijker: "het oog verdwijnt, een kluwen")  # (c): duikt met het hoofd naar rechtsonder
KRUIN = 0.13     # bovenkant toren: deel van de Gloophoogte, vanaf boven
HOED_STAP = 0.56 # elke volgende hoed staat 0,56 x zijn eigen hoogte hoger


def gloops():
    g = {s: v2.zonder_schaduw(Image.open(os.path.join(R, f"gloop-{s}-h0.png")).convert("RGBA")) for s in ("rust", "hap")}
    tmp = os.path.join(UIT, "_blij.png")
    v3.dikke_boog(os.path.join(R, "gloop-blij-h0.png"), tmp)
    g["blij"] = v2.zonder_schaduw(Image.open(tmp).convert("RGBA")); os.remove(tmp)
    return g


SLOK_HOEK2 = 42   # 16 nov 05:00: benen wijzen schuin linksboven uit de mond, weg van het oog
SLOK_MX, SLOK_MY = 0.40, 0.70  # knipkant van de held in de mond (deel van de mondbreedte/-hoogte)
SLOK_MOND = (1.35, 1.12)   # grotere mond bij de slok: breedte, hoogte t.o.v. de hap-O
SLOK_KEEL = 0.42           # vanaf hier (deel van de mondhoogte) is de keel donker over de held
MOND_KL, RAND_KL, TONG_KL = (62, 22, 40, 255), (30, 60, 50, 255), (236, 110, 130, 255)
MOND_E = None
SLOK_HELD = 1.0  # breedte van de held (benen en buik, vóór draaien) t.o.v. de mondbreedte


def alleen_benen():
    # held-vallen ligt ondersteboven. Alleen benen, laarzen, riem en buik; zonder armen (de hand
    # stak bij het oog en las als zwaaien) en zonder schild.
    h = v3.held_benen()   # al zonder schild en vloerschaduw, geknipt onder de riem, bijgesneden
    # rechterarm met hand zit in het rechter kwart: weg (gemeten: arm begint op 0,75 van de breedte)
    h = h.crop((0, 0, int(h.width * 0.74), h.height))
    return v2.bijsnijden(h)


def slok_sprite(W, M=False):
    # v2 van de slok (moet Daan 16 nov 04:40: geen kluwen, één mond, oog vrij).
    # Gloop op dezelfde maat als rust/hap (de toren blijft dus op zijn plek), zijn eigen O-mond
    # (de hap-render), en daarin alleen de benen en buik van de held, schuin naar linksboven.
    # De onderlip wordt over de held heen getekend, zodat hij echt IN de mond zit.
    hap = v2.zonder_schaduw(Image.open(os.path.join(R, "gloop-hap-h0.png")).convert("RGBA"))
    g = v2.schaal(hap, W * GLOOP_B)
    m0x, m0y, m1x, m1y = v3.mond(g)
    if M:   # MIP: Gloop met Bayer, held effen met zwarte omtrek (moet Daan: effen blauw)
        g = mip_sprite(g, bayer=True); m0x += 1; m0y += 1; m1x += 1; m1y += 1
    # één grotere mond (blinde kijker 05:00: de O was onder de held weg, "gevallen, niet ingeslikt"):
    # boven vast onder het oog, breder en dieper, de oude mond valt er helemaal binnen
    global MOND_E
    mb, mh = (m1x - m0x) * SLOK_MOND[0], (m1y - m0y) * SLOK_MOND[1]
    mc = (m0x + m1x) / 2
    MOND_E = (mc - mb / 2, m1y - mh, mc + mb / 2, m1y)   # onderkant gelijk (anders buiten de plaat)
    global MOND_KL, RAND_KL, TONG_KL
    if M:   # MIP: alleen paletkleuren
        MOND_KL, RAND_KL, TONG_KL = (85, 0, 85, 255), (0, 0, 0, 255), (255, 85, 170, 255)
    else:
        MOND_KL, RAND_KL, TONG_KL = (62, 22, 40, 255), (30, 60, 50, 255), (236, 110, 130, 255)
    gd = ImageDraw.Draw(g)
    gd.ellipse([MOND_E[0] - 1, MOND_E[1] - 1, MOND_E[2] + 1, MOND_E[3] + 1], fill=RAND_KL)
    gd.ellipse(MOND_E, fill=MOND_KL)
    m0x, m1x = MOND_E[0], MOND_E[2]; m0y, m1y = MOND_E[1], MOND_E[3]
    ruw = alleen_benen()
    f = (m1x - m0x) * SLOK_HELD / ruw.width
    hb = ruw.resize((max(1, round(ruw.width * f)), max(1, round(ruw.height * f))), Image.LANCZOS)
    # knipkant (onderkant) midden = draaipunt: na draaien opnieuw zoeken via een merkpixel
    vl = Image.new("RGBA", (hb.width * 3, hb.height * 3), (0, 0, 0, 0))
    vl.alpha_composite(hb, (hb.width, hb.height))
    hb = vl.rotate(SLOK_HOEK2, center=(hb.width * 1.5, hb.height * 2), resample=Image.BICUBIC)
    ax, ay = hb.width / 2, hb.height * 2 / 3   # waar de knipkant nu zit
    bb = hb.getbbox(); hb = hb.crop(bb); ax -= bb[0]; ay -= bb[1]
    if M:   # held lichter vóór het afronden: anders wordt het blauw 0,0,170 en verdwijnt hij in de donkere mond
        from PIL import ImageEnhance
        a_ = hb.getchannel("A"); hb = ImageEnhance.Brightness(hb.convert("RGB")).enhance(1.15).convert("RGBA"); hb.putalpha(a_)
        hb = mip_sprite(hb, bayer=False); ax += 1; ay += 1
    # knipkant op het midden van de mond, iets onder het midden
    mx, my = m0x + (m1x - m0x) * SLOK_MX, m0y + (m1y - m0y) * SLOK_MY
    hx, hy = int(mx - ax), int(my - ay)
    links, boven = max(0, -hx), max(0, -hy)
    vlak = Image.new("RGBA", (g.width + links, g.height + boven), (0, 0, 0, 0))
    vlak.alpha_composite(g, (links, boven))
    if not M:   # donkere rand (op MIP heeft mip_sprite al een zwarte omtrek gegeven)
        pad = Image.new("L", (hb.width + 8, hb.height + 8), 0)
        pad.paste(hb.getchannel("A").point(lambda a: 255 if a > 100 else 0), (4, 4))
        rand = pad.filter(ImageFilter.MaxFilter(3)).crop((4, 4, 4 + hb.width, 4 + hb.height))
        schim = Image.new("RGBA", hb.size, (40, 22, 34, 255)); schim.putalpha(rand)
        vlak.alpha_composite(schim, (hx + links, hy + boven))
    vlak.alpha_composite(hb, (hx + links, hy + boven))
    # keel: de onderste helft van de (grotere) mond weer donker over de held, met de tong erop;
    # zo verdwijnt zijn buik in het donker en zie je de open mond rondom hem
    d = ImageDraw.Draw(vlak)
    ex0, ey0, ex1, ey1 = [v + o for v, o in zip(MOND_E, (links, boven, links, boven))]
    keel = Image.new("L", vlak.size, 0); dk = ImageDraw.Draw(keel)
    dk.ellipse([ex0, ey0, ex1, ey1], fill=255)
    dk.rectangle([0, 0, vlak.width, int(ey0 + (ey1 - ey0) * SLOK_KEEL)], fill=0)
    vlak.paste(Image.new("RGBA", vlak.size, MOND_KL), (0, 0), keel)
    tb = (ex1 - ex0) * 0.5
    d.ellipse([(ex0 + ex1) / 2 - tb / 2 + (ex1 - ex0) * 0.08, ey1 - (ey1 - ey0) * 0.30, (ex0 + ex1) / 2 + tb / 2 + (ex1 - ex0) * 0.08, ey1 - (ey1 - ey0) * 0.06], fill=TONG_KL)
    return vlak, (links, boven)   # waar Gloops linkerbovenhoek in de slokplaat staat


def held_val(W):
    h = v2.zonder_schaduw(Image.open(os.path.join(R, "held-schrik.png")).convert("RGBA"))
    return v2.bijsnijden(v2.schaal(h, W * HELD_B).rotate(HELD_HOEK, expand=True, resample=Image.BICUBIC))


def los_weg(im):
    # losse spikkels uit de renders (paars plukje links van de kap, rode stip bij de helm) weg:
    # alleen stukken van minstens 3% van het grootste stuk blijven staan
    import numpy as np
    from scipy import ndimage
    a = np.array(im.getchannel("A")) > 40
    lab, n = ndimage.label(a)
    if n <= 1:
        return im
    maten = ndimage.sum(a, lab, range(1, n + 1))
    houd = np.isin(lab, [i + 1 for i, m in enumerate(maten) if m >= 0.03 * maten.max()])
    arr = np.array(im); arr[..., 3] = np.where(houd, arr[..., 3], 0)
    return v2.bijsnijden(Image.fromarray(arr))


def mip_sprite(im, bayer=True):
    # kleuren in de 64, rand hard: de compiler hoeft niets meer te doen. Hoeden zonder Bayer (effen
    # vlakken): blinde kijker 16 nov zag de toren met Bayer als "onleesbare prut". Alles krijgt een
    # zwarte omtrek van 1 px, zodat het los komt van de bruine grot.
    im = im.copy()
    a = im.getchannel("A").point(lambda v: 255 if v >= 128 else 0)
    w, h = im.size
    groot = Image.new("RGBA", (w + 2, h + 2), (0, 0, 0, 0)); groot.paste(im, (1, 1))
    a2 = Image.new("L", (w + 2, h + 2), 0); a2.paste(a, (1, 1))
    plat = Image.new("RGBA", groot.size, (0, 0, 0, 255)); plat.alpha_composite(groot)
    if bayer:
        kl = v2.mip(plat).convert("RGBA")
    else:
        kl = plat.convert("RGB").point(lambda v: round(v / 85) * 85).convert("RGBA")
    rand = a2.filter(ImageFilter.MaxFilter(3))
    out = Image.new("RGBA", groot.size, (0, 0, 0, 0))
    out.paste(Image.new("RGBA", groot.size, (0, 0, 0, 255)), (0, 0), rand)
    out.paste(kl, (0, 0), a2)
    return out


def kit(W, M):
    map_ = os.path.join(UIT, f"{W}{'-mip' if M else ''}")
    os.makedirs(map_, exist_ok=True)
    stuks = {}
    G = gloops()
    for s, im in G.items():
        stuks[f"gloop-{s}"] = v2.schaal(im, W * GLOOP_B)
    global SLOK_POS
    sl, slok_pos = slok_sprite(W, M); stuks["gloop-slok"] = sl; SLOK_POS = slok_pos
    stuks["held-val"] = held_val(W)
    H = v2.hoeden()
    for i, h in enumerate(H):
        stuks[f"hoed-{i:02d}-{v2.HOEDNAMEN[i]}"] = v2.schaal(h, W * HOED_B)
    stuks["helm-vlieg"] = v2.schaal(H[0], W * HOED_B).rotate(-24, expand=True, resample=Image.BICUBIC)
    info = {}
    for naam in list(stuks):
        if naam != "gloop-slok":   # niet bijsnijden: de plek van Gloop in de slokplaat moet kloppen
            stuks[naam] = los_weg(stuks[naam])
    for naam, im in stuks.items():
        if M and naam != "gloop-slok":   # slok is al op MIP gezet (held effen, Gloop met Bayer)
            im = mip_sprite(im, bayer=naam.startswith("gloop"))
        im.save(os.path.join(map_, naam + ".png"))
        stuks[naam] = im
        info[naam] = [im.width, im.height]
    g = stuks["gloop-rust"]
    info["_ankers"] = {
        "toren_voet": [round(g.width * 0.53), round(g.height * KRUIN)],
        "hoed_stap_deel_van_hoedhoogte": HOED_STAP,
        "slok_gloop_pos": list(slok_pos),  # teken gloop-slok op (gx - dx, gy - dy), gx,gy = waar gloop-rust staat
        "gloop_voet_y_deel_van_scherm": 0.90,
    }
    return stuks, info


def achtergrond_c(N, M):
    # (c): de schacht loopt schuin van linksboven naar Gloops mond; de toren staat recht in het midden
    v2.MIP = M
    if M:   # v2.achtergrond tekent op MIP altijd de rechte schacht: hier alleen de effen grot
        im = Image.new("RGBA", (N, N), (170, 85, 0, 255))
    else:
        im = v2.achtergrond(N, schacht=False)
    pad = [(N * 0.04, N * 0.04), (N * 0.38, N * 0.74)]
    sw = N * 0.20
    if M:
        d = ImageDraw.Draw(im)
        d.line(pad, fill=(255, 170, 85, 255), width=int(sw))
        for p in pad:
            d.ellipse([p[0] - sw / 2, p[1] - sw / 2, p[0] + sw / 2, p[1] + sw / 2], fill=(255, 170, 85, 255))
    else:
        lam = Image.new("L", (N, N), 0); d = ImageDraw.Draw(lam)
        d.line(pad, fill=255, width=int(sw))
        for p in pad:
            d.ellipse([p[0] - sw / 2, p[1] - sw / 2, p[0] + sw / 2, p[1] + sw / 2], fill=255)
        lam = lam.filter(ImageFilter.GaussianBlur(N * 0.02))
        im = Image.composite(Image.new("RGBA", (N, N), (226, 162, 92, 255)), im, lam)
    vloer = int(N * 0.86)
    kl = (85, 0, 0, 255) if M else (74, 34, 22, 255)
    ImageDraw.Draw(im).ellipse([int(-0.1 * N), vloer - int(N * 0.05), int(1.1 * N), vloer + int(N * 0.25)], fill=kl)
    return im


def toren_op(im, stuks, gnaam, cx, voet, rij, zaad, dy=0):
    g = stuks[gnaam]
    r = stuks["gloop-rust"]
    gx, gy = int(cx - r.width / 2), int(voet - r.height)
    if gnaam == "gloop-slok":   # slokplaat: Gloop (hap) staat erin op SLOK_POS, voet gelijk aan de hap
        hy = int(voet - stuks["gloop-hap"].height)
        im.alpha_composite(g, (gx - SLOK_POS[0], hy - SLOK_POS[1] + dy))
    else:
        im.alpha_composite(g, (gx, gy + dy))
    y = voet - r.height + r.height * KRUIN
    x = gx + r.width * 0.53
    rnd = random.Random(zaad)
    for naam in rij:
        h = stuks[naam].rotate(rnd.uniform(-10, 10), expand=True, resample=Image.NEAREST)
        top = y - h.height * 0.78
        im.alpha_composite(h, (int(x - h.width / 2), int(top)))
        y = top + h.height * 0.22
        x += rnd.uniform(-0.05, 0.05) * r.width
    return y, x


def proef(N, M, stuks, moment):
    im = achtergrond_c(N, M)
    d = ImageDraw.Draw(im)
    cx, voet = N / 2, N * 0.90
    hoednamen = sorted(k for k in stuks if k.startswith("hoed-"))
    rij = [hoednamen[i] for i in (4, 1, 9, 5, 2)]
    if moment == "val":
        toren_op(im, stuks, "gloop-rust", cx, voet, rij, 2)
        h = stuks["held-val"]
        hx, hy = int(N * 0.20 - h.width / 2), int(N * 0.30 - h.height / 2)
        im.alpha_composite(h, (hx, hy))
        v2.tekst(d, (hx + h.width + N * 0.02, hy + N * 0.02), "!", 0.11, N, (255, 230, 80))
        a0, a1 = -48, -22
        d.arc([N * 0.03, N * 0.03, N * 0.97, N * 0.97], a0, a1, fill=(255, 255, 255), width=max(3, int(N * 0.022)))
        hk = math.radians((a0 + a1) / 2); rr = N * 0.36
        v2.tekst(d, (N / 2 + rr * math.cos(hk), N / 2 + rr * math.sin(hk) + N * 0.02), "GULP", 0.075, N, (255, 255, 255))
        teller = 5
    else:
        g = stuks["gloop-slok"]
        top_y, top_x = toren_op(im, stuks, "gloop-slok", cx, voet, rij, 2)
        pan = stuks["helm-vlieg"]
        px_, py_ = int(top_x + N * 0.10), int(top_y - pan.height * 0.2)
        im.alpha_composite(pan, (px_, py_))
        v2.tekst(d, (N * 0.22, N * 0.52), "GULP!", 0.09, N, (255, 255, 255))
        v2.tekst(d, (px_ + pan.width + N * 0.05, py_ + pan.height * 0.5), "+1", 0.07, N, (255, 214, 90))
        teller = 6
    # teller met een grotere kroon (kijker: het helmpje was te klein om te lezen)
    kr = stuks[hoednamen[4]]
    f = ImageFont.truetype(v2.FONT, int(N * 0.11)); sx = str(teller)
    tw = d.textlength(sx, font=f); x0 = int(N / 2 - (tw + kr.width + N * 0.02) / 2)
    im.alpha_composite(kr, (x0, int(N * 0.12 - kr.height / 2)))
    v2.tekst(d, (x0 + kr.width + N * 0.02, N * 0.12), sx, 0.11, N, (255, 214, 90), anker="lm")
    if M:
        # alleen de tekst en lijnen kunnen nog tussenkleuren hebben: op het MIP-palet zetten zonder Bayer
        px = im.load()
        for y in range(N):
            for x in range(N):
                r, gg, b, a = px[x, y]
                px[x, y] = (round(r / 85) * 85, round(gg / 85) * 85, round(b / 85) * 85, 255)
    return v2.rond(im, N)


if __name__ == "__main__":
    os.makedirs(UIT, exist_ok=True)
    alles = {}
    proeven = []
    for W, M in TOESTELLEN:
        v2.MIP = M
        stuks, info = kit(W, M)
        alles[f"{W}{'-mip' if M else ''}"] = info
        if W in (260, 454):
            for mom in ("val", "slok"):
                p = proef(W, M, stuks, mom)
                p.convert("RGB").save(os.path.join(UIT, f"proef-c-{W}-{mom}.png"))
                proeven.append((W, mom, p))
    with open(os.path.join(UIT, "kit.json"), "w") as f:
        json.dump(alles, f, indent=1)
    # blad: boven 454 op ware pixels, midden 260 MIP vergroot, onder 260 op 1x
    B = Image.new("RGB", (2 * 474 + 20, 474 + 474 + 300), (24, 20, 26))
    for W, mom, p in proeven:
        i = 0 if mom == "val" else 1
        if W == 454:
            B.paste(p.convert("RGB"), (20 + i * 474, 20))
        else:
            B.paste(p.resize((454, 454), Image.NEAREST).convert("RGB"), (20 + i * 474, 494))
            B.paste(p.convert("RGB"), (20 + i * 474 + 97, 494 + 474 + 10))
    B.save(os.path.join(UIT, "blad-kit-c.png"))
    print("klaar")
