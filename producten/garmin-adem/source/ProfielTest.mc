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

// Besluit 22:53: het dier tijdens het inhouden hangt niet af van de inhoudtijd; het zwemt in een vaste cyclus van 20 s.
(:test)
function testZwemZonderBeloning(logger as Test.Logger) as Boolean {
    return EbbProfiel.zwem(0) == 0.0 && EbbProfiel.zwem(8000) == 0.5 && EbbProfiel.zwem(16000) == -1.0
        && EbbProfiel.zwem(20000) == 0.0 && EbbProfiel.zwem(188000) == 0.5;
}

// Dieren voor trouw: 24 stuks, elk één keer, nieuwe alleen bij het afsluiten van een sessie, beste reeks telt.
(:test)
function testDierenVoorTrouw(logger as Test.Logger) as Boolean {
    EbbTrouw.wis();
    var lijst = EbbTrouw.DIEREN.size() == 24;
    var geen = EbbTrouw.aantal() == 0 && EbbTrouw.gezelschap() == 0;
    var eerste = EbbTrouw.nieuweDieren(EbbTrouw.naSessie(100));        // 1 sessie: vis
    var tweede = EbbTrouw.nieuweDieren(EbbTrouw.naSessie(101));        // 2 sessies, 2 dagen: garnaal en kwal
    var zelfde = EbbTrouw.nieuweDieren(EbbTrouw.naSessie(101));        // 3 sessies, zelfde dag: niets
    var derde = EbbTrouw.nieuweDieren(EbbTrouw.naSessie(102));         // 3 dagen op rij: schildpad
    var na = EbbTrouw.aantal() == 4 && EbbTrouw.gezelschap() == 2;    // schildpad zwemt mee
    // Na een gat blijft wat je hebt; alles bij 60 sessies en 30 dagen op rij.
    EbbTrouw.naSessie(110);
    var alles = EbbTrouw.verdiend(60, 30) == (1 << 24) - 1 && EbbTrouw.verdiend(59, 30) != (1 << 24) - 1;
    var tekst = EbbTrouw.hoe(3).equals("3-day streak") && EbbTrouw.hoe(23).equals("60 sessions") && EbbTrouw.hoe(0).equals("1 session");
    logger.debug("eerste " + eerste + " tweede " + tweede + " zelfde " + zelfde + " derde " + derde);
    var gehouden = EbbTrouw.aantal() == 4;
    EbbTrouw.wis();
    return lijst && geen && eerste.size() == 1 && eerste[0] == 0 && tweede.size() == 2 && tweede[0] == 1 && tweede[1] == 2
        && zelfde.size() == 0 && derde.size() == 1 && derde[0] == 3 && na && alles && tekst && gehouden;
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
    // Vorige week: één dag met één inhouding van 100 s. Week 3 terug leeg. Oudste dag van week 1 telt mee.
    // (Niet ouder dan 56 dagen proberen: die plek in de ring is van een nieuwere dag.)
    o.voegToe(vandaag - 7, 100);
    o.voegToe(vandaag - 55, 200);
    var w = EbbProfiel.weken(o, vandaag);
    logger.debug("weken " + w);
    EbbOpslag.wis();
    return w.size() == 8
        && w[7][0] == 75 && w[7][1] == 3 && w[7][2] == 6
        && w[6][0] == 100 && w[6][1] == 1 && w[6][2] == 1
        && w[5][0] == 0 && w[5][1] == 0 && w[0][0] == 200 && w[0][2] == 1;
}

// Productkeuring: veiligheidsscherm bij de eerste start en daarna elke 30 dagen opnieuw.
(:test)
function testVeiligElkeDertigDagen(logger as Test.Logger) as Boolean {
    EbbVeilig.opnieuwTonen();
    var eerste = EbbVeilig.moetTonenOp(20400);
    EbbVeilig.bevestigOp(20400);
    var dag29 = EbbVeilig.moetTonenOp(20429);
    var dag30 = EbbVeilig.moetTonenOp(20430);
    var klokTerug = EbbVeilig.moetTonenOp(20390);
    Application.Storage.setValue(EbbVeilig.SLEUTEL, true);
    var oudeWaarde = EbbVeilig.moetTonenOp(20400);
    EbbVeilig.opnieuwTonen();
    return eerste && !dag29 && dag30 && klokTerug && oudeWaarde;
}

// Trouw: sessies tellen, dagen op rij, beste reeks blijft staan na een gat.
(:test)
function testTrouwTellers(logger as Test.Logger) as Boolean {
    EbbTrouw.wis();
    EbbTrouw.naSessie(100);
    EbbTrouw.naSessie(100);          // zelfde dag: reeks blijft 1
    EbbTrouw.naSessie(101);
    var t = EbbTrouw.naSessie(102);  // drie dagen op rij
    var drie = t[0] == 4 && t[1] == 3 && t[2] == 3;
    var vandaagNog = EbbTrouw.reeksOp(103) == 3;
    var voorbij = EbbTrouw.reeksOp(104) == 0;
    var g = EbbTrouw.naSessie(105);  // gat: opnieuw 1, beste blijft 3
    var gat = g[0] == 5 && g[1] == 1 && g[2] == 3;
    var terug = EbbTrouw.volgendeReeks(200, 4, 190) == 1;
    logger.debug("na drie " + t + ", na gat " + g);
    EbbTrouw.wis();
    return drie && vandaagNog && voorbij && gat && terug;
}
