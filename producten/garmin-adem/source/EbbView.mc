import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.Time;
import Toybox.Timer;
import Toybox.WatchUi;

class EbbView extends WatchUi.View {
    var sessie as Ebb.Rondes;
    private var _timer as Timer.Timer = new Timer.Timer();

    function initialize() {
        View.initialize();
        sessie = EbbInstellingen.rondes(System.getTimer());
    }

    var opname as EbbOpname = new EbbOpname();
    // Dieren die je deze sessie verdiende (nummers in EbbTrouw.DIEREN); het scherm "new friend" komt met blad v4.
    var nieuweDieren as Array<Number> = [] as Array<Number>;
    var opnemen as Boolean = true;
    // Alleen in de plaatjesbouw: start meteen in het inhouden op deze tijd en zet de klok stil.
    var plaatjeMs as Number = -1;
    var plaatjeFase as Ebb.Fase = Ebb.FASE_INHOUDEN;
    var plaatjeWeek as Number = 2;   // sessies deze week in de testbeelden
    // Na de sessie: today en 8 weeks (getij = true) wisselen met de knoppen.
    var getij as Boolean = false;
    // Keuring bouw 1 punt 7: eerst het eindscherm (6b met nieuw dier, 6c zonder), daarna today en 8 weeks.
    var einde as Boolean = false;
    var feest as Boolean = false;     // dit eindscherm is het feestscherm sea complete (alleen de eerste keer)
    var eindReeks as Number = 0;      // weken op rij na deze sessie
    var eindVolgend as Number = -1;   // volgende dier (nummer in EbbTrouw.DIEREN), -1 als je alles hebt
    var eindRest as Number = 0;       // wat er nog nodig is voor dat dier (0: ligt klaar voor de volgende sessie)
    private var _klaarSinds as Number = -1;
    var gezelschap as Number = EbbTrouw.zwemmer();
    private var _startTijd as Number = System.getTimer();
    private var _gestart as Boolean = false;
    private var _lapsGesloten as Number = 0;

    function onShow() as Void {
        if (!_gestart) {
            _gestart = true;
            sessie.segmentStart = System.getTimer();
            if (plaatjeMs >= 0) {
                var nu = System.getTimer();
                sessie.fase = plaatjeFase;
                sessie.segmentStart = nu - plaatjeMs;
                sessie.pauzeer(nu);
            }
            if (opnemen) {
                opname.start();
            }
        }
        _timer.start(method(:tik), 100, true);
    }

    // Stop het inhouden op tijdstip nu (uit de knophandler of de testbouw) en zet de tijd op de lap.
    function stopInhouden(nu as Number) as Boolean {
        var tijd = sessie.stopInhouden(nu);
        if (tijd < 0) {
            return false;
        }
        opname.inhouden((tijd + 500) / 1000, sessie.ademhalingen);
        return true;
    }

    // Dagnummer van de lokale datum (dagen sinds 1970).
    static function vandaag() as Number {
        return (Time.today().value() + System.getClockTime().timeZoneOffset) / 86400;
    }

    // Opslaan: activiteit bewaren en de inhoudtijden in de 56 dagen zetten.
    // Keuring bouw 1 punt 1: een sessie telt maar één keer (today, 8 weeks, dagen, dieren), ook als opslaan twee keer wordt gevraagd.
    var opgeslagen as Boolean = false;

    function opslaan() as Boolean {
        if (opgeslagen) {
            System.println("OPNAME al opgeslagen, niet dubbel");
            return false;
        }
        opgeslagen = true;
        var ok = opname.opslaan();
        System.println("OPNAME opgeslagen " + ok + " laps " + (opname.laps + 1));
        var opslag = new EbbOpslag();
        var dag = vandaag();
        for (var i = 0; i < sessie.inhoudtijden.size(); i += 1) {
            opslag.voegToe(dag, (sessie.inhoudtijden[i] + 500) / 1000);
        }
        opslag.bewaar();
        // Blad v6 today: de hele dag, per sessie de klok en de inhoudtijden.
        var secs = [] as Array<Number>;
        for (var i = 0; i < sessie.inhoudtijden.size(); i += 1) {
            secs.add((sessie.inhoudtijden[i] + 500) / 1000);
        }
        var klok = System.getClockTime();
        // Keuring bouw 3 punt 11: geen lege sessie in Today bij 0 inhouden.
        if (secs.size() > 0) {
            EbbVandaag.bewaar(dag, klok.hour * 60 + klok.min, secs);
        }
        // Trouw: tellers en nieuwe dieren pas aan het eind van de sessie (besluit 22:53, punt 1 en 4).
        var meetelt = EbbTrouw.telt(sessie.inhoudtijden.size(), 0);
        var tellers = meetelt ? EbbTrouw.naSessie(dag) : EbbTrouw.stand(dag);
        nieuweDieren = meetelt ? EbbTrouw.nieuweDieren(tellers) : [] as Array<Number>;
        eindReeks = tellers[1];
        var v = EbbTrouw.volgende(tellers);
        eindVolgend = v[0];
        eindRest = v[1];
        // Keuring bouw 6 punt 2: het feestscherm alleen de eerste keer dat alles gevonden is; daarna weer het gewone
        // eindscherm met de rondetijden (de winkeltekst belooft tijden na elke sessie).
        feest = false;
        if (eindVolgend < 0 && Application.Storage.getValue(EbbTrouw.FEEST) != true) {
            feest = true;
            Application.Storage.setValue(EbbTrouw.FEEST, true);
        }
        System.println("TROUW nieuwe dieren " + nieuweDieren);
        return ok;
    }

    // Keuring bouw 4 punt 9: opslaan uit het pauzemenu sluit de sessie af en toont het eindscherm; terug gaat dan
    // naar het menu, net als na een volledige sessie.
    function opslaanEnTonen() as Void {
        opslaan();
        sessie.pauzeVan = -1;
        sessie.fase = Ebb.FASE_KLAAR;
        _klaarSinds = System.getTimer();
        einde = true;
        WatchUi.requestUpdate();
    }

    // Pauze zet de klok en de opname stil; doorgaan gaat verder waar je was.
    function pauzeer(nu as Number) as Void {
        sessie.pauzeer(nu);
        opname.pauzeer();
    }

    function hervat(nu as Number) as Void {
        sessie.hervat(nu);
        opname.hervat();
        _vorigIn = sessie.isIn(nu);
    }

    function hervatNu() as Void {
        hervat(System.getTimer());
    }

    function weggooien() as Void {
        opname.weggooien();
        System.println("OPNAME weggegooid");
    }

    function onHide() as Void {
        _timer.stop();
        EbbSeaComplete.los();
    }

    private var _vorigeFase as Number = -1;
    private var _vorigIn as Boolean = false;
    private var _vorigInhoudMs as Number = 0;
    private var _tik30 as Boolean = EbbInstellingen.tik30();
    private var _laatste3 as Boolean = EbbInstellingen.laatste3();

    function tik() as Void {
        var nu = System.getTimer();
        if (sessie.gepauzeerd()) {
            return;
        }
        if (EbbBouw.DEMO && sessie.fase == Ebb.FASE_INHOUDEN) {
            var doel = EbbBouw.INHOUD_MS[sessie.ronde % EbbBouw.INHOUD_MS.size()];
            if (sessie.verstreken(nu) >= doel) {
                stopInhouden(sessie.segmentStart + doel);
            }
        }
        sessie.bijwerken(nu);
        // Elke afgeronde ronde die niet de laatste is sluit een lap (onUpdate kan de ronde al verder gezet hebben).
        while (_lapsGesloten < sessie.ronde && _lapsGesloten < sessie.rondes - 1) {
            opname.rondeKlaar();
            _lapsGesloten += 1;
        }
        if (sessie.fase == Ebb.FASE_KLAAR && opname.loopt()) {
            opslaan();
        }
        if (sessie.fase == Ebb.FASE_KLAAR && _klaarSinds < 0) {
            _klaarSinds = nu;
            // Alleen aanzetten: de testbeelden zetten einde zelf (scène 16 tot 18) en mogen niet overschreven worden.
            if (!EbbBouw.DEMO && !EbbBouw.PLAATJE) {
                einde = true;
            }
        }
        // Testbouw: 15 s na het today vanzelf naar 8 weeks, voor de schermafbeelding d.
        if (EbbBouw.DEMO && _klaarSinds >= 0 && !getij && nu - _klaarSinds >= 15000) {
            getij = true;
            System.println("GETIJ getoond, klaar na " + (_klaarSinds - _startTijd) + " ms");
        }
        trilBijWissel(nu);
        WatchUi.requestUpdate();
    }

    // Trilt één keer bij elke wissel van fase of van in naar uit (eis 6).
    function trilBijWissel(nu as Number) as Void {
        var fase = sessie.fase as Number;
        var isIn = (fase == Ebb.FASE_ADEMEN) && sessie.isIn(nu);
        if (fase != _vorigeFase) {
            if (fase == Ebb.FASE_ADEMEN) {
                EbbTrillen.tril(_vorigeFase == Ebb.FASE_HERSTEL ? EbbTrillen.M_LOS : EbbTrillen.M_IN);
            } else if (fase == Ebb.FASE_INHOUDEN) {
                _vorigInhoudMs = 0;
                EbbTrillen.tril(EbbTrillen.M_INHOUDEN);
            } else if (fase == Ebb.FASE_HERSTEL) {
                EbbTrillen.tril(EbbTrillen.M_HERSTEL);
            } else if (fase == Ebb.FASE_KLAAR) {
                EbbTrillen.tril(EbbTrillen.M_KLAAR);
            }
        } else if (fase == Ebb.FASE_ADEMEN && isIn != _vorigIn) {
            if (isIn && _laatste3 && sessie.laatsteDrie(nu)) {
                EbbTrillen.tril(EbbTrillen.M_LAATSTE);
            } else {
                EbbTrillen.tril(isIn ? EbbTrillen.M_IN : EbbTrillen.M_UIT);
            }
        } else if (fase == Ebb.FASE_INHOUDEN) {
            var ms = sessie.verstreken(nu);
            var sig = Ebb.inhoudSignaal(_vorigInhoudMs, ms, _tik30);
            if (sig == 2) {
                EbbTrillen.tril(EbbTrillen.M_DRIE_MIN);
            } else if (sig == 1) {
                EbbTrillen.tril(EbbTrillen.M_DERTIG);
            }
            _vorigInhoudMs = ms;
        }
        _vorigeFase = fase;
        _vorigIn = isIn;
    }

    // Keuring 01:55 punt 6: hoe je het inhouden stopt, per horloge de juiste knop (resources-venu2, -venu3, -vivoactive5).
    private var _stop as String or Null = null;
    function stopTekst() as String {
        if (_stop == null) {
            _stop = WatchUi.loadResource(Rez.Strings.StopTekst) as String;
        }
        return _stop as String;
    }

    // Tekenen staat in SessieScherm.mc (ademen, inhouden, herstel), EindScherm.mc en Overzicht.mc.
    function onUpdate(dc as Graphics.Dc) as Void {
        EbbSessieScherm.teken(self, dc);
    }
}
