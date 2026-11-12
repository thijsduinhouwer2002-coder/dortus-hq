import Toybox.Application;
import Toybox.Graphics;
import Toybox.Lang;
import Toybox.System;
import Toybox.WatchUi;

// Bij het thuiswater (Thuis.mc): de tekstvakken van de sea log (SeaLog.mc zit tegen de 300 regels) en de acht
// proefscènes van de plaatjesbouw. Startscherm en pauzemenu geven hun vakken zelf mee.
module EbbThuisSchermen {
    // Sea log (blad v9): kop 28, telling 58, het blad met de dieren en het belletje, naam 184, regel 210, stippen 236.
    // Het zand begint 6/260 onder de bladstippen. Geeft door wat EbbThuis.teken zegt (false: nog een beurt).
    function seaLog(dc as Graphics.Dc, d as Number, v as DierenView) as Boolean {
        var fs = dc.getFontHeight(EbbTeken.fS());
        var fx = dc.getFontHeight(EbbTeken.fX());
        var c = d / 2;
        var naam = (EbbTrouw.bonus(v.keuze) && !EbbTrouw.heeft(v.keuze)) ? "Bonus" : EbbDierData.NAMEN[v.keuze];
        var nb = dc.getTextWidthInPixels(naam, EbbTeken.fS()) / 2;
        var rb = dc.getTextWidthInPixels(v.regel(v.keuze), EbbTeken.fX()) / 2;
        var vakken = [
            c - d / 5, EbbTeken.px(d, 28), c + d / 5, EbbTeken.px(d, 58) + fx,
            EbbTeken.px(d, 28), EbbTeken.px(d, 74), d - EbbTeken.px(d, 28), EbbTeken.px(d, 180),
            c - nb, EbbTeken.px(d, 184), c + nb, EbbTeken.px(d, 184) + fs,
            c - rb, EbbTeken.px(d, 210), c + rb, EbbTeken.px(d, 210) + fx,
            c - EbbTeken.px(d, 24), EbbTeken.px(d, 232), c + EbbTeken.px(d, 24), EbbTeken.px(d, 240)
        ] as Array<Number>;
        return EbbThuis.teken(dc, d, EbbTeken.px(d, 240) + EbbTeken.px(d, 6) + 3, vakken, EbbThuis.SEALOG);
    }

    // De laatste acht scènes van de plaatjesbouw: menu, pauze en sea log bij dag en nacht, dan het menu zonder dier
    // (dag) en het zwaarste blad van de sea log met alle dieren (nacht). Geeft null voor elke andere scène.
    function scene(k as Number) as [WatchUi.Views, WatchUi.InputDelegates] or Null {
        var eerste = EbbBouw.SCENES - 8;
        if (k < eerste || eerste < 53) {
            return null;
        }
        var s = k - eerste;
        EbbThuis.proefNacht = (s == 6) ? 0 : ((s == 7) ? 1 : s % 2);
        if (s < 2 || s == 6) {
            Application.Storage.setValue(EbbTrouw.BITS, s == 6 ? 0 : 31);
            if (s < 2) {
                Application.Storage.setValue(EbbTrouw.GEKOZEN, 4);
            }
            var mv = new EbbMenuView();
            return [mv, new EbbMenuDelegate(mv)];
        }
        if (s < 4) {
            Application.Storage.setValue(EbbTrouw.BITS, 31);
            Application.Storage.setValue(EbbTrouw.GEKOZEN, 4);
            return [new PauzeView("round 2 · 1:12", EbbTrouw.zwemmer()), new WatchUi.BehaviorDelegate()];
        }
        Application.Storage.setValue(EbbTrouw.BITS, s == 7 ? (1 << 25) - 1 : 255);
        var dv = new DierenView();
        dv.keuze = (s == 7) ? 18 : 8;
        return [dv, new DierenDelegate(dv)];
    }
}
