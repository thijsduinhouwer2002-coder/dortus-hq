import Toybox.Lang;

// De vier thema's van de reeks. Kleuren uit het blad van Mila (maten-tij-tabel.md, tabel "thema").
// Eén rij per thema, zeven rollen per rij, in de volgorde van de kolommen van het blad.
module Thema {
    const AANTAL = 4;
    const DUSK = 0;
    const TIDE = 1;
    const KELP = 2;
    const NIGHT = 3;

    const ROLLEN = 7;
    const ZEE_BOVEN = 0;
    const ZEE_ONDER = 1;
    const UREN = 2;
    const MINUTEN = 3;
    const TEKST = 4;
    const PUNT = 5;
    const BOOT = 6;

    var kleuren as Array<Number> = [
        0xFF8C3C, 0x6E1928, 0xFFEED6, 0xFFAA50, 0xFFE2BE, 0x96684C, 0xFFF6E6,
        0x28C8DC, 0x082454, 0xE1F8FF, 0x3CDCE6, 0xC8ECF5, 0x508096, 0xFFFFFF,
        0x96D23C, 0x12381C, 0xECF4DC, 0xAAE146, 0xDCE8C8, 0x6E8454, 0xFFFAE6,
        0x5A6EFF, 0x120A38, 0xF0F0FF, 0x96A0FF, 0xDCDCF5, 0x6E6EA0, 0xFFDC78
    ] as Array<Number>;

    // Kleur van een rol in een thema. Onbekend thema: Tide. Onbekende rol: wit, zodat tekst leesbaar blijft.
    function kleur(thema as Number, rol as Number) as Number {
        if (rol < 0 || rol >= ROLLEN) {
            return 0xFFFFFF;
        }
        var t = thema;
        if (t < 0 || t >= AANTAL) {
            t = TIDE;
        }
        return kleuren[t * ROLLEN + rol];
    }

    // Alleen voor de proef in de bouwstraat (weg in stap (d), als de drager zelf kiest): elk proefhorloge een
    // ander thema, zodat alle vier in beeld komen. 208, 240 en 320 px: Dusk, 454: Tide, 260: Kelp, 390: Night.
    function voorProef(breedte as Number) as Number {
        if (breedte < 0) {
            return TIDE;
        }
        return (breedte / 10) % AANTAL;
    }
}
