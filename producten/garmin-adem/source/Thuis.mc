import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;

// Het thuiswater (besluit Thijs 12 nov 11:50, stap 4; Bas): dezelfde rustige zee onder water op het startscherm, het
// pauzemenu en de sea log. Alleen: het water (AMOLED verloop in 20 stroken, MIP bij dag het raster van inhouden, bij
// nacht nachtblauw), onderaan een zandbodem, hooguit een pluk zeegras links en rechts en een paar belletjes.
// Rustig: zeegras en belletjes worden alleen getekend als ze 6/260 van elk tekstvak en 10/260 van de ronde rand
// blijven; anders korter of weg. Het scherm geeft zijn tekstvakken mee (ThuisSchermen.mc voor de sea log).
// Elke kleur gaat bij nacht door de nachtregel (EbbNacht), behalve het nachtwater dat al een nachtkleur is.
// Geen groot plaatje: alles wordt elke beurt direct getekend en is licht (MIP: één strookje raster, tien keer geplakt).
module EbbThuis {
    const MENU = 0;
    const PAUZE = 1;
    const SEALOG = 2;
    // Water van inhouden (KrabV2Lagen.onder): boven en onder, dag en nacht (AMOLED); raster op MIP bij dag.
    const WATER = [0x00698C, 0x00163C, 0x000069, 0x000016] as Array<Number>;
    const RASTER = [0x005555, 0x0055AA] as Array<Number>;
    const ZAND = 0xFFFFAA;
    const GRAS = 0x00AA55;
    const BEL = 0xAAFFFF;
    // Belletjes per scherm: x, y, straal in 1/260, drie per scherm, naast de knoppen en nooit bij tekst.
    const BELLEN = [30, 134, 3, 37, 118, 2, 227, 126, 3,
        24, 142, 3, 220, 150, 3, 227, 134, 2,
        36, 196, 3, 226, 192, 3, 219, 206, 2] as Array<Number>;
    // Drie sprieten per pluk: voet opzij, hoogte en uitslag van de top, in 1/260.
    const SPRIET = [-7, 22, -8, 0, 30, 4, 7, 17, 8] as Array<Number>;
    const STROOK_H = 16;

    // Plaatjesbouw: 0 dag, 1 nacht; -1 is de klok van het horloge (nacht van 21 tot 6 uur, EbbLucht).
    var proefNacht as Number = -1;
    var _strook as Graphics.BufferedBitmapReference or Null = null;
    var _strookW as Number = 0;
    var _gemeld as Number = -1;

    function nacht() as Boolean {
        return proefNacht >= 0 ? proefNacht == 1 : EbbLucht.deelNu() == 3;
    }

    // De ene plek waar het thuiswater een kleur kiest: bij nacht door de nachtregel.
    function kleur(dc as Graphics.Dc, k as Number, n as Boolean, am as Boolean) as Void {
        k = n ? EbbNacht.k(k, am) : k;
        dc.setColor(k, Graphics.COLOR_TRANSPARENT);
    }

    // Het strookje raster voor MIP bij dag (w breed, 16 hoog). Geeft null in de beurt waarin het gemaakt wordt.
    function strook(w as Number) as Graphics.BufferedBitmap or Null {
        var ref = _strook;
        if (ref != null && _strookW == w) {
            var oud = ref.get();
            if (oud != null) {
                return oud as Graphics.BufferedBitmap;
            }
        }
        _strook = null;
        try {
            var smalRef = Graphics.createBufferedBitmap({:width => w, :height => 2});
            var smal = smalRef.get();
            var grootRef = Graphics.createBufferedBitmap({:width => w, :height => STROOK_H});
            var groot = grootRef.get();
            if (smal == null || groot == null) {
                return null;
            }
            var t = (smal as Graphics.BufferedBitmap).getDc();
            t.setColor(RASTER[0], RASTER[0]);
            t.clear();
            t.setColor(RASTER[1], RASTER[1]);
            for (var x = 0; x < w; x += 2) {
                t.drawPoint(x, 0);
                t.drawPoint(x + 1, 1);
            }
            var g = (groot as Graphics.BufferedBitmap).getDc();
            for (var y = 0; y < STROOK_H; y += 2) {
                g.drawBitmap(0, y, smal as Graphics.BufferedBitmap);
            }
            _strook = grootRef;
            _strookW = w;
        } catch (e instanceof Lang.Exception) {
            System.println("THUIS strook mislukt");
        }
        return null;
    }

    // Is de rechthoek (px) vrij: 6/260 van elk tekstvak en 10/260 binnen de ronde rand?
    function vrij(vakken as Array<Number>, x0 as Number, y0 as Number, x1 as Number, y1 as Number, d as Number) as Boolean {
        var m = EbbTeken.px(d, 6);
        for (var i = 0; i + 3 < vakken.size(); i += 4) {
            if (x0 < vakken[i + 2] + m && x1 > vakken[i] - m && y0 < vakken[i + 3] + m && y1 > vakken[i + 1] - m) {
                return false;
            }
        }
        var r = d / 2 - EbbTeken.px(d, 10);
        var c = d / 2;
        var dx = (c - x0) > (x1 - c) ? (c - x0) : (x1 - c);
        var dy = (c - y0) > (y1 - c) ? (c - y0) : (y1 - c);
        return dx * dx + dy * dy <= r * r;
    }

    // Tekent het thuiswater over het hele scherm. zand: bovenkant van de zandbodem in px (onder alle tekst).
    // vakken: de tekstvakken en knoppen van het scherm in px, x0, y0, x1, y1 om en om. soort: MENU, PAUZE of SEALOG.
    // Geeft false als er nog een beurt nodig is (MIP: het strookje raster is net gemaakt, de versiering volgt).
    function teken(dc as Graphics.Dc, d as Number, zand as Number, vakken as Array<Number>, soort as Number) as Boolean {
        var t0 = System.getTimer();
        var w = dc.getWidth();
        var h = dc.getHeight();
        var am = EbbTeken.amoled();
        var n = nacht();
        var af = true;
        if (am) {
            var stroken = 20;
            for (var i = 0; i < stroken; i += 1) {
                var a = h * i / stroken;
                var k = EbbTeken.meng(WATER[n ? 2 : 0], WATER[n ? 3 : 1], i / (stroken - 1.0));
                dc.setColor(k, k);
                dc.fillRectangle(0, a, w, h * (i + 1) / stroken - a + 1);
            }
        } else if (n) {
            dc.setColor(EbbTeken.NACHT, EbbTeken.NACHT);
            dc.fillRectangle(0, 0, w, h);
        } else {
            dc.setColor(RASTER[1], RASTER[1]);
            dc.fillRectangle(0, 0, w, h);
            var s = strook(w);
            if (s != null) {
                for (var y = 0; y < h; y += STROOK_H) {
                    dc.drawBitmap(0, y, s);
                }
            } else {
                af = (_strook == null);
            }
        }
        // Zandbodem: flauwe bolling, in het midden het hoogst (op zand), loopt door de rand (bodem mag dat).
        if (zand < h - 2) {
            var pts = [] as Array<[Numeric, Numeric]>;
            for (var i = 0; i <= 13; i += 1) {
                pts.add([w * i / 13, zand + (EbbTeken.px(d, 3) * (1.0 - Math.cos((i - 6.5) * 0.45))).toNumber()]);
            }
            pts.add([w, h]);
            pts.add([0, h]);
            kleur(dc, ZAND, n, am);
            dc.fillPolygon(pts);
        }
        if (!af) {
            return false;
        }
        var gras = 0;
        var bellen = 0;
        // Zeegras: een pluk links en rechts, geworteld in het zand; past hij niet, dan korter, anders weg.
        var voet = zand + EbbTeken.px(d, 3);
        var breed = EbbTeken.px(d, 13);
        var dik = EbbTeken.px(d, 3);
        for (var kant = -1; kant <= 1; kant += 2) {
            var gx = d / 2 + kant * EbbTeken.px(d, 56);
            for (var poging = 0; poging < 2; poging += 1) {
                var pct = (poging == 0) ? 100 : 65;
                var top = zand - EbbTeken.px(d, 30) * pct / 100;
                if (!vrij(vakken, gx - breed, top, gx + breed, voet, d)) {
                    continue;
                }
                kleur(dc, GRAS, n, am);
                dc.setPenWidth(dik < 2 ? 2 : dik);
                for (var b = 0; b < 3; b += 1) {
                    var xa = gx + kant * EbbTeken.px(d, SPRIET[3 * b]);
                    var ya = voet;
                    var hoog = EbbTeken.px(d, SPRIET[3 * b + 1]) * pct / 100;
                    for (var t = 1; t <= 5; t += 1) {
                        var xb = gx + kant * (EbbTeken.px(d, SPRIET[3 * b]) + EbbTeken.px(d, SPRIET[3 * b + 2]) * t * t / 25);
                        var yb = voet - EbbTeken.px(d, 3) - hoog * t / 5;
                        dc.drawLine(xa, ya, xb, yb);
                        xa = xb;
                        ya = yb;
                    }
                }
                dc.setPenWidth(1);
                gras += 1;
                break;
            }
        }
        // Belletjes: drie per scherm, alleen waar niets staat.
        kleur(dc, BEL, n, am);
        dc.setPenWidth(d >= 390 ? 2 : 1);
        for (var i = 0; i < 3; i += 1) {
            var bx = EbbTeken.px(d, BELLEN[9 * soort + 3 * i]);
            var by = EbbTeken.px(d, BELLEN[9 * soort + 3 * i + 1]);
            var br = EbbTeken.px(d, BELLEN[9 * soort + 3 * i + 2]);
            br = br < 2 ? 2 : br;
            if (by + br < zand && vrij(vakken, bx - br, by - br, bx + br, by + br, d)) {
                dc.drawCircle(bx, by, br);
                bellen += 1;
            }
        }
        dc.setPenWidth(1);
        if (EbbBouw.PLAATJE && _gemeld != soort * 2 + (n ? 1 : 0)) {
            _gemeld = soort * 2 + (n ? 1 : 0);
            System.println("THUIS scherm " + soort + (n ? " nacht " : " dag ") + d + (am ? " amoled" : " mip") + " zand " + zand + " gras " + gras + " van 2, bellen " + bellen + " van 3, beurt " + (System.getTimer() - t0) + " ms");
        }
        return true;
    }
}
