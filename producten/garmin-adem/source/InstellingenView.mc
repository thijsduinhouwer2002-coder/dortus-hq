import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.WatchUi;

// Settings in Ebb-stijl (blad v7 scherm 9 en 9b, keuring bouw 1 punt 9, Daan D9): zwart, kop "settings", de gekozen
// regel als blauwe pil met de naam groot en de waarde eronder, één regel erboven en twee eronder, de zeestrook onderaan.
// Omhoog en omlaag (of vegen) kiest een regel, select (of tik) verandert hem. Geen "touch lock": dat is geen instelling,
// het aanraakscherm doet tijdens een sessie altijd niets.
class EbbInstellingenView extends WatchUi.View {
    var keuze as Number = 0;
    // Per regel [naam, soort, sleutel]: soort 0 waarde uit EbbInstellingen, 1 aan/uit, 2 actie, 3 vaste regel.
    const REGELS = [
        ["Rounds", 0, 2], ["Breathing pace", 0, 1], ["Breaths", 0, 0], ["Recovery hold", 0, 3],
        ["Buzz every 30 s", 1, :tik30], ["Buzz on last 3 breaths", 1, :laatste3], ["Vibration", 1, :trillen],
        ["My pattern: in", 0, 4], ["My pattern: hold", 0, 5], ["My pattern: out", 0, 6], ["My pattern: rest", 0, 7],
        ["Start my pattern", 2, :eigen], ["Ebb makes no sound", 3, :geluid], ["Safety info", 2, :veilig]
    ] as Array<Array>;
    var veiligGezet as Boolean = false;

    function initialize() {
        View.initialize();
    }

    function aantal() as Number {
        return REGELS.size();
    }

    function waarde(r as Number) as String or Null {
        var regel = REGELS[r];
        var soort = regel[1] as Number;
        if (soort == 0) {
            return EbbInstellingen.tekst(regel[2] as Number);
        }
        if (soort == 1) {
            return aan(regel[2] as Symbol) ? "on" : "off";
        }
        var id = regel[2] as Symbol;
        if (id == :eigen) {
            return EbbStart.eigenTekst();
        }
        if (id == :geluid) {
            return "vibration only";
        }
        if (id == :veilig) {
            return veiligGezet ? "next start" : null;
        }
        return null;
    }

    function aan(id as Symbol) as Boolean {
        if (id == :tik30) {
            return EbbInstellingen.tik30();
        }
        if (id == :laatste3) {
            return EbbInstellingen.laatste3();
        }
        return EbbInstellingen.trillen();
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var d = w < dc.getHeight() ? w : dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        EbbTeken.strook(dc, d);
        var midden = Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER;
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (d * 0.21).toNumber(), Graphics.FONT_SMALL, "settings", midden);
        // Regel erboven (0,34), de pil (0,50), twee eronder (0,72 en 0,80).
        if (keuze > 0) {
            regelKort(dc, d, keuze - 1, 0.335);
        }
        var bw = (d * 0.66).toNumber();
        var bh = (d * 0.21).toNumber();
        var py = (d * 0.505).toNumber();
        dc.setColor(EbbTeken.ZEE_KLEUR[1], EbbTeken.ZEE_KLEUR[1]);
        dc.fillRoundedRectangle(w / 2 - bw / 2, py - bh / 2, bw, bh, bh / 2);
        var naam = REGELS[keuze][0] as String;
        var fNaam = (dc.getTextWidthInPixels(naam, Graphics.FONT_MEDIUM) <= bw - d * 0.06) ? Graphics.FONT_MEDIUM : Graphics.FONT_SMALL;
        var v = waarde(keuze);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        if (v == null) {
            dc.drawText(w / 2, py, fNaam, naam, midden);
        } else {
            dc.drawText(w / 2, py - (d * 0.045).toNumber(), fNaam, naam, midden);
            dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, py + (d * 0.055).toNumber(), Graphics.FONT_SMALL, v as String, midden);
        }
        if (keuze + 1 < aantal()) {
            regelKort(dc, d, keuze + 1, 0.69);
        }
        if (keuze + 2 < aantal()) {
            regelKort(dc, d, keuze + 2, 0.77);
        }
    }

    // Regel buiten de pil: "Rounds  3" in lichtcyaan, kleiner als hij niet binnen de ronde rand past.
    function regelKort(dc as Graphics.Dc, d as Number, r as Number, y as Float) as Void {
        var v = waarde(r);
        var tekst = (REGELS[r][0] as String) + ((v != null && (REGELS[r][1] as Number) != 3) ? "  " + v : "");
        var dy = y - 0.5;
        var koorde = 2.0 * Math.sqrt(0.25 - dy * dy) * d * 0.84;
        var f = (dc.getTextWidthInPixels(tekst, Graphics.FONT_SMALL) <= koorde) ? Graphics.FONT_SMALL : Graphics.FONT_XTINY;
        dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * y).toNumber(), f, tekst, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }

    function verschuif(stap as Number) as Void {
        keuze = (keuze + stap + aantal()) % aantal();
        WatchUi.requestUpdate();
    }

    // Select: waarde een stap verder, aan/uit wisselen, of de actie. Geeft true als er een nieuw scherm kwam.
    function kies() as Boolean {
        var regel = REGELS[keuze];
        var soort = regel[1] as Number;
        if (soort == 0) {
            EbbInstellingen.volgende(regel[2] as Number);
        } else if (soort == 1) {
            var id = regel[2] as Symbol;
            var nieuw = !aan(id);
            if (id == :tik30) {
                EbbInstellingen.zetTik30(nieuw);
            } else if (id == :laatste3) {
                EbbInstellingen.zetLaatste3(nieuw);
            } else {
                EbbInstellingen.zetTrillen(nieuw);
            }
        } else if ((regel[2] as Symbol) == :eigen) {
            var ev = new RustigView(EbbInstellingen.eigenPatroon(), "My pattern");
            (Application.getApp() as EbbApp).zetRustig(ev);
            WatchUi.pushView(ev, new RustigDelegate(ev), WatchUi.SLIDE_LEFT);
            return true;
        } else if ((regel[2] as Symbol) == :veilig) {
            EbbVeilig.opnieuwTonen();
            veiligGezet = true;
        }
        WatchUi.requestUpdate();
        return false;
    }
}

class EbbInstellingenDelegate extends WatchUi.BehaviorDelegate {
    private var _view as EbbInstellingenView;

    function initialize(view as EbbInstellingenView) {
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
        _view.kies();
        return true;
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        _view.kies();
        return true;
    }

    function onBack() as Boolean {
        WatchUi.popView(WatchUi.SLIDE_RIGHT);
        return true;
    }
}
