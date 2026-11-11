import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Mila blad v10 punt 1: "sea complete" als groepsfoto. Hoge zee (kamlijn 58/260), de walvis groot in het midden met
// een fontein van drie belletjes onder de kamlijn, de 23 andere vrienden in rijen eromheen (4 naast de walvis, dan
// 7, 6 en 6), op volgorde van het schema. "sea complete" bovenaan, "24 of 24 friends" en de reeks onderaan. Geen tijden.
// Watchdog: alle 24 dieren komen één keer in één doorzichtig plaatje; per beurt één laag, op AMOLED vanaf 390 px drie
// (lokaal gemeten: een tijdsbudget van 30 ms gaf op FR255 toch de watchdog). Keuring bouw 5 punt 3: de walvis eerst, en
// elke beurt wordt geplakt wat er al staat, zodat het feest meteen zichtbaar is en aangroeit. Keuring bouw 6 punt 3:
// alleen afgemaakte dieren komen in het plaatje (zie verder). Bij verlaten laat los() het plaatje los.
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
    var _gemeld as Boolean = false;
    var _los as EbbDierPlaatje or Null = null;   // het dier dat nu los wordt opgebouwd
    var _x0 as Number = 0;     // linksboven van het plaatje op het scherm
    var _y0 as Number = 0;
    var _mis as Number = 0;    // hoe vaak het plaatje niet te krijgen was (graphics pool vol); na 3 keer stoppen we met proberen

    // Plek op het scherm en maat van volgnummer k: [x, y, maat]. Maat vrienden floor(11 D / 260), onder 250 px één
    // kleiner; walvis round(32 D / 260).
    function plek(d as Number, k as Number) as Array<Number> {
        if (k == WALVIS) {
            return [d / 2, EbbTeken.px(d, 100), EbbTeken.px(d, 32)] as Array<Number>;
        }
        var m = 11 * d / 260;
        m = d < 250 ? m - 1 : m;
        return [d / 2 + EbbTeken.px(d, PLEK[k][0]), EbbTeken.px(d, PLEK[k][1]), m] as Array<Number>;
    }

    function maak(d as Number) as Void {
        _d = d;
        _dier = 0;
        _los = null;
        _gemeld = false;
        // Plaatje van x 14 tot 246 en y 62 tot 206 (in 1/260 D): alle dieren met stickerrand, binnen 0,85 R.
        _x0 = EbbTeken.px(d, 14);
        _y0 = EbbTeken.px(d, 62);
        _ref = Graphics.createBufferedBitmap({:width => EbbTeken.px(d, 232), :height => EbbTeken.px(d, 144)});
        // Codelezing hoofdchat 11 nov: is de graphics pool vol, dan geeft get() null. Niet crashen: zonder plaatje verder.
        var bb = (_ref as Graphics.BufferedBitmapReference).get();
        if (bb == null) {
            _ref = null;
            _mis += 1;
            System.println("SEA plaatje niet gekregen, poging " + _mis);
            return;
        }
        var dc = (bb as Graphics.BufferedBitmap).getDc();
        dc.setColor(Graphics.COLOR_TRANSPARENT, Graphics.COLOR_TRANSPARENT);
        dc.clear();
    }

    // Eén laag erbij (drie op AMOLED vanaf 390 px); true als alle 24 dieren erin staan.
    // Keuring bouw 6 punt 3: een dier wordt eerst los opgebouwd in een eigen EbbDierPlaatje en pas als het af is in de
    // groepsfoto geplakt. Zo staat er nooit een half dier (de witte halve krab op Venu 3S) en groeit de foto per dier.
    function verder() as Boolean {
        var bb = _ref != null ? (_ref as Graphics.BufferedBitmapReference).get() : null;
        if (bb == null) {
            // Keuring bouw 7 punt 7: het systeem gaf het plaatje vrij; opnieuw maken en van voren af aan opbouwen.
            // Na drie mislukte pogingen is het scherm "klaar" zonder groepsfoto (tekst en zee staan er wel), zodat het
            // horloge niet eindeloos blijft hertekenen.
            if (_mis >= 3) {
                return true;
            }
            maak(_d);
            bb = _ref != null ? (_ref as Graphics.BufferedBitmapReference).get() : null;
            if (bb == null) {
                return false;
            }
        }
        var dc = (bb as Graphics.BufferedBitmap).getDc();
        var n = (EbbTeken.amoled() && _d >= 390) ? 3 : 1;
        while (_dier <= WALVIS && n > 0) {
            n -= 1;
            // Volgorde: eerst de walvis (23), dan 0 tot 22.
            var k = (_dier + WALVIS) % (WALVIS + 1);
            var p = plek(_d, k);
            if (_los == null) {
                _los = new EbbDierPlaatje(k, p[2], EbbDierPlaatje.GEVONDEN);
            }
            var bezig = _los as EbbDierPlaatje;
            if (bezig.verder()) {
                bezig.plak(dc, p[0] - _x0, p[1] - _y0);
                _los = null;
                _dier += 1;
            }
        }
        if (_dier > WALVIS && !_gemeld) {
            // Keuring bouw 6 punt 3: geheugen meten met het plaatje erbij (de plaatjes zelf staan in de graphics pool,
            // die meet de app niet; een tekort daar geeft een crash die de stap "Geen crash" vangt).
            _gemeld = true;
            var st = System.getSystemStats();
            System.println("GEHEUGEN SEA klaar " + st.usedMemory + " van " + st.totalMemory + " = " + (st.usedMemory.toLong() * 100 / st.totalMemory) + "%");
        }
        return _dier > WALVIS;
    }

    // Plaatje loslaten als het scherm weggaat (geheugen voor de rest van de app).
    function los() as Void {
        _ref = null;
        _los = null;
        _d = 0;
        _mis = 0;
    }

    function teken(dc as Graphics.Dc, d as Number, reeks as Number) as Void {
        if (_d != d) {
            _mis = 0;
            maak(d);
        }
        var top = 58.0 / 260;
        EbbZee.zeeBanden(dc, d, [top, top + 0.45 * (1 - top), top + 0.72 * (1 - top)] as Array<Float>, [1, 2, 3] as Array<Number>, 0.010, 0.4);
        // Fontein: drie belletjes onder de kamlijn, boven de walvis.
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.setPenWidth(d / 260 > 1 ? d / 260 : 1);
        var bel = [[0, 71, 3], [-6, 64, 2], [5, 62, 2]] as Array<Array<Number> >;
        for (var i = 0; i < bel.size(); i += 1) {
            var r = EbbTeken.px(d, bel[i][2]);
            dc.drawCircle(d / 2 + EbbTeken.px(d, bel[i][0]), EbbTeken.px(d, bel[i][1]), r < 2 ? 2 : r);
        }
        dc.setPenWidth(1);
        var klaar = verder();
        var bb = _ref != null ? (_ref as Graphics.BufferedBitmapReference).get() : null;
        if (bb != null) {
            dc.drawBitmap(_x0, _y0, bb as Graphics.BufferedBitmap);
        }
        if (!klaar) {
            WatchUi.requestUpdate();
        }
        EbbTeken.tekst260(dc, d, 18, EbbTeken.fS(), "sea complete", EbbTeken.LICHT);
        EbbTeken.tekst260(dc, d, 206, EbbTeken.fX(), "24 of 24 friends", EbbTeken.SCHUIM);
        EbbTeken.tekst260(dc, d, 226, EbbTeken.fX(), reeks + (reeks == 1 ? " week in a row" : " weeks in a row"), EbbTeken.SCHUIM);
    }
}
