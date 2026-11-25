"""Helden in 3D, eerste stand-in (Daan, 13 nov 2026).

Twee helden die het hol binnenlopen en hun hoed verliezen aan Gloops toren. Zelfde hoeden als in
gloop.py (helm en heksenhoed), zodat je ziet waar de toren vandaan komt.
  ridder = blauwe tuniek, stalen helm met neusstuk, zwaard, rond schild
  heks   = oranje jurk, brede heksenhoed met gouden band, bezem met een geel borstel (ronde 3)

Speelgoedstijl zoals Gloop (3d-stijl.md, regel 2): groot hoofd, twee grote ogen met glimstip,
korte beentjes. Op ware grootte (120 px = 4,5 eenheden) is een held ±1,9 eenheden hoog, ±50 px:
iets groter dan Gloop, want hij komt binnen als bedreiging en wordt toch opgegeten.

Als module (Mila, hol.py):
    import held
    held.bouw("ridder", "stap1", plek=(-6.0, 0.2, 0.0), draai=35)
  draai = graden om de hoogte-as; positief kijkt naar rechts (naar de schat).
  stand = rust, stap1, stap2 (twee stappen om te lopen), schrik (armen omhoog boven de put),
          vallen (voorover gekanteld met armen omhoog, voor in de stekelput)
  schaal = 1.0 geeft ±1,8 eenheden (ridder met helm). De gangen van hol.py zijn 1,5 hoog:
           gebruik daar schaal 0.75 (±36 px op ware grootte), zodat de hoed niet in het plafond zit.
  gloed  = 0 (uit) of bijvoorbeeld 25: een zacht lampje voor het gezicht, voor in de donkere gang.
  rand   = 0 (uit) of bijvoorbeeld 40: een koel licht schuin achter de held, zodat hoed en schouders
           een lichte rand krijgen en hij loskomt van een donkere gang (ronde 2).

Ronde 2 (13 nov): hoofd ±20% groter (op ±30 px telt alleen het hoofd met de hoed), schild vast aan
de linkerhand, heks houdt de staf voor zich uit, rode pluim op de helm (leest niet meer als schaal),
stand vallen erbij.

Los renderen:
    <venv>/bin/python held.py <uit.png> <soort> <stand> <breedte> <hoogte> <samples> [kleur]
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy
import gedeeld as g
import held_soorten as hs_

HUID = "f2c2a0"
HUID_D = "d89a7a"


def _kind(o, ouder):
    o.parent = ouder
    return o


def _bol(ouder, loc, schaal, m, rot=(0, 0, 0), segs=32):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segs, ring_count=segs // 2, location=loc, rotation=rot)
    o = bpy.context.object; o.scale = schaal
    bpy.ops.object.shade_smooth(); o.data.materials.append(m)
    return _kind(o, ouder)


def _cil(ouder, loc, r, d, m, rot=(0, 0, 0), r2=None, verts=32):
    if r2 is None:
        bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=d, location=loc, rotation=rot)
    else:
        bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r, radius2=r2, depth=d, location=loc, rotation=rot)
    o = bpy.context.object; bpy.ops.object.shade_smooth(); o.data.materials.append(m)
    return _kind(o, ouder)


def _blok(ouder, loc, maat, m, rot=(0, 0, 0), rond=0.02):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    o = bpy.context.object; o.scale = maat
    if rond:
        b = o.modifiers.new("rond", "BEVEL"); b.width = rond; b.segments = 3
    o.data.materials.append(m)
    return _kind(o, ouder)


def _staaf(ouder, a, b, r, m, verts=24):
    """Cilinder van punt a naar punt b (been, arm), zodat ledematen meezwaaien in plaats van te schuiven."""
    from mathutils import Vector
    a, b = Vector(a), Vector(b)
    d = b - a
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=max(0.02, d.length), location=(a + b) / 2)
    o = bpy.context.object
    o.rotation_mode = "QUATERNION"
    o.rotation_quaternion = d.to_track_quat("Z", "Y")
    bpy.ops.object.shade_smooth(); o.data.materials.append(m)
    return _kind(o, ouder)


# Mila 25 nov (issue 32): elke soort een eigen loop. S = afstand die een voet aflegt van voor naar achter
# (eenheden), L = hoe hoog de zwaaivoet komt, bob = op en neer per stap, hop = sprongetje in de doorzwaai,
# buig = voorover (graden), zak = door de knieen, wieg = heen en weer (graden), dx = halve spreidstand,
# zwaai = hoe ver de vrije hand meezwaait. fps = voorstel voor het spel (Olaf), loopsnelheid = stap_px x fps.
LOOP = {
    # Mila 25 nov run 2: ridder liep stijf. Nu een zware stamp: dieper zakken op contact, meer wiegen, schild zwaait iets mee.
    "ridder": dict(S=0.24, L=0.07, bob=0.035, hop=0.0, buig=3, zak=0.02, wieg=8, dx=0.16, zwaai=8, fps=8),
    "dief": dict(S=0.46, L=0.13, bob=0.03, hop=0.0, buig=16, zak=0.07, wieg=0, dx=0.12, zwaai=0, fps=12),
    "bard": dict(S=0.30, L=0.08, bob=0.015, hop=0.12, buig=-3, zak=0.0, wieg=0, dx=0.12, zwaai=0, fps=10),
    # run 2: laarsjes komen onder de kortere mantel uit, dus de voet tilt hoger, zodat je haar ziet lopen.
    "heks": dict(S=0.28, L=0.07, bob=0.015, hop=0.0, buig=0, zak=0.0, wieg=4, dx=0.11, zwaai=22, fps=8),
    "held": dict(S=0.34, L=0.09, bob=0.025, hop=0.0, buig=4, zak=0.0, wieg=0, dx=0.13, zwaai=22, fps=10),
}
LOOPDRAAI = -40     # loopt naar rechts in beeld, net als in het spel (voor 25 nov keken ze naar links: maanloop)
STANDEN = ["rust", "stap1", "stap2", "stap3", "stap4", "stap5", "stap6", "schrik", "vallen", "kijk", "draai", "sprong"]


def stand_draai(stand):
    """Hoe de held in beeld staat per stand (graden, zie bouw)."""
    return {"kijk": 0, "draai": 15}.get(stand, LOOPDRAAI)


def stap_eenheid(soort):
    """Hoeveel eenheden de held per loopbeeld naar rechts in beeld moet schuiven, zodat de voet op de vloer stilstaat."""
    lp = LOOP.get(soort, LOOP["held"])
    return lp["S"] / 3 * abs(math.sin(math.radians(LOOPDRAAI)))


def _voeten(stand, lp):
    """{kant: (naar voren, optillen, teen in graden)} voor kant -1 (links) en 1 (rechts)."""
    S, L = lp["S"], lp["L"]
    fase = [(S / 2, 0.0, -14), (S / 6, 0.0, 0), (-S / 6, 0.0, 6), (-S / 2, 0.025, 28), (-S / 6, 0.7 * L, 18), (S / 6, L, -6)]
    if stand.startswith("stap") and stand[4:].isdigit():
        i = (int(stand[4:]) - 1) % 6
        hop = lp["hop"] if i in (2, 5) else 0.0
        l, r = fase[i], fase[(i + 3) % 6]
        return {-1: (l[0], l[1] + hop, l[2]), 1: (r[0], r[1] + hop, r[2])}
    if stand == "draai":
        return {-1: (0.08, 0.0, 0), 1: (-0.1, 0.03, 32)}   # draait op de bal van de achterste voet
    if stand == "sprong":
        return {-1: (0.1, 0.25, -25), 1: (-0.06, 0.2, 25)}   # voeten opgetrokken
    if stand == "kijk":
        return {-1: (0.03, 0.0, 0), 1: (-0.02, 0.0, 0)}
    return {-1: (0.0, 0.0, 0), 1: (0.0, 0.0, 0)}


def _romp(stand, lp):
    """(omhoog, voorover in graden, opzij in graden) voor alles boven de benen."""
    if stand == "vallen":
        return 0.0, 0.0, 0.0
    zak = 0.0 if stand in ("schrik",) else lp["zak"]
    buig = 0.0 if stand in ("schrik", "kijk") else lp["buig"]
    if stand.startswith("stap") and stand[4:].isdigit():
        i = (int(stand[4:]) - 1) % 6
        dz = [0.0, -lp["bob"], lp["bob"]][i % 3] + (lp["hop"] if i in (2, 5) else 0.0)
        wieg = lp["wieg"] * [0.6, 1.0, 0.6][i % 3] * (1 if i < 3 else -1)
        return dz - zak, buig, wieg
    if stand == "sprong":
        return 0.24 - zak, buig, 0.0
    if stand == "draai":
        return -zak, buig * 0.5, -4.0
    return -zak, buig, 0.0


def _noem_hoed(voor, naam):
    """Daan 13 nov (keuze A van Bram): elk hoedobject heet hoed_<naam>_..., zodat de pijplijn met
    HOL_VERBERG ["hoed"] een held zonder hoed rendert en het spel de hoed van held.gd erop zet.
    Zonder HOL_VERBERG verandert er niets aan het beeld."""
    for o in bpy.data.objects:
        if o not in voor and o.type not in ("CAMERA", "LIGHT"):
            o.name = "hoed_" + naam + "_" + o.name


def bouw(soort="ridder", stand="rust", plek=(0, 0, 0), draai=30, schaal=1.0, gloed=0, rand=0, kleur=0):
    """Bouwt één held met de voeten op plek. Geeft het ouderobject terug.
    soort: ridder, heks, held, dief, bard (die laatste drie in held_soorten.py). kleur: tuniek 0 tot 4 (alleen held)."""
    sc = bpy.context.scene
    ouder = bpy.data.objects.new("held_" + soort, None)
    sc.collection.objects.link(ouder)

    # ronde 3: matte speelgoedlak (frisse kijker ronde 2: "plastic glanst zo sterk dat ze goedkoop ogen")
    huid = g.mat("huid", HUID, rough=0.62, spec=0.25, sss=0.2)
    blos = g.mat("hblos", "blos", rough=0.7)
    wit = g.mat("hwit", "oogwit", rough=0.2, spec=0.5)
    pupil = g.mat("hpupil", "pupil", rough=0.35)
    glim = g.mat("hglim", "oogwit", emis=4.0)
    laars = g.mat("laars", "4a2e2a", rough=0.6)
    if soort in hs_.SOORTEN:
        kleed, kleed_d = hs_.kleding(soort, kleur)
    elif soort == "ridder":
        kleed = g.mat("tuniek", "4a86f0", rough=0.72, spec=0.25)
        kleed_d = g.mat("tuniek_d", "2a4a94", rough=0.75, spec=0.2)
    else:
        # jurk warm oranje, niet paars: paars op het pruimen hol viel weg (frisse kijker ronde 1)
        kleed = g.mat("jurk", "e8873a", rough=0.75, spec=0.25)
        kleed_d = g.mat("jurk_d", "a8552a", rough=0.75, spec=0.2)

    # benen (Mila 25 nov, issue 32): loopcyclus van 6 beelden, voeten op de vloer en elke soort een eigen loop.
    # Een voet op de grond schuift per beeld precies S/3 naar achteren, zodat hij stil op de vloer staat als het spel
    # de held stap_px naar voren zet. Het been is een staaf van heup naar enkel, dus het zwaait mee.
    lp = LOOP.get(soort, LOOP["held"])
    bang = stand in ("schrik", "vallen")
    voeten = _voeten(stand, lp)
    stap = voeten[-1][0] / (lp["S"] / 2) if stand.startswith("stap") else 0.0   # -1 tot 1: linkervoet voor of achter
    benen = set()
    voor_benen = set(bpy.data.objects)
    heup_z = 0.4 + _romp(stand, lp)[0]
    for kant in (-1, 1):
        dx = lp["dx"] * kant
        if stand == "vallen":
            # ronde 4: benen gespreid en schuin (spartelen), leest op 25 px als een V van laarzen
            sp = math.radians(28)
            _cil(ouder, (dx + 0.07 * kant, 0, 0.2), 0.075, 0.3, kleed_d, rot=(0, -kant * sp, 0))
            _bol(ouder, (dx + 0.15 * kant, -0.04, 0.07), (0.1, 0.12, 0.075), laars)
            continue
        vy, til, teen = voeten[kant]
        y = -vy                              # -y is naar voren (het gezicht kijkt naar -y)
        _staaf(ouder, (dx * 0.8, 0.0, heup_z), (dx, y, 0.11 + til), 0.075, kleed_d)
        _bol(ouder, (dx, y - 0.04, 0.06 + til), (0.1, 0.12, 0.075), laars, rot=(math.radians(teen), 0, 0))
    benen = set(bpy.data.objects) - voor_benen

    # lijf: rond, iets peervormig
    if soort != "heks":
        _bol(ouder, (0, 0, 0.55), (0.3, 0.26, 0.3), kleed)
        _cil(ouder, (0, 0, 0.42), 0.27, 0.07, g.mat("riem", "4a2e2a", rough=0.5))
        _blok(ouder, (0, -0.27, 0.42), (0.08, 0.02, 0.07), g.mat("gesp", "goud", rough=0.2, metaal=0.9), rond=0.01)
    else:
        # Mila 25 nov run 2: zoom op 0.24 in plaats van 0.15 en smaller, zodat de laarsjes eronder uitkomen
        # (keurpunt: haar benen vielen weg onder de jurk). De zoom zwaait iets mee met de stap.
        zoom = _cil(ouder, (0, 0, 0.5), 0.32, 0.52, kleed, r2=0.2)
        zoom.rotation_euler = (math.radians(-6 * stap), 0, 0)
        _bol(ouder, (0, 0, 0.75), (0.21, 0.19, 0.12), kleed)
        _cil(ouder, (0, 0, 0.62), 0.26, 0.05, g.mat("koord", "goud", rough=0.3, metaal=0.6))

    # hoofd: groot (speelgoed), met twee grote ogen en een kleine o-mond
    # ronde 2: alles van het hoofd x1,2 rond het midden (HZ); de ogen staan zo op dezelfde plek in het gezicht
    HZ = 1.24
    K = 1.2

    def hk(x, y, z):   # plek op het hoofd, geschaald rond het hoofdmidden
        return (x * K, y * K, HZ + (z - HZ) * K)

    def hs(a, b, c):
        return (a * K, b * K, c * K)

    _bol(ouder, (0, 0, HZ), hs(0.36, 0.33, 0.34), huid, segs=48)
    oy = 0.0
    if soort in hs_.SOORTEN:
        hs_.haar(ouder, soort, kleur, hk, hs, HZ)
        if soort == "dief":
            hs_.masker(ouder, hk, hs, HZ)
            oy = -0.03   # ogen iets naar voren, zodat ze wit op het zwarte masker liggen
    for kant in (-1, 1):
        ox = 0.11 * kant   # Mila 14 nov: was 0.13; ogen en blos iets naar binnen en dieper, zodat het achterste oog bij draai -40 binnen het hoofd blijft (kan Daan 18:28)
        if soort == "dief":   # Bram 15 nov: kleiner oogwit op het masker; groot wit om zwart las als een vlek
            _bol(ouder, hk(ox, -0.27 + oy, HZ + 0.0), hs(0.055, 0.05, 0.045), wit)   # Daan proef: oogwit midden in de band, niet erboven
        else:
            _bol(ouder, hk(ox, -0.27 + oy, HZ + 0.02), hs(0.1, 0.05, 0.12), wit)
        kijk = 0.025 if not bang else (0.06 if stand == "schrik" else 0.0)
        if stand == "kijk":
            kijk = 0.0   # kijkt de speler recht aan   # ronde 4 (plus = naar rechts in beeld, getoetst): schrik kijkt opzij naar wat hem bang maakt (naar rechts, naar Gloop), niet in de camera
        if soort == "dief":   # Daan proef: kleine pupil binnen het oogwit, zodat het oog een wit gaatje in de band is
            _bol(ouder, hk(ox + kijk * 0.6, -0.31 + oy, HZ - 0.005), hs(0.03, 0.03, 0.032), pupil)
        else:
            _bol(ouder, hk(ox + kijk, -0.31 + oy, HZ + 0.0), hs(0.06, 0.03, 0.075), pupil)
        if soort != "dief":   # Bram 15 nov: geen glimstip op het masker, las als losse witte ruis (frisse kijker)
            _bol(ouder, hk(ox + kijk + 0.025, -0.335 + oy, HZ + 0.04), hs(0.02, 0.01, 0.02), glim, segs=12)
        _bol(ouder, hk(0.18 * kant, -0.25, HZ - 0.1), hs(0.06, 0.02, 0.035), blos, segs=16)
    if bang:
        _bol(ouder, hk(0, -0.32, HZ - 0.15), hs(0.05, 0.02, 0.06), g.mat("hmond", "mond", rough=0.6), segs=16)
    else:
        # vastberaden: kleine glimlach (halve ring) en twee wenkbrauwen die naar binnen zakken
        # (frisse kijker ronde 1: de o-mond las als "verbaasd of leeg")
        bpy.ops.mesh.primitive_torus_add(major_radius=0.065 * K, minor_radius=0.017 * K, location=hk(0.02, -0.325, HZ - 0.12),
                                         rotation=(math.radians(90), 0, 0))
        lach = bpy.context.object; lach.data.materials.append(g.mat("hmond", "mond", rough=0.6)); _kind(lach, ouder)
        bpy.ops.mesh.primitive_cube_add(size=1, location=hk(0.02, -0.325, HZ - 0.07)); sn2 = bpy.context.object
        sn2.scale = hs(0.3, 0.2, 0.1); sn2.hide_render = True; sn2.hide_viewport = True; _kind(sn2, ouder)
        bl = lach.modifiers.new("snij", "BOOLEAN"); bl.object = sn2; bl.operation = "DIFFERENCE"
        brauw = g.mat("brauw", "5a3a2a", rough=0.6)
        for kant in (-1, 1):
            _blok(ouder, hk(0.13 * kant, -0.31, HZ + 0.15), hs(0.1, 0.02, 0.025), brauw,
                  rot=(0, math.radians(18 * kant), 0), rond=0.01)
    _bol(ouder, hk(0, -0.34, HZ - 0.05), hs(0.04, 0.03, 0.035), g.mat("neus", HUID_D, rough=0.5), segs=16)

    # armen en handen
    arm_z = 0.7
    if stand == "vallen":
        hoek_l, hoek_r = 105, 105   # ronde 4: armen wijd opzij, niet omhoog (op 25 px een plus-teken)
    elif bang:
        hoek_l, hoek_r = 150, 150
    else:
        hoek_l, hoek_r = 20, 20   # armen zwaaien naar voren en achteren (hieronder), niet opzij
        if soort == "heks":
            hoek_r = 70   # staf voor zich uit, zodat je arm en hand ziet (frisse kijker ronde 1)
    if soort in hs_.SOORTEN and hs_.armen(soort, stand, stap):
        hoek_l, hoek_r = hs_.armen(soort, stand, stap)
    if stand in ("kijk", "draai"):
        hoek_l, hoek_r = (12, 12) if stand == "kijk" else (40, 40)
        if soort == "heks":
            hoek_r = 70
        if soort in hs_.SOORTEN and hs_.armen(soort, "rust", 0):
            hoek_l, hoek_r = hs_.armen(soort, "rust", 0)   # dief houdt zijn zak, bard zijn luit
    elif stand == "sprong":
        hoek_l, hoek_r = 125, (80 if soort == "heks" else 125)   # armen omhoog, de heks houdt haar bezem
        if soort in ("dief", "bard"):
            hoek_l, hoek_r = hs_.armen(soort, "rust", 0)
    hy = hs_.hand_y(soort, stand) if soort in hs_.SOORTEN else -0.02
    handen = {}
    for kant, hoek in ((-1, hoek_l), (1, hoek_r)):
        a = math.radians(hoek)
        hx = kant * (0.3 + 0.18 * math.sin(a))
        hz = arm_z - 0.22 * math.cos(a)
        # vrije hand (links bij held en heks) zwaait tegen de benen in: linkervoet voor = linkerhand achter (+y)
        hyk = hy + (0.2 * stap * lp["zwaai"] / 20 if kant == -1 else 0.0)
        _staaf(ouder, (kant * 0.29, 0.0, arm_z), (hx, hyk, hz), 0.055, kleed)
        # Bram 15 nov (kan Daan 07:35): de dief draagt donkere handschoenen. De lichte linkerhand bij zijn wang
        # las op ware grootte als witte druppels naast het masker, zodat de band een witte rand leek te krijgen.
        hand_mat = g.mat("handschoen", "3a2e34", rough=0.7, spec=0.2) if soort == "dief" else huid
        _bol(ouder, (hx, hyk, hz), (0.085, 0.085, 0.085), hand_mat, segs=16)
        handen[kant] = (hx, hz)

    # spullen
    hx, hz = handen[1]
    if soort in hs_.SOORTEN:
        hs_.spullen(ouder, soort, stand, handen, kleur)
        top = HZ + 0.4 * K   # geen eigen hoed: de kruin van het haar
    elif soort == "ridder":
        staal = g.mat("hstaal", "staal", rough=0.42, spec=0.6, metaal=0.8)   # ronde 2b: minder spiegel, oogde goedkoop plastic
        goud = g.mat("hgoud", "goud", rough=0.2, metaal=0.9, emis=0.1)
        # zwaard rechtop in de rechterhand, iets schuin naar voren
        _blok(ouder, (hx, -0.06, hz + 0.33), (0.05, 0.015, 0.5), staal, rot=(0, math.radians(-12), 0), rond=0.008)
        _blok(ouder, (hx - 0.01, -0.06, hz + 0.06), (0.2, 0.04, 0.04), goud, rond=0.01)
        _bol(ouder, (hx + 0.005, -0.06, hz - 0.05), (0.035, 0.035, 0.035), goud, segs=12)
        # rond schild vast aan de linkerhand (ronde 2: zweefde los voor het lijf)
        lx, lz = handen[-1]
        if stand == "vallen":
            # schild vliegt los achter hem (frisse kijker ronde 2: schild bij het hoofd verwarde de val)
            lx, lz = -0.55, 0.15
        sx, sz = lx - 0.04, lz + 0.12   # run 2: schild hoger, zodat de benen eronder zichtbaar zijn
        _cil(ouder, (sx, -0.12, sz), 0.21, 0.05, g.mat("schild", "rood", rough=0.5),
             rot=(math.radians(90), 0, math.radians(-25)))
        bpy.ops.mesh.primitive_torus_add(major_radius=0.2, minor_radius=0.025, location=(sx, -0.15, sz),
                                         rotation=(math.radians(90), 0, math.radians(-25)))
        rnd = bpy.context.object; bpy.ops.object.shade_smooth(); rnd.data.materials.append(goud); _kind(rnd, ouder)
        _cil(ouder, (sx - 0.01, -0.165, sz), 0.06, 0.05, goud,
             rot=(math.radians(90), 0, math.radians(-25)))
        voor = set(bpy.data.objects)   # Daan 13 nov: alles wat hierna komt tot top= is de hoed
        # helm: zelfde als Gloops helm (koepel, rand, punt, neusstuk)
        bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, location=hk(0, 0, HZ + 0.1))
        helm = bpy.context.object; helm.scale = hs(0.37, 0.35, 0.33)
        bpy.ops.object.shade_smooth(); helm.data.materials.append(staal); _kind(helm, ouder)
        bpy.ops.mesh.primitive_cube_add(size=1, location=hk(0, 0, HZ - 0.12)); sn = bpy.context.object
        sn.scale = (2, 2, 0.44 * K); sn.hide_render = True; sn.hide_viewport = True; _kind(sn, ouder)
        bm = helm.modifiers.new("snij", "BOOLEAN"); bm.object = sn; bm.operation = "DIFFERENCE"
        _cil(ouder, hk(0, 0, HZ + 0.11), 0.385 * K, 0.05 * K, staal)
        # rode pluim in plaats van punt en neusstuk: helm leest niet meer als schaal of pannendeksel,
        # en geeft de ridder op 30 px een eigen kleur bovenop (zelfde pluim als op Gloops toren)
        pluim = g.mat("pluim", "rood", rough=0.7)
        for i, (px, pz, ps) in enumerate([(0.0, 0.47, 0.11), (0.06, 0.55, 0.1), (0.13, 0.6, 0.085), (0.2, 0.6, 0.07)]):
            _bol(ouder, hk(px, 0.02, HZ + pz), hs(ps, ps * 0.8, ps), pluim, segs=16)
        top = HZ + 0.68 * K
        _noem_hoed(voor, "helm")
    else:
        hout = g.mat("hout", "7a4a2a", rough=0.6)
        # ronde 3: bezem in plaats van staf, als eigen trek (zoals Gloops munt): steel schuin over de
        # schouder, gele borstel omhoog naast de hoed. Op 25 px is dat een eigen silhouet; een staf was een streepje.
        sk = math.radians(28) if not bang else math.radians(8)
        tx, tz = hx + 0.5 * math.sin(sk), hz + 0.62 * math.cos(sk)
        _cil(ouder, (hx + 0.15 * math.sin(sk), -0.04, hz + 0.15 * math.cos(sk)), 0.03, 0.95, hout, rot=(0, sk, 0))
        borstel = g.mat("borstel", "e8c25a", rough=0.85, spec=0.1)
        bx, bz = hx + 0.68 * math.sin(sk), hz + 0.68 * math.cos(sk)
        _cil(ouder, (bx, -0.04, bz), 0.045, 0.08, g.mat("bezemkoord", "rood", rough=0.7), rot=(0, sk, 0))
        _cil(ouder, (bx + 0.13 * math.sin(sk), -0.04, bz + 0.13 * math.cos(sk)), 0.05, 0.3, borstel,
             rot=(0, sk, 0), r2=0.16, verts=20)
        # klein groen lichtje blijft, nu als vonkje bij de borstel
        tx, tz = bx + 0.32 * math.sin(sk), bz + 0.32 * math.cos(sk)
        _bol(ouder, (tx, -0.06, tz), (0.05, 0.05, 0.05), g.mat("lichtje", "a8f0cf", emis=6.0), segs=12)
        l = bpy.data.lights.new("staflicht", "POINT"); l.color = (0.6, 1.0, 0.85); l.energy = 3
        l.shadow_soft_size = 0.1
        lo = bpy.data.objects.new("staflicht", l); lo.location = (tx, -0.2, tz)
        sc.collection.objects.link(lo); _kind(lo, ouder)
        # haar: twee paarse vlechten onder de hoed
        haar = g.mat("haar", "c8423b", rough=0.7)
        for kant in (-1, 1):
            _bol(ouder, hk(0.3 * kant, 0.02, HZ - 0.1), hs(0.08, 0.08, 0.16), haar, segs=16)
        # heksenhoed: zelfde als op Gloops toren
        voor = set(bpy.data.objects)
        pa = g.mat("hpaars", "paars", rough=0.65)
        _cil(ouder, hk(0, 0, HZ + 0.24), 0.55 * K, 0.04 * K, pa)
        _cil(ouder, hk(0, 0, HZ + 0.3), 0.32 * K, 0.08 * K, g.mat("hband", "goud", rough=0.3, metaal=0.6), r2=0.3 * K)
        _cil(ouder, hk(0, 0.0, HZ + 0.6), 0.31 * K, 0.65 * K, pa, r2=0.05 * K)
        _cil(ouder, hk(-0.13, 0, HZ + 0.98), 0.055 * K, 0.2 * K, pa, r2=0.0, rot=(0, math.radians(-35), 0))
        top = HZ + 1.05 * K
        _noem_hoed(voor, "heksenhoed")

    # romp (Mila 25 nov): alles boven de benen gaat op en neer, buigt voorover of wiegt, rond de heup
    dz, buig, wieg = _romp(stand, lp)
    if dz or buig or wieg:
        from mathutils import Matrix
        heup = Matrix.Translation((0, 0, 0.4))
        m = Matrix.Translation((0, 0, dz)) @ heup @ Matrix.Rotation(math.radians(buig), 4, "X") \
            @ Matrix.Rotation(math.radians(wieg), 4, "Y") @ heup.inverted()
        for o in list(ouder.children):
            if o not in benen:
                o.matrix_basis = m @ o.matrix_basis
    ouder.location = plek
    ouder.scale = (schaal, schaal, schaal)
    if stand == "vallen":
        # ronde 4: kop naar beneden de put in, laarzen omhoog (cartoon-val; 35 graden voorover las op
        # 25 px als struikelen). Draai rond het midden van de figuur, zodat hij in hetzelfde vak blijft.
        ouder.rotation_mode = "ZYX"
        ouder.rotation_euler = (0, math.radians(155), math.radians(-draai))
        ouder.location = (plek[0], plek[1], plek[2] + 0.95 * top * schaal)
    else:
        ouder.rotation_euler = (0, 0, math.radians(-draai))
    # gebouwd met het gezicht naar -y (de camera); draai positief kijkt naar rechts
    ouder["top"] = top * schaal
    if gloed:
        # eigen zacht licht voor het gezicht, voor in een donkere gang (zoals Mila's gloopgloed)
        gl = bpy.data.lights.new("heldgloed", "POINT"); gl.color = (1.0, 0.85, 0.65); gl.energy = gloed
        gl.shadow_soft_size = 0.6
        go = bpy.data.objects.new("heldgloed", gl); sc.collection.objects.link(go)
        go.location = (plek[0] + 0.3, plek[1] - 1.0, plek[2] + 1.3 * schaal)
    if rand:
        # koel licht schuin achter en boven de held: lichte rand om hoed en schouders
        rl = bpy.data.lights.new("heldrand", "POINT"); rl.color = (0.7, 0.8, 1.0); rl.energy = rand
        rl.shadow_soft_size = 0.3
        ro = bpy.data.objects.new("heldrand", rl); sc.collection.objects.link(ro)
        ro.location = (plek[0] - 0.5 * schaal, plek[1] + 0.55, plek[2] + 2.0 * schaal)
        ro.visible_camera = False
    return ouder


if __name__ == "__main__":
    uit = sys.argv[1]
    SOORT, STAND = sys.argv[2], sys.argv[3]
    W, H, SAMPLES = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    KLEUR_NR = int(sys.argv[7]) if len(sys.argv) > 7 else 0
    g.leeg()
    h = bouw(SOORT, STAND, (0, 0, 0), draai=stand_draai(STAND), kleur=KLEUR_NR)   # Mila 25 nov: was 30 (keek naar links)
    bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, 0))
    bpy.context.object.is_shadow_catcher = True
    top = h["top"]
    g.camera(hoogte_midden=top / 2 - 0.1, schaal=max(2.4, top * 1.25))
    g.licht()
    g.render(uit, W, H, SAMPLES, doorzichtig=True)
    print("klaar", uit)
