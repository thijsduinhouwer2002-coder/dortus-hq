import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.WatchUi;

// PROEF (berichten hoofdchat 12 nov 02:30 en 03:10 NL): de krabwereld v2.2 van Mila (ontwerp/garmin/werelden21/,
// bron/werelden_v21.py, bouwgegevens in ebb-werelden-v2.md) op zes schermen, dag en nacht, om te meten wat het
// horloge aankan. Alleen in de plaatjesbouw (scène 51 tot 62), niet in de gewone app. Maten in 1/260 D zoals het
// blad. Wat stil staat komt in vijf beurten in één plaatje van het hele scherm; lukt dat plaatje niet, dan tekent
// hij alles direct en meldt dat in het log.
// scherm: 0 inademen, 1 uitademen, 2 Calm (boven water), 3 inhouden, 4 menu, 5 eindscherm (onder water).
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
    private var _msBij as Number = 0;
    private var _gemeld as Boolean = false;
    private var _d as Number = 260;
    private var _am as Boolean = false;
    // slipper: hak x, y, schaal, hoek in graden; held: midden van het kader x, y en maat
    // Mila v3.1: de slipper kantelt mee met de adem (min 5 min 8 / 3 / 0 graden bij in / Calm / uit), de krab 0,6 keer.
    var wereld as Number = 0; // 0 krab, 1 schildpad (Mila v3.2)
    var dier as Number = 4;
    var sl as Array<Float> = [158.0, 146.0, 1.4125, -13.0] as Array<Float>;
    private var _kantel as Float = 4.8;
    private var _gedraaid as Number = 0;
    private var _held as Array<Number> = [154, 134, 36] as Array<Number>;

    function initialize(s as Number, n as Boolean, w as Number) {
        View.initialize();
        scherm = s;
        nacht = n;
        _kantel = (s == 0) ? 4.8 : ((s == 2) ? 1.8 : 0.0);
        if (s == 1) {
            sl = [128.0, 179.0, 1.4125, -5.0] as Array<Float>;
            _held = [124, 165, 36] as Array<Number>;
        } else if (s == 2) {
            sl = [128.0, 155.0, 1.4125, -8.0] as Array<Float>;
            _held = [124, 141, 36] as Array<Number>;
        } else if (s == 3) {
            sl = [120.0, 215.65, 1.4907, -4.0] as Array<Float>;
            _held = [118, 192, 43] as Array<Number>;
        } else if (s == 4) {
            sl = [120.0, 206.9, 1.3173, -4.0] as Array<Float>;
            _held = [118, 186, 38] as Array<Number>;
        } else if (s == 5) {
            sl = [70.0, 152.0, 1.0, -6.0] as Array<Float>;
            _held = [76, 130, 34] as Array<Number>;
        }
        wereld = w;
        if (w == 1) {
            dier = 3;
            _held = KrabV2Schild.held(s);
            _kantel = KrabV2Schild.kantel(s);
        }
    }

    function kantel() as Float {
        return _kantel;
    }

    function held() as Array<Number> {
        return _held;
    }

    function heldMaat() as Number {
        return _held[2];
    }

    function q(v as Numeric) as Number {
        return (v * _d / 260.0 + 0.5).toNumber();
    }

    function kleur(dc as Graphics.Dc, k as Number) as Void {
        dc.setColor(k, k);
        if (_am && (dc has :setFill)) {
            // Wit met volle dekking is hetzelfde getal als "doorzichtig" (-1): daarom een fractie onder wit.
            dc.setFill(Graphics.createColor(255, (k >> 16) & 0xFF, (k >> 8) & 0xFF, k == 0xFFFFFF ? 0xFE : (k & 0xFF)));
        }
    }

    // Doorschijnend vullen kan alleen met setFill (AMOLED); op MIP gebruiken we het niet.
    // Vaste mengtint (Mila v2.1): a van 255 van kleur k over wat er ligt. Met setFill echt gemengd; FR165 en
    // vivoactive 5 kennen setFill niet (crash in run 43135243219): daar de mengkleur met de tint basis.
    function glas(dc as Graphics.Dc, a as Number, k as Number, basis as Number) as Void {
        if (dc has :setFill) {
            dc.setFill(Graphics.createColor(a, (k >> 16) & 0xFF, (k >> 8) & 0xFF, k & 0xFF));
        } else {
            var m = EbbTeken.meng(basis, k, a / 255.0);
            dc.setColor(m, m);
        }
    }

    // Gloed zonder vervaging: drie ellipsen, buiten groot en zwak, binnen klein (alleen AMOLED).
    function gloed(dc as Graphics.Dc, cx as Numeric, cy as Numeric, rx as Numeric, ry as Numeric, k as Number, a as Number, basis as Number) as Void {
        for (var i = 0; i < 3; i += 1) {
            var f = 1.35 - 0.175 * i;
            glas(dc, a, k, EbbTeken.meng(basis, k, a * i / 255.0));
            dc.fillEllipse(q(cx), q(cy), q(rx * f), q(ry * f));
        }
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

    // Eén beurt van wat stil staat. Boven water: lucht, golven, verre slipper, slipper. Onder water: water, ver en
    // zand, rotsen met anemoon en zeester, lichtjes en bellen, slipper.
    function laag(dc as Graphics.Dc, stap as Number) as Void {
        if (stap == 4 && wereld == 1) {
            KrabV2Schild.onderHeld(self, dc, scherm, _am, _held);
        } else if (stap == 4) {
            if (scherm == 3 || scherm == 4) {
                if (_am) {
                    gloed(dc, _held[0] + 30, sl[1] + 15, 33, 4, 0x5A5028, 53, 0xEBE196);
                } else {
                    rondje(dc, _held[0] + 30, sl[1] + 15, 42, 5, 0xAAAA55, -1, -1);
                }
            }
            KrabV2Slipper.slipper(self, dc);
        } else if (scherm <= 2) {
            KrabV2Boven.boven(self, dc, stap, _am, nacht, KrabV2Tekst.KAM[scherm]);
        } else {
            KrabV2Lagen.onder(self, dc, stap, _am, nacht, scherm);
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
            var g = EbbDierMaat.grenzen(dier);
            var s = EbbDierData.SCHAAL;
            _gedraaid = EbbDierVoorraad.tekenHoek(dc, dier, q(_held[0]) - (g[0] + g[1]) * m / (2 * s), q(_held[1]) - (g[2] + g[3]) * m / (2 * s), m, EbbDierPlaatje.GEVONDEN, _kantel, _am);
            staat = _gedraaid > 0;
            if (staat) {
                if (wereld == 1) {
                    KrabV2Schild.voor(self, dc, scherm, _am, nacht, _held, _kantel);
                } else {
                    KrabV2Slipper.bandje(self, dc);
                }
                if (scherm == 5) {
                    // de nieuwe vriend (garnaal) in zijn belletje rechts
                    var m2 = q(31);
                    var vr = (wereld == 1) ? 2 : 1;
                    var g2 = EbbDierMaat.grenzen(vr);
                    staat = EbbDierVoorraad.teken(dc, vr, q(184) - (g2[0] + g2[1]) * m2 / (2 * s), q(123) - (g2[2] + g2[3]) * m2 / (2 * s), m2, EbbDierPlaatje.GEVONDEN);
                }
            }
        } else {
            WatchUi.requestUpdate();
        }
        KrabV2Tekst.teken(self, dc, _d, scherm, _am, nacht);
        var ms = System.getTimer() - t0;
        if (ms > _msMax) {
            _msMax = ms;
            _msBij = _beurten;
        }
        if (staat && !_gemeld) {
            _gemeld = true;
            var st = System.getSystemStats();
            System.println("KRABV2 wereld " + wereld + " scherm " + scherm + (nacht ? " nacht " : " dag ") + _d + (_am ? " amoled" : " mip") + (_direct ? " DIRECT" : " plaatje") + " (voorraad geschat " + (_d * _d * 2 / 1024) + " kB) beurten " + _beurten + " punten " + punten + " traagste beurt " + _msMax + " ms (beurt " + _msBij + "), held maat " + q(_held[2]) + " kantel " + _kantel + (_gedraaid == 2 ? " GEDRAAID" : " recht") + ", gebruikt " + st.usedMemory + " van " + st.totalMemory);
        }
    }
}
