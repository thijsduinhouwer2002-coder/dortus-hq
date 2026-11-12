import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;

// PROEF (bericht hoofdchat 12 nov 02:30 NL): de krabwereld v2 van Mila onder water op het inhoudscherm, om te meten
// wat het horloge aankan. Vormen en maten uit bron/krab-v2-vormen.json (gemaakt uit haar werelden_v2.py), in 1/260 D.
// Alles wordt elke beurt direct getekend (geen plaatje): ±50 tekenopdrachten, ±110 punten in veelhoeken.
// Alleen aan in de proefscènes 51 en 52. Niets hangt af van de inhoudtijd, behalve de cijfers zelf.
module EbbWereld2 {
    var proef as Boolean = false;
    var nacht as Boolean = false;
    var _gemeld as Boolean = false;

    // Zool van de teenslipper in tienden (hak op 0,0; neus op x 62), 30 punten, hoogstens 0,48 naast Mila's omtrek.
    const ZOOL = [-130, 0, -111, -55, -91, -74, -72, -87, -32, -101, -13, -103, 7, -103, 260, -70, 494, -119, 513, -120,
        552, -112, 572, -105, 592, -95, 611, -81, 630, -59, 650, 0, 630, 59, 611, 81, 592, 95, 572, 105, 552, 112, 513, 120,
        494, 119, 260, 70, 7, 103, -13, 103, -32, 101, -72, 87, -91, 74, -111, 55] as Array<Number>;
    const TENTAKELS = [18, 12, 158, 26, 22, 150, 36, 36, 146, 46, 50, 150, 54, 60, 160] as Array<Number>;
    const VERDER = [40, 176, 60, 26, 150, 186, 70, 20, 240, 168, 46, 30] as Array<Number>;
    const VER = [10, 192, 52, 36, 78, 208, 46, 20, 186, 206, 50, 20, 252, 186, 50, 40] as Array<Number>;
    const STOF_DAG = [24, 120, 36, 146, 230, 112, 242, 140, 214, 152, 18, 160] as Array<Number>;
    const STOF_NACHT = [22, 112, 34, 138, 16, 158, 48, 120, 232, 104, 244, 132, 220, 146, 208, 118, 60, 150, 196, 156, 30, 92, 236, 84] as Array<Number>;
    const STROKEN = 30;

    function p(d as Number, v as Numeric) as Number {
        return (v * d / 260.0 + 0.5).toNumber();
    }

    function rond(dc as Graphics.Dc, d as Number, cx as Numeric, cy as Numeric, rx as Numeric, ry as Numeric, kleur as Number) as Void {
        dc.setColor(kleur, kleur);
        dc.fillEllipse(p(d, cx), p(d, cy), p(d, rx), p(d, ry));
    }

    // Water onder water. MIP: twee vlakken (overdag petrol boven en indigo vanaf 150, 's nachts alles indigo).
    // AMOLED: verloop in 30 stroken, met daarin de lichtbundel in twee stappen (geen vervaging mogelijk).
    function water(dc as Graphics.Dc, d as Number) as Void {
        var w = dc.getWidth();
        if (!EbbTeken.amoled()) {
            var boven = nacht ? 0x000055 : 0x005555;
            dc.setColor(boven, boven);
            dc.clear();
            if (!nacht) {
                EbbZee.golf(dc, d, 150.0 / 260, d * 2.5 / 260, 0x000055, 0.0, false);
            }
        } else {
            var top = nacht ? 0x000069 : 0x00698C;
            var bodem = nacht ? 0x000016 : 0x00163C;
            var licht = nacht ? 0xAAAAFF : 0x55FFFF;
            var sh = d / STROKEN + 1;
            for (var i = 0; i < STROKEN; i += 1) {
                var f = i.toFloat() / (STROKEN - 1);
                var k = EbbTeken.meng(top, bodem, f);
                var y = d * i / STROKEN;
                dc.setColor(k, k);
                dc.fillRectangle(0, y, w, sh);
                // Bundel van (118, 0) naar de held (112, 236): boven 52 breed, onder 96; naar beneden zwakker.
                var yy = y * 260 / d;
                if (yy < 236) {
                    var mid = 118 - 6 * yy / 236;
                    var half = 26 + 22 * yy / 236;
                    var sterk = (nacht ? 0.10 : 0.16) * (1.0 - yy / 300.0);
                    var k1 = EbbTeken.meng(k, licht, sterk / 2);
                    dc.setColor(k1, k1);
                    dc.fillRectangle(p(d, mid - half), y, p(d, 2 * half), sh);
                    var k2 = EbbTeken.meng(k, licht, sterk);
                    dc.setColor(k2, k2);
                    dc.fillRectangle(p(d, mid - half * 0.6), y, p(d, 1.2 * half), sh);
                }
            }
        }
        // Oppervlak: lichte golvende rand bovenin.
        var rand = nacht ? 0x5555FF : 0x0055FF;
        var pts = [[0, 0], [d, 0]] as Array<[Numeric, Numeric]>;
        for (var x = 260; x >= 0; x -= 13) {
            pts.add([p(d, x), p(d, 7 + 2.5 * Math.sin(x / 260.0 * 2 * Math.PI * 5))]);
        }
        dc.setColor(rand, rand);
        dc.fillPolygon(pts);
    }

    // Ver weg de donkere ruggen, zand, twee rotsen met anemoon en zeester, lichtjes opzij.
    function wereld(dc as Graphics.Dc, d as Number) as Void {
        var verder = nacht ? 0x000055 : 0x0055AA;
        var ver = nacht ? 0x0000AA : 0x000055;
        if (EbbTeken.amoled()) {
            verder = nacht ? 0x000052 : 0x004B69;
            ver = nacht ? 0x00003C : 0x001E46;
        }
        for (var i = 0; i < VERDER.size(); i += 4) {
            rond(dc, d, VERDER[i], VERDER[i + 1], VERDER[i + 2], VERDER[i + 3], verder);
        }
        for (var i = 0; i < VER.size(); i += 4) {
            rond(dc, d, VER[i], VER[i + 1], VER[i + 2], VER[i + 3], ver);
        }
        rond(dc, d, 130, 276, 170, 54, 0xAAAA55);
        rond(dc, d, 130, 278, 160, 52, 0xFFFFAA);
        // Rots links met de anemoon: vijf dikke tentakels met ronde roze toppen.
        rond(dc, d, 36, 202, 36.2, 28.2, 0xAAAAFF);
        rond(dc, d, 36, 202, 34, 26, 0x5555AA);
        rond(dc, d, 15, 188, 7.5, 4.2, 0xAAAAFF);
        for (var laag = 0; laag < 2; laag += 1) {
            for (var i = 0; i < TENTAKELS.size(); i += 3) {
                var x1 = p(d, TENTAKELS[i + 1]);
                var y1 = p(d, TENTAKELS[i + 2]);
                dc.setColor(laag == 0 ? 0xFFFFFF : 0xAA55FF, Graphics.COLOR_TRANSPARENT);
                dc.setPenWidth(p(d, laag == 0 ? 8.6 : 5.6));
                dc.drawLine(p(d, TENTAKELS[i]), p(d, 180), x1, y1);
                dc.setColor(laag == 0 ? 0xFFFFFF : 0xFF55AA, Graphics.COLOR_TRANSPARENT);
                dc.fillCircle(x1, y1, p(d, laag == 0 ? 4.3 : 3.6));
            }
        }
        dc.setPenWidth(1);
        rond(dc, d, 36, 180, 23.6, 8.6, 0xFFFFFF);
        rond(dc, d, 36, 180, 22, 7, 0xAA55FF);
        // Rots rechts met de zeester.
        rond(dc, d, 222, 210, 32.2, 24.2, 0xAAAAFF);
        rond(dc, d, 222, 210, 30, 22, 0x5555AA);
        rond(dc, d, 203, 198, 6.6, 3.5, 0xAAAAFF);
        ster(dc, d, 218, 197, 12.8, 6.4, 0xFFFFFF);
        ster(dc, d, 218, 197, 11.0, 4.6, 0xFFFF55);
        // Zwevende lichtjes, alleen opzij (nooit achter tekst); 's nachts plankton.
        var stof = nacht ? STOF_NACHT : STOF_DAG;
        var sk = nacht ? 0x55FFAA : 0xAAFFFF;
        dc.setColor(sk, sk);
        var sr = d >= 360 ? 2 : 1;
        for (var i = 0; i < stof.size(); i += 2) {
            dc.fillCircle(p(d, stof[i]), p(d, stof[i + 1]), sr);
        }
    }

    function ster(dc as Graphics.Dc, d as Number, cx as Number, cy as Number, buiten as Float, binnen as Float, kleur as Number) as Void {
        var pts = [] as Array<[Numeric, Numeric]>;
        for (var i = 0; i < 10; i += 1) {
            var a = -Math.PI / 2 + i * Math.PI / 5;
            var r = (i % 2 == 0) ? buiten : binnen;
            pts.add([p(d, cx + r * Math.cos(a)), p(d, cy + r * Math.sin(a))]);
        }
        dc.setColor(kleur, kleur);
        dc.fillPolygon(pts);
    }

    // Punt (x, y) in de maat van de slipper naar het scherm: draaien over hoek (graden), schalen, verschuiven.
    function sl(d as Number, cx as Float, cy as Float, sch as Float, co as Float, si as Float, x as Float, y as Float) as [Numeric, Numeric] {
        return [p(d, cx + (x * co - y * si) * sch), p(d, cy + (x * si + y * co) * sch)];
    }

    // De roze teenslipper met witte rand, glans en teenafdruk. uit: hoeveel de rand buiten de zool steekt (0 voor de zool zelf).
    function slipper(dc as Graphics.Dc, d as Number, cx as Float, cy as Float, sch as Float, hoek as Float) as Void {
        var a = hoek * Math.PI / 180;
        var co = Math.cos(a).toFloat();
        var si = Math.sin(a).toFloat();
        for (var laag = 0; laag < 2; laag += 1) {
            var uit = (laag == 0) ? 2.2 / sch : 0.0;
            var pts = [] as Array<[Numeric, Numeric]>;
            for (var i = 0; i < ZOOL.size(); i += 2) {
                var x = ZOOL[i] / 10.0;
                var y = ZOOL[i + 1] / 10.0;
                if (uit > 0) {
                    // Rand: elk punt van het midden van de zool (27,8; 0) af naar buiten.
                    var dx = x - 27.8;
                    var l = Math.sqrt(dx * dx + y * y).toFloat();
                    l = l < 1.0 ? 1.0 : l;
                    x += dx / l * uit;
                    y += y / l * uit;
                }
                pts.add(sl(d, cx, cy, sch, co, si, x, y));
            }
            dc.setColor(laag == 0 ? 0xFFFFFF : 0xFF55AA, laag == 0 ? 0xFFFFFF : 0xFF55AA);
            dc.fillPolygon(pts);
        }
        dc.setColor(0xFFAAFF, 0xFFAAFF);
        dc.fillPolygon([sl(d, cx, cy, sch, co, si, 30.0, -4.5), sl(d, cx, cy, sch, co, si, 46.0, -6.0), sl(d, cx, cy, sch, co, si, 58.0, -4.0), sl(d, cx, cy, sch, co, si, 46.0, -3.0)] as Array<[Numeric, Numeric]>);
        dc.setColor(0xAA0055, 0xAA0055);
        dc.fillPolygon([sl(d, cx, cy, sch, co, si, 52.0, -1.0), sl(d, cx, cy, sch, co, si, 57.0, -3.5), sl(d, cx, cy, sch, co, si, 61.0, -1.0), sl(d, cx, cy, sch, co, si, 57.0, 1.5)] as Array<[Numeric, Numeric]>);
    }

    // Het witte V-bandje, over de krab heen: van het teenpaaltje naar beide kanten van de taille.
    function bandje(dc as Graphics.Dc, d as Number, cx as Float, cy as Float, sch as Float, hoek as Float) as Void {
        var a = hoek * Math.PI / 180;
        var co = Math.cos(a).toFloat();
        var si = Math.sin(a).toFloat();
        var paal = sl(d, cx, cy, sch, co, si, 50.0, -1.0 - 5.0);
        var kanten = [sl(d, cx, cy, sch, co, si, 24.0, -9.5), sl(d, cx, cy, sch, co, si, 26.0, 9.0)] as Array<[Numeric, Numeric]>;
        dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
        var dik = p(d, 5 * sch);
        dc.setPenWidth(dik < 2 ? 2 : dik);
        for (var i = 0; i < 2; i += 1) {
            dc.drawLine(kanten[i][0], kanten[i][1], paal[0], paal[1]);
            dc.fillCircle(kanten[i][0], kanten[i][1], p(d, 2.1 * sch));
        }
        dc.setPenWidth(1);
        dc.fillCircle(paal[0], paal[1], p(d, 3 * sch));
    }

    // Het hele inhoudscherm van de proef: water, wereld, slipper, krab (maat 43/260 op 106, 184), bandje, tekst.
    // s is alleen voor de cijfers; de wereld krijgt hem niet.
    function inhoud(dc as Graphics.Dc, d as Number, dier as Number, s as Number, stop as String, ronde as Number) as Void {
        var st0 = System.getTimer();
        water(dc, d);
        wereld(dc, d);
        var maat = 43;
        var sy = 184 + maat * 0.62;
        var sch = maat / 30.0 * 1.3;
        rond(dc, d, 140, sy + 17, 54, 6, 0xAAAA55);
        slipper(dc, d, 100.0, sy.toFloat(), sch.toFloat(), -4.0);
        var af = true;
        if (dier >= 0) {
            af = EbbDierVoorraad.teken(dc, dier, p(d, 106), p(d, 184), p(d, maat), EbbDierPlaatje.GEVONDEN);
        }
        bandje(dc, d, 100.0, sy.toFloat(), sch.toFloat(), -4.0);
        EbbTeken.bellen(dc, d, [[192 / 260.0, 160 / 260.0, 3 / 260.0], [198 / 260.0, 148 / 260.0, 2.2 / 260.0]] as Array<Array<Float> >);
        EbbTeken.tekst260(dc, d, 24, EbbTeken.fS(), "hold", EbbTeken.LICHT);
        EbbTeken.tekst260(dc, d, 48, EbbTeken.fX(), stop, Graphics.COLOR_WHITE);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, p(d, 90), EbbTeken.grootKlein(), (s / 60).toString() + ":" + (s % 60).format("%02d"), Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        EbbTeken.hartRonde(dc, d, p(d, 127), EbbBouw.PLAATJE ? 61 : EbbOpname.hartslag(), ronde);
        if (af && !_gemeld) {
            // Eén keer per start, als het dier er staat: hoe lang één hele tekenbeurt duurt en het geheugen.
            _gemeld = true;
            var st = System.getSystemStats();
            System.println("WERELD2 " + (nacht ? "nacht" : "dag") + " beurt " + (System.getTimer() - st0) + " ms, gebruikt " + st.usedMemory + " van " + st.totalMemory + " = " + (st.usedMemory.toLong() * 100 / st.totalMemory) + "%, geen plaatje (alles direct)");
        }
    }
}
