import Toybox.Activity;
import Toybox.ActivityRecording;
import Toybox.FitContributor;
import Toybox.Lang;

// Eis 10: elke sessie wordt een activiteit (training, subsport ademhaling 62), één lap per ronde,
// eigen veld "inhoud" (s) op de lap en "beste" (s) op de sessie. Label en eenheid in resources/fitcontributions.
class EbbOpname {
    private var _sessie as ActivityRecording.Session or Null = null;
    private var _inhoud as FitContributor.Field or Null = null;
    private var _beste as FitContributor.Field or Null = null;
    var besteS as Number = 0;
    var laps as Number = 0;

    function initialize() {
    }

    function loopt() as Boolean {
        return _sessie != null;
    }

    function start() as Void {
        if (_sessie != null || !(Toybox has :ActivityRecording)) {
            return;
        }
        var s = ActivityRecording.createSession({
            :sport => Activity.SPORT_TRAINING,
            :subSport => Activity.SUB_SPORT_BREATHING,
            :name => "Ebb"
        });
        _inhoud = s.createField("inhoud", 0, FitContributor.DATA_TYPE_UINT16, {:mesgType => FitContributor.MESG_TYPE_LAP, :units => "s"});
        _beste = s.createField("beste", 1, FitContributor.DATA_TYPE_UINT16, {:mesgType => FitContributor.MESG_TYPE_SESSION, :units => "s"});
        s.start();
        _sessie = s;
        besteS = 0;
        laps = 0;
    }

    // Na het inhouden: de inhoudtijd komt op de lap van deze ronde, de beste op de sessie.
    function inhouden(inhoudS as Number) as Void {
        if (_sessie == null) {
            return;
        }
        var s = (inhoudS > 65535) ? 65535 : inhoudS;
        (_inhoud as FitContributor.Field).setData(s);
        if (s > besteS) {
            besteS = s;
            (_beste as FitContributor.Field).setData(s);
        }
    }

    // Einde van een ronde die niet de laatste is: lap sluiten. De laatste lap sluit bij opslaan.
    function rondeKlaar() as Void {
        if (_sessie != null) {
            (_sessie as ActivityRecording.Session).addLap();
            laps += 1;
        }
    }

    // Pauze: de opname stopt (de activiteitstijd loopt niet door) en gaat bij doorgaan verder.
    function pauzeer() as Void {
        var s = _sessie;
        if (s != null && s.isRecording()) {
            s.stop();
        }
    }

    function hervat() as Void {
        var s = _sessie;
        if (s != null && !s.isRecording()) {
            s.start();
        }
    }

    function opslaan() as Boolean {
        var s = _sessie;
        if (s == null) {
            return false;
        }
        if (s.isRecording()) {
            s.stop();
        }
        var ok = s.save();
        _sessie = null;
        return ok;
    }

    function weggooien() as Void {
        var s = _sessie;
        if (s == null) {
            return;
        }
        if (s.isRecording()) {
            s.stop();
        }
        s.discard();
        _sessie = null;
    }
}
