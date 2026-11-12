import Toybox.Lang;
import Toybox.Test;

// Nachtregel: een paar regels uit de tabel van Mila (ebb-nachtregel-v1.json, mip) en de vaste punten op AMOLED.
(:test)
function testNachtregel(logger as Test.Logger) as Boolean {
    var mip = [0x0000AA, 0x000055, 0xFF5500, 0xAA0000, 0x55FFAA, 0x005555, 0x00FF00, 0x005500, 0xFFFFFF, 0xAAAAAA,
        0xFFFF00, 0xAAAA00, 0x000055, 0x000000, 0xAAFFAA, 0x555555, 0x00AAFF, 0x0055AA] as Array<Number>;
    var goed = true;
    for (var i = 0; i < mip.size(); i += 2) {
        var uit = EbbNacht.k(mip[i], false);
        if (uit != mip[i + 1]) {
            logger.debug("mip " + mip[i].format("%06X") + " werd " + uit.format("%06X") + ", moet " + mip[i + 1].format("%06X"));
            goed = false;
        }
    }
    // AMOLED: wit wordt grijs 178, zwart blijft zwart, fel groen wordt donker en nooit sterker dan 80 voor het grijs.
    if (EbbNacht.k(0xFFFFFF, true) != 0xB2B2B2 || EbbNacht.k(0x000000, true) != 0x000000) {
        logger.debug("amoled wit " + EbbNacht.k(0xFFFFFF, true).format("%06X"));
        goed = false;
    }
    var gr = EbbNacht.k(0x00FF00, true);
    if (((gr >> 8) & 0xFF) > 80) {
        logger.debug("amoled groen " + gr.format("%06X"));
        goed = false;
    }
    return goed;
}
