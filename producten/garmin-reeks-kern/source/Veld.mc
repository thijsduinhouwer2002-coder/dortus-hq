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
        if (info != null) {
            var nu = geldigeHart(info.currentHeartRate);
            if (nu != null) {
                return nu;
            }
        }
        // Geen actuele hartslag (de wijzerplaat krijgt hem niet altijd): de nieuwste geldige van de laatste
        // vijf metingen uit de geschiedenis. De nieuwste meting is soms leeg (horloge net omgedaan).
        if (ActivityMonitor has :getHeartRateHistory) {
            var it = ActivityMonitor.getHeartRateHistory(5, true);
            var lijst = [] as Array<Number?>;
            var s = it.next();
            while (s != null && lijst.size() < 5) {
                lijst.add(s.heartRate);
                s = it.next();
            }
            return eersteGeldigeHart(lijst);
        }
        return null;
    }

    // Eerste geldige hartslag uit een lijst (nieuwste eerst), of null als er geen geldige in staat.
    function eersteGeldigeHart(lijst as Array<Number?>) as Number? {
        for (var i = 0; i < lijst.size(); i++) {
            var v = geldigeHart(lijst[i]);
            if (v != null) {
                return v;
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

    // Laatste waarde uit een geschiedenis (oudste eerst), of null bij een lege lijst. Voor stress en Body Battery.
    function laatste(lijst as Array<Number>) as Number? {
        if (lijst.size() == 0) {
            return null;
        }
        return lijst[lijst.size() - 1];
    }

    function stress(st as Array<Number>) as Number? {
        return laatste(st);
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
