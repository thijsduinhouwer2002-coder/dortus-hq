import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Besluit Thijs 11 nov 23:13 NL: elk dier zijn eigen stukje zee. Dit bestand is het mechanisme (bericht hoofdchat
// 23:20 punt 2), zie platformen/garmin/werelden-techniek-2026-11-11.md op main en REGELS.md punt 7.
// De wereld is een strook onderin (volle breedte, van de bovenkant van deze wereld tot de onderkant; bij Mila v1.1 132 tot 142/260 D hoog), één keer opgebouwd in een eigen plaatje, één laag
// per beurt (tegen de watchdog, zoals EbbDierPlaatje), daarna alleen plakken. Hoogstens één wereld tegelijk.
// Lukt het plaatje niet (voorraad van het horloge vol), dan tekent het scherm gewoon de zee zonder wereld.

// De gegevens zijn geen code (codekeuring bouw 9 punt 1): bron/maak_werelden.py maakt per wereld één jsonData in
// resources/werelden/werelden.xml uit Mila's json, en alleen de wereld van het gekozen dier wordt geladen
// (EbbWereldData.laad). Geen palet: op de FR255 gaf een plaatje met palet een wit blok (zie DierPlaatje.mc).
// Watchdog (punt 6): een beurt tekent hoogstens PUNTEN_PER_BEURT punten (altijd minstens één veelhoek).
// Valt het plaatje uit de voorraad van het horloge (get() geeft null), dan bouwt hij opnieuw, hoogstens
// MAX_POGINGEN keer (punt 3); daarna blijft de zee zonder wereld.
class EbbWereldPlaatje {
    const PUNTEN_PER_BEURT = 200;
    const MAX_POGINGEN = 3;
    var dier as Number;
    var d as Number;
    var boven as Number = 0;      // bovenkant van de strook van deze wereld, in 1/260 D
    var hoog as Number = 0;
    var stap as Number = 0;
    var klaar as Boolean = false;
    var pogingen as Number = 0;
    var thuis as Array<Number> or Null = null;
    var voorlaag as Array<Array<Number> > or Null = null;
    private var _weken as Number;
    private var _eersteDetail as Number = 9999;
    private var _vl as Array<Array<Number> > or Null = null;
    private var _ref as Graphics.BufferedBitmapReference or Null = null;

    function initialize(i as Number, maat as Number) {
        dier = i;
        d = maat;
        // Punt 5: gehaalde weken één keer lezen per plaatje (dus per sessie), niet elke beurt.
        _weken = EbbTrouw.wekenTotaal();
        begin();
    }

    // Laadt de gegevens en maakt een leeg plaatje. Ook gebruikt om opnieuw te beginnen als het plaatje weg is.
    function begin() as Void {
        _ref = null;
        _vl = null;
        stap = 0;
        klaar = false;
        _eersteDetail = 9999;
        if (pogingen >= MAX_POGINGEN) {
            return;
        }
        pogingen += 1;
        var w = EbbWereldData.laad(dier);
        if (w == null) {
            return;
        }
        boven = w["b"] as Number;
        thuis = w["t"] as Array<Number>;
        voorlaag = w["f"] as Array<Array<Number> >;
        var l = w["v"] as Array<Array<Number> >;
        // Besluit 12 nov 00:25 punt 4: details die je met gehaalde weekdoelen verdiende komen er als laatste bij.
        var det = w["d"] as Array<Array<Number> >;
        var n = EbbWereld.verdiend(det, _weken);
        if (n > 0) {
            _eersteDetail = l.size();
            l.addAll(det.slice(0, n));
        }
        hoog = d - boven * d / EbbWereldData.EENHEID;
        try {
            var ref = Graphics.createBufferedBitmap({:width => d, :height => hoog});
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
            System.println("WERELD plaatje mislukt " + d + " x " + hoog + " poging " + pogingen);
        }
    }

    // Wordt er nog gebouwd? Nee als dit dier geen wereld heeft of het plaatje niet lukte.
    function bezig() as Boolean {
        return _ref != null && _vl != null && stap < (_vl as Array<Array<Number> >).size();
    }

    // Een aantal veelhoeken verder (tot de puntengrens). Geeft true als de wereld af is.
    function verder() as Boolean {
        if (_ref == null || _vl == null) {
            return false;
        }
        var vl = _vl as Array<Array<Number> >;
        var bb = (_ref as Graphics.BufferedBitmapReference).get();
        if (bb == null) {
            System.println("WERELD plaatje kwijt tijdens bouwen, poging " + pogingen);
            begin();
            return false;
        }
        var dc = (bb as Graphics.BufferedBitmap).getDc();
        var punten = 0;
        while (stap < vl.size() && (punten == 0 || punten + vl[stap].size() / 2 <= PUNTEN_PER_BEURT)) {
            EbbWereld.veelhoekVanaf(dc, vl[stap], stap >= _eersteDetail ? 1 : 0, d, 0, 0);
            punten += vl[stap].size() / 2;
            stap += 1;
        }
        if (stap >= vl.size()) {
            var st = System.getSystemStats();
            // De voorraad voor plaatjes meet de simulator niet; de schatting is breedte x hoogte x 2 bytes.
            System.println("GEHEUGEN WERELD dier " + dier + " plaatje " + d + " x " + hoog + " (voorraad geschat " + (d * hoog * 2 / 1024) + " kB) vlakken " + stap + " poging " + pogingen + " gebruikt " + st.usedMemory + " van " + st.totalMemory + " = " + (st.usedMemory.toLong() * 100 / st.totalMemory) + "%");
            _vl = null;
            klaar = true;
            return true;
        }
        return false;
    }

    // Plakt de strook. Geeft false als het plaatje uit de voorraad is gegooid; dan begint hij opnieuw (punt 3).
    function plak(dc as Graphics.Dc) as Boolean {
        var bb = (_ref != null) ? (_ref as Graphics.BufferedBitmapReference).get() : null;
        if (bb == null) {
            if (klaar) {
                System.println("WERELD plaatje kwijt, poging " + pogingen);
                begin();
            }
            return false;
        }
        dc.drawBitmap((dc.getWidth() - d) / 2, d - hoog, bb as Graphics.BufferedBitmap);
        return true;
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
        return proef && dier >= 0 && EbbWereldData.heeft(dier);
    }

    // Het plaatje van dit dier (maakt het als het er nog niet is), of null als er geen wereld hoort.
    function zorg(dier as Number, d as Number) as EbbWereldPlaatje or Null {
        if (!heeft(dier)) {
            return null;
        }
        if (_p == null || (_p as EbbWereldPlaatje).dier != dier || (_p as EbbWereldPlaatje).d != d) {
            _p = new EbbWereldPlaatje(dier, d);
        }
        return _p;
    }

    // Punt 6: al tijdens het ademen bouwen (zonder te tekenen), zodat de wereld er bij hold meteen staat.
    function bouw(dier as Number, d as Number) as Void {
        var p = zorg(dier, d);
        if (p != null && !p.klaar) {
            p.verder();
        }
    }

    // Waar het dier woont (midden van het dier, 1/260 D van het hele scherm); null zonder wereld.
    function thuis(dier as Number, d as Number) as Array<Number> or Null {
        var p = zorg(dier, d);
        return p != null ? p.thuis : null;
    }

    // Tekent de wereld van dit dier onderin. Geeft true als hij er staat; anders staat er alleen de zee.
    function teken(dc as Graphics.Dc, dier as Number, d as Number) as Boolean {
        var p = zorg(dier, d);
        if (p == null) {
            return false;
        }
        if ((p.klaar || p.verder()) && p.plak(dc)) {
            return true;
        }
        if (p.bezig()) {
            WatchUi.requestUpdate();
        }
        return false;
    }

    // Wat over het dier heen komt (hoogstens een paar veelhoeken, direct getekend). Na het dier aanroepen.
    function voor(dc as Graphics.Dc, dier as Number, d as Number) as Void {
        if (_p == null || (_p as EbbWereldPlaatje).dier != dier || !(_p as EbbWereldPlaatje).klaar) {
            return;
        }
        var p = _p as EbbWereldPlaatje;
        var vl = p.voorlaag;
        if (vl == null) {
            return;
        }
        var dy = p.boven * d / EbbWereldData.EENHEID;
        for (var i = 0; i < vl.size(); i += 1) {
            veelhoek(dc, vl[i], d, (dc.getWidth() - d) / 2, dy);
        }
    }

    // Aan het einde van de sessie (EbbView.onHide): plaatje en gegevens weg (punt 4).
    function los() as Void {
        _p = null;
    }
}
