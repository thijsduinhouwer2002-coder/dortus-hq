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
        } else {
            // Run 134: de zes nieuwe soorten (Mila, ontwerp/garmin/tij/iconen/iconen.mc.txt), elk een paar vlakken.
            var v = vlakken(soort);
            for (var i = 0; i < v.size(); i++) {
                dc.fillPolygon(vlak(v[i], cx, cy, h));
            }
        }
    }

    // De vlakken van een pictogram voor de soorten 3 tot 8 (Veld.mc): vlam (calorieën), trap (trappen), stopwatch
    // (intensiteitsminuten), speld (afstand), accu, thermometer (temperatuur). Een andere soort: lege lijst.
    // Ringen zijn twee halve vlakken, zo is er geen veelhoek met een gat nodig.
    function vlakken(soort as Number) as Array< Array<Number> > {
        if (soort == 3) {
            return [VLAM_0] as Array< Array<Number> >;
        } else if (soort == 4) {
            return [TRAP_0] as Array< Array<Number> >;
        } else if (soort == 5) {
            return [KLOK_0, KLOK_1, KLOK_2, KLOK_3] as Array< Array<Number> >;
        } else if (soort == 6) {
            return [SPELD_0, SPELD_1, SPELD_2] as Array< Array<Number> >;
        } else if (soort == 7) {
            return [ACCU_0, ACCU_1, ACCU_2, ACCU_3, ACCU_4, ACCU_5] as Array< Array<Number> >;
        } else if (soort == 8) {
            return [THERMO_0, THERMO_1] as Array< Array<Number> >;
        }
        return [] as Array< Array<Number> >;
    }

    const VLAM_0 = [10, -50, 30, -22, 38, 6, 34, 30, 18, 46, -12, 48, -30, 38, -38, 18, -38, -4, -34, -22, -20, -4, -10, -24];
    const TRAP_0 = [-50, 48, -50, 18, -18, 18, -18, -14, 14, -14, 14, -46, 48, -46, 48, 48];
    const KLOK_0 = [0, 50, -21, 44, -36, 29, -42, 8, -36, -13, -21, -28, 0, -34, 0, -18, -13, -15, -23, -5, -26, 8, -23, 21, -13, 31, 0, 34];
    const KLOK_1 = [0, -34, 21, -28, 36, -13, 42, 8, 36, 29, 21, 44, 0, 50, 0, 34, 13, 31, 23, 21, 26, 8, 23, -5, 13, -15, 0, -18];
    const KLOK_2 = [0, 8, 0, -19, 10, -17, 19, -11, 25, -2, 27, 8];
    const KLOK_3 = [-10, -50, 10, -50, 10, -38, -10, -38];
    const SPELD_0 = [0, 18, -17, 13, -29, 1, -34, -16, -29, -33, -17, -45, 0, -50, 0, -30, -7, -28, -12, -23, -14, -16, -12, -9, -7, -4, 0, -2];
    const SPELD_1 = [0, -50, 17, -45, 29, -33, 34, -16, 29, 1, 17, 13, 0, 18, 0, -2, 7, -4, 12, -9, 14, -16, 12, -23, 7, -28, 0, -30];
    const SPELD_2 = [-28, 4, 28, 4, 0, 50];
    const ACCU_0 = [-62, -34, 46, -34, 46, -20, -62, -20];
    const ACCU_1 = [-62, 20, 46, 20, 46, 34, -62, 34];
    const ACCU_2 = [-62, -34, -48, -34, -48, 34, -62, 34];
    const ACCU_3 = [32, -34, 46, -34, 46, 34, 32, 34];
    const ACCU_4 = [46, -14, 60, -14, 60, 14, 46, 14];
    const ACCU_5 = [-48, -20, -4, -20, -4, 20, -48, 20];
    const THERMO_0 = [-10, -44, -6, -50, 6, -50, 10, -44, 10, 10, -10, 10];
    const THERMO_1 = [26, 24, 23, 37, 13, 47, 0, 50, -13, 47, -23, 37, -26, 24, -23, 11, -13, 1, 0, -2, 13, 1, 23, 11];

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
