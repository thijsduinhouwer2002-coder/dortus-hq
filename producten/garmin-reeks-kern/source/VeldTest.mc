import Toybox.Lang;
import Toybox.Test;

// Toetsen voor de zes soorten velden van run 133 en voor het kiezen van de velden (Veld.mc, Keuze.mc).
function tekstIs(t as String?, verwacht as String?) as Boolean {
    if (t == null || verwacht == null) {
        return t == null && verwacht == null;
    }
    return t.equals(verwacht);
}

// Afstand: het horloge geeft centimeters, de plaat toont kilometers of mijlen, afgekapt op een tiende.
(:test)
function testVeldAfstand(logger as Test.Logger) as Boolean {
    return Veld.afstandTienden(null, false) == null && Veld.afstandTienden(-1, false) == null
        && Veld.afstandTienden(0, false) == 0 && Veld.afstandTienden(419999, false) == 41
        && Veld.afstandTienden(1250000, false) == 125 && Veld.afstandTienden(160934, true) == 10
        && Veld.afstandTienden(160900, true) == 9 && Veld.afstandTienden(4219500, true) == 262
        && Veld.afstandTienden(200000000, true) == 12427
        && tekstIs(Veld.afstandTekst(0), "0.0") && tekstIs(Veld.afstandTekst(41), "4.1")
        && tekstIs(Veld.afstandTekst(999), "99.9") && tekstIs(Veld.afstandTekst(1000), "100")
        && tekstIs(Veld.afstandTekst(9999), "999") && tekstIs(Veld.afstandTekst(20000), "999")
        && tekstIs(Veld.afstandTekst(null), null) && tekstIs(Veld.afstandTekst(-5), null);
}

// Temperatuur: Celsius of Fahrenheit op hele graden; onder nul het getal zonder teken, het minteken tekent de plaat.
(:test)
function testVeldTemperatuur(logger as Test.Logger) as Boolean {
    return Veld.graden(null, false) == null && Veld.graden(null, true) == null && Veld.graden(21, false) == 21
        && Veld.graden(0, true) == 32 && Veld.graden(-40, true) == -40 && Veld.graden(21, true) == 70
        && Veld.graden(-18, true) == 0 && Veld.graden(-3, false) == -3
        && Veld.graden(21.7, false) == 22 && Veld.graden(-0.4, false) == 0 && Veld.graden(21.4, true) == 71
        && tekstIs(Veld.tekstVan(Veld.TEMP, -3), "3") && Veld.isMin(Veld.TEMP, -3)
        && tekstIs(Veld.tekstVan(Veld.TEMP, 0), "0") && !Veld.isMin(Veld.TEMP, 0) && !Veld.isMin(Veld.TEMP, null)
        && !Veld.isMin(Veld.STAPPEN, -3) && tekstIs(Veld.tekstVan(Veld.TEMP, null), null)
        && tekstIs(Veld.tekstVan(Veld.STAPPEN, -3), null) && tekstIs(Veld.tekstVan(Veld.AFSTAND, 41), "4.1")
        && tekstIs(Veld.tekstVan(Veld.CALORIE, 2140), "2.1K");
}

// Accu: hele procenten naar beneden, en niets buiten 0 tot 100.
(:test)
function testVeldAccu(logger as Test.Logger) as Boolean {
    return Veld.accu(null) == null && Veld.accu(-1.0) == null && Veld.accu(100.5) == null && Veld.accu(0.0) == 0
        && Veld.accu(99.9) == 99 && Veld.accu(100.0) == 100 && Veld.accu(54.2) == 54;
}

// De zes nieuwe soorten lezen stopt de plaat nooit: elk geeft een getal of null, en een soort die niet bestaat null.
(:test)
function testVeldLeesAlleSoorten(logger as Test.Logger) as Boolean {
    var leeg = [] as Array<Number>;
    for (var s = Veld.CALORIE; s < Veld.AANTAL; s++) {
        var v = Veld.waarde(s, leeg);
        logger.debug("soort " + s + " geeft " + ((v == null) ? "niets" : v.format("%d")));
        if (v != null && !(v instanceof Lang.Number)) {
            return false;
        }
    }
    var a = Veld.waarde(Veld.ACCU, leeg);
    if (a != null && (a < 0 || a > 100)) {
        return false;
    }
    return Veld.AANTAL == 9 && Veld.lees(99) == null && Veld.lees(Veld.HART) == null && Veld.waarde(-1, leeg) == null;
}

// Velden kiezen: wat de telefoon ook stuurt, er komt een bestaande soort uit; niets of onzin wordt de standaard.
(:test)
function testKeuzeVeld(logger as Test.Logger) as Boolean {
    return Keuze.veld(null, Veld.STRESS) == Veld.STRESS && Keuze.veld(0, Veld.STAPPEN) == Veld.HART
        && Keuze.veld(8, Veld.HART) == Veld.TEMP && Keuze.veld(9, Veld.HART) == Veld.HART
        && Keuze.veld(-1, Veld.STAPPEN) == Veld.STAPPEN && Keuze.veld("7", Veld.HART) == Veld.ACCU
        && Keuze.veld("accu", Veld.STRESS) == Veld.STRESS && Keuze.veld(6.0, Veld.HART) == Veld.AFSTAND
        && Keuze.veld(true, Veld.STAPPEN) == Veld.STAPPEN && Veld.geldig(3, 0) == Veld.CALORIE
        && Veld.geldig(12, 2) == Veld.STAPPEN;
}

// Run 134: elk van de zes nieuwe soorten heeft een pictogram van Mila; het aantal vlakken per soort klopt met
// haar bestand, elk vlak heeft minstens drie punten en hoogstens 64 (grens van fillPolygon), en alles blijft
// binnen de hoogte (y van -50 tot 50) en in de breedte binnen -62 tot 60 (de accu is het breedst).
(:test)
function testIcoonVlakkenPerSoort(logger as Test.Logger) as Boolean {
    var aantal = [1, 1, 4, 3, 6, 2] as Array<Number>;
    for (var s = Veld.CALORIE; s < Veld.AANTAL; s++) {
        var v = Teken.vlakken(s);
        if (v.size() != aantal[s - Veld.CALORIE]) {
            logger.debug("soort " + s + " vlakken=" + v.size());
            return false;
        }
        for (var i = 0; i < v.size(); i++) {
            var rij = v[i];
            if (rij.size() < 6 || rij.size() % 2 != 0 || rij.size() > 128) {
                logger.debug("soort " + s + " vlak " + i + " punten=" + rij.size());
                return false;
            }
            for (var j = 0; j < rij.size(); j += 2) {
                if (rij[j] < -62 || rij[j] > 60 || rij[j + 1] < -50 || rij[j + 1] > 50) {
                    logger.debug("soort " + s + " vlak " + i + " buiten de maat");
                    return false;
                }
            }
        }
    }
    return true;
}

// De drie oude soorten en een onbekende soort hebben geen vlakken in deze lijst: lege lijst, geen fout.
(:test)
function testIcoonVlakkenOnbekend(logger as Test.Logger) as Boolean {
    return Teken.vlakken(Veld.HART).size() == 0 && Teken.vlakken(Veld.STAPPEN).size() == 0
        && Teken.vlakken(-1).size() == 0 && Teken.vlakken(99).size() == 0;
}

// De vlam op 12 px hoog rond (100, 50): de punt staat boven (y 44), rechts van het midden, en de voet onder het midden.
(:test)
function testIcoonVlamOpMaat(logger as Test.Logger) as Boolean {
    var p = Teken.vlak(Teken.vlakken(Veld.CALORIE)[0], 100, 50, 12);
    logger.debug("vlam: " + p);
    return p.size() == 12 && p[0][0] == 101 && p[0][1] == 44 && p[5][1] == 56;
}

// Het minteken (Mila): 40% van de cijferhoogte lang, minstens 2 px dik, gat van 10% en minstens 1 px.
(:test)
function testMinteken(logger as Test.Logger) as Boolean {
    var groot = Veld.minMaten(30, 3);
    var klein = Veld.minMaten(9, 1);
    // Heel klein of nul (punt van de keurder): de ondergrenzen 3, 2 en 1 gelden.
    var mini = Veld.minMaten(5, 0);
    var nul = Veld.minMaten(0, 0);
    return groot[0] == 12 && groot[1] == 3 && groot[2] == 3 && klein[0] == 3 && klein[1] == 2 && klein[2] == 1
        && mini[0] == 3 && mini[1] == 2 && mini[2] == 1 && nul[0] == 3 && nul[1] == 2 && nul[2] == 1;
}

// De toetsen bouwen als de winkel: daar telt de keuze van de drager, niet de velden van de proef.
(:test)
function testWinkelGekozenVelden(logger as Test.Logger) as Boolean {
    var v = Proef.velden([Veld.TEMP, Veld.HART, Veld.ACCU] as Array<Number>, 454);
    return v.size() == 3 && v[0] == Veld.TEMP && v[1] == Veld.HART && v[2] == Veld.ACCU;
}

// De toetsen bouwen als de winkel: daar telt wat het horloge geeft, nooit een proefwaarde, ook niet bij niets.
(:test)
function testWinkelEchteVelden(logger as Test.Logger) as Boolean {
    return Proef.veld(Veld.CALORIE, 7) == 7 && Proef.veld(Veld.TEMP, 21) == 21 && Proef.veld(Veld.AFSTAND, null) == null
        && Proef.veld(Veld.TRAPPEN, 0) == 0;
}

// Run 135 (moet van Daan): de kleine accu is een open rand met een nopje rechts en een vulling van links. Van 9
// tot 13 px hoog: zes rechthoeken, het open deel rechts van de vulling minstens 2 px breed en 2 px hoog, de
// vulling begint tegen de linkerrand, het nopje zit rechts buiten de rand en alles blijft binnen de hoogte.
(:test)
function testAccuKleinOpen(logger as Test.Logger) as Boolean {
    for (var h = 9; h < Teken.KLEIN; h++) {
        var d = Teken.accuKlein(100, 50, h);
        if (d.size() != 6) {
            return false;
        }
        var links = d[2];
        var rechts = d[3];
        var nop = d[4];
        var vul = d[5];
        var open = rechts[0] - (vul[0] + vul[2]);
        if (d[0][3] != 1 || d[1][3] != 1 || links[2] != 1 || rechts[2] != 1 || d[0][2] != d[1][2] || open < 2 || vul[3] < 2 || vul[2] < 2 || vul[0] != links[0] + 1 || nop[0] != rechts[0] + 1
            || d[0][1] < 50 - h / 2 || d[1][1] + 1 > 50 - h / 2 + h || nop[1] <= d[0][1] || nop[1] + nop[3] >= d[1][1] + 1) {
            logger.debug("accu h=" + h + " open=" + open + " vul=" + vul[2] + "x" + vul[3]);
            return false;
        }
    }
    return true;
}

// Run 135 (moet van Daan): de bol van de kleine thermometer is aan elke kant minstens 2 px breder dan de steel,
// de steel loopt van de bovenkant tot in de bol en alles blijft binnen de hoogte.
(:test)
function testThermoKleinBol(logger as Test.Logger) as Boolean {
    for (var h = 9; h < Teken.KLEIN; h++) {
        var t = Teken.thermoKlein(100, 50, h);
        var top = 50 - h / 2;
        var linksMeer = t[0] - (t[4] - t[6]);
        var rechtsMeer = (t[4] + t[6]) - (t[0] + t[2] - 1);
        if (linksMeer < 2 || rechtsMeer < 2 || t[1] != top || t[1] + t[3] < t[5] - t[6] || t[5] + t[6] > top + h - 1 || t[3] < 3) {
            logger.debug("thermo h=" + h + " links=" + linksMeer + " rechts=" + rechtsMeer);
            return false;
        }
    }
    return true;
}
