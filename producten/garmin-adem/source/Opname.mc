import Toybox.Activity;
import Toybox.ActivityRecording;
import Toybox.FitContributor;
import Toybox.Lang;
import Toybox.Sensor;

// Eis 10: elke sessie wordt een activiteit (training, subsport ademhaling 62), één lap per ronde,
// eigen veld "inhoud" (s) op de lap en "tijden" (tekst) op de sessie. Label en eenheid in resources/fitcontributions.
class EbbOpname {
    private var _sessie as ActivityRecording.Session or Null = null;
    private var _inhoud as FitContributor.Field or Null = null;
    private var _tijden as FitContributor.Field or Null = null;   // blad v5.4: "Hold times 1:20 · 1:45 · 3:04", geen "Longest hold"
    private var _tekst as String = "";
    private var _adem as FitContributor.Field or Null = null;     // blad v5 P2: "Breaths" per lap
    private var _rondes as FitContributor.Field or Null = null;   // blad v5 P2: "Rounds" in de samenvatting
    var laps as Number = 0;

    function initialize() {
    }

    // Live hartslag (slagen per minuut) voor het inhoudscherm, of 0 als er geen meting is.
    // De opname zelf legt de polshartslag vast in het FIT-bestand (records), zoals bij elke Garmin-activiteit.
    static function hartslag() as Number {
        var info = Activity.getActivityInfo();
        if (info != null && info.currentHeartRate != null) {
            return info.currentHeartRate as Number;
        }
        return 0;
    }

    // "1:20 · 1:45" plus een nieuwe tijd; past het niet meer in 47 tekens, dan blijft de tekst zoals hij was.
    static function tijdenTekst(oud as String, s as Number) as String {
        var t = (s / 60).toString() + ":" + (s % 60).format("%02d");
        var nieuw = oud.length() == 0 ? t : oud + " · " + t;
        return nieuw.toUtf8Array().size() <= 47 ? nieuw : oud;
    }

    function loopt() as Boolean {
        return _sessie != null;
    }

    function start() as Void {
        if (_sessie != null || !(Toybox has :ActivityRecording)) {
            return;
        }
        // Hartslag (besluit 22:53): polssensor aan, zodat de opname hartslag in de records zet en het
        // inhoudscherm de live hartslag krijgt. In de simulator komt er geen hartslag (run 42912105886: 0 records met hartslag).
        if (Sensor has :setEnabledSensors) {
            Sensor.setEnabledSensors([Sensor.SENSOR_HEARTRATE] as Array<Sensor.SensorType>);
        }
        var s = ActivityRecording.createSession({
            :sport => Activity.SPORT_TRAINING,
            :subSport => Activity.SUB_SPORT_BREATHING,
            :name => "Ebb"
        });
        _inhoud = s.createField("inhoud", 0, FitContributor.DATA_TYPE_UINT16, {:mesgType => FitContributor.MESG_TYPE_LAP, :units => "s"});
        _tijden = s.createField("tijden", 4, FitContributor.DATA_TYPE_STRING, {:mesgType => FitContributor.MESG_TYPE_SESSION, :count => 48});
        _adem = s.createField("adem", 2, FitContributor.DATA_TYPE_UINT8, {:mesgType => FitContributor.MESG_TYPE_LAP});
        _rondes = s.createField("rondes", 3, FitContributor.DATA_TYPE_UINT8, {:mesgType => FitContributor.MESG_TYPE_SESSION});
        s.start();
        _sessie = s;
        laps = 0;
        _tekst = "";
    }

    // Na het inhouden: inhoudtijd en ademhalingen op de lap van deze ronde, alle tijden en het aantal rondes op de sessie.
    function inhouden(inhoudS as Number, adem as Number) as Void {
        if (_sessie == null) {
            return;
        }
        var s = (inhoudS > 65535) ? 65535 : inhoudS;
        (_inhoud as FitContributor.Field).setData(s);
        (_adem as FitContributor.Field).setData(adem > 255 ? 255 : adem);
        (_rondes as FitContributor.Field).setData(laps + 1);
        _tekst = EbbOpname.tijdenTekst(_tekst, s);
        (_tijden as FitContributor.Field).setData(_tekst);
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
