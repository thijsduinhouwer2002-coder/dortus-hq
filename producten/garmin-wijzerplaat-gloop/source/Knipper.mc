import Toybox.Lang;
import Toybox.Timer;
import Toybox.WatchUi;

// Knipperen (Mila, 16 nov 12:10 UTC): alleen als het horloge wakker is (pols opgetild). Kort na het
// optillen en daarna om de paar seconden gaat het oog 150 ms dicht. In de slaapstand loopt er geen klok.
// In de bouwstraat (Bouw.AUTO) loopt de klok niet: daar bepaalt de stand of het oog dicht is,
// zodat het knipperbeeld op een vast plaatje staat.
class Knipper {
    var klok as Timer.Timer?;
    var dicht as Boolean = false;
    var aan as Boolean = false;
    const EERST = 700;
    const DICHT = 150;
    const PAUZE = 3800;

    function initialize() {
    }

    function start() as Void {
        if (Bouw.AUTO) {
            return;
        }
        var k = klok;
        if (k == null) {
            k = new Timer.Timer();
            klok = k;
        }
        k.stop();
        dicht = false;
        aan = true;
        k.start(method(:sluit), EERST, false);
    }

    function stop() as Void {
        var k = klok;
        if (k != null) {
            k.stop();
        }
        aan = false;
        dicht = false;
    }

    function sluit() as Void {
        var k = klok;
        if (k == null || !aan) {
            return;
        }
        dicht = true;
        WatchUi.requestUpdate();
        k.start(method(:opent), DICHT, false);
    }

    function opent() as Void {
        var k = klok;
        dicht = false;
        if (k == null || !aan) {
            return;
        }
        WatchUi.requestUpdate();
        k.start(method(:sluit), PAUZE, false);
    }
}
