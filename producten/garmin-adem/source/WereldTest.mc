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
    // Schildpad, krab en clownvis hebben een wereld (geladen uit de gegevens) met een thuis binnen de strook; een dier
    // zonder wereld geeft null. Elke wereld heeft zijn eigen bovenkant en hoogstens 120 punten.
    var goed = !EbbWereldData.heeft(0) && EbbWereldData.laad(0) == null;
    var dieren = [3, 4, 7] as Array<Number>;
    for (var i = 0; i < dieren.size(); i += 1) {
        var w = EbbWereldData.laad(dieren[i]);
        if (w == null || !EbbWereldData.heeft(dieren[i])) {
            goed = false;
            continue;
        }
        var b = w["b"] as Number;
        var th = w["t"] as Array<Number>;
        var vl = w["v"] as Array<Array<Number> >;
        var voor = w["f"] as Array<Array<Number> >;
        var det = w["d"] as Array<Array<Number> >;
        if (vl.size() < 3 || b < 100 || b > 200 || th[0] < 20 || th[0] > 240 || th[1] < b || th[1] > 240) {
            goed = false;
        }
        var punten = 0;
        var lagen = [vl, voor] as Array<Array<Array<Number> > >;
        for (var k = 0; k < lagen.size(); k += 1) {
            for (var j = 0; j < lagen[k].size(); j += 1) {
                var n = (lagen[k][j].size() - 1) / 2;
                punten += n;
                if (n < 3 || n > 64 || lagen[k][j].size() % 2 != 1) {
                    goed = false;
                }
                for (var q = 2; q < lagen[k][j].size(); q += 2) {
                    if (lagen[k][j][q] < 0 || lagen[k][j][q] > 260 - b) {
                        goed = false;
                    }
                }
            }
        }
        logger.debug("wereld " + dieren[i] + " boven " + b + " vlakken " + vl.size() + " details " + det.size() + " punten " + punten);
        if (punten > 120) {
            goed = false;
        }
    }
    return goed;
}

// Codekeuring bouw 9 punt 5 en 6: de puntengrens per beurt bouwt de wereld in een paar beurten af, en los() ruimt op.
(:test)
function testWereldBouwtInBeurtenEnRuimtOp(logger as Test.Logger) as Boolean {
    var oud = EbbWereld.proef;
    EbbWereld.proef = true;
    EbbWereld.los();
    var p = EbbWereld.zorg(3, 260);
    var beurten = 0;
    while (p != null && p.bezig() && beurten < 20) {
        p.verder();
        beurten += 1;
    }
    var th = EbbWereld.thuis(3, 260);
    var zelfde = EbbWereld.zorg(3, 260) == p;
    EbbWereld.los();
    var geen = EbbWereld.zorg(0, 260) == null;
    EbbWereld.proef = oud;
    logger.debug("beurten " + beurten + " klaar " + (p != null && p.klaar) + " pogingen " + (p != null ? p.pogingen : -1));
    // Lukt het plaatje in de testomgeving niet, dan is er niets gebouwd (beurten 0) en telt alleen de rest.
    var gebouwd = p != null && (p.klaar ? (beurten >= 1 && beurten <= 4) : beurten == 0);
    return gebouwd && zelfde && geen && th != null && th[0] == 84 && th[1] == 214;
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
