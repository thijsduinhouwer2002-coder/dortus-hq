import Toybox.Attention;
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
        var hadden = spel.hoeden;
        spel.druk();
        // Korte tik bij een vangst, iets steviger bij een voltreffer. Alleen als het horloge kan trillen.
        if (spel.hoeden > hadden && (Attention has :vibrate)) {
            Attention.vibrate([new Attention.VibeProfile(spel.raak ? 100 : 50, spel.raak ? 60 : 30)] as Array<Attention.VibeProfile>);
        }
        WatchUi.requestUpdate();
        return true;
    }
}
