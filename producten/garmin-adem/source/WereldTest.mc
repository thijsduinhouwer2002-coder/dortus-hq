import Toybox.Lang;
import Toybox.Test;

// Maan en dagdeel (besluit 12 nov 00:25 punt 2) en de wereldgegevens van Mila.
(:test)
function testMaanfaseBekendeDagen(logger as Test.Logger) as Boolean {
    // Nieuwe maan 9 nov 2026 07:02 UTC, eerste kwartier 17 nov 2026, volle maan 24 nov 2026 14:53 UTC,
    // volle maan 21 jan 2000, nieuwe maan (zonsverduistering) 21 aug 2017.
    var a = EbbLucht.maanfase(1794207720);
    var b = EbbLucht.maanfase(1794916080);
    var c = EbbLucht.maanfase(1795531980);
    var e = EbbLucht.maanfase(948429600);
    var f = EbbLucht.maanfase(1503340200);
    logger.debug("maan " + a + " " + b + " " + c + " " + e + " " + f);
    return a == 0 && b == 2 && c == 4 && e == 4 && f == 0;
}

(:test)
function testDagdeel(logger as Test.Logger) as Boolean {
    return EbbLucht.dagdeel(4) == 3 && EbbLucht.dagdeel(5) == 0 && EbbLucht.dagdeel(9) == 1 && EbbLucht.dagdeel(17) == 1
        && EbbLucht.dagdeel(18) == 2 && EbbLucht.dagdeel(21) == 3 && EbbLucht.dagdeel(0) == 3;
}

(:test)
function testWereldGegevens(logger as Test.Logger) as Boolean {
    // Schildpad, krab en clownvis hebben een wereld met een thuis binnen het scherm; een dier zonder wereld geeft null.
    var goed = EbbWereldData.vlakken(0) == null && EbbWereldData.thuis(0) == null;
    var dieren = [3, 4, 7] as Array<Number>;
    for (var i = 0; i < dieren.size(); i += 1) {
        var vl = EbbWereldData.vlakken(dieren[i]);
        var th = EbbWereldData.thuis(dieren[i]);
        if (vl == null || th == null || vl.size() < 3 || th[0] < 20 || th[0] > 240 || th[1] < EbbWereldData.BOVEN || th[1] > 240) {
            goed = false;
            continue;
        }
        var punten = 0;
        for (var j = 0; j < vl.size(); j += 1) {
            var n = (vl[j].size() - 1) / 2;
            punten += n;
            if (n < 3 || n > 64 || vl[j].size() % 2 != 1) {
                goed = false;
            }
        }
        logger.debug("wereld " + dieren[i] + " vlakken " + vl.size() + " punten " + punten);
        if (punten > 120) {
            goed = false;
        }
    }
    return goed;
}

(:test)
function testWekenTotaalGroeitEnZaktNiet(logger as Test.Logger) as Boolean {
    // Week 20 gehaald: 0 naar 1. Nog een sessie in dezelfde week: blijft 1. Week 21 nog niet gehaald: blijft 1.
    // Week 25 na vier gemiste weken gehaald: 2 (een gemiste week haalt niets weg).
    var t = EbbTrouw.wekenTotaalNa(0, 20, false, 20, true);
    var a = t;
    t = EbbTrouw.wekenTotaalNa(t, 20, true, 20, true);
    var b = t;
    t = EbbTrouw.wekenTotaalNa(t, 20, true, 21, false);
    var c = t;
    t = EbbTrouw.wekenTotaalNa(t, 21, false, 25, true);
    logger.debug("weken " + a + " " + b + " " + c + " " + t);
    return a == 1 && b == 1 && c == 1 && t == 2;
}

(:test)
function testDetailsVerdiend(logger as Test.Logger) as Boolean {
    // Details op week 1, 1 en 3: met 0 weken geen, met 1 week twee, met 2 weken twee, met 3 of meer alle drie.
    var det = [[1, 0xFFFFFF, 0, 0, 1, 0, 1, 1], [1, 0xFFFFFF, 0, 0, 1, 0, 1, 1], [3, 0xFFFFFF, 0, 0, 1, 0, 1, 1]] as Array<Array<Number> >;
    return EbbWereld.verdiend(det, 0) == 0 && EbbWereld.verdiend(det, 1) == 2 && EbbWereld.verdiend(det, 2) == 2
        && EbbWereld.verdiend(det, 3) == 3 && EbbWereld.verdiend(det, 40) == 3;
}
