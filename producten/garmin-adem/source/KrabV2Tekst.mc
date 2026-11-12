import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;

// PROEF krabwereld v2.2 (zie KrabV2.mc): de tekst van de zes schermen. De regels staan onder elkaar op de echte
// letterhoogte van het horloge (de systeemletter op MIP is hoger dan op het blad; in run 43135243219 liepen de
// cijfers door de kop). "press START to breathe" staat altijd in beeld tijdens inhouden (besluit 12 nov 03:10).
module KrabV2Tekst {
    // Tekent een regel met de bovenkant op y (pixels) en geeft de bovenkant van de volgende regel terug.
    function regel(dc as Graphics.Dc, d as Number, y as Number, f as Graphics.FontType, s as String, kleur as Number, pct as Number) as Number {
        dc.setColor(kleur, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, y, f, s, Graphics.TEXT_JUSTIFY_CENTER);
        return y + dc.getFontHeight(f) * pct / 100;
    }

    function teken(v as KrabV2View, dc as Graphics.Dc, d as Number, scherm as Number, am as Boolean, nacht as Boolean) as Void {
        var geel = EbbTeken.LICHT;
        var wit = 0xFFFFFF;
        var y = 0;
        if (scherm <= 2) {
            var top = ([134, 170, 146] as Array<Number>)[scherm];
            y = regel(dc, d, v.q(scherm == 0 ? 10 : 18), EbbTeken.fM(), scherm == 0 ? "breathe in" : "breathe out", wit, 78);
            y = regel(dc, d, y, EbbTeken.grootKlein(), (["12", "9", "5"] as Array<String>)[scherm], wit, 100);
            regel(dc, d, v.q(top + 38), EbbTeken.fX(), scherm == 2 ? "4-7-8 · 2 of 4" : "round 2 · 18 left", wit, 100);
            System.println("KRABV2 tekst scherm " + scherm + " cijfers tot y " + y + " van " + d + ", scharen vanaf " + v.q(top - 24));
        } else if (scherm == 3) {
            y = regel(dc, d, v.q(14), EbbTeken.fM(), "hold", geel, 78);
            y = regel(dc, d, y, EbbTeken.fX(), "press START to breathe", wit, 82);
            y = regel(dc, d, y, EbbTeken.grootKlein(), "1:45", wit, 92);
            y = regel(dc, d, y, EbbTeken.fX(), "61 bpm · round 2", wit, 100);
            System.println("KRABV2 tekst scherm 3 onderkant hartslagregel y " + y + " van " + d + ", scharen vanaf " + v.q(184 - 28));
        } else if (scherm == 4) {
            regel(dc, d, v.q(14), EbbTeken.fM(), "Ebb", geel, 100);
            var namen = ["Rounds", "Calm 4-7-8"] as Array<String>;
            for (var i = 0; i < 2; i += 1) {
                var py = 52 + 34 * i;
                // vaste kleur (Mila v2.1): 001E3C overdag, 000032 bij nacht; op MIP 000055
                var pk = am ? (nacht ? 0x000032 : 0x001E3C) : 0x000055;
                dc.setColor(pk, pk);
                if (am && (dc has :setFill)) {
                    dc.setFill(Graphics.createColor(255, (pk >> 16) & 0xFF, (pk >> 8) & 0xFF, pk & 0xFF));
                }
                dc.fillRoundedRectangle(v.q(64), v.q(py), v.q(132), v.q(28), v.q(14));
                dc.setColor(i == 0 ? wit : 0x00AAFF, Graphics.COLOR_TRANSPARENT);
                dc.setPenWidth(v.q(2.4) < 2 ? 2 : v.q(2.4));
                dc.drawRoundedRectangle(v.q(64), v.q(py), v.q(132), v.q(28), v.q(14));
                dc.setPenWidth(1);
                dc.setColor(wit, Graphics.COLOR_TRANSPARENT);
                dc.drawText(d / 2, v.q(py + 14), EbbTeken.fS(), namen[i], Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
            }
            regel(dc, d, v.q(118), EbbTeken.fX(), "Sea log  ·  Settings  ·  Today", geel, 100);
        } else {
            y = regel(dc, d, v.q(26), EbbTeken.fM(), "3 rounds done", geel, 82);
            regel(dc, d, y, EbbTeken.fS(), "1:20   1:45   1:58", wit, 100);
            y = regel(dc, d, v.q(160), EbbTeken.fX(), "new friend", wit, 78);
            y = regel(dc, d, y, EbbTeken.fM(), "Shrimp", geel, 95);
            var sy = y + v.q(5);
            v.kleur(dc, EbbTeken.SCHUIM);
            dc.fillCircle(v.q(130), sy, v.q(3.5));
            dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
            dc.drawCircle(v.q(117), sy, v.q(3.5));
            dc.drawCircle(v.q(143), sy, v.q(3.5));
        }
    }
}
