import Toybox.Lang;
import Toybox.Test;

(:test)
function testOpslagMaat616(logger as Test.Logger) as Boolean {
    EbbOpslag.wis();
    var o = new EbbOpslag();
    logger.debug("grootte " + o.bytes.size() + " B");
    return o.bytes.size() == 616;
}

(:test)
function testTweedeSessieZelfdeDag(logger as Test.Logger) as Boolean {
    EbbOpslag.wis();
    var o = new EbbOpslag();
    o.voegToe(20400, 60);
    o.voegToe(20400, 90);
    var d = o.dag(20400) as Array<Number>;
    logger.debug("beste " + d[0] + " gemiddeld " + d[1] + " aantal " + d[2]);
    return d[0] == 90 && d[1] == 75 && d[2] == 2;
}

(:test)
function testOverleeftHerstart(logger as Test.Logger) as Boolean {
    EbbOpslag.wis();
    var o = new EbbOpslag();
    o.voegToe(20401, 123);
    o.bewaar();
    var na = new EbbOpslag();
    var d = na.dag(20401);
    EbbOpslag.wis();
    return d != null && (d as Array<Number>)[0] == 123;
}

(:test)
function testOudsteDagValtWeg(logger as Test.Logger) as Boolean {
    EbbOpslag.wis();
    var o = new EbbOpslag();
    o.voegToe(20400, 50);
    o.voegToe(20410, 70);
    var voor = o.dag(20400) != null;
    o.voegToe(20456, 80);   // 56 dagen later, zelfde plek
    var gaten = 0;
    for (var dag = 20401; dag <= 20456; dag += 1) {
        if (o.dag(dag) == null) {
            gaten += 1;
        }
    }
    logger.debug("gaten in 56 dagen: " + gaten);
    return voor && o.dag(20400) == null && (o.dag(20456) as Array<Number>)[0] == 80
        && (o.dag(20410) as Array<Number>)[0] == 70 && gaten == 54;
}
