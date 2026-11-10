import Toybox.Application;
import Toybox.Lang;
import Toybox.Test;

// Eis 7: per ronde een V naar evenredige diepte, lichtpuntje bij de diepste, koraal alleen bij nieuw record.
(:test)
function testDuikprofielV(logger as Test.Logger) as Boolean {
    var p = EbbProfiel.vPunten([60000, 120000, 90000] as Array<Number>, 0, 10, 300, 100);
    logger.debug("punten " + p);
    return p.size() == 7
        && p[1][0] == 50 && p[1][1] == 60
        && p[3][0] == 150 && p[3][1] == 110
        && p[5][0] == 250 && p[5][1] == 85
        && p[6][0] == 300 && p[6][1] == 10
        && EbbProfiel.diepste([60000, 120000, 90000] as Array<Number>) == 1;
}

(:test)
function testKoraalAlleenBijRecord(logger as Test.Logger) as Boolean {
    var t = [70, 95, 80] as Array<Number>;
    return EbbProfiel.nieuwRecord(t, 90) && !EbbProfiel.nieuwRecord(t, 95) && !EbbProfiel.nieuwRecord(t, 120)
        && !EbbProfiel.nieuwRecord([] as Array<Number>, 0);
}

// Getijdenlijn na 8 weken nagebootste gegevens met overgeslagen dagen: 56 dagen, gaten waar geen sessie was.
(:test)
function testGetijdenlijnAchtWeken(logger as Test.Logger) as Boolean {
    EbbOpslag.wis();
    var o = new EbbOpslag();
    var vandaag = 20402;
    var sessies = 0;
    for (var d = vandaag - 70; d <= vandaag; d += 1) {
        if (d % 3 != 0) {
            o.voegToe(d, 60 + (d % 50));
            sessies += 1;
        }
    }
    var lijn = EbbProfiel.getijden(o, vandaag);
    var gaten = 0;
    var fout = 0;
    for (var i = 0; i < lijn.size(); i += 1) {
        var d = vandaag - 55 + i;
        var g = lijn[i];
        if (g == null) {
            gaten += 1;
            if (d % 3 != 0) { fout += 1; }
        } else if (d % 3 == 0 || g[0] != 60 + (d % 50)) {
            fout += 1;
        }
    }
    logger.debug("dagen " + lijn.size() + ", gaten " + gaten + ", fout " + fout);
    EbbOpslag.wis();
    return lijn.size() == 56 && gaten == 18 && fout == 0;
}

// Scherm 5: punten van de getijdenlijn. Hoogste beste is de volle hoogte, gemiddelde eronder, gaten blijven gaten.
(:test)
function testGetijPunten(logger as Test.Logger) as Boolean {
    var lijn = [[60, 40], null, [120, 90], [90, 90], null] as Array<Array<Number> or Null>;
    var p = EbbProfiel.getijPunten(lijn, 10, 200, 400, 100);
    logger.debug("punten " + p);
    var a = p[0] as Array<Number>;
    var c = p[2] as Array<Number>;
    var e = p[3] as Array<Number>;
    var leeg = EbbProfiel.getijPunten([null, null] as Array<Array<Number> or Null>, 0, 100, 50, 50);
    return p.size() == 5 && p[1] == null && p[4] == null
        && a[0] == 10 && a[1] == 150 && a[2] == 167
        && c[0] == 210 && c[1] == 100 && c[2] == 125
        && e[0] == 310 && e[1] == 125 && e[2] == 125
        && leeg[0] == null && leeg[1] == null
        && EbbProfiel.hoogsteDag(lijn) == 2
        && EbbProfiel.hoogsteDag([[50, 50], [50, 40]] as Array<Array<Number> or Null>) == 1
        && EbbProfiel.hoogsteDag([null] as Array<Array<Number> or Null>) == -1;
}

// Eis 8: met nagebootste klok het juiste dier bij 1:00, 1:30, 2:00 en 3:00; een eerste keer wordt één keer bewaard.
(:test)
function testDierenOpTijd(logger as Test.Logger) as Boolean {
    return EbbProfiel.dier(59999) == -1 && EbbProfiel.dier(60000) == 0 && EbbProfiel.dier(67999) == 0
        && EbbProfiel.dier(68000) == -1 && EbbProfiel.dier(90000) == 1 && EbbProfiel.dier(120500) == 2
        && EbbProfiel.dier(150000) == -1 && EbbProfiel.dier(180000) == 3 && EbbProfiel.dier(200000) == -1
        && EbbProfiel.gehaald(200000) == 3 && EbbProfiel.gehaald(30000) == -1;
}

(:test)
function testDierEenKeerBewaard(logger as Test.Logger) as Boolean {
    Application.Storage.deleteValue("dieren");
    var eerste = EbbProfiel.eersteKeer(2);
    var tweede = EbbProfiel.eersteKeer(2);
    var bits = EbbProfiel.dierenGezien();
    var ander = EbbProfiel.eersteKeer(0);
    var bits2 = EbbProfiel.dierenGezien();
    Application.Storage.deleteValue("dieren");
    logger.debug("bits " + bits + " daarna " + bits2);
    return eerste && !tweede && bits == 4 && ander && bits2 == 5;
}

// Eis 2: na bevestigen nooit meer, behalve na "opnieuw tonen".
(:test)
function testVeiligheidsschermEenKeer(logger as Test.Logger) as Boolean {
    EbbVeilig.opnieuwTonen();
    var begin = EbbVeilig.moetTonen();
    EbbVeilig.bevestig();
    var na = EbbVeilig.moetTonen();
    var nogmaals = EbbVeilig.moetTonen();
    EbbVeilig.opnieuwTonen();
    var weer = EbbVeilig.moetTonen();
    EbbVeilig.opnieuwTonen();
    return begin && !na && !nogmaals && weer;
}

// Besluit 22:53 punt 6: 8 weeks toont gemiddelde en hoe vaak, niet alleen het record.
(:test)
function testWekenGemiddeldeEnDagen(logger as Test.Logger) as Boolean {
    EbbOpslag.wis();
    var o = new EbbOpslag();
    var vandaag = 20402;
    // Deze week: drie dagen, elk twee inhoudingen van 60 en 90 s (gemiddeld 75).
    for (var d = vandaag - 2; d <= vandaag; d += 1) {
        o.voegToe(d, 60);
        o.voegToe(d, 90);
    }
    // Vorige week: één dag met één inhouding van 100 s. Week 3 terug leeg. Te oud (9 weken) telt niet mee.
    o.voegToe(vandaag - 7, 100);
    o.voegToe(vandaag - 63, 200);
    var w = EbbProfiel.weken(o, vandaag);
    logger.debug("weken " + w);
    EbbOpslag.wis();
    return w.size() == 8
        && w[7][0] == 75 && w[7][1] == 3 && w[7][2] == 6
        && w[6][0] == 100 && w[6][1] == 1 && w[6][2] == 1
        && w[5][0] == 0 && w[5][1] == 0 && w[0][2] == 0;
}
