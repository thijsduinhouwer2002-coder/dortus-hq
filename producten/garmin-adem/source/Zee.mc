import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;

// De enige zee van Ebb (besluit Thijs 11 nov 07:41): elk scherm tekent zijn water via deze functies.
// zee: inhoudscherm in standen; zeeBanden: elke andere zee; ademZee: ademen en rustig; strook: dunne zee onderaan.
// Alles komt uit golf(); op AMOLED een verloop (zeeVerloop), op MIP harde banden in de 64 kleuren.
module EbbZee {
    const GOLF_PUNTEN = 28;

    // Blad v6, inhoudscherm: zee in stand 0 tot 5 (EbbProfiel.ZEE). Bovenste band met golf en schuimrand op 0,12 D,
    // de banden eronder als zachte golf zonder schuim. Op AMOLED het hele water 10 procent donkerder per stand.
    function zee(dc as Graphics.Dc, d as Number, stand as Number, fase as Float) as Void {
        var banden = EbbProfiel.ZEE[stand];
        var pct = EbbTeken.amoled() ? EbbProfiel.amoledHelderheid(stand) : 100;
        if (EbbTeken.amoled()) {
            zeeVerloop(dc, d, banden, pct, fase);
            return;
        }
        for (var b = 0; b < banden.size(); b += 2) {
            var kleur = EbbTeken.ZEE_KLEUR[banden[b + 1]];
            if (pct < 100) {
                kleur = EbbTeken.dimmer(kleur, pct);
            }
            var top = banden[b] / 100.0;
            if (b == 0) {
                golf(dc, d, top, d * 0.014, kleur, fase, true);
            } else {
                golf(dc, d, top, d * 0.008, kleur, fase + 1.3 * b, false);
            }
        }
    }

    // Daan B6 en D3, keuring bouw 1 punt 4: op AMOLED een zacht verloop in plaats van rechte banden. Onder de bovenste golf
    // (met schuimkam) 18 smalle stroken met een lichte golf, de kleur loopt geleidelijk van band naar band.
    const VERLOOP_STROKEN = 18;
    function zeeVerloop(dc as Graphics.Dc, d as Number, banden as Array<Number>, pct as Number, fase as Float) as Void {
        var top = banden[0] / 100.0;
        var kleur0 = EbbTeken.dimmer(EbbTeken.ZEE_KLEUR[banden[1]], pct);
        golf(dc, d, top, d * 0.014, kleur0, fase, true);
        var n = banden.size() / 2;
        for (var j = 1; j < VERLOOP_STROKEN; j += 1) {
            var y = top + (1.0 - top) * j / VERLOOP_STROKEN;
            // Band waarin y valt, en hoe ver naar de volgende grens (de laatste band loopt door tot 000055).
            var b = 0;
            while (b + 1 < n && banden[2 * (b + 1)] / 100.0 <= y) {
                b += 1;
            }
            var van = banden[2 * b] / 100.0;
            var tot = (b + 1 < n) ? banden[2 * (b + 1)] / 100.0 : 1.0;
            var k1 = EbbTeken.ZEE_KLEUR[banden[2 * b + 1]];
            var k2 = (b + 1 < n) ? EbbTeken.ZEE_KLEUR[banden[2 * (b + 1) + 1]] : EbbTeken.ZEE_KLEUR[3];
            var f = (tot > van) ? (y - van) / (tot - van) : 0.0;
            golf(dc, d, y, d * 0.004, EbbTeken.dimmer(EbbTeken.meng(k1, k2, f), pct), fase + 0.35 * j, false);
        }
    }

    // Keuring bouw 3 punt 7: één zee voor alle schermen. Bovenste golf met dezelfde kamlijn, daaronder de banden.
    // Op MIP harde banden (alleen 64 kleuren), op AMOLED een echt verloop (zeeVerloop), ook op de eindschermen.
    // tops in delen van D, tinten als index in EbbTeken.ZEE_KLEUR; amp is de golf van de bovenste band.
    function zeeBanden(dc as Graphics.Dc, d as Number, tops as Array<Float>, tinten as Array<Number>, amp as Float, fase as Float) as Void {
        if (EbbTeken.amoled()) {
            var banden = [] as Array<Number>;
            for (var i = 0; i < tops.size(); i += 1) {
                banden.add((tops[i] * 100 + 0.5).toNumber());
                banden.add(tinten[i]);
            }
            zeeVerloop(dc, d, banden, 100, fase);
            return;
        }
        golf(dc, d, tops[0], d * amp, EbbTeken.ZEE_KLEUR[tinten[0]], fase, true);
        for (var i = 1; i < tops.size(); i += 1) {
            golf(dc, d, tops[i], d * 0.007, EbbTeken.ZEE_KLEUR[tinten[i]], fase + 1.3 * i, false);
        }
    }

    // Vlak vanaf hoogte top (deel van D vanaf boven) tot de onderkant, met een golvende bovenrand.
    function golf(dc as Graphics.Dc, d as Number, top as Float, amp as Float, kleur as Number, fase as Float, schuim as Boolean) as Void {
        var y0 = d * top;
        var pts = [] as Array<[Numeric, Numeric]>;
        for (var i = 0; i <= GOLF_PUNTEN; i += 1) {
            var x = (d * i) / GOLF_PUNTEN;
            var y = y0 + amp * Math.sin(2.0 * Math.PI * 2.0 * i / GOLF_PUNTEN + fase);
            pts.add([x, y.toNumber()]);
        }
        var vlak = [] as Array<[Numeric, Numeric]>;
        vlak.addAll(pts);
        vlak.add([d, d]);
        vlak.add([0, d]);
        dc.setColor(kleur, kleur);
        dc.fillPolygon(vlak);
        if (schuim) {
            // Keuring bouw 2 punt 8: op AMOLED een kamlijn van 3 px met een zachte gloed eronder (een brede lijn in
            // een menging van water en schuim); op MIP de harde lijn zoals op het blad. Geldt voor elke zee met schuim.
            if (EbbTeken.amoled()) {
                dc.setColor(EbbTeken.meng(kleur, EbbTeken.SCHUIM, 0.45), Graphics.COLOR_TRANSPARENT);
                dc.setPenWidth(9);
                for (var i = 0; i < GOLF_PUNTEN; i += 1) {
                    dc.drawLine(pts[i][0], pts[i][1] + 2, pts[i + 1][0], pts[i + 1][1] + 2);
                }
            }
            dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
            dc.setPenWidth(EbbTeken.amoled() ? 3 : (d / 160 > 1 ? d / 160 : 1));
            for (var i = 0; i < GOLF_PUNTEN; i += 1) {
                dc.drawLine(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1]);
            }
            dc.setPenWidth(1);
        }
    }

    // Blad v6 scherm 2 en 5 (keuring bouw 1 punt 5, Daan B2): zee onderaan die zacht mee ademt. water 0 (uit) tot 1 (in):
    // bovenkant van 0,68 D naar 0,60 D, golf 0,012 D, dus de hoogste golftop is 0,588 D en het grote getal (midden 0,39 D)
    // blijft er altijd boven. Bovenste band 00AAFF, daaronder 0055AA (daar staat de ondertekst, wit haalt 6:1), onderin 0000AA.
    const ADEM_TOP = 0.68;
    const ADEM_SLAG = 0.08;
    const ADEM_AMP = 0.012;
    function ademZee(dc as Graphics.Dc, d as Number, water as Float, fase as Float) as Void {
        var top = ADEM_TOP - ADEM_SLAG * water;
        zeeBanden(dc, d, [top, top + 0.09, 0.93] as Array<Float>, [0, 1, 2] as Array<Number>, ADEM_AMP, fase);
    }

    // Bericht hoofdchat 12 nov 01:45 (boven water is ademen): de zee stijgt en zakt groot. Kam van 0,72 D (uit) naar
    // 0,58 D (in): 36 px slag op 260 in plaats van 21. Het grote getal (onderkant ±0,51 D) blijft erboven en de
    // onderregel (midden 0,84 D) staat altijd in de tweede band 0055AA (wit 7,3 op 1), nooit op het lichte water.
    // Nu alleen in de proefscènes (EbbBovenWater).
    const GROOT_TOP = 0.72;
    const GROOT_SLAG = 0.14;
    function grootTop(water as Float) as Float {
        return GROOT_TOP - GROOT_SLAG * water;
    }

    function ademZeeGroot(dc as Graphics.Dc, d as Number, water as Float, fase as Float) as Void {
        var top = grootTop(water);
        var tweede = top + 0.09;
        tweede = tweede > 0.78 ? 0.78 : tweede;
        zeeBanden(dc, d, [top, tweede, 0.93] as Array<Float>, [0, 1, 2] as Array<Number>, ADEM_AMP, fase);
    }

    // Blad v6.4: dunne zeestrook onderaan (today, 8 weeks, settings, veiligheid), zodat elk scherm bij dezelfde zee hoort.
    const STROOK_TOP = 0.877;   // hoogste golftop van de strook (0,885 min amplitude 0,008)
    function strook(dc as Graphics.Dc, d as Number) as Void {
        // Keuring bouw 6 punt 5: ook de dunne zee (today, 8 weeks, uitleg, veiligheid, settings) krijgt de schuimkam.
        golf(dc, d, 0.885, d * 0.008, EbbTeken.ZEE_KLEUR[1], 0.0, true);
        golf(dc, d, 0.935, d * 0.006, EbbTeken.ZEE_KLEUR[2], 1.1, false);
    }

    // Stille zee van het pauzemenu (blad v10): platte kamlijn op 84 (1/260 D), één tint 0055AA, vanaf 208 de diepte 000055.
    function stil(dc as Graphics.Dc, d as Number) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        dc.setColor(EbbTeken.ZEE_KLEUR[1], EbbTeken.ZEE_KLEUR[1]);
        dc.fillRectangle(0, EbbTeken.px(d, 84), w, EbbTeken.px(d, 208) - EbbTeken.px(d, 84));
        dc.setColor(EbbTeken.ZEE_KLEUR[3], EbbTeken.ZEE_KLEUR[3]);
        dc.fillRectangle(0, EbbTeken.px(d, 208), w, h - EbbTeken.px(d, 208));
        dc.setColor(EbbTeken.SCHUIM, EbbTeken.SCHUIM);
        dc.fillRectangle(0, EbbTeken.px(d, 84) - 1, w, d >= 300 ? 3 : 2);
    }
}
