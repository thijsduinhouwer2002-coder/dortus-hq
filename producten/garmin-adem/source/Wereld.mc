import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Besluit Thijs 11 nov 23:13 NL: elk dier zijn eigen stukje zee. Dit bestand is het mechanisme (bericht hoofdchat
// 23:20 punt 2), zie platformen/garmin/werelden-techniek-2026-11-11.md op main en REGELS.md punt 7.
// De wereld is een strook onderin (volle breedte, van EbbWereldData.BOVEN tot de onderkant; bij Mila v1.1 142/260 D hoog), één keer opgebouwd in een eigen plaatje, één laag
// per beurt (tegen de watchdog, zoals EbbDierPlaatje), daarna alleen plakken. Hoogstens één wereld tegelijk.
// Lukt het plaatje niet (voorraad van het horloge vol), dan tekent het scherm gewoon de zee zonder wereld.

// De gegevens staan in WereldData.mc, gemaakt door bron/maak_werelden.py uit Mila's json (nu v1.1: schildpad, krab,
// clownvis). Geen palet: op de FR255 gaf een plaatje met palet een wit blok (zie DierPlaatje.mc), dus volle kleur.
// Een beurt tekent hoogstens PER_BEURT veelhoeken (tegen de watchdog).
class EbbWereldPlaatje {
    const PER_BEURT = 4;
    var dier as Number;
    var d as Number;
    var hoog as Number;
    var stap as Number = 0;
    var klaar as Boolean = false;
    var weken as Number = 0;
    private var _eersteDetail as Number = 9999;
    private var _vl as Array<Array<Number> > or Null = null;
    private var _ref as Graphics.BufferedBitmapReference or Null = null;

    function initialize(i as Number, maat as Number) {
        dier = i;
        d = maat;
        hoog = maat - EbbWereldData.BOVEN * maat / EbbWereldData.EENHEID;
        var l = EbbWereldData.vlakken(i);
        if (l == null) {
            return;
        }
        // Besluit 12 nov 00:25 punt 4: details die je met gehaalde weekdoelen verdiende komen er als laatste bij.
        weken = EbbTrouw.wekenTotaal();
        var det = EbbWereldData.details(i);
        if (det != null) {
            var n = EbbWereld.verdiend(det, weken);
            if (n > 0) {
                l = l.slice(0, null);
                _eersteDetail = l.size();
                l.addAll(det.slice(0, n));
            }
        }
        try {
            var ref = Graphics.createBufferedBitmap({:width => maat, :height => hoog});
            var bb = ref.get();
            if (bb != null) {
                var dc = (bb as Graphics.BufferedBitmap).getDc();
                dc.setColor(Graphics.COLOR_TRANSPARENT, Graphics.COLOR_TRANSPARENT);
                dc.clear();
                _ref = ref;
                _vl = l;
            }
        } catch (e instanceof Lang.Exception) {
            _ref = null;
        }
        if (_ref == null) {
            // Keuring bouw 8 punt 7: een mislukte poging staat in het log, met de maat.
            System.println("WERELD plaatje mislukt " + maat + " x " + hoog);
        }
    }

    // Wordt er nog gebouwd? Nee als dit dier geen wereld heeft of het plaatje niet lukte.
    function bezig() as Boolean {
        return _ref != null && _vl != null && stap < (_vl as Array<Array<Number> >).size();
    }

    // Een paar veelhoeken verder. Geeft true als de wereld af is.
    function verder() as Boolean {
        if (_ref == null || _vl == null) {
            return false;
        }
        var vl = _vl as Array<Array<Number> >;
        if (stap >= vl.size()) {
            return true;
        }
        var bb = (_ref as Graphics.BufferedBitmapReference).get();
        if (bb == null) {
            return false;
        }
        var dc = (bb as Graphics.BufferedBitmap).getDc();
        var tot = stap + PER_BEURT;
        tot = tot > vl.size() ? vl.size() : tot;
        while (stap < tot) {
            EbbWereld.veelhoekVanaf(dc, vl[stap], stap >= _eersteDetail ? 1 : 0, d, 0, 0);
            stap += 1;
        }
        if (stap >= vl.size()) {
            var st = System.getSystemStats();
            System.println("GEHEUGEN WERELD dier " + dier + " plaatje " + d + " x " + hoog + " vlakken " + stap + " gebruikt " + st.usedMemory + " van " + st.totalMemory + " = " + (st.usedMemory.toLong() * 100 / st.totalMemory) + "%");
            _vl = null;
            klaar = true;
            return true;
        }
        return false;
    }

    function plak(dc as Graphics.Dc) as Void {
        var bb = (_ref != null) ? (_ref as Graphics.BufferedBitmapReference).get() : null;
        if (bb != null) {
            dc.drawBitmap((dc.getWidth() - d) / 2, d - hoog, bb as Graphics.BufferedBitmap);
        }
    }
}

module EbbWereld {
    // Alleen aan in de proefscènes van de plaatjesbouw, tot Mila's werelden gekeurd zijn.
    var proef as Boolean = false;
    var _p as EbbWereldPlaatje or Null = null;

    // Eén veelhoek [kleur, x, y, ...] in 1/260 D, afgekapt zoals bij de dieren, verschoven met (dx, dy) in px.
    function veelhoek(dc as Graphics.Dc, v as Array<Number>, d as Number, dx as Number, dy as Number) as Void {
        veelhoekVanaf(dc, v, 0, d, dx, dy);
    }

    // Zelfde, maar de kleur staat op plek k (bij een detail staat de week ervoor).
    function veelhoekVanaf(dc as Graphics.Dc, v as Array<Number>, k as Number, d as Number, dx as Number, dy as Number) as Void {
        var pts = [] as Array<[Numeric, Numeric]>;
        for (var j = k + 1; j + 1 < v.size(); j += 2) {
            pts.add([v[j] * d / EbbWereldData.EENHEID + dx, v[j + 1] * d / EbbWereldData.EENHEID + dy]);
        }
        dc.setColor(v[k], Graphics.COLOR_TRANSPARENT);
        dc.fillPolygon(pts);
    }

    // Hoeveel details (oplopend op week, week op plek 0) zijn er verdiend met dit aantal gehaalde weken?
    function verdiend(details as Array<Array<Number> >, weken as Number) as Number {
        var n = 0;
        while (n < details.size() && details[n][0] <= weken) {
            n += 1;
        }
        return n;
    }

    // Heeft dit dier een wereld en staat hij aan?
    function heeft(dier as Number) as Boolean {
        return proef && dier >= 0 && EbbWereldData.thuis(dier) != null;
    }

    // Tekent de wereld van dit dier onderin. Geeft true als hij er staat; anders staat er alleen de zee.
    function teken(dc as Graphics.Dc, dier as Number, d as Number) as Boolean {
        if (!proef || dier < 0) {
            return false;
        }
        if (_p == null || (_p as EbbWereldPlaatje).dier != dier || (_p as EbbWereldPlaatje).d != d || (_p as EbbWereldPlaatje).weken != EbbTrouw.wekenTotaal()) {
            _p = new EbbWereldPlaatje(dier, d);
        }
        var p = _p as EbbWereldPlaatje;
        if (p.klaar || p.verder()) {
            p.plak(dc);
            return true;
        }
        if (p.bezig()) {
            WatchUi.requestUpdate();
        }
        return false;
    }

    // Wat over het dier heen komt (hoogstens een paar veelhoeken, direct getekend). Na het dier aanroepen.
    function voor(dc as Graphics.Dc, dier as Number, d as Number) as Void {
        if (!proef || dier < 0 || _p == null || !(_p as EbbWereldPlaatje).klaar) {
            return;
        }
        var vl = EbbWereldData.voor(dier);
        if (vl == null) {
            return;
        }
        var dy = EbbWereldData.BOVEN * d / EbbWereldData.EENHEID;
        for (var i = 0; i < vl.size(); i += 1) {
            veelhoek(dc, vl[i], d, (dc.getWidth() - d) / 2, dy);
        }
    }

    function los() as Void {
        _p = null;
    }
}
