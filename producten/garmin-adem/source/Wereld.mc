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
    var maat as Number = 20;      // maat van het dier op zijn thuis, in 1/260 D
    // Direct getekend (codekeuring bouw 9 punt 2 en 7): planten na het plaatje, voorlaag na het dier. De tweede
    // lijst is dezelfde vlakken in de stand bij inademen (zelfde aantal punten); bij de voorlaag mag die null zijn.
    var planten as Array<Array<Number> > or Null = null;
    var planten2 as Array<Array<Number> > or Null = null;
    var voorlaag as Array<Array<Number> > or Null = null;
    var voorlaag2 as Array<Array<Number> or Null> or Null = null;
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
        maat = w["m"] as Number;
        planten = w["p"] as Array<Array<Number> >;
        planten2 = w["q"] as Array<Array<Number> >;
        voorlaag = w["f"] as Array<Array<Number> >;
        voorlaag2 = w["g"] as Array<Array<Number> or Null>;
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

    // Eén veelhoek voor in het plaatje, in 1/260 D, afgekapt zoals bij de dieren, verschoven met (dx, dy) in px;
    // de kleur staat op plek k (bij een detail staat de week ervoor).
    function veelhoekVanaf(dc as Graphics.Dc, v as Array<Number>, k as Number, d as Number, dx as Number, dy as Number) as Void {
        var pts = [] as Array<[Numeric, Numeric]>;
        for (var j = k + 1; j + 1 < v.size(); j += 2) {
            pts.add([v[j] * d / EbbWereldData.EENHEID + dx, v[j + 1] * d / EbbWereldData.EENHEID + dy]);
        }
        dc.setColor(v[k], Graphics.COLOR_TRANSPARENT);
        dc.fillPolygon(pts);
    }

    // Punt 7: een vlak in twee standen. a is de stand bij uitademen en inhouden, b die bij inademen (zelfde aantal
    // punten, of null als het vlak niet beweegt); f is de plek daartussen in duizendsten (0 = a, 1000 = b).
    // Punten in 1/260 D vanaf de bovenkant van het scherm, dx in px (als het scherm breder is dan d).
    function buig(dc as Graphics.Dc, a as Array<Number>, b as Array<Number> or Null, f as Number, d as Number, dx as Number) as Void {
        var pts = [] as Array<[Numeric, Numeric]>;
        var mee = b != null && f > 0 && (b as Array<Number>).size() == a.size();
        for (var j = 1; j + 1 < a.size(); j += 2) {
            var x = a[j];
            var y = a[j + 1];
            if (mee) {
                x += ((b as Array<Number>)[j] - x) * f / 1000;
                y += ((b as Array<Number>)[j + 1] - y) * f / 1000;
            }
            pts.add([x * d / EbbWereldData.EENHEID + dx, y * d / EbbWereldData.EENHEID]);
        }
        dc.setColor(a[0], Graphics.COLOR_TRANSPARENT);
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

    // Maat van het dier op zijn thuis in px (Mila: 27/260 D), zonder wereld 20/260.
    function maat(dier as Number, d as Number) as Number {
        var p = zorg(dier, d);
        return (p != null ? p.maat : 20) * d / EbbWereldData.EENHEID;
    }

    // Tekent de wereld van dit dier onderin: het plaatje en daarna de planten in de stand van de adem
    // (f in duizendsten: 0 bij uitademen en inhouden, 1000 bij ingeademd). Geeft true als hij er staat; anders
    // staat er alleen de zee.
    function teken(dc as Graphics.Dc, dier as Number, d as Number, f as Number) as Boolean {
        var p = zorg(dier, d);
        if (p == null) {
            return false;
        }
        if ((p.klaar || p.verder()) && p.plak(dc)) {
            var pl = p.planten;
            var p2 = p.planten2;
            if (pl != null) {
                for (var i = 0; i < pl.size(); i += 1) {
                    buig(dc, pl[i], (p2 != null && i < p2.size()) ? p2[i] : null, f, d, (dc.getWidth() - d) / 2);
                }
            }
            return true;
        }
        if (p.bezig()) {
            WatchUi.requestUpdate();
        }
        return false;
    }

    // Wat over het dier heen komt (hoogstens een paar veelhoeken, direct getekend). Na het dier aanroepen.
    function voor(dc as Graphics.Dc, dier as Number, d as Number, f as Number) as Void {
        if (_p == null || (_p as EbbWereldPlaatje).dier != dier || !(_p as EbbWereldPlaatje).klaar) {
            return;
        }
        var p = _p as EbbWereldPlaatje;
        var vl = p.voorlaag;
        var v2 = p.voorlaag2;
        if (vl == null) {
            return;
        }
        for (var i = 0; i < vl.size(); i += 1) {
            buig(dc, vl[i], (v2 != null && i < v2.size()) ? v2[i] : null, f, d, (dc.getWidth() - d) / 2);
        }
    }

    // Aan het einde van de sessie (EbbView.onHide): plaatje en gegevens weg (punt 4).
    function los() as Void {
        _p = null;
    }
}
