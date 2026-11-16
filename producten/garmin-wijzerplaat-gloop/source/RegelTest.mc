import Toybox.Lang;
import Toybox.Test;

(:test)
function testHoedPerDuizendStappen(logger as Test.Logger) as Boolean {
    return Regel.hoeden(0) == 0 && Regel.hoeden(999) == 0 && Regel.hoeden(1000) == 1
        && Regel.hoeden(3420) == 3 && Regel.hoeden(10230) == 10 && Regel.hoeden(-5) == 0;
}

(:test)
function testTorenHoudtOpBijMaximum(logger as Test.Logger) as Boolean {
    return Regel.hoeden(14000) == 14 && Regel.hoeden(60000) == 14;
}

(:test)
function testKroonBijDoel(logger as Test.Logger) as Boolean {
    return !Regel.kroon(9999, 10000) && Regel.kroon(10000, 10000) && Regel.kroon(7600, 7500)
        && !Regel.kroon(5000, 0);
}

(:test)
function testHoedenBijDoel(logger as Test.Logger) as Boolean {
    return Regel.hoedenBijDoel(10000) == 10 && Regel.hoedenBijDoel(7500) == 8
        && Regel.hoedenBijDoel(0) == 10 && Regel.hoedenBijDoel(30000) == 14;
}

(:test)
function testUurTwaalfEnVierentwintig(logger as Test.Logger) as Boolean {
    return Regel.uur(0, false) == 12 && Regel.uur(13, false) == 1 && Regel.uur(12, false) == 12
        && Regel.uur(0, true) == 0 && Regel.uur(23, true) == 23;
}
