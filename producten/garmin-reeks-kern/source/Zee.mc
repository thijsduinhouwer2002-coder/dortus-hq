import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// De zee van Tij: de waterlijn uit het verloop van Body Battery, de banden eronder, het bootje op "nu".
// Alles hier rekent alleen (geen scherm), zodat de toetsen het kunnen nakijken. Het voorbeeld is het
// tekenscript van Mila: ontwerp/garmin/reeks/stijl_proef_v3.py en stijl_proef_v5.py.
module Zee {
    // Stukken van de lijn over de geschiedenis, en stukken van het rustige water rechts van het bootje.
    const N = 24;
    const STAART = 6;
    // De sinus van het golfje naast het getal, anderhalve golf in acht stukken, maal 1000.
    const GOLFJE = [0, 924, 707, -383, -1000, -383, 707, 924, 0];
    // Het bootje in honderdsten van de halve rompbreedte: romp (4 punten), zeil (3), mast onder en boven.
    const BOOT = [-100, -15, 100, -15, 60, 35, -60, 35, 8, -145, 8, -35, 85, -35, 0, -15, 0, -150];

    function klem(v as Number) as Number {
        if (v < 0) {
            return 0;
        }
        if (v > 100) {
            return 100;
        }
        return v;
    }

    // Hoogte van het water bij een waarde van 0 tot 100: 0 op yBodem, 100 op yTop, afgerond zoals in lijn().
    function niveau(b as Number, yTop as Number, yBodem as Number) as Number {
        return yBodem - Math.round((yBodem - yTop) * klem(b) / 100.0).toNumber();
    }

    // De waterlijn, van x0 tot de rechterrand w. De geschiedenis (oudste eerst) loopt van x0 tot nuX, zacht
    // tussen de meetpunten; rechts van nuX ligt rustig water op de hoogte van nu. Eén waarde: een vlakke zee
    // met een lichte deining op die hoogte. Een stuk op 100 deint een paar px omlaag. Geen waarde: dezelfde vlakke zee halverwege. Altijd N + STAART + 1 punten.
    function lijn(hist as Array<Number>, x0 as Number, nuX as Number, w as Number, yTop as Number, yBodem as Number, t as Number) as Array<Graphics.Point2D> {
        var p = [] as Array<Graphics.Point2D>;
        var m = hist.size();
        var alle = N + STAART;
        if (m < 2) {
            var y0 = (m == 1) ? niveau(hist[0], yTop, yBodem) : (yTop + yBodem) / 2;
            for (var i = 0; i <= alle; i++) {
                var dy = w * 0.012 * Math.sin(i * 13.823 / alle + t);
                p.add([x0 + (w - x0) * i / alle, y0 + Math.round(dy).toNumber()]);
            }
            return p;
        }
        var yNu = yBodem;
        for (var i = 0; i <= N; i++) {
            var u = i * (m - 1) / N.toFloat();
            var a = u.toNumber();
            if (a > m - 1) {
                a = m - 1;
            }
            var b = (a + 1 < m) ? a + 1 : m - 1;
            var k = (1.0 - Math.cos((u - a) * Math.PI)) / 2.0;
            var v = klem(hist[a]) * (1.0 - k) + klem(hist[b]) * k;
            yNu = yBodem - Math.round((yBodem - yTop) * v / 100.0).toNumber();
            // Vol (100): een kleine deining, alleen omlaag, zodat een volle zee geen rechte plank is en toch nooit
            // boven het plafond komt (kan van Daan, 17 nov).
            if (v >= 99.5) {
                yNu += Math.round(w * 0.006 * (1.0 + Math.sin(i * 1.6 + t))).toNumber();
            }
            p.add([x0 + (nuX - x0) * i / N, yNu]);
        }
        for (var i = 1; i <= STAART; i++) {
            var dy = w * 0.006 * Math.sin(i * 1.6 + t);
            p.add([nuX + (w - nuX) * i / STAART, yNu + Math.round(dy).toNumber()]);
        }
        return p;
    }

    // Hoogte van de lijn op x, tussen de twee punten ernaast. Buiten de lijn: het eerste of laatste punt. Lege lijn: 0.
    function hoogte(pts as Array<Graphics.Point2D>, x as Number) as Number {
        var n = pts.size();
        if (n == 0) {
            return 0;
        }
        if (x <= (pts[0][0] as Number)) {
            return pts[0][1] as Number;
        }
        for (var i = 0; i + 1 < n; i++) {
            var ax = pts[i][0] as Number;
            var bx = pts[i + 1][0] as Number;
            if (x >= ax && x <= bx) {
                var ay = pts[i][1] as Number;
                var by = pts[i + 1][1] as Number;
                return (bx == ax) ? ay : ay + (by - ay) * (x - ax) / (bx - ax);
            }
        }
        return pts[n - 1][1] as Number;
    }

    // Eén band van de zee: de lijn, af px lager, dichtgemaakt langs de linkerrand, de onderrand en de rechterrand.
    function band(pts as Array<Graphics.Point2D>, af as Number, w as Number, h as Number) as Array<Graphics.Point2D> {
        var p = [] as Array<Graphics.Point2D>;
        if (pts.size() < 2) {
            return p;
        }
        p.add([0, (pts[0][1] as Number) + af]);
        for (var i = 0; i < pts.size(); i++) {
            p.add([pts[i][0], (pts[i][1] as Number) + af]);
        }
        p.add([w, h]);
        p.add([0, h]);
        return p;
    }

    // Het bootje op bx, by (waterlijn onder het midden van de romp), s is de halve breedte van de romp.
    // Negen punten: romp (4), zeil (3), mast onder en boven. hoek in graden: bijna leeg ligt het scheef.
    function boot(bx as Number, by as Number, s as Number, hoek as Number) as Array<Graphics.Point2D> {
        var vorm = BOOT;
        var a = hoek * Math.PI / 180.0;
        var co = Math.cos(a);
        var si = Math.sin(a);
        var p = [] as Array<Graphics.Point2D>;
        for (var i = 0; i + 1 < vorm.size(); i += 2) {
            var px = s * vorm[i] / 100.0;
            var py = s * vorm[i + 1] / 100.0;
            p.add([bx + Math.round(px * co - py * si).toNumber(), by + Math.round(px * si + py * co).toNumber()]);
        }
        return p;
    }

    // De omtrek van het bootje als losse lijnstukken [x0, y0, x1, y1], voor de slaapstand (kan van Mila en Daan):
    // romp (4 stukken, gesloten), zeil (3, gesloten) en de mast (1). Geen negen punten: lege lijst.
    function bootLijnen(b as Array<Graphics.Point2D>) as Array<Array<Number>> {
        var uit = [] as Array<Array<Number>>;
        if (b.size() != 9) {
            return uit;
        }
        for (var i = 0; i < 4; i++) {
            var j = (i + 1) % 4;
            uit.add([b[i][0] as Number, b[i][1] as Number, b[j][0] as Number, b[j][1] as Number] as Array<Number>);
        }
        for (var i = 0; i < 3; i++) {
            var j = 4 + (i + 1) % 3;
            uit.add([b[4 + i][0] as Number, b[4 + i][1] as Number, b[j][0] as Number, b[j][1] as Number] as Array<Number>);
        }
        uit.add([b[7][0] as Number, b[7][1] as Number, b[8][0] as Number, b[8][1] as Number] as Array<Number>);
        return uit;
    }

    // Liggen alle punten binnen de cirkel met midden c, c en deze straal?
    function past(pts as Array<Graphics.Point2D>, c as Number, straal as Number) as Boolean {
        for (var i = 0; i < pts.size(); i++) {
            var dx = (pts[i][0] as Number) - c;
            var dy = (pts[i][1] as Number) - c;
            if (dx * dx + dy * dy > straal * straal) {
                return false;
            }
        }
        return true;
    }

    // Plek van het bootje: begint op nuX, schuift naar links tot het binnen de veilige cirkel past, maar nooit
    // verder dan minX (de rechterkant van het getal plus ruimte): het bootje vaart nooit onder het getal.
    function bootX(nuX as Number, minX as Number, by as Number, s as Number, hoek as Number, c as Number, straal as Number, stap as Number) as Number {
        var x = (nuX > minX) ? nuX : minX;
        if (stap < 1) {
            stap = 1;
        }
        while (x > minX && !past(boot(x, by, s, hoek), c, straal)) {
            x -= stap;
            if (x < minX) {
                x = minX;
            }
        }
        return x;
    }

    // Het hoogste punt (kleinste y) van de punten met x tussen xa en xb. Geen punt daar: 9999.
    function topTussen(pts as Array<Graphics.Point2D>, xa as Number, xb as Number) as Number {
        var top = 9999;
        for (var i = 0; i < pts.size(); i++) {
            var x = pts[i][0] as Number;
            var y = pts[i][1] as Number;
            if (x >= xa && x <= xb && y < top) {
                top = y;
            }
        }
        return top;
    }

    // Hoeveel px het getal omhoog moet om g px ruimte te houden boven top, hoogstens maxOmhoog.
    function schuif(onder as Number, g as Number, top as Number, maxOmhoog as Number) as Number {
        var tekort = onder + g - top;
        if (tekort < 0) {
            tekort = 0;
        }
        if (tekort > maxOmhoog) {
            tekort = maxOmhoog;
        }
        return (tekort < 0) ? 0 : tekort;
    }

    // Kleur tussen a (i = 0) en b (i = n), per kanaal.
    function meng(a as Number, b as Number, i as Number, n as Number) as Number {
        if (n < 1) {
            return a;
        }
        var uit = 0;
        for (var s = 16; s >= 0; s -= 8) {
            var ka = (a >> s) & 0xFF;
            var kb = (b >> s) & 0xFF;
            uit = uit | ((ka + (kb - ka) * i / n) << s);
        }
        return uit;
    }

    // Dezelfde kleur, elk kanaal erbij hoger (hoogstens 255): de kleur van de waterlijn.
    function lichter(kleur as Number, erbij as Number) as Number {
        var uit = 0;
        for (var s = 16; s >= 0; s -= 8) {
            var k = ((kleur >> s) & 0xFF) + erbij;
            if (k > 255) {
                k = 255;
            }
            uit = uit | (k << s);
        }
        return uit;
    }

    // De twee lijntjes van het golfje naast het getal: midden cx, cy, breedte k. Geeft twee rijen van negen punten.
    function golfje(cx as Number, cy as Number, k as Number) as Array<Array<Graphics.Point2D>> {
        var uit = [] as Array<Array<Graphics.Point2D>>;
        for (var r = -1; r <= 1; r += 2) {
            var p = [] as Array<Graphics.Point2D>;
            for (var i = 0; i < GOLFJE.size(); i++) {
                var y = cy + r * k * 19 / 100.0 - k * 13 * GOLFJE[i] / 100000.0;
                p.add([cx - k / 2 + k * i / 8, Math.round(y).toNumber()]);
            }
            uit.add(p);
        }
        return uit;
    }
}
