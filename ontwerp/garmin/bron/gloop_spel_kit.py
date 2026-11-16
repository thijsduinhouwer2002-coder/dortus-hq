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


def slok_sprite(W):
    # zelfde opbouw als v3.slok, maar op een doorzichtig vlak: Gloop met de held ondersteboven in zijn mond
    hap = v2.zonder_schaduw(Image.open(os.path.join(R, "gloop-hap-h0.png")).convert("RGBA"))
    g = v2.schaal(hap, W * SLOK_B)
    m0x, m0y, m1x, m1y = v3.mond(g)
    ruw = v3.held_benen()
    f = (m1x - m0x) * v3.HELD_B / 90
    hb = v2.bijsnijden(ruw.resize((max(1, round(ruw.width * f)), max(1, round(ruw.height * f))), Image.LANCZOS)
                       .rotate(SLOK_HOEK, expand=True, resample=Image.BICUBIC))
    hx = int((m0x + m1x) / 2 - hb.width * 0.85)
    hy = int(m0y + (m1y - m0y) * 0.60 - hb.height)
    boven = max(0, -hy)
    vlak = Image.new("RGBA", (g.width, g.height + boven), (0, 0, 0, 0))
    vlak.alpha_composite(g, (0, boven))
    rand = hb.getchannel("A").point(lambda a: 255 if a > 100 else 0).filter(ImageFilter.MaxFilter(max(3, round(W / 90)) | 1))
    schim = Image.new("RGBA", hb.size, (40, 22, 34, 255)); schim.putalpha(rand)
    vlak.alpha_composite(schim, (hx, hy + boven)); vlak.alpha_composite(hb, (hx, hy + boven))
    lip = Image.new("L", g.size, 0)
    ImageDraw.Draw(lip).rectangle([0, int(m0y + (m1y - m0y) * 0.50), g.width, g.height], fill=255)
    laag = Image.new("RGBA", g.size, (0, 0, 0, 0)); laag.paste(g, (0, 0), lip)
    vlak.alpha_composite(laag, (0, boven))
    return vlak, boven   # boven = hoeveel px de benen boven de kop van Gloop uitsteken


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
    sl, boven = slok_sprite(W); stuks["gloop-slok"] = sl
    stuks["held-val"] = held_val(W)
    H = v2.hoeden()
    for i, h in enumerate(H):
        stuks[f"hoed-{i:02d}-{v2.HOEDNAMEN[i]}"] = v2.schaal(h, W * HOED_B)
    stuks["helm-vlieg"] = v2.schaal(H[0], W * HOED_B).rotate(-24, expand=True, resample=Image.BICUBIC)
    info = {}
    for naam in list(stuks):
        stuks[naam] = los_weg(stuks[naam])
    for naam, im in stuks.items():
        if M:
            im = mip_sprite(im, bayer=naam.startswith("gloop"))
        im.save(os.path.join(map_, naam + ".png"))
        stuks[naam] = im
        info[naam] = [im.width, im.height]
    g = stuks["gloop-rust"]
    info["_ankers"] = {
        "toren_voet": [round(g.width * 0.53), round(g.height * KRUIN)],
        "hoed_stap_deel_van_hoedhoogte": HOED_STAP,
        "slok_benen_boven_kop_px": boven,
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
    gx, gy = int(cx - g.width / 2), int(voet - g.height)
    im.alpha_composite(g, (gx, gy + dy))
    r = stuks["gloop-rust"]
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
