import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.WatchUi;

// Mila blad v9 punt 3: "sea complete" als eigen feest, na de walvis. Hoge zee (kamlijn 77/260), de walvis groot in
// het midden met een fontein van drie belletjes, de 23 andere vrienden in een glimlach van twee bogen eronder,
// "sea complete", "24 of 24 friends" en de reeks in weken. Geen tijden (die staan één knop verder).
// Watchdog: alle 24 dieren komen één keer in één doorzichtig plaatje, één laag per beurt via EbbDierPlaatje.laag;
// daarna kost een beurt alleen de zee, de tekst en het plakken.
// Keuring bouw 5 punt 3: op 416 en 454 bleef het scherm 120 beurten leeg. Nu komt de walvis eerst en wordt elke beurt
// geplakt wat er al staat, zodat het feest meteen zichtbaar is en aangroeit. Bij verlaten laat los() het plaatje los.
module EbbSeaComplete {
    const WALVIS = 23;
    // [straal, aantal, van hoek, tot hoek] in 1/260 D en graden (90 is recht onder), midden (130, 98).
    const BOGEN = [[93, 14, 32, 148], [62, 9, 46, 134]] as Array<Array<Number> >;

    var _ref as Graphics.BufferedBitmapReference or Null = null;
    var _d as Number = 0;
    var _dier as Number = 0;   // volgnummer 0 tot 23 (0 tot 22 in de glimlach, 23 de walvis)
    var _laag as Number = 0;
    var _x0 as Number = 0;     // linksboven van het plaatje op het scherm
    var _y0 as Number = 0;

    function px(d as Number, v as Number) as Number {
        return (v * d + 130) / 260;
    }

    // Plek op het scherm en maat van volgnummer k: [x, y, maat].
    function plek(d as Number, k as Number) as Array<Number> {
        if (k == WALVIS) {
            return [d / 2, px(d, 108), d < 300 ? px(d, 38) : (66 * d + 227) / 454] as Array<Number>;
        }
        var b = k < 14 ? BOGEN[0] : BOGEN[1];
        var i = k < 14 ? k : k - 14;
        var hoek = Math.toRadians(b[2] + (b[3] - b[2]) * i / (b[1] - 1.0));
        var r = b[0] * d / 260.0;
        var m = d < 300 ? px(d, 11) : (19 * d + 227) / 454;
        return [(d / 2 + r * Math.cos(hoek)).toNumber(), (98 * d / 260.0 + r * Math.sin(hoek)).toNumber(), m] as Array<Number>;
    }

    function maak(d as Number) as Void {
        _d = d;
        _dier = 0;
        _laag = 0;
        // Plaatje van 0,08 D tot 0,92 D breed en van boven de walvis tot onder de buitenboog.
        _x0 = px(d, 22);
        _y0 = px(d, 66);
        var br = px(d, 216);
        var ho = px(d, 150);
        _ref = Graphics.createBufferedBitmap({:width => br, :height => ho});
        var bb = (_ref as Graphics.BufferedBitmapReference).get() as Graphics.BufferedBitmap;
        var dc = bb.getDc();
        dc.setColor(Graphics.COLOR_TRANSPARENT, Graphics.COLOR_TRANSPARENT);
        dc.clear();
    }

    // Eén laag erbij; true als alle 24 dieren erin staan.
    function verder() as Boolean {
        if (_dier > WALVIS) {
            return true;
        }
        var bb = (_ref as Graphics.BufferedBitmapReference).get();
        if (bb == null) {
            return false;
        }
        // Volgorde: eerst de walvis (23), dan 0 tot 22.
        var k = (_dier + WALVIS) % (WALVIS + 1);
        var p = plek(_d, k);
        EbbDierPlaatje.laag((bb as Graphics.BufferedBitmap).getDc(), k, p[0] - _x0, p[1] - _y0, p[2], EbbDierPlaatje.GEVONDEN, _laag);
        _laag += 1;
        if (_laag >= EbbDierPlaatje.lagenVan(EbbDierPlaatje.GEVONDEN)) {
            _laag = 0;
            _dier += 1;
        }
        return _dier > WALVIS;
    }

    // Plaatje loslaten als het scherm weggaat (geheugen voor de rest van de app).
    function los() as Void {
        _ref = null;
        _d = 0;
    }

    function tekst(dc as Graphics.Dc, d as Number, y as Number, f as Graphics.FontType, s as String, kleur as Number) as Void {
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, px(d, y), f, s, Graphics.TEXT_JUSTIFY_CENTER);
    }

    function teken(dc as Graphics.Dc, d as Number, reeks as Number) as Void {
        if (_ref == null || _d != d) {
            maak(d);
        }
        var top = 77.0 / 260;
        EbbZee.zeeBanden(dc, d, [top, top + 0.45 * (1 - top), top + 0.72 * (1 - top)] as Array<Float>, [1, 2, 3] as Array<Number>, 0.010, 0.4);
        // Fontein: drie belletjes boven de walvis.
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(d / 260 > 1 ? d / 260 : 1);
        var bel = [[0, 88, 4], [-7, 81, 3], [8, 78, 3]] as Array<Array<Number> >;
        for (var i = 0; i < bel.size(); i += 1) {
            var r = px(d, bel[i][2]);
            dc.drawCircle(d / 2 + px(d, bel[i][0]), px(d, bel[i][1]), r < 1 ? 1 : r);
        }
        dc.setPenWidth(1);
        var klaar = verder();
        var bb = (_ref as Graphics.BufferedBitmapReference).get();
        if (bb != null) {
            dc.drawBitmap(_x0, _y0, bb as Graphics.BufferedBitmap);
        }
        if (!klaar) {
            WatchUi.requestUpdate();
        }
        tekst(dc, d, 26, EbbTeken.fS(), "sea complete", EbbTeken.LICHT);
        tekst(dc, d, 51, EbbTeken.fX(), "24 of 24 friends", EbbTeken.SCHUIM);
        tekst(dc, d, 206, EbbTeken.fX(), reeks + (reeks == 1 ? " week in a row" : " weeks in a row"), EbbTeken.SCHUIM);
    }
}
