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
