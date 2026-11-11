import Toybox.Graphics;
import Toybox.Lang;
import Toybox.WatchUi;

// Mila blad v10 punt 1: "sea complete" als groepsfoto. Hoge zee (kamlijn 58/260), de walvis groot in het midden met
// een fontein van drie belletjes onder de kamlijn, de 23 andere vrienden in rijen eromheen (4 naast de walvis, dan
// 7, 6 en 6), op volgorde van het schema. "sea complete" bovenaan, "24 of 24 friends" en de reeks onderaan. Geen tijden.
// Watchdog: alle 24 dieren komen één keer in één doorzichtig plaatje via EbbDierPlaatje.laag; per beurt één laag, op
// grote AMOLED-schermen (416 en 454) drie (lokaal gemeten: een tijdsbudget van 30 ms gaf op FR255 toch de watchdog). Keuring bouw 5 punt 3: de walvis eerst, en elke beurt
// wordt geplakt wat er al staat, zodat het feest meteen zichtbaar is en aangroeit. Bij verlaten laat los() het plaatje los.
module EbbSeaComplete {
    const WALVIS = 23;
    // Plek van vriend 0 tot 22 in 1/260 D: x vanaf het midden, y vanaf de bovenkant (blad v10, tabel).
    const PLEK = [[-86, 100], [-58, 100], [58, 100], [86, 100],
        [-87, 136], [-58, 136], [-29, 136], [0, 136], [29, 136], [58, 136], [87, 136],
        [-76, 160], [-47, 160], [-18, 160], [18, 160], [47, 160], [76, 160],
        [-72, 188], [-45, 188], [-17, 188], [17, 188], [45, 188], [72, 188]] as Array<Array<Number> >;

    var _ref as Graphics.BufferedBitmapReference or Null = null;
    var _d as Number = 0;
    var _dier as Number = 0;   // hoeveelste in de opbouw (0 is de walvis, daarna vriend 0 tot 22)
    var _laag as Number = 0;
    var _x0 as Number = 0;     // linksboven van het plaatje op het scherm
    var _y0 as Number = 0;

    function px(d as Number, v as Number) as Number {
        return (v * d + 130) / 260;
    }

    // Plek op het scherm en maat van volgnummer k: [x, y, maat]. Maat vrienden floor(11 D / 260), onder 250 px één
    // kleiner; walvis round(32 D / 260).
    function plek(d as Number, k as Number) as Array<Number> {
        if (k == WALVIS) {
            return [d / 2, px(d, 100), px(d, 32)] as Array<Number>;
        }
        var m = 11 * d / 260;
        m = d < 250 ? m - 1 : m;
        return [d / 2 + px(d, PLEK[k][0]), px(d, PLEK[k][1]), m] as Array<Number>;
    }

    function maak(d as Number) as Void {
        _d = d;
        _dier = 0;
        _laag = 0;
        // Plaatje van x 14 tot 246 en y 62 tot 206 (in 1/260 D): alle dieren met stickerrand, binnen 0,85 R.
        _x0 = px(d, 14);
        _y0 = px(d, 62);
        _ref = Graphics.createBufferedBitmap({:width => px(d, 232), :height => px(d, 144)});
        var bb = (_ref as Graphics.BufferedBitmapReference).get() as Graphics.BufferedBitmap;
        var dc = bb.getDc();
        dc.setColor(Graphics.COLOR_TRANSPARENT, Graphics.COLOR_TRANSPARENT);
        dc.clear();
    }

    // Eén laag erbij (drie op 416 en 454); true als alle 24 dieren erin staan.
    function verder() as Boolean {
        var bb = (_ref as Graphics.BufferedBitmapReference).get();
        if (bb == null) {
            return false;
        }
        var dc = (bb as Graphics.BufferedBitmap).getDc();
        var lagen = EbbDierPlaatje.lagenVan(EbbDierPlaatje.GEVONDEN);
        var n = (EbbTeken.amoled() && _d >= 416) ? 3 : 1;
        while (_dier <= WALVIS && n > 0) {
            n -= 1;
            // Volgorde: eerst de walvis (23), dan 0 tot 22.
            var k = (_dier + WALVIS) % (WALVIS + 1);
            var p = plek(_d, k);
            EbbDierPlaatje.laag(dc, k, p[0] - _x0, p[1] - _y0, p[2], EbbDierPlaatje.GEVONDEN, _laag);
            _laag += 1;
            if (_laag >= lagen) {
                _laag = 0;
                _dier += 1;
            }
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
        var top = 58.0 / 260;
        EbbZee.zeeBanden(dc, d, [top, top + 0.45 * (1 - top), top + 0.72 * (1 - top)] as Array<Float>, [1, 2, 3] as Array<Number>, 0.010, 0.4);
        // Fontein: drie belletjes onder de kamlijn, boven de walvis.
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(d / 260 > 1 ? d / 260 : 1);
        var bel = [[0, 71, 3], [-6, 64, 2], [5, 62, 2]] as Array<Array<Number> >;
        for (var i = 0; i < bel.size(); i += 1) {
            var r = px(d, bel[i][2]);
            dc.drawCircle(d / 2 + px(d, bel[i][0]), px(d, bel[i][1]), r < 2 ? 2 : r);
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
        tekst(dc, d, 18, EbbTeken.fS(), "sea complete", EbbTeken.LICHT);
        tekst(dc, d, 206, EbbTeken.fX(), "24 of 24 friends", EbbTeken.SCHUIM);
        tekst(dc, d, 226, EbbTeken.fX(), reeks + (reeks == 1 ? " week in a row" : " weeks in a row"), EbbTeken.SCHUIM);
    }
}
