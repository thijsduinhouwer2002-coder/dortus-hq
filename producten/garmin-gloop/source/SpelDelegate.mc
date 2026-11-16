import Toybox.Lang;
import Toybox.WatchUi;

// Eén knop: START (of een tik op het scherm) is de enige bediening.
class SpelDelegate extends WatchUi.BehaviorDelegate {
    var spel as Spel;

    function initialize(hetSpel as Spel) {
        BehaviorDelegate.initialize();
        spel = hetSpel;
    }

    function onSelect() as Boolean {
        spel.druk();
        WatchUi.requestUpdate();
        return true;
    }
}
