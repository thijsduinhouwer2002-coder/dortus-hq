import Toybox.Application;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Startmenu (ontwerp, bediening): rondes beginnen of de instellingen openen.
module EbbStart {
    function menu() as WatchUi.Menu2 {
        var m = new WatchUi.Menu2({:title => "Ebb"});
        m.addItem(new WatchUi.MenuItem("Rounds", rondesTekst(), :rondes, null));
        var namen = PATROON_NAMEN;
        for (var i = 0; i < namen.size(); i += 1) {
            m.addItem(new WatchUi.MenuItem(namen[i], PATROON_TEKST[i], i, null));
        }
        m.addItem(new WatchUi.MenuItem("My pattern", eigenTekst(), :eigen, null));
        m.addItem(new WatchUi.MenuItem("Settings", null, :instellingen, null));
        return m;
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

    const NAMEN = ["Breaths per round", "Pace", "Rounds", "Recovery hold", "My pattern: in", "My pattern: hold", "My pattern: out", "My pattern: rest"] as Array<String>;

    function instellingen() as WatchUi.Menu2 {
        var m = new WatchUi.Menu2({:title => "Settings"});
        for (var i = 0; i < NAMEN.size(); i += 1) {
            m.addItem(new WatchUi.MenuItem(NAMEN[i], EbbInstellingen.tekst(i), i, null));
        }
        m.addItem(new WatchUi.ToggleMenuItem("Vibration", null, :trillen, EbbInstellingen.trillen(), null));
        m.addItem(new WatchUi.MenuItem("Show safety note", null, :veilig, null));
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
            var view = new EbbView();
            (Application.getApp() as EbbApp).zetView(view);
            WatchUi.pushView(view, new EbbDelegate(view), WatchUi.SLIDE_LEFT);
        } else if (id instanceof Number) {
            var n = id as Number;
            var rv = new RustigView(Ebb.patronen()[n], EbbStart.PATROON_NAMEN[n]);
            WatchUi.pushView(rv, new RustigDelegate(rv), WatchUi.SLIDE_LEFT);
        } else if (id == :eigen) {
            var ev = new RustigView(EbbInstellingen.eigenPatroon(), "My pattern");
            WatchUi.pushView(ev, new RustigDelegate(ev), WatchUi.SLIDE_LEFT);
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
