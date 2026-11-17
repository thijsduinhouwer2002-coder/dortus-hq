import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// Maakt de veelhoeken: de heuvellijn (waarden 0 tot 100 als hoogteprofiel) en een golf.
module Teken {
    // Profiel van x0 tot x1, waarde 0 op yB (onder) en 100 op yT (boven), met hoogstens n punten
    // op de lijn plus de twee hoeken onderaan. Minder dan 2 waarden: lege lijst.
    function profiel(waarden as Array<Number>, x0 as Number, x1 as Number, yB as Number, yT as Number, n as Number) as Array<Graphics.Point2D> {
        var p = [] as Array<Graphics.Point2D>;
        var m = waarden.size();
        if (m < n) {
            n = m;
        }
        if (n < 2) {
            return p;
        }
        p.add([x0, yB]);
        for (var i = 0; i < n; i++) {
            var v = waarden[i * (m - 1) / (n - 1)];
            if (v < 0) {
                v = 0;
            }
            if (v > 100) {
                v = 100;
            }
            p.add([x0 + (x1 - x0) * i / (n - 1), yB - (yB - yT) * v / 100]);
        }
        p.add([x1, yB]);
        return p;
    }

    // Golf tussen x0 en x1: bovenkant deint rond yT, onderkant vlak op yB. tik schuift de golf op.
    function golf(x0 as Number, x1 as Number, yT as Number, yB as Number, tik as Number, n as Number) as Array<Graphics.Point2D> {
        var p = [] as Array<Graphics.Point2D>;
        var amp = (yB - yT) / 2;
        p.add([x0, yB]);
        for (var i = 0; i < n; i++) {
            var y = yT + amp + (amp * Math.sin(i * 0.8 + tik * 0.9)).toNumber();
            p.add([x0 + (x1 - x0) * i / (n - 1), y]);
        }
        p.add([x1, yB]);
        return p;
    }
    // Pictogram boven een veld, als vlakken getekend (geen plaatje). soort als in Veld: 0 hart, 1 bliksem
    // (stress), 2 voet (stappen). cx, cy is het midden, h de hoogte in px. h onder 4: niets, te klein om te lezen.
    function icoon(dc as Graphics.Dc, soort as Number, cx as Number, cy as Number, h as Number) as Void {
        if (h < 4) {
            return;
        }
        var r = h / 4;
        var top = cy - h / 2;
        if (soort == 0) {
            dc.fillCircle(cx - r, top + r, r);
            dc.fillCircle(cx + r, top + r, r);
            dc.fillPolygon([[cx - 2 * r, top + r + 1], [cx + 2 * r, top + r + 1], [cx, top + h]] as Array<Graphics.Point2D>);
        } else if (soort == 1) {
            // Bliksem als twee driehoeken die elkaar in het midden raken: zo blijft de knik ook klein scherp.
            var mid = top + h / 2;
            dc.fillPolygon([[cx + r, top], [cx - 2 * r, mid + 1], [cx + 1, mid + 1]] as Array<Graphics.Point2D>);
            dc.fillPolygon([[cx - r, top + h], [cx + 2 * r, mid - 1], [cx - 1, mid - 1]] as Array<Graphics.Point2D>);
        } else if (soort == 2) {
            // Sportschoen van opzij, punt naar rechts (Mila, ontwerp/garmin/reeks/voet_schoen.py): bovenkant en
            // zool als twee vlakken met een donkere naad ertussen. Getallen in honderdsten van h, midden cx, cy.
            dc.fillPolygon(vlak(SCHOEN_BOVEN, cx, cy, h));
            dc.fillPolygon(vlak(SCHOEN_ZOOL, cx, cy, h));
        }
    }

    const SCHOEN_BOVEN = [-50, 16, -52, 0, -44, -44, -12, -44, -5, -20, 22, -10, 42, -2, 54, 8, 56, 16];
    const SCHOEN_ZOOL = [-56, 26, 60, 26, 58, 40, -54, 40];

    // Maakt van een rij x, y in honderdsten van h de punten op het scherm.
    function vlak(rij as Array<Number>, cx as Number, cy as Number, h as Number) as Array<Graphics.Point2D> {
        var p = [] as Array<Graphics.Point2D>;
        for (var i = 0; i + 1 < rij.size(); i += 2) {
            p.add([cx + Math.round(h * rij[i] / 100.0).toNumber(), cy + Math.round(h * rij[i + 1] / 100.0).toNumber()]);
        }
        return p;
    }
}
