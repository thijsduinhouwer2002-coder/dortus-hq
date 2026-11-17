import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Test;

(:test)
function testProfielDriePunten(logger as Test.Logger) as Boolean {
    var p = Teken.profiel([10, 50, 90] as Array<Number>, 0, 100, 100, 0, 3);
    return p.size() == 5 && p[1][1] == 90 && p[2][1] == 50 && p[3][1] == 10 && p[3][0] == 100;
}

(:test)
function testProfielTeWeinigWaarden(logger as Test.Logger) as Boolean {
    return Teken.profiel([40] as Array<Number>, 0, 100, 100, 0, 40).size() == 0
        && Teken.profiel([] as Array<Number>, 0, 100, 100, 0, 40).size() == 0;
}

(:test)
function testGolfAantalPunten(logger as Test.Logger) as Boolean {
    return Teken.golf(0, 100, 50, 60, 3, 24).size() == 26;
}

// De toetsen draaien op de fēnix 7 (260 px): daar horen de maten van kolom 260 uit het blad van Mila.
(:test)
function testMatenVan260(logger as Test.Logger) as Boolean {
    var l = Maten.laad();
    logger.debug("maten: " + l.size() + " tijd=" + Maten.m(Maten.TIJD_PX) + " bbY=" + Maten.m(Maten.BB_Y));
    return l.size() == Maten.AANTAL && Maten.m(Maten.TIJD_PX) == 78 && Maten.m(Maten.TIJD_Y) == 78
        && Maten.m(Maten.BB_Y) == 164 && Maten.m(Maten.BB_PX) == 29 && Maten.m(Maten.BB_RAND) == 1 && Maten.m(Maten.VELD_XL) == 73
        && Maten.m(Maten.VELD_XR) == 187 && Maten.m(Maten.WATER_TOP) == 186 && Maten.m(Maten.WATER_BODEM) == 233
        && Maten.m(Maten.VEILIG) == 124;
}

(:test)
function testMatenBuitenDeLijst(logger as Test.Logger) as Boolean {
    return Maten.m(-1) == 0 && Maten.m(Maten.AANTAL) == 0 && Maten.m(999) == 0;
}

// Stap (b) van de kern: thema's en velden.
(:test)
function testThemaKleurenUitHetBlad(logger as Test.Logger) as Boolean {
    return Thema.kleur(Thema.DUSK, Thema.ZEE_BOVEN) == 0xFF8C3C && Thema.kleur(Thema.DUSK, Thema.BOOT) == 0xFFF6E6
        && Thema.kleur(Thema.TIDE, Thema.ZEE_ONDER) == 0x082454 && Thema.kleur(Thema.TIDE, Thema.MINUTEN) == 0x3CDCE6
        && Thema.kleur(Thema.KELP, Thema.TEKST) == 0xDCE8C8 && Thema.kleur(Thema.NIGHT, Thema.PUNT) == 0x6E6EA0
        && Thema.kleur(Thema.NIGHT, Thema.BOOT) == 0xFFDC78 && Thema.kleuren.size() == Thema.AANTAL * Thema.ROLLEN;
}

(:test)
function testThemaOnbekend(logger as Test.Logger) as Boolean {
    return Thema.kleur(99, Thema.UREN) == 0xE1F8FF && Thema.kleur(-1, Thema.UREN) == 0xE1F8FF
        && Thema.kleur(Thema.TIDE, 99) == 0xFFFFFF && Thema.kleur(Thema.TIDE, -1) == 0xFFFFFF;
}

function veldIs(v as Number?, verwacht as String) as Boolean {
    var t = Veld.tekst(v);
    return t != null && t.equals(verwacht);
}

(:test)
function testVeldTekst(logger as Test.Logger) as Boolean {
    return veldIs(0, "0") && veldIs(61, "61") && veldIs(999, "999") && veldIs(1000, "1.0K") && veldIs(8400, "8.4K")
        && veldIs(8499, "8.4K") && veldIs(9999, "9.9K") && veldIs(10000, "10K") && veldIs(12345, "12K")
        && veldIs(999999, "999K") && veldIs(5000000, "999K");
}

// Zonder gegevens geeft een veld null (de wijzerplaat tekent dan een streepje) en stopt de app niet.
(:test)
function testVeldZonderGegevens(logger as Test.Logger) as Boolean {
    var leeg = [] as Array<Number>;
    return Veld.tekst(null) == null && Veld.tekst(-1) == null && Veld.stress(leeg) == null
        && Veld.waarde(Veld.STRESS, leeg) == null && Veld.waarde(99, leeg) == null
        && Veld.stress([10, 35] as Array<Number>) == 35;
}

(:test)
function testHartOngeldig(logger as Test.Logger) as Boolean {
    return Veld.geldigeHart(null) == null && Veld.geldigeHart(255) == null && Veld.geldigeHart(0) == null
        && Veld.geldigeHart(-3) == null && Veld.geldigeHart(61) == 61 && Veld.geldigeHart(254) == 254;
}

// Lege Body Battery of stress: null, de plaat tekent dan het streepje. Anders de nieuwste waarde (achteraan).
(:test)
function testLaatsteWaarde(logger as Test.Logger) as Boolean {
    return Veld.laatste([] as Array<Number>) == null && Veld.laatste([5] as Array<Number>) == 5
        && Veld.laatste([93, 40, 12] as Array<Number>) == 12 && Veld.laatste([0] as Array<Number>) == 0;
}

// Hartslag uit de geschiedenis: de nieuwste geldige, lege en 255 overslaan; niets geldigs is null.
(:test)
function testEersteGeldigeHart(logger as Test.Logger) as Boolean {
    return Veld.eersteGeldigeHart([] as Array<Number?>) == null
        && Veld.eersteGeldigeHart([null, 255, 0] as Array<Number?>) == null
        && Veld.eersteGeldigeHart([255, null, 72, 80] as Array<Number?>) == 72
        && Veld.eersteGeldigeHart([61, 255] as Array<Number?>) == 61;
}

// Stappen en hartslag zonder gegevens: geen tekst (streepje), en nul stappen is wel een getal.
(:test)
function testStappenEnHartZonderGegevens(logger as Test.Logger) as Boolean {
    return Veld.tekst(Veld.geldigeHart(null)) == null && Veld.tekst(Veld.eersteGeldigeHart([255] as Array<Number?>)) == null
        && Veld.tekst(null) == null && veldIs(0, "0");
}

// De proef laat alle vier de thema's zien, en geeft nooit een thema dat niet bestaat.
(:test)
function testProefThema(logger as Test.Logger) as Boolean {
    var gezien = [false, false, false, false] as Array<Boolean>;
    var maten = [208, 240, 260, 390, 454, 176, 320, 218, 280, 416] as Array<Number>;
    for (var i = 0; i < maten.size(); i++) {
        var t = Thema.voorProef(maten[i]);
        if (t < 0 || t >= Thema.AANTAL) {
            return false;
        }
        gezien[t] = true;
    }
    return gezien[0] && gezien[1] && gezien[2] && gezien[3] && Thema.voorProef(260) == Thema.KELP
        && Thema.voorProef(454) == Thema.TIDE && Thema.voorProef(390) == Thema.NIGHT && Thema.voorProef(-5) == Thema.TIDE;
}

// Slaapstand: vier plekken, twee stappen na elkaar nooit op dezelfde plek en hooguit 4 px uit elkaar.
(:test)
function testSlaapSchuif(logger as Test.Logger) as Boolean {
    for (var n = -3; n < 130; n++) {
        var a = Slaap.schuif(n);
        var b = Slaap.schuif(n + 1);
        var d = (a[0] - b[0]).abs() + (a[1] - b[1]).abs();
        if (d < 1 || d > 4 || a[0] < 0 || a[0] > 2 || a[1] < 0 || a[1] > 2) {
            return false;
        }
    }
    return Slaap.schuif(0)[0] == 0 && Slaap.schuif(0)[1] == 0 && Slaap.schuif(59)[0] == 0 && Slaap.schuif(59)[1] == 2
        && Slaap.schuif(60)[0] == 0 && Slaap.schuif(60)[1] == 0;
}

// Het winkelpakket (monkey.jungle) heeft geen proefgedrag: nooit een wit scherm of een slaapbeeld uit zichzelf.
(:test)
function testWinkelZonderProef(logger as Test.Logger) as Boolean {
    return Proef.fase(0) == Proef.WAKKER && Proef.fase(7000) == Proef.WAKKER && Proef.fase(600000) == Proef.WAKKER
        && Proef.schuifTel(41, 7) == 41;
}

// De schoen (stappen): de zool heeft vier punten en schaalt mee met de hoogte van het pictogram.
(:test)
function testSchoenZool(logger as Test.Logger) as Boolean {
    var z = Teken.vlak(Teken.SCHOEN_ZOOL, 100, 50, 12);
    var b = Teken.vlak(Teken.SCHOEN_BOVEN, 100, 50, 12);
    logger.debug("zool: " + z + " boven: " + b.size());
    return z.size() == 4 && b.size() == 9 && z[0][0] == 93 && z[0][1] == 53 && z[1][0] == 107 && z[2][1] == 55;
}

// De zee van Tij (Zee.mc).
(:test)
function testZeeNiveau(logger as Test.Logger) as Boolean {
    return Zee.niveau(0, 186, 233) == 233 && Zee.niveau(100, 186, 233) == 186 && Zee.niveau(150, 186, 233) == 186
        && Zee.niveau(-5, 186, 233) == 233;
}

(:test)
function testZeeLijn(logger as Test.Logger) as Boolean {
    var p = Zee.lijn([40, 80, 20] as Array<Number>, 10, 182, 260, 186, 233, 0);
    logger.debug("lijn: " + p.size() + " nu=" + p[Zee.N][0] + "," + p[Zee.N][1] + " eind=" + p[p.size() - 1][0]);
    return p.size() == Zee.N + Zee.STAART + 1 && p[0][0] == 10 && p[0][1] == Zee.niveau(40, 186, 233)
        && p[Zee.N][0] == 182 && p[Zee.N][1] == Zee.niveau(20, 186, 233) && p[Zee.N / 2][1] == Zee.niveau(80, 186, 233)
        && p[p.size() - 1][0] == 260;
}

// Een volle zee (100) is geen rechte plank: de lijn deint een paar px, alleen omlaag, nooit boven het plafond.
(:test)
function testZeeVolDeint(logger as Test.Logger) as Boolean {
    var p = Zee.lijn([100, 100, 100] as Array<Number>, 10, 182, 260, 186, 233, 0);
    var laagste = 186;
    var hoogste = 999;
    for (var i = 0; i <= Zee.N; i++) {
        var y = p[i][1] as Number;
        if (y > laagste) {
            laagste = y;
        }
        if (y < hoogste) {
            hoogste = y;
        }
    }
    logger.debug("vol: van " + hoogste + " tot " + laagste);
    return hoogste >= 186 && laagste <= 190 && laagste > hoogste;
}

// Eén waarde of geen waarde: toch een hele lijn, vlak rond de hoogte van die waarde of halverwege.
(:test)
function testZeeLijnWeinigGegevens(logger as Test.Logger) as Boolean {
    var een = Zee.lijn([55] as Array<Number>, 10, 182, 260, 186, 233, 0);
    var geen = Zee.lijn([] as Array<Number>, 10, 182, 260, 186, 233, 0);
    var goed = een.size() == Zee.N + Zee.STAART + 1 && geen.size() == een.size() && een[een.size() - 1][0] == 260;
    for (var i = 0; i < een.size(); i++) {
        var d1 = (een[i][1] as Number) - Zee.niveau(55, 186, 233);
        var d0 = (geen[i][1] as Number) - 209;
        if (d1 < -4 || d1 > 4 || d0 < -4 || d0 > 4) {
            goed = false;
        }
    }
    return goed;
}

(:test)
function testZeeBand(logger as Test.Logger) as Boolean {
    var p = Zee.lijn([40, 80, 20] as Array<Number>, 10, 182, 260, 186, 233, 0);
    var b = Zee.band(p, 9, 260, 260);
    return b.size() == p.size() + 3 && b[0][0] == 0 && b[1][1] == (p[0][1] as Number) + 9
        && b[b.size() - 2][0] == 260 && b[b.size() - 2][1] == 260 && b[b.size() - 1][0] == 0
        && Zee.band([] as Array<Graphics.Point2D>, 9, 260, 260).size() == 0;
}

// Het bootje schuift naar links tot het in de veilige cirkel past, maar nooit voorbij de grens bij het getal.
(:test)
function testZeeBootX(logger as Test.Logger) as Boolean {
    var vrij = Zee.bootX(182, 150, 200, 13, 0, 130, 124, 2);
    var krap = Zee.bootX(240, 150, 200, 13, 0, 130, 124, 2);
    var klem = Zee.bootX(240, 236, 200, 13, 0, 130, 124, 2);
    logger.debug("bootX vrij=" + vrij + " krap=" + krap + " klem=" + klem);
    return vrij == 182 && krap < 240 && krap >= 150 && Zee.past(Zee.boot(krap, 200, 13, 0), 130, 124)
        && klem == 236 && Zee.bootX(100, 150, 200, 13, 0, 130, 124, 0) == 150 && Zee.boot(182, 200, 13, -22).size() == 9;
}

(:test)
function testZeeSchuif(logger as Test.Logger) as Boolean {
    return Zee.schuif(176, 5, 190, 20) == 0 && Zee.schuif(176, 5, 175, 20) == 6 && Zee.schuif(176, 5, 150, 20) == 20
        && Zee.schuif(176, 5, 150, -3) == 0 && Zee.topTussen([[10, 50], [20, 30], [90, 5]] as Array<Graphics.Point2D>, 0, 40) == 30
        && Zee.topTussen([] as Array<Graphics.Point2D>, 0, 40) == 9999;
}

(:test)
function testZeeKleuren(logger as Test.Logger) as Boolean {
    return Zee.meng(0xFF8C3C, 0x6E1928, 0, 3) == 0xFF8C3C && Zee.meng(0xFF8C3C, 0x6E1928, 3, 3) == 0x6E1928
        && Zee.meng(0x000000, 0x0000FF, 1, 0) == 0x000000 && Zee.lichter(0xFF8C3C, 70) == 0xFFD282
        && Thema.band(Thema.DUSK, 0, Thema.VOL) == 0xFF8C3C && Thema.band(Thema.DUSK, 3, Thema.VOL) == 0x6E1928
        && Thema.band(Thema.DUSK, 0, Thema.MIP64) == 0xAA5555 && Thema.band(99, 9, Thema.MIP64) == 0x000055;
}

(:test)
function testZeeGolfje(logger as Test.Logger) as Boolean {
    var g = Zee.golfje(100, 50, 16);
    return g.size() == 2 && g[0].size() == 9 && g[0][0][0] == 92 && g[0][8][0] == 108 && (g[0][0][1] as Number) < (g[1][0][1] as Number);
}

// Vier banden per thema, ook op 64 kleuren alle vier verschillend (punt van de keurder, run 130).
(:test)
function testZeeBandenVerschillen(logger as Test.Logger) as Boolean {
    for (var t = 0; t < Thema.AANTAL; t++) {
        for (var m = 0; m < 2; m++) {
            for (var i = 0; i < 3; i++) {
                if (Thema.band(t, i, m) == Thema.band(t, i + 1, m)) {
                    logger.debug("gelijk: thema " + t + " band " + i + " diepte " + m);
                    return false;
                }
            }
        }
    }
    return true;
}

// De kleuren van Mila voor 64 en 8 kleuren (ontwerp/garmin/tij/kleuren-64-8.md): de tabel, het witte zeil, de zwarte
// rand, en op 8 kleuren één vaste zee voor elk thema. Op een vol scherm verandert er niets.
// De toetsen draaien op de fēnix 7 met de lijst van 260 px: die past op 260 px rond, niet op de Instinct 2 (176),
// niet op 360 px en niet op een rechthoek (de Venu Sq 2 heeft een eigen lijst zonder cirkel).
(:test)
function testMatenPassen(logger as Test.Logger) as Boolean {
    return Maten.passen(260, 260) && !Maten.passen(176, 176) && !Maten.passen(360, 360) && !Maten.passen(320, 360)
        && !Maten.passen(240, 240) && Maten.passen(270, 270);
}

(:test)
function testKleuren64En8(logger as Test.Logger) as Boolean {
    var goed = Thema.band(Thema.KELP, 0, Thema.MIP64) == 0xAAAA55 && Thema.band(Thema.NIGHT, 1, Thema.MIP64) == 0x5500AA
        && Thema.band(Thema.TIDE, 3, Thema.MIP64) == 0x000055 && Thema.waterlijn(Thema.DUSK, Thema.MIP64) == 0xFFAAAA
        && Thema.minuten(Thema.KELP, Thema.MIP64) == 0xAAFFAA && Thema.waterlijn(99, Thema.MIP64) == 0xAAFFFF
        && Thema.waterlijn(Thema.DUSK, Thema.VOL) == 0xFFD282 && Thema.minuten(Thema.TIDE, Thema.VOL) == 0x3CDCE6
        && Thema.zeil(Thema.TIDE, Thema.VOL) == 0x3CDCE6 && Thema.rand(Thema.TIDE, Thema.MIP64) == 0x000000
        && Thema.uren(Thema.DUSK, Thema.MIP64) == 0xFFEED6 && Thema.punt(Thema.NIGHT, Thema.MIP64) == 0xAAAAFF && Thema.punt(Thema.KELP, Thema.MIP64) == Thema.minuten(Thema.KELP, Thema.MIP64)
        && Thema.punt(Thema.NIGHT, Thema.VOL) == 0x6E6EA0
        && Thema.mipBanden.size() == Thema.AANTAL * 4 && Thema.mipLijn.size() == Thema.AANTAL && Thema.mipMinuten.size() == Thema.AANTAL;
    for (var t = 0; t < Thema.AANTAL; t++) {
        // Het zeil is op 64 en 8 kleuren wit en dus nooit een kleur van het water.
        for (var d = Thema.MIP64; d <= Thema.MIP8; d++) {
            goed = goed && Thema.zeil(t, d) == 0xFFFFFF && Thema.rand(t, d) == 0x000000;
            for (var i = 0; i < 4; i++) {
                goed = goed && Thema.band(t, i, d) != 0xFFFFFF;
            }
        }
        goed = goed && Thema.band(t, 0, Thema.MIP8) == 0x00FFFF && Thema.band(t, 1, Thema.MIP8) == 0x00FFFF
            && Thema.band(t, 2, Thema.MIP8) == 0x0000FF && Thema.band(t, 3, Thema.MIP8) == 0x0000FF
            && Thema.waterlijn(t, Thema.MIP8) == 0x00FFFF && Thema.minuten(t, Thema.MIP8) == 0x00FFFF
            && Thema.uren(t, Thema.MIP8) == 0xFFFFFF && Thema.punt(t, Thema.MIP8) == 0x00FFFF;
    }
    return goed;
}

(:test)
function testZeeHoogte(logger as Test.Logger) as Boolean {
    var p = [[10, 100], [20, 120], [40, 80]] as Array<Graphics.Point2D>;
    return Zee.hoogte(p, 15) == 110 && Zee.hoogte(p, 30) == 100 && Zee.hoogte(p, 0) == 100 && Zee.hoogte(p, 99) == 80
        && Zee.hoogte([] as Array<Graphics.Point2D>, 5) == 0;
}

// De toetsen bouwen als de winkel: daar geeft Proef.bb altijd de echte geschiedenis terug, nooit de vaste proefdag.
(:test)
function testWinkelEchteGeschiedenis(logger as Test.Logger) as Boolean {
    var echt = [11, 12, 13] as Array<Number>;
    var uit = Proef.bb(echt, Thema.KELP);
    return uit.size() == 3 && uit[0] == 11 && uit[2] == 13 && Proef.bb([] as Array<Number>, Thema.NIGHT).size() == 0;
}

// Slaapstand: het bootje als omtrek. Acht lijnstukken (romp 4, zeil 3, mast 1), romp en zeil gesloten.
(:test)
function testZeeBootLijnen(logger as Test.Logger) as Boolean {
    var b = Zee.boot(200, 300, 20, 0);
    var k = Zee.bootLijnen(b);
    if (k.size() != 8) {
        return false;
    }
    // Romp: elk stuk begint waar het vorige eindigt, en het laatste eindigt op het begin van het eerste.
    for (var i = 0; i < 4; i++) {
        var v = k[(i + 3) % 4];
        if (k[i][0] != v[2] || k[i][1] != v[3]) {
            return false;
        }
    }
    for (var i = 0; i < 3; i++) {
        var v = k[4 + (i + 2) % 3];
        if (k[4 + i][0] != v[2] || k[4 + i][1] != v[3]) {
            return false;
        }
    }
    // Romp van 180 tot 220 breed, mast recht omhoog van de romp tot 30 px boven de waterlijn.
    return k[0][0] == 180 && k[0][2] == 220 && k[0][1] == 297 && k[7][0] == 200 && k[7][1] == 297 && k[7][2] == 200 && k[7][3] == 270
        && Zee.bootLijnen([] as Array<Graphics.Point2D>).size() == 0;
}

// Instellingen: wat de telefoon ook stuurt, er komt een geldig thema uit; niets of onzin wordt Tide.
(:test)
function testKeuzeThema(logger as Test.Logger) as Boolean {
    return Keuze.thema(null) == Thema.TIDE && Keuze.thema(0) == Thema.DUSK && Keuze.thema(2) == Thema.KELP
        && Keuze.thema(3) == Thema.NIGHT && Keuze.thema(4) == Thema.TIDE && Keuze.thema(-1) == Thema.TIDE
        && Keuze.thema("3") == Thema.NIGHT && Keuze.thema("kelp") == Thema.TIDE && Keuze.thema(2.0) == Thema.KELP
        && Keuze.thema(true) == Thema.TIDE && Keuze.thema([2] as Array<Number>) == Thema.TIDE;
}

// De toetsen bouwen als de winkel: daar telt het gekozen thema, niet het thema van de proef. De standaard is Tide.
(:test)
function testWinkelGekozenThema(logger as Test.Logger) as Boolean {
    var proef = Proef.thema(Thema.DUSK, 454) == Thema.DUSK && Proef.thema(Thema.NIGHT, 260) == Thema.NIGHT;
    // Run 134: de instelling lezen alleen bij de betaalde versie. De gratis versie heeft geen instellingen en roept
    // Keuze.leesThema nergens aan (Soort.thema is daar vast Tide); in de simulator stopt die aanroep zonder
    // instellingen met een fout die niet te vangen is (runs 44035849963 en 44037821030).
    if (Soort.BETAALD) {
        return proef && Keuze.leesThema() == Thema.TIDE;
    }
    return proef && Soort.thema() == Thema.TIDE;
}

// Past bij de versie die gebouwd is (de toetsen draaien als betaald en als gratis): betaald neemt thema en velden
// uit de instellingen, met als standaard hartslag, stress en stappen; gratis heeft Tide en die drie velden vast.
(:test)
function testSoortPastBijVersie(logger as Test.Logger) as Boolean {
    logger.debug("betaald=" + (Soort.BETAALD ? "ja" : "nee"));
    var v = Soort.velden();
    var drie = v.size() == 3 && v[0] == Veld.HART && v[1] == Veld.STRESS && v[2] == Veld.STAPPEN;
    if (Soort.BETAALD) {
        return drie && Soort.thema() == Keuze.leesThema();
    }
    return drie && Soort.thema() == Thema.TIDE;
}
