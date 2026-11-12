import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.Time;

// Besluit hoofdchat 12 nov 00:25 punt 2: de lucht volgt het uur en de maan staat in de fase van die dag.
// Alleen rekenen uit de klok en de datum, geen netwerk. Tekenen: `teken` (lucht, horizon, zon of maan, sterren, wolk)
// volgens Mila's werelden v1.4 (ontwerp/garmin/werelden14/ebb-lucht-v14-data.json); nu alleen in de proefscènes.
module EbbLucht {
    // Maanfase in achtsten: 0 nieuw, 1 wassende sikkel, 2 eerste kwartier, 3 wassend, 4 vol, 5 afnemend,
    // 6 laatste kwartier, 7 afnemende sikkel. Gemiddelde maanmaand van 29,530588 dagen vanaf de nieuwe maan van
    // 6 jan 2000 18:14 UTC; de echte maan wijkt hoogstens ruim een halve dag af, voor acht standen is dat genoeg.
    function maanfase(unix as Number) as Number {
        var maand = 2551443;
        var r = (unix - 947182440) % maand;
        if (r < 0) {
            r += maand;
        }
        return ((r * 8 + maand / 2) / maand) % 8;
    }

    // Dagdeel uit het uur van de klok, uren van Mila (lucht v1.4): 0 ochtend (6 tot 10), 1 dag (10 tot 17),
    // 2 avond (17 tot 21), 3 nacht.
    function dagdeel(uur as Number) as Number {
        if (uur >= 6 && uur < 10) {
            return 0;
        }
        if (uur >= 10 && uur < 17) {
            return 1;
        }
        if (uur >= 17 && uur < 21) {
            return 2;
        }
        return 3;
    }

    // Alleen aan in de proefscènes van de plaatjesbouw (scène 47 tot 50), tot Mila's blad boven water gekeurd is.
    var proef as Boolean = false;
    var proefDeel as Number = 0;
    var proefMaan as Number = 0;

    function deelNu() as Number {
        return proef ? proefDeel : dagdeel(System.getClockTime().hour);
    }

    function maanNu() as Number {
        return proef ? proefMaan : maanfase(Time.now().value());
    }

    // Kleur van de lucht per dagdeel (alleen de 64 kleuren van MIP).
    const KLEUR = [0x0000AA, 0x0000AA, 0x550055, 0x000055] as Array<Number>;
    // Sterren in 1/260 D, buiten het fasewoord en het grote getal en binnen de ronde rand; 's avonds alleen de eerste drie.
    const STERREN = [52, 70, 196, 84, 100, 22, 70, 112, 40, 128, 224, 108, 170, 18] as Array<Number>;
    const WOLK = [208, 96, 214, 88, 224, 88, 230, 80, 240, 82, 246, 90, 250, 96] as Array<Number>;
    const WOLK2 = [14, 110, 20, 104, 30, 105, 36, 100, 46, 104, 50, 110] as Array<Number>;
    // Zon overdag en de maan staan rechtsboven. Mila gaf 214, 40 met straal 8; dat valt 1 buiten de ronde rand
    // (afstand tot het midden 123 plus 8 is 131 van 130) en op 210, 44 stond hij 4 px naast de t van "breathe out"
    // (beeld FR255, run 43130206691). Nu 222, 60: 16 px rechts van het fasewoord, onder de regel, 10 px boven de wolk.
    const HOOG_X = 222;
    const HOOG_Y = 60;
    const HOOG_R = 8;

    // Lucht van de ademschermen, vóór de zee getekend: de zee dekt alles onder de kam. kam is de hoogte van de
    // waterlijn in pixels; de horizonstreep ligt er direct boven en beweegt mee. Hoogstens 13 punten in veelhoeken.
    function teken(dc as Graphics.Dc, d as Number, deel as Number, maan as Number, kam as Number) as Void {
        var w = dc.getWidth();
        var lucht = KLEUR[deel];
        dc.setColor(lucht, lucht);
        dc.clear();
        var onder = EbbTeken.px(d, 6);   // tot onder de golf, zodat er geen kier tussen streep en water valt
        if (deel == 0) {
            dc.setColor(0xFF55AA, 0xFF55AA);
            dc.fillRectangle(0, kam - EbbTeken.px(d, 13), w, EbbTeken.px(d, 9) + 1);
            dc.setColor(0xFFAA55, 0xFFAA55);
            dc.fillRectangle(0, kam - EbbTeken.px(d, 4), w, EbbTeken.px(d, 4) + onder);
        } else if (deel == 2) {
            dc.setColor(0xFF5500, 0xFF5500);
            dc.fillRectangle(0, kam - EbbTeken.px(d, 7), w, EbbTeken.px(d, 7) + onder);
        }
        if (deel >= 2) {
            var n = (deel == 2) ? 3 : STERREN.size() / 2;
            var s = EbbTeken.px(d, 2);
            dc.setColor(EbbTeken.LICHT, EbbTeken.LICHT);
            for (var i = 0; i < n; i += 1) {
                dc.fillRectangle(EbbTeken.px(d, STERREN[2 * i]), EbbTeken.px(d, STERREN[2 * i + 1]), s, s);
            }
        }
        if (deel == 0) {
            // Grote zon komt links van het midden half uit het water.
            dc.setColor(0xFFFF55, 0xFFFF55);
            dc.fillCircle(EbbTeken.px(d, 96), kam + EbbTeken.px(d, 2), EbbTeken.px(d, 10));
        } else if (deel == 1) {
            dc.setColor(0xFFFF55, 0xFFFF55);
            dc.fillCircle(EbbTeken.px(d, HOOG_X), EbbTeken.px(d, HOOG_Y), EbbTeken.px(d, HOOG_R));
            wolk(dc, d, WOLK);
            wolk(dc, d, WOLK2);
        } else if (deel == 2) {
            // Oranje zon zakt rechts van het midden in het water.
            dc.setColor(0xFFAA00, 0xFFAA00);
            dc.fillCircle(EbbTeken.px(d, 166), kam + EbbTeken.px(d, 1), EbbTeken.px(d, 11));
        } else {
            maanSchijf(dc, d, maan, lucht);
        }
    }

    function wolk(dc as Graphics.Dc, d as Number, p as Array<Number>) as Void {
        var pts = [] as Array<[Numeric, Numeric]>;
        for (var i = 0; i + 1 < p.size(); i += 2) {
            pts.add([EbbTeken.px(d, p[i]), EbbTeken.px(d, p[i + 1])]);
        }
        dc.setColor(0xFFFFFF, 0xFFFFFF);
        dc.fillPolygon(pts);
    }

    // De maan in acht standen: schijf in het licht, de donkere helft in de kleur van de lucht eroverheen, en bij sikkel
    // (lucht, 0,35 r) en bolle maan (licht, 0,6 r) een ellips over de middellijn. Nieuwe maan is alleen een dunne ring.
    function maanSchijf(dc as Graphics.Dc, d as Number, stand as Number, lucht as Number) as Void {
        var x = EbbTeken.px(d, HOOG_X);
        var y = EbbTeken.px(d, HOOG_Y);
        var r = EbbTeken.px(d, HOOG_R);
        if (stand == 0) {
            dc.setColor(0x5555AA, Graphics.COLOR_TRANSPARENT);
            dc.drawCircle(x, y, r);
            return;
        }
        dc.setColor(EbbTeken.LICHT, EbbTeken.LICHT);
        dc.fillCircle(x, y, r);
        if (stand == 4) {
            return;
        }
        dc.setColor(lucht, lucht);
        dc.fillRectangle(stand < 4 ? x - r - 1 : x + 1, y - r - 1, r + 1, 2 * r + 3);
        if (stand == 1 || stand == 7) {
            dc.fillEllipse(x, y, (r * 35 + 50) / 100, r);
        } else if (stand == 3 || stand == 5) {
            dc.setColor(EbbTeken.LICHT, EbbTeken.LICHT);
            dc.fillEllipse(x, y, (r * 60 + 50) / 100, r);
        }
    }
}
