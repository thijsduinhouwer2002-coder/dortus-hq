import Toybox.Activity;
import Toybox.ActivityMonitor;
import Toybox.Lang;

// De velden onder de tijd. Elke waarde is een getal of null; bij null tekent de wijzerplaat een streepje.
module Veld {
    const HART = 0;
    const STRESS = 1;
    const STAPPEN = 2;

    // Getal als tekst voor een veld, hooguit vier tekens uit de letter Veld (cijfers, punt en K).
    // Afkappen, niet afronden: het horloge toont nooit meer dan er gelopen is. null of negatief: null.
    function tekst(v as Number?) as String? {
        if (v == null || v < 0) {
            return null;
        }
        if (v < 1000) {
            return v.format("%d");
        }
        if (v < 10000) {
            var honderden = v / 100;
            return (honderden / 10).format("%d") + "." + (honderden % 10).format("%d") + "K";
        }
        if (v < 1000000) {
            return (v / 1000).format("%d") + "K";
        }
        return "999K";
    }

    // Hartslag van nu, of null als het horloge er geen geeft.
    function hart() as Number? {
        var info = Activity.getActivityInfo();
        if (info != null && info.currentHeartRate != null) {
            return info.currentHeartRate;
        }
        // Geen actuele hartslag (de wijzerplaat krijgt hem niet altijd): de laatste meting uit de geschiedenis.
        if (ActivityMonitor has :getHeartRateHistory) {
            var s = ActivityMonitor.getHeartRateHistory(1, true).next();
            if (s != null) {
                return geldigeHart(s.heartRate);
            }
        }
        return null;
    }

    // Het horloge geeft 255 als er geen meting is. Alles buiten 1 tot 254 telt als geen hartslag.
    function geldigeHart(v as Number?) as Number? {
        if (v == null || v <= 0 || v >= 255) {
            return null;
        }
        return v;
    }

    // Stappen van vandaag, of null.
    function stappen() as Number? {
        var info = ActivityMonitor.getInfo();
        return info.steps;
    }

    // Laatste waarde uit de geschiedenis van stress (oudste eerst), of null bij een lege lijst.
    function stress(st as Array<Number>) as Number? {
        if (st.size() == 0) {
            return null;
        }
        return st[st.size() - 1];
    }

    function waarde(soort as Number, st as Array<Number>) as Number? {
        if (soort == HART) {
            return hart();
        }
        if (soort == STRESS) {
            return stress(st);
        }
        if (soort == STAPPEN) {
            return stappen();
        }
        return null;
    }
}
