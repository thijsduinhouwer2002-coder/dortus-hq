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

    // Banden van de zee op een scherm met 64 kleuren: vaste paletkleuren (elk kanaal 00, 55, AA of FF), licht boven,
    // donker onder. Voorstel van Daan (17 nov) voor Dusk en Kelp, Tide en Night op dezelfde manier; Mila kiest nog.
    var mipBanden as Array<Number> = [
        0xFFAA55, 0xFF5500, 0xAA0000, 0x550000,
        0x55FFFF, 0x00AAFF, 0x0055AA, 0x000055,
        0xAAFF55, 0x55FF00, 0x55AA00, 0x005500,
        0x5555FF, 0x0000FF, 0x0000AA, 0x000055
    ] as Array<Number>;

    // Kleur van band i (0 boven tot 3 onder). Gewoon scherm: in vier stappen van zee boven naar zee onder.
    function band(thema as Number, i as Number, mip as Boolean) as Number {
        if (i < 0) {
            i = 0;
        }
        if (i > 3) {
            i = 3;
        }
        var t = thema;
        if (t < 0 || t >= AANTAL) {
            t = TIDE;
        }
        if (mip) {
            return mipBanden[t * 4 + i];
        }
        return Zee.meng(kleur(t, ZEE_BOVEN), kleur(t, ZEE_ONDER), i, 3);
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
