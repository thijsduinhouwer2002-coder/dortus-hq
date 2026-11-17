"""Drie helden erbij in 3D: gewone held, dief en bard (Daan, 13 nov 2026).

Aanvulling op held.py (ridder en heks). Het spel zet zelf een hoed op elke held (held.gd, hoed_nr),
dus deze drie hebben geen eigen hoed: je herkent ze aan lijf, kleur en wat ze dragen. Dat moet op
±14 spelpixels lezen, dus per held één groot ding met een eigen vorm:
  held = de gewone avonturier, 55% van alle helden en de eerste tien van elk spel. Tuniek in 5 kleuren,
         in dezelfde volgorde als de pixelrijen in held_lijf_kleuren.png (kleur_nr 0 rood, 1 groen, 2 paars,
         3 geel, 4 blauwgroen), zodat Kees bij terugkomst dezelfde tuniek heeft. Eigen trek: een brandende
         lantaarn in de rechterhand (een warm lichtpunt in de donkere gang) en een tas op de heup.
  dief = grijsgroen, zwart masker over de ogen (de klassieke boef), mosterdgele sjaal, een dolkje,
         en een grote lichte buit over de schouder. De zak is het silhouet: licht op het donkere hol.
  bard = room met gele mouwen en kraag, een donkere luit schuin voor de buik (rond lijf, lange hals).
Ronde 2 (frisse kijker 7): dief antraciet en jute zak (grijsgroen en room lazen als groene held met
zonnebril en een tweede hoofd), bard room in plaats van rood (leek op de rode held, luit viel weg).
Alle drie hebben haar, zodat een held die zijn hoed kwijt is aan Gloop niet kaal is.

Gebruik: held.bouw("held", stand, kleur=2), held.bouw("dief", ...), held.bouw("bard", ...).
"""
import math
import bpy
import gedeeld as g

SOORTEN = ("held", "dief", "bard", "edelman")

# (licht, donker): rood, groen, paars, geel, blauwgroen, uit held_lijf_kleuren.png. Paars een stap lichter
# dan de pixelrij (7a52b0), anders valt hij weg op het pruimen hol (zelfde les als de jurk van de heks).
TUNIEK = [("ee6a4f", "b23a3c"), ("5aa04a", "2f5e34"), ("9a74d6", "5a3a8a"), ("f0b43c", "c27f1f"), ("2f9f88", "1f5c56")]
HAAR = ["6a3e26", "3a2a22", "c8843a", "8a4a2a", "e0b860"]


def kleding(soort, kleur=0):
    if soort == "held":
        l, d = TUNIEK[kleur % len(TUNIEK)]
    elif soort == "dief":
        l, d = "4e4c5e", "2e2c3a"   # ronde 2: antraciet, grijsgroen leek op de groene held (frisse kijker)
    elif soort == "edelman":
        l, d = "bc3f55", "8a2a44"   # wijnrood fluweel; 02:45 een tikje lichter en roder (Daan: viel weg voor de bruine krat), was a83a5a/7a2444
        return g.mat("kleed_" + soort, l, rough=0.6, spec=0.35), g.mat("kleed_d_" + soort, d, rough=0.65, spec=0.3)
    else:
        l, d = "eee4cc", "b0a080"   # ronde 2: room, geen van de vijf heldkleuren, donkere luit komt erop los
    return g.mat("kleed_" + soort, l, rough=0.72, spec=0.25), g.mat("kleed_d_" + soort, d, rough=0.75, spec=0.2)


def armen(soort, stand, stap):
    """Armhoeken (links, rechts) of None voor de gewone hoeken uit held.py."""
    if stand in ("schrik", "vallen"):
        return None
    if soort == "bard":
        return 75, 12                 # linkerhand op de hals van de luit, rechterhand tokkelt
    if soort == "dief":
        return 150, 45 - 10 * stap
    if soort == "edelman":
        if stand in ("wacht", "wacht_tik"):
            return -55, -55                 # beide handen voor zich op de knop van de stok
        if stand == "na_u":
            return 70, 28                   # linkerarm zwaait naar voren: "na u"
        if stand == "na_u2":
            return 95, 28                   # tweede beeld: arm wijd uit, buiging
        if stand == "tenen":
            return 135, 135                 # armen omhoog, sierlijk op de tenen om de val heen
        return 18 + 8 * stap, 28            # rechts houdt de stok vast, links zwaait iets mee
    return None


def hand_y(soort, stand):
    if soort == "edelman" and stand in ("wacht", "wacht_tik"):
        return -0.3                         # handen voor het lijf, op de stokknop
    if soort == "edelman" and stand in ("na_u", "na_u2"):
        return -0.18                        # de zwaai gaat naar voren, naar wie er komt
    return -0.2 if soort == "bard" and stand not in ("schrik", "vallen") else -0.02


def haar(ouder, soort, kleur, hk, hs, HZ):
    """Haar als kapje achter en boven op het hoofd, plus een pony. Geen hoed: die zet het spel erop."""
    import held as h
    kl = {"held": HAAR[kleur % len(HAAR)], "dief": "2a1a1f", "bard": "a8482a", "edelman": "a49ca6"}[soort]   # edelman: was b8b0b8, Mila 17 nov iets donkerder zodat haar, gezicht en witte hoed niet één klont worden
    m = g.mat("haar_" + soort, kl, rough=0.75)
    h._bol(ouder, hk(0, 0.05, HZ + 0.08), hs(0.375, 0.33, 0.31), m, segs=40)
    for i, x in enumerate((-0.16, -0.05, 0.07, 0.17)):
        h._bol(ouder, hk(x, -0.24, HZ + 0.25 - 0.02 * (i % 2)), hs(0.1, 0.08, 0.07), m, segs=16)
    if soort == "bard":   # krullen opzij
        for kant in (-1, 1):
            h._bol(ouder, hk(0.33 * kant, 0.04, HZ - 0.05), hs(0.09, 0.09, 0.11), m, segs=16)


def masker(ouder, hk, hs, HZ):
    """Zwart boevenmasker rond de ogen (dief). Ogen komen erbovenop (held.py schuift ze naar voren)."""
    import held as h
    zw = g.mat("masker", "1e1418", rough=0.9, spec=0.05)   # Bram 15 nov: mat en egaal (frisse kijker: band oogde korrelig)
    # Bram 15 nov: band op ooghoogte en iets smaller (was HZ + 0.03, dikte 0.13). Zo lopen de ogen door de band
    # heen (klassiek boevenmasker) in plaats van dat grote witte ogen eroverheen een vlek maken (moet Daan 05:50, scherm 5)
    h._bol(ouder, hk(0, -0.03, HZ + 0.0), hs(0.38, 0.34, 0.105), zw, segs=40)
    for kant in (-1, 1):   # knoopje met twee slippen achter het hoofd
        h._blok(ouder, hk(0.12 * kant, 0.36, HZ - 0.02), hs(0.05, 0.03, 0.14), zw,
                rot=(0, math.radians(25 * kant), 0), rond=0.01)


def gezicht(ouder, soort, stand, hk, hs, HZ):
    """Edelman (Mila 17 nov): ooglid half dicht (verveeld, neus omhoog) en een gouden monocle om het rechteroog."""
    import held as h
    if soort != "edelman" or stand in ("schrik", "vallen"):
        return
    huid = g.mat("ooglid", h.HUID_EDEL, rough=0.75, spec=0.12)
    for kant in ((-1, 1) if stand not in ("tenen", "na_u2") else ()):   # na_u2 (Daan 03:50): ogen open, anders op spelmaat een bleke vlek zonder ogen   # tenen: ogen wijd open, hij moet opletten; monocle blijft
        # bovenste helft van het oog dicht: een huidkleurig kapje net voor het oogwit, met een donker randje eronder
        h._bol(ouder, hk(0.11 * kant, -0.285, HZ + 0.075), hs(0.112, 0.06, 0.07), huid, segs=24)
        h._blok(ouder, hk(0.11 * kant, -0.335, HZ + 0.03), hs(0.11, 0.012, 0.014), g.mat("ooglidrand", "5a3a2a", rough=0.6), rond=0.004)
    goud = g.mat("monocle", "goud", rough=0.22, metaal=0.9)
    bpy.ops.mesh.primitive_torus_add(major_radius=0.085 * 1.2, minor_radius=0.013 * 1.2, location=hk(0.11, -0.345, HZ + 0.01),
                                     rotation=(math.radians(90), 0, 0), major_segments=32, minor_segments=8)
    o = bpy.context.object; bpy.ops.object.shade_smooth(); o.data.materials.append(goud); h._kind(o, ouder)
    h._blok(ouder, hk(0.2, -0.3, HZ - 0.12), hs(0.008, 0.008, 0.16), goud, rot=(0, math.radians(-15), 0), rond=0.003)  # kettinkje


def spullen(ouder, soort, stand, handen, kleur):
    import held as h
    bang = stand in ("schrik", "vallen")
    hx, hz = handen[1]
    lx, lz = handen[-1]
    hout = g.mat("hout2", "8a5a32", rough=0.6)
    leer = g.mat("leer", "6e4632", rough=0.6)
    goud = g.mat("hgoud2", "goud", rough=0.25, metaal=0.85)
    if soort == "held":
        # schuine tas aan een band over de borst, tas op de linkerheup
        bpy.ops.mesh.primitive_torus_add(major_radius=0.3, minor_radius=0.022, location=(0, 0, 0.56),
                                         rotation=(0, math.radians(-38), 0))
        band = bpy.context.object; band.scale = (1, 0.9, 1); band.data.materials.append(leer); h._kind(band, ouder)
        h._blok(ouder, (-0.28, -0.02, 0.33), (0.13, 0.12, 0.14), leer, rond=0.03)
        h._blok(ouder, (-0.28, -0.09, 0.38), (0.15, 0.03, 0.06), g.mat("leer_d", "4a2e22", rough=0.6), rond=0.015)
        # lantaarn hangt onder de rechterhand: hengsel, dak, glas dat brandt, voet
        ijzer = g.mat("ijzer", "3a3440", rough=0.45, metaal=0.7)
        ly = -0.08
        bpy.ops.mesh.primitive_torus_add(major_radius=0.06, minor_radius=0.012, location=(hx, ly, hz - 0.02),
                                         rotation=(math.radians(90), 0, 0))
        o = bpy.context.object; o.data.materials.append(ijzer); h._kind(o, ouder)
        h._cil(ouder, (hx, ly, hz - 0.1), 0.12, 0.07, ijzer, r2=0.03, verts=6)
        h._cil(ouder, (hx, ly, hz - 0.24), 0.1, 0.22, g.mat("lantaarnglas", "ff9a2a", emis=14.0), verts=6)
        h._bol(ouder, (hx, ly - 0.01, hz - 0.24), (0.05, 0.05, 0.07), g.mat("vlam", "fff0a0", emis=30.0), segs=12)
        h._cil(ouder, (hx, ly, hz - 0.37), 0.12, 0.05, ijzer, verts=6)
        l = bpy.data.lights.new("lantaarnlicht", "POINT"); l.color = (1.0, 0.75, 0.4); l.energy = 12
        l.shadow_soft_size = 0.08
        lo = bpy.data.objects.new("lantaarnlicht", l); lo.location = (hx, ly - 0.15, hz - 0.24)
        bpy.context.scene.collection.objects.link(lo); h._kind(lo, ouder)
    elif soort == "dief":
        sjaal = g.mat("sjaal", "e0b040", rough=0.8)
        bpy.ops.mesh.primitive_torus_add(major_radius=0.2, minor_radius=0.06, location=(0, 0, 0.8))
        o = bpy.context.object; bpy.ops.object.shade_smooth(); o.data.materials.append(sjaal); h._kind(o, ouder)
        h._blok(ouder, (0.12, 0.2, 0.68), (0.08, 0.04, 0.24), sjaal, rot=(math.radians(-20), math.radians(10), 0), rond=0.03)
        # dolkje kort en recht in de rechterhand
        staal = g.mat("hstaal2", "staal", rough=0.4, metaal=0.8)
        h._blok(ouder, (hx + 0.02, -0.08, hz + 0.16), (0.04, 0.012, 0.22), staal, rot=(0, math.radians(-20), 0), rond=0.006)
        h._blok(ouder, (hx, -0.07, hz + 0.04), (0.13, 0.03, 0.03), goud, rond=0.008)
        # grote buit: lichte zak met een knoop, over de linkerschouder op de rug
        zak = g.mat("zak", "8a6438", rough=0.9, spec=0.1)   # jute, niet huidkleurig (licht creme las op ware grootte als een tweede hoofd)
        if stand == "vallen":
            zx, zy, zz = -0.6, 0.15, 0.2    # zak vliegt los, zoals het schild van de ridder
        elif bang:
            zx, zy, zz = -0.35, 0.3, 0.55   # zak glijdt van de schouder
        else:
            zx, zy, zz = -0.55, 0.3, 0.92
        h._bol(ouder, (zx, zy, zz), (0.32, 0.26, 0.34), zak, segs=32)
        h._bol(ouder, (zx - 0.08, zy - 0.02, zz + 0.32), (0.07, 0.07, 0.06), g.mat("zakknoop", "5a3a22", rough=0.8), segs=16)
        h._bol(ouder, (zx - 0.22, zy - 0.18, zz - 0.1), (0.07, 0.03, 0.07), goud, segs=16)   # een munt piept eruit
    elif soort == "edelman":
        wit = g.mat("jabot", "f6efe2", rough=0.8)
        for i, z in enumerate((0.86, 0.78, 0.7)):   # kanten jabot: drie bolletjes onder de kin
            h._bol(ouder, (0.0, -0.27 - 0.01 * i, z), (0.11 - 0.015 * i, 0.06, 0.055), wit, segs=16)
        for z in (0.6, 0.51, 0.42):   # drie gouden knopen
            h._bol(ouder, (0.0, -0.3, z), (0.035, 0.02, 0.035), goud, segs=10)
        # gouden bies langs de voorkant van de jas (op de jasrand, geen losse ring: die zweefde als hoepel)
        for kant in (-1, 1):
            h._bol(ouder, (0.085 * kant, -0.262, 0.57), (0.018, 0.02, 0.17), goud, segs=12)
        # twee slippen achter die bij elke stap meezwaaien: het tweede silhouet naast de hoed
        zw = {"stap1": 12, "stap2": -12}.get(stand, 0) + (35 if stand == "vallen" else 0)
        jas_d = g.mat("kleed_d_edelman", "8a2a44", rough=0.65, spec=0.3)
        for kant in (-1, 1):
            a = math.radians(zw + 8 * kant)
            # proef 1 GEZIEN: achter het lijf onzichtbaar; nu langer, lager en wijder, zodat de punten naast de benen uitsteken
            h._blok(ouder, (0.17 * kant + 0.12 * math.sin(a), 0.16, 0.24), (0.11, 0.05, 0.38), jas_d,
                    rot=(math.radians(-10), a + math.radians(10 * kant), 0), rond=0.03)
            h._blok(ouder, (0.17 * kant + 0.12 * math.sin(a) + 0.03 * kant, 0.19, 0.06), (0.115, 0.045, 0.025), goud,
                    rot=(math.radians(-10), a + math.radians(10 * kant), 0), rond=0.008)
        # wandelstok met gouden knop in de rechterhand, tot op de vloer (bij schrik en vallen vliegt hij weg)
        stok = g.mat("stok", "2a1a20", rough=0.4)
        if stand in ("wacht", "wacht_tik"):
            # stok recht voor zich, beide handen op de knop; bij de tik even 0,07 los van de vloer
            til = 0.07 if stand == "wacht_tik" else 0.0
            kz = 0.6 + til
            h._blok(ouder, (0.0, -0.36, (kz + til) / 2), (0.045, 0.045, kz - til), stok, rond=0.015)
            h._bol(ouder, (0.0, -0.36, kz + 0.05), (0.075, 0.075, 0.065), goud, segs=16)
        elif stand == "tenen":
            # stok hoog in de rechterhand, schuin omhoog als een dirigent
            h._blok(ouder, (hx + 0.12, -0.08, hz + 0.25), (0.04, 0.04, 0.6), stok, rot=(0, math.radians(25), 0), rond=0.012)
            h._bol(ouder, (hx + 0.25, -0.08, hz + 0.53), (0.065, 0.065, 0.065), goud, segs=16)
        elif bang:
            h._blok(ouder, (0.6, 0.1, 0.35), (0.04, 0.04, 0.8), stok, rot=(0, math.radians(60), 0), rond=0.012)
        else:
            h._blok(ouder, (hx + 0.02, -0.1, hz / 2), (0.045, 0.045, hz), stok, rond=0.015)
            h._bol(ouder, (hx + 0.02, -0.1, hz + 0.07), (0.065, 0.065, 0.065), goud, segs=16)
    else:
        kraag = g.mat("kraag", "f0c040", rough=0.7)
        bpy.ops.mesh.primitive_torus_add(major_radius=0.19, minor_radius=0.05, location=(0, 0, 0.82))
        o = bpy.context.object; bpy.ops.object.shade_smooth(); o.data.materials.append(kraag); h._kind(o, ouder)
        for kant in (-1, 1):
            h._bol(ouder, (kant * 0.3, 0, 0.72), (0.1, 0.1, 0.09), kraag, segs=16)   # gele pofmouwen
        # luit: rond lijf schuin voor de buik, hals omhoog naar de linkerhand; vliegt weg bij schrik en vallen
        if bang:
            cx, cy, cz, hoek = 0.55, 0.15, 0.25, 70
        else:
            cx, cy, cz, hoek = 0.14, -0.3, 0.48, 62
        lh = g.mat("luit", "8a4a22", rough=0.45, spec=0.5)
        a = math.radians(hoek)
        h._bol(ouder, (cx, cy, cz), (0.22, 0.09, 0.22), lh, rot=(0, -a, 0), segs=32)
        h._bol(ouder, (cx - 0.17 * math.sin(a), cy, cz + 0.17 * math.cos(a)), (0.15, 0.08, 0.15), lh, rot=(0, -a, 0), segs=32)
        h._cil(ouder, (cx - 0.12 * math.sin(a), cy - 0.085, cz + 0.12 * math.cos(a)), 0.055, 0.02, g.mat("luitgat", "3a2018", rough=0.8),
               rot=(math.radians(90), 0, 0), verts=20)
        h._blok(ouder, (cx + 0.06 * math.sin(a), cy - 0.09, cz - 0.06 * math.cos(a)), (0.1, 0.02, 0.03),
                g.mat("luitkam", "5a3420", rough=0.6), rot=(0, -a, 0), rond=0.008)
        nx, nz = cx - 0.62 * math.sin(a), cz + 0.62 * math.cos(a)
        h._blok(ouder, ((cx + nx) / 2 - 0.08 * math.sin(a), cy - 0.02, (cz + nz) / 2 + 0.08 * math.cos(a)), (0.07, 0.05, 0.5), g.mat("luithals", "5a3420", rough=0.6), rot=(0, -a, 0), rond=0.01)
        h._blok(ouder, (nx - 0.06 * math.sin(a), cy + 0.01, nz + 0.06 * math.cos(a)), (0.09, 0.05, 0.12),
                g.mat("luitkop", "5a3420", rough=0.6), rot=(0, -a + math.radians(25), 0), rond=0.015)
    return None
