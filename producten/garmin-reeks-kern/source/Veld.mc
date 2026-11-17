import Toybox.Activity;
import Toybox.ActivityMonitor;
import Toybox.Lang;
import Toybox.Math;
import Toybox.System;
import Toybox.Weather;

// De velden onder de tijd. Elke waarde is een getal of null; bij null tekent de wijzerplaat een streepje.
module Veld {
    const HART = 0;
    const STRESS = 1;
    const STAPPEN = 2;
    // Run 133: de zes soorten die erbij komen (deel 3 van ontwerp.md). De betaalde versie kiest er drie uit negen.
    const CALORIE = 3;
    const TRAPPEN = 4;
    const MINUTEN = 5;
    const AFSTAND = 6;
    const ACCU = 7;
    const TEMP = 8;
    const AANTAL = 9;

    // Een soort buiten de lijst wordt de standaard van dat veld.
    function geldig(soort as Number, standaard as Number) as Number {
        if (soort < 0 || soort >= AANTAL) {
            return standaard;
        }
        return soort;
    }

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

    // Afstand van vandaag in tienden van een kilometer of mijl. Het horloge geeft centimeters. Afkappen, niet
    // afronden: nooit meer tonen dan er gelopen is. null of negatief: null.
    function afstandTienden(cm as Number?, mijl as Boolean) as Number? {
        if (cm == null || cm < 0) {
            return null;
        }
        if (mijl) {
            // 1 mijl is 160.934 cm. Als lang getal rekenen: centimeters keer tien past anders niet altijd.
            return (cm.toLong() * 10 / 160934).toNumber();
        }
        return cm / 10000;
    }

    // Tienden als tekst: tot 99.9 met één cijfer achter de punt, daarboven hele kilometers of mijlen, hooguit 999.
    function afstandTekst(tienden as Number?) as String? {
        if (tienden == null || tienden < 0) {
            return null;
        }
        if (tienden < 1000) {
            return (tienden / 10).format("%d") + "." + (tienden % 10).format("%d");
        }
        if (tienden < 10000) {
            return (tienden / 10).format("%d");
        }
        return "999";
    }

    // Graden voor de drager: Celsius zoals het weer hem geeft, of Fahrenheit, afgerond op hele graden. Het horloge
    // mag ook een kommagetal geven (punt van de keurder, run 133).
    function graden(celsius as Numeric?, fahrenheit as Boolean) as Number? {
        if (celsius == null) {
            return null;
        }
        var c = celsius.toFloat();
        if (fahrenheit) {
            c = c * 9.0 / 5.0 + 32.0;
        }
        return Math.round(c).toNumber();
    }

    // Accu in hele procenten, naar beneden: het horloge belooft nooit meer dan er in zit. Buiten 0 tot 100: null.
    function accu(procent as Float?) as Number? {
        if (procent == null || procent < 0.0 || procent > 100.0) {
            return null;
        }
        return Math.floor(procent).toNumber();
    }

    // Leest een van de zes nieuwe soorten van het horloge. Bestaat het gegeven niet op dit horloge (geen
    // hoogtemeter, geen weer van de telefoon) of geeft het een fout: null, de plaat tekent dan een streepje.
    function lees(soort as Number) as Number? {
        try {
            if (soort == ACCU) {
                return accu(System.getSystemStats().battery);
            }
            if (soort == TEMP) {
                if (!(Toybox has :Weather) || !(Weather has :getCurrentConditions)) {
                    return null;
                }
                var nu = Weather.getCurrentConditions();
                if (nu == null) {
                    return null;
                }
                return graden(nu.temperature, System.getDeviceSettings().temperatureUnits == System.UNIT_STATUTE);
            }
            var info = ActivityMonitor.getInfo();
            if (soort == CALORIE) {
                return info.calories;
            }
            if (soort == TRAPPEN) {
                return (info has :floorsClimbed) ? info.floorsClimbed : null;
            }
            if (soort == MINUTEN) {
                if (!(info has :activeMinutesWeek)) {
                    return null;
                }
                var m = info.activeMinutesWeek;
                if (m == null) {
                    return null;
                }
                return m.total;
            }
            if (soort == AFSTAND) {
                return afstandTienden(info.distance, System.getDeviceSettings().distanceUnits == System.UNIT_STATUTE);
            }
        } catch (e instanceof Lang.Exception) {
            return null;
        }
        return null;
    }

    // De tekst van een veld. Afstand heeft een eigen vorm (tienden); temperatuur toont het getal zonder teken,
    // het minteken tekent de plaat zelf (de letter Veld heeft alleen cijfers, punt en K), zie isMin.
    function tekstVan(soort as Number, v as Number?) as String? {
        if (soort == AFSTAND) {
            return afstandTekst(v);
        }
        if (soort == TEMP && v != null && v < 0) {
            return tekst(-v);
        }
        return tekst(v);
    }

    // Alleen een temperatuur onder nul krijgt een minteken.
    function isMin(soort as Number, v as Number?) as Boolean {
        return soort == TEMP && v != null && v < 0;
    }

    // Maten van het minteken bij een temperatuur onder nul (Mila, 17 nov): lengte 40% van de cijferhoogte, dikte
    // gelijk aan de veldstreep maar minstens 2 px (op 208 px valt 1 px weg), gat tot het getal 10% van de
    // cijferhoogte en minstens 1 px. Geeft [lengte, dikte, gat].
    function minMaten(cijferPx as Number, streepDik as Number) as Array<Number> {
        var lengte = cijferPx * 40 / 100;
        if (lengte < 3) {
            lengte = 3;
        }
        var gat = cijferPx / 10;
        if (gat < 1) {
            gat = 1;
        }
        return [lengte, (streepDik < 2) ? 2 : streepDik, gat] as Array<Number>;
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
        if (soort >= CALORIE && soort < AANTAL) {
            return lees(soort);
        }
        return null;
    }
}
