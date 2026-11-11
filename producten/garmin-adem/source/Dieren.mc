import Toybox.Graphics;
import Toybox.Lang;
import Toybox.WatchUi;

// Sea log volgens blad v7 en v8 (keuring bouw 1 punt 8): raster 3 x 3 over drie bladen met Mila's dieren als data.
// Gevonden dieren in eigen kleuren met witte stickerrand, de rest als silhouet met kenmerk. Bovenaan "sea log" en
// "8 of 24", onderaan naam en eerlijk wat er nog nodig is, daaronder drie bladstippen. Omhoog en omlaag (of vegen)
// verschuift de keuze; select kiest een gevonden dier dat met je meezwemt.
class DierenView extends WatchUi.View {
    var keuze as Number = 0;
    const PER_BLAD = 9;
    // Run 42953647184: met 3 per beurt (15 keer tekenen) trapte de watchdog op de FR255; 1 dier (5 keer) per beurt.
    const NIEUW_PER_BEURT = 1;
    var _plaatje as Graphics.BufferedBitmapReference or Null = null;
    var _sleutel as Number = -1;
    var _getekend as Number = 0;

    // De 64 kleuren van het MIP-scherm: alle dieren en silhouetten gebruiken alleen deze, 1 byte per pixel.
    function palet() as Array<Number> {
        var p = [] as Array<Number>;
        for (var r = 0; r < 4; r += 1) {
            for (var g = 0; g < 4; g += 1) {
                for (var b = 0; b < 4; b += 1) {
                    p.add(r * 0x550000 + g * 0x5500 + b * 0x55);
                }
            }
        }
        return p;
    }

    // Voor de toets: staat het hele blad in het plaatje?
    function klaar() as Boolean {
        var blad = keuze / PER_BLAD;
        return _plaatje != null && (_getekend >= PER_BLAD || blad * PER_BLAD + _getekend >= EbbTrouw.DIEREN.size());
    }

    function initialize() {
        View.initialize();
        var m = EbbTrouw.zwemmer();
        keuze = m >= 0 ? m : 0;
    }

    function bladen() as Number {
        return (EbbTrouw.DIEREN.size() + PER_BLAD - 1) / PER_BLAD;
    }

    function verschuif(stap as Number) as Void {
        var n = EbbTrouw.DIEREN.size();
        keuze = (keuze + stap + n) % n;
        WatchUi.requestUpdate();
    }

    // Wat er onder de naam staat (blad v8 C): gevonden "swims with you" of "found"; anders "next session",
    // "2 more days in a row" of "at 50 sessions"; de bonus blijft een verrassing.
    function regel(i as Number) as String {
        if (EbbTrouw.heeft(i)) {
            // Keuring bouw 3 punt 9: de hint zegt welke knop ("START: swims with you").
            return (EbbTrouw.zwemmer() == i) ? "swims with you" : WatchUi.loadResource(Rez.Strings.KiesHint) as String;
        }
        if (EbbTrouw.bonus(i)) {
            return "a surprise";
        }
        var r = EbbTrouw.DIEREN[i];
        var drempel = r[2] as Number;
        if ((r[1] as Number) == EbbTrouw.SOORT_REEKS) {
            var reeks = EbbTrouw.reeksOp(EbbView.vandaag());
            var rest = (EbbTrouw.getal(EbbTrouw.BESTE) >= drempel) ? 0 : drempel - reeks;
            if (rest <= 0) {
                return "next session";
            }
            return rest + (rest == 1 ? " more week in a row" : " more weeks in a row");
        }
        var nog = drempel - EbbTrouw.getal(EbbTrouw.SESSIES);
        return (nog <= 1) ? "next session" : "at " + drempel + " sessions";
    }

    // Keuring bouw 3 punt 9: boven- en onderkant van dier i in 1/SCHAAL van de diermaat (uit de punten zelf).
    function grens(i as Number) as Array<Number> {
        var b = EbbDierData.DATA[i];
        var o = 1;
        var boven = 0;
        var onder = 0;
        for (var deel = 0; deel < b[0]; deel += 1) {
            var n = b[o + 1];
            o += 2;
            for (var k = 0; k < n; k += 1) {
                var y = EbbDierData.s8(b[o + 1]);
                if (y < boven) { boven = y; }
                if (y > onder) { onder = y; }
                o += 2;
            }
        }
        return [boven, onder] as Array<Number>;
    }

    // Opbouw van een blad (keuring bouw 3 punt 9): rijen 3 px uit elkaar (op 260; groter scherm iets meer), het raster
    // tussen de telling en de naam; past het niet, dan wordt de diermaat voor dat blad kleiner. Zet _maat, _rijY, _boven, _onder.
    var _maat as Number = 20;
    var _rijY as Array<Number> = [0, 0, 0] as Array<Number>;
    var _boven as Number = 0;
    var _onder as Number = 0;
    var _grenzen as Array<Array<Number> > = [] as Array<Array<Number> >;

    function bouwBlad(dc as Graphics.Dc, d as Number, blad as Number) as Void {
        var schaal = EbbDierData.SCHAAL;
        var rijen = 0;
        var top = [0, 0, 0] as Array<Number>;
        var bod = [0, 0, 0] as Array<Number>;
        _grenzen = [] as Array<Array<Number> >;
        for (var k = 0; k < PER_BLAD; k += 1) {
            var i = blad * PER_BLAD + k;
            if (i >= EbbTrouw.DIEREN.size()) {
                break;
            }
            var g = grens(i);
            _grenzen.add(g);
            var r = k / 3;
            rijen = r + 1;
            if (g[0] < top[r]) { top[r] = g[0]; }
            if (g[1] > bod[r]) { bod[r] = g[1]; }
        }
        var tussen = (d * 0.0116).toNumber();
        tussen = tussen < 3 ? 3 : tussen;
        var fs = dc.getFontHeight(Graphics.FONT_SMALL);
        var fx = dc.getFontHeight(Graphics.FONT_XTINY);
        var boven = (d * 0.135).toNumber() + fs / 2 + fx + 4;
        var naamLucht = (d * 0.0385).toNumber();
        naamLucht = naamLucht < 10 ? 10 : naamLucht;
        // Onder het raster: naam, regel en bladstippen, met de stippen hoogstens op 0,91 D.
        var eronder = naamLucht + fs + 2 + fs + (d * 0.04).toNumber();
        var ruimte = (d * 0.91).toNumber() - eronder - boven;
        var eenheden = 0;
        for (var r = 0; r < rijen; r += 1) {
            eenheden += bod[r] - top[r];
        }
        var rand = 3;
        var vast = rijen * 2 * rand + (rijen - 1) * tussen;
        var maat = (d * 0.078).toNumber();
        if (eenheden * maat / schaal + vast > ruimte) {
            maat = (ruimte - vast) * schaal / eenheden;
            maat = maat < 8 ? 8 : maat;
        }
        _maat = maat;
        var hoog = eenheden * maat / schaal + vast;
        var y = (d * 0.475).toNumber() - hoog / 2;
        y = y < boven ? boven : y;
        _boven = y;
        for (var r = 0; r < rijen; r += 1) {
            _rijY[r] = y + rand - top[r] * maat / schaal;
            y += (bod[r] - top[r]) * maat / schaal + 2 * rand + tussen;
        }
        _onder = y - tussen;
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var d = w < dc.getHeight() ? w : dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        var midden = Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER;
        var blad = keuze / PER_BLAD;
        // Keuring bouw 2 punt 1 (watchdog): de dieren van een blad komen in één plaatje op zwart (het raster), dat over
        // een paar beurten vol getekend wordt: hoogstens NIEUW_PER_BEURT dieren per beurt, elke beurt een eigen watchdog.
        // Is het plaatje af, dan kost een beurt alleen nog het plakken. Opnieuw na een ander blad of een nieuw dier.
        var ox = (d * 0.13).toNumber();
        var sleutel = blad * 100000000 + EbbTrouw.getal(EbbTrouw.BITS) % 100000000;
        var ref = _plaatje;
        var bb = (ref != null) ? ref.get() : null;
        if (bb == null || sleutel != _sleutel) {
            bouwBlad(dc, d, blad);
            ref = Graphics.createBufferedBitmap({:width => (d * 0.74).toNumber(), :height => _onder - _boven + 2, :palette => palet()});
            _plaatje = ref;
            bb = ref.get();
            var pdc0 = (bb as Graphics.BufferedBitmap).getDc();
            pdc0.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
            pdc0.clear();
            _sleutel = sleutel;
            _getekend = 0;
        }
        var oy = _boven;
        var maat = _maat;
        var plaatje = bb as Graphics.BufferedBitmap;
        var pdc = plaatje.getDc();
        var gekozenY = 0;
        var gekozenX = 0;
        var nu = 0;
        for (var k = 0; k < PER_BLAD; k += 1) {
            var i = blad * PER_BLAD + k;
            if (i >= EbbTrouw.DIEREN.size()) {
                break;
            }
            var x = (d * (0.29 + 0.21 * (k % 3))).toNumber();
            var y = _rijY[k / 3];
            if (k >= _getekend && nu < NIEUW_PER_BEURT) {
                if (EbbTrouw.heeft(i)) {
                    EbbDierData.teken(pdc, i, x - ox, y - oy, maat, -1);
                } else {
                    EbbDierData.silhouet(pdc, i, x - ox, y - oy, maat);
                }
                nu += 1;
                _getekend = k + 1;
            }
            if (i == keuze) {
                gekozenX = x;
                gekozenY = y + (_grenzen[k][1] * maat) / EbbDierData.SCHAAL;
            }
        }
        var later = _getekend < PER_BLAD && blad * PER_BLAD + _getekend < EbbTrouw.DIEREN.size();
        dc.drawBitmap(ox, oy, plaatje);
        // Kop na het plaatje, zodat het zwarte raster de tekst niet bedekt.
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        // Beelden run 42953647184: "sea log" en "8 of 24" liepen in elkaar; nu de telling kleiner eronder.
        dc.drawText(w / 2, (d * 0.135).toNumber(), Graphics.FONT_SMALL, "sea log", midden);
        dc.drawText(w / 2, (d * 0.135).toNumber() + dc.getFontHeight(Graphics.FONT_SMALL) / 2 + dc.getFontHeight(Graphics.FONT_XTINY) / 2, Graphics.FONT_XTINY, EbbTrouw.aantalGewoon() + " of " + EbbTrouw.totaal(), midden);
        // Keuzestip 3 px onder de onderkant van het gekozen dier (blad v8, keuring bouw 3 punt 9), na de stickerrand.
        dc.setColor(EbbTeken.SCHUIM, EbbTeken.SCHUIM);
        var rs = (d * 0.011).toNumber();
        rs = rs < 3 ? 3 : rs;
        dc.fillCircle(gekozenX, gekozenY + 3 + 3 + rs, rs);
        // Naam 10 px onder het raster (op 260), regel en bladstippen eronder.
        var fs = dc.getFontHeight(Graphics.FONT_SMALL);
        var lucht = (d * 0.0385).toNumber();
        lucht = lucht < 10 ? 10 : lucht;
        var yNaam = _onder + lucht + fs / 2;
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        var naam = (EbbTrouw.bonus(keuze) && !EbbTrouw.heeft(keuze)) ? "Bonus" : EbbDierData.NAMEN[keuze];
        dc.drawText(w / 2, yNaam, Graphics.FONT_SMALL, naam, midden);
        var tekst = regel(keuze);
        var f = (dc.getTextWidthInPixels(tekst, Graphics.FONT_SMALL) <= d * 0.74) ? Graphics.FONT_SMALL : Graphics.FONT_XTINY;
        dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        var yRegel = yNaam + fs / 2 + 2 + dc.getFontHeight(f) / 2;
        dc.drawText(w / 2, yRegel, f, tekst, midden);
        // Bladstippen: actief schuim, de andere 00AAFF (blad v8).
        var n = bladen();
        var stap = (d * 0.04).toNumber();
        var rb = (d * 0.009).toNumber();
        rb = rb < 2 ? 2 : rb;
        var yStip = yRegel + dc.getFontHeight(f) / 2 + (d * 0.02).toNumber();
        for (var b = 0; b < n; b += 1) {
            var kleur = (b == blad) ? EbbTeken.SCHUIM : EbbTeken.ZEE_KLEUR[0];
            dc.setColor(kleur, kleur);
            dc.fillCircle(w / 2 + (b - (n - 1) / 2.0) * stap, yStip, rb);
        }
        if (later) {
            WatchUi.requestUpdate();
        }
    }
}

class DierenDelegate extends WatchUi.BehaviorDelegate {
    private var _view as DierenView;

    function initialize(view as DierenView) {
        BehaviorDelegate.initialize();
        _view = view;
    }

    function onNextPage() as Boolean {
        _view.verschuif(1);
        return true;
    }

    function onPreviousPage() as Boolean {
        _view.verschuif(-1);
        return true;
    }

    function onSelect() as Boolean {
        if (EbbTrouw.kies(_view.keuze)) {
            WatchUi.requestUpdate();
        }
        return true;
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        return onSelect();
    }
}
