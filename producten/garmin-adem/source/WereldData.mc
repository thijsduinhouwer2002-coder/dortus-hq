import Toybox.Lang;

// GEMAAKT door bron/maak_werelden.py uit ebb-werelden-v11-data.json (werelden v1.1). Niet met de hand wijzigen.
// Per veelhoek [kleur, x, y, x, y, ...] in 1/260 D; y telt vanaf de bovenkant van de strook (BOVEN).
module EbbWereldData {
    const EENHEID = 260;
    const BOVEN = 118;

    function vlakken(dier as Number) as Array<Array<Number> > or Null {
        if (dier == 3) {   // Turtle: zeegrasweide
            return [
                [0xAAAA55, 0, 110, 45, 104, 95, 108, 135, 103, 175, 107, 220, 101, 260, 107, 260, 142, 0, 142],
                [0xFFFFAA, 70, 118, 100, 114, 128, 119, 100, 121],
                [0xFFFFAA, 150, 126, 178, 122, 204, 127, 178, 129],
                [0x00AA55, 0, 116, 7, 58, 0, 0, 12, 116],
                [0x55AA00, 14, 116, 12, 69, 22, 22, 26, 116],
                [0x005500, 12, 118, 31, 88, 34, 58, 20, 118],
                [0x55AA00, 36, 112, 47, 88, 48, 64, 44, 112],
                [0x00AA55, 248, 114, 247, 59, 260, 4, 260, 114],
                [0x55AA00, 234, 114, 241, 68, 236, 22, 246, 114],
                [0x005500, 240, 116, 225, 88, 226, 60, 248, 116],
                [0x55AA00, 214, 110, 208, 89, 210, 68, 222, 110],
                [0x00AA55, 50, 114, 54, 88, 60, 78, 66, 82, 62, 86, 62, 94, 66, 98, 64, 114],
                [0x55AA00, 109, 112, 110, 108, 108, 105, 115, 112],
                [0x00AA55, 147, 111, 148, 108, 154, 105, 153, 111]
            ] as Array<Array<Number> >;
        }
        if (dier == 4) {   // Crab: rotsen met verloren slipper
            return [
                [0xFFFFAA, 0, 112, 60, 106, 130, 109, 200, 105, 260, 111, 260, 142, 0, 142],
                [0xAAAA55, 40, 130, 90, 125, 140, 130, 90, 133],
                [0x555555, 0, 8, 16, 2, 32, 16, 36, 52, 52, 80, 60, 114, 0, 118],
                [0xAAAAAA, 2, 10, 16, 4, 28, 14, 14, 16],
                [0x5555AA, 46, 114, 58, 92, 78, 88, 92, 102, 94, 116],
                [0xAAAAFF, 60, 94, 76, 90, 82, 96, 68, 96],
                [0x555555, 260, 14, 244, 8, 228, 22, 224, 54, 210, 86, 206, 114, 260, 118],
                [0xAAAAAA, 258, 16, 244, 10, 232, 20, 246, 22],
                [0x5555AA, 214, 115, 200, 100, 184, 102, 178, 116],
                [0xAA0055, 108, 122, 118, 114, 146, 112, 160, 117, 152, 127, 116, 128],
                [0xFF55AA, 111, 121, 119, 116, 145, 114, 157, 117, 150, 125, 117, 126],
                [0xFFFFFF, 124, 121, 140, 106, 154, 118, 150, 118, 140, 110, 129, 122],
                [0xFFAAAA, 170, 122, 176, 116, 182, 122, 176, 124],
                [0xFFAA55, 20, 72, 27, 67, 31, 74, 24, 78]
            ] as Array<Array<Number> >;
        }
        if (dier == 7) {   // Clownfish: anemoon met zwaaiende arm
            return [
                [0xAA5555, 0, 108, 50, 104, 110, 110, 160, 104, 210, 108, 260, 102, 260, 142, 0, 142],
                [0xFFAA55, 80, 122, 100, 116, 124, 122, 100, 126],
                [0xFFAA55, 150, 118, 166, 114, 180, 119, 166, 122],
                [0xAA0055, 0, 118, 6, 86, 60, 86, 66, 118],
                [0xFF55AA, -8, 92, -2, 12, 4, 82, 9, 26, 14, 82, 19, 38, 24, 82, 29, 48, 34, 82, 40, 58, 46, 82, 52, 68, 58, 82, 64, 78, 70, 92],
                [0xAA55FF, 260, 10, 238, 18, 226, 54, 212, 88, 224, 108, 260, 112],
                [0x550055, 246, 104, 240, 42, 243, 42, 250, 104],
                [0xFFAA00, 196, 110, 193, 94, 188, 86, 191, 84, 197, 90, 200, 80, 204, 81, 202, 96, 204, 110]
            ] as Array<Array<Number> >;
        }
        return null;
    }

    // Details die met trouw verschijnen: [week, kleur, x, y, ...], oplopend op week.
    function details(dier as Number) as Array<Array<Number> > or Null {
        return null;
    }

    // Komt over het dier heen (bijvoorbeeld de voorste vingers van de anemoon).
    function voor(dier as Number) as Array<Array<Number> > or Null {
        if (dier == 7) {   // Clownfish: anemoon met zwaaiende arm
            return [
                [0xFFAAFF, -2, 96, 7, 50, 12, 86, 21, 60, 26, 86, 35, 68, 40, 86, 49, 76, 54, 86, 63, 84, 68, 96],
                [0xFFAAFF, 60, 96, 66, 80, 72, 70, 82, 64, 84, 72, 74, 78, 72, 96],
                [0xFFFFAA, 78, 64, 84, 60, 88, 66, 84, 72]
            ] as Array<Array<Number> >;
        }
        return null;
    }

    // Waar het dier woont (midden van het dier), in 1/260 D van het hele scherm.
    function thuis(dier as Number) as Array<Number> or Null {
        if (dier == 3) { return [84, 214] as Array<Number>; }
        if (dier == 4) { return [178, 214] as Array<Number>; }
        if (dier == 7) { return [36, 196] as Array<Number>; }
        return null;
    }
}
