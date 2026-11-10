import Toybox.Application;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Startmenu (ontwerp, bediening): rondes beginnen of de instellingen openen.
// Rustig ademen komt hier bij zodra het eigen scherm er is.
module EbbStart {
    function menu() as WatchUi.Menu2 {
        var m = new WatchUi.Menu2({:title => "Ebb"});
        m.addItem(new WatchUi.MenuItem("Rounds", rondesTekst(), :rondes, null));
        m.addItem(new WatchUi.MenuItem("Settings", null, :instellingen, null));
        return m;
    }

    function rondesTekst() as String {
        return EbbInstellingen.waarde(EbbInstellingen.RONDES) + " x " + EbbInstellingen.waarde(EbbInstellingen.ADEMHALINGEN) + " breaths";
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
