import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Startmenu (ontwerp, bediening): rondes beginnen of de instellingen openen.
module EbbStart {
    const MENU_AANTAL = 4;
    const UITLEG = "uitlegGezien";   // blad v7 scherm 1c gezien
    // Op aanraakhorloges (vivoactive, venu) is het systeemmenu een wit vlak; daar een eigen donker menu
    // in de kleuren van Ebb (kan-punt Daan 10 nov). Knophorloges houden het systeemmenu, dat is daar al donker.
    function menu() as WatchUi.Menu2 {
        var labels = ["Rounds"] as Array<String>;
        var subs = [rondesTekst()] as Array<String or Null>;
        var ids = [:rondes] as Array<Symbol or Number>;
        for (var i = 0; i < PATROON_NAMEN.size(); i += 1) {
            labels.add(PATROON_NAMEN[i]);
            subs.add(PATROON_TEKST[i]);
            ids.add(i);
        }
        labels.add("My pattern"); subs.add(eigenTekst()); ids.add(:eigen);
        labels.add("Sea log"); subs.add(null); ids.add(:dieren);
        labels.add("Settings"); subs.add(null); ids.add(:instellingen);
        var m = null as WatchUi.Menu2 or Null;
        if (System.getDeviceSettings().isTouchScreen) {
            var h = System.getDeviceSettings().screenHeight;
            var cm = new WatchUi.CustomMenu(h / 5, Graphics.COLOR_BLACK, {
                :title => new EbbMenuTitel("Ebb"),
                :titleItemHeight => h / 4,
                :focusItemHeight => h / 4
            });
            for (var i = 0; i < labels.size(); i += 1) {
                cm.addItem(new EbbMenuItem(ids[i], labels[i], subs[i]));
            }
            m = cm;
        } else {
            m = new WatchUi.Menu2({:title => "Ebb", :theme => WatchUi.MENU_THEME_CYAN});
            for (var i = 0; i < labels.size(); i += 1) {
                m.addItem(new WatchUi.MenuItem(labels[i], subs[i], ids[i], null));
            }
        }
        return m as WatchUi.Menu2;
    }

    // Kop van het startscherm (blad v5, 1b): "Rounds 3 x 30".
    // Blad v6 scherm 1b: "3 rounds · 30 breaths".
    function startKop() as String {
        var r = EbbInstellingen.waarde(EbbInstellingen.RONDES);
        return r + (r == 1 ? " round · " : " rounds · ") + EbbInstellingen.waarde(EbbInstellingen.ADEMHALINGEN) + " breaths";
    }

    function rondesKop() as String {
        return "Rounds " + EbbInstellingen.waarde(EbbInstellingen.RONDES) + " x " + EbbInstellingen.waarde(EbbInstellingen.ADEMHALINGEN);
    }

    function rondesTekst() as String {
        return EbbInstellingen.waarde(EbbInstellingen.RONDES) + " x " + EbbInstellingen.waarde(EbbInstellingen.ADEMHALINGEN) + " breaths";
    }

    // De drie vaste patronen uit Ebb.patronen(), in dezelfde volgorde.
    const PATROON_NAMEN = ["Box", "4-7-8", "Calm"] as Array<String>;
    const PATROON_TEKST = ["4-4-4-4", "in 4, hold 7, out 8", "5.5 in, 5.5 out"] as Array<String>;

    function eigenTekst() as String {
        var p = EbbInstellingen.eigenPatroon();
        return (p[0] / 1000) + "-" + (p[1] / 1000) + "-" + (p[2] / 1000) + "-" + (p[3] / 1000);
    }

    const NAMEN = ["Breaths per round", "Breathing pace", "Rounds", "Recovery hold", "My pattern: in", "My pattern: hold", "My pattern: out", "My pattern: rest"] as Array<String>;

    function instellingen() as WatchUi.Menu2 {
        var m = new WatchUi.Menu2({:title => "Settings", :theme => WatchUi.MENU_THEME_CYAN});
        for (var i = 0; i < NAMEN.size(); i += 1) {
            m.addItem(new WatchUi.MenuItem(NAMEN[i], EbbInstellingen.tekst(i), i, null));
        }
        m.addItem(new WatchUi.ToggleMenuItem("Vibration", null, :trillen, EbbInstellingen.trillen(), null));
        m.addItem(new WatchUi.ToggleMenuItem("Buzz on last 3 breaths", null, :laatste3, EbbInstellingen.laatste3(), null));
        m.addItem(new WatchUi.ToggleMenuItem("Buzz every 30 s", null, :tik30, EbbInstellingen.tik30(), null));
        m.addItem(new WatchUi.MenuItem("Start my pattern", eigenTekst(), :eigen, null));
        // Blad v7 punt 6: "Sound off" weg; een vaste regel dat Ebb nooit geluid maakt (alleen trillen).
        m.addItem(new WatchUi.MenuItem("Ebb makes no sound", "vibration only", :geluid, null));
        m.addItem(new WatchUi.MenuItem("Safety info", null, :veilig, null));
        return m;
    }
}

class StartDelegate extends WatchUi.Menu2InputDelegate {
    function initialize() {
        Menu2InputDelegate.initialize();
    }

    function onSelect(item as WatchUi.MenuItem) as Void {
        var id = item.getId();
        if (id == :rondes) {
            // Blad v5 (S2): eerst "Seated or lying?", pas dan de sessie.
            var sc = new StartCheckView();
            WatchUi.pushView(sc, new StartCheckDelegate(sc), WatchUi.SLIDE_LEFT);
        } else if (id instanceof Number) {
            var n = id as Number;
            var rv = new RustigView(Ebb.patronen()[n], EbbStart.PATROON_NAMEN[n]);
            (Application.getApp() as EbbApp).zetRustig(rv);
            WatchUi.pushView(rv, new RustigDelegate(rv), WatchUi.SLIDE_LEFT);
        } else if (id == :eigen) {
            var ev = new RustigView(EbbInstellingen.eigenPatroon(), "My pattern");
            (Application.getApp() as EbbApp).zetRustig(ev);
            WatchUi.pushView(ev, new RustigDelegate(ev), WatchUi.SLIDE_LEFT);
        } else if (id == :dieren) {
            WatchUi.pushView(new DierenView(), new WatchUi.BehaviorDelegate(), WatchUi.SLIDE_LEFT);
        } else if (id == :instellingen) {
            WatchUi.pushView(EbbStart.instellingen(), new InstellingenDelegate(), WatchUi.SLIDE_LEFT);
        }
    }

    function onBack() as Void {
        System.exit();
    }
}

class InstellingenDelegate extends WatchUi.Menu2InputDelegate {
    function initialize() {
        Menu2InputDelegate.initialize();
    }

    function onSelect(item as WatchUi.MenuItem) as Void {
        var id = item.getId();
        if (id instanceof Number) {
            EbbInstellingen.volgende(id as Number);
            item.setSubLabel(EbbInstellingen.tekst(id as Number));
        } else if (id == :trillen) {
            EbbInstellingen.zetTrillen((item as WatchUi.ToggleMenuItem).isEnabled());
        } else if (id == :laatste3) {
            EbbInstellingen.zetLaatste3((item as WatchUi.ToggleMenuItem).isEnabled());
        } else if (id == :tik30) {
            EbbInstellingen.zetTik30((item as WatchUi.ToggleMenuItem).isEnabled());
        } else if (id == :eigen) {
            var ev = new RustigView(EbbInstellingen.eigenPatroon(), "My pattern");
            (Application.getApp() as EbbApp).zetRustig(ev);
            WatchUi.pushView(ev, new RustigDelegate(ev), WatchUi.SLIDE_LEFT);
            return;
        } else if (id == :veilig) {
            EbbVeilig.opnieuwTonen();
            item.setSubLabel("next start");
        }
        WatchUi.requestUpdate();
    }

    // Terug naar het startscherm (blad v6, eigen scherm onder de instellingen).
    function onBack() as Void {
        WatchUi.popView(WatchUi.SLIDE_RIGHT);
    }
}

// Titel van het donkere menu: "Ebb" in schuimkleur met een golflijn eronder.
class EbbMenuTitel extends WatchUi.Drawable {
    private var _tekst as String;

    function initialize(tekst as String) {
        Drawable.initialize({});
        _tekst = tekst;
    }

    function draw(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, (h * 6) / 10, Graphics.FONT_SMALL, _tekst, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }
}

// Regel van het donkere menu: wit label, zachte ondertekst; de regel met focus krijgt een turquoise streep links.
class EbbMenuItem extends WatchUi.CustomMenuItem {
    private var _label as String;
    private var _sub as String or Null;

    function initialize(id as Symbol or Number, label as String, sub as String or Null) {
        CustomMenuItem.initialize(id, {});
        _label = label;
        _sub = sub;
    }

    function draw(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var focus = isFocused();
        dc.setColor(focus ? EbbTeken.DIEPTE[3] : Graphics.COLOR_BLACK, focus ? EbbTeken.DIEPTE[3] : Graphics.COLOR_BLACK);
        dc.clear();
        var groot = focus ? Graphics.FONT_MEDIUM : Graphics.FONT_SMALL;
        var y = h / 2;
        if (_sub != null) {
            y = h / 2 - dc.getFontHeight(Graphics.FONT_XTINY) / 2;
        }
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(w / 2, y, groot, _label, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        if (_sub != null) {
            dc.setColor(EbbTeken.ZACHT, Graphics.COLOR_TRANSPARENT);
            dc.drawText(w / 2, y + dc.getFontHeight(groot) / 2, Graphics.FONT_XTINY, _sub as String, Graphics.TEXT_JUSTIFY_CENTER);
        }
        if (focus) {
            dc.setColor(EbbTeken.SCHUIM, EbbTeken.SCHUIM);
            dc.fillRectangle(w / 2 - w / 8, h - 3, w / 4, 2);
        }
    }
}

// Blad v6 scherm 1 (keuring 01:55, besluit 22:53 punt 7): eigen startscherm in plaats van een systeemmenu.
// "Ebb" bovenaan, twee gelijke pillen Rounds en Calm 4-7-8 (gekozen = dikke schuimrand), daaronder "Sea log · Settings",
// onderaan de zee met je eigen dier. Box staat er niet meer in; My pattern zit in de instellingen.
class EbbMenuView extends WatchUi.View {
    var keuze as Number = 0;   // 0 Rounds, 1 Calm 4-7-8, 2 Sea log, 3 Settings (EbbStart.MENU_AANTAL)

    function initialize() {
        View.initialize();
    }

    function onShow() as Void {
        System.println("MENU keuze " + keuze);
    }

    function pilRand(dc as Graphics.Dc, d as Number, y as Float, tekst as String, gekozen as Boolean) as Void {
        var bw = (d * 0.62).toNumber();
        var fh = dc.getFontHeight(Graphics.FONT_SMALL);
        var bh = (d * 0.15).toNumber();
        bh = bh < fh + 6 ? fh + 6 : bh;
        var lw = (d / 130 > 2 ? d / 130 : 2) * (gekozen ? 2 : 1);
        var x0 = d / 2 - bw / 2;
        var y0 = (d * y).toNumber() - bh / 2;
        dc.setColor(gekozen ? EbbTeken.SCHUIM : EbbTeken.ZEE_KLEUR[1], Graphics.COLOR_TRANSPARENT);
        dc.fillRoundedRectangle(x0, y0, bw, bh, bh / 2);
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.fillRoundedRectangle(x0 + lw, y0 + lw, bw - 2 * lw, bh - 2 * lw, (bh - 2 * lw) / 2);
        dc.setColor(Graphics.COLOR_WHITE, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * y).toNumber(), Graphics.FONT_SMALL, tekst, Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
    }

    function onUpdate(dc as Graphics.Dc) as Void {
        var w = dc.getWidth();
        var h = dc.getHeight();
        var d = (w < h) ? w : h;
        dc.setColor(Graphics.COLOR_BLACK, Graphics.COLOR_BLACK);
        dc.clear();
        EbbTeken.golf(dc, d, 0.775, d * 0.008, EbbTeken.ZEE_KLEUR[1], 0.0, true);
        EbbTeken.golf(dc, d, 0.86, d * 0.008, EbbTeken.ZEE_KLEUR[2], 1.3, false);
        EbbTeken.dierKlein(dc, d, EbbTrouw.gezelschap(), d / 2, (d * 0.875).toNumber());
        dc.setColor(EbbTeken.SCHUIM, Graphics.COLOR_TRANSPARENT);
        dc.drawText(d / 2, (d * 0.165).toNumber(), Graphics.FONT_MEDIUM, "Ebb", Graphics.TEXT_JUSTIFY_CENTER | Graphics.TEXT_JUSTIFY_VCENTER);
        pilRand(dc, d, 0.335, "Rounds", keuze == 0);
        pilRand(dc, d, 0.510, "Calm 4-7-8", keuze == 1);
        // "Sea log · Settings": het gekozen woord wit met een schuimstreep eronder, het andere lichtcyaan.
        var f = Graphics.FONT_XTINY;
        var a = "Sea log";
        var m = "  ·  ";
        var b = "Settings";
        var wa = dc.getTextWidthInPixels(a, f);
        var wm = dc.getTextWidthInPixels(m, f);
        var wb = dc.getTextWidthInPixels(b, f);
        var x0 = d / 2 - (wa + wm + wb) / 2;
        var y = (d * 0.655).toNumber();
        var fh = dc.getFontHeight(f);
        dc.setColor(keuze == 2 ? Graphics.COLOR_WHITE : EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x0, y, f, a, Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.setColor(EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x0 + wa, y, f, m, Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
        dc.setColor(keuze == 3 ? Graphics.COLOR_WHITE : EbbTeken.LICHTCYAAN, Graphics.COLOR_TRANSPARENT);
        dc.drawText(x0 + wa + wm, y, f, b, Graphics.TEXT_JUSTIFY_LEFT | Graphics.TEXT_JUSTIFY_VCENTER);
        if (keuze >= 2) {
            dc.setColor(EbbTeken.SCHUIM, EbbTeken.SCHUIM);
            var lw = d / 130 > 2 ? d / 130 : 2;
            var xs = keuze == 2 ? x0 : x0 + wa + wm;
            dc.fillRectangle(xs, y + fh / 2, keuze == 2 ? wa : wb, lw);
        }
    }
}

class EbbMenuDelegate extends WatchUi.BehaviorDelegate {
    private var _view as EbbMenuView;

    function initialize(view as EbbMenuView) {
        BehaviorDelegate.initialize();
        _view = view;
    }

    function stap(n as Number) as Boolean {
        _view.keuze = (_view.keuze + n + EbbStart.MENU_AANTAL) % EbbStart.MENU_AANTAL;
        System.println("MENU keuze " + _view.keuze);
        WatchUi.requestUpdate();
        return true;
    }

    function onNextPage() as Boolean {
        return stap(1);
    }

    function onPreviousPage() as Boolean {
        return stap(-1);
    }

    function onSwipe(evt as WatchUi.SwipeEvent) as Boolean {
        var r = evt.getDirection();
        if (r == WatchUi.SWIPE_UP) {
            return stap(1);
        } else if (r == WatchUi.SWIPE_DOWN) {
            return stap(-1);
        }
        return false;
    }

    function onTap(evt as WatchUi.ClickEvent) as Boolean {
        var xy = evt.getCoordinates();
        var d = System.getDeviceSettings().screenWidth;
        var y = xy[1].toFloat() / d;
        if (y < 0.42) {
            _view.keuze = 0;
        } else if (y < 0.59) {
            _view.keuze = 1;
        } else if (y < 0.74) {
            _view.keuze = (xy[0] < d / 2) ? 2 : 3;
        } else {
            return false;
        }
        return onSelect();
    }

    function onSelect() as Boolean {
        var k = _view.keuze;
        System.println("MENU kies " + k);
        if (k == 0) {
            // Blad v5 (S2): eerst de startcheck (en bij de eerste keer de uitleg), pas dan de sessie.
            var sc = new StartCheckView();
            WatchUi.pushView(sc, new StartCheckDelegate(sc), WatchUi.SLIDE_LEFT);
        } else if (k == 1) {
            var rv = new RustigView(Ebb.patronen()[1], EbbStart.PATROON_NAMEN[1]);
            (Application.getApp() as EbbApp).zetRustig(rv);
            WatchUi.pushView(rv, new RustigDelegate(rv), WatchUi.SLIDE_LEFT);
        } else if (k == 2) {
            WatchUi.pushView(new DierenView(), new WatchUi.BehaviorDelegate(), WatchUi.SLIDE_LEFT);
        } else {
            WatchUi.pushView(EbbStart.instellingen(), new InstellingenDelegate(), WatchUi.SLIDE_LEFT);
        }
        return true;
    }

    function onBack() as Boolean {
        System.exit();
        return true;
    }
}
