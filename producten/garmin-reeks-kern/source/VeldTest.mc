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
        logger.debug("soort " + s + " geeft " + v);
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
