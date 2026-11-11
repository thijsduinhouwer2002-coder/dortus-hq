import Toybox.Lang;
import Toybox.Test;

// Today (blad v6): de hele dag, hoogstens 3 sessies, nieuwe dag leeg, gemiddelde over alle holds (624 s / 6 = 104 = 1:44).
(:test)
function testVandaag(logger as Test.Logger) as Boolean {
    EbbVandaag.wis();
    var leeg = EbbVandaag.lees(500).size() == 0;
    EbbVandaag.bewaar(500, 460, [70, 85, 100] as Array<Number>);
    EbbVandaag.bewaar(500, 1275, [80, 105, 184] as Array<Number>);
    var twee = EbbVandaag.lees(500);
    var s = EbbVandaag.samen(twee);
    var klok = EbbVandaag.klokTekst(460).equals("7:40") && EbbVandaag.klokTekst(1275).equals("21:15");
    EbbVandaag.bewaar(500, 1300, [60] as Array<Number>);
    EbbVandaag.bewaar(500, 1310, [61] as Array<Number>);
    var drie = EbbVandaag.lees(500);
    var andere = EbbVandaag.lees(501).size() == 0;
    EbbVandaag.bewaar(501, 400, [90] as Array<Number>);
    var nieuw = EbbVandaag.lees(501).size() == 1 && EbbVandaag.lees(500).size() == 0;
    logger.debug("samen " + s + " drie " + drie);
    EbbVandaag.wis();
    return leeg && twee.size() == 2 && s[0] == 6 && s[1] == 104 && klok && drie.size() == 3
        && (drie[0][0] as Number) == 1275 && (drie[2][0] as Number) == 1310 && andere && nieuw;
}

// Keuring bouw 3 punt 11: Calm onder 1 minuut toont seconden, daarboven afgeronde minuten.
(:test)
function testCalmDuurTekst(logger as Test.Logger) as Boolean {
    var a = EbbStart.duurTekst(45000);
    var b = EbbStart.duurTekst(59999);
    var c = EbbStart.duurTekst(240000);
    var e = EbbStart.duurTekst(89000);
    logger.debug(a + " / " + b + " / " + c + " / " + e);
    return a.equals("45 s") && b.equals("59 s") && c.equals("4 min") && e.equals("1 min");
}
