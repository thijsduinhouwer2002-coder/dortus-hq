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

    // Hoeveel kleuren het scherm heeft: VOL (AMOLED en andere schermen met duizenden kleuren), MIP64 of MIP8.
    const VOL = 0;
    const MIP64 = 1;
    const MIP8 = 2;

    // 64 kleuren (elk kanaal 00, 55, AA of FF), keuze van Mila (ontwerp/garmin/tij/kleuren-64-8.md, 17 nov):
    // gedempt boven, en bij elk thema hetzelfde nachtblauw onder.
    var mipBanden as Array<Number> = [
        0xAA5555, 0xAA0055, 0x550055, 0x000055,
        0x55AAAA, 0x0055AA, 0x0000AA, 0x000055,
        0xAAAA55, 0x55AA55, 0x005555, 0x000055,
        0x5555AA, 0x5500AA, 0x0000AA, 0x000055
    ] as Array<Number>;
    // 64 kleuren: de waterlijn en de minuten per thema, uit dezelfde tabel.
    var mipLijn as Array<Number> = [0xFFAAAA, 0xAAFFFF, 0xFFFFAA, 0xAAAAFF] as Array<Number>;
    var mipMinuten as Array<Number> = [0xFFAA55, 0x55FFFF, 0xAAFFAA, 0xAAAAFF] as Array<Number>;
    // 8 kleuren: één vaste zee voor alle thema's, cyaan boven en blauw onder.
    const CYAAN = 0x00FFFF;
    const BLAUW = 0x0000FF;

    // Thema binnen de lijst; onbekend: Tide.
    function geldig(thema as Number) as Number {
        return (thema < 0 || thema >= AANTAL) ? TIDE : thema;
    }

    // Kleur van band i (0 boven tot 3 onder). VOL: in vier stappen van zee boven naar zee onder.
    function band(thema as Number, i as Number, diepte as Number) as Number {
        if (i < 0) {
            i = 0;
        }
        if (i > 3) {
            i = 3;
        }
        var t = geldig(thema);
        if (diepte == MIP8) {
            return (i < 2) ? CYAAN : BLAUW;
        }
        if (diepte == MIP64) {
            return mipBanden[t * 4 + i];
        }
        return Zee.meng(kleur(t, ZEE_BOVEN), kleur(t, ZEE_ONDER), i, 3);
    }

    // De waterlijn (ook de kleur van het golfje naast het getal).
    function waterlijn(thema as Number, diepte as Number) as Number {
        var t = geldig(thema);
        if (diepte == MIP8) {
            return CYAAN;
        }
        if (diepte == MIP64) {
            return mipLijn[t];
        }
        return Zee.lichter(kleur(t, ZEE_BOVEN), 70);
    }

    // De minuten (en het hart). 64 kleuren: de lichte themakleur van Mila. 8 kleuren: cyaan.
    function minuten(thema as Number, diepte as Number) as Number {
        var t = geldig(thema);
        if (diepte == MIP8) {
            return CYAAN;
        }
        if (diepte == MIP64) {
            return mipMinuten[t];
        }
        return kleur(t, MINUTEN);
    }

    // Het zeil. Op 64 en 8 kleuren altijd wit: het lichtste vlak, nooit een kleur die ook in het water zit (moet van Daan).
    function zeil(thema as Number, diepte as Number) as Number {
        return (diepte == MIP64 || diepte == MIP8) ? 0xFFFFFF : kleur(thema, MINUTEN);
    }

    // De uren en de dubbele punt. Op 8 kleuren vast: uren wit, punt cyaan. Op 64 kleuren is de punt de kleur van de minuten.
    function uren(thema as Number, diepte as Number) as Number {
        return (diepte == MIP8) ? 0xFFFFFF : kleur(thema, UREN);
    }

    function punt(thema as Number, diepte as Number) as Number {
        if (diepte == MIP64) {
            // Kan van Daan (17 nov): op 64 kleuren de dubbele punt gelijk aan de minuten, één blok kleur naast wit.
            return minuten(thema, diepte);
        }
        return (diepte == MIP8) ? CYAAN : kleur(thema, PUNT);
    }

    // De rand om het getal van Body Battery. VOL: de donkere zee, nog donkerder. 64 en 8 kleuren: zwart.
    function rand(thema as Number, diepte as Number) as Number {
        return (diepte == MIP64 || diepte == MIP8) ? 0x000000 : Zee.meng(kleur(thema, ZEE_ONDER), 0x000000, 4, 10);
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
