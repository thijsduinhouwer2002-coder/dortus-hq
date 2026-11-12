import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// PROEF krabwereld v2.2 (zie KrabV2.mc): de tekst van de zes schermen. De regels staan onder elkaar op de echte
// letterhoogte van het horloge (de systeemletter op MIP is hoger dan op het blad; in run 43135243219 liepen de
// cijfers door de kop). "press START to breathe" staat altijd in beeld tijdens inhouden (besluit 12 nov 03:10).
module KrabV2Tekst {
    // Kam van de zee bij in, uit en Calm (1/260).
    const KAM = [134, 170, 146] as Array<Number>;
    const DONKER = 0x001E3C;

    var _rand as Number = 0;
    var _cijfers as WatchUi.FontResource or Null = null;
    // Tekstvakken van dit scherm in pixels (x0, y0, x1, y1 achter elkaar), gemeten met de echte letter van het
    // horloge door dezelfde code die de tekst tekent (meet). Versiering vraagt met vrij() of ze mag staan.
    var _meet as Boolean = false;
    var _vak as Array<Number> = [] as Array<Number>;
    var _onder as Array<Number> = [0, 0] as Array<Number>;
    var _stond as Number = 0;
    var _weg as Number = 0;

    function meet(v as KrabV2View, dc as Graphics.Dc, d as Number, scherm as Number, am as Boolean, nacht as Boolean) as Void {
        _vak = [] as Array<Number>;
        _meet = true;
        teken(v, dc, d, scherm, am, nacht);
        _meet = false;
    }

    // Keuring 12 nov 05:25 NL punt 2 en 3: versiering (belletjes, sterren, vonkjes, lichtjes) blijft minstens 6/260
    // weg van elk tekstvak, op elk scherm. Staat ze te dicht, dan wordt ze niet getekend. x, y, r in 1/260.
    function vrij(v as KrabV2View, x as Numeric, y as Numeric, r as Numeric) as Boolean {
        if (raakt(v, x, y, r)) {
            _weg += 1;
            return false;
        }
        _stond += 1;
        return true;
    }

    // Zelfde meting zonder te tellen: staat een cirkel (x, y, r) binnen 6/260 van een tekstvak?
    function raakt(v as KrabV2View, x as Numeric, y as Numeric, r as Numeric) as Boolean {
        var m = v.q(r + 6);
        var px = v.q(x);
        var py = v.q(y);
        for (var i = 0; i + 3 < _vak.size(); i += 4) {
            if (px + m > _vak[i] && px - m < _vak[i + 2] && py + m > _vak[i + 1] && py - m < _vak[i + 3]) {
                return true;
            }
        }
        return false;
    }

    // Boven- en onderkant (pixels) van de onderste regel van het ademscherm: de golfrijen blijven daar 6/260 vandaan.
    function onderRegel() as Array<Number> {
        return _onder;
    }

    function meldVersiering(v as KrabV2View, scherm as Number) as Void {
        System.println("VERSIERING wereld " + v.wereld + " scherm " + scherm + " getekend " + _stond + ", geweken voor tekst " + _weg + ", " + (_vak.size() / 4) + " tekstvakken, norm " + v.q(6) + " px");
    }


    // Cijferletter van de wereldschermen: 85 procent van EbbCijfersKlein (56 van 260, de maat van Mila's blad),
    // zodat er lucht is tussen kop, cijfers, hartslagregel en de held (keuring 12 nov 04:05 NL punt 1 en 2).
    function cijfers() as Graphics.FontType {
        if (_cijfers == null) {
            _cijfers = WatchUi.loadResource(Rez.Fonts.EbbCijfersWereld) as WatchUi.FontResource;
        }
        return _cijfers as WatchUi.FontResource;
    }

    // Veilige zone (REGELS.md punt 8, toets van Mila 12 nov 03:45 UTC): minstens 6/260 lucht tussen de onderkant van
    // de tekst en de bovenkant van de held (bij kantelen komt één kant ±1/260 per graad omhoog).
    // De workflow maakt de run rood bij "VEILIG ... NEE". Meet nu in, uit, Calm en inhouden; menu en eind nog niet.
    function veilig(v as KrabV2View, scherm as Number, tekstOnder as Number, heldBoven as Number) as Void {
        var lucht = heldBoven - v.q(kantelMaat(v)) - tekstOnder;
        // Bij de krab zijn de scharen de bovenkant: te weinig lucht is NEE (run rood). Bij een ander dier is dit het
        // kader van het hele dier, te grof voor een rond schild naast de cijfers: daar meldt hij "krap" (niet rood).
        System.println("VEILIG wereld " + v.wereld + " scherm " + scherm + (v.wereld == 0 ? " lucht " : " kader lucht ") + lucht + " px, norm " + v.q(6) + (lucht >= v.q(6) ? " ja" : (v.wereld == 0 ? " NEE" : " krap")));
    }

    function kantelMaat(v as KrabV2View) as Float {
        var k = v.kantel();
        return k < 0.0 ? -k : k;
    }

    // Bovenkant van de held in 1/260: bij de krab de scharen (vaste maat van het blad), anders uit het kader van het dier.
    function heldBoven(v as KrabV2View, scherm as Number, top as Number) as Number {
        if (v.wereld == 0) {
            return scherm <= 2 ? v.held()[1] - 24 : 164;
        }
        var g = EbbDierMaat.grenzen(v.dier);
        var h = v.held();
        return h[1] - (g[3] - g[2]) * h[2] / (2 * EbbDierData.SCHAAL);
    }

    // De meeuw op het schild staat naast de cijfers, niet eronder: lucht is de grootste van opzij en erboven.
    function veiligMeeuw(v as KrabV2View, scherm as Number, tekstRechts as Number, tekstOnder as Number) as Void {
        var mp = KrabV2Schild.meeuwPlek(v.held(), v.kantel());
        var dx = v.q(mp[0] - 14) - tekstRechts;
        var dy = v.q(mp[1] - 13.2) - tekstOnder;
        var lucht = dx > dy ? dx : dy;
        System.println("VEILIG wereld " + v.wereld + " scherm " + scherm + " meeuw lucht " + lucht + " px, norm " + v.q(6) + (lucht >= v.q(6) ? " ja" : " NEE"));
    }

    // Tekent een regel met de bovenkant op y (pixels) en geeft de bovenkant van de volgende regel terug.
    // Vulkleur zonder nachtregel (knoppen en banden achter tekst). Wit met volle dekking is hetzelfde getal als
    // doorzichtig, daarom een fractie onder wit.
    function vul(dc as Graphics.Dc, am as Boolean, k as Number) as Void {
        dc.setColor(k, k);
        if (am && (dc has :setFill)) {
            dc.setFill(Graphics.createColor(255, (k >> 16) & 0xFF, (k >> 8) & 0xFF, k == 0xFFFFFF ? 0xFE : (k & 0xFF)));
        }
    }

    function regel(dc as Graphics.Dc, d as Number, y as Number, f as Graphics.FontType, s as String, kleur as Number, pct as Number) as Number {
        if (_meet) {
            var w = dc.getTextWidthInPixels(s, f);
            _vak.addAll([d / 2 - w / 2, y, d / 2 + w / 2, y + dc.getFontHeight(f)] as Array<Number>);
            return y + dc.getFontHeight(f) * pct / 100;
        }
        if (_rand > 0) {
            // Keuring 12 nov 04:05 NL punt 4: donkere rand om de letters als een achtergrond het contrast onder 4,5 haalt.
            dc.setColor(DONKER, Graphics.COLOR_TRANSPARENT);
            var o = [-1, -1, 0, -1, 1, -1, -1, 0, 1, 0, -1, 1, 0, 1, 1, 1] as Array<Number>;
            for (var i = 0; i < 8; i += 1) {
                dc.drawText(d / 2 + o[2 * i] * _rand, y + o[2 * i + 1] * _rand, f, s, Graphics.TEXT_JUSTIFY_CENTER);
            }
        }
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, y, f, s, Graphics.TEXT_JUSTIFY_CENTER);
        return y + dc.getFontHeight(f) * pct / 100;
    }

    function teken(v as KrabV2View, dc as Graphics.Dc, d as Number, scherm as Number, am as Boolean, nacht as Boolean) as Void {
        var geel = EbbTeken.LICHT;
        var wit = 0xFFFFFF;
        var y = 0;
        _rand = 0; // de rand staat uit sinds de bundel boven de tekst zwak is (Mila v3.2 a); in de simulator kostte hij ±40 ms per beurt
        if (scherm <= 2) {
            var top = v.kam();
            // Run 43139810543: de cijferletter vult zijn hele regel, dus geen overlap met de kop; de cijfers eindigen
            // 12/260 boven de scharen (keuring 12 nov 04:05 NL punt 2), de kop staat er direct boven (niet hoger dan 4/260).
            var hk = dc.getFontHeight(EbbTeken.fM()) * 92 / 100;
            var hb = heldBoven(v, scherm, top);
            var yd = v.q(hb) - v.q((v.wereld == 0 ? 11 : 7) + kantelMaat(v)) - dc.getFontHeight(cijfers()); // krab 11 (keuring 05:25 punt 6: ruim), anders 7 lucht plus wat door het kantelen omhoog komt
            yd = yd > v.q(18) + hk ? v.q(18) + hk : yd;
            yd = yd < v.q(4) + hk ? v.q(4) + hk : yd;
            regel(dc, d, yd - hk, EbbTeken.fM(), scherm == 0 ? "breathe in" : "breathe out", wit, 100);
            var getal = (["12", "9", "5"] as Array<String>)[scherm];
            y = regel(dc, d, yd, cijfers(), getal, wit, 100);
            var yo = regel(dc, d, v.q(top + 38), EbbTeken.fX(), scherm == 2 ? "4-7-8 · 2 of 4" : "round 2 · 18 left", wit, 100);
            if (_meet) {
                _onder = [v.q(top + 38), yo] as Array<Number>;
                return;
            }
            System.println("KRABV2 tekst scherm " + scherm + " cijfers tot y " + y + " van " + d + ", held vanaf " + v.q(hb));
            veilig(v, scherm, y, v.q(hb));
            if (v.wereld == 1) {
                veiligMeeuw(v, scherm, d / 2 + dc.getTextWidthInPixels(getal, cijfers()) / 2, y);
            }
        } else if (scherm == 3) {
            y = regel(dc, d, v.q(12), EbbTeken.fM(), "hold", geel, 90);
            y = regel(dc, d, y, EbbTeken.fX(), "press START to breathe", wit, 100);
            y = regel(dc, d, y, cijfers(), "1:45", wit, 100);
            y = regel(dc, d, y, EbbTeken.fX(), "61 bpm · round 2", wit, 100);
            if (_meet) {
                return;
            }
            System.println("KRABV2 tekst scherm 3 onderkant hartslagregel y " + y + " van " + d + ", held vanaf " + v.q(heldBoven(v, 3, 0)));
            veilig(v, scherm, y, v.q(heldBoven(v, 3, 0)));
        } else if (scherm == 4) {
            regel(dc, d, v.q(14), EbbTeken.fM(), "Ebb", geel, 100);
            var namen = ["Rounds", "Calm 4-7-8"] as Array<String>;
            // vaste kleur (Mila v2.1): 001E3C overdag, 000032 bij nacht; op MIP 000055
            var pk = am ? (nacht ? 0x000032 : 0x001E3C) : 0x000055;
            // Keuring 05:25 punt 3: voetregel wit op een rustige band over de hele breedte
            var by = v.q(116);
            var bh = dc.getFontHeight(EbbTeken.fX()) + v.q(4);
            if (_meet) {
                _vak.addAll([v.q(60), v.q(52), v.q(200), v.q(114), 0, by, d, by + bh] as Array<Number>);
                return;
            }
            for (var i = 0; i < 2; i += 1) {
                var py = 52 + 34 * i;
                // Keuring 05:25 punt 3: de gekozen knop is gevuld met een pijltje; de andere is donker met een dunne rand.
                // Mila 12 nov 06:05 UTC (ebb-punten-0600.md punt 1): gekozen knop zoals Resume. Overdag vlak 00FFFF
                // zonder rand met tekst 000055; bij nacht vlak 0055AA, rand 55AAFF 2 px, tekst wit. Knoppen vallen
                // buiten de nachtregel.
                var gt = nacht ? wit : 0x000055;
                vul(dc, am, (i == 0) ? (nacht ? 0x0055AA : 0x00FFFF) : pk);
                dc.fillRoundedRectangle(v.q(64), v.q(py), v.q(132), v.q(28), v.q(14));
                if (i == 0) {
                    if (nacht) {
                        dc.setColor(0x55AAFF, Graphics.COLOR_TRANSPARENT);
                        dc.setPenWidth(v.q(2) < 2 ? 2 : v.q(2));
                        dc.drawRoundedRectangle(v.q(64), v.q(py), v.q(132), v.q(28), v.q(14));
                        dc.setPenWidth(1);
                    }
                    vul(dc, am, gt);
                    var pts = [] as Array<[Numeric, Numeric]>;
                    pts.add([v.q(74), v.q(py + 8)]);
                    pts.add([v.q(74), v.q(py + 20)]);
                    pts.add([v.q(82), v.q(py + 14)]);
                    dc.fillPolygon(pts);
                } else {
                    dc.setColor(nacht ? 0x0055AA : 0x00AAFF, Graphics.COLOR_TRANSPARENT);
                    dc.drawRoundedRectangle(v.q(64), v.q(py), v.q(132), v.q(28), v.q(14));
                }
                dc.setColor(i == 0 ? gt : wit, Graphics.COLOR_TRANSPARENT);
                dc.drawText(d / 2 + (i == 0 ? v.q(4) : 0), v.q(py + 14), EbbTeken.fS(), namen[i], Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            }
            dc.setColor(pk, pk);
            if (am && (dc has :setFill)) {
                dc.setFill(Graphics.createColor(255, (pk >> 16) & 0xFF, (pk >> 8) & 0xFF, pk & 0xFF));
            }
            dc.fillRectangle(0, by, d, bh);
            regel(dc, d, by + v.q(2), EbbTeken.fX(), "Sea log  ·  Settings  ·  Today", wit, 100);
            veilig(v, scherm, by + bh, v.q(v.wereld == 0 ? 186 - 25 : heldBoven(v, 4, 0)));
        } else {
            y = regel(dc, d, v.q(26), EbbTeken.fM(), "3 rounds done", geel, 82);
            var yt = regel(dc, d, y, EbbTeken.fS(), "1:20   1:45   1:58", wit, 100);
            y = regel(dc, d, v.q(165), EbbTeken.fX(), "new friend", wit, 78);
            y = regel(dc, d, y, EbbTeken.fM(), v.wereld == 1 ? "Jellyfish" : "Shrimp", geel, 95);
            var sy = y + v.q(5);
            if (_meet) {
                _vak.addAll([v.q(112), sy - v.q(4), v.q(148), sy + v.q(4)] as Array<Number>);
                return;
            }
            veilig(v, scherm, yt, v.q(v.wereld == 0 ? 130 - 22 : heldBoven(v, 5, 0)));
            // Keuring 3 punt 5: de bolletjes vielen weg tegen het zand; nu op een donker pilletje.
            v.kleur(dc, am ? DONKER : 0x000055);
            dc.fillRoundedRectangle(v.q(106), sy - v.q(7), v.q(48), v.q(14), v.q(7));
            v.kleur(dc, EbbTeken.SCHUIM);
            dc.fillCircle(v.q(130), sy, v.q(3.5));
            dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
            dc.drawCircle(v.q(117), sy, v.q(3.5));
            dc.drawCircle(v.q(143), sy, v.q(3.5));
        }
    }
}
