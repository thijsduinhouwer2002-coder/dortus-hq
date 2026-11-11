import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Besluit Thijs 11 nov 23:13 NL: elk dier zijn eigen stukje zee. Dit bestand is het mechanisme (bericht hoofdchat
// 23:20 punt 2), zie platformen/garmin/werelden-techniek-2026-11-11.md op main en REGELS.md punt 7.
// De wereld is een strook onderin (volle breedte, 0,40 D hoog), één keer opgebouwd in een eigen plaatje, één laag
// per beurt (tegen de watchdog, zoals EbbDierPlaatje), daarna alleen plakken. Hoogstens één wereld tegelijk.
// Lukt het plaatje niet (voorraad van het horloge vol), dan tekent het scherm gewoon de zee zonder wereld.

// PROEF: drie werelden van Gijs om de techniek te bewijzen (geen ontwerp). Mila's werelden vervangen deze.
// Een laag is [kleur, soort, vormen]: soort 0 = veelhoeken (per veelhoek x, y, x, y, ...), soort 1 = cirkels
// (x, y, straal, ...). Maten in 1/100 D: x 0 tot 100, y 0 (bovenkant strook) tot 40. Alleen MIP-kleuren.
module EbbWereldData {
    const HOOG = 40;

    function lagen(dier as Number) as Array<Array> or Null {
        var zand = [0xFFAA55, 0, [[0, 31, 30, 29, 50, 30, 70, 29, 100, 31, 100, 40, 0, 40]]] as Array;
        if (dier == 3) {
            // Schildpad: zeegras links en rechts.
            return [zand,
                [0x00AA55, 0, [[17, 31, 19, 31, 14, 10], [20, 31, 22, 31, 20, 14], [14, 31, 16, 31, 9, 16],
                    [83, 31, 81, 31, 86, 10], [80, 31, 78, 31, 80, 14], [86, 31, 84, 31, 91, 16]]] as Array,
                [0x005500, 0, [[18, 31, 20, 31, 17, 18], [82, 31, 80, 31, 83, 18]]] as Array] as Array<Array>;
        }
        if (dier == 4) {
            // Krab: rotsen en kiezels.
            return [zand,
                [0x555555, 0, [[7, 31, 9, 21, 14, 16, 20, 18, 23, 25, 22, 31], [78, 31, 77, 24, 81, 17, 87, 15, 92, 22, 93, 31]]] as Array,
                [0xAAAAAA, 0, [[10, 22, 14, 17, 18, 19, 13, 23], [80, 23, 83, 18, 87, 17, 84, 23]]] as Array,
                [0xAA5500, 1, [40, 33, 1, 58, 34, 1, 50, 36, 1]] as Array] as Array<Array>;
        }
        if (dier == 7) {
            // Clownvis: anemonen.
            return [zand,
                [0xAA0055, 0, [[14, 31, 16, 31, 13, 17, 12, 17], [17, 31, 19, 31, 18, 14, 17, 14], [20, 31, 22, 31, 23, 17, 22, 17],
                    [86, 31, 84, 31, 87, 17, 88, 17], [83, 31, 81, 31, 82, 14, 83, 14], [80, 31, 78, 31, 77, 17, 78, 17]]] as Array,
                [0xFF55AA, 1, [12, 16, 2, 17, 13, 2, 23, 16, 2, 88, 16, 2, 83, 13, 2, 77, 16, 2]] as Array] as Array<Array>;
        }
        return null;
    }
}

class EbbWereldPlaatje {
    var dier as Number;
    var d as Number;
    var hoog as Number;
    var stap as Number = 0;
    private var _lagen as Array<Array> or Null = null;
    private var _ref as Graphics.BufferedBitmapReference or Null = null;

    function initialize(i as Number, maat as Number) {
        dier = i;
        d = maat;
        hoog = maat * EbbWereldData.HOOG / 100;
        var l = EbbWereldData.lagen(i);
        if (l == null) {
            return;
        }
        try {
            var ref = Graphics.createBufferedBitmap({:width => maat, :height => hoog});
            var bb = ref.get();
            if (bb != null) {
                var dc = (bb as Graphics.BufferedBitmap).getDc();
                dc.setColor(Graphics.COLOR_TRANSPARENT, Graphics.COLOR_TRANSPARENT);
                dc.clear();
                _ref = ref;
                _lagen = l;
            }
        } catch (e instanceof Lang.Exception) {
            _ref = null;
        }
        if (_ref == null) {
            // Keuring bouw 8 punt 7: een mislukte poging staat in het log, met de maat.
            System.println("WERELD plaatje mislukt " + maat + " x " + hoog);
        }
    }

    // Wordt er nog gebouwd? Nee als dit dier geen wereld heeft of het plaatje niet lukte.
    function bezig() as Boolean {
        return _ref != null && _lagen != null && stap < (_lagen as Array<Array>).size();
    }

    // Eén laag verder. Geeft true als de wereld af is.
    function verder() as Boolean {
        if (_ref == null || _lagen == null) {
            return false;
        }
        var lagen = _lagen as Array<Array>;
        if (stap >= lagen.size()) {
            return true;
        }
        var bb = (_ref as Graphics.BufferedBitmapReference).get();
        if (bb == null) {
            return false;
        }
        var dc = (bb as Graphics.BufferedBitmap).getDc();
        var laag = lagen[stap] as Array;
        dc.setColor(laag[0] as Number, Graphics.COLOR_TRANSPARENT);
        if ((laag[1] as Number) == 0) {
            var vormen = laag[2] as Array<Array>;
            for (var v = 0; v < vormen.size(); v += 1) {
                var p = vormen[v] as Array<Number>;
                var pts = [] as Array<[Numeric, Numeric]>;
                for (var j = 0; j + 1 < p.size(); j += 2) {
                    pts.add([p[j] * d / 100, p[j + 1] * d / 100]);
                }
                dc.fillPolygon(pts);
            }
        } else {
            var c = laag[2] as Array<Number>;
            for (var n = 0; n + 2 < c.size(); n += 3) {
                var r = c[n + 2] * d / 100;
                dc.fillCircle(c[n] * d / 100, c[n + 1] * d / 100, r < 1 ? 1 : r);
            }
        }
        stap += 1;
        if (stap >= lagen.size()) {
            var st = System.getSystemStats();
            System.println("GEHEUGEN WERELD dier " + dier + " plaatje " + d + " x " + hoog + " lagen " + stap + " gebruikt " + st.usedMemory + " van " + st.totalMemory + " = " + (st.usedMemory.toLong() * 100 / st.totalMemory) + "%");
            return true;
        }
        return false;
    }

    function plak(dc as Graphics.Dc) as Void {
        var bb = (_ref != null) ? (_ref as Graphics.BufferedBitmapReference).get() : null;
        if (bb != null) {
            dc.drawBitmap((dc.getWidth() - d) / 2, d - hoog, bb as Graphics.BufferedBitmap);
        }
    }
}

module EbbWereld {
    // Alleen aan in de proefscènes van de plaatjesbouw, tot Mila's werelden gekeurd zijn.
    var proef as Boolean = false;
    var _p as EbbWereldPlaatje or Null = null;

    // Tekent de wereld van dit dier onderin. Geeft true als hij er staat; anders staat er alleen de zee.
    function teken(dc as Graphics.Dc, dier as Number, d as Number) as Boolean {
        if (!proef || dier < 0) {
            return false;
        }
        if (_p == null || (_p as EbbWereldPlaatje).dier != dier || (_p as EbbWereldPlaatje).d != d) {
            _p = new EbbWereldPlaatje(dier, d);
        }
        var p = _p as EbbWereldPlaatje;
        if (p.verder()) {
            p.plak(dc);
            return true;
        }
        if (p.bezig()) {
            WatchUi.requestUpdate();
        }
        return false;
    }

    function los() as Void {
        _p = null;
    }
}
