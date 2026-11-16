import Toybox.Lang;
import Toybox.Test;

(:test)
function testHoedPerDuizendStappen(logger as Test.Logger) as Boolean {
    return Regel.hoeden(0) == 0 && Regel.hoeden(999) == 0 && Regel.hoeden(1000) == 1
        && Regel.hoeden(3420) == 3 && Regel.hoeden(10230) == 10 && Regel.hoeden(-5) == 0;
}

(:test)
function testTorenHoudtOpBijMaximum(logger as Test.Logger) as Boolean {
    return Regel.hoeden(14000) == 14 && Regel.hoeden(60000) == 60 && Regel.hoeden(990000) == 60;
}

(:test)
function testKroonBijDoel(logger as Test.Logger) as Boolean {
    return !Regel.kroon(9999, 10000) && Regel.kroon(10000, 10000) && Regel.kroon(7600, 7500)
        && !Regel.kroon(5000, 0);
}

(:test)
function testHoedenBijDoel(logger as Test.Logger) as Boolean {
    return Regel.hoedenBijDoel(10000) == 10 && Regel.hoedenBijDoel(7500) == 8
        && Regel.hoedenBijDoel(0) == 10 && Regel.hoedenBijDoel(30000) == 30 && Regel.hoedenBijDoel(900000) == 60;
}

(:test)
function testUurTwaalfEnVierentwintig(logger as Test.Logger) as Boolean {
    return Regel.uur(0, false) == 12 && Regel.uur(13, false) == 1 && Regel.uur(12, false) == 12
        && Regel.uur(0, true) == 0 && Regel.uur(23, true) == 23;
}

(:test)
function testStapKroonPastBijDoel(logger as Test.Logger) as Boolean {
    // Ruimte genoeg: de gewone stap. Te weinig: de toren van het doel is precies `ruimte` hoog.
    var f = Regel.stap(340, 131);
    var hoogte = (340 * f + 0.5).toNumber();
    return Regel.stap(100, 131) == 0.56 && Regel.stap(0, 50) == 0.56 && hoogte == 131
        && Regel.stap(3000, 100) == 0.18;
}

(:test)
function testBuigingNaarRechts(logger as Test.Logger) as Boolean {
    return Regel.buiging(0, 10, 8) == 0 && Regel.buiging(5, 10, 8) == 2 && Regel.buiging(10, 10, 8) == 8
        && Regel.buiging(14, 10, 8) == 15 && Regel.buiging(3, 0, 8) == 0;
}

(:test)
function testRandVolgtDeCirkel(logger as Test.Logger) as Boolean {
    // Rond 260: in het midden mag tekst bij de marge beginnen, onderaan pas verder naar binnen.
    var midden = Regel.randLinks(120, 140, 260, 260, true, 4);
    var onder = Regel.randLinks(215, 233, 260, 260, true, 4);
    return midden == 5 && onder > 50 && onder < 60 && Regel.randLinks(215, 233, 320, 360, false, 4) == 4
        && Regel.randBoven(130, 260, 260, true, 2) == 2 && Regel.randBoven(208, 260, 260, true, 2) > 20
        && Regel.randBoven(300, 320, 360, false, 2) == 2;
}

(:test)
function testHoedWachtTotJeKijkt(logger as Test.Logger) as Boolean {
    return Regel.wachtend(7, 6) == 6 && Regel.wachtend(7, 7) == 7 && Regel.wachtend(0, 9) == 0
        && Regel.wachtend(5, -1) == 5 && Regel.wachtend(11, 8) == 8;
}

(:test)
function testAantalMetKroon(logger as Test.Logger) as Boolean {
    return Regel.aantal(3420, 10000) == 3 && Regel.aantal(10000, 10000) == 10 && Regel.aantal(14800, 10000) == 14
        && Regel.aantal(600, 500) == 1 && Regel.aantal(0, 10000) == 0;
}

(:test)
function testRegelOnderDeStappen(logger as Test.Logger) as Boolean {
    return Regel.regel(7612, 10000).equals("7/10 HATS") && Regel.regel(10000, 10000).equals("GOAL!")
        && Regel.regel(10999, 10000).equals("GOAL!") && Regel.regel(14800, 10000).equals("GOAL! +4")
        && Regel.regel(7600, 7500).equals("GOAL!");
}

(:test)
function testPuntBijDuizend(logger as Test.Logger) as Boolean {
    return Regel.punt(0).equals("0") && Regel.punt(999).equals("999") && Regel.punt(7612).equals("7.612")
        && Regel.punt(10005).equals("10.005") && Regel.punt(14800).equals("14.800");
}

(:test)
function testKorteRegel(logger as Test.Logger) as Boolean {
    return Regel.kort("7/10 HATS").equals("7/10") && Regel.kort("GOAL! +4").equals("GOAL+4")
        && Regel.kort("GOAL! +12").equals("GOAL+12") && Regel.kort("GOAL!").equals("GOAL!");
}
