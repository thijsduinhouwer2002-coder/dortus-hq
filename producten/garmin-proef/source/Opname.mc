import Toybox.Activity;
import Toybox.ActivityRecording;
import Toybox.FitContributor;
import Toybox.Lang;
import Toybox.System;
import Toybox.Timer;

// Proefrun (Gijs, 10 nov 2026): neemt een korte sessie op met bekende waarden, zodat de workflow
// kan laten zien waar de simulator het FIT-bestand neerzet en of fitdecode het leest.
// Verwacht: sport 10 (training), subsport 62 (ademhaling), 2 laps, lapveld "inhoud" 42 en 57, sessieveld "beste" 57.
class Opname {
    private var _sessie as ActivityRecording.Session or Null = null;
    private var _inhoud as FitContributor.Field or Null = null;
    private var _beste as FitContributor.Field or Null = null;
    private var _timer as Timer.Timer = new Timer.Timer();
    private var _stap as Number = 0;

    function initialize() {
    }

    function start() as Void {
        if (_sessie != null) {
            return;
        }
        var s = ActivityRecording.createSession({
            :sport => Activity.SPORT_TRAINING,
            :subSport => 62 as Activity.SubSport,
            :name => "Proef adem"
        });
        _inhoud = s.createField("inhoud", 0, FitContributor.DATA_TYPE_UINT16, {:mesgType => FitContributor.MESG_TYPE_LAP, :units => "s"});
        _beste = s.createField("beste", 1, FitContributor.DATA_TYPE_UINT16, {:mesgType => FitContributor.MESG_TYPE_SESSION, :units => "s"});
        s.start();
        _sessie = s;
        System.println("OPNAME start");
        _timer.start(method(:volgende), 2500, true);
    }

    function volgende() as Void {
        var s = _sessie;
        if (s == null) {
            _timer.stop();
            return;
        }
        _stap += 1;
        if (_stap == 1) {
            (_inhoud as FitContributor.Field).setData(42);
            s.addLap();
            System.println("OPNAME lap 1");
        } else if (_stap == 2) {
            (_inhoud as FitContributor.Field).setData(57);
            (_beste as FitContributor.Field).setData(57);
        } else {
            _timer.stop();
            s.stop();
            var ok = s.save();
            System.println("OPNAME opgeslagen " + ok);
            _sessie = null;
        }
    }
}
