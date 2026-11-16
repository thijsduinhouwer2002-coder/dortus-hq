# Daan, proef op Mila's v3 slok: held kleiner, mond opgerekt rond zijn middel, oog vrij.
import sys, os
sys.path.insert(0, '/home/claude/dortus-hq/ontwerp/garmin/bron')
R = '/home/claude/dortus-hq/ontwerp/garmin/gloop-spel/bron-renders'
UIT = sys.argv[1]; HB = float(sys.argv[2]); KN = int(sys.argv[3]); HK = float(sys.argv[4]); MW = float(sys.argv[5]); ZAK = float(sys.argv[6])
sys.argv = [sys.argv[0], R, UIT]
import gloop_spel_v3 as v3
v2 = v3.v2
v2.toren = v3.toren_v3
from PIL import Image, ImageDraw, ImageFilter

def slok(N):
    H = v2.hoeden(); im = v2.achtergrond(N); d = ImageDraw.Draw(im)
    cx, voet = N/2, N*0.90; gb = N*v3.GLOOP_B
    hap = v2.zonder_schaduw(Image.open(os.path.join(R, "gloop-hap-h0.png")).convert("RGBA"))
    top_y, top_x = v2.toren(im, hap, [H[4], H[1]], N, cx, voet, gb, 1)
    g = v2.schaal(hap, gb); gx, gy = int(cx-g.width/2), int(voet-g.height)
    m0x, m0y, m1x, m1y = v3.mond(g); mcx, mcy = (m0x+m1x)/2, (m0y+m1y)/2
    mw, mh = (m1x-m0x), (m1y-m0y)
    # opgerekte mond: donker ovaal, breder dan de held, iets lager
    W2, H2 = mw*MW, mh*MW*0.62
    mcy2 = mcy + mh*ZAK
    gm = g.copy(); dm = ImageDraw.Draw(gm)
    dm.ellipse([mcx-W2/2-3, mcy2-H2/2-3, mcx+W2/2+3, mcy2+H2/2+3], fill=(70, 30, 50, 255))
    dm.ellipse([mcx-W2/2, mcy2-H2/2, mcx+W2/2, mcy2+H2/2], fill=(105, 52, 78, 255))
    dm.ellipse([mcx-W2*0.30, mcy2+H2*0.05, mcx+W2*0.30, mcy2+H2*0.48], fill=(236, 120, 140, 255))
    im.alpha_composite(gm, (gx, gy))
    v3.KNIP = KN
    ruw = v3.held_benen()
    f = mw*MW*HB/ruw.width
    hb = v2.bijsnijden(ruw.resize((round(ruw.width*f), round(ruw.height*f)), Image.LANCZOS).rotate(HK, expand=True, resample=Image.BICUBIC))
    hx = int(gx+mcx-hb.width*0.5); hy = int(gy+mcy2-hb.height + H2*0.05)
    rand = hb.getchannel("A").point(lambda a: 255 if a > 100 else 0).filter(ImageFilter.MaxFilter(v3.RAND))
    schim = Image.new("RGBA", hb.size, (40, 22, 34, 255)); schim.putalpha(rand)
    im.alpha_composite(schim, (hx, hy)); im.alpha_composite(hb, (hx, hy))
    # onderlip: alleen de onderste helft van het mondovaal en wat eronder, als boog
    lip = Image.new("L", g.size, 0); dl = ImageDraw.Draw(lip)
    dl.rectangle([0, int(mcy2), g.width, g.height], fill=255)
    laag = Image.new("RGBA", g.size, (0,0,0,0)); laag.paste(gm, (0,0), lip)
    im.alpha_composite(laag, (gx, gy))
    pan = v2.schaal(H[0], N*0.15).rotate(-24, expand=True, resample=Image.BICUBIC)
    px_, py_ = int(top_x-pan.width/2+N*0.10), int(top_y-pan.height-N*0.03)
    for k in range(3):
        xx = px_+pan.width*(0.25+0.25*k)
        d.line([(xx, py_+pan.height+N*0.005), (xx, py_+pan.height+N*0.045)], fill=(255,245,220), width=max(2,int(N*0.01)))
    im.alpha_composite(pan, (px_, py_))
    v2.tekst(d, (N*0.22, N*0.50), "GULP!", 0.09, N, (255,255,255))
    v2.tekst(d, (px_+pan.width+N*0.06, py_+pan.height*0.5), "+1", 0.07, N, (255,214,90))
    v2.teller(im, 3, N, H[0])
    return v2.rond(im, N)

os.makedirs(UIT, exist_ok=True)
v2.MIP = False; slok(454).convert("RGB").save(os.path.join(UIT, "daan-slok-454.png"))
v2.MIP = True; v2.rond(v2.mip(slok(260)).convert("RGBA"), 260).convert("RGB").save(os.path.join(UIT, "daan-slok-260.png"))
print("ok")
