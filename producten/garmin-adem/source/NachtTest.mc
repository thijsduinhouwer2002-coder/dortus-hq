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

// Nachtregel v1.4 voor de held (run 73): groen, bruin en elke koele kleur (blauw minstens zo sterk als rood) houden
// op MIP hun dagkleur en op AMOLED 80 procent; warm gaat door de gewone regel. De orka (555555) was op MIP zwart
// op zwart water.
(:test)
function testNachtHeld(logger as Test.Logger) as Boolean {
    var rij = [0x555555, 0x555555, 0x444444, 0x5555FF, 0x5555FF, 0x4444CC, 0x5555AA, 0x5555AA, 0x444488,
        0x55AAFF, 0x55AAFF, 0x4488CC, 0xAA55FF, 0xAA55FF, 0x8844CC, 0x00AA55, 0x00AA55, 0x008844,
        0xFFFF55, 0xFFFF55, 0xCCCC44, 0xAA5500, 0xAA5500, 0x884400, 0xAAAAAA, 0xAAAAAA, 0x888888,
        0xFFFFFF, 0xFFFFFF, 0xCCCCCC, 0x000000, 0x000000, 0x000000] as Array<Number>;
    var goed = true;
    for (var i = 0; i < rij.size(); i += 3) {
        var m = EbbNacht.held(rij[i], false);
        var a = EbbNacht.held(rij[i], true);
        if (m != rij[i + 1] || a != rij[i + 2]) {
            logger.debug("held " + rij[i].format("%06X") + " werd " + m.format("%06X") + " en " + a.format("%06X"));
            goed = false;
        }
    }
    // Warm blijft de gewone nachtregel volgen, ook donkerrood (anders valt de schaar samen met het lijf).
    var warm = [0xFF5500, 0xFFAA55, 0xFF55AA, 0xFFAA00, 0xFF5555, 0xAA0000, 0x550000, 0xAA0055] as Array<Number>;
    for (var j = 0; j < warm.size(); j += 1) {
        if (EbbNacht.held(warm[j], false) != EbbNacht.k(warm[j], false) || EbbNacht.held(warm[j], true) != EbbNacht.k(warm[j], true)) {
            logger.debug("held warm " + warm[j].format("%06X") + " volgt de regel niet");
            goed = false;
        }
    }
    return goed;
}
