import Toybox.Lang;
import Toybox.Test;

// Toetsen voor eis 3 (rondes) en eis 5 (rustig ademen) uit producten/garmin-adem/ontwerp.md.
// De klok wordt nagebootst met onregelmatige stappen (zoals een echte timer die soms later komt).

// Stapgrootte die wisselt tussen 37 en 151 ms.
function stapMs(i as Number) as Number {
    return 37 + (i * 53) % 115;
}

(:test)
function testRondeDuur30x16(logger as Test.Logger) as Boolean {
    var s = new Ebb.Rondes(30, 1600, 3, 15000, 1000);
    var nu = 1000;
    var i = 0;
    while (s.fase == Ebb.FASE_ADEMEN) {
        nu += stapMs(i);
        i += 1;
        s.bijwerken(nu);
    }
    var ademen = s.segmentStart - 1000;
    logger.debug("ademen duurde " + ademen + " ms (verwacht 96000)");
    // inhouden 30 s, dan herstel
    s.stopInhouden(s.segmentStart + 30000);
    var herstelStart = s.segmentStart;
    while (s.fase == Ebb.FASE_HERSTEL) {
        nu = (nu < herstelStart) ? herstelStart : nu;
        nu += stapMs(i);
        i += 1;
        s.bijwerken(nu);
    }
    var herstel = s.segmentStart - herstelStart;
    logger.debug("herstel duurde " + herstel + " ms (verwacht 15000)");
    return (ademen - 96000).abs() <= 500 && (herstel - 15000).abs() <= 500 && s.ronde == 1 && s.fase == Ebb.FASE_ADEMEN;
}

(:test)
function testZesRondesGeenAfwijking(logger as Test.Logger) as Boolean {
    var start = 5000;
    var s = new Ebb.Rondes(60, 1600, 6, 15000, start);
    var nu = start;
    var i = 0;
    var verwacht = start;
    var inhoud = [31000, 45500, 62000, 70250, 80000, 95125] as Array<Number>;
    while (s.fase != Ebb.FASE_KLAAR) {
        nu += stapMs(i);
        i += 1;
        s.bijwerken(nu);
        if (s.fase == Ebb.FASE_INHOUDEN) {
            var r = s.ronde;
            nu = s.segmentStart + inhoud[r];
            s.stopInhouden(nu);
        }
    }
    for (var r = 0; r < 6; r += 1) {
        verwacht += 60 * 2 * 1600 + inhoud[r] + 15000;
    }
    var afwijking = (s.segmentStart - verwacht).abs();
    logger.debug("einde " + s.segmentStart + " verwacht " + verwacht + " afwijking " + afwijking + " ms, stappen " + i);
    return afwijking <= 500 && s.inhoudtijden.size() == 6 && s.inhoudtijden[5] == 95125;
}

(:test)
function testAdemhalingTellen(logger as Test.Logger) as Boolean {
    var s = new Ebb.Rondes(30, 1600, 3, 15000, 0);
    return s.ademhaling(0) == 1 && s.isIn(0) && !s.isIn(1600) && s.ademhaling(3199) == 1
        && s.ademhaling(3200) == 2 && s.ademhaling(95999) == 30;
}

(:test)
function testWaterStijgtEnZakt(logger as Test.Logger) as Boolean {
    var s = new Ebb.Rondes(30, 1600, 3, 15000, 0);
    var leeg = s.water(0);
    var half = s.water(800);
    var vol = s.water(1599);
    var terug = s.water(2400);
    logger.debug("water " + leeg + " " + half + " " + vol + " " + terug);
    return leeg < 0.01 && (half - 0.5).abs() < 0.01 && vol > 0.99 && (terug - 0.5).abs() < 0.01;
}

(:test)
function testStopBuitenInhoudenDoetNiets(logger as Test.Logger) as Boolean {
    var s = new Ebb.Rondes(30, 1600, 3, 15000, 0);
    return s.stopInhouden(500) == -1 && s.fase == Ebb.FASE_ADEMEN && s.inhoudtijden.size() == 0;
}

// Eis 5: elk patroon loopt 3 minuten; elke fasegrens valt precies op de berekende tijd.
function patroonKlopt(patroon as Array<Number>, logger as Test.Logger) as Boolean {
    var start = 777;
    var r = new Ebb.Rustig(patroon, start);
    var nu = start;
    var i = 0;
    var vorige = r.faseIndex(nu);
    var grenzen = 0;
    var slechtste = 0;
    while (nu < start + 180000) {
        var stap = stapMs(i);
        i += 1;
        var oud = nu;
        nu += stap;
        var f = r.faseIndex(nu);
        if (f != vorige) {
            // De grens moet tussen oud en nu liggen en gelijk zijn aan de som van de fases.
            var grens = r.faseStart(nu);
            var verschuiving = (grens - start) % r.cyclus();
            var somFases = 0;
            for (var j = 0; j < f; j += 1) {
                somFases += patroon[j];
            }
            var afw = (verschuiving - somFases).abs();
            if (grens <= oud || grens > nu) {
                afw = 99999;
            }
            if (afw > slechtste) {
                slechtste = afw;
            }
            grenzen += 1;
            vorige = f;
        }
    }
    logger.debug("patroon " + patroon + ": " + grenzen + " grenzen in 3 min, slechtste afwijking " + slechtste + " ms");
    return slechtste <= 500 && grenzen > 10;
}

(:test)
function testRustigVastePatronen(logger as Test.Logger) as Boolean {
    var p = Ebb.patronen();
    return patroonKlopt(p[0], logger) && patroonKlopt(p[1], logger) && patroonKlopt(p[2], logger);
}

(:test)
function testRustigEigenPatroon(logger as Test.Logger) as Boolean {
    return patroonKlopt([3000, 0, 9000, 2000] as Array<Number>, logger);
}

// Pauze zet de klok stil: 60 s pauze tijdens het ademen schuift het einde van het ademen 60 s op.
(:test)
function testPauzeZetKlokStil(logger as Test.Logger) as Boolean {
    var s = new Ebb.Rondes(30, 1600, 3, 15000, 0);
    s.bijwerken(10000);
    var adem = s.ademhaling(10000);
    s.pauzeer(10000);
    s.bijwerken(70000);
    var tijdensPauze = s.ademhaling(69999);
    var stilFase = s.fase;
    s.hervat(70000);
    s.bijwerken(155999);
    var voorGrens = s.fase;
    s.bijwerken(156000);
    logger.debug("ademhaling " + adem + "/" + tijdensPauze + ", fase voor grens " + voorGrens + ", na grens " + s.fase);
    return adem == tijdensPauze && stilFase == Ebb.FASE_ADEMEN && voorGrens == Ebb.FASE_ADEMEN
        && s.fase == Ebb.FASE_INHOUDEN && !s.gepauzeerd();
}

// Dubbel pauzeren of hervatten zonder pauze verandert niets.
(:test)
function testPauzeDubbelVeilig(logger as Test.Logger) as Boolean {
    var s = new Ebb.Rondes(30, 1600, 3, 15000, 0);
    s.hervat(5000);
    var start1 = s.segmentStart;
    s.pauzeer(10000);
    s.pauzeer(20000);
    s.hervat(30000);
    s.hervat(40000);
    return start1 == 0 && s.segmentStart == 20000;
}

// Rustig ademen: pauze zet de klok stil, doorgaan gaat verder in dezelfde fase met dezelfde resttijd.
(:test)
function testRustigPauze(logger as Test.Logger) as Boolean {
    var r = new Ebb.Rustig([4000, 4000, 4000, 4000] as Array<Number>, 0);
    var voor = r.faseIndex(5500);
    var restVoor = r.overS(5500);
    r.pauzeer(5500);
    var stil = r.klok(60000) == 5500;
    r.hervat(65500);
    var na = r.faseIndex(65500);
    var restNa = r.overS(65500);
    var later = r.faseIndex(65500 + 2600);
    logger.debug("fase " + voor + " rest " + restVoor + " na " + na + " rest " + restNa + " later " + later);
    return voor == 1 && restVoor == 3 && stil && na == 1 && restNa == 3 && later == 2
        && new Ebb.Rustig([4000, 4000, 4000, 4000] as Array<Number>, 0).overS(4000) == 4;
}
