import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.WatchUi;

// PROEF (berichten hoofdchat 12 nov 02:30 en 03:10 NL): de krabwereld v2.2 van Mila (ontwerp/garmin/ebb-werelden-v2.md,
// ontwerp/garmin/bron/werelden_v21.py) op zes schermen, dag en nacht, om te meten wat het horloge aankan. Alleen in de
// plaatjesbouw (scène 51 tot 62), niet in de gewone app. Maten in 1/260 D zoals het blad. Wat stil staat komt in vijf
// beurten in één plaatje van het hele scherm; lukt dat plaatje niet, dan tekent hij alles direct en meldt dat in het log.
// Niets is doorschijnend: licht en gloed zijn vlakken in een vaste mengtint (FR165 en vivoactive 5 kennen setFill niet,
// en wit met setFill viel op de fenix 8 weg).
// scherm: 0 inademen, 1 uitademen, 2 Calm (boven water), 3 inhouden, 4 menu, 5 eindscherm (onder water).
class KrabV2View extends WatchUi.View {
    const STAPPEN = 5;
    var scherm as Number;
    var nacht as Boolean;
    var punten as Number = 0;
    // hoogte van de kam boven water
    var top as Number = 134;
    private var _ref as Graphics.BufferedBitmapReference or Null = null;
    private var _stap as Number = 0;
    private var _direct as Boolean = false;
    private var _beurten as Number = 0;
    private var _msMax as Number = 0;
    private var _gemeld as Boolean = false;
    private var _d as Number = 260;
    private var _am as Boolean = false;
    private var _cijfers as WatchUi.FontResource or Null = null;
    // slipper: hak x, y, schaal, hoek in graden; held: midden van het kader x, y en maat
    private var _sl as Array<Float> = [158.0, 146.0, 1.412, -5.0] as Array<Float>;
    private var _held as Array<Number> = [154, 134, 36] as Array<Number>;

    function initialize(s as Number, n as Boolean) {
        View.initialize();
        scherm = s;
        nacht = n;
        if (s < 3) {
            // Bouwgegevens Mila: kam 134 (in), 170 (uit), 146 (Calm); bij hoge zee de krab rechts, bij lage 5 hoger.
            top = (s == 0) ? 134 : ((s == 1) ? 170 : 146);
            var hx = (top > 140) ? 124 : 154;
            var dy = (top < 140) ? 0 : -5;
            _held = [hx, top + dy, 36] as Array<Number>;
            _sl = [hx + 4.0, top + 12.0 + dy * 0.6, 1.412, -5.0] as Array<Float>;
        } else if (s == 3) {
            _held = [118, 184, 43] as Array<Number>;
            _sl = [120.0, 207.65, 1.4907, -4.0] as Array<Float>;
        } else if (s == 4) {
            _held = [118, 186, 38] as Array<Number>;
            _sl = [120.0, 206.9, 1.3173, -4.0] as Array<Float>;
        } else {
            _held = [76, 130, 34] as Array<Number>;
            _sl = [70.0, 152.0, 1.0, -6.0] as Array<Float>;
        }
    }

    function q(v as Numeric) as Number {
        return (v * _d / 260.0 + 0.5).toNumber();
    }

    function kleur(dc as Graphics.Dc, k as Number) as Void {
        dc.setColor(k, k);
    }

    // Gloed zonder vervaging en zonder doorschijnendheid (bouwgegevens Mila): een paar ellipsen, buiten groot en zwak,
    // binnen klein; elke stap mengt hetzelfde deel van de lichtkleur over de vorige. basis is de kleur eronder.
    function gloed(dc as Graphics.Dc, cx as Numeric, cy as Numeric, rx as Numeric, ry as Numeric, basis as Number, k as Number, sterkte as Float, stappen as Number, groei as Float) as Void {
        var a = (1.0 - Math.pow(1.0 - sterkte, 1.0 / stappen)).toFloat();
        var c = basis;
        for (var i = 0; i < stappen; i += 1) {
            var f = 1.0 + groei * (stappen - 1 - i) / (stappen > 1 ? stappen - 1 : 1);
            c = EbbTeken.meng(c, k, a);
            kleur(dc, c);
            dc.fillEllipse(q(cx), q(cy), q(rx * f), q(ry * f));
        }
    }

    function rondje(dc as Graphics.Dc, cx as Numeric, cy as Numeric, rx as Numeric, ry as Numeric, k as Number, rand as Number, glans as Number) as Void {
        rondjeD(dc, cx, cy, rx, ry, k, rand, glans, 2.2);
    }

    function rondjeD(dc as Graphics.Dc, cx as Numeric, cy as Numeric, rx as Numeric, ry as Numeric, k as Number, rand as Number, glans as Number, dikte as Float) as Void {
        if (rand >= 0) {
            kleur(dc, rand);
            dc.fillEllipse(q(cx), q(cy), q(rx + dikte), q(ry + dikte));
        }
        kleur(dc, k);
        dc.fillEllipse(q(cx), q(cy), q(rx), q(ry));
        if (glans >= 0) {
            kleur(dc, glans);
            dc.fillEllipse(q(cx - rx * 0.62), q(cy - ry * 0.55), q(rx * 0.22), q(ry * 0.16));
        }
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
        // dikke zool: dezelfde vorm iets lager in donkerroze met de witte rand, daarop de zool zelf
        var z = [] as Array<Float>;
        for (var i = 0; i < p.size() / 2; i += 1) {
            z.add(p[2 * i] + 0.8 * _sl[2]);
            z.add(p[2 * i + 1] + 3.2 * _sl[2]);
        }
        blob(dc, z, 0xAA0055, 0xFFFFFF, 2.2);
        blob(dc, p, 0xFF55AA, -1, 0.0);
        var g = [] as Array<Float>;
        g.addAll(rs(30.0, -4.5)); g.addAll(rs(46.0, -6.0)); g.addAll(rs(58.0, -4.0)); g.addAll(rs(46.0, -3.0));
        blob(dc, g, 0xFFAAFF, -1, 0.0);
        var t = [] as Array<Float>;
        t.addAll(rs(52.0, -1.0)); t.addAll(rs(57.0, -3.5)); t.addAll(rs(61.0, -1.0)); t.addAll(rs(57.0, 1.5));
        blob(dc, t, 0xAA0055, -1, 0.0);
    }

    // V-bandje (v2.2): van het teenpaaltje in de neus naar beide kanten van de taille, wit en dik, vrij naast de krab.
    function bandje(dc as Graphics.Dc) as Void {
        var sch = _sl[2];
        var paal = rs(55.0, 0.0);
        var py = paal[1] - 2.0 * sch;
        var kant = [rs(31.0, -10.5), rs(31.0, 10.5)] as Array<Array<Float> >;
        dc.setColor(0xFFFFFF, Graphics.COLOR_TRANSPARENT);
        var w = q(5.0 * sch);
        dc.setPenWidth(w < 2 ? 2 : w);
        for (var i = 0; i < 2; i += 1) {
            dc.drawLine(q(kant[i][0]), q(kant[i][1]), q(paal[0]), q(py));
            dc.fillCircle(q(kant[i][0]), q(kant[i][1]), q(2.1 * sch));
        }
        dc.fillCircle(q(paal[0]), q(py), q(3.2 * sch));
        dc.setPenWidth(1);
    }

    // Eén beurt van wat stil staat. Boven water: lucht, golven, verre slipper, slipper. Onder water: water, ver en zand,
    // rotsen met anemoon en zeester, lichtjes en bellen, slipper.
    function laag(dc as Graphics.Dc, stap as Number) as Void {
        if (stap == 4) {
            if (scherm == 3 || scherm == 4) {
                // schaduw van de slipper op het zand
                if (_am) {
                    gloed(dc, _held[0] + 30, _sl[1] + 15, 44, 5, 0xEBE196, 0x5A5028, 0.5, 3, 0.25);
                } else {
                    rondje(dc, _held[0] + 30, _sl[1] + 15, 42, 5, 0xAAAA55, -1, -1);
                }
            }
            slipper(dc);
        } else if (scherm < 3) {
            KrabV2Lagen.boven(self, dc, stap, _am, nacht, top);
        } else {
            KrabV2Lagen.onder(self, dc, stap, _am, nacht, scherm);
        }
    }

    function cijfers() as Graphics.FontType {
        if (_cijfers == null) {
            _cijfers = WatchUi.loadResource(Rez.Fonts.EbbCijfersWereld) as WatchUi.FontResource;
        }
        return _cijfers as WatchUi.FontResource;
    }

    // Tekst. De cijferletter is hier 40 van 260 hoog (EbbCijfersWereld) en begint op zijn y; de plekken zijn zo gekozen
    // dat woord, getal en regels elkaar op de echte letters niet raken (run 51: "12" liep door "breathe in").
    function tekst(dc as Graphics.Dc) as Void {
        var geel = EbbTeken.LICHT;
        var wit = 0xFFFFFF;
        var d = _d;
        if (scherm < 3) {
            var hoog = top < 140;
            EbbTeken.tekst260(dc, d, hoog ? 14 : 22, EbbTeken.fM(), scherm == 0 ? "breathe in" : "breathe out", wit);
            EbbTeken.tekst260(dc, d, hoog ? 50 : 58, cijfers(), scherm == 0 ? "12" : (scherm == 1 ? "9" : "5"), wit);
            EbbTeken.tekst260(dc, d, top + 40, EbbTeken.fX(), scherm == 2 ? "4-7-8 · 2 of 4" : "round 2 · 18 left", wit);
        } else if (scherm == 3) {
            // "press START to breathe" blijft altijd staan tijdens inhouden (veiligheid, besluit hoofdchat 12 nov 03:10 NL).
            EbbTeken.tekst260(dc, d, 14, EbbTeken.fM(), "hold", geel);
            EbbTeken.tekst260(dc, d, 46, EbbTeken.fX(), "press START to breathe", wit);
            EbbTeken.tekst260(dc, d, 68, cijfers(), "1:45", wit);
            EbbTeken.tekst260(dc, d, 112, EbbTeken.fX(), "61 bpm · round 2", wit);
        } else if (scherm == 4) {
            EbbTeken.tekst260(dc, d, 16, EbbTeken.fM(), "Ebb", geel);
            var namen = ["Rounds", "Calm 4-7-8"] as Array<String>;
            for (var i = 0; i < 2; i += 1) {
                var y = 52 + 34 * i;
                // vaste kleur, geen doorschijnende pil (bouwgegevens Mila)
                var pk = _am ? (nacht ? 0x000032 : 0x001E3C) : 0x000055;
                dc.setColor(pk, pk);
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
            EbbTeken.tekst260(dc, d, 26, EbbTeken.fM(), "3 rounds done", geel);
            EbbTeken.tekst260(dc, d, 56, EbbTeken.fS(), "1:20   1:45   1:58", wit);
            EbbTeken.tekst260(dc, d, 160, EbbTeken.fX(), "new friend", wit);
            EbbTeken.tekst260(dc, d, 174, EbbTeken.fM(), "Shrimp", geel);
            for (var i = -1; i <= 1; i += 1) {
                dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
                if (i == 0) {
                    dc.fillCircle(q(130), q(212), q(3.5));
                } else {
                    dc.drawCircle(q(130 + 13 * i), q(212), q(3.5));
                }
            }
        }
    }

    // Dier i met het midden van zijn kader op (x, y) in 1/260 (de voorraad plakt op het zwaartepunt).
    function dier(dc as Graphics.Dc, i as Number, x as Number, y as Number, maat as Number) as Boolean {
        var m = q(maat);
        var g = EbbDierMaat.grenzen(i);
        var s = EbbDierData.SCHAAL;
        return EbbDierVoorraad.teken(dc, i, q(x) - (g[0] + g[1]) * m / (2 * s), q(y) - (g[2] + g[3]) * m / (2 * s), m, EbbDierPlaatje.GEVONDEN);
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
            staat = dier(dc, 4, _held[0], _held[1], _held[2]);
            if (scherm == 5) {
                // de nieuwe vriend (garnaal) in zijn belletje rechts
                var vriend = dier(dc, 1, 184, 123, 31);
                staat = staat && vriend;
            }
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
