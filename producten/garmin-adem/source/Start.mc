import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Startmenu (ontwerp, bediening): rondes beginnen of de instellingen openen.
module EbbStart {
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
        m.addItem(new WatchUi.ToggleMenuItem("Buzz in hold", "every 30 s", :tik30, EbbInstellingen.tik30(), null));
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
            WatchUi.pushView(new StartCheckView(), new StartCheckDelegate(), WatchUi.SLIDE_LEFT);
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
        } else if (id == :tik30) {
            EbbInstellingen.zetTik30((item as WatchUi.ToggleMenuItem).isEnabled());
        } else if (id == :veilig) {
            EbbVeilig.opnieuwTonen();
            item.setSubLabel("next start");
        }
        WatchUi.requestUpdate();
    }

    // Terug naar het startmenu, met de nieuwe rondes in de tekst.
    function onBack() as Void {
        WatchUi.popView(WatchUi.SLIDE_RIGHT);
        WatchUi.switchToView(EbbStart.menu(), new StartDelegate(), WatchUi.SLIDE_IMMEDIATE);
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
