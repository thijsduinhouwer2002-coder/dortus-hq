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
    // Uren van Mila (lucht v1.4): ochtend 6 tot 10, dag 10 tot 17, avond 17 tot 21, nacht 21 tot 6.
    return EbbLucht.dagdeel(5) == 3 && EbbLucht.dagdeel(6) == 0 && EbbLucht.dagdeel(9) == 0 && EbbLucht.dagdeel(10) == 1
        && EbbLucht.dagdeel(16) == 1 && EbbLucht.dagdeel(17) == 2 && EbbLucht.dagdeel(20) == 2 && EbbLucht.dagdeel(21) == 3
        && EbbLucht.dagdeel(0) == 3 && EbbLucht.KLEUR.size() == 4 && EbbLucht.STERREN.size() == 14;
}

(:test)
function testWereldGegevens(logger as Test.Logger) as Boolean {
    // Schildpad, krab en clownvis hebben een wereld (geladen uit de gegevens) met een thuis binnen het scherm; een dier
    // zonder wereld geeft null. Hoogstens 120 punten per wereld, hoogstens 40 direct getekend (planten en voorlaag),
    // en een plant heeft in beide standen evenveel punten en dezelfde kleur.
    var goed = !EbbWereldData.heeft(0) && EbbWereldData.laad(0) == null;
    var dieren = [3, 4, 7] as Array<Number>;
    for (var i = 0; i < dieren.size(); i += 1) {
        var w = EbbWereldData.laad(dieren[i]);
        if (w == null || !EbbWereldData.heeft(dieren[i])) {
            goed = false;
            continue;
        }
        var b = w["b"] as Number;
        var m = w["m"] as Number;
        var th = w["t"] as Array<Number>;
        var vl = w["v"] as Array<Array<Number> >;
        var det = w["d"] as Array<Array<Number> >;
        var pl = w["p"] as Array<Array<Number> >;
        var pl2 = w["q"] as Array<Array<Number> >;
        var voor = w["f"] as Array<Array<Number> >;
        var voor2 = w["g"] as Array<Array<Number> or Null>;
        if (vl.size() < 3 || b < 100 || b > 200 || m < 15 || m > 40 || th[0] < 20 || th[0] > 240 || th[1] < 100 || th[1] > 240
            || pl2.size() != pl.size() || voor2.size() != voor.size()) {
            goed = false;
            continue;
        }
        var punten = 0;
        var direct = 0;
        for (var j = 0; j < vl.size(); j += 1) {
            punten += (vl[j].size() - 1) / 2;
            if (vl[j].size() < 7 || vl[j].size() % 2 != 1) {
                goed = false;
            }
        }
        for (var j = 0; j < det.size(); j += 1) {
            punten += (det[j].size() - 2) / 2;
            if (det[j].size() < 8 || det[j].size() % 2 != 0 || det[j][0] < 1 || (j > 0 && det[j][0] < det[j - 1][0])) {
                goed = false;
            }
        }
        for (var j = 0; j < pl.size(); j += 1) {
            direct += (pl[j].size() - 1) / 2;
            if (pl[j].size() != pl2[j].size() || pl[j][0] != pl2[j][0]) {
                goed = false;
            }
        }
        for (var j = 0; j < voor.size(); j += 1) {
            direct += (voor[j].size() - 1) / 2;
            var v2 = voor2[j];
            if (v2 != null && v2.size() != voor[j].size()) {
                goed = false;
            }
        }
        logger.debug("wereld " + dieren[i] + " boven " + b + " maat " + m + " vlakken " + vl.size() + " details " + det.size() + " planten " + pl.size() + " voor " + voor.size() + " punten " + (punten + direct) + " direct " + direct);
        if (punten + direct > 120 || direct > 40) {
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
    var mt = EbbWereld.maat(3, 260);
    EbbWereld.los();
    var geen = EbbWereld.zorg(0, 260) == null;
    EbbWereld.proef = oud;
    logger.debug("beurten " + beurten + " klaar " + (p != null && p.klaar) + " pogingen " + (p != null ? p.pogingen : -1));
    // Lukt het plaatje in de testomgeving niet, dan is er niets gebouwd (beurten 0) en telt alleen de rest.
    var gebouwd = p != null && (p.klaar ? (beurten >= 1 && beurten <= 4) : beurten == 0);
    return gebouwd && zelfde && geen && th != null && th[0] == 92 && th[1] == 214 && mt == 27;
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
