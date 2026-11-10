import Toybox.Application;
import Toybox.Lang;

// Instellingen op het horloge (ontwerp, bediening): onthouden in de opslag, altijd binnen de grenzen.
// Elke instelling heeft [sleutel, kleinste, grootste, stap, standaard]. Kiezen in het menu zet hem een stap
// verder; na de grootste begint hij weer bij de kleinste.
module EbbInstellingen {
    const ADEMHALINGEN = 0;   // per ronde, 20 tot 60
    const TEMPO = 1;          // ms per in of uit, 1200 tot 2400
    const RONDES = 2;         // 1 tot 6
    const HERSTEL = 3;        // s, 10 tot 30
    const EIGEN_IN = 4;       // eigen patroon, s per fase; vast mag 0
    const EIGEN_VAST = 5;
    const EIGEN_UIT = 6;
    const EIGEN_LEEG = 7;

    const LIJST = [
        ["ademhalingen", 20, 60, 5, 30],
        ["tempo", 1200, 2400, 200, 1600],
        ["rondes", 1, 6, 1, 3],
        ["herstel", 10, 30, 5, 15],
        ["eigenIn", 1, 12, 1, 4],
        ["eigenVast", 0, 12, 1, 4],
        ["eigenUit", 1, 12, 1, 6],
        ["eigenLeeg", 0, 12, 1, 2]
    ] as Array<Array>;

    const TRILLEN = "trillen";
    const TIK30 = "tik30";

    // Waarde uit de opslag; onbekend of buiten de grenzen geeft de standaard.
    function waarde(i as Number) as Number {
        var r = LIJST[i];
        var v = Application.Storage.getValue(r[0] as String);
        if (v instanceof Number && (v as Number) >= (r[1] as Number) && (v as Number) <= (r[2] as Number)) {
            return v as Number;
        }
        return r[4] as Number;
    }

    // Zet een stap verder (rond na de grootste) en bewaart; geeft de nieuwe waarde.
    function volgende(i as Number) as Number {
        var r = LIJST[i];
        var v = waarde(i) + (r[3] as Number);
        if (v > (r[2] as Number)) {
            v = r[1] as Number;
        }
        Application.Storage.setValue(r[0] as String, v);
        return v;
    }

    function wis() as Void {
        for (var i = 0; i < LIJST.size(); i += 1) {
            Application.Storage.deleteValue(LIJST[i][0] as String);
        }
        Application.Storage.deleteValue(TRILLEN);
        Application.Storage.deleteValue(TIK30);
    }

    // Tijdens inhouden elke 30 s een zachte tik; standaard aan (je weet de tijd met je ogen dicht).
    function tik30() as Boolean {
        var v = Application.Storage.getValue(TIK30);
        return !((v instanceof Boolean) && !(v as Boolean));
    }

    function zetTik30(aan as Boolean) as Void {
        Application.Storage.setValue(TIK30, aan);
    }

    function trillen() as Boolean {
        var v = Application.Storage.getValue(TRILLEN);
        return !((v instanceof Boolean) && !(v as Boolean));
    }

    function zetTrillen(aan as Boolean) as Void {
        Application.Storage.setValue(TRILLEN, aan);
        EbbTrillen.aan = aan;
    }

    // Het eigen patroon in ms, voor Ebb.Rustig.
    function eigenPatroon() as Array<Number> {
        return [waarde(EIGEN_IN) * 1000, waarde(EIGEN_VAST) * 1000, waarde(EIGEN_UIT) * 1000, waarde(EIGEN_LEEG) * 1000] as Array<Number>;
    }

    // Een nieuwe rondesessie met de bewaarde instellingen.
    function rondes(startMs as Number) as Ebb.Rondes {
        return new Ebb.Rondes(waarde(ADEMHALINGEN), waarde(TEMPO), waarde(RONDES), waarde(HERSTEL) * 1000, startMs);
    }

    // Tekst onder een menuregel, bijvoorbeeld "1.6 s" of "15 s".
    function tekst(i as Number) as String {
        var v = waarde(i);
        if (i == TEMPO) {
            return (v / 1000) + "." + ((v % 1000) / 100) + " s";
        }
        if (i == HERSTEL || i >= EIGEN_IN) {
            return v + " s";
        }
        return v.toString();
    }
}
