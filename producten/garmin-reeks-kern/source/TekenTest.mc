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
        && Maten.m(Maten.BB_Y) == 166 && Maten.m(Maten.BB_PX) == 29 && Maten.m(Maten.VELD_XL) == 73
        && Maten.m(Maten.VELD_XR) == 187 && Maten.m(Maten.WATER_TOP) == 182 && Maten.m(Maten.WATER_BODEM) == 233
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
