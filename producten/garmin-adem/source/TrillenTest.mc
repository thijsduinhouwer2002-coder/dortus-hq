import Toybox.Lang;
import Toybox.Test;

(:test)
function testTrilpatronenAllemaalAnders(logger as Test.Logger) as Boolean {
    var namen = ["in", "uit", "inhouden", "herstel", "los", "vast", "klaar"] as Array<String>;
    var gezien = {} as Dictionary<String, String>;
    for (var m = 0; m < 7; m += 1) {
        var k = EbbTrillen.sleutel(m as EbbTrillen.Moment);
        logger.debug(namen[m] + " -> " + k);
        if (gezien.hasKey(k)) {
            logger.debug("zelfde patroon als " + gezien[k]);
            return false;
        }
        gezien.put(k, namen[m]);
    }
    return true;
}

(:test)
function testTrillenUit(logger as Test.Logger) as Boolean {
    EbbTrillen.aan = false;
    var uit = EbbTrillen.tril(EbbTrillen.M_IN);
    EbbTrillen.aan = true;
    return uit == false;
}
