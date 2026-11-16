import Toybox.Lang;
import Toybox.Test;

// Laat de tijd lopen in stappen van 50 ms, zoals het scherm dat doet.
function laatLopen(spel as Spel, ms as Number) as Void {
    var t = 0;
    while (t < ms) {
        spel.tik(50);
        t += 50;
    }
}

function totInZone(spel as Spel) as Void {
    var n = 0;
    while (!(spel.toestand == Regel.VALT && spel.y >= Regel.RAAK_BOVEN) && n < 400) {
        spel.tik(50);
        n += 1;
    }
}

(:test)
function testBegintKlaarEnDrukStart(logger as Test.Logger) as Boolean {
    var s = new Spel(7);
    var klaar = (s.toestand == Regel.KLAAR);
    s.druk();
    return klaar && s.toestand == Regel.VALT && s.hoeden == 0 && s.tijdOver == Regel.RONDE_MS;
}

(:test)
function testDrukInZoneGeeftHoed(logger as Test.Logger) as Boolean {
    var s = new Spel(7);
    s.druk();
    totInZone(s);
    s.druk();
    logger.debug("y bij druk: " + s.y + ", hoeden: " + s.hoeden);
    return s.hoeden == 1 && s.toestand == Regel.SLOK && s.raak && s.reeks == 1;
}

(:test)
function testTeVroegGeeftGeenHoedEnBekEvenDicht(logger as Test.Logger) as Boolean {
    var s = new Spel(7);
    s.druk();
    laatLopen(s, 200);
    s.druk();
    return s.hoeden == 0 && s.toestand == Regel.VALT && s.hapDicht == Regel.DICHT_MS;
}

(:test)
function testMissenStraftNiet(logger as Test.Logger) as Boolean {
    var s = new Spel(7);
    s.druk();
    totInZone(s);
    s.druk();
    laatLopen(s, 1000);
    var hoedenVoor = s.hoeden;
    var snelVoor = s.snelheid;
    // Niet drukken: de held loopt weg.
    laatLopen(s, 4000);
    logger.debug("snelheid voor " + snelVoor + ", na " + s.snelheid);
    return s.hoeden == hoedenVoor && s.snelheid < snelVoor && s.toestand != Regel.EINDE;
}

(:test)
function testRondeEindigtNaDertigSecondenMetNieuwBeste(logger as Test.Logger) as Boolean {
    var s = new Spel(7);
    s.druk();
    totInZone(s);
    s.druk();
    // Precies tot het einde lopen, niet verder: de wachttijd van 0,8 s telt vanaf het eindscherm.
    var n = 0;
    while (s.toestand != Regel.EINDE && n < 700) {
        s.tik(50);
        n += 1;
    }
    logger.debug("einde na tikken: " + n);
    var einde = (s.toestand == Regel.EINDE && s.tijdOver == 0 && n > 500 && n < 600);
    var beste = s.beste;
    // Direct drukken doet nog niets (bescherming tegen per ongeluk), na 0,8 s wel.
    s.druk();
    var nogEinde = (s.toestand == Regel.EINDE);
    laatLopen(s, 900);
    s.druk();
    return einde && beste == 1 && s.nieuwBeste == false && nogEinde && s.toestand == Regel.VALT && s.beste == 1;
}

(:test)
function testEenGoedeSpelerHaaltTorenBovenHetScherm(logger as Test.Logger) as Boolean {
    // Een speler die elke held raakt: hoeveel hoeden in één ronde? De toren past
    // tot 13 hoeden op het scherm; een goed potje moet daar overheen gaan.
    var s = new Spel(99);
    s.druk();
    var eersteHoedMs = -1;
    var t = 0;
    while (s.toestand != Regel.EINDE && t < 40000) {
        if (s.toestand == Regel.VALT && s.y >= Regel.RAAK_BOVEN) {
            s.druk();
            if (eersteHoedMs < 0) {
                eersteHoedMs = t;
            }
        }
        s.tik(50);
        t += 50;
    }
    logger.debug("hoeden in 30 s: " + s.hoeden + ", eerste hoed na ms: " + eersteHoedMs + ", snelheid: " + s.snelheid);
    return s.hoeden >= 15 && eersteHoedMs < 2500;
}
