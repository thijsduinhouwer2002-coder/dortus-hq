import Toybox.Lang;
import Toybox.SensorHistory;
import Toybox.System;
import Toybox.Time;
import Toybox.Weather;

// Leest wat het horloge geeft en schrijft per soort een regel "KERN ..." in het log.
module Lees {
    const UREN = 4;

    // soort 0 = Body Battery, 1 = stress. Geeft de waarden van de laatste UREN uur, oudste eerst.
    function hist(soort) {
        var w = [] as Array<Number>;
        var naam = (soort == 0) ? "BB" : "STRESS";
        if (!(Toybox has :SensorHistory)) {
            System.println("KERN " + naam + " module nee");
            return w;
        }
        var it = null;
        try {
            var opt = { :period => new Time.Duration(UREN * 3600), :order => SensorHistory.ORDER_OLDEST_FIRST };
            if (soort == 0) {
                if (SensorHistory has :getBodyBatteryHistory) {
                    it = SensorHistory.getBodyBatteryHistory(opt);
                }
            } else {
                if (SensorHistory has :getStressHistory) {
                    it = SensorHistory.getStressHistory(opt);
                }
            }
        } catch (e) {
            System.println("KERN " + naam + " fout " + e.getErrorMessage());
            return w;
        }
        if (it == null) {
            System.println("KERN " + naam + " has nee");
            return w;
        }
        var eerste = 0;
        var laatste = 0;
        var leeg = 0;
        var n = 0;
        var s = it.next();
        while (s != null && n < 600) {
            n++;
            var d = s.data;
            if (d != null) {
                var t = s.when.value();
                if (w.size() == 0) {
                    eerste = t;
                }
                laatste = t;
                w.add(d.toNumber());
            } else {
                leeg++;
            }
            s = it.next();
        }
        System.println("KERN " + naam + " has ja, waarden=" + w.size() + " leeg=" + leeg
            + " span_s=" + (laatste - eerste) + " min=" + it.getMin() + " max=" + it.getMax());
        return w;
    }

    // Aantal uren weersverwachting: -1 geen module, 0 geen gegevens, -3 fout.
    function weerUren() {
        if (!(Toybox has :Weather)) {
            return -1;
        }
        try {
            var f = Weather.getHourlyForecast();
            if (f == null) {
                return 0;
            }
            return f.size();
        } catch (e) {
            return -3;
        }
    }
}
