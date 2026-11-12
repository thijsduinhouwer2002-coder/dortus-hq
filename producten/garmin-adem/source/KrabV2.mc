import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.WatchUi;

// PROEF (bericht hoofdchat 12 nov 02:30 NL): de krabwereld v2 van Mila (ontwerp/garmin/ebb-werelden-v2.md,
// bron/werelden_v2.py) op vier schermen, dag en nacht, om te meten wat het horloge aankan. Alleen in de plaatjesbouw
// (scène 51 tot 58), niet in de gewone app. Maten in 1/260 D zoals het blad. Wat stil staat komt in vijf beurten in
// één plaatje van het hele scherm; lukt dat plaatje niet, dan tekent hij alles direct en meldt dat in het log.
// scherm: 0 inademen (boven water), 1 inhouden, 2 menu, 3 eindscherm (onder water).
class KrabV2View extends WatchUi.View {
    const STAPPEN = 5;
    var scherm as Number;
    var nacht as Boolean;
    var punten as Number = 0;
    private var _ref as Graphics.BufferedBitmapReference or Null = null;
    private var _stap as Number = 0;
    private var _direct as Boolean = false;
    private var _beurten as Number = 0;
    private var _msMax as Number = 0;
    private var _gemeld as Boolean = false;
    private var _d as Number = 260;
    private var _am as Boolean = false;
    // slipper: hak x, y, schaal, hoek in graden; held: midden van het kader x, y en maat
    private var _sl as Array<Float> = [100.0, 152.0, 1.45, -5.0] as Array<Float>;
    private var _held as Array<Number> = [104, 136, 34] as Array<Number>;

    function initialize(s as Number, n as Boolean) {
        View.initialize();
        scherm = s;
        nacht = n;
        if (s == 1) {
            _sl = [100.0, 210.7, 1.863, -4.0] as Array<Float>;
            _held = [106, 184, 43] as Array<Number>;
        } else if (s == 2) {
            _sl = [100.0, 209.6, 1.647, -4.0] as Array<Float>;
            _held = [106, 186, 38] as Array<Number>;
        } else if (s == 3) {
            _sl = [92.0, 151.0, 1.5, -6.0] as Array<Float>;
            _held = [98, 127, 39] as Array<Number>;
        }
    }

    function q(v as Numeric) as Number {
        return (v * _d / 260.0 + 0.5).toNumber();
    }

    function kleur(dc as Graphics.Dc, k as Number) as Void {
        dc.setColor(k, k);
        if (_am) {
            dc.setFill(Graphics.createColor(255, (k >> 16) & 0xFF, (k >> 8) & 0xFF, k & 0xFF));
        }
    }

    // Doorschijnend vullen kan alleen met setFill (AMOLED); op MIP gebruiken we het niet.
    function glas(dc as Graphics.Dc, a as Number, k as Number) as Void {
        dc.setFill(Graphics.createColor(a, (k >> 16) & 0xFF, (k >> 8) & 0xFF, k & 0xFF));
    }

    function rondje(dc as Graphics.Dc, cx as Numeric, cy as Numeric, rx as Numeric, ry as Numeric, k as Number, rand as Number, glans as Number) as Void {
        if (rand >= 0) {
            kleur(dc, rand);
            dc.fillEllipse(q(cx), q(cy), q(rx + 2.2), q(ry + 2.2));
        }
        kleur(dc, k);
        dc.fillEllipse(q(cx), q(cy), q(rx), q(ry));
        if (glans >= 0) {
            kleur(dc, glans);
            dc.fillEllipse(q(cx - rx * 0.62), q(cy - ry * 0.55), q(rx * 0.22), q(ry * 0.16));
        }
    }

    function vierhoek(dc as Graphics.Dc, x0 as Number, y0 as Number, x1 as Number, y1 as Number, x2 as Number, y2 as Number, x3 as Number, y3 as Number) as Void {
        var pts = [] as Array<[Numeric, Numeric]>;
        pts.add([x0, y0]);
        pts.add([x1, y1]);
        pts.add([x2, y2]);
        pts.add([x3, y3]);
        dc.fillPolygon(pts);
        punten += 4;
    }

    // Golvende rand op hoogte y met het vlak eronder tot onder (n golven over de breedte).
    function golf(dc as Graphics.Dc, y as Numeric, onder as Numeric, k as Number, a as Numeric, n as Number, fase as Numeric) as Void {
        var pts = [] as Array<[Numeric, Numeric]>;
        for (var x = 0; x <= 260; x += 10) {
            pts.add([q(x), q(y + a * Math.sin(x / 260.0 * 2.0 * Math.PI * n + fase))]);
        }
        pts.add([q(260), q(onder)]);
        pts.add([0, q(onder)]);
        kleur(dc, k);
        dc.fillPolygon(pts);
        punten += pts.size();
    }

    // Veelhoek uit punten in 1/260 (x, y om en om), met een rand van dikte rd naar buiten vanaf het midden.
    function blob(dc as Graphics.Dc, p as Array<Float>, k as Number, rand as Number, rd as Float) as Void {
        var n = p.size() / 2;
        var mx = 0.0;
        var my = 0.0;
        for (var i = 0; i < n; i += 1) {
            mx += p[2 * i] / n;
            my += p[2 * i + 1] / n;
        }
        for (var ronde = (rand >= 0 ? 0 : 1); ronde < 2; ronde += 1) {
            var pts = [] as Array<[Numeric, Numeric]>;
            for (var i = 0; i < n; i += 1) {
                var dx = p[2 * i] - mx;
                var dy = p[2 * i + 1] - my;
                var l = Math.sqrt(dx * dx + dy * dy);
                var f = (ronde == 0 && l > 1.0) ? rd / l : 0.0;
                pts.add([q(p[2 * i] + dx * f), q(p[2 * i + 1] + dy * f)]);
            }
            kleur(dc, ronde == 0 ? rand : k);
            dc.fillPolygon(pts);
            punten += n;
        }
    }

    // Punt op de slipper (hak op 0, neus op 62) naar 1/260 van het scherm.
    function rs(x as Float, y as Float) as Array<Float> {
        var a = Math.toRadians(_sl[3]);
        var c = Math.cos(a);
        var s = Math.sin(a);
        return [(_sl[0] + (x * c - y * s) * _sl[2]).toFloat(), (_sl[1] + (x * s + y * c) * _sl[2]).toFloat()] as Array<Float>;
    }

    function halveBreedte(x as Float) as Float {
        if (x < 0.0) {
            return Math.sqrt(169.0 - x * x).toFloat();
        } else if (x < 26.0) {
            return 13.0 - 4.2 * x / 26.0;
        } else if (x <= 50.0) {
            return 8.8 + 6.2 * (x - 26.0) / 24.0;
        }
        var r = 225.0 - (x - 50.0) * (x - 50.0);
        return r > 0.0 ? Math.sqrt(r).toFloat() : 0.0;
    }

    function slipper(dc as Graphics.Dc) as Void {
        var p = [] as Array<Float>;
        for (var i = 0; i <= 14; i += 1) {
            var x = -13.0 + i * 78.0 / 14.0;
            p.addAll(rs(x, -halveBreedte(x) * 0.8));
        }
        for (var i = 14; i >= 0; i -= 1) {
            var x = -13.0 + i * 78.0 / 14.0;
            p.addAll(rs(x, halveBreedte(x) * 0.8));
        }
        blob(dc, p, 0xFF55AA, 0xFFFFFF, 2.2);
        var g = [] as Array<Float>;
        g.addAll(rs(30.0, -4.5)); g.addAll(rs(46.0, -6.0)); g.addAll(rs(58.0, -4.0)); g.addAll(rs(46.0, -3.0));
        blob(dc, g, 0xFFAAFF, -1, 0.0);
        var t = [] as Array<Float>;
        t.addAll(rs(52.0, -1.0)); t.addAll(rs(57.0, -3.5)); t.addAll(rs(61.0, -1.0)); t.addAll(rs(57.0, 1.5));
        blob(dc, t, 0xAA0055, -1, 0.0);
    }

    // V-bandje over de krab heen: van het teenpaaltje naar beide kanten van de taille, wit en dik.
    function bandje(dc as Graphics.Dc) as Void {
        var sch = _sl[2];
        var paal = rs(50.0, -1.0);
        var py = paal[1] - 5.0 * sch;
        var kant = [rs(24.0, -9.5), rs(26.0, 9.0)] as Array<Array<Float> >;
        kleur(dc, 0xFFFFFF);
        var w = q(5.0 * sch);
        dc.setPenWidth(w < 2 ? 2 : w);
        for (var i = 0; i < 2; i += 1) {
            dc.drawLine(q(kant[i][0]), q(kant[i][1]), q(paal[0]), q(py));
            dc.fillCircle(q(kant[i][0]), q(kant[i][1]), q(2.1 * sch));
        }
        dc.fillCircle(q(paal[0]), q(py), q(3.0 * sch));
        dc.setPenWidth(1);
    }

    // Eén beurt van wat stil staat. Boven water: lucht, golven, vonkjes, slipper. Onder water: water, ver en zand,
    // rotsen met anemoon en zeester, lichtjes en bellen, slipper.
    function laag(dc as Graphics.Dc, stap as Number) as Void {
        if (stap == 4) {
            if (scherm == 1 || scherm == 2) {
                if (_am) {
                    glas(dc, 110, 0x5A5028);
                    dc.fillEllipse(q(140), q(_sl[1] + 17), q(56), q(7));
                } else {
                    rondje(dc, 140, _sl[1] + 17, 54, 6, 0xAAAA55, -1, -1);
                }
            }
            slipper(dc);
        } else if (scherm == 0) {
            KrabV2Lagen.boven(self, dc, stap, _am, nacht);
        } else {
            KrabV2Lagen.onder(self, dc, stap, _am, nacht, scherm);
        }
    }

    function tekst(dc as Graphics.Dc) as Void {
        var geel = EbbTeken.LICHT;
        var wit = 0xFFFFFF;
        var d = _d;
        if (scherm == 0) {
            EbbTeken.tekst260(dc, d, 22, EbbTeken.fM(), "breathe in", wit);
            EbbTeken.tekst260(dc, d, 42, EbbTeken.grootKlein(), "12", wit);
            EbbTeken.tekst260(dc, d, 200, EbbTeken.fX(), "round 2 · 18 left", wit);
        } else if (scherm == 1) {
            EbbTeken.tekst260(dc, d, 24, EbbTeken.fM(), "hold", geel);
            EbbTeken.tekst260(dc, d, 48, EbbTeken.fX(), "press START to breathe", wit);
            EbbTeken.tekst260(dc, d, 58, EbbTeken.grootKlein(), "1:45", wit);
            EbbTeken.tekst260(dc, d, 118, EbbTeken.fX(), "61 bpm · round 2", wit);
        } else if (scherm == 2) {
            EbbTeken.tekst260(dc, d, 16, EbbTeken.fM(), "Ebb", geel);
            var namen = ["Rounds", "Calm 4-7-8"] as Array<String>;
            for (var i = 0; i < 2; i += 1) {
                var y = 52 + 34 * i;
                if (_am) {
                    glas(dc, 140, 0x00003C);
                } else {
                    dc.setColor(0x000055, 0x000055);
                }
                dc.fillRoundedRectangle(q(64), q(y), q(132), q(28), q(14));
                dc.setColor(i == 0 ? wit : 0x00AAFF, Graphics.COLOR_TRANSPARENT);
                dc.setPenWidth(q(2.4) < 2 ? 2 : q(2.4));
                dc.drawRoundedRectangle(q(64), q(y), q(132), q(28), q(14));
                dc.setPenWidth(1);
                dc.setColor(wit, Graphics.COLOR_TRANSPARENT);
                dc.drawText(d / 2, q(y + 14), EbbTeken.fS(), namen[i], Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            }
            EbbTeken.tekst260(dc, d, 118, EbbTeken.fX(), "Sea log  ·  Settings  ·  Today", geel);
        } else {
            EbbTeken.tekst260(dc, d, 30, EbbTeken.fM(), "3 rounds done", geel);
            EbbTeken.tekst260(dc, d, 56, EbbTeken.fS(), "1:20   1:45   1:58", wit);
            EbbTeken.tekst260(dc, d, 172, EbbTeken.fM(), "new friend: Crab", geel);
            kleur(dc, EbbTeken.SCHUIM);
            for (var i = -1; i <= 1; i += 1) {
                if (i == 0) {
                    dc.fillCircle(q(130), q(205), q(3.5));
                } else {
                    dc.drawCircle(q(130 + 13 * i), q(205), q(3.5));
                }
            }
        }
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var t0 = System.getTimer();
        _d = dc.getWidth();
        _am = EbbTeken.amoled();
        _beurten += 1;
        if (_ref == null && !_direct) {
            try {
                var ref = Graphics.createBufferedBitmap({:width => _d, :height => _d});
                _ref = ref;
            } catch (e instanceof Lang.Exception) {
                _direct = true;
                System.println("KRABV2 plaatje mislukt " + _d + " x " + _d);
            }
        }
        var bb = (_ref != null) ? (_ref as Graphics.BufferedBitmapReference).get() : null;
        if (bb == null && !_direct) {
            _direct = true;
            System.println("KRABV2 plaatje kwijt bij stap " + _stap);
        }
        var af = true;
        if (bb != null) {
            if (_stap < STAPPEN) {
                laag((bb as Graphics.BufferedBitmap).getDc(), _stap);
                _stap += 1;
            }
            dc.drawBitmap(0, 0, bb as Graphics.BufferedBitmap);
            af = _stap >= STAPPEN;
        } else {
            for (var i = 0; i < STAPPEN; i += 1) {
                laag(dc, i);
            }
        }
        var staat = false;
        if (af) {
            // Midden van het kader van het dier op de plek van het blad (de voorraad plakt op het zwaartepunt).
            var m = q(_held[2]);
            var g = EbbDierMaat.grenzen(4);
            var s = EbbDierData.SCHAAL;
            staat = EbbDierVoorraad.teken(dc, 4, q(_held[0]) - (g[0] + g[1]) * m / (2 * s), q(_held[1]) - (g[2] + g[3]) * m / (2 * s), m, EbbDierPlaatje.GEVONDEN);
            if (staat) {
                bandje(dc);
            }
        } else {
            WatchUi.requestUpdate();
        }
        tekst(dc);
        var ms = System.getTimer() - t0;
        _msMax = ms > _msMax ? ms : _msMax;
        if (staat && !_gemeld) {
            _gemeld = true;
            var st = System.getSystemStats();
            System.println("KRABV2 scherm " + scherm + (nacht ? " nacht " : " dag ") + _d + (_am ? " amoled" : " mip") + (_direct ? " DIRECT" : " plaatje") + " (voorraad geschat " + (_d * _d * 2 / 1024) + " kB) beurten " + _beurten + " punten " + punten + " traagste beurt " + _msMax + " ms, held maat " + q(_held[2]) + ", gebruikt " + st.usedMemory + " van " + st.totalMemory);
        }
    }
}
