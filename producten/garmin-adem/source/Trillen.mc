import Toybox.Attention;
import Toybox.Lang;

// Eis 6: elke fase een eigen trilpatroon, zodat het met je ogen dicht werkt. Trillen is uit te zetten.
// Een patroon is een lijst van [sterkte 0-100, duur ms]; sterkte 0 is een pauze.
module EbbTrillen {
    enum Moment {
        M_IN = 0,          // begin inademen: één korte tik
        M_UIT = 1,         // begin uitademen: één lange zachte
        M_INHOUDEN = 2,    // begin inhouden: twee korte
        M_HERSTEL = 3,     // begin herstel (volle teug): drie korte
        M_LOS = 4,         // einde herstel, laat los: lang en sterk
        M_VAST = 5,        // rustig ademen, vasthouden: twee zachte
        M_KLAAR = 6        // sessie klaar: kort, pauze, lang
    }

    var aan as Boolean = true;

    function patroon(m as Moment) as Array<Array<Number> > {
        switch (m) {
            case M_IN: return [[60, 80]] as Array<Array<Number> >;
            case M_UIT: return [[30, 300]] as Array<Array<Number> >;
            case M_INHOUDEN: return [[80, 100], [0, 120], [80, 100]] as Array<Array<Number> >;
            case M_HERSTEL: return [[80, 80], [0, 100], [80, 80], [0, 100], [80, 80]] as Array<Array<Number> >;
            case M_LOS: return [[100, 600]] as Array<Array<Number> >;
            case M_VAST: return [[30, 120], [0, 150], [30, 120]] as Array<Array<Number> >;
            default: return [[80, 100], [0, 200], [80, 500]] as Array<Array<Number> >;
        }
    }

    // Geeft true als er getrild is (voor de toets); doet niets als trillen uit staat of het horloge niet kan trillen.
    function tril(m as Moment) as Boolean {
        if (!aan || !(Attention has :vibrate)) {
            return false;
        }
        var p = patroon(m);
        var reeks = [] as Array<Attention.VibeProfile>;
        for (var i = 0; i < p.size(); i += 1) {
            reeks.add(new Attention.VibeProfile(p[i][0], p[i][1]));
        }
        Attention.vibrate(reeks);
        return true;
    }

    function sleutel(m as Moment) as String {
        return patroon(m).toString();
    }
}
